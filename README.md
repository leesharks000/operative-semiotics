# operativesemiotics.org — preliminary index

**Not the site.** A first offering, published early so the work sits at stable, resolvable
addresses while the surface is built.

| file | what it is |
|---|---|
| `index.html` | the centre, the disciplines, the site plan, twelve entry points, and a machine-reader section |
| `index.json` | schema.org `Dataset` — every discipline, tier and document as AXN + record URL |
| `topology.svg` | the discipline centre-out, five rings, node area proportional to documents |
| `robots.txt` | open to machine readers, pointing at the JSON index and the OAI endpoint |
| `sitemap.xml` | three URLs |

## What it does now

States the discipline. Names the eight disciplines with founding deposits. Shows the site plan
as five rings rather than implying a finished structure. Offers twelve entry points that
resolve to canonical records with full text and AXNs. Declares three states — **read**,
**surveyed**, **listed** — and says they must not be summed.

## What it does not do yet

No per-element operative affordances (download / open / copy / execute) beyond the spine. No
per-element schematics. No issue surfaces. The full 117-document index exists in `index.json`
but is not yet rendered as pages.

## Deployment

Static. Any host. Canonical text stays at alexanarch.org — this surface points, it does not
duplicate. If that changes, the pointers here are the thing to update, not the texts.

## Contents

```
index.html      the page — centre, materials, disciplines, site plan, spine, machine section
index.json      schema.org Dataset with 4 declared distributions
topology.svg    the discipline centre-out
vercel.json     static config; CORS and content-type headers for /data and /pdf
robots.txt      open to machine readers; points at the JSON index and the OAI endpoint
sitemap.xml
data/
  gather.json          the full working index (122 KB)
  assembly-brief.md    the brief circulated for Assembly rounds (28 KB)
pdf/
  Operative-Semiotics-A-Grundrisse-SIGIL.pdf   880 pp, 2.3 MB
  HESPERUS-The-Back-Matter-Machine-SIGIL.pdf   147 pp, 0.4 MB
```

## Deploy

Static. No build step. Import to Vercel, framework preset **Other**, output directory the
repository root. `vercel.json` sets `cleanUrls`, CORS on `/data` and `/pdf`, and the correct
content types.

The page carries Google Scholar `citation_*` tags including `citation_pdf_url`, which is the
block Scholar parses to index a PDF against a landing page. That is the mechanism by which the
work becomes findable in scholarly retrieval, and it is the reason the PDFs are hosted here
rather than only linked.
