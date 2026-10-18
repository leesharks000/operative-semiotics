#!/usr/bin/env python3
"""triage_currency.py — is each find still in its deposit's text? (2026-10-17)

The sweep read the texts of 2026-10-15 (sha256 per deposit in queue.json). The record repair of 2026-10-15/16 then
restored wrong bodies and missing parts in alexanarch, so some texts changed after they were read. For each find:
  current  the quote is in the current text at its recorded lines
  moved    the quote is in the current text at other lines (new lines recorded)
  gone     the quote is not in the current text — read from a body since replaced; kept, not assembled into claims
And for each deposit whose text changed since it was read: what changed, for a re-reading queue.
Matching is whitespace-normalized. USAGE  python3 scripts/reading/triage_currency.py
"""
import json, pathlib, hashlib, collections
ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'; T = R / 'triage'
norm = lambda s: ' '.join(s.split())


def main():
    meta = {}
    for b in json.load(open(R / 'queue.json'))['batches']:
        for d in b['deposits']:
            meta[d['deposit']] = d
    for d in json.load(open(T / 'deposit-titles.json')):
        if d['deposit'] not in meta and d.get('path'):
            meta[d['deposit']] = d  # read outside the queue; no sha recorded
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    ids = [json.loads(l)['id'] for l in open(T / 'finds.ids.jsonl')]
    texts = {}
    out, dep, jtexts = {}, collections.defaultdict(collections.Counter), {}
    for f, i in zip(F, ids):
        m = meta.get(f['deposit'])
        if not m or not pathlib.Path(m['path']).exists():
            out[i] = {'state': 'unchecked'}; continue
        if m['path'] not in texts:
            texts[m['path']] = pathlib.Path(m['path']).read_text(encoding='utf-8').split('\n')
        L = texts[m['path']]; q = norm(f['quote'])
        if m['path'].endswith('.json'):
            # #3 and #4 were read through their own-voice fields (derived texts); a quote is current if it is still in
            # one of the dataset's string values (TC12: F3.C19 and F3.C22 were wrongly marked gone)
            if m['path'] not in jtexts:
                vals = []
                def walk(x):
                    if isinstance(x, str): vals.append(x)
                    elif isinstance(x, dict): [walk(v) for v in x.values()]
                    elif isinstance(x, list): [walk(v) for v in x]
                walk(json.load(open(m['path'])))
                jtexts[m['path']] = norm('\n'.join(vals))
            st = {'state': 'current' if q in jtexts[m['path']] else 'gone', 'basis': 'dataset string values'}
            out[i] = st; dep[f['deposit']][st['state']] += 1
            continue
        a, z = f['lines']
        if q in norm('\n'.join(L[a - 1:z])):
            st = {'state': 'current'}
        elif q in norm('\n'.join(L)):
            first = norm(f['quote'].split('\n')[0])[:80]
            k = next((n for n, x in enumerate(L) if first and first in norm(x)), None)
            st = {'state': 'moved', 'lines_now': [k + 1, k + z - a + 1] if k is not None else None}
        else:
            st = {'state': 'gone'}
        out[i] = st; dep[f['deposit']][st['state']] += 1
    changed = []
    for n, m in meta.items():
        p = pathlib.Path(m['path'])
        if p.exists() and m.get('sha256') and hashlib.sha256(p.read_bytes()).hexdigest() != m.get('sha256'):
            L = p.read_text(encoding='utf-8').split('\n')
            changed.append({'deposit': n, 'title': m.get('title'), 'path': m['path'], 'lines_read': m.get('lines_total'),
                            'lines_now': len(L), 'words_now': sum(len(x.split()) for x in L),
                            'finds': dict(dep.get(n, {})), 'body_replaced': bool(dep.get(n)) and not dep[n]['current'] and not dep[n]['moved']})
    json.dump({'what': 'Currency of each sweep find against the current alexanarch texts, and the deposits whose text changed '
                       'after it was read. Built by scripts/reading/triage_currency.py.', 'finds': out,
               'changed_since_read': sorted(changed, key=lambda x: x['deposit'])},
              open(T / 'currency.json', 'w'), ensure_ascii=False, indent=0)
    c = collections.Counter(v['state'] for v in out.values())
    print(dict(c), 'changed texts', len(changed), 'bodies replaced', sum(x['body_replaced'] for x in changed),
          'words to re-read', sum(x['words_now'] for x in changed))


if __name__ == '__main__':
    main()
