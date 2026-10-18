#!/usr/bin/env python3
"""build_pass2.py — the second reading pass of the prediction sweep: text the sweep has not read (2026-10-17).

    python3 scripts/reading/build_pass2.py [--alexanarch /home/claude/alexanarch] [--words 35000]

Two kinds of text were never read under READING-PROTOCOL:

  R  CHANGED TEXT. The sweep read the texts of alexanarch at the queue's commit. The record repair of 2026-10-15/16
     then restored bodies and missing parts, so some deposits' texts changed after they were read. For each deposit
     whose current text differs from the text read (sha256 against the queue), the old text is taken from git at the
     queue's commit and compared with the current one: lines aligned first, then words within each changed block. Every current line holding a word the old text
     did not have, at that place, is new text; the new lines, with 3 lines of context either side and runs closer than
     10 lines joined, are the ranges to read. A reflowed paragraph (same words, new line breaks) is not new text.
     #3 and #4 are JSON datasets read through their derived own-voice texts (derive_voice.py): the current derived
     text is written to derived/<n>-voice-p2.md and compared block by block with the derived text that was read.
  A  ATTACHMENTS. The files under alexanarch data/attachments/. Text files are read as they are; PDF and DOCX are
     converted to plain text (pdftotext; pandoc) into derived/attachments/. Excluded, and listed with the reason:
     images and binary data (png, jpg, parquet, gz); a file whose text already stands in a deposit text the sweep
     read, or in a derived own-voice text (30 sampled 10-word runs, 27 or more found there); JSON over 15,000 words
     (machine-written data rows); a file of machine transcripts (other parties' speech, as for #3); the edition of the
     capture registry's commentary (words-no-good), which is #3's own-voice fields, read through its derived texts.
     Each attachment is tied to the deposits that link it (registry fields, deposit texts, the AXN-<hex> folder).

Rows are units (a deposit's new text, or one attachment) with the line ranges to read; batches are cut at 35,000
words, and a unit larger than that is cut into range parts. Writes data/reading/pass2-queue.json. Deterministic for a
given alexanarch commit.
"""
import argparse, difflib, hashlib, json, pathlib, random, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
R = ROOT / "data/reading"
sys.path.insert(0, str(ROOT / "scripts/reading"))
TEXT = {".md", ".txt", ".py", ".yaml", ".yml", ".sh", ".html", ".json", ".jsonl", ".csv", ".tex", ".sha256"}
CONV = {".pdf", ".docx"}
CTX, JOIN = 3, 10
# attachments no registry field or deposit text links, tied by title to the deposit whose text they are a source of
# (the earliest of a same-title pair); New Human Compiled names no deposit and is read with none
DEPOSIT_OF = {"recovered-sources/EA-LOGOS-01_The_Word_That_Became_Text.md": 626,
              "recovered-sources/EA-LOGOS-02_Prolegomena_to_the_Historical_Logos.md": 625,
              "recovered-sources/THE-SEALED-ROOM-v1.2.md": 466, "recovered-sources/cleis.md": 1165,
              "recovered-sources/The-Magistrate-Refuses-the-Mirror.md": 772,
              "recovered-sources/botanical-effective-act-academic.md": 37,
              "recovered-sources/f01-FBDP-v1.2-academic.md": 571,
              "recovered-sources/ASW_Kindle_RexFraction_2026.md": 498,
              "ea-lo-collapse-diagnostic-01/EA-LO-COLLAPSE-DIAGNOSTIC-01.pdf": 1573,
              "ea-measures-report-01/collapse_diagnostic.py": 1573}
norm = lambda s: " ".join(s.split())


