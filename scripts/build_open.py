#!/usr/bin/env python3
"""Build operativesemiotics.org/open/ from data/predictions.json (+ archive intake).
Registry canonical; this page derived. Static-first: full content renders with no
JS; the small script at the bottom only adds status/effort filtering on top."""
import json, html, re, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
reg = json.load(open(ROOT / "data" / "predictions.json"))
try:
    intake = json.load(open(ROOT / "data" / "archive-intake.json"))
    intake_preds = intake.get("predictions", [])
except Exception:
    intake, intake_preds = {}, []

esc = lambda s: html.escape(str(s)) if s is not None else ""
CLS = [("experimental", "1 · Experimental predictions"),
       ("applied-theory", "2 · Predictions from applied theory"),
       ("unbuilt", "3 · Unimplemented software builds")]
STATUS_COLOR = {"open": "#8a6a20", "in-progress": "#1f6f8b", "partial": "#7a4b9e",
                "supported": "#2f7d3a", "disconfirmed": "#a83232",
                "built": "#2f7d3a", "superseded": "#777"}

def chip(s):
    c = STATUS_COLOR.get(s, "#777")
    return (f'<span class="chip" data-status="{esc(s)}" style="background:{c}1a;'
            f'color:{c};border:1px solid {c}55">{esc(s)}</span>')

