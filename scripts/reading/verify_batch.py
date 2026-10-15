#!/usr/bin/env python3
"""verify_batch.py — check a parallel reader's output against the source texts, mechanically.

    python3 scripts/reading/verify_batch.py data/reading/batches/B0001.json [--write]

Checks, per deposit and per find (laws record; they do not block — every failure is written into the
verification record, nothing is dropped):
  COVER   read_ranges cover lines 1..lines_total of the file for status 'read'
  HASH    the file read is the one queued (sha256 at the queue's alexanarch commit)
  QUOTE   each quote occurs verbatim in the file (whitespace-normalised) and inside its stated lines (±2)
  FALSI   same for falsifier_quote
  SHAPE   shape in A–G
  NONE    none_found consistent with finds
  QUEUED  every queued deposit of the batch has an entry, and no entry is outside the batch
With --write, the verification is stored beside the batch as <batch>.verified.json.
"""
import json, pathlib, re, sys, hashlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
SH = set("ABCDEFG")


def norm(s):
    return re.sub(r"\s+", " ", s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')).strip()


def main():
    bp = pathlib.Path(sys.argv[1]); write = "--write" in sys.argv
    out = json.loads(bp.read_text())
    q = json.loads((ROOT / "data/reading/queue.json").read_text())
    if out["batch_id"] == "CAL":
        cal = json.loads((ROOT / "data/reading/calibration-batch.json").read_text())
        queued = {r["deposit"]: r for r in cal["deposits"]}
    else:
        b = next(x for x in q["batches"] if x["batch_id"] == out["batch_id"])
        queued = {r["deposit"]: r for r in b["deposits"]}
    res = {"batch_id": out["batch_id"], "checks": [], "summary": {}}
    seen = set()
    nq = nfail = 0
    for e in out.get("deposits", []):
        n = e.get("deposit"); seen.add(n); fails = []
        if n not in queued:
            fails.append("QUEUED: not in this batch")
            res["checks"].append({"deposit": n, "fails": fails}); continue
        row = queued[n]; p = pathlib.Path(row["path"]); raw = p.read_bytes(); t = raw.decode("utf-8", "replace")
        lines = t.split("\n")
        if hashlib.sha256(raw).hexdigest() != row["sha256"]:
            fails.append("HASH: file changed since queued")
        if e.get("status") == "read":
            covered = set()
            for a, b2 in e.get("read_ranges") or []:
                covered.update(range(int(a), int(b2) + 1))
            missing = [i for i in range(1, row["lines_total"] + 1) if i not in covered]
            if missing:
                fails.append(f"COVER: {len(missing)} of {row['lines_total']} lines not in read_ranges (first {missing[:5]})")
        finds = e.get("finds") or []
        if e.get("none_found") and finds:
            fails.append("NONE: none_found true with finds")
        if not finds and not e.get("none_found") and e.get("status") == "read":
            fails.append("NONE: no finds and none_found false")
        for i, f in enumerate(finds):
            nq += 1
            if f.get("shape") not in SH:
                fails.append(f"SHAPE: find {i} shape {f.get('shape')!r}")
            for qk, lk, tag in (("quote", "lines", "QUOTE"), ("falsifier_quote", "falsifier_lines", "FALSI")):
                qt = f.get(qk) or ""
                if not qt:
                    if tag == "QUOTE":
                        fails.append(f"QUOTE: find {i} empty"); nfail += 1
                    continue
                if norm(qt) not in norm(t):
                    fails.append(f"{tag}: find {i} not verbatim in file: {qt[:70]!r}")
                    if tag == "QUOTE": nfail += 1
                    continue
                ln = f.get(lk) or []
                if len(ln) == 2:
                    a, b2 = max(1, ln[0] - 2), min(len(lines), ln[1] + 2)
                    if norm(qt) not in norm("\n".join(lines[a - 1:b2])):
                        fails.append(f"{tag}: find {i} verbatim but not at lines {ln}")
        res["checks"].append({"deposit": n, "status": e.get("status"), "finds": len(finds), "fails": fails})
    for n in queued:
        if n not in seen:
            res["checks"].append({"deposit": n, "fails": ["QUEUED: no entry for a queued deposit"]})
    res["summary"] = {"deposits": len(queued), "entries": len(seen), "finds": nq, "quotes_failed": nfail,
                      "deposits_with_fails": sum(1 for c in res["checks"] if c["fails"]),
                      "status": dict((s, sum(1 for e in out.get("deposits", []) if e.get("status") == s)) for s in ("read", "partial", "skipped"))}
    print(json.dumps(res["summary"]))
    for c in res["checks"]:
        for f in c["fails"]:
            print(f"  #{c['deposit']}: {f}")
    if write:
        bp.with_suffix(".verified.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n")


if __name__ == "__main__":
    main()
