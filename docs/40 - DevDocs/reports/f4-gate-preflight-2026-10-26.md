# F4 gate run — preflight of 1045, 1047, 1048 (read-only)

Seat `f4-gate-preflight`. Main tip at read: `341b4558` (1047's BASE `05366873` is the desk's to reset at launch). Nothing was run except reads.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1a | read 1045 whole | MODEL · SEAT · SESSION present, one launch line, `CLASS: K2`, `LADDER`, `RULINGS: 2026-10-18 R1863`. No METER tag; precedent 970 has none either. No unfilled token (`<n>`, `<s>`, `<time>` are report-fill values). | OK (NOTE 1) |
| 1b | read 1047 against `prompts/CARD.md:9-32` | JOB, LADDER, BRANCH, WORKTREE, BASE, TIP (empty), REPORT, CHECK REPORT (empty), HOUSE B (empty), BAND, RULINGS all present. Sections in order, DEPLOY PROOF present. | OK |
| 1c | read 1047 `## DEPLOY PROOF` against `ops/desk/deploy-smoke.sh` `shape()` (`:122-131`) | Marker 2 is `grep -c -F "PROBE_ITEMS = (\"X15\",)" …`. `pat=${r%%\"*}` cuts at the first quote, giving `PROBE_ITEMS = (\`. That holds a backslash, so the row is RED `not a mapped smoke command`. Precedent 973:62 used `"PROBE_ITEMS = ("` with no escaped quote. | FAIL |
| 2 | read 1045 `## REPORT` lines 55-61 against R2463 | Five `GATE RESULT` lines in order X7 X8 X9 X10 X15. X10 `OK` cites `reports/deploy-f4-refresh-attempt2.md:263`. X8 is a post-load watch (`RULED`). X15 waits for the 1047 probe, second pass. X7 is the two offline tests plus his render leg. X9 is the hub legs, his Sync leg, and firings post-load. | OK |
| 3a | every 1045 command against its launch line | Steps 0-3 and the second pass match allow strings byte for byte, including both `uv run pytest …` strings, `COBALT_ENV=dev uv run cobalt jobs restarts 5623c3ff..54feb833` and `COBALT_ENV=dev uv run prefill probe X15`. `ls`, `grep`, `date`, `git -C … rev-parse*` are allowed. `prefill` is an entry point (`pyproject.toml:73`). | OK |
| 3b | `grep -n -F -e "= \`<t down>\`" -e "= \`<t up>\`" <deploy report>` | Prints `:189` and `:204`. The tokens are literal text in the report, not placeholders. The hook passed the escaped backticks. | OK |
| 3c | 1047 against `prompts/BUILD-HUB.md:14` | The card gives the builder only `uv run pytest`, `uv run cobalt jobs restarts`, `git commit` and `ls`/`grep` reads. None of `git apply`, `cherry-pick`, `git mv`, `rm`, `mv`, `revert`. | OK |
| 3d | `desk-launch.sh:836-844` against 1045's `uv run` and `COBALT_ENV=` | The write-string refusal is waived when `RULINGS` validates (`:793`). 1045 carries `RULINGS: 2026-10-18 R1863` and `R1863` is a row in `cto-2026-10-18.md`. Same as 970. | OK |
| 4a | `git grep main` `daily.py` | `:759` `refresh_demand_consumer`, `:774-776` `REFRESH_GETS`, `:787-797` gate, `:794` `check_scheduled_demand`, `:800` `_gated_fetch`, `:1109` `VaultWriteStore()`, `:682` `REFRESH_GETS = 3` | OK |
| 4b | `git grep main` test classes | `:300` `TestDailyRefreshConfig`, `:350` `TestTheJobRow`, `:358`, `:365`, `:394` the three tests, `:454` `TestStamp`, `:491` t6, `:569` `TestSharedGate`, `:1115` a4. All match the ranges 1045 cites. | OK |
| 4c | `restarts.py` | `:274` `ESCALATE:`, `:276` `RESTARTS: ` | OK |
| 4d | deploy report | `:189` `<t down>`, `:204` `<t up>` · downtime 28 s, `:263` DEPLOYED line with `offline 8539/0 · with-DB 5552/0 · live-note 146/0`. 1048's "bounce 28 s" is true. | OK |
| 4e | `F4-FINAL-2026-10-10.md` | `:200` section, `:213` X7, `:214` X8, `:215` X9, `:216` X10, `:221` X15 | OK |
| 4f | `ops/com.cobalt.prefill-refresh.plist` | `:149-150` `RunAtLoad`, `:151-154` log paths, `:14` `COBALT_VAULT_PATH` | OK |
| 4g | `tests/conftest.py:13`, `tests/cobalt/conftest.py:289-298` | `load_dotenv()`; the `POSTGRES_HOST`/`USER` test and the dev connection | OK |
| 4h | `data/deploy/bootstrap-owed.json:2`; `778 …card.md:21` | Line 2 is the prefill-refresh entry with gate X7 X8 X9 X10 X15. 778 `:21` is the `deferred` LAUNCHD line. | OK |
| 4i | 1047 cites at main | `cli.py:77`, `:83`, `:88`; `env.py:60`; `collector.py:205`, `:222`, `:255`; `market.py:55`, `:68`; `calendar.py:52`, `:62`, `:83`; `detector.py:80`, `:103`, `:131`, `:238`, `:313`; `radar/collector.py:42`; `daymode/note.py:83`, `:140`; `tunables.yaml:702`; `DEPLOY-HUB.md:146`; `deploy-step-c.sh:176`, `:185-186` | OK |
| 4j | counts | `grep -c -F com.cobalt.prefill-refresh bootstrap-owed.json` is 1 (1048 marker "before 1" holds). `grep -c … test_x7_the_daymode_unit…` is 0 (1047 "before 0" holds). The tag `deploy-2026-10-27*` does not exist. `refresh_probe.py` absent. | OK |
| 5a | 1048 TAG against `desk-launch.sh:2206` | `deploy-2026-10-27-prefill-refresh-bootstrap` matches `[A-Za-z0-9._-]`; the desk can re-date it at launch. | OK |
| 5b | 1048 against `deploy-step-c.sh --bootstrap-only` (`:176-196`) | `## LAUNCHD` line is `add` and its build-card ref passes the shape regex (726 `…-card.md:C2`). Plist Label is on main. Owed file lists the label. | OK |
| 5c | 1048 `## GATE RESULTS` | Holds X10 and X8 only. X7, X9, X15 are absent, so `:185-186` refuses until the desk adds each as `OK`. This is the load rule holding. | OK |
| 5d | 1048 `## SMOKE READS` against `deploy-smoke.sh:341-359` | Both rows use the expectations `prints 1 or more` and `prints 1`. The script reads only `exit 0, listed`, `` exit 0, `<v>` ``, `exit 0, a count of 1 or more`, `exit 0, one integer`, or a backticked value. Anything else is RED `expectation … is not one this script reads`. Precedent 929 used `` `0` ``. Both commands are the mapped `grep -c -F` shape. | FAIL |
| 5e | 1048 `## MARKERS` | `grep -c -F … bootstrap-owed.json` before `1` after `0`, backticked, mapped shape. | OK |
| 6 | 1047 BAND, CLASS, probe | `BAND: HIGH`, `CLASS: K2`. PASS is "no virtual minute above 50 and no 429". In process on a virtual clock with an `httpx.MockTransport`, no Finviz GET (P2 (b), DECISION 1). T1 and T2 are "GREEN on BASE expected". | OK |
| 7a | R2463 RECORDS line in 1045 (`:67`), 1047 (`:66`), 1048 (`:41`) | The line is identical in all three and in the drafter report. It is a longer form of the row text at `cto-2026-10-26.md:16`, not a byte copy of the row. | OK (NOTE 2) |
| 7b | R2465 RECORDS line | `1049-f4-strike-reserve-card.md:57`: "F4 reservation 1049 — drafted in parallel with f4-probe; launched only on PROBE X15 FAIL, dropped on OK — brain 9b07db5a 2026-10-26 (R2465)" | OK |
| 8 | header values the prompts write | 1045 writes `RULINGS` only. 1047 writes `BASE` (card format) and `RULINGS`, with `TIP`, `CHECK REPORT`, `HOUSE B` empty. 1048 writes `BASE: main` and `TIP: none` as the 929 deploy shape. No `TIP`, `CHECK REPORT`, `HOUSE B` or `BASE` value is invented. | OK |

