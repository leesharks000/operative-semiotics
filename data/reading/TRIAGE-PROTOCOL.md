# Triage Protocol: the prediction sweep's second pass (v1.1, 2026-10-18)

The ruling (Lee Sharks, 2026-10-17): "lets do the triage pass."

The sweep (READING-PROTOCOL.md v1.2) read all 1,616 readable deposits and recorded 6,162 verified finds in eight shapes.
It left two things to triage:

- "A thesis repeated across deposits is recorded in each deposit that argues it (triage links them)."
- A confirmation record (shape C) records "what it points back to".

Triage links. It does not judge whether a prediction came true, and it does not re-read deposits for new finds. Every
link it makes is checked mechanically against the finds and the source texts.

## What is already done mechanically

Built by `scripts/reading/triage_base.py`, `triage_cluster.py` and `triage_queue.py`, in `data/reading/triage/`:

- **Find ids.** `F<deposit>.<shape><n>`, where n is the find's order among that deposit's finds of that shape (`finds.ids.jsonl`).
- **Pointers.** For each C find, the deposits its `points_to` names: by number, DOI, AXN or quoted title, or "self" for
  "this deposit". Each comes with up to six candidate finds in the target, ranked by word overlap (`pointers.json`).
- **Restatements.** Finds in different deposits whose quotes are near-verbatim (TF-IDF cosine ≥ 0.85) are joined
  without judgment, each join recorded with its score (`restatements.json`).
- **Candidate pairs.** Pairs with cosine from 0.35 to below 0.85 are left for judgment (`candidate-pairs.json`).

## Scratch files

Keep your scratch scripts in your own folder, `<scratchpad>/<batch id>/`. Readers working in a shared folder have
overwritten each other's helper scripts.

## Your batch

Your batch is the entry with your `batch_id` in `data/reading/triage/queue.json`. Each item quotes every find in full,
with its deposit, date, title and the path of the deposit's text. Read each item whole. Where a judgment needs context
the quote does not carry, open the deposit's text at the find's lines and read around them, then record the range you
read. You may look up deposits by title in `data/reading/triage/deposit-titles.json` and look up finds in
`data/reading/finds.jsonl` joined with `triage/finds.ids.jsonl`. A lookup finds a record; it is not a reading of it.

## TC: a confirmation record

The question is what the deposit says came true or failed, and where that earlier statement is. For each item, record:

