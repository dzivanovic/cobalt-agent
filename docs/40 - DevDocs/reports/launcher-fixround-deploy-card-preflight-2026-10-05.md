# launcher-fixround deploy card 47 — preflight (read-only), 2026-10-05

Card: `prompts/2026-10-05/47-deploy-launcher-fixround-card.md`. Every command below was run by this seat; output quoted.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | `git -C /Users/cobalt/cobalt rev-parse --verify a545a4d8^{commit}` | `a545a4d8d424c72df46d86c240b7484427f0cad2` | OK |
| 1b | `git -C /Users/cobalt/cobalt rev-parse ops/launcher-fixround-1005` | `a545a4d8d424c72df46d86c240b7484427f0cad2` (head = TIP = code tip) | OK |
| 1c | `git -C /Users/cobalt/cobalt log --oneline a545a4d8..ops/launcher-fixround-1005 -- tests ops configs src` | nothing | OK |
| 1d | `tail -n 1 …/launcher-checks-check-2026-10-05-r2.md` | `CHECK DONE · job: launcher-checks · pass: 1 · tip: a545a4d8 · … · held unfixed: 0 · open: 0 · … · RESTARTS: none · … · ready: YES · …` | OK |
| 1e | `git log -1 --format=%h -- <check report>` · `git diff --stat -- <check report>` | `6bf0b815` · nothing | OK |
| 2 | `rev-parse --verify` on `deploy/deploy-launcher-fixround-1005` and on tag `deploy-2026-10-05-launcher-fixround`; `ls` of the worktree and of the report | both `fatal: Needed a single revision` (exit 128); both `ls`: `No such file or directory` | OK |
| 3 | `grep -n "^| R412 " reports/cto-2026-10-05.md`; `git diff --stat` and `git log -1 --format=%h` on that file | `109:\| R412 \| 10-05 13:16 ET \| HIS RULING: drop pre-merge (d2) from DEPLOY-HUB (O4 closed); … \| APPROVED (in cto-desk-contract.md, NOW at 13:16; launch gate L7a) \|`; diff nothing; log `4c42fbde`. Card's only RULINGS entry is R412. | OK |
| 4a | markers on main: step0 `is not committed and unmodified` · hub `Fix-round row` · CARD.md `On a fix-round row (a small fix after the check, his R376, L75)` · deploy-card.sh `\| fix report \|` | `0` · `0` · `0` · `0` = the card's four `before 0` | OK |
| 4b | after on `a545a4d8` (read from `git show a545a4d8:ops/desk/deploy-step0.sh`, `git diff 5fb0ddf5 a545a4d8 -- DEPLOY-HUB.md`, `git show ops/launcher-fixround-1005:…CARD.md`, `git diff main...a545a4d8 -- ops/desk/deploy-card.sh`; counted by eye, `git grep` is not in this seat's allowlist) | step0: 1 (the `why=` line) · hub: 1 (the inserted `Fix-round row` line) · CARD.md: 1 · deploy-card.sh: 1 (the header `\| fix report \|`; the ships row ends `\| \|`, no match) = the card's `after 1` ×4 | OK |
| 4c | `git diff --stat main...a545a4d8` | 8 files: `prompts/CARD.md`, `prompts/DEPLOY-HUB.md`, `reports/launcher-fixround-build-2026-10-05.md`, `ops/desk/deploy-card.sh`, `ops/desk/deploy-step0.sh`, `ops/desk/desk-launch.sh`, `tests/ops/test_deploy_step0.py`, `tests/ops/test_desk_launch_prechecks.py` (586 insertions, 11 deletions). The card lists exactly these 8, each with a class (operator script / test / DOCS); no `src/`. Check report: `RESTARTS: none` (lines 136, 160, 197). | OK |
| 5 | main's `CARD.md` `## SHIPS` header; `grep -n` on main's `ops/desk/desk-launch.sh`; `git show main:ops/desk/deploy-card.sh`; the card's header | main CARD.md: `\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \|` (6 columns). main `desk-launch.sh:698`: same 6 columns; main `deploy-card.sh` writes the same 6-column header and rows. Card 47: `\| # \| branch \| code tip \| branch head \| check report \| its stop line must carry \| fix report \|` (7 columns); siblings 39 and 41 have 6. Main's launcher reads cells by `awk -F'\|'` (`$7` = the literals) with no column count, so a seventh cell would be ignored, but that is by reading, not by running; the rule says 7 vs 6 is a FAIL. | FAIL |
| 6a | `git diff 5fb0ddf5 main -- DEPLOY-HUB.md` (`-U0` for the numbers) | main changes base lines 26, 50, 57 (P1), 74, 93 (removed), 101 (removed, (d2)), 134, 178, 181. Card says "26, 50, 57 (P1), 74, 93, 100, 134, 176-177": 100 should be 101, and 176-177 should be 178 and 181. | FAIL |
| 6b | `git diff 5fb0ddf5 a545a4d8 -- DEPLOY-HUB.md` | one hunk `@@ -56,6 +56,7 @@`: context P0 (56), P1 (57), P2 (58), then one `+  - Fix-round row …` line after P2 | OK |
| 6c | separation | main's P1 hunk ends at 57, the branch insertion sits after 58; line 58 (P2) is unchanged on main (context in main's diff). One unchanged line apart. | OK (merge itself not run: `merge-tree` is outside the allowlist) |
| 7a | `grep -c -F "«FILL" <card>` | `0` | OK |
| 7b | shape against `CARD.md`, `39-…`, `41-…` | header keys and section order (SHIPS, MARKERS, SMOKE READS, RECORDS) match; SHIPS header differs (7 columns vs 6, see 5). In `## RECORDS` the `- OWED …` bullet is glued to the end of the previous bullet (`…without a conflict.- OWED, a later card…`, no line break), so it is not its own record line. | FAIL |
| 8 | `git diff --stat -- <card>` · `git log -1 --format=%h -- <card>` | nothing · `4c42fbde` (committed, clean) | OK |

## ISSUES
- FAIL 5: the card's `## SHIPS` has 7 columns (`fix report`), main's `CARD.md`, `desk-launch.sh:698` and `deploy-card.sh` read 6. The new column exists only on the branch. Either drop the seventh column from the card (the check's tip equals the code tip, so no fix report is needed) or deploy only once the column is on main.
- FAIL 6a: `## RECORDS` misnames the base lines main changes in `DEPLOY-HUB.md`: `100` should be `101`, and `176-177` should be `178` and `181`. The no-conflict conclusion stands.
- FAIL 7b: `## RECORDS` runs two bullets together (`…without a conflict.- OWED, …`). Put the OWED bullet on its own line.

PREFLIGHT DONE · card: launcher-fixround-deploy-47 · checks: 8 · fails: 3 · ready: NO
