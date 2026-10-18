#!/usr/bin/env python3
"""categories.py — the subject pages of the prediction index (2026-10-17).

Lee Sharks, 2026-10-17: "id like to do individual pages, not for each prediction - thats too many - but perhaps by
category ... 100-200, maybe - but not thousands." Pages are built from the claims' own links, not from a scheme laid
over them: a graph whose edges are the triage and topical links (series co-membership, weighted down by series size;
related; contains/in), shared registration deposit (weak), and each claim's five nearest statements by TF-IDF cosine
(>= 0.25). Louvain communities (resolution R, seed 1) above MIN become pages; a page over MAX is split again by the
same method; a community under MIN joins the page whose centroid its statements are nearest; a page still over MAX
is divided by k-means (SVD-150, seed 0) into pages of about 30. Deterministic.
Writes data/index/categories.json: page id, its claims, and the evidence for naming it (top terms, the series and
deposit titles its claims carry). Names are given in names.json, written by reading each page, not by this script.
USAGE  python3 scripts/index/categories.py
"""
import json, collections, itertools, pathlib
import numpy as np, networkx as nx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'data/reading/triage'; OUT = ROOT / 'data/index'
R, MIN, MAX = 1.5, 12, 45


def main():
    C = json.load(open(T / 'claims.json'))['claims']; ids = [c['id'] for c in C]; ix = {c: i for i, c in enumerate(ids)}
    S = json.load(open(T / 'series.json'))['series']
    vec = TfidfVectorizer(sublinear_tf=True, min_df=2, max_df=0.3, stop_words='english', ngram_range=(1, 2))
    X = normalize(vec.fit_transform([c['statement'] for c in C])); terms = np.array(vec.get_feature_names_out())
    G = nx.Graph(); G.add_nodes_from(range(len(C)))

    def add(a, b, w):
        if a != b:
            G.add_edge(a, b, weight=G.get_edge_data(a, b, {'weight': 0})['weight'] + w)
    for s in S:
        m = [ix[c] for c in s['claims'] if c in ix]
        for a, b in itertools.combinations(m, 2):
            add(a, b, 2.0 / max(1, len(m) - 1))
    for c in C:
        for k in ('related', 'contains', 'in'):
            for o in c.get(k) or []:
                if o in ix:
                    add(ix[c['id']], ix[o], 1.0)
    dep = collections.defaultdict(list)
    for i, c in enumerate(C):
        dep[c['registered_in']].append(i)
    for m in dep.values():
        if len(m) <= 40:
            for a, b in itertools.combinations(m, 2):
                add(a, b, 0.3)
    Sim = (X @ X.T).tocsr()
    for i in range(len(C)):
        row = Sim.getrow(i)
        for j in row.indices[np.argsort(-row.data)][1:6]:
            if Sim[i, j] > 0.25:
                add(i, int(j), float(Sim[i, j]))

    def split(nodes, r):
        sub = G.subgraph(nodes)
        return [sorted(c) for c in nx.community.louvain_communities(sub, weight='weight', resolution=r, seed=1)]
    pages, small = [], []
    work = split(list(G.nodes), R)
    while work:
        c = work.pop()
        if len(c) > MAX:
            parts = split(c, R * 1.6)
            if len(parts) == 1:
                pages.append(c)
            else:
                work += parts
        elif len(c) >= MIN:
            pages.append(c)
        else:
            small.append(c)
    cent = normalize(np.vstack([np.asarray(X[p].mean(axis=0)) for p in pages]))
    for c in small:
        v = normalize(np.asarray(X[c].mean(axis=0)))
        k = int(np.argmax(cent @ v.T))
        pages[k] = sorted(pages[k] + c)
    # a page still over MAX (Louvain could not split it, or small communities joined it) is divided by k-means on
    # its statements, into pages of about 30
    from sklearn.cluster import KMeans
    from sklearn.decomposition import TruncatedSVD
    Z = normalize(TruncatedSVD(150, random_state=0).fit_transform(X))
    final = []
    for pg in pages:
        if len(pg) <= MAX:
            final.append(pg); continue
        k = int(np.ceil(len(pg) / 30))
        lab = KMeans(k, n_init=4, random_state=0).fit_predict(Z[pg])
        final += [[pg[j] for j in range(len(pg)) if lab[j] == q] for q in range(k) if (lab == q).any()]
    pages = final
    pages.sort(key=lambda p: min(C[i]['registered'] or '9999' for i in p))
    ser = collections.defaultdict(list)
    for s in S:
        for c in s['claims']:
            ser[c].append(s['name'])
    out = []
    for n, p in enumerate(pages):
        top = terms[np.asarray(X[p].sum(axis=0)).ravel().argsort()[::-1][:10]].tolist()
        out.append({'page': f'P{n + 1:03d}', 'claims': [ids[i] for i in sorted(p, key=lambda i: (C[i]['registered'] or '9999', ids[i]))],
                    'terms': top,
                    'series': collections.Counter(x for i in p for x in ser.get(ids[i], [])).most_common(8),
                    'titles': collections.Counter(C[i].get('title') for i in p).most_common(6),
                    'tiers': dict(collections.Counter(C[i]['tier'] for i in p))})
    OUT.mkdir(parents=True, exist_ok=True)
    json.dump({'what': 'Subject pages of the prediction index: communities of the claims\' own link graph. Built by '
                       'scripts/index/categories.py; named in names.json.', 'params': {'resolution': R, 'min': MIN, 'max': MAX},
               'pages': out}, open(OUT / 'categories.json', 'w'), ensure_ascii=False, indent=1)
    sz = sorted(len(p['claims']) for p in out)
    print(len(out), 'pages; claims per page', sz[0], '-', sz[-1], 'median', sz[len(sz) // 2])


if __name__ == '__main__':
    main()
