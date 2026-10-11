## CHECKS

HEAD `07c0f79e`; BASE `26327808`. `git diff --stat HEAD -- ops tests` prints nothing, so a working-tree read is HEAD's; `git show HEAD:<file>` was run for `deploy-card.sh`, `DEPLOY-HUB.md`.

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- <317 card>`; `git log --oneline -2 -- <317 card>` | empty; `07c0f79e` | OK |
| 2 | `git merge-base --is-ancestor 26327808 HEAD` (HEAD is `main`) | exit 0 | OK |
| 3 | header read | BASE `26327808`; TIP empty; CHECK REPORT empty; HOUSE B `as needed`; RULINGS `2026-10-10 R993` (comma form, one row) | OK |
| 4 | `grep -n -E "^\| R993 " reports/cto-2026-10-10.md` | line 8, `DESK RECORD (brain, L79)` | OK |
| 5 | `grep -n "cto-2026-10-10.md"` over the card | one hit, line 2, path with `R993`, no line number | OK |
| 6 | `deploy-card.sh` anchors | `:172`, `:173`, `:179-195` (block `:182-195`), `:201` all as cited (4 of 4) | OK |
| 7 | `desk-launch.sh` anchors | `:907` def, `:947-954` literal loop, `:959-972` `fixed_ok`, `:973-974` refusal, `:987` close (5 of 5) | OK |
| 8 | `deploy-step0.sh` anchors | `:24-31`, `:337`, `:340`, `:352-356`, `:368-376`, `:389-405` (6 of 6); `rel()` at `:129` | OK |
| 9 | `DEPLOY-HUB.md:59`, `CARD.md:48` | `:59` is the fix-round bullet and ends "the literals are still read from the check report's last line." (H4's insertion point); `CARD.md:48` holds the "literals `held unfixed: 0` and `ready: YES` are read from the CHECK report's last line" text (2 of 2) | OK |
| 10 | test anchors | `test_deploy_card.py` `:40`, `:47`, `:239`, `:442`, `:487`, `:581`; `test_deploy_step0.py` `:546`, `:578`, `:619`, `:637`, `:78`, `:204`; `test_desk_launch_prechecks.py` `:68`, `:163`, `:187`, `:195`, `:559`; `test_hub_lines.py` exists (17 of 17; `:426` is `:427-428`, see ISSUES) | OK |
| 11 | sample size | 34 anchors proven, over the 15 floor, every line of `:172-173`, `fixed_ok`, P2 read, `:59`, `:48` | OK |
| 12 | check report 298 | `## RUNS` `:68-72`, O1 row `:69` is the only `HELD, NOT FIXED` row there (count 1 = n); last line `held unfixed: 1 · open: 1 … ready: NO`, `tip: ed48d80d`; `:99`, `:106` are under `## OPEN`/`## DECISIONS`, excluded | OK |
| 13 | `## RECORDS` names every read | names the ls, HEAD, the cites, suites, precedents; misses a few (ISSUES) | OK |
| 14 | rows vs brain's row text (316 head) | FIXED grammar, every held id, tests at code tip not xfail, `ready:` satisfied, unnamed id refused naming it, check report never edited: all in THE RULE | OK |
| 15 | n = 0 unchanged and pinned | H1 `test_no_fix_report_leaves_every_cell_empty`, `test_a_check_line_with_a_held_defect_is_refused` (`:487`, `:239`); H2 n = 0 fix-round pin; H3 five `test_f2_*` pins | OK |
| 16 | tests exist for: n = 1 passes; missing id; missing test; xfail; two lines; unlisted id | all six in H1; H2 has four of six (no two-lines-per-id duplicate case named under refusals beyond "two lines for one id": present; no unlisted id); H3 has missing id, test, xfail, empty cell | OK (NOTE) |
| 17 | red-first on BASE, H1 | BASE `:172` refuses `held unfixed: 0`: happy path and every refusal RED on that text; the new text assertions differ | OK |
| 18 | red-first on BASE, H2 | BASE `fixed_ok` (`:959-972`) reads only the last line: a held row with a `BUILT · … tip: <code tip>` fix report PASSES on BASE; the happy-path test is green on BASE, and the stated RED text `the check's tip … is neither the code tip` is not what BASE prints | FAIL |
| 19 | red-first on BASE, H3 | BASE `:340` prefixes `held unfixed: 0`: `P2 check 1 — … the last line lacks 'held unfixed: 0'` is what BASE prints; refusals name the id and so differ | OK |
| 20 | `ls -la ~/.claude/ops/desk-launch.sh` (and `deploy-card.sh`, `deploy-step0.sh`) | all three `->` `/Users/cobalt/cobalt/ops/desk/<same name>`; builder edits the repo files | OK |
| 21 | no new command (R411, R412) | `deploy-card.sh` option list stands; no new script, option or seat | OK |
| 22 | H4 hub text reads | H4 names the L67 house read, house A (Grok) | OK |
| 23 | RESTARTS none, class homes | `ops/desk/` → `restarts.py:230-232` (`OPS_DESK_PREFIX` `:38`); `tests/ops/` → `:246`; `docs/` → `:225-226` (not named in the card, ISSUES) | OK |
| 24 | six decisions, each a stated default, rows consistent | D1..D6 each have `Default:`; H3 = D1, cell literals = D2, extraction = D3, static = D4, `open: <n>` = D5 (tightening), duplicates/unlisted refused = D6 | OK |
| 25 | D1 without H3 P2 refuses every held row | `deploy-step0.sh:340` prefixes `held unfixed: 0` to `$lits`, `:368-376` then fails `lacks 'held unfixed: 0'` for a last line `held unfixed: 1` | OK |
| 26 | THE RULE reaches a held row whose check tip equals the code tip | H2: `:973` is `[ "$ltip" = "$ctip" ] \|\| [ "$ltip" = "$shead" ] \|\| fixed_ok`; `fixed_ok` is the only place H2 adds the FIXED reads, and it is skipped when `ltip` is `ctip` or `shead`. H3: `:389` runs only when `$why` is set (tip differs). So a held check line (`held unfixed: 1`, `ready: NO`, tip = code tip) with a hand-written cell passes both with no FIXED line, no fix report; the card's own "n ≥ 1 with no fix report is refused" (line 19) does not hold in H2 and H3 | FAIL |

