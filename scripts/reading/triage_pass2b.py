#!/usr/bin/env python3
"""triage_pass2b.py — the second round of the pass-2 triage: pass-2 finds against each other (2026-10-18).

The TN readers judged each pass-2 find against the claims that stood BEFORE pass 2 (claims-p2-base.json), so two pass-2
finds that state one claim could not be joined to each other: an attachment and its other edition (the HTML and PDF of
#1409, the PDF and machine text of Pearl #1121), two deposits carrying one restored body, or a promise and its later
rendering (#402's "book of Damascus" and #1277's). After the TN decisions are assembled, every pair of pass-2 finds that
still sit in different claims and whose quotes have TF-IDF cosine >= 0.40 is a candidate pair for a TE decision, as in
pass 1 (TRIAGE-PROTOCOL, "TE: a candidate pair"): batches TEP01…, appended to triage/queue.json.

It also seats the one pass-2 find whose unit named no deposit: New Human Compiled, the revised double issue, is the
compiled 2015 edition that #1204 ("new human 2: a distributed journal of voice — Charter, Compiled Edition (2015), and
Issue 1 (2026)") holds as its PDF (new-human-compiled-double-issue-revised.pdf). Its find takes #1204 and is judged in TN17.
USAGE  python3 scripts/reading/triage_pass2b.py   (after triage_assemble.py has run on the verified TN batches)
"""
import collections, json, pathlib, sys
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'; T = R / 'triage'
AX = ROOT.parent / 'alexanarch'
NH = 'A:recovered-sources/New-Human-Compiled-Double-issue-revised.md'


