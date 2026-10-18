#!/usr/bin/env python3
"""naming_queue.py — batches for naming the subject pages (2026-10-17). Each page carries every claim on it: id,
tier, registration date and deposit, the deposit's title and archive line, the statement (first 700 characters), and
the series it belongs to. Batches of 16 pages. Protocol: data/index/NAMING-PROTOCOL.md.
USAGE  python3 scripts/index/naming_queue.py
"""
import json, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parents[2]
T = ROOT / 'data/reading/triage'; I = ROOT / 'data/index'


def main():
    reg = {int(d['deposit_number']): d for d in json.load(open(ROOT.parent / 'alexanarch/data/registry.json'))['deposits']
           if d.get('deposit_number') is not None}
    C = {c['id']: c for c in json.load(open(T / 'claims.json'))['claims']}
    P = json.load(open(I / 'categories.json'))['pages']
    lines = sorted({d['line'] for d in reg.values() if d.get('line')})
    pages = []
    for p in P:
        pages.append({'page': p['page'], 'terms': p['terms'], 'claims': [
            {'claim': c, 'tier': C[c]['tier'], 'registered': C[c]['registered'], 'deposit': C[c]['registered_in'],
             'title': C[c].get('title'), 'line': reg.get(C[c]['registered_in'], {}).get('line'),
             'statements': len(C[c]['statements']), 'series': C[c].get('series', []),
             'statement': (C[c]['statement'] or '')[:700]} for c in p['claims']]})
    B = [{'batch_id': f'NM{n // 16 + 1:02d}', 'pages': pages[n:n + 16]} for n in range(0, len(pages), 16)]
    json.dump({'what': 'Naming batches for the subject pages of the prediction index. Built by scripts/index/naming_queue.py.',
               'lines': lines, 'all_pages': [p['page'] for p in P], 'batches': B}, open(I / 'naming-queue.json', 'w'),
              ensure_ascii=False, indent=1)
    print(len(pages), 'pages;', len(B), 'batches')


if __name__ == '__main__':
    main()