def git_show(ax, commit, rel):
    r = subprocess.run(["git", "-C", str(ax), "show", f"{commit}:{rel}"], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def new_lines(old, new):
    """Current-file line numbers (1-based) that hold a word the old text did not have at that place. Lines are aligned
    first (whitespace-normalized); within each changed block the words are compared, so a reflowed paragraph counts
    only where its words differ."""
    ol, nl = old.split("\n"), new.split("\n")
    sm = difflib.SequenceMatcher(None, [norm(x) for x in ol], [norm(x) for x in nl], autojunk=False)
    hit = set()
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag not in ("replace", "insert"):
            continue
        ow = " ".join(ol[i1:i2]).split()
        nw, where = [], []
        for k in range(j1, j2):
            for w in nl[k].split():
                nw.append(w); where.append(k + 1)
        if not ow:
            hit.update(where); continue
        wm = difflib.SequenceMatcher(None, ow, nw, autojunk=False)
        for t2, a1, a2, b1, b2 in wm.get_opcodes():
            if t2 in ("replace", "insert"):
                hit.update(where[b1:b2])
    return sorted(hit), len(nl) - (1 if nl and nl[-1] == "" else 0)


def ranges_of(lines, total):
    out = []
    for n in lines:
        a, b = max(1, n - CTX), min(total, n + CTX)
        if out and a <= out[-1][1] + JOIN:
            out[-1][1] = max(out[-1][1], b)
        else:
            out.append([a, b])
    return out


def words_in(text_lines, rr):
    return sum(len(text_lines[i - 1].split()) for a, b in rr for i in range(a, b + 1) if i - 1 < len(text_lines))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--alexanarch", default="/home/claude/alexanarch")
    ap.add_argument("--words", type=int, default=35000)
    a = ap.parse_args()
    ax = pathlib.Path(a.alexanarch)
    head = subprocess.run(["git", "-C", str(ax), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    q = json.loads((R / "queue.json").read_text())
    old_commit = q["alexanarch_commit"]
    rows = {}
    for b in q["batches"]:
        for d in b["deposits"]:
            rows[d["deposit"]] = d
    units, excluded = [], []

    # R: changed text
    import derive_voice as dv
    for n in sorted(rows):
        m = rows[n]; p = pathlib.Path(m["path"])
        if not p.exists():
            excluded.append({"unit": f"R{n}", "deposit": n, "path": str(p), "reason": "text file no longer present"}); continue
        raw = p.read_bytes()
        if hashlib.sha256(raw).hexdigest() == m["sha256"]:
            continue
        rel = str(p.relative_to(ax))
        oldb = git_show(ax, old_commit, rel)
        if oldb is None or hashlib.sha256(oldb).hexdigest() != m["sha256"]:
            excluded.append({"unit": f"R{n}", "deposit": n, "path": str(p),
                             "reason": "the text read is not at the queue's commit; re-read in full"})
            oldb = b""
        if n in dv.SPECS:
            newt = "\n".join(dv.render(n, dv.SPECS[n])) + "\n"
            dp = R / "derived" / f"{n:04d}-voice-p2.md"
            dp.write_text(newt)
            oldt = (R / "derived" / f"{n:04d}-voice.md").read_text()
            hit, total = new_lines(oldt, newt)
            path, text = dp, newt
        else:
            text = raw.decode("utf-8", "replace")
            hit, total = new_lines(oldb.decode("utf-8", "replace"), text)
            path = p
        if not hit:
            continue
        rr = ranges_of(hit, total)
        L = text.split("\n")
        units.append({"unit": f"R{n}", "kind": "changed text" + (" (derived own-voice)" if n in dv.SPECS else ""),
                      "deposit": n, "deposits": [n], "title": m.get("title"), "date": m.get("date"), "path": str(path),
                      "lines_total": total, "ranges": rr, "new_lines": len(hit), "words": words_in(L, rr),
                      "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})

    # A: attachments
    reg = json.loads((ax / "data/registry.json").read_text())["deposits"]
    hexmap = {d.get("hex"): d.get("deposit_number") for d in reg if d.get("hex")}
    refs = {}
    for d in reg:
        for mm in re.findall(r"data/attachments/([^\"\s\)\]\\]+)", json.dumps(d, ensure_ascii=False)):
            refs.setdefault(mm.rstrip("/.,;"), set()).add(d.get("deposit_number"))
    for tp in sorted((ax / "data/texts").glob("*.md")):
        t = tp.read_text(encoding="utf-8", errors="replace")
        if "attachments/" not in t:
            continue
        hx = re.match(r"AXN-([0-9A-F]{4})-text", tp.name)
        dn = hexmap.get(hx.group(1)) if hx else None
        for mm in re.findall(r"attachments/([^\s\)\]\"'`<>]+)", t):
            if dn:
                refs.setdefault(mm.rstrip("/.,;:"), set()).add(dn)
    seated = []
    for d in rows.values():
        try:
            seated.append(norm(pathlib.Path(d["path"]).read_text(encoding="utf-8", errors="replace")))
        except Exception:
            pass
    for dp in sorted((R / "derived").glob("*-voice*.md")):
        seated.append(norm(dp.read_text(encoding="utf-8", errors="replace")))
    big = "\n".join(seated)
    conv = R / "derived" / "attachments"
    att = sorted(x for x in (ax / "data/attachments").rglob("*") if x.is_file())
    for f in att:
        rel = str(f.relative_to(ax / "data/attachments")); ext = f.suffix.lower()
        deps = set()
        for r, v in refs.items():
            if rel == r or rel.startswith(r.rstrip("/") + "/") or r.startswith(rel):
                deps |= v
        hx = re.match(r"AXN-([0-9A-F]{4})", rel)
        if hx and hx.group(1) in hexmap:
            deps.add(hexmap[hx.group(1)])
        if rel in DEPOSIT_OF:
            deps.add(DEPOSIT_OF[rel])
        deps = sorted(x for x in deps if x)
        unit = "A:" + rel
        if ext not in TEXT and ext not in CONV:
            excluded.append({"unit": unit, "deposits": deps, "path": str(f), "reason": f"not text ({ext or 'no extension'})"}); continue
        path = f
        if ext in CONV:
            out = conv / (rel + ".txt"); out.parent.mkdir(parents=True, exist_ok=True)
            if ext == ".pdf":
                subprocess.run(["pdftotext", "-enc", "UTF-8", str(f), str(out)], check=False)
            else:
                subprocess.run(["pandoc", "-t", "plain", "--wrap=none", str(f), "-o", str(out)], check=False)
            if not out.exists():
                excluded.append({"unit": unit, "deposits": deps, "path": str(f), "reason": "conversion failed"}); continue
            path = out
        text = path.read_text(encoding="utf-8", errors="replace")
        L = text.split("\n"); total = len(L) - (1 if L and L[-1] == "" else 0)
        nw = len(text.split())
        if nw == 0:
            excluded.append({"unit": unit, "deposits": deps, "path": str(path), "reason": "no text extracted"}); continue
        if rel.startswith("words-no-good/capture-registry-") and "commentary" in rel:
            excluded.append({"unit": unit, "deposits": deps, "path": str(path), "words": nw,
                             "reason": "an edition of the capture registry (#3) commentary: its readings, analyses and findings are "
                                       "read through #3's derived own-voice texts (38 of 60 sampled runs verbatim there; the rest are "
                                       "the edition's headings and the records' one-line descriptions)"}); continue
        if "transcripts" in pathlib.Path(rel).name.lower():
            excluded.append({"unit": unit, "deposits": deps, "path": str(path), "words": nw,
                             "reason": "machine transcripts (other parties' speech: What NOT to record)"}); continue
        if ext in (".json", ".jsonl", ".csv") and nw > 15000:
            excluded.append({"unit": unit, "deposits": deps, "path": str(path), "words": nw,
                             "reason": "data file over 15,000 words (machine-written rows)"}); continue
        w = text.split()
        if len(w) >= 40:
            rnd = random.Random(rel)
            starts = [rnd.randrange(0, len(w) - 10) for _ in range(30)]
            found = sum(1 for s in starts if " ".join(w[s:s + 10]) in big)
            if found >= 27:
                excluded.append({"unit": unit, "deposits": deps, "path": str(path), "words": nw,
                                 "reason": f"text already stands in a deposit text the sweep read ({found}/30 sampled runs)"}); continue
        units.append({"unit": unit, "kind": "attachment", "deposit": deps[0] if deps else None, "deposits": deps,
                      "title": rel, "path": str(path), "source": str(f), "lines_total": total, "ranges": [[1, total]],
                      "words": nw, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})

    # cut units larger than the budget into range parts, then pack batches
    parts = []
    for u in units:
        if u["words"] <= a.words:
            parts.append(u); continue
        L = pathlib.Path(u["path"]).read_text(encoding="utf-8", errors="replace").split("\n")
        k = 0; cur, cw = [], 0
        lines = [i for rr in u["ranges"] for i in range(rr[0], rr[1] + 1)]
        for i in lines:
            lw = len(L[i - 1].split()) if i - 1 < len(L) else 0
            if cw and cw + lw > a.words and (i - 1 >= len(L) or not L[i - 1].strip() or cw + lw > a.words * 1.15):
                k += 1; parts.append({**u, "unit": f"{u['unit']}#{k}", "ranges": _runs(cur), "words": cw})
                cur, cw = [], 0
            cur.append(i); cw += lw
        if cur:
            k += 1; parts.append({**u, "unit": f"{u['unit']}#{k}", "ranges": _runs(cur), "words": cw})
    batches = []
    for kind, pre in (("R", "R"), ("A", "A")):
        cur, cw = [], 0
        for u in [x for x in parts if x["unit"].startswith(kind)]:
            if cur and cw + u["words"] > a.words:
                batches.append({"batch_id": f"{pre}{len([b for b in batches if b['batch_id'][0] == pre]) + 1:04d}", "units": cur, "words": cw})
                cur, cw = [], 0
            cur.append(u); cw += u["words"]
        if cur:
            batches.append({"batch_id": f"{pre}{len([b for b in batches if b['batch_id'][0] == pre]) + 1:04d}", "units": cur, "words": cw})
    out = {"what": "Pass 2 of the prediction sweep: the text the first pass did not read. Built by scripts/reading/build_pass2.py; "
                   "see its docstring for what is new text, what is an attachment, and what is excluded.",
           "read_commit": old_commit, "alexanarch_commit": head, "word_budget": a.words,
           "counts": {"R_units": sum(1 for u in units if u["unit"].startswith("R")),
                      "R_words": sum(u["words"] for u in units if u["unit"].startswith("R")),
                      "A_units": sum(1 for u in units if u["unit"].startswith("A")),
                      "A_words": sum(u["words"] for u in units if u["unit"].startswith("A")),
                      "excluded": len(excluded), "batches": len(batches)},
           "batches": batches, "excluded": excluded}
    (R / "pass2-queue.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps(out["counts"]))


def _runs(ls):
    out = []
    for i in ls:
        if out and i == out[-1][1] + 1:
            out[-1][1] = i
        else:
            out.append([i, i])
    return out


if __name__ == "__main__":
    main()
