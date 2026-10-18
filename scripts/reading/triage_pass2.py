#!/usr/bin/env python3
"""triage_pass2.py — the finds of reading pass 2 into the triage (2026-10-18).

Lee Sharks, 2026-10-18: "lets fo that triage pass". Pass 2 (READING-PROTOCOL v1.3, data/reading/pass2-queue.json) read
the text the record repair added and the attachments: 767 verified finds. This script does what needs no judgment and
builds the judgment batches for the rest.

  finds        appended to finds.jsonl and triage/finds.ids.jsonl after the 6162 of pass 1, so every earlier id stands.
               id F<deposit>.<shape><n>, n continuing that deposit's count. An attachment's find takes the first deposit
               that carries it (all are kept as "deposits"). A unit that names no deposit is held (pass2.json "held").
  duplicates   a pass-2 find in the same deposit as a pass-1 find, quoting the same passage (one quote contains the
               other, or TF-IDF cosine >= 0.85): the passage was read twice — by pass 1 before the repair moved it, or as
               context. Not a new statement; recorded as a duplicate of that find. Likewise between two pass-2 finds.
  restatements a pass-2 find and a find of another deposit with cosine >= 0.85: joined mechanically, as in pass 1
               (triage_cluster.py); written to triage/restatements-p2.json.
  superseded   the record repair kept each replaced body under "## Appendix — ... previously seated here ... superseded
               ... (retained per non-destruction)". A find that now lies below that heading was read from a body that is
               not the record's text. Every such find, of either pass, is listed in triage/superseded.json, and the
               assembler holds it out as it holds out finds whose quote is gone.
  TN           each remaining pass-2 find (not C), with the six existing claims nearest it (TF-IDF over all of a claim's
               statements): is it one of them (same / variant), a member of one (in) or a list holding one (contains),
               related to one, or a new claim? Batches TN01…, 30 items each, appended to triage/queue.json.
  TC           each pass-2 confirmation record (C), with its mechanical pointers (triage_base.py), as in pass 1:
               batches TCP01…, appended to triage/queue.json.
USAGE  python3 scripts/reading/triage_pass2.py   (once; it refuses to append twice)
"""
import collections, glob, json, pathlib, re, subprocess, sys
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'; T = R / 'triage'
AX = ROOT.parent / 'alexanarch'
APPX = re.compile(r'^## Appendix\b.*(previously seated|superseded).*retained per non-destruction', re.I)
norm = lambda s: ' '.join((s or '').split())
SIZE = 30


def appendix_start(path):
    try:
        for i, l in enumerate(pathlib.Path(path).read_bytes().decode('utf-8', 'replace').split('\n')):
            if APPX.search(l):
                return i + 1
    except Exception:
        pass
    return None


