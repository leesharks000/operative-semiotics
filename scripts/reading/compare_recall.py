#!/usr/bin/env python3
"""compare_recall.py — the first reading and the recall audit's second reading, side by side, deposit by deposit.

For each sampled deposit: the first reading's finds that quote the file the auditor read (relocated to the file as it
stands), and the auditor's passages. Two passages MATCH when their line ranges overlap (±2 lines); a NEAR passage lies
within 15 lines of a find without overlapping it. Writes data/reading/recall-compare.json, and the queue of unmatched
audit passages for adjudication (recall-adjudicate-queue.json): did the first reading miss a passage the protocol
covers, or does the auditor's broader brief catch what the protocol excludes?
USAGE  python3.12 scripts/reading/compare_recall.py
"""
import collections, json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build_annotate import norm_map, nq

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'; T = R / 'triage'


def main():
    Q = json.load(open(R / 'recall-queue.json'))
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    ids = [json.loads(l)['id'] for l in open(T / 'finds.ids.jsonl')]
    claims = json.load(open(T / 'claims.json'))['claims']
    of = {s['find']: c['id'] for c in claims for s in c['statements']}
    rows, unmatched = [], []
    tot = collections.Counter()
    for b in Q['batches']:
        out = json.load(open(R / f"batches/{b['batch_id']}.json"))
        got = {e['deposit']: e for e in out['deposits']}
        for d in b['deposits']:
            n = d['deposit']; t = pathlib.Path(d['path']).read_text(encoding='utf-8', errors='replace')
            nt, ln = norm_map(t)
            orig = []
            for fid, f in zip(ids, F):
                if f['deposit'] != n and n not in (f.get('deposits') or []):
                    continue
                i = nt.find(nq(f['quote']))
                if i < 0:
                    continue  # quotes another file of the deposit (an attachment), or text since removed
                orig.append({'find': fid, 'shape': f['shape'], 'lines': [ln[i], ln[i + len(nq(f['quote'])) - 1]], 'claim': of.get(fid)})
            aud = got[n].get('passages') or []
            ov = lambda a, b, k=2: a[0] - k <= b[1] and b[0] - k <= a[1]
            om = [o for o in orig if any(ov(o['lines'], p['lines']) for p in aud)]
            am, near, un = [], [], []
            for k, p in enumerate(aud):
                if any(ov(o['lines'], p['lines']) for o in orig):
                    am.append(k)
                else:
                    (near if any(ov(o['lines'], p['lines'], 15) for o in orig) else un).append(k)
                    unmatched.append({'item': f'U:{n}:{k}', 'deposit': n, 'title': d['title'], 'path': d['path'], 'lines_total': d['lines_total'],
                                      'quote': p['quote'], 'lines': p['lines'], 'kind': p.get('kind'), 'why': p.get('why'),
                                      'near': k in near,
                                      'first_reading_finds': [{'find': o['find'], 'shape': o['shape'], 'lines': o['lines'],
                                                               'quote': next(f['quote'] for i2, f in zip(ids, F) if i2 == o['find'])[:600]} for o in orig]})
            rows.append({'deposit': n, 'words': d['words'], 'first_reading_finds': len(orig), 'first_found_by_audit': len(om),
                         'first_missed_by_audit': [o['find'] for o in orig if o not in om],
                         'audit_passages': len(aud), 'audit_matched': len(am), 'audit_near': len(near), 'audit_unmatched': len(un)})
            tot.update({'first': len(orig), 'first_matched': len(om), 'audit': len(aud), 'audit_matched': len(am), 'audit_near': len(near), 'audit_unmatched': len(un)})
    res = {'what': 'recall audit: first reading against a second reading of 40 random deposits (compare_recall.py)', 'totals': dict(tot),
           'rates': {'first_reading_finds_also_found_by_audit': round(tot['first_matched'] / max(1, tot['first']), 3),
                     'audit_passages_matching_a_first_find': round(tot['audit_matched'] / max(1, tot['audit']), 3),
                     'audit_passages_near_a_first_find': round(tot['audit_near'] / max(1, tot['audit']), 3),
                     'audit_passages_with_no_first_find': round(tot['audit_unmatched'] / max(1, tot['audit']), 3)},
           'deposits': rows}
    (R / 'recall-compare.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n')
    per = 40
    (R / 'recall-adjudicate-queue.json').write_text(json.dumps({'what': 'audit passages that overlap no first-reading find (near or not), for adjudication (RECALL-ADJUDICATE.md)',
        'batches': [{'batch_id': f'J{i // per + 1:02d}', 'items': unmatched[i:i + per]} for i in range(0, len(unmatched), per)]}, ensure_ascii=False, indent=1) + '\n')
    print(json.dumps(res['totals']), json.dumps(res['rates']), len(unmatched), 'to adjudicate')


if __name__ == '__main__':
    main()
