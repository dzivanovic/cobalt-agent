# Card 462 `brain-replace-1013` — preflight (2026-10-13, Sonnet 5.5, read-only)

Card read at main HEAD `a4c92bb0`. `git diff HEAD --stat -- ops tests src` prints nothing: every `ops/` and `tests/` anchor below is HEAD's.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git -C /Users/cobalt/cobalt diff HEAD --stat -- "…/462-brain-replace-card.md"`; `git log --oneline -3 -- <card>` | diff empty; last commits `599e6f98`, `3391673a` | OK |
| 2 | `grep -n "«FILL" <card>` | one hit, line 7: `BASE: «FILL: BASE, …»` (the desk's placeholder; not a FAIL) | OK |
| 3 | `grep CLASS` of the card (Read, line 3) | `CLASS: K5` | OK |
| 4 | `RULINGS: 2026-10-12 R1138` (line 14); `grep -n "^\| R1138 \|" reports/cto-2026-10-12.md` | line 173: `HIS RULING · APPROVED … K1–K5` | OK |
| 5 | `desk-done.sh` anchors read at HEAD | `:2`, `:22` usage; `:14-17` header; `:23-33` kinds, `:32` `unknown kind`; `:34-45` stop-line read; `:46-61` agents read, `:57` `case $? in`; `:62-64` guard; `:65-71` step/stop/rm/tab; 71 lines | OK |
| 6 | `desk-launch.sh` anchors read at HEAD | `:150-156` and `:803-804` comments; `:220` REPORTS; `:233-237` committed; `:264` here; `:309` `rfile="$REPORTS/cto-$rdate.md"`; `:805` list; `:807-811` rows; `:813` refuse; `:814` run_launch | OK |
| 7 | `desk-launch.sh:730` and `desk-done.sh:57` as R1331 cites them | `:57` is `case $? in`; `:730` is the PROD-READ refuse in kind `prompt`. Neither is R76 text. The card says so and names `desk-done.sh:62-64` and `desk-launch.sh:803-813` | OK (NOTE 1) |
| 8 | the guards carry the old R76 text | `desk-done.sh:63` `…stopped only on his word (2026-09-30 R76)`; `desk-launch.sh:813` `…(2026-09-30 R76); launch its successor after he has stopped it` | OK |
| 9 | the rule's window (card line 20, D1, L1) | today's `cto-<D>.md` and yesterday's `cto-<D-1>.md`, ET, nothing older; D-2 cases in both scripts' tests | OK |
| 10 | what counts as an ask (card line 20) | a committed, unchanged line matching `^\| R[0-9]+ \|`, holding `DESK RECORD` and `` brain `<id>` asked for its replacement `` (`grep -F`); the card lists the five shapes that do not count; the backticked id rules out a prefix or extension | OK |
| 11 | an unasked brain refused before and after | D1 `test_d1_a_brain_with_no_ask_is_refused`, L1 `test_l1_a_brain_with_no_ask_is_refused` and `test_l1_two_brains_one_asked_is_refused`: R76 text, no call. Green on BASE (BASE refuses the kind / the live brain) and after | OK |
| 12 | 10-11 case red on BASE, green after | D1 `test_d1_the_10_11_ask…` fails on `returncode == 0` (`REFUSED: unknown kind: brain`, `:32`); L1 `test_l1_the_10_11_ask…` fails on `returncode == 0` (`:813`). R1102 and R1104 rows exist at `cto-2026-10-11.md:41` and `:39`; R1104 has no ask phrase, R1102's LAUNCHED shape is a decoy case | OK |
| 13 | each named test has a stated failing reason on BASE | red: D1 two tests, L1 three tests, each with its assertion; the other tests are covered by "the refused cases are green on BASE too". `test_l1_a_failing_desk_done_launches_nothing` is in neither list | OK (NOTE 2) |
| 14 | test-file anchors | `test_desk_done.py` `:19-25` AGENTS, `:164-171` `test_a_brain_or_the_desk_is_refused`; `test_desk_launch_brain.py` `:69-123` Desk, `:170-176`, `:179-188`; `:485` `test_p5_the_hubs_measure…` | OK |
| 15 | no new command on a seat's `--allowedTools` (R411, R412) | BUILD-HUB line 12 already holds `uv run pytest *`, `uv run cobalt jobs restarts *`, `sh /Users/cobalt/cobalt/ops/desk/*`, `git -C * diff*`, `Edit(//Users/cobalt/cobalt-wt/**)`; the brain stop runs inside `desk-done.sh`, no seat types `claude` | OK |
| 16 | RESTARTS class homes (`restarts.py`) | `:225-229` `docs/` → `DOCS`; `:230-234` `ops/desk/` → "operator script; no Cobalt reader"; `:245-246` `tests/` → "test/documentation; no resident"; all three named in `## RECORDS` line 65 and row R2; header `RESTARTS: none` | OK |
| 17 | FOR THE CHECK row 19 line, `grep -c -F` of the whole line | `1` | OK |
| 18 | FOR THE CHECK card 462 line, `grep -c -F` of the whole line | `1` | OK |
| 19 | `## DEPLOY PROOF` before values | `grep -c -F "card 462"` `desk-done.sh:0` `desk-launch.sh:0`; `grep -c -F "asked for its replacement" desk-done.sh` `0` | OK |
| 20 | install path | `ls -la /Users/cobalt/.claude/ops`: `desk-done.sh` and `desk-launch.sh` are symlinks into `/Users/cobalt/cobalt/ops/desk/`; `INSTALL: none` matches precedent `458-desk-refresh-card.md:4`, `RESTARTS: none` `:13` | OK |
| 21 | rule rows the card cites | `cto-2026-09-30.md:67` R76; `cto-2026-10-02.md:138` R131; `cto-2026-10-03.md:194` R188, `:197` R191; `cto-2026-10-13.md` rows R1331, R1332, R1334 | OK |
| 22 | brain's directions D1 D3 D4 D5 KEEP, D2 changed | R1332 row: "D1, D3, D4, D5 KEEP; D2 CHANGED, an ask in today's or yesterday's ET report counts" | OK |
| 23 | what blocks the card's own deploy | see NOTE 3 | OK |
| 24 | the quote of R1331 | see NOTE 4 | OK |
| 25 | other fences | `desk-list.sh` is 19 lines, unchanged; `## NOT IN THIS JOB` leaves `BRAIN-HUB.md`, kind `prompt`, `src/`, `configs/`, `.claude/` alone | OK |

## ISSUES

- NOTE 1: R1331's `desk-done.sh:57` and `desk-launch.sh:730` are shifted or wrong anchors; the card names the real guards (`desk-done.sh:62-64`, `desk-launch.sh:803-813`). Nothing to fix.
- NOTE 2: `test_l1_a_failing_desk_done_launches_nothing` has no stated BASE state. It is green on BASE unless it asserts the new text `REFUSED: desk-done.sh could not replace brain <id>`; the builder must assert that text, or the test pins nothing.
- NOTE 3: the card's deploy waits: one deploy at a time, and 304 goes first (OWED in `cto-2026-10-13.md`: 446 build `d590d2e9` BUILDING, then its check, row CR on 304, deploy 304). Card 446 also touches `ops/desk/desk-launch.sh` (`446-k5-gate-card.md:27`, `:62`): the line anchors for `desk-launch.sh` can shift when 446 merges, so the desk re-proves them at the BASE fill (build launches after 304 merges or on the BASE it picks). Card 458 (desk refresh) and card 448 (DML roles) also deploy after 304.
- NOTE 4: the "byte for byte" quote of THE ROW is the text of the drafter prompt `461-draft-brain-replace.md:5`; the R1331 row in the report holds a shorter summary of it. The quote is the brain's direction as the desk typed it to the drafter; nothing in the tests depends on the wording.
- NOTE 5: the new test helper in `test_desk_done.py` commits to a tmp git repo, and that file has no `GIT_ENV` (identity, hooks, global config) as `test_desk_launch_brain.py:30-37` does; the builder must set it. Both D-dates come from ET `now()`, so a run across 00:00 ET can flake.

PREFLIGHT DONE · card: brain-replace-1013 · checks: 25 · fails: 0 · ready: YES
