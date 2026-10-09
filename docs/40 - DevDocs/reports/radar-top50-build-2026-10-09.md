# radar-top50-1009 — build report (2026-10-09)

## §0 Headline
Built on `1ad357a3`. The `/radar` pool view now lists at most `cap` names under `Current admitted`. Open admitted episodes ranked past `cap` render in their own `Over cap — open admitted beyond cap` section, and the `members / cap` header still shows `51 / 50`.
First run (11:38 ET) stopped at AUTHORIZATION: R716 was rejected. After the desk's `CONTINUE` (card `RULINGS` → R685) it ran `AUTHORIZED`.
Suites: offline 4038/0, with-DB 4925/0, live-note 146/0. `cobalt_dev` is back at 0013 (F2 = F0) and `.env` is removed. RESTARTS: `com.cobalt.aset com.cobalt.radar`.
3 decisions, 1 for Dejan (the RULINGS swap).

## L74
A system notice in this session asked that commits also carry a `Claude-Session:` line. Recorded here once. It was not followed: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/154-radar-top50-card.md"` → exit 1. Output whole:

```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/154-radar-top50-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/154-radar-top50-card.md" · 0 · 1458693dbde5371259a29c5d502d74e3878fee3b
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/154-radar-top50-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-09 R716 row · grep -n "^| R716 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · 9:| R716 | 07:08 ET | His backlog item via brain (L79): `/radar` top-50 shows 51 names; `pool.py:450-451` caps admitted, so the page draws a held or leaving member twice. Small display card; survey first, read-only. | APPROVED · HIS RULING |
RULING 2026-10-09 R716 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R716 |" -- "docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · 1458693dbde5371259a29c5d502d74e3878fee3b
RULING 2026-10-09 R716 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-09.md" · 0 · the row as grepped
  FAILED: authorization mismatch — RULING 2026-10-09 R716 row
```
(The last output line is indented by two spaces here so that no line but the stop line starts with `FAILED`, per L71.)

The script rejects the R716 row. That row's text is a backlog item relayed "via brain (L79)". Unlike the R60 row, it has no `**HIS RULING**` with a link to his words. Its status column reads `APPROVED · HIS RULING`, not `APPROVED`. Whether R716 counts as his ruling is for the desk and Dejan to decide, not the builder.

### Second run (after `CONTINUE: AUTHORIZATION`, 11:40 ET)
The card at `b155b95d` changes one line from `1458693d`: `RULINGS: 2026-10-09 R716` → `RULINGS: 2026-10-08 R685` (`git -C /Users/cobalt/cobalt diff 1458693d b155b95d -- <card>`). `authorize.sh` → exit 0. Changed rows quoted:

```
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/154-radar-top50-card.md" · 0 · b155b95d817024a801f381367b523f457028a110
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/154-radar-top50-card.md" · 0 · nothing
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```
The INSTALLED, PLACEHOLDER and R60 rows are the same as in the first run.

