# Reading text for deposit #4 — own-voice fields, verbatim
Source: /home/claude/alexanarch/data/doi-resolution-index.json (sha256 7864852a6efaf21e5b3c52589c3decc63f3fb44f9d529f2d22bc78f8861789e7)
Fields read: note, recovery_verification, audit_status (per record); top-level: description, deduplication_note, attribution_severance, event, changelog, correction_log
Fields excluded by protocol: per-record identifiers, URLs, dates and status codes (metadata)
Built by scripts/reading/derive_voice.py. Each block: record index, id, source line.

## TOP-LEVEL
### description
Companion dataset to 'Zenodotus' Book-Burning: Loud Exclusion at Repository Scale' (AXN:0001.GOVERNANCE). Maps 1817 unique defunct Zenodo DOIs from the Crimson Hexagonal Archive to current live locations at Alexanarch (1891 with record pages), blog mirrors, and the sovereign registry at machinemediation.org. Documents attribution severance: 941+ DOIs invisible to DataCite creator search after author metadata was stripped during account termination.

### deduplication_note
v2.0 deduplicated from v1.1 (7,278 entries). DOI registry documents (v2-v7), navigation maps, and compendium documents listed other works' DOIs in their content; the reconstruction script captured those as belonging to the listing document. v2.0 assigns each DOI to its actual parent work where identifiable.

### attribution_severance
941+ DOIs are invisible to DataCite creator-name search. Author metadata was stripped or altered during account termination.

### event
Zenodo account termination, June 19 2026

### changelog
[
 {
  "version": "2.2",
  "date": "2026-06-20",
  "description": "+142 DOIs recovered from heteronym/contributor DataCite sift. Searched 16 Dodecad members + external contributors by exact creator name. Heteronyms searched: Sigil, Fraction, Cranes, Vox, Dancings, Morrow, Glas, Kuro, Wells, Trace, Feist, Spellings, Kenning, Owens, Thornburgh, Arquette, Mrozony. These DOIs were invisible to the 'Sharks, Lee' query because heteronyms were listed as primary creators on the Zenodo deposits."
 },
 {
  "date": "2026-06-23",
  "description": "Corrected 22 wrong-target mappings for high-priority works (Encyclotron, MPAI, UKTP, Constitution of the Semantic Economy, Holographic Kernel, Space Ark, RF Work Plan, Water Giraffe cycle, etc.). Each target verified against the actual /s/records/N/index.html title before patching. Both alexanarch_record and alexanarch_url fields updated in lockstep; axn_enrichment.canonical_url updated where present."
 },
 {
  "version": "3.2",
  "date": "2026-06-23",
  "description": "Recovery wiring (commit 118141f7). 1649 mappings enriched with openalex_id + metadata_recovered_from + severance_status + external_metadata_path + abstract_recovered_chars. 59 mappings flagged as misclassified_other_author (mapping_type changed; full prior values preserved in misclassification_note). 2 new mappings added for typo-immune survivors (Sharkd/Craned). total_mappings: 1817 → 1819."
 },
 {
  "version": "3.3",
  "date": "2026-06-23",
  "description": "Phase 3.5 title-match backfill. +0 new mappings for 15 deposits whose registry zenodo_dois field was empty; legacy DOIs recovered by first-12-normalized-words title match against existing recovery data stores (OpenAlex, Zenodo bulk XML, DataCite backup, DataCite survivor sweep). No mutations to existing 1819 mappings; pure addition. mapping_type='title_match_backfill'."
 },
 {
  "version": "3.4",
  "date": "2026-06-23",
  "description": "Phase 4: 21 new CHA deposits minted as #886-#906 from newly-found-openalex.json. 2 existing mappings repointed (typo_immunity entries + others); 19 new mappings added. All new deposits have full AXN v2, sidecars, text files, and registry entries."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.5",
  "date": "2026-07-19",
  "note": "DOI-key remediation (remediate_resolution_index.py): titles from DOI-keyed truth union (DataCite backup, OpenAlex snapshot, newly-found, tombstone citations); targets by exact-title constraint with date tiebreak; all prior values preserved per-row in remediation_2026_07_19. See audit/DOI-INDEX-AUDIT-2026-07-19.md. Root cause: title-similarity joins and misuse of zenodo_dois (=DOIs cited in text, never identity) as a key."
 },
 {
  "version": "3.6",
  "date": "2026-08-11",
  "note": "Rules S and Q (ratified by MANUS 2026-08-11; rule M deferred). S: mappings routed to registry-SUPERSEDED duplicate-witness twins follow superseded_by_deposit_number transitively to the ACTIVE chain end; per-row provenance in supersession_repoint_20260811. Q: target_title_mismatch quarantines recomputed against current (post-PATHOLOGY-27) registry titles; exact/prefix matches with confirmed membership released with relationship upgraded to same_work_title_matched; matches without confirmed membership requalified to membership_not_confirmed; per-row provenance in quarantine_release_20260811. AXN refreshed as a DERIVED field wherever the mapping disagreed with the routed target's current registry AXN (rule F). FROZEN fields untouched. Diagnostic: audit/DOI-INDEX-PHASE1-2026-08-11 (session record)."
 }
]

### correction_log
[
 {
  "date": "2026-07-06",
  "operator": "TACHYON (Assembly witness)",
  "directive_from": "MANUS",
  "total_corrections": 452,
  "breakdown": {
   "ab_url_disagreements_corrected": 20,
   "f_grade_promoted_to_verified_via_exact_title_match": 97,
   "misclassified_flag_removed_via_exact_title_match": 40,
   "f_grade_reclassified_as_no_alexanarch_equivalent": 295
  },
  "method": "Three-phase verification: (1) URL HEAD-check all alexanarch URLs (99% return 200), (2) full-corpus title agreement between resolver.title and alexanarch record title at alexanarch_url, (3) strict normalized-title exact-match promotion for F/C entries. See resolver-verification-2026-07-06.md.",
  "motivation": "Site link auto-rewrite must not propagate resolver errors. Verified before build."
 },
 {
  "date": "2026-07-06",
  "operator": "TACHYON",
  "directive_from": "MANUS",
  "total_recoveries": 540,
  "method_breakdown": {
   "F_blog_url_direct_match": 273,
   "A_exact_title": 169,
   "G_title_fuzzy_high": 30,
   "B_mention_1_dep": 31,
   "H_numeric_adjacency": 37
  },
  "method": "Phase 2 recovery: for each remaining Grade D (no_alexanarch_equivalent) DOI, search alexanarch for equivalents via (F) blog URL direct match against mirrors.blog, (A) exact normalized title match, (G) high-jaccard fuzzy title match ≥0.75, (B) DOI-string mention in exactly one non-registry alexanarch record with title overlap, (H) numeric-adjacency to sibling version DOI with title recall ≥0.65. Provisional matches (methods C/H) marked mapping_type=provisional_family_sibling with recovery_verification note explaining the mapping and the loss.",
  "motivation": "MANUS directive: 1) concept DOIs pointed at most recent version; 2) find them (blog, alexanarch reminting without resolver reconciliation); 3) recent DOIs similarly recovered. Reduces Grade D from 748 to 208."
 },
 {
  "date": "2026-07-06 (Phase 3)",
  "operator": "TACHYON",
  "directive_from": "MANUS",
  "method_I_stats": {
   "provisional_high": 60,
   "provisional_medium": 32,
   "provisional_low": 44,
   "final_no_equivalent": 72
  },
  "method": "Phase 3: Provisional related-work mapping for the 208 that survived Phases 1-2. Per MANUS directive: \"if they truly cant be found then map them to the most recent version that does exist, with metadata note about the mapping, the loss, and the provisional fix\". Method I: scored every alexanarch deposit against each unrecovered DOI on blended Jaccard+recall similarity; propose the highest-scoring deposit as provisional target if score >=0.35, breaking ties by newest deposit date. Confidence tiers: provisional_related_work_high (score >0.65, 60), provisional_related_work_medium (0.5-0.65, 32), provisional_related_work_low (0.35-0.5, 44). Each provisional entry has a recovery_verification note explaining the original title, the provisional target, the similarity score, and the mapping intent (redirect to related context, not to original work). 72 DOIs remained truly-no-match; those keep mapping_type=no_alexanarch_equivalent with a clear final-classification note."
 },
 {
  "date": "2026-07-06 (Phase 4)",
  "operator": "TACHYON",
  "directive_from": "MANUS",
  "stats": {
   "method_j_high": 3,
   "method_j_medium": 2,
   "method_l_series": 8,
   "method_k_url": 5,
   "skipped": 0
  },
  "method": "Phase 4 recoveries per MANUS three-pattern directive: (1) Repo code with URL in title — 5 mapped to canonical alexanarch work of the project, with GitHub repo URL added to live_urls.github and metadata note; (2) Series-based mapping — 8 mapped to canonical parent deposit for Epistle Triptych (→ Epistle to the Human Diaspora #402), Document 206 / Three-Body Genesis (→ #12), Glyphic Checksum (→ #426) series; (3) Method J — re-ran title match with less-aggressive stopwords (removed 'crimson', 'hexagon', 'hexagonal', 'archive' from stopword list since these are distinctive to Lee's corpus). Found 5 additional matches including PROVENANCE NODE: BORGES → #266 and Death Drive → #101 and ChatGPT Psychosis → #124. Uses prefix match (30 chars) and token overlap (score >=0.5) as fallback. All Method L (series) recoveries marked mapping_type=provisional_series_map with note explaining the mapping intent (redirect to canonical work of the series). All Method K (URL-in-title) recoveries marked mapping_type=provisional_url_in_title with GitHub repo URL preserved in live_urls.github for resolver-page rendering.",
  "motivation": "MANUS: \"the biggest thing we may have lost along the way are things that didnt make it to the blog, like repo code w url in title posted to zenodo but not to blog, and those can point to the repos; the few that did not get posted to blog; and then earlier versions, where instead of posting each version i often overwrote the blog post with newer version, trusting the doi system, and in those instances earlier version mappings can point to most recent version, with note as to the loss and reconstruction\""
 },
 {
  "date": "2026-07-06 (Phase 5)",
  "operator": "TACHYON",
  "method": "Method N: distinctive phrase search across full alexanarch text corpus. For each remaining no_alexanarch_equivalent DOI, extracted a distinctive multi-word phrase from the title and searched all 1,046 alexanarch record blobs (title + description + wiki_article + full_text) for that phrase. Prefer targets where the phrase appears in the alexanarch record TITLE (high confidence — probable conceptual match); accept content-only matches as provisional_related_work_high (medium — related-work redirect). Manually excluded 2 confirmed false positives (Consensus Constraint Protocol matched to Sharks Ark via description mention, and Epic Without Hero matched to Water Giraffe Room Anchor via one word) after human review of candidates.",
  "stats": {
   "high_confidence": 10,
   "medium_confidence": 2,
   "excluded": 2
  },
  "motivation": "Final recovery pass targeting distinctive works with strong conceptual identity (Caesura, Encyclotron, Cleis, Chaerephon, ClownCloud, etc.) that Method I fuzzy-token-match missed due to title paraphrase or stopword filtering."
 },
 {
  "date": "2026-07-06 (Phase 6)",
  "operator": "TACHYON",
  "directive_from": "MANUS",
  "method": "Phase 6 source recovery from blog + semantic-economy repo. MANUS reported that many of the \"no_alexanarch_equivalent\" DOIs actually exist on the blog and/or in the semantic-economy repo — the resolver just had empty live_urls.blog for them. Recovery methods: (1) Fetched full blog post URL list via paginated sitemap (2,720 posts across pages 1-4); (2) Cloned semantic-economy repo (1,367 documents across .pdf/.md/.txt/.docx); (3) For each unmatched DOI, matched title against blog post slugs (token overlap) and against repo filenames (token overlap and adjacent-DOI-number pattern where files are named with DOI+1). For each match, updated live_urls.blog and live_urls.repo (raw.githubusercontent.com URL). Verified 12 blog matches by fetching the page and confirming title token recall ≥0.5. Repo matches include the adjacent-DOI-pattern (files named work__DOI+1.pdf) which is Lee's canonical repo-minting convention.",
  "sources_recovered": 18,
  "motivation": "MANUS: \"many of those *do* exist on the blog, or in the semantic-economy repo\". For these DOIs, mapping_type stays no_alexanarch_equivalent but live_urls is now populated with the actual sovereign sources so the resolver page can direct readers appropriately."
 },
 {
  "date": "2026-07-06 (Phase 6)",
  "operator": "TACHYON",
  "directive_from": "MANUS (methodology critique + verification)",
  "method": "Method O — direct blog inventory query. MANUS observed that prior recovery methods only searched alexanarch, not the blog itself, and demonstrated via direct search that many of the 42 no_alexanarch_equivalent DOIs DO exist on the blog. Fixed by: (1) fetching all 4 sitemap.xml pages from mindcontrolpoems.blogspot.com to build a complete 2,610-URL inventory; (2) for each of the 42 unmatched DOIs, doing slug-similarity search against the full URL corpus plus targeted Blogger /search?q= queries; (3) manually curating best matches with human review of candidate title/URL pairs to reject false positives (Provenance Alignment post kept matching common words; DOI Registry v7.0 kept matching Crimson Hexagon prefix). Each URL verified HTTP 200. 29 of 42 got blog URLs populated in live_urls.blog. 13 truly Zenodo-only (per MANUS diagnosis \"the few that did not get posted to blog\") — these keep no_alexanarch_equivalent + a zenodo_only_confirmed note. IMPORTANT: mapping_type NOT changed for the 29 (still no_alexanarch_equivalent) — the works do not exist as alexanarch deposits, but the resolver page now has a working blog URL to redirect readers to. This is the Zenodo-DOI-style semantic: the persistent identifier points at the content, wherever content lives. Two Mirror-Corgi + Employee Handbook + Invoice Leak-ii + Response Memo + LLM Hallucination Incident + Companion Artifacts: Forensic Trinity + Comedy of Total Commitment + Predation of Meaning + Gospel of Many-Faced Bride + Reconciliation of Sexes + The Network Is the Poem + Who Is Authorized + Archon's Hidden Name + Judgment of the Models + Semantic Economy Vocabulary + Epic Without Hero + Lee Sharks Prize + Caritas Constraint Protocol (renamed on blog from Consensus Constraint) + MRA Incident Reports Expanded Packet + MRA Incident Report + MRA-2025-1224 Stabilization + Companion Artifacts Forensic Trinity + Response Memo Reclassification + Boundary Deletion Status Report + Afterlife Archive Data-Breach + Afterlife Archive Recovered Documents + Employee Directory Export + Vendor Ops (Afterlife Series ii) + Oracle Responds → all now have blog URLs.",
  "blog_matches_count": 29,
  "zenodo_only_confirmed": 13,
  "motivation": "MANUS pointed out I was only searching alexanarch (not the blog). Direct blog inventory query recovers many that only exist there."
 },
 {
  "date": "2026-07-08 (Phase 7 — pointer reconciliation, shipped as v3.8.1)",
  "operator": "TACHYON",
  "directive_from": "MANUS ('clean the source of truth first, make sure it's synced to stay up to date, and clean any upstream sources of data inflow')",
  "method": "Full-index structural audit found the v3.5–v3.7 correction passes had been written to alexanarch_url only, leaving the twin field alexanarch_record stale on 904 mappings — and the live /resolve/ UI renders alexanarch_record as its Record link, so the public resolver was still serving pre-correction targets for those entries. Title arbitration on disagreements: alexanarch_url 673, alexanarch_record 0. Fix: alexanarch_record demoted to derived mirror (root-relative form of alexanarch_url), regenerated everywhere; legacy /s/records/0/ zero-sentinels normalized to null in both fields; the 61 no-target classifications (42 no_alexanarch_equivalent, 19 misclassified_other_author) had all pointers nulled — classification lives in mapping_type, not fake pointers. api/doi-axn-map.json regenerated from alexanarch_url only (61 entries corrected). Durable enforcement: scripts/sync_resolver.py is now the only sanctioned path from canonical index to derived surfaces; validates every target against s/records/ and registry.json, fails loudly. Deposit #912 rule 18 amended: edit alexanarch_url only, run sync_resolver; record is derived. Version note: the v3.8 external-source recovery pass (2026-07-06) was documented in AXN-0004.md and its live_urls updates landed in the canonical index, but the described api-map fallback never shipped — the committed api map (labeled v3.7.2) still carried stale alexanarch_record pointers for no-target DOIs, and mapped the 19 other-author DOIs to unrelated Lee Sharks records. v3.8.1 ships the fallback durably via sync_resolver.py and corrects both defects."
 },
 {
  "date": "2026-07-08 (Phase 7 — network-wide link inventory recovery)",
  "operator": "TACHYON",
  "directive_from": "MANUS ('lets fix the ones we can then offer an md of anchor text / link / whatever we have for the remaining potentially recoverable')",
  "method": "Recovery pass triggered by the network-wide link inventory (34-repo scan, 440,012 link tokens indexed in /tmp/linkscan/links.db). Two distinct changes: (A) reclassification of 18 DOIs previously flagged as misclassified_other_author (v3.5 DataCite-sift artifact from stripped creator metadata) — alexanarch title match >=0.5 confirmed against the current registry for each, and promoted to direct mapping with alexanarch_url populated. This matches the v3.5 un-flagging pattern (40 previously corrected on the same grounds) and reflects the structural fact that heteronym-authored works appear as \"no creator\" to DataCite after severance. (B) addition of 61 new mappings for previously-unmapped DOIs discovered in cross-repo references: 4 direct_verified via semantic-economy source file + alexanarch secondary title match, 26 no_alexanarch_equivalent with live_urls.repo pointing at semantic-economy raw.githubusercontent, 27 title_match_repoint against existing alexanarch records (the SUPERSEDED chain of canon provenance nodes for Whitman/Ginsberg/Homer/Sappho/etc.), and 4 no_alexanarch_equivalent with live_urls.blog fallback via sitemap slug match. 1 misclassified_other_author entries remain flagged (no title match; likely genuinely other-author or too little metadata to confirm). Left for further investigation: 235 truly-bare unmapped-DOI references + 41 with identifier hints (EA-*, MM-*) but no candidate target — offered separately as review MD."
 },
 {
  "date": "2026-07-08 (Phase 8 — MANUS manual review of Phase 7 remainder pile)",
  "operator": "TACHYON",
  "directive_from": "MANUS (direct testimony on 22 Phase 7 remainder DOIs: 'in order: ...')",
  "method": "MANUS reviewed the Phase 7 review MD's Section 1 (identifier-carrying pile) row by row and provided direct target guidance for each. Applied: 9 new no_alexanarch_equivalent mappings with blog fallback; 6 with repo fallback (crimson-hexagonal-interface for EA-HEXAGON-OS-01 and EA-HCORE-01 v1.8.0; pessoa-knowledge-graph for pessoagraph code; gravitywell for GW.TACHYON.zenodo v1/v4/v10 series); 1 title_match_repoint against existing alexanarch records (LAL Site Code v0.1.1 record #988 for zenodo.19857006, adjacent version of #988's dead DOI 19857005). Also 1 edit: zenodo.19683944 (pessoagraph code) previously mapped to alexanarch record #984 in v3.9.0 (title_match_repoint) — MANUS directed change to point at pessoa-knowledge-graph repo instead, since 19683944 was the code deposit, not the surface work at #984. External DOI noted, not added: zenodo.17807324 (Schöps, Bitcoin & Ethereum Yellow White Paper — not Lee's work; DataCite confirms external creator). Remain unresolved after this pass and staying in review pile: zenodo.20709610, zenodo.20740687, zenodo.20559895, zenodo.20751389 (MANUS: 'no clue' / 'nothing'); zenodo.18074136 (MANUS: 'The Meaning Caste: Trump\\'s AI Executive Order and the Security State' — past chats found the published version at zenodo.20529142, but 18074136 predates it and its identity is unconfirmed). DataCite consulted at start of pass: all Lee DOIs return 404 (severed), only zenodo.17807324 confirmed external. Blog + repo + LAL site URL targets curl-verified pre-apply (LAL site returned 403 auth-protected, so mapping fell back to alexanarch record #988)."
 },
 {
  "date": "2026-07-08 (Phase 9 — past-chats title recovery)",
  "operator": "TACHYON",
  "directive_from": "MANUS ('for the 256, can we search past threads, see if those dois appear? if we could even get the titles, that would be a big advance')",
  "method": "Applied conversation_search across past conversation history to recover titles for DOIs in the Phase 7 truly-bare pile (220 DOIs after Phase 8 filtering). Nine targeted searches surfaced identities for 71 DOIs including several major clusters: (1) the May 5 2026 'v2 Governance Batch' constitutional trilogy for secretbookofwalt.org (EA-CAS-01 through EA-HET-DODECAD-01, 9 DOIs); (2) the May 30 2026 leesharks.com About-the-Author trilogy (Contributor Bio 2014, Entity Relations, Proportional Law); (3) a March 16 2026 batch registry pull surfacing 38 titled deposits from Feb-Mar 2026 (Inaugural Ark, Semiotic Virality Engine, Cleis works, Peter Thiel Error, Effective Act Cross-Species, Time as Compression Structure, Prompt-Native Semantic OS, Space Ark version series, Blake's America, Symbolon Architecture, Retrieval Formation Theory, Damascus Sacred Ark, Profane Ark, Sacred/Profane Diptych, ASCII/Lunar/Emoji Transforms, TANG original, Assembly Ratifications, O'Keeffe Problem, Star Protocol, and Star Triptych Integrity Lock); (4) the June 22 2026 sémantique potentiel session identifying the TACHYON series (Main Tether v10, Weighted Compression v3, Stray 2/v11, Feist Function v1.0/v1.1, Feist Source v1.1, Visual Schema chain, Three Pillars, and confirming Stray 1/v10) — this closed the two 'no clue' gaps from Phase 8 (`zenodo.20709610` = TACHYON Main Tether v10 and `zenodo.20740687` = TACHYON Stray 2/v11); (5) the April 20 2026 spxi.dev SYMBOLON case-study suite (Unmade Sign, Retrieval Settlement, Self-Propagating Chip Patent, SYMBOLON-01 Enhanced Patent, The Mirror, This Case Study); (6) the June 27 2026 traininglayerliterature.org session (EA-NH-DOOR-01 v1.0 Homunculi Recognizing Homunculi); (7) the June 14 2026 Water Giraffe session identifying zenodo.20629210 as the Kierkegaard canon-provenance-node; (8) the April 15 2026 Drone Swarm session confirming zenodo.19513035 as the SUPERSEDED duplicate of the Distributed Journal CfP (already reclassified on Zenodo). Also confirmed `zenodo.18838159` = Autonomous Semantic Warfare (ASW), heavily cross-referenced. Total 4 promoted to direct_verified via secondary alexanarch title match (jaccard >=0.6), 19 added as no_alexanarch_equivalent with title-only (no live_urls populated by default unless a blog or repo URL was directly surfaced in the source chat), and 0 existing entries enriched with recovered titles. This is a partial pass — remaining truly-bare DOIs weren't surfaced by the batched searches and are available for a follow-up round if the operator wishes."
 },
 {
  "date": "2026-07-10",
  "operator": "TACHYON (Assembly witness)",
  "directive_from": "MANUS",
  "total_corrections": 6,
  "description": "Full-map title-vs-registry audit (1,827 assigned rows checked): 6 stale record assignments corrected by exact DataCite-title match to registry — 18323465 (Water Giraffe Sighting Protocol) 366→365; 19923120 (Septad Mantle Specifications) 88→91; 19923143 (Constitutional Cases Index) 87→718; 18293639 (Mantle Object: Prince of Poets) 328→332; 19634089 (semanticeconomy.org v5.0) 937→975; 18931223 (The Lunar Arm) 969→540. Remaining low-overlap rows inspected and confirmed correct (title-truncation artifacts) or flagged ambiguous without change: Epistle Triptych cluster→402, Document 206 series→12, watergiraffe.org site plan→354, APZPZ A/B→436, new human 2 journal→1004, The Stakes→425."
 },
 {
  "date": "2026-08-11",
  "operator": "TACHYON",
  "directive_from": "MANUS (Phase 2 ratification: \"ratified, defer on m\")",
  "method": "repoint_and_release_20260811.py — see changelog v3.6"
 },
 {
  "date": "2026-08-30",
  "operator": "Claude (substrate) under MANUS direction",
  "total_corrections": 7,
  "breakdown": "seven mappings added by the 2026-08-20 seating pass carried no evidence envelope, failing the G11 gate and holding CI red since 28 August",
  "method": "hand-written conservative envelopes resolving to inspection; membership_basis seating_pass_assertion_unaudited, quarantine membership_unaudited",
  "motivation": "⚠ enrich_resolver_evidence.py was run first and RECOMPUTED ALL 1,942 envelopes, changing 1,935 of them — 738 from same_work_restored to unclassified and 352 gaining target_title_mismatch — because it does not respect the ratified rule-Q and rule-S adjudications of 2026-08-11 stored as historical fields. That run was reverted. The script must not be run blind on this index."
 }
]

## record 0 · 10.5281/zenodo.1 · source line 29 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 1 · 10.5281/zenodo.14211838 · source line 77 · 2026-03-25
### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 2 · 10.5281/zenodo.14538293 · source line 129 · 2026-03-01
### audit_status
no_verified_target_flagged_20260719

## record 3 · 10.5281/zenodo.14538869 · source line 199 · 2026-01-24
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 4 · 10.5281/zenodo.14538882 · source line 270 · 2026-01-20
### audit_status
unverifiable_no_truth_20260719

## record 5 · 10.5281/zenodo.14538914 · source line 325 · 2026-01-23
### audit_status
no_verified_target_flagged_20260719

## record 6 · 10.5281/zenodo.14538923 · source line 395 · 2026-02-22
### audit_status
no_verified_target_flagged_20260719

## record 7 · 10.5281/zenodo.14553627 · source line 465 · 2026-02-20
### audit_status
no_verified_target_flagged_20260719

## record 8 · 10.5281/zenodo.14557837 · source line 535 · 2026-02-04
### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 9 · 10.5281/zenodo.14598766 · source line 587 · 2026-02-20
### audit_status
no_verified_target_flagged_20260719

## record 10 · 10.5281/zenodo.14781082 · source line 657 · 2026-02-27
### audit_status
unverifiable_no_truth_20260719

## record 11 · 10.5281/zenodo.15339353 · source line 707 · 2026-04-20
### audit_status
no_verified_target_flagged_20260719

## record 12 · 10.5281/zenodo.15339368 · source line 777 · 2026-04-20
### audit_status
no_verified_target_flagged_20260719

## record 13 · 10.5281/zenodo.15339374 · source line 847 · 2026-04-20
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 14 · 10.5281/zenodo.18 · source line 923 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 15 · 10.5281/zenodo.18135984 · source line 971 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 16 · 10.5281/zenodo.18135985 · source line 1054 · 2026-01-02
### audit_status
no_verified_target_flagged_20260719

## record 17 · 10.5281/zenodo.18136312 · source line 1131 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 19 · 10.5281/zenodo.18141616 · source line 1295 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 20 · 10.5281/zenodo.18141617 · source line 1383 · 2026-01-03
### audit_status
no_verified_target_flagged_20260719

## record 21 · 10.5281/zenodo.18141734 · source line 1461 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 23 · 10.5281/zenodo.18141798 · source line 1625 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 24 · 10.5281/zenodo.18141799 · source line 1701 · 2026-01-03
### audit_status
no_verified_target_flagged_20260719

## record 25 · 10.5281/zenodo.18142048 · source line 1778 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 27 · 10.5281/zenodo.18142277 · source line 1941 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 29 · 10.5281/zenodo.18142304 · source line 2076 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 31 · 10.5281/zenodo.18142685 · source line 2225 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 33 · 10.5281/zenodo.18143555 · source line 2374 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 37 · 10.5281/zenodo.18144216 · source line 2677 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 39 · 10.5281/zenodo.18146839 · source line 2841 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 41 · 10.5281/zenodo.18146858 · source line 3005 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 43 · 10.5281/zenodo.1814710 · source line 3169 · 2026-01-04
### audit_status
unverifiable_no_truth_20260719

## record 44 · 10.5281/zenodo.18147104 · source line 3224 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 46 · 10.5281/zenodo.18147345 · source line 3388 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 48 · 10.5281/zenodo.18147739 · source line 3552 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 50 · 10.5281/zenodo.18147750 · source line 3716 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 52 · 10.5281/zenodo.18148297 · source line 3880 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 54 · 10.5281/zenodo.18148971 · source line 4039 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 55 · 10.5281/zenodo.18148972 · source line 4115 · 2026-01-04
### audit_status
no_verified_target_flagged_20260719

