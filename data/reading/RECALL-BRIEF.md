# Recall brief v1.0 — second reading of a random sample (2026-10-18)

This brief is deliberately worded differently from the reading protocol, so that a second reading can show what the
first one missed. Do not open READING-PROTOCOL.md or any other file under data/reading except your batch entry.

You read, in full, a handful of texts from a scholarly and literary archive. Your job is to mark every passage in which
the text commits itself to something that could, in principle, be checked by someone else. That includes, among
others:

- a statement about what will happen, or what something will become, at any time-scale, however it is phrased —
  including in poems, stories, dreams, satire, invented products and imagined future documents;
- a statement that a system, platform, model, institution or practice behaves in a certain way, especially if the text
  says what would show it wrong;
- a statement that the archive or its author named, did or published something before others did;
- a proposed experiment, measurement, benchmark or tool not yet carried out or built;
- a thesis about the past that the text argues for itself — authorship, dating, priority between texts, what a
  passage originally meant, how a work was received;
- a report that an earlier statement of the archive came true, or failed.

Leave out: other people's claims the text does not adopt; plain summary of settled scholarship; boilerplate about
checking a record's bytes or URLs; procedural timelines (review windows, cooling periods); reports of what already
happened that are not framed as bearing out an earlier claim. When the same commitment recurs in one text, mark its
fullest statement once.

## How

1. Your batch is the entry with your batch id in data/reading/recall-queue.json (load it with a short python3
   snippet). Each deposit gives a path and lines_total (authoritative). Read every file IN FULL with the Read tool in
   consecutive chunks; for the last chunk use offset with no limit. Record the ranges you read. Do not substitute
   search for reading.
2. For each passage, take the quote by slicing the file's lines with a scratch python script, so it is verbatim, one
   contiguous slice, and inside its stated lines. A quote is the commitment itself, at most about 120 words.
3. Write data/reading/batches/<ID>.json:

```json
{"batch_id": "<ID>", "brief": "RECALL-BRIEF v1.0", "started_at": "<date -u>", "finished_at": "<date -u>",
 "self_description": "<what you are, or 'unknown'>",
 "deposits": [{"deposit": 123, "status": "read" | "partial", "read_ranges": [[1, 400], [401, 812]],
   "passages": [{"quote": "<verbatim>", "lines": [a, b], "kind": "<a few words: what sort of commitment>",
                 "why": "<one line: what would check it>"}],
   "none_found": false, "note": "<anything a later reader must know>"}]}
```

4. Never copy a credential, token or key string into your output. Do not edit any other file and do not run git.
