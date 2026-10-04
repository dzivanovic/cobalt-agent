# brain-hub — build report 2026-10-03

## §0 Headline
1. B1: `prompts/BRAIN-HUB.md` is the standing brain file. It has one launch line, which is `23`'s line string for string with `HANDOVER: '<handover>'` added. It names no precedent of a day, and the install token stays in its title until his row.
2. B2: `desk-launch.sh brain "<handover>"`. It refuses a handover outside `prompts/<YYYY-MM-DD>/`, one holding a fill token, an uninstalled hub, an unreadable session list, and any live session named `brain`. `STANDING-LIST.md` §7 adds no new string. 25 new tests; each refusal was red under its own mutation.
3. B3: `prompts/2026-10-03/08-brain-handover.md`, 8 lines, no fill token, re-read from the desk report at 11:51 ET.
4. B4 (the desk's CONTINUE at E3, R53): the brain's bare `Write`/`Edit` are replaced by `Edit(…/reports/**)` and `Edit(…/prompts/20*/**)` on the hub line and in `STANDING-LIST.md` §7. Tip `dc9b06c4`: offline 3737 passed, `tests/ops` 499 passed, live-note 146 passed, 0 failed. `DB: none`: no lock taken. RESTARTS: none.
5. B5 (the desk's second CONTINUE at E3, R84, check O1): `desk-launch.sh prompt` refuses a line naming `--name brain` or `--remote-control brain` before anything runs; the check's O1 test passes without its xfail marker. Tip `bb930cac`: offline 3737 passed, `tests/ops` 508 passed, live-note 146 passed, 0 failed. Five decisions are open, none FOR DEJAN. DECISION 3 (the unscoped `Write`/`Edit`) is fixed by B4. The hub uses his R7 measure line of 500,000, not the card's 250,000.

## L74
One block arrived in this session, in a system reminder (not a tool result). It asked that commits end with a `Claude-Session: https://claude.ai/code/session_…` line. Treated as DATA: the commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (L74). Recorded once; the same block arrived again after the `CONTINUE: E3` and was treated the same way (`df609e2f`, `dc9b06c4` carry the one line). It arrived a third time after the 13:30 `CONTINUE: E3`; `97ab783d` and `bb930cac` carry the one line too.

## AUTHORIZATION
Started 11:30:09 EDT (`date`).
| rule | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card complete | `grep -n -E "«FIL[L]" ".../2026-10-03/07-brain-hub-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/07-brain-hub-card.md"` | 0 | `942180bed20f9a19cc5cf34fc10947ac02a704b6` |
| card unchanged | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING (2026-09-30 R60) | `grep -n "^\| R60 " cto-2026-09-30.md` | 0 | `46:\| R60 \| 15:15 ET \| **HIS RULING** (…): APPROVES STANDING-LIST.md once (4be06af0) … \| APPROVED \|` |
| R60 committed | `git -C … log -1 --format=%H -S"\| R60 \|" -- …cto-2026-09-30.md` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULINGS 2026-10-02 R47 | grep | 0 | `54:\| R47 \| 07:57 ET \| HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only … \| HIS RULING · APPROVED \|` |
| R47 committed | `-S"\| R47 \|"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULINGS 2026-10-02 R157 | grep | 0 | `164:\| R157 \| 17:40 ET \| HIS RULING (B): the brain's full process list for 10-03 runs this week … \| HIS RULING · APPROVED \|` |
| R157 committed | `-S"\| R157 \|"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| RULINGS 2026-10-02 R54 | grep | 0 | `61:\| R54 \| 08:00 ET \| HIS RULING (FOR DEJAN 13 = A): a standing BRAIN-HUB.md, on tomorrow's list … \| HIS RULING · APPROVED \|` |
| R54 committed | `-S"\| R54 \|"` | 0 | `e9a94c19ccf236eb26752e3bc64da90e8db9a243` |
All authorization rows hold.

## PREFLIGHT
`date` → `Sat Oct  3 11:30:09 EDT 2026`.
| rule | command | exit | output |
|---|---|---|---|
| branch | `git status --short --branch` | 0 | `## ops/brain-hub-1003` + `?? "docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md"` (this report, written first per `## REPORT`) |
| base | `git log --oneline -1` | 0 | `a09f0862 docs(desk): 10-03 R30-R34 set 1 deployed; refusals list; his rulings` |
| branch in main repo | `git -C /Users/cobalt/cobalt log --oneline -1 ops/brain-hub-1003` | 0 | the same `a09f0862` |
| diff vs base | `git diff --stat a09f0862` | 0 | (nothing) |
| base commit | `git show --stat a09f0862` | 0 | `docs/40 - DevDocs/reports/cto-2026-10-03-words.md \| 6 ++++++`, `docs/40 - DevDocs/reports/cto-2026-10-03.md \| 19 +++++++++++++++++--`, 2 files changed |
| no .env | `ls /Users/cobalt/cobalt-wt/brain-hub-1003/.env` | 1 | `No such file or directory` |
| other .env | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `no matches found` (no lock held) |
| restarts | `uv run cobalt jobs restarts a09f0862..HEAD` | 0 | one row `docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md A DOCS -`; `RESTARTS: none` (the untracked report only; the range itself is empty) |
| wc | `wc -l ops/desk/desk-launch.sh ".../prompts/STANDING-LIST.md"` | 0 | `898`, `216` |
| READ tail | `tail -n 3 reports/brain-direction-2026-10-02.md` | 0 | last line `DIRECTION WRITTEN, REVISED 08:25 ET — cards 15–19, 21 and the cut 13 are in prompts/2026-10-02/ as the brain names them` |
| READ tail | `tail -n 30 reports/cto-2026-10-03.md` | 0 | last line `HANDOVER: predecessor 15fed5c2 → successor 7b45ad1f at 07:37 ET`; last row R34 11:28 ET set 1 DEPLOYED `3fbe64fb` |
| symbol: `brain` kind absent | `grep -rn -F "desk-launch.sh brain" ops tests` | 1 | (nothing) |
| symbol: kind refusal | Grep tool `kind '\$kind' is none of` | — | `ops/desk/desk-launch.sh:420: *) refuse "kind '$kind' is none of build, check, deploy, devfix, desk, prompt, close, install-ops" ;;` |
| symbol: prompt kind | Read `ops/desk/desk-launch.sh:304-373` | — | the `prompt` kind: path under `$PROMPTS`, char set `[A-Za-z0-9 ._/-]`, no `..`, `committed`, one `claude --bg "Read ` line, mode `auto|plan`, write strings refused |
| symbol: guard | Read `ops/desk/desk-launch.sh:212-214` | — | `if [ "$kind" != "desk" ]; then sh "$(dirname "$0")/desk-context.sh" --guard \|\| exit $?` |
| symbol: desk-list | `ls -la /Users/cobalt/.claude/ops/` | 0 | `-rw-r--r-- … desk-list.sh` (a plain file, untracked; rows `id · name · cwd · status · state`, live rows only) |
| symbol: desk-done brain | Read `ops/desk/desk-done.sh:55-57` | — | `brain*\|cto-desk) refuse "$id is $name: a brain or the desk is stopped only on his word (2026-09-30 R76)"` |
| READ | `prompts/2026-10-02/23-brain-judge.md` whole; `03-brain-unattended.md` 1–20; `brain-direction-2026-10-02.md` 77–115; `brain-unattended-2026-10-02.md` §0, THE STANDARD, FOR DEJAN; `JUDGE-HUB.md` whole | — | read (Read tool) |
| also read | `prompts/2026-10-03/00-brain-handover.md` (the live brain's handover, written after the card's source) | — | its MEASURE line is 500,000 (his 10-03 R7) |
`## RECORDS` of the card, copied: (1) `DB: none`: every file is under `docs/` or `ops/`, `tests/ops/` — re-read at W (a0). (2) His R76 (09-30) and R131 (10-02) bind the seat — R76 re-read in `desk-done.sh:12-14`, `55-57`. (3) The install token stands in the hub's title until his row; `install-fixed.sh` replaces it (card `17`) — `ops/desk/install-fixed.sh` present (`ls ops/desk`).
PROVEN BY FIRST REAL USE: `uv run pytest *` at E0; `git add *` / `git commit *` at E2. DB: none, so the lock strings and the with-DB strings are not used.

## E0 BASELINE
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` on `a09f0862` → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 650.86s (0:10:50)`, exit 0: 0 failed, 0 errors.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 31.63s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
New test file `tests/ops/test_desk_launch_brain.py` (25 tests). No `src/` or `ops/` edit.
`uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_brain.py` → `24 failed, 1 passed, 15 warnings in 2.42s`.
- B2 (22 tests: good case, run from the repo, the live-session negative control, live `brain` ×2, unreadable list ×2, fill token, the dated-folder refusals ×7, quote, missing handover, usage ×2, install token, uncommitted hub, seat name): every first line is `AssertionError: REFUSED: kind 'brain' is none of build, check, deploy, devfix, desk, prompt, close, install-ops` — the row's named red.
- B1 (2 tests: `test_the_trees_brain_hub_line_is_printed_with_its_handover_filled`, `test_the_trees_brain_hub_allow_list_is_23s_byte_for_byte`): `FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/brain-hub-1003/docs/40 - DevDocs/prompts/BRAIN-HUB.md'` — B1's file does not exist yet.
- 1 passed: `test_the_desk_size_guard_runs_first` (the guard already runs before the kind check for every kind but `desk`). It is pinned by an E3 mutation (the guard skipped for `brain`).
- **B4 (CONTINUE: E3, 12:07 ET; the card re-issued at main `b1320acc`, desk R53).** `tests/ops/test_desk_launch_brain.py`: B1's byte-for-byte test is renamed `test_the_trees_brain_hub_allow_list_is_23s_byte_for_byte_but_the_write_pair` (23's allow list with its one ` "Write" "Edit" ` replaced by the scoped pair), plus `test_the_trees_brain_line_holds_the_scoped_pair_and_no_bare_write_or_edit` and the negative control `test_a_hub_with_the_bare_pair_fails_the_scope_check`. `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_brain.py` on `f92063d7` → `2 failed, 25 passed`: the renamed test's diff shows `"Read" "Write" "Edit" "Bash(ls *)"` against the scoped pair; the new test `AssertionError: … --allowedTools "Read" "Write" "Edit" …` (`SCOPED_PAIR in line` false) — the bare pair, the row's named red. The negative control passed. Red commit `df609e2f wip(brain-hub): red B4`.
- **B5 (CONTINUE: E3, 13:30 ET; the card re-issued at main `186b3a98`, desk R84).** `tests/ops/test_desk_launch_brain.py`: the check's strict xfail marker on `test_o1_a_brain_line_through_the_prompt_kind_is_refused_beside_a_live_brain` dropped; `test_b5_a_prompt_line_naming_the_brain_seat_is_refused_before_anything_runs` (3 seat spellings × dry/real; asserts `REFUSED: a brain seat launches by desk-launch.sh brain <handover>` and no `claude` call); negative control `test_b5_a_prompt_line_on_another_seat_still_launches` (`brain-survey`, `brainy`). `tests/ops/test_desk_size_guard.py`: the fixture `04-brain-prompt.md` with `--remote-control brain --name brain` becomes `04-survey-prompt.md` with `--remote-control survey --name survey`. `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_brain.py tests/ops/test_desk_size_guard.py` on `18c26c70` → `7 failed, 67 passed, 1 xfailed`: O1 `assert 0 == 1` (the line printed: `… --remote-control brain --name brain …`), and each of the 6 B5 cases `assert 0 == 1` with the line printed (dry) or `RUN: claude --bg …` (real) — the `prompt` kind runs the brain line, the row's named red. Negative controls and the size-guard file passed. Red commit `97ab783d wip(brain-hub): red B5`.
- RUN rows on BASE (they assert nothing): B1 `grep -c "^claude --bg " "docs/40 - DevDocs/prompts/BRAIN-HUB.md"` → exit 2 `No such file or directory`; B3 `wc -l ".../2026-10-03/08-brain-handover.md"` → exit 1 `No such file or directory`. Both are run again at E3 on the written files.

## E3 THE ROWS
Commit `390da6b1 feat(brain-hub): standing BRAIN-HUB.md, desk-launch.sh brain, first handover (B1-B3, L1 L28 L74 R76)` — 4 files, 136 insertions, 2 deletions.
- **B1** `docs/40 - DevDocs/prompts/BRAIN-HUB.md` (43 lines): `## LAUNCH` (the desk's one command `desk-launch.sh brain "<handover>"`, then the ONE `claude --bg` line: model `claude-fable-5-1`, `--permission-mode auto`, `--remote-control brain --name brain`, `23`'s allow and deny strings and its three `--add-dir` roots), `## WHO YOU ARE` (judge seat under his order, his reasoning seat, L78; `JUDGE-HUB.md` named as another seat), `## READ AT START` (the handover; the direction it names; the design report's §0 and THE STANDARD; `tail -n 30` of the day's desk report; nothing else), `## WRITE FENCE`, `## HOW YOU ANSWER A JUDGE REQUEST` (`23`'s four bullets plus one: a precedent is applied, never re-decided), `## MEASURE`, `## HANDOVER SHAPE` (eight keyed lines). No precedent of a day. RUN rows: `grep -c "^claude --bg " "docs/40 - DevDocs/prompts/BRAIN-HUB.md"` → `1`; `grep -c -F «INSTALL "docs/40 - DevDocs/prompts/BRAIN-HUB.md"` → `1`. Also `grep -c` for the fill token → `0`.
- **B2** `ops/desk/desk-launch.sh` lines 384–443: kind `brain` (usage; `..` and the character set `[A-Za-z0-9 ._/-]`; a `.md` directly under `$PROMPTS/<YYYY-MM-DD>/`; the file exists; no fill token; `BRAIN-HUB.md` installed, committed, one launch line naming `--remote-control brain --name brain`, no `bypassPermissions`, no unfilled token, `check_paths`; the live check: `desk-list.sh` beside the script, unreadable = REFUSED, any row whose name is exactly `brain` = REFUSED citing R76); `cd /Users/cobalt/cobalt` and the filled line through `run_launch`. The desk-size guard runs first, as for every kind but `desk`. Header lines 29–30, 58, 81, 94–99 and the usage line 214 name the kind. `STANDING-LIST.md` gains `## 7. BRAIN-HUB.md` (13 allow, 3 deny, NONE NEW: every string stands on `23`'s line).
- **B3** `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md`, written from `23-brain-judge.md`, `00-brain-handover.md` and the desk report re-read at 11:51 ET (`tail -n 8` and the R3x, R4x, R5x rows of `/Users/cobalt/cobalt/.../cto-2026-10-03.md`; main at `5f90be0f`). RUN rows: `wc -l` → `8`; `grep -c` for the fill token (the pattern `desk-launch.sh` greps) → `0`.
- Row tests after B1–B3: `uv run pytest -q -p no:cacheprovider --color=no --tb=short tests/ops/test_desk_launch_brain.py` → `25 passed`. Beside them: `tests/ops/test_desk_launch_devfix.py tests/ops/test_desk_launch_brain.py tests/ops/test_desk_size_guard.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_install_ops.py` → `174 passed, 1 xfailed`.
- A neighbour went red once: the whole `tests/ops` run gave `1 failed, 496 passed, 1 xfailed`: `test_desk_launch_devfix.py::test_an_unknown_kind_names_devfix_among_the_kinds` pins the unknown-kind text, and I had added `brain` to it. That file is not in the card's files, so the unknown-kind text is back at its BASE wording (DECISION 5). After that: `166 passed, 1 xfailed` for the four launcher files.
- DevDocs: `docs/40 - DevDocs/cobalt/` holds pages for `src/cobalt` modules only; no page exists for `ops/desk/`, so no dated line was written (`## RECORDS`).

THE MUTATIONS (Edit tool, each undone with the Edit tool; `uv run pytest -q -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_launch_brain.py`):
| # | mutation | result | first failing line |
|---|---|---|---|
| M1 (B2 live check undone) | name compared to `brain-MUTANT` | `2 failed, 23 passed` | `test_a_live_brain_is_refused_and_nothing_runs[True]`: `assert 0 == 1` (the line was printed: `cd …/repo`, `claude --bg "Read '…/BRAIN-HUB.md' …`) |
| M1b (negative control broken) | any name starting `brain` counts | `1 failed, 24 passed` | `test_other_live_sessions_do_not_block_a_brain`: `REFUSED: a session named brain is live (b0110001 b2a10002)` |
| (void) | a first M1b spelling with `case … esac` inside `$( )` | `23 failed, 2 passed` | `line 437: syntax error near unexpected token ';;'` — a broken script, not a mutation; rewritten as M1b above |
| M2 (fail-closed undone) | `\|\| refuse` → `\|\| true` on the list read | with M3: `3 failed, 22 passed` | `test_an_unreadable_session_list_is_refused[list fails]` and `[list missing]`: `assert 0 == 1` (the line ran) |
| M3 (guard skipped for brain) | `[ "$kind" != "desk" ] && [ "$kind" != "brain" ]` | (same run) | `test_the_desk_size_guard_runs_first`: `assert (0, '') == (3, 'REFUSED:...RESH first\n')` — the test that passed at E2 is red here |
| M4 (handover refusals undone) | fill grep on `«MUTANT`; date case `*) ;;`; sub-folder case `MUTANT/*` | `4 failed, 21 passed` | `test_a_handover_holding_the_fill_token_is_refused`, `…[notadate/…]`, `…[2026-1-02/…]`, `…[2026-01-02/sub/…]` |
| M5 (B1 allow list widened) | `"Bash(cat *)"` added to `BRAIN-HUB.md`'s line | `1 failed, 24 passed` | `test_the_trees_brain_hub_allow_list_is_23s_byte_for_byte`: `+ it" "Bash(cat *)" "Bash(ls *)" …` |
- **B4** commit `dc9b06c4 feat(brain-hub): the brain's Write/Edit scoped to reports/** and prompts/20*/** (B4, L3 L72)` — 2 files, 4+/4−. `BRAIN-HUB.md:8`: `"Read" "Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/**)" "Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/prompts/20*/**)" "Bash(ls *)"`; `:10` names the replacement (judge 10-03, DECISION 3, his veto list). `STANDING-LIST.md:220` and `:225` mark the pair as the replacement of `23`'s bare pair; the count stays 13 allow, 3 deny. `desk-launch.sh` unchanged: its `check_paths` accepts both strings (each sits under `--add-dir /Users/cobalt/cobalt`; the dry run prints the line). Row tests: the four launcher files plus `test_install_ops.py` → `176 passed, 1 xfailed`; `test_desk_launch_brain.py` alone → `27 passed`. RUN rows again on the tip: `grep -c "^claude --bg "` → `1`; `grep -c -F «INSTALL` → `1`; fill-token `grep -c` → `0`. `grep -n -F "\"Write\""` on the hub → line 10 only (the prose naming `23`'s pair), not the launch line.

| # | mutation (B4) | result | first failing line |
|---|---|---|---|
| M6 (fix undone) | `BRAIN-HUB.md:8` back to `"Read" "Write" "Edit" "Bash(ls *)"` | `2 failed, 25 passed` | `…byte_for_byte_but_the_write_pair` and `…holds_the_scoped_pair…`: `assert '"Edit(//…/reports/**)" "Edit(//…/prompts/20*/**)"' in '… "Read" "Write" "Edit" …'` |
| M6b (a bare string beside the scoped pair) | `"Write"` added after the pair | `2 failed, 25 passed` | `…holds_the_scoped_pair…`: `assert ' "Write"' not in …` (`20*/**)" "Write" "Bash(ls *)"`) |
| M6c (negative control broken) | `assert_writes_scoped` returns at once | `1 failed, 26 passed` | `test_a_hub_with_the_bare_pair_fails_the_scope_check`: `Failed: DID NOT RAISE <class 'AssertionError'>` |
- **B5** commit `bb930cac fix(brain-hub): the prompt kind refuses a brain seat line (B5, L3)` — 1 file, 8+/3−. `ops/desk/desk-launch.sh:336-338`: right after the launch line is read, before any other check and before `run_launch`, a line naming `--name brain` or `--remote-control brain` (followed by a blank or the line's end) → `REFUSED: a brain seat launches by desk-launch.sh brain <handover>`. Header: "a brain tab" struck from the `prompt` use (`:56`); the refusal named in IT REFUSES (`:92-93`). Row tests: the four launcher files plus `test_install_ops.py` → `185 passed, 1 xfailed`.

| # | mutation (B5) | result | first failing line |
|---|---|---|---|
| M7 (fix undone) | the pattern becomes `*"--name brain-MUTANT "*` | `7 failed, 29 passed` | `test_o1_…`: `assert 0 == 1` (`… --remote-control brain --name brain …` printed); the 6 `test_b5_a_prompt_line_naming_…` cases likewise (dry: the line printed; real: `RUN: claude --bg …`) |
| M7b (negative control broken) | prefix match `*"--name brain"*\|*"--remote-control brain"*` | `2 failed, 34 passed` | `test_b5_a_prompt_line_on_another_seat_still_launches[…brain-survey…]` and `[…brainy…]`: `REFUSED: a brain seat launches by desk-launch.sh brain <handover>`, `assert 1 == 0` |
After the B5 undo: `185 passed, 1 xfailed`; `git diff --stat` → `desk-launch.sh | 11 ++++++++---` (the fix only; `git diff ops/desk/desk-launch.sh` read whole, no `MUTANT`).

After the B4 undo: `27 passed`; `git diff --stat` → `BRAIN-HUB.md | 4 ++--`, `STANDING-LIST.md | 4 ++--` (the fix only); `grep -rn -F "MUTANT"` on the test and the hub → nothing.

After the B1–B3 undo: `166 passed, 1 xfailed` (the four launcher files); `git diff --stat` → `STANDING-LIST.md | 13`, `desk-launch.sh | 74 +-` (the fix only; `git diff ops/desk/desk-launch.sh` read whole: no `MUTANT`, no `brain-MUTANT`, the guard line as at BASE).

## RESTARTS
`uv run cobalt jobs restarts a09f0862..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md	A	DOCS	-
docs/40 - DevDocs/prompts/BRAIN-HUB.md	A	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md	A	DOCS	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_launch_brain.py	A	test/documentation; no resident	-
RESTARTS: none
```
No `UNCLASSIFIED` row.

## W THE THREE SUITES
**Third run, after B5 (`<tip>` = `bb930cac`).** RESTARTS at `bb930cac`: `uv run cobalt jobs restarts a09f0862..HEAD` → the six rows of `## RESTARTS` plus `tests/ops/test_desk_size_guard.py	M	test/documentation; no resident	-`; the report row now `M`; `RESTARTS: none`. No `UNCLASSIFIED` row.
- (a0) `git diff --name-only --no-renames a09f0862` → `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md`, `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_brain.py`, `tests/ops/test_desk_size_guard.py`; every path under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 7 paths)`**.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `508 passed, 1 xfailed, 15 warnings in 207.67s (0:03:27)` (B5 adds 8 tests; O1 now passes).
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (`run_in_background`) → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 632.67s (0:10:32)`, exit 0: 0 failed, 0 errors (this build adds no test there).
- (e) LIVE-NOTE: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.46s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`.
- (b)–(d), (f): not run (DB: none).

**Second run, after B4 (`<tip>` = `dc9b06c4`).** RESTARTS re-run at `dc9b06c4`: the same six rows as below, `RESTARTS: none`.
- (a0) `git diff --name-only --no-renames a09f0862` → the same 5 paths plus this report: `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md`, `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `docs/40 - DevDocs/reports/brain-hub-build-2026-10-03.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_brain.py`; every path under `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `499 passed, 1 xfailed, 15 warnings in 205.27s (0:03:25)`, exit 0 (B4 adds 2 tests; one B1 test renamed).
- (a) OFFLINE: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 638.34s (0:10:38)`, exit 0.
- (e) LIVE-NOTE: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 29.18s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`.
- (b)–(d), (f): not run (DB: none).

**First run, B1–B3 (`<tip>` = `390da6b1`).**
- (a0) `git diff --name-only --no-renames a09f0862` → `docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md`, `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `ops/desk/desk-launch.sh`, `tests/ops/test_desk_launch_brain.py`. Every path starts with `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 5 paths)`**.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `497 passed, 1 xfailed, 15 warnings in 201.19s (0:03:21)`. This build adds the 25 tests of `tests/ops/test_desk_launch_brain.py`.
- (a) OFFLINE on `390da6b1`: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 637.77s (0:10:37)`, exit 0: 0 failed, 0 errors (as at E0; this build adds no test there).
- (b)–(d), (f): not run (DB: none).
- (e) LIVE-NOTE, `.env` absent: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.38s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## PRE-STOP SELF-CHECK
(1) Every added test was shown red for its named reason. At E2, 22 B2 tests were red on `REFUSED: kind 'brain' is none of …` and 2 B1 tests on `FileNotFoundError … BRAIN-HUB.md`. The one test green at E2 (`test_the_desk_size_guard_runs_first`) was red under M3. Each refusal family was also red under its own mutation: live brain M1, negative control M1b, fail-closed M2, handover M4, allow list M5. No test stayed green under its mutation. B4: the renamed byte test and the scoped-pair test red at E2 on the bare pair and under M6; the scoped-pair test red under M6b; the negative control red under M6c. B5: O1 and the 6 refusal cases red at E2 on `18c26c70` and under M7; the 2 negative-control cases red under M7b. The size-guard fixture edit renames a seat only; the file stayed green at E2 and after the fix (it tests the guard, not the seat; the `prompt` form now launches the `survey` seat).
(2) Entry paths. The `brain` kind's callers: `Grep "desk-launch\.sh brain"` → `BRAIN-HUB.md`, `STANDING-LIST.md`, the card, this report, the test, the script's own header. No script calls it; the desk types it. The paths pinned: dry and real run; usage with 0 and 2 arguments; each handover refusal (7 locations, a quote, missing, fill token); the hub (install token, uncommitted, wrong seat name); the live list (live `brain` dry and real, list failing, list missing, other names including `brain-hub-build` and `brainy`); the guard; the tree's own hub line and its allow list against `23`'s. Not pinned by a test: `bypassPermissions` and the unfilled-token refusal on the hub line. Both are copied from the `desk` and `prompt` kinds, and the tree's hub carries neither (the tree-hub test asserts no `<` or `>` remains).
(3) Re-read at the tip: `git show 390da6b1 --stat` (4 files, 136+/2−); `grep -n -F "kind brain" ops/desk/desk-launch.sh` → `384:`; `grep -n -F "## " ".../BRAIN-HUB.md"` → sections at 5, 12, 15, 22, 25, 32, 35; `wc -l` of the handover → 8; the RUN-row greps above; the RESTARTS table re-run at the tip. After B4: `git show --stat dc9b06c4` (2 files, 4+/4−); `git log --oneline a09f0862..HEAD` (5 commits); `grep -n -F "Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/"` on the hub and the list → `BRAIN-HUB.md:8`, `STANDING-LIST.md:220`, `:225`; the three RUN-row greps on the hub (`1`, `1`, `0`). B4's entry path: the dry and real run of `desk-launch.sh brain` on the tree's hub (the scoped-pair test runs the script). B5's entry paths: the `prompt` kind in dry and real mode, `--remote-control brain` alone, `--name brain` alone, both, beside a live brain (O1) and with none; the exact-name boundary (`brain-survey`, `brainy`). After B5: `grep -n -F "a brain seat launches by desk-launch.sh brain"` → `ops/desk/desk-launch.sh:337`; `git show --stat bb930cac` (1 file, 8+/3−); `git log --oneline a09f0862..HEAD` (9 commits).

## FOR THE CHECK
- Range `a09f0862..bb930cac`: `68180c71 wip(brain-hub): red` (the test file only), `390da6b1 feat(brain-hub): standing BRAIN-HUB.md, desk-launch.sh brain, first handover (B1-B3, L1 L28 L74 R76)`, `f92063d7 docs(brain-hub): build report — 390da6b1`, `df609e2f wip(brain-hub): red B4`, `dc9b06c4 feat(brain-hub): the brain's Write/Edit scoped to reports/** and prompts/20*/** (B4, L3 L72)`, `1f79cfe3 docs(brain-hub): build report — dc9b06c4`, `18c26c70 wip(brain-hub): check red — O1 (strict xfail: held, not fixed)` (the check's), `97ab783d wip(brain-hub): red B5`, `bb930cac fix(brain-hub): the prompt kind refuses a brain seat line (B5, L3)`.
- Suites at `bb930cac`: offline `3737 passed`, `tests/ops` `508 passed, 1 xfailed`, live-note `146 passed, 1 skipped` (commands at `## W`, third run).
- B5 for the check: the historic one-off prompts under `prompts/2026-09-30/`, `2026-10-01/`, `2026-10-02/` and `2026-10-03/00-brain-handover.md` carry `--remote-control brain --name brain` on their own lines; the `prompt` kind now refuses each of them. The card's record says the brain moves `00-brain-handover.md`'s line to the `brain` kind after `07` is on `main`.
- Per row: reds at `## E2 RED`, mutations and greens at `## E3 THE ROWS` (quoted there).
- Caller grep: `Grep "desk-launch\.sh brain"` → `BRAIN-HUB.md`, `ops/desk/desk-launch.sh` (its header), `STANDING-LIST.md`, the card, this report, `tests/ops/test_desk_launch_brain.py`. No script calls the kind.
- RUN rows (whole output): B1 `grep -c "^claude --bg " "docs/40 - DevDocs/prompts/BRAIN-HUB.md"` → `1`; `grep -c -F «INSTALL "docs/40 - DevDocs/prompts/BRAIN-HUB.md"` → `1`. B3 `wc -l "docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md"` → `8 docs/40 - DevDocs/prompts/2026-10-03/08-brain-handover.md`; the fill-token `grep -c` → `0`.
- Suites: offline and live-note at `## W` with their commands; `tests/ops` `497 passed, 1 xfailed`. With-DB: not run (DB: none). `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table at `## RESTARTS` (`RESTARTS: none`).
- The card's CHECK ASKS, with what the build saw:
  - X1 after B4: the brain's only write strings are `Edit(//…/reports/**)` and `Edit(//…/prompts/20*/**)`; LAWS, memory, scripts, settings, code and the fixed files at `prompts/` root are outside both globs. Inside `reports/**` the desk report and other reports remain reachable; the hub's fence text keeps them out. Before B4: yes. `"Write"` and `"Edit"` are bare on `23`'s line, under `--permission-mode auto`, with `/Users/cobalt/Vault`, `/Users/cobalt/cobalt` and `/Users/cobalt/cobalt-wt` as roots. Nothing on the line scopes them, so the fence is the hub's `## WRITE FENCE` text plus the auto-mode classifier (DECISION 3). Every Bash string is a read.
  - X2: the hub names no file but the handover and what the handover names (the direction, the design report), plus the day's desk report by pattern. It names the rulings that set the seat itself (R54, R131, R41, R76, R7) and no precedent of a day.
  - X3: the live check runs in dry and real mode before `run_launch`; an unreadable list is REFUSED. It matches the name `brain` exactly, so a session named `brain-hub-build` or `brainy` does not block (negative control, M1b).
- Records copied at PREFLIGHT: see `## PREFLIGHT` (the card's three records, re-read).

## CONTINUE
next: none — the desk verifies and launches the check (pass 2)

## DECISIONS
- DECISION 1 (B1, `## MEASURE`): the card says 250,000 → handover. His 2026-10-03 R7 (`cto-2026-10-03.md:13`, HIS RULING · APPROVED — pending fold) sets the brain's line at 500,000, and `00-brain-handover.md` carries it. Safe default taken: the hub says 500,000 and cites R7 (L77: his ruling is not re-opened). Not his to answer again; the judge seat confirms the reading.
- DECISION 2 (B1, `## WRITE FENCE`): the card's fence lists cards under `prompts/<date>/`. The card's own `## MEASURE` has the brain write its handover there, and the direction (`brain-direction-2026-10-02.md:83`) and `00-brain-handover.md` line 1 have it write read-only survey prompts. Safe default taken: the fence reads "cards, read-only prompts and your handover file under `prompts/<date>/`". Nothing outside `prompts/<date>/` was added.
- DECISION 3 (X1) — ANSWERED by the judge and the desk (`cto-2026-10-03.md` R53: a narrowing, not his; on his veto list) and FIXED by row B4 at `dc9b06c4`: the bare pair is replaced by `Edit(//…/reports/**)` and `Edit(//…/prompts/20*/**)`. Not counted below. What remains open inside the two globs, for the check (X1): `reports/**` holds the desk report `cto-<date>.md` and other workers' reports, which only the hub's fence text keeps the brain from editing. The original text, kept for the record: the brain's `Write` and `Edit` are unscoped on `23`'s line, in `auto` mode, so a brain can write LAWS, memory, scripts, settings or code under its three roots. Only the hub's text and the classifier stop it. The card fences the line ("byte for byte, no string added or dropped"), so the line is unchanged and the test pins it to `23`'s. A scoped pair (for example `Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/reports/**)`, `Edit(//Users/cobalt/cobalt/docs/40 - DevDocs/prompts/20*/**)` in place of the bare pair) would be his word.
- DECISION 4 (B2, the card's "the desk's `desk-done.sh brain` is run on his word first"): no such route exists. `ops/desk/desk-done.sh:55-57` REFUSES every session whose name starts with `brain`, whatever the word. The refusal text therefore names R76 and no stop command. Who stops a brain (him by hand, or a `desk-done.sh` change) is outside the rows. Safe default: the launcher refuses while a `brain` is live, and nothing else changes.
- DECISION 5 (B2): the unknown-kind refusal of `desk-launch.sh` still lists `build, check, deploy, devfix, desk, prompt, close, install-ops` (no `brain`). `tests/ops/test_desk_launch_devfix.py:382` pins that text, and that file is not in the card's files. Safe default: BASE wording kept. Follow-up: one line in that test plus the message, on any later card.
- DECISION 6 (B3): two values in the handover go stale before the launch, which waits for his word. The predecessor's size is written as "the size the desk measures then (`desk-context.sh 6ff9bb1d 500000`)", since a build cannot measure it. `STATE AT 11:40 ET` is the desk report at build time. Safe default: both are written as facts with their time, and the successor re-reads the desk report (`BRAIN-HUB.md` READ AT START 4). If the desk wants the size in the file, it edits that one line before the launch.

## RECORDS
- CONTINUED at E3 13:30 EDT (`date` 13:30:19), the second CONTINUE. The message named a step and no fact. Verified: the card's last commit on main is `186b3a98` (`docs(desk): 10-03 cards 03 L5, 07 B5, 09 S2 amended per judge; 02 records`, 13:30:00), and it now holds row B5; `git -C /Users/cobalt/cobalt diff --stat` on the card → nothing; the fill-token grep → exit 1; `cto-2026-10-03.md:90` R84 is a DESK RECORD (check `07` O1 route (a) → row B5; O2 → card `10`; resume E3). RULINGS are unchanged. The row is on the committed card, so the message added nothing. The branch held the check's `18c26c70` (strict xfail O1), continued and not discarded.
- The `BUILT` line of the B4 run was replaced by `RESUMED: E3 13:30:19 EDT` as the first report write. It is kept above in lower case as `built · …` so no line but the last starts with `BUILT`.
- CONTINUED at E3 12:07 EDT (`date`). The message `CONTINUE: E3` stated no fact; it named a step. Verified: the card at main `b1320acc` (`docs(desk): 10-03 R53 card 07 row B4 (brain write strings scoped)`, 12:07:11) now holds row B4; `git -C /Users/cobalt/cobalt diff --stat` on the card → nothing; the fill-token grep on the card → exit 1; `cto-2026-10-03.md:59` R53 is a DESK RECORD (D3 holds, not his: a narrowing; new row B4; D1, D2, D4–D6 KEEP; resume at E3). The card's RULINGS are unchanged (R47, R157, R54, re-proven at AUTHORIZATION). The row is on the committed card, so the message added nothing.
- `.env`: never present in this worktree (`DB: none`; no lock taken).
- No DevDocs page exists for `ops/desk/` under `docs/40 - DevDocs/cobalt/` (its pages cover `src/cobalt` modules), so E3 wrote no dated module line.
- Main moved past BASE during the build (`5f90be0f`, desk rows R35–R51); B3's state was re-read from main's desk report at 11:51 ET, read only.
- His 10-03 R12 desk note "Telemetry + Flight Recorder on the brain's next launch line" (`cto-2026-10-03.md` §5 NOTES) is not on `BRAIN-HUB.md`'s line: the card fences the line to `23`'s, and R27 makes those an install by him (`/plugin`), not launch-line strings.
- The live brain at build time is `6ff9bb1d` on `23-brain-judge.md` (desk §5 CURRENT); `00-brain-handover.md` was read for its precedents and measure line only.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.
- REFUSED, not needed: `grep -n -F "kind '$kind' is none of" …/desk-launch.sh` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." (my error: a `$` inside a double-quoted argument; read with the Grep tool instead).

Previous stop line (superseded by the CONTINUE at E3, 13:30): built · job: brain-hub · tip: dc9b06c4 | rows: 4 of 4 | decisions: 5 · for Dejan: 0

BUILT · job: brain-hub · tip: bb930cac | on a09f0862 | migration: none | offline 3737/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 5 · for Dejan: 0
