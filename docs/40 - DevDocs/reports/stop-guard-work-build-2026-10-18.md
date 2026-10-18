# stop-guard-work-1018 — build report 2026-10-18 (routed card 739, BAND MID, builder grok-4.7, gate seat stop-guard-work-1018-gate)

## §0 Headline
Grok 4.7 built W1, W2 and W4 in three passes: T, S, and one S2 that fixed its own test. The seat ran every command. Tip `9b9177ea`: stop-guard tests 125 passed, `tests/ops` 3935 passed, gate offline 8507/0, live-note 146/0. The suites were red at their first run: one Grok test re-staged `Sized` into a used `tmp_path`. S2 #1 fixed it. The seat ran no mutations: its write fence is the instructions and this report (DECISION 2). `RESTARTS` names the untracked `SHADOW-INSTRUCTIONS.md` (DECISION 1).

## L74
A `Claude-Session:` attribution block arrived in a system reminder during the session. Recorded here once; no commit carries it. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh shadow "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/739-stop-guard-work-card.md"`:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/739-stop-guard-work-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/739-stop-guard-work-card.md" · 0 · 6b33017d0784105e624bcc590f8c6b4bddf77e42
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/739-stop-guard-work-card.md" · 0 · nothing
STANDING LIST 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
STANDING LIST 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
STANDING LIST 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1841 row · grep -n "^| R1841 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 39:| R1841 | 06:25 ET | HIS RULING (brain relays, L79): the desk does not idle; until MVP it launches the next card, every turn ends with a live worker and watch, the night is a shift. Words: [R1841](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at 06:46 |
RULING 2026-10-18 R1841 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1841 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 7317d540b338bf299f1e555362b25230a75d1120
RULING 2026-10-18 R1841 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-18 R1863 row · grep -n "^| R1863 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 17:| R1863 | 07:09 ET | HIS RULING · APPROVED (brain, L79): work first, tools second; morning work runs to end; agy read card drafted now (his Gemini ask); tool polish = one question, never a stop. Words: cto-2026-10-18-words.md. | APPLIED: topics/cto-desk-contract.md, areas/cobalt.md at 07:09 |
RULING 2026-10-18 R1863 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1863 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 11563e825a4ca9f5dffbae3ce05e012cdfe61838
RULING 2026-10-18 R1863 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh shadow "<card>"`:
```
clock · date · 0 · Sun Oct 18 07:13:13 EDT 2026
status · git status --short --branch · 0 · ## ops/stop-guard-work-1018
head · git log --oneline -1 · 0 · 7317d540 docs(desk): R1841-R1842 no idle desk, stop-guard drafter prompt, handover plan
diff · git diff --stat 7317d540 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/stop-guard-work-1018 · 0 · 7317d540 docs(desk): R1841-R1842 no idle desk, stop-guard drafter prompt, handover plan
env here · ls /Users/cobalt/cobalt-wt/stop-guard-work-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/test-llm-reds-1018/.env
PREFLIGHT OK
```
- `git show --stat 7317d540` → `docs(desk): R1841-R1842 no idle desk, stop-guard drafter prompt, handover plan`, 5 docs files, `58 insertions(+), 17 deletions(-)`.
- `git diff --stat 7317d540 main` → 44 files, every one under `docs/40 - DevDocs/`; `ops/desk/stop-guard.py` and `tests/ops/test_stop_guard.py` are not among them, so main equals BASE for both.
- Symbols: the seat read `ops/desk/stop-guard.py` at BASE in full. Every card `file:line` matches: `CURRENT :117`, `WAITING :123`, `BRAIN :127`, `PGREP :131`, `BLOCKS :132`, `PREDECESSOR :147`, `owed_block :263`, `queued :302` (walk `:306-308`), `listed :320`, `watched :334`, `unsettled :345`, `finished_open :379`, `desk :407`, the `finished_open` call `:429-430`, `ListUnreadable` `:431-432`, `start it:` `:434`, cap and record `:445-454`, `handed_over :466-469`. Tests at BASE: `stage :30-39`, `ROW :305`, `Desk :313-369`, `watcher :536-541`, G4 `:568-579`, G7 end `:808-812`, card-458 block `:815`, `SID :817`, `Sized :837`.
- `wc -l` → `719 ops/desk/stop-guard.py`, `1124 tests/ops/test_stop_guard.py`.
- `cto-2026-10-17.md` (worktree = main): `:107 owed: none`, `:108 STATE AT 21:07 …`, `:109 NEXT (not launched, so not OWED, R590): …`, `:122 HANDOVER: predecessor 5cf91de3 → successor 8ea7dcd3 at 21:06 · pane w2:pV1`.
- `uv run cobalt jobs restarts 7317d540..HEAD` → `path	change	rule	restart` / `RESTARTS: none` (empty range).
- Card preflight: `reports/stop-guard-work-r2-preflight-2026-10-18.md` last line `PREFLIGHT DONE · card: stop-guard-work-1018 · checks: 19 · fails: 0 · ready: YES`.
- DB: none: no lock probe.

