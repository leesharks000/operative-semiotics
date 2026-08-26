#!/usr/bin/env python3
"""Compile Notebook X into one flat markdown file from any ordering — a cut."""
import json, os, sys, datetime
D = os.path.dirname(os.path.abspath(__file__))
oid = sys.argv[1] if len(sys.argv)>1 else 'arrival'
M = json.load(open(f'{D}/manifest.json'))
order = json.load(open(f'{D}/orders/{oid}.json'))
by = {p['plate']: p for p in M['plates']}
def body(path):
    t = open(D + '/' + path.replace('/texts/notebook-x/','')).read()
    return t.split('---',2)[2].strip() if t.startswith('---') else t.strip()
out = [f"""# OPERATIVE SEMIOTICS: A GRUNDRISSE — NOTEBOOK X: THE GATE

**A workshop, not a treatise. Open and accreting.**
Johannes Sigil (Lee Sharks), with the Assembly · opened 2026-08-26 · cut of {datetime.date.today()} · ordering: **{order['name']}**
{len(M['plates'])} plates · {len(M['seams'])} seams · live at operativesemiotics.org/texts/notebook-x/

> **Synthesis status: asynthetic by declaration.** No synthesis has been performed across these plates. Seams are unresolved by declaration, not by omission. Any composition that reads this assembly as a single argument has supplied a merge the notebook withheld — and should say so.

*Ordering note: {order['note']}*

---

## CHARTER

""" + open(f'{D}/README.md').read().split('## The charter',1)[1].split('## Machine index')[0].strip()]
out.append("\n---\n\n# PLATES\n")
for pid in order['sequence']:
    p = by.get(pid)
    if not p: continue
    meta = f"*{p.get('voice','—')} · {p.get('kind','—')} · {p.get('date','—')} · {p.get('status','open')}"
    if p.get('seams'): meta += f" · seams: {', '.join(p['seams'])}"
    if p.get('extends'): meta += f" · extends {p['extends']}"
    out.append(f"\n---\n\n{body(p['file'])}\n\n{meta}*\n")
out.append("\n---\n\n# SEAMS HELD OPEN\n\n*A seam is a declared collision between plates, stated at full strength on both sides and left unresolved. A seam that closes was a misdescription.*\n")
for s in M['seams']:
    out.append(f"\n---\n\n{body(s['file'])}\n")
out.append("\n---\n\n# REGISTRY\n\nORS-Core v0.1 and its working entries are machine-readable instruments accompanying this notebook: `registry/ors-core-v0.1.json`, `registry/entries/working-set.json`. Registering an operator is not endorsing it (see S-09).\n\n∮ = 1\n")
txt = '\n'.join(out)
open('/mnt/user-data/outputs/NOTEBOOK-X-THE-GATE-cut-2026-08-26.md','w').write(txt)
print(f"compiled: {len(txt):,} chars, {len(order['sequence'])} plates, {len(M['seams'])} seams")