## ISSUES
- FAIL #18 (H2): the happy-path test is green on BASE, because `fixed_ok` already passes a `BUILT ·` report. Fix the card: list `test_h2_a_held_row_with_a_fixed_line_per_id_launches` as a pin (green before and after), and take red-first from the refusals (missing id, missing test, xfail, two lines: BASE launches, returncode 0). Drop the false BASE text.
- FAIL #26 (H2, H3; X3): the held path must run before the `ltip = ctip` / `ltip = shead` short-circuit in `ships_checked` and outside the `[ -n "$why" ]` guard in step0's P2, keyed on the check's last line (`held unfixed: <n>` n ≥ 1), not on the tip comparison. Add one red test each: held check, tip = code tip, no fix report → refused naming the id (RED on BASE: launches / passes).
- NOTE H2 refusal list: "the cell saying `held unfixed: 0` over a check line `held unfixed: 1`" is refused by the literal loop with no id in its text, and is green on BASE, so it is a pin, not an id-naming refusal.
- NOTE H2/H3 lack the unlisted-id case (H3 also the two-lines case): the id extraction and grammar are three separate copies in three shell scripts, so a case missing from one suite is an untested copy (X4). Consider the same two refusals in each suite, or one sourced helper.
- NOTE fixtures: all three `check_line` helpers (`test_deploy_card.py:40`, `test_deploy_step0.py:78`, `test_desk_launch_prechecks.py:68`) hard-code `open: 0`; the builder must add an `open` parameter for `open: 1` and the `open: ≠ n` refusal.
- NOTE H1: `frep` is read at `:180`, after the refusals at `:172-173`; the builder moves the `--fix-report` lookup before `:172` (the card's "when the job has a `--fix-report`" implies it).
- NOTE step0 `:371` matches a literal by substring (`*"$lit"*`), so `held unfixed: 1` also matches `held unfixed: 10`; the held path's `<n>` compare should be exact (boundary), as `deploy-card.sh:172` (`( |$)`).
- NOTE H4 test cite: `test_deploy_card.py` reads `CARD.md`/`DEPLOY-HUB.md` at `:427-428` and `:588-589`; the card says `:426`, `:589`. Off by one, harmless.
- NOTE `## RECORDS` does not name: `deploy-step0.sh:24-31`, `:359-367`, `:406-412` (read list only), `test_desk_launch_prechecks.py:555-600` (`fix_round`), the `docs/` class home (`restarts.py:225-226`) for the two hub files.

PREFLIGHT DONE · card: held-closed-1010 · checks: 26 · fails: 2 · ready: NO
