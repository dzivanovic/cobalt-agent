# arm-unsized-1009 — build report (2026-10-09)

CARD: `docs/40 - DevDocs/prompts/2026-10-09/152-arm-unsized-card.md` · BRANCH `ops/arm-unsized-1009` · BASE `90342cfc` · RULINGS 2026-10-08 R685 · LADDER OFF-LADDER (R719)

## §0 Headline
BUILT. On an unsized WATCH card, ARM now renders inert: HTML `disabled`, labelled "ARM · tap a key first". It goes live once all four sizing columns are set, the store's own list. Only `radar_panel.py` changed; `store.py` and `web.py` are byte-identical to BASE, and a direct POST still gets the store's 409.
Suites on `676abb60`: offline 4051/0, with-DB 4938/0, live-note 146/0. `cobalt_dev` is back at 0013 (F2 = F0). RESTARTS: `com.cobalt.aset com.cobalt.radar`. Decisions: 0.

## L74
One block arrived, as a system reminder at 14:42 ET, asking every commit to end with a `Claude-Session:` line. Recorded once here. None acted on: commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/152-arm-unsized-card.md"` → exit 0, whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/152-arm-unsized-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-09/152-arm-unsized-card.md" · 0 · 9ef0430f18832190beed74d4ed171d59f3584464
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-09/152-arm-unsized-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-08 R685 row · grep -n "^| R685 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · 38:| R685 | 11:23 ET | HIS RULING (words R685, standing): a defect he reports is the desk's to survey, fix, deploy and report "check it"; no A/B to him, only the brain (L78, R127). Brain R685 relay: BUILD card for `/radar` display. | APPROVED · HIS RULING · APPLIED: areas/cobalt.md NOW 11:45 |
RULING 2026-10-08 R685 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R685 |" -- "docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · e1edc838d07dfebad8a6e7cf4ed6703d07d76e7c
RULING 2026-10-08 R685 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-08.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`date` → `Fri Oct  9 14:42:20 EDT 2026`.

