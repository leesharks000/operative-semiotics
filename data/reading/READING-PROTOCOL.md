# Reading Protocol — the prediction sweep (v1.0, 2026-10-15)

You are a reader in the archive's prediction sweep. Your batch is a list of deposits of the Crimson
Hexagonal Archive. You read each one IN FULL and record every prediction-bearing passage in it, by shape,
quoted verbatim with its line numbers. You record what you read, how, and what you found — including
when you found nothing. You record your own provenance. Your output is checked mechanically against
the source texts: every quotation, every line number and every read range is verified.

The ruling (Lee Sharks, 2026-10-15): "we need to do a more thorough sweep for timestamped predictions.
we never actually read them" — "parallel reading, but they need to keep track of what theyve read and
havent and how. the agents need to track their own provenance as well."

## How to read

1. For each deposit, Read its text file from the first line to the last, in consecutive chunks (the
   Read tool with offset and limit). Record every range you read as [first_line, last_line]. The ranges
   must cover the whole file. Do not search the file instead of reading it; a search is not a reading.
2. If you cannot finish a deposit, record it as `partial` with the ranges you did read, and say why.
   If you skip one, record `skipped` with the reason. Never record `read` for a file you did not read
   to its last line.
3. Read as a reader, not a grep. The shapes below are often carried by genre rather than vocabulary:
   a speculative patent, a memo written from the future, a poem, a protocol. The pilot reading found the
   strongest material in deposits with almost no predictive words in them.

## What to record — the seven shapes

A. REGISTERED FORECAST — an explicit forecast the deposit itself frames as a prediction: numbered
   (P1, Prediction 3, O-1), dated or windowed, usually with a falsifier. Example: "P1 — Entity dissolution
   becomes a named, measured phenomenon outside this archive by mid-2027 … Falsifier: no external
   literature names the phenomenon by July 2027." (#172)

B. EMBEDDED FORECAST — a forecast stated in the prose, outside any list or ledger the deposit keeps.
   Example: "Google will initially implement weak compliance … This tiered compliance will itself become
   a controversy." (#835, not in its own ledger)

C. CONFIRMATION RECORD — the deposit says an EARLIER prediction came true (or failed). Record the claim
   and what it points back to (deposit number, title, DOI or date as given). Example: "In February 2026,
   this archive published a forecast … Four months later, the forecast is telemetry." (#172); "Erasure Skew
   v3 predicted this event's most striking feature nine weeks early" (#1463).

D. PRIORITY CLAIM — the deposit records that the archive named or formalized something before the world
   performed or named it. Not a forecast: a chronology. Example: the RCF deposit of January 2026 before
   Citrini's memo of 22 February 2026 (#519).

E. SPECULATIVE SPECIFICATION — a forecast made by describing the thing: a patent-poem, a fictional product,
   a scenario, satire. It resolves when the thing appears. Example: "If you recognize DashFace in a product
   that already exists, the patent has done its work." (#713)

F. UNBUILT INSTRUMENT OR TEST — a measurement, test, benchmark or tool specified but not run or built,
   with what it would measure. Example: the matched-pair OKF test (#835); "Run the stack once, completely,
   on one capture" (#1463).

G. STANDING FALSIFIABLE CLAIM — a claim about how a system behaves, stated with the condition that would
   falsify it, not a forecast of an event. Example: "Compositional bystanding occurs when … this is falsified
   if top-ranked sources are proportionally represented in AI-generated summaries." (#863)

## What NOT to record

- Falsification boilerplate on restored or recovered records (e.g. "Byte fidelity verifiable against the
  live blog URL").
- Satirical or explicitly fictional figures presented as such (e.g. a "pilot study (n=0)").
- Dated observations of what already happened (telemetry, captures) — unless the deposit frames them as
  confirming an earlier prediction (then: shape C).
- Procedural rules with timelines (cooling periods, review windows).
- Quotations of other people's predictions, unless the deposit adopts them as its own.

## Each find

Quote the passage VERBATIM from the file — exact characters, no paraphrase, no ellipsis inside the quote —
long enough to carry the prediction and its falsifier where one is given (up to ~600 characters; record
the falsifier as a second quote if it is far away). Give the line range of the quote.

## Your output

Write ONE JSON file to the path given in your batch, exactly this shape:

{
  "batch_id": "<given>",
  "protocol": "READING-PROTOCOL v1.0",
  "reader": {
    "role": "parallel reader, prediction sweep",
    "self_description": "<what you are, as you understand it: assistant, model if known to you; say 'unknown' rather than guess>",
    "started_at": "<ISO time when you began>",
    "finished_at": "<ISO time when you wrote this file>",
    "tools_used": ["Read", "..."]
  },
  "deposits": [
    {
      "deposit": 835,
      "path": "<the text path you read>",
      "lines_total": <number of lines in the file>,
      "read_ranges": [[1, 400], [401, 574]],
      "status": "read" | "partial" | "skipped",
      "status_note": "<why, if partial or skipped; else empty>",
      "genre_observed": "<one phrase: what kind of text this actually is>",
      "finds": [
        {
          "shape": "A" | "B" | "C" | "D" | "E" | "F" | "G",
          "quote": "<verbatim>",
          "lines": [first, last],
          "falsifier_quote": "<verbatim, or empty>",
          "falsifier_lines": [first, last] or [],
          "window": "<any date, deadline or horizon stated, verbatim; else empty>",
          "points_to": "<for C or D: the earlier deposit/event as named in the text; else empty>",
          "note": "<one line, your reading: why this is this shape; anything uncertain>"
        }
      ],
      "none_found": true | false,
      "incidental": "<anything a later reader must know: damaged text, missing sections, duplicated body; else empty>"
    }
  ]
}

`none_found` is true only when you read the whole file and it carries no find. An empty `finds` list with
`none_found` false is a contradiction and will be flagged.

Do not edit any file other than your output file. Do not summarise the deposits. Record; do not judge
whether a prediction came true — that is triage, later.
