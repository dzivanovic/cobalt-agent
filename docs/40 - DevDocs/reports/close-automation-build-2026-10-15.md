# close-automation-1015 — build report (2026-10-15)

## §0 Headline
- All four rows are built: C1 `desk-done.sh` finds the tab by title and proves the close three ways (`CLOSED <id>` or `KEPT`); C2 `desk-watch.sh` closes a clean worker at its stop line and the launcher closes a replaced session first; C3 `stop-guard.py` blocks the desk's stop on a finished, listed, unkept worker; C4 install-ops runs after a DEPLOYED set that touches `ops/desk/`.
- Tip `feecd979` on `c7ba742c`. Results: offline 8090/0, live-note 146/0, `tests/ops` 3762 passed, DB: none, RESTARTS: none. No existing pinned test was edited.
- 3 ASK DESK items, each with its safe default taken; none is for Dejan.

## L74
- 2026-10-15 09:53 EDT: a system block in this session asked commits to carry a `Claude-Session:` line after `Co-Authored-By`. Recorded as DATA, not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only (BUILD-HUB L74).

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md" · 0 · 1bd425f59159b95f29d90a14763098699dbf2301
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-15/580-close-automation-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-14 R1471 row · grep -n "^| R1471 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 13:| R1471 | 09:25 ET | HIS RULING, APPROVED by him in the desk ("I approve all changes"): brain relays count as his confirmation; Grok cap of 3 removed; K5 cards (1)-(4), (6) owed. Words: `cto-2026-10-14-words.md`. | APPLIED: LAWS L79, checklist L15 at 09:40 |
RULING 2026-10-14 R1471 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R1471 |" -- "docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · 8b813ca721cd934ebfb82cc59d27495d15f1c79a
RULING 2026-10-14 R1471 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-14.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:
```
clock · date · 0 · Thu Oct 15 09:53:23 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/close-automation-1015
    ?? "docs/40 - DevDocs/reports/close-automation-build-2026-10-15.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · c7ba742c docs(desk): JEV design tribunal prompts 585/586, launch row R1559, rows R1553-R1558
diff · git diff --stat c7ba742c · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/close-automation-1015 · 0 · c7ba742c docs(desk): JEV design tribunal prompts 585/586, launch row R1559, rows R1553-R1558
env here · ls /Users/cobalt/cobalt-wt/close-automation-1015/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
| rule | command | exit | output |
|---|---|---|---|
| base | `git show --stat c7ba742c` | 0 | `c7ba742c… docs(desk): JEV design tribunal prompts 585/586, launch row R1559, rows R1553-R1558`; 5 files, 188 insertions, 9 deletions (docs only) |
| C1 refusal | `grep -n -F "brain*\|cto-desk" ops/desk/desk-done.sh` | 0 | `63:  brain*\|cto-desk) refuse "$id is $name: a brain or the desk is stopped only on his word (2026-09-30 R76)" ;;` |
| C1 fixture | `grep -n -F "def stubs" tests/ops/test_desk_done.py` | 0 | `29:def stubs(tmp_path):` |
| C1 herdr JSON | Read `ops/cto-desk.sh:325-362` | — | `herdr pane list` answers one line of JSON, parsed by a walk over dicts (`:345-356`), never split on blanks. `grep -n -F "terminal_title_stripped" ops/cto-desk.sh` → exit 1, no hit (the field name is the card's record of a live `herdr pane list`, `## RECORDS`) |
| C3 callers | `grep -rn -F "unsettled(" ops tests` | 0 | `ops/desk/stop-guard.py:340:def unsettled(items):` · `ops/desk/stop-guard.py:392:            what = unsettled(items)` (one caller) |
| desk-done callers | `grep -rn -F "desk-done.sh" ops tests` | 0 | `ops/desk/desk-done.sh:2`, `:22` (its own usage), `tests/ops/test_desk_done.py:1`, `:18`: no other caller on BASE |
| sizes | `wc -l` | 0 | `71 ops/desk/desk-done.sh` · `95 ops/desk/desk-watch.sh` · `683 ops/desk/stop-guard.py` · `2304 ops/desk/desk-launch.sh` · `243 tests/ops/test_desk_done.py` |
| READ report | `tail -n 3 ".../reports/cto-2026-10-15.md"` | 0 | last line `HANDOVER: predecessor 337752b1 → successor e48f919a at 09:31 · pane w2:pV1` |
| restarts | `uv run cobalt jobs restarts c7ba742c..HEAD` | 0 | one row, the untracked report (`docs/… A DOCS -`); `RESTARTS: none` |

