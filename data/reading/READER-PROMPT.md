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

## Pass 2 (R- and A-batches, 2026-10-18)

> You are a parallel reader in a prediction sweep of an archive. Your batch id is <ID>.
>
> 1. Read the protocol in full first: /home/claude/operative-semiotics/data/reading/READING-PROTOCOL.md (v1.3), with particular care for "Pass 2". Follow it exactly.
> 2. Your batch is the entry with "batch_id": "<ID>" in /home/claude/operative-semiotics/data/reading/pass2-queue.json (load it with a short python3 snippet; each unit gives unit, deposits, path, lines_total, ranges, title). Read every range of every unit IN FULL with the Read tool, in consecutive chunks (offset/limit), recording the ranges you read. For a range that runs to the end of a file, call Read with offset and NO limit. lines_total in the queue is authoritative. Do not substitute search for reading.
> 3. Write your output JSON to /home/claude/operative-semiotics/data/reading/batches/<ID>.json in the protocol's shape, each entry keyed by "unit" (copied exactly) with "deposits" copied from the queue. Take every quote by slicing the source lines with a scratch python script in the session scratchpad, so it is verbatim and ONE contiguous slice, and check it lies within its stated lines. Every entry carries "status" ("read" | "partial" | "skipped") and "status_note". Record started_at/finished_at from `date -u`, and your self_description honestly ('unknown' rather than guess). Never copy a credential, token or key string into your output.
> 4. Run `python3.12 /home/claude/operative-semiotics/scripts/reading/verify_batch.py /home/claude/operative-semiotics/data/reading/batches/<ID>.json` and fix every failure it reports in your output. Do not edit any other project file and do not run git.
> 5. When done, reply with one short paragraph: the output path, units read, finds by shape, and anything a later reader must know. When two deposits seem to contradict each other, report it as an observation, not as an error.

## Annotation pass (N-batches, 2026-10-18)

> You are a parallel reader in an annotation pass over a prediction index. Your batch id is <ID>.
>
> 1. Read the protocol in full first: /home/claude/operative-semiotics/data/reading/ANNOTATION-PROTOCOL.md (v1.0). Follow it exactly.
> 2. Your batch is the entry with "batch_id": "<ID>" in /home/claude/operative-semiotics/data/reading/annotate-queue.json (load it with a short python3 snippet). For every item, read with the Read tool what the protocol requires for its tasks, recording the ranges. Do not substitute search for reading.
> 3. Write your output JSON to /home/claude/operative-semiotics/data/reading/batches/<ID>.json in the protocol's shape. Take every quote by slicing the source lines with a scratch python script in the session scratchpad, so it is verbatim and ONE contiguous slice inside its stated lines. Record started_at/finished_at from `date -u`, and your self_description honestly ('unknown' rather than guess). Never copy a credential, token or key string into your output.
> 4. Run `python3.12 /home/claude/operative-semiotics/scripts/reading/verify_annotate.py /home/claude/operative-semiotics/data/reading/batches/<ID>.json` and fix every failure it reports in your output. Do not edit any other project file and do not run git.
> 5. When done, reply with one short paragraph: the output path, items answered, counts by answer (bases, retrospective, modes, falsifier kinds), and anything a later reader must know.

## Recall audit (K-batches, 2026-10-18)

Launched with model override `sonnet`, so the second reading is by a different model from the first.

> You are a reader in a second, independent reading of a few texts. Your batch id is <ID>.
>
> 1. Read the brief in full first: /home/claude/operative-semiotics/data/reading/RECALL-BRIEF.md. Follow it exactly. Do not open any other file under /home/claude/operative-semiotics/data/reading except recall-queue.json, and do not read anything under /home/claude/operative-semiotics/data/index, /home/claude/operative-semiotics/predictions or data/reading/batches other than your own output.
> 2. Your batch is the entry with "batch_id": "<ID>" in /home/claude/operative-semiotics/data/reading/recall-queue.json. Read every deposit's file IN FULL with the Read tool in consecutive chunks; for the last chunk call Read with offset and NO limit. lines_total in the queue is authoritative.
> 3. Write /home/claude/operative-semiotics/data/reading/batches/<ID>.json in the brief's shape, every quote sliced verbatim with a scratch python script in the session scratchpad.
> 4. Run `python3.12 /home/claude/operative-semiotics/scripts/reading/verify_recall.py /home/claude/operative-semiotics/data/reading/batches/<ID>.json` and fix every failure. Do not edit any other file and do not run git.
> 5. Reply with one short paragraph: output path, deposits read, passages marked.

## Recall adjudication (J-batches, 2026-10-18)

> You are an adjudicator in the recall audit of a prediction sweep. Your batch id is <ID>.
>
> 1. Read /home/claude/operative-semiotics/data/reading/RECALL-ADJUDICATE.md, then /home/claude/operative-semiotics/data/reading/READING-PROTOCOL.md (v1.3), both in full. Follow the first exactly; the second is the standard.
> 2. Your batch is the entry with "batch_id": "<ID>" in /home/claude/operative-semiotics/data/reading/recall-adjudicate-queue.json. For every item read the passage and the lines around it with the Read tool, recording the ranges.
> 3. Write /home/claude/operative-semiotics/data/reading/batches/<ID>.json in the shape given. Record started_at/finished_at from `date -u`, self_description honestly.
> 4. Run `python3.12 /home/claude/operative-semiotics/scripts/reading/verify_adjudicate.py /home/claude/operative-semiotics/data/reading/batches/<ID>.json` and fix every failure. Do not edit any other file and do not run git.
> 5. Reply with one short paragraph: output path, verdict counts, anything a later reader must know.

## Describe pass (DS-batches, 2026-10-18)

> You are a reader rewriting subject-page descriptions of a prediction index. Your batch id is <ID>.
>
> 1. Read /home/claude/operative-semiotics/data/index/DESCRIBE-PROTOCOL.md in full and follow it exactly.
> 2. Your batch is the entry with "batch_id": "<ID>" in /home/claude/operative-semiotics/data/index/describe-queue.json (load it with a short python3 snippet). Read every page's claims before writing its description.
> 3. Write /home/claude/operative-semiotics/data/index/describe/<ID>.json in the protocol's shape, then run `python3.12 /home/claude/operative-semiotics/scripts/index/verify_describe.py /home/claude/operative-semiotics/data/index/describe/<ID>.json` and fix every failure. Keep scratch files in your own folder of the session scratchpad. Do not edit any other file and do not run git.
> 4. Reply with one short paragraph: output path, pages rewritten, pages with residue, anything a later reader must know.
