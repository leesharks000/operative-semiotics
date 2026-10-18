# Recall adjudication v1.0 (2026-10-18)

The recall audit re-read 40 random deposits on a broader, differently worded brief (RECALL-BRIEF.md). 272 of its
passages overlap no find of the first reading. You decide, for each, whether the first reading MISSED a passage its own
protocol required it to record. Read data/reading/READING-PROTOCOL.md (v1.3) in full first: its eight shapes, "What NOT
to record", and the boundary rules. That protocol, not the audit brief, is the standard.

Your batch is an entry of data/reading/recall-adjudicate-queue.json. Each item gives the deposit, the file path, the
audit passage (quote, lines, the auditor's kind and why), whether it is `near` a first-reading find (within 15 lines),
and every first-reading find in that file (find id, shape, lines, quote).

For each item, read the passage's lines and at least 30 lines either side with the Read tool (and more where the
judgement needs it), recording the ranges. Then give ONE verdict:

- `covered` — a first-reading find already records this commitment: the same claim at another place in the deposit
  (the protocol's ONE FORECAST, ONE FIND rule, `also_at`), or the find's quote is a fuller statement of it. Name the
  find in `find`.
- `missed` — the protocol requires this passage to be recorded, as shape `shape`, and no first-reading find records it.
  If two items of your batch are the same missed commitment, mark the second `same_as` the first item's id.
- `excluded` — the passage is a commitment of a kind the protocol excludes (name the rule in `rule`, e.g. "quotations
  of other people's predictions", "dated observations of what already happened", "procedural rules with timelines",
  "falsification boilerplate", "summary of established scholarship", "satirical figure presented as such").
- `not-a-claim` — on reading, the passage commits to nothing checkable (description, definition, programme statement).

Be exact rather than generous either way: the number this produces is the sweep's measured recall.

Write data/reading/batches/<ID>.json:

```json
{"batch_id": "<ID>", "protocol": "RECALL-ADJUDICATE v1.0", "started_at": "<date -u>", "finished_at": "<date -u>",
 "self_description": "<what you are, or 'unknown'>",
 "items": [{"item": "<item id, exactly>", "read_ranges": [[a, b]], "verdict": "covered" | "missed" | "excluded" | "not-a-claim",
            "find": "<find id>" | null, "shape": "A".."H" | null, "rule": "<rule>" | null, "same_as": "<item id>" | null,
            "note": "<one line: why>"}]}
```
