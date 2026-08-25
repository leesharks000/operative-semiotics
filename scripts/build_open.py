#!/usr/bin/env python3
"""Build operativesemiotics.org/open/ from data/predictions.json (+ archive intake).
Registry canonical; page derived. Static-first: all three class sections render
stacked with no JS (nav tabs are anchor links); with JS the nav becomes true
tabs and each section gains sort/filter controls. Tracker tiles are BUILD-TIME
numbers — they derive from the same commit as the cards, so a live fetch would
add a failure mode without adding truth."""
import json, html, re, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
reg = json.load(open(ROOT / "data" / "predictions.json"))
try:
    intake = json.load(open(ROOT / "data" / "archive-intake.json"))
    intake_preds = intake.get("predictions", [])
except Exception:
    intake_preds = []

esc = lambda s: html.escape(str(s)) if s is not None else ""
CLS = [("experimental", "1 · Experimental", "Experimental predictions"),
       ("applied-theory", "2 · Applied theory", "Predictions from applied theory"),
       ("unbuilt", "3 · Builds", "Unimplemented software builds")]
STATUS_COLOR = {"open": "#8a6a20", "in-progress": "#1f6f8b", "partial": "#7a4b9e",
                "supported": "#2f7d3a", "disconfirmed": "#a83232",
                "built": "#2f7d3a", "superseded": "#777"}
LIVE = ("open", "in-progress", "partial")


def effort_rank(s):
    s = (s or "").lower()
    for k, r in (("low", 1), ("one ", 1), ("medium-high", 2.5), ("medium", 2), ("high", 3)):
        if k in s: return r
    return 2


def due_key(s):
    m = re.search(r"\d{4}-\d{2}-\d{2}", s or "")
    return m.group(0) if m else "9999-12-31"


def chip(s):
    c = STATUS_COLOR.get(s, "#777")
    return (f'<span class="chip" style="background:{c}1a;color:{c};'
            f'border:1px solid {c}55">{esc(s)}</span>')


def card(e):
    srcs = ""
    for s in e.get("sources", []):
        label = f"#{s['deposit']}" if s.get("deposit") else (s.get("url", "").split("//")[-1][:34])
        note = f' <span class="dim">— {esc(s["note"])}</span>' if s.get("note") else ""
        srcs += f'<a href="{esc(s["url"])}">{esc(label)}</a>{note} · '
    srcs = srcs.rstrip(" ·")
    rows = []
    if e.get("requires"): rows.append(("requires", f'{esc(e["requires"])} · {esc(e.get("effort", ""))}'))
    if e.get("due"): rows.append(("check by", esc(e["due"])))
    if e.get("registered"): rows.append(("registered", esc(e["registered"])))
    verb = {"unbuilt": "how to build"}.get(e["cls"], "how to check")
    if e.get("check"): rows.append((verb, esc(e["check"])))
    if e.get("settles"): rows.append(("what it settles", esc(e["settles"])))
    if e.get("status_note"): rows.append(("status note", esc(e["status_note"])))
    if srcs: rows.append(("sources", srcs))
    for u in e.get("updates", []):
        rows.append((f'update {esc(u.get("date", ""))}',
                     esc(u.get("note", "")) + (f' — <a href="{esc(u["evidence_url"])}">evidence</a>' if u.get("evidence_url") else "")))
    body = "".join(f'<div class="row"><span class="k">{k}</span><span class="v">{v}</span></div>' for k, v in rows)
    return (f'<article class="card" data-status="{esc(e["status"])}" data-id="{esc(e["id"])}" '
            f'data-registered="{esc(e.get("registered") or "")}" data-due="{due_key(e.get("due"))}" '
            f'data-effort="{effort_rank(e.get("effort"))}">'
            f'<header>{chip(e["status"])}<code>{esc(e["id"])}</code></header>'
            f'<h3>{esc(e["title"])}</h3>'
            f'<p class="stmt">{esc(e["statement"])}</p>{body}</article>')


