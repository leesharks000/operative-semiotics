#!/usr/bin/env python3
"""derive_voice.py — reading texts for the two data deposits too large to read whole, and their batches.

    python3 scripts/reading/derive_voice.py

#3 (EA-WG-CAPTURES-01, ~2.3M words) and #4 (doi-resolution-index, ~390k words) are JSON datasets. Most of their bulk
is machine transcript (AI surfaces speaking — excluded by the protocol: "quotations of other people's predictions")
and dated observation/metadata (excluded: "dated observations of what already happened"). The archive's own voice
lives in named fields. This script extracts those fields VERBATIM, record by record, into a derived markdown text
with each block headed by the record's id and its line in the source file, so a reader can read the archive's voice
in full and a quote can be traced back. Fields read and fields excluded are listed in the derived file's header.

Writes data/reading/derived/<n>-voice.md and data/reading/xqueue.json (batches X0001…, ~35k words, cut at block
boundaries). The registry header (top-level fields) of #3 was read directly by B0093 (lines 1–899).
Deterministic for a given source file.
"""
import hashlib, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / "data/reading"
AX = pathlib.Path("/home/claude/alexanarch")
SPECS = {
    3: {"path": AX / "data/EA-WG-CAPTURES-01.json", "list": "entries", "id": ("slug", "id"),
        "read": ["d_full", "reading", "analysis", "findings", "notes", "per_note", "maxim", "maxim_note"],
        "excluded": "transcript, transcript_raw, observations (machine speech and dated telemetry); cite_list, links, "
                    "rounds, per_v, collisions and other structured metadata",
        "top": ["maxim", "maxim_note", "description", "note", "notes"]},
    4: {"path": AX / "data/doi-resolution-index.json", "list": "mappings", "id": ("dead_doi", "sovereign_id"),
        "read": ["note", "recovery_verification", "audit_status"],
        "excluded": "per-record identifiers, URLs, dates and status codes (metadata)",
        "top": ["description", "deduplication_note", "attribution_severance", "event", "changelog", "correction_log"]},
}


def txt(v):
    if isinstance(v, str):
        return v
    return json.dumps(v, ensure_ascii=False, indent=1)


def main():
    (R / "derived").mkdir(exist_ok=True)
    xb = []
    for n, s in SPECS.items():
        raw = s["path"].read_bytes(); src = raw.decode("utf-8")
        d = json.loads(src); lines = src.split("\n")
        recs = d.get(s["list"]) or []
        # locate each record's first line in the source: the line holding its id value
        out = [f"# Reading text for deposit #{n} — own-voice fields, verbatim",
               f"Source: {s['path']} (sha256 {hashlib.sha256(raw).hexdigest()})",
               f"Fields read: {', '.join(s['read'])} (per record); top-level: {', '.join(s['top'])}",
               f"Fields excluded by protocol: {s['excluded']}",
               "Built by scripts/reading/derive_voice.py. Each block: record index, id, source line.", ""]
        out.append("## TOP-LEVEL")
        for k in s["top"]:
            if k in d:
                out += [f"### {k}", txt(d[k]), ""]
        cursor = 0
        for i, e in enumerate(recs):
            rid = next((str(e[k]) for k in s["id"] if k in e), f"#{i}")
            ln = next((j + 1 for j in range(cursor, len(lines)) if rid in lines[j]), None)
            if ln:
                cursor = ln
            body = [(k, e[k]) for k in s["read"] if e.get(k)]
            if not body:
                continue
            head = f"## record {i} · {rid} · source line {ln}" + (f" · {e.get('date')}" if e.get('date') else "")
            if n == 3:
                head += f" · {e.get('surface','')} · q: {str(e.get('q',''))[:120]}"
            out.append(head)
            for k, v in body:
                out += [f"### {k}", txt(v), ""]
        p = R / "derived" / f"{n:04d}-voice.md"
        p.write_text("\n".join(out) + "\n")
        t = p.read_text(); L = t.split("\n")
        # cut into batches at '## ' block boundaries, ~35k words
        starts = [j for j, l in enumerate(L) if l.startswith("## ")] + [len(L)]
        a = 0; w = 0; parts = []
        for k in range(len(starts) - 1):
            seg = L[starts[k]:starts[k + 1]]; sw = sum(len(x.split()) for x in seg)
            if w and w + sw > 35000:
                parts.append((a, starts[k])); a = starts[k]; w = 0
            w += sw
        parts.append((a, len(L)))
        for a, b in parts:
            xb.append({"batch_id": f"X{len(xb)+1:04d}", "deposit": n, "path": str(p), "range": [a + 1, b],
                       "words": sum(len(x.split()) for x in L[a:b]), "lines_total": len(L) - (1 if L[-1] == "" else 0),
                       "sha256": hashlib.sha256(p.read_bytes()).hexdigest()})
        print(n, p, len(L), sum(len(x.split()) for x in L))
    (R / "xqueue.json").write_text(json.dumps({"what": "Batches over the derived own-voice reading texts of #3 and #4. "
                                               "Each batch is a line range of one derived file.", "batches": xb},
                                              ensure_ascii=False, indent=1) + "\n")
    print(len(xb), [(b["batch_id"], b["deposit"], b["range"], b["words"]) for b in xb])


if __name__ == "__main__":
    main()
