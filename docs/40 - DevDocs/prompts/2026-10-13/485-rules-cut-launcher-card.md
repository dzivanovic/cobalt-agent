JOB: rules-cut-launcher-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1341
CLASS: K5
INSTALL: none
BRANCH: ops/rules-cut-launcher-1013
WORKTREE: rules-cut-launcher-1013
BASE: «FILL: BASE, the desk's 8-hex main commit at the build launch»
TIP:
REPORT: /Users/cobalt/cobalt-wt/rules-cut-launcher-1013/docs/40 - DevDocs/reports/rules-cut-launcher-build-2026-10-13.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-cut-launcher-check-2026-10-13.md
HOUSE B: as needed
DB: none
RESTARTS: none
RULINGS: 2026-10-12 R1138

## ROWS

WHY: his ruling R1341 (`reports/cto-2026-10-13.md` R1341, R1344; direction file `## RULED 2026-10-13 — the rules cut list, all of it`: "the 25 stale lines … are deleted"). Map S1 (row 416; R438, 2026-10-05: a check has one pass, no `PASS-2`) and S23 (row 417; R686, 2026-10-08: the `PROD-READ:` stamp is read by no rule). The launcher still takes `PASS-2` and still stamps `PROD-READ:`; `preflight.sh` still reads a pass-1 line for a second pass. Every `file:line` is HEAD `7516154c`'s; cards 446 and 462 also change `ops/desk/desk-launch.sh`, so BASE is set after both merge and the builder re-proves each anchor at BASE by its text (the quoted code), recording the new numbers. In a cell, `\|` is ONE `|`.

