# D5 deploy card — draft report, 2026-10-05

## §0 Headline
- The D5 deploy card is written: `prompts/2026-10-05/64-deploy-d5-card.md`, one row, `c96b5118` = head = code tip, no placeholder token.
- The launcher accepts the row as written: `ships_checked` matches only the card's own backticked literals (`held unfixed: 1`, `ready: NO`) against the check's last line, so no STOP. `deploy-card.sh` would refuse; the card is by hand.
- O1 ruling rows cited: R326 and R350 (both `HIS RULING · APPROVED`, committed), plus R412. 10-02 R4 is `LAUNCHED`, not a ruling, so not cited.
- No D5 test reaches the DB without `requires_db`. No overlap with main since the merge base. 1 decision (A3).

## CARD
- JOB `deploy-d5-1005` · LADDER `S3-P3 · F14` · BRANCH `deploy/deploy-d5-1005` · WORKTREE `deploy-d5-1005` · BASE `main` · TIP `c96b5118`
- REPORT `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-d5-1005.md` · TAG `deploy-2026-10-05-d5` · MIGRATIONS `none` · SET `s3`
- RULINGS `2026-10-03 R326, 2026-10-05 R350, 2026-10-05 R412` (R376, R390 are LAWS L75, L43)
- Absent today: `rev-parse --verify` fails for `deploy/deploy-d5-1005` and `deploy-2026-10-05-d5`; `ls` fails for the worktree and the report.
- SHIPS: D5, check `drc-d5-check-2026-10-04.md`, literals `held unfixed: 1` and `ready: NO`, 15 files as `diff --stat main...drc/d5-reconcile-1004`, `reconcile.py` class `com.cobalt.aset,com.cobalt.radar` (build report `## RESTARTS`), fix report empty.

## DECISIONS
1. ASK DESK: A3 (entry-price correction through `record_correction` rewrites the fill cache, sizing) and the check's `ready: NO` are open in the check; R326/R350 cover O1 only. Default: ship as built (R314 KEEP), as the card records. [22:45 ET]

## RECORDS
- Gate read: `desk-launch.sh` `ships_checked` (lines 748–830): literals from the SHIPS cell, matched by `*"$lit"|*"$lit "*` on the check's last line; `ltip` = `ctip` so `fixed_ok` is not needed. No code reads a ruling row against the stop line; rulings are checked only for shape and commit (`ruling_row`).
- `deploy-card.sh:130-131` demands `held unfixed: 0` and `ready: YES`: it refuses D5 (as the S3 card said).
- Merge by reading: merge-base `3e40359a` (ancestor of `07a4b8fe`, which main holds); main changed none of D5's 15 files; `test_drc_k3.py` diff `3e40359a..c96b5118` empty.
- DB tests at `c96b5118`: all 4 with-DB tests carry `@requires_db`; `test_drc_d5.py` is offline. No unmarked test.
- Counts: before on main `d664b926`: files absent, `reconcile` in `units.py` 5, `refused_cards` in `build.py` 0. After: 8, 2, `NO_WRITER_CODE` 4, `def test_` 27.
- The check report is committed; the card and this report are not (the desk commits).

D5 DEPLOY CARD DRAFTED · decisions: 1