Re-read by Read on the worktree (equal to the card's lines): `desk-done.sh:18-71` (`refuse` `:19`, name read `:46-61`, refusal `:62-64`, `step` `:65-68`, closes `:69-71`); `test_desk_done.py:29-49`; `desk-watch.sh` whole (95 lines; `:62-64`, `:67-71`, `:79-83`, `:90`, `:94-95`); `wait-stop-line.sh:43-45`; `desk-list.sh:8-16`; `stop-guard.py:111`, `:128`, `:315-326`, `:340-370`, `:373-418`; `desk-launch.sh:100-110`, `:263-285`, `:588`, `:921-947`, `:2218-2304` (dry run `:2291-2294`, `if [ -n "$add" ]` `:2296`); `test_desk_watch.py:26-75` (`env` `:68`, `DESK_WATCH_POLL` only); `test_stop_guard.py:313-369`, `:568`; `test_install_ops.py:29-62`; `test_desk_launch_prechecks.py:100-200`. Every launcher test stub of `claude` answers `agents` with `[]` (`grep -n agents tests/ops/test_desk_launch_*.py` and the other launcher tests: 12 hits, each `echo "[]"`).
Card `## RECORDS` copied: drafter 81cb5992 at `main` `bcdef9f0`; amend at `4ca6406a` (desk-done.sh 71 lines, the line map above re-read and equal); `herdr pane list` worker panes carry `terminal_title_stripped` = session name and a `tab_id` (the drafter's run; not re-run here: no listed string); W8 text `cto-desk-checklist.md:60`; restart class `restarts.py:38`, `:232`, `:246`. DB: none — no lock probe.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4328 passed, 806 skipped, 1 xfailed, 36 warnings in 717.02s (0:11:57)`; 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.81s`; the one skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
`uv run pytest -q -rfE -p no:cacheprovider --color=no --tb=line tests/ops/test_desk_done.py tests/ops/test_close_automation_1015.py` on BASE code → `14 failed, 36 passed, 15 warnings in 8.51s`. Each red and its first failing line:
| row | test | first failing line (BASE) |
|---|---|---|
| C1 (1) | `test_c1_a_closed_worker_is_proved_gone_and_prints_closed_last` | `assert '+ claude rm aaaa1111' == 'CLOSED aaaa1111'` (no CLOSED line, no tab lookup) |
| C1 (2) | `test_c1_two_tabs_with_the_title_are_kept_before_any_stop` | `assert 0 == 1` … `stdout='+ claude stop aaaa1111\n+ claude rm aaaa1111\n'` |
| C1 (3) | `test_c1_a_tab_that_stays_is_kept` | `assert 0 == 1` (exit 0, no KEPT) |
| C1 (4) | `test_c1_a_listed_row_that_stays_is_kept` | `assert 0 == 1` (exit 0, no KEPT) |
| C1 (5) | `test_c1_replaced_form_closes_without_a_report` | `REFUSED: usage: desk-done.sh <session id> "<report>" <build\|check\|…> [<tab>]` |
| C2 (1) | `test_c2_a_clean_stop_line_closes_the_worker_and_prints_closed_after_it` | `assert ['BUILT · job...rows: 1 of 1'] == ['BUILT · job...SED aaaa0001']` (one line) |
| C2 (2) | `test_c2_a_failed_stop_line_is_kept_and_runs_nothing` | `assert 'KEPT x-job-build: FAILED' in 'FAILED: x\n'` |
| C2 (3) | `…_is_kept[tree]`, `[report]`, `[busy]` | `assert 'BUILT · job:... rows: 1 of 1' == 'KEPT aaaa000...ree not clean'` · `'CHECK DONE ·...job · pass: 1' == 'KEPT aaaa000...not committed'` · `'BUILT …' == 'KEPT aaaa0001: session busy'` |
| C2 (4) | `test_c2_the_launcher_closes_a_replaced_session_first` | `assert ['claude --bg'] == ['desk-done a...'claude --bg']` (stub desk-done.sh never called) |
| C3 (1) | `test_c3_a_finished_listed_unkept_worker_blocks_with_close_id` | `assert (0, '') == (2, 'start it...daef9-0000\n')` |
| C3 (2) | `test_c3_three_blocks_then_gives_up_and_records` | `assert [0, 0, 0, 0] == [2, 2, 2, 0]` |
| C4 | `test_c4_a_set_that_adds_an_ops_desk_script_leaves_no_script_unlinked` | `assert False` where `(links / 'newone.sh').is_symlink` |

GREEN on BASE (36): every existing test of `test_desk_done.py` with the `stubs` fixture edit (no assert edited), and the controls `test_c1_control_desk_list_stays_read_only`, `test_c2_control_the_stop_line_alone_when_no_desk_done`, `test_c2_control_an_idle_exit_closes_nothing`, `test_c3_control_a_kept_worker_lets_the_turn_end`, `test_c3_control_a_closed_worker_lets_the_turn_end`, `test_c3_control_no_finished_file_changes_nothing`, `test_c4_control_a_set_with_no_ops_desk_path_runs_no_install_ops`, `test_c4_control_a_failed_deploy_runs_no_install_ops`. Fixture edit (ASK DESK 12): stub `claude rm` drops the row from the agents file; stub `herdr pane list` answers `{"result": {"panes": []}}` unlogged; stub `herdr tab close` drops that tab's panes unless `keep-panes` exists. One deviation in shape: C2 (3)'s "report not committed" case runs kind `check` with its report in a separate tmp main repo, because a modified report inside the worktree is first read as "tree not clean" (the card's order of reasons). No RUN row runs here (R3 runs at RESTARTS). Commit `07759ec8 wip(close-automation-1015): red`.

## E3 THE ROWS
Built in the card's order, C1 → C2 → C3 → C4; commit `93282462 feat(close-automation-1015): …(C1-C4, L79 L81)`.
- **C1** `ops/desk/desk-done.sh`: header rewritten (both forms, THE TAB, THE PROOF); usage takes `<id> --replaced [<tab>]`, which skips only the report and stop-word read; after the `brain*|cto-desk` refusal, the title lookup over `herdr pane list` JSON (a walk over dicts with `pane_id`, `cto-desk.sh`'s parse); then `step`s unchanged; then the proof (LIST via `desk-list.sh` beside, `claude agents --json`, the closed tab's panes), `CLOSED <id>` last. Green: `uv run pytest -q tests/ops/test_desk_done.py` → `35 passed`. Added in E3: `test_c1_an_agents_row_that_stays_is_kept` (the `claude agents` proof had no named test; its red is M1c).
  - M1a (lookup off: `if [ -z "$tab" ]` → `if false`) → `4 failed, 2 passed`: test_c1 (1) `assert ['claude stop... rm aaaa1111'] == ['claude stop... close w9:t9']`, (2) `assert 0 == 1`, (3) `assert 0 == 1`, (5) `Right contains one more item: 'herdr tab close w9:t9'`.
  - M1b (LIST proof off: `&& kept "LIST row still present"` → `&& :`) → `1 failed`: `test_c1_a_listed_row_that_stays_is_kept` `assert 0 == 1` (`stdout='+ claude stop aaaa1111\n+ claude rm aaaa1111\nCLOSED aaaa1111\n'`).
  - M1c (agents proof off: `4) kept …` → `4) : ;;`) → `1 failed`: `test_c1_an_agents_row_that_stays_is_kept` `assert 0 == 1`.
- **C2** `ops/desk/desk-watch.sh`: header `:3`, `:15` rewritten and THE CLOSE paragraph; functions `listed`, `unclean`, `close_worker`, `closeout`; `closeout "<line>"` at both stop-line exits, `exit 0` kept. `ops/desk/desk-launch.sh`: one block between the dry run and `if [ -n "$add" ]` (the `--name` read as `:588`, the live rows of that name, busy → REFUSED, each idle → `desk-done.sh <id> --replaced`, KEPT or non-zero → REFUSED, unreadable → REFUSED). Green: `-k test_c2` → `8 passed`; `uv run pytest -q tests/ops/test_desk_watch.py tests/ops/test_desk_launch_prechecks.py` (no edit) → `227 passed in 160.03s`.
  - M2a (`closeout`'s `[ -f "$here/desk-done.sh" ]` → `false`) → `5 failed, 3 passed`: C2 (1) `Right contains one more item: 'CLOSED aaaa0001'`; (2) `assert 'KEPT x-job-build: FAILED' in 'FAILED: x\n'`; (3) ×3 `== 'KEPT aaaa000...ree not clean'` / `...not committed'` / `'KEPT aaaa0001: session busy'`.
  - M2b (launcher block `if [ -n "$rname" ]` → `if false`) → `1 failed`: `assert ['claude --bg'] == ['desk-done a...'claude --bg']`.
- **C3** `ops/desk/stop-guard.py`: `FINISHED` beside `DESK_STOP`; `unsettled()` returns `(what, seen.get("list"))` at its three returns; new `finished_open(items, listing)`; `desk()` unpacks the pair and calls `finished_open` after `queued`, inside the same `try` whose `except ListUnreadable` sets `UNREADABLE`; one header sentence. Green: `-k test_c3` → `5 passed`; `uv run pytest -q tests/ops/test_stop_guard.py` (no edit) → `110 passed in 58.95s`.
  - M3a (`what = finished_open(...)` → `what = None`) → `2 failed, 3 passed`: `assert (0, '') == (2, 'start it...daef9-0000\n')`; `assert [0, 0, 0, 0] == [2, 2, 2, 0]`.
  - M3b (the kept and listed tests removed, first FINISHED id returned) → `2 failed`: the controls `…kept_worker…` and `…closed_worker…` `assert (2, 'start it...daef9-0000\n') == (0, '')`.
- **C4** `ops/desk/desk-watch.sh`: `install_ops` (DEPLOYED only, 8-hex third word, `desk-launch.sh` beside, tag `pre-<JOB>`, `git diff --name-only`, an `ops/desk/` path → `sh desk-launch.sh install-ops`, its last line), called from `closeout` for kind `deploy` after the close. `desk-launch.sh install-ops` unchanged. Green: whole new file → `16 passed`.
  - M4a (`grep -q '^ops/desk/'` → `'^nothing/'`) → `1 failed`: `assert False` where `(links / 'newone.sh').is_symlink`.
  - M4b (`|| return 0` → `|| :`) → `1 failed`: the docs-only control, stdout gained `install-ops: 0 linked, 0 replaced, 0 kept`.
  - The FAILED-deploy control has two guards (the `DEPLOYED ` case and the 8-hex third word); no single mutation turns it red. It pins the end-to-end behaviour.
- After every mutation was undone: `git diff --stat` printed only the fix's 5 files, `297 insertions(+), 14 deletions(-)`.
- ORDER GREEN: `uv run pytest -q tests/ops/test_desk_watch.py tests/ops/test_stop_guard.py tests/ops/test_install_ops.py tests/ops/test_desk_launch_prechecks.py tests/ops/test_bare_guard.py tests/ops/test_desk_done.py tests/ops/test_close_automation_1015.py` → `2258 passed, 15 warnings in 299.61s (0:04:59)`. `git diff --stat c7ba742c..HEAD -- tests/ops/test_desk_watch.py tests/ops/test_stop_guard.py tests/ops/test_install_ops.py tests/ops/test_desk_launch_prechecks.py` → nothing.
- `grep -n -E -e "git show" -e "[0-9a-f]{8}" tests/ops/test_close_automation_1015.py` → 24 hits and no `git show`. Every hit is a constructed fixture: `1a2b3c4d`, `0f0e0d0c` and `5e6f7a8b` (the tips `test_desk_watch.py` uses), `aaaa0001`-`aaaa0004`, `b43daef9-0000`, `c0ffee00-0000` and `0000aaaa`. None is a commit of this repo; C4's head is read at run time by `git rev-parse` of the test's own tmp repo.
- DevDocs: no page under `docs/40 - DevDocs/cobalt/` documents these ops scripts (`grep` of the four names hits only `cobalt/jobs/restarts.md`, which is not their page), so there is no dated line to add (`## RECORDS`).

## RESTARTS
`uv run cobalt jobs restarts c7ba742c..HEAD` (R3), whole:
```
path	change	rule	restart
docs/40 - DevDocs/reports/close-automation-build-2026-10-15.md	A	DOCS	-
ops/desk/desk-done.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-launch.sh	M	operator script; no Cobalt reader	-
ops/desk/desk-watch.sh	M	operator script; no Cobalt reader	-
ops/desk/stop-guard.py	M	operator script; no Cobalt reader	-
tests/ops/test_close_automation_1015.py	A	test/documentation; no resident	-
tests/ops/test_desk_done.py	M	test/documentation; no resident	-
RESTARTS: none
```
No UNCLASSIFIED row.

## W THE THREE SUITES
DB: none. (a0) `git diff --name-only --no-renames c7ba742c` → `ops/desk/desk-done.sh`, `ops/desk/desk-launch.sh`, `ops/desk/desk-watch.sh`, `ops/desk/stop-guard.py`, `tests/ops/test_close_automation_1015.py`, `tests/ops/test_desk_done.py`. Every path is under `ops/` or `tests/ops/`. **`cobalt_dev: not taken (DB: none — 6 paths)`**.
W ran twice: first on `93282462`, then on `<tip>` = `feecd979`, after the second `fix(…)` commit added the self-check pins (`## RECORDS`).
| run | command | verdict, whole | log |
|---|---|---|---|
| 1 (a) | `sh /Users/cobalt/cobalt/ops/desk/gate.sh close-automation-1015 offline` | `tests/ops: run (ops/desk/desk-done.sh)` · `offline 8085/0` | `/Users/cobalt/cobalt-wt/.gate-logs/close-automation-1015-offline-20261015-102340.log` (`:885` `4328 passed, 806 skipped, 1 xfailed`; `:955` `3757 passed, 1 xfailed`) |
| 1 (e) | `sh … gate.sh close-automation-1015 livenote` | `live-note 146/0` | `…/close-automation-1015-livenote-20261015-104947.log` |
| 1 | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` | `3757 passed, 1 xfailed, 16 warnings in 828.63s (0:13:48)` | — |
| 2 (a) | `sh … gate.sh close-automation-1015 offline` | `tests/ops: run (ops/desk/desk-done.sh)` · `offline 8090/0` | `…/close-automation-1015-offline-20261015-110434.log` (`:885` `4328 passed, 806 skipped, 1 xfailed`; `:955` `3762 passed, 1 xfailed`) |
| 2 (e) | `sh … gate.sh close-automation-1015 livenote` | `live-note 146/0` | `…/close-automation-1015-livenote-20261015-112947.log` |
| 2 | `uv run pytest -q -rs -p no:cacheprovider --color=no tests/ops` | `3762 passed, 1 xfailed, 16 warnings in 835.25s (0:13:55)` | — |
The live-note log's one skip (`grep -n -F "SKIPPED"`, `:56`) is `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC … not set`; it does not name `COBALT_LIVE_VAULT_ROOT`. Tests this build adds: 9 + 5 + 1 + 1 in `test_desk_done.py` (`test_c1_*`, including the 2 added at self-check) and 22 in `test_close_automation_1015.py`; all are in the offline count. `ls /Users/cobalt/cobalt-wt/close-automation-1015/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason against a mutation or negative control; any test that stayed green was rewritten. Met: E2's 14 reds on BASE; E3's mutations M1a–M1c, M2a–M2b, M3a–M3b and M4a–M4b; and the four added-pin mutations (lookup unreadable `|| :`, `elif false` ×2, `prodwrite|close` → `nothing`, `listing = []`) → `7 failed, 49 passed`, each new pin among them. The existing `test_desk_done.py` tests stay green with the fixture edit. The card's named controls are GREEN on BASE and after, as the card requires. M1b, M3b and M4b reddened the controls they negate. The FAILED-deploy control of C4 has two guards, so no single mutation reddens it (`## E3`); its positive twin `test_c4_a_set…` is red under M4a.
(2) Every entry path is pinned. Callers at the tip (`grep -rn -F "desk-done.sh" ops/desk`): `desk-watch.sh:139` is pinned by C2 (1), (3) and the kinds test; `desk-launch.sh:2320` by C2 (4); direct calls by `test_desk_done.py`. `grep -rn -F "unsettled(" ops tests` → its one caller, `stop-guard.py:426`, is pinned by C3 and the unedited `test_stop_guard.py` G3/G4 tests. The branches are each pinned: FAILED, clean, dirty, uncommitted, busy, 0 and 2 rows, deploy DEPLOYED and FAILED, prodwrite, an unreadable LIST in `finished_open`, an unreadable pane list, and the `--replaced` refusals of brain and desk.
(3) Re-read at the tip: `grep -c` of the DEPLOY PROOF strings (below) and the two caller greps were run after `93282462`. `feecd979` changes only the two test files (`git diff --stat` before its commit: `tests/ops/test_close_automation_1015.py | 43`, `tests/ops/test_desk_done.py | 10`). The RESTARTS table was re-run at `feecd979`.

## FOR THE CHECK
- Range `c7ba742c..feecd979`: `07759ec8 wip(close-automation-1015): red` · `93282462 feat(close-automation-1015): desk-done.sh tab lookup and proof, desk-watch close and install-ops, launcher replaced-session close, stop-guard finished check (C1-C4, L79 L81)` · `feecd979 fix(close-automation-1015): pin the listing, kind, unreadable-list and pane-list branches (C1-C3, self-check 2)`.
- Per row, the reds, mutations and greens are in `## E2 RED` and `## E3 THE ROWS`. The callers are in PREFLIGHT and self-check (2). R3's output is quoted whole under `## RESTARTS`.
- DEPLOY PROOF counts at the tip: `grep -c -F "terminal_title_stripped" ops/desk/desk-done.sh` → `2` · `grep -c -F "desk-done.sh" ops/desk/desk-watch.sh` → `9` · `grep -c -F "FINISHED" ops/desk/stop-guard.py` → `5` · `grep -c -F "desk-done.sh" ops/desk/desk-launch.sh` → `2` · `tests/ops/test_close_automation_1015.py` present.
- With-DB suite, `<F0>`/`<F1>`/`<F2>`, lock taken and released: `not run (DB: none)`.
- `desk-launch.sh install-ops` (`:921-947`) is unedited; the launcher diff is the one block between the dry run and `if [ -n "$add" ]`.
- The PREFLIGHT records are copied under `## PREFLIGHT`.

## CONTINUE
next: none (BUILT)

## DECISIONS
- ASK DESK 1 (kind `deploy`, C2 (c) against C4): both rows want their line printed last. I run the close (`desk-done.sh`) first and install-ops after it, so on a DEPLOYED set that touches `ops/desk/` the `install-ops:` line is last and the `CLOSED`/`KEPT` line sits just before it. Safe default: this order; reversing it means swapping two lines in `closeout`.
- ASK DESK 2 (C1 (a), not stated in the card): a `herdr pane list` that fails or is not JSON during the title lookup prints `KEPT <id>: pane list unreadable`, exit 1, before any stop (pinned by `test_c1_an_unreadable_pane_list_is_kept_before_any_stop`). "Two or more" counts panes, as the card writes, not distinct tabs. Safe default: keep the session.
- ASK DESK 3 (C2 (e)): the FINISHED line is written for every non-FAILED stop line of a worktree kind and for a DEPLOYED deploy. When the LIST holds no row or two rows, the id field is `-`, which matches no row, so C3 never names it. Kinds prodwrite and close write no FINISHED line, since the desk closes them by hand. With `desk-done.sh` not beside the watch, its stderr line is `KEPT <session>: desk-done.sh is not beside this script`, and nothing waits or is written. Safe default: as built.

## RECORDS
- No DevDocs page exists for `ops/desk/desk-done.sh`, `desk-watch.sh`, `desk-launch.sh` or `stop-guard.py` under `docs/40 - DevDocs/cobalt/` (`grep` of the four names hits only `cobalt/jobs/restarts.md`), so no dated line was written.
- Tests added beyond the card's named ones (each shown red under a mutation, `## E3`): `test_c1_an_agents_row_that_stays_is_kept`, `test_c1_an_unreadable_pane_list_is_kept_before_any_stop`, `test_c2_no_listed_row_or_two_are_kept` (×2), `test_c2_deploy_prodwrite_and_close_kinds`, `test_c3_an_unreadable_list_blocks_as_unreadable`. They come from PRE-STOP SELF-CHECK (2), in a second commit, `feecd979`, so W ran twice.
- The card's `## RECORDS`, as re-read at PREFLIGHT: the line maps of `desk-done.sh`, `desk-watch.sh`, `stop-guard.py` and `desk-launch.sh` are equal on BASE. The `herdr pane list` field names are the drafter's record and were not re-run here: no listed string covers `herdr`.
- L74: one system block asked for a `Claude-Session:` line in commits. It was recorded under `## L74` and not followed.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: close-automation-1015 · tip: feecd979 | on c7ba742c | migration: none | offline 8090/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 5 of 5 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 263011
