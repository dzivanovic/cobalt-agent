# checkin-install-1018 — build report (routed, BAND MID, builder grok-4.7, gate seat Opus 5.5) — 2026-10-18

## §0 Headline
The check-in timer is built: `ops/desk/checkin-timer.sh`, its plist (06:00, 12:00, 18:00, 24:00 ET), the one-turn `CHECKIN-PING.md`, and the R1854 A–D lines in CTO-DESK-WAKEUP.md, BRAIN-HUB.md and STANDING-LIST.md §10.
Grok 4.7 wrote every file in three passes (T, S, S2). One red after pass S was in its own P1 test, which staged the launcher twice in one tmp folder. Pass S2 fixed that in the test only.
Suites green: offline 8507/0, live-note 146/0, tests/ops 3935 passed. DB: none, so no lock was taken.
F1 fix round (14:00–14:30 EDT, Opus): the timer now closes a `checkin-ping` session older than 30 min (or of unknown age) before the launch, and defers only on a younger one (O1, A1 FIXED; tip `a55810c2`). Suites: offline 8515/0, live-note 146/0, tests/ops 3943 passed. RESTARTS: none. One ASK DESK: the agents keys were not read live.

## L74
None arrived in any tool result.
F1 round: a system reminder at the session's start asked commits to end with a `Claude-Session:` line. Recorded once, not followed: the commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
06:58 EDT. `sh /Users/cobalt/cobalt/ops/desk/authorize.sh shadow "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/751-checkin-install-card.md"`:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-18/751-checkin-install-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-18/751-checkin-install-card.md" · 0 · 76e67e765bc35a60707f40e5c5b0e66dc03cc5b0
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-18/751-checkin-install-card.md" · 0 · nothing
STANDING LIST 2026-10-11 R1069 row · grep -n "^| R1069 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 74:| R1069 | 10:37 ET | HIS RULING · APPROVED (via the brain, L79; words R1069): OpenAI available, tribunal seats approved, no stops, no design round; deploy 324, install SHADOW-HUB, Grok, Sonnet, Terra arms in parallel (only the lock serializes). | APPLIED: cobalt.md NOW 11:17 |
STANDING LIST 2026-10-11 R1069 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1069 |" -- "docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · 2322ed1e5044b6ec734e2cd0d225252408f87dbd
STANDING LIST 2026-10-11 R1069 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-11.md" · 0 · the row as grepped
RULING 2026-10-18 R1854 row · grep -n "^| R1854 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 19:| R1854 | 06:45 ET | HIS RULING (brain relays, L79): fixes A-D (MVP first, DAY PLAN, check-ins 06/12/18/24 ET, owned waits, no idle nights). Words: [R1854](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at wake-up 06:46 |
RULING 2026-10-18 R1854 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1854 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 49371f09c96483d11b12eb166983c185f0f1c6f6
RULING 2026-10-18 R1854 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
RULING 2026-10-18 R1841 row · grep -n "^| R1841 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 32:| R1841 | 06:25 ET | HIS RULING (brain relays, L79): the desk does not idle; until MVP it launches the next card, every turn ends with a live worker and watch, the night is a shift. Words: [R1841](cto-2026-10-18-words.md). | HIS RULING · APPROVED · APPLIED: cto-desk-contract.md at 06:46 |
RULING 2026-10-18 R1841 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1841 |" -- "docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · 7317d540b338bf299f1e555362b25230a75d1120
RULING 2026-10-18 R1841 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-18.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh shadow "<card>"`:
```
clock · date · 0 · Sun Oct 18 06:58:49 EDT 2026
status · git status --short --branch · 0 · ## ops/checkin-install-1018
head · git log --oneline -1 · 0 · 8033d70e docs(desk): R1856 install drafter 15719707, 12:00 check-in wait
diff · git diff --stat 8033d70e · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/checkin-install-1018 · 0 · 8033d70e docs(desk): R1856 install drafter 15719707, 12:00 check-in wait
env here · ls /Users/cobalt/cobalt-wt/checkin-install-1018/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 0 · siblings holding .env: /Users/cobalt/cobalt-wt/test-llm-reds-1018/.env
PREFLIGHT OK
```
- `git show --stat 8033d70e` → `docs/40 - DevDocs/reports/cto-2026-10-18.md | 7 ++++---`, 1 file changed.
- Card symbols, by `grep -n -E`: `tests/ops/test_close_timer.py:74:def box(tmp_path):`; `tests/ops/test_desk_launch_prechecks.py:73:class Desk:`, `:215:def desk(tmp_path):`, `:1183:def staged_launcher(tmp_path: Path) -> Path:`, `:1334:def read_prompt(`, `:1346:def dry_prompt(`; `tests/ops/test_hub_lines.py:60:def tools(line: str, option: str) -> list[str]:`. `CTO-DESK-WAKEUP.md:13` holds `"SendMessage"` on the desk's line, `:16` `MESSAGE: SendMessage`, `:48` `ON TRIGGER — open, then act`; `BRAIN-HUB.md:8` holds `"Bash(date*)"`, `:25` `## HOW YOU ANSWER A JUDGE REQUEST`, `:32` `## MEASURE`; `STANDING-LIST.md:238` `## 9. PRODWRITE-HUB.md …`; `restarts.py:38` `OPS_DESK_PREFIX = "ops/desk/"`, `:225-233` the DOCS and operator-script rules; `desk-launch.sh:583-584` the card and hub refusals, `:616-619` the `auto|plan` mode check. Read by the Read tool.
- `wc -l`: CTO-DESK-WAKEUP.md 55, BRAIN-HUB.md 43, STANDING-LIST.md 255, close-timer.sh 164, test_close_timer.py 423, desk-launch.sh 2407, restarts.py 281.
- `uv run cobalt jobs restarts 8033d70e..HEAD` → empty table, `RESTARTS: none`.
- No lock probe (DB: none).
- The card's `## RECORDS` were copied into SHADOW-INSTRUCTIONS.md whole. Re-read here: BASE `8033d70e` (preflight `head`); the rulings rows and their commits (AUTHORIZATION); the pattern files exist (`close-timer.sh` 164 lines).

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4572 passed, 806 skipped, 1 xfailed, 36 warnings in 787.46s (0:13:07)`.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 32.18s`. The one skip is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`, not `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Pass T (Grok). `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_checkin_install_1018.py` → `13 failed, 15 warnings in 1.93s`. First line of each red:
- T1, all six: `AssertionError: sh: …/ops/desk/checkin-timer.sh: No such file or directory` (`assert 127 == 0` / `127 == 1` / `127 == 4`).
- T2 plist: `FileNotFoundError` on `ops/desk/com.cobalt.checkin-timer.plist`. T2 restarts: `assert PLIST.exists() and …` fails.
- P1, both: `FileNotFoundError: … docs/40 - DevDocs/prompts/CHECKIN-PING.md`.
- W1: `AssertionError: - A tool or harness gap → ` / `assert 0 == 1`.
- B1: `assert 0 == 1` (no `## CHECK-IN` heading).
- S1: `assert 0 == 1` (no `## 10. THE CHECK-IN TIMER` heading).
Every red is the row's named reason (absent file or count 0). Committed `03f40555 wip(checkin-install-1018): red`.

## E3 THE ROWS
- Pass S (Grok) wrote the six row files. Row tests: `1 failed, 12 passed`. The red: `test_p1_the_real_launcher_accepts_the_ping_line_dry`, on its second `dry_prompt` (the negative control): `FileExistsError: [Errno 17] File exists: '…/test_p1_the_real_launcher_acce0/ops'` (`staged_launcher` makes `<tmp>/ops` and cannot run twice on one root). The first dry launch (the accepted line) passed every assert. Committed `0e910a70 feat(checkin-install-1018): rows`.
- Pass S2 #1 (Grok): the negative control stages in its own `tmp_path / "neg"`. Row tests: `13 passed, 15 warnings in 2.84s`. Committed `d5acbada fix(checkin-install-1018): pass S2 1`.
- Controls, whole: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_desk_refresh_wakeup.py tests/ops/test_desk_wakeup_rule.py tests/ops/test_hub_lines.py tests/ops/test_desk_launch_brain.py` → `105 passed, 15 warnings in 48.63s`.
- MUTATIONS (gate seat, by Edit, undone by Edit, never committed):
  - T1: step (3)'s `if [ -z "$desk" ] … exit 1 fi` removed → `-k t1`: `1 failed, 5 passed`. `FAILED …::test_t1_no_cto_desk_row_sends_one_notify_and_launches_nothing`, `assert 0 == 1` (returncode 0, a log written). Undone.
  - T2: the Hour 0 dict removed → `-k t2`: `1 failed, 1 passed`. `Right contains one more item: {'Hour': 0, 'Minute': 0}`. Undone.
  - P1: `--permission-mode auto` → `dontAsk` in CHECKIN-PING.md → `-k p1`: `1 failed, 1 passed`. `REFUSED: permission mode 'dontAsk': a one-off prompt runs auto or plan; …`. Undone.
  - W1, B1, S1: each red on BASE (E2) is the absent text itself. The rows add only text, so removing the row's text puts the tree back at BASE for that test.
  - `git diff --stat` after the undo → nothing (the tree is at `d5acbada`).
- R1 (RUN): `wc -c` before → CTO-DESK-WAKEUP.md 14109, BRAIN-HUB.md 7665, STANDING-LIST.md 46754. After → 14844 (+735), 7849 (+184), 47651 (+897). `tests/ops` and RESTARTS below.
- No `src/` module changed, so no page under `docs/40 - DevDocs/cobalt/` was written.

## RESTARTS
`uv run cobalt jobs restarts 8033d70e..HEAD` (exit 1):
```
FAILED: RestartError: one or more changed paths were unclassified
path	change	rule	restart
SHADOW-INSTRUCTIONS.md	A	UNCLASSIFIED	com.cobalt.agent,com.cobalt.aset,com.cobalt.herdr,com.cobalt.mainframe,com.cobalt.obsidian,com.cobalt.radar
ESCALATE: unclassified path SHADOW-INSTRUCTIONS.md
docs/40 - DevDocs/prompts/BRAIN-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECKIN-PING.md	A	DOCS	-
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/checkin-install-build-2026-10-18.md	A	DOCS	-
ops/desk/checkin-timer.sh	A	operator script; no Cobalt reader	-
ops/desk/com.cobalt.checkin-timer.plist	A	operator script; no Cobalt reader	-
tests/ops/test_checkin_install_1018.py	A	test/documentation; no resident	-
RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar
```
The tool reads untracked files. `SHADOW-INSTRUCTIONS.md` is the gate seat's untracked file, never committed (SHADOW-HUB step 4, X9). Every committed path classifies with no restart. Not classified here: `configs/` is outside the rows, and the same default was taken on 10-11 (`strike-fallback-env-1010-terra-check-2026-10-11.md:182`, D4). DECISION 1.

## W THE THREE SUITES
- (a0) `git diff --name-only --no-renames 8033d70e` → `docs/40 - DevDocs/prompts/BRAIN-HUB.md`, `docs/40 - DevDocs/prompts/CHECKIN-PING.md`, `docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md`, `docs/40 - DevDocs/prompts/STANDING-LIST.md`, `ops/desk/checkin-timer.sh`, `ops/desk/com.cobalt.checkin-timer.plist`, `tests/ops/test_checkin_install_1018.py`. Every path starts with `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 7 paths)`**.
- (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh checkin-install-1018 offline` (07:29 EDT):
```
tests/ops: run (docs/40 - DevDocs/prompts/BRAIN-HUB.md)
offline 8507/0
log: /Users/cobalt/cobalt-wt/.gate-logs/checkin-install-1018-offline-20261018-072917.log
```
  `grep -c -F "OUTSIDE the allowed set" <log>` → `0`. Its SKIPPED lines are the with-DB tests: `Postgres env settings not available` (no `.env`, DB: none).
- (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh checkin-install-1018 livenote` → `live-note 146/0`, `log: /Users/cobalt/cobalt-wt/.gate-logs/checkin-install-1018-livenote-20261018-075916.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `3935 passed, 1 xfailed, 16 warnings in 966.36s (0:16:06)`.
- With-DB, (b)–(d), (f): not run (DB: none). `ls /Users/cobalt/cobalt-wt/checkin-install-1018/.env` → `No such file or directory` (08:16 EDT).

## PASSES
| pass | env check | command as run | wall | tokens | diff stat | commit |
|---|---|---|---|---|---|---|
| T | `ls: /Users/cobalt/cobalt-wt/checkin-install-1018/.env: No such file or directory` | `grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/checkin-install-1018/**)" -p "You are GROK (xAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass T: tests only under tests/. Write only the rows' files. Run no command. Reply with the list of files you wrote."` | 07:14:44 → 07:21:37 (7 min) | UNKNOWN | `tests/ops/test_checkin_install_1018.py \| 327 +++` | `03f40555` |
| S | same, `No such file or directory` | same, `Pass S: the rows.` | 07:22:11 → 07:25:35 (3 min) | UNKNOWN | 6 files, 206 insertions (BRAIN-HUB 3, CHECKIN-PING 6, CTO-DESK-WAKEUP 4, STANDING-LIST 14, checkin-timer.sh 141, plist 38) | `0e910a70` |
| S2 #1 | same, `No such file or directory` | same, `Pass S2: fix the failing lines quoted under PASS S2.` | 07:26:07 → 07:27:18 (1 min) | UNKNOWN | `tests/ops/test_checkin_install_1018.py \| 7 +++++--` | `d5acbada` |

Grok's replies listed exactly the files `git status` showed: pass T the test file; pass S the six row files ("The test file was not changed"); pass S2 the test file. No path outside the fence: no SCOPE.
Suites at first run: red. The row tests after pass S were `1 failed, 12 passed`, the model's own test harness. Pass S2 was sent on that red before the full gate, since the gate's tests/ops run would show the same red.

## PRE-STOP SELF-CHECK
(1) Every added test was shown red for its named reason. All 13 are red on BASE (E2). T1, T2 and P1 are also red under their mutation (E3, quoted). The T1 no-desk negative control (the `x-build` row whose cwd holds `cto-desk`) is the input of that test, and it is green at the tip. The P1 negative control (`acceptEdits` refused) is green at the tip and passes inside the test.
(2) Entry paths. The timer is entered only by the plist's ProgramArguments (pinned by `test_t2_the_plist_…`). The ping prompt is entered only by the timer's step 5 (pinned by `test_t1_a_live_desk_gets_one_ping_launch_and_a_log`, the stub call `prompt <repo>/docs/40 - DevDocs/prompts/CHECKIN-PING.md`), and through the real launcher's kind `prompt` (pinned by `test_p1_the_real_launcher_accepts_the_ping_line_dry`). Each of the five fire steps has its test: (1) missing launcher, (2) list missing and unreadable, (3) no desk, (4) live ping, (5) launch and failed launch.
(3) Re-read at the tip: `git rev-parse --short=8 HEAD` → `d5acbada`; `git log --oneline 8033d70e..HEAD` (three commits); `wc -c` of the three fixed files; the RESTARTS table; `git diff --name-only --no-renames 8033d70e`; the file contents by the Read tool after each pass.

## FOR THE CHECK
- `8033d70e..d5acbada`: `03f40555 wip(checkin-install-1018): red` · `0e910a70 feat(checkin-install-1018): rows` · `d5acbada fix(checkin-install-1018): pass S2 1`.
- Per row: reds (E2), mutations (E3), greens (`13 passed`), controls (`105 passed`), all quoted above.
- R1 output: `tests/ops` `3935 passed, 1 xfailed`; `wc -c` growth +735 / +184 / +897; the RESTARTS table, whole, above.
- Suites: offline 8507/0 (`gate.sh … offline`), live-note 146/0 (`gate.sh … livenote`), with-DB: not run (DB: none). F0 / F1 / F2: not run (DB: none). Lock taken / released: not run (DB: none).
- X3, seen while reading: the DEFERRED test feeds a constructed `checkin-ping` row. Whether a finished `claude --bg` ping leaves a live row in `desk-list.sh` is not tested here and is the check's question.
- The diff of the three fixed files is additions only: `git diff` shows 3 + 4 + 14 inserted lines and no removed line.

## F1 FIX ROUND (CONTINUE: F1, Opus 5.5, 14:00 EDT)
The check's held items O1 and A1 (D1), settled by brain L79 (a): `checkin-timer.sh` step (4) judges every `checkin-ping` row by age, never by state.
- RECOVERY: `git status --short --branch` → `## ops/checkin-install-1018`; `git log --oneline -3` → `3108359f` · `d614e296` · `b72748d4`; `ls -la <WT>/.env` → `No such file or directory`.
- AUTHORIZATION: `sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` → `AUTHORIZED` (exit 0). Rows: INSTALLED nothing; PLACEHOLDER nothing; CARD COMMITTED `95207ab89ab25bb4ac01da496e58351eb63886db`; CARD UNCHANGED nothing; STANDING LIST 2026-09-30 R60 at `cto-2026-09-30.md:46`, committed `962e9d17…`; R1854 at `cto-2026-10-18.md:70`, committed `49371f09…`; R1841 at `:83`, committed `7317d540…`; each at HEAD.
- Read before the edit: `checkin-timer.sh:111-127` (the defer loop with `break`), `:41-49` (the overridables); `desk-done.sh:3`, `:16-17`, `:38-40` (`--replaced`); `desk-launch.sh:2385-2395` (the `idle`/`working` read and the KEPT refusal); `ops/cto-desk.sh:187-189` (row fields `cwd, id, kind, name, sessionId, startedAt, state`), `:225-229` (epoch ms, CLI 2.1.276); `/Users/cobalt/.claude/ops/desk-list.sh:16` (`id · name · cwd · status · state`, no start time).
- THE AGENTS KEYS: not read live. `claude agents --json` is no listed string, and BUILD-HUB names `claude` as never typed. The recorded facts: `ops-2026-09-18.md:190` (real output, CLI 2.1.276: `cwd, id, kind, name, sessionId, startedAt, state`) and `cto-2026-10-18.md:30` R1896 (`startedAt proven present in claude agents --json`). ASK DESK under `## DECISIONS`.
- RED on the tip `3108359f`, test edits only: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_checkin_install_1018.py` → `4 failed, 15 passed, 2 xfailed, 15 warnings in 3.09s`. First lines:
  - `test_f1_a_stale_working_ping_is_closed_then_replaced`: `AssertionError: DEFERRED: ping live — eeee5555-0000-4000-8000-000000000005` (red at `DEFERRED` not in stdout, the row's reason).
  - `test_f1_a_young_ping_defers_even_when_a_stale_one_is_closed`: `AssertionError: assert [] == ['done eeee55...5 --replaced']`.
  - `test_f1_an_unknown_age_counts_stale`: `AssertionError: assert [] == ['done eeee55...CKIN-PING.md']`.
  - `test_f1_a_failed_close_refuses_and_launches_nothing`: `assert 0 == 1` (stdout `DEFERRED: ping live — eeee5555-…`).
  - CONTROLS green on the tip: `test_f1_a_five_minute_old_ping_still_defers`, `test_f1_no_ping_row_launches_directly`.
  Committed `2ca50897 wip(checkin-install-1018): F1 red — a stale ping defers`.
- THE FIX, `a55810c2 fix(checkin-install-1018): a check-in ping is judged by age; a stale one is closed before the launch (F1, O1 A1, L79 a)`:
  - `ops/desk/checkin-timer.sh`: `PING_MAX_AGE_MIN=30`; `COBALT_AGENTS_CMD` (default `claude agents --json`) and `COBALT_DESK_DONE` (default `<REPO>/ops/desk/desk-done.sh`) beside the three roots; step (4) collects every `checkin-ping` id (no `break`), reads the listing once, closes each row older than 30 min or of unknown age with `sh <DESK_DONE> <id> --replaced` (`CLOSED STALE PING: <last line>`), refuses on a non-zero exit or a `KEPT` last line (`REFUSED: close of stale ping <id> failed — <last line>`, one notify, exit 1, no launch), then defers on the first young row (`DEFERRED: ping live — <id>`, `finish 0`). Header step 4 rewritten to the rule. Steps 1–3 and 5 unchanged.
  - `tests/ops/test_checkin_install_1018.py`: the `box` fixture gains the agents stub (`AGENTS_JSON`, `AGENTS_FAIL`) and the desk-done stub (appends `done <args>` to `CALLS`, prints `${DONE_LINE:-CLOSED $1}`, exits `${DONE_EXIT:-0}`). O1 `test_x3_a_finished_ping_row_does_not_defer_the_next_fire`: the 6-hour `startedAt`, xfail mark removed; its call assert reads `[done <id> --replaced, prompt <PING>]`, since the card puts both stubs on one ordered log. A1 `test_x3_a_finished_ping_is_not_left_as_a_named_session`: same name, body restated on `box` (a 6-hour-old row; calls `[done <id> --replaced, prompt <PING>]`, once each, in that order), xfail mark removed. `test_t1_a_live_ping_defers`: `startedAt` five minutes back. The `staged_launcher` import, used only by A1's old body, is dropped.
- GREEN: `uv run pytest -q -p no:cacheprovider --color=no tests/ops/test_checkin_install_1018.py` → `21 passed, 15 warnings in 3.54s`.
- MUTATION (by Edit, undone by Edit, never committed): the 30-minute test removed (`if False:` before `print(pid, "young")`) → `-k "f1 or x3 or t1"`: `3 failed, 11 passed, 7 deselected`. `FAILED …::test_f1_a_five_minute_old_ping_still_defers`: `AssertionError: assert 'DEFERRED: ping live — ffff6666-0000-4000-8000-000000000006' in 'CLOSED STALE PING: CLOSED ffff6666-… LAUNCHED: checkin — exit 0 — …'`; also `test_t1_a_live_ping_defers` and `test_f1_a_young_ping_defers_even_when_a_stale_one_is_closed`. Undone; `git diff --stat` → `ops/desk/checkin-timer.sh | 72`, `tests/ops/test_checkin_install_1018.py | 43`, the report `| 4` (the uncommitted fix itself, before its commit; the mutation left nothing), and the file again `21 passed`.
- RESTARTS: `uv run cobalt jobs restarts 8033d70e..HEAD` (exit 0), whole:
```
path	change	rule	restart
docs/40 - DevDocs/prompts/BRAIN-HUB.md	M	DOCS	-
docs/40 - DevDocs/prompts/CHECKIN-PING.md	A	DOCS	-
docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md	M	DOCS	-
docs/40 - DevDocs/prompts/STANDING-LIST.md	M	DOCS	-
docs/40 - DevDocs/reports/checkin-install-build-2026-10-18.md	M	DOCS	-
docs/40 - DevDocs/reports/checkin-install-build-2026-10-18.result	A	DOCS	-
ops/desk/checkin-timer.sh	A	operator script; no Cobalt reader	-
ops/desk/com.cobalt.checkin-timer.plist	A	operator script; no Cobalt reader	-
tests/ops/test_checkin_install_1018.py	A	test/documentation; no resident	-
RESTARTS: none
```
  `SHADOW-INSTRUCTIONS.md` is gone from the worktree, so the build's DECISION 1 and the check's D2 no longer apply.
- W (a0): `git diff --name-only --no-renames 8033d70e` → the 7 row paths + `docs/40 - DevDocs/reports/checkin-install-build-2026-10-18.md` + `.result`; every path under `ops/`, `tests/ops/` or `docs/`. **`cobalt_dev: not taken (DB: none — 9 paths)`**.
- W (a) `sh /Users/cobalt/cobalt/ops/desk/gate.sh checkin-install-1018 offline` (14:03 EDT, exit 0), whole: `tests/ops: run (docs/40 - DevDocs/prompts/BRAIN-HUB.md)` · `offline 8515/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/checkin-install-1018-offline-20261018-140320.log`. `grep -c -F "OUTSIDE the allowed set" <log>` → `0`. 8515 = 8507 + the 8 new F1-round tests (6 `test_f1_*`, the 2 `test_x3_*` now counted as passes).
- W (e) `sh /Users/cobalt/cobalt/ops/desk/gate.sh checkin-install-1018 livenote` (exit 0), whole: `live-note 146/0` · `log: /Users/cobalt/cobalt-wt/.gate-logs/checkin-install-1018-livenote-20261018-142939.log`.
- `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (exit 0) → `3943 passed, 1 xfailed, 16 warnings in 865.96s (0:14:25)`. The 1 xfail predates this card; `grep -c -F "xfail" tests/ops/test_checkin_install_1018.py` → `0`.
- With-DB (b)–(d), (f): not run (DB: none). `ls <WT>/.env` → `No such file or directory` (14:30 EDT).
- SELF-CHECK, F1: (1) every F1 test red on the tip or green as a named control (above), and the five-minute control red under the mutation. (2) The one caller of `checkin-timer.sh` is `ops/desk/com.cobalt.checkin-timer.plist:20` (the Grep tool over the worktree outside `docs/`), pinned by `test_t2_the_plist_…`. Step (4)'s inputs are each pinned: no ping row, a young row, a stale `working` row, an `idle · done` row, two rows (one stale, one young), no `startedAt`, a non-numeric `startedAt`, an unreadable listing, a close exit 1, and a `KEPT` last line on exit 0. (3) Re-read at the tip `a55810c2`: `grep -n -F "PING_MAX_AGE_MIN" ops/desk/checkin-timer.sh` → `:28`, `:54`, `:125`, `:159`; `grep -n -F "def test_x3_"` → `:240`, `:252`; `git log --oneline 8033d70e..HEAD` (8 commits).

FIXED: O1 — tests/ops/test_checkin_install_1018.py::test_x3_a_finished_ping_row_does_not_defer_the_next_fire
FIXED: A1 — tests/ops/test_checkin_install_1018.py::test_x3_a_finished_ping_is_not_left_as_a_named_session

## CONTINUE
next: none (F1 stop line written). Next, the desk's: the scoped check (`desk-launch.sh check` on this card), then the deploy (card F1 ORDER OF THE ROW).

## DECISIONS
- DECISION 1 (RESTARTS): `uv run cobalt jobs restarts 8033d70e..HEAD` reads the untracked `SHADOW-INSTRUCTIONS.md` as UNCLASSIFIED / ESCALATE and widens the line to six residents. Every committed path derives no restart. Safe default: not classified (`configs/` is outside the rows; the file is the gate seat's and is never committed; the 10-11 precedent). The stop line carries the table's last line untrimmed. For the deploy: the committed range is `RESTARTS: none` once the file is gone. F1 round: settled. The file is gone, and the table reads `RESTARTS: none`.
- ASK DESK (F1, the agents keys) [14:30 EDT]: the card asks for the KEYS of one live `claude agents --json` row before the edit. This seat cannot run `claude`: it is on no listed string, and BUILD-HUB names it never typed. Safe default taken: the edit was made on the recorded facts, `ops-2026-09-18.md:190` (real output, `… startedAt …`) and the desk's R1896 (`cto-2026-10-18.md:30`, "startedAt proven present"). If the key is gone, every ping row has an unknown age and is closed, never deferred, so the timer cannot stall. To prove it, the desk reads the keys of one live row once.

## RECORDS
- F1: `CONTINUED at F1 14:00 EDT`. A new session at `CONTINUE: F1` (the card's fix round). The report's `BUILT` line from the build round is kept above as a record line.
- F1: no lock taken (DB: none). No `REFUSED, not needed` line: `claude agents --json` was not typed (ASK DESK above).
- Routed card (BAND MID, no `SHADOW OF`): the stop line is BUILD-HUB's `BUILT ·`, SHADOW-HUB `:28`, `:57`, `:74`.
- The one untracked file at the stop line is `SHADOW-INSTRUCTIONS.md`, the launcher's one exception (BUILD-HUB CLOSE).
- Mutations were made and undone by the gate seat with the Edit tool on the rows' files (BUILD-HUB E3). The builder's files were never repaired: the P1 red went back to Grok as pass S2.
- No extra lock take, no `REFUSED, not needed`, no `CONTINUED`, no L74 line.
- The card's records as re-read at PREFLIGHT: BASE, rulings and pattern files, as above.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

Build-round stop line (d5acbada), kept as a record: `job: checkin-install-1018 · tip: d5acbada | on 8033d70e | migration: none | offline 8507/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: com.cobalt.agent com.cobalt.aset com.cobalt.herdr com.cobalt.mainframe com.cobalt.obsidian com.cobalt.radar | rows: 7 of 7 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 180293`

BUILT · job: checkin-install-1018 · tip: a55810c2 | on 8033d70e | migration: none | offline 8515/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 8 of 8 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 148233
