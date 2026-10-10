# ops-hand install card 306 — preflight, 2026-10-10 (read-only)

Read against `HEAD` `1449bb1e`; card `BASE` `936c9b1e`. `git diff 936c9b1e HEAD --stat` touches only 306, 307, the day report, the words file and the drafter report: `OPS-HAND.md`, `STANDING-LIST.md`, `ops/desk/*` and `tests/ops/*` are unchanged since `BASE`.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `git diff HEAD --stat -- <306 card>`; `git log --oneline -2 -- <306 card>` | empty; `1449bb1e docs(desk): R972 ops-hand install card 306 drafted, preflight 307` | OK |
| 2 | header read: `grep -n "«FILL" <card>` | no `«FILL` in the header (only the `OPS-HAND` `«INSTALL` text in OLD blocks and prose). `BASE: 936c9b1e` is filled; `TIP:`, `CHECK REPORT:`, `HOUSE B:` are empty, as CARD.md `:18-21` marks them | OK |
| 3 | `RULINGS: 2026-10-10 R969` vs CARD.md `:23` and `desk-launch.sh:253-260, :843-844` | comma form, one item `<date> R<n>`, no space form | OK |
| 4 | R969 row: `grep -n R969 reports/cto-2026-10-10.md` | `:10 \| R969 \| … HIS RULING · APPROVED: "Approved" …` (R971 `:8` also `HIS RULING · APPROVED`, "confirms R969"); `git diff HEAD` of the report and words file empty (committed) | OK (row form) |
| 5 | card anchor "R969 is `reports/cto-2026-10-10.md:8`" (I1, RECORDS) | `:8` is R971; R969 is `:10` at `HEAD` | FAIL |
| 6 | H4 anchors `desk-launch.sh` `:628`, `:633-634`, `:636-638`, `:663-673`, `:704-705` | all match: `:633` `if grep -q '«INSTALL' "$fixed"; then`, `:634` `refuse "OPS-HAND.md still carries its «INSTALL token …"`, `:636-637` one `^claude --bg ` line, `:638` `line=$(…)`, `:673` allow set `Bash(launchctl print *)\|Bash(pgrep *)\|Bash(ps *)\|SendMessage\|`, `:704-705` shape | OK |
| 7 | H4 reads the title? `Read` of `:628-705` | the only title read is the token grep `:633`; every later gate reads `$line` alone. A title without `«INSTALL` passes | OK |
| 8 | `authorize.sh` `:148`, `:173-183`; `grep -n "OPS-HAND\|ops-hand" authorize.sh` | `:148` `grep -n -E "«INSTAL[L]" "$fixed"`; `:176` `i = index($0, "INSTALL: ")`, `:183` row `the title names no INSTALL: <date> R<n>`; no `OPS-HAND`/`ops-hand` match, so it never reads this title | OK |
| 9 | I1 OLD vs `git show HEAD:…/OPS-HAND.md` line 1; `wc -l` | OLD is byte-for-byte line 1 (`… R855) «INSTALL: his row»`); 22 lines; NEW holds no `«`, `<`, `>` | OK |
| 10 | OPS-HAND anchors `:14` class, `:16` bound, `:20` launch line | `:14` THE CLASS, `:16` THE BOUND, `:20` the `claude --bg` line, `:22` `No --add-dir` | OK |
| 11 | I2 vs `OPS-HAND.md:20`, string by string | allow: `Bash(ps *)`, `Bash(pgrep *)`, `Bash(launchctl print *)`, `SendMessage` (4, I2 lists them in another order; H4 sorts them, `:668-673`); deny: the 17 in the same order as the line (`AskUserQuestion` … `Bash(sudo *)`); `--model claude-sonnet-5-5`, `--permission-mode default`, `--remote-control ops-hand --name ops-hand`, no `--add-dir` | OK |
| 12 | I2 block line count | blank, heading, blank, NEW para, blank, 6 table lines, blank, Deny = 13 | OK |
| 13 | STANDING-LIST anchors: `wc -l`; `:5`; `:148`, `:149`; `:209`, `:220` | 220 lines; `:5` HOW THE DESK RECORDS IT holds `«INSTALL` (prose); `:148` `launchctl print gui/501/*` row, `:149` `cobalt.sh status` row; `## 7.` at `:209`, its last line `:220` | OK |
| 14 | I2 red-first deny count: `grep -o -F -e '"Bash(sudo *)"'` → "1 after" | I2's Deny line writes `` `Bash(sudo *)` `` in backticks and no double quote; the count after the row is 0, not 1 | FAIL |
| 15 | I2 red-first line count "233 on `BASE` as it stands" | `BASE` is 220 (card's own `:220` and 284's `:78`); 233 is the count after I2 alone (234 with 284 K3) | NOTE (wording) |
| 16 | brain test `test_desk_launch_brain.py:497-501` | splits at `\n## 7. \`BRAIN-HUB.md\``, reads everything after, needs `claude-opus-5-5`, `claude-fable-5-1`, `the only variable`; they stay in `## 7.`, `## 8.` only adds text, adds none of them | OK |
| 17 | I3 trace `test_desk_launch_ops_hand.py` `:296-300`, `:303-315`; constants `:21-25`; `:164-166` | `:296-300` asserts `INSTALL` in line 1 → red after I1, becomes `INSTALL not in …`. `:303-315` slices the title at `INSTALL` (a `ValueError` once the token is gone) → red after I1; the new form copies the real text with only `REAL_PATH` re-pointed, then `desk.commit`, `desk.run()`: H4 passes (no token, one line, `default`, names, 4 allow, 17 deny, shape, no `<>`). `:164-166` still pins the refusal; `INSTALL` constant stays. `:291-293` unchanged | OK |
| 18 | `grep -rn "STANDING-LIST\|OPS-HAND" tests ops` | readers: `test_desk_launch_brain.py:498` (`## 7.` on), `test_desk_launch_ops_hand.py` (REAL, `:296-315`), `desk-launch.sh`, `bare-guard.py` (names the file only, `:15,:99`), `test_bare_guard.py:1938`, `test_stop_guard.py:243` (a launch message string). Others are constructed titles (`test_authorize.py:32,:65`, `test_deploy_step0.py:100`, `test_install_fixed.py:67`). No other read of `STANDING-LIST.md` past `## 7.` or of `OPS-HAND.md` line 1 | OK |
| 19 | rows touch only `OPS-HAND.md` (I1), `STANDING-LIST.md` (I2), `tests/ops/test_desk_launch_ops_hand.py` (I3) | yes; the one non-docs edit is I3 | OK |
| 20 | no new command (R411, R412) | every string is an existing allow string; no row adds a command, `NOT IN THIS JOB` last bullet says so | OK |
| 21 | house: `grep -i "openai\|grok"` on the card | `:83` house A Grok, `HOUSE B: as needed`, "never OpenAI (R920)" | OK |
| 22 | collision with card 284 | 284 K3 inserts ONE line at `STANDING-LIST.md:149` (after `:148`, before the old `:149`); I2 appends after `:220` (`:221-233` alone; `:222-234` once K3 lands). Different lines, no overlap; I2's red counts "13 more lines", not an absolute (except the item in 15) | OK |
| 23 | other anchors: `bare-guard.py:1122` G5, `231` D2 line 27, `231` `## DECISIONS FOR HIM` line 24, words `:12-13` | `:1122` `return ROUTE["G5 fixed"]`; `231:27` D2; `231:24` the heading; words `:12` R969, `:15` R971 (the card says `:12-13`, R969 spans 12-13) | OK |
| 24 | drafter decisions 1-2 vs rows | 1: default = the prompt's title form `HIS RULING · APPROVED 2026-10-10 R969`; I1 NEW is that form. 2: default = include I3; I3 is a row, `DB: none` holds | OK |

