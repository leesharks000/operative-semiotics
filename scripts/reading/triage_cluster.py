#!/usr/bin/env python3
"""triage_cluster.py — restatements and candidate pairs of the prediction triage (2026-10-17).

The protocol (READING-PROTOCOL v1.2, shape H): "A thesis repeated across deposits is recorded in each deposit that argues
it (triage links them)." Within a deposit the reader already recorded one forecast once (boundary rule 1); across
deposits the same claim recurs — in version series, reprinted sections, and later papers that restate it.

Similarity is TF-IDF cosine (word unigrams and bigrams, sublinear tf) between the verbatim quotes of finds in DIFFERENT
deposits.
  >= AUTO (0.85)    a RESTATEMENT: near-verbatim; joined mechanically (union-find), each join recorded with its score
  LOW..AUTO         a CANDIDATE PAIR for the judgment pass (same claim / related / distinct), unless already joined
Lexical similarity does not find a claim restated in other words; that is left to the topical pass and said so.

USAGE  python3 scripts/reading/triage_cluster.py
"""
import json, pathlib, collections
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
R = pathlib.Path(__file__).resolve().parents[2] / 'data/reading'
AUTO, LOW = 0.85, 0.35


def main():
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    ids = [json.loads(l)['id'] for l in open(R / 'triage/finds.ids.jsonl')]
    X = TfidfVectorizer(sublinear_tf=True, min_df=2, stop_words='english', ngram_range=(1, 2)).fit_transform(
        [f['quote'] for f in F])
    S = (X @ X.T).tocoo()
    dep = np.array([f['deposit'] for f in F])
    m = (S.row < S.col) & (dep[S.row] != dep[S.col]) & (S.data >= LOW)
    pairs = sorted(zip(S.row[m].tolist(), S.col[m].tolist(), np.round(S.data[m], 3).tolist()), key=lambda p: -p[2])
    par = list(range(len(F)))

    def g(i):
        while par[i] != i:
            par[i] = par[par[i]]; i = par[i]
        return i
    joins = []
    for a, b, s in pairs:
        if s >= AUTO:
            joins.append([ids[a], ids[b], s]); par[g(a)] = g(b)
    comp = collections.defaultdict(list)
    for i in range(len(F)):
        comp[g(i)].append(i)
    groups = []
    for k, v in comp.items():
        if len(v) > 1:
            v.sort(key=lambda i: (F[i].get('date') or '9999', F[i]['deposit']))
            groups.append({'members': [ids[i] for i in v], 'deposits': sorted({F[i]['deposit'] for i in v}),
                           'earliest': ids[v[0]], 'earliest_date': F[v[0]].get('date')})
    cand = [{'a': ids[a], 'b': ids[b], 'score': s} for a, b, s in pairs if s < AUTO and g(a) != g(b)]
    # one candidate per pair of groups: the highest-scoring
    seen, cand1 = set(), []
    gid = {ids[i]: g(i) for i in range(len(F))}
    for c in cand:
        k = tuple(sorted((gid[c['a']], gid[c['b']])))
        if k in seen:
            continue
        seen.add(k); cand1.append(c)
    json.dump({'what': f'Restatement groups of the prediction triage: finds in different deposits whose verbatim quotes have '
                       f'TF-IDF cosine >= {AUTO}, joined mechanically. Built by scripts/reading/triage_cluster.py.',
               'auto_threshold': AUTO, 'groups': sorted(groups, key=lambda x: x['earliest']), 'joins': joins},
              open(R / 'triage/restatements.json', 'w'), ensure_ascii=False, indent=1)
    json.dump({'what': f'Candidate pairs for the judgment pass: cross-deposit finds with {LOW} <= cosine < {AUTO}, not '
                       f'already in one restatement group; one pair per pair of groups.', 'pairs': cand1},
              open(R / 'triage/candidate-pairs.json', 'w'), ensure_ascii=False, indent=1)
    print(f'restatement groups {len(groups)} covering {sum(len(x["members"]) for x in groups)} finds; joins {len(joins)}; '
          f'candidate pairs {len(cand1)}')


if __name__ == '__main__':
    main()
