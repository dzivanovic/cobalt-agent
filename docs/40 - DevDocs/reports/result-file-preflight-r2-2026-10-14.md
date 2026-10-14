# Card 548 `result-file-1014` — preflight round 2 (2026-10-14, read-only)

Read at `main` HEAD `bbeed8af`. The card is `00921627`. No test was run.

Round 1's three FAILs (`reports/result-file-preflight-2026-10-14.md`): RF1 (3) and RF3/RF5 are repaired. RF2 (5) is repaired only in part: it still fails (ISSUE 1). A new FAIL turned up in RF4 (ISSUE 2).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff --stat HEAD -- <548 card>` · `git log --oneline -3 -- <548 card>` | diff empty; commits `00921627` (amend), `32687899` | OK |
| 2 | `grep -c "«FILL" <548 card>` | `0` | OK |
| 3 | header vs `CARD.md` (build): JOB, LADDER, BRANCH, WORKTREE, BASE, TIP, REPORT, CHECK REPORT, HOUSE B, DB, RULINGS | all present. Empty: BASE, TIP (the desk's), CHECK REPORT, HOUSE B (filled at the check). No other placeholder. CLASS, INSTALL, RESTARTS are not in the `CARD.md` table (NOTE 6) | OK |
| 4 | RF1 (3), round-1 FAIL: `gate.sh:67-68` vs the test | `refuse()` is `printf 'REFUSED: %s\n' "$*" >&2`; the card now says no `>` "once every `>&2` is removed". A conforming script passes its own test | OK (NOTE 4) |
| 5 | RF1 (1), (2), (3): red reason on BASE | script absent → `sh` exit 127, not 0 / not 1. Keys: 15 build + 22 check, each one a stop-line field of `BUILD-HUB.md:108` / `CHECK-HUB.md:124` | OK |
| 6 | RF2 (5), round-1 FAIL: the EXEMPT list vs BASE lines the open cards replace. `grep -n -E '^<prefix>'` of every prefix on `BUILD-HUB.md` | each of the 9 prefixes matches at the card's line (`:12`, `:17`, `:65`, `:80`, `:81`, `:82`, `:105`, `:109`, `:111`). Cards 537, 523, 480 and 521 are covered. Card 547 (now in `prompts/2026-10-14/`) edits `BUILD-HUB.md:83` `- (b) THE LOCK`: not exempt | FAIL (ISSUE 1) |
| 7 | RF2 (1)-(4), other pins on the two hub lines: `grep` over `tests/` for the `:109` and `:125` sentences; `test_check_hub_gate_wording.py:67`, `test_check_hub_shadow.py:93` | no test pins either sentence. `:125` is appended to, no line added; the pinned `- THE MECHANICAL ROWS` bullet is another line | OK |
| 8 | RF2 (5) negative control and the red first | `test_build_hub_no_clutter.py:57-60` is the whole-file equality to `BASE = "5e5fab02"`; any hub edit gives `1 failed`; the negative control (a BASE line deleted from a copy stays RED) is named | OK |
| 9 | RF3, round-1 FAIL: `deploy-step0.sh` anchors | `:69` HERE, `:132` rel, `:657` clean pair, `:677-733` P2, `:679`, `:686-694`, `:706`, `:721`, `:741-749` all as written; read-only blob proof (`ls-files`, `rev-parse HEAD:`, `hash-object`) is allowed by the script's header | OK |
| 10 | RF3 (7) and the committed proof | RF3 now proves the check's `.result` committed and unchanged before any key is read; test (7) is a negative control with a stated red on BASE | OK |
| 11 | RF4: `deploy-card.sh` anchors `:477-482`, `:483`, `:488`, `:490-491`, `:493-494`, `:501`, `:504-507`, `:524`; `dirname "$0"` | all as written. The script has no `HERE`; `dirname "$0"` is at `:127` and in `desk-launch.sh:369`. The held read is `:488`: `[ -z "$frep" ] \|\| hn=$(held_n "$last")` | OK |
| 12 | RF3 / RF4 / RF5 on the input "stop line `held unfixed: 1`, clean `.result`, NO fix report" (X5) | `deploy-step0.sh:702` runs `held_rule` on the stop line → refused. `desk-launch.sh:1479` takes `hn=1` → refused. `deploy-card.sh:488` leaves `hn` empty with no fix report, and RF4 reads the file → written. The three gates differ; RF5 (4) has no such row | FAIL (ISSUE 2) |
| 13 | RF5: `desk-launch.sh` anchors `:264` here, `:1446-1449`, `:1450-1459`, `:1469-1473`, `:1479`, `:1450-1489`; RF5 (4) table rows | all as written; table now holds uncommitted and edited-after-commit rows. Harness `test_desk_launch_prechecks.py:561`, `:566`, `:1070` all as written | OK |
| 14 | test fixtures: `test_deploy_step0.py:78`, `:85`, `:238`; `test_deploy_card.py:40`, `:47`, `:155`, `:232` | all as written. `tests/ops` has no `__init__.py` (`conftest.py` only): the card allows copying the constructor (NOTE 7) | OK |
| 15 | red test names its failing reason on BASE, every row | RF1 exit 127; RF2 count 0, `1 failed`; RF3 `lacks 'held unfixed: 0'`, `P2 passes`, `fix report … does not end 'BUILT ·'`; RF4 `lacks 'held unfixed: 0'` / written; RF5 `its stop line lacks … — the check is not clean` / launches; RF6 RUN | OK |
| 16 | no test pins a whole file, a whole fixed-file line equal to a commit, or a BASE literal | RF1, RF3-RF5 pin by content. RF2 (5) reads `base_lines()` by the existing `BASE` constant, as brain R1472 allows. RF2 (4) names `git diff --stat <BASE>..HEAD`: it must be a builder command, not an assertion (NOTE 3) | OK |
| 17 | the stop line stays the finish signal (L71); the file is additional | `desk-watch.sh:40-44` and `desk-done.sh:24-31` end on the stop line and are named in `## NOT IN THIS JOB`; no `.result` on `FAILED` or `SHADOW BUILT` | OK |
| 18 | the file carries only keys the stop line carries | 15 build keys and 22 check keys, one per field. `env` = `.env` is an explicit exception to the `.`→`_` rule (NOTE 5) | OK |
| 19 | each row's files hold its RESTARTS class home (K10): `restarts.py:225-228`, `:230-234`, `:245-246` | `docs/` → DOCS; `ops/desk/` → operator script, no reader; `tests/` → no resident. RF6 expects none | OK |
| 20 | overlap with 521, 523, 537, 546, 549, 550 and 547 (`grep -o file:line` of each card) | 546: `deploy-card.sh:38-39`, `desk-launch.sh:502-522, 541, 1727`, `BUILD-HUB.md:80, 105`; 537: `deploy-card.sh:29-31, 534-543`, `desk-launch.sh:994`; 547: `desk-launch.sh:1003, 1082-1089, 2119-2121`, `BUILD-HUB.md:8, 12, 81-83, 87`, `CHECK-HUB.md:10`; 521: `desk-launch.sh:135-138, 2174-2189`, `BUILD-HUB.md:12, 65, 80-82`; 523: `desk-launch.sh:199`, `BUILD-HUB.md:105, 111, new :112`; 549, 550: none. None touches `deploy-step0.sh:677-733`, `deploy-card.sh:483-507`, `desk-launch.sh:1450-1489`, `BUILD-HUB.md:109`, `CHECK-HUB.md:125`. The one shared body is `test_build_hub_no_clutter.py:57-60` (523 H3 (3)); the shared effect is ISSUE 1 | OK (ISSUE 1) |
| 21 | X1: readers of a BUILT or CHECK DONE line outside the three gates | `card-fill.sh:71`, `preflight.sh:251`, `desk-launch.sh:1693` are named. `preflight.sh:169-176`, `desk-launch.sh:157` and `:1671` (`house B: needed`) are not (NOTE 2) | OK (NOTE 2) |
| 22 | what blocks the card's own deploy | NOTE 8 | OK |

## ISSUES

1. FAIL RF2 (5): the EXEMPT list omits `` - (b) THE LOCK `` (`BUILD-HUB.md:83`), the BASE line card 547 H1 replaces (547 is now committed). Whichever of 547 and 548 lands second turns the repaired `test_no_other_line_changes_from_base` RED; if 547 lands first, RF2's own "GREEN after the edit" step fails. Add the prefix `` - (b) THE LOCK `` to EXEMPT.
2. FAIL RF4 / RF5 (4) / X5: `deploy-card.sh:488` reads `held_n` only when a fix report exists, so a stop line saying `held unfixed: 1` beside a `.result` saying `held_unfixed=0` (no fix report) is written by `deploy-card.sh` but refused by `deploy-step0.sh:702` and `desk-launch.sh:1479`. RF4 must take `held_n "$last"` regardless of `frep` when a `.result` exists (a held line then keeps today's refusal), and RF5 (4) needs that row.
3. NOTE RF2 (4): state that `git diff --stat <BASE>..HEAD -- tests/ops/test_hub_lines.py` is a builder command with its output quoted, not a pytest assertion (an assertion would pin a BASE literal).
4. NOTE RF1 (3): the test forbids the substrings `git `, `rm ` and `curl`. `rm ` also matches `form `, `perform `, `confirm `, and "no git" would match `git `: the header comment must avoid those words.
5. NOTE: the key rule says `.` → `_`, so `.env` would be `_env`; the card's explicit `env` = `.env` wins. Say so in RF1's header comment.
6. NOTE: `CLASS`, `INSTALL` and `RESTARTS` are not in the `CARD.md` header table (card 550 owns the table; 537 carries them too).
7. NOTE: `tests/ops` has no `__init__.py`; copy the `Desk` constructor rather than import it. Also RF3 "`lits` holds only the clean pair": `deploy-step0.sh:657` prepends the pair to the row's own, so the test is "every line of `lits` is one of the two", not a count.
8. NOTE (deploy blockers): (a) `deploy-smoke-string-1014` (537) deploys first (one deploy at a time). (b) The build waits for card 523's recut: `deploy hub-text-1013` was rolled back (`de2965d9`, `cdf2233c`), so 523 H3 (3) and the FR-T1 fix are not on `main`. 523 must land first: RF2 rewrites the body of the test 523 H3 (3) repairs, and keeps 523's two exemptions (`FIX-ROUND REPORT (brain R1309):` and `§0 Headline`). (c) The deploy waits for this card's own check. (d) 546's edits to `deploy-card.sh:38-39` shift lines before `:483`: RF3-RF5 re-read by content (E3). (e) BASE, TIP, CHECK REPORT and HOUSE B are the desk's.

PREFLIGHT DONE · card: result-file-1014 · checks: 22 · fails: 2 · ready: NO
