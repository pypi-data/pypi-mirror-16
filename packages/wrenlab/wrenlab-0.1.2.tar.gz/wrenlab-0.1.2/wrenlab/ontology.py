"""
Ontology handling (focused on Open Biomedical Ontology [OBO] format).
"""

import collections
import functools

import networkx as nx
import pandas as pd
import numpy as np

import acfsa
from wrenlab.util import memoize, download

Term = collections.namedtuple("Term", [
    "id", "name", "synonym", "relations", "namespace"
])

class Ontology(object):
    """
    Attribute specifications (DataFrame objects):
        terms: Term ID, Name, Depth, Namespace
        synonyms: Term ID, Synonym
        relations: Agent, Target, Relation
    """
    def __init__(self, terms, synonyms, relations, prefix=None):
        self._terms = terms
        self._synonyms = synonyms
        self._relations = relations

        if isinstance(prefix, str):
            self._prefix = prefix
        else:
            self._prefix = collections.Counter([t.split(":")[0] for t in self.terms.index])\
                    .most_common(1)[0][0]

    def __repr__(self):
        return "<Ontology with %s terms, %s synonyms, and %s relations>" \
                % (len(self._terms), len(self._synonyms), len(self._relations))

    @property
    def terms(self):
        return self._terms.copy()

    @property
    def synonyms(self):
        return self._synonyms.copy()

    @property
    def relations(self):
        return self._relations.copy()

    def _resolve_id(self, x):
        if isinstance(x, str):
            if x.startswith(self._prefix):
                return x
            else:
                return self._name_to_id(x)
        elif isinstance(x, int):
            return "{}:{:07d}".format(self._prefix, x)
        else:
            msg = "{} could not be resolved to a term ID in ontology {}"\
                .format(repr(x), self._prefix)
            raise ValueError(msg)

    def _name_to_id(self, name):
        ix = self.terms["Name"].str.lower() == name.lower()
        if ix.sum() == 1:
            return self.terms.ix[ix,:].index[0]
        raise KeyError

    def descendants(self, term):
        id = self._resolve_id(term)
        return nx.ancestors(self.graph, id)

    @property
    def depths(self):
        g = self.graph
        depths = nx.single_source_shortest_path_length(g.reverse(), g.root)
        o = {}
        for t in g.nodes():
            depth = depths.get(t)
            if depth is not None:
                o[t] = depth
        return pd.Series(o)

    @property
    def graph(self):
        if not hasattr(self, "_graph"):
            self._graph = self.to_graph()
        return self._graph
    
    def to_graph(self, relations=None):
        """
        Convert this Ontology into a NetworkX graph for efficient traversal.

        Parameters
        ----------
        relations : list of str or None, optional
            The relation types to use as edges in the graph. (default: is_a)

        Returns
        -------
        A :class:`networkx.DiGraph`. The edges are directed in the 
            same direction as the relation. In the common case of 
            the `is_a` relation, this means from children to parents.
        """
        g = nx.DiGraph()
        R = self.relations
        if relations is not None:
            R = R.ix[R["Relation"].isin(relations),:]

        for id,name,ns in self.terms.to_records():
            g.add_node(id, name=name, namespace=ns)
        for id,synonym in self.synonyms.to_records(index=False):
            if not "synonyms" in g.node[id]:
                g.node[id]["synonyms"] = []
            g.node[id]["synonyms"].append(synonym)
        for _,agent,target,relation in R.to_records():
            g.add_edge(agent, target, type=relation)

        g.root = sorted([n for n in g.nodes() if len(nx.descendants(g,n)) == 0],
                key=lambda n: -len(nx.ancestors(g,n)))[0]
        depths = nx.single_source_shortest_path_length(g.reverse(), g.root)
        o = {}
        for t in g.nodes():
            depth = depths.get(t)
            if depth is not None:
                g.node[t]["depth"] = depth
        return g

    def _expand_synonym(self, text):
        o = [text]
        if not text.endswith("s"):
            o.append(text+"s")
        return o

    @property
    def trie(self):
        if not hasattr(self, "_trie"):
            o = acfsa.MixedCaseSensitivityTrie(allow_overlaps=False)
            for ix,t in self.terms.loc[:,["Name"]].to_records():
                for s in self._expand_synonym(t):
                    o.add(s, key=ix, case_sensitive=(len(s) < 5))
            for ix,t in self.synonyms.loc[:,["Term ID", "Synonym"]].to_records(index=False):
                for s in self._expand_synonym(t):
                    o.add(s, key=ix, case_sensitive=(len(s) < 5))
            o.build()
            self._trie = o
        return self._trie

    def match(self, text):
        if text is None:
            return None
        trie = self.trie
        ms = trie.search(text)
        if len(ms) == 1:
            k = ms[0].key
            if isinstance(k, np.float64) and np.isnan(k):
                return
            return k

    @property
    def ancestry_table(self):
        g = self.to_graph()
        rows = []
        for n in g.nodes():
            for ancestor in nx.descendants(g, n):
                rows.append((ancestor, n))
        return pd.DataFrame(rows, 
                columns=["Ancestor", "Descendant"])

    def annotation_matrix(self, mapping, recursive=False):
        """
        Create a DataFrame representing the mapping between a set
        of ontology terms and another set of objects (genes, samples, etc.).

        Parameters
        ----------
        mapping : :class:`pandas.DataFrame`
            A DataFrame representing the mapping between ontology terms 
            and genes/samples/whatever. Two columns are required:
            Column 1 - The sample/gene ID
            Column 2 - The ontology term ID
            Column 3 (optional) - An integer, float, or boolean column. If not 
                provided, an int8 :class:`pandas.DataFrame` will be returned
                wherein all matching sample/ontology pairs will
                be assigned integer value 1 and non-matching pairs will be
                assigned 0.
        recursive : bool, optional
            If True, the ontology tree will be traversed and all parent
            terms will be assigned the same value

        Returns
        -------
        :class:`pandas.DataFrame`
            Rows are sample/gene IDs, columns are ontology IDs, and
            values are ints/floats/booleans as described above.
        """
        msg = "Provided DataFrame must have either two or three columns."
        assert mapping.shape[1] in (2,3), msg

        A = mapping
        if A.shape[1] == 2:
            A["Value"] = 1
            dtype = np.uint8
        else:
            dtype = mapping.iloc[2].dtype
            msg = "Value column must be numeric or boolean, not object."
            assert dtype is not np.object, msg

        A.columns = [A.columns[0]] + ["Term ID", "Value"]

        if recursive:
            inferred = mapping.merge(self.ancestry_table,
                    left_on=A.columns[1],
                    right_on="Descendant")\
                            .ix[:,["Ancestor", A.columns[0], "Value"]]
            inferred.columns = ["Term ID", A.columns[0], "Value"]
            A = pd.concat([A, inferred], axis=0).drop_duplicates()
        return A.pivot(A.columns[0], "Term ID", "Value")\
                .fillna(0).astype(dtype)

