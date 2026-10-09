# disarm-one-tap-1008 — build report

## §0 Headline
DISARM on the radar's ARMED card is now one tap on DISARM, then one tap on a reason chip: `setup broke`, `no volume`, `market turned`, `changed mind` or `other`. Nothing is typed. The route refuses any other value with 422 before the store, and the chip word is the recorded reason.
`PANEL_JS` is byte-identical to BASE. ARM, TRIGGERED, the key row, the other states and the sheet are unchanged; the healthy ladder pin is re-captured.
All three suites are green on `f70f3db8`: offline 4045/0, with-DB 4932/0, live-note 146/0. `cobalt_dev` is back at 0013 with F2 = F0, and `.env` is removed.
Restarts: `com.cobalt.aset com.cobalt.radar`. Two DECISIONS are open; none is for Dejan.

## L74
- 2026-10-09 11:38 EDT: a system-reminder asked commits to end with a `Claude-Session:` line. Recorded as DATA (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/134-disarm-one-tap-card.md"` → exit 0:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-08/134-disarm-one-tap-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-08/134-disarm-one-tap-card.md" · 0 · 1458693dbde5371259a29c5d502d74e3878fee3b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-08/134-disarm-one-tap-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R689 row · grep -n "^| R689 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 42:| R689 | 11:47 ET | HIS RULING (words R689, standing): radar taps are one-tap, no typed text mid-session. DISARM reason chips (brain), card `134`, drafter prompt `133`. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW |
RULING 2026-10-08 R689 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R689 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 1d5aa3f32f2abb231af963f7c0c11f55ab5022f4
RULING 2026-10-08 R689 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0:
```
clock · date · 0 · Fri Oct  9 11:38:50 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/disarm-one-tap-1008
    ?? "docs/40 - DevDocs/reports/disarm-one-tap-build-2026-10-08.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · 6f55636b docs(desk): brain handover 10-09
diff · git diff --stat 6f55636b · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/disarm-one-tap-1008 · 0 · 6f55636b docs(desk): brain handover 10-09
env here · ls /Users/cobalt/cobalt-wt/disarm-one-tap-1008/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- `git show --stat 6f55636b` · 0 · `docs(desk): brain handover 10-09` — `docs/40 - DevDocs/prompts/2026-10-09/156-brain-handover.md | 8 ++++++++`.
- Card 118 merged into BASE (`git log --oneline -12 -- src/cobalt/aset/radar_panel.py` · 0 · top: `8f42bf2e fix(radar-display-fix-1008): the ladder tick no longer stalls silently …`, then `0544f91d feat(radar-arm-disarm) …`). Line numbers moved from the card's drafting HEAD `1d5aa3f3`; re-read below (the card's D allows it).
- SYMBOLS (`grep -n -E` over `src/cobalt/aset/radar_panel.py`) · 0:
  `1116:def _dot_html` · `1129: data-dot-toggle="1"` · `1139: <div class="tap-strip" data-card-id=… data-factor=… hidden>` · `1178:#: R627: the ARM and DISARM taps…` · `1179:ARM_BUTTON` · `1180:DISARM_TAP = (` · `1182: '<button class="arm-key danger">DISARM</button>'` · `1190:def _hidden_input` · `1201:def _card_form` · `1214: data-card-tap="1"` · `1425: _card_form(card.id, '/arm', ARM_BUTTON, …)` · `1434: # R627: ARMED -> WATCH, his tap with a reason the store requires.` · `1435: _card_form(card.id, '/disarm', DISARM_TAP, source='panel')` · `1521:PANEL_CSS` · `1523: … .tap-strip[hidden]{display:none} …` · `1532:.s3-form button.arm-key{min-height:44px;padding:0 14px}` · `1536:PANEL_JS` · `1575:   const dot=target.closest('[data-dot-toggle]');` · `1576: if(dot){const tray=dot.parentElement.querySelector('.tap-strip'); …` · `1577: const grade=target.closest('.tap-strip [data-grade]');` · `1584: if(tap){const block=tap.closest('[data-card-tap]'); … querySelectorAll('input[name]') …` · `1614: if(ladderInFlight||sending>0||layer.querySelector('.tap-strip:not([hidden])')…` · `1626: if(sending>0||sendGeneration!==seen||now.querySelector('.tap-strip:not([hidden])')…` (card's `:1609` / `:1620` → `:1614` / `:1626`).
  `web.py` · 0: `75:from .radar_panel import (` · `174: function askReason(btn, label){` · `713: onclick="return askReason(…)` · `1672:class _TapInputRefused(ValueError):` · `1775:async def _card_tap` · `1788: except (_TapInputRefused, SizingError) as e:` · `2007:@app.post("/radar/card/{card_id}/arm")` · `2020:@app.post("/radar/card/{card_id}/disarm")` · `2021:async def radar_card_disarm` · `2027: raise _TapInputRefused(`.
  `cards/store.py` · 0: `384:    def _assert_reason(`.
  Tests (re-read): `test_s3_c3_panel_offline.py` `GatedCards` `:102`–`:118`, R627 block `:210`–`:295`, market reset `:459`–`:471`; `test_radar_panel_cards.py` pins `:475`–`:482` (LADDER `:481`), `_page` `:525`, pin test `:579`–`:593`, `_ladder_articles` `:785`, R627 block `:943`–`:1035`, `ARM_KEY_CSS` `:947`, `ARM_TAP` `:948`, `DISARM_TAP` `:952`–`:956`, BASE hashes `:957`–`:961`, render test `:971`–`:993`, unchanged test `:1000`–`:1014`, sheet test `:1022`–`:1035`, allowlist `:1064`–`:1078`; `test_radar_panel.py:1113` `TICK_GUARDS`.
- CALLERS: `grep -rn -F "DISARM_TAP" src` · 0 · `radar_panel.py:1180`, `:1435` (one user). `grep -rn -F "/disarm" src` · 0 · `web.py:2020`, `radar_panel.py:1435`. `grep -rn -F "_assert_reason(" src` · 0 · `store.py:321` (in `transition`), `:384` (def).
- `wc -l` · 0 · `radar_panel.py` 1700 · `web.py` 2260 · `test_s3_c3_panel_offline.py` 773 · `test_radar_panel_cards.py` 1138.
- `## READ` names no report (the one doc is card 92's prompt); no `tail` owed.
- `uv run cobalt jobs restarts 6f55636b..HEAD` · 0 · range empty of commits; the tool lists the untracked report only: `docs/40 - DevDocs/reports/disarm-one-tap-build-2026-10-08.md	A	DOCS	-` / `RESTARTS: none`.
- Card `## RECORDS` copied: (1) the other radar taps ask for no text; (2) nothing reads the disarm reason back today; (3) the tray seam (`PANEL_JS` toggle / grade / tap / tick guards; dot-tray tests match `class="tap-strip" data-card-id=` exact — re-read: `test_radar_panel_cards.py:371`, `:377`); (4) RESTARTS expected `com.cobalt.aset com.cobalt.radar`; (5) DB: no schema change, every new test offline; the card has no `DB` key; (6) ORDER: 118 first — re-read: merged (`8f42bf2e` on BASE); (7) BASE at drafting `1d5aa3f3`, now refilled to `6f55636b`.

## E0 BASELINE
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` (background) · exit 0 · `4036 passed, 790 skipped, 1 xfailed, 36 warnings in 657.78s (0:10:57)` — 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · exit 0 · `146 passed, 1 skipped, 15 warnings in 29.57s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests only, committed `0d9d4f4a wip(disarm-one-tap-1008): red — DISARM chips route, render, tray seam and controls (A-D, R689)`. No with-DB red, so no lock was taken at E2.
- BASE CAPTURE first (rows C, D): the two controls ran on BASE with empty hash constants and printed BASE's values. `uv run pytest … test_radar_panel_cards.py -k "ride_the_existing_tray or leave_arm_and_triggered"` · 1 · `AssertionError: 326400594ef47fdd85fc8d130e75ec2aaaff6558b37204a4873dc9059ff2e67a` (`:1036`, `PANEL_JS`) · `AssertionError: f91f7966b24284029c58e8415491d5a526673efdc5eff26dba9cc9e33099b846` ×2 (`:1066`, the ARMED `/triggered` block, both frames, the same) · `3 failed, 54 deselected`. Pinned as `BASE_PANEL_JS_SHA256` and `BASE_ARMED_TRIGGERED_TAP_SHA256`.
- Row A: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_s3_c3_panel_offline.py` · 2 · `E   AttributeError: module 'cobalt.aset.radar_panel' has no attribute 'DISARM_REASONS'` (collecting `test_s3_c3_panel_offline.py`), `1 error`. This is the row's named red. The second test's own red (409 / 200 on BASE's route) is hidden behind the collection error, so it is shown under mutation A1 (E3).
- Rows B–D: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_radar_panel_cards.py` · 1 · `2 failed, 54 passed, 1 skipped`. Both reds are `test_radar_arm_and_disarm_taps_render_on_watch_and_armed_only` (both frames): `E   assert 0 == 1` … `.count('data-dot-toggle="disarm"')` (`:996`), the row's named red. REWRITTEN once: the first draft asserted `panel.DISARM_REASONS == DISARM_CHIPS` first and went red on `AttributeError` instead; the assert was moved after the toggle count. C (`test_the_disarm_chips_ride_the_existing_tray_and_tap_paths`) and D (`test_disarm_chips_leave_arm_and_triggered_unchanged`, both frames) are GREEN on BASE. The pin test is GREEN on BASE.
- The skip is pre-existing: `SKIPPED [1] tests/cobalt/test_radar_panel_cards.py:202: reaches cobalt_dev (lock-relief G1)`.

## E3 THE ROWS
Commit `f70f3db8 feat(disarm-one-tap-1008): DISARM is one tap on a reason chip; the route refuses any value off the list (A, B, C, D; R689, L1, L3, L72)`. It holds `radar_panel.py`, `web.py`, `test_radar_panel_cards.py` (the re-pin) and the two DevDocs lines (`docs/40 - DevDocs/cobalt/aset/radar_panel.md`, `web.md`, `## 2026-10-08 — disarm-one-tap-1008`).
- A: `DISARM_REASONS` next to `ARM_BUTTON`, with the card's comment line; `web.py` imports it; `radar_card_disarm` refuses `reason not in DISARM_REASONS` with the card's message, passes `reason=reason`, and drops the 80-character check; the docstring is updated. `uv run pytest … test_s3_c3_panel_offline.py` · 0 · `50 passed, 9 skipped` (9 pre-existing `reaches cobalt_dev (lock-relief G1)` skips at `:175`, `:185`, `:301`, `:324`, `:334`, `:344`, `:353`, `:370`, `:378`).
- B: `DISARM_TAP` → `_disarm_chips(card_id)`; the ARMED block calls it, with the card's comment; one CSS line after the `arm-key` line. `uv run pytest … test_radar_panel_cards.py test_s3_c3_panel_offline.py test_radar_panel.py` · 1 · `2 failed, 214 passed, 11 skipped`: only `test_bars_stale_badge_absent_and_output_unchanged_when_healthy` [both frames] `AssertionError: 1866a7ad92de42fd7552f5e7b39673b3c95060cd5570250e3492695dff92c427` (`:593`), the pin red row D names.
- D (pin): `PIN_HEALTHY_LADDER_SHA256` `9a52577cbe07733c1f933857e2ed14d531a12a911c64bd899be3b48a0e16ff15` → `1866a7ad92de42fd7552f5e7b39673b3c95060cd5570250e3492695dff92c427`, with the card's comment line under the last LADDER comment. POOL and API pins are unchanged.
- After all rows: `uv run pytest … test_radar_panel_cards.py test_s3_c3_panel_offline.py test_radar_panel.py test_aset_web.py` · 0 · `238 passed, 40 skipped` (every skip is pre-existing: `reaches cobalt_dev (lock-relief G1)` or `requires_db`).
- MUTATIONS (Edit tool, each undone; after the last, `git diff 0d9d4f4a -- src` showed the fix only, with `PANEL_JS` untouched):
  - A1 `if False and reason not in DISARM_REASONS:` → `-k disarm` · 1 · `5 failed, 8 passed`: all five `test_a_disarm_reason_off_the_list_is_refused[data0..4]`. First lines: `E   AssertionError: {"status":"REFUSED","reason":"REFUSED ARMED -> WATCH: a reason is required. …"}` / `assert 409 == 422` (`{}`, `"   "`), and `E   AssertionError: {"status":"ok","card_id":1,"state":"WATCH","transition_id":77}` / `assert 200 == 422` (the other three). These are BASE's behaviours, as the card names them.
  - A2 `reason="other"` in place of `reason=reason` → · 1 · `4 failed, 9 passed`: `test_each_disarm_chip_moves_the_card_to_watch[setup broke|no volume|market turned|changed mind]`, `E   AssertionError: assert ['other'] == ['setup broke']`. The `[other]` param stays green by construction (the mutant's word is that chip).
  - B1 `data-x-toggle="disarm"` → `-k disarm` · 1 · `2 failed`: the render test, both frames, `E   assert 0 == 1` … `count('data-dot-toggle="disarm"')`.
  - B2 the chip button gets `data-grade="1"` → · 1 · `2 failed`: the render test, both frames, `At index 0 diff: … class="arm-key danger" data-grade="1">setup broke</button>') != …` (`:1000`).
  - B3 the CSS line removed → · 1 · `2 failed`: the render test, both frames, `E   IndexError: list index out of range` (`:1028`, nothing after `ARM_KEY_CSS`).
  - C1 `PANEL_JS` toggle `dot.closest('.dot-cell')` in place of `dot.parentElement` → `-k ride_the_existing_tray` · 1 · `1 failed`: `E   AssertionError: e353bb611bf4fa67b42da5a8c23812c199fe858bd44fcf263342dee9eac6a676` (`:1036`, ≠ BASE `326400594e…`).
  - D1 `TRIGGERED_BUTTON = '<button class="arm-key">TRIGGERED</button>'` → `-k leave_arm_and_triggered` · 1 · `2 failed`: both frames, `E   AssertionError: 7dbf496cefb46bb9b6de54aa26edf172e1be7a2cef250feca674dc26895625cb` (`:1066`, ≠ BASE `f91f7966…`).
  - Re-run after the undo · 0 · `238 passed, 40 skipped`.

## RESTARTS
Row E (RUN): `uv run cobalt jobs restarts 6f55636b..HEAD` · 0:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/cobalt/aset/web.md	M	DOCS	-
docs/40 - DevDocs/reports/disarm-one-tap-build-2026-10-08.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
src/cobalt/aset/web.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No UNCLASSIFIED row. It matches the card's expected `com.cobalt.aset com.cobalt.radar`.

## W THE THREE SUITES
`<tip>` = `f70f3db8`. ONE call: `sh /Users/cobalt/cobalt/ops/desk/gate.sh disarm-one-tap-1008 all --deploy` (background) · exit 0. No `--deselect`, because this build adds no with-DB test. No `--tickers`, because no test of this build writes a ticker. No `--migration`. The verdict lines, WHOLE:
```
offline 4045/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4932/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/disarm-one-tap-1008-all-20261009-115424.log
```
- (a) offline: log `:867` `4045 passed, 790 skipped, 1 xfailed, 36 warnings in 661.98s (0:11:01)` → `offline 4045/0`. This build adds `test_each_disarm_chip_moves_the_card_to_watch` [×5], `test_a_disarm_reason_off_the_list_is_refused` [×5], `test_the_disarm_chips_ride_the_existing_tray_and_tap_paths` and `test_disarm_chips_leave_arm_and_triggered_unchanged` [×2]. It deletes three R627 disarm tests (1 + 1 + 1 params = 4 ids). Net +9 against E0's 4036: 4036 + 13 − 4 = 4045.
- (b) lock: `:873` `lock taken: disarm-one-tap-1008`; `:878` `ls -la /Users/cobalt/cobalt-wt/*/.env` → this worktree's only. `<F0>` `:884` `F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; `LEVEL 0013`.
- (c) PASS 1, executed (`:939`), WHOLE: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py` → `:1092` `4737 passed, 7 skipped, 89 deselected, 3 xfailed, 43 warnings in 820.01s (0:13:40)` → `<d1>` = 4737. The seven SKIPPED lines are quoted above. None is marked `OUTSIDE the allowed set` (`grep -n -F "OUTSIDE" <log>` · 1 · nothing).
- (c2) `:1094` **`dev forward: APPLIED 12:19:34`**; `<F1>` `:1170` `F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) PASS 2: `:1898` `195 passed, 1 deselected, 5 warnings in 228.05s (0:03:48)` → `<d2>` = 195. This build has no with-DB test id of its own. `<d>` = 4737 + 195 = 4932 = `with-DB 4932/0`.
- (c3r) `stray rows: not read (no --tickers given)`: no test of this build writes a ticker.
- (f) `<F2>` `:1964` `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = `<F0>` field for field → **`cobalt_dev: 0013 — F2 = F0`** (`:2015`). `:2017` `lock released`; `:2020` `No such file or directory`; `.env: removed`. My own `ls /Users/cobalt/cobalt-wt/disarm-one-tap-1008/.env` · 1 · `No such file or directory`.
- (e) live-note: `:2086` `146 passed, 1 skipped, 15 warnings in 26.51s` → `live-note 146/0`. Its skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- The proof-only line `:2011` `code: f70f3db8 (DIRTY: 1 path(s))`: the one path is this report, uncommitted until CLOSE.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason. `test_each_disarm_chip_moves_the_card_to_watch`: E2 collection `AttributeError … 'DISARM_REASONS'`, and E3 A2 `assert ['other'] == ['setup broke']` (4 of 5 params; `[other]` is green by construction, see DECISIONS). `test_a_disarm_reason_off_the_list_is_refused` [×5]: E3 A1, `assert 409 == 422` / `assert 200 == 422`, BASE's own answers. `test_radar_arm_and_disarm_taps_render_on_watch_and_armed_only` [×2]: E2 `assert 0 == 1` … `data-dot-toggle="disarm"`, and E3 B1, B2, B3. `test_the_disarm_chips_ride_the_existing_tray_and_tap_paths`: E3 C1 `AssertionError: e353bb61…`. `test_disarm_chips_leave_arm_and_triggered_unchanged` [×2]: E3 D1 `AssertionError: 7dbf496c…`. The pin test: E3 after row B, `AssertionError: 1866a7ad…`. Rewritten once: the render test (E2), so its red is the row's. The edge test and the market-reset param changed only their data (`"setup broke"`). Both stay green and test their own gates (edge 409, `inside MARKET RESET`), shown in the E3 runs and in the gate.
(2) Every entry path is pinned. The route `/disarm` (`web.py:2020`, the one `src` caller of the list check) has chips in, off-list values in (missing, blank, other text, over-long, case), the WATCH edge, market reset, `source=panel` (the evidence `via`) and the sheet source by `_card_tap` (unchanged). `_disarm_chips` has one caller, `radar_panel.py:1449` (`grep -rn -F "_disarm_chips(" src` · 0), pinned by the render test in both frames. The `DISARM_REASONS` users are `radar_panel.py:1181`, `:1192` and `web.py:76`, `:2027`, `:2029` (`grep -n -F` · 0), pinned by both offline tests. `DISARM_TAP` is gone from `src` and `tests` (`grep -rn -F "DISARM_TAP" src tests` · 1 · nothing). The sheet's DISARM (`askReason`) is pinned unchanged by `test_the_sheet_keeps_its_arm_and_disarm_buttons` (green in E3 and the gate).
(3) Re-read at the tip: the `grep -n -F` calls in (2); `git diff 0d9d4f4a -- src` (E3); `git diff --stat 6f55636b -- tests/cobalt/test_radar_panel.py tests/cobalt/test_aset_web.py src/cobalt/cards` · 0 · nothing (fenced files unchanged); every gate figure by `grep -n -F` / Read of the log at the line numbers cited.

## FOR THE CHECK
- Range `6f55636b..f70f3db8`: `0d9d4f4a wip(disarm-one-tap-1008): red — DISARM chips route, render, tray seam and controls (A-D, R689)` · `f70f3db8 feat(disarm-one-tap-1008): DISARM is one tap on a reason chip; the route refuses any value off the list (A, B, C, D; R689, L1, L3, L72)`. The report commit follows.
- Per-row reds, mutations and greens: `## E2 RED` and `## E3 THE ROWS` above (quoted). BASE captures: `PANEL_JS` `326400594ef47fdd85fc8d130e75ec2aaaff6558b37204a4873dc9059ff2e67a`; the ARMED `/triggered` block `f91f7966b24284029c58e8415491d5a526673efdc5eff26dba9cc9e33099b846`. LADDER pin `9a52577c…` → `1866a7ad92de42fd7552f5e7b39673b3c95060cd5570250e3492695dff92c427`.
- Caller greps: `## PREFLIGHT` CALLERS and PRE-STOP (2).
- RUN row E: `## RESTARTS` (whole).
- Suites: `## W` (executed pass-1 command whole). `<F0>` `664 35 272c95bbb12241e3611e4b36326ccf87` · `<F1>` `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` · `<F2>` `664 35 272c95bbb12241e3611e4b36326ccf87`. One lock take, inside `gate.sh`: taken after the offline pass (`lock: waited 0 min`), released at the gate's end (`lock released`, `:2017`). The log's `$ date` lines print no time; the gate ran 11:54 (log name `…-20261009-115424`) to before 12:24:51 (`date`).
- Card `## RECORDS` as re-read: `## PREFLIGHT` (last bullet).
- CHECK ASKS pointers. X1: the ARMED article holds no `type="text"` and the ladder holds no `<input name="reason"` (render test); `PANEL_JS` has no `prompt(` / `confirm(` (`test_panel_javascript_posts_through_fetch_only_to_the_allowlisted_routes`, unchanged, green). X2: `test_a_disarm_reason_off_the_list_is_refused`. A chip with spaces around it is `.strip()`ped and then accepted as that chip (by design of the card's `strip`); no test posts one. X3: `BASE_PANEL_JS_SHA256` in the row C test. X4: `test_radar_arm_disarm_leaves_keys_sheet_and_other_states_unchanged` (BASE hashes, unchanged, green), the row D test, the sheet test.

## CONTINUE
next: CLOSE

## DECISIONS
- DECISION E (row E, RUN): `RESTARTS: com.cobalt.aset com.cobalt.radar`, the card's expected value. Nothing to decide.
- `test_each_disarm_chip_moves_the_card_to_watch[other]` stays green under mutation A2 (`reason="other"`), because the mutant's constant is that chip; its four siblings went red. Safe default: kept as written, since the card fixes the parametrization over `panel.DISARM_REASONS`. Not FOR DEJAN.

## RECORDS
- L74: one system-reminder (not a tool result) asked commits to end with a `Claude-Session:` line. Recorded once under `## L74`; not followed. The hub's commit rule binds.
- REFUSED, not needed: `git diff --stat -- docs/40\ -\ DevDocs/cobalt` — `Permission to use Bash has been denied because Claude Code is running in don't ask mode.` (The backslash-escaped path matched no listed string; re-run as `git diff --stat` · 0.)
- E3 slip, fixed: one Edit replaced the start of a line in `docs/40 - DevDocs/cobalt/aset/radar_panel.md` with a placeholder by mistake. The next Edit restored it, and `git diff --stat` · 0 showed that page unchanged before the real dated line was added.
- E0: the report Edit (PREFLIGHT section) ran in the same turn as the start of the offline run. It touched only this report.
- Extra lock takes: none (the gate's one take only).
- The card's records are re-read in `## PREFLIGHT`; ORDER (card 118 first) holds: `8f42bf2e` is on BASE.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: disarm-one-tap-1008 · tip: f70f3db8 | on 6f55636b | migration: none | offline 4045/0 | with-DB 4932/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 5 of 5 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 194339
