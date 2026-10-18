#!/usr/bin/env python3
"""triage_entry_dates.py — the date of a find in a data deposit is its record's date, not the file's (2026-10-17).

#3 (the Capture Registry) and #4 are datasets versioned in place; the sweep gave their finds the deposit's date
(2026-06-17 for #3), so a reading written in October was registered in June (topical readers, TP07 and TP11). Their
finds were quoted from the derived own-voice texts (data/reading/derived/000N-voice.md), where each block is headed
'## record <n> · <id> · source line <l> · <date> · …'. A find's date is the date in the heading of the block that holds
its quote. Writes triage/entry-dates.json {find id: {date, record}}; triage_assemble.py applies it.
USAGE  python3 scripts/reading/triage_entry_dates.py
"""
import json, re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'; T = R / 'triage'
HEAD = re.compile(r'^## record \d+ · (\S+) · source line \d+ · (\d{4}-\d{2}-\d{2})')
norm = lambda s: ' '.join(s.split())


def main():
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    ids = [json.loads(l)['id'] for l in open(T / 'finds.ids.jsonl')]
    out, miss = {}, []
    for dep in (3, 4):
        p = R / f'derived/{dep:04d}-voice.md'
        L = p.read_text(encoding='utf-8').split('\n')
        head = [None] * len(L); cur = None
        for n, x in enumerate(L):
            m = HEAD.match(x)
            if m:
                cur = (m.group(2), m.group(1))
            elif x.startswith('## '):
                cur = None
            head[n] = cur
        for f, i in zip(F, ids):
            if f['deposit'] != dep:
                continue
            a, z = f['lines']; q = norm(f['quote'])
            if not (0 < a <= len(L)) or q[:60] not in norm('\n'.join(L[a - 1:z + 1])):
                miss.append(i); continue
            h = head[a - 1]
            if h:
                out[i] = {'date': h[0], 'record': h[1]}
            else:
                miss.append(i)
    json.dump({'what': 'Dates of finds in the data deposits #3 and #4, from the heading of the record block holding the quote '
                       'in the derived own-voice text. Built by scripts/reading/triage_entry_dates.py.',
               'dates': out, 'unresolved': miss}, open(T / 'entry-dates.json', 'w'), ensure_ascii=False, indent=0)
    print(len(out), 'dated by record;', len(miss), 'unresolved (top-level fields or quote not at its lines)')


if __name__ == '__main__':
    main()