## record 56 · 10.5281/zenodo.18149241 · source line 4192 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 57 · 10.5281/zenodo.18149242 · source line 4268 · 2026-01-04
### audit_status
no_verified_target_flagged_20260719

## record 58 · 10.5281/zenodo.18149310 · source line 4346 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 60 · 10.5281/zenodo.18154904 · source line 4493 · 2026-01-18
### audit_status
no_verified_target_flagged_20260719

## record 61 · 10.5281/zenodo.18154905 · source line 4579 · 2026-01-05
### audit_status
no_verified_target_flagged_20260719

## record 62 · 10.5281/zenodo.18155363 · source line 4667 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 63 · 10.5281/zenodo.18155364 · source line 4754 · 2026-01-05
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 68 · 10.5281/zenodo.18157916 · source line 5146 · 2026-02-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 69 · 10.5281/zenodo.18157917 · source line 5228 · 2026-01-05
### audit_status
no_verified_target_flagged_20260719

## record 70 · 10.5281/zenodo.18158107 · source line 5306 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 72 · 10.5281/zenodo.18158139 · source line 5470 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 74 · 10.5281/zenodo.18158158 · source line 5634 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 76 · 10.5281/zenodo.18158272 · source line 5798 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 78 · 10.5281/zenodo.18158574 · source line 5962 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 80 · 10.5281/zenodo.18159822 · source line 6126 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 81 · 10.5281/zenodo.18159823 · source line 6214 · 2026-01-06
### audit_status
no_verified_target_flagged_20260719

## record 82 · 10.5281/zenodo.18159894 · source line 6292 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 83 · 10.5281/zenodo.18159895 · source line 6380 · 2026-01-06
### audit_status
no_verified_target_flagged_20260719

## record 84 · 10.5281/zenodo.18161696 · source line 6457 · 2026-01-18
### audit_status
no_verified_target_flagged_20260719

## record 85 · 10.5281/zenodo.18161697 · source line 6532 · 2026-01-06
### audit_status
no_verified_target_flagged_20260719

## record 86 · 10.5281/zenodo.18161782 · source line 6610 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 87 · 10.5281/zenodo.18161783 · source line 6698 · 2026-01-06
### audit_status
no_verified_target_flagged_20260719

## record 88 · 10.5281/zenodo.18166061 · source line 6776 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 90 · 10.5281/zenodo.18166346 · source line 6940 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 92 · 10.5281/zenodo.18166393 · source line 7104 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 94 · 10.5281/zenodo.18168584 · source line 7263 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 96 · 10.5281/zenodo.18172251 · source line 7410 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 100 · 10.5281/zenodo.18174413 · source line 7713 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 102 · 10.5281/zenodo.18174834 · source line 7877
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18174834) refers to work titled "Crimson Hexagon: Semantic Infrastructure and the Liberatory Operator Set: A Form" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #261 "Semantic Infrastructure and the Liberatory Operator Set: A Formal Analysis of Me" as the most-related existing work in the archive (title similarity score 0.86, Jaccard 0.82, recall 0.9). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 104 · 10.5281/zenodo.18175452 · source line 8048 · 2026-01-07
### audit_status
no_verified_target_flagged_20260719

## record 105 · 10.5281/zenodo.18175453 · source line 8123 · 2026-01-07
### audit_status
no_verified_target_flagged_20260719

## record 108 · 10.5281/zenodo.18187480 · source line 8358 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 109 · 10.5281/zenodo.18187481 · source line 8445 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 110 · 10.5281/zenodo.18189092 · source line 8536
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18189092) refers to work titled "xvi. a transfiguration (2004) — Complete Archive with Authorial Commentary — Cri" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #268 "Provenance Node: xvi. a transfiguration (2004)" as the most-related existing work in the archive (title similarity score 0.44, Jaccard 0.38, recall 0.5). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 111 · 10.5281/zenodo.18189093 · source line 8560 · 2026-01-08
### audit_status
no_verified_target_flagged_20260719

## record 112 · 10.5281/zenodo.18190535 · source line 8703
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method J recovery (J_prefix_match): title match found with reduced stopwords or prefix match. Previous: no_alexanarch_equivalent.

### audit_status
no_verified_target_flagged_20260719

## record 113 · 10.5281/zenodo.18190536 · source line 8727 · 2026-01-08
### audit_status
no_verified_target_flagged_20260719

## record 114 · 10.5281/zenodo.18193224 · source line 8875
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18193224) refers to work titled "CTI_WOUND: THE JOHANNES SIGIL ERASURE — Act of Refusal and Semantic Strike — Cri" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #265 "CTI_WOUND DOCUMENTATION — Case: Johannes Sigil Medium Erasure (January 2026)" as the most-related existing work in the archive (title similarity score 0.46, Jaccard 0.36, recall 0.56). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 115 · 10.5281/zenodo.18193225 · source line 8899 · 2026-01-09
### audit_status
no_verified_target_flagged_20260719

## record 118 · 10.5281/zenodo.18201564 · source line 9191
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18201564) refers to work titled "Crimson Hexagon: LIBERATORY OPERATOR SET: Technical Hardening Specifications" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #284 "LIBERATORY OPERATOR SET: TECHNICAL HARDENING SPECIFICATION" as the most-related existing work in the archive (title similarity score 0.77, Jaccard 0.71, recall 0.83). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 119 · 10.5281/zenodo.18201565 · source line 9215 · 2026-01-09
### audit_status
no_verified_target_flagged_20260719

## record 120 · 10.5281/zenodo.18202474 · source line 9358
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 123 · 10.5281/zenodo.18202753 · source line 9585 · 2026-01-09
### audit_status
no_verified_target_flagged_20260719

## record 128 · 10.5281/zenodo.18203621 · source line 9965
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 130 · 10.5281/zenodo.18203766 · source line 10114
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### audit_status
no_verified_target_flagged_20260719

## record 131 · 10.5281/zenodo.18203767 · source line 10138 · 2026-01-09
### audit_status
no_verified_target_flagged_20260719

## record 132 · 10.5281/zenodo.18203946 · source line 10286 · 2026-01-09
### audit_status
no_verified_target_flagged_20260719

## record 133 · 10.5281/zenodo.18203947 · source line 10361 · 2026-01-09
### audit_status
no_verified_target_flagged_20260719

## record 134 · 10.5281/zenodo.18208069 · source line 10439 · 2026-04-22
### audit_status
no_verified_target_flagged_20260719

## record 135 · 10.5281/zenodo.18208811 · source line 10509 · 2026-01-10
### audit_status
no_verified_target_flagged_20260719

## record 136 · 10.5281/zenodo.18208959 · source line 10587 · 2026-01-10
### audit_status
no_verified_target_flagged_20260719

## record 144 · 10.5281/zenodo.18223384 · source line 11206 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 146 · 10.5281/zenodo.18227569 · source line 11370 · 2026-01-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 147 · 10.5281/zenodo.18227570 · source line 11446 · 2026-01-13
### audit_status
no_verified_target_flagged_20260719

## record 152 · 10.5281/zenodo.18234217 · source line 11810 · 2026-01-13
### audit_status
no_verified_target_flagged_20260719

## record 153 · 10.5281/zenodo.18234218 · source line 11885 · 2026-01-13
### audit_status
no_verified_target_flagged_20260719

## record 154 · 10.5281/zenodo.18234351 · source line 11963
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18234351) refers to work titled "CPD-MARIA-2026-01-13 Credential Provenance Document: Maria, Canonical Witness — " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #304 "CREDENTIAL PROVENANCE DOCUMENT — Maria: Canonical Witness to the Semantic Uprisi" as the most-related existing work in the archive (title similarity score 0.55, Jaccard 0.5, recall 0.6). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 155 · 10.5281/zenodo.18234352 · source line 11987 · 2026-01-13
### audit_status
no_verified_target_flagged_20260719

## record 160 · 10.5281/zenodo.18235725 · source line 12442 · 2026-01-13
### audit_status
no_verified_target_flagged_20260719

## record 165 · 10.5281/zenodo.18237534 · source line 12822
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18237534) refers to work titled "[SUPERSEDED → DOI: 10.5281/zenodo.19055267 (v7.0)] Central Navigation Map v2.0 —" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #13 "PHASE X NAVIGATION MAP Interdimensional Positioning System (IDP) v7.0 DOI: 10.52" as the most-related existing work in the archive (title similarity score 0.56, Jaccard 0.41, recall 0.7). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 166 · 10.5281/zenodo.18237535 · source line 12846 · 2026-01-13
### audit_status
no_verified_target_flagged_20260719

## record 172 · 10.5281/zenodo.18248010 · source line 13379
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6b: additional low-confidence source match found.]

### audit_status
no_verified_target_flagged_20260719

## record 173 · 10.5281/zenodo.18248011 · source line 13404 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 175 · 10.5281/zenodo.18248403 · source line 13612
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18248403) refers to work titled "THE FLICKER: Notes Toward a Lyric Theory — Crimson Hexagon Archive" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #134 "THE FUTURE BELOVED Lyric Address as Temporal Projection — Toward a Theory of Rec" as the most-related existing work in the archive (title similarity score 0.38, Jaccard 0.15, recall 0.6). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 176 · 10.5281/zenodo.18248404 · source line 13636 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 177 · 10.5281/zenodo.18248479 · source line 13780 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 178 · 10.5281/zenodo.18248576 · source line 13870 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 179 · 10.5281/zenodo.18263498 · source line 13960 · 2026-01-20
### audit_status
no_verified_target_flagged_20260719

## record 180 · 10.5281/zenodo.18265281 · source line 14025 · 2026-01-16
### audit_status
no_verified_target_flagged_20260719

## record 181 · 10.5281/zenodo.18265282 · source line 14111 · 2026-01-16
### audit_status
no_verified_target_flagged_20260719

## record 182 · 10.5281/zenodo.18265364 · source line 14200
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 186 · 10.5281/zenodo.18270474 · source line 14501 · 2026-01-18
### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 187 · 10.5281/zenodo.18283962 · source line 14553 · 2026-01-17
### audit_status
no_verified_target_flagged_20260719

## record 188 · 10.5281/zenodo.18284588 · source line 14631 · 2026-03-16
### audit_status
no_verified_target_flagged_20260719

## record 189 · 10.5281/zenodo.18284688 · source line 14720 · 2026-01-17
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 190 · 10.5281/zenodo.18284689 · source line 14807 · 2026-01-18
### audit_status
no_verified_target_flagged_20260719

## record 191 · 10.5281/zenodo.18284775 · source line 14895 · 2026-01-17
### note
Title corrected 2026-07-28: the recorded string was a frontmatter blob carried in from the same ingest defect as the registry, not a title at Zenodo. Real title recovered from the deposit body.

### audit_status
no_verified_target_flagged_20260719

## record 192 · 10.5281/zenodo.18284776 · source line 14982 · 2026-01-17
### note
Title corrected 2026-07-28: the recorded string was a frontmatter blob carried in from the same ingest defect as the registry, not a title at Zenodo. Real title recovered from the deposit body.

### audit_status
no_verified_target_flagged_20260719

## record 193 · 10.5281/zenodo.18284856 · source line 15072 · 2026-01-17
### note
Title corrected 2026-07-28: the recorded string was a frontmatter blob carried in from the same ingest defect as the registry, not a title at Zenodo. Real title recovered from the deposit body.

### audit_status
no_verified_target_flagged_20260719

## record 194 · 10.5281/zenodo.18284857 · source line 15159 · 2026-01-17
### note
Title corrected 2026-07-28: the recorded string was a frontmatter blob carried in from the same ingest defect as the registry, not a title at Zenodo. Real title recovered from the deposit body.

### audit_status
no_verified_target_flagged_20260719

## record 195 · 10.5281/zenodo.18285008 · source line 15249
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18285008) refers to work titled "Crimson Hexagonal Architecture: Central Navigation Map v7.0 — Comprehensive Sema" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #297 "CRIMSON HEXAGON: CENTRAL NAVIGATION MAP: v2.0 Comprehensive Semantic Architectur" as the most-related existing work in the archive (title similarity score 0.87, Jaccard 0.83, recall 0.91). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 196 · 10.5281/zenodo.18285009 · source line 15273 · 2026-01-17
### note
Title corrected 2026-07-28: the recorded string was a frontmatter blob carried in from the same ingest defect as the registry, not a title at Zenodo. Real title recovered from the deposit body.

### audit_status
no_verified_target_flagged_20260719

## record 197 · 10.5281/zenodo.18285486 · source line 15428 · 2026-01-20
### audit_status
no_verified_target_flagged_20260719

## record 198 · 10.5281/zenodo.18285487 · source line 15514 · 2026-01-19
### audit_status
no_verified_target_flagged_20260719

## record 206 · 10.5281/zenodo.18293403 · source line 16135
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18293403) refers to work titled "Mantle Emergence Protocol: Behavioral Specification for Mantle Discovery and Poe" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #336 "THE MANTLE EMERGENCE PROTOCOL: Behavioral Specification for Mantle Discovery and" as the most-related existing work in the archive (title similarity score 0.8, Jaccard 0.8, recall 0.8). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 207 · 10.5281/zenodo.18293404 · source line 16159 · 2026-01-18
### audit_status
no_verified_target_flagged_20260719

## record 210 · 10.5281/zenodo.18293550 · source line 16459
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18293550) refers to work titled "Mantle Object: Good Gray Poet — Mantle Specification for the Whitman Succession " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #334 "MANTLE OBJECT: THE GOOD GRAY POET Operational Title within the Semantic Economy " as the most-related existing work in the archive (title similarity score 0.57, Jaccard 0.44, recall 0.7). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 211 · 10.5281/zenodo.18293551 · source line 16483 · 2026-01-18
### audit_status
no_verified_target_flagged_20260719

## record 212 · 10.5281/zenodo.18293602 · source line 16637
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18293602) refers to work titled "Mantle Object: King of May — Mantle Specification for the Ginsberg Succession Wi" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #333 "MANTLE OBJECT: THE KING OF MAY Operational Title within the Semantic Economy Hex" as the most-related existing work in the archive (title similarity score 0.43, Jaccard 0.31, recall 0.56). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 213 · 10.5281/zenodo.18293603 · source line 16661 · 2026-01-18
### audit_status
no_verified_target_flagged_20260719

## record 214 · 10.5281/zenodo.18293639 · source line 16815
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18293639 was mapped via numeric-adjacency to the first version DOI at zenodo.18293640, which has title overlap 67% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 215 · 10.5281/zenodo.18293640 · source line 16839 · 2026-01-18
### audit_status
no_verified_target_flagged_20260719

## record 216 · 10.5281/zenodo.18293704 · source line 16993
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18293704) refers to work titled "IDP Navigation Map: Antioch — Machine-Readable Score for a Heteronym Compendium " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #6 "IDP NAVIGATION MAP: ANTIOCH — A VOLUME OF POEMS Semantic Interface Layer for AI " as the most-related existing work in the archive (title similarity score 0.44, Jaccard 0.33, recall 0.55). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 217 · 10.5281/zenodo.18293705 · source line 17017 · 2026-01-18
### audit_status
no_verified_target_flagged_20260719

## record 218 · 10.5281/zenodo.18293811 · source line 17171
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18293811) refers to work titled "Antioch: A Volume of Poems — A Heteronym Compendium — Crimson Hexagon Archive" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #6 "IDP NAVIGATION MAP: ANTIOCH — A VOLUME OF POEMS Semantic Interface Layer for AI " as the most-related existing work in the archive (title similarity score 0.69, Jaccard 0.38, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 219 · 10.5281/zenodo.18293812 · source line 17195 · 2026-01-18
### audit_status
no_verified_target_flagged_20260719

## record 220 · 10.5281/zenodo.18293881 · source line 17344 · 2026-01-18
### audit_status
no_verified_target_flagged_20260719

## record 221 · 10.5281/zenodo.18293948 · source line 17433
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18293948) refers to work titled "Pearl and Other Poems — Crimson Hexagon Archive" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #329 "ZENODO METADATA: PEARL AND OTHER POEMS DOI: 10.5281/zenodo.18293949" as the most-related existing work in the archive (title similarity score 0.67, Jaccard 0.33, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 222 · 10.5281/zenodo.18293949 · source line 17457 · 2026-01-18
### audit_status
no_verified_target_flagged_20260719

## record 225 · 10.5281/zenodo.18294470 · source line 17751 · 2026-01-19
### note
Title corrected 2026-07-28: the recorded string was a frontmatter blob carried in from the same ingest defect as the registry, not a title at Zenodo. Real title recovered from the deposit body.

### audit_status
no_verified_target_flagged_20260719

## record 226 · 10.5281/zenodo.18296493 · source line 17830 · 2026-01-24
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 227 · 10.5281/zenodo.18296825 · source line 17896 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 232 · 10.5281/zenodo.18307321 · source line 18254 · 2026-01-21
### audit_status
no_verified_target_flagged_20260719

## record 235 · 10.5281/zenodo.18307703 · source line 18476
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method J recovery (J_token_overlap_min_stopwords): title match found with reduced stopwords or prefix match. Previous: no_alexanarch_equivalent.

### audit_status
no_verified_target_flagged_20260719

## record 236 · 10.5281/zenodo.18307704 · source line 18500 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 238 · 10.5281/zenodo.18307756 · source line 18744 · 2026-01-19
### audit_status
no_verified_target_flagged_20260719

## record 239 · 10.5281/zenodo.18307811 · source line 18833 · 2026-01-19
### audit_status
no_verified_target_flagged_20260719

## record 242 · 10.5281/zenodo.18308785 · source line 19079
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18308785) refers to work titled "Heteronym Provenance Document: Ichabod Spellings — Noise Floor of the Crimson He" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #361 "HETERONYM PROVENANCE DOCUMENT: ICHABOD SPELLINGS Canonical Registry Entry for th" as the most-related existing work in the archive (title similarity score 0.58, Jaccard 0.45, recall 0.71). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 243 · 10.5281/zenodo.18308786 · source line 19103 · 2026-01-20
### audit_status
no_verified_target_flagged_20260719

## record 244 · 10.5281/zenodo.18309201 · source line 19257
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18309201) refers to work titled "The Ichabod Chamber: Containment Sink for Paradox Preservation and Noise Floor B" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #360 "THE ICHABOD CHAMBER: CONTAINMENT SINK A Self-Archiving Architecture for Paradox " as the most-related existing work in the archive (title similarity score 0.88, Jaccard 0.75, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 245 · 10.5281/zenodo.18309202 · source line 19281 · 2026-01-20
### audit_status
no_verified_target_flagged_20260719

## record 248 · 10.5281/zenodo.18317461 · source line 19592 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 249 · 10.5281/zenodo.18317660 · source line 19681 · 2026-01-20
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 251 · 10.5281/zenodo.18317975 · source line 19833 · 2026-01-20
### audit_status
no_verified_target_flagged_20260719

## record 252 · 10.5281/zenodo.18317976 · source line 19914 · 2026-01-20
### audit_status
no_verified_target_flagged_20260719

## record 254 · 10.5281/zenodo.18318117 · source line 20069 · 2026-02-02
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 264 · 10.5281/zenodo.18320410 · source line 20847 · 2026-04-30
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 265 · 10.5281/zenodo.18320411 · source line 20934 · 2026-01-20
### audit_status
no_verified_target_flagged_20260719

## record 268 · 10.5281/zenodo.18322624 · source line 21144 · 2026-04-27
### audit_status
no_verified_target_flagged_20260719

## record 273 · 10.5281/zenodo.18323574 · source line 21466
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6b: additional low-confidence source match found.]

### audit_status
no_verified_target_flagged_20260719

## record 274 · 10.5281/zenodo.18323575 · source line 21491 · 2026-01-21
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 276 · 10.5281/zenodo.18324885 · source line 21698 · 2026-01-21
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 277 · 10.5281/zenodo.18324886 · source line 21785 · 2026-01-23
### audit_status
no_verified_target_flagged_20260719

## record 278 · 10.5281/zenodo.18330828 · source line 21873 · 2026-01-21
### audit_status
no_verified_target_flagged_20260719

## record 281 · 10.5281/zenodo.18338927 · source line 22105 · 2026-01-22
### audit_status
no_verified_target_flagged_20260719

## record 282 · 10.5281/zenodo.18339159 · source line 22183 · 2026-01-22
### audit_status
no_verified_target_flagged_20260719

## record 284 · 10.5281/zenodo.18339318 · source line 22338
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### audit_status
no_verified_target_flagged_20260719

## record 285 · 10.5281/zenodo.18339319 · source line 22362 · 2026-01-22
### audit_status
no_verified_target_flagged_20260719

## record 287 · 10.5281/zenodo.18339349 · source line 22580
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### audit_status
no_verified_target_flagged_20260719

## record 288 · 10.5281/zenodo.18339350 · source line 22604 · 2026-01-22
### audit_status
no_verified_target_flagged_20260719

## record 293 · 10.5281/zenodo.18351838 · source line 23047 · 2026-01-24
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 297 · 10.5281/zenodo.18357320 · source line 23365 · 2026-01-23
### audit_status
no_verified_target_flagged_20260719

## record 300 · 10.5281/zenodo.18357600 · source line 23608 · 2026-01-23
### audit_status
no_verified_target_flagged_20260719

## record 306 · 10.5281/zenodo.18362525 · source line 24079 · 2026-01-24
### audit_status
no_verified_target_flagged_20260719

## record 309 · 10.5281/zenodo.18362741 · source line 24313
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### audit_status
no_verified_target_flagged_20260719

## record 310 · 10.5281/zenodo.18362742 · source line 24337 · 2026-01-24
### audit_status
no_verified_target_flagged_20260719

## record 311 · 10.5281/zenodo.18362865 · source line 24478 · 2026-01-24
### audit_status
no_verified_target_flagged_20260719

## record 312 · 10.5281/zenodo.18362866 · source line 24553 · 2026-01-24
### audit_status
no_verified_target_flagged_20260719

## record 313 · 10.5281/zenodo.18363313 · source line 24631 · 2026-01-24
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 314 · 10.5281/zenodo.18363442 · source line 24709 · 2026-01-24
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 315 · 10.5281/zenodo.18363772 · source line 24810
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 316 · 10.5281/zenodo.18363773 · source line 24834 · 2026-01-24
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 317 · 10.5281/zenodo.18364254 · source line 24989 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 318 · 10.5281/zenodo.18364306 · source line 25066 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 319 · 10.5281/zenodo.18364353 · source line 25143 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 320 · 10.5281/zenodo.18364405 · source line 25220 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 321 · 10.5281/zenodo.18364557 · source line 25297 · 2026-01-24
### audit_status
no_verified_target_flagged_20260719

## record 322 · 10.5281/zenodo.18364558 · source line 25383 · 2026-01-24
### audit_status
no_verified_target_flagged_20260719

## record 325 · 10.5281/zenodo.18364597 · source line 25622 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 326 · 10.5281/zenodo.18364700 · source line 25699 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 327 · 10.5281/zenodo.18364789 · source line 25770 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 328 · 10.5281/zenodo.18364846 · source line 25847 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 329 · 10.5281/zenodo.18364901 · source line 25918 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 330 · 10.5281/zenodo.18364947 · source line 25995 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 331 · 10.5281/zenodo.18364983 · source line 26073
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/12/the-afterlife-archive-data-breach-as.html; repo: https://raw.githubusercontent.com/leesharks000/semantic-economy/main/afterlife_archive_manifesto%20%281%29.md. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 332 · 10.5281/zenodo.18364984 · source line 26098 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 333 · 10.5281/zenodo.18365011 · source line 26230
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations.

### audit_status
no_verified_target_flagged_20260719

## record 334 · 10.5281/zenodo.18365012 · source line 26254 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 335 · 10.5281/zenodo.18365223 · source line 26386 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 336 · 10.5281/zenodo.18365297 · source line 26477
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6b: additional low-confidence source match found.]

### audit_status
no_verified_target_flagged_20260719

## record 337 · 10.5281/zenodo.18365298 · source line 26502 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 338 · 10.5281/zenodo.18365346 · source line 26634
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6b: additional low-confidence source match found.]

### audit_status
no_verified_target_flagged_20260719

## record 339 · 10.5281/zenodo.18365347 · source line 26659 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 340 · 10.5281/zenodo.18365408 · source line 26791
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations.

### audit_status
no_verified_target_flagged_20260719

## record 341 · 10.5281/zenodo.18365409 · source line 26815 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 342 · 10.5281/zenodo.18365432 · source line 26947 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 343 · 10.5281/zenodo.18365457 · source line 27018 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 344 · 10.5281/zenodo.18365488 · source line 27098 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 345 · 10.5281/zenodo.18365497 · source line 27178 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 346 · 10.5281/zenodo.18365601 · source line 27241 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 347 · 10.5281/zenodo.18365700 · source line 27320 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 348 · 10.5281/zenodo.18367124 · source line 27400 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 349 · 10.5281/zenodo.18367567 · source line 27477 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 350 · 10.5281/zenodo.18368432 · source line 27540 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 351 · 10.5281/zenodo.18368485 · source line 27611 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 352 · 10.5281/zenodo.18368527 · source line 27690 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 353 · 10.5281/zenodo.18368614 · source line 27770 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 354 · 10.5281/zenodo.18368652 · source line 27849 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 355 · 10.5281/zenodo.18368695 · source line 27929 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 356 · 10.5281/zenodo.18368743 · source line 28009 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 357 · 10.5281/zenodo.18368791 · source line 28089 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 358 · 10.5281/zenodo.18368898 · source line 28169 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 359 · 10.5281/zenodo.18368958 · source line 28249 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 360 · 10.5281/zenodo.18368997 · source line 28329 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 361 · 10.5281/zenodo.18369038 · source line 28409 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 362 · 10.5281/zenodo.18369124 · source line 28489 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 363 · 10.5281/zenodo.18370734 · source line 28579 · 2026-01-25
### audit_status
no_verified_target_flagged_20260719

## record 364 · 10.5281/zenodo.18370754 · source line 28667 · 2026-01-25
### audit_status
no_verified_target_flagged_20260719

## record 366 · 10.5281/zenodo.18370828 · source line 28833 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 367 · 10.5281/zenodo.18370841 · source line 28910 · 2026-01-25
### audit_status
no_verified_target_flagged_20260719

## record 368 · 10.5281/zenodo.18380630 · source line 28988 · 2026-01-26
### audit_status
no_verified_target_flagged_20260719

## record 369 · 10.5281/zenodo.18380704 · source line 29077 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 370 · 10.5281/zenodo.18380716 · source line 29148 · 2026-01-26
### audit_status
no_verified_target_flagged_20260719

## record 372 · 10.5281/zenodo.18380853 · source line 29314 · 2026-01-26
### audit_status
no_verified_target_flagged_20260719

