# Reader prompt — as sent to each parallel reader (wave 2 onward)

`<ID>` is the batch id. B0019, a single ~64k-word deposit, carried one added sentence allowing `partial` with ranges and reason.

> You are a parallel reader in a prediction sweep of an archive. Your batch id is <ID>.
>
> 1. Read the protocol in full first: /home/claude/operative-semiotics/data/reading/READING-PROTOCOL.md (v1.2). Follow it exactly.
> 2. Your batch is the entry with "batch_id": "<ID>" in /home/claude/operative-semiotics/data/reading/queue.json (load it with a short python3 snippet; each deposit row gives deposit, path, lines_total, title). Read every deposit's text file IN FULL with the Read tool in consecutive chunks (offset/limit), recording the ranges. Do not substitute search for reading.
> 3. Write your output JSON to /home/claude/operative-semiotics/data/reading/batches/<ID>.json in exactly the protocol's shape. Take every quote by slicing the source lines (e.g. with a scratch python script in the session scratchpad) so it is verbatim, and check each quote lies within its stated lines. Record started_at/finished_at from `date -u`, and your self_description honestly ('unknown' rather than guess).
> 4. Do not edit any other project file. When done, reply with one short paragraph: the output path, deposits read, finds by shape, and anything a later reader must know (damaged text, duplicate bodies).

The wave-1 prompt text was lost to context compaction; its run entries record "batch entry in queue.json + protocol" and the protocol sha. This file is the record from wave 2 on.

## Wave 3 onward, additions

- Step 2 adds: "For the last chunk of each file, call Read with offset and NO limit so the final line is not cut off; check your ranges reach lines_total." (After S0001: the launcher's own first pass stopped one line short.)
- Wave 4 onward adds: "lines_total in the queue is authoritative; do not recount with wc -l, which misses a final line without a newline." (After B0024: five deposits' last lines missed that way; completed by S0002.)
- Wave 5 onward: the protocol reference reads v1.2 (shape H, historical thesis, added on Lee's ruling).
- H back-pass batches (HB…): step 2 reads "Your batch is the entry with "batch_id": "<ID>" in data/reading/hpass.json … This is the H back-pass: record ONLY shape H (see the protocol's 'The H back-pass')."
- Wave 10 onward adds to step 3: "Each quote must be ONE contiguous slice of the source (no joining of separate passages, no skipped lines inside the range)." (After B0054.)
- X-batches (wave 17 on): step 2 reads the entry in data/reading/xqueue.json — a line RANGE of a derived own-voice text; read that range in full, all shapes, quote from the derived text.
- Wave 26 onward adds to step 4: "When two deposits seem to contradict each other, report it as an observation, not as an error: the archive's apparent contradictions can be deliberate structure." (After Lee's ruling on #330 and on the scope of the repair pass.)
- Wave 30 onward adds to step 3: "every deposit entry must carry "status" ("read" | "partial" | "skipped") and "status_note"" (after B0145) and "Never copy a credential, token or key string into your output." (after #870/#871).
