#!/usr/bin/env python3
"""verify_adjudicate.py — mechanical check of a recall-adjudication batch (RECALL-ADJUDICATE v1.0).

    python3.12 scripts/reading/verify_adjudicate.py data/reading/batches/J01.json [--write]
"""
import json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'
V = {'covered', 'missed', 'excluded', 'not-a-claim'}


def main():
    bp = pathlib.Path(sys.argv[1]); out = json.loads(bp.read_text())
    b = next(x for x in json.load(open(R / 'recall-adjudicate-queue.json'))['batches'] if x['batch_id'] == out['batch_id'])
    q = {x['item']: x for x in b['items']}; res = {'batch_id': out['batch_id'], 'checks': []}; seen = set()
    for it in out.get('items', []):
        i = it.get('item'); seen.add(i); fails = []
        if i not in q:
            res['checks'].append({'item': i, 'fails': ['QUEUED: not in this batch']}); continue
        x = q[i]; v = it.get('verdict')
        if v not in V:
            fails.append(f'VERDICT: {v!r}')
        cov = set()
        for a, z in it.get('read_ranges') or []:
            cov.update(range(int(a), int(z) + 1))
        a, z = x['lines']
        if not set(range(max(1, a - 10), min(x['lines_total'], z + 10) + 1)) <= cov:
            fails.append('COVER: passage lines ±10 not read')
        if v == 'covered' and it.get('find') not in {f['find'] for f in x['first_reading_finds']}:
            fails.append(f"FIND: {it.get('find')!r} is not a first-reading find of this file")
        if v == 'missed' and it.get('shape') not in list('ABCDEFGH'):
            fails.append(f"SHAPE: {it.get('shape')!r}")
        if v == 'excluded' and not it.get('rule'):
            fails.append('RULE: excluded without rule')
        if it.get('same_as') and it['same_as'] not in q:
            fails.append('SAME: same_as names no item of this batch')
        res['checks'].append({'item': i, 'fails': fails})
    for i in q:
        if i not in seen:
            res['checks'].append({'item': i, 'fails': ['QUEUED: no entry']})
    res['summary'] = {'items': len(q), 'answered': len(seen & set(q)), 'items_with_fails': sum(bool(c['fails']) for c in res['checks'])}
    print(json.dumps(res['summary']))
    for c in res['checks']:
        for f in c['fails']:
            print(f"  {c['item']}: {f}")
    if '--write' in sys.argv:
        bp.with_suffix('.verified.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n')


if __name__ == '__main__':
    main()
