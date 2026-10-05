JOB: preflight-fixes
LADDER: OFF-LADDER — cto-2026-10-05.md R387
BRANCH: ops/preflight-fixes-1005
WORKTREE: preflight-fixes-1005
BASE: b56622fa
TIP:
REPORT: /Users/cobalt/cobalt-wt/preflight-fixes-1005/docs/40 - DevDocs/reports/preflight-fixes-build-2026-10-05.md
CHECK REPORT:
HOUSE B:
DB: none
RULINGS: 2026-10-05 R412

## ROWS

WHY: `ops/desk/preflight.sh` is stricter than the hub it serves; the hub, a fixed file, wins and the script is fixed here (`prompts/2026-10-05/00-brain-handover.md` lines 25 and 31). Three rows, one per fix. Each is derived from the hub text quoted in its row; neither hub file is edited.

| row | what | red first | files |
|---|---|---|---|
| F1 | SELF-CHECK BELOW 3 IS RECORDED, NOT FAILED. `ops/desk/preflight.sh:203-205` passes the `report` row only when the build report's last line carries `self-check: 3 of 3`. The hub: `BUILD-HUB.md:97` "A line you cannot back → fix it, or `self-check: <k> of 3` in the stop line with the gap under `## DECISIONS`"; `CHECK-HUB.md:61` "A lower self-check count is recorded and goes to the house as a fact." So a last line that starts `BUILT · job: <JOB> · tip: <TIP>` and carries `self-check: <k> of 3` (k one digit, 0–3) passes the `report` row; when k is below 3 the script also prints one line `report: self-check <k> of 3 (recorded)` after the row. A last line with no `self-check: <k> of 3` field, or not starting `BUILT · job: <JOB> · tip: <TIP>`, still fails `report` | in `tests/ops/test_preflight.py`: REWRITE `test_a_check_whose_report_is_short_of_three_self_checks_fails` (line 213) as `test_a_check_whose_report_is_below_three_self_checks_passes_and_records_it` (last line with `self-check: 2 of 3` → exit 0, last stdout line `PREFLIGHT OK`, stdout holds `report: self-check 2 of 3 (recorded)`); ADD `test_a_check_whose_report_has_no_self_check_field_fails` (the `GOOD_LAST` line with ` \| self-check: 3 of 3` cut out → exit 1, last line `FAILED PREFLIGHT: report`). RED on `BASE`: the first fails on `assert done.returncode == 0` (the script exits 1, `FAILED PREFLIGHT: report`); the second is green on `BASE` and stays green (a negative control, say so in the report) | `ops/desk/preflight.sh`, `tests/ops/test_preflight.py` |
| F2 | PASS-2 HEAD ROW. `ops/desk/preflight.sh:143-157` takes the card's `TIP` as the check's head reference. `CHECK-HUB.md:120` for a PASS-2 launch: "`<tip now>` = its `tip:`, and `git log --oneline -1` shows it (or a docs-only commit above it)", where "its" is pass 1's last non-blank line of `CHECK REPORT`, which "starts `CHECK DONE · job: <JOB> · pass: 1` and carries `house B: needed`". Pass 1's fixes sit above the card's `TIP`, so on a PASS-2 launch the `head` row fails. The fix, with NO new argument (`CHECK-HUB.md:8,61` calls `preflight.sh check "<card>"` for both passes): in a check, when the file `CHECK REPORT` exists and its last non-blank line starts `CHECK DONE · job: <JOB> · pass: 1` and carries `house B: needed`, the head reference is that line's `tip: <hex>` value (up to the next ` ·`) in place of the card's `TIP`: `head` passes when HEAD is that tip, or when only docs-only commits sit above it (the same `git log --stat` rule as today). Any other state (no report, another last line) keeps the card's `TIP` as today. The `range` and `report` rows still read the card's `TIP` | in `tests/ops/test_preflight.py`: ADD `test_a_pass_2_check_with_the_pass_1_tip_above_the_card_tip_passes` (a built branch; a `fix(x-job):` src commit above the card `TIP`; a CHECK REPORT at the card's `CHECK REPORT` path whose last line is `CHECK DONE · job: x-job · pass: 1 · tip: <that fix commit> · … · house B: needed · …`; the card's `TIP` stays the build tip → exit 0, `PREFLIGHT OK`). RED on `BASE`: `assert done.returncode == 0` fails, last line `FAILED PREFLIGHT: head`. ADD `test_a_pass_1_report_that_says_house_b_not_needed_keeps_the_card_tip` (same setup, `house B: not needed` → exit 1, `FAILED PREFLIGHT: head`), and `test_a_pass_2_check_with_a_src_commit_above_the_pass_1_tip_fails` (a further src commit above the pass-1 tip → exit 1, `FAILED PREFLIGHT: head`); both are negative controls, green on `BASE` for the same wrong reason as today, so each is also run against the fixed script and quoted green | `ops/desk/preflight.sh`, `tests/ops/test_preflight.py` |
| F3 | tests/ops/test_desk_launch_brain.py:285: the token was filled on his R54 approval (desk R358, commit 4a19b075); assert `INSTALL not in text` with the comment `# filled on his approval row (R358)`. Red: the line as it stands fails on main. | test `test_the_trees_brain_hub_line_is_printed_with_its_handover_filled`, assertion `assert INSTALL in text` (line 285): it fails on BASE `b56622fa`, because the hub title reads `installed 2026-10-05`, not the unfilled token | `tests/ops/test_desk_launch_brain.py` |

