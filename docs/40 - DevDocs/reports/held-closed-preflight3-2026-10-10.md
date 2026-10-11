## CHECKS

Card `317` at HEAD `a7c1050d` (card last committed `69a432b0`). Read 2026-10-10 21:48 ET (`date`). `git diff --stat HEAD -- <card> ops tests` and `git diff --stat 26327808 HEAD -- ops tests` print nothing, so the working `ops/` and `tests/` are HEAD's and BASE's.

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff 52ff6771 69a432b0 --stat` (whole commit) | card 16 lines (9+, 7-); the other files are prompts 321/322, desk rows, reports; no `ops/`, `tests/`, `DEPLOY-HUB.md`, `CARD.md` | OK |
| 2 | `git diff 52ff6771 69a432b0 -U0 -- <card>` | hunks at lines 20-24 (THE RULE: FIXED LINES, new CARRIED LINES, new COVER, EACH NAMED TEST, REFUSED) and rows H1-H4 (lines 29-32) only. Header (1-11), WHY, NOT IN THIS JOB, READ, CHECK ASKS, RECORDS untouched. H1-H4 each differ by CARRIED additions; the file lists and the FIXED-only text stand | OK |
| 3 | CARRIED line form in THE RULE | `CARRIED: <finding id> — <test id> — R<n>`, one space each side of each em dash U+2014, `R<n>` = `R[0-9]+`, from column 0 | OK |
| 4 | strict-xfail test required | (a): file exists, `def <name>(`, a decorator in the contiguous `@…` lines above holds `xfail` and `strict=True`; non-xfail, non-strict, absent all refused; `pytestmark` does not satisfy | OK |
| 5 | DESK RECORD row required | (b): row `| R<n> |` of `reports/cto-<date>.md` (date of the check report's file name) carrying `DESK RECORD`; missing report, row, or marker refused naming the id | OK |
| 6 | exactly one FIXED or CARRIED line per held id | COVER: one line per id; two FIXED, two CARRIED, or one of each refused; unlisted id refused; mix allowed; check report never edited | OK |
| 7 | three suites carry the CARRIED tests with red-first lines | H1: happy, mix, six refusals (not xfail, non-strict, absent, row missing, no DESK RECORD, FIXED+CARRIED for one id), each "RED on `BASE`" with `returncode == 1` and the `:172` text. H2: happy and mix (PIN-shaped, red-first from refusals, "RED on `BASE` = the launch runs"), six refusals. H3: happy and mix RED on `P2 check 1 … lacks 'held unfixed: 0'`, six refusals naming the id | OK |
| 8 | DEPLOY-HUB P2 and CARD.md rows name CARRIED | H4(a) adds the `CARRIED: <finding id> — <test id> — R<n>` clause and the strict-xfail and `DESK RECORD` conditions to `:59`; H4(b) adds "a FIXED or CARRIED line per held id" to `CARD.md:48`; greps added for both | OK |
| 9 | `ls -la ~/.claude/ops/desk-launch.sh deploy-card.sh deploy-step0.sh` | all three `->` `/Users/cobalt/cobalt/ops/desk/<same name>` | OK |
| 10 | card committed, header | `git diff --stat HEAD -- <card>` empty; `git log` `69a432b0`, `52ff6771`, `07c0f79e`; BASE `26327808` (`merge-base --is-ancestor 26327808 HEAD` exit 0); TIP and CHECK REPORT empty; HOUSE B `as needed`; RULINGS `2026-10-10 R993` | OK |
| 11 | `grep -n -E "^\| R(993\|998) " reports/cto-2026-10-10.md` | line 10 `R998 … DESK RECORD (brain, L79) … card H takes CARRIED lines`; line 15 `R993 … DESK RECORD (brain, L79) … build launcher row H`. Both match the `| R<n> |` + `DESK RECORD` shape the rule reads. Card cites no line number of that file | OK |
| 12 | `deploy-card.sh` at HEAD (`grep -n`) | `:172` `held unfixed: 0`, `:173` `ready: YES`, `:180` `frep=`, `:183` `fblob=`, `:189` `flast` refusal, `:201` SHIPS row; fix-report block `:179-195` (`:194` last record line); 6 of 6 | OK |
| 13 | `desk-launch.sh` at HEAD (read `:944-975`) | `:907` `ships_checked`, `:946` `clast`, `:947-954` literal loop (`:949` exact `*"$lit"\|*"$lit "*`), `:955` `ltip`, `:959-972` `fixed_ok`, `:973` short-circuit, `:974` refusal; 7 of 7 | OK |
| 14 | `deploy-step0.sh` at HEAD (`grep -n`) | `:24` P2 header, `:337` `lits=`, `:340` prefix, `:367` `if [ -z "$why" ]`, `:371` `*"$lit"*` (substring), `:378` fix-round `if`, `:394` `BUILT ·`; 7 of 7 | OK |
| 15 | `DEPLOY-HUB.md:59`, `CARD.md:48` at HEAD | `:59` fix-round bullet ends "the literals are still read from the check report's last line."; `CARD.md:48` holds "the literals … are read from the CHECK report's last line"; unmodified; `wc -l` 181 and 139 | OK |
| 16 | H4 BASE counts | `grep -n "CARRIED\|FIXED:\|has no FIXED line"`: DEPLOY-HUB 3 lines (`:32`, `:118`, `:119`), all the bare word `CARRIED`, none `CARRIED:`, `FIXED:` or `has no FIXED line` (so the full-form greps are 0 on BASE and the card's choice of the full form is right); `CARD.md` 0 for all, so bare `CARRIED` → 0 on BASE, 1 after | OK |
| 17 | test anchors at HEAD | `test_deploy_card.py` `:40`/`:42` (`check_line`, `open: 0`), `:427-428`, `:442`, `:588-589`, `:598`; `test_deploy_step0.py` `:78`/`:80`, `:578`; `test_desk_launch_prechecks.py` `:68`/`:70`, `:198`, `:559`; 12 of 12 | OK |
| 18 | rows against the brain's CARRIED form (321 head, R998) | "a CARRIED line naming a strict-xfail test plus a recorded brain ruling": strict xfail required (a), recorded `DESK RECORD` row (b) | OK |
| 19 | n = 0 as today, pinned | pins unchanged in H1 (`test_no_fix_report_leaves_every_cell_empty`, `test_a_check_line_with_a_held_defect_is_refused`, `test_h1_held_check_without_a_fix_report_is_still_refused`), H2 (n = 0 fix-round launch, `test_a_fix_report_round_trips_…`), H3 (`test_f2_*`, five) | OK |
| 20 | held path before the tip short-circuit and outside the `$why` guard | HELD PATH bullet unchanged; code agrees (`desk-launch.sh:973` ORs `ltip = ctip` before `fixed_ok`; `deploy-step0.sh:367` guards on `$why`); tests `test_h2_a_held_check_at_the_code_tip_…` and `test_h3_a_held_check_at_the_code_tip_…` stay | OK |
| 21 | no new command, no `src/` or `configs/` (R411, R412) | NOT IN THIS JOB untouched; files lists unchanged | OK |
| 22 | L67 other-house read, RESTARTS none | H4 names house A (Grok); `ops/desk/` and `docs/` class homes in RECORDS (`restarts.py:225-226`, `:230-232`); unchanged by the amend | OK |
| 23 | the carried report's four decisions against the card | D1 static decorator read = rule (a); D2 `reports/cto-<date>.md` `| R<n> |` = rule (b), R993/R998 match (checked, #11); D3 DEPLOY-HUB full-form grep, CARD.md bare word = H4 greps and #16; D4 `:366`/`:367` note, see ISSUES | OK |
| 24 | amended card's new `## RECORDS` lines each with a command and time | the amend added NO line to the card's `## RECORDS` (diff #2); the reads are in the carried report's `## RECORDS` (commands, `21:46`/`21:47 ET`, `git diff --stat HEAD` empty). Re-proven here at 21:48 ET, #12-#17 | OK (see ISSUES) |

## ISSUES
- NOTE card `## RECORDS` (amend reads line) says the `why` guard is at `:366`; HEAD has `esac` at `:366` and `if [ -z "$why" ]` at `:367`. No H row cites `:366`. The carried report (D4) already says so; the builder may correct it when it quotes its reads.
- NOTE the amend added no line to the card's `## RECORDS` (the CARRIED reads and times sit in `held-closed-carried-2026-10-10.md`). The proofs hold (#12-#17); the card's own RECORDS still says "proven against HEAD `26327808`" (BASE, round 2 NOTE, unchanged).
- NOTE H2 and H3 name the CARRIED `pytestmark` case and `def` absent only in H1 (same remark as round 2: three shell copies, one suite each). Not a block.
- NOTE the F4 fix round's present line form `CARRIED: O1 — strict xfail, follow-up card` does not match `CARRIED: <id> — <test id> — R<n>`; its fix report must use the card's form (a test id and an `R<n>`), as R998 and prompt 321 say.

PREFLIGHT DONE · card: held-closed-1010 · checks: 24 · fails: 0 · ready: YES