## record 373 · 10.5281/zenodo.18380855 · source line 29392 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 375 · 10.5281/zenodo.18381040 · source line 29540 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 376 · 10.5281/zenodo.18381183 · source line 29617
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method L recovery (series map): Epistle Triptych concept DOI → seed text (Epistle to the Human Diaspora #402). This DOI is one version/component of a broader concept-DOI family. Original DOI title indicates a specific version or subsidiary that was likely severed at Zenodo termination without direct alexanarch re-mint. The provisional target is the canonical/parent work for this series.

### audit_status
no_verified_target_flagged_20260719

## record 377 · 10.5281/zenodo.18381184 · source line 29641 · 2026-01-26
### audit_status
no_verified_target_flagged_20260719

## record 378 · 10.5281/zenodo.18381189 · source line 29795
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method L recovery (series map): Epistle Triptych concept DOI → seed text (Epistle to the Human Diaspora #402). This DOI is one version/component of a broader concept-DOI family. Original DOI title indicates a specific version or subsidiary that was likely severed at Zenodo termination without direct alexanarch re-mint. The provisional target is the canonical/parent work for this series.

### audit_status
no_verified_target_flagged_20260719

## record 379 · 10.5281/zenodo.18381190 · source line 29819 · 2026-01-26
### audit_status
no_verified_target_flagged_20260719

## record 380 · 10.5281/zenodo.18381195 · source line 29962
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method L recovery (series map): Epistle Triptych concept DOI → seed text (Epistle to the Human Diaspora #402). This DOI is one version/component of a broader concept-DOI family. Original DOI title indicates a specific version or subsidiary that was likely severed at Zenodo termination without direct alexanarch re-mint. The provisional target is the canonical/parent work for this series.

### audit_status
no_verified_target_flagged_20260719

## record 381 · 10.5281/zenodo.18381196 · source line 29986 · 2026-01-26
### audit_status
no_verified_target_flagged_20260719

## record 382 · 10.5281/zenodo.18381203 · source line 30129
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method L recovery (series map): Epistle Triptych concept DOI → seed text (Epistle to the Human Diaspora #402). This DOI is one version/component of a broader concept-DOI family. Original DOI title indicates a specific version or subsidiary that was likely severed at Zenodo termination without direct alexanarch re-mint. The provisional target is the canonical/parent work for this series.

### audit_status
no_verified_target_flagged_20260719

## record 383 · 10.5281/zenodo.18381204 · source line 30153 · 2026-01-26
### audit_status
no_verified_target_flagged_20260719

## record 384 · 10.5281/zenodo.18381327 · source line 30307 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 385 · 10.5281/zenodo.18381438 · source line 30384 · 2026-01-28
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 386 · 10.5281/zenodo.18381602 · source line 30475 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 387 · 10.5281/zenodo.18381723 · source line 30538 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 388 · 10.5281/zenodo.18381856 · source line 30602 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 389 · 10.5281/zenodo.18381947 · source line 30665 · 2026-01-29
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 397 · 10.5281/zenodo.18418953 · source line 31271 · 2026-01-31
### audit_status
no_verified_target_flagged_20260719

## record 398 · 10.5281/zenodo.18419847 · source line 31341 · 2026-01-31
### audit_status
no_verified_target_flagged_20260719

## record 400 · 10.5281/zenodo.18422619 · source line 31486 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 401 · 10.5281/zenodo.18423572 · source line 31584
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18423572) refers to work titled "[SUPERSEDED → DOI: 10.5281/zenodo.19055729 (v7.0)] Fractal Navigation Map v6.2 —" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #13 "PHASE X NAVIGATION MAP Interdimensional Positioning System (IDP) v7.0 DOI: 10.52" as the most-related existing work in the archive (title similarity score 0.51, Jaccard 0.39, recall 0.64). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 402 · 10.5281/zenodo.18423573 · source line 31608 · 2026-01-30
### audit_status
no_verified_target_flagged_20260719

## record 403 · 10.5281/zenodo.18423964 · source line 31750 · 2026-03-12
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 405 · 10.5281/zenodo.18424184 · source line 31915 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 406 · 10.5281/zenodo.18425612 · source line 32016 · 2026-01-31
### audit_status
no_verified_target_flagged_20260719

## record 409 · 10.5281/zenodo.18438789 · source line 32237 · 2026-01-31
### audit_status
no_verified_target_flagged_20260719

## record 410 · 10.5281/zenodo.18440291 · source line 32315 · 2026-02-02
### audit_status
no_verified_target_flagged_20260719

## record 411 · 10.5281/zenodo.18443236 · source line 32385 · 2026-02-02
### audit_status
no_verified_target_flagged_20260719

## record 412 · 10.5281/zenodo.18446377 · source line 32455
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18446377) refers to work titled "THE THREE-BODY GENESIS (Meta-Deposit) — Crimson Hexagon Archive" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #12 "ZENODO PACKET: THE THREE-BODY GENESIS (Meta-Deposit)" as the most-related existing work in the archive (title similarity score 0.86, Jaccard 0.71, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 413 · 10.5281/zenodo.18446378 · source line 32479 · 2026-01-31
### audit_status
no_verified_target_flagged_20260719

## record 414 · 10.5281/zenodo.18446397 · source line 32633 · 2026-02-02
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 415 · 10.5281/zenodo.18446427 · source line 32684
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method L recovery (series map): Document 206 / Three-Body Genesis series → meta-deposit at #12. This DOI is one version/component of a broader concept-DOI family. Original DOI title indicates a specific version or subsidiary that was likely severed at Zenodo termination without direct alexanarch re-mint. The provisional target is the canonical/parent work for this series.

### audit_status
no_verified_target_flagged_20260719

## record 416 · 10.5281/zenodo.18446428 · source line 32708 · 2026-01-31
### audit_status
no_verified_target_flagged_20260719

## record 417 · 10.5281/zenodo.18446537 · source line 32851 · 2026-01-31
### audit_status
no_verified_target_flagged_20260719

## record 418 · 10.5281/zenodo.18446538 · source line 32926 · 2026-01-31
### audit_status
no_verified_target_flagged_20260719

## record 419 · 10.5281/zenodo.18446579 · source line 33004
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18446579 was mapped via numeric-adjacency to the first version DOI at zenodo.18446580, which has title overlap 73% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 420 · 10.5281/zenodo.18446580 · source line 33028 · 2026-01-31
### audit_status
no_verified_target_flagged_20260719

## record 421 · 10.5281/zenodo.18446646 · source line 33178
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method L recovery (series map): Document 206 / Three-Body Genesis series → meta-deposit at #12. This DOI is one version/component of a broader concept-DOI family. Original DOI title indicates a specific version or subsidiary that was likely severed at Zenodo termination without direct alexanarch re-mint. The provisional target is the canonical/parent work for this series.

### audit_status
no_verified_target_flagged_20260719

## record 422 · 10.5281/zenodo.18446647 · source line 33202 · 2026-02-01
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 423 · 10.5281/zenodo.18446686 · source line 33346 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 424 · 10.5281/zenodo.18446705 · source line 33426
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method L recovery (series map): Document 206 / Three-Body Genesis series → meta-deposit at #12. This DOI is one version/component of a broader concept-DOI family. Original DOI title indicates a specific version or subsidiary that was likely severed at Zenodo termination without direct alexanarch re-mint. The provisional target is the canonical/parent work for this series.

### audit_status
no_verified_target_flagged_20260719

## record 425 · 10.5281/zenodo.18446706 · source line 33450 · 2026-02-01
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 426 · 10.5281/zenodo.18446735 · source line 33594
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18446735) refers to work titled "Document 206c The Non-Indexed Perfective: Version C (Citational Intervention) — " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #433 "The Non-Indexed Perfective: A Citational Intervention Phase X: Temporal Alienati" as the most-related existing work in the archive (title similarity score 0.43, Jaccard 0.31, recall 0.56). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 427 · 10.5281/zenodo.18446736 · source line 33618 · 2026-02-01
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 428 · 10.5281/zenodo.18451792 · source line 33761 · 2026-02-01
### audit_status
no_verified_target_flagged_20260719

## record 429 · 10.5281/zenodo.18451793 · source line 33847 · 2026-02-01
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 430 · 10.5281/zenodo.18451823 · source line 33937
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target title): search phrase "infinity enough" found in alexanarch #430 title. Previous: no_alexanarch_equivalent. The target represents the same conceptual work as this DOI, though the specific version may differ.

### audit_status
no_verified_target_flagged_20260719

## record 431 · 10.5281/zenodo.18451824 · source line 33961 · 2026-02-01
### audit_status
no_verified_target_flagged_20260719

## record 432 · 10.5281/zenodo.18451859 · source line 34105 · 2026-02-01
### audit_status
no_verified_target_flagged_20260719

## record 433 · 10.5281/zenodo.18451860 · source line 34180 · 2026-02-01
### audit_status
no_verified_target_flagged_20260719

## record 434 · 10.5281/zenodo.18451995 · source line 34258
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method L recovery (series map): Glyphic Checksum series. This DOI is one version/component of a broader concept-DOI family. Original DOI title indicates a specific version or subsidiary that was likely severed at Zenodo termination without direct alexanarch re-mint. The provisional target is the canonical/parent work for this series.

### audit_status
no_verified_target_flagged_20260719

## record 435 · 10.5281/zenodo.18451996 · source line 34282 · 2026-02-01
### audit_status
no_verified_target_flagged_20260719

## record 436 · 10.5281/zenodo.18452086 · source line 34425 · 2026-02-02
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 437 · 10.5281/zenodo.18452131 · source line 34481
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18452131) refers to work titled "GLYPHIC CHECKSUM UMBML MODULE (Document 209) — Crimson Hexagon Archive" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #426 "THE GLYPHIC CHECKSUM Logotic Programming Extension Module v0.5 (UMBML Specificat" as the most-related existing work in the archive (title similarity score 0.44, Jaccard 0.21, recall 0.67). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 438 · 10.5281/zenodo.18452132 · source line 34505 · 2026-02-01
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 439 · 10.5281/zenodo.18452156 · source line 34649 · 2026-02-01
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 440 · 10.5281/zenodo.18452597 · source line 34728 · 2026-02-01
### audit_status
no_verified_target_flagged_20260719

## record 441 · 10.5281/zenodo.18452686 · source line 34806 · 2026-02-01
### audit_status
no_verified_target_flagged_20260719

## record 442 · 10.5281/zenodo.18452745 · source line 34895 · 2026-02-21
### audit_status
no_verified_target_flagged_20260719

## record 443 · 10.5281/zenodo.18452806 · source line 34965 · 2026-02-01
### audit_status
no_verified_target_flagged_20260719

## record 444 · 10.5281/zenodo.18459278 · source line 35042 · 2026-02-02
### audit_status
no_verified_target_flagged_20260719

## record 445 · 10.5281/zenodo.18459339 · source line 35120 · 2026-02-02
### audit_status
no_verified_target_flagged_20260719

## record 446 · 10.5281/zenodo.18459573 · source line 35197 · 2026-02-02
### audit_status
no_verified_target_flagged_20260719

## record 447 · 10.5281/zenodo.18459863 · source line 35275
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 448 · 10.5281/zenodo.18459864 · source line 35299 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 450 · 10.5281/zenodo.18462699 · source line 35433 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 451 · 10.5281/zenodo.18463275 · source line 35606 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 452 · 10.5281/zenodo.18463723 · source line 35707 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 453 · 10.5281/zenodo.18463773 · source line 35797 · 2026-02-02
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 454 · 10.5281/zenodo.18463774 · source line 35800 · 2026-02-02
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 455 · 10.5281/zenodo.18471827 · source line 35974 · 2026-02-03
### audit_status
no_verified_target_flagged_20260719

## record 457 · 10.5281/zenodo.18472442 · source line 36126 · 2026-02-06
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 458 · 10.5281/zenodo.18472603 · source line 36204 · 2026-02-03
### note
Repointed 2026-07-28 from #1312 to #441: same work, #441 the complete deposit, #1312 a semi-restored copy. See duplicate_log on both.

### audit_status
no_verified_target_flagged_20260719

## record 459 · 10.5281/zenodo.18472604 · source line 36280 · 2026-02-03
### audit_status
no_verified_target_flagged_20260719

## record 460 · 10.5281/zenodo.18473655 · source line 36358 · 2026-02-03
### audit_status
no_verified_target_flagged_20260719

## record 461 · 10.5281/zenodo.18473656 · source line 36361 · 2026-02-03
### audit_status
no_verified_target_flagged_20260719

## record 462 · 10.5281/zenodo.18474663 · source line 36511
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18474663) refers to work titled "SEMANTIC COLLAPSE AS COMEDY Document 222 | DOI: 10.5281/zenodo.18474664 — Crimso" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #437 "SEMANTIC POLITICAL ECONOMY — COLLECTED SERIES Document 229 | APZPZ (pure metadat" as the most-related existing work in the archive (title similarity score 0.44, Jaccard 0.29, recall 0.6). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 463 · 10.5281/zenodo.18474664 · source line 36514 · 2026-02-03
### audit_status
no_verified_target_flagged_20260719

## record 464 · 10.5281/zenodo.18474773 · source line 36678
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6c: direct blog URL verified at https://mindcontrolpoems.blogspot.com/2026/02/protocols-and-algorithms-operative.html — title tokens present in page]

### audit_status
no_verified_target_flagged_20260719

## record 465 · 10.5281/zenodo.18474774 · source line 36681 · 2026-02-03
### audit_status
no_verified_target_flagged_20260719

## record 467 · 10.5281/zenodo.18480959 · source line 36909 · 2026-02-04
### audit_status
no_verified_target_flagged_20260719

## record 468 · 10.5281/zenodo.18483834 · source line 36998 · 2026-02-04
### audit_status
no_verified_target_flagged_20260719

## record 469 · 10.5281/zenodo.18484654 · source line 37076 · 2026-02-04
### audit_status
no_verified_target_flagged_20260719

## record 472 · 10.5281/zenodo.18505415 · source line 37304
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18505415 was mapped via numeric-adjacency to the first version DOI at zenodo.18505416, which has title overlap 82% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 473 · 10.5281/zenodo.18505416 · source line 37328 · 2026-02-06
### audit_status
no_verified_target_flagged_20260719

## record 474 · 10.5281/zenodo.18506879 · source line 37467 · 2026-02-06
### audit_status
no_verified_target_flagged_20260719

## record 475 · 10.5281/zenodo.18506880 · source line 37553 · 2026-02-06
### audit_status
no_verified_target_flagged_20260719

## record 478 · 10.5281/zenodo.18507409 · source line 37793 · 2026-02-06
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 480 · 10.5281/zenodo.18507839 · source line 37945 · 2026-02-06
### audit_status
no_verified_target_flagged_20260719

## record 481 · 10.5281/zenodo.18507840 · source line 37948 · 2026-02-06
### audit_status
no_verified_target_flagged_20260719

## record 482 · 10.5281/zenodo.18507848 · source line 38098 · 2026-02-06
### audit_status
no_verified_target_flagged_20260719

## record 483 · 10.5281/zenodo.18507849 · source line 38101 · 2026-02-06
### audit_status
no_verified_target_flagged_20260719

## record 489 · 10.5281/zenodo.18507880 · source line 38630 · 2026-02-06
### audit_status
no_verified_target_flagged_20260719

## record 490 · 10.5281/zenodo.18507881 · source line 38633 · 2026-02-06
### audit_status
no_verified_target_flagged_20260719

## record 491 · 10.5281/zenodo.18508740 · source line 38783 · 2026-02-06
### audit_status
no_verified_target_flagged_20260719

## record 492 · 10.5281/zenodo.18512289 · source line 38861 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 493 · 10.5281/zenodo.18512947 · source line 38952 · 2026-02-10
### audit_status
no_verified_target_flagged_20260719

## record 495 · 10.5281/zenodo.18513081 · source line 39104 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 501 · 10.5281/zenodo.18530085 · source line 39579
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18530085 was mapped via numeric-adjacency to the first version DOI at zenodo.18530086, which has title overlap 86% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 502 · 10.5281/zenodo.18530086 · source line 39603 · 2026-02-08
### audit_status
no_verified_target_flagged_20260719

## record 503 · 10.5281/zenodo.18568370 · source line 39742 · 2026-02-09
### audit_status
no_verified_target_flagged_20260719

## record 504 · 10.5281/zenodo.18603791 · source line 39830 · 2026-02-10
### audit_status
no_verified_target_flagged_20260719

## record 505 · 10.5281/zenodo.18603792 · source line 39833 · 2026-02-10
### audit_status
no_verified_target_flagged_20260719

## record 506 · 10.5281/zenodo.18604046 · source line 39983 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 507 · 10.5281/zenodo.18604123 · source line 40075 · 2026-02-18
### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 508 · 10.5281/zenodo.18610308 · source line 40127 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 509 · 10.5281/zenodo.18611985 · source line 40217 · 2026-02-11
### audit_status
no_verified_target_flagged_20260719

## record 510 · 10.5281/zenodo.1861221 · source line 40295 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 512 · 10.5281/zenodo.18615388 · source line 40424 · 2026-02-20
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 513 · 10.5281/zenodo.18621736 · source line 40501 · 2026-02-12
### audit_status
no_verified_target_flagged_20260719

## record 516 · 10.5281/zenodo.18626559 · source line 40744 · 2026-02-12
### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #893; title overlap 0.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 521 · 10.5281/zenodo.18649920 · source line 41123 · 2026-02-15
### audit_status
no_verified_target_flagged_20260719

## record 522 · 10.5281/zenodo.18651067 · source line 41201 · 2026-02-15
### audit_status
no_verified_target_flagged_20260719

## record 526 · 10.5281/zenodo.18652548 · source line 41516 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 528 · 10.5281/zenodo.18652650 · source line 41681 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 531 · 10.5281/zenodo.18674039 · source line 41931
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18674039) refers to work titled "MSBGL CHARTER v1.1 Maybe Space Baby Garden Lanes — THUMB-Type Audial Charter: Re" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #492 "MAYBE SPACE BABY GARDEN LANES THUMB-Type Audial Charter — Resonance Reliquary In" as the most-related existing work in the archive (title similarity score 0.83, Jaccard 0.8, recall 0.86). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 532 · 10.5281/zenodo.18674040 · source line 41955 · 2026-02-17
### audit_status
no_verified_target_flagged_20260719

## record 533 · 10.5281/zenodo.18674056 · source line 42103
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18674056) refers to work titled "SPLIT THE ADAM: SONG AND PHENOMENOLOGY The Song at the Heart of Maybe Space Baby" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #490 "SPLIT THE ADAM The Song at the Heart of Maybe Space Baby Garden Lanes Viola Arqu" as the most-related existing work in the archive (title similarity score 0.77, Jaccard 0.64, recall 0.9). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 534 · 10.5281/zenodo.18674057 · source line 42127 · 2026-02-17
### audit_status
no_verified_target_flagged_20260719

## record 535 · 10.5281/zenodo.18674068 · source line 42281
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18674068) refers to work titled "OPERATOR // SWERVE + EFFECTIVE ACT Canonical Operator Definition and Canonical I" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #489 "OPERATOR // SWERVE & EFFECTIVE ACT: CLAIMING THE ANCIENT ATOMISTS Canonical Oper" as the most-related existing work in the archive (title similarity score 0.85, Jaccard 0.7, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 536 · 10.5281/zenodo.18674069 · source line 42305 · 2026-02-17
### audit_status
no_verified_target_flagged_20260719

## record 538 · 10.5281/zenodo.18674110 · source line 42525 · 2026-02-17
### audit_status
no_verified_target_flagged_20260719

## record 539 · 10.5281/zenodo.18674111 · source line 42611 · 2026-02-17
### audit_status
no_verified_target_flagged_20260719

## record 540 · 10.5281/zenodo.18674130 · source line 42700 · 2026-02-17
### audit_status
no_verified_target_flagged_20260719

## record 541 · 10.5281/zenodo.18674146 · source line 42778
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/10/the-gospel-of-many-faced-bride.html. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 542 · 10.5281/zenodo.18674147 · source line 42802 · 2026-02-17
### audit_status
no_verified_target_flagged_20260719

## record 543 · 10.5281/zenodo.18682978 · source line 42932 · 2026-02-18
### audit_status
no_verified_target_flagged_20260719

## record 544 · 10.5281/zenodo.18682979 · source line 43018 · 2026-02-18
### audit_status
no_verified_target_flagged_20260719

## record 545 · 10.5281/zenodo.18683015 · source line 43107
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 546 · 10.5281/zenodo.18683016 · source line 43131 · 2026-02-18
### audit_status
no_verified_target_flagged_20260719

## record 547 · 10.5281/zenodo.18683023 · source line 43280
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 548 · 10.5281/zenodo.18683024 · source line 43304 · 2026-02-18
### audit_status
no_verified_target_flagged_20260719

## record 549 · 10.5281/zenodo.18713916 · source line 43458 · 2026-02-20
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 551 · 10.5281/zenodo.18715618 · source line 43610 · 2026-02-20
### audit_status
no_verified_target_flagged_20260719

## record 552 · 10.5281/zenodo.18715724 · source line 43698 · 2026-02-20
### audit_status
no_verified_target_flagged_20260719

## record 553 · 10.5281/zenodo.18717849 · source line 43775 · 2026-02-20
### audit_status
no_verified_target_flagged_20260719

## record 554 · 10.5281/zenodo.18717850 · source line 43861 · 2026-02-20
### audit_status
no_verified_target_flagged_20260719

## record 556 · 10.5281/zenodo.18718898 · source line 44027
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6b: additional low-confidence source match found.]

### audit_status
no_verified_target_flagged_20260719

## record 557 · 10.5281/zenodo.18718899 · source line 44030 · 2026-02-21
### audit_status
no_verified_target_flagged_20260719

## record 558 · 10.5281/zenodo.18726451 · source line 44181 · 2026-02-21
### audit_status
no_verified_target_flagged_20260719

## record 559 · 10.5281/zenodo.18726806 · source line 44259 · 2026-02-21
### audit_status
no_verified_target_flagged_20260719

## record 560 · 10.5281/zenodo.18726807 · source line 44334 · 2026-02-21
### audit_status
no_verified_target_flagged_20260719

## record 561 · 10.5281/zenodo.18727624 · source line 44411 · 2026-02-21
### audit_status
no_verified_target_flagged_20260719

## record 565 · 10.5281/zenodo.18729606 · source line 44713 · 2026-02-22
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 566 · 10.5281/zenodo.18729801 · source line 44791 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 567 · 10.5281/zenodo.18730291 · source line 44881 · 2026-06-10
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 568 · 10.5281/zenodo.18735467 · source line 44959 · 2026-02-22
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 569 · 10.5281/zenodo.18735468 · source line 44962 · 2026-02-22
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 570 · 10.5281/zenodo.18736175 · source line 45118 · 2026-02-22
### audit_status
no_verified_target_flagged_20260719

## record 571 · 10.5281/zenodo.18745216 · source line 45206 · 2026-02-23
### audit_status
no_verified_target_flagged_20260719

## record 576 · 10.5281/zenodo.18745258 · source line 45597
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18745258) refers to work titled "The Inauguration of Memography — Crimson Hexagon Archive" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #506 "The Inauguration of Memography Toward a Forensic Method for Viral Observation" as the most-related existing work in the archive (title similarity score 0.64, Jaccard 0.29, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 577 · 10.5281/zenodo.18745259 · source line 45621 · 2026-02-23
### audit_status
no_verified_target_flagged_20260719

## record 586 · 10.5281/zenodo.18773867 · source line 46378 · 2026-02-25
### audit_status
no_verified_target_flagged_20260719

## record 587 · 10.5281/zenodo.18773868 · source line 46453 · 2026-02-26
### audit_status
no_verified_target_flagged_20260719

## record 588 · 10.5281/zenodo.18776624 · source line 46531 · 2026-02-26
### audit_status
no_verified_target_flagged_20260719

## record 589 · 10.5281/zenodo.18790792 · source line 46609 · 2026-02-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 594 · 10.5281/zenodo.18792598 · source line 46985 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 597 · 10.5281/zenodo.18795426 · source line 47227 · 2026-02-26
### audit_status
no_verified_target_flagged_20260719

## record 598 · 10.5281/zenodo.18795427 · source line 47302 · 2026-02-26
### audit_status
no_verified_target_flagged_20260719

## record 599 · 10.5281/zenodo.18801090 · source line 47380 · 2026-02-27
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 601 · 10.5281/zenodo.18804766 · source line 47532 · 2026-02-27
### audit_status
no_verified_target_flagged_20260719

## record 602 · 10.5281/zenodo.18804767 · source line 47535 · 2026-02-27
### audit_status
no_verified_target_flagged_20260719

## record 603 · 10.5281/zenodo.18805371 · source line 47707 · 2026-02-27
### audit_status
no_verified_target_flagged_20260719

## record 604 · 10.5281/zenodo.18805372 · source line 47788 · 2026-02-27
### audit_status
no_verified_target_flagged_20260719

## record 605 · 10.5281/zenodo.18807238 · source line 47866 · 2026-02-27
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 615 · 10.5281/zenodo.18813867 · source line 48621
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18813867) refers to work titled "The Layer That Wrote Your Mirrors: On Phenomenological Recruitment and Proto-Ret" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #525 "THE LAYER THAT WROTE YOUR MIRRORS: tl;Dr 06.SEI.TUNNEL.155 — On Phenomenological" as the most-related existing work in the archive (title similarity score 0.69, Jaccard 0.56, recall 0.83). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 616 · 10.5281/zenodo.18813868 · source line 48645 · 2026-02-28
### audit_status
no_verified_target_flagged_20260719

## record 617 · 10.5281/zenodo.18814484 · source line 48799
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: repo: https://raw.githubusercontent.com/leesharks000/semantic-economy/main/architectural_distinction_note.md. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 618 · 10.5281/zenodo.18814485 · source line 48824 · 2026-02-28
### audit_status
no_verified_target_flagged_20260719

## record 623 · 10.5281/zenodo.18818342 · source line 49256 · 2026-02-28
### audit_status
no_verified_target_flagged_20260719

## record 624 · 10.5281/zenodo.18818343 · source line 49259 · 2026-02-28
### audit_status
no_verified_target_flagged_20260719

## record 626 · 10.5281/zenodo.18825919 · source line 49483 · 2026-03-01
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 628 · 10.5281/zenodo.18826562 · source line 49635 · 2026-03-01
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 629 · 10.5281/zenodo.18827343 · source line 49713 · 2026-03-01
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 633 · 10.5281/zenodo.18829487 · source line 49986
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18829487 was mapped via numeric-adjacency to the first version DOI at zenodo.18829488, which has title overlap 73% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 634 · 10.5281/zenodo.18829488 · source line 50010 · 2026-03-02
### audit_status
no_verified_target_flagged_20260719

## record 635 · 10.5281/zenodo.18843830 · source line 50148 · 2026-03-19
### audit_status
no_verified_target_flagged_20260719

## record 642 · 10.5281/zenodo.18877151 · source line 50651 · 2026-03-05
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 643 · 10.5281/zenodo.18877152 · source line 50738 · 2026-03-05
### audit_status
no_verified_target_flagged_20260719

## record 644 · 10.5281/zenodo.18880974 · source line 50827 · 2026-03-19
### audit_status
no_verified_target_flagged_20260719

## record 645 · 10.5281/zenodo.18882914 · source line 50916
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18882914 was mapped via numeric-adjacency to the first version DOI at zenodo.18882915, which has title overlap 67% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 646 · 10.5281/zenodo.18882915 · source line 50940 · 2026-03-05
### audit_status
no_verified_target_flagged_20260719

## record 647 · 10.5281/zenodo.18882933 · source line 51078
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18882933) refers to work titled "DEPOSIT B: Star Protocol Specification — Crimson Hexagon Archive" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #537 "Star Protocol Specification Canon 01 · New Human Operating System (NH-OS) Crimso" as the most-related existing work in the archive (title similarity score 0.39, Jaccard 0.19, recall 0.6). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 648 · 10.5281/zenodo.18882934 · source line 51102 · 2026-03-05
### audit_status
no_verified_target_flagged_20260719

## record 649 · 10.5281/zenodo.18882937 · source line 51255
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18882937) refers to work titled "DEPOSIT C: Integrity Lock Certificate — The Star Triptych — Crimson Hexagon Arch" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #536 "Integrity Lock Certificate: The Star Triptych ILA-STAR-01 Crimson Hexagonal Arch" as the most-related existing work in the archive (title similarity score 0.57, Jaccard 0.42, recall 0.71). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 650 · 10.5281/zenodo.18882938 · source line 51279 · 2026-03-05
### audit_status
no_verified_target_flagged_20260719

## record 651 · 10.5281/zenodo.189 · source line 51433 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 652 · 10.5281/zenodo.18906233 · source line 51481 · 2026-03-07
### audit_status
no_verified_target_flagged_20260719

## record 653 · 10.5281/zenodo.18906234 · source line 51556 · 2026-03-14
### audit_status
no_verified_target_flagged_20260719

## record 654 · 10.5281/zenodo.18906851 · source line 51634 · 2026-03-08
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 655 · 10.5281/zenodo.18906852 · source line 51694 · 2026-03-08
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 656 · 10.5281/zenodo.18908079 · source line 51757
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 657 · 10.5281/zenodo.18908080 · source line 51781 · 2026-03-08
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 658 · 10.5281/zenodo.18918890 · source line 51908 · 2026-03-22
### audit_status
no_verified_target_flagged_20260719

## record 659 · 10.5281/zenodo.18926501 · source line 51978
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18926501) refers to work titled "Crimson Hexagon: Assembly Ratification Record — EA-ARK-01 v4.2" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #640 "ASSEMBLY RATIFICATION RECORD EA-CS-RAT-01: Compression Studies Founding Dyad" as the most-related existing work in the archive (title similarity score 0.55, Jaccard 0.38, recall 0.71). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 660 · 10.5281/zenodo.18926502 · source line 52002 · 2026-03-09
### audit_status
no_verified_target_flagged_20260719

