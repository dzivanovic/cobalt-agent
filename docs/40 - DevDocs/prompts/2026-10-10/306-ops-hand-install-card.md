JOB: ops-hand-install-1010
LADDER: OFF-LADDER — reports/cto-2026-10-10.md R969
BRANCH: ops/ops-hand-install-1010
WORKTREE: ops-hand-install-1010
BASE: a780d176
TIP:
REPORT: /Users/cobalt/cobalt-wt/ops-hand-install-1010/docs/40 - DevDocs/reports/ops-hand-install-build-2026-10-10.md
CHECK REPORT:
HOUSE B:
DB: none
RULINGS: 2026-10-10 R969, 2026-10-10 R971

## ROWS

WHY: his R969 ("Approved", row R969 of `reports/cto-2026-10-10.md`, `HIS RULING · APPROVED`, words `reports/cto-2026-10-10-words.md` R969) approved D1-D5 of card `231` as written (`prompts/2026-10-10/231-ops-hand-card.md` `## DECISIONS FOR HIM`, line 24 on). D1 is already in LAWS L63 (the EXCEPTION line). D2 is these rows: `OPS-HAND.md`'s launch line joins `STANDING-LIST.md`, and his approval row replaces `«INSTALL: his row»` in the title of `OPS-HAND.md`. D3-D5 take their stated defaults: no text of theirs changes. Two fixed files change, so they change by card rows, never in place (G5, `ops/desk/bare-guard.py:1122`). The ops-hand seat (deployed `1e9f2e4c`) cannot launch until this lands: `desk-launch.sh` kind ops-hand refuses while the file holds the token (`ops/desk/desk-launch.sh:633-634`). No row adds a command (R411, R412). Every row's red first ends with `uv run pytest -q tests/ops/test_desk_launch_ops_hand.py tests/ops/test_desk_launch_brain.py tests/ops/test_hub_lines.py` → `0 failed`.

