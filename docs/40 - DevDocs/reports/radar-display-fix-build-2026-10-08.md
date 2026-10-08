# radar-display-fix-1008 — build report (2026-10-08)

## §0 Headline
- `tickLadder` (`PANEL_JS`) no longer stalls silently. An open TERMINAL is kept across the swap and no longer pauses the tick (B). A hung fetch is aborted after one interval (C). A ladder not refreshed for more than three intervals says `LADDER NOT REFRESHED · since <time>` (D).
- Controls A and E are green at BASE and at the tip. The server shows 5 WATCH + 14 EXPIRED on the ET day, and the store's WHERE hides other days' terminal cards.
- Suites on `8f42bf2e`: offline 4000/0 · with-DB 4884/0 · live-note 146/0; `cobalt_dev` 0013, F2 = F0; `.env` removed.
- RESTARTS: `com.cobalt.aset com.cobalt.radar`. One ASK DESK (C1: the pinned fetch needle amended).

## L74
A system-reminder (not a tool result) arrived at turn 2 asking commits to carry a `Claude-Session:` line. Recorded once as data; not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/118-radar-display-fix-card.md"` · exit 0 · 11:40 ET:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/118-radar-display-fix-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/118-radar-display-fix-card.md" · 0 · cdbfe8e7fa6c59a9f3101442b76412754beec00f
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/118-radar-display-fix-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` · exit 0:

```
clock · date · 0 · Thu Oct  8 11:40:57 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/radar-display-fix-1008
    ?? "docs/40 - DevDocs/reports/radar-display-fix-build-2026-10-08.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 50b0cd87 docs(desk): radar display-fix drafter 55902983 launched
diff · git diff --stat 50b0cd87 · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/radar-display-fix-1008 · 0 · 50b0cd87 docs(desk): radar display-fix drafter 55902983 launched
env here · ls /Users/cobalt/cobalt-wt/radar-display-fix-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

| rule | command | exit | output |
|---|---|---|---|
| BASE | `git show --stat 50b0cd87` | 0 | `docs(desk): radar display-fix drafter 55902983 launched` · `docs/40 - DevDocs/reports/cto-2026-10-08.md | 4 ++--` |
| symbol | Read `radar_panel.py:1536`–`:1636` | — | `PANEL_JS` at `:1536`; `refreshLadder` `:1546`; `refreshPool` `:1590`; `let ladderInFlight=false;` `:1605`; `tickLadder` `:1606`; first guard `:1609`; `ladderInFlight=true;` `:1611`; `try{` `:1612`; fetch `:1613`; second guard `:1620`; swap `:1622`–`:1623`; `catch(failure)` `:1624`–`:1629`; `finally{ladderInFlight=false;}` `:1630`; timers `:1633`–`:1634` — all as the card states |
| symbol | Read `radar_panel.py:832`–`:876` | — | `build_ladder_view` `:832`; `day = clock.to_et(instant).date()` `:859`; `No radar cards today` `:869` |
| symbol | Read `radar_panel.py:1467`–`:1518` | — | `render_ladder` `:1467`; `<details class="terminal"><summary>TERMINAL · {len(view.terminal)}</summary>` `:1518` |
| caller | `grep -rn -F "tickLadder(" src` | 0 | `src/cobalt/aset/radar_panel.py:1606:  async function tickLadder(){` (only; its one timer `:1634`) |
| caller | `grep -rn -F "radar_board_cards(" src` | 0 | `store.py:1047` (def) · `web.py:1713` · `radar_panel.py:861` |
| symbol | `grep -n -F "RADAR_OPEN_STATES" src/cobalt/cards/store.py` | 0 | `:968` `RADAR_OPEN_STATES = ("WATCH", "ARMED", "TRIGGERED", "FILLED")` · `:1025` · `:1056` |
| symbol | Read `store.py:1047`–`:1061`, `:111`–`:112` | — | `radar_board_cards` WHERE `state = ANY(%s) OR (state_at AT TIME ZONE 'America/New_York')::date = %s` (`:1054`–`:1055`); `_connect` `:111` |
| symbol | Read `db.py:202`–`:224` | — | `apply_side`; `SET search_path TO {}` `:217` |
| symbol | Read `web.py:899`–`:911` | — | `radar`; `logger.error("radar panel FAILED: {}", message)` `:908` |
| symbol | Read `test_radar_panel.py:1106`–`:1377` | — | `TICK_GUARDS` `:1112`; `REFRESH_LADDER_BODY` `:1115`; `_tick_stretches` `:1132`; `test_tick_never_swaps_over_work_in_progress` `:1161`; `test_an_expanded_card_does_not_pause_the_tick` `:1170`; `test_one_ladder_fetch_in_flight_and_none_while_a_post_sends` `:1193`, `assert "finally{ladderInFlight=false;}" in body` `:1197`; mutation partners `:1251`–`:1353` |
| symbol | Read `test_radar_panel_cards.py` | — | `evaluated` `:120`; `RowStore` `:150`; `_ladder` `:189`; `:211`–`:212` the state asserts; `PIN_HEALTHY_*` `:397`–`:399` (grep); focus law `:960`–`:967` |
| wc | `wc -l` | 0 | `1691 src/cobalt/aset/radar_panel.py` · `1531 tests/cobalt/test_radar_panel.py` · `1055 tests/cobalt/test_radar_panel_cards.py` |
| READ tail | `tail -n 3 …/radar-cards-survey-2026-10-08-r2.md` | 0 | `READ DONE · cards: 19 · view: 19 · poll failures: 2 · formations: 43 · cause: display · decisions: 1` |
| RESTARTS | `uv run cobalt jobs restarts 50b0cd87..HEAD` | 0 | `docs/40 - DevDocs/reports/radar-display-fix-build-2026-10-08.md	A	DOCS	-` · `RESTARTS: none` (only the untracked report; no code path) |