## E0 BASELINE
- W0 (card): `uv run pytest -q -p no:cacheprovider tests/ops/test_stop_guard.py` on BASE → `110 passed, 15 warnings in 64.44s (0:01:04)`.
- offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4572 passed, 806 skipped, 1 xfailed, 36 warnings in 781.46s (0:13:01)`.
- live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 29.70s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## THE INSTRUCTIONS
`/Users/cobalt/cobalt-wt/stop-guard-work-1018/SHADOW-INSTRUCTIONS.md` is untracked and never committed. It holds the whole card, the two RULINGS rows as `authorize.sh` printed them, BUILD-HUB `## E2` and `## E3` verbatim, and the fence (`ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py`, no exceptions: a routed card with no original build, and no DevDocs page for `ops/desk/`). It also points at lines 108, 109 and 122 of `cto-2026-10-17.md` and carries the seat's notes, facts read in the folder: the `sid` argument the card's `desk()` text leaves out (the preflight's NOTE), `Sized`'s per-turn stderr lines, where `owed()` ends the report, the pgrep rewrite, and the 160 cut. `## PASS S2` was added before pass S2.

## PASSES
| pass | env check | command as run | wall | builder tokens | diff stat | commit |
|---|---|---|---|---|---|---|
| T | `ls: /Users/cobalt/cobalt-wt/stop-guard-work-1018/.env: No such file or directory` | `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/stop-guard-work-1018/**)" -p "You are GROK (xAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass T: tests only under tests/. Write only the rows' files. Run no command. Reply with the list of files you wrote."` | 07:28:57 → 07:36:22 (7.4 min) | UNKNOWN (Grok prints none) | `tests/ops/test_stop_guard.py | 229 +++…` / `1 file changed, 229 insertions(+)` | `61d3169a wip(stop-guard-work-1018): red` |
| S | `ls: /Users/cobalt/cobalt-wt/stop-guard-work-1018/.env: No such file or directory` | the same with `Pass S: the rows.` | 07:36:42 → 07:41:49 (5.1 min) | UNKNOWN | `ops/desk/stop-guard.py | 121 +++…` / `1 file changed, 121 insertions(+)` | `f8190fbc feat(stop-guard-work-1018): rows` |
| S2 #1 | `ls: /Users/cobalt/cobalt-wt/stop-guard-work-1018/.env: No such file or directory` | the same with `Pass S2: fix the failing lines quoted under PASS S2.` | 08:12:57 → 08:13:43 (0.8 min) | UNKNOWN | `tests/ops/test_stop_guard.py | 8 ++++++--` / `1 file changed, 6 insertions(+), 2 deletions(-)` | `9b9177ea fix(stop-guard-work-1018): pass S2 1` |

