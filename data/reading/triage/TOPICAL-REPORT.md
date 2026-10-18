# Topical pass of the prediction triage: report (2026-10-17)

The ruling (Lee Sharks, 2026-10-17): "lets proceed thru the next pass."

The protocol is `data/reading/TOPICAL-PROTOCOL.md`.

- The decisions are in `triage/topical/TP01.json` to `TP50.json`, all 50 verified.
- The claims are in `triage/claims.json` and the series in `triage/series.json`.
- The 293 observations the readers recorded for a later pass are in `triage/topical-observations.json`.

## What came out

The 4,446 triage claims were grouped by subject into 124 groups and read in 50 batches. Readers made three kinds of link,
each backed by a verbatim phrase from every member:

- **155 `same` sets.** These are one claim stated in different words. They merge 301 claims, which leaves **4,145
  claims**:

  | Tier | Claims |
  |---|---|
  | Forecasts | 955 |
  | Standing claims | 914 |
  | Unbuilt tests | 959 |
  | Historical theses | 1,043 |
  | Priority records | 274 |

  926 claims now carry more than one statement.

- **56 `states` sets.** These are one claim revised over time. Each is kept in the order of the claim's development,
  with what changed at each step. The longest:

  | Claim | States | Course |
  |---|---|---|
  | Revelation First (#1132; 31 statements in all) | 12 | From "written first, 68–73 CE", through the TANG framing, the workshop clause added and dropped, and priority over the Synoptics, to "first in composition, not early" with its four-part falsifier (#202), carried as frame in #1483 |
  | The otium stanza of Catullus 51 (#313) | 9 | Through the erratum chain, ending at #1601 (see below) |
  | The Josephus Thesis (#1226) | 8 | From "authored", to "authored or substantially shaped", to "an available reading", to #837's disclaimer that Josephus personally wrote the 27 books |
  | Where Sappho 31 ends (#201) | 7 | From a reconstructed fifth stanza, to a hanging line, to Longinus's citation as the break, to the poem complete at πὰν τόλματον |
  | The machine as κῆνος's reader (#278) | 6 | Summarizer, then training layer, then the musical and liturgical registers |
  | The 1844 lacuna (#367) | 6 | "Marx could not write the passage", then the missing Second Manuscript, then a Grade C reconstruction of the passage's function |

  The rest include:
  - the Theophrastus–Λ demand and supply (#1595, 5)
  - the Logotic Programming conformance suite v0.9–1.2 (#461, 4)
  - the SE 34 placement of Socrates (#1574, 4)
  - the reversal from "not one hidden person" to "one hand wrote Plato and Socrates" (#1261 → #1569)

- **506 series.** These are distinct claims of one programme, battery or template, linked by name and kept separate.

The most restated single claims are:

| Claim | Statements |
|---|---|
| Revelation First | 31 |
| κῆνος as the future reader (#277) | 24 |
| The Josephus Thesis | 20 |
| The 1844 lacuna | 15 |
| The otium stanza | 14 |
| The *phainetai moi → si fas est → ei exestin* chain (#625) | 11 |

## Dates

A claim is registered at its earliest statement, so it is only as reliably dated as its deposit.

- **Fixed in this pass.** The 83 finds in the Capture Registry (#3) and #4 had taken the file's date (2026-06-17). They
  now take the date of the record that holds them. This comes from the record headings in the derived reading text
  (`triage/entry-dates.json`).
- **Not fixed: registry dates the texts contradict.** These are registry metadata, so they wait on Lee.

  | Deposit | Registered | The text says |
  |---|---|---|
  | #1226 (the Josephus Thesis's registration point) | 2026-01-01 | "Date: 14 June 2026" |
  | #1238, #1242, #1243 | 2026-01-01 | "Deposited 2026-04-17" |
  | #1240 | 2026-01-01 | 2026-04-01 |
  | #1241 | 2026-01-01 | April 7, 2026 |
  | #1246 | 2026-01-01 | 19 June 2026 |
  | #1247 | 2026-01-01 | Later statements are dated 2026-06-18 |
  | #1249 | 2026-01-01 | Headed "June 2026" |
  | #1389 | 2026-03-22 | Headed 2026-06-04; the March date matches a predecessor's identifier, …_20260322; the same text is #149 |
  | #1110 | 2026-01-13 | Is the Central Navigation Map v7.0 of 2026-03-16 |
  | #1251 | 2026-01-17 | Holds sections dated from 2026-02-07, and lists February deposits |

  In all, 22 deposits carry 2026-01-01; the ones above state another date in their text.

  Other cases readers flagged:
  - #1098 is registered at the poem's 2015 blog date for 2026 recovery framing.
  - #999's text is dated November 2025.
  - #1337 is titled MRA-2025-1224 but dated 2026-03-16.
  - #744 is registered at its deposit date for a 2015 text.

  Future dates inside fiction (2027, 2031, 2041, 2049, 2062) are the genre, not errors.

## What needs Lee

These are recorded and nothing has been changed:

1. **The registry dates above.** If the text's own date is the date of record, the registry entries are mislabelled
   records under the repair scope. Correcting them would move the registration of the Josephus Thesis and several
   others. Two examples:
   - The Irenaeus-anchor same set would register at #971 (2026-04-10), not #1226.
   - The Mary Lee induction forecast would register at #149, not #1389.
2. **The ordering of #1601.** #1601 is "a First Edition, Reconstructed from Its Corrections", the anticipatory-erratum
   genre. Its statement that the otium stanza "has no Greek counterpart" is placed last in the nine-step chain, by its
   registration date. The genre presents it as coming first.
3. **#402's appendix.** The current text of #402 carries the superseded wrong body, "Render unto the Operator", dated
   2026-05-24, as an appendix. #402's only find is drawn from it, so it registers that paper's PER definition at #402's
   January date.

## What the readers recorded

- **54 apparent contradictions or tensions**, recorded as observations and not reconciled. Examples:
  - two endings of Sappho 31 deposited the same day (#1474, #1478);
  - "a lost fourth stanza" (#281) against "the transmitted poem is complete";
  - #263 against #1634 on which held the name Crimson Hexagon first;
  - "Plato does not construct heteronymically" (#1570) against the heteronymic theses;
  - DOI deposits "cannot be removed" (#660, #661) against the seal that depends on the server (#540).
- **Claims that belong with claims in other groups.** These are named pairs across batches, a list for a closing
  cross-batch join.
- **Duplicate deposits:**
  - #467 and #892 are one essay.
  - #1585 and #1589 hold the same notebook text.
  - #498 and #499 may be versions of one work.

## Next

- A cross-batch join of the pairs the readers named (`topical-observations.json`).
- The re-reading of the text the record repair added, about 348,000 words.
- The attachments.
- The index's home, which waits on Lee's ruling.

## Rulings applied and the join pass (2026-10-17)

Lee Sharks, 2026-10-17:
- "go with the in text date and repair the dates"
- "we go by registration date"
- "lets join the pairs"

### Dates

Twelve alexanarch records now carry the date their own text states. The repair is alexanarch
`scripts/repair_dates_from_text_20261017.py`, which records each record's `date_basis` and its prior value.

| Record | Date now |
|---|---|
| #1226 | 2026-06-14 |
| #1234 | 2026-04-16 |
| #1235 | 2026-04-04 |
| #1236 | 2026-04-05 |
| #1237 | 2026-04-01 |
| #1238, #1242, #1243 | 2026-04-17 |
| #1240 | 2026-04-02 |
| #1241 | 2026-04-07 |
| #1246 | 2026-06-19 |
| #1389 | 2026-06-04 |

The claims take their dates from the current registry. The Josephus Thesis now registers at #203 (2026-06-14).

Left unchanged:
- #1110 and #1251: their own front matter states the registry date.
- #1247, #1249, #1233, #206 and #1239: the text gives no date.

### Order of states

A claim's states are ordered by registration date. Each state keeps the change the reader wrote for it, and the reader's
order is kept beside it as `read_order`. #1601 is last in the otium chain.

### The join pass

The 206 observations that named claims across groups were read in nine batches under `data/reading/JOIN-PROTOCOL.md`:

- 5 `same` sets;
- 2 `states` sets: #1570 → #1671 (the library channel, where the will premise is corrected) and #1497 → #1514 (the
  build list revised after the build);
- 86 series, many of them extending series by name.

Series with one name are now one series. The index now holds:

| | Count |
|---|---|
| Claims | 4,137 |
| Revised over time (states) | 58 |
| Series | 550 |
| Claims stated more than once | 928 |

### Still open, from the join readers

- **Two `same` sets to join.** #283.H7 + #1483.H4 (Catullus is κῆνος) state the same thesis as #281.H6 + #134.H2.
- **Links the batches could not make**, because a claim was not in the batch:
  - #1598.E1 belongs in the anticipatory-erratum sequence with #1601.H3.
  - #1226.G1 and #1249.H3 belong in the Josephus Thesis chain.
  - #1054.G1 belongs in "Sappho 31 in the compression layer".
  - #1486.F8 belongs in the Philo blind-reconstruction series.
- **Near-duplicate series names**, such as the Sappho 31 and diversity-contraction variants. These are left as named.
- **Registry dates not covered by the ruling**, because the text states no other date for itself:
  - #1249 is headed "June 2026" with no day.
  - #1384 (05-21) summarizes #194, which says it was deposited 12 June 2026.
  - #1118 is registered 2026-01-18 for a July deposit.
- **Duplicates:** #467 = #892; #498 is a shorter version of #499.
- **#402** still carries the superseded "Render unto the Operator" body as an appendix. This has not been ruled on.