| row | what | red first | files |
|---|---|---|---|
| L1 | PASS-2 RETIRED in `ops/desk/desk-launch.sh`. (a) The argument loop (`:951-963`): an argument `PASS-2` at position 3 or 4, for any kind, refuses `REFUSED: PASS-2 is retired: a check has one pass (his 2026-10-05 R438)` before anything runs; the variable `pass2` and the refusal `PASS-2 is an option of kind check only` go; the usage strings (`:358`, `:951`) drop ` [PASS-2]`. (b) Kind check (`:1540-1549`): the `if [ -n "$pass2" ] …` branch goes; a first launch (no step) whose CHECK REPORT exists refuses `the check report already exists: a new worker names its CONTINUE step`. (c) `:1563-1572` and `:1584-1589`: the `[ -z "$pass2" ]` conditions go (the built-line test and the first-launch tip test run on every launch they ran on before for a non-PASS-2 launch: the built line always; the tip test when no step). (d) `:2059-2062` (the `PASS-2. ` message prefix) goes. (e) The header comments `:4`, `:7`, `:19`, `:27`, `:59-60`, `:157-158`, `:196` drop the PASS-2 words; `:19`'s line goes whole | NEW in `tests/ops/test_desk_launch_prechecks.py`, section `# ---- card 485 L1`: `test_485_l1_pass_2_is_refused_for_every_kind` (parametrized `("check", "PASS-2")`, `("check", "PASS-2", "E3")`, `("check", "E3", "PASS-2")`, `("build", "PASS-2")`; the check cases with a CHECK REPORT ending `CHECK DONE · job: x-job · pass: 1 · house B: needed`: exit 1, stderr `REFUSED: PASS-2 is retired: a check has one pass (his 2026-10-05 R438)\n`, `desk.called() == []`). RED on BASE: `("check", "PASS-2")` exits 0 (it launches) and `("build", "PASS-2")` prints `PASS-2 is an option of kind check only`. CHANGED: `test_l2_a_pass_2_launch_keeps_the_test_it_has` (`:362`) is removed (its case is now L1's refusal); `test_x1_a_check_resume_or_pass_2_on_its_own_code_commits_launches` (`:521-530`) keeps its `("E3",)` case only and is renamed `test_x1_a_check_resume_on_its_own_code_commits_launches`; `tests/ops/test_desk_size_guard.py` drops the form `check PASS-2` (`:287-288`, `:297`, `:311`). `tests/ops/test_desk_launch_recut.py:325` stands (recut refuses any third argument before the loop) | `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py`, `tests/ops/test_desk_size_guard.py` |
| L2 | PROD-READ RETIRED in `ops/desk/desk-launch.sh` kind `prompt` (`:701-733`): the stamp is never appended (the comment `:701-707`, the `stamp=` block `:708-720` and the `*)` arm `:731-732` go; the `*PROD-READ:*)` arm `:723-730` becomes the one refusal below); a line that types `PROD-READ:` anywhere refuses `REFUSED: the launch line types PROD-READ:, a marker retired by his 2026-10-08 R686`. The header comment `:146-148` becomes `a line that types \`PROD-READ:\` (a marker retired by his 2026-10-08 R686);`. The kind's RULINGS reads that serve its write-string rule (cards f5-f7, `:1150-1254` of the tests) are not touched | `tests/ops/test_desk_launch_prechecks.py` section `# ---- card 21 guard-g2 R1` (`:1261-1470`) becomes `# ---- card 485 L2 (his 2026-10-08 R686): PROD-READ retired`: `test_r1_a_proven_row_stamps_the_launch_line` becomes `test_485_l2_a_proven_row_stamps_nothing` (`PROD-READ` absent from stdout and stderr, exit 0); every `test_r1_*typed_marker*` test becomes a refusal with the L2 text, the proving row present or not; `test_r1_a_row_that_proves_nothing_stamps_nothing`, `test_r1_a_disapproved_row_stamps_nothing`, `test_r1_production_ready_is_not_a_production_read` keep their asserts; `test_r1_an_uncommitted_prompt_is_refused` keeps its refusal. RED on BASE: `test_485_l2_a_proven_row_stamps_nothing` (BASE prints ` PROD-READ: 2026-01-02 R2` after `follow it exactly.`) and `test_r1_a_typed_marker_with_its_proving_row_launches_stamped_once` turned refusal (BASE exit 0). `tests/ops/test_bare_guard.py:539` (`MARKER`) stands: the guard reads no stamp (`bare-guard.py:990-1000`, R686) | `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_prechecks.py` |
| L3 | PASS-2 RETIRED in `ops/desk/preflight.sh`: the head reference of a check is always the card's `TIP`; the pass-1 read (`:168-189`, `# card 20 F2 (CHECK-HUB.md:120): on a PASS-2 launch …`) and its header lines `:15-17` (`a PASS-2 check (CHECK REPORT's last …) reads that line's \`tip:\` in place of TIP (card 20 F2)`) go | `tests/ops/test_preflight.py` section `# ---- card 20 F2` (`:335-387`) becomes `# ---- card 485 L3`: `test_a_pass_2_check_with_the_pass_1_tip_above_the_card_tip_passes` becomes `test_485_l3_a_pass_1_line_never_moves_the_head` (a CHECK REPORT ending `PASS1_LAST` with `house B: needed` and a src commit above the card's TIP: `FAILED PREFLIGHT: head`); `test_a_pass_1_report_that_says_house_b_not_needed_keeps_the_card_tip` stands; `test_a_pass_2_check_with_a_src_commit_above_the_pass_1_tip_fails` is removed (L3's test covers it). RED on BASE: `test_485_l3_a_pass_1_line_never_moves_the_head` passes the head row (BASE reads pass 1's `tip:`) | `ops/desk/preflight.sh`, `tests/ops/test_preflight.py` |
| L4 | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`; quote the table and the `RESTARTS:` line. Expected none: `ops/desk/` → "operator script; no Cobalt reader" (`src/cobalt/jobs/restarts.py:230-234`), `tests/` → "test/documentation; no resident" (`:245-246`) | — (output quoted) | none |

## NOT IN THIS JOB
- The deploy window gate in `deploy-step0.sh` and `deploy-outage.sh`, the brain-stop guards of `desk-launch.sh` and `desk-done.sh`, the wake-up's `awk` read and the 310k text: card 462 and the desk's own items (prompt 466), not here.
- `ops/desk/stop-guard.py` and `tests/ops/test_stop_guard.py:174-175` (a generic prefix test; the hook reads no `PASS-2`); `ops/desk/bare-guard.py` and `tests/ops/test_bare_guard.py`.
- Any other kind's logic in `desk-launch.sh`; the RESUME step rules; `card-fill.sh`, `deploy-card.sh`, `deploy-step0.sh`.
- The fixed files' `PASS-2` words: cards 479, 480, 481.
- Any file under `/Users/cobalt/Vault`; any `src/` or `configs/` file; any with-DB test (`DB: none`).

## READ
- `/Users/cobalt/cobalt/ops/desk/desk-launch.sh` lines 1-60, 140-200, 355-360, 690-740, 945-966, 1530-1595, 2050-2066.
- `/Users/cobalt/cobalt/ops/desk/preflight.sh` lines 1-30, 150-200.
- `/Users/cobalt/cobalt/tests/ops/test_desk_launch_prechecks.py` lines 355-372, 515-532, 1255-1475; `tests/ops/test_preflight.py` lines 330-390; `tests/ops/test_desk_size_guard.py` lines 280-320.
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rules-map-2026-10-13.md` S1, S23; rows 416, 417.

