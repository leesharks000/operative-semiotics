# Review Protocol: the subject pages after the moves (v1.0, 2026-10-17)

## Why there is a second pass

The naming readers titled 153 pages. They also moved about 200 claims to the pages where those claims belong, so many
pages now hold claims their reader never saw, and have lost claims their description mentions. The readers flagged about
40 pages as holding two or more subjects.

This pass reads each page as it now stands and makes it one subject under one true title. The ruling it serves
(Lee Sharks, 2026-10-17): pages "by category ... 100-200, maybe - but not thousands".

## Your batch

Your batch is the entry with your `batch_id` in `data/index/review-queue.json`. For each page it gives:

- the current title, description and line;
- the naming reader's note;
- every claim now on the page, with its tier, registration, deposit title, series and the first 700 characters of its
  statement;
- `moved_in`: the claims that arrived by a move.

Read every claim.

## What to write, per page

- `title`, `description`, `line`: keep them if they fit the page as it now stands, and rewrite them if they do not. The
  rules are those of `NAMING-PROTOCOL.md`:
  - a title of at most 80 characters, specific to the subject;
  - a description of two to four declarative sentences, with no claim the page's claims do not make;
  - a line from the archive's own lines.
- `split`: use this when the page holds two or more subjects. List each extra page as
  `{"title", "slug", "description", "line", "claims": [...]}`. The claims you list leave this page for the new one, and
  every claim stays on exactly one page.
  - Split only where each part would hold at least 6 claims and stand as one subject.
  - Do not split for its own sake. The index aims at 100 to 200 pages in all, and there are 153 now.
  - Mixed stray claims that belong nowhere on the page stay where they are. Name them in `note`.
- `note`: anything a later pass must know.

## Output

Write `data/index/review/<ID>.json`:

```
{"batch_id": "<ID>", "protocol": "REVIEW-PROTOCOL v1.0", "reader": {...},
 "pages": [{"page": "P001", "title": "...", "slug": "...", "description": "...", "line": "...", "split": [], "note": ""}]}
```

Check it with `python3.12 /home/claude/operative-semiotics/scripts/index/review_verify.py <ID>`, and fix every failure it
reports until it prints VERIFIED.

Keep scratch scripts in `<scratchpad>/<ID>/`. Do not edit any other file and do not run git.
