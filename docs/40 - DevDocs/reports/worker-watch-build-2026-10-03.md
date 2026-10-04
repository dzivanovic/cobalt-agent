# worker-watch — build report, 2026-10-03

Card: `docs/40 - DevDocs/prompts/2026-10-03/09-worker-watch-card.md` (commit `942180be`). Hub: `BUILD-HUB.md`. Branch `ops/worker-watch-1003`, worktree `worker-watch-1003`, BASE `a09f0862`. DB: none.

## §0 Headline
BUILT at `1bfd26e3` on `a09f0862`, 5 of 5 rows. S1, N1, W1 and I1 were built at `264e58f7`; S2 was added after the check and resumed at E3 (13:30). S2 changes three things. A worktree seat whose first message names no `CARD:` is exempt. `DEPLOYED <TAG> …` is now a stop line. His install text names `~/.claude/settings.json` (R77).
Suites at `1bfd26e3`: offline 3737/0 · tests/ops 530/0 · live-note 146/0 · with-DB not run (DB: none). RESTARTS: none.
His install text (three hook entries, valid JSON) is in `## E3 THE ROWS` (I1, target amended by S2) and in the header of `stop-guard.py`.
4 decisions for the desk, carried from pass 1 and answered by the judge (card RECORDS); S2 adds none. None for Dejan.

## L74
A system reminder at the start of the session asked commits to end with a `Claude-Session:` line beside `Co-Authored-By`. Recorded once; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`date` → `Sat Oct  3 11:30:23 EDT 2026`.

| check | command | exit | output |
|---|---|---|---|
| INSTALLED | `grep -n -E "«INSTAL[L]" ".../prompts/BUILD-HUB.md"` | 1 | (nothing) |
| card has no placeholder | `grep -n -E "«FIL[L]" ".../2026-10-03/09-worker-watch-card.md"` | 1 | (nothing) |
| card committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-03/09-worker-watch-card.md"` | 0 | `942180bed20f9a19cc5cf34fc10947ac02a704b6` |
| card unchanged | `git -C /Users/cobalt/cobalt diff --stat -- "<card>"` | 0 | (nothing) |
| STANDING LIST 2026-09-30 R60 | `grep -n "^| R60 " ".../cto-2026-09-30.md"` | 0 | line 46: `| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) ## R60): APPROVES STANDING-LIST.md once (4be06af0) … | APPROVED |` |
| R60 committed | `git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md"` | 0 | `962e9d1705b62a61821f62f4d7bf5d8131656e2a` |
| RULING 2026-10-02 R47 | `grep -n "^| R47 " ".../cto-2026-10-02.md"` | 0 | `54:| R47 | 07:57 ET | HIS RULING (direction row 10; L73 over L67 house A): script program by Anthropic seats only, no outside house, … | HIS RULING · APPROVED |` |
| R47 committed | `git -C … log -1 --format=%H -S"| R47 |" -- ".../cto-2026-10-02.md"` | 0 | `4e3fa8d8aaf48b3ed59ff8ec87e2d3dfe00af52a` |
| RULING 2026-10-02 R157 | `grep -n "^| R157 " ".../cto-2026-10-02.md"` | 0 | `164:| R157 | 17:40 ET | HIS RULING (B): the brain's full process list for 10-03 runs this week, … | HIS RULING · APPROVED |` |
| R157 committed | `git -C … log -1 --format=%H -S"| R157 |" -- ".../cto-2026-10-02.md"` | 0 | `edd6f7aa2da34451b0e0b9034d9692c0bc3064f2` |
| RULING 2026-10-03 R24 | `grep -n "^| R24 " ".../cto-2026-10-03.md"` | 0 | line 30: `| R24 | 10:10 ET | HIS RULING (A, via brain): worker-watch hooks ASAP — card 09-worker-watch-card.md (Stop hook, idle hook, watch idle exit), DB: none, Opus check (R12), launched after set 1 DEPLOYED, ships in set 2 … | HIS RULING · APPROVED |` |
| R24 committed | `git -C … log -1 --format=%H -S"| R24 |" -- ".../cto-2026-10-03.md"` | 0 | `18666364a59bc1ab62f89627e9531be95f4e7318` |

All pass.

