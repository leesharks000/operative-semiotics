#!/usr/bin/env python3
"""review_verify.py — check a review batch: every page once, in order; title/slug/description/line as the naming
protocol; each split part has >= 6 claims, all on that page, none in two parts, and the page keeps >= 6; slugs unique
across the batch and its parts. Writes <ID>.verified.json; exit 1 on failure.
USAGE  python3 scripts/index/review_verify.py <ID> [...]
"""
import json, sys, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]; I = ROOT / 'data/index'


def chk(o, w, lines, fails):
    t = o.get('title') or ''
    if not t or len(t) > 80:
        fails.append(f'{w}: title {t!r}')
    sl = o.get('slug') or ''
    if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', sl) or len(sl) > 60:
        fails.append(f'{w}: slug {sl!r}')
    n = len(re.findall(r'[.!?](\s|$)', (o.get('description') or '').strip()))
    if not 2 <= n <= 4:
        fails.append(f'{w}: description has {n} sentences')
    if o.get('line') not in lines:
        fails.append(f'{w}: line {o.get("line")!r}')


def main():
    Q = json.load(open(I / 'review-queue.json')); B = {b['batch_id']: b for b in Q['batches']}; lines = set(Q['lines'])
    bad = False
    for bid in sys.argv[1:]:
        fails = []; b = B[bid]; out = json.load(open(I / f'review/{bid}.json'))
        if [p.get('page') for p in out.get('pages', [])] != [p['page'] for p in b['pages']]:
            fails.append('pages not one per queue page, in order')
        on = {p['page']: [c['claim'] for c in p['claims']] for p in b['pages']}
        slugs = []
        for p in out.get('pages', []):
            w = p.get('page'); chk(p, w, lines, fails); slugs.append(p.get('slug'))
            used = set()
            for n, s in enumerate(p.get('split') or []):
                chk(s, f'{w}.split{n + 1}', lines, fails); slugs.append(s.get('slug'))
                cs = s.get('claims') or []
                if len(cs) < 6:
                    fails.append(f'{w}.split{n + 1}: {len(cs)} claims (< 6)')
                for c in cs:
                    if c not in on.get(w, []):
                        fails.append(f'{w}.split{n + 1}: {c} not on the page')
                    if c in used:
                        fails.append(f'{w}: {c} in two parts')
                    used.add(c)
            if len(on.get(w, [])) - len(used) < 6 and p.get('split'):
                fails.append(f'{w}: keeps {len(on.get(w, [])) - len(used)} claims (< 6)')
        d = {s for s in slugs if slugs.count(s) > 1}
        if d:
            fails.append(f'duplicate slugs {sorted(d)[:4]}')
        json.dump({'batch_id': bid, 'fails': fails, 'verified': not fails}, open(I / f'review/{bid}.verified.json', 'w'), indent=1)
        print(f'{bid}: ' + ('VERIFIED' if not fails else f'{len(fails)} FAIL(S): ' + ' | '.join(fails[:6])))
        bad |= bool(fails)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
