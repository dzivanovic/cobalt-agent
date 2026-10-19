## §0 Headline
- Card 731 amended in place: K6 takes `0027` (rollback too); FORWARD/REVERSE entries, placement, K6 RED text, head pins, K0 and DECISION 3 move one place.
- Pins stated against the merged state: Genesis's build touches 18 pin test files plus `ops/desk/gate-lists.md` (proved by `git diff 40e646ed ops/f21-genesis-1013 --stat`).
- Added to FOR THE CHECK: the lower-number take-back line.
- 2 ASK DESK items.

## DECISIONS
1. ASK DESK: K0 now STOPs (`FAILED: K0 — Genesis (card 468) not merged`) if `FORWARD` ends `0025`; the card said K0 "next free number", which no longer holds at BASE `40e646ed` (still `0025`). Left BASE as is. Default: the desk sets BASE to main after Genesis merges before launching F5. [2026-10-19 07:35]
2. ASK DESK: the merged-state pin list was traced from Genesis's diff and the build report, not from a merged tree (none exists). Default: the builder re-finds each pin by content on the merged tree; the card says so. [2026-10-19 07:35]

## RECORDS
- Card edited: `prompts/2026-10-18/731-f5-card.md` (K0, K6, K6 RED, DECISION 3, `## RECORDS` migration line, `## CHECK ASKS`). BASE, TIP, CHECK REPORT untouched.
- Genesis proof: `ops/f21-genesis-1013` merge-base with main is `40e646ed`; `FORWARD` tail `0026_genesis_chunk.sql`, `REVERSE` head `0026_genesis_chunk.rollback.sql`; `placement.py` gains `"genesis_chunk": Side.USER`; `test_dml_roles_offline.py` moved to `FORWARD[-2]` / `REVERSE[1]`; `cli.py` +2 lines (`strike_cli` mount `:546` → `:547`); `gate-lists.md` `--deselect` tails gain `test_genesis_db.py`, `test_genesis_experiments_db.py`.
- New pin comment text on every moved line: `# F5 card 731 K6: 0027 after Genesis 0026`.
- Times from `date`: Mon Oct 19 07:27:53 EDT 2026 (start). Report written 07:35 EDT (estimated). Nothing committed.

DRAFTED · decisions: 2
