# Describe protocol v1.0 — page descriptions that keep historical standing (2026-10-18)

ChatGPT's review of the draft deposit EA-PREDICTION-INDEX-01 (adopted by Lee Sharks, 2026-10-18): a page description
can turn a historical source claim into an apparently current description by summarising it. Its example: the severance
page said deletions propagate "through the OpenAIRE Graph's weekly cycle" — the June 22 paper's account (#875), stated as
if it were the index's own. The index records claims and does not judge them; its descriptions must do the same. Kimi's
review: pages whose description admits unrelated residue should carry that caveat in the data.

Your batch is an entry of data/index/describe-queue.json. Each page gives its id, title, current description, and every
claim on it: id, tier, registered date and deposit (number and title), the statement (opening), and its dated states.

For each page, rewrite the description:

1. Keep its subject, its order and roughly its length (within a quarter either way; never over 1,100 characters). Add
   no fact the page's claims do not carry.
2. Every sentence that says how something is — how a platform behaves, what an institution did, what a text means, who
   wrote what, what came first — names whose claim it is: the deposit (by number, or a short form of its title, with its
   month where the order matters: "the June 2026 OpenAIRE papers (#875, #876) hold…"), or "these claims", "the papers
   on this page argue". The deposit's own figures may be given as its figures ("#868 counts 871 DOIs").
3. Use the tier's verb: forecasts forecast; standing claims hold or claim; unbuilt tests specify; historical theses argue;
   priority records record that the archive claims to have named or formalised something first — membership records the
   claim, it does not settle the comparison.
4. Where a later claim on the page revises, corrects or contests an earlier one (a dated state, or a later statement that
   says otherwise), say so in the description, in order.
5. No verdicts: no "correctly", "shows", "proves", "demonstrates" said in the index's own voice (a deposit may "show"
   only as "#N reports that it shows…").
6. If some claims on the page are not about its subject, say so plainly ("The page also holds unrelated claims on …")
   and list their ids in `residue`. List nothing in `residue` for claims that belong.

Write data/index/describe/<ID>.json:

```json
{"batch_id": "<ID>", "protocol": "DESCRIBE-PROTOCOL v1.0", "started_at": "<date -u>", "finished_at": "<date -u>",
 "self_description": "<what you are, or 'unknown'>",
 "pages": [{"page": "<page id>", "description": "<new description>", "residue": ["<claim id>", ...], "note": "<one line>"}]}
```

Then run `python3.12 scripts/index/verify_describe.py data/index/describe/<ID>.json` and fix every failure.
