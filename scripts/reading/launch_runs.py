#!/usr/bin/env python3
"""launch_runs.py — record launched readers in runs.json before they start (pass 2 onward).

    python3 scripts/reading/launch_runs.py "<phase>" R0001 R0002 ...
"""
import datetime, hashlib, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / "data/reading"


def main():
    phase, ids = sys.argv[1], sys.argv[2:]
    rp = R / "runs.json"; runs = json.loads(rp.read_text())
    sha = hashlib.sha256((R / "READING-PROTOCOL.md").read_bytes()).hexdigest()
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for b in ids:
        runs["runs"].append({"run": f"R-p2-{b}", "batch_id": b, "phase": phase, "launched_at": now,
                             "reader_kind": "general-purpose subagent (background), spawned by the launcher",
                             "protocol": "READING-PROTOCOL v1.3", "protocol_sha256": sha,
                             "instructions": "data/reading/READER-PROMPT.md, 'Pass 2', with <ID> filled",
                             "output": f"data/reading/batches/{b}.json", "status": "launched"})
    rp.write_text(json.dumps(runs, ensure_ascii=False, indent=1) + "\n")
    print(len(ids), "launched", now)


if __name__ == "__main__":
    main()
