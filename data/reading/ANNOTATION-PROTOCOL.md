# Annotation protocol v1.0 — dates, mode, falsifier (2026-10-18)

The prediction index records claims, each with one or more verbatim statements (finds) from the archive's deposits. Two
reviews of the draft deposit EA-PREDICTION-INDEX-01 (ChatGPT, Kimi; adopted by Lee Sharks 2026-10-18, "adopted on all")
showed three things the first reading did not ask. This pass asks them, claim by claim. You answer only the questions
each item lists in "tasks". Your answers are verified mechanically: every quote must be verbatim at its lines.

Your batch is an entry of data/reading/annotate-queue.json. Each item gives a claim, its tier, its tasks, and its
statements: find id, deposit, recorded date, path of the source text, `lines_now` (where the quote stands in that file
now — use these, not older line numbers), the quote, and any falsifier already recorded.

## Reading

For every statement, read with the Read tool at least `lines_now` and 40 lines either side (clipped to the file). For a
`dates` item, also read the opening of the file (lines 1–60) and any header, dateline, post heading or editorial note
that governs the statement's lines. For a `falsifier` item, also look in the file for a falsification section
("Falsification", "Falsifiers", "What would refute", "Conditions") and read it if present. Read more whenever the
question needs it. Record every range you read in `read_ranges`. Do not substitute search for reading; grep may find a
heading, but the answer comes from reading the lines.

## Task `dates` — when was this said, and does it look back?

The index used to give every statement its deposit's recorded date. That is wrong where a deposit carries material of
several dates: a 2014 correspondence deposited with a 2026 introduction; a post dated four days after the container's
date; an editor's note identifying what an earlier passage "anticipated". For EACH statement of the claim, answer:

- `stated`: the date the quoted words were written or first stated, as precisely as the evidence allows ("2014",
  "2014-05", "2014-05-11"), or null when nothing establishes it.
- `stated_basis`, one of:
  - `in-text` — the text dates the passage itself: a dated post or entry heading, a dateline, "written on 11 May 2014".
    Give the dating words in `basis_quote` / `basis_lines`.
  - `container` — nothing in or around the passage dates it otherwise; the deposit's recorded date stands.
  - `framing` — the passage belongs to a later layer than the material it presents (an introduction, preface,
    editor's or archivist's note, commentary, abstract, record description). Give the framing's date in `stated` if
    the text gives one (quote it), else null.
  - `unknown` — the passage's date cannot be told from the text and the container date is doubtful.
- `retrospective`: true when the passage identifies the significance of something earlier: says it anticipated,
  predicted, prefigured, was the earliest, came "years before", "would become". Otherwise false.
- `looks_back_to` (when retrospective): `what` (a few words: the earlier text or event), `date` (its date as the text
  gives it, or null), and optionally `quote` / `lines` where the text names it.

The innocent reading first: most passages are stated when their deposit says (`container`, not retrospective). Mark
`framing` or `in-text` only on evidence you quote.

## Task `mode` — what kind of anticipation is this?

Shape E (speculative specification) holds forecasts made by describing a thing. They are not all the same act, and a
machine reading the index must not turn a scenario into a failed literal forecast, nor count a resemblance as a hit.
Give ONE `mode` for the claim:

- `empirical-forecast` — says that something will happen or be the case, in the world, and means it literally.
- `design-specification` — describes a product, protocol, system or instrument in enough detail that its appearance
  (built by anyone) is the outcome: a patent-poem, a fictional product sheet, a spec.
- `scenario` — narrates a possible future as one path among others ("scenario, not a prediction"); its outcome is
  whether the conditions it names come to hold.
- `fictional-report` — a report written from inside a fictional future or alternate present (a dated future
  document, a retrocausal history); its dates are narrative anchors, not forecasts.
- `performative-anticipation` — the text anticipates in order to act on its present: a test of present uptake or
  retrieval ("the test is present basin depth"), a summons, a declaration that works by being read.
- `vision` — a dream, premonition or vision recorded as such.

Then `fulfilment`: one sentence, in your words, saying what outcome would count as fulfilment for THIS claim in this
mode (e.g. "a product with these features exists, built by anyone"; "present retrieval systems compose from the
named terms"). Where the source itself characterises its mode ("This is not prediction.", "scenario, not a
prediction", "the patent has done its work"), quote that in `basis_quote` / `basis_lines` / `basis_path`.

## Task `falsifier` — what would show the standing claim false?

A standing claim (shape G) was defined as stated with its falsifying condition; 673 were recorded without one. For the
CLAIM (all its statements together), answer:

- `kind`, one of:
  - `stated` — a source text states a condition under which this claim would be false or weakened: in the passage, near
    it, or in the deposit's falsification section where that section covers this claim. Quote it verbatim
    (`quote`, `lines`, `path`).
  - `recoverable` — no condition is stated, but the claim's own wording entails an observation that would refute it.
    Write that observation in `reader_condition`, beginning "Reader-supplied: ". It will be shown as the reader's,
    never as the source's.
  - `none` — no condition is stated and none follows from the wording (the claim is definitional, programmatic, or
    too general).

## Output

Write ONE JSON file, data/reading/batches/<ID>.json:

```json
{
  "batch_id": "<ID>", "protocol": "ANNOTATION-PROTOCOL v1.0",
  "started_at": "<date -u>", "finished_at": "<date -u>", "self_description": "<what you are, or 'unknown'>",
  "items": [
    {
      "claim": "<claim id, exactly as queued>",
      "read_ranges": [{"path": "<path>", "ranges": [[1, 60], [300, 420]]}],
      "dates": {"statements": [
        {"find": "<find id>", "stated": "2014-05-11" | null, "stated_basis": "in-text" | "container" | "framing" | "unknown",
         "basis_quote": "<verbatim>" | null, "basis_lines": [a, b] | null,
         "retrospective": true | false,
         "looks_back_to": {"what": "<few words>", "date": "<date>" | null, "quote": "<verbatim>" | null, "lines": [a, b] | null} | null,
         "note": "<one line>"}
      ]},
      "mode": {"mode": "<one of the six>", "fulfilment": "<one sentence>", "basis_quote": "<verbatim>" | null,
               "basis_lines": [a, b] | null, "basis_path": "<path>" | null, "note": "<one line>"},
      "falsifier": {"kind": "stated" | "recoverable" | "none", "quote": "<verbatim>" | null, "lines": [a, b] | null,
                    "path": "<path>" | null, "reader_condition": "Reader-supplied: …" | null, "note": "<one line>"}
    }
  ]
}
```

Include only the keys of the item's tasks. `basis_quote`/`basis_lines` in `dates` refer to that statement's own path.
Take every quote by slicing the source lines with a scratch python script, so it is verbatim and one contiguous slice
inside its stated lines. Quotes in your output are evidence; your sentences (`note`, `fulfilment`, `reader_condition`,
`what`) are your reading and are kept as such.
