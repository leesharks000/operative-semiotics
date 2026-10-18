#!/usr/bin/env python3
"""verify_annotate.py — mechanical check of an annotation batch (ANNOTATION-PROTOCOL v1.0).

    python3.12 scripts/reading/verify_annotate.py data/reading/batches/N001.json [--write]

Checks: every queued claim answered, each listed task present with legal vocabulary, every quote verbatim and inside its
stated lines in a path belonging to the claim, read ranges covering each statement's lines_now, file unchanged since
queued. With --write the result is stored as <batch>.verified.json.
"""
import hashlib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'
BASIS = {'in-text', 'container', 'framing', 'unknown'}
MODES = {'empirical-forecast', 'design-specification', 'scenario', 'fictional-report', 'performative-anticipation', 'vision'}
KINDS = {'stated', 'recoverable', 'none'}
DATE = re.compile(r'^\d{4}(-\d{2}(-\d{2})?)?$')


def norm(s):
    return re.sub(r"\s+", " ", s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip()


_cache = {}


def lines_of(p):
    if p not in _cache:
        raw = pathlib.Path(p).read_bytes()
        _cache[p] = (raw.decode('utf-8', 'replace').split('\n'), hashlib.sha256(raw).hexdigest())
    return _cache[p]


def quote_ok(p, q, ln, tag, fails):
    if not q:
        return
    L, _ = lines_of(p)
    if norm(q) not in norm('\n'.join(L)):
        fails.append(f'{tag}: not verbatim in {pathlib.Path(p).name}: {q[:60]!r}'); return
    if not ln or len(ln) != 2:
        fails.append(f'{tag}: quote without [a, b] lines'); return
    a, b = max(1, int(ln[0]) - 2), min(len(L), int(ln[1]) + 2)
    if norm(q) not in norm('\n'.join(L[a - 1:b])):
        fails.append(f'{tag}: verbatim but not at lines {ln}')


def main():
    bp = pathlib.Path(sys.argv[1]); out = json.loads(bp.read_text())
    Q = json.load(open(R / 'annotate-queue.json'))
    b = next(x for x in Q['batches'] if x['batch_id'] == out['batch_id'])
    queued = {x['claim']: x for x in b['items']}
    res = {'batch_id': out['batch_id'], 'checks': []}; seen = set(); nf = 0
    for it in out.get('items', []):
        cid = it.get('claim'); fails = []; seen.add(cid)
        if cid not in queued:
            res['checks'].append({'claim': cid, 'fails': ['QUEUED: not in this batch']}); continue
        q = queued[cid]; paths = {s['path'] for s in q['statements']}
        for s in q['statements']:
            if lines_of(s['path'])[1] != s['sha256']:
                fails.append(f"HASH: {pathlib.Path(s['path']).name} changed since queued")
        cov = {}
        for rr in it.get('read_ranges') or []:
            for a, z in rr.get('ranges') or []:
                cov.setdefault(rr.get('path'), set()).update(range(int(a), int(z) + 1))
        for s in q['statements']:
            a, z = s['lines_now']
            want = set(range(max(1, a - 10), min(s['lines_total'], z + 10) + 1))
            if not want <= cov.get(s['path'], set()):
                fails.append(f"COVER: {s['find']} lines {a}-{z} (±10) not all in read_ranges")
        for t in ('dates', 'mode', 'falsifier'):
            if (t in q['tasks']) != (t in it):
                fails.append(f"TASK: {t} {'missing' if t in q['tasks'] else 'not asked'}")
        if 'dates' in it:
            byf = {s['find']: s for s in q['statements']}
            got = {d.get('find'): d for d in it['dates'].get('statements') or []}
            for f in byf:
                if f not in got:
                    fails.append(f'DATES: no entry for {f}')
            for f, d in got.items():
                if f not in byf:
                    fails.append(f'DATES: {f} is not a statement of this claim'); continue
                if d.get('stated_basis') not in BASIS:
                    fails.append(f"DATES: {f} basis {d.get('stated_basis')!r}")
                if d.get('stated') is not None and not DATE.match(str(d['stated'])):
                    fails.append(f"DATES: {f} stated {d.get('stated')!r} not a date")
                if d.get('stated_basis') == 'in-text' and not d.get('basis_quote'):
                    fails.append(f'DATES: {f} in-text without basis_quote')
                if not isinstance(d.get('retrospective'), bool):
                    fails.append(f'DATES: {f} retrospective not true/false')
                if d.get('retrospective') and not (d.get('looks_back_to') or {}).get('what'):
                    fails.append(f'DATES: {f} retrospective without looks_back_to.what')
                lb = d.get('looks_back_to') or {}
                if lb.get('date') is not None and not DATE.match(str(lb['date'])):
                    fails.append(f"DATES: {f} looks_back_to.date {lb.get('date')!r} not a date")
                quote_ok(byf[f]['path'], d.get('basis_quote'), d.get('basis_lines'), f'DATES {f} basis', fails)
                quote_ok(byf[f]['path'], lb.get('quote'), lb.get('lines'), f'DATES {f} looks_back', fails)
        if 'mode' in it:
            m = it['mode']
            if m.get('mode') not in MODES:
                fails.append(f"MODE: {m.get('mode')!r}")
            if not m.get('fulfilment'):
                fails.append('MODE: no fulfilment')
            if m.get('basis_quote'):
                p = m.get('basis_path') or (next(iter(paths)) if len(paths) == 1 else None)
                if p not in paths:
                    fails.append('MODE: basis_path missing or not a path of this claim')
                else:
                    quote_ok(p, m['basis_quote'], m.get('basis_lines'), 'MODE basis', fails)
        if 'falsifier' in it:
            x = it['falsifier']
            if x.get('kind') not in KINDS:
                fails.append(f"FALSI: kind {x.get('kind')!r}")
            if x.get('kind') == 'stated':
                p = x.get('path') or (next(iter(paths)) if len(paths) == 1 else None)
                if not x.get('quote'):
                    fails.append('FALSI: stated without quote')
                elif p not in paths:
                    fails.append('FALSI: path missing or not a path of this claim')
                else:
                    quote_ok(p, x['quote'], x.get('lines'), 'FALSI', fails)
            if x.get('kind') == 'recoverable' and not str(x.get('reader_condition') or '').startswith('Reader-supplied: '):
                fails.append('FALSI: recoverable without "Reader-supplied: " condition')
        nf += bool(fails)
        res['checks'].append({'claim': cid, 'fails': fails})
    for c in queued:
        if c not in seen:
            res['checks'].append({'claim': c, 'fails': ['QUEUED: no entry for a queued claim']}); nf += 1
    res['summary'] = {'items': len(queued), 'answered': len(seen & set(queued)), 'items_with_fails': nf}
    print(json.dumps(res['summary']))
    for c in res['checks']:
        for f in c['fails']:
            print(f"  {c['claim']}: {f}")
    if '--write' in sys.argv:
        bp.with_suffix('.verified.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n')


if __name__ == '__main__':
    main()
