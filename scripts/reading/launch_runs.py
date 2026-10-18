#!/usr/bin/env python3
"""launch_runs.py — record launched readers in runs.json before they start (pass 2 onward).

    python3 scripts/reading/launch_runs.py "<phase>" R0001 R0002 ...
"""
import datetime, hashlib, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / "data/reading"


KIND = {"R": ("READING-PROTOCOL.md", "READING-PROTOCOL v1.3", "data/reading/READER-PROMPT.md, 'Pass 2', with <ID> filled", "inherited"),
        "A": ("READING-PROTOCOL.md", "READING-PROTOCOL v1.3", "data/reading/READER-PROMPT.md, 'Pass 2', with <ID> filled", "inherited"),
        "N": ("ANNOTATION-PROTOCOL.md", "ANNOTATION-PROTOCOL v1.0", "data/reading/READER-PROMPT.md, 'Annotation pass', with <ID> filled", "inherited"),
        "J": ("RECALL-ADJUDICATE.md", "RECALL-ADJUDICATE v1.0", "data/reading/READER-PROMPT.md, 'Recall adjudication', with <ID> filled", "inherited"),
        "D": ("../index/DESCRIBE-PROTOCOL.md", "DESCRIBE-PROTOCOL v1.0", "data/reading/READER-PROMPT.md, 'Describe pass', with <ID> filled", "inherited"),
        "K": ("RECALL-BRIEF.md", "RECALL-BRIEF v1.0", "data/reading/READER-PROMPT.md, 'Recall audit', with <ID> filled", "sonnet")}


def main():
    phase, ids = sys.argv[1], sys.argv[2:]
    rp = R / "runs.json"; runs = json.loads(rp.read_text())
    proto, pname, instr, model = KIND.get(ids[0][0], KIND["R"])
    sha = hashlib.sha256((R / proto).read_bytes()).hexdigest()
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for b in ids:
        runs["runs"].append({"run": (f"R-p2-{b}" if b[0] in "RA" else f"R-{b}"), "batch_id": b, "phase": phase, "launched_at": now,
                             "reader_kind": f"general-purpose subagent (background), spawned by the launcher; model {model}",
                             "protocol": pname, "protocol_sha256": sha,
                             "instructions": instr,
                             "output": f"data/reading/batches/{b}.json", "status": "launched"})
    rp.write_text(json.dumps(runs, ensure_ascii=False, indent=1) + "\n")
    print(len(ids), "launched", now)


if __name__ == "__main__":
    main()
