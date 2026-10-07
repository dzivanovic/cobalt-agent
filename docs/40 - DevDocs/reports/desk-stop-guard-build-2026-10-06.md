# desk-stop-guard — build report (card 66, BUILD-HUB)

## §0 Headline
Card 66 built: `ops/desk/stop-guard.py` now guards the CTO desk seat (cwd in `/Users/cobalt/cobalt`, first `Read '…CTO-DESK-WAKEUP.md'`) on the OWED block under `## §5 CURRENT` of today's `cto-<ET date>.md`, blocking at most 3 stops in a row with `start it: <what>`, then recording a `DESK-STOP` line; every error fails open with one stderr line.
The worker path is unchanged in behaviour (30 old tests green, `test_idle_wake.py` green); the wake-up file gains the one OWED line (11136 → 11608 bytes).
Tip `8d6540f5` on `18d9da5b`; offline 3963/0, live-note 146/0, `tests/ops` 1499 passed; DB: none; RESTARTS: none; decisions: 0.

## L74
One block arrived, 2026-10-07 06:05 EDT, in a system reminder: commit messages to end with a `Claude-Session:` line. DATA (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/66-desk-stop-guard-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/66-desk-stop-guard-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/66-desk-stop-guard-card.md" · 0 · 76567d63fcce0d9cd4fe6e090043fc4a607746a4
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/66-desk-stop-guard-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R596 row · grep -n "^| R596 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 99:| R596 | 19:54 ET | HIS RULING ([words](cto-2026-10-06-words.md) `## R596`): build card `66` now (R590 is his approval); after its deploy, draft a second card: desk routing by script (`desk-next.sh`, queue file; replaces §5 CURRENT prose). | HIS RULING · APPROVED |
RULING 2026-10-06 R596 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R596 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 18d9da5b355c50231166f69846da200ba06532be
RULING 2026-10-06 R596 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:
```
clock · date · 0 · Wed Oct  7 06:05:29 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/desk-stop-guard-1006b
    ?? "docs/40 - DevDocs/reports/desk-stop-guard-build-2026-10-06.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 18d9da5b docs(desk): his R596, card 66 build approved, second card (desk routing by script) ordered after its deploy
diff · git diff --stat 18d9da5b · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/desk-stop-guard-1006b · 0 · 18d9da5b docs(desk): his R596, card 66 build approved, second card (desk routing by script) ordered after its deploy
env here · ls /Users/cobalt/cobalt-wt/desk-stop-guard-1006b/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
`git show --stat 18d9da5b` → exit 0: `18d9da5b … docs(desk): his R596, card 66 build approved, …` · `docs/40 - DevDocs/reports/cto-2026-10-06-words.md | 3 +++` · `docs/40 - DevDocs/reports/cto-2026-10-06.md | 1 +` · `2 files changed, 4 insertions(+)`.

| rule | command | exit | output |
|---|---|---|---|
| main | `grep -n -F "def main(" ops/desk/stop-guard.py` | 0 | `112:def main():` |
| worktree | `grep -n -F "def worktree(" ops/desk/stop-guard.py` | 0 | `57:def worktree(cwd):` |
| report_last_line | `grep -n -F "def report_last_line(" ops/desk/stop-guard.py` | 0 | `100:def report_last_line(transcript_path, cwd):` |
| first_user_text | `grep -n -F "def first_user_text(" ops/desk/stop-guard.py` | 0 | `65:def first_user_text(transcript_path):` |
| WT_ROOT | `grep -n -F "WT_ROOT = " ops/desk/stop-guard.py` | 0 | `37:WT_ROOT = "/Users/cobalt/cobalt-wt"` |
| stop_hook_active | `grep -n -F "stop_hook_active" ops/desk/stop-guard.py` | 0 | `4:# …` · `119:    if event.get("stop_hook_active"):` |
| callers of report_last_line | `grep -rn -F "report_last_line(" ops src tests` | 0 | `ops/desk/stop-guard.py:13` (comment) · `ops/desk/stop-guard.py:100` (def) · `ops/desk/stop-guard.py:130` · `ops/desk/idle-wake.py:42:        last = guard.report_last_line(event.get("transcript_path") or "", cwd)` |
| readers of stop-guard.py | `grep -rn -F "stop-guard.py" ops tests src` | 0 | `ops/desk/stop-guard.py:2,25` · `ops/desk/idle-wake.py:8,23,26` · `tests/ops/test_stop_guard.py:1,24,25,27,235` · `tests/ops/test_idle_wake.py:3,25,115` |
| bare-guard desk rule | `grep -n -F "CTO-DESK-WAKEUP.md" ops/desk/bare-guard.py` | 0 | `16:# with CTO-DESK-WAKEUP.md = desk, …` · `736:    elif in_repo and hub == "CTO-DESK-WAKEUP.md":` |
| stage | `grep -n -F "def stage(" tests/ops/test_stop_guard.py` | 0 | `23:def stage(tmp_path: Path) -> Path:` |
| desk exempt test | `grep -n -F "def test_the_desk_and_the_brain_cwd_is_exempt_and_reads_no_report(" …` | 0 | `101:` |
| install test | `grep -n -F "def test_i1_run_his_install_text(" …` | 0 | `233:` |
| wake-up EVERY TURN | `grep -n -F "EVERY TURN:" "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` | 0 | `40:EVERY TURN: every turn begun by his message …` |
| wake-up ON TRIGGER | `grep -n -F "ON TRIGGER" …` | 0 | `42:ON TRIGGER — open, then act …` |
| G6 red on BASE | `grep -c -F "OWED (his 10-06 R590;" "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` | 1 | `0` |
| restarts rule (op script) | `grep -n -F "operator script; no Cobalt reader" src/cobalt/jobs/restarts.py` | 0 | `232:` |
| restarts rule (tests) | `grep -n -F "test/documentation; no resident" src/cobalt/jobs/restarts.py` | 0 | `246:` |
| wc -l | `wc -l ops/desk/stop-guard.py tests/ops/test_stop_guard.py "docs/…/CTO-DESK-WAKEUP.md"` | 0 | `138` · `251` · `49` |
| wc -c BEFORE | `wc -c "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` | 0 | `11136` |
| tail words | `tail -n 3 ".../cto-2026-10-06-words.md"` | 0 | last line `> For a single-feature deploy, the desk writes the deploy card with ops/desk/deploy-card.sh plus header values: …` |
| tail desk report | `tail -n 3 ".../cto-2026-10-06.md"` | 0 | last line `HANDOVER: predecessor 9149c1a1 → successor 02bc7d67 at 06:09 ET` |
| restarts | `uv run cobalt jobs restarts 18d9da5b..HEAD` | 0 | `docs/40 - DevDocs/reports/desk-stop-guard-build-2026-10-06.md	A	DOCS	-` · `RESTARTS: none` (only this report, untracked) |

Card `## RECORDS`, copied and re-read:
- "Citations proven at main HEAD `d2f651ce` … see `reports/desk-stop-guard-draft-2026-10-06.md` `## RECORDS`." — `grep -n -F "## RECORDS"` on that report → `26:## RECORDS` (present). Every card citation used here re-read above.
- "`/Users/cobalt/.claude/ops/desk-list.sh` is a separate untracked copy (not a symlink; it lacks the tracked copy's id-less-row skip)" — `ls -la` both → regular files, 442 and 868 bytes; `grep -n -F "skipped" /Users/cobalt/.claude/ops/desk-list.sh` → exit 1 (no skip). Holds.

DB: none card — no lock probe, no with-DB string.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → exit 0: `3963 passed, 787 skipped, 1 xfailed, 36 warnings in 602.12s (0:10:02)`. Skips: `Postgres env settings not available`, `reaches cobalt_dev (lock-relief G1)`, and the two `COBALT_LIVE_VAULT_ROOT not set` (live-note, run next).
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → exit 0: `146 passed, 1 skipped, 15 warnings in 25.08s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (no skip names `COBALT_LIVE_VAULT_ROOT`).
- Card's gate files on BASE: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py` → `37 passed, 15 warnings in 4.31s`. `test_stop_guard.py` test count BEFORE: `--collect-only` → `30 tests collected`.

## E2 RED
Tests only, in `tests/ops/test_stop_guard.py`: `stage()` now also replaces `"/Users/cobalt/cobalt"` (with its quotes) by `tmp_path/repo`, after the `-wt` replacement; a `Desk` world beside `World`; 37 new tests (G1-G5). No `src/` or `ops/` edit. Commit `1f07578c wip(desk-stop-guard): red — desk seat tests G1-G5 (card 66)`.

`uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/ops/test_stop_guard.py` → exit 1: `25 failed, 42 passed, 15 warnings in 2.62s` (the 30 existing tests green). `-rA --tb=no -k "g1 or g2 or g3 or g4 or g5"` → `25 failed, 12 passed, 30 deselected`:
- RED, each for its row's reason (BASE exits 0 at `:122-123` before any read): G1 `test_g1_the_desk_with_no_owed_block_is_blocked` (`assert (0, '', '') == (2, '', 'star...6-10-07.md\n')`), `test_g1_a_cwd_below_the_repo_is_the_desk` (`assert 0 == 2`); G2 `…an_item_with_no_marker_blocks` (`assert (0, '', '') == (2, '', 'star... rebuild x\n')`), `…an_item_with_an_unknown_marker_blocks`, `…no_report_for_today_blocks`, `…a_report_with_no_current_section_blocks`, `…the_block_under_history_only_blocks`, `…the_block_before_a_blank_line_and_the_table_is_read_as_the_block` (`assert (0, '') == (2, 'start it: b\n')`); G3 `…a_session_id_with_no_row_blocks`, `…the_desks_own_row_is_not_live`, `…a_short_id_is_not_live` (`assert (0, '') == (2, 'start it: build x\n')`), `…a_watch_with_no_process_blocks` (`assert (0, '') == (2, 'start it: watch x\n')`); G4 `…three_blocks_then_the_fourth_stop_gives_up_and_records` (`assert [0, 0, 0, 0] == [2, 2, 2, 0]`), `…a_new_message_resets_the_count` (`assert [0, 0] == [2, 2]`), `…a_settled_block_removes_the_count` (`assert 0 == 2`), `…the_first_unsettled_item_is_named`; G5 (stderr empty: `where '' = CompletedProcess(…returncode=0, stdout='', stderr='').stderr`) `…a_garbage_block_fails_open`, `…an_unparseable_block_fails_open[two-bars|none-beside-an-item|empty-live]`, `…a_directory_at_the_report_path_fails_open`, `…a_failing_desk_list_fails_open`, `…a_directory_at_the_count_file_fails_open`, `…active_with_no_count_file_fails_open`, `…a_count_file_out_of_range_fails_open`.
- NEGATIVE CONTROLS, PASSED on BASE: `test_g1_no_other_seat_in_the_repo_is_the_desk[brain|deploy|close|prompt-seat|prose|later-read]`, `test_g1_the_desk_message_outside_the_repo_is_not_the_desk`, `test_g1_an_unreadable_desk_transcript_is_not_the_desk`, `test_g2_owed_none_lets_the_turn_end`, `test_g2_an_item_waiting_on_dejan_lets_the_turn_end`, `test_g3_a_live_session_id_lets_the_turn_end`, `test_g3_a_running_watch_on_the_path_lets_the_turn_end`.
- G6 red: `grep -c -F "OWED (his 10-06 R590;" "docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` → `0` (PREFLIGHT); `test_i1_run_his_install_text` PASSED on BASE (negative control).

## E3 THE ROWS
Commit `8d6540f5 feat(desk-stop-guard): the Stop hook guards the CTO desk seat on its OWED block (G1-G6, L1 L3 L28 L72)` — `ops/desk/stop-guard.py`, `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` (`git diff --stat`: 212 insertions, 14 deletions).

What was built, in the card's order:
- G1 `REPO = "/Users/cobalt/cobalt"` beside `WT_ROOT`; `main()`: unreadable JSON → 0; `worktree(cwd)` → `worker(event, cwd)` (the old body, its `stop_hook_active` exit moved inside, unchanged otherwise); `is_desk(event)` (cwd `== REPO` or `startswith(REPO + "/")`, the first `Read '([^']+)'` of `first_user_text`, basename `CTO-DESK-WAKEUP.md`; any exception reading the transcript → not the desk) → `desk(event)`; else 0. `worktree()`, `first_user_text()`, `report_path()`, `report_last_line()` untouched.
- G2 `desk_report()` (`REPO + "/docs/40 - DevDocs/reports/cto-<ET date>.md"`), `owed_block()`.
- G3 `listed()` (`sh <dir>/desk-list.sh`, timeout 20), `watched()` (PGREP, timeout 10, exit 1 = none, >1 → G5), `unsettled()` (each read command run at most once per stop, lazily).
- G4 `desk()`: the count file `<transcript_path>.desk-stop`, `BLOCKS = 3`, the `DESK-STOP` line `<ISO ET> <session_id> GAVE UP after 3 blocks — start it: <what>`.
- G5 `Unguarded` and one `except Exception` around `desk(event)` in `main()` → stderr `stop-guard: desk not guarded — <reason>`, exit 0.
- G6 (a) header `:2-31` rewritten (the desk seat, OWED block, count file, DESK-STOP line, the two read commands, the desk path writes); `INSTALL BEGIN…END` unchanged. (b) the WAKE-UP LINE, byte for byte.

Row tests after the rows: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py` → `74 passed, 15 warnings in 3.62s` (after G1-G5), `74 passed, 15 warnings in 3.66s` (after G6). `test_stop_guard.py` count AFTER: `67 tests collected` (BEFORE 30).

G6 proofs: `grep -c -F "OWED (his 10-06 R590;" ".../CTO-DESK-WAKEUP.md"` → `1` (BASE `0`); `grep -n -F` → `42:OWED (his 10-06 R590; …`; `grep -n -F "EVERY TURN:"` → `40:`; `grep -n -F "ON TRIGGER"` → `44:`; `wc -c` BEFORE `11136`, AFTER `11608`; `git diff --stat 18d9da5b -- ".../CTO-DESK-WAKEUP.md"` → `1 file changed, 2 insertions(+)` (the line and its blank line).

THE MUTATIONS (Edit tool, run alone, undone with Edit):
| row | mutation | run | result, first failing line |
|---|---|---|---|
| G1 fix | `if False and is_desk(event):` | `-k g1` | `2 failed, 8 passed` — `test_g1_the_desk_with_no_owed_block_is_blocked`: `assert (0, '', '') == (2, '', 'star...6-10-07.md\n')`; `test_g1_a_cwd_below_the_repo_is_the_desk`: `assert 0 == 2` |
| G1 control | seat by substring: `return DESK_HUB in (text or "")` | `-k g1` | `2 failed, 8 passed` — `[prose]`, `[later-read]` |
| G1 control | cwd `cwd.startswith(REPO)` (no `/`) | `-k g1` | `1 failed, 9 passed` — `test_g1_the_desk_message_outside_the_repo_is_not_the_desk` |
| G2 fix | missing block → `what = None` | `-k g2` | `3 failed, 5 passed` — `no_report_for_today` `assert (0, '', '') == (2, '', 'star...6-10-07.md\n')`, `no_current_section`, `under_history_only` |
| G2 fix | an item with no / unknown marker settles | `-k g2` | `3 failed, 5 passed` — `no_marker` `assert (0, '', '') == (2, '', 'star... rebuild x\n')`, `unknown_marker`, `blank_line_and_the_table` `assert (0, '') == (2, 'start it: b\n')` |
| G2 control | `waiting on Dejan` not settled (`marker == WAITING + "!"`) | `-k g2` | `2 failed, 6 passed` — `an_item_waiting_on_dejan_lets_the_turn_end`, `blank_line_and_the_table` |
| G3 fix | every `live:` trusted | `-k g3` | `4 failed, 2 passed` — `no_row` `assert (0, '') == (2, 'start it: build x\n')`, `desks_own_row`, `short_id`, `watch_with_no_process` `assert (0, '') == (2, 'start it: watch x\n')` |
| G3 fix | drop `name != "cto-desk"` and the id rule (`if True:`) | `-k g3` | `2 failed, 4 passed` — `the_desks_own_row_is_not_live`, `a_short_id_is_not_live` |
| G3 control | watch path `path + "x" in line` | `-k g3` | `1 failed, 5 passed` — `a_running_watch_on_the_path_lets_the_turn_end` |
| G3 control | id equality, not prefix (`i == sid`) | `-k g3` | `1 failed, 5 passed` — `a_live_session_id_lets_the_turn_end` |
| G4 fix | `count < BLOCKS + 1` | `-k g4` | `1 failed, 3 passed` — `assert [2, 2, 2, 2] == [2, 2, 2, 0]` |
| G4 fix | count read when not active + no unlink when settled | `-k g4` | `2 failed, 2 passed` — `a_new_message_resets_the_count` `assert '3' == '1'`; `a_settled_block_removes_the_count` `assert not True` (`desk.jsonl.desk-stop` exists) |
| G4 fix | `reversed(items)` | `-k g4` | `1 failed, 3 passed` — `assert (2, '', 'start it: b\n') == (2, '', 'start it: a\n')` |
| G5 fix | `except ZeroDivisionError` | `-k g5` | `9 failed` — each a traceback, exit 1, with its own reason, e.g. `Unguarded: an empty item in: OWED:  | | live:` · `more than one ' | ' in: …` · `` `owed: none` beside an OWED: line `` · `an empty live: value in: OWED: x | live:` · `the report cannot be read: …cto-2026-10-07.md'` · `desk-list.sh exit 1` · `…desk.jsonl.desk-stop'` · `stop_hook_active with no count file` · `the count file holds '7'`; `assert 1 == 0` |
| G6 | `R590` → `R59` in the line | `grep -c -F "OWED (his 10-06 R590;"` | `0` |
After the last undo: `wc -c` → `11608`; `git diff --stat` → `CTO-DESK-WAKEUP.md | 2 +`, `ops/desk/stop-guard.py | 224 +++…--` (the fix, uncommitted then); `74 passed, 15 warnings in 4.57s`. No named test stayed green under its mutation.

DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (`ls` of that folder lists `src/cobalt` module pages only; `Grep stop-guard|idle-wake|bare-guard` there → no files). The hook's header comment is its doc (G6 a); no page was made (outside the rows). Recorded under `## RECORDS`.

## RESTARTS
`uv run cobalt jobs restarts 18d9da5b..HEAD` → exit 0, whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/reports/desk-stop-guard-build-2026-10-06.md	A	DOCS	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. As the card expected.

## W THE THREE SUITES
`<tip>` = `8d6540f5`.
- (a0) `git diff --name-only --no-renames 18d9da5b` → exit 0, whole: `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md` · `ops/desk/stop-guard.py` · `tests/ops/test_stop_guard.py` — every path under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 3 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-stop-guard-1006b offline` → exit 0: `offline 3963/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-stop-guard-1006b-offline-20261007-062157.log` (its line 862: `3963 passed, 787 skipped, 1 xfailed, 36 warnings in 602.32s (0:10:02)`). This build adds no test under `tests/cobalt` or `tests/taxonomy`; its 37 new tests are in `tests/ops/test_stop_guard.py` (run below).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh desk-stop-guard-1006b livenote` → exit 0: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/desk-stop-guard-1006b-livenote-20261007-063212.log` (line 57: `146 passed, 1 skipped, 15 warnings in 25.02s`); `grep -n -F "COBALT_LIVE_VAULT_ROOT not set" <log>` → no line.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → exit 0: `1499 passed, 1 xfailed, 15 warnings in 370.98s (0:06:10)` (run at `8d6540f5`).
- THE CARD'S DEPLOY GATE: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py` at the tip → `74 passed, 15 warnings in 3.59s`; then `tests/ops` → `1499 passed, 1 xfailed` (above). `test_stop_guard.py`: 30 tests BEFORE, 67 AFTER (`--collect-only`).
- with-DB: `not run (DB: none)`. `ls /Users/cobalt/cobalt-wt/desk-stop-guard-1006b/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown RED for its named reason against a mutation or negative control — YES: the 25 E2 reds (quoted under `## E2 RED`, each `0 != 2` or empty stderr on BASE) and every one of the 12 negative controls turned red under an E3 mutation (`[prose]`, `[later-read]`, `outside_the_repo`, `waiting_on_dejan`, `running_watch`, `live_session_id` — table under `## E3`); `test_g1_an_unreadable_desk_transcript_is_not_the_desk`, `[brain|deploy|close|prompt-seat]` and `test_g2_owed_none_lets_the_turn_end` are the card's NEGATIVE CONTROLS, shown PASSING on BASE (E2) and after (E3), as the card's rows require; no mutation was run against these five. The `stage()` change is pinned by every Desk test (REPO unstaged → the desk is never reached → the G1 red). No test stayed green under its row's mutation.
(2) Every entry path pinned — callers of `report_last_line` (PREFLIGHT: `ops/desk/idle-wake.py:42`; re-read at tip `42:        last = guard.report_last_line(…)`) → `tests/ops/test_idle_wake.py` green (in the 74); the worker path → the 30 existing tests unchanged and green; `test_the_desk_and_the_brain_cwd_is_exempt_and_reads_no_report` body unchanged (literal `/Users/cobalt/cobalt` is not the staged repo) and green. Desk entry: cwd = repo (`test_g1_the_desk_with_no_owed_block_is_blocked`), under repo (`…a_cwd_below_the_repo_is_the_desk`), sibling `repo-other` (`…outside_the_repo…`), unreadable transcript, each seat (`[brain|deploy|close|prompt-seat|prose|later-read]`). `stop_hook_active` false/true, count 0-3, bad count, missing count: G4 / G5 tests. Day state: the report at today's ET date, missing (`no_report_for_today`).
(3) Re-read at the tip: `git show 8d6540f5:ops/desk/stop-guard.py` (whole), `grep -n -F "    if is_desk(event):"` → `306:`, `grep -n -F "# INSTALL BEGIN"` → `36:`, `grep -n -F "guard.report_last_line("` idle-wake → `42:`, the G6 greps (`42:`, `40:`, `44:`, count `1`, `wc -c` `11608`), `git log --oneline 18d9da5b..HEAD`, `git diff --stat 18d9da5b..HEAD -- ops/desk/idle-wake.py ops/desk/bare-guard.py ops/desk/desk-list.sh .claude` → nothing.

## FOR THE CHECK
- Range `18d9da5b..8d6540f5`: `1f07578c wip(desk-stop-guard): red — desk seat tests G1-G5 (card 66)` · `8d6540f5 feat(desk-stop-guard): the Stop hook guards the CTO desk seat on its OWED block (G1-G6, L1 L3 L28 L72)`; the report commit follows.
- Per row: reds `## E2 RED`; mutations `## E3` table; greens `74 passed` (two files), `1499 passed, 1 xfailed` (`tests/ops`).
- Caller greps: PREFLIGHT table (`report_last_line(`, `stop-guard.py`).
- RUN rows: none in this card.
- Suites: offline `3963/0`, live-note `146/0` (commands and logs under `## W`); with-DB `not run (DB: none)`. `<F0>/<F1>/<F2>`: `not run (DB: none)`. Lock taken/released: `not run (DB: none)`.
- RESTARTS table: `## RESTARTS` (`RESTARTS: none`).
- Records copied at PREFLIGHT: `## PREFLIGHT` end.
- For the check asks: X1 → `is_desk()` needs cwd under REPO AND the first `Read '…'` basename = `CTO-DESK-WAKEUP.md`; worker cwds go to `worker()` first, so a worker whose message names the wake-up file never reaches the desk path. X2 → every exit 2 is in `desk()` behind `count < BLOCKS`; every count read/write error raises into the one `except Exception` → 0. X3 → short id (`SESSION_ID.fullmatch`, 8+), the desk's own row (`name != "cto-desk"`) pinned; a prefix of another session's id and a watch on a path that CONTAINS `<path>` pass as live, as the card's G3 text states (row id "equals `<id>` or starts with it"; a pgrep line that "contains `<path>`") — built as written, not re-decided (L72). X4 → `worker()` is the old body after the moved `stop_hook_active` exit; `test_idle_wake.py` stages the new file and is green.

## CONTINUE
next: none — BUILT; the desk verifies the artifact and launches the check.

## DECISIONS
none

## RECORDS
- L74: one system reminder at 06:05 EDT asked for a `Claude-Session:` line in commits; recorded under `## L74`, not followed. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.
- DevDocs: `docs/40 - DevDocs/cobalt/` has no page for `ops/desk/` scripts; no dated line written, no page made (outside the rows). The hook's header comment (G6 a) is its doc.
- The card's records, re-read at PREFLIGHT: the drafter report's `## RECORDS` exists (`26:`); `/Users/cobalt/.claude/ops/desk-list.sh` is a separate 442-byte file without the `skipped` handling (tracked copy 868 bytes). G3 runs the tracked copy beside the hook.
- No extra lock take; no `REFUSED, not needed`; no `CONTINUED`.
- The report path's date is the card's (`…-2026-10-06.md`); the build ran 2026-10-07 06:05-06:33 EDT.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: desk-stop-guard · tip: 8d6540f5 | on 18d9da5b | migration: none | offline 3963/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 6 of 6 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 197604