def intake_block():
    if not intake_preds:
        return ""
    by_dep = {}
    for p in intake_preds:
        by_dep.setdefault(p.get("deposit"), []).append(p)
    groups = []
    for dep in sorted(by_dep, key=lambda d: -len(by_dep[d])):
        ps = by_dep[dep]
        rows = "".join(f'<li><span class="dim">[{esc(p.get("status", "OPEN"))}]</span> '
                       f'{esc((p.get("statement") or "").strip()[:220])}</li>' for p in ps)
        groups.append(f'<details class="dep"><summary>#{dep} — {esc((ps[0].get("deposit_title") or "")[:70])} '
                      f'<span class="dim">({len(ps)})</span></summary>'
                      f'<div class="deplink"><a href="https://www.alexanarch.org/s/records/{dep}/">record</a></div>'
                      f'<ul>{rows}</ul></details>')
    return (f'<details class="intake" id="intake"><summary><strong>Intake queue — {len(intake_preds)} machine-extracted '
            f'predictions from the whole archive, untriaged</strong> <span class="dim">'
            f'(snapshot of the archive prediction registry; entries graduate into the classes above by '
            f'triage: class, check route, status)</span></summary>'
            f'<p class="dim">Source: <a href="https://www.alexanarch.org/datasets/prediction-registry.json">'
            f'alexanarch.org/datasets/prediction-registry.json</a> · local snapshot '
            f'<a href="/data/archive-intake.json">data/archive-intake.json</a>. Triage is itself shareable work.</p>'
            + "".join(groups) + "</details>")


entries = reg["entries"]
counts = {c: [e for e in entries if e["cls"] == c] for c, _, _ in CLS}
live_n = sum(1 for e in entries if e["status"] in LIVE)
sup_n = sum(1 for e in entries if e["status"] in ("supported", "built"))
dis_n = sum(1 for e in entries if e["status"] == "disconfirmed")
src_deps = {s.get("deposit") for e in entries for s in e.get("sources", []) if s.get("deposit")}
today = datetime.date.today().isoformat()

SORTBAR = ('<div class="sortbar" hidden>sort · '
           '<button data-s="status">status</button>'
           '<button data-s="registered">registered</button>'
           '<button data-s="due">check-by</button>'
           '<button data-s="effort">effort</button>'
           '<button data-s="id">id</button>'
           ' <span class="dim">· filter</span> <input type="text" placeholder="text or status…" size="14"></div>')

sections = ""
for key, tab, label in CLS:
    es = counts[key]
    open_n = sum(1 for e in es if e["status"] in LIVE)
    sections += (f'<section id="{key}" class="clspanel"><h2>{esc(label)} <span class="dim">· {len(es)} registered, '
                 f'{open_n} live</span></h2><p class="clsdef">{esc(reg["classes"][key])}</p>{SORTBAR}'
                 f'<div class="grid">' + "".join(card(e) for e in es) + "</div></section>")

# tracker tiles — build-time numbers, machinemediation card-num idiom in the warm-paper palette
tiles = [
    (len(entries), "registered", "#all"),
    (len(counts["experimental"]), "experimental", "#experimental"),
    (len(counts["applied-theory"]), "applied theory", "#applied-theory"),
    (len(counts["unbuilt"]), "unbuilt", "#unbuilt"),
    (live_n, "live now", "#all"),
    (sup_n, "supported / built", "#all"),
    (dis_n, "disconfirmed", "#all"),
    (len(intake_preds), "intake queue", "#intake"),
    (len(src_deps), "source deposits", "#all"),
]
tiles_html = "".join(f'<a class="tile" href="{h}"><div class="tnum">{n}</div><div class="tlab">{esc(l)}</div></a>'
                     for n, l, h in tiles)

nav_tabs = ('<a href="#all" class="tab on" data-t="all">All</a>' +
            "".join(f'<a href="#{k}" class="tab" data-t="{k}">{esc(t)}</a>' for k, t, _ in CLS))

