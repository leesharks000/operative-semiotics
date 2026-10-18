# Triage reader prompt (as sent to each parallel reader)

`<ID>` is the batch id.

> You are a parallel reader in the triage pass of an archive's prediction sweep. Your batch id is <ID>.
>
> 1. Read the protocol in full first: /home/claude/operative-semiotics/data/reading/TRIAGE-PROTOCOL.md (v1.0). Follow it exactly.
> 2. Your batch is the entry with "batch_id": "<ID>" in /home/claude/operative-semiotics/data/reading/triage/queue.json (load it with a short python3.12 snippet and print the items a few at a time). Read every item whole. Open deposit texts (the "path" field) with the Read tool at the find's lines where you need context, and record what you opened.
> 3. Write /home/claude/operative-semiotics/data/reading/triage/batches/<ID>.json in exactly the protocol's shape: one decision per item, in queue order. Copy every evidence phrase out of the quote or text with a script so it is verbatim. Record started_at/finished_at from `date -u` and your self_description honestly ('unknown' rather than guess).
> 4. Run `python3.12 /home/claude/operative-semiotics/scripts/reading/triage_verify.py <ID>` and fix every failure it reports until it prints VERIFIED.
> 5. Do not edit any other project file and do not run git. When done, reply with one short paragraph: the output path, the decisions by value, and anything a later pass must know.
