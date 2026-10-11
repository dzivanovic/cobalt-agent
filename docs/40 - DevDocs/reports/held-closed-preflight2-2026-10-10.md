## CHECKS

Card `317` at commit `52ff6771`. Read 2026-10-10 21:42 ET (`date`). HEAD had moved to `4a7f74eb` by the end of the run. `git diff --stat 26327808 HEAD -- ops tests` prints nothing, so BASE, the old HEAD and the current HEAD hold the same `ops/` and `tests/`. Every anchor below was read from `git show HEAD:<file>`, or from the working tree where it equals HEAD (empty `git diff --stat HEAD`).

Round 1 resolution (each FAIL and NOTE, by row of the amended card):

| # | round 1 item | where the amended card resolves it | OK/FAIL |
|---|---|---|---|
| 1 | FAIL 18, H2 happy path green on BASE | H2 red-first cell: "This is a PIN, green on `BASE` and after (`fixed_ok` already passes a `BUILT ·` report)"; the false BASE text is gone; RED comes from the refusals (missing id, missing test, xfail, two lines, unlisted id, tip = code tip) with "RED on `BASE` = the launch runs, `returncode 0`" | OK |
| 2 | FAIL 26, held path behind the tip short-circuit | THE RULE, HELD PATH bullet: "keyed on the check's last line alone … BEFORE the `ltip = ctip` / `ltip = shead` short-circuit … OUTSIDE the `[ -n "$why" ]` guard of step0's P2"; red tests `test_h2_a_held_check_at_the_code_tip_without_a_fix_report_is_refused` (H2) and `test_h3_a_held_check_at_the_code_tip_without_a_fix_report_fails_p2` (H3), each "RED on `BASE`: launches / P2 passes" | OK |
| 3 | NOTE H2 refusal list (`held unfixed: 0` over `1`) | H2: moved to "Pins, green on `BASE` and after … (refused by the literal loop on `BASE`, no id in its text)" | OK |
| 4 | NOTE unlisted-id and two-lines per suite | H2 lists a FIXED line for an unlisted id and two lines for one id; H3 lists both; H1 had both | OK |
| 5 | NOTE `check_line` hard-codes `open: 0` (3 helpers) | H1 (`:40`), H2 (`held_unfixed`, `open: 0`), H3 (`:78`) each say the helper gains an `open` parameter. Proven: `test_deploy_card.py:40,42`, `test_deploy_step0.py:78,80`, `test_desk_launch_prechecks.py:68,70` | OK |
| 6 | NOTE H1 `frep` read after `:172-173` | H1: "`frep` is read at `:180`, after the refusals at `:172-173`: move the `--fix-report` lookup before `:172`". Proven: HEAD `deploy-card.sh:180` `frep=`, `:172-173` refusals | OK |
| 7 | NOTE step0 `:371` substring match | THE RULE: "The `<n>` compare is exact … `held unfixed: 10` is not n = 1"; H3 adds "One test pins `held unfixed: 10` against n = 1 (`:371` …)". Proven: HEAD `deploy-step0.sh:371` is `*"$lit"*`. H2's literal loop (`:949`, `*"$lit"|*"$lit "*`) is already exact | OK |
| 8 | NOTE H4 test cite `:426`, `:589` | H4 now `:427-428`, `:588-589`. Proven: `test_deploy_card.py:427-428` (`CARD.md`, `DEPLOY-HUB.md`), `:588-589` | OK |
| 9 | NOTE `## RECORDS` misses reads | New line "Amend reads (card 319, 2026-10-10 21:41 ET, …)" names `deploy-step0.sh:24-31`, `:359-367`, `:406-412`, `test_desk_launch_prechecks.py:555-600`, and `restarts.py:225-226` (the `docs/` class home). It carries commands and the time. Proven: `restarts.py:225` `path.startswith("docs/")`, `:230` `OPS_DESK_PREFIX` | OK |

Checks again (round 1 list, `318`):

