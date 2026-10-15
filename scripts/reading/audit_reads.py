#!/usr/bin/env python3
"""audit_reads.py — check, from a reader's own session transcript, which lines it actually opened.

    python3 scripts/reading/audit_reads.py <transcript.jsonl> [<transcript.jsonl> ...] [--write]

verify_batch.py checks what a reader CLAIMS (read_ranges cover the file; quotes are verbatim). This script checks
what it DID: it parses the reader's transcript (the harness's JSONL record of its tool calls and results), finds the
batch it was given (from the output path in its prompt), collects every Read tool call on each deposit's text file
and the line numbers the tool actually returned, and compares that coverage with the claimed read_ranges.

Per deposit it records: lines_total; lines actually returned by Read; lines claimed; claimed-but-not-returned lines
(the measure that matters); the number of Read calls; and any Bash/other tool calls that named the file (a reader
may also slice quotes with a script — that is allowed and listed, not counted as reading).
With --write the result is stored beside the batch as <batch>.audit.json, carrying the transcript's sha256 (not its
path or agent id). Laws record; they do not block: a shortfall is written down, nothing is dropped.
"""
import hashlib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / "data/reading"
LN = re.compile(r"^\s*(\d+)\t", re.M)
BID = re.compile(r"batches/((?:HB|B|S)\d{4}|CAL)\.json")


def batch_rows(bid):
    if bid == "CAL":
        return {r["deposit"]: r for r in json.loads((R / "calibration-batch.json").read_text())["deposits"]}
    src = R / ("hpass.json" if bid.startswith("HB") else "queue.json")
    b = next(x for x in json.loads(src.read_text())["batches"] if x["batch_id"] == bid)
    return {r["deposit"]: r for r in b["deposits"]}


def text_of(c):
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return "\n".join(x.get("text", "") for x in c if isinstance(x, dict))
    return ""


def audit(tp):
    raw = pathlib.Path(tp).read_bytes()
    recs = [json.loads(l) for l in raw.decode("utf-8", "replace").splitlines() if l.strip().startswith("{")]
    first = next((text_of(r["message"].get("content")) for r in recs if r.get("type") == "user"), "")
    m = BID.search(first)
    if not m:
        return None
    bid = m.group(1)
    rows = batch_rows(bid)
    bypath = {str(pathlib.Path(r["path"])): n for n, r in rows.items()}
    calls, other = {}, {}
    for r in recs:
        msg = r.get("message") or {}
        for c in msg.get("content") or [] if isinstance(msg.get("content"), list) else []:
            if not isinstance(c, dict):
                continue
            if c.get("type") == "tool_use":
                inp = c.get("input") or {}
                fp = str(inp.get("file_path") or "")
                if c.get("name") == "Read" and fp in bypath:
                    calls[c["id"]] = fp
                else:
                    blob = json.dumps(inp)
                    for p, n in bypath.items():
                        if p in blob or pathlib.Path(p).name in blob:
                            other.setdefault(n, []).append(c.get("name"))
            elif c.get("type") == "tool_result" and c.get("tool_use_id") in calls:
                fp = calls[c["tool_use_id"]]
                got = {int(x) for x in LN.findall(text_of(c.get("content")))}
                calls[c["tool_use_id"]] = (fp, got)
    seen = {}
    for v in calls.values():
        if isinstance(v, tuple):
            seen.setdefault(bypath[v[0]], []).append(v[1])
    bp = R / "batches" / f"{bid}.json"
    claimed = {}
    if bp.exists():
        for e in json.loads(bp.read_text()).get("deposits", []):
            s = set()
            for a, b in e.get("read_ranges") or []:
                s.update(range(int(a), int(b) + 1))
            claimed[e["deposit"]] = s
    out = []
    for n, row in rows.items():
        got = set().union(*seen.get(n, [set()]))
        cl = claimed.get(n, set())
        tot = set(range(1, row["lines_total"] + 1))
        out.append({"deposit": n, "lines_total": row["lines_total"], "read_calls": len(seen.get(n, [])),
                    "lines_returned": len(got & tot), "lines_claimed": len(cl & tot),
                    "claimed_not_returned": len((cl & tot) - got), "unread_lines": len(tot - got),
                    "first_unread": sorted(tot - got)[:5], "other_tool_access": sorted(set(other.get(n, [])))})
    summ = {"deposits": len(out), "fully_returned": sum(1 for o in out if o["unread_lines"] == 0),
            "claimed_not_returned_total": sum(o["claimed_not_returned"] for o in out),
            "unread_lines_total": sum(o["unread_lines"] for o in out)}
    return {"batch_id": bid, "transcript_sha256": hashlib.sha256(raw).hexdigest(), "summary": summ, "deposits": out}


def main():
    write = "--write" in sys.argv
    for tp in [a for a in sys.argv[1:] if a != "--write"]:
        res = audit(tp)
        if not res:
            continue
        print(res["batch_id"], json.dumps(res["summary"]))
        for o in res["deposits"]:
            if o["unread_lines"]:
                print(f"   #{o['deposit']}: {o['unread_lines']} of {o['lines_total']} lines never returned by Read "
                      f"(claimed-not-returned {o['claimed_not_returned']}; first {o['first_unread']}; other {o['other_tool_access']})")
        if write:
            (R / "batches" / f"{res['batch_id']}.audit.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n")


if __name__ == "__main__":
    main()