- `target_kind`, one of:
  - `find`: one or more finds state the earlier prediction or claim
  - `deposit`: an archive deposit with no find that states it, because it was not a prediction-bearing passage under the
    sweep's protocol (a poem, a book, a capture)
  - `self`: the same deposit, earlier in it
  - `external`: outside the archive (a book's ISBN, a third-party post)
  - `unlocated`: you looked and could not find it
- `links`: a list of `{"find": <id>, "claimed": "came_true" | "partly" | "failed" | "pending"}`. The `claimed` value is
  what the C deposit claims, not your verdict. `pending` means the deposit says the matter is still running.
- `claimed`, at the decision level, for a target that is not a find (`deposit`, `self`, `external`, `unlocated`): the same
  vocabulary, plus `disclaimed` for a deposit that records a correspondence but says it is not a fulfilment.
- `deposit`: the deposit number, when `target_kind` is `deposit` or `self`.
- `external`: a short description, when `target_kind` is `external`.
- `evidence`: for each link, a verbatim phrase (8 to 200 characters) from the linked find's quote that carries the
  earlier claim. For `deposit` and `self`, give a phrase from the deposit's text with its lines.
- `basis`: one sentence.
- `read`: any text ranges you opened, as `[[deposit, first, last], ...]`.

A C find can name several earlier things. Link each one.

## TE: a candidate pair

Decide one of:

- `same`: one claim, stated twice. A reader of the index should see it as one prediction with two statements.
- `variant`: the same claim changed in a way that matters for checking it: the window moved, the scope narrowed or
  widened, the falsifier changed, or the claim was reversed. Say what changed in `change`.
- `contains`: one find is a list, a ledger or a battery that includes the other's claim as one of its members. Say
  which in `container` ("a" or "b"). The member is not merged with the list, because that would pull the list's
  other members into one claim.
- `related`: distinct claims on one subject, such as two predictions in one series or a claim and its test.
- `distinct`: the shared words are boilerplate or a common phrase, and the claims are not related.

Give `basis` in one sentence. Where it decides the call, quote the differing phrase from each side as `evidence_a` and
`evidence_b`, verbatim, from the find's quote or its falsifier quote. A `same` needs no evidence. When in doubt between `same` and `variant`, choose `variant`: the index keeps both statements
either way, and a variant also keeps the change.

## TR: a register card or an intake item

The question is which finds state this card's prediction. Record:

- `match`, one of:
  - `found`: one or more finds state it
  - `partial`: a find states part of it, or a weaker form
  - `not_found`: the source deposit was read and no find states it
  - `excluded`: the text exists, but the reading protocol's "What NOT to record" rules leave it out. Name the rule in `rule`.
  - `no_source`: the card gives no archive deposit, and a search of the finds turns up none that states it. When the
    card gives no deposit but a search finds the claim, record `found` or `partial` and say in `basis` that the card
    names no deposit.
- `finds`: the matching find ids.
- `evidence`: for each find, a verbatim phrase from its quote.
- `basis`: one sentence.
- `read`: any ranges you opened.

Where a card's deposit is not given, or its finds are capped at 40 in the queue, search `finds.jsonl` by deposit.

Register cards also carry `cls`, `status` and the rest. Do not change them. Record only the crosswalk.

## Texts changed since the reading

The record repair changed some deposit texts after the sweep read them, so a find's recorded lines may no longer
match the current file. Locate the quote in the current text, and record your read ranges in current-file lines.
`triage/currency.json` records, for each find, whether its quote is still at its lines, at other lines, or gone.

## TN: a find of reading pass 2 (v1.1)

The ruling (Lee Sharks, 2026-10-18): "lets fo that triage pass". Reading pass 2 read the text the record repair added
and the deposits' attachments (READING-PROTOCOL v1.3). Its finds now join an index that already holds about 4,100
claims, grouped and joined by the triage, topical and join passes. Each TN item is one pass-2 find (`find`, quoted in
full; `path` is the file it was read from) and the six existing claims nearest it in wording (`candidates`: the claim's
id, tier, registration, title, first statement and falsifier, and how many statements it has). Read the find, and the
candidates, and decide:

- `same`: the find states one of these claims. Give `claim`.
- `variant`: it states one of them, changed in a way that matters for checking it (window, scope, falsifier, reversal).
  Give `claim` and `change`.
- `in`: the claim is a list, ledger or battery and the find is one of its members. Give `claim`.
- `contains`: the find is a list, ledger or battery and the claim is one of its members. Give `claim`.
- `related`: distinct, but on the same subject: a claim and its test, or two of one series. Give `claims` (a list).
- `new`: none of these. The find becomes a claim of its own.

For `same`, `variant`, `in` and `contains`, give `evidence_find` (a verbatim phrase of 8 to 400 characters from the
find's quote or falsifier) and `evidence_claim` (a verbatim phrase from the claim's statement or falsifier as given
in the candidate; the verifier also accepts a phrase from any of the claim's other statements). When in doubt between
`same` and `variant`, choose `variant`; between `same` and `new`, choose `new` unless the find plainly states the claim.

The nearest claims are found by wording; a claim restated in other words may not be among them. If you know the claim
it states from elsewhere in the index, you may give a `claim` that is not a candidate. Look claims up in
`data/reading/triage/claims.json`.

Give `basis` in one sentence. `read` may name an attachment by its path: `[["/path/to/file", first, last]]`.

Pass-2 confirmation records come as TC items (batches TCP…), exactly as above.

## Output

Write `data/reading/triage/batches/<ID>.json`:

```
{"batch_id": "<ID>", "kind": "TC|TE|TR|TN", "protocol": "TRIAGE-PROTOCOL v1.1",
 "reader": {"self_description": "...", "started_at": "...", "finished_at": "..."},
 "decisions": [{"item": "<item>", ...fields above...}],
 "observations": ["anything a later pass must know"]}
```

Make exactly one decision for every item in the batch, in order. Take every evidence phrase by copying it out of the
quote with a script, so it is exact. Use `date -u` for the times. Use "unknown" rather than guess. Do not edit any other
file. When two deposits seem to contradict each other, record it as an observation, not an error: the archive's apparent
contradictions can be deliberate structure. Never copy a credential, token or key string into your output.

## What follows

`scripts/reading/triage_verify.py` checks each batch. Then `scripts/reading/triage_assemble.py` builds the claims:

- each group of `same` finds and restatements becomes one claim, registered at its earliest statement;
- variants are kept as dated states of that claim;
- C and D finds are attached as evidence.

Lexical candidates miss a claim restated in different words. A topical pass, by subject within each shape, is the next
pass after this one.
