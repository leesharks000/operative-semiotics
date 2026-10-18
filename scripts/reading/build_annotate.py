#!/usr/bin/env python3
"""build_annotate.py — the annotation pass queue (2026-10-18), on the two reviews of the draft deposit.

Three questions the first reading did not ask, put to readers claim by claim (data/reading/ANNOTATION-PROTOCOL.md):
  dates      when was the quoted passage stated, and does it look back on something earlier?
             (every priority record; and every claim one of whose quotes reads as a look-back by the RETRO pattern)
  mode       what kind of anticipation is a speculative specification (every claim with an E statement)
  falsifier  is there a stated falsifying condition for a standing claim recorded without one

Each statement is located again in its source file as it stands now (the quote is searched for in the normalised
text and its current line range recorded), so a reader opens the right lines even where repairs shifted them.
USAGE  python3.12 scripts/reading/build_annotate.py
"""
import collections, hashlib, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'; T = R / 'triage'
RETRO = re.compile(r"years (before|earlier|ago|prior)|would (later )?become|anticipat|prefigur|foresaw|forecast(ed)? in|predicted|"
                   r"earliest|first (appear|stat|record)|already (in|stated)|before the archive|retrospect|in hindsight|long before|"
                   r"decade before|had (already )?(stated|written|predicted)", re.I)
PER = 30


def norm_map(t):
    """normalised text plus, for each normalised char, the source line it came from"""
    out, ln, line, sp = [], [], 1, False
    for ch in t.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"'):
        if ch.isspace():
            if not sp and out:
                out.append(' '); ln.append(line); sp = True
            if ch == '\n':
                line += 1
            continue
        out.append(ch); ln.append(line); sp = False
    return ''.join(out), ln


def nq(s):
    return re.sub(r"\s+", " ", s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')).strip()


def paths():
    """batch id -> deposit -> path, for every queue the first reading used"""
    P = collections.defaultdict(dict)
    for b in json.load(open(R / 'queue.json'))['batches']:
        for r in b['deposits']:
            P[b['batch_id']][r['deposit']] = r['path']; P['*'][r['deposit']] = r['path']
    for b in json.load(open(R / 'xqueue.json'))['batches']:
        P[b['batch_id']][b['deposit']] = b['path']
    for b in json.load(open(R / 'hpass.json'))['batches']:
        for r in b['deposits']:
            P[b['batch_id']][r['deposit']] = r['path']
    for r in json.load(open(R / 'calibration-batch.json'))['deposits']:
        P['CAL'][r['deposit']] = r['path']
    return P


def main():
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    ids = [json.loads(l)['id'] for l in open(T / 'finds.ids.jsonl')]
    by = dict(zip(ids, F))
    C = json.load(open(T / 'claims.json'))['claims']
    P = paths(); cache = {}

    def locate(fid):
        f = by[fid]
        p = f.get('path') or P.get(f['batch_id'], {}).get(f['deposit']) or P['*'].get(f['deposit'])
        if not p or not pathlib.Path(p).exists():
            return p, None
        if p not in cache:
            raw = pathlib.Path(p).read_bytes()
            cache[p] = (norm_map(raw.decode('utf-8', 'replace')), hashlib.sha256(raw).hexdigest(), raw.decode('utf-8', 'replace').count('\n') + 1)
        (nt, ln), sha, tot = cache[p]
        q = nq(f['quote']); i = nt.find(q)
        if i < 0:
            return p, None
        return p, [ln[i], ln[i + len(q) - 1]]

    items = []; miss = []
    for c in C:
        tasks = []
        if c['tier'] == 'priority record' or any(RETRO.search(by[s['find']]['quote']) for s in c['statements'] if s['find'] in by):
            tasks.append('dates')
        if 'E' in c['shapes']:
            tasks.append('mode')
        if c['tier'] == 'standing claim' and not c.get('falsifier') and not any(by.get(s['find'], {}).get('falsifier_quote') for s in c['statements']):
            tasks.append('falsifier')
        if not tasks:
            continue
        sts = []
        for s in c['statements']:
            if s['find'] not in by:
                continue
            f = by[s['find']]; p, now = locate(s['find'])
            if now is None:
                miss.append(s['find'])
            sts.append({'find': s['find'], 'deposit': s['deposit'], 'date': s.get('date'), 'shape': f['shape'], 'path': p,
                        'sha256': cache[p][1] if p in cache else None, 'lines_total': cache[p][2] if p in cache else None,
                        'lines_now': now, 'quote': f['quote'], 'falsifier_quote': f.get('falsifier_quote'), 'window': f.get('window'),
                        'retro_pattern': bool(RETRO.search(f['quote']))})
        items.append({'claim': c['id'], 'tier': c['tier'], 'registered': c['registered'], 'title': c.get('title'), 'tasks': tasks,
                      'statements': sts})
    items.sort(key=lambda x: (x['statements'][0]['deposit'] if x['statements'] else 0, x['claim']))
    batches = [{'batch_id': f'N{n // PER + 1:03d}', 'items': items[n:n + PER]} for n in range(0, len(items), PER)]
    cnt = collections.Counter(t for x in items for t in x['tasks'])
    out = {'what': 'annotation pass: dates, mode and falsifier questions put claim by claim (ANNOTATION-PROTOCOL.md)',
           'built': 'build_annotate.py', 'counts': {'claims': len(items), 'by_task': dict(cnt), 'statements': sum(len(x['statements']) for x in items),
                                                   'not_relocated': len(miss), 'batches': len(batches)},
           'not_relocated': miss, 'batches': batches}
    (R / 'annotate-queue.json').write_text(json.dumps(out, ensure_ascii=False, indent=1) + '\n')
    print(json.dumps(out['counts']))


if __name__ == '__main__':
    main()