| row | what | red first | files |
|---|---|---|---|
| I1 | D2, his R969. `OPS-HAND.md` line 1: the trailing `«INSTALL: his row»` becomes `HIS RULING · APPROVED 2026-10-10 R969`; every other byte of the file stands (22 lines before and after). Line 1, OLD = TEXT I1 OLD, NEW = TEXT I1 NEW. The form is proved against H4 (`ops/desk/desk-launch.sh:633-634`): the one install gate is `grep -q '«INSTALL' "$fixed"`, a refusal while it hits; NEW holds no `«`, so the gate passes. The same file's launch-line gates are untouched by the title: exactly one `^claude --bg ` line (`:636-637`), the line read from it (`:638`), every later check reads that line alone. `ops/desk/authorize.sh` (`:148`, `:173-183`, the `«INSTAL[L]` and `INSTALL: <date> R<n>` title reads) serves the build, check and deploy hubs and names no `OPS-HAND`, so NEW need not spell `INSTALL: <date> R<n>` (see DECISIONS in the report, item 1). Backed by rows R969 and R971 of `reports/cto-2026-10-10.md` (both `HIS RULING · APPROVED`, committed at `HEAD`; R971 confirms R969) and `231` D2 (line 27) | `grep -c -F -e "«INSTALL" "docs/40 - DevDocs/prompts/OPS-HAND.md"` → 0 after, 1 on `BASE` (line 1). `grep -c -F -e "HIS RULING · APPROVED 2026-10-10 R969"` on the same file → 1 after (line 1), 0 on `BASE`. `grep -c "^claude --bg "` → 1 before and after. `wc -l` → 22 before and after. Test I3 (below) is red on `BASE` | `docs/40 - DevDocs/prompts/OPS-HAND.md` (line 1 only) |
| I2 | D2. `STANDING-LIST.md`: ONE new section `## 8. `OPS-HAND.md`` appended after the last line (`:220` at `BASE`, the `## 7.` paragraph ending `… launches after he has stopped it).`), 13 lines, TEXT I2 NEW: the launch line of `OPS-HAND.md` as H3 wrote it (`OPS-HAND.md:20`), its four allow strings and its seventeen deny strings, each allow string with its use, its reach and its limit. It restates the line, it adds none: `OPS-HAND.md` holds the line the launcher runs. The section says `NEW as a launch line` plainly (L62: a string not in this file is new) and that it stands on his R969. No other line of the file changes (line 1 title, `HOW THE DESK RECORDS IT` at `:5` and `## 1`-`## 7` stand byte for byte). `test_p5_the_standing_list_names_the_two_model_words_as_the_only_variable` (`tests/ops/test_desk_launch_brain.py:497-501`) splits at `\n## 7. `BRAIN-HUB.md`` and reads everything after it: it still finds `claude-opus-5-5`, `claude-fable-5-1` and `the only variable` in `## 7.`, and the new section adds neither word. Backed by `231` D2 (line 27), row R969 | `grep -c -F -e '## 8. `OPS-HAND.md`' "docs/40 - DevDocs/prompts/STANDING-LIST.md"` → 1 after, 0 on `BASE`. `grep -c -F -e '--permission-mode default'` on the file → ≥ 1 after, 0 on `BASE`. The deny count: `grep -c -F -e '`Bash(sudo *)`'` on the file → 1 after, 0 on `BASE`. The file's line count is 13 more than before the row (220 on `BASE`, 233 after the row; any other row that lands first, such as card `284` K3's one line, moves the number, never the 13). `uv run pytest -q tests/ops/test_desk_launch_brain.py` → `0 failed` | `docs/40 - DevDocs/prompts/STANDING-LIST.md` (13 lines appended) |
| I3 | D2, his R969. The two tests that run the tree's own `OPS-HAND.md` through H4 pin the token and go red with I1; they change with it. `test_h3_the_real_file_is_refused_while_it_holds_its_install_token` (`tests/ops/test_desk_launch_ops_hand.py:296-300`) becomes `test_h3_the_real_file_is_installed_on_his_row`: `assert INSTALL not in REAL.read_text()` and the title (line 1) ends with `HIS RULING · APPROVED 2026-10-10 R969`. `test_h3_the_real_file_passes_once_his_row_fills_the_title` (`:303-315`) becomes `test_h3_the_real_file_passes_as_installed`: the tmp copy is the real text with only the Read path re-pointed (`REAL.read_text().replace(REAL_PATH, str(desk.fixed))`, no title edit), the same four assertions after (`returncode == 0`, stdout `[f"cd {desk.hand}", line_for(str(desk.fixed))]`, `--permission-mode default`, `--remote-control ops-hand --name ops-hand`). The token's refusal stays pinned by `:165-166` (a constructed title with the token) and the `INSTALL` constant stays. `DB: none` holds: the one test file is under `tests/ops/` | `test_h3_the_real_file_is_installed_on_his_row` (new name): on `BASE` fails at `assert INSTALL not in REAL.read_text()` (line 1 holds `«INSTALL`). `test_h3_the_real_file_passes_as_installed`: on `BASE` rc is 1 and stderr holds `OPS-HAND.md still carries its «INSTALL token` (`desk-launch.sh:634`), so `done.returncode == 0` fails. Mutation: put the token back into `OPS-HAND.md` line 1 → both tests red | `tests/ops/test_desk_launch_ops_hand.py` |

TEXT I1 OLD (`OPS-HAND.md:1` at `BASE`, whole line):

```text
# OPS-HAND — the ops-hand seat (card 2026-10-10 231; his 2026-10-10 R855) «INSTALL: his row»
```

TEXT I1 NEW (whole line):

```text
# OPS-HAND — the ops-hand seat (card 2026-10-10 231; his 2026-10-10 R855) HIS RULING · APPROVED 2026-10-10 R969
```

TEXT I2 NEW (appended after `STANDING-LIST.md:220`, 13 lines, the first line blank; the launch line is `OPS-HAND.md:20` byte for byte in the file, summarized here by its strings):

