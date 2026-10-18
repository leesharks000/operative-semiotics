# Join Protocol: the pairs named across groups (v1.0, 2026-10-17)

The ruling (Lee Sharks, 2026-10-17): "lets join the pairs."

## What this pass is for

Each topical reader saw only the claims in its own batch. When a reader found a claim that belonged with one in another
group, it recorded the pair as an observation and did not link it. The triage readers did the same. This pass decides
those pairs.

## Your batch

Your batch is the entry with your `batch_id` in `data/reading/triage/join-queue.json`. Each item (`group`) holds:

- one reader's observation, verbatim;
- `from_batch`, the batch where the observation was recorded;
- every claim the observation names, each in full in the same form as the topical queue. A claim's card also shows what
  is already linked to it: `series`, `states` and `related`.

The claim ids are current. A claim that has already been merged appears under the id of the claim that now holds it.

## Deciding

Follow `data/reading/TOPICAL-PROTOCOL.md` for the meaning of `same`, `states` and `series` and for the evidence each set
needs. Read that protocol first.

For each item:

- **A set can use any of the item's claims.** It need not use all of them.
- **Not every observation is a join.**
  - An apparent contradiction stays two claims. Record nothing for it, unless the texts show that one claim is a revision
    of the other; that is `states`.
  - If the claims are related only by subject, `series` is enough. Leave `sets` empty if even that is too loose.
- **Extending existing links.**
  - If a claim already belongs to a series, a new series with the same `name` extends it.
  - If a claim already has `states`, a new `states` set must list the whole chain. Include the existing members, in
    development order, so the result is one chain. Give a `change` for every step, including the steps already
    recorded.

Write one entry per item, in order:

- `reviewed` lists every claim in the item.
- Record what you read under `read`. Lines you only found by search go under `located`.
- Put anything a later pass must know in `observations`.

## Output

Write `data/reading/triage/topical/<ID>.json`, in the topical protocol's shape, with `"protocol": "JOIN-PROTOCOL v1.0"`.
Check it with:

```
python3.12 /home/claude/operative-semiotics/scripts/reading/topical_verify.py <ID>
```

Keep scratch scripts in `<scratchpad>/<ID>/`. Do not edit any other file and do not run git.