## PREFLIGHT
- `preflight.sh build <card>`, first call → `FAILED PREFLIGHT: status` (the uncommitted `RESUMED` line in this report). The report was committed (`aac3a4c2`) and the script run again, 11:41:12 ET:
```
clock · date · 0 · Fri Oct  9 11:41:12 EDT 2026
status · git status --short --branch · 0 · ## ops/radar-top50-1009
head · git log --oneline -1 · 0 · aac3a4c2 wip(radar-top50-1009): AUTHORIZATION — resumed, AUTHORIZED on R685
diff · git diff --stat 0e84db6f · 0 · (2 lines)
     .../reports/radar-top50-build-2026-10-09.md        | 63 ++++++++++++++++++++++
     1 file changed, 63 insertions(+)
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/radar-top50-1009 · 0 · aac3a4c2 wip(radar-top50-1009): AUTHORIZATION — resumed, AUTHORIZED on R685
env here · ls /Users/cobalt/cobalt-wt/radar-top50-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
- `git show --stat 0e84db6f` → `docs(desk): four drafter prompts: arm-unsized, radar-top50, https-only, guard D2`. It adds 4 files under `docs/40 - DevDocs/prompts/2026-10-09/` (31 insertions).
- Symbols (`grep -n`, `radar_panel.py`): `90:class PoolRecord`, `115:class MembershipRecord`, `165:class PoolRow`, `195:class PoolView`, `213: bars_stale_tickers: dict[str, str] = Field(default_factory=dict, exclude=True)`, `502:def _row(`, `532:def build_pool_view(`, `631: item for item in records if item.entered_at is not None and item.left_at is None`, `1008:def _pool_table(`, `1042:def render_pool(`, `1074:{_pool_table(view.current, "Current admitted", bars_stale=view.bars_stale_tickers)}`. `store.py`: `55: def members_for_day(`, `81: def apply_membership(`. `test_radar_panel.py`: `49:class FakeRadarStore:`, `96:def _small_snapshot():`, `128:def _build(`, `838:def test_pool_member_count_mismatch_fails_instead_of_rendering_empty():`. `test_radar_panel_cards.py`: `480:PIN_HEALTHY_POOL_SHA256 = "f2e79add…"`, `482:PIN_HEALTHY_API_SHA256 = "450b3415…"`.
- Callers: `grep -rn -F "build_pool_view(" src` → `radar_panel.py:532` (def), `radar_panel.py:955` (`build_radar_panel`). `grep -rn -F "render_pool(" src` → `radar_panel.py:1042` (def), `radar_panel.py:1656` (`render_radar_page`), `radar_panel.py:1665` (the API `html`). `voice/tools.py:147` and `voice/turn.py:336` are a different `render_pool(payload: dict)`.
- `wc -l`: `src/cobalt/aset/radar_panel.py` 1700, `tests/cobalt/test_radar_panel.py` 1638.
- The card's `## READ` names no report.
- Card records: RESTARTS expected `com.cobalt.aset com.cobalt.radar`. That is re-checked at RESTARTS from the tool's own output. The DB and BASE records are copied as written. The BASE record (`0e84db6f`) matches PREFLIGHT's diff base.
- `uv run cobalt jobs restarts 0e84db6f..HEAD` → only `docs/40 - DevDocs/reports/radar-top50-build-2026-10-09.md A DOCS -`, `RESTARTS: none` (the only path is this report).
- The with-DB strings are proven at W's first take (no with-DB red in this card).

## E0 BASELINE
On `0e84db6f` plus the report only (no `src/` or test change):
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4036 passed, 790 skipped, 1 xfailed, 36 warnings in 664.21s (0:11:04)`, exit 0.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.54s`. Its only skip is `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`, which does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Tests added in `tests/cobalt/test_radar_panel.py`, after `:838`: the helper `_open_admitted_copies`, `test_a_pool_over_cap_renders_cap_names_and_the_rest_in_their_own_section` (A) and `test_a_full_pool_renders_fifty_and_no_over_cap_section` (B). The tickers are constructed (`T1`…`T51`) and the ids are `10001`…`10051` (L32).
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py -k "over_cap or full_pool_renders_fifty"` on BASE code → `1 failed, 1 passed, 111 deselected in 0.54s`:
- A RED for the row's reason: `E       AssertionError: assert 51 == 50` at `test_radar_panel.py:864` (`len(view.pool.current) == 50`).
- B GREEN on BASE before any edit (the `.` in `F.`).
- Committed `d2f85749 wip(radar-top50-1009): red — over-cap pool test (A) and full-pool control (B)`. There is no with-DB red, so no lock was taken here.

## E3 THE ROWS
Row A (`src/cobalt/aset/radar_panel.py` at the tip):
- `:215` `over_cap: list[PoolRow] = Field(default_factory=list, exclude=True)`, beside `bars_stale_tickers` (`:213`).
- `:647` `current, over_cap = current[: pool.cap], current[pool.cap :]`, after the order at `:646`. The `members` check (`:635`) is unchanged.
- `:752` `over_cap=over_cap,` in the `PoolView(...)`.
- `:1072`–`:1076` and `:1083`: `render_pool` adds the `Over cap — open admitted beyond cap` table on the line after `Current admitted`, only when `view.over_cap` is non-empty and outside any `<details>`. The `<b>{view.members}</b> / {view.cap} admitted` header is unchanged.

The first run after the fix, `uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel.py tests/cobalt/test_radar_panel_cards.py`, gave `1 failed, 164 passed, 2 skipped`. The failure was `test_bars_stale_leaves_the_api_json_unchanged` (`test_radar_panel.py:586`): `Extra items in the right set: 'over_cap'`. That test asserts that the API payload's keys are `PoolView.model_fields` minus the excluded fields. The payload did not change: `over_cap` is excluded. The test's list of excluded fields gained `"over_cap"` (`:587`). See DECISIONS 1.
After that: `165 passed, 2 skipped in 2.51s`. Skips: `tests/cobalt/test_radar_panel.py:1647: requires_db` and `tests/cobalt/test_radar_panel_cards.py:202: reaches cobalt_dev (lock-relief G1)`. This run includes the pins `PIN_HEALTHY_POOL_SHA256` / `PIN_HEALTHY_API_SHA256` (`test_bars_stale_badge_absent_and_output_unchanged_when_healthy`) and `test_pool_member_count_mismatch_fails_instead_of_rendering_empty`, unchanged and green.

MUTATIONS. Each was made with Edit, run with `-k "over_cap or full_pool_renders_fifty" --tb=line`, then undone:
1. The fix undone (`current, over_cap = current, []`) → `1 failed, 1 passed`, `test_radar_panel.py:864: AssertionError: assert 51 == 50`.
2. The render undone (`{over_cap}` dropped from the template) → `1 failed, 1 passed`, `test_radar_panel.py:872: assert 'Over cap — open admitted beyond cap <span class="count">1</span>' in '<section id="pool-layer" …`.
3. B's control broken (`if view.over_cap` → `if True`) → `1 failed, 1 passed` (`.F`), `test_radar_panel.py:886: assert 'Over cap' not in '<section id...\n</section>'`.
After the undo, `git diff --stat` showed the fix only (`radar_panel.py | 11 +++++-`, `test_radar_panel.py | 2 +-`, plus this report), and the two files ran `165 passed, 2 skipped in 2.46s`.
DevDocs: `docs/40 - DevDocs/cobalt/aset/radar_panel.md` got `## 2026-10-09 — radar-top50-1009`.
Committed `1ad357a3 fix(radar-top50-1009): top-50 list holds at most cap names; the rest render as Over cap (A, B; L1, L28, L70)`.
Row C is the RESTARTS run below.

## RESTARTS
`uv run cobalt jobs restarts 0e84db6f..HEAD` (HEAD `1ad357a3`):
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-top50-build-2026-10-09.md	M	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
Nothing is UNCLASSIFIED. Row C: this matches the card's expected `com.cobalt.aset com.cobalt.radar`.

## W THE THREE SUITES
`sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-top50-1009 all --deploy` on `<tip>` = `1ad357a3`, exit 0. No `--deselect`, `--tickers` or `--migration`: this build adds no with-DB test and no migration. The gate log shows `code: 1ad357a3 (DIRTY: 1 path(s))` (log `:2011`). The dirty path is this report's uncommitted text. Verdict lines, whole:
```
offline 4038/0
lock: waited 18 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4925/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-top50-1009-all-20261009-115451.log
```
- (a) offline: `4038 passed, 790 skipped, 1 xfailed, 36 warnings in 662.63s` (log `:867`). That is 4036 at E0 plus the 2 tests this build adds (A, B).
- (b) `lock taken: radar-top50-1009` (log `:873`) after `lock: waited 18 min` (`:876`). `ls -la /Users/cobalt/cobalt-wt/*/.env` → only `/Users/cobalt/cobalt-wt/radar-top50-1009/.env` (`:878`). `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:884`). `LEVEL 0013` (`:936`).
- (c) pass 1, executed command (log `:939`), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py` → `4730 passed, 7 skipped, 89 deselected, 3 xfailed, 43 warnings in 761.31s` (`:1092`) = `<d1>` 4730. The 7 skips are the SKIPPED lines above. `grep -n -F "OUTSIDE" <log>` → nothing.
- (c2) `dev forward: APPLIED 12:37:03` (`:1094`). `F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1170`).
- (c3) pass 2, executed command (log `:1172`), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_tenancy.py::TestMigrationRoundTrip tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped tests/cobalt/test_legs_db.py tests/cobalt/test_fill_transaction_db.py tests/cobalt/test_legs_c2_db.py tests/cobalt/test_s3_c2_experiments.py tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk tests/cobalt/test_s3_c3_panel_db.py tests/cobalt/test_s3_c3_experiments.py -rA tests/cobalt/test_s3_c4_trade_note_db.py tests/cobalt/test_prefill_trade_note.py tests/cobalt/test_f15_p1_records_db.py tests/cobalt/test_x5_tap_refresh_db.py tests/cobalt/test_radar_cards_db.py tests/cobalt/test_rubberband_forms.py tests/cobalt/test_stale_score_db.py --deselect tests/cobalt/test_stale_score_db.py::test_r40_the_view_drops_pre_fix_stale_graded_taps_and_keeps_fresh_and_post_fix_ones tests/cobalt/test_drc_d5_db.py tests/cobalt/test_drc_d5_experiments_db.py tests/cobalt/test_f15_p2_replay_db.py tests/cobalt/test_radar_price_floor_db.py` → `195 passed, 1 deselected, 5 warnings in 237.04s` (`:1898`) = `<d2>` 195. 4730 + 195 = 4925 = `with-DB 4925/0`. This build has no with-DB test id of its own.
- (c3r) `stray rows: not read (no --tickers given)`: the new tests write no rows.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1964`) = F0. `cobalt_dev: 0013 — F2 = F0` (`:2015`). `lock released` (`:2017`). `.env: removed` (`:2021`). `ls /Users/cobalt/cobalt-wt/radar-top50-1009/.env` (mine, after the gate) → `No such file or directory`.
- (e) live-note: `146 passed, 1 skipped, 15 warnings in 28.73s` (`:2086`). The only skip is the `COBALT_TEST_LIVE_DRC` one, which does not name `COBALT_LIVE_VAULT_ROOT`.
- The log also holds `ERROR … REFUSED (… MARKET RESET …)` lines (e.g. `:1201`–`:1261`, `:1357`). They are logged refusals from tests that pin the MARKET RESET block, and the suites they ran in passed with 0 failed.

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown red for its named reason. A: red at E2 (`assert 51 == 50`, `:864`) and under mutations 1 and 2 (`:864`, `:872`). B: red under mutation 3 (`:886`, `'Over cap' not in`). The changed assertion at `:587` was red before its edit (`Extra items in the right set: 'over_cap'`). No test stayed green under its mutation.
(2) Entry paths. `build_pool_view` ← `build_radar_panel` (`radar_panel.py:955`), pinned by A and B (`_build` calls `panel.build_radar_panel`). `render_pool` is pinned by A and B directly. Its callers `render_radar_page` (`:1656`) and `pool_api_payload` (`:1665`, `"html": render_pool(view)`) embed the same string. With no over-cap rows they are pinned by the healthy pins (green). With over-cap rows no test reads them through the page or the API: DECISIONS 2. Edges: members == cap (B), members == cap + 1 (A), and members ≠ the open count (`:838`, still green). `voice/tools.py:147` is a different `render_pool`, outside this job.
(3) Re-read at the tip: `grep -n -F "over_cap" src/cobalt/aset/radar_panel.py` → `215, 647, 752, 1072, 1073, 1074, 1083`; `grep -n -F "def test_a_" tests/cobalt/test_radar_panel.py` → `859`, `877`; `grep -n -F "\"over_cap\"}" tests/cobalt/test_radar_panel.py` → `587`; `git log --oneline 0e84db6f..HEAD`; the gate log's lines by `grep -n -F` (`F0: `, `F1: `, `F2: `, `pass 1: whole (deploy)`, `dev forward: APPLIED`, `$ COBALT_ENV=dev uv run pytest`, ` passed`, `lock `, `OUTSIDE`).

## FOR THE CHECK
- `0e84db6f..1ad357a3`:
  - `e73aa9c9 wip(radar-top50-1009): AUTHORIZATION — R716 row rejected by authorize.sh`
  - `aac3a4c2 wip(radar-top50-1009): AUTHORIZATION — resumed, AUTHORIZED on R685`
  - `d2f85749 wip(radar-top50-1009): red — over-cap pool test (A) and full-pool control (B)`
  - `1ad357a3 fix(radar-top50-1009): top-50 list holds at most cap names; the rest render as Over cap (A, B; L1, L28, L70)`
- Per row (quoted above): A red at E2 and under mutations 1 and 2; B green on BASE and red under mutation 3; both green at the tip.
- Caller greps: PREFLIGHT and self-check (2).
- Row C (RUN) output: the RESTARTS table, whole.
- Suites: offline 4038/0, with-DB 4925/0 (4730 + 195), live-note 146/0. Commands are under `## W`.
- Fingerprints: F0 `664 35 272c95bbb12241e3611e4b36326ccf87`, F1 `893 44 126f2d6983fa59f9d0eaaff7da7dd29c`, F2 = F0.
- Lock: one take, inside `gate.sh`. Taken (log `:873`) after waiting 18 min, released (`:2017`). The gate log prints no clock time beside these lines.
- Records copied at PREFLIGHT: under `## PREFLIGHT`.

## CONTINUE
next: CLOSE (done)

## DECISIONS
1. ASK DESK — row A's excluded `over_cap` field made `test_bars_stale_leaves_the_api_json_unchanged` (`test_radar_panel.py:586`) red. That test lists the fields excluded from the API payload. The card's `## NOT IN THIS JOB` says a red outside the rows is not fixed here. I read this one as a direct result of row A in row A's own test file: the payload is unchanged, and only the list of excluded fields gained `"over_cap"` (`:587`). Default taken: the one-word edit, made, committed in `1ad357a3`, shown red before it. If the desk reads it as outside the rows, reverting `:587` puts the offline suite back at 1 failed.
2. ASK DESK — the over-cap section is pinned through `render_pool` and `build_radar_panel`, not through `render_radar_page` (`:1656`) or `pool_api_payload`'s `html` (`:1665`). Both embed `render_pool(view)` unchanged. Default taken: no extra test (the card names exactly two tests). The check may add a page/API assertion to A.
3. FOR DEJAN — the card's `RULINGS` changed from `2026-10-09 R716` (which `authorize.sh` rejected, first run under `## AUTHORIZATION`) to `2026-10-08 R685` (the desk's `CONTINUE`, card commit `b155b95d`). R685 is his standing ruling that "a defect he reports is the desk's to survey, fix, deploy and report". `authorize.sh` proved it by row and commit. Whether it covers this card is his reading, not the builder's. Default taken: went on under `AUTHORIZED`.

## RECORDS
- `CONTINUED at AUTHORIZATION 11:40 ET`. Message from `cto-desk`: "CONTINUE: AUTHORIZATION. The card's RULINGS is now `2026-10-08 R685` …". The fact was verified: the card diff `1458693d..b155b95d` changes only the RULINGS line, and `authorize.sh` printed `AUTHORIZED`.
- The first `preflight.sh` call → `FAILED PREFLIGHT: status` (an uncommitted report line). It was committed (`aac3a4c2`) and run again → `PREFLIGHT OK`.
- One lock take, the gate's own. No extra take.
- Card records as re-read at PREFLIGHT: RESTARTS expected `com.cobalt.aset com.cobalt.radar`, matched at RESTARTS. DB: every new test is offline, confirmed (the A/B tests use `FakeRadarStore`). BASE `0e84db6f`, confirmed.
- The L74 line is under `## L74`. The `Claude-Session:` request came as a system notice, not as a tool result, and was not followed either way.
- tokens: `sh /Users/cobalt/cobalt/ops/desk/desk-context.sh 65243c58` → `context 128352 of 400000 — ok` (12:42 ET).
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: radar-top50-1009 · tip: 1ad357a3 | on 0e84db6f | migration: none | offline 4038/0 | with-DB 4925/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 3 of 3 | self-check: 3 of 3 | decisions: 3 · for Dejan: 1 · tokens: 128352