Grok's replies: T `- tests/ops/test_stop_guard.py`; S `- ops/desk/stop-guard.py` ("The tests already match the card, so Pass S only changes the guard"); S2 `- tests/ops/test_stop_guard.py`. Every path is inside the fence: no `SCOPE`.

## E2 RED
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py -k "test_w1 or test_w2 or test_w4"` at `61d3169a` (guard = BASE) → `11 failed, 4 passed, 110 deselected, 15 warnings in 2.21s`. The first line of each red:
- `test_w1_the_1017_2107_shape_with_nothing_live_blocks` → `AssertionError: assert (0, '', '') == (2, '', 'star...drafters …\n')`. Returncode `0` where `2` is asserted, as the card says.
- `test_w1_the_first_unwaiting_item_is_the_one_named` → `assert (0, '', '') == (2, '', 'start it: b\n')`
- `test_w1_a_semicolon_inside_parentheses_does_not_split` → `assert (0, '', '') == (2, '', 'star...: x (a; b)\n')`
- `test_w1_the_count_and_the_record_stand` → `assert [0, 0, 0, 0] == [2, 2, 2, 0]`
- `test_w2_a_live_worker_alone_blocks` → `assert (0, '', '') == (2, '', 'star...drafters …\n')`
- `test_w2_an_armed_watch_alone_blocks` → `assert (0, '', '') == (2, '', 'star...drafters …\n')`
- `test_w2_a_brain_row_is_not_live` → `assert (0, '', '') == (2, '', 'star... next card\n')`
- `test_w4_a_dead_successor_is_still_blocked` → `assert (0, '', '') == (2, '', 'star...drafters …\n')`
- `test_w4_a_missing_successor_is_still_blocked` → `assert (0, '', '') == (2, '', 'star...drafters …\n')`
- `test_w4_a_handover_naming_another_predecessor_is_still_blocked` → `assert 'DESK SIZE 123,456 / 300,000' == 'start it: th...by drafters …'`
- `test_w4_only_the_last_handover_line_counts` → `assert 'DESK SIZE 123,456 / 300,000' == 'start it: th...by drafters …'`

Green on BASE (the card's controls): `test_w1_no_next_line_changes_nothing`, `test_w2_an_all_waiting_next_block_passes`, `test_w2_a_live_worker_and_an_armed_watch_pass`, `test_w4_the_blocked_shape_with_a_refresh_to_a_live_successor_passes` (exit 0 on BASE: no block exists).

## E3 THE ROWS
- After pass S (`f8190fbc`): `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py` → `1 failed, 124 passed, 15 warnings in 60.60s (0:01:00)`. The red is `test_w4_a_missing_successor_is_still_blocked` → `FileExistsError: [Errno 17] File exists: '…/test_w4_a_missing_successor_is0/repo/docs/40 - DevDocs/reports'` at `d = Sized(tmp_path)` (`tests/ops/test_stop_guard.py:1012`). It is the builder's own test, not the guard: the first half of that test, the no-HANDOVER block, passed.
- After pass S2 #1 (`9b9177ea`): the same command → `125 passed, 15 warnings in 60.54s (0:01:00)`.
- The rows at tip (`grep -n -E`): `333:def next_items(lines):`, `470:def _waiting_on(text):`, `484:def refreshing(lines, sid, listing):`, `505:def next_unlaunched(lines, sid, listing):`, `551:                what = next_unlaunched(lines, event.get("session_id"), listing)`. Constants `NEXT`, `WAITING_ON` beside `WAITING`; `SUCCESSOR` beside `PREDECESSOR`; the header comment has a 10-line paragraph after the FINISHED rule.
- MUTATIONS: not run (DECISION 2).

## RESTARTS
`uv run cobalt jobs restarts 7317d540..HEAD` at tip (exit 1):
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/reports/stop-guard-work-build-2026-10-18.md	A	DOCS	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_stop_guard.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The tool reads the working tree's untracked files. The committed range `git diff --name-only --no-renames 7317d540` → `ops/desk/stop-guard.py`, `tests/ops/test_stop_guard.py`, both classified `-`. See DECISION 1.

## W THE THREE SUITES
DB: none → (a0), (a), (e), plus `tests/ops`.
- (a0) `git diff --name-only --no-renames 7317d540` → `ops/desk/stop-guard.py` / `tests/ops/test_stop_guard.py`: every path under `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 2 paths)`**.
- First run, at `f8190fbc`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh stop-guard-work-1018 offline` → exit 1: `tests/ops: run (ops/desk/stop-guard.py)` / `RED (exit 1): 1 failed, 3934 passed, 1 xfailed, 16 warnings in 981.16s (0:16:21)` (the same `FileExistsError`) / `log: /Users/cobalt/cobalt-wt/.gate-logs/stop-guard-work-1018-offline-20261018-074313.log`. **Suites at first run: red.**
- Second run, at tip `9b9177ea`: `sh /Users/cobalt/cobalt/ops/desk/gate.sh stop-guard-work-1018 offline` → exit 0: `tests/ops: run (ops/desk/stop-guard.py)` / `offline 8507/0` / `log: /Users/cobalt/cobalt-wt/.gate-logs/stop-guard-work-1018-offline-20261018-081458.log`.
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh stop-guard-work-1018 livenote` → `live-note 146/0` / `log: /Users/cobalt/cobalt-wt/.gate-logs/stop-guard-work-1018-livenote-20261018-084432.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3935 passed, 1 xfailed, 16 warnings in 972.29s (0:16:12)`.
- with-DB: not run (DB: none). F0/F1/F2: not run (DB: none). Lock: not run (DB: none).
- `ls -la /Users/cobalt/cobalt-wt/stop-guard-work-1018/.env` → `No such file or directory` (09:01).
- W3 (card): `tests/ops/test_stop_guard.py` → `125 passed` (0 failed); `tests/ops` → `3935 passed` (0 failed); `RESTARTS:` line above; `git diff 7317d540 --stat` → `ops/desk/stop-guard.py | 121`, `tests/ops/test_stop_guard.py | 233`, `2 files changed, 354 insertions(+)`.

## PRE-STOP SELF-CHECK
(1) The 11 reds against BASE are quoted under `## E2 RED`. The 4 controls are green on BASE and after. The W4 pass test was never shown red against W1-without-`refreshing`, and no mutation was run (DECISION 2). **Not met.**
(2) `desk()` is the one caller of `next_unlaunched` (line 551 at tip). The tests pin: the no-NEXT path (`test_w1_no_next_line_changes_nothing`, no `desk-list.sh` staged), the all-waiting path, the AND of worker and watch (both `…alone_blocks` tests and `…and_an_armed_watch_pass`), the brain row, the count and cap, and the four refresh shapes. Met.
(3) Re-read at tip: the `grep -n -E` of the four defs and the call line, `git log --oneline 7317d540..HEAD`, `git diff 7317d540 --stat`, the RESTARTS table, `desk-context.sh`. Met.
→ `self-check: 2 of 3`.