def _obo_make_term(attrs):
    if ("id" in attrs) and ("name" in attrs):
        for key in Term._fields:
            attrs.setdefault(key, [])
        attrs["namespace"] = attrs["namespace"] or None
        return Term(**attrs)

def _obo_parse(handle):
    """
    A simple iterative reader for OBO (Open Biomedical Ontology) files.
    
    :param handle: File handle to the OBO file
    :type handle: A file handle in 'rt' mode

    Currently, only a subset of the OBO specification is supported. 
    Namely, only the following attribute of [Term] entries:
    - id
    - name
    - relations
    - synonym
    - namespace
    """
    is_term = False
    attrs = collections.defaultdict(list)
    for line in handle:
        line = line.strip()
        if line in ("[Term]", "[Typedef]", "[Instance]"):
            is_term = line == "[Term]"
            t = _obo_make_term(attrs)
            if t and is_term: 
                yield t
            attrs = collections.defaultdict(list)
        elif line:
            try:
                key, value = line.split(": ", 1)
            except ValueError:
                continue

            if key == "id":
                attrs["id"] = value
            elif key == "name":
                attrs["name"] = value
            elif key == "is_a":
                attrs["relations"].append(("is_a", value.split("!")[0].strip()))
            elif key == "relationship":
                value = value.split("!")[0].strip()
                rel, target, *rest = value.split(" ")
                attrs["relations"].append((rel,target))
            elif key == "namespace":
                attrs["namespace"] = value
            elif key == "synonym":
                value = value[1:]
                attrs["synonym"].append(value[:value.find("\"")])
    t = _obo_make_term(attrs)
    if t and is_term: 
        yield t

def _obo_parse_as_data_frame(handle):
    terms, synonyms, relations = [], [], []

    for t in _obo_parse(handle):
        terms.append((t.id, t.name, t.namespace))
        for s in t.synonym:
            synonyms.append((t.id, s))
        synonyms.append((t.id, t.name))
        for rel, target in t.relations:
            relations.append((t.id, target, rel))

    terms = pd.DataFrame.from_records(terms,
            columns=["Term ID", "Name", "Namespace"],
            index="Term ID")
    synonyms = pd.DataFrame.from_records(synonyms,
            columns=["Term ID", "Synonym"])\
                    .drop_duplicates()
    relations = pd.DataFrame.from_records(relations,
            columns=["Agent", "Target", "Relation"])
    return terms, synonyms, relations
        
def parse(handle, format="obo"):
    assert (format=="obo"), "Only OBO format currently supported."
    return Ontology(*_obo_parse_as_data_frame(handle))

@memoize
def _fetch(abbreviation):
    """
    Fetch an OBO-format ontology from BerkeleyBOP.
    """
    url = "http://www.berkeleybop.org/ontologies/%s.obo" \
            % abbreviation.lower()
    path = download(url)
    for encoding in ["utf-8", "iso-8859-1"]:
        try:
            with open(str(path), encoding=encoding) as handle:
                return parse(handle, format="obo")
        except UnicodeDecodeError:
            continue

@functools.lru_cache()
def fetch(abbreviation):
    return _fetch(abbreviation)
