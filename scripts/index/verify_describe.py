#!/usr/bin/env python3
"""verify_describe.py — mechanical check of a describe batch.  python3.12 scripts/index/verify_describe.py <file> [--write]"""
import json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
VERDICT = re.compile(r'\b(correctly|proves?|proven|demonstrates?)\b', re.I)


def main():
    bp = pathlib.Path(sys.argv[1]); out = json.loads(bp.read_text())
    b = next(x for x in json.load(open(ROOT / 'data/index/describe-queue.json'))['batches'] if x['batch_id'] == out['batch_id'])
    q = {p['page']: p for p in b['pages']}; res = {'batch_id': out['batch_id'], 'checks': []}; seen = set()
    for p in out.get('pages', []):
        pid = p.get('page'); seen.add(pid); fails = []
        if pid not in q:
            res['checks'].append({'page': pid, 'fails': ['QUEUED: not in this batch']}); continue
        d = p.get('description') or ''
        if not d.strip():
            fails.append('DESC: empty')
        if len(d) > 1100:
            fails.append(f'DESC: {len(d)} characters (over 1,100)')
        old = len(q[pid]['description'] or '')
        if old and not (0.6 * old <= len(d) <= max(1.5 * old, old + 250)):
            fails.append(f'DESC: length {len(d)} far from the old {old}')
        for m in VERDICT.finditer(d):
            if not re.search(r'#\d+[^.]{0,60}$', d[:m.start()]):
                fails.append(f'VOICE: "{m.group(0)}" in the index\'s own voice; say it only as a deposit\'s report ("#N reports that it shows")')
        ids = {c['id'] for c in q[pid]['claims']}
        bad = [r for r in p.get('residue') or [] if r not in ids]
        if bad:
            fails.append(f'RESIDUE: not on this page: {bad[:4]}')
        fails = [f for f in fails if f]
        res['checks'].append({'page': pid, 'fails': fails})
    for pid in q:
        if pid not in seen:
            res['checks'].append({'page': pid, 'fails': ['QUEUED: no entry']})
    res['summary'] = {'pages': len(q), 'answered': len(seen & set(q)), 'pages_with_fails': sum(bool(c['fails']) for c in res['checks'])}
    print(json.dumps(res['summary']))
    for c in res['checks']:
        for f in c['fails']:
            print(f"  {c['page']}: {f}")
    if '--write' in sys.argv:
        bp.with_suffix('.verified.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n')


if __name__ == '__main__':
    main()
