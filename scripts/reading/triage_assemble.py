#!/usr/bin/env python3
"""triage_assemble.py — the claims of the prediction triage, from the finds and the verified judgment batches (2026-10-17).

One CLAIM per group of finds that state the same thing:
  joined by  restatement (cosine >= 0.85, mechanical) | TE 'same' | TE 'variant' (the change kept as a dated state)
  id         PRED-<deposit>.<shape><n> — the find id of the claim's earliest statement (by deposit date, then number)
  tier       forecast (A B E) | standing claim (G) | unbuilt test (F) | historical thesis (H) | priority record (D);
             a claim whose statements carry several shapes takes the first of A B E G F H D present
  registered the date of the earliest statement's deposit
  statements every find stating it, dated, with deposit, lines and quote; variants carry their change
  evidence   confirmation records (C) that link to any statement: who claims what came true or failed, and when
  related    claims a TE decision called 'related'
  aliases    register cards (data/predictions.json) and intake items (data/archive-intake.json) that a TR decision matched
Finds whose quote is no longer in the current text (currency.json 'gone') are held out and listed.
C finds are evidence, not claims; a C that links to nothing in the archive stays in confirmations.json with its target.
Only batches whose .verified.json says verified are used; the rest are listed as pending.
USAGE  python3 scripts/reading/triage_assemble.py
"""
import json, pathlib, collections, glob
ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'; T = R / 'triage'
TIER = [('A', 'forecast'), ('B', 'forecast'), ('E', 'forecast'), ('G', 'standing claim'), ('F', 'unbuilt test'),
        ('H', 'historical thesis'), ('D', 'priority record')]


