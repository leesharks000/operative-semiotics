#!/usr/bin/env python3
"""verify_recall.py — mechanical check of a recall-audit batch (RECALL-BRIEF v1.0).

    python3.12 scripts/reading/verify_recall.py data/reading/batches/K01.json [--write]
"""
import hashlib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'


def norm(s):
    return re.sub(r"\s+", " ", s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip()


def main():
    bp = pathlib.Path(sys.argv[1]); out = json.loads(bp.read_text())
    b = next(x for x in json.load(open(R / 'recall-queue.json'))['batches'] if x['batch_id'] == out['batch_id'])
    queued = {d['deposit']: d for d in b['deposits']}
    res = {'batch_id': out['batch_id'], 'checks': []}; seen = set()
    for e in out.get('deposits', []):
        n = e.get('deposit'); seen.add(n); fails = []
        if n not in queued:
            res['checks'].append({'deposit': n, 'fails': ['QUEUED: not in this batch']}); continue
        q = queued[n]; raw = pathlib.Path(q['path']).read_bytes(); t = raw.decode('utf-8', 'replace'); L = t.split('\n')
        if hashlib.sha256(raw).hexdigest() != q['sha256']:
            fails.append('HASH: file changed since queued')
        cov = set()
        for a, z in e.get('read_ranges') or []:
            cov.update(range(int(a), int(z) + 1))
        miss = [i for i in range(1, q['lines_total'] + 1) if i not in cov]
        if e.get('status') == 'read' and miss:
            fails.append(f'COVER: {len(miss)} of {q["lines_total"]} lines not read (first {miss[:5]})')
        if e.get('status') not in ('read', 'partial'):
            fails.append(f"STATUS: {e.get('status')!r}")
        ps = e.get('passages') or []
        if not ps and not e.get('none_found'):
            fails.append('NONE: no passages and none_found false')
        for i, p in enumerate(ps):
            qt = p.get('quote') or ''
            if not qt or norm(qt) not in norm(t):
                fails.append(f'QUOTE: passage {i} not verbatim: {qt[:60]!r}'); continue
            ln = p.get('lines') or []
            if len(ln) != 2 or norm(qt) not in norm('\n'.join(L[max(0, ln[0] - 3):ln[1] + 2])):
                fails.append(f'QUOTE: passage {i} not at lines {ln}')
        res['checks'].append({'deposit': n, 'passages': len(ps), 'fails': fails})
    for n in queued:
        if n not in seen:
            res['checks'].append({'deposit': n, 'fails': ['QUEUED: no entry']})
    res['summary'] = {'deposits': len(queued), 'entries': len(seen), 'passages': sum(c.get('passages', 0) for c in res['checks']),
                      'deposits_with_fails': sum(bool(c['fails']) for c in res['checks'])}
    print(json.dumps(res['summary']))
    for c in res['checks']:
        for f in c['fails']:
            print(f"  #{c['deposit']}: {f}")
    if '--write' in sys.argv:
        bp.with_suffix('.verified.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n')


if __name__ == '__main__':
    main()