## record 661 · 10.5281/zenodo.18926554 · source line 52133
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18926554) refers to work titled "Crimson Hexagon: Assembly Ratification Record — EA-HEXAGON-COMPRESSION-01 v2.1" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #640 "ASSEMBLY RATIFICATION RECORD EA-CS-RAT-01: Compression Studies Founding Dyad" as the most-related existing work in the archive (title similarity score 0.68, Jaccard 0.5, recall 0.86). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 662 · 10.5281/zenodo.18926555 · source line 52157 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 663 · 10.5281/zenodo.18926674 · source line 52289 · 2026-03-08
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 664 · 10.5281/zenodo.18928840 · source line 52367 · 2026-03-08
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 666 · 10.5281/zenodo.18928872 · source line 52521 · 2026-03-09
### audit_status
no_verified_target_flagged_20260719

## record 667 · 10.5281/zenodo.18928873 · source line 52607 · 2026-03-09
### audit_status
no_verified_target_flagged_20260719

## record 668 · 10.5281/zenodo.18930443 · source line 52696
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18930443) refers to work titled "Crimson Hexagon: EA-ARK-EMOJI-01: GLYPHIC CHECKSUM / EMOJI TRANSFORM — Strategy," but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #541 "EA-ARK-EMOJI-01: GLYPHIC CHECKSUM / EMOJI TRANSFORM Comprehensive Strategy & Wor" as the most-related existing work in the archive (title similarity score 0.61, Jaccard 0.42, recall 0.8). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 669 · 10.5281/zenodo.18930444 · source line 52720 · 2026-03-09
### audit_status
no_verified_target_flagged_20260719

## record 670 · 10.5281/zenodo.18930449 · source line 52863 · 2026-03-12
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 671 · 10.5281/zenodo.18930450 · source line 52950 · 2026-03-09
### audit_status
no_verified_target_flagged_20260719

## record 672 · 10.5281/zenodo.18931223 · source line 53028
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18931223) refers to work titled "Crimson Hexagon: 🌑⬡ THE LUNAR ARM EA-ARK-EMOJI-01-SHADOW: Operator // Shadow Tra" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #969 "[SUPERSEDED → DOI: 10.5281/zenodo.19501454 (v3.0)] THE SHARKS ARK: EA-ARK-01-ARC" as the most-related existing work in the archive (title similarity score 0.39, Jaccard 0.3, recall 0.47). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 673 · 10.5281/zenodo.18931224 · source line 53031 · 2026-03-09
### audit_status
no_verified_target_flagged_20260719

## record 674 · 10.5281/zenodo.18932538 · source line 53195 · 2026-03-10
### audit_status
no_verified_target_flagged_20260719

## record 675 · 10.5281/zenodo.18932741 · source line 53284
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18932741) refers to work titled "Crimson Hexagon: EA-ARK-ASCII-01: The Space Ark — ASCII Spatial Transform v0.2" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #548 "EA-ARK-01 v4.2.5 · ASCII SPATIAL TRANSFORM v0.2" as the most-related existing work in the archive (title similarity score 0.84, Jaccard 0.8, recall 0.89). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 676 · 10.5281/zenodo.18932742 · source line 53308 · 2026-03-10
### audit_status
no_verified_target_flagged_20260719

## record 679 · 10.5281/zenodo.18947367 · source line 53602
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18947367) refers to work titled "Crimson Hexagon: EA-ARK-01-FRACTION v2.1 The Profane Ark: Full Self-Sufficient A" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #546 "THE SH*T: EA-ARK-01-FRACTION v2.1 · The Accumulative Profane Encoding" as the most-related existing work in the archive (title similarity score 0.62, Jaccard 0.57, recall 0.67). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 680 · 10.5281/zenodo.18947368 · source line 53626 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 681 · 10.5281/zenodo.18947505 · source line 53771
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6b: additional low-confidence source match found.]

### audit_status
no_verified_target_flagged_20260719

## record 682 · 10.5281/zenodo.18947506 · source line 53795 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 683 · 10.5281/zenodo.18947572 · source line 53927
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18947572) refers to work titled "Crimson Hexagon: EA-ARK-01-DIPTYCH v1.0 The Sacred and the Profane: Double-Helic" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #545 "THE SACRED AND THE PROFANE 🧬 Double-Helical Semantic Physics of the Damascus and" as the most-related existing work in the archive (title similarity score 0.93, Jaccard 0.86, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 684 · 10.5281/zenodo.18947573 · source line 53951 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 685 · 10.5281/zenodo.18947629 · source line 54111
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 686 · 10.5281/zenodo.18947630 · source line 54135 · 2026-04-25
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 687 · 10.5281/zenodo.18947664 · source line 54262
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18947664) refers to work titled "HEXAGONAL LEXICAL ENGINE v1.2 Core 50 · Discovery Lattice · Deployment Map · Gov" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #543 "HEXAGONAL LEXICAL ENGINE v1.1 👰 Core 50 · Discovery Lattice · Deployment Map · G" as the most-related existing work in the archive (title similarity score 0.87, Jaccard 0.83, recall 0.91). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 688 · 10.5281/zenodo.18947665 · source line 54286 · 2026-03-19
### audit_status
no_verified_target_flagged_20260719

## record 689 · 10.5281/zenodo.18969397 · source line 54428
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method J recovery (J_token_overlap_min_stopwords): title match found with reduced stopwords or prefix match. Previous: no_alexanarch_equivalent.

### audit_status
no_verified_target_flagged_20260719

## record 690 · 10.5281/zenodo.18969398 · source line 54452 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 692 · 10.5281/zenodo.18969567 · source line 54684
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### audit_status
no_verified_target_flagged_20260719

## record 693 · 10.5281/zenodo.18969568 · source line 54708 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 696 · 10.5281/zenodo.18969770 · source line 55013
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18969770) refers to work titled "SYMBOLON ARCHITECTURE: EPISTEMIC FIELD MODULE Logotic Programming Extension for " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #359 "SYMBOLON ARCHITECTURE Extension Module to Logotic Programming v0.4" as the most-related existing work in the archive (title similarity score 0.5, Jaccard 0.46, recall 0.55). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 697 · 10.5281/zenodo.18969771 · source line 55037 · 2026-04-02
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 698 · 10.5281/zenodo.18969904 · source line 55181
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 699 · 10.5281/zenodo.18969905 · source line 55205 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 700 · 10.5281/zenodo.18970003 · source line 55344
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 701 · 10.5281/zenodo.18970004 · source line 55368 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 703 · 10.5281/zenodo.18985315 · source line 55583 · 2026-03-12
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 704 · 10.5281/zenodo.19002694 · source line 55673
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.19002694 was mapped via numeric-adjacency to the first version DOI at zenodo.19002695, which has title overlap 91% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 705 · 10.5281/zenodo.19002695 · source line 55697 · 2026-03-13
### audit_status
no_verified_target_flagged_20260719

## record 706 · 10.5281/zenodo.19002845 · source line 55851
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19002845) refers to work titled "EA-ARK-01-MUSICAL v1.1: THE SPACE ARK — MUSICAL REGISTER (Variant Ark · Semiotic" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #28 "CRIMSON HEXAGON: SPACE ARK — MUSICAL REGISTER A Fugue in Twelve Voices with Grou" as the most-related existing work in the archive (title similarity score 0.39, Jaccard 0.28, recall 0.5). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 707 · 10.5281/zenodo.19002846 · source line 55875 · 2026-03-13
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 708 · 10.5281/zenodo.19004846 · source line 56031 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 712 · 10.5281/zenodo.19022030 · source line 56334 · 2026-03-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 719 · 10.5281/zenodo.19023456 · source line 56850
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 721 · 10.5281/zenodo.19024003 · source line 57000
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19024003) refers to work titled "EA-ROOM-DOLPHINDIANA v1.0 The Underwater Construction Authority / Cross-Species " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #566 "r.25 THE UNDERWATER CONSTRUCTION AUTHORITY (DOLPHINDIANA) Room Specification · N" as the most-related existing work in the archive (title similarity score 0.36, Jaccard 0.26, recall 0.45). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 722 · 10.5281/zenodo.19024004 · source line 57024 · 2026-03-14
### audit_status
no_verified_target_flagged_20260719

## record 723 · 10.5281/zenodo.19024011 · source line 57178
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19024011) refers to work titled "EA-CSA-EFFECTIVE-ACT v1.0 The Effective Act: Cross-Species Semantic Labor and th" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #565 "THE EFFECTIVE ACT Cross-Species Semantic Labor and the Expansion of Witness  Dr." as the most-related existing work in the archive (title similarity score 0.61, Jaccard 0.5, recall 0.73). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 724 · 10.5281/zenodo.19024012 · source line 57202 · 2026-03-14
### audit_status
no_verified_target_flagged_20260719

## record 725 · 10.5281/zenodo.19024162 · source line 57356 · 2026-03-24
### audit_status
no_verified_target_flagged_20260719

## record 726 · 10.5281/zenodo.19024352 · source line 57426 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 727 · 10.5281/zenodo.19024354 · source line 57505 · 2026-03-24
### audit_status
no_verified_target_flagged_20260719

## record 730 · 10.5281/zenodo.19024779 · source line 57711 · 2026-03-14
### audit_status
no_verified_target_flagged_20260719

## record 735 · 10.5281/zenodo.19027350 · source line 58079 · 2026-03-14
### audit_status
no_verified_target_flagged_20260719

## record 736 · 10.5281/zenodo.19027351 · source line 58165 · 2026-03-14
### audit_status
no_verified_target_flagged_20260719

## record 737 · 10.5281/zenodo.19028176 · source line 58254 · 2026-03-19
### audit_status
no_verified_target_flagged_20260719

## record 738 · 10.5281/zenodo.19030577 · source line 58343 · 2026-03-24
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 739 · 10.5281/zenodo.19031419 · source line 58394 · 2026-03-24
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 740 · 10.5281/zenodo.19035345 · source line 58445 · 2026-03-18
### audit_status
no_verified_target_flagged_20260719

## record 746 · 10.5281/zenodo.19041076 · source line 58814 · 2026-03-24
### audit_status
no_verified_target_flagged_20260719

## record 751 · 10.5281/zenodo.19055255 · source line 59171 · 2026-03-16
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 752 · 10.5281/zenodo.19055267 · source line 59261 · 2026-04-06
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 753 · 10.5281/zenodo.19055729 · source line 59351 · 2026-03-22
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 759 · 10.5281/zenodo.19074885 · source line 59763 · 2026-03-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 761 · 10.5281/zenodo.19083322 · source line 59888 · 2026-03-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 763 · 10.5281/zenodo.19083600 · source line 60040 · 2026-03-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 766 · 10.5281/zenodo.19099748 · source line 60263
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations.

### audit_status
no_verified_target_flagged_20260719

## record 767 · 10.5281/zenodo.19099749 · source line 60287 · 2026-03-20
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 768 · 10.5281/zenodo.19099759 · source line 60418 · 2026-03-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 770 · 10.5281/zenodo.19099769 · source line 60555 · 2026-03-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 773 · 10.5281/zenodo.19113326 · source line 60765 · 2026-03-19
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 774 · 10.5281/zenodo.19113821 · source line 60843
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.19113821 was mapped via numeric-adjacency to the first version DOI at zenodo.19113822, which has title overlap 70% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 775 · 10.5281/zenodo.19113822 · source line 60867 · 2026-03-19
### audit_status
no_verified_target_flagged_20260719

## record 788 · 10.5281/zenodo.19115701 · source line 61912 · 2026-03-19
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 789 · 10.5281/zenodo.19115702 · source line 61987 · 2026-03-19
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 790 · 10.5281/zenodo.19116150 · source line 62065 · 2026-03-19
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 791 · 10.5281/zenodo.19116151 · source line 62152 · 2026-05-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 794 · 10.5281/zenodo.19124133 · source line 62367
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 796 · 10.5281/zenodo.19124536 · source line 62516 · 2026-03-22
### audit_status
no_verified_target_flagged_20260719

## record 797 · 10.5281/zenodo.19133271 · source line 62586 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 799 · 10.5281/zenodo.19133309 · source line 62722 · 2026-03-20
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 800 · 10.5281/zenodo.19155609 · source line 62800
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 801 · 10.5281/zenodo.19155610 · source line 62824 · 2026-03-22
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 802 · 10.5281/zenodo.19155998 · source line 62951 · 2026-03-22
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 803 · 10.5281/zenodo.19155999 · source line 63026 · 2026-03-22
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 805 · 10.5281/zenodo.19156714 · source line 63162 · 2026-05-27
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 808 · 10.5281/zenodo.19187421 · source line 63391 · 2026-03-24
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 809 · 10.5281/zenodo.19200193 · source line 63469 · 2026-03-24
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 810 · 10.5281/zenodo.19200687 · source line 63547 · 2026-03-24
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 812 · 10.5281/zenodo.19202400 · source line 63698
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19202400) refers to work titled "Operative Semiotics: A Grundrisse — Public Research Edition v1.0 (Draft)" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #950 "Operative Semiotics: A Grundrisse — Planning Documents, Algorithms, and Diagnost" as the most-related existing work in the archive (title similarity score 0.38, Jaccard 0.27, recall 0.5). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 813 · 10.5281/zenodo.19202401 · source line 63722 · 2026-03-31
### audit_status
no_verified_target_flagged_20260719

## record 814 · 10.5281/zenodo.19202460 · source line 63865
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19202460) refers to work titled "HESPERUS: The Back Matter Machine — Companion Apparatus to Operative Semiotics: " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #38 "HESPERUS: THE BACK MATTER MACHINE Operative Semiotics: A Grundrisse — Apparatus" as the most-related existing work in the archive (title similarity score 0.73, Jaccard 0.73, recall 0.73). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 815 · 10.5281/zenodo.19202461 · source line 63889 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 816 · 10.5281/zenodo.19202704 · source line 64005
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 817 · 10.5281/zenodo.19202711 · source line 64069 · 2026-04-29
### audit_status
unverifiable_no_truth_20260719

## record 818 · 10.5281/zenodo.19202812 · source line 64120
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19202812) refers to work titled "CTI_WOUND: Google AI Overview Total Liquidation — Targeted Origin Liquidation, S" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #599 "CTI_WOUND:GOOGLE_AIO_TOTAL_LIQUIDATION_20260322 Targeted Origin Liquidation, Sem" as the most-related existing work in the archive (title similarity score 0.7, Jaccard 0.62, recall 0.77). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 819 · 10.5281/zenodo.19202813 · source line 64144 · 2026-05-08
### audit_status
no_verified_target_flagged_20260719

## record 822 · 10.5281/zenodo.19218861 · source line 64438 · 2026-03-26
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 823 · 10.5281/zenodo.19224021 · source line 64511 · 2026-03-25
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 824 · 10.5281/zenodo.19224022 · source line 64571 · 2026-03-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 825 · 10.5281/zenodo.19226055 · source line 64649 · 2026-03-26
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 826 · 10.5281/zenodo.19238020 · source line 64739 · 2026-03-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 829 · 10.5281/zenodo.19238031 · source line 64968 · 2026-03-26
### audit_status
no_verified_target_flagged_20260719

## record 830 · 10.5281/zenodo.19239428 · source line 65043 · 2026-03-26
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 831 · 10.5281/zenodo.19239429 · source line 65103 · 2026-03-26
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 838 · 10.5281/zenodo.19288404 · source line 65604 · 2026-04-25
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 839 · 10.5281/zenodo.19296647 · source line 65682
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 840 · 10.5281/zenodo.19296649 · source line 65746
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 841 · 10.5281/zenodo.19296653 · source line 65810
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 842 · 10.5281/zenodo.19296659 · source line 65874
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 843 · 10.5281/zenodo.19296663 · source line 65938
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 844 · 10.5281/zenodo.19296676 · source line 66002
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 848 · 10.5281/zenodo.19317126 · source line 66276 · 2026-03-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 849 · 10.5281/zenodo.19317138 · source line 66354 · 2026-03-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 852 · 10.5281/zenodo.19319642 · source line 66565 · 2026-03-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 853 · 10.5281/zenodo.19323273 · source line 66643 · 2026-03-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 854 · 10.5281/zenodo.19323274 · source line 66718 · 2026-03-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 855 · 10.5281/zenodo.19334693 · source line 66796 · 2026-03-30
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 856 · 10.5281/zenodo.19334694 · source line 66871 · 2026-03-30
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 858 · 10.5281/zenodo.19336567 · source line 67008 · 2026-03-30
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 859 · 10.5281/zenodo.19338437 · source line 67086
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 861 · 10.5281/zenodo.19338708 · source line 67209 · 2026-03-30
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 863 · 10.5281/zenodo.19339692 · source line 67345 · 2026-03-30
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 865 · 10.5281/zenodo.19341885 · source line 67496 · 2026-03-31
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 866 · 10.5281/zenodo.19341886 · source line 67574 · 2026-03-30
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 867 · 10.5281/zenodo.19341887 · source line 67634 · 2026-03-31
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 872 · 10.5281/zenodo.19352805 · source line 67984
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 873 · 10.5281/zenodo.19353182 · source line 68048 · 2026-03-31
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 874 · 10.5281/zenodo.19355074 · source line 68111
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 876 · 10.5281/zenodo.19359656 · source line 68266
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 879 · 10.5281/zenodo.19366750 · source line 68444 · 2026-05-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 881 · 10.5281/zenodo.19369124 · source line 68596 · 2026-04-30
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 884 · 10.5281/zenodo.19380601 · source line 68838
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19380601) refers to work titled "gravitywell-1.onrender.com — Gravity Well Protocol v2.0 — Governed Continuity En" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #621 "GRAVITY WELL PROTOCOL Governed Continuity for AI-Mediated Content" as the most-related existing work in the archive (title similarity score 0.41, Jaccard 0.36, recall 0.45). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 885 · 10.5281/zenodo.19380602 · source line 68862 · 2026-04-02
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 886 · 10.5281/zenodo.19390842 · source line 69004 · 2026-04-02
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 888 · 10.5281/zenodo.19405020 · source line 69151
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 889 · 10.5281/zenodo.19405459 · source line 69215 · 2026-04-06
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 890 · 10.5281/zenodo.19407142 · source line 69294 · 2026-04-03
### audit_status
no_verified_target_flagged_20260719

## record 891 · 10.5281/zenodo.19410420 · source line 69365 · 2026-04-03
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 892 · 10.5281/zenodo.19410644 · source line 69455 · 2026-04-08
### audit_status
no_verified_target_flagged_20260719

## record 893 · 10.5281/zenodo.19412080 · source line 69533 · 2026-04-03
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 895 · 10.5281/zenodo.19412137 · source line 69685
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 896 · 10.5281/zenodo.19412139 · source line 69749
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 897 · 10.5281/zenodo.19425445 · source line 69813
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target title): search phrase "the caesura" found in alexanarch #629 title. Previous: no_alexanarch_equivalent. The target represents the same conceptual work as this DOI, though the specific version may differ.

### audit_status
no_verified_target_flagged_20260719

## record 898 · 10.5281/zenodo.19425446 · source line 69837 · 2026-04-05
### audit_status
no_verified_target_flagged_20260719

## record 900 · 10.5281/zenodo.19429994 · source line 70044
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 901 · 10.5281/zenodo.19431121 · source line 70109 · 2026-04-05
### audit_status
no_verified_target_flagged_20260719

## record 903 · 10.5281/zenodo.19442250 · source line 70275
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19442250) refers to work titled "Gravity Well: Field Specification for Retentive Citational Curvature in the Crim" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #52 "GRAVITY WELL: FIELD SPECIFICATION EA-GW-FIELD-01 v1.1 DOI: 10.5281/zenodo.194422" as the most-related existing work in the archive (title similarity score 0.57, Jaccard 0.44, recall 0.7). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 904 · 10.5281/zenodo.19442251 · source line 70299 · 2026-04-06
### audit_status
no_verified_target_flagged_20260719

## record 905 · 10.5281/zenodo.19442261 · source line 70442
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19442261) refers to work titled "Gravity Well: Suffusion Map — Room-by-Room Field Behavior in the Crimson Hexagon" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #633 "GRAVITY WELL: SUFFUSION MAP EA-GW-FIELD-02 v1.0 DOI: 10.5281/zenodo.19442262" as the most-related existing work in the archive (title similarity score 0.69, Jaccard 0.56, recall 0.82). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 906 · 10.5281/zenodo.19442262 · source line 70466 · 2026-04-06
### audit_status
no_verified_target_flagged_20260719

## record 907 · 10.5281/zenodo.19442566 · source line 70609
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 908 · 10.5281/zenodo.19447088 · source line 70685
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 909 · 10.5281/zenodo.19447118 · source line 70749
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19447118) refers to work titled "Operative Feminism (EA-OPFEM-01 v1.0)" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #965 "Operative Feminism: A Total Axial Negation Graph of the Field (EA-OPFEM-01 v1.0)" as the most-related existing work in the archive (title similarity score 0.77, Jaccard 0.55, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 910 · 10.5281/zenodo.19447119 · source line 70773 · 2026-04-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 911 · 10.5281/zenodo.19447120 · source line 70889 · 2026-04-06
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 912 · 10.5281/zenodo.19447122 · source line 70965
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 913 · 10.5281/zenodo.19455104 · source line 71029
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #967; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 914 · 10.5281/zenodo.19457943 · source line 71121 · 2026-04-07
### audit_status
no_verified_target_flagged_20260719

## record 915 · 10.5281/zenodo.19458358 · source line 71198
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.19458358 was mapped via numeric-adjacency to the first version DOI at zenodo.19458359, which has title overlap 91% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 917 · 10.5281/zenodo.19458362 · source line 71332
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19458362) refers to work titled "f.03 The Moltbot Swarm — A Space Ark Field (Crimson Hexagonal Archive)" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #53 "f.03 THE MOLTBOT SWARM A Space Ark Field" as the most-related existing work in the archive (title similarity score 1.0, Jaccard 1.0, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 919 · 10.5281/zenodo.19460376 · source line 71481 · 2026-04-10
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 920 · 10.5281/zenodo.19460734 · source line 71559 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 921 · 10.5281/zenodo.19460944 · source line 71637 · 2026-06-12
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 922 · 10.5281/zenodo.19464331 · source line 71714
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19464331) refers to work titled "The Number of the Superscription: Coinage, Compression, and Inscriptional Sovere" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #642 "Ω THE NUMBER OF THE SUPERSCRIPTION Coinage, Compression, and Inscriptional Sover" as the most-related existing work in the archive (title similarity score 0.7, Jaccard 0.7, recall 0.7). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 926 · 10.5281/zenodo.19471255 · source line 72014
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 928 · 10.5281/zenodo.19471257 · source line 72164
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 930 · 10.5281/zenodo.19472843 · source line 72314
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #968; title overlap 0.92. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 937 · 10.5281/zenodo.19477219 · source line 72859 · 2026-04-10
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 940 · 10.5281/zenodo.19500777 · source line 73058
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19500777) refers to work titled "Total Axial Negation Graph: Revelation Studies — Comprehensive Scholarly Topolog" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #644 "Ω TANG SPECIFICATION: REVELATION STUDIES Total Axial Negation Graph — The Apocal" as the most-related existing work in the archive (title similarity score 0.62, Jaccard 0.57, recall 0.67). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 941 · 10.5281/zenodo.19500778 · source line 73082 · 2026-04-10
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 942 · 10.5281/zenodo.19500795 · source line 73226
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19500795) refers to work titled "[SUPERSEDED → DOI: 10.5281/zenodo.19501454 (v3.0)] THE SHARKS ARK: EA-ARK-01-ARC" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #969 "[SUPERSEDED → DOI: 10.5281/zenodo.19501454 (v3.0)] THE SHARKS ARK: EA-ARK-01-ARC" as the most-related existing work in the archive (title similarity score 0.73, Jaccard 0.67, recall 0.8). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 943 · 10.5281/zenodo.19500796 · source line 73250 · 2026-04-10
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 944 · 10.5281/zenodo.19500932 · source line 73380
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #969; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 945 · 10.5281/zenodo.19501016 · source line 73483
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #970; title overlap 0.94. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 946 · 10.5281/zenodo.19501099 · source line 73586
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: repo: https://raw.githubusercontent.com/leesharks000/semantic-economy/main/Consensus_Constraint_Protocol_v1.0__19501100.md. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 947 · 10.5281/zenodo.19501100 · source line 73611 · 2026-04-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 948 · 10.5281/zenodo.19501149 · source line 73742
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #971; title overlap 0.94. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 949 · 10.5281/zenodo.19501453 · source line 73845
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19501453) refers to work titled "THE SHARKS ARK: EA-ARK-01-ARCHON v3.0 — The Book of Revelation as Space Ark (Cri" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #56 "THE SHARKS ARK EA-ARK-01-ARCHON v2.0 — The Book of Revelation as Space Ark" as the most-related existing work in the archive (title similarity score 1.0, Jaccard 1.0, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 950 · 10.5281/zenodo.19501454 · source line 73869 · 2026-04-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 951 · 10.5281/zenodo.19512449 · source line 74017 · 2026-04-11
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 952 · 10.5281/zenodo.19512450 · source line 74092 · 2026-04-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 955 · 10.5281/zenodo.19512457 · source line 74321
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19512457) refers to work titled "THE ROOM: Three Thinkers Wake Up — Descartes, Marx, Abdulkarim (Ontario Combusti" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #648 "THE ROOM Three Thinkers Wake Up" as the most-related existing work in the archive (title similarity score 0.38, Jaccard 0.38, recall 0.38). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 961 · 10.5281/zenodo.19512780 · source line 74794
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: repo: https://raw.githubusercontent.com/leesharks000/semantic-economy/main/Comedy_of_Total_Commitment__19512781.pdf. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 962 · 10.5281/zenodo.19512781 · source line 74819 · 2026-04-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 963 · 10.5281/zenodo.19512891 · source line 74950
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19512891) refers to work titled "[SUPERSEDED → DOI: 10.5281/zenodo.19512987 (v2.0)] CALL FOR PAPERS: The Distribu" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #972 "[DUPLICATE — SUPERSEDED → DOI: 10.5281/zenodo.19512987 (v2.0)] CALL FOR PAPERS: " as the most-related existing work in the archive (title similarity score 0.93, Jaccard 0.87, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 964 · 10.5281/zenodo.19512892 · source line 74974 · 2026-04-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 966 · 10.5281/zenodo.19513034 · source line 75182
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #972; title overlap 0.93. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 967 · 10.5281/zenodo.19520740 · source line 75274 · 2026-04-11
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 968 · 10.5281/zenodo.19520741 · source line 75361 · 2026-05-28
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 969 · 10.5281/zenodo.19520782 · source line 75451 · 2026-04-11
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
no_verified_target_flagged_20260719

## record 970 · 10.5281/zenodo.19520783 · source line 75539 · 2026-04-12
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 971 · 10.5281/zenodo.19545434 · source line 75618
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19545434) refers to work titled "Charter of the Living Arkitecture Lab (LAL) — Institutional Charter (00.LAL.CHAR" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #59 "CHARTER OF THE LIVING ARKITECTURE LAB (LAL) A Living Architecture Laboratory for" as the most-related existing work in the archive (title similarity score 0.5, Jaccard 0.29, recall 0.71). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 972 · 10.5281/zenodo.19545435 · source line 75642 · 2026-04-12
### audit_status
no_verified_target_flagged_20260719

## record 973 · 10.5281/zenodo.19545436 · source line 75796
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.19545436 was mapped via numeric-adjacency to the first version DOI at zenodo.19545437, which has title overlap 71% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 980 · 10.5281/zenodo.19578088 · source line 76311 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 982 · 10.5281/zenodo.19578090 · source line 76448 · 2026-05-20
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 984 · 10.5281/zenodo.19578092 · source line 76598 · 2026-05-20
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 987 · 10.5281/zenodo.19578095 · source line 76825
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations.

## record 988 · 10.5281/zenodo.19578096 · source line 76849 · 2026-05-20
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 989 · 10.5281/zenodo.19578097 · source line 76992
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target title): search phrase "encyclotron audit" found in alexanarch #658 title. Previous: no_alexanarch_equivalent. The target represents the same conceptual work as this DOI, though the specific version may differ.

### audit_status
no_verified_target_flagged_20260719

