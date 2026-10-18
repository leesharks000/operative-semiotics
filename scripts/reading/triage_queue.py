#!/usr/bin/env python3
"""triage_queue.py — the judgment batches of the prediction triage (2026-10-17).

Three kinds of item, each self-contained (the finds quoted in full, with deposit, date, title and text path):
  TC  a confirmation record (shape C): what it points back to — a find, a deposit with no find, something outside the
      archive, or unlocated — with the mechanical pointer resolution and up to six ranked candidate finds
  TE  a candidate pair (0.35 <= cosine < 0.85, different deposits): same claim, variant, related, or distinct
  TR  a register card (data/predictions.json) or an intake item (data/archive-intake.json): which finds state it
USAGE  python3 scripts/reading/triage_queue.py
"""
import json, pathlib, re
ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'; T = R / 'triage'
SIZE = {'TC': 30, 'TE': 50, 'TR': 32}


def main():
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    ids = [json.loads(l)['id'] for l in open(T / 'finds.ids.jsonl')]
    for f, i in zip(F, ids):
        f['id'] = i
    byid = {f['id']: f for f in F}
    q = json.load(open(R / 'queue.json'))
    meta = {}
    for b in q['batches']:
        for d in b['deposits']:
            meta[d['deposit']] = {'title': d.get('title'), 'date': d.get('date'), 'path': d.get('path'), 'lines_total': d.get('lines_total')}
    try:
        for b in json.load(open(R / 'xqueue.json'))['batches']:
            for d in b.get('deposits', [b]):
                if 'deposit' in d:
                    meta.setdefault(d['deposit'], {'title': d.get('title'), 'path': d.get('path')})
    except Exception:
        pass
    json.dump([{'deposit': k, **v} for k, v in sorted(meta.items())], open(T / 'deposit-titles.json', 'w'), ensure_ascii=False, indent=0)

    def card(i):
        f = byid[i]; m = meta.get(f['deposit'], {})
        return {'id': i, 'deposit': f['deposit'], 'date': f.get('date'), 'title': m.get('title'), 'path': m.get('path'),
                'shape': f['shape'], 'lines': f['lines'], 'quote': f['quote'], 'falsifier_quote': f.get('falsifier_quote'),
                'window': f.get('window'), 'points_to': f.get('points_to'), 'note': f.get('note')}
    items = {'TC': [], 'TE': [], 'TR': []}
    for p in json.load(open(T / 'pointers.json'))['pointers']:
        if p['shape'] != 'C':
            continue
        items['TC'].append({'item': 'C:' + p['id'], 'find': card(p['id']), 'resolved': [
            {'deposit': t['deposit'], 'how': t['how'], 'title': meta.get(t['deposit'], {}).get('title'),
             'path': meta.get(t['deposit'], {}).get('path'),
             'candidates': [dict(card(c['id']), score=c['score']) for c in t['candidates']]} for t in p['targets']]})
    for p in json.load(open(T / 'candidate-pairs.json'))['pairs']:
        items['TE'].append({'item': f"E:{p['a']}~{p['b']}", 'score': p['score'], 'a': card(p['a']), 'b': card(p['b'])})
    reg = json.load(open(ROOT / 'data/predictions.json'))['entries']
    for e in reg:
        srcs = sorted({int(x) for s in (e.get('sources') or []) for x in re.findall(r'#?(\d{1,4})\b', str(s)) if int(x) in meta})
        items['TR'].append({'item': 'R:' + e['id'], 'kind': 'register card', 'card': e, 'source_deposits': srcs,
                            'finds_in_sources': [card(f['id']) for f in F if f['deposit'] in srcs][:40]})
    intake = json.load(open(ROOT / 'data/archive-intake.json'))['predictions']
    for n, e in enumerate(intake):
        d = e.get('deposit')
        items['TR'].append({'item': f'I:{n:03d}', 'kind': 'intake item (2026-08-23)', 'card': e, 'source_deposits': [d] if d in meta else [],
                            'finds_in_sources': [card(f['id']) for f in F if f['deposit'] == d][:40]})
    batches = []
    for k, L in items.items():
        for n in range(0, len(L), SIZE[k]):
            batches.append({'batch_id': f'{k}{n // SIZE[k] + 1:02d}', 'kind': k, 'items': L[n:n + SIZE[k]]})
    json.dump({'what': 'Judgment batches of the prediction triage. Built by scripts/reading/triage_queue.py; protocol '
                       'data/reading/TRIAGE-PROTOCOL.md.', 'counts': {k: len(v) for k, v in items.items()},
               'batches': batches}, open(T / 'queue.json', 'w'), ensure_ascii=False, indent=1)
    print({k: len(v) for k, v in items.items()}, len(batches), 'batches:', ' '.join(b['batch_id'] for b in batches))


if __name__ == '__main__':
    main()
