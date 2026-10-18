#!/usr/bin/env python3
"""build_describe.py — the describe pass queue (DESCRIBE-PROTOCOL v1.0): every subject page with its claims.
USAGE  python3.12 scripts/index/build_describe.py
"""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
I = ROOT / 'data/index'


def main():
    toc = json.load(open(ROOT / 'predictions/index.json'))['pages']
    recs = {}
    for t in toc:
        r = json.load(open(ROOT / f"predictions/{t['slug']}/record.json"))
        recs[t['page']] = r
    pages = []
    for t in toc:
        r = recs[t['page']]
        pages.append({'page': t['page'], 'title': t['title'], 'description': t['description'], 'line': t['line'],
                      'claims': [{'id': c['id'], 'tier': c['tier'], 'registered': c['registered'], 'registered_in': c['registered_in'],
                                  'registered_title': (c.get('registered_title') or '')[:140], 'statement': (c['statement'] or '')[:420],
                                  'states': [{k: s.get(k) for k in ('claim', 'registered', 'change')} for s in c.get('states') or []]}
                                 for c in r['claims']]})
    per = 20
    out = {'what': 'describe pass: every subject page with its claims (DESCRIBE-PROTOCOL v1.0)',
           'batches': [{'batch_id': f'DS{i // per + 1:02d}', 'pages': pages[i:i + per]} for i in range(0, len(pages), per)]}
    (I / 'describe-queue.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    print(len(pages), 'pages', len(out['batches']), 'batches')


if __name__ == '__main__':
    main()