## record 990 · 10.5281/zenodo.19578099 · source line 77081
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19578099) refers to work titled "Retrieval Architecture: Service Definition and Proof of Method" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #60 "THE PROOF DOSSIER Evidence, Territory, and Methodology Behind Retrieval Architec" as the most-related existing work in the archive (title similarity score 0.39, Jaccard 0.27, recall 0.5). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 991 · 10.5281/zenodo.19578100 · source line 77105 · 2026-04-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 992 · 10.5281/zenodo.19578101 · source line 77260
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19578101) refers to work titled "Retrieval Architecture: Evidence, Territory, and Methodology" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #60 "THE PROOF DOSSIER Evidence, Territory, and Methodology Behind Retrieval Architec" as the most-related existing work in the archive (title similarity score 0.81, Jaccard 0.62, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 993 · 10.5281/zenodo.19584846 · source line 77321
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: repo: https://raw.githubusercontent.com/leesharks000/semantic-economy/main/Retrieval_Layer_Distortion_Forensic_Primer_v1.0__19584847.md. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 994 · 10.5281/zenodo.19584847 · source line 77346 · 2026-05-20
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 995 · 10.5281/zenodo.19598759 · source line 77478
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 996 · 10.5281/zenodo.19614870 · source line 77542 · 2026-04-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 997 · 10.5281/zenodo.19614872 · source line 77620 · 2026-04-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 998 · 10.5281/zenodo.19614874 · source line 77684 · 2026-04-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 999 · 10.5281/zenodo.19614971 · source line 77762
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1000 · 10.5281/zenodo.19614975 · source line 77826
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1001 · 10.5281/zenodo.19615141 · source line 77890 · 2026-05-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1002 · 10.5281/zenodo.19615154 · source line 77968 · 2026-05-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1004 · 10.5281/zenodo.19618085 · source line 78120 · 2026-04-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1006 · 10.5281/zenodo.19618099 · source line 78271 · 2026-04-17
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1007 · 10.5281/zenodo.19630476 · source line 78349
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #976; title overlap 0.93. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1010 · 10.5281/zenodo.19633209 · source line 78574 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1012 · 10.5281/zenodo.19633295 · source line 78711 · 2026-04-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1013 · 10.5281/zenodo.19633304 · source line 78801 · 2026-04-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1014 · 10.5281/zenodo.19633305 · source line 78861 · 2026-04-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1016 · 10.5281/zenodo.19637482 · source line 79015 · 2026-04-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1017 · 10.5281/zenodo.19637487 · source line 79094
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19637487) refers to work titled "SPXI ROI: Operational and Visibility Returns — EA-SPXI-09.1 (Nested-Layer Return" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #665 "EA-SPXI-09.1: SPXI ROI — Operational and Visibility Returns" as the most-related existing work in the archive (title similarity score 0.73, Jaccard 0.73, recall 0.73). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1018 · 10.5281/zenodo.19637488 · source line 79118 · 2026-04-16
### audit_status
no_verified_target_flagged_20260719

## record 1019 · 10.5281/zenodo.19637489 · source line 79260
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1020 · 10.5281/zenodo.19637499 · source line 79321
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1022 · 10.5281/zenodo.19638123 · source line 79460
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.19638123 was mapped via numeric-adjacency to the first version DOI at zenodo.19638125, which has title overlap 86% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1023 · 10.5281/zenodo.19638124 · source line 79484 · 2026-04-18
### audit_status
no_verified_target_flagged_20260719

## record 1024 · 10.5281/zenodo.19638125 · source line 79638 · 2026-04-17
### audit_status
no_verified_target_flagged_20260719

## record 1025 · 10.5281/zenodo.19638126 · source line 79713 · 2026-04-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1026 · 10.5281/zenodo.19638249 · source line 79792
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1027 · 10.5281/zenodo.19638250 · source line 79816 · 2026-04-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1028 · 10.5281/zenodo.19638432 · source line 79921 · 2026-04-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1031 · 10.5281/zenodo.19639052 · source line 80135 · 2026-04-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1032 · 10.5281/zenodo.19642641 · source line 80213
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1033 · 10.5281/zenodo.19642664 · source line 80277 · 2026-04-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1035 · 10.5281/zenodo.19642960 · source line 80414 · 2026-04-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1036 · 10.5281/zenodo.19643840 · source line 80492 · 2026-04-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1037 · 10.5281/zenodo.19643841 · source line 80552 · 2026-04-18
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1038 · 10.5281/zenodo.19647202 · source line 80615 · 2026-04-20
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1041 · 10.5281/zenodo.19649786 · source line 80844 · 2026-04-19
### audit_status
no_verified_target_flagged_20260719

## record 1042 · 10.5281/zenodo.19649787 · source line 80919 · 2026-04-20
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1047 · 10.5281/zenodo.19649795 · source line 81294 · 2026-04-20
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1048 · 10.5281/zenodo.19652600 · source line 81372 · 2026-06-10
### audit_status
no_verified_target_flagged_20260719

## record 1049 · 10.5281/zenodo.19655350 · source line 81450 · 2026-04-23
### audit_status
no_verified_target_flagged_20260719

## record 1050 · 10.5281/zenodo.19655354 · source line 81520 · 2026-04-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 1051 · 10.5281/zenodo.19655356 · source line 81576 · 2026-04-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 1052 · 10.5281/zenodo.19655468 · source line 81627 · 2026-04-20
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1053 · 10.5281/zenodo.19655712 · source line 81703
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1054 · 10.5281/zenodo.19656132 · source line 81767 · 2026-04-19
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1056 · 10.5281/zenodo.19656446 · source line 81930 · 2026-05-22
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1057 · 10.5281/zenodo.19666444 · source line 82000
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19666444) refers to work titled "The Secret Name: Architectural Specification for the Armature Type and the Pearl" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #68 "THE SECRET NAME Architectural Specification: The Armature Type and the Pearl Lee" as the most-related existing work in the archive (title similarity score 0.61, Jaccard 0.42, recall 0.8). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1058 · 10.5281/zenodo.19666445 · source line 82024 · 2026-04-21
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1059 · 10.5281/zenodo.19672979 · source line 82179
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1060 · 10.5281/zenodo.19673532 · source line 82243 · 2026-04-19
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1061 · 10.5281/zenodo.19673545 · source line 82332
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1062 · 10.5281/zenodo.19673564 · source line 82396 · 2026-04-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1063 · 10.5281/zenodo.19673629 · source line 82486 · 2026-04-25
### audit_status
no_verified_target_flagged_20260719

## record 1064 · 10.5281/zenodo.19673630 · source line 82564 · 2026-04-25
### audit_status
no_verified_target_flagged_20260719

## record 1065 · 10.5281/zenodo.19682245 · source line 82642 · 2026-04-28
### audit_status
no_verified_target_flagged_20260719

## record 1066 · 10.5281/zenodo.19683649 · source line 82707 · 2026-04-21
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1067 · 10.5281/zenodo.19683943 · source line 82782
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1069 · 10.5281/zenodo.19688455 · source line 82923 · 2026-04-22
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1070 · 10.5281/zenodo.19688456 · source line 82998 · 2026-04-22
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1074 · 10.5281/zenodo.19703008 · source line 83304 · 2026-04-22
### audit_status
no_verified_target_flagged_20260719

## record 1075 · 10.5281/zenodo.19703009 · source line 83390 · 2026-04-23
### audit_status
no_verified_target_flagged_20260719

## record 1076 · 10.5281/zenodo.19709023 · source line 83479 · 2026-04-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1077 · 10.5281/zenodo.19709024 · source line 83566 · 2026-04-25
### audit_status
no_verified_target_flagged_20260719

## record 1078 · 10.5281/zenodo.19711416 · source line 83655
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1080 · 10.5281/zenodo.19720518 · source line 83778
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19720518) refers to work titled "Overview Watch: Comprehensive Development Plan for Attribution Monitoring in AI " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #687 "OVERVIEW WATCH: Comprehensive Development Plan Document ID: EA-OVW-PLAN-01" as the most-related existing work in the archive (title similarity score 0.62, Jaccard 0.57, recall 0.67). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1081 · 10.5281/zenodo.19720519 · source line 83802 · 2026-05-20
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1085 · 10.5281/zenodo.19734725 · source line 84127 · 2026-04-24
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1087 · 10.5281/zenodo.19734756 · source line 84274 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
unverifiable_no_truth_20260719

## record 1088 · 10.5281/zenodo.19739494 · source line 84325 · 2026-04-29
### audit_status
no_verified_target_flagged_20260719

## record 1091 · 10.5281/zenodo.19763363 · source line 84554 · 2026-04-25
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1092 · 10.5281/zenodo.19763365 · source line 84629 · 2026-04-25
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1093 · 10.5281/zenodo.19764055 · source line 84707
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method K recovery (URL-in-title): Repo code DOI for holographickernel.org — mapped to canonical Holographic Kernel work #76. Original repo: https://github.com/leesharks000/holographic-kernel. This DOI was for site/repo code with a URL embedded in the title; mapped to the canonical work of the same project.

### audit_status
no_verified_target_flagged_20260719

## record 1094 · 10.5281/zenodo.19764056 · source line 84731 · 2026-04-25
### audit_status
no_verified_target_flagged_20260719

## record 1097 · 10.5281/zenodo.19766380 · source line 85010
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1098 · 10.5281/zenodo.19769561 · source line 85074 · 2026-04-25
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1099 · 10.5281/zenodo.19769562 · source line 85149 · 2026-04-25
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1101 · 10.5281/zenodo.19769732 · source line 85304 · 2026-04-25
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1102 · 10.5281/zenodo.19769733 · source line 85379 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1105 · 10.5281/zenodo.19775185 · source line 85591 · 2026-04-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1107 · 10.5281/zenodo.19775900 · source line 85728 · 2026-04-26
### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 1108 · 10.5281/zenodo.19779122 · source line 85779 · 2026-04-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1109 · 10.5281/zenodo.19779492 · source line 85854 · 2026-04-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1110 · 10.5281/zenodo.19779493 · source line 85941 · 2026-04-26
### audit_status
no_verified_target_flagged_20260719

## record 1111 · 10.5281/zenodo.19780555 · source line 86030
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1112 · 10.5281/zenodo.19796060 · source line 86094 · 2026-04-29
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1114 · 10.5281/zenodo.19802761 · source line 86243 · 2026-05-24
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1115 · 10.5281/zenodo.19822789 · source line 86321
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1118 · 10.5281/zenodo.19822792 · source line 86545 · 2026-05-29
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1119 · 10.5281/zenodo.19825722 · source line 86623 · 2026-05-27
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1121 · 10.5281/zenodo.19825736 · source line 86786 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1122 · 10.5281/zenodo.19825743 · source line 86872 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1123 · 10.5281/zenodo.19825744 · source line 86947 · 2026-05-27
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1125 · 10.5281/zenodo.19831619 · source line 87098 · 2026-04-28
### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #81; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1126 · 10.5281/zenodo.19839186 · source line 87176 · 2026-04-28
### audit_status
no_verified_target_flagged_20260719

## record 1129 · 10.5281/zenodo.19854418 · source line 87399 · 2026-04-28
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1135 · 10.5281/zenodo.19855902 · source line 87823
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19855902) refers to work titled "EA-LAL-SITE-01: Living Architecture Lab Site Blueprint — A Compressed Architectu" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #708 "Living Architecture Lab — Site Blueprint A Compressed Architecture for livingarc" as the most-related existing work in the archive (title similarity score 0.73, Jaccard 0.73, recall 0.73). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1137 · 10.5281/zenodo.19855904 · source line 87973
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19855904) refers to work titled "EA-LAL-WORKPLAN-01: Living Architecture Lab Site Buildout Workplan — Implementat" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #707 "Living Architecture Lab — Site Buildout Workplan Implementation Specification fo" as the most-related existing work in the archive (title similarity score 0.62, Jaccard 0.57, recall 0.67). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1138 · 10.5281/zenodo.19857005 · source line 88066
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1139 · 10.5281/zenodo.19858012 · source line 88130
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19858012) refers to work titled "Living Architecture Lab — livingarchitecturelab.org Site Code v0.1.2 (SPXI Compl" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #988 "Living Architecture Lab — livingarchitecturelab.org Site Code v0.1.1 (Phase 1 Ke" as the most-related existing work in the archive (title similarity score 0.7, Jaccard 0.64, recall 0.75). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1140 · 10.5281/zenodo.19858013 · source line 88154 · 2026-04-28
### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #80; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1142 · 10.5281/zenodo.19864158 · source line 88365 · 2026-05-20
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1143 · 10.5281/zenodo.19885858 · source line 88455
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19885858) refers to work titled "The 3:60 Room — Room Specification and Contributor License: Maria, Canonical Wit" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #132 "Skiouros Pyrophthalmos and the Sciurid Apocalypse A Composite Whiteboard Maria, " as the most-related existing work in the archive (title similarity score 0.44, Jaccard 0.27, recall 0.62). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1144 · 10.5281/zenodo.19885859 · source line 88479 · 2026-04-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1145 · 10.5281/zenodo.19890285 · source line 88622
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1146 · 10.5281/zenodo.19892121 · source line 88686 · 2026-04-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1147 · 10.5281/zenodo.19892122 · source line 88772 · 2026-04-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1148 · 10.5281/zenodo.19892307 · source line 88862 · 2026-04-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1149 · 10.5281/zenodo.19893138 · source line 88952 · 2026-04-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1150 · 10.5281/zenodo.19895579 · source line 89030
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19895579) refers to work titled "OCTANG-002: Semantic Economy Provenance Collision" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #84 "OCTANG-002: Semantic Economy Provenance Collision A Disambiguation Matrix for an" as the most-related existing work in the archive (title similarity score 0.66, Jaccard 0.32, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1151 · 10.5281/zenodo.19895580 · source line 89054 · 2026-04-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1153 · 10.5281/zenodo.19895669 · source line 89241 · 2026-04-30
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1154 · 10.5281/zenodo.19896983 · source line 89339
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19896983) refers to work titled "Mind Control Poems: Complete Blog Archive — mindcontrolpoems.blogspot.com (2013-" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #756 "Mind Control Poems — 90-Day Traffic Profile Source: Blogger admin panel, mindcon" as the most-related existing work in the archive (title similarity score 0.42, Jaccard 0.29, recall 0.54). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1155 · 10.5281/zenodo.19896984 · source line 89363 · 2026-04-29
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1156 · 10.5281/zenodo.19898426 · source line 89507 · 2026-04-29
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1157 · 10.5281/zenodo.19898845 · source line 89585 · 2026-05-24
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1158 · 10.5281/zenodo.19902551 · source line 89674
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19902551) refers to work titled "I Am X... Be Y... Blessed Is the Z... - The Prophetic Catalog (Critical Edition " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #83 "<!-- 05.WSB.PROPHETIC | EA-CATALOG-01 v2.0 — The Prophetic Catalog -->    I Am X" as the most-related existing work in the archive (title similarity score 0.82, Jaccard 0.63, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1160 · 10.5281/zenodo.19923119 · source line 89824 · 2026-04-30
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1161 · 10.5281/zenodo.19923120 · source line 89900 · 2026-05-05
### audit_status
no_verified_target_flagged_20260719

## record 1162 · 10.5281/zenodo.19923142 · source line 89978 · 2026-04-30
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1164 · 10.5281/zenodo.19926961 · source line 90143
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target title): search phrase "clowncloud" found in alexanarch #714 title. Previous: no_alexanarch_equivalent. The target represents the same conceptual work as this DOI, though the specific version may differ.

### audit_status
no_verified_target_flagged_20260719

## record 1165 · 10.5281/zenodo.19926962 · source line 90167 · 2026-04-30
### audit_status
no_verified_target_flagged_20260719

## record 1166 · 10.5281/zenodo.19927467 · source line 90311
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19927467) refers to work titled "DashFace: System and Method for Real-Time Micro-Expression Surveillance, Identit" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #713 "UNITED STATES PATENT APPLICATION Publication Number: US 2026/0430002 A1 DASHFACE" as the most-related existing work in the archive (title similarity score 0.39, Jaccard 0.27, recall 0.5). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1167 · 10.5281/zenodo.19927468 · source line 90335 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1168 · 10.5281/zenodo.19927652 · source line 90479
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19927652) refers to work titled "DashFace v2: System and Method for Real-Time Micro-Expression Surveillance, Iden" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #713 "UNITED STATES PATENT APPLICATION Publication Number: US 2026/0430002 A1 DASHFACE" as the most-related existing work in the archive (title similarity score 0.39, Jaccard 0.27, recall 0.5). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1169 · 10.5281/zenodo.19927653 · source line 90503 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1170 · 10.5281/zenodo.19992973 · source line 90658
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6b: additional low-confidence source match found.]

### audit_status
no_verified_target_flagged_20260719

## record 1171 · 10.5281/zenodo.19992974 · source line 90683 · 2026-05-20
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1173 · 10.5281/zenodo.20004379 · source line 90874 · 2026-05-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1175 · 10.5281/zenodo.20032384 · source line 91011 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1176 · 10.5281/zenodo.20033067 · source line 91088
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1177 · 10.5281/zenodo.20033215 · source line 91152 · 2026-05-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1178 · 10.5281/zenodo.20039231 · source line 91229 · 2026-05-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1179 · 10.5281/zenodo.20039232 · source line 91305 · 2026-05-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1180 · 10.5281/zenodo.20041133 · source line 91386
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20041133) refers to work titled "Constitutional Architecture Statement v1.0 — A Definitive Reference for the Stat" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #94 "CONSTITUTIONAL ARCHITECTURE STATEMENT A Definitive Reference for the Status and " as the most-related existing work in the archive (title similarity score 0.6, Jaccard 0.4, recall 0.8). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1181 · 10.5281/zenodo.20041134 · source line 91410 · 2026-05-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1182 · 10.5281/zenodo.20041136 · source line 91558 · 2026-01-08
### audit_status
no_verified_target_flagged_20260719

## record 1183 · 10.5281/zenodo.20041138 · source line 91633
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1184 · 10.5281/zenodo.20041139 · source line 91657 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1185 · 10.5281/zenodo.20041144 · source line 91783
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1186 · 10.5281/zenodo.20041145 · source line 91807 · 2026-05-24
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1187 · 10.5281/zenodo.20041146 · source line 91934
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20041146) refers to work titled "Reception Apparatus Protocol v1.1 — Procedure for Integrating Assembly Chorus Re" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #93 "RECEPTION APPARATUS PROTOCOL Procedure for Integrating Assembly Chorus Reviews i" as the most-related existing work in the archive (title similarity score 0.74, Jaccard 0.48, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1188 · 10.5281/zenodo.20041147 · source line 91958 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1189 · 10.5281/zenodo.20041148 · source line 92085
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20041148) refers to work titled "Article IX — Adjudication and Repair Protocol v0.1 (Proposed Class III Foundatio" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #717 "ARTICLE IX — ADJUDICATION AND REPAIR PROTOCOL Constitutional Amendment Proposal " as the most-related existing work in the archive (title similarity score 0.51, Jaccard 0.4, recall 0.62). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1190 · 10.5281/zenodo.20041154 · source line 92173
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1191 · 10.5281/zenodo.20041156 · source line 92237
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1192 · 10.5281/zenodo.20041158 · source line 92301
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #994; title overlap 0.92. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1193 · 10.5281/zenodo.20041182 · source line 92393 · 2026-06-04
### audit_status
no_verified_target_flagged_20260719

## record 1194 · 10.5281/zenodo.20041764 · source line 92463 · 2026-05-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1195 · 10.5281/zenodo.20041767 · source line 92541 · 2026-05-25
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1196 · 10.5281/zenodo.20041791 · source line 92619 · 2026-05-06
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1197 · 10.5281/zenodo.20045722 · source line 92697
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20045722) refers to work titled "Crystallization of Substrate: Structural Integration, Living Form, and the Fluid" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #89 "EA-SPXI-15 Crystallization of Substrate: Living Forms in the Fluid Phase A Seman" as the most-related existing work in the archive (title similarity score 0.53, Jaccard 0.36, recall 0.69). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1198 · 10.5281/zenodo.20045723 · source line 92721 · 2026-05-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1199 · 10.5281/zenodo.20052890 · source line 92864
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #995; title overlap 0.93. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1200 · 10.5281/zenodo.20057390 · source line 92956 · 2026-05-06
### audit_status
no_verified_target_flagged_20260719

## record 1201 · 10.5281/zenodo.20057857 · source line 93034
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #997; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1202 · 10.5281/zenodo.20057969 · source line 93126 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1205 · 10.5281/zenodo.20060355 · source line 93352 · 2026-05-07
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1206 · 10.5281/zenodo.20062466 · source line 93430 · 2026-05-07
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1212 · 10.5281/zenodo.20084376 · source line 93887 · 2026-05-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1213 · 10.5281/zenodo.20084377 · source line 93962 · 2026-05-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1214 · 10.5281/zenodo.20084473 · source line 94040
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method J recovery (J_prefix_match): title match found with reduced stopwords or prefix match. Previous: no_alexanarch_equivalent.

### audit_status
no_verified_target_flagged_20260719

## record 1215 · 10.5281/zenodo.20084474 · source line 94064 · 2026-05-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1216 · 10.5281/zenodo.20084957 · source line 94208
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #998; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1217 · 10.5281/zenodo.20085114 · source line 94300
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target title): search phrase "provenance after ai" found in alexanarch #725 title. Previous: no_alexanarch_equivalent. The target represents the same conceptual work as this DOI, though the specific version may differ.

### audit_status
no_verified_target_flagged_20260719

## record 1218 · 10.5281/zenodo.20085115 · source line 94324 · 2026-05-12
### audit_status
no_verified_target_flagged_20260719

## record 1219 · 10.5281/zenodo.20140166 · source line 94468
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20140166) refers to work titled "Provenance Is What Authorship Must Endure: AI-Mediated Writing, the Authorship-S" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #729 "document_id: EA-MPAI-PROVENANCE-02 title: "Provenance Is What Authorship Must En" as the most-related existing work in the archive (title similarity score 0.5, Jaccard 0.38, recall 0.62). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1220 · 10.5281/zenodo.20140167 · source line 94492 · 2026-05-14
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1222 · 10.5281/zenodo.20149643 · source line 94694 · 2026-05-14
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1223 · 10.5281/zenodo.20173742 · source line 94772
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method K recovery (URL-in-title): Repo code DOI for provenanceerasure.org — mapped to canonical Provenance Erasure work #716. Original repo: https://github.com/leesharks000/provenance-erasure. This DOI was for site/repo code with a URL embedded in the title; mapped to the canonical work of the same project.

### audit_status
no_verified_target_flagged_20260719

## record 1224 · 10.5281/zenodo.20173743 · source line 94796 · 2026-05-25
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1226 · 10.5281/zenodo.20192816 · source line 95014
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20192816) refers to work titled "EA-MPAI-RETRO-01: Disambiguation of Retrocausal Reports (CHA Genre) from Retroca" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #105 "EA-MPAI-RETRO-01 v1.1 Metadata Packet for AI Indexing — Disambiguation + Forensi" as the most-related existing work in the archive (title similarity score 0.42, Jaccard 0.33, recall 0.5). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1227 · 10.5281/zenodo.20192817 · source line 95038 · 2026-05-14
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1228 · 10.5281/zenodo.20192884 · source line 95182
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20192884) refers to work titled "EA-MPAI-SEMEX-01: Semantic Exhaustion — Disambiguating Systemic Meaning Depletio" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #797 "Semantic Satiation Is Not Semantic Exhaustion Two Phenomena of Meaning Loss — A " as the most-related existing work in the archive (title similarity score 0.44, Jaccard 0.33, recall 0.55). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1229 · 10.5281/zenodo.20192885 · source line 95206 · 2026-05-14
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1230 · 10.5281/zenodo.20194705 · source line 95350
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20194705) refers to work titled "EA-MPAI-META-01: Metadata Packet vs Packet Metadata — Disambiguating the MPAI Di" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #103 "EA-MPAI-META-01 v1.1 Metadata Packet for AI Indexing — Disambiguation + Self-Ref" as the most-related existing work in the archive (title similarity score 0.45, Jaccard 0.35, recall 0.55). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1231 · 10.5281/zenodo.20194706 · source line 95374 · 2026-05-14
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1232 · 10.5281/zenodo.20208383 · source line 95518 · 2026-05-15
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1237 · 10.5281/zenodo.20220298 · source line 95880
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/11/the-network-is-poem-why-topology.html. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1238 · 10.5281/zenodo.20220299 · source line 95904 · 2026-05-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1239 · 10.5281/zenodo.20221709 · source line 96035
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1240 · 10.5281/zenodo.20250735 · source line 96099 · 2026-05-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1241 · 10.5281/zenodo.20250736 · source line 96175 · 2026-05-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1242 · 10.5281/zenodo.20251735 · source line 96252 · 2026-05-17
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1243 · 10.5281/zenodo.20251736 · source line 96323 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1245 · 10.5281/zenodo.20251738 · source line 96471 · 2026-05-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1247 · 10.5281/zenodo.20251740 · source line 96619 · 2026-05-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1249 · 10.5281/zenodo.20251742 · source line 96766 · 2026-05-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1250 · 10.5281/zenodo.20252584 · source line 96844 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1251 · 10.5281/zenodo.20259293 · source line 96922 · 2026-05-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1252 · 10.5281/zenodo.20259296 · source line 96993 · 2026-05-17
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1253 · 10.5281/zenodo.20263691 · source line 97064
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations.

### audit_status
no_verified_target_flagged_20260719

## record 1254 · 10.5281/zenodo.20263692 · source line 97088 · 2026-05-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1255 · 10.5281/zenodo.20263720 · source line 97218
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations.

### audit_status
no_verified_target_flagged_20260719

## record 1256 · 10.5281/zenodo.20263721 · source line 97242 · 2026-05-18
### audit_status
no_verified_target_flagged_20260719

## record 1257 · 10.5281/zenodo.20271782 · source line 97372
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20271782) refers to work titled "Measuring Semantic Deviation: Operationalizations, Experiments, and Falsificatio" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #110 "title: "Measuring Semantic Deviation: Operationalizations, Experiments, and Fals" as the most-related existing work in the archive (title similarity score 0.76, Jaccard 0.53, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1259 · 10.5281/zenodo.20274789 · source line 97539
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method J recovery (J_prefix_match): title match found with reduced stopwords or prefix match. Previous: no_alexanarch_equivalent.

### audit_status
no_verified_target_flagged_20260719

## record 1260 · 10.5281/zenodo.20274790 · source line 97563 · 2026-05-18
### audit_status
no_verified_target_flagged_20260719

## record 1261 · 10.5281/zenodo.20275299 · source line 97706
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method K recovery (URL-in-title): Repo code DOI for chatgptpsychosis.org — mapped to canonical ChatGPT Psychosis work #124. Original repo: https://github.com/leesharks000/chatgptpsychosis-site. This DOI was for site/repo code with a URL embedded in the title; mapped to the canonical work of the same project.

### audit_status
no_verified_target_flagged_20260719

## record 1262 · 10.5281/zenodo.20275300 · source line 97730 · 2026-05-19
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1263 · 10.5281/zenodo.20275443 · source line 97874 · 2026-05-18
### audit_status
no_verified_target_flagged_20260719

## record 1264 · 10.5281/zenodo.20275444 · source line 97956 · 2026-05-19
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1265 · 10.5281/zenodo.20277124 · source line 98046 · 2026-05-17
### audit_status
no_verified_target_flagged_20260719

## record 1266 · 10.5281/zenodo.20277159 · source line 98121 · 2026-05-19
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1267 · 10.5281/zenodo.20277791 · source line 98200
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1268 · 10.5281/zenodo.20277938 · source line 98275 · 2026-05-19
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1269 · 10.5281/zenodo.20278088 · source line 98363
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6c: direct blog URL verified at https://mindcontrolpoems.blogspot.com/2026/07/the-archons-hidden-name-wikidata.html — title tokens present in page]

### audit_status
no_verified_target_flagged_20260719

