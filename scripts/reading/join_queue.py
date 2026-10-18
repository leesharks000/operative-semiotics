#!/usr/bin/env python3
"""join_queue.py — the claims the topical readers named across groups, for the join pass (2026-10-17).

Lee Sharks, 2026-10-17: "lets join the pairs." A topical reader saw only the claims of its own batch; where a claim
belonged with one in another group it recorded the pair as an observation (TOPICAL-PROTOCOL: "a claim that belongs with
a claim in another group (name both ids)"). The triage readers recorded such pairs too. This collects every observation
(triage/topical-observations.json, triage/observations.json) naming two or more claims — by PRED id, find id or the
readers' shorthand <deposit>.<shape><n>, each resolved through its find to the claim that now holds it — and makes
each one an item: the observation verbatim, and every claim it names in full, as in the topical queue. Batches of 24.
The decision vocabulary and output are the topical protocol's (same / states / series), so topical_verify.py checks them.
USAGE  python3 scripts/reading/join_queue.py
"""
import json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'data/reading/triage'
ID = re.compile(r'(?:PRED-|F)?\b(\d{1,4})\.([A-H])(\d{1,2})\b')
SIZE = 24


def main():
    C = json.load(open(T / 'claims.json'))['claims']; byid = {c['id']: c for c in C}
    by_find = {st['find']: c['id'] for c in C for st in c['statements']}
    F = {json.loads(i)['id']: json.loads(f) for i, f in zip(open(T / 'finds.ids.jsonl'), open(ROOT / 'data/reading/finds.jsonl'))}
    titles = {d['deposit']: d for d in json.load(open(T / 'deposit-titles.json'))}
    obs = json.load(open(T / 'topical-observations.json'))['observations'] + json.load(open(T / 'observations.json'))['observations']

    def card(cid):
        c = byid[cid]
        return {'claim': cid, 'tier': c['tier'], 'registered': c['registered'], 'registered_in': c['registered_in'],
                'title': c.get('title'), 'path': titles.get(c['registered_in'], {}).get('path'), 'statement': c['statement'],
                'falsifier': c.get('falsifier'), 'window': c.get('window'),
                'later_statements': [{'find': s['find'], 'deposit': s['deposit'], 'date': s['date'], 'lines': s['lines'],
                                      'quote': F[s['find']]['quote']} for s in c['statements'][1:]],
                'series': c.get('series', []), 'states': c.get('states', []), 'related': c['related']}
    items, seen = [], set()
    for o in obs:
        t = o['observation'] if isinstance(o['observation'], str) else json.dumps(o['observation'], ensure_ascii=False)
        ids = []
        for m in ID.finditer(t):
            c = by_find.get(f'F{m.group(1)}.{m.group(2)}{m.group(3)}')
            if c and c not in ids:
                ids.append(c)
        if len(ids) < 2 or tuple(sorted(ids)) in seen:
            continue
        seen.add(tuple(sorted(ids)))
        items.append({'observation': t, 'from_batch': o['batch'], 'claims': ids})
    batches = []
    for n in range(0, len(items), SIZE):
        bid = f'TJ{n // SIZE + 1:02d}'
        batches.append({'batch_id': bid, 'groups': [
            {'group': f'{bid}.{j + 1}', 'observation': it['observation'], 'from_batch': it['from_batch'],
             'claims': [card(c) for c in it['claims']]} for j, it in enumerate(items[n:n + SIZE])]})
    try:  # batches of decisions made in-session on Lee's rulings (TM…) are kept across rebuilds
        batches += [b for b in json.load(open(T / 'join-queue.json'))['batches'] if b['batch_id'].startswith('TM')]
    except Exception:
        pass
    json.dump({'what': 'Join pass: each item is one reader observation naming claims across groups, with every claim it names. '
                       'Built by scripts/reading/join_queue.py; protocol data/reading/JOIN-PROTOCOL.md.',
               'counts': {'items': len(items), 'batches': len(batches)}, 'batches': batches},
              open(T / 'join-queue.json', 'w'), ensure_ascii=False, indent=1)
    print(len(items), 'items;', len(batches), 'batches')


if __name__ == '__main__':
    main()
