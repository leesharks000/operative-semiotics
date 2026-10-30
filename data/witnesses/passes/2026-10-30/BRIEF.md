# External-witness pass over the prediction index — brief for one reader (2026-10-30)

## The task

Lee Sharks, the archive's operator, asked: "lets look for external research that has already confirmed or supported predictions in the index on operativesemiotics after their timestamp. or disconfirmations, of course - but only solid witnesses in either direction." He also ruled that "weaker evidence than peer-reviewed can enter the record so long as its status is recorded - i dont mean just anything, but it would be extremely hypocritical to reproduce the notability regime. evidence is evidence." He also wants research that existed before a claim was registered recorded, as an anticipation. Every search is logged.

Your theme's claims are in /tmp/claude-0/wit/claims-<THEME>.json. Each claim has an id, a tier (forecast or unbuilt test), a registered date (the claim's timestamp), its statement, falsifier and window. Read them all first. Then search for outside research and evidence that bears on them. Disconfirmations are wanted as much as confirmations.

Read the protocol first: /home/claude/fleet/operative-semiotics/data/witnesses/WITNESS-PROTOCOL.md. The four witnesses already recorded are in /home/claude/fleet/operative-semiotics/data/witnesses/witnesses.json. Do not duplicate them, but use them as the model of the form and of the scope discipline.

## What counts

A witness has three things:
- a source that can be checked: a URL or DOI that you fetched and read;
- a dated earliest public version, verified. Use the arXiv v1 date, the preprint server date, the working paper date, or the post's date. Look for earlier versions: a 2026 article whose preprint is from 2025 is dated 2025;
- a finding quoted verbatim, copied from the page you fetched. Say where the quote came from (abstract, results, landing page).

Any evidence class may enter (peer-reviewed article, peer-reviewed conference paper, preprint, working paper, report, dataset, book, thesis, documentation, post, news, system output, other). Record the class honestly. "I dont mean just anything": a source must report a finding with some method or evidence behind it. Opinion pieces and uncorroborated claims do not count.

The fit must be honest. Attach a witness to a claim only where it bears on what the claim states. State how it bears on the claim:
- `whole`: the claim as stated, with its threshold, entity and cause;
- `component`: one part of a compound claim;
- `mechanism`: the process the claim names, in another system or setting;
- `method`: the claim's proposed test, carried out by others.

In `scope`, say in one or two sentences where the witness and the claim part. Most fits will be mechanism or component; say so. A study on a nearby topic that does not test what the claim says is not a witness: log it as an exclusion with the reason.

Work in either direction of time. The order is computed later from the dates. Research published before the claim was registered is recorded the same way, and becomes an anticipation.

## Method

1. Read the claims. Mark the ones with concrete, externally testable content: measurable effects, named systems, dated forecasts, proposed experiments.
2. For those, search. Use WebSearch in "standard" mode, and "extended" where standard comes back thin or the topic is recent. Search arXiv, ACL Anthology, SSRN, PsyArXiv, medRxiv, journals, conference proceedings, and credible reports and datasets.
3. Fetch each promising source with WebFetch and read it. Verify the title, authors, dates of every version, and the finding you will quote.
4. Use only WebSearch and WebFetch for the web. Do not use curl or any other route, and never change a user agent. If a site refuses, record the refusal and try another copy (arXiv, a repository page, the publisher).
5. Budget: up to about 60 searches and 60 fetches. Go first to the claims most likely to have outside evidence.

## Output

Write one JSON file: /tmp/claude-0/wit/out-<THEME>.json, shaped as follows.

```json
{"theme": "<THEME>",
 "witnesses": [ {"id": "<THEME>-W01", "direction": "supports|disconfirms", "evidence_class": "...",
   "claims": [{"claim": "PRED-…", "bears_on": "whole|component|mechanism|method", "scope": "…"}],
   "source": {"authors": [...], "title": "…", "venue": "…", "doi": "…|null", "urls": ["…"]},
   "versions": [{"date": "YYYY-MM-DD|YYYY-MM", "kind": "…", "where": "…", "url": "…"}],
   "finding": [{"quote": "verbatim", "from": "abstract, arXiv"}],
   "shows": "…", "does_not_show": "…",
   "checked": {"how": "which pages you read, and when", "unverified": ["details you could not confirm"]}} ],
 "searches": [ {"query": "…", "mode": "standard|extended|fetch", "aimed_at": ["PRED-…"], "result": "what came back, in a line", "outcome": "witness <id> | candidate | excluded: reason | nothing"} ],
 "candidates": [ {"source": "…", "url": "…", "claims": ["PRED-…"], "why_unresolved": "…"} ],
 "notes": "anything the main session must know"}
```

Every search goes in `searches`, including those that found nothing. Fetches go there too, with mode "fetch".

## Rules for your prose (binding)

- Never "not X but Y", and never "X, not Y".
- No "rather than" or "instead of" outside quotations.
- Third person. No gendered generics.
- Plain words. No hard line breaks inside a string.
- Never adjust a quote. Copy it exactly from the fetched page, or leave it out.

## Out of bounds

- Write only /tmp/claude-0/wit/out-<THEME>.json.
- Do not edit any repository.
- Do not commit.

## Report

When done, report in a few lines:
- how many witnesses, by direction and evidence class;
- the strongest two;
- any disconfirmation;
- what you could not resolve.