```text

## 8. `OPS-HAND.md` — THE OPS-HAND SEAT, launched on its own file (card `prompts/2026-10-10/231-ops-hand-card.md` H3, H4; his 2026-10-10 R855 for the build, R969 for D1-D5 and this install): 4 allow, 17 deny · `--model claude-sonnet-5-5` · `--permission-mode default` (the one fixed file whose mode is `default`: every Bash call waits on his tap, L63 EXCEPTION) · `--remote-control ops-hand --name ops-hand` · launched from `/Users/cobalt/cobalt-wt/.ops-hand` by `desk-launch.sh ops-hand` · NO `--add-dir`

**NEW as a launch line** (L62: a string not in this file is NEW): all four allow strings and the mode `default`, approved as written by his R969. The seat runs only what the CTO desk hands it by `SendMessage`; guard rule G12 (`ops/desk/bare-guard.py`) holds every Bash call to its class before any prompt; `desk-launch.sh ops-hand` (H4) copies and checks the line word for word against `OPS-HAND.md` and refuses a persisted `settings.local.json` in the seat's directory (D4).

| string | for | can touch | never touches |
|---|---|---|---|
| `SendMessage` | the seat's one reply channel to `cto-desk` | the desk's inbox | any other seat |
| `Bash(ps *)` | the desk's `ps -o pid,ppid,command -p <pid>` before a `kill`, and its other `ps` reads | read only | writes nothing |
| `Bash(pgrep *)` | the desk's `pgrep` reads | read only | writes nothing |
| `Bash(launchctl print *)` | the desk's `launchctl print gui/<uid>/…` reads | read only | writes nothing |

Deny (17): `AskUserQuestion`, `EnterWorktree`, `Write`, `Edit`, `NotebookEdit`, `Agent`, `Monitor`, `CronCreate`, `RemoteTrigger`, `ScheduleWakeup`, `Skill`, `WebFetch`, `mcp__*`, `Artifact*`, `Bash(git *)`, `Bash(claude *)`, `Bash(sudo *)`. The `kill` and `launchctl kickstart` of its class are no allow string: each is the desk's command, typed whole, on his tap (G12 admits only the class; his tap is "Yes" only, D4).
```

## NOT IN THIS JOB
- `ops/desk/desk-launch.sh` and `ops/desk/bare-guard.py` (H4 and G12 are built and deployed; the token gate at `desk-launch.sh:633-634` is the proof this card reads, never edits).
- Any other line of `OPS-HAND.md` than line 1, and any change to its launch line (`:20`), its class (`:14`) or its bound (`:16`): D3-D5 take their stated defaults, no change of text.
- Any other line of `STANDING-LIST.md` than the 13 appended: title, `HOW THE DESK RECORDS IT`, `## 1`-`## 7` and the CLASSES stand. Card `284` K3 (its one line after `:148`) is its own card and lands on its own order; the two cards touch different lines.
- LAWS L63 (D1 is in), `NOW`, `.claude/settings.json`, `~/.claude/settings.json`, any `settings.local.json`; the seat's first launch and its worktree (the desk's, after this lands).
- A new command of any kind (R411, R412): a row that needs one is not built; the build stops with `decisions: 1`.

## READ
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/OPS-HAND.md` whole (22 lines).
- `ops/desk/desk-launch.sh` lines 624-722 (kind ops-hand: `:633-634` the token gate, `:636-638` the one launch line, `:663-673` the four allow strings, `:704-705` the shape).
- `tests/ops/test_desk_launch_ops_hand.py` lines 20-26 (`REAL`, `REAL_PATH`, `INSTALL`), 160-170, 282-315.
- `docs/40 - DevDocs/prompts/STANDING-LIST.md` lines 1-6 and 209-220; `tests/ops/test_desk_launch_brain.py` lines 497-501.
- `prompts/2026-10-10/231-ops-hand-card.md` `## DECISIONS FOR HIM` (lines 24-30); `reports/cto-2026-10-10.md` rows R969, R971; `reports/cto-2026-10-10-words.md:12-13`.
- Precedent: `prompts/2026-10-10/284-kill-hub-card.md` (TEXT blocks, a STANDING-LIST row, `DB: none`).