## PREFLIGHT
| rule | command | exit | output |
|---|---|---|---|
| clock | `date` | 0 | `Sat Oct  3 11:30:23 EDT 2026` |
| branch | `git status --short --branch` | 0 | `## ops/worker-watch-1003` |
| HEAD = BASE | `git log --oneline -1` | 0 | `a09f0862 docs(desk): 10-03 R30-R34 set 1 deployed; refusals list; his rulings` |
| branch on the main repo | `git -C /Users/cobalt/cobalt log --oneline -1 ops/worker-watch-1003` | 0 | `a09f0862 docs(desk): 10-03 R30-R34 set 1 deployed; refusals list; his rulings` |
| no diff on BASE | `git diff --stat a09f0862` | 0 | (nothing) |
| BASE | `git show --stat a09f0862` | 0 | `docs/40 - DevDocs/reports/cto-2026-10-03-words.md | 6 ++++++` · `docs/40 - DevDocs/reports/cto-2026-10-03.md | 19 +++++++++++++++++--` · `2 files changed, 23 insertions(+), 2 deletions(-)` |
| no .env here | `ls /Users/cobalt/cobalt-wt/worker-watch-1003/.env` | 1 | `ls: /Users/cobalt/cobalt-wt/worker-watch-1003/.env: No such file or directory` |
| .env anywhere | `ls -la /Users/cobalt/cobalt-wt/*/.env` | 1 | `(eval):1: no matches found: /Users/cobalt/cobalt-wt/*/.env` |
| RESTARTS empty range | `uv run cobalt jobs restarts a09f0862..HEAD` | 0 | `path	change	rule	restart` / `RESTARTS: none` |
| wc -l | `wc -l ops/desk/wait-stop-line.sh ops/desk/desk-watch.sh tests/ops/test_desk_watch.py ops/desk/bare-guard.py` | 0 | `26` · `52` · `165` · `117` (`360 total`) |
| READ report | `tail -n 3 ".../reports/harness-mods-review-2026-10-03.md"` | 0 | last line: `- R71 (no new vendors) is not touched: this is the vendor we already run on.` |
| READ section | `grep -n -F "OPERATIONS A HOOK CAN TAKE" ".../harness-mods-review-2026-10-03.md"` | 0 | `51:## OPERATIONS A HOOK CAN TAKE (his ask, 07:2x ET; his four items are 1, 2, 3 and 20–23)` |
| callers of wait-stop-line.sh | `grep -rn -F "wait-stop-line.sh" ops` | 0 | `ops/desk/wait-stop-line.sh:2` (its usage) · `ops/desk/desk-watch.sh:8` (comment) · `ops/desk/desk-launch.sh:880` (the devfix reminder text `watch: wait-stop-line.sh <its REPORT> '^(REBUILT|FAILED)'`) · `ops/desk/desk-context.sh:10` (comment) |
| callers of desk-watch.sh | `grep -rn -F "desk-watch.sh" ops` | 0 | `ops/desk/desk-watch.sh:2,16` (usage) · `ops/desk/desk-launch.sh:69,177,202` (the `WATCH:` line it prints) · `ops/desk/desk-done.sh:4` (comment) |
| bare-guard exit shape | `grep -n -F "sys.exit" ops/desk/bare-guard.py` | 0 | `117:    sys.exit(main())` |

THE CARD'S SYMBOLS, read whole with the Read tool: `ops/desk/bare-guard.py` (stdin JSON → `json.loads(sys.stdin.read())`, exit 2 with one stderr line, any error → exit 0), `ops/desk/desk-watch.sh`, `ops/desk/wait-stop-line.sh`, `ops/desk/desk-context.sh`, `ops/desk/wait-desk-idle.sh`, `tests/ops/test_desk_watch.py`, `tests/ops/test_desk_size_guard.py` (G3 stages `wait-stop-line.sh`), `BUILD-HUB.md` `## STOP LINE` and `## UNATTENDED RULES`.

`desk-list.sh`: NOT under `ops/desk/` at BASE (`Glob **/desk-list*` in `/Users/cobalt/cobalt` → no files). The live file is `/Users/cobalt/.claude/ops/desk-list.sh` (read whole, 9 lines; rows `id · name · cwd · status · state`), named at `ops/desk/desk-context.sh:18` (`DESK_LIST=/Users/cobalt/.claude/ops/desk-list.sh`). Card `03` (set 2) tracks it at `ops/desk/desk-list.sh`. The watch scripts are run as `sh /Users/cobalt/.claude/ops/<script>` (install-ops links, `desk-launch.sh:58-64`), so "beside the script" is `/Users/cobalt/.claude/ops/desk-list.sh` today. See `## DECISIONS`.

LIST row shapes (from `reports/fixed-files-scratch-test-2026-09-30.md` OBSERVATIONS 1, line 69): a finished worker `idle · done`; a worker idle on a `FAILED:` line `idle · blocked`; a dialog `waiting · blocked`. `wait-desk-idle.sh:5-7`: "watch shells keep LIST `state: working` after the turn ends" (R117).

Hook facts (read-only, local): `stop_hook_active` and `cwd` read from the Stop input at `~/.claude/plugins/marketplaces/claude-plugins-official/plugins/security-guidance/hooks/security_reminder_hook.py:1911-1912`; exit 2 = blocking, stderr fed back to Claude (`…/plugin-dev/skills/hook-development/SKILL.md:294-298`); common input fields `session_id`, `transcript_path`, `cwd`, `hook_event_name` (same file, 302-311); Notification matcher values `permission_prompt`, `idle_prompt` ("Claude waiting for input (60+ seconds)"), `auth_success`, `elicitation_dialog` (`…/claude-automation-recommender/references/hooks-patterns.md:191-196`). The input FIELD that carries the type is not in any local file (see `## DECISIONS`).

Hub session names (`--name` on each fixed launch line): `<job>-build`, `<job>-check`, `<job>-devfix`, `deploy-hub-<job>`, `close-<mmdd>`. Every hub line's message carries `CARD: '<card>'` except CLOSE (`DATE: <date>`); deploy and close run in `/Users/cobalt/cobalt` (`desk-launch.sh:45-46,56`).

Card `## RECORDS`, copied: (1) `DB: none`: every file is under `ops/` or `tests/ops/`; no lock. (2) His words, brain session 10-03, about 10:1x ET: "As far as your hooks, yes, I want them installed as soon as possible because this is one of the biggest issues that we're having. …" (3) Mods and hooks are Anthropic process tuning: no outside house (desk row 2026-10-03 R12). (4) Base: `main` after set 1; ships in set 2 with `03`, `02`, `06`; his install follows set 2's DEPLOYED line. Re-read: (1) holds for the rows' files; (4) BASE `a09f0862` is `main`'s head per the PREFLIGHT rows above.

