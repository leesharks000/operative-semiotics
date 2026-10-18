# Naming Protocol: the subject pages of the prediction index (v1.0, 2026-10-17)

The ruling (Lee Sharks, 2026-10-17): "id like to do individual pages, not for each prediction - thats too many - but
perhaps by category, whatever were doing for individual capture pages, theyre indexing very well, so id like to
replicate that without attempting thousands of standalone pages. 100-200, maybe - but not thousands."

## What the pages are

There are about 4,100 claims in the index. Each claim was triaged out of the prediction sweep and dated by the first
deposit that states it. The claims are grouped into 153 subject pages on operativesemiotics.org.

Each group was formed from the claims' own links:
- the series they belong to;
- the claims they relate to;
- the deposit they share;
- how close their wording is.

A grouping can still be loose. Your job is to read each page and make it a page. The title and description you write
are what a search engine and a composition surface will see first.

## Your batch

Your batch is the entry with your `batch_id` in `data/index/naming-queue.json`. Each page lists its claims in date
order. For each claim it gives:
- the id, tier, registration date and deposit;
- the deposit's title and archive line;
- how many statements the claim has;
- its series;
- the first 700 characters of its statement.

Read every claim on every page. For context, the full claim is in `data/reading/triage/claims.json` and the deposit's
text is at the path in `data/reading/triage/deposit-titles.json`.

## What to write, per page

- `title`: what the claims on this page claim, as a specific subject.
  - At most 80 characters, in plain words.
  - Examples: "Revelation written first: dating, priority and the Irenaeus anchor", or "Sappho 31: where the poem
    ends".
  - Do not use a generic label ("Assorted claims", "Retrieval"). Do not use an archive code alone.
  - Name works, people and terms as the archive names them.
- `slug`: lowercase words joined by hyphens, at most 60 characters, and unique within your batch.
- `description`: two to four sentences, declarative.
  - Say what the claims on the page assert, predict or set out to test, and in which works.
  - Count by tier where it helps ("eleven historical theses and four unbuilt tests").
  - Make no claim the page's claims do not make. Give no verdict on whether they came true.
- `line`: the archive line the page belongs under, from the queue's `lines` list. This is the archive's own taxonomy.
  Choose the line most of the page's claims carry. Where none do, choose the closest.
- `moves`: claims that belong on another page rather than this one, as `{"claim", "to", "reason"}`. `to` is a page id
  from `all_pages`. Move a claim only when it plainly belongs elsewhere, for example a Josephus claim on a page about
  retrieval metrics. If you know the claim's subject but not its page, give `to: null`.
- `note`: anything a later pass must know. For example, that the page holds two subjects and should be split. Give
  where to split it.

## Output

Write `data/index/naming/<ID>.json`:

```
{"batch_id": "<ID>", "protocol": "NAMING-PROTOCOL v1.0",
 "reader": {"self_description": "...", "started_at": "...", "finished_at": "..."},
 "pages": [{"page": "P001", "title": "...", "slug": "...", "description": "...", "line": "...",
            "moves": [], "note": ""}]}
```

Write one entry per page, in queue order. Then run
`python3.12 /home/claude/operative-semiotics/scripts/index/naming_verify.py <ID>` and fix every failure it reports until
it prints VERIFIED.

Keep scratch scripts in `<scratchpad>/<ID>/`. Do not edit any other file and do not run git.
