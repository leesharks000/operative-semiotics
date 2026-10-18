#!/usr/bin/env python3
"""naming_verify.py — check a naming batch: every page named once and in order; title <= 80 chars and not generic;
slug [a-z0-9-] <= 60, unique across all verified batches; description 2-4 sentences; line in the archive's lines; each
move names a claim on that page and a real page (or null). Writes <ID>.verified.json; exit 1 on failure.
USAGE  python3 scripts/index/naming_verify.py <ID> [...]
"""
import json, sys, re, pathlib, glob
ROOT = pathlib.Path(__file__).resolve().parents[2]; I = ROOT / 'data/index'
GENERIC = re.compile(r'(?i)^((assorted|misc|various|other|general)\b|(retrieval|claims?)$)')


def main():
    Q = json.load(open(I / 'naming-queue.json')); B = {b['batch_id']: b for b in Q['batches']}
    allp = set(Q['all_pages']); lines = set(Q['lines'])
    taken = {}
    for f in glob.glob(str(I / 'naming/NM*.json')):
        if f.endswith('.verified.json'):
            continue
        bid = pathlib.Path(f).stem
        for p in json.load(open(f)).get('pages', []):
            taken.setdefault(p.get('slug'), set()).add(bid)
    bad = False
    for bid in sys.argv[1:]:
        fails = []; b = B[bid]; out = json.load(open(I / f'naming/{bid}.json'))
        want = [p['page'] for p in b['pages']]; got = [p.get('page') for p in out.get('pages', [])]
        if got != want:
            fails.append(f'pages {got[:3]}… != {want[:3]}…')
        onpage = {p['page']: {c['claim'] for c in p['claims']} for p in b['pages']}
        for p in out.get('pages', []):
            w = p.get('page'); t = p.get('title') or ''
            if not t or len(t) > 80 or GENERIC.match(t):
                fails.append(f'{w}: title {t!r}')
            sl = p.get('slug') or ''
            if not re.fullmatch(r'[a-z0-9]+(-[a-z0-9]+)*', sl) or len(sl) > 60:
                fails.append(f'{w}: slug {sl!r}')
            elif len(taken.get(sl, set())) > 1 or sum(1 for q in out['pages'] if q.get('slug') == sl) > 1:
                fails.append(f'{w}: slug {sl!r} not unique')
            n = len(re.findall(r'[.!?](\s|$)', (p.get('description') or '').strip()))
            if not 2 <= n <= 4:
                fails.append(f'{w}: description has {n} sentences')
            if p.get('line') not in lines:
                fails.append(f'{w}: line {p.get("line")!r}')
            for m in p.get('moves') or []:
                if m.get('claim') not in onpage.get(w, set()):
                    fails.append(f'{w}: move of {m.get("claim")} not on page')
                if m.get('to') is not None and m.get('to') not in allp:
                    fails.append(f'{w}: move to {m.get("to")!r}')
        json.dump({'batch_id': bid, 'fails': fails, 'verified': not fails}, open(I / f'naming/{bid}.verified.json', 'w'), indent=1)
        print(f'{bid}: ' + ('VERIFIED' if not fails else f'{len(fails)} FAIL(S): ' + ' | '.join(fails[:6])))
        bad |= bool(fails)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