## ISSUES
- FAIL (5): I1 and RECORDS cite R969 as `reports/cto-2026-10-10.md:8`; at `HEAD` `:8` is R971 and R969 is `:10`. Re-point to `:10` (or cite R971 `:8` as the confirming row).
- FAIL (14): I2's `"Bash(sudo *)"` red (double quotes) hits 0 after the row, since I2 writes the deny strings in backticks without quotes. Use `grep -c -F -e '`Bash(sudo *)`'` or drop the quotes.
- NOTE (15): I2's "233 on `BASE` as it stands" should read "220 on `BASE`, 233 after the row".
- NOTE: I2's red `grep -c -F -e "## 8. `OPS-HAND.md`" …` holds backticks inside double quotes; typed in a shell they run a command substitution. Single-quote it.
- NOTE: `RULINGS` names R969 only; R971 (confirms R969, `APPLIED: R969 row`) needs no row of its own.
- NOTE: `BASE` `936c9b1e` is 2 commits behind `HEAD` `1449bb1e`; the files the rows touch are the same at both, so the desk's re-write at launch changes nothing.
- NOTE: `uv run pytest` and `uv run cobalt jobs restarts` were not run (read-only seat); the I3 trace above is by reading.

PREFLIGHT DONE · card: ops-hand-install-1010 · checks: 24 · fails: 2 · ready: NO
