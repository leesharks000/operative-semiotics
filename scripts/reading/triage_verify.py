#!/usr/bin/env python3
"""triage_verify.py — check a triage batch against the queue, the finds and the texts (2026-10-17).

Per decision: the item exists in the batch and is decided once, in order; the vocabulary is the protocol's; every find id
named exists; every evidence phrase is a verbatim substring of the named find's quote (TC links, TR finds) or of the side
it is given for (TE), or, for deposit/self targets, of the deposit's text at the stated lines; read ranges lie in the file.
Writes <ID>.verified.json beside the batch. A failure is recorded, not hidden; exit 1 if any.
USAGE  python3 scripts/reading/triage_verify.py <ID> [<ID> ...]
"""
import json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'; T = R / 'triage'
V = {'TC': {'target_kind': {'find', 'deposit', 'self', 'external', 'unlocated'}},
     'TE': {'decision': {'same', 'variant', 'contains', 'related', 'distinct'}},
     'TR': {'match': {'found', 'partial', 'not_found', 'excluded', 'no_source'}}}
CLAIMED = {'came_true', 'partly', 'failed', 'pending'}


def main():
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    ids = [json.loads(l)['id'] for l in open(T / 'finds.ids.jsonl')]
    Q = dict(zip(ids, (f['quote'] + '\n' + (f.get('falsifier_quote') or '') for f in F)))  # quote or falsifier
    paths = {d['deposit']: d.get('path') for d in json.load(open(T / 'deposit-titles.json'))}
    q = {b['batch_id']: b for b in json.load(open(T / 'queue.json'))['batches']}
    bad_any = False
    for bid in sys.argv[1:]:
        fails = []
        b = q[bid]; out = json.load(open(T / f'batches/{bid}.json'))
        want = [i['item'] for i in b['items']]; got = [d.get('item') for d in out.get('decisions', [])]
        if got != want:
            fails.append(f'items: {len(got)} decided of {len(want)}; missing {sorted(set(want) - set(got))[:5]}; extra {sorted(set(got) - set(want))[:5]}')
        items = {i['item']: i for i in b['items']}

        def ev_in(phrase, fid, where):
            if fid not in Q:
                fails.append(f'{where}: unknown find {fid}'); return
            if not isinstance(phrase, str) or not (8 <= len(phrase) <= 400) or phrase not in Q[fid]:
                fails.append(f'{where}: evidence not verbatim in {fid}: {str(phrase)[:60]!r}')

        def text_ok(dep, lines, phrase, where):
            p = paths.get(dep)
            if not p or not pathlib.Path(p).exists():
                fails.append(f'{where}: no text for #{dep}'); return
            L = pathlib.Path(p).read_text(encoding='utf-8').split('\n')
            a, z = lines
            if phrase not in '\n'.join(L[a - 1:z]) and phrase not in ' '.join(x.strip() for x in L[a - 1:z]):
                fails.append(f'{where}: phrase not in #{dep} lines {a}-{z}: {str(phrase)[:60]!r}')
        for d in out.get('decisions', []):
            it = d.get('item'); w = it
            k = b['kind']
            for field, vocab in V[k].items():
                if d.get(field) not in vocab:
                    fails.append(f'{w}: {field}={d.get(field)!r}')
            for r in d.get('read') or []:
                try:
                    dep, a, z = r; p = paths.get(int(dep)); n = len(pathlib.Path(p).read_text(encoding='utf-8').split('\n'))
                    if not (1 <= a <= z <= n + 1):
                        fails.append(f'{w}: read range {r} outside 1..{n}')
                except Exception as e:
                    fails.append(f'{w}: read range {r}: {e}')
            if k == 'TC':
                ev = d.get('evidence') or []
                if d.get('target_kind') == 'find':
                    if not d.get('links'):
                        fails.append(f'{w}: find target with no links')
                    for n, l in enumerate(d.get('links') or []):
                        if l.get('claimed') not in CLAIMED:
                            fails.append(f'{w}: claimed={l.get("claimed")!r}')
                        e = ev[n] if n < len(ev) else None
                        e = e.get('phrase') if isinstance(e, dict) else e
                        ev_in(e, l.get('find'), w)
                if d.get('target_kind') in ('deposit', 'self'):
                    for e in ev:
                        if not isinstance(e, dict) or 'lines' not in e:
                            fails.append(f'{w}: deposit evidence needs {{phrase, lines}}'); continue
                        text_ok(int(d.get('deposit') or e.get('deposit')), e['lines'], e.get('phrase'), w)
            if k == 'TE':
                a, z = it[2:].split('~')
                if d.get('decision') == 'variant' and not d.get('change'):
                    fails.append(f'{w}: variant without change')
                if d.get('evidence_a'):
                    ev_in(d['evidence_a'], a, w)
                if d.get('evidence_b'):
                    ev_in(d['evidence_b'], z, w)
            if k == 'TR':
                if d.get('match') in ('found', 'partial'):
                    if not d.get('finds'):
                        fails.append(f'{w}: {d.get("match")} with no finds')
                    ev = d.get('evidence') or []
                    for n, fid in enumerate(d.get('finds') or []):
                        e = ev[n] if n < len(ev) else None
                        e = e.get('phrase') if isinstance(e, dict) else e
                        ev_in(e, fid, w)
                if d.get('match') == 'excluded' and not d.get('rule'):
                    fails.append(f'{w}: excluded without rule')
            if not d.get('basis'):
                fails.append(f'{w}: no basis')
        res = {'batch_id': bid, 'decisions': len(out.get('decisions', [])), 'fails': fails, 'verified': not fails}
        json.dump(res, open(T / f'batches/{bid}.verified.json', 'w'), ensure_ascii=False, indent=1)
        print(f'{bid}: {len(out.get("decisions", []))} decisions; ' + ('VERIFIED' if not fails else f'{len(fails)} FAIL(S): ' + ' | '.join(fails[:6])))
        bad_any |= bool(fails)
    return 1 if bad_any else 0


if __name__ == '__main__':
    sys.exit(main())
