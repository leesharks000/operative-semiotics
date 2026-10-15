# Reader prompt — as sent to each parallel reader (wave 2 onward)

`<ID>` is the batch id. B0019, a single ~64k-word deposit, carried one added sentence allowing `partial` with ranges and reason.

> You are a parallel reader in a prediction sweep of an archive. Your batch id is <ID>.
>
> 1. Read the protocol in full first: /home/claude/operative-semiotics/data/reading/READING-PROTOCOL.md (v1.1). Follow it exactly.
> 2. Your batch is the entry with "batch_id": "<ID>" in /home/claude/operative-semiotics/data/reading/queue.json (load it with a short python3 snippet; each deposit row gives deposit, path, lines_total, title). Read every deposit's text file IN FULL with the Read tool in consecutive chunks (offset/limit), recording the ranges. Do not substitute search for reading.
> 3. Write your output JSON to /home/claude/operative-semiotics/data/reading/batches/<ID>.json in exactly the protocol's shape. Take every quote by slicing the source lines (e.g. with a scratch python script in the session scratchpad) so it is verbatim, and check each quote lies within its stated lines. Record started_at/finished_at from `date -u`, and your self_description honestly ('unknown' rather than guess).
> 4. Do not edit any other project file. When done, reply with one short paragraph: the output path, deposits read, finds by shape, and anything a later reader must know (damaged text, duplicate bodies).

The wave-1 prompt text was lost to context compaction; its run entries record "batch entry in queue.json + protocol" and the protocol sha. This file is the record from wave 2 on.