## E0 BASELINE
- Offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 658.56s (0:10:58)`; 0 failed, 0 errors.
- Live-note: `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.52s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. No skip names `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Test files written: `tests/ops/test_stop_guard.py` (new), `tests/ops/test_idle_wake.py` (new), `tests/ops/test_desk_watch.py` (gains W1; its helper now runs a staged copy of the watch with a `desk-list.sh` stub beside it, default answer `busy · working`, so the existing tests read nothing outside `tmp_path`). `tests/ops/test_wait_stop_line.py` does not exist (`ls -la tests/ops` at PREFLIGHT); wait-stop-line's W1 tests are in `test_desk_watch.py`.

`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py tests/ops/test_desk_watch.py` → `47 failed, 24 passed, 15 warnings in 248.87s (0:04:08)`.
- S1: every `test_stop_guard.py` test red with `E       FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/worker-watch-1003/ops/desk/stop-guard.py'`. The row's reason: no such file.
- N1: every `test_idle_wake.py` test red with `E       FileNotFoundError: [Errno 2] No such file or directory: '/Users/cobalt/cobalt-wt/worker-watch-1003/ops/desk/idle-wake.py'`. The row's reason: no such file.
- W1: the positive tests red with `E       AssertionError: STILL RUNNING after 20s — last line: (run in progress — next step under ## CONTINUE)` / `assert 2 == 3`: two idle polls, a WAKE line, GONE, the check / devfix / deploy / close session names. `test_w1_a_changed_last_line_restarts_the_idle_count`: `STILL RUNNING after 20s — last line: RESUMED: E2 11:00`. `test_w1_wait_stop_line_with_a_session_exits_3_on_idle`: `TIMEOUT after 200s — last line was: (run in progress — next step under ## CONTINUE)` / `assert 2 == 3`. The refusals (`…close_report_not_named_by_its_date…`, `…no_desk_list_beside_the_watch…`): `assert 2 == 1`. The row's reason: the watch waits past the stub's idle answers until its timeout.
- REWRITTEN: `test_w1_two_rows_of_the_session_are_idle_only_when_both_are` went red for the wrong reason (`FileNotFoundError: … list-calls`; BASE never calls the stub). Fixed with `unlink(missing_ok=True)`. Re-run alone → `1 failed`, with `E       AssertionError: assert 2 == 3` (`STILL RUNNING after 20s`). The same fix went into the wait-stop-line test.
- GREEN on BASE, by design (negative controls; each gets a mutation at E3): `test_w1_one_idle_poll_between_busy_ones_never_fires`, `test_w1_idle_with_state_working_is_a_background_run_not_idle`, `test_w1_old_wake_lines_and_other_worktrees_never_fire`, `test_w1_a_wake_line_while_the_listing_shows_the_session_working_does_not_fire`, `test_w1_busy_with_a_changed_stop_line_exits_0_as_today`, `test_w1_a_stop_line_written_as_the_session_goes_idle_wins`, `test_w1_one_missing_listing_between_busy_ones_is_not_gone`, `test_w1_an_unreadable_listing_is_never_gone`, `test_w1_wait_stop_line_without_a_session_reads_no_listing`, plus the 15 existing desk-watch tests through the staged copy.
- No RUN row's test: I1 is a RUN row with no test file. Its command runs at E3.

Commit: `a6e8d571 wip(worker-watch): red — S1, N1, W1 tests before the scripts`.