page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Predictions &amp; Builds — Operative Semiotics</title>
<meta name="description" content="The open commitments of operative semiotics: experimental predictions, predictions from applied theory, and unimplemented software builds — each with sources, status, and the route to run or build it. Results by others are admissible on the same terms as results obtained here.">
<link rel="canonical" href="https://operativesemiotics.org/open/">
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@type": "Dataset", "name": reg["name"], "description": reg["description"], "version": reg["version"], "dateModified": today, "license": reg["license"], "creator": {"@type": "Person", "name": "Lee Sharks"}, "distribution": [{"@type": "DataDownload", "contentUrl": "https://operativesemiotics.org/data/predictions.json", "encodingFormat": "application/json"}]}, ensure_ascii=False)}</script>
<style>
:root{{--bg:#faf8f4;--fg:#1a1a1a;--dim:#6b6560;--line:#ddd6cc;--acc:#8a6a20;--teal:#1f6f5b}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--fg);
font:16px/1.55 Georgia,'Times New Roman',serif;padding:0 16px}}
main{{max-width:980px;margin:0 auto;padding:18px 0 60px}}
a{{color:var(--acc)}}.dim{{color:var(--dim);font-weight:400}}
h1{{font-size:1.65em;margin:.25em 0 .1em}}h2{{font-size:1.2em;border-bottom:1px solid var(--line);padding-bottom:6px;margin-top:38px}}
h3{{font-size:1.02em;margin:.45em 0 .3em}}
.topnav{{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);
display:flex;gap:4px;align-items:center;padding:8px 0;z-index:5;flex-wrap:wrap}}
.topnav .home{{font-weight:bold;margin-right:12px;text-decoration:none;color:var(--fg)}}
.tab{{text-decoration:none;color:var(--dim);border:1px solid transparent;border-radius:14px;padding:3px 12px;font-size:.9em}}
.tab.on{{color:var(--acc);border-color:var(--acc);background:#8a6a2012}}
.topnav .data{{margin-left:auto;font-size:.82em}}
.tiles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(96px,1fr));gap:8px;margin:16px 0 4px}}
.tile{{border:1px solid var(--line);border-radius:8px;padding:8px 6px;text-align:center;
text-decoration:none;background:#fffdf9;color:var(--fg)}}
.tnum{{font-size:1.5em;font-weight:bold;color:var(--teal);font-family:ui-monospace,monospace;line-height:1.2}}
.tlab{{font-size:.68em;color:var(--dim);text-transform:uppercase;letter-spacing:.05em;margin-top:2px}}
.top p{{max-width:72ch;font-size:.95em}}
.clsdef{{color:var(--dim);font-size:.92em;max-width:74ch;margin-top:2px}}
.sortbar{{font-size:.8em;color:var(--dim);margin:10px 0 0}}
.sortbar button{{font:inherit;background:none;border:1px solid var(--line);border-radius:12px;
padding:1px 9px;margin:0 3px 3px 0;cursor:pointer;color:var(--dim)}}
.sortbar button.on{{border-color:var(--acc);color:var(--acc)}}
.sortbar input{{font:inherit;border:1px solid var(--line);border-radius:12px;padding:1px 8px;background:#fffdf9}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(430px,1fr));gap:14px;margin-top:12px}}
@media(max-width:520px){{.grid{{grid-template-columns:1fr}}}}
.card{{border:1px solid var(--line);border-radius:8px;padding:12px 14px;background:#fffdf9}}
.card header{{display:flex;gap:8px;align-items:center;font-size:.78em}}
.card header code{{color:var(--dim);letter-spacing:.03em}}
.chip{{border-radius:10px;padding:1px 8px;font:600 .95em/1.5 ui-monospace,monospace;text-transform:lowercase}}
.stmt{{font-size:.94em;margin:.3em 0 .5em}}
.row{{font-size:.85em;margin:3px 0;display:grid;grid-template-columns:108px 1fr;gap:8px}}
.row .k{{color:var(--dim);font-variant:small-caps;letter-spacing:.03em}}
details.intake{{margin:26px 0 4px;border:1px dashed var(--line);border-radius:8px;padding:10px 14px;background:#fdfbf6}}
details.intake summary{{cursor:pointer}}
details.dep{{margin:8px 0 0 6px;font-size:.88em}}
details.dep summary{{cursor:pointer;color:#3a3630}}
details.dep ul{{margin:4px 0 8px;padding-left:20px}}details.dep li{{margin:3px 0}}
.deplink{{font-size:.85em;margin:2px 0 0 2px}}
footer{{margin-top:56px;border-top:1px solid var(--line);padding-top:14px;font-size:.85em;color:var(--dim)}}
.honesty{{border-left:3px solid var(--line);padding:2px 12px;margin:26px 0;font-size:.9em;color:#3a3630}}
</style></head><body><main id="all">
<nav class="topnav">{'<a class="home" href="/">Operative Semiotics</a>'}{nav_tabs}<a class="data" href="/data/predictions.json">predictions.json</a></nav>
<div class="top">
<h1>Predictions &amp; Builds</h1>
<div class="tiles">{tiles_html}</div>
<p>The register of the discipline's open commitments, in three classes sorted by <strong>the kind of labour that resolves them</strong>: experimental predictions resolve by running a frozen protocol or checking an observable; applied-theory predictions resolve by watching a live system the theory was applied to; unimplemented builds resolve by construction. Every entry links its primary sources in the record layer, states its status, and gives the route to run or build it — <strong>a result obtained by someone else is admissible on the same terms as one obtained here. Nothing requires permission.</strong></p>
</div>
{sections}
{intake_block()}
<div class="honesty"><strong>Honesty.</strong> {esc(reg["honesty"])}</div>
<footer>Whole-archive layer: <a href="https://www.alexanarch.org/datasets/prediction-registry.json">prediction-registry.json</a> · <a href="https://www.alexanarch.org/datasets/prediction-ledger/">prediction ledger</a> · <a href="https://www.alexanarch.org/datasets/study-dashboard/">study dashboard</a> · <a href="https://www.alexanarch.org/datasets/work-queue/manifest.json">work-queue</a><br>
Operative Semiotics · <a href="https://operativesemiotics.org/">operativesemiotics.org</a> · Lee Sharks, <a href="https://orcid.org/0009-0000-1599-0703">ORCID 0009-0000-1599-0703</a> · CC BY 4.0 · generated {today} by scripts/build_open.py · ∮ = 1</footer>
</main>
<script>
(function(){{
var tabs=document.querySelectorAll('.tab'),panels=document.querySelectorAll('.clspanel');
tabs.forEach(function(t){{t.addEventListener('click',function(ev){{ev.preventDefault();
tabs.forEach(x=>x.classList.toggle('on',x===t));var k=t.dataset.t;
panels.forEach(p=>p.style.display=(k==='all'||p.id===k)?'':'none');
if(k!=='all')document.getElementById(k).scrollIntoView({{behavior:'smooth',block:'start'}});
else window.scrollTo({{top:0,behavior:'smooth'}});}});}});
document.querySelectorAll('.sortbar').forEach(function(sb){{sb.hidden=false;
var grid=sb.parentElement.querySelector('.grid');
sb.querySelectorAll('button').forEach(function(b){{b.addEventListener('click',function(){{
var k=b.dataset.s,asc=!b.classList.contains('on')||b.dataset.d!=='1';
sb.querySelectorAll('button').forEach(x=>{{x.classList.toggle('on',x===b);if(x!==b)delete x.dataset.d;}});
b.dataset.d=asc?'1':'0';
var cards=[].slice.call(grid.children);
cards.sort(function(a,c){{var x=a.dataset[k]||'',y=c.dataset[k]||'';
var nx=parseFloat(x),ny=parseFloat(y);
var r=(!isNaN(nx)&&!isNaN(ny))?nx-ny:x.localeCompare(y);return asc?r:-r;}});
cards.forEach(c=>grid.appendChild(c));}});}});
var inp=sb.querySelector('input');
inp.addEventListener('input',function(){{var q=inp.value.toLowerCase();
[].forEach.call(grid.children,function(c){{
c.style.display=(!q||c.textContent.toLowerCase().indexOf(q)>-1)?'':'none';}});}});}});
}})();
</script></body></html>"""

out = ROOT / "open" / "index.html"
out.write_text(page, encoding="utf-8")
print(f"wrote {out} ({len(page):,} bytes) — {len(entries)} curated, {len(intake_preds)} intake, "
      f"{live_n} live, {len(src_deps)} source deposits")