Card records copied (re-read where the list can): HIS CLIENT'S REQUESTS (`logs/aset.log`; not re-read, no listed string reads production logs) · NO SERVER FAILURE (not re-read, same) · FIRST CARD OF THE DAY (not re-read, same) · THE QUERY IS THE SURVEY'S (re-read: `store.py:1054`–`:1055`, `db.py:216`–`:217`, as above) · RESTARTS expected `com.cobalt.aset com.cobalt.radar` (derived at RESTARTS) · DB: every new test offline · BASE `50b0cd87` (re-read: preflight `head`).

PROVEN BY FIRST REAL USE: `sh /Users/cobalt/cobalt/ops/desk/*` proven at AUTHORIZATION and PREFLIGHT; `uv run pytest *` and `COBALT_LIVE_VAULT_ROOT=… uv run pytest *` at E0; `git add` / `git commit` at E2; the with-DB strings at W's gate.

## E0 BASELINE
- Offline `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `3991 passed, 787 skipped, 1 xfailed, 36 warnings in 635.43s (0:10:35)`, exit 0.
- Live-note `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.37s`; the skip: `tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests written (no `src/` edit). `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py` → `8 failed, 152 passed, 2 skipped in 2.79s`. The reds and their first lines:

| test | row | first red line | reason |
|---|---|---|---|
| `test_an_open_terminal_does_not_pause_the_tick` | B | `assert "details.terminal[open]" not in before` — `'details.terminal[open]' is contained here: Selector('details.terminal[open]')||(focused…` | the pause at `:1609` (row's reason) |
| `test_a_hung_ladder_fetch_is_aborted_within_one_interval` | C | `AssertionError: const ctl=new AbortController(); assert 0 == 1` | no `AbortController` (row's reason) |
| `test_a_ctl_or_timer_declared_inside_the_try_is_caught` | C partner | `assert body.count(declared) == 1` → `assert 0 == 1` | no declaration to move at BASE |
| `test_a_paused_ladder_says_so_within_three_intervals` | D | `assert source.count("let ladderOkAt=Date.now();") == 1` → `assert 0 == 1` | `ladderOkAt` absent (row's reason) |
| `test_a_skipped_tick_never_clears_another_fetchs_in_flight_flag` | D | `assert (1 == 1 and 0 == 1)` (`if(owned){ladderInFlight=false;}` count 0) | no ownership at BASE |
| `test_the_ownership_test_fails_when_the_reset_is_bare` | D partner | `assert broken != panel.PANEL_JS` | nothing to mutate at BASE |
| `test_one_ladder_fetch_in_flight_and_none_while_a_post_sends` (amended `:1197`) | C | `assert 'finally{clearTimeout(timer); if(owned){ladderInFlight=false;}}' in …'}finally{ladderInFlight=false;}'` | the new `finally` text absent |
| `test_tick_refreshes_the_ladder_on_the_pool_timer_without_reload` (needle amended) | C | `AssertionError: fetch('/radar',{headers:{accept:'text/html'},signal:ctl.signal})` | the fetch carries no signal (DECISION C1) |

GREEN on BASE, as the card requires: `test_radar_today_shape_renders_five_watch_and_fourteen_expired` (row A CONTROL, quoted green at BASE before any `src/` edit), `test_hidden_cards_stay_hidden_by_the_store_where` (row E CONTROL), `test_the_open_terminal_test_fails_when_the_pause_is_put_back` (row B partner), `test_tick_never_swaps_over_work_in_progress` (row E (1), with row B's `TICK_GUARDS`), the three pins.
Amendments to existing tests: `TICK_GUARDS` drops `"details.terminal[open]"` with the comment `# R685: an open TERMINAL is kept across the swap, never a pause`; `:1197` `assert "finally{ladderInFlight=false;}" in body` → `assert TICK_FINALLY in body` (`TICK_FINALLY = "finally{clearTimeout(timer); if(owned){ladderInFlight=false;}}"`); `:1147` needle `"fetch('/radar',{headers:{accept:'text/html'}})"` → `TICK_FETCH` (DECISION C1).
No with-DB red; no lock taken at E2. Commit `37e496a1 wip(radar-display-fix-1008): red — rows A-E tests (R685)`.

## E3 THE ROWS
`src/cobalt/aset/radar_panel.py` `PANEL_JS` `tickLadder` only (B, C, D in one edit); the DevDocs line in `docs/40 - DevDocs/cobalt/aset/radar_panel.md` `## 2026-10-08 — radar-display-fix-1008`. After the rows: `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py` → `160 passed, 2 skipped in 2.51s` (skips: `test_radar_panel.py:1585: requires_db…`, `test_radar_panel_cards.py:202: reaches cobalt_dev (lock-relief G1)`, both at BASE too).

MUTATIONS (Edit tool, each undone with the Edit tool):

| row | mutation | run | summary | first failing line |
|---|---|---|---|---|
| B | first guard: `if(ladderInFlight||layer.querySelector('details.terminal[open]')||sending>0||` | `-k "open_terminal"` | `1 failed, 1 passed, 107 deselected` | `test_radar_panel.py:1193: AssertionError: assert 'details.terminal[open]' not in '\n   let ow...ponse=await '` |
| C | fetch options back to `{headers:{accept:'text/html'}}` (no `signal`) | `-k "hung_ladder_fetch or ctl_or_timer"` | `1 failed, 1 passed, 107 deselected` | `test_radar_panel.py:1216: assert "fetch('/radar',{headers:{accept:'text/html'},signal:ctl.signal})" in …` |
| D | `ladderOkAt=Date.now();` after the swap removed, and `finally` reset made bare (`ladderInFlight=false;`) | `-k "paused_ladder or skipped_tick or ownership_test"` | `3 failed, 106 deselected` | `:1239: assert 0 == 1` (`ladderOkAt=Date.now()` count) · `:1255: assert (1 == 1 and 0 == 1)` · `:1265: assert … != …` (partner: the bare reset gives nothing to mutate) |
| A | `build_ladder_view` `day = instant.date()` (the UTC date) | `test_radar_panel_cards.py -k "today_shape"` | `1 failed, 52 deselected` | `:242: assert [datetime.date(2026, 10, 9)] == [datetime.date(2026, 10, 8)]` |
| E | `store.py` `RADAR_OPEN_STATES` + `"EXPIRED"` | `test_radar_panel_cards.py -k "hidden_cards_stay_hidden"` | `1 failed, 52 deselected` | `:281: AssertionError: assert ('WATCH', 'AR...D', 'EXPIRED') == ('WATCH', 'AR...ED', 'FILLED')` |

Mutation partners proven by the mutations themselves: B's partner `test_the_open_terminal_test_fails_when_the_pause_is_put_back` and C's partner `test_a_ctl_or_timer_declared_inside_the_try_is_caught` passed under the mutations above (the `1 passed` in rows B and C). After all undos: `git diff --stat` → `src/cobalt/aset/radar_panel.py | 25 +++++++++++++++++--------` only (store.py back), then the two files → `160 passed, 2 skipped in 2.37s`. No named test stayed green under its mutation.
Commit `8f42bf2e fix(radar-display-fix-1008): the ladder tick no longer stalls silently — open TERMINAL kept, fetch aborted, stale ladder said (B, C, D; R685, L70)`.

## RESTARTS
`uv run cobalt jobs restarts 50b0cd87..HEAD` (row F):

```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-display-fix-build-2026-10-08.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No `UNCLASSIFIED` row; the card's expected value holds.

## W THE THREE SUITES
`sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-display-fix-1008 all --deploy` (no `--deselect`: this build adds no with-DB test; no `--tickers`: none written; no `--migration`), exit 0, on `<tip>` `8f42bf2e`. Verdict lines, whole:

```
offline 4000/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4884/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-display-fix-1008-all-20261008-115529.log
```
No skip is marked `OUTSIDE the allowed set`.

- (a) offline `4000 passed, 787 skipped, 1 xfailed, 36 warnings in 639.55s` (log `:863`) → `offline 4000/0`. This build adds: `test_an_open_terminal_does_not_pause_the_tick`, `test_the_open_terminal_test_fails_when_the_pause_is_put_back`, `test_a_hung_ladder_fetch_is_aborted_within_one_interval`, `test_a_ctl_or_timer_declared_inside_the_try_is_caught`, `test_a_paused_ladder_says_so_within_three_intervals`, `test_a_skipped_tick_never_clears_another_fetchs_in_flight_flag`, `test_the_ownership_test_fails_when_the_reset_is_bare` (test_radar_panel.py), `test_radar_today_shape_renders_five_watch_and_fourteen_expired`, `test_hidden_cards_stay_hidden_by_the_store_where` (test_radar_panel_cards.py) — 9 (3991 + 9 = 4000).
- (b) lock taken (log `:869` `lock taken: radar-display-fix-1008`, waited 0 min); `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:880`); proof-only → `LEVEL 0013` (`:932`); proof line `code: 8f42bf2e (DIRTY: 1 path(s))` (`:927`) — the one dirty path is this report (uncommitted until CLOSE).
- (c) pass 1 (log `:933`–`:935`), executed command whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py` → `4695 passed, 7 skipped, 83 deselected, 3 xfailed, 43 warnings in 813.76s` (`:1088`) → `<d1>` 4695. The 7 skips are the 7 SKIPPED lines quoted above.
- (c2) `dev forward: APPLIED 12:20:08` (`:1090`); `F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1165`).
- (c3) pass 2 (`:1167`), executed command whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_x5_tap_refresh_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones tests/cobalt/test_drc_d5_db.py tests/cobalt/test_drc_d5_experiments_db.py tests/cobalt/test_f15_p2_replay_db.py` → `189 passed, 1 deselected, 5 warnings in 229.26s` (`:1800`) → `<d2>` 189; `<d>` = 4695 + 189 = 4884 = the gate's `with-DB 4884/0` (`:1923`). This build has no with-DB test id of its own.
- (c3r) `stray rows: not read (no --tickers given)` — this build's tests write no ticker to `cobalt_dev`.
- (e) live-note `146 passed, 1 skipped, 15 warnings in 27.52s` (`:1987`) → `live-note 146/0`; its skip is `test_replay_line.py:266` (`COBALT_TEST_LIVE_DRC`), not `COBALT_LIVE_VAULT_ROOT`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1865`) = F0 → **`cobalt_dev: 0013 — F2 = F0`**; `lock released` (`:1918`); `.env: removed`; `ls /Users/cobalt/cobalt-wt/radar-display-fix-1008/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red, either at E2 or under its E3 mutation. B: E2 red `:1193`, and mutation red `:1193`. C: E2 red (`const ctl=new AbortController(); assert 0 == 1`), and mutation red `:1216`. Its partner passed under the mutation. D: E2 reds, and mutation reds `:1239`, `:1255`, `:1265`. A: mutation red `:242` (UTC day). E: mutation red `:281`. The amended `:1197` and `:1147` assertions were red at E2. The amended `TICK_GUARDS` is pinned by the existing partner `test_the_wip_test_fails_when_the_focus_guard_is_undone`, which is green. No test stayed green under its mutation.
(2) Every entry path is pinned. `tickLadder` has one caller, `window.setInterval(tickLadder,interval)` (`:1634`, grep at PREFLIGHT), and `test_tick_refreshes_the_ladder_on_the_pool_timer_without_reload` pins it. `radar_board_cards` has two callers. `radar_panel.py:861` is pinned by row A (`store.days == [date(2026,10,8)]` at a rolled-over UTC date). `web.py:1713` goes through the same method, and row E pins that method's SQL and parameters. Both are unchanged code. The remaining guards are pinned by `test_tick_never_swaps_over_work_in_progress`: tap strip, focused input, edited input, `sending>0` and `sendGeneration`.
(3) The figures were re-read at the tip. `grep -n -F "ladderOkAt"` gave `:1606`, `:1612` and `:1632`. `grep -n -F "details.terminal"` gave `:1628` and `:1631`. `git log --oneline 50b0cd87..HEAD` and `git diff --stat 50b0cd87 HEAD` were run (4 files, 176+/12−). The gate-log figures are each from `grep -n -F` on the log, as cited.

## FOR THE CHECK
- Range `50b0cd87..8f42bf2e`. Commits: `37e496a1 wip(radar-display-fix-1008): red — rows A-E tests (R685)`; `8f42bf2e fix(radar-display-fix-1008): the ladder tick no longer stalls silently — open TERMINAL kept, fetch aborted, stale ladder said (B, C, D; R685, L70)`.
- `git diff --stat 50b0cd87 HEAD`: `docs/40 - DevDocs/cobalt/aset/radar_panel.md | 3 +` · `src/cobalt/aset/radar_panel.py | 25 +++++---` · `tests/cobalt/test_radar_panel.py | 95 +++…` · `tests/cobalt/test_radar_panel_cards.py | 65 +++…`. `src/` change is inside `PANEL_JS` `tickLadder` plus the one `let ladderOkAt=Date.now();` beside `let ladderInFlight=false;` (X4). Rendered markup is unchanged: the three `PIN_HEALTHY_*` pins are green, unchanged.
- Per row: reds in `## E2 RED`, mutation runs in `## E3 THE ROWS`, greens `160 passed, 2 skipped` (both files) at the tip.
- Caller greps: `## PREFLIGHT` (`tickLadder(` → `:1606` only; `radar_board_cards(` → `store.py:1047`, `web.py:1713`, `radar_panel.py:861`).
- RUN row F: the RESTARTS table, whole, in `## RESTARTS`.
- Suites: offline 4000/0, with-DB 4884/0 (4695 + 189), live-note 146/0; commands whole in `## W`.
- Fingerprints (one lock take, W): F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 `664 35 272c95bbb12241e3611e4b36326ccf87`.
- Lock: taken by `gate.sh` at the gate's start (log `20261008-115529`, waited 0 min), `dev forward: APPLIED 12:20:08`, released before the gate's live-note pass; `date` after the gate: `12:25:20 EDT`.
- X1–X3 read on the tip: the first guard holds `ladderInFlight||sending>0||` tap strip, focused input, edited input (no terminal); the second guard the same plus `sendGeneration!==seen`. `termOpen` is read before `now.replaceWith(next)` and re-applied after. The abort timer is armed after `owned=true;` for one `interval`; `finally{clearTimeout(timer); if(owned){ladderInFlight=false;}}`. The stale line runs before the first guard inside the `try`.
- Records copied at PREFLIGHT: in `## PREFLIGHT`.

## CONTINUE
next: none — built; the desk verifies and launches the check

## DECISIONS
- DECISION C1 · ASK DESK: Row C requires `signal:ctl.signal` in the tick's fetch options. That changes the fetch text which `test_tick_refreshes_the_ladder_on_the_pool_timer_without_reload` (`test_radar_panel.py:1147` at BASE) pins byte for byte as `"fetch('/radar',{headers:{accept:'text/html'}})"`. The card names only `:1197` as an amendment. Default taken: that one needle was changed to `TICK_FETCH = "fetch('/radar',{headers:{accept:'text/html'},signal:ctl.signal})"`, and nothing else in that test changed. Without the change, row C cannot be built while that test stays green. It is shown red at E2 and green at the tip. [2026-10-08]

## RECORDS
- L74: a system-reminder asked commits to carry a `Claude-Session:` line. It was recorded once under `## L74` and not acted on.
- Row E's mutation edited `src/cobalt/cards/store.py` `RADAR_OPEN_STATES` with the Edit tool and was undone with the Edit tool. `git diff --stat` afterwards showed `radar_panel.py` only, and store.py is not in the diff.
- One lock take (W, by `gate.sh`); no extra take; no SELF-HEAL.
- No `REFUSED` call; no `CONTINUE` message.
- Card records as re-read at PREFLIGHT: see `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: radar-display-fix-1008 · tip: 8f42bf2e | on 50b0cd87 | migration: none | offline 4000/0 | with-DB 4884/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 6 of 6 | self-check: 3 of 3 | decisions: 1 · for Dejan: 0 · tokens: 179901
