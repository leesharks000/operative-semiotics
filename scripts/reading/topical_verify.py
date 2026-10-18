#!/usr/bin/env python3
"""topical_verify.py — check a topical batch against the queue and the claims (2026-10-17).

Per batch: every group decided once, in order, with 'reviewed' equal to the group's claims; every set's kind in
{same, states, series}; every claim id exists in the batch; a claim in at most one same/states set across the batch;
'states' carries len(claims)-1 changes; every member has a verbatim evidence phrase from its own statement, falsifier
or later statements; read ranges inside the file. Writes <ID>.verified.json; exit 1 on any failure.
USAGE  python3 scripts/reading/topical_verify.py <ID> [<ID> ...]
"""
import json, sys, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'data/reading/triage'


def main():
    Q = {b['batch_id']: b for b in json.load(open(T / 'topical-queue.json'))['batches']}
    if (T / 'join-queue.json').exists():  # the join pass (JOIN-PROTOCOL.md) uses the same shape
        Q.update({b['batch_id']: b for b in json.load(open(T / 'join-queue.json'))['batches']})
    paths = {d['deposit']: d.get('path') for d in json.load(open(T / 'deposit-titles.json'))}
    bad = False
    for bid in sys.argv[1:]:
        fails = []; b = Q[bid]; out = json.load(open(T / f'topical/{bid}.json'))
        cards = {c['claim']: c for g in b['groups'] for c in g['claims']}
        text = {k: '\n'.join([c['statement'] or '', c.get('falsifier') or ''] + [s['quote'] for s in c['later_statements']])
                for k, c in cards.items()}
        want = [g['group'] for g in b['groups']]; got = [g.get('group') for g in out.get('groups', [])]
        if got != want:
            fails.append(f'groups {got[:4]}… != {want[:4]}…')
        seen = collections.Counter()
        for g, qg in zip(out.get('groups', []), b['groups']):
            if sorted(g.get('reviewed') or []) != sorted(c['claim'] for c in qg['claims']):
                fails.append(f"{g.get('group')}: reviewed does not list the group's claims")
            for s in g.get('sets') or []:
                w = f"{g.get('group')}:{s.get('kind')}"
                ids = s.get('claims') or []
                if s.get('kind') not in ('same', 'states', 'series'):
                    fails.append(f'{w}: kind'); continue
                if len(ids) < 2:
                    fails.append(f'{w}: fewer than two claims')
                for i in ids:
                    if i not in cards:
                        fails.append(f'{w}: {i} not in batch')
                if s['kind'] in ('same', 'states'):
                    seen.update(ids)
                if s['kind'] == 'states' and len(s.get('change') or []) != len(ids) - 1:
                    fails.append(f'{w}: change needs {len(ids) - 1} entries')
                if s['kind'] == 'series' and not s.get('name'):
                    fails.append(f'{w}: series without name')
                if not s.get('basis'):
                    fails.append(f'{w}: no basis')
                ev = {e.get('claim'): e.get('phrase') for e in s.get('evidence') or [] if isinstance(e, dict)}
                for i in ids:
                    p = ev.get(i)
                    if i in cards and (not isinstance(p, str) or not 8 <= len(p) <= 400 or p not in text[i]):
                        fails.append(f'{w}: evidence for {i} not verbatim: {str(p)[:50]!r}')
            for r in g.get('read') or []:
                try:
                    dep, a, z = r; n = len(pathlib.Path(paths[int(dep)]).read_text(encoding='utf-8').split('\n'))
                    if not 1 <= a <= z <= n + 1:
                        fails.append(f"{g.get('group')}: read {r} outside 1..{n}")
                except Exception as e:
                    fails.append(f"{g.get('group')}: read {r}: {e}")
        for i, n in seen.items():
            if n > 1:
                fails.append(f'{i} in {n} same/states sets')
        json.dump({'batch_id': bid, 'fails': fails, 'verified': not fails}, open(T / f'topical/{bid}.verified.json', 'w'), indent=1)
        sets = collections.Counter(s['kind'] for g in out.get('groups', []) for s in g.get('sets') or [])
        print(f'{bid}: {dict(sets)}; ' + ('VERIFIED' if not fails else f'{len(fails)} FAIL(S): ' + ' | '.join(fails[:6])))
        bad |= bool(fails)
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
