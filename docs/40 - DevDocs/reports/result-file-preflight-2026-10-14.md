# Card 548 `result-file-1014` — preflight (2026-10-14, read-only)

Read at `main` HEAD `32687899`. No test was run.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git log --oneline -2 -- <548 card>` · `git diff --stat -- <548 card>` | commit `32687899`; diff empty | OK |
| 2 | header vs `CARD.md` (build): JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, DB, RULINGS all present; `grep -c "«FILL"` | 0; only BASE, TIP (and CHECK REPORT, HOUSE B, which the desk fills at the check) are empty. Extra keys CLASS, INSTALL, RESTARTS are not in the CARD.md table (537 carries them too) | OK (NOTE 5) |
| 3 | `git diff --stat 0ffb6949 HEAD -- ops tests/ops src/cobalt/jobs/restarts.py BUILD-HUB CHECK-HUB DEPLOY-HUB CARD.md` | empty: the card's `0ffb6949` proofs still hold at HEAD | OK |
| 4 | `deploy-step0.sh` anchors: 69 `HERE`, 132 `rel`, 657 clean pair, 677-733 P2, 679, 686-694, 706, 721 | all as the card says | OK |
| 5 | `deploy-card.sh` anchors: 477-482, 483, 490-491, 493-494, 501, 504-507, 524. `dirname "$0"` idiom | all as written; the script has no `HERE`; `desk-launch.sh:369` holds `$(dirname "$0")` | OK |
| 6 | `desk-launch.sh` anchors: 264 `here`, 1450, 1451-1458, 1459, 1469-1473, 1479, 1450-1489 | all as written | OK |
| 7 | `gate.sh:67` `refuse()`; `restarts.py:225-228`, `:230-234`, `:245-246`; `desk-watch.sh:40-44`; `desk-done.sh:24-31`; `card-fill.sh:71-78`; `preflight.sh:251,263` | all as written | OK |
| 8 | hubs: `BUILD-HUB.md:109` and `CHECK-HUB.md:125` are the `DB: none` sentences, `:108` and `:124` the stop lines; the key lists vs the stop-line fields | 15 build keys and 22 check keys, one per stop-line field; no key added | OK |
| 9 | test anchors: `test_deploy_step0.py:78,85,238`; `test_deploy_card.py:47,155,232`; `test_desk_launch_prechecks.py:561,566,1070`; `test_build_hub_no_clutter.py:57-60`; `grep` for the two hub sentences in `tests/ops` | all as written; no test pins either sentence; `tests/ops` has no `__init__.py` (NOTE 6) | OK |
| 10 | each row's red test names its failing reason on BASE (RF1 exit 127; RF2 count 0 and `1 failed`; RF3 `lacks 'held unfixed: 0'`; RF4 refused text; RF5 refused text; RF6 RUN) | named for every row | OK |
| 11 | RF1 (3) against the `refuse()` shape RF1 requires | `gate.sh:67` is `printf 'REFUSED: %s\n' "$*" >&2`; test (3) forbids `>` in the script text | FAIL (ISSUE 1) |
| 12 | RF2 (5): the repaired `test_no_other_line_changes_from_base` against brain R1472 and the open cards | the one exemption is `A "DB: none" build writes`; BASE lines that 537 (`:12`, `:65`, `:80-82`), 523 (`:105`) and 480 (`:17`, `:111`) replace are not exempt | FAIL (ISSUE 2) |
| 13 | no test holds a whole file, a whole fixed-file line equal to a commit, or a BASE literal | RF1, RF3, RF4 and RF5 tests pin by content. RF2 (4) names `<BASE>..HEAD` (NOTE 1) | OK |
| 14 | the stop line stays the finish signal (L71); the file carries only keys the stop line carries | `## NOT IN THIS JOB` keeps `desk-watch`, `desk-done`, `stop-guard`; no `FAILED` and no `SHADOW BUILT` file | OK |
| 15 | X3/X5 re-derived: where each gate proves the `.result` | `deploy-card.sh` (RF4) requires it committed and unchanged. `deploy-step0.sh` (`:741-749`) and `desk-launch.sh` (`:1446-1449`) prove the report only | FAIL (ISSUE 3) |
| 16 | readers of a BUILT / CHECK DONE line outside the gates (X1): `grep` over `ops/desk/*.sh` | `desk-launch.sh:1671` (pass-1 `house B: needed`), `:157`, `preflight.sh:169-176` read a CHECK DONE line and are not named in `## NOT IN THIS JOB` | OK (NOTE 3) |
| 17 | RESTARTS class home per row (K10) | RF1 `ops/desk/` operator script; RF2 `docs/` and `tests/`; RF3-RF5 `ops/desk/`, `tests/`: none | OK |
| 18 | overlap with 521, 523, 537, 546, 547, 549, 550 (`grep -o file:line` of each card) | none on `deploy-step0.sh:677-733`, `deploy-card.sh:483-507`, `desk-launch.sh:1450-1489`, `BUILD-HUB.md:109`, `CHECK-HUB.md:125`; the one overlap is `test_build_hub_no_clutter.py:57-60` with 523 H3 (3) (NOTE 2). 546 and 537 touch other lines of `deploy-card.sh` (`:38-39`, `:534-543`) and of `desk-launch.sh` (`:502-522`, `:541`, `:1727`), disjoint from this card's | OK |
| 19 | what blocks the card's own deploy | see NOTE 7 | OK |