def main():
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    for f, l in zip(F, open(T / 'finds.ids.jsonl')):
        f['id'] = json.loads(l)['id']
    byid = {f['id']: f for f in F}
    titles = {d['deposit']: d.get('title') for d in json.load(open(T / 'deposit-titles.json'))}
    q = json.load(open(T / 'queue.json'))
    done, pending = {}, []
    for b in q['batches']:
        v = T / f"batches/{b['batch_id']}.verified.json"
        if v.exists() and json.load(open(v)).get('verified'):
            done[b['batch_id']] = json.load(open(T / f"batches/{b['batch_id']}.json"))
        else:
            pending.append(b['batch_id'])
    cur = json.load(open(T / 'currency.json'))['finds']
    gone = sorted(i for i, v in cur.items() if v['state'] == 'gone')  # read from a body since replaced: held out, listed
    par = {f['id']: f['id'] for f in F if f['shape'] != 'C' and f['id'] not in set(gone)}

    def g(i):
        while par[i] != i:
            par[i] = par[par[i]]; i = par[i]
        return i

    def join(a, b):
        if a in par and b in par:
            par[g(a)] = g(b)
    for a, b, s in json.load(open(T / 'restatements.json'))['joins']:
        join(a, b)
    variants, related, conf, alias, contains = {}, [], [], collections.defaultdict(list), []
    # a find linked 'same'/'variant' to two or more finds of one other deposit is a list holding them: its links are
    # 'contains', not joins (TE03 item 28, TE06 items 19 and 38: a ledger joined to one of its members)
    links = collections.defaultdict(set)
    for bid, out in done.items():
        if bid.startswith('TE'):
            for d in out['decisions']:
                if d['decision'] in ('same', 'variant'):
                    a, b = d['item'][2:].split('~'); links[a].add(b); links[b].add(a)
    hub = set()
    for x, ys in links.items():
        per = collections.Counter(byid[y]['deposit'] for y in ys)
        if any(v >= 2 for v in per.values()):
            hub.add(x)
    for bid, out in done.items():
        for d in out['decisions']:
            it = d['item']
            if bid.startswith('TE'):
                a, b = it[2:].split('~')
                la, lb = len(byid[a]['quote']), len(byid[b]['quote'])
                if (d['decision'] in ('same', 'variant') and max(la, lb) > 3 * min(la, lb)):
                    d = dict(d, container='a' if la > lb else 'b'); hub.add(a if la > lb else b)  # a long list joined to one short member
                if d['decision'] == 'contains' or (d['decision'] in ('same', 'variant') and (a in hub or b in hub)):
                    contains.append((a, b) if (d.get('container') == 'a' or (d.get('container') != 'b' and a in hub)) else (b, a))
                elif d['decision'] in ('same', 'variant'):
                    join(a, b)
                    if d['decision'] == 'variant':
                        later = max((a, b), key=lambda x: (byid[x].get('date') or '', byid[x]['deposit']))
                        variants[later] = {'change': d.get('change'), 'from': a if later == b else b, 'batch': bid}
                elif d['decision'] == 'related':
                    related.append((a, b))
            elif bid.startswith('TC'):
                cid = it[2:]; c = byid[cid]
                conf.append({'confirmation': cid, 'deposit': c['deposit'], 'date': c.get('date'), 'quote': c['quote'],
                             'target_kind': d['target_kind'], 'links': d.get('links') or [],
                             'target_deposit': d.get('deposit'), 'external': d.get('external'), 'basis': d.get('basis'),
                             'batch': bid})
            elif bid.startswith('TR') and d['match'] in ('found', 'partial'):
                for fid in d.get('finds') or []:
                    alias[fid].append({'item': it, 'match': d['match'], 'batch': bid})
    groups = collections.defaultdict(list)
    for i in par:
        groups[g(i)].append(i)
    key = lambda i: (byid[i].get('date') or '9999', byid[i]['deposit'], i)
    claims, of = [], {}
    for mem in groups.values():
        mem.sort(key=key)
        first = byid[mem[0]]
        shapes = {byid[i]['shape'] for i in mem}
        tier = next(t for s, t in TIER if s in shapes)
        cid = 'PRED-' + mem[0][1:]
        for i in mem:
            of[i] = cid
        claims.append({'id': cid, 'tier': tier, 'shapes': sorted(shapes), 'registered': first.get('date'),
                       'registered_in': first['deposit'], 'title': titles.get(first['deposit']),
                       'statement': first['quote'], 'falsifier': first.get('falsifier_quote') or None,
                       'window': first.get('window') or None,
                       'statements': [{'find': i, 'deposit': byid[i]['deposit'], 'date': byid[i].get('date'),
                                       'lines': cur.get(i, {}).get('lines_now') or byid[i]['lines'], 'shape': byid[i]['shape'],
                                       **({'variant': variants[i]} if i in variants else {})} for i in mem],
                       'aliases': sorted({a['item'] for i in mem for a in alias.get(i, [])}),
                       'evidence': [], 'related': []})
    C = {c['id']: c for c in claims}
    for a, b in related:
        if a in of and b in of and of[a] != of[b]:
            C[of[a]]['related'].append(of[b]); C[of[b]]['related'].append(of[a])
    for a, b in contains:
        if a in of and b in of and of[a] != of[b]:
            C[of[a]].setdefault('contains', []).append(of[b]); C[of[b]].setdefault('in', []).append(of[a])
    for c in conf:
        for l in c['links']:
            t = of.get(l.get('find'))
            if t:
                C[t]['evidence'].append({'confirmation': c['confirmation'], 'deposit': c['deposit'], 'date': c['date'],
                                         'claimed': l.get('claimed')})
    for c in claims:
        c['related'] = sorted(set(c['related']))
        c['evidence'].sort(key=lambda e: e['date'] or '')
    claims.sort(key=lambda c: (c['registered'] or '9999', c['registered_in'], c['id']))
    by_tier = collections.Counter(c['tier'] for c in claims)
    summ = {'claims': len(claims), 'by_tier': dict(by_tier), 'multi_statement': sum(len(c['statements']) > 1 for c in claims),
            'with_evidence': sum(bool(c['evidence']) for c in claims), 'with_register_alias': sum(bool(c['aliases']) for c in claims),
            'confirmations': len(conf), 'held_out_gone': len(gone), 'batches_verified': sorted(done), 'batches_pending': pending}
    json.dump({'what': 'Claims of the prediction triage: the sweep\'s 6162 finds grouped into claims, each registered at its '
                       'earliest statement. Built by scripts/reading/triage_assemble.py from finds.jsonl, restatements.json '
                       'and the verified judgment batches; protocol data/reading/TRIAGE-PROTOCOL.md.',
               'summary': summ, 'held_out': gone, 'claims': claims}, open(T / 'claims.json', 'w'), ensure_ascii=False, indent=1)
    obs = [{'batch': bid, 'observation': o} for bid, out in sorted(done.items()) for o in out.get('observations') or []]
    json.dump({'what': 'Observations the triage readers recorded for a later pass, by batch.', 'observations': obs},
              open(T / 'observations.json', 'w'), ensure_ascii=False, indent=1)
    json.dump({'what': 'Confirmation records (shape C) and what each points back to, as judged in the TC batches.',
               'confirmations': conf}, open(T / 'confirmations.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(summ))


if __name__ == '__main__':
    main()