## CHECK ASKS
- X1 Can any argument shape still reach a launch with `PASS-2` in it (as a step, a third or fourth argument, under a kind other than check)?
- X2 Can any prompt line still be stamped, or launch while typing `PROD-READ:`?
- X3 Is every refusal and launch of kind check that does not name `PASS-2` the same as on BASE (the built line, the tip test, the existing-report refusal, a resume)?
- X4 Do all of `tests/ops/` pass, and is every removed or renamed test named in the build report with its reason?
FOR THE CHECK: rules cut 2026-10-13 HIS RULING: the whole cut list executed (13 contradictions, 25 stale, 40 duplicate groups deleted; moves as mapped; preferences to preferences.md; L82-L84 added, vetoable)
FOR THE CHECK: rules-cut cards 2026-10-13 brain: 11 KEEP; STANDING-LIST:107 deleted (CHECK-HUB wins, R1340); cards fill gaps behind MVP cards

## DEPLOY PROOF
- `grep -c -F "PASS-2 is retired" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1` or more
- `grep -c -F "pass2" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `8` (HEAD `7516154c`; re-read at BASE) · after `0`
- `grep -c -F "PASS-2" /Users/cobalt/cobalt/ops/desk/preflight.sh` · before `2` · after `0`

## RECORDS
- Reads by the drafter `draft-rules-cut-cards`, 2026-10-13 07:25-07:45 ET, at `main` HEAD `7516154c`; `git -C /Users/cobalt/cobalt status --short -- ops tests` printed nothing.
- `grep -n -E "PASS-2|PROD-READ|R686" ops/desk/desk-launch.sh`: `:4`, `:7`, `:19`, `:27`, `:59-60`, `:146-148`, `:157`, `:196`, `:358`, `:703-705`, `:717`, `:723-730`, `:951`, `:958`, `:963`, `:1542`, `:1546`, `:1549`, `:1562`, `:1583`, `:2060-2061`; `sed -n` of `1,30`, `140,200`, `695,735`, `945,966`, `1530,1590`, `2050,2066`.
- `grep -rn -c -E "PASS-2|PROD-READ" ops/desk`: `desk-launch.sh` 27, `preflight.sh` 2, every other script 0 (`bare-guard.py` 0; its `:990-1000` read R686 as "every seat, no stamp").
- `preflight.sh` `sed -n 10,20p` (`:15-17` the PASS-2 head note) and `160,190p` (`:168` the F2 branch).
- Tests naming `PASS-2` or `PROD-READ` (Grep of `tests/ops`): `test_desk_launch_prechecks.py:362-365`, `:521`, `:1261-1470`; `test_desk_launch_recut.py:325`; `test_desk_size_guard.py:287`, `:297`, `:311`; `test_preflight.py:335-387`; `test_stop_guard.py:174-175`; `test_bare_guard.py:539`.
- Card 446 (`446-k5-gate-card.md`) and card 462 (`462-brain-replace-card.md` rows L1) edit `desk-launch.sh`: BASE after both merge.
- `grep -n -F "pass2"` at HEAD: 8 lines, `:954`, `:958`, `:963`, `:1540`, `:1548`, `:1563`, `:1584`, `:2059` (so L1 (b)'s branch is `:1540-1549`).