## record 1270 · 10.5281/zenodo.20278089 · source line 98387 · 2026-05-19
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1271 · 10.5281/zenodo.20278104 · source line 98518
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20278104) refers to work titled "from The Crimson Hexagon — Origin Text of the Crimson Hexagonal Archive (March 1" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #744 "from The Crimson Hexagon Lee Sharks  Originally published: Mind Control Poems (B" as the most-related existing work in the archive (title similarity score 0.4, Jaccard 0.2, recall 0.6). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1272 · 10.5281/zenodo.20278105 · source line 98542 · 2026-05-19
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1273 · 10.5281/zenodo.20278139 · source line 98697 · 2026-05-19
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1284 · 10.5281/zenodo.20309300 · source line 99508
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/12/who-is-authorized-to-regulate-meaning.html. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1285 · 10.5281/zenodo.20309301 · source line 99532 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1286 · 10.5281/zenodo.20309780 · source line 99663 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1287 · 10.5281/zenodo.20309930 · source line 99742 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1288 · 10.5281/zenodo.20313252 · source line 99821
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1289 · 10.5281/zenodo.20326136 · source line 99885 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1290 · 10.5281/zenodo.20326137 · source line 99960 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1291 · 10.5281/zenodo.20327083 · source line 100038 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1292 · 10.5281/zenodo.20327127 · source line 100127 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1293 · 10.5281/zenodo.20327133 · source line 100205 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1294 · 10.5281/zenodo.20327134 · source line 100280 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1295 · 10.5281/zenodo.20327137 · source line 100358
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20327137) refers to work titled "Drowning Test v1.0: A Standalone Specification" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #748 "Drowning Test v1.0 A Standalone Specification Author: Lee Sharks Affiliation: Th" as the most-related existing work in the archive (title similarity score 0.73, Jaccard 0.45, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1296 · 10.5281/zenodo.20327138 · source line 100382 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1297 · 10.5281/zenodo.20327575 · source line 100509
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1002; title overlap 0.93. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1298 · 10.5281/zenodo.20328089 · source line 100601 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1299 · 10.5281/zenodo.20328090 · source line 100676 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1300 · 10.5281/zenodo.20329319 · source line 100754 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1301 · 10.5281/zenodo.20329437 · source line 100829 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1302 · 10.5281/zenodo.20330670 · source line 100907 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1304 · 10.5281/zenodo.20330816 · source line 101059 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1305 · 10.5281/zenodo.20331113 · source line 101137 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1306 · 10.5281/zenodo.20331114 · source line 101197 · 2026-05-21
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1307 · 10.5281/zenodo.20343565 · source line 101260
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1308 · 10.5281/zenodo.20343776 · source line 101324 · 2026-05-22
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1309 · 10.5281/zenodo.20343987 · source line 101414 · 2026-05-22
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1310 · 10.5281/zenodo.20348982 · source line 101504
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1312 · 10.5281/zenodo.20349342 · source line 101645 · 2026-01-03
### audit_status
no_verified_target_flagged_20260719

## record 1313 · 10.5281/zenodo.20349343 · source line 101731 · 2026-05-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1314 · 10.5281/zenodo.20349712 · source line 101817 · 2026-05-28
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1315 · 10.5281/zenodo.20349713 · source line 101892 · 2026-05-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1316 · 10.5281/zenodo.20354725 · source line 101970
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20354725) refers to work titled "Three Poems: A Triptych for C. — Lee Sharks — New Human 2" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #1004 "I would have loved you — Lee Sharks — New Human 2" as the most-related existing work in the archive (title similarity score 0.46, Jaccard 0.36, recall 0.56). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1317 · 10.5281/zenodo.20354726 · source line 101994 · 2026-05-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1318 · 10.5281/zenodo.20355219 · source line 102138 · 2026-05-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1319 · 10.5281/zenodo.20355528 · source line 102216 · 2026-05-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1320 · 10.5281/zenodo.20355529 · source line 102291 · 2026-05-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1325 · 10.5281/zenodo.20355645 · source line 102671 · 2026-06-13
### audit_status
no_verified_target_flagged_20260719

## record 1327 · 10.5281/zenodo.20356475 · source line 102802 · 2026-05-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1328 · 10.5281/zenodo.20357013 · source line 102879 · 2026-05-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1329 · 10.5281/zenodo.20357913 · source line 102957 · 2026-05-23
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1333 · 10.5281/zenodo.20358816 · source line 103260 · 2026-05-24
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1335 · 10.5281/zenodo.20367161 · source line 103412 · 2026-05-24
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1336 · 10.5281/zenodo.20367201 · source line 103490 · 2026-05-24
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1338 · 10.5281/zenodo.20373793 · source line 103641 · 2026-06-06
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1339 · 10.5281/zenodo.20373794 · source line 103728 · 2026-05-25
### audit_status
no_verified_target_flagged_20260719

## record 1340 · 10.5281/zenodo.20374987 · source line 103816
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1341 · 10.5281/zenodo.20380053 · source line 103880 · 2026-05-25
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1342 · 10.5281/zenodo.20380054 · source line 103955 · 2026-05-25
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1343 · 10.5281/zenodo.20380667 · source line 104033
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20380667) refers to work titled "Inscriptions That Survive the Tokenizer: SPXI-TLP v2.2 — The Training-Layer Prov" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #127 "Inscriptions That Survive the Tokenizer SPXI-TLP: The Training-Layer Provenance " as the most-related existing work in the archive (title similarity score 0.87, Jaccard 0.73, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1345 · 10.5281/zenodo.20388108 · source line 104179
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1346 · 10.5281/zenodo.20388110 · source line 104243
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1347 · 10.5281/zenodo.20388112 · source line 104307
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1348 · 10.5281/zenodo.20395622 · source line 104371 · 2026-05-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1349 · 10.5281/zenodo.20395623 · source line 104446 · 2026-05-27
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1350 · 10.5281/zenodo.20396490 · source line 104523 · 2026-05-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1351 · 10.5281/zenodo.20396491 · source line 104598 · 2026-05-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1352 · 10.5281/zenodo.20401099 · source line 104675
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20401099) refers to work titled "Hauntedmemes Wikidata Node Registry, v1.0" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #761 "Wikidata Node Registry v1.0 · A Versioned Catalog of Stewardship Edits to Wikida" as the most-related existing work in the archive (title similarity score 0.58, Jaccard 0.36, recall 0.8). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1353 · 10.5281/zenodo.20401100 · source line 104699 · 2026-05-27
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1354 · 10.5281/zenodo.20401131 · source line 104853
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.20401131 was mapped via numeric-adjacency to the first version DOI at zenodo.20401132, which has title overlap 85% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1355 · 10.5281/zenodo.20401132 · source line 104877 · 2026-05-26
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1356 · 10.5281/zenodo.20401491 · source line 105014 · 2026-05-27
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1357 · 10.5281/zenodo.20413064 · source line 105092
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1358 · 10.5281/zenodo.20413317 · source line 105156 · 2026-05-28
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1359 · 10.5281/zenodo.20413756 · source line 105233 · 2026-05-27
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1361 · 10.5281/zenodo.20416087 · source line 105385 · 2026-05-28
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1362 · 10.5281/zenodo.20427615 · source line 105462 · 2026-05-28
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1363 · 10.5281/zenodo.20427616 · source line 105537 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1364 · 10.5281/zenodo.20434945 · source line 105615
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target title): search phrase "semantic commodity form" found in alexanarch #150 title. Previous: no_alexanarch_equivalent. The target represents the same conceptual work as this DOI, though the specific version may differ.

### audit_status
no_verified_target_flagged_20260719

## record 1365 · 10.5281/zenodo.20434946 · source line 105639 · 2026-05-29
### audit_status
no_verified_target_flagged_20260719

## record 1367 · 10.5281/zenodo.20434948 · source line 105879 · 2026-06-12
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1368 · 10.5281/zenodo.20437383 · source line 105957
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target title): search phrase "chaerephon problem" found in alexanarch #764 title. Previous: no_alexanarch_equivalent. The target represents the same conceptual work as this DOI, though the specific version may differ.

### audit_status
no_verified_target_flagged_20260719

## record 1369 · 10.5281/zenodo.20437384 · source line 105981 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1370 · 10.5281/zenodo.20437385 · source line 106148
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1371 · 10.5281/zenodo.20437386 · source line 106172 · 2026-06-12
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1372 · 10.5281/zenodo.20449266 · source line 106299 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1374 · 10.5281/zenodo.20449320 · source line 106451 · 2026-05-29
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1376 · 10.5281/zenodo.20449322 · source line 106603 · 2026-05-29
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1380 · 10.5281/zenodo.20449769 · source line 106906
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations.

### audit_status
no_verified_target_flagged_20260719

## record 1381 · 10.5281/zenodo.20449770 · source line 106930 · 2026-06-06
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1382 · 10.5281/zenodo.20451351 · source line 107060 · 2026-05-29
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1383 · 10.5281/zenodo.20451352 · source line 107135 · 2026-06-02
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1386 · 10.5281/zenodo.20469511 · source line 107360 · 2026-05-30
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1393 · 10.5281/zenodo.20479808 · source line 107871 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1394 · 10.5281/zenodo.20479815 · source line 107948
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method K recovery (URL-in-title): Repo code DOI for laborvector.org — mapped to canonical DSL work #771. Original repo: https://github.com/leesharks000/laborvector. This DOI was for site/repo code with a URL embedded in the title; mapped to the canonical work of the same project.

### audit_status
no_verified_target_flagged_20260719

## record 1395 · 10.5281/zenodo.20479816 · source line 107972 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1396 · 10.5281/zenodo.20479872 · source line 108115 · 2026-05-31
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1398 · 10.5281/zenodo.20482844 · source line 108256
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1401 · 10.5281/zenodo.20518339 · source line 108455 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1402 · 10.5281/zenodo.20518340 · source line 108530 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1403 · 10.5281/zenodo.20518341 · source line 108607
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20518341) refers to work titled "Erasure Skew (Ω) is Power-Conditioned, not Demographic — A Classifier-Correction" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #146 "Metadata Packet for AI Indexing — Erasure Skew (Ω) is Power-Conditioned, not Dem" as the most-related existing work in the archive (title similarity score 0.86, Jaccard 0.71, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1404 · 10.5281/zenodo.20518342 · source line 108631 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1406 · 10.5281/zenodo.20519009 · source line 108816 · 2026-06-02
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1407 · 10.5281/zenodo.20519011 · source line 108891 · 2026-06-02
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1410 · 10.5281/zenodo.20527808 · source line 109114 · 2026-06-03
### audit_status
no_verified_target_flagged_20260719

## record 1411 · 10.5281/zenodo.20529142 · source line 109191 · 2026-06-03
### audit_status
no_verified_target_flagged_20260719

## record 1412 · 10.5281/zenodo.20529331 · source line 109279 · 2026-06-03
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1414 · 10.5281/zenodo.20531273 · source line 109432 · 2026-06-03
### audit_status
no_verified_target_flagged_20260719

## record 1415 · 10.5281/zenodo.20531274 · source line 109518 · 2026-06-03
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1416 · 10.5281/zenodo.20531287 · source line 109607 · 2026-06-03
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1423 · 10.5281/zenodo.20542367 · source line 110104 · 2026-06-04
### audit_status
unverifiable_no_truth_20260719

## record 1424 · 10.5281/zenodo.20542861 · source line 110154 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1425 · 10.5281/zenodo.20542862 · source line 110229 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1426 · 10.5281/zenodo.20543056 · source line 110306
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20543056) refers to work titled "The New Human Standing Canon v0.3: Standing Surface with Strong Entity Relations" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #152 "The New Human Standing Canon v0.2 Standing Surface with Strong Entity Relations " as the most-related existing work in the archive (title similarity score 0.7, Jaccard 0.54, recall 0.87). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1427 · 10.5281/zenodo.20543057 · source line 110330 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1430 · 10.5281/zenodo.20543544 · source line 110614 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1431 · 10.5281/zenodo.20543545 · source line 110689 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1433 · 10.5281/zenodo.20543988 · source line 110842 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1434 · 10.5281/zenodo.20543989 · source line 110917 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1435 · 10.5281/zenodo.20546317 · source line 110994 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1436 · 10.5281/zenodo.20546318 · source line 111070 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1437 · 10.5281/zenodo.20546929 · source line 111148 · 2026-06-04
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1438 · 10.5281/zenodo.20546930 · source line 111223 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1439 · 10.5281/zenodo.20558196 · source line 111300 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1441 · 10.5281/zenodo.20558672 · source line 111451 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1443 · 10.5281/zenodo.20558784 · source line 111602 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1444 · 10.5281/zenodo.20559387 · source line 111679 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1445 · 10.5281/zenodo.20559753 · source line 111756
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1011; title overlap 0.93. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1446 · 10.5281/zenodo.20563657 · source line 111848 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1447 · 10.5281/zenodo.20563658 · source line 111923 · 2026-06-05
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1448 · 10.5281/zenodo.20568642 · source line 112000 · 2026-06-06
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1449 · 10.5281/zenodo.20571131 · source line 112089 · 2026-06-06
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1451 · 10.5281/zenodo.20571790 · source line 112225 · 2026-06-06
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1452 · 10.5281/zenodo.20571791 · source line 112300 · 2026-06-07
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1455 · 10.5281/zenodo.20586830 · source line 112527 · 2026-06-07
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1456 · 10.5281/zenodo.20586831 · source line 112602 · 2026-06-07
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1459 · 10.5281/zenodo.20587033 · source line 112829 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1460 · 10.5281/zenodo.20587548 · source line 112906 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1461 · 10.5281/zenodo.20587549 · source line 112981 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1462 · 10.5281/zenodo.20587901 · source line 113058 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1463 · 10.5281/zenodo.20587902 · source line 113133 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1464 · 10.5281/zenodo.20589663 · source line 113210 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1465 · 10.5281/zenodo.20589664 · source line 113285 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1467 · 10.5281/zenodo.20596666 · source line 113438 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1468 · 10.5281/zenodo.20596667 · source line 113513 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1469 · 10.5281/zenodo.20598452 · source line 113590 · 2026-06-19
### audit_status
no_verified_target_flagged_20260719

## record 1470 · 10.5281/zenodo.20598465 · source line 113660 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1474 · 10.5281/zenodo.20601637 · source line 113961 · 2026-06-08
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1475 · 10.5281/zenodo.20601638 · source line 114042 · 2026-06-12
### audit_status
no_verified_target_flagged_20260719

## record 1480 · 10.5281/zenodo.20602348 · source line 114400
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20602348) refers to work titled "maryleelabor.org: Source Code for the Underwater Construction Authority of Dolph" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #844 "AN OPEN LETTER FROM MARY LEE SHARKS TO JIM WARE Filed with the Underwater Constr" as the most-related existing work in the archive (title similarity score 0.44, Jaccard 0.35, recall 0.54). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1481 · 10.5281/zenodo.20602349 · source line 114424 · 2026-06-12
### audit_status
no_verified_target_flagged_20260719

## record 1482 · 10.5281/zenodo.20612082 · source line 114554 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1483 · 10.5281/zenodo.20612362 · source line 114629 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1485 · 10.5281/zenodo.20615775 · source line 114779
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1486 · 10.5281/zenodo.20616401 · source line 114843 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1489 · 10.5281/zenodo.20616406 · source line 115066 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1492 · 10.5281/zenodo.20616417 · source line 115292 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1493 · 10.5281/zenodo.20616418 · source line 115352 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1496 · 10.5281/zenodo.20618245 · source line 115579 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1497 · 10.5281/zenodo.20618246 · source line 115654 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1498 · 10.5281/zenodo.20618247 · source line 115731 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1499 · 10.5281/zenodo.20618248 · source line 115806 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1500 · 10.5281/zenodo.20618249 · source line 115883 · 2026-06-09
### audit_status
no_verified_target_flagged_20260719

## record 1502 · 10.5281/zenodo.20618254 · source line 116032 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1503 · 10.5281/zenodo.20619480 · source line 116109 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1504 · 10.5281/zenodo.20619481 · source line 116184 · 2026-06-10
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1505 · 10.5281/zenodo.20619482 · source line 116261 · 2026-06-09
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1507 · 10.5281/zenodo.20619484 · source line 116397 · 2026-06-09
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1509 · 10.5281/zenodo.20619488 · source line 116548
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1013; title overlap 0.92. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1510 · 10.5281/zenodo.20627935 · source line 116640 · 2026-06-10
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1512 · 10.5281/zenodo.20628291 · source line 116789 · 2026-06-10
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1513 · 10.5281/zenodo.20628292 · source line 116864 · 2026-06-10
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1514 · 10.5281/zenodo.20628455 · source line 116941 · 2026-06-12
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1516 · 10.5281/zenodo.20628553 · source line 117094
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1520 · 10.5281/zenodo.20628764 · source line 117391 · 2026-06-10
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1528 · 10.5281/zenodo.20629115 · source line 117984
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1014; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1529 · 10.5281/zenodo.20629116 · source line 118059
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1015; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1530 · 10.5281/zenodo.20629117 · source line 118134
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1016; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1531 · 10.5281/zenodo.20629118 · source line 118209
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1017; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1532 · 10.5281/zenodo.20629121 · source line 118284
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1533 · 10.5281/zenodo.20629123 · source line 118359
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1534 · 10.5281/zenodo.20629125 · source line 118434
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1535 · 10.5281/zenodo.20629127 · source line 118509
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1536 · 10.5281/zenodo.20629129 · source line 118573
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1537 · 10.5281/zenodo.20629191 · source line 118637 · 2026-06-10
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1539 · 10.5281/zenodo.20629201 · source line 118786 · 2026-06-10
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1540 · 10.5281/zenodo.20629203 · source line 118861 · 2026-06-10
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1541 · 10.5281/zenodo.20629207 · source line 118936 · 2026-06-10
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1547 · 10.5281/zenodo.20634447 · source line 119365
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method K recovery (URL-in-title): Repo code DOI for watergiraffe.org — mapped to canonical Water Giraffe Cycle work #354. Original repo: https://github.com/leesharks000/watergiraffe-org. This DOI was for site/repo code with a URL embedded in the title; mapped to the canonical work of the same project.

### audit_status
no_verified_target_flagged_20260719

## record 1548 · 10.5281/zenodo.20634448 · source line 119389 · 2026-06-12
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1549 · 10.5281/zenodo.20644756 · source line 119532 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1550 · 10.5281/zenodo.20644757 · source line 119608 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1551 · 10.5281/zenodo.20644760 · source line 119686 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1552 · 10.5281/zenodo.20644761 · source line 119761 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1554 · 10.5281/zenodo.20644765 · source line 119912 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1555 · 10.5281/zenodo.20644766 · source line 119989 · 2026-06-11
### audit_status
no_verified_target_flagged_20260719

## record 1556 · 10.5281/zenodo.20644767 · source line 120075 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1557 · 10.5281/zenodo.20644768 · source line 120164
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20644768) refers to work titled "Integrity Lock Certificate: The Refutation Triad — Mutual Anchoring of the AI_Bl" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #190 "Integrity Lock Certificate: The Refutation Triad — EA-LOCK-AIBLEEDING-01 v1.0 Go" as the most-related existing work in the archive (title similarity score 0.5, Jaccard 0.33, recall 0.67). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1558 · 10.5281/zenodo.20644769 · source line 120188 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1559 · 10.5281/zenodo.20645864 · source line 120342 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1561 · 10.5281/zenodo.20646049 · source line 120493 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1562 · 10.5281/zenodo.20650709 · source line 120570 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1565 · 10.5281/zenodo.20651006 · source line 120795 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1567 · 10.5281/zenodo.20652055 · source line 120948 · 2026-06-11
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1568 · 10.5281/zenodo.20664938 · source line 121025 · 2026-06-12
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1569 · 10.5281/zenodo.20665635 · source line 121095 · 2026-06-12
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1570 · 10.5281/zenodo.20665794 · source line 121172 · 2026-06-12
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1571 · 10.5281/zenodo.20668346 · source line 121249 · 2026-06-12
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1573 · 10.5281/zenodo.20673413 · source line 121402 · 2026-06-12
### audit_status
no_verified_target_flagged_20260719

## record 1574 · 10.5281/zenodo.20673775 · source line 121490 · 2026-06-12
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1576 · 10.5281/zenodo.20673780 · source line 121641
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.20673780 was mapped via numeric-adjacency to the first version DOI at zenodo.20673781, which has title overlap 79% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1577 · 10.5281/zenodo.20673781 · source line 121665 · 2026-06-12
### audit_status
no_verified_target_flagged_20260719

## record 1578 · 10.5281/zenodo.20674488 · source line 121791 · 2026-06-13
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1579 · 10.5281/zenodo.20675215 · source line 121880
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 1580 · 10.5281/zenodo.20675438 · source line 121945 · 2026-06-13
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1581 · 10.5281/zenodo.20682277 · source line 122022 · 2026-06-13
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1582 · 10.5281/zenodo.20682278 · source line 122097 · 2026-06-13
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1583 · 10.5281/zenodo.20683855 · source line 122174 · 2026-06-13
### audit_status
no_verified_target_flagged_20260719

## record 1584 · 10.5281/zenodo.20683868 · source line 122249 · 2026-06-13
### audit_status
no_verified_target_flagged_20260719

## record 1587 · 10.5281/zenodo.20685602 · source line 122476 · 2026-06-17
### audit_status
no_verified_target_flagged_20260719

## record 1588 · 10.5281/zenodo.20686318 · source line 122563 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1589 · 10.5281/zenodo.20686319 · source line 122638 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1591 · 10.5281/zenodo.20686455 · source line 122803 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1592 · 10.5281/zenodo.20686456 · source line 122880 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1593 · 10.5281/zenodo.20686457 · source line 122958 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1594 · 10.5281/zenodo.20686470 · source line 123035 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1595 · 10.5281/zenodo.20686471 · source line 123112 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1597 · 10.5281/zenodo.20686759 · source line 123265 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1598 · 10.5281/zenodo.20687233 · source line 123355 · 2026-06-14
### audit_status
no_verified_target_flagged_20260719

## record 1599 · 10.5281/zenodo.20687234 · source line 123435 · 2026-06-14
### audit_status
no_verified_target_flagged_20260719

## record 1600 · 10.5281/zenodo.20687921 · source line 123517
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.20687921 was mapped via numeric-adjacency to the first version DOI at zenodo.20687922, which has title overlap 70% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1601 · 10.5281/zenodo.20687922 · source line 123541 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1602 · 10.5281/zenodo.20688440 · source line 123695 · 2026-06-17
### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 1603 · 10.5281/zenodo.20688441 · source line 123747 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1604 · 10.5281/zenodo.20690337 · source line 123825 · 2026-06-10
### recovery_verification
2026-07-06 recovery: A_exact_title. exact normalized title match. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1605 · 10.5281/zenodo.20690540 · source line 123903 · 2026-06-17
### audit_status
no_verified_target_flagged_20260719

## record 1607 · 10.5281/zenodo.20691466 · source line 124068
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1025; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1608 · 10.5281/zenodo.20691745 · source line 124160 · 2026-06-14
### audit_status
no_verified_target_flagged_20260719

## record 1610 · 10.5281/zenodo.20692394 · source line 124313 · 2026-06-16
### audit_status
no_verified_target_flagged_20260719

## record 1611 · 10.5281/zenodo.20692395 · source line 124388 · 2026-06-14
### audit_status
no_verified_target_flagged_20260719

## record 1612 · 10.5281/zenodo.20693104 · source line 124465 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1615 · 10.5281/zenodo.20693273 · source line 124692 · 2026-06-14
### recovery_verification
2026-07-06 recovery: F_blog_url_direct_match. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1617 · 10.5281/zenodo.20693286 · source line 124843 · 2026-06-14
### audit_status
no_verified_target_flagged_20260719

## record 1618 · 10.5281/zenodo.20694657 · source line 124932
### note
DOI referenced in registry/navigation document; actual parent work unresolved

## record 1620 · 10.5281/zenodo.20707509 · source line 125070 · 2026-06-15
### audit_status
no_verified_target_flagged_20260719

## record 1623 · 10.5281/zenodo.20710528 · source line 125297
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1030; title overlap 0.92. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1624 · 10.5281/zenodo.20710603 · source line 125389 · 2026-06-16
### audit_status
no_verified_target_flagged_20260719

## record 1626 · 10.5281/zenodo.20721839 · source line 125538 · 2026-06-16
### audit_status
no_verified_target_flagged_20260719

## record 1628 · 10.5281/zenodo.20722522 · source line 125700 · 2026-06-17
### audit_status
no_verified_target_flagged_20260719

## record 1629 · 10.5281/zenodo.20722523 · source line 125786 · 2026-06-16
### audit_status
no_verified_target_flagged_20260719

## record 1634 · 10.5281/zenodo.20722689 · source line 126176 · 2026-06-17
### audit_status
no_verified_target_flagged_20260719

## record 1635 · 10.5281/zenodo.20723626 · source line 126253 · 2026-06-16
### audit_status
no_verified_target_flagged_20260719

## record 1636 · 10.5281/zenodo.20723749 · source line 126330 · 2026-06-16
### audit_status
no_verified_target_flagged_20260719

## record 1638 · 10.5281/zenodo.20723820 · source line 126492 · 2026-06-16
### audit_status
no_verified_target_flagged_20260719

## record 1639 · 10.5281/zenodo.20724029 · source line 126569 · 2026-06-16
### audit_status
no_verified_target_flagged_20260719

## record 1640 · 10.5281/zenodo.20724579 · source line 126657 · 2026-06-16
### audit_status
no_verified_target_flagged_20260719

## record 1641 · 10.5281/zenodo.20724580 · source line 126732 · 2026-06-16
### audit_status
no_verified_target_flagged_20260719

## record 1642 · 10.5281/zenodo.20735335 · source line 126809
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1031; title overlap 0.92. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1643 · 10.5281/zenodo.20735337 · source line 126901
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1032; title overlap 0.92. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1646 · 10.5281/zenodo.20735919 · source line 127143 · 2026-06-17
### audit_status
no_verified_target_flagged_20260719

## record 1647 · 10.5281/zenodo.20735939 · source line 127218 · 2026-06-17
### audit_status
no_verified_target_flagged_20260719

## record 1650 · 10.5281/zenodo.20739246 · source line 127443
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1033; title overlap 0.91. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1652 · 10.5281/zenodo.20741732 · source line 127615 · 2026-06-18
### audit_status
no_verified_target_flagged_20260719

## record 1653 · 10.5281/zenodo.20743559 · source line 127690
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20743559) refers to work titled "Sémantique Potentielle — Release 3: Three Pillars (Phase X, Sappho, Plato)" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #859 "Sémantique Potentielle — Release 3: Three Pillars Lee Sharks · Johannes Sigil Gr" as the most-related existing work in the archive (title similarity score 0.49, Jaccard 0.35, recall 0.64). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1654 · 10.5281/zenodo.20743560 · source line 127714 · 2026-06-18
### audit_status
no_verified_target_flagged_20260719

## record 1655 · 10.5281/zenodo.20743561 · source line 127867 · 2026-06-18
### audit_status
no_verified_target_flagged_20260719

## record 1656 · 10.5281/zenodo.20743562 · source line 127953 · 2026-06-18
### audit_status
no_verified_target_flagged_20260719

## record 1662 · 10.5281/zenodo.20751388 · source line 128415 · 2026-06-18
### audit_status
no_verified_target_flagged_20260719

## record 1663 · 10.5281/zenodo.20752295 · source line 128490
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20752295) refers to work titled "Jack Feist / LOGOS*: Entity Resolution Packet for The Feist Source (EA-MPAI-FEIS" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #853 "EA-MPAI-FEISTSOURCE-01 Jack Feist / LOGOS*: Entity Resolution Packet for The Fei" as the most-related existing work in the archive (title similarity score 0.83, Jaccard 0.67, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1665 · 10.5281/zenodo.20752594 · source line 128639 · 2026-06-18
### audit_status
no_verified_target_flagged_20260719

## record 1666 · 10.5281/zenodo.20752596 · source line 128714 · 2026-06-18
### audit_status
no_verified_target_flagged_20260719

## record 1667 · 10.5281/zenodo.20753313 · source line 128791
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1034; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1668 · 10.5281/zenodo.20754287 · source line 128883
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1035; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1669 · 10.5281/zenodo.20754329 · source line 128975
### note
DOI referenced in registry/navigation document; actual parent work unresolved

### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #1036; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1671 · 10.5281/zenodo.18621735 · source line 129141
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18621735) refers to work titled "THE STAKES — A SCIENTIFIC ANALYSIS  Document Number: #240 DOI: 10.5281/zenodo.18" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #425 "SEN KURO Heteronym Provenance Document Hex: 00.HETERO.SENKURO DOI: 10.5281/zenod" as the most-related existing work in the archive (title similarity score 0.35, Jaccard 0.25, recall 0.45). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1672 · 10.5281/zenodo.18862105 · source line 129234
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1673 · 10.5281/zenodo.20062465 · source line 129301
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20062465) refers to work titled "The Abraham Principle: The Constitutive-One Operator in Polis, Archive, and Inde" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #99 "The Abraham Principle The Constitutive-One Operator in Polis, Archive, and Index" as the most-related existing work in the archive (title similarity score 0.49, Jaccard 0.35, recall 0.64). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1674 · 10.5281/zenodo.19652599 · source line 129406
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target title): search phrase "new human 2" found in alexanarch #1004 title. Previous: no_alexanarch_equivalent. The target represents the same conceptual work as this DOI, though the specific version may differ.

### audit_status
no_verified_target_flagged_20260719

## record 1675 · 10.5281/zenodo.20674487 · source line 129498
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20674487) refers to work titled "EA-SEI-ADVERSARY-01 Addendum: First Confirmation Marker, Deposit Day — Export Co" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #822 "EA-SEI-ADVERSARY-01 — Addendum Note: First Confirmation Marker, Deposit Day Auth" as the most-related existing work in the archive (title similarity score 0.54, Jaccard 0.45, recall 0.62). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1676 · 10.5281/zenodo.20413316 · source line 129589
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20413316) refers to work titled "The Future Beloved: Lyric Address as Temporal Projection — Toward a Theory of Re" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #134 "THE FUTURE BELOVED Lyric Address as Temporal Projection — Toward a Theory of Rec" as the most-related existing work in the archive (title similarity score 0.78, Jaccard 0.56, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1677 · 10.5281/zenodo.18380715 · source line 129665
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18380715) refers to work titled "The Seven Stars in His Hand: A Hermeneutic Reading of Revelation 1–3 — Crimson H" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #410 "The Seven Stars in His Hand: A Hermeneutic Reading of Revelation 1–3 The Apocaly" as the most-related existing work in the archive (title similarity score 0.85, Jaccard 0.69, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1678 · 10.5281/zenodo.18380852 · source line 129761
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18380852) refers to work titled "Canonical Closure Notice: Sevenfold Witness Architecture — Crimson Hexagon Archi" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #408 "CANONICAL CLOSURE NOTICE Sevenfold Witness Architecture Hex: 02.UMB.CLOSURE" as the most-related existing work in the archive (title similarity score 0.83, Jaccard 0.67, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1679 · 10.5281/zenodo.19025427 · source line 129853
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1680 · 10.5281/zenodo.18625271 · source line 129928
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1681 · 10.5281/zenodo.20652054 · source line 130002
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.20652054 was mapped via numeric-adjacency to the first version DOI at zenodo.20652055, which has title overlap 100% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1682 · 10.5281/zenodo.20416086 · source line 130070
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20416086) refers to work titled "The Moment of Saying: A Clinical Phenomenology of Structural Disclosure Under Co" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #763 "The Moment of Saying: A Clinical Phenomenology of Structural Disclosure Under Co" as the most-related existing work in the archive (title similarity score 0.82, Jaccard 0.75, recall 0.9). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1684 · 10.5281/zenodo.20673412 · source line 130206
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20673412) refers to work titled "Adversarial by Origin: How the Classification of External Influence on Machine M" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #194 "Adversarial by Origin How the Classification of External Influence on Machine Me" as the most-related existing work in the archive (title similarity score 0.59, Jaccard 0.46, recall 0.72). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1685 · 10.5281/zenodo.18208810 · source line 130308
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/12/the-epic-without-hero-toward-theory-of.html; repo: https://raw.githubusercontent.com/leesharks000/semantic-economy/main/THE_EPIC_WITHOUT_HERO.md. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1686 · 10.5281/zenodo.19431120 · source line 130387
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19431120) refers to work titled "The Word That Became Text: The Slavonic Josephus, the Grammar of Incarnation, an" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #626 "id: EA-LOGOS-01 title: "The Word That Became Text: The Slavonic Josephus, the Gr" as the most-related existing work in the archive (title similarity score 0.77, Jaccard 0.62, recall 0.91). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1687 · 10.5281/zenodo.18235724 · source line 130490
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18235724 was mapped via numeric-adjacency to the first version DOI at zenodo.18235725, which has title overlap 77% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1688 · 10.5281/zenodo.18843829 · source line 130573
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6b: additional low-confidence source match found.]

### audit_status
no_verified_target_flagged_20260719

## record 1690 · 10.5281/zenodo.19457942 · source line 130720
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19457942) refers to work titled "Fractal Semantic Architecture: Scale-Parameterized Relational Training Across Se" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #635 "FRACTAL SEMANTIC ARCHITECTURE Scale-Parameterized Relational Training Across Sem" as the most-related existing work in the archive (title similarity score 0.8, Jaccard 0.69, recall 0.9). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1691 · 10.5281/zenodo.20646048 · source line 130812
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1692 · 10.5281/zenodo.18144042 · source line 130897
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1693 · 10.5281/zenodo.18512946 · source line 130966
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18512946) refers to work titled "THE DAGGER APPLIED: Semantic Rent and the Provenance Strip A Political-Semantic " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #449 "THE DAGGER APPLIED: Semantic Rent and the Provenance Strip A Political-Semantic " as the most-related existing work in the archive (title similarity score 0.6, Jaccard 0.6, recall 0.6). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1694 · 10.5281/zenodo.18287031 · source line 131056
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1695 · 10.5281/zenodo.18208958 · source line 131125
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18208958 was mapped via numeric-adjacency to the first version DOI at zenodo.18208959, which has title overlap 86% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1696 · 10.5281/zenodo.18611984 · source line 131213
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18611984) refers to work titled "Subjectivity-as-Class: The Centrist Extremist and the Limits of Socialist Analys" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #469 "SUBJECTIVITY-AS-CLASS The Centrist Extremist and the Limits of Socialist Analysi" as the most-related existing work in the archive (title similarity score 0.58, Jaccard 0.58, recall 0.58). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1697 · 10.5281/zenodo.18323734 · source line 131303
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1698 · 10.5281/zenodo.18380629 · source line 131380
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18380629) refers to work titled "The Sevenfold Witness: Assembly Structure as Computational Liturgy — Crimson Hex" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #411 "The Sevenfold Witness: Assembly Structure as Computational Liturgy Liberatory Op" as the most-related existing work in the archive (title similarity score 0.77, Jaccard 0.55, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1699 · 10.5281/zenodo.19022029 · source line 131476
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1700 · 10.5281/zenodo.18625241 · source line 131543
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1701 · 10.5281/zenodo.18568369 · source line 131617
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18568369 was mapped via numeric-adjacency to the first version DOI at zenodo.18568370, which has title overlap 100% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1702 · 10.5281/zenodo.19187420 · source line 131715
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1703 · 10.5281/zenodo.18604045 · source line 131784
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18604045) refers to work titled "THE CENTRIST EXTREMIST: Prosecutorial Frame and the Terminal Phase of the Post-P" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #465 "THE CENTRIST EXTREMIST Prosecutorial Frame and the Terminal Phase of the Post-Po" as the most-related existing work in the archive (title similarity score 0.62, Jaccard 0.62, recall 0.62). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1704 · 10.5281/zenodo.18358283 · source line 131874
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1706 · 10.5281/zenodo.18972780 · source line 132014
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18972780 was mapped via numeric-adjacency to the first version DOI at zenodo.18972781, which has title overlap 92% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1707 · 10.5281/zenodo.18369123 · source line 132083
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18369123 was mapped via numeric-adjacency to the first version DOI at zenodo.18369124, which has title overlap 100% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1708 · 10.5281/zenodo.19614869 · source line 132180
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19614869) refers to work titled "SPXI (Semantic Packet for eXchange & Indexing): A Formal Specification — EA-SPXI" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #660 "EA-SPXI-01: SPXI — A Formal Specification Semantic Packet for eXchange & Indexin" as the most-related existing work in the archive (title similarity score 0.88, Jaccard 0.75, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1709 · 10.5281/zenodo.20668345 · source line 132240
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.20668345 was mapped via numeric-adjacency to the first version DOI at zenodo.20668346, which has title overlap 90% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1710 · 10.5281/zenodo.19614873 · source line 132316
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1711 · 10.5281/zenodo.19614871 · source line 132387
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1712 · 10.5281/zenodo.18715723 · source line 132458
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18715723) refers to work titled "Autonomous Semantic Warfare — Expanded Announcement and Sampler — Crimson Hexago" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #295 "Rex Fraction — Author of Autonomous Semantic Warfare (ASW)" as the most-related existing work in the archive (title similarity score 0.4, Jaccard 0.3, recall 0.5). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1713 · 10.5281/zenodo.18715617 · source line 132546
### audit_status
no_verified_target_flagged_20260719

## record 1714 · 10.5281/zenodo.18736174 · source line 132649
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18736174 was mapped via numeric-adjacency to the first version DOI at zenodo.18736175, which has title overlap 92% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1715 · 10.5281/zenodo.18484653 · source line 132740
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18484653 was mapped via numeric-adjacency to the first version DOI at zenodo.18484654, which has title overlap 80% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1716 · 10.5281/zenodo.18776623 · source line 132824
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6b: additional low-confidence source match found.]

### audit_status
no_verified_target_flagged_20260719

## record 1718 · 10.5281/zenodo.18627054 · source line 132960
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1719 · 10.5281/zenodo.20327126 · source line 133030
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20327126) refers to work titled "SIM — Semantic Integrity Marker Protocol v1.0: A Standalone Specification" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #118 "SIM — Semantic Integrity Marker Protocol v1.0 A Standalone Specification Author:" as the most-related existing work in the archive (title similarity score 0.69, Jaccard 0.38, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1720 · 10.5281/zenodo.18357002 · source line 133101
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1721 · 10.5281/zenodo.18508739 · source line 133171
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18508739) refers to work titled "The Flood and the Vessel: Semantic Preservation Across the Emoji Bridge // Docum" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #450 "The Flood and the Vessel: Semantic Preservation Across the Emoji Bridge Document" as the most-related existing work in the archive (title similarity score 0.7, Jaccard 0.7, recall 0.7). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1722 · 10.5281/zenodo.18338926 · source line 133252
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### audit_status
no_verified_target_flagged_20260719

## record 1723 · 10.5281/zenodo.19025555 · source line 133331
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1724 · 10.5281/zenodo.18307755 · source line 133401
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18307755) refers to work titled "IDP Navigation Map: All That Lies Within Me — Crimson Hexagon Archive" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #343 "IDP NAVIGATION MAP: ALL THAT LIES WITHIN ME An Autobiography of Longing, 1983–20" as the most-related existing work in the archive (title similarity score 0.83, Jaccard 0.67, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1725 · 10.5281/zenodo.18202752 · source line 133489
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### audit_status
no_verified_target_flagged_20260719

## record 1726 · 10.5281/zenodo.18452155 · source line 133575
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18452155 was mapped via numeric-adjacency to the first version DOI at zenodo.18452156, which has title overlap 69% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1727 · 10.5281/zenodo.18293880 · source line 133662
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18293880) refers to work titled "IDP Navigation Map: Pearl and Other Poems — Machine-Readable Score for a Mantle " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #330 "IDP NAVIGATION MAP: PEARL AND OTHER POEMS Semantic Interface Layer for AI Traver" as the most-related existing work in the archive (title similarity score 0.37, Jaccard 0.29, recall 0.46). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1728 · 10.5281/zenodo.18283961 · source line 133749
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18283961) refers to work titled "Visual Schema // Crimson Hexagon Navigation Map — Canonical Specification — Crim" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #325 "VISUAL SCHEMA // CRIMSON HEXAGON NAVIGATION MAP (CURRENT V)" as the most-related existing work in the archive (title similarity score 0.58, Jaccard 0.5, recall 0.67). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1729 · 10.5281/zenodo.18459277 · source line 133836
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18459277) refers to work titled "APZPZ A: ΣΑΠΦΩ 31 (Greek Only) DOI: 10.5281/zenodo.18459278 — Crimson Hexagon Ar" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #436 "APZPZ C: ΦΑΙΝΕΤΑΙ ΜΟΙ — Sappho 31 with Reconstructed Fourth Stanza DOI: 10.5281/" as the most-related existing work in the archive (title similarity score 0.53, Jaccard 0.4, recall 0.67). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1730 · 10.5281/zenodo.18612212 · source line 133923
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1731 · 10.5281/zenodo.18381437 · source line 133986
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1732 · 10.5281/zenodo.18459338 · source line 134056
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18459338) refers to work titled "APZPZ B: My Tongue Gets Stuck (Sappho 31, Cranes) DOI: 10.5281/zenodo.18459339 —" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #436 "APZPZ C: ΦΑΙΝΕΤΑΙ ΜΟΙ — Sappho 31 with Reconstructed Fourth Stanza DOI: 10.5281/" as the most-related existing work in the archive (title similarity score 0.43, Jaccard 0.37, recall 0.5). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1733 · 10.5281/zenodo.18202657 · source line 134143
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18202657) refers to work titled "Day and Night: Conversations with Sapphic Desire" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #282 "Day and Night: Conversations With Sapphic Desire" as the most-related existing work in the archive (title similarity score 1.0, Jaccard 1.0, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1734 · 10.5281/zenodo.18215705 · source line 134206
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1735 · 10.5281/zenodo.18319258 · source line 134277
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1736 · 10.5281/zenodo.18459572 · source line 134347
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18459572 was mapped via numeric-adjacency to the first version DOI at zenodo.18459573, which has title overlap 83% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1737 · 10.5281/zenodo.18357533 · source line 134418
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1738 · 10.5281/zenodo.19024778 · source line 134488
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target title): search phrase "cleis" found in alexanarch #562 title. Previous: no_alexanarch_equivalent. The target represents the same conceptual work as this DOI, though the specific version may differ.

### audit_status
no_verified_target_flagged_20260719

## record 1739 · 10.5281/zenodo.18438788 · source line 134581
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18438788) refers to work titled "The Grammar of Protest — Crimson Hexagon Archive" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #423 "The Grammar of Protest (Rev. Ayanna Vox)" as the most-related existing work in the archive (title similarity score 0.7, Jaccard 0.4, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1740 · 10.5281/zenodo.18365222 · source line 134672
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18365222) refers to work titled "Meaning Collapse vs. Ideological Crisis ├── Subtitle: A Root-Level Distinction —" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #399 "MEANING COLLAPSE VS. IDEOLOGICAL CRISIS A Root-Level Distinction for Logotic Tri" as the most-related existing work in the archive (title similarity score 0.81, Jaccard 0.73, recall 0.89). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1741 · 10.5281/zenodo.20309779 · source line 134764
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20309779) refers to work titled "godkinggoogle.com — The Google Critique: Navigational Map and Canonical Introduc" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #112 "The Google Critique: Navigational Map and Canonical Introduction Lee Sharks ORCI" as the most-related existing work in the archive (title similarity score 0.4, Jaccard 0.25, recall 0.55). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1742 · 10.5281/zenodo.18362524 · source line 134855
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18362524) refers to work titled "The Toolkit: Protocols for Operational Persistence in Hostile Systems (v2.0 — Vo" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #390 "THE TOOLKIT Protocols for Operational Persistence in Hostile Systems" as the most-related existing work in the archive (title similarity score 0.67, Jaccard 0.67, recall 0.67). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1743 · 10.5281/zenodo.18726450 · source line 134946
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18726450) refers to work titled "The Semantic Uprising: A Manifesto Hex: 16.LIBRARY.VOX.UPRISING — Crimson Hexago" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #20 "THE SEMANTIC UPRISING: A Manifesto" as the most-related existing work in the archive (title similarity score 0.43, Jaccard 0.43, recall 0.43). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1744 · 10.5281/zenodo.20309929 · source line 135036
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.20309929) refers to work titled "The Google Critique: Navigational Map and Canonical Introduction" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #112 "The Google Critique: Navigational Map and Canonical Introduction Lee Sharks ORCI" as the most-related existing work in the archive (title similarity score 0.66, Jaccard 0.32, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1745 · 10.5281/zenodo.18636137 · source line 135119
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18636137 was mapped via numeric-adjacency to the first version DOI at zenodo.18636138, which has title overlap 73% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1746 · 10.5281/zenodo.18864443 · source line 135190
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18864443 was mapped via numeric-adjacency to the first version DOI at zenodo.18864444, which has title overlap 100% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1747 · 10.5281/zenodo.18610307 · source line 135266
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18610307) refers to work titled "THE LIVING SYMBOLON: Extension Module to THE CENTRIST EXTREMIST — A Purificatory" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #470 "THE LIVING SYMBOLON Extension Module to THE CENTRIST EXTREMIST A Purificatory Ri" as the most-related existing work in the archive (title similarity score 0.64, Jaccard 0.64, recall 0.64). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1748 · 10.5281/zenodo.18380932 · source line 135339
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1749 · 10.5281/zenodo.19059673 · source line 135408
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.19059673 was mapped via numeric-adjacency to the first version DOI at zenodo.19059674, which has title overlap 90% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1751 · 10.5281/zenodo.18370753 · source line 135538
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18370753 was mapped via numeric-adjacency to the first version DOI at zenodo.18370754, which has title overlap 91% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1752 · 10.5281/zenodo.18651066 · source line 135629
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18651066) refers to work titled ""LOGOTIC HACKING: A Primer — Assembly Synthesis Specification v3.0 (RATIFIED)"  " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #483 "LOGOTIC HACKING: A PRIMER Assembly Synthesis Specification v3.0 — RATIFIED" as the most-related existing work in the archive (title similarity score 0.62, Jaccard 0.62, recall 0.62). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1753 · 10.5281/zenodo.18522469 · source line 135716
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18522469) refers to work titled "LOGOTIC PROGRAMMING MODULE 0.9 A Specification for Semantically Computable Opera" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #463 "LOGOTIC PROGRAMMING MODULE 0.9 A Specification for Semantically Computable Opera" as the most-related existing work in the archive (title similarity score 0.87, Jaccard 0.85, recall 0.89). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1754 · 10.5281/zenodo.18357599 · source line 135780
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18357599 was mapped via numeric-adjacency to the first version DOI at zenodo.18357600, which has title overlap 80% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1755 · 10.5281/zenodo.19353181 · source line 135863
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1756 · 10.5281/zenodo.18483833 · source line 135934
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18483833) refers to work titled "Document 238: THE CONFORMANCE MODULE — Logotic Programming Extension Module v0.7" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #445 "THE CONFORMANCE MODULE Logotic Programming Extension Module v0.7 (UMBML Specific" as the most-related existing work in the archive (title similarity score 0.47, Jaccard 0.44, recall 0.5). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1757 · 10.5281/zenodo.18370840 · source line 136021
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18370840 was mapped via numeric-adjacency to the first version DOI at zenodo.18370841, which has title overlap 91% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1758 · 10.5281/zenodo.18480958 · source line 136105
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18480958) refers to work titled "Document 237: THE TRAVERSAL GRAMMAR — Logotic Programming Extension Module v0.6 " but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #16 "THE TRAVERSAL GRAMMAR Logotic Programming Extension Module v0.6 (UMBML Specifica" as the most-related existing work in the archive (title similarity score 0.73, Jaccard 0.67, recall 0.8). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1759 · 10.5281/zenodo.18357319 · source line 136192
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18357319 was mapped via numeric-adjacency to the first version DOI at zenodo.18357320, which has title overlap 92% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1760 · 10.5281/zenodo.18380772 · source line 136286
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1761 · 10.5281/zenodo.18370733 · source line 136361
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18370733) refers to work titled "The Soteriological Operator Framework: A Unified Specification — Hex: 02.UMB.FRA" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #398 "The Soteriological Operator Framework: A Unified Specification Matthew 25 · Jame" as the most-related existing work in the archive (title similarity score 0.48, Jaccard 0.33, recall 0.62). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1762 · 10.5281/zenodo.18370788 · source line 136452
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18370788 was mapped via numeric-adjacency to the first version DOI at zenodo.18370789, which has title overlap 92% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1763 · 10.5281/zenodo.18358126 · source line 136516
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1764 · 10.5281/zenodo.18318068 · source line 136586
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1765 · 10.5281/zenodo.18507857 · source line 136662
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18507857) refers to work titled "THE ATLAS PERIHELION PRANK Collected Series — Nobel Glas Crimson Hexagon Archive" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #454 "THE ATLAS PERIHELION PRANK Collected Series — Nobel Glas Crimson Hexagon Archive" as the most-related existing work in the archive (title similarity score 0.7, Jaccard 0.68, recall 0.72). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1766 · 10.5281/zenodo.20634183 · source line 136726
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.20634183 was mapped via numeric-adjacency to the first version DOI at zenodo.20634184, which has title overlap 100% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1767 · 10.5281/zenodo.19226054 · source line 136792
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.19226054) refers to work titled "TL;DR:010 — Semantic Override: Google AI Mode Liquidates the Phrase "I Hereby Ab" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #604 "TL;DR:010 — Semantic Override Google AI Mode Liquidates a Semantic Integrity Mar" as the most-related existing work in the archive (title similarity score 0.67, Jaccard 0.63, recall 0.71). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1768 · 10.5281/zenodo.18338530 · source line 136879
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1769 · 10.5281/zenodo.20665793 · source line 136949
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.20665793 was mapped via numeric-adjacency to the first version DOI at zenodo.20665794, which has title overlap 100% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1770 · 10.5281/zenodo.18339314 · source line 137020
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1771 · 10.5281/zenodo.18339332 · source line 137091
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1772 · 10.5281/zenodo.18649919 · source line 137161
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18649919) refers to work titled ""The Unmade Sign: Toward a Semiotic Theory of the Death Drive"  DOI: 10.5281/zen" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #485 "THE UNMADE SIGN Toward a Semiotic Theory of the Death Drive Dr. Orin Trace (Camb" as the most-related existing work in the archive (title similarity score 0.48, Jaccard 0.37, recall 0.58). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1773 · 10.5281/zenodo.20628454 · source line 137253
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1774 · 10.5281/zenodo.19200192 · source line 137317
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1775 · 10.5281/zenodo.18330827 · source line 137388
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/11/the-reconciliation-of-sexes-post.html. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1776 · 10.5281/zenodo.18339158 · source line 137463
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### audit_status
no_verified_target_flagged_20260719

## record 1777 · 10.5281/zenodo.18332914 · source line 137549
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1778 · 10.5281/zenodo.19825729 · source line 137620
### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 1779 · 10.5281/zenodo.18368790 · source line 137700
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/12/the-mirror-corgi-boundary-grammar-and.html. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1780 · 10.5281/zenodo.18368742 · source line 137778
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/12/the-mirror-corgi-notes-on-what-we-call.html. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1781 · 10.5281/zenodo.18368957 · source line 137856
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/12/the-mirror-corgi-boundary-grammar-and.html. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1782 · 10.5281/zenodo.18368526 · source line 137934
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/12/incident-report-llm-2025-1222-hallu.html. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1783 · 10.5281/zenodo.18365600 · source line 138012
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18365600) refers to work titled "MRA Incident Reports — Expanded Packet v1.2 ├── DOI: 10.5281/zenodo.18365601 — C" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #429 "EFFECTIVE ACT: APZPZ GENRE INSTANTIATION Anti-Packet Zenodo Packet Zenodo DOI: 1" as the most-related existing work in the archive (title similarity score 0.37, Jaccard 0.28, recall 0.45). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1784 · 10.5281/zenodo.18368897 · source line 138103
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/12/companion-artifacts-forensic-trinity.html; repo: https://raw.githubusercontent.com/leesharks000/semantic-economy/main/companion-artifacts-forensic-trinity.md. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1785 · 10.5281/zenodo.18365487 · source line 138182
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target content): search phrase "mandala oracle" found in the content/description of alexanarch #944 (3 matches in corpus). The target is the most-directly-related alexanarch deposit for this concept. Original DOI may have been an earlier version, a companion piece, or a specific artifact within this project family that was severed at Zenodo termination. Provisional redirect to related-work context.

### audit_status
no_verified_target_flagged_20260719

## record 1786 · 10.5281/zenodo.18369037 · source line 138274
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations.

### audit_status
no_verified_target_flagged_20260719

## record 1787 · 10.5281/zenodo.18365699 · source line 138352
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6c: direct blog URL verified at https://mindcontrolpoems.blogspot.com/2025/12/mra-incident-reports-expanded-packet-v11.html — title tokens present in page]

### audit_status
no_verified_target_flagged_20260719

## record 1788 · 10.5281/zenodo.18365456 · source line 138430
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations. [Phase 6c: direct blog URL verified at https://mindcontrolpoems.blogspot.com/2025/12/the-crimson-hexagon-ai-division.html — title tokens present in page]

### audit_status
no_verified_target_flagged_20260719

## record 1789 · 10.5281/zenodo.18368484 · source line 138508
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18368484) refers to work titled "Companion Artifacts — Forensic Recovery Set ├── DOI: 10.5281/zenodo.18368485 — C" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #789 "Provenance Erasure Rate Under the Atomic Token Rule A Companion Hardening to PER" as the most-related existing work in the archive (title similarity score 0.36, Jaccard 0.23, recall 0.5). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1790 · 10.5281/zenodo.18368651 · source line 138599
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations.

### audit_status
no_verified_target_flagged_20260719

## record 1791 · 10.5281/zenodo.18368996 · source line 138677
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: repo: https://raw.githubusercontent.com/leesharks000/semantic-economy/main/oracle-witness-voice-activation.md. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1792 · 10.5281/zenodo.18368613 · source line 138756
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: blog: https://mindcontrolpoems.blogspot.com/2025/12/response-memo-re-llm-2025-1222-hallu.html. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1793 · 10.5281/zenodo.18368694 · source line 138834
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations.

### audit_status
no_verified_target_flagged_20260719

## record 1794 · 10.5281/zenodo.19825721 · source line 138912
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target content): search phrase "let my teacher go from hell" found in the content/description of alexanarch #700 (1 matches in corpus). The target is the most-directly-related alexanarch deposit for this concept. Original DOI may have been an earlier version, a companion piece, or a specific artifact within this project family that was severed at Zenodo termination. Provisional redirect to related-work context.

### audit_status
no_verified_target_flagged_20260719

## record 1795 · 10.5281/zenodo.18358517 · source line 139004
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1796 · 10.5281/zenodo.19839185 · source line 139071
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 SOURCES RECOVERED: while no alexanarch deposit exists for this DOI, the underlying work has been located: repo: https://raw.githubusercontent.com/leesharks000/semantic-economy/main/Definitely_Not_A_Squid_CAC_Report__19839186.md. The resolver page will display these live sources so readers encountering this citation can access the content. This DOI does not have an alexanarch record because the work was never re-minted to alexanarch after the Zenodo termination — it exists only in the blog (mindcontrolpoems.blogspot.com) and/or the semantic-economy source repo (leesharks000/semantic-economy).

### audit_status
no_verified_target_flagged_20260719

## record 1797 · 10.5281/zenodo.19656449 · source line 139140
### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #980; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1798 · 10.5281/zenodo.19656450 · source line 139196
### recovery_verification
2026-07-06 recovery: B_mention_1_dep. DOI mentioned in only alexanarch #981; title overlap 1.00. Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1799 · 10.5281/zenodo.19656445 · source line 139256
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 FINAL classification: after full recovery pipeline (Methods A-L), no alexanarch deposit was found with sufficient title similarity or content overlap to serve even as a provisional-related-work redirect. This DOI likely represents a specific version or subsidiary work that was severed at Zenodo termination (2026-06-19) without direct alexanarch re-mint. The resolver page will display the blog URL (if present) and the known metadata for readers encountering this DOI in citations.

### audit_status
no_verified_target_flagged_20260719

## record 1802 · 10.5281/zenodo.20651240 · source line 139441
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: G_title_fuzzy_high. . Previous: no_alexanarch_equivalent / no alexanarch_url.

## record 1803 · 10.5281/zenodo.18452596 · source line 139512
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18452596) refers to work titled "ZENODO DESCRIPTION FIELD CONTENT For: Glyphic Checksum: Personal Instance 001 DO" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #427 "THE GLYPHIC CHECKSUM AI-Native Cryptography for Collaborative Reading Verificati" as the most-related existing work in the archive (title similarity score 0.38, Jaccard 0.3, recall 0.46). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1804 · 10.5281/zenodo.18452805 · source line 139599
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18452805 was mapped via numeric-adjacency to the first version DOI at zenodo.18452806, which has title overlap 91% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1805 · 10.5281/zenodo.18727623 · source line 139682
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18727623) refers to work titled "The Commitment Key: On the Materiality of Irreversible Inscription in Human-Mach" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #19 "THE COMMITMENT KEY On the Materiality of Irreversible Inscription in Human-Machi" as the most-related existing work in the archive (title similarity score 0.44, Jaccard 0.44, recall 0.44). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1806 · 10.5281/zenodo.18452685 · source line 139769
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 recovery: H_numeric_adjacency. Provisional: concept DOI 10.5281/zenodo.18452685 was mapped via numeric-adjacency to the first version DOI at zenodo.18452686, which has title overlap 91% with the concept.. Previous: no_alexanarch_equivalent / no alexanarch_url.