## FOR THE CHECK
- `7317d540..9b9177ea`: `61d3169a wip(stop-guard-work-1018): red`, `f8190fbc feat(stop-guard-work-1018): rows`, `9b9177ea fix(stop-guard-work-1018): pass S2 1`. Scored build = `9b9177ea`.
- The seat's reading of the diff, for X1: `desk()` gains exactly the two lines `if what is None:` / `what = next_unlaunched(lines, event.get("session_id"), listing)`. `owed_block`, `queued`, `unsettled`, `finished_open` and the cap appear in no hunk (`git diff 7317d540 -- ops/desk/stop-guard.py`, 6 hunks: header, constants ×2, `next_items`, the three new functions, `desk()`).
- Read by the seat, not run: `next_unlaunched` checks `refreshing` AFTER it has taken `listing` (it runs `listed()` once when `listing` is None) and BEFORE `watched()`. The card says "before any of that". The result is the same: `listed()` runs only once an unwaiting item exists, and at most once.
- Read by the seat, not run: `next_items` returns the pieces of the FIRST `NEXT` line even when they are all empty (`[]`); it does not go on to a later `NEXT` line. That matches the card's "the first line that is NEXT …".
- X2: `NEXT_1017`, `STATE_1017` and `HANDOVER_REAL` are split across Python string literals in the test file. The seat did not byte-compare them with lines 108, 109 and 122; that is the check's to run. The pgrep isolation is `isolate_pgrep(d)` (asserts the needle exists, then rewrites `d.hook`).
- X4: not run by the seat (a check ask).
- The card's text about W4 on BASE says "every W4 case exits 0". In fact the two `Sized` cases whose last HANDOVER line does not name `SID` exit 2 on BASE, from the per-turn lines (`DESK SIZE 123,456 / 300,000`). Their red was that the last stderr line is not `start it: …`.

