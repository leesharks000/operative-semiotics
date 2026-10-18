#!/usr/bin/env python3
"""seat_recall.py — the recall audit's result, and its misses seated as finds (2026-10-18).

The adjudicators (RECALL-ADJUDICATE v1.0, batches J01–J07) judged every audit passage that overlaps no first-reading
find. A passage judged `missed` (and not `same_as` another) is a passage the protocol required and the first reading did
not record: it is appended to finds.jsonl as a find of its deposit (pass 'recall', run R-<J batch>), quoted verbatim from
the audit, so the index carries it. Measured recall over the sample = first-reading finds / (those + distinct misses);
passages both readings missed are not counted, so the figure is an upper bound on the sweep's recall.
Writes data/reading/recall-result.json. USAGE  python3.12 scripts/reading/seat_recall.py (once)
"""
import collections, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'; T = R / 'triage'


def main():
    if any(json.loads(l).get('pass') == 'recall' for l in open(R / 'finds.jsonl')):
        sys.exit('recall misses already seated')
    Q = {x['item']: x for b in json.load(open(R / 'recall-adjudicate-queue.json'))['batches'] for x in b['items']}
    reg = {int(d['deposit_number']): d for d in json.load(open(ROOT.parent / 'alexanarch/data/registry.json'))['deposits'] if d.get('deposit_number') is not None}
    V = collections.Counter(); miss = []
    for b in sorted({k for k in (f'J{n:02d}' for n in range(1, 8))}):
        for it in json.load(open(R / f'batches/{b}.json'))['items']:
            V[it['verdict']] += 1
            if it['verdict'] == 'missed' and not it.get('same_as'):
                miss.append((b, it))
    cmp_ = json.load(open(R / 'recall-compare.json'))
    first = cmp_['totals']['first']
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    cnt = collections.Counter((f['deposit'], f['shape']) for f in F)
    rows, idrows, seated = [], [], []
    for b, it in miss:
        q = Q[it['item']]; n = q['deposit']; sh = it['shape']
        cnt[(n, sh)] += 1; fid = f'F{n}.{sh}{cnt[(n, sh)]}'
        rows.append({'deposit': n, 'deposits': [n], 'date': reg.get(n, {}).get('date'), 'batch_id': b, 'run': f'R-{b}', 'pass': 'recall',
                     'path': q['path'], 'shape': sh, 'quote': q['quote'], 'lines': q['lines'], 'falsifier_quote': None, 'falsifier_lines': None,
                     'window': None, 'points_to': None, 'also_at': [], 'note': f"recall audit: {it.get('note')}", 'verified': True,
                     'verification_fails': [], 'seated_by': f"seat_recall.py from audit passage {it['item']}"})
        idrows.append({'id': fid, 'deposit': n, 'shape': sh, 'lines': q['lines']}); seated.append({'find': fid, 'item': it['item'], 'batch': b})
    with open(R / 'finds.jsonl', 'a') as o:
        for r in rows:
            o.write(json.dumps(r, ensure_ascii=False) + '\n')
    with open(T / 'finds.ids.jsonl', 'a') as o:
        for r in idrows:
            o.write(json.dumps(r) + '\n')
    res = {'what': 'Recall audit result (2026-10-18): 40 random deposits, a second reading on a different brief by a different model, and adjudication of every audit passage overlapping no first-reading find.',
           'sample': {'deposits': len(cmp_['deposits']), 'words': sum(d['words'] for d in cmp_['deposits']), 'seed': json.load(open(R / 'recall-queue.json'))['seed']},
           'second_reading': {'reader': 'general-purpose subagent, model sonnet (the first reading: inherited model)', 'brief': 'RECALL-BRIEF v1.0', 'passages': cmp_['totals']['audit']},
           'comparison': cmp_['totals'], 'adjudication': dict(V), 'distinct_misses': len(miss),
           'misses_by_shape': dict(collections.Counter(it['shape'] for _, it in miss)),
           'recall': {'first_reading_finds': first, 'value': round(first / (first + len(miss)), 3),
                      'definition': 'first-reading finds / (first-reading finds + distinct passages the protocol required that only the second reading found); passages both readings missed are not counted'},
           'agreement': {'first_reading_finds_overlapped_by_second_reading': cmp_['rates']['first_reading_finds_also_found_by_audit']},
           'seated': seated}
    (R / 'recall-result.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n')
    print(json.dumps({k: res[k] for k in ('adjudication', 'distinct_misses', 'misses_by_shape', 'recall')}))


if __name__ == '__main__':
    main()
