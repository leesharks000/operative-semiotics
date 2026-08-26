#!/usr/bin/env python3
"""Notebook X build — regenerate manifest from plates/ and seams/, extend the arrival
ordering with anything new, and render. One command per accretion."""
import json, glob, os, subprocess, sys
D = os.path.dirname(os.path.abspath(__file__))
def fm(p):
    t = open(p).read(); block = t.split('---')[1]; d = {}
    for line in block.strip().split('\n'):
        if ':' in line:
            k, v = line.split(':', 1); v = v.strip()
            if v.startswith('['): v = [x.strip() for x in v.strip('[]').split(',') if x.strip()]
            d[k.strip()] = v
    return d
M = json.load(open(f'{D}/manifest.json'))
M['plates'] = []; M['seams'] = []
for p in sorted(glob.glob(f'{D}/plates/*.md')):
    d = fm(p); d['file'] = '/texts/notebook-x/plates/' + os.path.basename(p); M['plates'].append(d)
for p in sorted(glob.glob(f'{D}/seams/*.md')):
    d = fm(p); d['file'] = '/texts/notebook-x/seams/' + os.path.basename(p); M['seams'].append(d)
ids = [p['plate'] for p in M['plates']]
for op in glob.glob(f'{D}/orders/*.json'):
    o = json.load(open(op))
    missing = [i for i in ids if i not in o['sequence']]
    if missing:
        o['sequence'] += missing          # new plates append; existing order untouched
        json.dump(o, open(op, 'w'), indent=1)
        print(f"  {os.path.basename(op)}: +{len(missing)}")
json.dump(M, open(f'{D}/manifest.json', 'w'), ensure_ascii=False, indent=1)
print(f"manifest: {len(M['plates'])} plates, {len(M['seams'])} seams")
subprocess.run([sys.executable, f'{D}/render.py'] + sys.argv[1:])