def main():
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    if any(f.get('pass') == 2 for f in F):
        sys.exit('pass-2 finds are already in finds.jsonl')
    ids = [json.loads(l)['id'] for l in open(T / 'finds.ids.jsonl')]
    for f, i in zip(F, ids):
        f['id'] = i
    n1 = len(F)
    cnt = collections.Counter((f['deposit'], f['shape']) for f in F)
    reg = {int(d['deposit_number']): d for d in json.load(open(AX / 'data/registry.json'))['deposits'] if d.get('deposit_number') is not None}
    q2 = json.load(open(R / 'pass2-queue.json'))
    unit = {u['unit']: u for b in q2['batches'] for u in b['units']}
    new, held = [], []
    for p in sorted(glob.glob(str(R / 'batches/[RA][0-9][0-9][0-9][0-9].json'))):
        out = json.load(open(p)); bid = out['batch_id']
        if not json.load(open(p.replace('.json', '.verified.json')))['summary']['quotes_failed'] == 0:
            sys.exit(f'{bid} has failed quotes')
        for e in out['deposits']:
            u = unit[e['unit']]; deps = u.get('deposits') or ([u['deposit']] if u.get('deposit') else [])
            for f in e.get('finds') or []:
                row = {'deposit': deps[0] if deps else None, 'deposits': deps, 'date': (reg.get(deps[0]) or {}).get('date') if deps else None,
                       'batch_id': bid, 'run': f'R-p2-{bid}', 'pass': 2, 'unit': u['unit'], 'path': u['path'],
                       **{k: f.get(k) for k in ('shape', 'quote', 'lines', 'falsifier_quote', 'falsifier_lines', 'window',
                                                'points_to', 'also_at', 'note')}, 'verified': True, 'verification_fails': []}
                (new if deps else held).append(row)
    # ids
    for f in new:
        cnt[(f['deposit'], f['shape'])] += 1
        f['id'] = f"F{f['deposit']}.{f['shape']}{cnt[(f['deposit'], f['shape'])]}"
    allF = F + new
    X = TfidfVectorizer(sublinear_tf=True, min_df=2, stop_words='english', ngram_range=(1, 2)).fit_transform([f['quote'] for f in allF])
    S = (X[n1:] @ X.T).toarray()
    dup, joins = {}, []
    for k, f in enumerate(new):
        j = n1 + k; s = S[k]
        qf = norm(f['quote'])
        for i in np.argsort(-s):
            if i == j or s[i] < 0.5:
                break
            g = allF[i]
            if g['deposit'] == f['deposit'] and (i < j) and (s[i] >= 0.85 or qf in norm(g['quote']) or norm(g['quote']) in qf):
                dup[f['id']] = {'of': g['id'], 'score': round(float(s[i]), 3)}; break
        if f['id'] in dup:
            continue
        for i in np.argsort(-s):
            if s[i] < 0.85:
                break
            g = allF[i]
            if i != j and g['deposit'] != f['deposit'] and g['id'] not in dup and g['shape'] != 'C' and f['shape'] != 'C':
                joins.append([f['id'], g['id'], round(float(s[i]), 3)])
    # superseded bodies: every find, either pass, below its deposit's retained-appendix heading
    titles = {d['deposit']: d for d in json.load(open(T / 'deposit-titles.json'))}
    cur = json.load(open(T / 'currency.json'))['finds']
    starts, sup = {}, []
    for f in allF:
        path = f.get('path') if f.get('pass') == 2 else (titles.get(f['deposit']) or {}).get('path')
        if not path:
            continue
        if path not in starts:
            starts[path] = appendix_start(path)
        a = starts[path]
        ln = (cur.get(f['id'], {}).get('lines_now') if f.get('pass') != 2 else None) or f['lines']
        if a and ln and ln[0] >= a and cur.get(f['id'], {}).get('state') != 'gone':
            sup.append({'find': f['id'], 'deposit': f['deposit'], 'pass': f.get('pass', 1), 'lines': ln, 'appendix_from': a, 'path': path})
    # write finds
    with open(R / 'finds.jsonl', 'a') as o:
        for f in new:
            o.write(json.dumps({k: v for k, v in f.items() if k != 'id'}, ensure_ascii=False) + '\n')
    with open(T / 'finds.ids.jsonl', 'a') as o:
        for f in new:
            o.write(json.dumps({'id': f['id'], 'deposit': f['deposit'], 'shape': f['shape'], 'lines': f['lines']}) + '\n')
    json.dump({'what': 'Pass-2 finds in the triage (triage_pass2.py): duplicates of finds already held, and finds held for want '
                       'of a deposit.', 'appended': len(new), 'duplicates': dup,
               'held': [{k: f.get(k) for k in ('unit', 'shape', 'quote', 'lines', 'path', 'batch_id')} for f in held]},
              open(T / 'pass2.json', 'w'), ensure_ascii=False, indent=1)
    json.dump({'what': 'Pass-2 restatements: a pass-2 find and a find of another deposit with TF-IDF cosine >= 0.85, joined '
                       'mechanically (triage_pass2.py).', 'joins': joins}, open(T / 'restatements-p2.json', 'w'), ensure_ascii=False, indent=1)
    json.dump({'what': 'Finds read from a body the record repair replaced and kept as an appendix ("## Appendix — ... previously '
                       'seated here ... superseded ... (retained per non-destruction)"). Held out of the claims (triage_pass2.py).',
               'appendix_starts': {p: a for p, a in sorted(starts.items()) if a}, 'finds': sup},
              open(T / 'superseded.json', 'w'), ensure_ascii=False, indent=1)
    # pointers for the new C finds (triage_base regenerates ids and pointers for all; ids are unchanged by construction)
    subprocess.run([sys.executable, str(ROOT / 'scripts/reading/triage_base.py'), '--registry', str(AX / 'data/registry.json')], check=True)
    ids2 = [json.loads(l)['id'] for l in open(T / 'finds.ids.jsonl')]
    assert ids2[:n1] == ids and ids2[n1:] == [f['id'] for f in new], 'find ids moved'
    # judgment batches
    claims = json.load(open(T / 'claims.json'))['claims']
    byid = {f['id']: f for f in allF}
    held_sup = {x['find'] for x in sup}
    meta = {d['deposit']: d for d in json.load(open(T / 'deposit-titles.json'))}

    def card(i):
        f = byid[i]; m = meta.get(f['deposit'], {})
        return {'id': i, 'deposit': f['deposit'], 'deposits': f.get('deposits'), 'date': f.get('date'), 'title': m.get('title'),
                'path': f.get('path') or m.get('path'), 'shape': f['shape'], 'lines': f['lines'], 'quote': f['quote'],
                'falsifier_quote': f.get('falsifier_quote'), 'window': f.get('window'), 'points_to': f.get('points_to'), 'note': f.get('note')}
    cdoc = [' '.join(byid[s['find']]['quote'] for s in c['statements'] if s['find'] in byid) for c in claims]
    vec = TfidfVectorizer(sublinear_tf=True, min_df=2, stop_words='english', ngram_range=(1, 2)).fit(cdoc + [f['quote'] for f in new])
    CM = vec.transform(cdoc)
    joined = {a for a, b, s in joins}
    tn = []
    for f in new:
        if f['shape'] == 'C' or f['id'] in dup or f['id'] in joined or f['id'] in held_sup:
            continue
        s = (vec.transform([f['quote'] + ' ' + (f.get('falsifier_quote') or '')]) @ CM.T).toarray()[0]
        top = [int(i) for i in np.argsort(-s)[:6]]
        tn.append({'item': 'N:' + f['id'], 'find': card(f['id']), 'candidates': [
            {'claim': claims[i]['id'], 'score': round(float(s[i]), 3), 'tier': claims[i]['tier'], 'registered': claims[i]['registered'],
             'registered_in': claims[i]['registered_in'], 'title': claims[i].get('title'), 'statements': len(claims[i]['statements']),
             'series': claims[i].get('series') or [], 'statement': (claims[i].get('statement') or '')[:900],
             'falsifier': (claims[i].get('falsifier') or '')[:400] or None} for i in top]})
    tc = []
    for p in json.load(open(T / 'pointers.json'))['pointers']:
        if p['shape'] != 'C' or p['id'] not in {f['id'] for f in new} or p['id'] in dup or p['id'] in held_sup:
            continue
        tc.append({'item': 'C:' + p['id'], 'find': card(p['id']), 'resolved': [
            {'deposit': t['deposit'], 'how': t['how'], 'title': meta.get(t['deposit'], {}).get('title'),
             'path': meta.get(t['deposit'], {}).get('path'),
             'candidates': [dict(card(c['id']), score=c['score']) for c in t['candidates'] if c['id'] in byid]} for t in p['targets']]})
    Q = json.load(open(T / 'queue.json'))
    for k, L in (('TN', tn), ('TCP', tc)):
        for n in range(0, len(L), SIZE):
            Q['batches'].append({'batch_id': f'{k}{n // SIZE + 1:02d}', 'kind': 'TN' if k == 'TN' else 'TC', 'items': L[n:n + SIZE]})
    Q['counts']['TN'] = len(tn); Q['counts']['TCP'] = len(tc)
    json.dump(Q, open(T / 'queue.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps({'appended': len(new), 'held_no_deposit': len(held), 'duplicates': len(dup), 'restatement_joins': len(joins),
                      'superseded_finds': len(sup), 'superseded_pass1': sum(1 for x in sup if x['pass'] == 1),
                      'TN_items': len(tn), 'TC_items': len(tc)}))


if __name__ == '__main__':
    main()
