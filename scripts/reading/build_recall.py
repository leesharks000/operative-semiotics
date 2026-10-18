#!/usr/bin/env python3
"""build_recall.py — the recall audit sample (2026-10-18; Kimi's review, adopted by Lee Sharks: "adopted on all").

Forty deposits drawn at random (seed 20261018) from the first reading's queue, re-read in full by a second reader on a
differently worded brief (data/reading/RECALL-BRIEF.md) that names no shapes. compare_recall.py then sets the two
readings side by side. Deposits whose seated text is a derived own-voice text are drawn on the same footing.
USAGE  python3.12 scripts/reading/build_recall.py
"""
import hashlib, json, pathlib, random

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'
SEED, N, WORDS = 20261018, 40, 40000


def main():
    rows = [r for b in json.load(open(R / 'queue.json'))['batches'] for r in b['deposits']]
    rows = sorted({r['deposit']: r for r in rows}.values(), key=lambda r: r['deposit'])
    pick = sorted(random.Random(SEED).sample(rows, N), key=lambda r: -r['words'])
    units = []
    for r in pick:
        p = pathlib.Path(r['path']); raw = p.read_bytes()
        units.append({'deposit': r['deposit'], 'title': r['title'], 'path': str(p), 'lines_total': raw.decode('utf-8', 'replace').count('\n') + 1,
                      'words': len(raw.decode('utf-8', 'replace').split()), 'sha256': hashlib.sha256(raw).hexdigest(),
                      'sha256_first_reading': r['sha256']})
    batches, cur, w = [], [], 0
    for u in units:  # largest first; fill to ~WORDS per batch
        if cur and w + u['words'] > WORDS:
            batches.append(cur); cur, w = [], 0
        cur.append(u); w += u['words']
    if cur:
        batches.append(cur)
    out = {'what': 'recall audit: 40 random deposits re-read in full on a different brief', 'seed': SEED, 'population': len(rows),
           'words': sum(u['words'] for u in units),
           'batches': [{'batch_id': f'K{n + 1:02d}', 'words': sum(u['words'] for u in b), 'deposits': b} for n, b in enumerate(batches)]}
    (R / 'recall-queue.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    print(len(units), 'deposits', out['words'], 'words', len(batches), 'batches', [b['words'] for b in out['batches']])


if __name__ == '__main__':
    main()
