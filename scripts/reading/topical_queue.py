#!/usr/bin/env python3
"""topical_queue.py — subject groups of the triage claims, for the topical pass (2026-10-17).

The triage joined statements by shared wording (TF-IDF cosine on quotes). A claim restated in other words, or revised
until its wording no longer overlaps, is not found that way (TRIAGE-PROTOCOL, "What follows"). This pass reads claims by
SUBJECT: the claims are grouped by their statements' TF-IDF (unigrams+bigrams, df <= 30%) reduced to 200 dimensions
(SVD) and clustered (k-means, k=120, seed 0); a group over 60 claims is split again the same way. Groups are packed into
batches of at most 90 claims (first-fit decreasing); each group carries its top terms so the reader sees what binds it.
A same claim split across two groups is not seen by this pass either; the topical readers record such cases.
USAGE  python3 scripts/reading/topical_queue.py
"""
import json, pathlib, collections
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.cluster import KMeans
from sklearn.preprocessing import normalize
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'data/reading/triage'
K, CAP, BATCH = 120, 60, 90


def main():
    C = json.load(open(T / 'claims.json'))['claims']
    F = {json.loads(i)['id']: json.loads(f) for i, f in zip(open(T / 'finds.ids.jsonl'), open(ROOT / 'data/reading/finds.jsonl'))}
    titles = {d['deposit']: d for d in json.load(open(T / 'deposit-titles.json'))}
    vec = TfidfVectorizer(sublinear_tf=True, min_df=2, max_df=0.3, stop_words='english', ngram_range=(1, 2))
    X = vec.fit_transform([c['statement'] for c in C]); terms = np.array(vec.get_feature_names_out())
    Z = normalize(TruncatedSVD(200, random_state=0).fit_transform(X))
    lab = KMeans(K, n_init=4, random_state=0).fit_predict(Z)
    groups = []
    for k in range(K):
        idx = np.where(lab == k)[0]
        if len(idx) > CAP:
            sub = KMeans(int(np.ceil(len(idx) / 40)), n_init=4, random_state=0).fit_predict(Z[idx])
            groups += [idx[sub == s] for s in sorted(set(sub))]
        else:
            groups.append(idx)
    out = []
    for g in groups:
        top = terms[np.asarray(X[g].sum(axis=0)).ravel().argsort()[::-1][:8]].tolist()
        out.append({'terms': top, 'claims': [C[i]['id'] for i in sorted(g, key=lambda i: (C[i]['registered'] or '', C[i]['id']))]})
    byid = {c['id']: c for c in C}

    def card(cid):
        c = byid[cid]
        return {'claim': cid, 'tier': c['tier'], 'registered': c['registered'], 'registered_in': c['registered_in'],
                'title': c.get('title'), 'path': titles.get(c['registered_in'], {}).get('path'),
                'statement': c['statement'], 'falsifier': c.get('falsifier'), 'window': c.get('window'),
                'later_statements': [{'find': s['find'], 'deposit': s['deposit'], 'date': s['date'], 'lines': s['lines'],
                                      'quote': F[s['find']]['quote'], **({'variant': s['variant']} if 'variant' in s else {})}
                                     for s in c['statements'][1:]],
                'contains': c.get('contains', []), 'in': c.get('in', []), 'related': c['related']}
    batches = []  # first-fit decreasing
    for g in sorted(out, key=lambda g: -len(g['claims'])):
        for b in batches:
            if sum(len(x['claims']) for x in b) + len(g['claims']) <= BATCH:
                b.append(g); break
        else:
            batches.append([g])
    Q = [{'batch_id': f'TP{i + 1:02d}', 'groups': [{'group': f'TP{i + 1:02d}.{j + 1}', 'terms': g['terms'],
                                                     'claims': [card(c) for c in g['claims']]} for j, g in enumerate(b)]}
         for i, b in enumerate(batches)]
    json.dump({'what': 'Subject groups of the triage claims for the topical pass. Built by scripts/reading/topical_queue.py; '
                       'protocol data/reading/TOPICAL-PROTOCOL.md.', 'counts': {'claims': len(C), 'groups': len(out), 'batches': len(Q)},
               'batches': Q}, open(T / 'topical-queue.json', 'w'), ensure_ascii=False, indent=1)
    sz = [sum(len(g['claims']) for g in b['groups']) for b in Q]
    print(len(out), 'groups;', len(Q), 'batches; claims per batch', min(sz), '-', max(sz))
    for b in Q[:2]:
        for g in b['groups'][:3]:
            print(g['group'], len(g['claims']), g['terms'])


if __name__ == '__main__':
    main()
