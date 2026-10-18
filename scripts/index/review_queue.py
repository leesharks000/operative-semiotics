#!/usr/bin/env python3
"""review_queue.py — the subject pages as they stand after the naming moves, for the review pass (2026-10-17).
Pages come from build_index.page_members (categories.json + verified naming batches, moves placed as it says); each
carries its current title/description/line, the naming reader's note, every claim (700-character statement) and the
claims moved in. Batches of 16. Protocol: data/index/REVIEW-PROTOCOL.md.
USAGE  python3 scripts/index/review_queue.py
"""
import json, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts/index'))
import build_index as B
I = ROOT / 'data/index'


def main():
    reg, C, F, S, conf, P, names = B.load()
    byid = {c['id']: c for c in C}
    mem = B.page_members(P, names, C)
    orig = {p['page']: set(p['claims']) for p in P}
    lines = sorted({d['line'] for d in reg.values() if d.get('line')})
    pages = []
    for p in P:
        pid = p['page']; n = names.get(pid, {})
        pages.append({'page': pid, 'title': n.get('title'), 'slug': n.get('slug'), 'description': n.get('description'),
                      'line': n.get('line'), 'naming_note': n.get('note'),
                      'moved_in': sorted(set(mem[pid]) - orig[pid]),
                      'claims': [{'claim': c, 'tier': byid[c]['tier'], 'registered': byid[c]['registered'],
                                  'deposit': byid[c]['registered_in'], 'title': byid[c].get('title'),
                                  'series': byid[c].get('series', []), 'statement': (byid[c]['statement'] or '')[:700]}
                                 for c in mem[pid]]})
    Bt = [{'batch_id': f'RV{n // 16 + 1:02d}', 'pages': pages[n:n + 16]} for n in range(0, len(pages), 16)]
    json.dump({'what': 'Review batches: the subject pages after the naming moves. Built by scripts/index/review_queue.py.',
               'lines': lines, 'batches': Bt}, open(I / 'review-queue.json', 'w'), ensure_ascii=False, indent=1)
    print(len(pages), 'pages;', len(Bt), 'batches; named', sum(1 for p in pages if p['title']))


if __name__ == '__main__':
    main()
