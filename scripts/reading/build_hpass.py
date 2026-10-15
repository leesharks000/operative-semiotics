#!/usr/bin/env python3
"""build_hpass.py — the H back-pass queue: deposits read before shape H existed (protocol v1.0/v1.1), cut into
batches for a re-reading that records shape H only.

    python3 scripts/reading/build_hpass.py

Reads data/reading/tracker.json (rebuild it first) and data/reading/queue.json; writes data/reading/hpass.json with
batches HB0001… in queue order (tier, then oldest first), 35k words each. The eight in-session readings are included;
their rows are looked up from the alexanarch registry paths recorded in calibration-batch.json. Deterministic for a
given tracker.
"""
import json, pathlib

R = pathlib.Path(__file__).resolve().parents[2] / "data/reading"


def main():
    t = json.loads((R / "tracker.json").read_text())
    q = json.loads((R / "queue.json").read_text())
    rows = {r["deposit"]: r for b in q["batches"] for r in b["deposits"]}
    cal = {r["deposit"]: r for r in json.loads((R / "calibration-batch.json").read_text())["deposits"]}
    need = [d for d in t["deposits"] if d["state"] == "read" and not d["h_covered"]]
    todo = []
    for d in need:
        r = rows.get(d["deposit"]) or cal.get(d["deposit"])
        if r:
            todo.append(r)
    todo.sort(key=lambda r: (r.get("tier", 0), r.get("date", ""), r["deposit"]))
    batches, cur, cw = [], [], 0
    for r in todo:
        w = r.get("words") or 0
        if cur and cw + w > 35000:
            batches.append(cur); cur, cw = [], 0
        cur.append(r); cw += w
    if cur:
        batches.append(cur)
    out = {"what": "H back-pass: deposits read before protocol v1.2 introduced shape H, re-read in full for shape H only.",
           "counts": {"deposits": len(todo), "batches": len(batches), "words": sum(r.get("words") or 0 for r in todo)},
           "batches": [{"batch_id": f"HB{i+1:04d}", "words": sum(r.get("words") or 0 for r in b), "deposits": b}
                       for i, b in enumerate(batches)]}
    (R / "hpass.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps(out["counts"]))


if __name__ == "__main__":
    main()