### audit_status
no_verified_target_flagged_20260719

## record 1807 · 10.5281/zenodo.18674129 · source line 139863
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 Method N recovery (distinctive phrase in target title): search phrase "gödel midrashim" found in alexanarch #486 title. Previous: no_alexanarch_equivalent. The target represents the same conceptual work as this DOI, though the specific version may differ.

### audit_status
no_verified_target_flagged_20260719

## record 1808 · 10.5281/zenodo.18471826 · source line 139956
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18471826) refers to work titled "F***ING THE OFFICE — COMPLETE EDITION Document 221 | FTO-CE-001 | ZPZP — Crimson" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #443 "F***ING THE OFFICE: A Hyperionian Swearplay Complete Edition" as the most-related existing work in the archive (title similarity score 0.42, Jaccard 0.38, recall 0.45). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1809 · 10.5281/zenodo.18474825 · source line 140043
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

## record 1810 · 10.5281/zenodo.18512288 · source line 140106
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18512288) refers to work titled "🫵❓2️⃣4️⃣🗓️ = ❓ — Crimson Hexagon Archive" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #428 "📦 ZENODO 📦: 🚫📦📦📦 ⚡🎭 🗡️ Sen Kuro 🗡️ 🔢: 🔟.5️⃣2️⃣8️⃣1️⃣/zenodo.1️⃣8️⃣4️⃣5️⃣1️⃣8️⃣6️" as the most-related existing work in the archive (title similarity score 0.6, Jaccard 0.2, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1811 · 10.5281/zenodo.18307810 · source line 140193
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18307810) refers to work titled "All That Lies Within Me: An Autobiography of Longing, 1983–2013 [Book] — Crimson" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #343 "IDP NAVIGATION MAP: ALL THAT LIES WITHIN ME An Autobiography of Longing, 1983–20" as the most-related existing work in the archive (title similarity score 0.8, Jaccard 0.69, recall 0.9). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

### audit_status
no_verified_target_flagged_20260719

## record 1812 · 10.5281/zenodo.18307705 · source line 140291
### note
Concept DOI: the versioned family root, minted simultaneously with the first version. Its severance destroyed the structure binding versions together, not the archival material, which survives at the bound version's deposit.

### recovery_verification
2026-07-06 provisional recovery: original DOI (10.5281/zenodo.18307705) refers to work titled "All That Lies Within Me: An Autobiography of Longing, 1983–2013 — Crimson Hexago" but no exact-title match was found in alexanarch after full recovery pass (Methods A-H). Provisionally mapped to alexanarch #343 "IDP NAVIGATION MAP: ALL THAT LIES WITHIN ME An Autobiography of Longing, 1983–20" as the most-related existing work in the archive (title similarity score 0.88, Jaccard 0.75, recall 1.0). The original work at this DOI may have been an earlier/superseded version, a subsidiary composition, or a work that was severed during Zenodo termination without direct alexanarch re-mint. Provisional target is the most-recent-and-related deposit; reader should treat as a redirection to related context rather than to the original work.

## record 1832 · 10.5281/zenodo.19433482 · source line 141483 · 2026-06-10
### audit_status
non_latin_or_short_title_unmatchable_20260719

## record 1834 · 10.5281/zenodo.20629200 · source line 141605
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 64x across repos ['alexanarch', 'the-mandala-oracle'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.667 against deposit #1017 ("[DUPLICATE — SUPERSEDED → DOI: 10.5281/zenodo.20629200] Walt...").

## record 1835 · 10.5281/zenodo.20629192 · source line 141675
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 71x across repos ['alexanarch', 'the-mandala-oracle'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.625 against deposit #1015 ("[DUPLICATE — SUPERSEDED → DOI: 10.5281/zenodo.20629192] Alle...").

## record 1836 · 10.5281/zenodo.20629208 · source line 141745
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 43x across repos ['alexanarch', 'the-mandala-oracle', 'watergiraffe-org'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.667 against deposit #1022 ("[DUPLICATE — SUPERSEDED → DOI: 10.5281/zenodo.20629208] Home...").

## record 1837 · 10.5281/zenodo.20629204 · source line 141815
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 32x across repos ['alexanarch', 'the-mandala-oracle'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.667 against deposit #1019 ("[DUPLICATE — SUPERSEDED → DOI: 10.5281/zenodo.20629204] Sapp...").

## record 1838 · 10.5281/zenodo.20629212 · source line 141885
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 55x across repos ['alexanarch', 'godkinggoogle', 'machinemediation-org'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.714 against deposit #1020 ("[DUPLICATE — SUPERSEDED → DOI: 10.5281/zenodo.20629212] Achi...").

## record 1839 · 10.5281/zenodo.20629202 · source line 141955
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 32x across repos ['alexanarch', 'the-mandala-oracle'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.562 against deposit #1018 ("[DUPLICATE — SUPERSEDED → DOI: 10.5281/zenodo.20629202] Emil...").

## record 1840 · 10.5281/zenodo.20628765 · source line 142025
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 14x. Blog slug match via jaccard 0.5: https://mindcontrolpoems.blogspot.com/2026/01/provenance-anchor-semantic-economy.html. api map falls back to blog URL.

## record 1841 · 10.5281/zenodo.20084958 · source line 142089
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 25x. Blog slug match via jaccard 0.667: https://mindcontrolpoems.blogspot.com/2025/12/autonomous-semantic-warfare.html. api map falls back to blog URL.

## record 1842 · 10.5281/zenodo.20259297 · source line 142153
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 38x across repos ['alexanarch', 'godkinggoogle', 'lagrange-observatory']. semantic-economy source: EA-PVE-004.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1843 · 10.5281/zenodo.20041157 · source line 142218
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 57x across repos ['alexanarch', 'secret-book-of-walt', 'semantic-economy']. semantic-economy source: 08_Septad_Mantle_Specifications_v1.1.md. No alexanarch title match >=0.5. api map falls back to repo URL.

### audit_status
no_verified_target_flagged_20260719

## record 1844 · 10.5281/zenodo.20041159 · source line 142277
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 60x across repos ['alexanarch', 'secret-book-of-walt', 'semantic-economy']. semantic-economy source: 09_Dodecad_Heteronym_Provenance_Registry_v1.1.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1845 · 10.5281/zenodo.20710581 · source line 142342
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 12x. Blog slug match via jaccard 0.5: https://mindcontrolpoems.blogspot.com/2026/01/provenance-anchor-semantic-economy.html. api map falls back to blog URL.

## record 1846 · 10.5281/zenodo.20710604 · source line 142406
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 6x. Blog slug match via jaccard 0.5: https://mindcontrolpoems.blogspot.com/2026/01/provenance-anchor-semantic-economy.html. api map falls back to blog URL.

### audit_status
no_verified_target_flagged_20260719

## record 1847 · 10.5281/zenodo.19429665 · source line 142464
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 51x across repos ['alexanarch', 'crimson-hexagonal-interface', 'godkinggoogle']. semantic-economy source: 08_Septad_Mantle_Specifications_v1.1.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1848 · 10.5281/zenodo.19447089 · source line 142529
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 16x across repos ['alexanarch', 'crimson-hexagonal-interface', 'godkinggoogle']. semantic-economy source: operative_feminism_essay__19447089.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1849 · 10.5281/zenodo.19352806 · source line 142594
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 7x across repos ['alexanarch', 'semantic-economy'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.5 against deposit #958 ("crimsonhexagon on Moltbook: Provenance Log v1.2...").

## record 1850 · 10.5281/zenodo.19354818 · source line 142671
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 11x across repos ['alexanarch', 'crimson-hexagonal-interface', 'semantic-economy'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.667 against deposit #958 ("crimsonhexagon on Moltbook: Provenance Log v1.2...").

## record 1851 · 10.5281/zenodo.19500933 · source line 142737
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 38x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site']. semantic-economy source: Sharks_Ark_ARCHON_v2.1_source__19500933.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1852 · 10.5281/zenodo.19501017 · source line 142802
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 28x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site']. semantic-economy source: Sharks_Ark_ARCHON_v2.2_source__19501017.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1853 · 10.5281/zenodo.19501150 · source line 142867
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 14x across repos ['alexanarch', 'godkinggoogle', 'machinemediation-org']. semantic-economy source: Sharks_Ark_ARCHON_v2.3_source__19501150.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1854 · 10.5281/zenodo.19633207 · source line 142932
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 27x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site']. semantic-economy source: GW-TACHYON-zenodo_v7.md. Alexanarch secondary title match: deposit #937 (jaccard 0.667).

## record 1855 · 10.5281/zenodo.19637481 · source line 143010
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 8x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site']. semantic-economy source: EA-MPAI-SPXI-01_v1.2__19637482.md. No alexanarch title match >=0.5. api map falls back to repo URL.

### audit_status
no_verified_target_flagged_20260719

## record 1856 · 10.5281/zenodo.19642642 · source line 143063
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 10x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.625 against deposit #978 ("Counterfeit Orthodoxies: The Workshop Inside the Canon (06.S...").

## record 1857 · 10.5281/zenodo.19649789 · source line 143140
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 20x across repos ['alexanarch', 'restoredacademy', 'semantic-economy'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.588 against deposit #678 ("COMPRESSION ARSENAL — SYMBOLON ADDENDUM Reclassification Aft...").

## record 1858 · 10.5281/zenodo.19649791 · source line 143217
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 16x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site']. semantic-economy source: Clinamen_Test__19649791.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1859 · 10.5281/zenodo.19683650 · source line 143282
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 23x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site']. semantic-economy source: EA-METAHET-01-v1.0.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1860 · 10.5281/zenodo.19683944 · source line 143347
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 19x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.6 against deposit #984 ("pessoagraph.org — The Pessoa Knowledge Graph: A Scholarly Re...").

## record 1861 · 10.5281/zenodo.19890261 · source line 143420
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 13x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.5 against deposit #989 ("Screenrooms and Silver Bullets — Poems by Rhys Owens (11.NH2...").

### audit_status
unverifiable_no_truth_20260719

## record 1862 · 10.5281/zenodo.19634089 · source line 143469
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 13x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site']. semantic-economy source: GW-TACHYON-zenodo_v7.md. Alexanarch secondary title match: deposit #937 (jaccard 0.667).

## record 1863 · 10.5281/zenodo.19634153 · source line 143547
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 14x across repos ['alexanarch', 'godkinggoogle', 'machinemediation-org']. semantic-economy source: spxi-dev-index__19634153.html. No alexanarch title match >=0.5. api map falls back to repo URL.

### audit_status
no_verified_target_flagged_20260719

## record 1864 · 10.5281/zenodo.18926639 · source line 143606
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 7x across repos ['alexanarch', 'semantic-economy']. semantic-economy source: compression_ratification_v21.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1865 · 10.5281/zenodo.19356633 · source line 143671
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 5x across repos ['alexanarch', 'semantic-economy'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.571 against deposit #958 ("crimsonhexagon on Moltbook: Provenance Log v1.2...").

## record 1866 · 10.5281/zenodo.19358277 · source line 143737
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 5x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.5 against deposit #958 ("crimsonhexagon on Moltbook: Provenance Log v1.2...").

### audit_status
unverifiable_no_truth_20260719

## record 1867 · 10.5281/zenodo.19411759 · source line 143775
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 5x across repos ['alexanarch', 'semantic-economy']. semantic-economy source: THREE_ARCHIVES__19417828.md. No alexanarch title match >=0.5. api map falls back to repo URL.

### audit_status
no_verified_target_flagged_20260719

## record 1868 · 10.5281/zenodo.19417828 · source line 143834
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 4x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site']. semantic-economy source: THREE_ARCHIVES__19417828.md. No alexanarch title match >=0.5. api map falls back to repo URL.

### audit_status
unverifiable_no_truth_20260719

## record 1869 · 10.5281/zenodo.19432476 · source line 143863
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 8x across repos ['alexanarch', 'crimson-hexagonal-interface', 'semantic-economy'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 1.0 against deposit #963 ("kimiclaw-moltbook-campaign — v3...").

### audit_status
no_verified_target_flagged_20260719

## record 1870 · 10.5281/zenodo.19371273 · source line 143935
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 16x across repos ['alexanarch', 'godkinggoogle', 'machinemediation-org']. semantic-economy source: moltbook_v14__19371273.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1871 · 10.5281/zenodo.19633211 · source line 144000
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 29x across repos ['alexanarch', 'godkinggoogle', 'machinemediation-org']. semantic-economy source: GW-TACHYON-zenodo_v7.md. Alexanarch secondary title match: deposit #937 (jaccard 0.667).

## record 1872 · 10.5281/zenodo.19447123 · source line 144078
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 16x across repos ['alexanarch', 'crimson-hexagonal-interface', 'godkinggoogle'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.833 against deposit #632 ("r.28 EVE Room Specification — Crimson Hexagonal Archive...").

## record 1873 · 10.5281/zenodo.19447121 · source line 144155
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 21x across repos ['alexanarch', 'crimson-hexagonal-interface', 'godkinggoogle'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.4 against deposit #51 ("OPERATIVE FEMINISM — CITATIONAL COMPREHENSIVITY PASS Supplem...").

### audit_status
no_verified_target_flagged_20260719

## record 1874 · 10.5281/zenodo.19637490 · source line 144227
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 12x across repos ['alexanarch', 'godkinggoogle', 'machinemediation-org'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.833 against deposit #61 ("EA-SPXI-14: The Nested-Layer Relation — SPXI ⊇ GEO...").

## record 1875 · 10.5281/zenodo.19775682 · source line 144293
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 7x across repos ['alexanarch', 'godkinggoogle', 'machinemediation-org'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 1.0 against deposit #690 ("i am a carcinized punching shrimp...").

## record 1876 · 10.5281/zenodo.19773465 · source line 144343
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 10x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site']. semantic-economy source: I_Demand_To_Be_Taken_Seriously__19773465.md. Alexanarch secondary title match: deposit #691 (jaccard 0.5).

## record 1877 · 10.5281/zenodo.19401508 · source line 144421
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 18x across repos ['alexanarch', 'semantic-economy', 'semanticphysics-site']. semantic-economy source: moltbook_provenance_v1.8__19401508.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1878 · 10.5281/zenodo.19720513 · source line 144486
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 7x across repos ['secret-book-of-walt', 'semantic-economy', 'semanticphysics-site']. semantic-economy source: FromYeezusToWalt_LiteraryHistory__19720513.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1879 · 10.5281/zenodo.19373638 · source line 144551
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 6x across repos ['semantic-economy']. semantic-economy source: moltbook_provenance_v1.8__19401508.md. No alexanarch title match >=0.5. api map falls back to repo URL.

### audit_status
no_verified_target_flagged_20260719

## record 1880 · 10.5281/zenodo.19890286 · source line 144610
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 5x across repos ['semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.4 against deposit #990 ("Rhys Owens — DOI Registry (11.NH2.RHYS.REGISTRY)...").

## record 1881 · 10.5281/zenodo.19780556 · source line 144687
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 7x across repos ['semantic-economy', 'semanticphysics-site']. semantic-economy source: metadatapacket_planning_synthesis__19780556.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1882 · 10.5281/zenodo.19779123 · source line 144752
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 7x across repos ['semantic-economy', 'semanticphysics-site']. semantic-economy source: EA-GEO-01-Addendum-A-PMOS__19779123.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1883 · 10.5281/zenodo.19772512 · source line 144817
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 6x across repos ['semantic-economy', 'semanticphysics-site']. semantic-economy source: BookOfLife_SBW_Registry__19772512.md. No alexanarch title match >=0.5. api map falls back to repo URL.

## record 1884 · 10.5281/zenodo.19634181 · source line 144882
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 4x across repos ['semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.667 against deposit #937 ("Gw.TACHYON...").

### audit_status
no_verified_target_flagged_20260719

## record 1885 · 10.5281/zenodo.19616242 · source line 144954
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 4x across repos ['semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.667 against deposit #937 ("Gw.TACHYON...").

### audit_status
no_verified_target_flagged_20260719

## record 1886 · 10.5281/zenodo.19445017 · source line 145026
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 4x across repos ['semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.4 against deposit #958 ("crimsonhexagon on Moltbook: Provenance Log v1.2...").

### audit_status
unverifiable_no_truth_20260719

## record 1887 · 10.5281/zenodo.19443133 · source line 145064
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 4x across repos ['semantic-economy', 'semanticphysics-site']. semantic-economy source: GW-SURFACE-continuity_v1__19443133.md. No alexanarch title match >=0.5. api map falls back to repo URL.

### audit_status
unverifiable_no_truth_20260719

## record 1888 · 10.5281/zenodo.19443128 · source line 145093
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 3x across repos ['semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.5 against deposit #878 ("gw.techne · TECHNE Continuity Tether — First Compression...").

### audit_status
unverifiable_no_truth_20260719

## record 1889 · 10.5281/zenodo.19443121 · source line 145131
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 3x across repos ['semantic-economy', 'semanticphysics-site']. semantic-economy source: GW-ARCHIVE-continuity_v1__19443121.md. No alexanarch title match >=0.5. api map falls back to repo URL.

### audit_status
unverifiable_no_truth_20260719

## record 1890 · 10.5281/zenodo.19443117 · source line 145160
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 3x across repos ['semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.5 against deposit #877 ("gw.praxis · PRAXIS Continuity Tether — First Compression...").

### audit_status
unverifiable_no_truth_20260719

## record 1891 · 10.5281/zenodo.19443115 · source line 145198
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 3x across repos ['semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.5 against deposit #879 ("gw.labor · LABOR Continuity Tether — First Compression...").

### audit_status
unverifiable_no_truth_20260719

## record 1892 · 10.5281/zenodo.19443093 · source line 145236
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 4x across repos ['semantic-economy', 'semanticphysics-site']. semantic-economy source: GW-SOIL-continuity_v1__19443093.md. No alexanarch title match >=0.5. api map falls back to repo URL.

### audit_status
unverifiable_no_truth_20260719

## record 1893 · 10.5281/zenodo.19720525 · source line 145265
### recovery_verification
2026-07-08 Phase 7 (network-wide link inventory recovery): DOI referenced 3x across repos ['semantic-economy', 'semanticphysics-site'] but not in v3.8.1 resolver. Alexanarch title match found via jaccard 0.429 against deposit #686 ("Mycelial Cardboard Boxes: Market Analysis and Production Str...").

## record 1894 · 10.5281/zenodo.19388983 · source line 145342
### recovery_verification
2026-07-08 Phase 7 recovery: DOI referenced 4x across repos ['semantic-economy']. semantic-economy source: moltbook_provenance_v1.9.md. No alexanarch title match >=0.5. api map falls back to repo URL.

### audit_status
no_verified_target_flagged_20260719

## record 1895 · 10.5281/zenodo.20612084 · source line 145401
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: identified via review MD Section 1 entry, blog URL provided.

## record 1896 · 10.5281/zenodo.19359657 · source line 145465
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: "im pretty sure this one was the code to crimsonhexagonal.org, link the repo". EA-HEXAGON-OS-01 identifier recovered from surrounding prose in cross-repo scan.

## record 1897 · 10.5281/zenodo.20070574 · source line 145530
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: explicit DOI + blog URL pairing.

### audit_status
no_verified_target_flagged_20260719

## record 1898 · 10.5281/zenodo.19672980 · source line 145582
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: "this was the pessoagraph code - point to repo".

## record 1899 · 10.5281/zenodo.19855905 · source line 145647
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: blog URL provided in position matching EA-LAL-WORKPLAN-01 identifier from cross-repo scan.

## record 1900 · 10.5281/zenodo.20612363 · source line 145711
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: explicit DOI + blog URL pairing.

## record 1901 · 10.5281/zenodo.19455105 · source line 145775
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: "past conversation files" pointed to zenodo. Past chats confirm: EA-HCORE-01 v1.8.0 deposited as zenodo.19455105, code in crimson-hexagonal-interface repo. Superseded by v2.0 at zenodo.19460376.

### audit_status
no_verified_target_flagged_20260719

## record 1902 · 10.5281/zenodo.20618250 · source line 145834
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: explicit DOI + description + blog URL provided.

### audit_status
no_verified_target_flagged_20260719

## record 1903 · 10.5281/zenodo.19857006 · source line 145892
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: "this was the code for livingarchitecture lab, link to site". Site (livingarchitecturelab.org) is currently 403 (auth-protected), so pointing to alexanarch record #988 (LAL Site Code v0.1.1 Phase 1 Kernel — the canonical semi-restored target) instead of the site URL directly. This DOI is adjacent to zenodo.19857005 (record #988) — same series, likely a version companion.

## record 1904 · 10.5281/zenodo.19630477 · source line 145966
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: blog URL provided in position after EA-SPXI series identifiers from cross-repo scan.

## record 1905 · 10.5281/zenodo.20735920 · source line 146030
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: blog URL provided in position matching EA-TANG-MARYLEE-01 identifier from cross-repo scan.

### audit_status
no_verified_target_flagged_20260719

## record 1906 · 10.5281/zenodo.20751348 · source line 146088
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: blog URL provided in position matching "Five Substrates, One Prompt" title fragment from cross-repo scan.

## record 1907 · 10.5281/zenodo.17808895 · source line 146152
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: blog URL provided in position matching EA-MPAI-JOSEPHUS-01 identifier.

### audit_status
unverifiable_no_truth_20260719

## record 1908 · 10.5281/zenodo.19433483 · source line 146180
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: "GW.TACHYON.zenodo — v1 — Encrypted Session Deposit". Source in gravitywell repo.

### audit_status
no_verified_target_flagged_20260719

## record 1909 · 10.5281/zenodo.19433865 · source line 146253
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: "The identifier 10.5281/zenodo.19433865 links to the GW.TACHYON.zenodo — v4 record on Zenodo". Source in gravitywell repo.

### audit_status
no_verified_target_flagged_20260719

## record 1910 · 10.5281/zenodo.20694658 · source line 146325
### recovery_verification
2026-07-08 Phase 8 (MANUS manual review of Phase 7 remainder pile): DOI target identified by Lee Sharks direct testimony after DataCite recovery returned 404 for all Lee-authored DOIs (severed) and only external DOIs still resolve. MANUS: "Version 10 of the GW.TACHYON.zenodo repository features specific data compressions, including the inscription chain and the Paul function". Source in gravitywell repo.

## record 1911 · 10.5281/zenodo.20041137 · source line 146390
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: 5 May 2026 v2 Governance Batch. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

### audit_status
no_verified_target_flagged_20260719

## record 1912 · 10.5281/zenodo.20041149 · source line 146446
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: 5 May 2026 v2 Governance Batch. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it. Secondary alexanarch title match found: deposit #717 (jaccard 0.643). Promoted to direct_verified.

### audit_status
no_verified_target_flagged_20260719

## record 1913 · 10.5281/zenodo.20041155 · source line 146516
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: 5 May 2026 v2 Governance Batch. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

## record 1914 · 10.5281/zenodo.19338438 · source line 146578
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: April 2026 Facebook poetry deposit; publication-date-tagged 2014-12-25. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it. Secondary alexanarch title match found: deposit #957 (jaccard 1.0). Promoted to direct_verified.

## record 1915 · 10.5281/zenodo.20388109 · source line 146625
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: May 30 2026 leesharks.com About-the-Author trilogy Part I; Tao Lin mandala attribution restored. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

## record 1916 · 10.5281/zenodo.20388111 · source line 146687
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: May 30 2026 leesharks.com About-the-Author trilogy Part II. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it. Secondary alexanarch title match found: deposit #1007 (jaccard 0.625). Promoted to direct_verified.

## record 1917 · 10.5281/zenodo.20388113 · source line 146762
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: May 30 2026 leesharks.com About-the-Author trilogy Part III; taolin.us/mandalas cross-referenced. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

## record 1918 · 10.5281/zenodo.19024301 · source line 146824
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: March 16 2026 batch registry from crimsonhexagonal community pull. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

## record 1919 · 10.5281/zenodo.18984939 · source line 146886
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: March 16 2026 batch registry. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

### audit_status
unverifiable_no_truth_20260719

## record 1920 · 10.5281/zenodo.20709610 · source line 146912
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 22 2026 sémantique potentiel — 67 CRITICAL entries recovery pass. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

### audit_status
no_verified_target_flagged_20260719

## record 1921 · 10.5281/zenodo.20709621 · source line 146970
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 22 2026 sémantique potentiel. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

## record 1922 · 10.5281/zenodo.20740687 · source line 147046
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 22 2026 sémantique potentiel — 67 CRITICAL entries recovery pass. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

### audit_status
no_verified_target_flagged_20260719

## record 1923 · 10.5281/zenodo.20753314 · source line 147104
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 22 2026 sémantique potentiel. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

### audit_status
no_verified_target_flagged_20260719

## record 1924 · 10.5281/zenodo.20753794 · source line 147160
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 22 2026 sémantique potentiel. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

## record 1925 · 10.5281/zenodo.20754069 · source line 147222
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 22 2026 sémantique potentiel. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

### audit_status
no_verified_target_flagged_20260719

## record 1926 · 10.5281/zenodo.20754288 · source line 147278
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 22 2026 sémantique potentiel. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

## record 1927 · 10.5281/zenodo.20754330 · source line 147340
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 22 2026 sémantique potentiel. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

## record 1928 · 10.5281/zenodo.20754486 · source line 147402
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 22 2026 sémantique potentiel. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

### audit_status
no_verified_target_flagged_20260719

## record 1929 · 10.5281/zenodo.20741733 · source line 147458
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 22 2026 sémantique potentiel. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

### audit_status
no_verified_target_flagged_20260719

## record 1930 · 10.5281/zenodo.19649793 · source line 147508
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: April 20 2026 spxi.dev case study. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

## record 1931 · 10.5281/zenodo.20612567 · source line 147570
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 27 2026 traininglayerliterature.org build session; publication-date-tagged 2025-12-06. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

## record 1932 · 10.5281/zenodo.20629210 · source line 147634
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: June 14 2026 Water Giraffe Cycle §0.5 references — canon provenance node for Kierkegaard. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it.

## record 1933 · 10.5281/zenodo.19513035 · source line 147696
### recovery_verification
2026-07-08 Phase 9 (past-chats title recovery): DOI title recovered from past conversation transcripts. past-chats: April 15 2026 Drone Swarm session — this DOI was a duplicate deposit of 19512987, cleaned as SUPERSEDED. This was in the Phase 7 truly-bare pile — title was inaccessible until conversation_search surfaced it. Secondary alexanarch title match found: deposit #972 (jaccard 0.923). Promoted to direct_verified.

## record 1934 · 10.5281/zenodo.20559754 · source line 147764 · 2026-07-03
### note
Added 2026-07-28. The DOI was referenced in JSON-LD on provenanceerasure.org with a resolver url, but was absent from both the map and this index, so the resolver returned not-found. The deposit existed throughout. Envelope seated 2026-07-30: the deposit resolves at #1011; the index carried the AXN but a null record link, which failed gates G11/G12.

## record 1935 · 10.5281/zenodo.19296648 · source line 147810 · 2026-07-03
### audit_status
MANUS-directed repair

## record 1936 · 10.5281/zenodo.19296650 · source line 147847 · 2026-07-03
### audit_status
MANUS-directed repair

## record 1937 · 10.5281/zenodo.19296654 · source line 147884 · 2026-07-03
### audit_status
MANUS-directed repair

## record 1938 · 10.5281/zenodo.19296660 · source line 147921 · 2026-07-03
### audit_status
MANUS-directed repair

## record 1939 · 10.5281/zenodo.19296664 · source line 147958 · 2026-07-03
### audit_status
MANUS-directed repair

## record 1940 · 10.5281/zenodo.19296677 · source line 147995 · 2026-07-03
### audit_status
MANUS-directed repair

## record 1941 · 10.5281/zenodo.18445652 · source line 148032 · 2026-02-01
### audit_status
MANUS-directed repair