def main():
    Q = json.load(open(T / 'queue.json'))
    if any(b['batch_id'].startswith('TEP') for b in Q['batches']):
        sys.exit('second round already queued')
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    ids = [json.loads(l)['id'] for l in open(T / 'finds.ids.jsonl')]
    for f, i in zip(F, ids):
        f['id'] = i
    p2 = json.load(open(T / 'pass2.json'))
    reg = {int(d['deposit_number']): d for d in json.load(open(AX / 'data/registry.json'))['deposits'] if d.get('deposit_number') is not None}
    # the held New Human find takes #1204
    seat = [h for h in p2['held'] if h['unit'] == NH]
    cnt = collections.Counter((f['deposit'], f['shape']) for f in F)
    new = []
    for h in seat:
        cnt[(1204, h['shape'])] += 1
        fid = f"F1204.{h['shape']}{cnt[(1204, h['shape'])]}"
        row = {'deposit': 1204, 'deposits': [1204], 'date': reg[1204].get('date'), 'batch_id': h['batch_id'], 'run': f"R-p2-{h['batch_id']}",
               'pass': 2, 'unit': h['unit'], 'path': h['path'], 'shape': h['shape'], 'quote': h['quote'], 'lines': h['lines'],
               'verified': True, 'verification_fails': [], 'seated_by': 'triage_pass2b.py: New Human Compiled is the compiled edition #1204 holds'}
        full = next(x for b in json.load(open(R / 'pass2-queue.json'))['batches'] for x in b['units'] if x['unit'] == NH)
        out = next(json.load(open(R / f"batches/{b['batch_id']}.json")) for b in json.load(open(R / 'pass2-queue.json'))['batches']
                   if any(u['unit'] == NH for u in b['units']))
        e = next(x for x in out['deposits'] if x['unit'] == NH)
        src = next(x for x in e['finds'] if x['quote'] == h['quote'])
        row.update({k: src.get(k) for k in ('falsifier_quote', 'falsifier_lines', 'window', 'points_to', 'also_at', 'note')})
        new.append((fid, row))
    with open(R / 'finds.jsonl', 'a') as o:
        for fid, row in new:
            o.write(json.dumps(row, ensure_ascii=False) + '\n')
    with open(T / 'finds.ids.jsonl', 'a') as o:
        for fid, row in new:
            o.write(json.dumps({'id': fid, 'deposit': 1204, 'shape': row['shape'], 'lines': row['lines']}) + '\n')
    p2['held'] = [h for h in p2['held'] if h['unit'] != NH]
    p2['seated'] = [{'find': fid, 'unit': NH, 'deposit': 1204} for fid, _ in new]
    json.dump(p2, open(T / 'pass2.json', 'w'), ensure_ascii=False, indent=1)
    for fid, row in new:
        row['id'] = fid; F.append(row)
    byid = {f['id']: f for f in F}
    # pairs of pass-2 finds in different claims
    claims = json.load(open(T / 'claims.json'))['claims']
    of = {st['find']: c['id'] for c in claims for st in c['statements']}
    P2 = [f for f in F if f.get('pass') == 2 and f['shape'] != 'C' and f['id'] in of]
    X = TfidfVectorizer(sublinear_tf=True, min_df=2, stop_words='english', ngram_range=(1, 2)).fit_transform([f['quote'] for f in F])
    idx = {f['id']: n for n, f in enumerate(F)}
    M = X[[idx[f['id']] for f in P2]]
    S = (M @ M.T).toarray()
    seen, pairs = set(), []
    for a in range(len(P2)):
        for b in range(a + 1, len(P2)):
            if S[a, b] >= 0.40 and of[P2[a]['id']] != of[P2[b]['id']]:
                k = tuple(sorted((of[P2[a]['id']], of[P2[b]['id']])))
                if k in seen:
                    continue
                seen.add(k); pairs.append((P2[a]['id'], P2[b]['id'], round(float(S[a, b]), 3)))
    pairs.sort(key=lambda p: -p[2])
    meta = {d['deposit']: d for d in json.load(open(T / 'deposit-titles.json'))}

    def card(i):
        f = byid[i]; m = meta.get(f['deposit'], {})
        return {'id': i, 'deposit': f['deposit'], 'date': f.get('date'), 'title': m.get('title'), 'path': f.get('path') or m.get('path'),
                'shape': f['shape'], 'lines': f['lines'], 'quote': f['quote'], 'falsifier_quote': f.get('falsifier_quote'),
                'window': f.get('window'), 'points_to': f.get('points_to'), 'note': f.get('note')}
    te = [{'item': f'E:{a}~{b}', 'score': s, 'a': card(a), 'b': card(b)} for a, b, s in pairs]
    for n in range(0, len(te), 50):
        Q['batches'].append({'batch_id': f'TEP{n // 50 + 1:02d}', 'kind': 'TE', 'items': te[n:n + 50]})
    # TN17: the seated find, against the nearest claims
    base = json.load(open(T / 'claims-p2-base.json'))['claims']
    cdoc = [' '.join(byid[s['find']]['quote'] for s in c['statements'] if s['find'] in byid) for c in base]
    vec = TfidfVectorizer(sublinear_tf=True, min_df=2, stop_words='english', ngram_range=(1, 2)).fit(cdoc)
    CM = vec.transform(cdoc)
    tn = []
    for fid, row in new:
        s = (vec.transform([row['quote']]) @ CM.T).toarray()[0]
        tn.append({'item': 'N:' + fid, 'find': card(fid), 'candidates': [
            {'claim': base[i]['id'], 'score': round(float(s[i]), 3), 'tier': base[i]['tier'], 'registered': base[i]['registered'],
             'registered_in': base[i]['registered_in'], 'title': base[i].get('title'), 'statements': len(base[i]['statements']),
             'series': base[i].get('series') or [], 'statement': (base[i].get('statement') or '')[:900],
             'falsifier': (base[i].get('falsifier') or '')[:400] or None} for i in [int(j) for j in np.argsort(-s)[:6]]]})
    if tn:
        Q['batches'].append({'batch_id': 'TN17', 'kind': 'TN', 'items': tn})
    Q['counts']['TEP'] = len(te); Q['counts']['TN'] = Q['counts'].get('TN', 0) + len(tn)
    json.dump(Q, open(T / 'queue.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps({'seated': [fid for fid, _ in new], 'TEP_pairs': len(te), 'TEP_batches': (len(te) + 49) // 50, 'TN17': len(tn)}))


if __name__ == '__main__':
    main()
