# Triage of the prediction sweep: report (2026-10-17)

The ruling (Lee Sharks, 2026-10-17): "lets do the triage pass." The protocol is `data/reading/TRIAGE-PROTOCOL.md`.
The claims are in `triage/claims.json`, and each is registered at its earliest statement. The confirmation records and
their targets are in `triage/confirmations.json`. Everything the readers flagged for a later pass, 189 observations, is
in `triage/observations.json`.

## What came out

**6,162 finds became 4,446 claims.** By tier:

| Tier | Claims |
|---|---|
| Forecasts (shapes A, B, E) | 981 |
| Standing falsifiable claims (G) | 951 |
| Unbuilt tests (F) | 995 |
| Historical theses (H) | 1,232 |
| Priority records (D) | 287 |

- 871 claims are stated more than once. 650 are stated twice, 134 three times, and 87 four times or more.
- The most restated include:
  - the Phase X Invariance Condition (#367; 8 statements)
  - the Slavonic Josephus interpolation thesis (#626; 8)
  - Sappho 31's χλωροτέρα ποίας (#281; 7)
  - the Fulfillment Map's Citrini row (#1110; 7)
  - the Second Prophecy (#636; 7)
- **Changed versions.** Where a later statement changes a claim (its window moves, its scope widens or narrows, its
  falsifier changes, or it is reversed), the change is kept as a dated state of that claim.
- **Lists and their members.** 60 claims are lists, ledgers or batteries that contain other claims. The members are not
  merged into the list.
- **Related claims.** 187 claims have links to related claims, such as series siblings, a claim and its test, or one
  template used for different subjects.

**339 confirmation records** were traced to what they point back to:

| Target | Records |
|---|---|
| A find | 165 |
| A deposit passage that is not a find | 82 |
| Earlier in the same deposit | 42 |
| Outside the archive | 19 |
| Unlocated | 31 |

- What the deposits claim on those links: came true 173, partly 20, still pending 17, failed 8. These are the deposits'
  own claims, not triage verdicts.
- 118 claims now carry confirmation evidence.

**The 67 register cards:**
- 35 are found and 18 partly found.
- 11 give no archive source, and no find states them: P-EXPORT-RESUMES, P-STALE-INDEX, P-PEO-COHORT-2, P-PEO-PANEL-2,
  M6-CT-02, M6-CT-01-DEPOSIT, BLOG-INDEX-CADENCE, COUNTS-REGEN, PROJECTION-GROUPING, CORPORA-SPLIT and RESOLUTION-ROUTES.
- 3 are not found: ATHETIC-APPARATUS (#1540 l.293 specifies it, but no reader recorded it), WEBSPAM-VECTOR-SCORE (only
  in an attached rows.json) and MIRROR-KAPPA (stated only on the card).

**The 190 intake items of 2026-08-23:**
- 123 are found and 24 partly found.
- 29 are excluded by the reading protocol's own rules: procedural timelines, dated observations, other people's
  predictions, and fiction presented as such.
- 14 are not found. Most are parse artefacts, such as "Prediction 3" read out of a sentence, instructions or theorems.

**142 finds are held out.** Their quote is no longer in the current text. These come from the
record repair of 10-15 and 10-16, which changed 364 texts after they were read; 13 of those deposits had their bodies
replaced outright. The held-out finds are listed in `claims.json` and are not assembled into claims.

## What needs Lee

These are recorded and nothing has been changed:

- **INVERSION-T3.** The card says the test was never run. #1456 (ll.70, 78, 277) records T3 as implemented after the
  results came in (deviation V3-D14) and as CONFIRMED.
- **The "three pressures" forecast.** #1088 and #1090 credit #835 §III–V with a forecast of three pressures (receipts,
  conformance fixtures, lifecycle) that is not in #835's text. It first appears in #1088 itself.
- **Dates.** 23 claims are registered at deposits dated 2026-01-01. Several readers found this to be a placeholder:
  #1238, #1242 and #1243 record 2026-04-17, and #1249 restates an 06-18 line. Those claims are flagged. Some other
  deposits' dates precede events they discuss (#1110, #1251, #234 and the Citrini memo; #510 and #513), so their
  registration dates are as reliable as the deposit dates.
- **Attachments were not read by the sweep.** Predictions written only in attachments have no finds:
  - #1616's PREREGISTRATION.md, the FLAT-W2 predictions
  - #1613's rows.json
  - #1610's transmission-toy.py
  - the battery v0.2 and v0.3 code headers
- **The 25-of-28 bar** cited by #1585, #1586 and #1589 is not stated as a bar in any current text.

## Next

- **A topical pass.** It joins claims restated in other words, which word overlap does not catch. It will:
  - order the dated states of revised claims, for example the Sappho 31 / Catullus 51 otium claim across seven deposits;
  - add the deposit passages that confirmation records point to but no find records, which are anchor candidates.
- **A re-reading of the text added by the record repair.** About 348,000 words, read under the sweep protocol.
- **The attachments.** Read them under the sweep protocol.
- **Where the index lives.** This waits on Lee's ruling.