**S2 (resumed at E3 13:30; the card's row asks red first on the tip `264e58f7`).** In `tests/ops/test_stop_guard.py`, the parametrized `DEPLOYED · tag: x` (`:124`) became `DEPLOYED deploy-2026-10-03-1 at 1a2b3c4d · smoke GREEN`. The new test `test_s2_a_worktree_seat_whose_first_message_names_no_card_never_blocks` covers a worktree cwd with a prose last line: with `CARD:` it exits 2 with the sentence (a negative control, green at the tip); with a first message `fix the watch in ops/desk` and no `CARD:` it exits 0. `test_a_transcript_with_no_card_blocks` was rewritten as `test_a_transcript_with_no_first_message_blocks`: a transcript with no user message, or a missing one, still blocks. Its `hi` case contradicted S2 (a).
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops/test_stop_guard.py` → `2 failed, 28 passed, 15 warnings in 1.82s`:
- `test_every_stop_shape_lets_the_turn_end[DEPLOYED deploy-2026-10-03-1 at 1a2b3c4d · smoke GREEN]`: `E       AssertionError: assert (2, 'NOT A RE...then stop.\n') == (0, '')`. The row's reason: the `DEPLOYED ` case exits 2.
- `test_s2_a_worktree_seat_whose_first_message_names_no_card_never_blocks`: `E       AssertionError: assert (2, '', 'NOT ...then stop.\n') == (0, '', '')` at `:197` (the no-`CARD:` half; the `CARD:` half passed before it). The row's reason: the no-card case exits 2.
Commit: `0a725bed wip(worker-watch): red — S2 tests before the fix`.

## E3 THE ROWS
Built in card order: S1, N1, W1, I1. Only the rows' files changed. DevDocs: no page under `docs/40 - DevDocs/cobalt/` covers `ops/desk/` (Grep `desk-watch|wait-stop-line|bare-guard` there → only `jobs/restarts.md`, the RESTARTS classifier's page, which lists paths and already classifies all of `ops/desk/` by rule at line 48). Earlier ops builds wrote none (`devfix-route-build-2026-10-02.md:110`, `launcher-checks-build-2026-10-02.md:169`), and I invented none.

**S1 `ops/desk/stop-guard.py`.** It finds the report through the card, not the newest-by-mtime glob. Every hub launch message carries `CARD: '<card>'` (BUILD, CHECK, DEPLOY, DEVFIX launch lines). The card names the exact report, including a devfix `REPORT` outside the worktree and a check whose report does not exist yet. The glob could not tell a check with no report from the build's `BUILT` report, and it misses `devfix-<name>.md`. Stop shapes accepted: `BUILT ·`, `CHECK DONE ·`, `DEPLOYED ·`, `REBUILT ·`, `FAILED`, `FAILED PREFLIGHT`, `ASK DESK:`, and `(run in progress` (the pinned line is `(run in progress — next step under ## CONTINUE)`, so the card's `(run in progress)` is matched as a prefix without its closing parenthesis). Green: `tests/ops/test_stop_guard.py tests/ops/test_bare_guard.py` → `68 passed`.
- M-S1a, `return 2` → `return 0`: `12 failed, 17 passed`. First line: `E   AssertionError: assert (0, '', 'NOT ...then stop.\n') == (2, '', 'NOT ...then stop.\n')` (`test_a_prose_last_line_blocks_once_with_the_sentence`, `…no_report_file…`, the six look-alike lines, `…check_session…`, `…cwd_below…`, `…no_card…`, `…empty_report_value…`).
- M-S1b, loop guard removed (`if event.get("stop_hook_active") and False`): `1 failed, 28 passed`. `test_the_same_prose_with_stop_hook_active_ends_the_turn`: `E   AssertionError: assert (2, '', 'NOT ...then stop.\n') == (0, '', '')`.
- M-S1c, cwd exemption removed: `1 failed, 28 passed`. `test_the_desk_and_the_brain_cwd_is_exempt_and_reads_no_report`: `E   AssertionError: /Users/cobalt/cobalt` / `assert (2, '', 'NOT ...then stop.\n') == (0, '', '')`.
- M-S1d, a check reads `REPORT:`: `1 failed, 28 passed`. `test_a_check_session_reads_the_check_report_not_the_build_report`: `E   AssertionError: no check report yet: blocked`.

**N1 `ops/desk/idle-wake.py`.** It loads `stop-guard.py` beside it (`importlib`, `sys.dont_write_bytecode = True`) for `worktree()` and `report_last_line()`: one report finder (L3). Line: `<datetime.now(America/New_York).isoformat(timespec="seconds")> <worktree> IDLE <last line | no report>`. It runs no subprocess, so the card's `LC_ALL=C` for subprocesses has nothing to apply to. Green: `tests/ops/test_idle_wake.py tests/ops/test_stop_guard.py tests/ops/test_bare_guard.py` → `75 passed`.
- M-N1a, type filter removed: `1 failed, 6 passed`. `test_a_non_idle_notification_writes_nothing`: `E   AssertionError: assert not True` (WAKE exists).
- M-N1b, `"a"` → `"w"`: `1 failed, 6 passed`. `test_a_second_idle_appends_a_second_line`: `E   AssertionError: assert [('x-job-0102', 'prose two')] == [('x-job-0102... 'prose two')]`.
- M-N1c, cwd filter removed: `1 failed, 6 passed`. `test_a_cwd_outside_the_worktrees_writes_nothing`: `E   AssertionError: assert not True`.

**W1 `ops/desk/wait-stop-line.sh`, `ops/desk/desk-watch.sh`.** One idle probe, `wait-stop-line.sh --idle <session> <worktree|-> <wake-lines-at-start> <previous> <report>`, which `desk-watch.sh` calls every poll after the stop-line read (L3: one implementation for both watches). `wait-stop-line.sh` takes an optional 4th argument `[session]`; without it, it is today's watch. Session names come from the card: `<JOB>-build|-check|-devfix`, `deploy-hub-<JOB>`, `close-<mmdd>`. WAKE lines count only when they name the card's `WORKTREE` (build, check, devfix) or the report path's worktree (wait-stop-line), and only when appended after the watch began. Idle = every LIST row of that name has `status` `idle` and a `state` other than `working`, because a background run keeps `working` after the turn ends (`wait-desk-idle.sh:5-7`, R117; this answers X3). Gone = no row of that name for two consecutive polls. An unreadable listing counts as busy. A WAKE line fires at once unless the listing shows the session busy. Green: `tests/ops/test_desk_watch.py tests/ops/test_desk_size_guard.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_desk_done.py` → `148 passed, 1 xfailed`. That xfail is G3's strict mutation probe `test_g3_shipped_refusal_checks_stay_green_when_the_file_is_read_first`, and it still xfails: the guard line and the `initial=$(lastline "$f")` anchor are unchanged.
- M-W1a, the desk-watch probe call replaced by `out=busy; rc=0` (all W1 tests): `10 failed, 11 passed, 15 deselected`. `…idle_for_two_polls…`: `E   AssertionError: STILL RUNNING after 20s — last line: (run in progress — next step under ## CONTINUE)` / `assert 2 == 3`. The other nine: `…restarts_the_idle_count`, `…wake_line_for_the_worktree…`, `…exits_3_gone`, `…two_rows…`, the three `…each_kind…`, `…close_watches_close_mmdd`, `…no_desk_list…` (`assert 2 == 1`).
- From here, each negative-control mutation ran only the test(s) it targets (`-k`), because a full W1 run takes about 4 min (M-W1a: `236.60s`):
- M-W1b, the `$5 != "working"` rule removed: `2 failed`. `…idle_with_state_working…`: `E   AssertionError: IDLE: x-job-build — no WAKE line` / `assert 3 == 2`; also `…wake_line_while_the_listing_shows_the_session_working…`.
- M-W1c, one poll fires (`[ "$state" != "idle" ]`, `[ "$state" != "gone" ]`): `4 failed`. `…one_idle_poll_between_busy_ones…`: `assert 3 == 2`. `…restarts_the_idle_count`: `assert 1 == 3`. `…exits_3_gone`: `assert 1 == 2`. `…one_missing_listing…`: `GONE: x-job-build` / `assert 3 == 2`.
- M-W1d, WAKE skip removed (`tail -n +1`): GREEN on the first try. The test used the default `busy` stub, so the busy gate hid the skip. REWRITTEN with alternating `idle done` / `busy working` answers; re-run under the mutation → `1 failed`: `E   AssertionError: IDLE: x-job-build — 2026-01-02T10:00:00-05:00 x-job IDLE (run in progress — next step under ## CONTINUE)` / `assert 3 == 2`.
- M-W1e, worktree match removed (`'$3 == "IDLE"'`): `1 failed`: `E   AssertionError: IDLE: x-job-build — 2026-01-02T10:01:00-05:00 y-job IDLE x-job` / `assert 3 == 2`.
- M-W1f, unreadable listing read as empty (`|| true`): `1 failed`. `…unreadable_listing_is_never_gone`: `E   AssertionError: GONE: x-job-build` / `assert 3 == 2`.
- M-W1g, the idle-count reset on a changed last line removed: `1 failed`. `…restarts_the_idle_count`: `E   AssertionError: assert 2 == 3` (list calls).
- M-W1h, the wait-stop-line probe call replaced by `out=busy; rc=0`: `1 failed, 1 passed`. `…wait_stop_line_with_a_session…`: `E   AssertionError: TIMEOUT after 200s — last line was: (run in progress — next step under ## CONTINUE)` / `assert 2 == 3`. The negative control `…without_a_session…` passed.
- M-W1i, the WAKE busy gate removed: `1 failed`. `…wake_line_while_the_listing_shows_the_session_working…`: `E   AssertionError: IDLE: x-job-build — 2026-01-02T10:00:00-05:00 x-job IDLE …` / `assert 3 == 2`.
- M-W1j, a probe without a session (`session="${4:-x-job-build}"`): `1 failed`. `…without_a_session_reads_no_listing`: `E   AssertionError: assert 3 == 2`.
- M-W1k, the probe before the stop-line read in desk-watch: GREEN on the first try. A new last line already resets the idle count, so order only matters when a WAKE line lands with the stop line. REWRITTEN `…stop_line_written_as_the_session_goes_idle_wins` to append a WAKE line with the `FAILED` line; re-run under the mutation → `1 failed`: `E   AssertionError: assert (3, 'IDLE: x-...AILED: W — x') == (0, 'FAILED: W — x')`.
- M-W1l, the close-name refusal replaced by `session="$b"`: `1 failed`. `…close_report_not_named_by_its_date…`: `assert 3 == 1` (`GONE: close-notes`).
- Every mutation was undone with the Edit tool. `git diff --stat` afterwards: `ops/desk/desk-watch.sh | 36`, `ops/desk/wait-stop-line.sh | 72`, `tests/ops/test_desk_watch.py | 4` (the two rewrites), `tests/ops/test_stop_guard.py | 12` (I1's test); no mutation text left.

**I1 (RUN, asserts nothing).** `python3 -c "import json,sys; json.load(open(sys.argv[1]))" <tmp file>` is on no allow string of this launch line. The same proof ran as `tests/ops/test_stop_guard.py::test_i1_run_his_install_text`: it cuts the object out of the header between `# INSTALL BEGIN` / `# INSTALL END`, writes it to a `tmp_path` file, `json.load`s it and prints it. `uv run pytest -q -rP -p no:cacheprovider --color=no tests/ops/test_stop_guard.py -k i1_run` → `1 passed`; captured stdout, whole:
```
{
  "PreToolUse": [
    {"matcher": "Bash", "hooks": [{"type": "command", "command": "python3 /Users/cobalt/cobalt/ops/desk/bare-guard.py"}]}
  ],
  "Stop": [
    {"hooks": [{"type": "command", "command": "python3 /Users/cobalt/cobalt/ops/desk/stop-guard.py"}]}
  ],
  "Notification": [
    {"matcher": "idle_prompt", "hooks": [{"type": "command", "command": "python3 /Users/cobalt/cobalt/ops/desk/idle-wake.py"}]}
  ]
}
```
This is the value of `"hooks"` in user settings `~/.claude/settings.json` (S2 (c), his R77; pass 1 named `/Users/cobalt/cobalt/.claude/settings.json`). The `Notification` entry carries matcher `idle_prompt` (the matcher value from local docs); the script also checks the type itself.

After the rows: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `529 passed, 1 xfailed, 15 warnings in 256.23s (0:04:16)`.

Commit: `264e58f7 feat(worker-watch): Stop hook, idle hook, watch idle exit (S1, N1, W1, I1; L1, L3, L28, L71)`.

**S2 `ops/desk/stop-guard.py` (resumed at E3).** Re-read the file whole before the edit. Three changes:
- (a) `main()` (`stop-guard.py:124-129` at the tip) reads the first user message. When it exists and `CARD.search` finds nothing, the hook exits 0, because this is a `prompt` seat. An unreadable or missing transcript, or one with no user message, still falls through to the report read and blocks (L1: it is not provably a prompt seat).
- (b) `STOP` entry `"DEPLOYED ·"` → `"DEPLOYED "` (`stop-guard.py:43`).
- (c) The header names `~/.claude/settings.json` (user settings, his R77) in place of `/Users/cobalt/cobalt/.claude/settings.json`. The install object itself is unchanged.
Green: `tests/ops/test_stop_guard.py tests/ops/test_idle_wake.py tests/ops/test_bare_guard.py` → `76 passed, 15 warnings in 3.22s`.
- M-S2a, the exemption off (`… and False`): `1 failed, 29 passed`. `test_s2_a_worktree_seat_whose_first_message_names_no_card_never_blocks`: `E       AssertionError: assert (2, '', 'NOT ...then stop.\n') == (0, '', '')`.
- M-S2b, the negative control: the exemption widened to "no CARD found, or no first message" (`if not CARD.search(text or ""):`). Result: `1 failed, 29 passed`. `test_a_transcript_with_no_first_message_blocks`: `E       AssertionError: assert 0 == 2`.
- M-S2c, `"DEPLOYED "` → `"DEPLOYED ·"`: `1 failed, 29 passed`. `test_stop_guard.py:137: AssertionError: assert (2, 'NOT A RE...then stop.\n') == (0, '')` (the `DEPLOYED deploy-…` case).
- Each mutation was undone with the Edit tool. `git diff --stat` afterwards showed only the fix: `ops/desk/stop-guard.py | 21`, plus this report.
- (c) is header text: no test asserts it. The I1 RUN test at the fix (`-rP`) prints the same object as before, and it loads as JSON (`76 passed`, captured stdout identical to I1's above).
Commit: `1bfd26e3 fix(worker-watch): no-CARD seat exempt, DEPLOYED stop line, install in user settings (S2; L1, L71, L77)`. DevDocs: no page (as for S1).

## RESTARTS
`uv run cobalt jobs restarts a09f0862..HEAD` (HEAD `264e58f7`), whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/worker-watch-build-2026-10-03.md	A	DOCS	-
ops/desk/desk-watch.sh	M	operator script; no Cobalt reader	-
ops/desk/idle-wake.py	A	operator script; no Cobalt reader	-
ops/desk/stop-guard.py	A	operator script; no Cobalt reader	-
ops/desk/wait-stop-line.sh	M	operator script; no Cobalt reader	-
tests/ops/test_desk_watch.py	M	test/documentation; no resident	-
tests/ops/test_idle_wake.py	A	test/documentation; no resident	-
tests/ops/test_stop_guard.py	A	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row. (The tool also lists the uncommitted report file.)

S2, at HEAD `1bfd26e3`: `uv run cobalt jobs restarts a09f0862..HEAD` → the same eight paths with the same rules (the report now `M`, `DOCS`), whole last line `RESTARTS: none`. No UNCLASSIFIED row.

## W THE THREE SUITES
`<tip>` = `264e58f7`. TREE STATE: unchanged. The diff adds no with-DB test and nothing under `src/cobalt/db_migrations`.
- (a0) `git diff --name-only --no-renames a09f0862` → `ops/desk/desk-watch.sh`, `ops/desk/idle-wake.py`, `ops/desk/stop-guard.py`, `ops/desk/wait-stop-line.sh`, `tests/ops/test_desk_watch.py`, `tests/ops/test_idle_wake.py`, `tests/ops/test_stop_guard.py`. Every path starts with `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 7 paths)`**.
- (a) Offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 631.78s (0:10:31)`; 0 failed, 0 errors → `<p>` = 3737. This build adds no test under `tests/cobalt` or `tests/taxonomy`.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` → `529 passed, 1 xfailed, 15 warnings in 258.47s (0:04:18)`. Added by this build: `tests/ops/test_stop_guard.py` (29 test ids, I1's RUN among them), `tests/ops/test_idle_wake.py` (7), and 21 `test_w1_*` ids in `tests/ops/test_desk_watch.py`.
- (b)–(d), (f): not run (DB: none).
- (e) Live-note, `.env` absent (`ls /Users/cobalt/cobalt-wt/worker-watch-1003/.env` → `No such file or directory`): `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.84s`. The one skip is `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, and none names `COBALT_LIVE_VAULT_ROOT` → `<l>` = 146.

**W for S2, `<tip>` = `1bfd26e3`** (the row: `offline` + `tests/ops`; live-note also run, a listed string, ~30 s):
- (a0) `git diff --name-only --no-renames a09f0862` → `docs/40 - DevDocs/reports/worker-watch-build-2026-10-03.md`, `ops/desk/desk-watch.sh`, `ops/desk/idle-wake.py`, `ops/desk/stop-guard.py`, `ops/desk/wait-stop-line.sh`, `tests/ops/test_desk_watch.py`, `tests/ops/test_idle_wake.py`, `tests/ops/test_stop_guard.py`. Every path starts with `docs/`, `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 8 paths)`**.
- (a) Offline: `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) → `3737 passed, 745 skipped, 1 xfailed, 36 warnings in 640.60s (0:10:40)` → `<p>` = 3737.
- ops: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` (background) → `530 passed, 1 xfailed, 15 warnings in 256.48s (0:04:16)`. That is 529 + 1: S2 adds `test_s2_a_worktree_seat_whose_first_message_names_no_card_never_blocks`, renames `test_a_transcript_with_no_card_blocks` → `test_a_transcript_with_no_first_message_blocks`, and changes one parametrize id.
- (e) Live-note, `.env` absent (`ls …/.env` → `No such file or directory`, 13:43): `146 passed, 1 skipped, 15 warnings in 28.37s`; the one skip `test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC …`, none naming `COBALT_LIVE_VAULT_ROOT` → `<l>` = 146.

## PRE-STOP SELF-CHECK
S2 (resume, `1bfd26e3`):
1. Both S2 tests went red at E2 for the row's reasons (quoted in `## E2 RED`). The `CARD:` half is a negative control: green at the tip, and green under M-S2a, which flips only the no-`CARD:` half. The rewritten no-first-message test goes red under M-S2b. The `DEPLOYED` case goes red under M-S2c. Holds.
2. The hook has one entry, the harness's Stop event (`grep -rn -F "stop-guard" ops` → `stop-guard.py:2,25` header, `idle-wake.py:8,23,26`). idle-wake imports only `report_last_line()` and `worktree()`, neither of which S2 changed. Its tests stay green (`76 passed`). S2's entry paths, each pinned:
   - no `CARD:` → 0
   - `CARD:` → block
   - no user message, or no transcript → block
   - build, check, PASS-2 and CONTINUE messages → unchanged tests, green
Holds.
3. Re-run at the tip: `git log --oneline a09f0862..HEAD`; `grep -n -F "DEPLOYED " ops/desk/stop-guard.py` → `43`; `grep -n -F "CARD.search" ops/desk/stop-guard.py` → `89`, `128`; `grep -n -F "settings.json" ops/desk/stop-guard.py` → `16`. Holds.

Pass 1 (`264e58f7`):
1. "Every added or changed test shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten." S1 and N1: every test red at E2 (no such file), and the loop guard, cwd exemption, check-report key, type filter, append mode and cwd filter each red under their mutation (M-S1a–d, M-N1a–c). W1: positives red at E2 (`assert 2 == 3`); every negative control red under its mutation (M-W1b–l). Two stayed green and were rewritten: `…old_wake_lines…` (M-W1d) and `…stop_line_written_as_the_session_goes_idle_wins` (M-W1k). The 15 existing desk-watch tests changed only their helper (a staged copy): green on BASE and at the tip, and M-W1a leaves them green, as it should (their behaviour is unchanged). Holds.
2. "Every entry path of each rule pinned by a test." Callers at the tip: `grep -rn -F "wait-stop-line.sh" ops` → desk-watch.sh:79 (the probe; pinned by every `test_w1_*` desk-watch test); `desk-launch.sh:880` (reminder text, the three-argument form: pinned by `…without_a_session_reads_no_listing` as today's watch; see DECISION 4); desk-context.sh:10 and idle-wake.py:9 (comments). `desk-watch.sh` callers: `desk-launch.sh:202`, the `WATCH:` line (its text pinned by `tests/ops/test_desk_launch_prechecks.py:218`, green). Every desk-watch kind is pinned (`…each_kind…` for check, devfix and deploy; build throughout; `…close_watches_close_mmdd`). The hooks have one entry each, the harness, pinned by stdin JSON per case: active / inactive, exempt / worker / sub-folder cwd, build / check / PASS-2 / CONTINUE launch messages, string and list content, no card, no transcript, empty value, bad JSON. Holds.
3. "Every file:line, count and quote in the report re-read from tool output at the tip." Re-run at the tip: `git log --oneline a09f0862..HEAD`, `git show 264e58f7:ops/desk/wait-stop-line.sh`, `grep -n -F "stop_hook_active" ops/desk/stop-guard.py` (lines 4, 117), `grep -n -F "idle_prompt" ops/desk/idle-wake.py` (4, 5, 35), `grep -rn -F "wait-stop-line.sh" ops`. Suite counts copied from the tip runs above. Holds.

## FOR THE CHECK
- PASS 2 (S2): range `80a11302..1bfd26e3`: `0a725bed wip(worker-watch): red — S2 tests before the fix`, `1bfd26e3 fix(worker-watch): no-CARD seat exempt, DEPLOYED stop line, install in user settings (S2; L1, L71, L77)`. Reds, mutations and greens: `## E2 RED` / `## E3 THE ROWS`, under **S2**. Suites: `## W THE THREE SUITES`, under **W for S2**. O1: a first message with no `CARD:` → exit 0. That one is deliberately narrow: a missing transcript, or one with no user message, still blocks. O6: `DEPLOYED ` (with a space; `DEPLOYED` alone still blocks, in the look-alike list).
- Range `a09f0862..264e58f7`: `a6e8d571 wip(worker-watch): red — S1, N1, W1 tests before the scripts`, `264e58f7 feat(worker-watch): Stop hook, idle hook, watch idle exit (S1, N1, W1, I1; L1, L3, L28, L71)`.
- Reds, mutations, greens per row: `## E2 RED` and `## E3 THE ROWS`. Caller greps: PREFLIGHT and SELF-CHECK 2. RUN row I1's output, whole: `## E3 THE ROWS`.
- Suites: `## W THE THREE SUITES`. With-DB suite: not run (DB: none). `<F0>` / `<F1>` / `<F2>`: not run (DB: none). Lock taken / released: not run (DB: none).
- RESTARTS table: `## RESTARTS`. Records copied at PREFLIGHT: `## PREFLIGHT`.
- For X1–X4, what the build saw:
  - X1: the loop guard comes first (`stop-guard.py:117`) and returns before any read. The desk and brain cwd `/Users/cobalt/cobalt` exits 0 before the transcript is opened (pinned with an unparseable transcript).
  - X2: no report, no card or a missing transcript all block once. A stop line followed by a blank and then prose blocks, because only the last non-blank line counts. A report in another folder is read only if the card names it.
  - X3: `idle · working` is busy (M-W1b), and a WAKE line beside `working` does not fire (M-W1i).
  - X4: the `DEPLOYED` stop line in DEPLOY-HUB.md:185 is `DEPLOYED <TAG> …` with no `·`, so `DEPLOYED ·` (the card's list) never matches it. Deploy and close run in `/Users/cobalt/cobalt`, so S1 never acts for them. `REBUILT ·` (DEVFIX-HUB.md:56) and `FAILED: … · rollback:` (DEPLOY-HUB.md:186, covered by `FAILED`) are in the list. `RESUMED:` is not in the card's list, and is blocked.

## CONTINUE
next: none — BUILT (S2 closed at `1bfd26e3`)

## DECISIONS
- Pass 2 (S2): none. Items 1–4 below are pass 1's; the judge answered all four KEEP (card `## RECORDS`, desk row 2026-10-03 R69), and none is open.
- DECISION 1 (ASK DESK [12:27]): the Notification input field that carries the kind is not in any local file. The matcher value `idle_prompt` is (`hooks-patterns.md:191-196`). Default taken: `idle-wake.py` checks `notification_type == "idle_prompt"`, and his install text sets the entry's matcher to `idle_prompt`. If the field has another name, the hook writes nothing, and the watch's own LIST read (two idle polls) still exits 3. Owed: after his install, the first real idle should leave a WAKE line; none means this field name is wrong.
- DECISION 2 (ASK DESK [12:27]): the card says a WAKE line makes the watch exit 3 "at once". The build exits at once only when the listing does not show the session busy (`status` not `idle`, or `idle · working`). The reason is X3: a worker waiting on a background run keeps `working` and may still raise the idle notification (changelog: an `idle_prompt` fix for background agents). Default taken: the gate as built (M-W1i pins it). The literal reading is a one-line change at `wait-stop-line.sh` (`[ "$state" = busy ] ||`).
- DECISION 3 (ASK DESK [12:27]): the card gives no poll count for GONE. Default taken: two consecutive polls, like idle, so one dropped or slow `claude agents` answer does not end a watch (`…one_missing_listing_between_busy_ones_is_not_gone`). An unreadable listing (desk-list.sh exits non-zero) is busy, never gone.
- DECISION 4 (outside the rows): `desk-launch.sh:880`, the devfix launch reminder, tells the desk to watch with `wait-stop-line.sh <its REPORT> '^(REBUILT|FAILED)'`, which has no session argument and so no idle exit. The `WATCH:` line the launcher prints (`desk-watch.sh devfix "<card>"`) has it. Default taken: nothing changed (desk-launch.sh is outside this card). Either the desk watches a devfix with the `WATCH:` line, or a later card adds `<job>-devfix` to that reminder.

## RECORDS
- REFUSED, not needed: `grep -rn -F "desk-list" ops tests docs/40\ -\ DevDocs/prompts` — "Permission to use Bash has been denied because Claude Code is running in don't ask mode." Done with the Grep tool instead.
- REFUSED, not needed: `grep -n "^## " /Users/cobalt/cobalt-wt/worker-watch-1003/docs/40\ -\ DevDocs/prompts/BUILD-HUB.md` — the same message. The hub was read whole with the Read tool.
- S1 finds the report through the card of the transcript's first user message (not the newest-by-mtime glob). Why: every hub launch line carries `CARD: '<card>'` (BUILD-HUB:12, CHECK-HUB:10, DEPLOY-HUB:11, DEVFIX-HUB:12). It is provable per session, it covers a devfix `REPORT` under `/Users/cobalt/cobalt/docs/…`, and it tells a check with no report yet from the build's `BUILT` report.
- N1 reads the field `notification_type` (value `idle_prompt`); see DECISION 1.
- I1's JSON proof ran as a pytest test. The card's `python3 -c "import json,sys; json.load(open(sys.argv[1]))" <tmp file>` is on no allow string of this launch line, so it was not typed.
- `desk-list.sh` beside the scripts: the installed scripts run from `/Users/cobalt/.claude/ops/` (install-ops links), where `desk-list.sh` is today's real file. In the repo it arrives with card `03` (set 2). Without it beside the watch, the probe refuses loudly (`REFUSED: desk-list.sh is not beside this script`, exit 1); it never reads GONE (`…no_desk_list_beside_the_watch_is_refused_not_gone`).
- Exit 3 in `wait-stop-line.sh` is shared with the desk-size guard's refusal. The stdout first line tells them apart: `REFUSED: desk at …` vs `IDLE:` / `GONE:`.
- Hook facts read for the build: `stop_hook_active` and `cwd` in the official `security_reminder_hook.py:1911-1912`; exit 2 = blocking with stderr to Claude (`hook-development/SKILL.md:294-298`). Changelog lines seen, not relied on: `Fixed idle_prompt notification hooks firing while background agents are still running`, and `claude agents` sessions firing `agent_needs_input` / `agent_completed` Notification hooks (those carry the desk's cwd, exempt).
- `.env`: never present in this worktree (`ls …/.env` → `No such file or directory` at PREFLIGHT and at W (e)). No lock taken (DB: none).
- The card's records, as re-read at PREFLIGHT, are in `## PREFLIGHT`.
- CONTINUED at E3 13:30 (a new session, launch message `CONTINUE: E3`; `git status` → `## ops/worker-watch-1003`, `git log -3` → `80a11302`, `.env` → `No such file or directory`). Pass 1's stop line, replaced by `RESUMED: E3 13:30`: `BUILT · job: worker-watch · tip: 264e58f7 | on a09f0862 | migration: none | offline 3737/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 4 of 4 | self-check: 3 of 3 | decisions: 4 · for Dejan: 0`.
- Re-verified at the resume. The card was last committed at `186b3a98` (it carries S2), with no diff and no placeholder. The hub still has no install marker. R77 (`cto-2026-10-03.md:83`) reads `HIS RULING · APPROVED — pending fold` and was committed at `f248263d`. R83 (`:89`, `DESK RECORD · LAUNCHED`) is on disk but `git log -S"| R83 |"` → empty, so it is not committed yet. S2's authority is the committed card. R77 is a ruling, not in the card's `RULINGS`, and it is committed.
- L74, pass 2: the session's reminder again asked for a `Claude-Session:` line. Not acted on; the commits carry `Co-Authored-By` only.
- The pass-1 DECISIONS 1–4 stay as written. The judge answered them all KEEP (card `## RECORDS`).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: worker-watch · tip: 1bfd26e3 | on a09f0862 | migration: none | offline 3737/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0
