#!/usr/bin/env python3
"""build_queue.py — the reading queue for the prediction sweep, cut into batches.

    python3 scripts/reading/build_queue.py --alexanarch /path/to/alexanarch [--words 35000]

Every readable deposit of alexanarch (registry entry with a text file; metadata stubs excluded) is one row.
Order, by the pilot reading of 2026-10-15 (density alone buries the strongest finds — DashFace #713 carries
2.0 predictive markers per thousand words, the RCF priority record #519 carries 1.6):
  tier 1  predictive or speculative genres by content_type (prediction, forecast, memo, patent, probe,
          pre-registration, empirical, effective act, scenario), or >= 5 predictive markers
  tier 2  any predictive marker
  tier 3  none
oldest first within each tier (early dates carry the most priority value). Batches are cut by a word budget
so each reader holds its batch in full. Deposits already read are carried with their reading and not queued.
Writes data/reading/queue.json. Deterministic for a given alexanarch commit.
"""
import argparse, hashlib, json, pathlib, re, subprocess

GENRE = re.compile(r"predict|forecast|memo|patent|probe|pre-?regist|empirical|effective act|scenario|speculat", re.I)
MARK = re.compile(r"\bpredict|falsif|\bwithin (\d+|one|two|three|six|twelve) (hours|days|weeks|months|years)\b"
                  r"|\bby 20\d\d\b|\bwill (become|replace|collapse|emerge|produce|fail|appear)\b"
                  r"|\b(specification|unbuilt|not yet built|would measure)\b", re.I)
ROOT = pathlib.Path(__file__).resolve().parents[2]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--alexanarch", required=True)
    ap.add_argument("--words", type=int, default=35000)
    a = ap.parse_args()
    ax = pathlib.Path(a.alexanarch)
    commit = subprocess.run(["git", "-C", str(ax), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    reg = json.loads((ax / "data/registry.json").read_text())["deposits"]
    done = json.loads((ROOT / "data/reading/in-session-readings.json").read_text())["readings"]
    done_n = {r["deposit"] for r in done}
    rows = []
    for d in reg:
        n = d.get("deposit_number")
        if not n or ((d.get("body_status") or {}).get("retired") or {}).get("class") == "stub":
            continue
        rel = str(d.get("full_text_path") or "").lstrip("/")
        p = ax / rel
        if not rel or not p.is_file():
            continue
        raw = p.read_bytes(); t = raw.decode("utf-8", "replace")
        w = len(t.split()); m = len(MARK.findall(t)); ct = str(d.get("content_type") or "")
        tier = 1 if (GENRE.search(ct) or m >= 5) else (2 if m else 3)
        rows.append({"deposit": n, "date": str(d.get("date") or "")[:10], "title": str(d.get("title") or "")[:160],
                     "content_type": ct[:80], "path": str(p), "lines_total": t.count("\n") + (0 if t.endswith("\n") else 1),
                     "words": w, "markers": m, "tier": tier, "sha256": hashlib.sha256(raw).hexdigest()})
    rows.sort(key=lambda r: (r["tier"], r["date"], r["deposit"]))
    queue = [r for r in rows if r["deposit"] not in done_n]
    batches, cur, cw = [], [], 0
    for r in queue:
        if cur and cw + r["words"] > a.words:
            batches.append(cur); cur, cw = [], 0
        cur.append(r); cw += r["words"]
    if cur:
        batches.append(cur)
    out = {"what": "The reading queue of the prediction sweep. One row per readable alexanarch deposit; batches are "
                   "what one parallel reader holds. Read under data/reading/READING-PROTOCOL.md.",
           "alexanarch_commit": commit, "word_budget": a.words,
           "counts": {"deposits": len(rows), "already_read": len(done_n & {r["deposit"] for r in rows}),
                      "queued": len(queue), "batches": len(batches),
                      "tiers": {t: sum(1 for r in queue if r["tier"] == t) for t in (1, 2, 3)},
                      "words_queued": sum(r["words"] for r in queue)},
           "batches": [{"batch_id": f"B{i+1:04d}", "tier": b[0]["tier"], "words": sum(r["words"] for r in b),
                        "deposits": b} for i, b in enumerate(batches)]}
    (ROOT / "data/reading/queue.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps(out["counts"]))


if __name__ == "__main__":
    main()