Each row ends with the deploy gate: `ops/desk/preflight.sh` is an `ops/desk/` script, so the card is DB: none (every file under `ops/` and `tests/ops/`), it takes no `cobalt_dev` lock, and the job's tip deploys only through the gate (`DEPLOY-HUB.md`, one feature per deploy, his R390): the gate runs `uv run pytest -q tests/ops/test_preflight.py` green on the combined tree before the merge.

## NOT IN THIS JOB
- `BUILD-HUB.md`, `CHECK-HUB.md` and every other fixed file: the hub wins and is not edited here (the hub text R375/R376/R389/R390 and the removal of the pre-merge (d2) line are a drafter's own card, R412).
- The PASS-2 rows the hub ADDS to PREFLIGHT (`CHECK-HUB.md:120`: the `tail -n 3` of `CHECK REPORT`, the `house B` probe): not mechanical rows of `preflight.sh`; not built here.
- Any other rule of `preflight.sh` (clock, status, M1 report line, diff, main repo, env rows, range) and any other file under `ops/desk/`.
- A new argument or a new command for `preflight.sh`: the hub's call stays `preflight.sh check "<card>"`.
- A red outside these three rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `ops/desk/preflight.sh` whole (header comment lines 1-25; `head` rows 128-158; `report` row 199-209).
- `docs/40 - DevDocs/prompts/BUILD-HUB.md` lines 93-97 (`## PRE-STOP SELF-CHECK`) and 105-109 (`## STOP LINE`).
- `docs/40 - DevDocs/prompts/CHECK-HUB.md` lines 60-61 (`## PREFLIGHT`, the self-check sentence at 61) and lines 119-120 (`## PASS 2`, the PREFLIGHT added).
- `tests/ops/test_preflight.py`: the helpers `built`, `write_card`, `preflight`, `GOOD_LAST` (lines 68-101) and the tests at lines 193-230.

## CHECK ASKS
- X1 Does `ops/desk/preflight.sh` differ from `BASE` only at the `report` row and the check's `head` row (and the header comment lines that describe them)? Quote `git diff <BASE>..<TIP> -- ops/desk/preflight.sh`.
- X2 F1: does a last line with no `self-check: <k> of 3` field, or one with `self-check: 4 of 3`, or another job's name, still fail `report`?
- X3 F2: is the pass-1 `tip:` read only when the last non-blank line of `CHECK REPORT` starts `CHECK DONE · job: <JOB> · pass: 1` and carries `house B: needed`; do a pass-1 launch (no report), a `CONTINUE` and a `FAILED` last line all keep the card's `TIP`?
- X4 Is every non-test line of the diff derived from a hub line quoted in its row, and nothing else changed (no new argument, no new command)?

## RECORDS
- Derived by the drafter 2026-10-05 from `BUILD-HUB.md:97,106` and `CHECK-HUB.md:61,120`; the brain's two items are `prompts/2026-10-05/00-brain-handover.md` lines 25 and 31.
- The build seat uses only the existing `ops/desk/` scripts and the commands on its allow line (his R411, R412); no row needs another command.
