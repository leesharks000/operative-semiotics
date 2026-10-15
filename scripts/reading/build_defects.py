#!/usr/bin/env python3
"""build_defects.py — collect every record defect the readers noted, for the repair pass after the sweep.

    python3 scripts/reading/build_defects.py

Reads each batch's per-deposit "incidental" and "status_note" fields and the rulings in data/reading/rulings.json,
and writes data/reading/defects.json: one row per deposit with every note, which reading made it, and any ruling.
It collects; it does not classify or repair. The ruling (Lee Sharks, 2026-10-15): "when we finish these passes lets
take this opportunity to repair the many record defects theyve identified."
"""
import json, pathlib

R = pathlib.Path(__file__).resolve().parents[2] / "data/reading"


def main():
    rulings = json.loads((R / "rulings.json").read_text())["rulings"] if (R / "rulings.json").exists() else []
    rows = {}
    for bp in sorted((R / "batches").glob("*.json")):
        if bp.name.endswith((".verified.json", ".audit.json")):
            continue
        out = json.loads(bp.read_text())
        for e in out.get("deposits", []):
            for k in ("incidental", "status_note"):
                t = (e.get(k) or "").strip()
                if t:
                    rows.setdefault(e["deposit"], {"deposit": e["deposit"], "notes": [], "rulings": []})["notes"].append(
                        {"batch_id": out["batch_id"], "field": k, "text": t})
    for ru in rulings:
        for n in ru.get("deposits", []):
            rows.setdefault(n, {"deposit": n, "notes": [], "rulings": []})["rulings"].append(ru)
    out = {"what": "Record defects noted by the sweep's readers (damaged text, wrong or duplicate bodies, version and DOI "
                   "conflicts), collected for the repair pass. Rebuilt by scripts/reading/build_defects.py.",
           "deposits_with_notes": len(rows), "deposits": sorted(rows.values(), key=lambda r: r["deposit"])}
    (R / "defects.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print(len(rows))


if __name__ == "__main__":
    main()
