#!/usr/bin/env python3
"""build_tracker.py — the reading tracker of the prediction sweep, rebuilt from the batch files.

    python3 scripts/reading/build_tracker.py

Inputs: data/reading/queue.json (what is to be read), data/reading/in-session-readings.json (read before the
sweep), data/reading/runs.json (the launcher's record), data/reading/batches/*.json (each reader's record)
and their *.verified.json (the mechanical check). Outputs:
  data/reading/tracker.json   one row per deposit: unread | read | partial | skipped, by which reading, under
                              which run, how (ranges covered), the reader's provenance, the verification
                              result, the number of finds by shape, none_found, incidental notes
  data/reading/finds.jsonl    every find, one per line, carrying deposit, date, batch, run, shape, verbatim
                              quote and lines, falsifier, window, points_to, note, and verified true/false
A deposit read more than once keeps every reading; the tracker row names them all. Nothing is dropped for
failing verification — it is marked. Deterministic.
"""
import json, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / "data/reading"


def main():
    q = json.loads((R / "queue.json").read_text())
    ins = json.loads((R / "in-session-readings.json").read_text())
    runs = {r["batch_id"]: r for r in json.loads((R / "runs.json").read_text())["runs"]}
    rows = {}
    for b in q["batches"]:
        for d in b["deposits"]:
            rows[d["deposit"]] = {"deposit": d["deposit"], "date": d["date"], "title": d["title"], "tier": d["tier"],
                                  "words": d["words"], "batch_id": b["batch_id"], "state": "unread", "readings": []}
    for r in ins["readings"]:
        rows.setdefault(r["deposit"], {"deposit": r["deposit"], "state": "unread", "readings": []})
        rows[r["deposit"]]["readings"].append({"by": "in-session", "reader": ins["reader"]["role"], "date": ins["reader"]["date"],
                                               "status": r["status"], "how": ins["reader"]["how"],
                                               "shapes": sorted(r.get("shapes", {})), "none_found": bool(r.get("none_found"))})
    finds = []
    for bp in sorted((R / "batches").glob("*.json")):
        if bp.name.endswith((".verified.json", ".audit.json")):
            continue
        out = json.loads(bp.read_text())
        vp = bp.with_suffix(".verified.json")
        ver = {c["deposit"]: c for c in json.loads(vp.read_text())["checks"]} if vp.exists() else {}
        run = runs.get(out["batch_id"], {})
        ap = bp.with_name(bp.stem + ".audit.json")
        aud = {a["deposit"]: a for a in json.loads(ap.read_text())["deposits"]} if ap.exists() else {}
        for e in out.get("deposits", []):
            n = e["deposit"]; v = ver.get(n)
            fails = v["fails"] if v else ["UNVERIFIED"]
            sc = collections.Counter(f.get("shape") for f in e.get("finds") or [])
            rows.setdefault(n, {"deposit": n, "state": "unread", "readings": []})
            rows[n]["readings"].append({"by": "parallel", "batch_id": out["batch_id"], "run": run.get("run"),
                                        "reader": out.get("reader"), "protocol": out.get("protocol"), "status": e.get("status"), "status_note": e.get("status_note"),
                                        "read_ranges": e.get("read_ranges"), "lines_total": e.get("lines_total"),
                                        "genre_observed": e.get("genre_observed"), "finds_by_shape": dict(sc),
                                        "none_found": e.get("none_found"), "incidental": e.get("incidental"),
                                        "verification": "pass" if not fails else fails,
                                        "audit": ({k: aud[n][k] for k in ("read_calls", "lines_returned", "unread_lines", "claimed_not_returned")}
                                                  if n in aud else "not audited")})
            for i, f in enumerate(e.get("finds") or []):
                bad = [x for x in fails if f"find {i} " in x or x == "UNVERIFIED"]
                finds.append({"deposit": n, "date": rows[n].get("date"), "batch_id": out["batch_id"], "run": run.get("run"),
                              **{k: f.get(k) for k in ("shape", "quote", "lines", "falsifier_quote", "falsifier_lines",
                                                       "window", "points_to", "note")},
                              "verified": not bad, "verification_fails": bad})
    xq = json.loads((R / "xqueue.json").read_text())["batches"] if (R / "xqueue.json").exists() else []
    xneed = {}
    for b in xq:
        xneed.setdefault(b["deposit"], set()).add(b["batch_id"])
    for r in rows.values():
        if r["deposit"] in xneed:
            done = {x.get("batch_id") for x in r["readings"] if x.get("batch_id", "").startswith("X")
                    and x.get("status") == "read" and x.get("verification") == "pass"}
            r["xpass"] = {"needed": sorted(xneed[r["deposit"]]), "done": sorted(done),
                          "scope": "own-voice fields read in full from a derived text; transcripts and observations "
                                   "excluded by protocol (see scripts/reading/derive_voice.py)"}
            r["readings"] = [dict(x, status=("partial" if x.get("batch_id", "").startswith("X") and xneed[r["deposit"]] - done else x.get("status")))
                             for x in r["readings"]]
            if xneed[r["deposit"]] <= done:
                r["readings"].append({"by": "xpass", "status": "read", "protocol": "READING-PROTOCOL v1.2"})
    for r in rows.values():
        st = [x["status"] for x in r["readings"]]
        r["state"] = "read" if "read" in st else ("partial" if "partial" in st else ("skipped" if "skipped" in st else "unread"))
    for r in rows.values():
        r["h_covered"] = any(x.get("status") == "read" and str(x.get("protocol", "")) >= "READING-PROTOCOL v1.2"
                             for x in r["readings"])
    tr = sorted(rows.values(), key=lambda r: (r.get("tier") or 0, r.get("date") or "", r["deposit"]))
    c = collections.Counter(r["state"] for r in tr)
    out = {"what": "The reading tracker of the prediction sweep: every readable alexanarch deposit, whether it has been read, "
                   "how, by which reader under which run, and what it yielded. Rebuilt by scripts/reading/build_tracker.py.",
           "alexanarch_commit": q["alexanarch_commit"], "counts": dict(c),
           "h_covered": sum(1 for r in tr if r["h_covered"]),
           "h_note": "shape H (historical thesis) entered at protocol v1.2; deposits read under v1.0/v1.1 are not yet swept for H",
           "finds_by_shape": dict(collections.Counter(f["shape"] for f in finds)),
           "finds_verified": sum(1 for f in finds if f["verified"]), "finds_total": len(finds),
           "deposits": tr}
    (R / "tracker.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    (R / "finds.jsonl").write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in finds))
    print(json.dumps({k: out[k] for k in ("counts", "h_covered", "finds_by_shape", "finds_verified", "finds_total")}))


if __name__ == "__main__":
    main()