## ISSUES
- FAIL 1048: `## SMOKE READS` rows 1 and 2 use expectations `prints 1 or more` and `prints 1`. `deploy-smoke.sh` marks both RED, so the deploy smoke is RED even when the plist and `REFRESH_JOB` are fine. Fix: `exit 0, a count of 1 or more` for row 1, `` exit 0, `1` `` for row 2.
- FAIL 1047: `## DEPLOY PROOF` marker 2 (`grep -c -F "PROBE_ITEMS = (\"X15\",)" …`) has a backslash in the pattern and is RED `not a mapped smoke command`. Fix: pattern `"PROBE_ITEMS = ("` as in 973:62, before `0` after `1`. It blocks the later deploy of f4-probe, not the build launch.
- NOTE 1 (1045): no METER tag. Precedent 970 is the same shape.
- NOTE 2 (1045, 1047, 1048): the R2463 RECORDS line is a longer form of the brain row, written the same in all prompts. The row has "bootstrap card drafter-written" and the line has "brain 9b07db5a 2026-10-26". The desk should confirm that is the line it relayed.
- NOTE 3 (1047): no `RESTARTS:` header key (973 had `RESTARTS: com.cobalt.radar`). `CARD.md` does not require it, and R1 derives it.
- NOTE 4 (1047): BASE `05366873` is stale against main `341b4558`. The desk resets it at launch, and the cited lines hold at the current tip.
- NOTE 5 (1048): the `deploy-smoke.sh` header says `<` and `>` in a command are RED, but the code does not check the pattern for them. Row 1's `<string>…</string>` pattern should map, so this is not a blocker.
- Launch blocker: 1045 is clear to launch. 1048 must not launch its deploy until the smoke expectations are fixed. 1047 builds, but its DEPLOY PROOF line 2 must be fixed before the deploy card is cut.

PREFLIGHT DONE · cards: 1045 1047 1048 · checks: 27 · fails: 2 · ready: NO