## ISSUES

1. FAIL RF1 (3): the test forbids `>` in `result-read.sh`, and the `refuse()` shape RF1 requires (`gate.sh:67`) holds `>&2`. A conforming script is RED on its own test. Make the test forbid `>` except `>&2`, or have `refuse()` write with `1>&2` and exempt that string.
2. FAIL RF2 (5): the repaired test exempts only the `A "DB: none" build writes` line. Cards 537, 523 and 480 each replace a BASE line of `BUILD-HUB.md`, so each turns the new subsequence check RED when it lands, and brain R1472 says a test pins only the lines its own card changes. Exempt by content every line another open card replaces, or drop the BASE comparison. Keep the negative control that a hub missing a BASE line still fails.
3. FAIL RF3, RF5, RF5 (4): only RF4 proves that the `.result` is committed and unchanged. A hand-edited or uncommitted `.result` passes `deploy-step0.sh` P2 and `desk-launch.sh` P2 but is refused by `deploy-card.sh`, so the three gates disagree. Add the same proof to RF3 and RF5 (a committed `.result` at HEAD equal to the file), and add an "uncommitted .result" row to the RF5 (4) table.
4. NOTE: `deploy-step0.sh:702` and `desk-launch.sh:1479` still read `held_n` from the stop line. `deploy-card.sh:488` does so only when a fix report exists. A `.result` saying `held_unfixed=0` beside a stop line saying `held unfixed: 1` therefore gives different verdicts. State which wins and add the row to RF5 (4).
5. NOTE: `CLASS`, `INSTALL` and `RESTARTS` are not in the CARD.md header table. Card 550 owns that table; 537 carries the same keys.
6. NOTE: `tests/ops` has no `__init__.py`, so importing `Desk` from `test_deploy_step0.py` may fail. Copy the constructor if so (the card allows it).
7. NOTE (deploy blockers): `deploy-smoke-string-1014` (537) deploys first, as the one deploy at a time. This build does not start before card 523's recut lands. The deploy then waits for this card's own check, and for any 521, 523 or K5 siblings that are ahead of it in the desk's order. BASE, TIP, CHECK REPORT and HOUSE B are the desk's to fill.

NOTE 1: RF2 (4) names `git diff --stat <BASE>..HEAD -- tests/ops/test_hub_lines.py`. Run it as a builder command, not as a pytest assertion (a pytest assertion would pin a BASE literal). The kept test `test_the_launch_line_is_byte_identical_to_base` and the constant `BASE = "5e5fab02"` are existing and not edited.

NOTE 2: 523 must land before RF2. The card's own default says so. After 523 lands, `:57-60` is no longer the body (523 H3 (3) rewrites it), so the builder re-reads it (E3). RF2's rewrite must keep 523's two exemptions (the `FIX-ROUND REPORT (brain R1309):` line and the `§0 Headline` line), or ISSUE 2 recurs.

NOTE 3: add `preflight.sh:169-176`, `desk-launch.sh:157` and `:1671` to `## NOT IN THIS JOB` so X1 is closed.

PREFLIGHT DONE · card: result-file-1014 · checks: 19 · fails: 3 · ready: NO