## CHECK ASKS
- X1 Does `desk-launch.sh ops-hand` now pass its token gate on the tree's own `OPS-HAND.md` and no other gate fail on line 1's new text (`grep -c "^claude --bg "` still 1; no `<`, `>`, `\`, `$`, backtick, `;`, `&`, `|` newly on the launch line)?
- X2 Is the diff `<BASE>..<TIP>` only `OPS-HAND.md` line 1, 13 appended lines of `STANDING-LIST.md` and the two renamed tests (`git diff --numstat`: `OPS-HAND.md` 1/1, `STANDING-LIST.md` 13/0)?
- X3 Does the new `## 8.` restate `OPS-HAND.md:20` exactly: the four allow strings, the seventeen deny strings in order, the mode, the model, the two names, no `--add-dir`? Compare string by string, not by count.
- X4 Does any other test or script read `STANDING-LIST.md` past `## 7.` or `OPS-HAND.md` line 1 (`grep -rn "STANDING-LIST\|OPS-HAND" tests ops`)?
- X5 L63 and D1-D5 are his and approved (R969): write no finding that rests only on the seat being unapproved.

## RECORDS
- Read by the drafter `ops-hand-install`, 2026-10-10, against `HEAD` `936c9b1e` (`git -C /Users/cobalt/cobalt log --oneline -1`): `git diff HEAD --stat` over `OPS-HAND.md`, `STANDING-LIST.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_ops_hand.py`, `tests/ops/test_desk_launch_brain.py`, `reports/cto-2026-10-10.md` and `CARD.md` → nothing, so main's files equal `HEAD`. `git show HEAD:` read of `OPS-HAND.md` whole. `wc -l`: `OPS-HAND.md` 22, `STANDING-LIST.md` 220, `CARD.md` 139.
- H4, kind ops-hand (`desk-launch.sh` at `HEAD`): `:628` the kind, `:633-634` `grep -q '«INSTALL' "$fixed"` → `refuse`, `:636-638` one `^claude --bg ` line, `:673` the four allow strings `Bash(launchctl print *)|Bash(pgrep *)|Bash(ps *)|SendMessage|`, `:704-705` the words outside the lists. The only title-reading gate is the token grep: any title without `«INSTALL` passes.
- `authorize.sh` (`:148`, `:152`, `:173-183`) reads `«INSTAL[L]` and `INSTALL: <date> R<n>` titles of the build, check and deploy hubs; `grep -n "OPS-HAND\|ops-hand" ops/desk/authorize.sh` → no match.
- R969 is row `R969` of `reports/cto-2026-10-10.md`, `HIS RULING · APPROVED: "Approved" to the plate: F4 FINAL … and ops-hand D1-D5`; R971 is row `R971`, `HIS RULING · APPROVED: "Yes both" confirms R969`, `APPLIED: R969 row`; words at `cto-2026-10-10-words.md:12-13`; both committed at `HEAD` (`git show HEAD:` of the report holds both). R969's row names `ops-hand install` as next. Rows are cited by id, never by line (`authorize.sh` proves by row id).
- Amend 308, 2026-10-10, against `HEAD` `9d498807`: `git diff HEAD --stat` over `STANDING-LIST.md`, `OPS-HAND.md`, `reports/cto-2026-10-10.md` → empty, so the files equal `git show HEAD:`; `git show HEAD:` of the report holds rows R971 and R969 (`grep -n -E "^\| R9(69|71) "`). `wc -l`: `STANDING-LIST.md` 220, `OPS-HAND.md` 22. `grep -c -F -e '`Bash(sudo *)`'` on `STANDING-LIST.md` → 0 on `BASE` (the double-quoted form hit 0 after the row too); `grep -c -F -e '## 8. `OPS-HAND.md`'` → 0 on `BASE`. The sudo pattern matches I2's Deny line, which writes `` `Bash(sudo *)` `` in backticks.
- `«INSTALL` stands once in `OPS-HAND.md` (line 1) and once in `STANDING-LIST.md` (`:5`, prose about the hubs' tokens, not a token); `231-ops-hand-card.md` holds it six times as text about the gate.
- Tests tied to the rows: `test_desk_launch_ops_hand.py:296-300` and `:303-315` read the real file's title and go red with I1; `test_desk_launch_brain.py:497-501` reads `STANDING-LIST.md` after `## 7.` and stays green with I2. `grep -rn "STANDING-LIST" tests/` also finds `test_authorize.py:32`, `:65`, `test_deploy_step0.py:100`, `test_install_fixed.py:67`, strings inside constructed titles, not reads of the file.
- RESTARTS: every path is `docs/` or `tests/ops/` (`DB: none`); `uv run cobalt jobs restarts <BASE>..HEAD` is UNPROVEN at drafting (no `uv` on the drafter's allow list), the build hub runs it.
- `BASE`, `TIP`, `CHECK REPORT` and `HOUSE B` are the desk's: docs-only hub text, so house A is Grok, `HOUSE B: as needed`, the second read (L67) by one other house, never OpenAI (R920). `BASE` `936c9b1e` is `HEAD` at drafting; the desk re-writes it at launch if `main` has moved.
