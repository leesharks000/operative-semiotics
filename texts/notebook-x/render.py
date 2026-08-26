#!/usr/bin/env python3
"""Notebook X renderer — builds index.html from any ordering.
The structure is a view: re-cut by passing a different ordering id.
Usage: python3 render.py [ordering_id]   (default: manifest['default_ordering'])"""
import json, sys, html, os

M = json.load(open(os.path.join(os.path.dirname(__file__),'manifest.json')))
oid = sys.argv[1] if len(sys.argv)>1 else M['default_ordering']
order = json.load(open(os.path.join(os.path.dirname(__file__),'orders',oid+'.json')))
by_id = {p['plate']: p for p in M['plates']}

CSS = """body{max-width:820px;margin:2rem auto;padding:0 1.2rem;font:16px/1.65 Georgia,serif;color:#161616;background:#fbfaf7}
.mono{font-family:ui-monospace,monospace;font-size:.78em;letter-spacing:.05em}
h1{font-size:1.7rem;line-height:1.2;margin-bottom:.2em}h2{font-size:1.1rem;margin-top:2.2em}
a{color:#7a1f5e}.dim{color:#666}
.charter{border-left:3px solid #7a1f5e;padding:.8em 1.1em;background:rgba(0,0,0,.03);margin:1.4em 0;font-size:.93em}
.plate{border-top:1px solid rgba(0,0,0,.14);padding-top:1em;margin-top:1.8em}
.meta{font-family:ui-monospace,monospace;font-size:.74em;color:#666;letter-spacing:.04em}
.seam{border:1px solid #7a1f5e;padding:.8em 1.1em;margin:1.6em 0;background:rgba(122,31,94,.04)}
.orders a{margin-right:1em}"""

rows = []
for pid in order['sequence']:
    p = by_id.get(pid)
    if not p: continue
    seams = (' · seams: ' + ', '.join(p['seams'])) if p.get('seams') else ''
    ext = (' · extends ' + html.escape(p['extends'])) if p.get('extends') else ''
    rows.append(f"""<div class="plate"><h2><a href="{p['file']}">{html.escape(p['plate'])} · {html.escape(p['title'])}</a></h2>
<p class="meta">{html.escape(p.get('voice','—'))} · {html.escape(p.get('kind','—'))} · {html.escape(p.get('date','—'))} · {html.escape(p.get('status','open'))}{seams}{ext}</p></div>""")

seam_rows = "".join(f"""<div class="seam"><strong><a href="{s['file']}">{html.escape(s['seam'])} · {html.escape(s['title'])}</a></strong>
<p class="meta">{html.escape(s.get('status','OPEN'))} · plates: {', '.join(s.get('plates',[]))}</p></div>""" for s in M['seams'])

ord_links = " ".join(f'<a href="?order={o["id"]}">{html.escape(o["name"])}</a>' for o in M['orderings'])

page = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Notebook X: The Gate — Operative Semiotics: A Grundrisse</title>
<meta name="description" content="The tenth notebook of Operative Semiotics: A Grundrisse, by Johannes Sigil (Lee Sharks). A workshop, not a treatise: plates accrete, orderings are views, seams are held open. On the admission boundary between retrieval and composition.">
<link rel="canonical" href="https://www.operativesemiotics.org/texts/notebook-x/">
<style>{CSS}</style></head><body>
<p class="mono"><a href="/">operative semiotics</a> · <a href="/texts/">texts</a> · notebook x · canonical record <a href="https://www.alexanarch.org/s/records/1550/">Alexanarch #1550</a> · <a href="/texts/notebook-x/contributors.json">contributors</a></p>
<h1>Notebook X: The Gate</h1>
<p class="mono">Johannes Sigil (Lee Sharks), with the Assembly · opened 2026-08-26 · <strong>open, accreting</strong> · {len(M['plates'])} plates, {len(M['seams'])} seams</p>
<div class="charter"><strong>A workshop, not a treatise.</strong> The unit is the <em>plate</em>: one complete utterance from one position, provenanced and numbered on arrival. Plates are storage; <strong>orderings are views</strong>, and no ordering is canonical — the first structure does not determine the structure. Material arrives from significantly different perspectives and is <strong>not merged</strong>: where plates collide, the collision is declared as a <strong>seam</strong> and held open with both sides at full strength. Voices are preserved. Nothing is edited to fit; superseded plates stay, marked. The notebook is never finished — it is periodically <em>cut</em> into a dated edition while the plates keep accreting. Full charter: <a href="/texts/notebook-x/README.md">README</a>. Machine index: <a href="/texts/notebook-x/manifest.json">manifest.json</a>.</div>
<div class="charter" style="border-left-color:#444"><strong>Synthesis status: asynthetic by declaration.</strong> No synthesis has been performed across these plates. Seams are unresolved by declaration, not by omission. Any composition that reads this assembly as a single argument has supplied a merge the notebook withheld — and should say so.</div>
<p class="mono orders">Current ordering — <strong>{html.escape(order['name'])}</strong>: {html.escape(order['note'])}<br>Available orderings: {ord_links} <span class="dim">(re-cut with render.py)</span></p>
{''.join(rows)}
<h2 style="margin-top:2.6em">Seams held open</h2>
<p class="dim" style="font-size:.92em">A seam is a declared collision between plates, stated at full strength on both sides and left unresolved. A seam that closes was a misdescription.</p>
{seam_rows}
<p class="mono" style="margin-top:2.5em">Canonical records at the <a href="https://www.alexanarch.org/">Crimson Hexagonal Archive</a> · CC BY 4.0 · ∮ = 1</p>
</body></html>"""
out = os.path.join(os.path.dirname(__file__),'index.html')
open(out,'w').write(page)
print(f"rendered ordering '{oid}' ({len(order['sequence'])} plates) → {out}")
