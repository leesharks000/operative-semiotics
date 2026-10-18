# Reading Protocol — the prediction sweep (v1.3, 2026-10-18)

You are a reader in the archive's prediction sweep. Your batch is a list of deposits of the Crimson
Hexagonal Archive. You read each one IN FULL and record every prediction-bearing passage in it, by shape,
quoted verbatim with its line numbers. You record what you read, how, and what you found — including
when you found nothing. You record your own provenance. Your output is checked mechanically against
the source texts: every quotation, every line number and every read range is verified.

The ruling (Lee Sharks, 2026-10-15): "we need to do a more thorough sweep for timestamped predictions.
we never actually read them" — "parallel reading, but they need to keep track of what theyve read and
havent and how. the agents need to track their own provenance as well."

v1.2 adds shape H, on the ruling (Lee Sharks, 2026-10-15): "yes - we *absolutely* need historical theses, thats one of
the most important and deepest categories."

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

## What to record — the eight shapes

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

H. HISTORICAL THESIS — a claim about the past that the deposit advances as its own and that evidence could
   confirm or refute: who wrote a text, when it was written, which came first, what a passage originally meant,
   how a work was received, what an author was doing. It need not be labelled falsifiable; it is a thesis when
   the deposit argues it rather than reports it. Examples: "Revelation was the first-written book of the New
   Testament" (#556, labelled there as a falsifiable claim); a thesis that Plato and Aristotle are one authorial
   practice divided by name; Socrates as an edition of a received Aristophanic character. Record the thesis at
   its fullest statement, and its stated evidence or test (in "falsifier_quote") where one is given; put the
   period or text concerned in "window". A thesis repeated across deposits is recorded in each deposit that
   argues it (triage links them). Do NOT record: summaries of established scholarship the deposit does not
   contest; other scholars' theses unless the deposit adopts them; the archive's own internal chronology (when a
   deposit was filed — that is D or provenance, not history).

## What NOT to record

- Falsification boilerplate on restored or recovered records (e.g. "Byte fidelity verifiable against the
  live blog URL").
- Satirical or explicitly fictional figures presented as such (e.g. a "pilot study (n=0)").
- Dated observations of what already happened (telemetry, captures) — unless the deposit frames them as
  confirming an earlier prediction (then: shape C).
- Procedural rules with timelines (cooling periods, review windows).
- Quotations of other people's predictions, unless the deposit adopts them as its own.

## Boundary rules (v1.1 — from the pilot: four readers, 37 deposits, and a blind re-reading of eight)

1. ONE FORECAST, ONE FIND. When a deposit states the same forecast several times (stage text, probability
   table, ledger row), record it once — at its fullest statement — and list the other places in "also_at" as
   line ranges. Do not record the same forecast as separate finds.
2. TIMESTAMPED ANCHORS ARE THEIR OWN FIND. A third-party timestamp the deposit points to as proof of when it
   said something — a GitHub issue, a share link, a DOI's date, a filing, a post — is recorded as shape D
   even when it sits inside a forecast passage. Quote the sentence that names the anchor.
3. TAGGED "PREDICTIONS" ABOUT HOW A SYSTEM BEHAVES are G (standing claims) unless they name an event, a date
   or a window, which makes them A.
4. CHECKLISTS AND PLANNED PROBES. An "evidence needed" list, a list of planned probes, or a test battery is
   ONE find of shape F for the whole list, quoted by its heading and first items, with its full line range.
5. A MONITORING CHECK the deposit sets for itself ("track whether X keeps returning Y") is F.
6. QUOTES stay under ~600 characters. For a table, quote the row, not the table.
7. Add to each find: "also_at": [[first, last], ...] (empty list if none).

## Data deposits read by their own-voice fields (X-batches)

Two deposits are JSON datasets too large for any reader to hold: #3 (the capture registry, ~2.3M words) and #4 (the
DOI resolution index). Most of their bulk is machine transcript — AI surfaces speaking, excluded above as other
parties' text — and dated observation or metadata, excluded above. The archive's own voice is in named fields
(reading, analysis, findings, notes; descriptions; change and correction logs). Those fields are extracted verbatim,
record by record, into derived reading texts (data/reading/derived/, built by scripts/reading/derive_voice.py, each
block headed with the record's id and its line in the source file). X-batches are line ranges of those texts; read
the range IN FULL, as above, all shapes A–H, and quote from the derived text. The deposit counts as read only when
every X-batch over it has passed.

## The H back-pass

Deposits read before v1.2 are re-read for shape H alone (batches HB0001…, from data/reading/hpass.json). Read each
deposit IN FULL exactly as above, record ONLY shape-H finds, and set none_found true when the deposit argues no
historical thesis. The other shapes were already recorded by the first reading; do not record them again.

## Pass 2: changed text and attachments (v1.3, R- and A-batches)

The ruling (Lee Sharks, 2026-10-17): "lets do those reading sweeps." Two kinds of text were never read under this
protocol, and pass 2 reads them. The queue is data/reading/pass2-queue.json, built by scripts/reading/build_pass2.py.
Its rows are UNITS, not deposits:

- **R-units: changed text.** The record repair of 2026-10-15/16 changed some deposits' texts after the first pass read
  them. An R-unit is one deposit's current text with the RANGES that hold new words (with three lines of context). Read
  every listed range IN FULL, as above, and record every find inside the ranges, all shapes A–H. You may read outside
  the ranges for context; record a find there only if it continues across a range boundary. Line numbers are those of
  the current file. A find the first pass may already hold is recorded anyway: triage matches it.
- **A-units: attachments.** A file attached to one or more deposits (data/attachments in alexanarch), or the plain text
  converted from a PDF or DOCX. Read it IN FULL, all shapes A–H. The unit names the deposits that carry the
  attachment; a find belongs to them. Code is read as text: a prediction in a comment, docstring or header is a find,
  the code itself is not. For a data file, record only the archive's own prose (notes, descriptions, stated
  predictions), not data values.

Your output has the shape above, with one change: each entry carries `"unit"` (the unit id exactly as queued) in
place of `"deposit"`, and `read_ranges` must cover the unit's ranges. Copy `"deposits"` from the queue row.

## Each find

Quote the passage VERBATIM from the file — exact characters, no paraphrase, no ellipsis inside the quote —
long enough to carry the prediction and its falsifier where one is given (up to ~600 characters; record
the falsifier as a second quote if it is far away). Give the line range of the quote.

## Your output

Write ONE JSON file to the path given in your batch, exactly this shape:

{
  "batch_id": "<given>",
  "protocol": "READING-PROTOCOL v1.2" (v1.3 for pass 2),
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
          "shape": "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H",
          "quote": "<verbatim>",
          "lines": [first, last],
          "falsifier_quote": "<verbatim, or empty>",
          "falsifier_lines": [first, last] or [],
          "window": "<any date, deadline or horizon stated, verbatim; else empty>",
          "points_to": "<for C or D: the earlier deposit/event as named in the text; else empty>",
          "also_at": [],
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
