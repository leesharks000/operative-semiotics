#!/usr/bin/env python3
"""complete_run.py — record a finished reader in runs.json: launcher-observed stats, the reader's self-report
(read from its own output file), and the verification summary (from <batch>.verified.json).

    python3 scripts/reading/complete_run.py B0006 --ms 51718 --tools 11 --tokens 116456
"""
import argparse, json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / "data/reading"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("batch"); ap.add_argument("--ms", type=int); ap.add_argument("--tools", type=int)
    ap.add_argument("--tokens", type=int); ap.add_argument("--status", default="completed")
    a = ap.parse_args()
    rp = R / "runs.json"; runs = json.loads(rp.read_text())
    run = next(x for x in reversed(runs["runs"]) if x["batch_id"] == a.batch)
    out = json.loads((R / "batches" / f"{a.batch}.json").read_text())
    ver = json.loads((R / "batches" / f"{a.batch}.verified.json").read_text())
    rd = out.get("reader") or {}
    run.update({"status": a.status,
                "observed_by_launcher": {"duration_ms": a.ms, "tool_uses": a.tools, "tokens": a.tokens},
                "reader_self_reported": {k: rd.get(k) for k in ("started_at", "finished_at", "self_description", "tools_used")},
                "verification": ver["summary"]})
    rp.write_text(json.dumps(runs, ensure_ascii=False, indent=1) + "\n")
    print(a.batch, run["run"], ver["summary"])


if __name__ == "__main__":
    main()
