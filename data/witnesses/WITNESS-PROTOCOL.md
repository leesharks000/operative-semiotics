# External witnesses of the prediction index

Adopted by Lee Sharks on 2026-10-30. His request: "lets look for external research that has already confirmed or supported predictions in the index on operativesemiotics after their timestamp. or disconfirmations, of course - but only solid witnesses in either direction. and we'll have to record it in some way to when it turns out there was pre existing confirming research, and track what weve searched for and when". To the proposal: "adopted. and weaker evidence than peer-reviewed can enter the record so long as its status is recorded - i dont mean just anything, but it would be extremely hypocritical to reproduce the notability regime. evidence is evidence."

## What a witness is

A witness is research or evidence from outside the archive that bears on a claim of the index (data/reading/triage/claims.json). It is recorded in `witnesses.json` and shown on the claim's subject page under "external witnesses". A witness never changes a claim's status. Status is curated, and changes only by the operator's ruling.

A witness enters when it has a source that can be checked (a URL, DOI or archival location), a dated earliest public version, and a finding quoted verbatim from the source. Its kind is recorded as `evidence_class`, and every class is admissible. The class says what kind of evidence it is; it does not rank the evidence out of the record.

`evidence_class`: `peer-reviewed article`, `peer-reviewed conference paper`, `preprint`, `working paper`, `report`, `dataset`, `book`, `thesis`, `documentation`, `post`, `news`, `system output`, `other`.

## Direction and order

- `direction`: `supports` or `disconfirms`.
- `order` is computed per claim by scripts/witnesses/check_witnesses.py, from the claim's `registered` date and the witness's earliest public version: `after` (the witness came later), `before` (the research already existed when the claim was registered: an anticipation, recorded as such), or `undetermined` (a version dated only to the month of registration, or no dated version). The earliest public version governs: a 2026 journal article whose preprint appeared in 2025 is ordered by the preprint.

## What it bears on

Each link from a witness to a claim states `bears_on`: `whole` (the claim as stated, its threshold, entity and cause), `component` (one part of a compound claim), `mechanism` (the process the claim names, in another system or setting), or `method` (the claim's proposed test, carried out by others). `scope` says in one or two sentences where the witness and the claim part.

## The search log

Every search is logged in `searches.json`, whether or not it found anything: its date, who ran it, the claims or lines it aimed at, the queries and sources consulted, and its outcome (witnesses recorded, candidates held for checking, exclusions with their reasons, and nothing found). A candidate is a source a search turned up that has not been checked; it is not a witness until it is.

## Checking

`checked` records who verified the witness, when, and how (which pages were read), and lists under `unverified` any detail a report gave that the check could not confirm. Run `python3 scripts/witnesses/check_witnesses.py` before committing: it refuses a witness whose claims do not exist, whose class or direction is outside the vocabulary, or which lacks a source, a dated version or a quoted finding.
