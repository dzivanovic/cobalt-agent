# radar-ladder-refresh — build report 2026-10-06

## §0 Headline
- `/radar` now refreshes its ladder on the pool's timer through a new `tickLadder` in `PANEL_JS`; `refreshPool`, `:1576` and `refreshLadder` are unchanged.
- The tick skips, and drops a late result, while a tap strip, TERMINAL, a focused or edited ladder input, or a `post()` is active. An expanded card does not pause it. A failed tick says `REFRESH FAILED` on the ladder.
- Rows A and B built. Six static tests were red on BASE and red under their mutations; the route control was green throughout.
- Gate: offline 3952/0, with-DB 4836/0, live-note 146/0, `cobalt_dev: 0013 — F2 = F0`, `.env` removed. RESTARTS: `com.cobalt.aset com.cobalt.radar`.
- 2 decisions, none for Dejan: X29's setup error was there before this build, and a residual race that rule (4) as written leaves open.

## L74
A harness system block in this session asked for a `Claude-Session:` commit trailer. Recorded here once and not acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/54-radar-ladder-refresh-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-06/54-radar-ladder-refresh-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-06/54-radar-ladder-refresh-card.md" · 0 · 90855248bd012948537772e679ec8a2dac1f7434
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-06/54-radar-ladder-refresh-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-06 R556 row · grep -n "^| R556 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 106:| R556 | 14:20 ET | HIS RULING ([words](cto-2026-10-06-words.md) `## R556`): fix the empty radar screen if the brain says GO (bandwidth, no blocker); desk asked the brain 14:20; on GO the desk launches the fix flow, no further ask to him. | HIS RULING · APPROVED |
RULING 2026-10-06 R556 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R556 |" -- "docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · 8bceed0a20d4157786a85a2f0e44a76a1ff2bf30
RULING 2026-10-06 R556 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-06.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Tue Oct  6 16:59:35 EDT 2026
status · git status --short --branch · 0 · ## ops/radar-ladder-refresh-1006
head · git log --oneline -1 · 0 · 8c554d77 docs(desk): wake-up cba361c6, amend drafter 38437177 launched
diff · git diff --stat 8c554d77 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/radar-ladder-refresh-1006 · 0 · 8c554d77 docs(desk): wake-up cba361c6, amend drafter 38437177 launched
env here · ls /Users/cobalt/cobalt-wt/radar-ladder-refresh-1006/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 8c554d77` | 0 | `docs(desk): wake-up cba361c6, amend drafter 38437177 launched` — `cto-2026-10-06.md \| 2 +-`, `desk-wakeup-log.md \| 1 +` |
| pool timer | `grep -n -F "window.setInterval(refreshPool,interval)" src/cobalt/aset/radar_panel.py` | 0 | `1576: window.setInterval(refreshPool,interval);` |
| refreshLadder callers | Grep `refreshLadder` in `src` | 0 | `radar_panel.py:1518: async function refreshLadder(){` · `:1534:     await refreshLadder();` · `:1575: window.COBALT_RADAR={…refreshLadder:refreshLadder};` |
| new names absent | Grep `tickLadder\|ladder-refresh-status` in `*.py` | 1 | No matches |
| PANEL_JS readers | Grep `PANEL_JS` in `*.py` | 0 | `radar_panel.py:1508`, `:1589`, `:1604`; `tests/cobalt/test_s3_c3_panel_offline.py:547`; `test_radar_panel_cards.py:646`, `:666`; `test_radar_panel.py:563` (docstring), `:1038`, `:1097` |
| interval | Grep `refreshSeconds\|data-refresh-seconds` in `src` | 0 | `radar_panel.py:1559: const interval=Number(document.body.dataset.refreshSeconds)*1000;` · `:1589 … data-refresh-seconds="{view.pool.scan_interval}"` |
| select/textarea | Grep count `<select\|<textarea` in radar_panel.py | 1 | 0 occurrences |
| JS runner | Grep `jsdom\|playwright\|quickjs\|mini_racer\|dukpy` in `tests` | 0 | only `tests/test_finviz_extractor.py`, `tests/test_browser_fast_path.py`, `tests/test_browser_aom.py`, `tests/test_browser_actions.py` (none runs the page script) |
| playwright in tests/cobalt | `grep -rln playwright tests/cobalt` | 1 | (no output) |
| web.radar | Grep in `web.py` | 0 | `900:def radar(frame: str \| None = None) -> str:` · `909: page = render_failed_page(message, phone_frame=phone_frame)` |
| wc -l | `wc -l` of the three row files | 0 | `1633 radar_panel.py` · `1257 test_radar_panel.py` · `201 radar_panel.md` |
| READ tails | `tail -n 3` each | 0 | `TRACE DONE · cause: design · line: src/cobalt/cards/store.py:1055 · decisions: 2 · tokens: not recorded` · `SURVEY DONE · first zero day: none · decisions: 2` · `READ DONE · table: 26 · view: 26 · lost: 0 · cause: state · decisions: 1` |
| RESTARTS empty | `uv run cobalt jobs restarts 8c554d77..HEAD` | 0 | only this uncommitted report: `docs/…/radar-ladder-refresh-build-2026-10-06.md A DOCS -` · `RESTARTS: none` |

Records copied (card `## RECORDS`): LANE build, no migration · RESTARTS expected `com.cobalt.aset com.cobalt.radar` (re-read: `jobs.yaml:90 imports: [cobalt.aset.__main__, cobalt.aset.web]`, `:194 imports: [cobalt.cli]`) · LIMIT: static tests only, browser timing UNPROVEN (re-read: no playwright in tests/cobalt) · BEHAVIOUR NOTE · LOAD · RULINGS R556 (re-read by authorize.sh: row 106, `8bceed0a`) · BASE at drafting `542a8348`, refilled `8c554d77`; every `file:line` the card names re-read at BASE matches (`radar_panel.py:1508`–`:1578` read whole).

## E0 BASELINE
On `8c554d77`. `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3945 passed, 787 skipped, 1 xfailed, 36 warnings in 604.45s (0:10:04)`, exit 0; 0 failed, 0 errors.
`COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 28.69s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests written in `tests/cobalt/test_radar_panel.py` after `:1103`; no `src/` edit. No with-DB red, so no lock take at E2. `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py -k "tick or expanded or failed_tick or one_ladder_fetch or formed_after_an_empty_load"` → `6 failed, 4 passed, 81 deselected in 0.71s`. Each red's first line:
- (1) `test_tick_refreshes_the_ladder_on_the_pool_timer_without_reload` → `assert 'window.setInterval(tickLadder,interval)' in "…"` (tickLadder absent)
- (2) `test_tick_never_swaps_over_work_in_progress` → `AssertionError: async function tickLadder(){ absent from PANEL_JS`
- (2b) `test_an_expanded_card_does_not_pause_the_tick` → `AssertionError: async function tickLadder(){ absent from PANEL_JS`
- (3) `test_a_failed_tick_is_said_on_the_ladder` → `AssertionError: async function tickLadder(){ absent from PANEL_JS`
- (4) `test_one_ladder_fetch_in_flight_and_none_while_a_post_sends` → `AssertionError: async function tickLadder(){ absent from PANEL_JS`
- (5) `test_tick_uses_the_pool_interval` → `assert 'window.setInterval(tickLadder,interval);' in "…"`
- ROUTE CONTROL `test_radar_route_serves_a_card_formed_after_an_empty_load` → PASSED on BASE (a control, as the card says). The other 3 passes are existing tests the `-k` matched.
Commit `7ba8880e wip(radar-ladder-refresh): red — tickLadder static tests and route control (A, R556)`.

## E3 THE ROWS
Row A: `PANEL_JS` only — `let sending=0;` before `post`, `sending+=1` after the `'sending'` status, `finally{sending-=1;}`; `let ladderInFlight=false;` + `async function tickLadder(){…}` after `refreshPool`, before `window.COBALT_RADAR`; `window.setInterval(tickLadder,interval);` after `:1576`, which is byte-identical. `refreshLadder` unchanged (pinned by test (1) against BASE's body). Row B: the dated paragraph at the end of `docs/40 - DevDocs/cobalt/aset/radar_panel.md` (also this module's DevDocs line).
After the rows: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_s3_c3_panel_offline.py` → `156 passed, 11 skipped in 2.13s` (skips: `requires_db` / `reaches cobalt_dev (lock-relief G1)`).
X29 control: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/experiments/stale_score/test_x29_ladder_render.py` → `1 error in 0.08s`: `ERROR at setup … fixture 'offline_skip_guard' not found` (`tests/cobalt/conftest.py:262` `dev_db_tx(monkeypatch, request, offline_skip_guard)`; `tests/experiments/stale_score/conftest.py:31` re-exports `dev_db_tx` only). Not this build's: `git diff --stat 8c554d77 -- tests/experiments tests/cobalt/conftest.py` → no output. Under `## DECISIONS` (UNPROVEN, L70).

MUTATIONS (each made with Edit, the named test run alone, undone with Edit):
| row | mutation | result (first failing line) |
|---|---|---|
| (1),(5) | delete `window.setInterval(tickLadder,interval);` | `2 failed` — `test_radar_panel.py:1143: assert 'window.setInterval(tickLadder,interval)' in …`; `:1206` same for (5) |
| (5) | `window.setInterval(tickLadder,60000);` | `1 failed` — `:1206: assert 'window.setInterval(tickLadder,interval);' in "…window.setInterval(tickLadder,60000);…"` |
| (2) | drop `details.terminal[open]` from the guard after the await | `1 failed` — `:1163: AssertionError: details.terminal[open] not checked again before the swap` |
| (2b) | add `layer.querySelector('.ladder-item.open')` to the first guard | `1 failed` — `:1170: AssertionError: assert ('.ladder-item.open' not in …` |
| (3) | empty `catch(failure){}` | `1 failed` — `:1187: AssertionError: classList.add('refresh-failed','stale-data')` |
| (4) | remove tickLadder's `finally{ladderInFlight=false;}` | `1 failed` — `:1195: assert 'finally{ladderInFlight=false;}' in …` |
| (4) | post's `finally{sending-=1;}` → ` sending-=1;` after the catch | `1 failed` — `:1200: assert False … .endswith('finally{sending-=1;}')` |
After the undo: `git diff --stat` → `src/cobalt/aset/radar_panel.py | 32 ++++++++++++++++++++++++++++++--` (30+/2-, the fix as first written); the three files again `156 passed, 11 skipped`.
Commit `d2330003 fix(radar-ladder-refresh): the pool timer also refreshes the ladder through tickLadder (A, B, L1, L3)`.

## RESTARTS
`uv run cobalt jobs restarts 8c554d77..HEAD` →
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-ladder-refresh-build-2026-10-06.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No UNCLASSIFIED row; matches the card's expectation.

## W THE THREE SUITES
`<tip>` = `d2330003`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-ladder-refresh-1006 all --deploy` (no `--deselect`: this build adds no with-DB test; no `--tickers`: no with-DB test writes a ticker; no `--migration`) → exit 0. Verdict lines, whole:
```
offline 3952/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4836/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-ladder-refresh-1006-all-20261006-171423.log
```
None of the skips is marked `OUTSIDE the allowed set`. Taken from the log with `grep -n -F`:
- (a) `:862` `3952 passed, 787 skipped, 1 xfailed, 36 warnings in 592.83s` → offline 3952/0 (the 7 tests this build adds: the six static tests and the route control, `test_radar_panel.py:1141`–`:1209`).
- (b) `:868 lock taken: radar-ladder-refresh-1006`; `:873` the only `.env` is this worktree's; `:879 F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; proof-only → `LEVEL 0013`.
- (c) PASS 1, `:934`: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py` → `:1087 4647 passed, 7 skipped, 83 deselected, 3 xfailed` = d1 4647.
- (c2) `:1089 dev forward: APPLIED 17:37:04`; `:1164 F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2, the `:1166` command (the gate-lists PASS 2 list, with no addition from this build) → `:1800 189 passed, 1 deselected` = d2 189; 4647 + 189 = 4836, which is the gate's `with-DB 4836/0`.
- (c3r) `stray rows: not read (no --tickers given)`: this build's tests write no ticker.
- (f) `:1804` rollback `--down-to 0013`; `:1865 F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0 → `:1916 cobalt_dev: 0013 — F2 = F0`; `:1918 lock released`; `:1921 No such file or directory`. My own call, `ls /Users/cobalt/cobalt-wt/radar-ladder-refresh-1006/.env`, gave `No such file or directory`.
- (e) `:1987 146 passed, 1 skipped` → live-note 146/0.
- Gate log `:1912` shows `code: d2330003 (DIRTY: 1 path(s))`: that path is this uncommitted report, and no test reads it.

## PRE-STOP SELF-CHECK
(1) Each added test was shown red. At E2 six tests were red on BASE (quoted under `## E2 RED`). At E3 each was red under its named mutation (the table under `## E3`): (1) `:1143`, (2) `:1163`, (2b) `:1170`, (3) `:1187`, (4) `:1195` and `:1200`, (5) `:1206`. The route control is a control the card says is green on BASE and after; it was green at both points. No test stayed green under its mutation, so none was rewritten.
(2) Callers and entry paths, each pinned:
- `refreshLadder` is called by `post()` at `:1534` (pinned by test (1)'s `await refreshLadder()` and its byte pin of `refreshLadder`'s body) and exported in `window.COBALT_RADAR` (the line is unchanged).
- `tickLadder` has one caller, the new `setInterval` (tests (1) and (5)).
- `post()` is entered from the click handler for dot, key, promote and tap; those branches are unchanged and pinned by `test_s3_c3_panel_offline.py:546` and `test_radar_panel_cards.py:665`, both green. Its send counter is pinned by test (4).
- Each guard state is pinned by tests (2) and (2b), checked both before the fetch and after the await.
- The failed-page path (`web.py:909`, a page with no `#ladder-layer`) throws `the /radar page returned no ladder` and lands in the catch: test (1) pins the throw and test (3) pins the catch.
(3) Re-read at the tip with `grep -n -F "tickLadder" src/cobalt/aset/radar_panel.py` → `1577: async function tickLadder(){` · `1604: window.setInterval(tickLadder,interval);`. The test line numbers come from `grep -n -F "def test_" tests/cobalt/test_radar_panel.py` (`:1141`, `:1159`, `:1168`, `:1180`, `:1191`, `:1203`, `:1209`). Commits come from `git log --oneline 8c554d77..HEAD`, and the gate lines from `grep -n -F` of the log.

## FOR THE CHECK
- `8c554d77..d2330003`: `7ba8880e wip(radar-ladder-refresh): red — tickLadder static tests and route control (A, R556)` · `d2330003 fix(radar-ladder-refresh): the pool timer also refreshes the ladder through tickLadder (A, B, L1, L3)`.
- Per row, the reds, mutations and greens are under `## E2 RED` and `## E3 THE ROWS`. The caller greps are under `## PREFLIGHT` and self-check (2). There is no RUN row.
- Suites: under `## W` (the commands are copied whole above, at log lines `:2`, `:934`, `:1166` and `:1932`).
- Fingerprints: F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 `664 35 272c95bbb12241e3611e4b36326ccf87`. One lock take, inside `gate.sh`: the log started 17:14:23, the lock was taken after offline (`lock: waited 0 min`), forward ran at 17:37:04, and the lock was released before live-note. The gate log does not print the take and release clock times, and the gate run finished before 17:42:10 (`date`).
- RESTARTS table: under `## RESTARTS`.
- Records copied at PREFLIGHT: under `## PREFLIGHT`.
- X1: the guards before the fetch and after the last await cover the tap strip, TERMINAL, a focused input, an edited input or checkbox, and `sending>0`. A result that lands while any of them holds is dropped. See DECISION 2 for a `post()` that both begins and ends inside one tick's fetch.
- X2: the catch writes `#ladder-refresh-status` and the `refresh-failed stale-data` classes. The swapped-in layer has neither, so the next good tick clears them. `refreshPool`, `mirrorDegraded`, `mirrorStale`, the cursor and `:1576` are unchanged (`git diff 8c554d77 -- src/cobalt/aset/radar_panel.py` touches no pool line).

## CONTINUE
next: CLOSE (done)

## DECISIONS
- DECISION 1 (UNPROVEN, L70; outside the rows, not fixed): the card's control `tests/experiments/stale_score/test_x29_ladder_render.py:44`–`:63` cannot be shown green, because it errors at setup: `fixture 'offline_skip_guard' not found` (`tests/cobalt/conftest.py:262` needs it, and `tests/experiments/stale_score/conftest.py:31` re-exports `dev_db_tx` only). This build does not touch either file (`git diff --stat 8c554d77 -- tests/experiments tests/cobalt/conftest.py` → no output), and X29 is in no gate list (`grep -n -F "stale_score" ops/desk/gate-lists.md` → its with-DB file only). The text constraints X29 reads still hold, and the new tests pin them: `refreshPool` is unchanged, `post()` still awaits `refreshLadder()`, and `mirrorStale(next)` is unchanged. Safe default taken: not fixed here; for the desk.
- DECISION 2 (ASK DESK, safe default taken): rule (4) as the card writes it is an in-progress counter. A `post()` that both begins and ends while a tick's `GET /radar` is in flight leaves the counter at 0 when the tick checks it after the await. The tick may then swap in a render older than the one `post()` just drew, and the next tick (one interval) replaces it. The cost is that render for one interval and the `saved` status line in the swapped layer. Closing the gap would take a monotonic send sequence, which is a second mechanism the card does not name. Safe default: built exactly as the card says (L72, THE ROWS); not widened.

## RECORDS
- The build ran in one session. No `REFUSED, not needed` line, no `CONTINUED`, and no extra lock take: the only take was the one inside `gate.sh`.
- `.env`: removed, proven gone (W).
- L74: one harness block asking for a `Claude-Session:` trailer was recorded under `## L74` and not acted on.
- The card's records, as re-read at PREFLIGHT: RESTARTS came out as expected (`com.cobalt.aset com.cobalt.radar`). LIMIT: browser timing is UNPROVEN, because the tests read the script's text and do not run it. The live proof after deploy is `logs/aset.log` showing `GET /radar` once per interval beside `/api/radar/pool`.
- The PREFLIGHT RESTARTS run was not an empty range: it listed this uncommitted report (DOCS, `RESTARTS: none`).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: radar-ladder-refresh · tip: d2330003 | on 8c554d77 | migration: none | offline 3952/0 | with-DB 4836/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 2 of 2 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 172093