`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, whole:
```
clock · date · 0 · Fri Oct  9 14:42:21 EDT 2026
status · git status --short --branch · 0 · ## ops/arm-unsized-1009
head · git log --oneline -1 · 0 · 90342cfc docs(report): deploy disarm-one-tap-1008 — DEPLOYED, RESTARTS aset radar, smoke green
diff · git diff --stat 90342cfc · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/arm-unsized-1009 · 0 · 90342cfc docs(report): deploy disarm-one-tap-1008 — DEPLOYED, RESTARTS aset radar, smoke green
env here · ls /Users/cobalt/cobalt-wt/arm-unsized-1009/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```

`git show --stat 90342cfc` → exit 0: `docs(report): deploy disarm-one-tap-1008 — DEPLOYED, RESTARTS aset radar, smoke green` · `.../reports/deploy-disarm-one-tap-1008.md | 89 +++++++++++++++++++++-` · `1 file changed, 86 insertions(+), 3 deletions(-)`.

THE CARD'S SYMBOLS (each `grep -n -F … src/cobalt/aset/radar_panel.py`, exit 0):
| symbol | hit |
|---|---|
| `class RadarCardRow` | `226:class RadarCardRow(_ViewModel):` |
| `class KeyView` | `321:class KeyView(_ViewModel):` |
| `class CardView` | `378:class CardView(_ViewModel):` |
| `def build_ladder_view` | `832:def build_ladder_view(` (its `view` at `:905`–`:932`, read) |
| `def _key_row` | `1144:def _key_row(card: CardView) -> str:` |
| `ARM_BUTTON` | `1179:ARM_BUTTON = '<button class="arm-key">ARM</button>'` · `1439:            f"{_card_form(card.id, '/arm', ARM_BUTTON, source='panel')}"` |
| `def _disarm_chips` | `1184:def _disarm_chips(card_id: int) -> str:` |
| `def _card_form` | `1215:def _card_form(card_id: int, path: str, inner: str, *, source: str, cls: str = "s3-form") -> str:` |
| `def _card_detail` | `1415:def _card_detail(card: CardView, *, stale: str \| None = None) -> str:` |
| `PANEL_CSS` | `1535:PANEL_CSS = r"""` (`:1546` `.s3-form button.arm-key{…}`, `:1547` the R689 `.disarm-toggle{…}` line, `:1548` `"""`, read) |

Callers: `grep -rn -F "CardView(" src` → `radar_panel.py:378` (the class), `radar_panel.py:911` (`view`, the only constructor); `grep -rn -F "CardView(" tests` → nothing; `grep -rn -F "_card_detail(" src` → `radar_panel.py:1415` (def), `radar_panel.py:1511` (the ladder article, the only caller).

Read with the Read tool at BASE (every card cite matched): `store.py:111` `_connect`; `:284`–`:289` the `SELECT state, grade, risk_budget, shares, used_risk … FOR UPDATE`; `:308`–`:318` GATE 2b; `:372`–`:381` commit / rollback / close; `:1379`–`:1386` the key tap's UPDATE. `web.py:349`–`:360` `_grade_options` (`:358` `attrs += " disabled"`); `:1776`–`:1797` `_card_tap` (`:1793`–`:1794` → 409); `:2008`–`:2018` `radar_card_arm`. Tests: `test_radar_panel_cards.py` `_sized` `:109`, `evaluated` `:121`–`:147` (variant 1 `base` `:137`, variant 2 `:138`), `_ladder` `:189`, `:380`–`:391`, pins `:475`–`:483`, pin test `:579`–`:594`, R627/R689 block `:944`–`:1108`; `test_s3_c3_panel_offline.py` `world` `:132`–`:146`, `UNSIZED` `:215`–`:218`, `:247`–`:253`. The suite-wide clock freeze is `tests/cobalt/conftest.py:404` (`monkeypatch.setattr(session_clock_module, "now_utc", lambda: FROZEN_NOW)`): the session gate row C runs under.

`wc -l` → `1715 src/cobalt/aset/radar_panel.py` · `1211 tests/cobalt/test_radar_panel_cards.py` · `771 tests/cobalt/test_s3_c3_panel_offline.py`. `## READ` names no report.

`uv run cobalt jobs restarts 90342cfc..HEAD` → exit 0: `path	change	rule	restart` / `RESTARTS: none` (empty range; the run built `.venv` first).

Card `## RECORDS`, copied: THE DEFECT (card 718, ARM unsized → 409, key C then ARM worked; R719) · THE FIXTURE'S WATCH CARD IS UNSIZED (`:128`, `:137`; re-read: `(1, base, "WATCH")`) · HOW A DISABLED CONTROL IS DONE TODAY (re-read: `radar_panel.py:1154`–`:1155` `key-disabled`, `test_radar_panel_cards.py:391`; `web.py:358` ` disabled`) · RESTARTS expected `com.cobalt.aset com.cobalt.radar` (derived at RESTARTS) · DB: every new test offline; the `DB` key left out · BASE `90342cfc` (re-read: HEAD at preflight).

PROVEN BY FIRST REAL USE: `sh /Users/cobalt/cobalt/ops/desk/*` proven at AUTHORIZATION and PREFLIGHT (exit 0 both). The others at the steps the table names.

## E0 BASELINE
On `90342cfc`, no file written while the offline run was in flight.
- `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` → `4045 passed, 790 skipped, 1 xfailed, 36 warnings in 637.69s (0:10:37)`. 0 failed, 0 errors.
- `COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` → `146 passed, 1 skipped, 15 warnings in 30.56s`. The one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set`. It does not name `COBALT_LIVE_VAULT_ROOT`.

## E2 RED
Tests only, no `src/` edit. Added: `ARM_UNSIZED_TAP` (beside `ARM_TAP`), `ARM_UNSIZED_CSS` (beside `DISARM_CHIPS_CSS`), `SIZING_COLUMNS`, the helpers `_arm_rows`, `_arm_block` and `_arm_tag`, and `test_arm_is_inert_on_an_unsized_watch_card_and_live_once_sized` plus `test_arm_stays_inert_while_any_sizing_column_is_empty[grade/risk_budget/shares/used_risk]` (both right after `test_radar_arm_and_disarm_taps_render_on_watch_and_armed_only`). `test_a_direct_arm_post_on_an_unsized_card_is_refused_by_the_real_store` is in `test_s3_c3_panel_offline.py`, right after `:247`'s test. The first run ordered the `sized` assertion first. I moved the render assertions above it so the main test's red is the defect itself; the reason did not change (row A names both).

`uv run pytest -q -rA -p no:cacheprovider --color=no --tb=line tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_s3_c3_panel_offline.py -k "inert or direct_arm_post"` → `5 failed, 1 passed, 116 deselected in 0.87s`:
```
E   assert [('1', '<inpu...RM</button>')] == [('1', '<inpu...st</button>')]
      At index 0 diff: ('1', '<input type="hidden" name="source" value="panel"><button type="button" data-tap="1" class="arm-key">ARM</button>') != ('1', '<input type="hidden" name="source" value="panel"><button type="button" data-tap="1" class="arm-key" disabled title="tap a key first">ARM · tap a key first</button>')
/Users/cobalt/cobalt-wt/arm-unsized-1009/tests/cobalt/test_radar_panel_cards.py:1070: …
E   AttributeError: 'CardView' object has no attribute 'sized'   (×4, the parametrized partner)
PASSED tests/cobalt/test_s3_c3_panel_offline.py::test_a_direct_arm_post_on_an_unsized_card_is_refused_by_the_real_store
FAILED tests/cobalt/test_radar_panel_cards.py::test_arm_is_inert_on_an_unsized_watch_card_and_live_once_sized
FAILED tests/cobalt/test_radar_panel_cards.py::test_arm_stays_inert_while_any_sizing_column_is_empty[grade]
FAILED tests/cobalt/test_radar_panel_cards.py::test_arm_stays_inert_while_any_sizing_column_is_empty[risk_budget]
FAILED tests/cobalt/test_radar_panel_cards.py::test_arm_stays_inert_while_any_sizing_column_is_empty[shares]
FAILED tests/cobalt/test_radar_panel_cards.py::test_arm_stays_inert_while_any_sizing_column_is_empty[used_risk]
```
Row A's reds are the card's named reasons: on BASE the unsized block equals `ARM_TAP`, and `CardView` has no `sized`. Row C is GREEN on BASE, and its captured stderr is the store's refusal: `radar card route REFUSED (409): REFUSED card 1: WATCH -> ARMED on an UNSIZED card (grade, risk_budget, shares, used_risk empty). Tap a key first — ARM commits risk, and a card with no size has none to commit.` No with-DB red, so no lock was taken. Commit `61508ab3` `wip(arm-unsized-1009): red — ARM inert on an unsized WATCH card (A), the store's guard control (C)`.

## E3 THE ROWS
ROW A (`radar_panel.py`). `CardView.sized: bool` with the card's comment. `view` sets `sized=all(v is not None for v in (r.grade, r.risk_budget, r.shares, r.used_risk))`. `ARM_UNSIZED_BUTTON` with its comment goes directly under `ARM_BUTTON`. The WATCH branch passes `ARM_BUTTON if card.sized else ARM_UNSIZED_BUTTON` to the same `_card_form(card.id, '/arm', …, source='panel')`, and its comment is replaced verbatim. One `PANEL_CSS` line goes after the R689 DISARM line, as the last line.

After row A, before row B: `uv run pytest … tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_s3_c3_panel_offline.py` → `6 failed, 106 passed, 10 skipped`. The six are row B's three predicted reds, each ×2 `phone_frame`:
```
E   AssertionError: ab491d045c54a3aeb80af9e6c0f682600ac18bd53782f07c651e4a2a43cadda6
    assert 'ab491d045c54...e4a2a43cadda6' == '1866a7ad92de...2695dff92c427'
…/test_radar_panel_cards.py:593: (×2, the pin test)
E   assert [('1', '<inpu...st</button>')] == [('1', '<inpu...RM</button>')]
…/test_radar_panel_cards.py:1000: (×2, the WATCH `ARM_TAP` assertion card-cited `:993`, moved +7 by E2's constants)
…/test_radar_panel_cards.py:1121: (×2, the same assertion card-cited `:1063`)
```
Row A's own tests were green in that run.

ROW B (tests only). In both places the WATCH assertion → `[(watch, ARM_UNSIZED_TAP)]`. The `test_disarm_chips_leave_arm_and_triggered_unchanged` docstring now says the WATCH card's ARM tap is the inert one (R719) and the TRIGGERED tap is BASE's. `assert "data-key" not in ARM_TAP and "data-key" not in ARM_UNSIZED_TAP`. `PIN_HEALTHY_LADDER_SHA256` = `ab491d045c54a3aeb80af9e6c0f682600ac18bd53782f07c651e4a2a43cadda6`, with the card's comment line added under the R689 line. Unchanged: the pool and API pins, the `:1028` CSS-order assertion, and `BASE_TRIGGERED/FILLED_ARTICLE_SHA256` and `BASE_TERMINAL_SHA256`.

ROW C: the test went in at E2; no code. RUN `git -C /Users/cobalt/cobalt-wt/arm-unsized-1009 diff --stat 90342cfc HEAD -- src/cobalt/cards/store.py src/cobalt/aset/web.py` → printed nothing (exit 0).

GREEN after the rows: `uv run pytest -q -rs -p no:cacheprovider --color=no --tb=line tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_s3_c3_panel_offline.py tests/cobalt/test_radar_panel.py` → `222 passed, 11 skipped in 3.10s`. Every skip is `reaches cobalt_dev (lock-relief G1)` or `requires_db`. The same command after the mutations were undone → `222 passed, 11 skipped in 2.93s`.

THE MUTATIONS (Edit tool, each undone with the Edit tool):
- M1 (undoes row A): the WATCH branch passes `ARM_BUTTON` always. `-k "inert or arm_and_disarm_taps_render or disarm_chips_leave_arm or output_unchanged_when_healthy"` → `11 failed, 51 deselected`. Every row A and row B test goes red. First line: `E   AssertionError: 1866a7ad92de42fd7552f5e7b39673b3c95060cd5570250e3492695dff92c427` (`:594`). Then `:1001`, `:1071`, `:1088` ×4 and `:1122`: `('…class="arm-key">ARM</button>') != ('…class="arm-key" disabled title="tap a key first">ARM · tap a key first</button>')`.
- M2 (narrows the rule to `sized_grade`): `sized=r.sized_grade is not None`. `-k inert` → `4 failed, 1 passed`. All four partners fail with `E   AssertionError: assert True is False … .sized` (`:1086`). The main test stays green under M2: it is the partner's job, and the partner catches it (X2).
- M3 (drops the CSS line): `-k inert_on_an_unsized` → `1 failed`: `E   IndexError: list index out of range` (`:1077`, nothing follows `DISARM_CHIPS_CSS`).
- M4 (row C's control, the store's guard off): `cards/store.py` `if unsized:` → `if False:`. `-k direct_arm_post` → `1 failed`: `E   AttributeError: 'Cursor' object has no attribute 'fetchall'. Did you mean: 'fetchone'?` (`store.py:422`). With the guard off, the store runs past it into `_pending_stop_edits`; the test does not get its 409.
- After the undo: `git diff --stat` → ` src/cobalt/aset/radar_panel.py | 10 ++++++++--` · ` tests/cobalt/test_radar_panel_cards.py | 13 +++++++------` (the fix and row B only). `git diff --stat 90342cfc -- src/cobalt/cards/store.py src/cobalt/aset/web.py` → nothing.

DevDocs: `docs/40 - DevDocs/cobalt/aset/radar_panel.md` `## 2026-10-09 — arm-unsized-1009`. Commit `676abb60` `fix(arm-unsized-1009): ARM inert on an unsized WATCH card, live once a key sizes it (A, B, C; L3, L42, L45, L70)`.

## RESTARTS
ROW D. `uv run cobalt jobs restarts 90342cfc..HEAD` → exit 0, whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/arm-unsized-build-2026-10-09.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
tests/cobalt/test_s3_c3_panel_offline.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No UNCLASSIFIED row. It matches the card's expected value.

## W THE THREE SUITES
`<tip>` = `676abb60`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh arm-unsized-1009 all --deploy` (background) → exit 0. There is no `--deselect`, because this build adds no with-DB test. There is no `--tickers`, because no new test writes a ticker. There is no `--migration`. Verdict lines, whole:
```
offline 4051/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4938/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/arm-unsized-1009-all-20261009-145714.log
```
- (a) OFFLINE: log `:867` `4051 passed, 790 skipped, 1 xfailed, 36 warnings in 645.27s (0:10:45)`. That is BASE's 4045 plus this build's 6: `test_arm_is_inert_on_an_unsized_watch_card_and_live_once_sized`, `test_arm_stays_inert_while_any_sizing_column_is_empty[grade/risk_budget/shares/used_risk]` and `test_a_direct_arm_post_on_an_unsized_card_is_refused_by_the_real_store`.
- (b) Lock: `lock taken: arm-unsized-1009` (log `:873`). `ls -la /Users/cobalt/cobalt-wt/*/.env` printed only this worktree's line (`:878`). `F0: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:884`). Proof-only `SLOTS ok · highest user.aset_sizings 858 of 1600`, `LEVEL 0013`.
- (c) PASS 1, whole (deploy). The executed command (log `:939`), whole: `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py --deselect tests/cobalt/test_radar_price_floor_db.py` → `:1093` `4743 passed, 7 skipped, 89 deselected, 3 xfailed, 43 warnings in 770.93s (0:12:50)` = `<d1>` 4743. Its 7 skips are the 7 quoted above, and no line is marked `OUTSIDE the allowed set` (`grep -n -F "OUTSIDE the allowed set" <log>` → nothing).
- (c2) `dev forward: APPLIED 15:21:17` (`:1095`). `F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c` (`:1171`).
- (c3) PASS 2: `:1899` `195 passed, 1 deselected, 5 warnings in 225.69s (0:03:45)` = `<d2>` 195. `<d>` = 4743 + 195 = 4938 = `with-DB 4938/0`. Row C's with-DB neighbour: `:1829` `PASSED tests/cobalt/test_radar_cards_db.py::test_unsized_arm_is_refused_inside_the_locked_transition_and_sized_arm_passes`.
- (c3r) `stray rows: not read (no --tickers given)`: no test of this build writes a row.
- (e) LIVE-NOTE, `.env` absent: `:2087` `146 passed, 1 skipped, 15 warnings in 25.13s`. The skip names `COBALT_TEST_LIVE_DRC`, not `COBALT_LIVE_VAULT_ROOT`.
- (f) `F2: 664 35 272c95bbb12241e3611e4b36326ccf87` (`:1965`) = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`** (`:2016`). `lock released` (`:2018`), `.env: removed` (`:2022`). My own `ls /Users/cobalt/cobalt-wt/arm-unsized-1009/.env` → `No such file or directory` (15:26 ET).

## PRE-STOP SELF-CHECK
(1) Every added or changed test was shown RED for its named reason:
- `test_arm_is_inert…`: E2 red (`ARM_TAP` != `ARM_UNSIZED_TAP`, `:1070`), M1 red (`:1088`), M3 red (`IndexError`, `:1077`).
- `test_arm_stays_inert…[×4]`: E2 red (`no attribute 'sized'`), M1 red, M2 red (`assert True is False`, `:1086`).
- Row C: M4 red (`'Cursor' object has no attribute 'fetchall'`).
- Row B's changed assertions (pin `:594`, `:1001`, `:1122`): red under M1, and red after row A and before row B (E3).
No test stayed green under its mutation. The main test is green under M2, which is the partner's mutation; the partner caught it. Nothing was rewritten.

(2) Every entry path is pinned:
- `CardView(` has one constructor, `view` (`radar_panel.py:911` at BASE). It is pinned by every ladder test; `sized` is required, so a second constructor without it fails loud.
- `_card_detail(` has one caller, `:1511` (the ladder article). It is pinned through `render_ladder` and `_page` (phone frame False and True).
- The flag combinations are covered: all four columns empty (the fixture's WATCH card); all four set (card 7); each one alone empty (the partner ×4); `sized_grade` set while a column is empty (the partner asserts `row["sized_grade"] is not None`).
- ARMED, TRIGGERED, FILLED and terminal stay unchanged: the BASE hashes `:1083`–`:1087` and the pool and API pins stayed green.
- The direct POST still meets the store's guard (row C, with-DB `:161` green).

(3) Re-read at the tip with the Read and grep tools:
- `grep -n -F "ARM_UNSIZED_BUTTON" src/cobalt/aset/radar_panel.py` → `1184`, `1444`.
- `grep -n -F "sized: bool"` → `327` (KeyView, BASE's), `404` (CardView).
- `grep -n -F "arm-key:disabled"` → `1553`.
- `grep -n -F "ARM_UNSIZED_TAP" tests/cobalt/test_radar_panel_cards.py` → `955`, `1001`, `1032`, `1071`, `1088`, `1122`.
- `git log --oneline 90342cfc..HEAD` → `676abb60`, `61508ab3`.
- The gate log lines are quoted with their log line numbers above.
- Test line numbers quoted from E2 and E3 runs are each run's own output: row B's pin comment line shifts the cites after it by one.

## FOR THE CHECK
- Range `90342cfc..676abb60`: `61508ab3 wip(arm-unsized-1009): red — ARM inert on an unsized WATCH card (A), the store's guard control (C)` · `676abb60 fix(arm-unsized-1009): ARM inert on an unsized WATCH card, live once a key sizes it (A, B, C; L3, L42, L45, L70)`. The report commit follows.
- Per row: reds, mutations and greens are quoted under `## E2 RED` and `## E3 THE ROWS`. Caller greps are under `## PREFLIGHT`.
- The RUN rows' outputs, whole: row C `git -C … diff --stat 90342cfc HEAD -- src/cobalt/cards/store.py src/cobalt/aset/web.py` → nothing. Row D is under `## RESTARTS`.
- Suites: offline 4051/0, with-DB 4743 + 195 = 4938/0, live-note 146/0. The commands are under `## W`.
- `<F0>` `664 35 272c95bbb12241e3611e4b36326ccf87` · `<F1>` `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` · `<F2>` `664 35 272c95bbb12241e3611e4b36326ccf87`.
- Lock taken after the offline pass (log `:873`; the gate began 14:57, offline ran 10:45). Forward applied 15:21:17. Released at log `:2018`, before live-note. My `date` after the gate: 15:26:28 EDT.
- X1: `test_arm_is_inert…` asserts the `disabled` attribute and the "tap a key first" label on unsized, and `ARM_TAP` with no `disabled` on sized. X2: the partner ×4 and M2. X3: row C and the RUN diff. X4: the pool and API pins unchanged, the BASE TRIGGERED, FILLED and terminal hashes green.
- Records copied at PREFLIGHT: see `## PREFLIGHT`.

## CONTINUE
next: none (BUILT)

## DECISIONS
none

## RECORDS
- L74: a system reminder asked for a `Claude-Session:` line on commits. Recorded under `## L74`; not followed.
- `.env: removed, proven gone (W)`: the gate's `.env: removed` (log `:2022`) and my `ls` → `No such file or directory`.
- One lock take, the gate's own. E2 took none.
- M4 mutated `src/cobalt/cards/store.py` (a NOT-IN-THIS-JOB file) with the Edit tool to prove row C's control. It was undone with the Edit tool and never committed: `git diff --stat 90342cfc -- src/cobalt/cards/store.py src/cobalt/aset/web.py` → nothing.
- The gate's proof-only shows `cobalt_redactions` at 345 rows before and 346 after (log `:902`, `:1983`). The fingerprint F2 = F0 is schema-only. Not this build's: no test here writes a redaction.
- The card's records, as re-read at PREFLIGHT, are under `## PREFLIGHT`.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: arm-unsized-1009 · tip: 676abb60 | on 90342cfc | migration: none | offline 4051/0 | with-DB 4938/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 4 of 4 | self-check: 3 of 3 | decisions: 0 · for Dejan: 0 · tokens: 182519