def card(e):
    srcs = ""
    for s in e.get("sources", []):
        label = f"#{s['deposit']}" if s.get("deposit") else (s.get("url","").split("//")[-1][:34])
        note = f' <span class="dim">— {esc(s["note"])}</span>' if s.get("note") else ""
        srcs += f'<a href="{esc(s["url"])}">{esc(label)}</a>{note} · '
    srcs = srcs.rstrip(" ·")
    rows = []
    if e.get("requires"): rows.append(("requires", f'{esc(e["requires"])} · {esc(e.get("effort",""))}'))
    if e.get("due"): rows.append(("check by", esc(e["due"])))
    if e.get("registered"): rows.append(("registered", esc(e["registered"])))
    verb = {"unbuilt": "how to build"}.get(e["cls"], "how to check")
    if e.get("check"): rows.append((verb, esc(e["check"])))
    if e.get("settles"): rows.append(("what it settles", esc(e["settles"])))
    if e.get("status_note"): rows.append(("status note", esc(e["status_note"])))
    if srcs: rows.append(("sources", srcs))
    for u in e.get("updates", []):
        rows.append((f'update {esc(u.get("date",""))}',
                     esc(u.get("note","")) + (f' — <a href="{esc(u["evidence_url"])}">evidence</a>' if u.get("evidence_url") else "")))
    body = "".join(f'<div class="row"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in rows)
    return (f'<article class="card" data-status="{esc(e["status"])}" data-cls="{e["cls"]}">'
            f'<header>{chip(e["status"])}<code>{esc(e["id"])}</code></header>'
            f'<h3>{esc(e["title"])}</h3>'
            f'<p class="stmt">{esc(e["statement"])}</p>{body}</article>')

def intake_block(cls_key):
    # Untriaged whole-archive predictions shown per class only as a shared queue on
    # the first class section (they are unclassed until triage); grouped by deposit.
    if cls_key != "experimental" or not intake_preds:
        return ""
    by_dep = {}
    for p in intake_preds:
        by_dep.setdefault(p.get("deposit"), []).append(p)
    groups = []
    for dep in sorted(by_dep, key=lambda d: -len(by_dep[d])):
        ps = by_dep[dep]
        rows = "".join(
            f'<li><span class="dim">[{esc(p.get("status","OPEN"))}]</span> '
            f'{esc((p.get("statement") or "").strip()[:220])}</li>' for p in ps)
        groups.append(f'<details class="dep"><summary>#{dep} — {esc((ps[0].get("deposit_title") or "")[:70])} '
                      f'<span class="dim">({len(ps)})</span></summary>'
                      f'<div class="deplink"><a href="https://www.alexanarch.org/s/records/{dep}/">record</a></div>'
                      f'<ul>{rows}</ul></details>')
    return (f'<details class="intake"><summary><strong>Intake queue — {len(intake_preds)} machine-extracted '
            f'predictions from the whole archive, untriaged</strong> <span class="dim">'
            f'(snapshot of the archive prediction registry; entries graduate into the classes above by '
            f'triage: class, check route, status)</span></summary>'
            f'<p class="dim">Source: <a href="https://www.alexanarch.org/datasets/prediction-registry.json">'
            f'alexanarch.org/datasets/prediction-registry.json</a> · local snapshot '
            f'<a href="/data/archive-intake.json">data/archive-intake.json</a>. Triage is itself shareable work.</p>'
            + "".join(groups) + "</details>")

entries = reg["entries"]
counts = {c: [e for e in entries if e["cls"] == c] for c, _ in CLS}
stat_totals = {}
for e in entries:
    stat_totals[e["status"]] = stat_totals.get(e["status"], 0) + 1

sections = ""
for key, label in CLS:
    es = counts[key]
    open_n = sum(1 for e in es if e["status"] in ("open", "in-progress", "partial"))
    sections += (f'<section id="{key}"><h2>{esc(label)} <span class="dim">· {len(es)} registered, '
                 f'{open_n} live</span></h2><p class="clsdef">{esc(reg["classes"][key])}</p>'
                 f'<div class="grid">' + "".join(card(e) for e in es) + "</div>"
                 + intake_block(key) + "</section>")

nav = " · ".join(f'<a href="#{k}">{l.split("·")[1].strip()}</a> <span class="dim">({len(counts[k])})</span>'
                 for k, l in CLS)
statbar = " ".join(f'{chip(s)} <span class="dim">{n}</span>' for s, n in sorted(stat_totals.items()))
today = datetime.date.today().isoformat()

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Predictions &amp; Builds — Operative Semiotics</title>
<meta name="description" content="The open commitments of operative semiotics: experimental predictions, predictions from applied theory, and unimplemented software builds — each with sources, status, and the route to run or build it. Results by others are admissible on the same terms as results obtained here.">
<link rel="canonical" href="https://operativesemiotics.org/open/">
<script type="application/ld+json">{json.dumps({"@context":"https://schema.org","@type":"Dataset","name":reg["name"],"description":reg["description"],"version":reg["version"],"dateModified":today,"license":reg["license"],"creator":{"@type":"Person","name":"Lee Sharks"},"distribution":[{"@type":"DataDownload","contentUrl":"https://operativesemiotics.org/data/predictions.json","encodingFormat":"application/json"}]}, ensure_ascii=False)}</script>
<style>
:root{{--bg:#faf8f4;--fg:#1a1a1a;--dim:#6b6560;--line:#ddd6cc;--acc:#8a6a20}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.55 Georgia,'Times New Roman',serif;padding:0 16px}}
main{{max-width:960px;margin:0 auto;padding:32px 0 60px}}
a{{color:var(--acc)}}.dim{{color:var(--dim);font-weight:400}}
h1{{font-size:1.7em;margin:.2em 0}}h2{{font-size:1.2em;border-bottom:1px solid var(--line);padding-bottom:6px;margin-top:44px}}
h3{{font-size:1.02em;margin:.45em 0 .3em}}
.top p{{max-width:70ch}}
.navbar{{font-size:.92em;margin:10px 0 2px}}
.statbar{{margin:8px 0 0;font-size:.85em}}
.filters{{margin:14px 0 0;font-size:.82em}}
.filters button{{font:inherit;background:none;border:1px solid var(--line);border-radius:12px;
padding:2px 10px;margin:0 4px 4px 0;cursor:pointer;color:var(--dim)}}
.filters button.on{{border-color:var(--acc);color:var(--acc)}}
.clsdef{{color:var(--dim);font-size:.92em;max-width:74ch;margin-top:2px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(430px,1fr));gap:14px;margin-top:14px}}
@media(max-width:520px){{.grid{{grid-template-columns:1fr}}}}
.card{{border:1px solid var(--line);border-radius:8px;padding:12px 14px;background:#fffdf9}}
.card header{{display:flex;gap:8px;align-items:center;font-size:.78em}}
.card header code{{color:var(--dim);letter-spacing:.03em}}
.chip{{border-radius:10px;padding:1px 8px;font:600 .95em/1.5 ui-monospace,monospace;text-transform:lowercase}}
.stmt{{font-size:.94em;margin:.3em 0 .5em}}
.row{{font-size:.85em;margin:3px 0;display:grid;grid-template-columns:108px 1fr;gap:8px}}
.row .k{{color:var(--dim);font-variant:small-caps;letter-spacing:.03em}}
details.intake{{margin:20px 0 4px;border:1px dashed var(--line);border-radius:8px;padding:10px 14px;background:#fdfbf6}}
details.intake summary{{cursor:pointer}}
details.dep{{margin:8px 0 0 6px;font-size:.88em}}
details.dep summary{{cursor:pointer;color:#3a3630}}
details.dep ul{{margin:4px 0 8px;padding-left:20px}}details.dep li{{margin:3px 0}}
.deplink{{font-size:.85em;margin:2px 0 0 2px}}
footer{{margin-top:56px;border-top:1px solid var(--line);padding-top:14px;font-size:.85em;color:var(--dim)}}
.honesty{{border-left:3px solid var(--line);padding:2px 12px;margin:26px 0;font-size:.9em;color:#3a3630}}
</style></head><body><main>
<div class="top">
<p class="dim" style="font-size:.85em"><a href="/">Operative Semiotics</a> → Predictions &amp; Builds</p>
<h1>Predictions &amp; Builds</h1>
<p>Operative semiotics is the study <em>and design</em> of signs that intervene in the systems in which they circulate. A discipline defined that way owes a public account of what it has committed to and not yet done. This register holds three classes, sorted by <strong>the kind of labour that resolves them</strong>: experimental predictions resolve by running a frozen protocol or checking an observable — the world does the work, you check; applied-theory predictions resolve by watching a live system the theory was applied to; unimplemented builds resolve by construction. Every entry links its primary sources in the record layer, states its status, and gives the route to run or build it — because <strong>a result obtained by someone else is admissible on the same terms as one obtained here. Nothing requires permission.</strong> Data: <a href="/data/predictions.json">predictions.json</a>.</p>
<nav class="navbar">{nav}</nav>
<div class="statbar">{statbar}</div>
<div class="filters" id="filters" hidden>filter · status:
<button data-f="status" data-v="">all</button>""" + "".join(
    f'<button data-f="status" data-v="{s}">{s}</button>' for s in reg["status_vocabulary"]) + """
</div></div>
""" + sections + f"""
<div class="honesty"><strong>Honesty.</strong> {esc(reg["honesty"])}</div>
<footer>Whole-archive layer: <a href="https://www.alexanarch.org/datasets/prediction-registry.json">prediction-registry.json</a> · <a href="https://www.alexanarch.org/datasets/prediction-ledger/">prediction ledger</a> · <a href="https://www.alexanarch.org/datasets/study-dashboard/">study dashboard</a> · <a href="https://www.alexanarch.org/datasets/work-queue/manifest.json">work-queue</a><br>
Operative Semiotics · <a href="https://operativesemiotics.org/">operativesemiotics.org</a> · Lee Sharks, <a href="https://orcid.org/0009-0000-1599-0703">ORCID 0009-0000-1599-0703</a> · CC BY 4.0 · generated {today} by scripts/build_open.py · ∮ = 1</footer>
</main>
<script>
(function(){{var f=document.getElementById('filters');f.hidden=false;var cur='';
f.addEventListener('click',function(e){{var b=e.target.closest('button');if(!b)return;
cur=b.dataset.v;f.querySelectorAll('button').forEach(x=>x.classList.toggle('on',x===b));
document.querySelectorAll('.card').forEach(function(c){{
c.style.display=(!cur||c.dataset.status===cur)?'':'none';}});}});}})();
</script></body></html>"""

out = ROOT / "open" / "index.html"
out.write_text(page, encoding="utf-8")
print(f"wrote {out} ({len(page):,} bytes) — {len(entries)} curated entries, {len(intake_preds)} intake")
