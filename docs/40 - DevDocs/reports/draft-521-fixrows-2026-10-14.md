# draft-521-fixrows — 2026-10-14

## §0 Headline
- Rows FR-O2 and FR-O3 added to card 521 (`prompts/2026-10-13/521-gate-tests-ops-card.md`), after T2; no existing row, header value or section touched.
- FR-O2: the two BUILD-HUB sentences (`:80`, `:82`) + A1's test. The no-clutter test already exempts both lines by content (548 RF2), so it is green before and after; the row edits its comments only.
- FR-O3: gate.sh needs no logic change. A check's W types T2's `--deploy-gate` (`CHECK-HUB.md:113`, `:127`). The `DEPLOY-HUB.md:100` clause edit is fenced, so it is held as ASK DESK 1.
- Nothing run; every read is a `git show`, `git grep` or file read.

## DECISIONS
1. ASK DESK: `DEPLOY-HUB.md:100` (THE EQUAL-TREE CLAUSE) needs ONE edit and is fenced by the card's `## NOT IN THIS JOB` ("any other line of … DEPLOY-HUB.md (but 101 and 102)"; `:100` is neither; main's two lines are now `:102` and `:103`). Without it, a single with-DB branch whose check ran before 521 deployed, or without `--deploy-gate`, reuses the check's three suite lines and `tests/ops` never runs. DEFAULT (not written into the row): in `:100`, after "AND the check's stop line carries a with-DB count above 0" add "AND its `## Suites` offline line sits under `tests/ops: run (deploy gate)`"; the clause then reads "otherwise the gate runs whole". A test pins it (`DEPLOY-HUB.md:100` holds `tests/ops: run (deploy gate)`). Desk: approve to add it as a third row FR-O3b, or widen the fence. [23:50 ET]
2. ASK DESK: the brain asked that `test_build_hub_no_clutter.py` pin "never a whole line against a BASE hash". On main, 548 RF2 (R1472) already does that for the two lines this card edits (`EXEMPT` `:66`, `:68`, by leading words); the file still reads every OTHER BASE line from `BASE = "5e5fab02"` (`:15`, `:88`). DEFAULT: KEEP; FR-O2 edits comments only. Say so if the whole BASE read is to go; that is a rewrite of the file, not a mechanical row. [23:50 ET]
3. ASK DESK: how gate.sh knows "a check's W" (no new option, R411 and R412): DEFAULT taken in the row: the check types `--deploy-gate` (`CHECK-HUB.md:113` call, its DB: none sentence, and `:127`'s fix-round gate). A DB: none check then runs `offline --deploy-gate`. [23:50 ET]

## RECORDS
Reads at main HEAD `364b0c6d` (`git -C /Users/cobalt/cobalt rev-parse --short=8 HEAD`) unless stated; `git status --short -- ops tests` and the three hub files: empty (working tree equals HEAD).
- `git show HEAD:ops/desk/gate.sh`, the whole file: usage `:95`, `deploy=""` `:109`, `copy_on=""` `:110`, `--deploy)` `:130`, `--copy)` `:131`, refusal `:137`, tuple `:181`, `OFFLINE=` `:207`, `do_offline` `:556`, dispatch `:685`, `:688`. No `--deploy-gate`, no `OFFLINE OPS`, no `tests/ops` line. Gate header `:2` names no `--copy`.
- `git grep -c -F -e "tests/ops: skipped (no ops paths)" -e "--deploy-gate" -e "OFFLINE OPS" HEAD -- ops/desk/gate.sh ops/desk/gate-lists.md BUILD-HUB.md DEPLOY-HUB.md CHECK-HUB.md` → no output (zero in each).
- `git show 9bf45ac3:ops/desk/gate.sh` (the check's tip): `:2`, `:72`, `deploy_gate=""` `:87`, `--deploy-gate)` `:108`, refusal `:118`, tuple `:162`, `OFFLINE_OPS=` `:189`, `ops_reason` `:409` (`:411` the `deploy gate` branch), `do_offline` `:420`. Its header MODES block holds no `--deploy-gate` entry. `9bf45ac3:ops/desk/gate-lists.md` holds `## OFFLINE OPS`.
- `git grep -n HEAD -- BUILD-HUB.md`: `:65` (E0), `:80` (a0), `:81` THE GATE ONE CALL, `:82` (a) OFFLINE; none holds a `tests/ops:` sentence.
- `git grep -n HEAD -- DEPLOY-HUB.md`: `:100` THE EQUAL-TREE CLAUSE (text read: `otherwise the gate runs whole (--deploy)`), `:101` (a0) THE EARLY READ, `:102` THE GATE, ONE CALL (`all --deploy`, no `--deploy-gate`), `:103` (a) OFFLINE. `9bf45ac3:` `:102` is the call with `--deploy-gate`.
- `git grep -n HEAD -- CHECK-HUB.md`: `:113` the check's W call (`all --deploy …`) and its DB: none sentence, `:127` the fix round's "gate.sh with --deploy". `git grep -c -F "Bash(sh /Users/cobalt/cobalt/ops/desk/*)" HEAD -- CHECK-HUB.md` → `2`.
- `git show HEAD:tests/ops/test_build_hub_no_clutter.py`, whole: `BASE` `:15`, `EXEMPT` `:61-72` (`:66` a0, `:68` (a)), `unmatched` `:75`, `test_no_other_line_changes_from_base` `:88`, negative control `:103`.
- `git grep HEAD -- tests`: only `test_build_hub_no_clutter.py:66,:68` and `test_gate.py:143` name the (a0) or (a) lines.
- `reports/gate-tests-ops-check-2026-10-13.md` lines 140-214 (O2 `:149`, `:156`, `:193`, `:201`; O3 `:150`, `:157`, `:194`, `:202`; A1 `:151`) and `<S>/house-a.md` (the A1 test, lines 5-12), whole.
- `git grep HEAD -- src/cobalt/jobs/restarts.py`: `:38` `OPS_DESK_PREFIX`, `:230-232` "operator script; no Cobalt reader", `:246` "test/documentation; no resident". `:225-228` (`DOCS`) is taken from the card's own records, not re-read here.
- Not read: `tests/ops/test_hub_text_1013.py`, `tests/ops/test_db_copy_1014.py`, `tests/ops/test_check_hub_gate_wording.py` (named as pins the builder runs, not proven here); `test_gate.py` at the tip only through grep (`:844`, `:868`, `:877-879`, `:978`).
- Card 574 `RESTARTS`: all of the row's paths are `none`.

DRAFTED · decisions: 3
