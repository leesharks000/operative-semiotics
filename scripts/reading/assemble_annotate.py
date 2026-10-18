#!/usr/bin/env python3
"""assemble_annotate.py — the verified annotation batches (N*.json) gathered into data/reading/triage/annotations.json.

Only batches whose .verified.json shows no failing item are taken. Per claim: the readers' dates per statement, mode, and
falsifier kind. The index build (scripts/index/build_index.py) applies them; this script changes no claim.
USAGE  python3.12 scripts/reading/assemble_annotate.py
"""
import collections, glob, json, pathlib, re, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from build_annotate import norm_map, nq, paths

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'; T = R / 'triage'


def main():
    Q = json.load(open(R / 'annotate-queue.json'))
    want = {b['batch_id'] for b in Q['batches']}
    out, used, open_b = {}, [], []
    for b in sorted(want):
        p = R / f'batches/{b}.json'; v = R / f'batches/{b}.verified.json'
        if not p.exists() or not v.exists() or json.load(open(v))['summary']['items_with_fails']:
            open_b.append(b); continue
        o = json.load(open(p)); used.append(b)
        for it in o['items']:
            a = {'batch': b}
            if 'dates' in it:
                a['dates'] = {d['find']: {k: d.get(k) for k in ('stated', 'stated_basis', 'basis_quote', 'basis_lines', 'retrospective', 'looks_back_to', 'note')}
                              for d in it['dates']['statements']}
            if 'mode' in it:
                a['mode'] = {k: it['mode'].get(k) for k in ('mode', 'fulfilment', 'basis_quote', 'basis_lines', 'basis_path', 'note')}
            if 'falsifier' in it:
                a['falsifier'] = {k: it['falsifier'].get(k) for k in ('kind', 'quote', 'lines', 'path', 'reader_condition', 'note')}
            out[it['claim']] = a
    cnt = collections.Counter()
    for a in out.values():
        for d in (a.get('dates') or {}).values():
            cnt['basis:' + str(d['stated_basis'])] += 1; cnt['retrospective'] += bool(d['retrospective'])
        if 'mode' in a:
            cnt['mode:' + a['mode']['mode']] += 1
        if 'falsifier' in a:
            cnt['falsifier:' + a['falsifier']['kind']] += 1
    # mechanical: a find quoted from a derived own-voice text (data/reading/derived/*.md) is dated by the record heading it
    # sits under ("## record N · id · source line L · YYYY-MM-DD"), not by the dataset deposit's date
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    ids = [json.loads(l)['id'] for l in open(T / 'finds.ids.jsonl')]
    P = paths(); heads = {}; mech = {}
    HD = re.compile(r'^## record \d+ · (.+?) · source line \d+ · (\d{4}-\d{2}-\d{2})')
    for fid, f in zip(ids, F):
        p = f.get('path') or P.get(f['batch_id'], {}).get(f['deposit']) or P['*'].get(f['deposit'])
        if not p or '/data/reading/derived/' not in p:
            continue
        if p not in heads:
            t = pathlib.Path(p).read_text(encoding='utf-8', errors='replace')
            hl = [(n + 1, m.group(1), m.group(2)) for n, l in enumerate(t.split('\n')) for m in [HD.match(l)] if m]
            heads[p] = (norm_map(t), hl)
        (nt, ln), hl = heads[p]
        i = nt.find(nq(f['quote']))
        if i < 0:
            continue
        L = ln[i]; h = [x for x in hl if x[0] <= L]
        if h:
            mech[fid] = {'stated': h[-1][2], 'stated_basis': 'in-text', 'basis': f'record heading, line {h[-1][0]}: {h[-1][1]}',
                         'retrospective': None, 'by': 'assemble_annotate.py (mechanical)'}
    cnt['mechanical_record_dates'] = len(mech)
    res = {'what': 'Readers\' annotations (ANNOTATION-PROTOCOL v1.0): statement dates, E modes, standing-claim falsifier kinds. Applied by build_index.py.',
           'batches_used': used, 'batches_open': open_b, 'claims': len(out), 'record_dates': mech, 'counts': dict(sorted(cnt.items())), 'annotations': out}
    (T / 'annotations.json').write_text(json.dumps(res, ensure_ascii=False, indent=1) + '\n')
    print(len(used), 'batches;', len(out), 'claims; open:', open_b); print(json.dumps(res['counts']))


if __name__ == '__main__':
    main()
