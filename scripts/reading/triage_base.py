#!/usr/bin/env python3
"""triage_base.py — the mechanical layer of the prediction triage (2026-10-17).

Lee Sharks, 2026-10-17: "lets do the triage pass." The sweep (finds.jsonl, 6162 verified finds, 1616 deposits read)
recorded every prediction-bearing passage; the protocol leaves to triage the linking of a thesis repeated across
deposits and of each confirmation record to what it points back to. This script does only what can be done without
judgment, and writes it as data for the judgment passes:

  find ids     F<deposit>.<shape><n> — n is the find's order among that deposit's finds of that shape in finds.jsonl
  pointers     for each shape-C find (and any find whose points_to names a record), the deposits its points_to names:
               by number (#N, deposit N), DOI (10.5281/zenodo.N), AXN hex, or quoted title; 'this deposit/same text' = self
  candidates   for each resolved pointer, the finds of shapes A B D E F G H in the target deposit, ranked by word overlap
               with the C find's quote — candidates only; the judgment pass chooses

USAGE  python3 scripts/reading/triage_base.py --registry <alexanarch>/data/registry.json
"""
import json, re, sys, pathlib, collections, math
ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / 'data/reading'
OUT = R / 'triage'
WORD = re.compile(r"[a-z][a-z'\-]{2,}")
STOP = set("the and for that this with from are was were has have its not but which into they their them than then what when where who will would can could been being also only such these those there here over under more most other about after before between each every some any all one two our out his her him she you your yes per via may might must shall should".split())


def toks(s):
    return [w for w in WORD.findall((s or '').lower()) if w not in STOP]


def norm_title(t):
    return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()


def main():
    reg = json.load(open(sys.argv[sys.argv.index('--registry') + 1]))['deposits']
    by_doi, by_hex, by_title = {}, {}, {}
    for d in reg:
        n = d.get('deposit_number')
        if n is None:
            continue
        n = int(n)
        for k in ('zenodo_dois', 'legacy_doi', 'original_doi'):
            v = d.get(k)
            for x in (v if isinstance(v, list) else [v]):
                m = re.search(r'zenodo\.(\d+)', str(x or ''))
                if m:
                    by_doi.setdefault(m.group(1), n)
        if d.get('hex'):
            by_hex.setdefault(d['hex'].upper(), n)
        t = norm_title(d.get('title'))
        if len(t) > 12:
            by_title.setdefault(t, n)
            by_title.setdefault(norm_title(t.split(':')[0]), n) if len(norm_title(t.split(':')[0])) > 12 else None
    F = [json.loads(l) for l in open(R / 'finds.jsonl')]
    cnt = collections.Counter()
    for f in F:
        cnt[(f['deposit'], f['shape'])] += 1
        f['id'] = f"F{f['deposit']}.{f['shape']}{cnt[(f['deposit'], f['shape'])]}"
    by_dep = collections.defaultdict(list)
    for f in F:
        by_dep[f['deposit']].append(f)
    df = collections.Counter()
    for f in F:
        df.update(set(toks(f['quote'])))
    N = len(F)

    def sim(a, b):
        A, B = set(toks(a)), set(toks(b))
        if not A or not B:
            return 0.0
        w = lambda x: math.log(N / (1 + df[x]))
        inter = sum(w(x) for x in A & B)
        return round(inter / math.sqrt(sum(w(x) for x in A) * sum(w(x) for x in B)), 3)

    ptr = []
    for f in F:
        p = f.get('points_to') or ''
        if f['shape'] != 'C' and not re.search(r'#\d+|zenodo\.\d+|AXN:', p):
            continue
        hits = {}
        for m in re.finditer(r'(?:#|deposit\s+|EA-\S+\s+#)(\d{1,4})\b', p):
            hits.setdefault(int(m.group(1)), 'number')
        for m in re.finditer(r'zenodo\.(\d+)', p):
            if m.group(1) in by_doi:
                hits.setdefault(by_doi[m.group(1)], 'doi')
        for m in re.finditer(r'AXN:([0-9A-Fa-f]{4})', p):
            if m.group(1).upper() in by_hex:
                hits.setdefault(by_hex[m.group(1).upper()], 'axn')
        for m in re.finditer(r'["“\'‘*_]{1,2}([^"”\'’*_]{8,160})["”\'’*_]{1,2}', p):
            t = norm_title(m.group(1))
            if t in by_title:
                hits.setdefault(by_title[t], 'title')
        if re.search(r'\b(this|same) (deposit|text|paragraph|document|paper|section)\b|\bthis same\b', p, re.I):
            hits.setdefault(f['deposit'], 'self')
        targets = []
        for n, how in hits.items():
            cands = [g for g in by_dep.get(n, []) if g['shape'] != 'C' and g['id'] != f['id']]
            cands = sorted(({'id': g['id'], 'score': sim(f['quote'] + ' ' + p, g['quote'])} for g in cands),
                           key=lambda c: -c['score'])[:6]
            targets.append({'deposit': n, 'how': how, 'readable': n in by_dep or n in {d for d in by_dep}, 'candidates': cands})
        ptr.append({'id': f['id'], 'deposit': f['deposit'], 'date': f.get('date'), 'shape': f['shape'],
                    'points_to': p, 'targets': targets})
    OUT.mkdir(exist_ok=True)
    with open(OUT / 'finds.ids.jsonl', 'w') as o:
        for f in F:
            o.write(json.dumps({'id': f['id'], 'deposit': f['deposit'], 'shape': f['shape'], 'lines': f['lines']}) + '\n')
    json.dump({'what': 'Pointers of the prediction triage: what each confirmation record (and any find naming a record) '
                       'points back to, resolved mechanically, with ranked candidate finds in the target. Built by '
                       'scripts/reading/triage_base.py; candidates are for the judgment pass, not links.',
               'pointers': ptr}, open(OUT / 'pointers.json', 'w'), ensure_ascii=False, indent=1)
    C = [x for x in ptr if x['shape'] == 'C']
    hows = collections.Counter(t['how'] for x in ptr for t in x['targets'])
    print(f"finds {N}; pointer records {len(ptr)} (C {len(C)}); C resolved {sum(1 for x in C if x['targets'])}; "
          f"C external/unresolved {sum(1 for x in C if not x['targets'])}; resolved by {dict(hows)}")


if __name__ == '__main__':
    main()
