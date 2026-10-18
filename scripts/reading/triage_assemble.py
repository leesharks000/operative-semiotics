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


def topical(claims, C, T, byid):
    """The topical pass (TOPICAL-PROTOCOL v1.0): 'same' and 'states' sets merge claims into one, registered at the
    earliest; 'states' keeps the claims' order and changes as dated states; 'series' links distinct claims by name."""
    sets = []
    for v in sorted(glob.glob(str(T / 'topical/T[PJM]*.verified.json'))):
        if json.load(open(v)).get('verified'):
            out = json.load(open(v.replace('.verified.json', '.json')))
            for g in out['groups']:
                for st in g.get('sets') or []:
                    sets.append(dict(st, batch=out['batch_id']))
    # a topical set names claims by the id they had when the topical queue was built: PRED-<find id of the earliest
    # statement>. Re-dating can make another statement earliest, so a member is resolved through its find.
    by_find = {st['find']: c['id'] for c in claims for st in c['statements']}
    res = lambda i: by_find.get('F' + i[5:], i) if i.startswith('PRED-') else i
    for st in sets:
        st['claims'] = list(dict.fromkeys(res(i) for i in st['claims']))
    par = {c['id']: c['id'] for c in claims}

    def g(i):
        while par[i] != i:
            par[i] = par[par[i]]; i = par[i]
        return i
    for st in sets:
        if st['kind'] in ('same', 'states'):
            ids = [i for i in st['claims'] if i in par]
            for i in ids[1:]:
                par[g(i)] = g(ids[0])
    comp = collections.defaultdict(list)
    for c in claims:
        comp[g(c['id'])].append(c)
    key = lambda c: (c['registered'] or '9999', c['registered_in'], c['id'])
    new, to = [], {}
    for mem in comp.values():
        mem.sort(key=key); base = mem[0]
        for m in mem:
            to[m['id']] = base['id']
        if len(mem) > 1:
            base = dict(base)
            base['merged'] = [m['id'] for m in mem[1:]]
            base['statements'] = sorted([s for m in mem for s in m['statements']], key=lambda s: (s['date'] or '9999', s['deposit']))
            base['shapes'] = sorted({x for m in mem for x in m['shapes']})
            base['tier'] = next(t for sh, t in TIER if sh in base['shapes'])
            for k in ('aliases', 'flags'):
                base[k] = sorted({x for m in mem for x in m.get(k) or []})
            for k in ('evidence', 'related', 'contains', 'in'):
                base[k] = [x for m in mem for x in m.get(k) or []]
        new.append(base)
    reg = {c['id']: c['registered'] for c in claims}
    for st in sets:
        if st['kind'] == 'states':
            b = next(c for c in new if c['id'] == to[st['claims'][0]])
            ch = st.get('change') or []
            rows = [{'claim': i, 'registered': reg.get(i), 'read_order': n + 1,
                     'change': ch[n - 1] if n and n - 1 < len(ch) else None} for n, i in enumerate(st['claims'])]
            # states are ordered by registration date (Lee Sharks, 2026-10-17: "we go by registration date"); each
            # claim keeps the change the reader wrote for the step into it, and the reader's order as read_order
            b['states'] = sorted(rows, key=lambda r: (r['registered'] or '9999', r['read_order']))
    series = []
    for st in sets:
        if st['kind'] == 'series':
            mem = sorted({to.get(i, i) for i in st['claims']})
            series.append({'name': st.get('name'), 'claims': mem, 'basis': st.get('basis'), 'batch': st['batch']})
    merged = {}  # one series per name: a later pass extends a series by reusing its name (JOIN-PROTOCOL)
    for x in series:
        m = merged.setdefault(x['name'], {'name': x['name'], 'claims': [], 'basis': [], 'batches': []})
        m['claims'] = sorted(set(m['claims']) | set(x['claims'])); m['basis'].append(x['basis']); m['batches'].append(x['batch'])
    series = sorted(merged.values(), key=lambda x: x['name'] or '')
    names = collections.defaultdict(list)
    for x in series:
        for i in x['claims']:
            names[i].append(x['name'])
    for c in new:
        for k in ('related', 'contains', 'in'):
            if c.get(k):
                c[k] = sorted({to.get(i, i) for i in c[k]} - {c['id']})
        if names.get(c['id']):
            c['series'] = sorted(set(names[c['id']]))
    json.dump({'what': 'Series of the topical pass: distinct claims linked as one programme, battery or template.',
               'series': series}, open(T / 'series.json', 'w'), ensure_ascii=False, indent=1)
    return new, series


def main():
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    for f, l in zip(F, open(T / 'finds.ids.jsonl')):
        f['id'] = json.loads(l)['id']
    byid = {f['id']: f for f in F}
    titles = {d['deposit']: d.get('title') for d in json.load(open(T / 'deposit-titles.json'))}
    dates = {d['deposit']: d.get('date') for d in json.load(open(T / 'deposit-titles.json'))}
    ed = (json.load(open(T / 'entry-dates.json'))['dates'] if (T / 'entry-dates.json').exists() else {})
    # a deposit's date is the registry's current date (dates repaired 2026-10-17 to the date the text states:
    # alexanarch scripts/repair_dates_from_text_20261017.py); the sweep recorded the dates of 2026-10-15
    A = ROOT.parent / 'alexanarch/data/registry.json'
    if A.exists():
        cur = {int(d['deposit_number']): d.get('date') for d in json.load(open(A))['deposits'] if d.get('deposit_number') is not None}
        for f in F:
            if cur.get(f['deposit']):
                f['date'] = cur[f['deposit']]
        for k in list(dates):
            dates[k] = cur.get(k) or dates[k]
    for f in F:  # a find in a data deposit (#3, #4) is dated by its record, not by the file (triage_entry_dates.py)
        if f['id'] in ed:
            f['date'] = ed[f['id']]['date']; f['record'] = ed[f['id']]['record']
    for f in F:  # finds of deposits read outside the queue carry no date: the registry's
        if not f.get('date'):
            f['date'] = dates.get(f['deposit'])
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
        flags = []
        if first.get('date') == '2026-01-01':
            flags.append('registered on 2026-01-01, a date several readers found to be a placeholder (#1238, #1242, #1243, #1249)')
        claims.append({'id': cid, 'tier': tier, 'flags': flags, 'shapes': sorted(shapes), 'registered': first.get('date'),
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
    claims, series = topical(claims, C, T, byid)
    claims.sort(key=lambda c: (c['registered'] or '9999', c['registered_in'], c['id']))
    by_tier = collections.Counter(c['tier'] for c in claims)
    summ = {'claims': len(claims), 'merged_by_topical': sum(len(c.get('merged') or []) for c in claims),
            'with_states': sum(bool(c.get('states')) for c in claims), 'series': len(series), 'by_tier': dict(by_tier), 'multi_statement': sum(len(c['statements']) > 1 for c in claims),
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
