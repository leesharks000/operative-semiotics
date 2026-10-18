# Topical Protocol: the prediction triage's third pass (v1.0, 2026-10-17)

The ruling (Lee Sharks, 2026-10-17): "lets proceed thru the next pass."

## What this pass is for

The triage (TRIAGE-PROTOCOL.md) grouped 6,162 finds into 4,446 claims, each registered at its earliest statement. It
joined statements only where they shared wording. Two things are left for this pass, because word overlap misses them:

1. **A claim restated in other words.** The same thesis, forecast or test stated in two deposits with different
   wording, sometimes coded under different shapes: a standing claim (G) in one deposit, a historical thesis (H) in
   another.
2. **A claim revised over time.** A claim whose dated versions drift until their wording no longer overlaps. Examples:
   the Sappho 31 / Catullus 51 otium claim across seven deposits through the erratum chain, the Phase X Invariance
   Condition's scope, a hypothesis that a later deposit says was "backwards".

Like the triage, this pass links. It does not judge whether a claim is true or came true, and it does not create new
finds.

## Your batch

Your batch is the entry with your `batch_id` in `data/reading/triage/topical-queue.json`. It holds one or more subject
groups. Each group was formed by clustering the claims' statements, and carries its top terms. Each claim in it gives:

- its id (`PRED-…`), tier, registration date and deposit;
- its earliest statement and falsifier;
- every later statement, quoted in full;
- what the triage already linked: `contains`, `in` and `related`.

Read every claim in every group in full. Where you need context the statement does not carry, open the deposit's text
(the `path` field) around the find's lines, and record the range you read. Lines you only saw as search hits are not a
reading: list them under `located` (same shape as `read`), not under `read`. Some statements contain non-breaking
spaces, so copy phrases by script rather than retyping them.

## What to record, per group

**`same`**: a set of two or more claims that are one claim. A reader of the index should see one prediction with
several statements. Use this for paraphrase, a translation into another register, or one thesis coded as G here and H
there.

**`states`**: a set of two or more claims that are one claim revised over time. List them in the order of the claim's
development as the texts show it, with what changed at each step (`change`): the window moved, the scope narrowed or
widened, the falsifier changed, the claim was withdrawn, or the claim was reversed. When a later deposit corrects or
supersedes an earlier claim, that is a state of it; do not reconcile the two. The index orders a claim's states by
registration date (Lee Sharks, 2026-10-17: "we go by registration date"). Where the development order you read disagrees
with the registration dates, say so in that step's `change` and in an observation; the index keeps your order beside
the date order.

**`series`**: a set of distinct claims that belong together as members of one programme or battery, or one
template applied to different subjects. They stay separate claims, linked as a series. Give the series a short `name`.

A claim can be in at most one `same` or `states` set, and in any number of series. A claim you leave out stays as it is.
Do not repeat what the triage already linked unless you are adding to it.

For every set, give:

- `basis`: one sentence;
- `evidence`: one verbatim phrase (8 to 200 characters) per member, as `{"claim": id, "phrase": ...}`. Take the phrase
  from that claim's statement, its falsifier or one of its later statements, and copy it with a script.

Record as `observations`:

- an apparent contradiction between claims. It is an observation, not an error: the archive's apparent contradictions
  can be deliberate structure.
- a claim that belongs with a claim in another group (name both ids).
- a registration date that seems wrong: a deposit dated before an event it discusses, or a placeholder date.

## Output

Write `data/reading/triage/topical/<ID>.json`:

```
{"batch_id": "<ID>", "protocol": "TOPICAL-PROTOCOL v1.0",
 "reader": {"self_description": "...", "started_at": "...", "finished_at": "..."},
 "groups": [{"group": "<group id>", "reviewed": ["<every claim id in the group>"],
             "sets": [{"kind": "same|states|series", "claims": [...], "name": "...", "change": ["...", ...],
                       "basis": "...", "evidence": [{"claim": "...", "phrase": "..."}]}],
             "read": [[deposit, first, last], ...], "located": [[deposit, first, last], ...]}],
 "observations": ["..."]}
```

- Fill one `groups` entry for every group in the batch, in order. `reviewed` lists every claim in the group, so the
  record shows each one was read. A group with nothing to link has an empty `sets`.
- A set may name a claim from another group in the same batch.
- `change` is required for `states` and has one entry per step, so its length is the number of claims minus one.

Keep scratch scripts in `<scratchpad>/<batch id>/`. Use `date -u` for the times and "unknown" rather than guess. Do not
edit any other file and do not run git. Never copy a credential, token or key string into your output.

## What follows

- `scripts/reading/topical_verify.py` checks each batch: the ids, the vocabulary, that each claim is in at most one
  same/states set, that every phrase is verbatim, and that every group is fully reviewed.
- `scripts/reading/triage_assemble.py` then merges `same` sets into one claim, registered at its earliest statement;
  orders `states` as dated states of one claim; and records series.