| # | command | output | OK/FAIL |
|---|---|---|---|
| 10 | `git diff --stat HEAD -- <317 card>`; `git log --oneline -3 -- <317 card>` | empty; `52ff6771` (amend), `07c0f79e` (draft). Card committed, clean | OK |
| 11 | `git merge-base --is-ancestor 26327808 HEAD` | exit 0 | OK |
| 12 | header read | BASE `26327808`; TIP and CHECK REPORT empty; HOUSE B `as needed`; RULINGS `2026-10-10 R993` (comma form); header and BASE untouched by the amend (`git diff 07c0f79e 52ff6771` touches no header line) | OK |
| 13 | `grep -n -E "^\| R993 " reports/cto-2026-10-10.md` | line 10: `DESK RECORD (brain, L79) … build launcher row H`. The card cites the row by id, no line number of `cto-2026-10-10.md` | OK |
| 14 | `deploy-card.sh` anchors at HEAD (`grep -n`) | `:172` `held unfixed: 0`, `:173` `ready: YES`, `:180` `frep=`, `:183` `fblob=`, `:201` SHIPS row; block `:179-195` (fix-report block); 5 of 5 | OK |
| 15 | `desk-launch.sh` anchors at HEAD (read `:900-991`) | `:907` `ships_checked`, `:946` `clast`, `:947-954` literal loop, `:959-972` `fixed_ok`, `:973-974` short-circuit and refusal, `:987` close; 6 of 6 | OK |
| 16 | `deploy-step0.sh` anchors at HEAD | `:24-31` header, `:337` `lits=`, `:340` prefix, `:352-356` dry list, `:359` P2, `:366` `[ -z "$why" ]` guard, `:368-376` literal loop (`:371` substring, `:374` `done <<EOF`), `:389-405` fix-round branch (`:394` `BUILT ·`), `:406-412` close; 9 of 9 | OK |
| 17 | `DEPLOY-HUB.md:59`, `CARD.md:48` | `:59` is the fix-round bullet and ends "the literals are still read from the check report's last line."; `CARD.md:48` holds "the literals `held unfixed: 0` and `ready: YES` are read from the CHECK report's last line". Neither holds `FIXED:` or `has no FIXED line` today, so the BASE counts 0 hold. Both files unchanged against HEAD | OK |
| 18 | test anchors at HEAD (`grep -n "def "`) | `test_deploy_card.py` `:40`, `:47`, `:239`, `:442`, `:487`, `:581`, `:598`; `test_deploy_step0.py` `:78`, `:546`, `:578`, `:619`, `:637`; `test_desk_launch_prechecks.py` `:68`, `:163` (`write_deploy`, holds `:174`), `:187` (`ship`, holds `:188`), `:559`; `test_hub_lines.py` and `restarts.py` exist; 20 of 20 (`:597` is `:598`, see ISSUES) | OK |
| 19 | sample size | 55 anchors proven, over the floor of 15; every line of `deploy-card.sh:172-173`, `fixed_ok`, the P2 read, `DEPLOY-HUB.md:59`, `CARD.md:48` | OK |
| 20 | `## RECORDS` names every read | Lines 57, 58, 59, 60 (new), 61 name the ls, the HEAD reads, the check report, the amend reads, the suites and RESTARTS. The new line (60) carries commands and `21:41 ET`; the `ls` line carries its time `21:36 ET` | OK |
| 21 | rows against the brain's row H text (`316` head, R993) | FIXED grammar `FIXED: <finding id> — <test id>`, every held id named, tests at the code tip and not xfail, `ready:` read as satisfied (`ready: NO` + `open: <n>`), an unnamed id refused naming it, the check report never edited: all in THE RULE and the three rows | OK |
| 22 | n = 0 as today, and a test pins it | H1 `test_no_fix_report_leaves_every_cell_empty`, `test_a_check_line_with_a_held_defect_is_refused`, `test_h1_held_check_without_a_fix_report_is_still_refused`; H2 n = 0 fix-round pin and `test_a_fix_report_round_trips_…`; H3 `test_f2_a_fix_round_row_passes_p2_and_step0` and four `test_f2_*` cases | OK |
| 23 | tests: n = 1 passes; missing id, missing test, xfail, two lines, unlisted id refused | H1 all six (plus `def` absent, `pytestmark`, count ≠ n, `open:` ≠ n); H2 all six; H3 all six plus empty cell. Each suite now carries the same six | OK |
| 24 | red-first on BASE, H1 | BASE `:172` refuses `held unfixed: 0`, so the happy path and every refusal are RED on `REFUSED: alpha: the check's last line lacks 'held unfixed: 0'`; each refusal asserts its own new text | OK |
| 25 | red-first on BASE, H2 | Happy path stated a PIN. Refusals: BASE `fixed_ok` reads only the last line and a `BUILT ·` report passes, so the launch runs, `returncode 0` → RED (missing id, missing test, xfail, two lines, unlisted id). Tip = code tip, no fix report: BASE short-circuits at `:973` → launches → RED | OK |
| 26 | red-first on BASE, H3 | Happy path RED on `P2 check 1 — … the last line lacks 'held unfixed: 0'` (BASE `:340` prefix). Id-naming refusals fail on BASE with the same text, which differs from the asserted id text → RED. Tip = code tip, no fix report: BASE `:366` guard passes it → P2 passes → RED. `held unfixed: 10` test: a pin against n = 1 | OK |
| 27 | held path before the short-circuit and outside the `$why` guard | THE RULE says so, and the code confirms the need: `desk-launch.sh:973` ORs `ltip = ctip` before `fixed_ok`; `deploy-step0.sh:389` runs only when `$why` is set (it is empty when the tip equals the code tip) | OK |
| 28 | `ls -la ~/.claude/ops/desk-launch.sh`, `deploy-card.sh`, `deploy-step0.sh` | all three `->` `/Users/cobalt/cobalt/ops/desk/<same name>`; the builder edits the repo files | OK |
| 29 | no new command (R411, R412) | `deploy-card.sh` option list stands (`NOT IN THIS JOB`); no new script, option or seat | OK |
| 30 | H4 hub text, L67 other-house read | H4: "This hub text rides the L67 house read: the check's house A (Grok) reads it"; `wc -l` unchanged; `grep -c` lines with BASE → 0 | OK |
| 31 | RESTARTS none, class homes | `ops/desk/` → `restarts.py:230-232` ("operator script; no Cobalt reader", `OPS_DESK_PREFIX` `:38`); `tests/ops/` named in `## RECORDS`; `docs/` → `:225-226`, now named | OK |
| 32 | the six decisions (drafter) and the amend's seven | drafter D1..D6 each keep a stated default and the rows still match (H3 = D1, cell literals = D2, extraction = D3, static = D4, `open: <n>` = D5, duplicates and unlisted refused = D6); the amend's D1..D7 each land in a row (D1 H2, D2 THE RULE, D3 H2 pin, D4 H2/H3 cases, D5 `open` and `frep`, D6 exact `<n>`, D7 H4 cites and RECORDS) | OK |
| 33 | D1 without H3: P2 refuses every held row | `deploy-step0.sh:340` prefixes `held unfixed: 0` to `$lits`; `:368-376` fails a last line with `held unfixed: 1`. H3 is needed | OK |
| 34 | CHECK ASKS X1-X5 present and answerable | X1 n = 0 byte for byte, X2 job and id named, X3 bypass cases (space in id, ASCII hyphen, indented), X4 three readers the same, X5 P2 refuses the H1 row without H3; each has a row and a test behind it | OK |

## ISSUES
- NOTE `## RECORDS` line 58 says "proven against HEAD `26327808`": that is BASE, not HEAD (HEAD was `07c0f79e`, now `4a7f74eb`). The claim holds, because `git diff --stat 26327808 HEAD -- ops tests` prints nothing, but the line names no time. It is an old line, not one the amend added; the builder may fix it when it quotes its reads.
- NOTE H2 cites `tests/ops/test_deploy_card.py:597` for `DESK_LAUNCH_DRY=1`; the line is `:598`. Harmless.
- NOTE THE RULE's `ready:` not `NO` refusal and the `HELD, NOT FIXED` count ≠ n / `open:` ≠ n refusals have a test in H1 only (count and `open:` listed; `ready:` is covered there by today's `:173` text). H2 and H3 are three separate shell copies of the same read, so a case in one suite is an untested copy in the other two (X4). The check may ask for the same three in H2 and H3, or accept the H1 cases as the pin. Not a block.
- NOTE H2 and H3 name the `xfail` case once each (a decorator or one form); the `pytestmark` form and the `def` absent case are named only in H1. Same remark.

PREFLIGHT DONE · card: held-closed-1010 · checks: 34 · fails: 0 · ready: YES