## CONTINUE
next: none (CLOSE written)

## DECISIONS
- DECISION 1 (RESTARTS): `cobalt jobs restarts 7317d540..HEAD` reads the untracked `SHADOW-INSTRUCTIONS.md` and prints `UNCLASSIFIED` with six restarts. The seat may not write `configs/cobalt/jobs.yaml`: its fence is this report and the instructions. The file is the launcher's, its ignored path is X9's and still open, so it never reaches main. The committed range's two paths are both `-`. Safe default: the stop line carries `RESTARTS: none (committed range; the tool's line names only the untracked SHADOW-INSTRUCTIONS.md)`, and the tool's own line is quoted under `## RESTARTS`. The deploy derives its own.
- DECISION 2 (mutations, self-check 1): SHADOW-HUB lets the gate seat write only `SHADOW-INSTRUCTIONS.md` and the report (G5, kind `shadow`). So the card's three MUTATIONS were not made: `next_unlaunched` → None, the worker-AND-watch `and` → `or`, `refreshing` → False. Neither was the ORDER step "W1 without `refreshing` → the W4 pass test RED", because Grok wrote W1 and W4 in the one pass S. Safe default: `self-check: 2 of 3`. The check runs the three mutations on `9b9177ea`.
- DECISION 3 (the per-turn lines on BASE): the W4 `Sized` tests on BASE exit 2 from per-turn lines, not 0 as the card says (`## FOR THE CHECK`). This is a recorded fact, and no test was changed for it.
- DECISION 4 (the builder's own red): the suites at first run were red because of one Grok test (`FileExistsError`, a second `Sized(tmp_path)`). S2 #1 fixed it in the test file only. For the routing results file this is "the model's own red", fixed in 1 of 2 re-passes.

## RECORDS
- The report was first written at 07:26 EDT, after E0 offline, not at PREFLIGHT as BUILD-HUB `## PREFLIGHT` says. The worker stop hook fired once at the turn end before that (`NOT A REFUSAL. Your report's last line is not a stop line…`).
- The card's `## RECORDS` were copied into `SHADOW-INSTRUCTIONS.md` whole. The seat re-read the line cites against the worktree (= BASE = main for the two code files and `cto-2026-10-17.md`); they hold.
- The card names RULINGS R1841 and R1863. Its rows cite R1844 (the refresh exemption, a desk row), and the r2 preflight lists R1841 and R1844. `authorize.sh` proved R1841 and R1863.
- `SHADOW-INSTRUCTIONS.md` is the one untracked file at the stop line (SHADOW-HUB step 4, X9).
- Builder: grok-4.7, 3 passes (T, S, S2 #1). Builder wall 13.3 min. Builder tokens UNKNOWN (L70). Seat wall 07:13 → 09:03, about 110 min.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: stop-guard-work-1018 · tip: 9b9177ea | on 7317d540 | migration: none | offline 8507/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none (committed range; the tool's line names only the untracked SHADOW-INSTRUCTIONS.md) | rows: 4 of 4 | self-check: 2 of 3 | decisions: 4 · for Dejan: 0 · tokens: 168001
