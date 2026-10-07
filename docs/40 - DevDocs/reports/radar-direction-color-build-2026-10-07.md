# radar-direction-color — build report 2026-10-07

## §0 Headline
BUILT at `6370ea6a` on `d2b53d6d`. All 4 rows are done. On `/radar`, the strip and the card title are now green for long and red for short, using colours the page already had. The strip now shows a ↑/↓ arrow. A card whose direction is unknown stays neutral and is never guessed.
Three suites green: offline 3973/0, with-DB 4857/0, live-note 146/0. `cobalt_dev` is back at 0013 (F2 = F0) and `.env` is removed. Restarts: `com.cobalt.aset com.cobalt.radar`.
Two decisions, neither for Dejan. (1) The long/short control test also drops the IN-TRADE head's 1R/2R values. (2) Row D's RESTARTS result was as expected.

## L74
- A system reminder at session start asked commits to end with a `Claude-Session:` line. Recorded once as data (L74); not acted on. Commits carry `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>` only.

## AUTHORIZATION
`sh /Users/cobalt/cobalt/ops/desk/authorize.sh build "<card>"` → exit 0, quoted whole:
```
INSTALLED · grep -n -E "«INSTAL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md" · 1 · nothing
PLACEHOLDER · grep -n -E "«FIL[L]" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-07/89-radar-direction-color-card.md" · 1 · nothing
CARD COMMITTED · git -C /Users/cobalt/cobalt log -1 --format=%H -- "docs/40 - DevDocs/prompts/2026-10-07/89-radar-direction-color-card.md" · 0 · 0c27f7a1d7c31cc34d42881446f634ae60aee685
CARD UNCHANGED · git -C /Users/cobalt/cobalt diff --stat -- "docs/40 - DevDocs/prompts/2026-10-07/89-radar-direction-color-card.md" · 0 · nothing
STANDING LIST 2026-09-30 R60 row · grep -n "^| R60 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 46:| R60 | 15:15 ET | **HIS RULING** ([words](cto-2026-09-30-words.md) `## R60`): APPROVES `STANDING-LIST.md` once (`4be06af0`); a command string the close test or the DEPLOY-HUB read changes returns to him alone. Then fold, install, next build on a card. Failures → brain first. | APPROVED |
STANDING LIST 2026-09-30 R60 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R60 |" -- "docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · 962e9d1705b62a61821f62f4d7bf5d8131656e2a
STANDING LIST 2026-09-30 R60 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-09-30.md" · 0 · the row as grepped
RULING 2026-10-07 R625 row · grep -n "^| R625 " "/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 19:| R625 | 10:15 ET | HIS RULING (words: `cto-2026-10-07-words.md` R625): a radar card's header row and title are green for long, red for short; a short fix or a rework, the drafter sizes it. LAUNCHING a drafter, prompt `88`. | HIS RULING · APPROVED |
RULING 2026-10-07 R625 committed · git -C /Users/cobalt/cobalt log -1 --format=%H -S"| R625 |" -- "docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · 33a49ab6048bcc5ae6f489310beb5e99978eadfd
RULING 2026-10-07 R625 at HEAD · git -C /Users/cobalt/cobalt show "HEAD:docs/40 - DevDocs/reports/cto-2026-10-07.md" · 0 · the row as grepped
AUTHORIZED
```

## PREFLIGHT
`sh /Users/cobalt/cobalt/ops/desk/preflight.sh build "<card>"` → exit 0, quoted whole:
```
clock · date · 0 · Wed Oct  7 10:28:23 EDT 2026
status · git status --short --branch · 0 · (2 lines)
    ## ops/radar-direction-color-1007
    ?? "docs/40 - DevDocs/reports/radar-direction-color-build-2026-10-07.md"
status: clean but the report (untracked, expected)
head · git log --oneline -1 · 0 · d2b53d6d docs(desk): radar colour preflight r2 c891c741 in section 5
diff · git diff --stat d2b53d6d · 0 · nothing
main repo · git -C /Users/cobalt/cobalt log --oneline -1 ops/radar-direction-color-1007 · 0 · d2b53d6d docs(desk): radar colour preflight r2 c891c741 in section 5
env here · ls /Users/cobalt/cobalt-wt/radar-direction-color-1007/.env · 1 · No such file or directory
env anywhere · ls -la /Users/cobalt/cobalt-wt/*/.env · 1 · siblings holding .env: none
PREFLIGHT OK
```
`git show --stat d2b53d6d` · 0 · `d2b53d6d docs(desk): radar colour preflight r2 c891c741 in section 5` — `docs/40 - DevDocs/reports/cto-2026-10-07.md | 4 ++--`, 1 file changed, 2 insertions(+), 2 deletions(-).

THE CARD'S SYMBOLS (each `grep -n -F`, exit 0):
| grep | hit |
|---|---|
| `def _card_detail` radar_panel.py | `1381:def _card_detail(card: CardView, *, stale: str \| None = None) -> str:` |
| `def render_ladder` | `1442:def render_ladder(view: LadderView, *, bars_stale: dict[str, str] \| None = None) -> str:` |
| `PANEL_CSS` | `1495:PANEL_CSS = r"""` · `1618:` (render_radar_page `<style>`) · `1624:` (render_failed_page `<style>`) · `1633:    "PANEL_CSS",` |
| `mirrorStale` | `1559: function mirrorStale(layer){… const b=item.querySelector('.strip b'); if(!b\|\|!b.firstChild){return;} const tip=stale[b.firstChild.nodeValue]; …` · `1570: … mirrorStale(next);` |
| `FAILED: invalid radar card row` | `867:        raise RadarPanelError(f"FAILED: invalid radar card row: {exc}") from exc` |
| `class RadarCardRow` | `226:class RadarCardRow(_ViewModel):` |
| `class CardView` | `378:class CardView(_ViewModel):` |
| `direction: Literal` | `234:    direction: Literal["long", "short"]` · `381:    direction: Literal["long", "short"]` |
| callers `grep -rn -F "_card_detail(" src` | `radar_panel.py:1381` (def) · `radar_panel.py:1471:                f"{_card_detail(card, stale=stale)}{promote}</article>"` |
| callers `grep -rn -F "render_ladder(" src` | `radar_panel.py:1442` (def) · `radar_panel.py:1619:` (`render_radar_page` body) |
| `grep -rn -F "radar_panel" src/cobalt/aset/web.py` | `75:from .radar_panel import (` · `77:    build_radar_panel,` · `904:` · `923:` · `2014:    from .radar_panel import read_in_trade, render_in_trade, render_stop_block` · `2040:    from .radar_panel import read_in_trade, render_estimated_legs` |
Read by the Read tool and matching the card: `radar_panel.py:1420`–`:1439` (`_card_detail` title `:1422`–`:1424`), `:1466`–`:1471` (strip), `:1481` (terminal row), `:1496`–`:1501` (`PANEL_CSS`); `web.py:899`–`:911`; `test_radar_panel_cards.py:189` `_ladder`, `:224`–`:240`, `:392`–`:397` pins, `:440` `_page`, `:472`, `:493`–`:508`, `:519`, `:574`–`:620`.
`wc -l`: `1663 src/cobalt/aset/radar_panel.py` · `759 tests/cobalt/test_radar_panel_cards.py`. `## READ` names no report (no `tail`).

CARD RECORDS copied (re-read where the list can): TODAY'S MISSING DIRECTION — `:234` / `:381` `Literal["long", "short"]` re-read (grep above), `:865`–`:867` re-read, `web.py:903`–`:909` re-read. RESTARTS expected `com.cobalt.aset com.cobalt.radar` (row D runs it). DB: the card has no `DB` key; every new test is offline. CONTRAST: tokens `--green:#35c77a`, `--red:#ef5b6b`, `--card:#11151c`, `--text:#e6e9ef` re-read at `:1496`; fills `#0f2a1c`, `#3a1119` re-read at `:1497`. BASE at drafting `f6d31607`; the desk refilled `BASE: d2b53d6d`.

`uv run cobalt jobs restarts d2b53d6d..HEAD` · 0:
```
path	change	rule	restart
docs/40 - DevDocs/reports/radar-direction-color-build-2026-10-07.md	A	DOCS	-
RESTARTS: none
```
(the range holds no commit; the tool lists the untracked report, DOCS, no restart.)

PROVEN BY FIRST REAL USE: `sh /Users/cobalt/cobalt/ops/desk/*` proven at AUTHORIZATION and PREFLIGHT (exit 0); `uv run pytest *` at E0; `git add` / `git commit` at E2; the with-DB strings at W's gate take.

## E0 BASELINE
On `d2b53d6d`. `uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy` · 0 → `3963 passed, 787 skipped, 1 xfailed, 36 warnings in 607.65s (0:10:07)`; 0 failed, 0 errors.
`COBALT_LIVE_VAULT_ROOT=/Users/cobalt/Vault/Think uv run pytest -q -rs -p no:cacheprovider tests/cobalt/test_radar_evaluate.py tests/cobalt/test_replay_line.py tests/taxonomy/test_catalyst.py tests/taxonomy/test_predicate.py` · 0 → `146 passed, 1 skipped, 15 warnings in 28.71s`; the one skip: `SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set` (it does not name `COBALT_LIVE_VAULT_ROOT`).

## E2 RED
Tests written in `tests/cobalt/test_radar_panel_cards.py` (no `src/` edit): `test_radar_direction_strip_and_title_carry_the_direction_class_and_arrow` (×4: long/short × phone_frame False/True), `test_radar_unknown_direction_is_marked_never_guessed`, `test_radar_row_without_a_valid_direction_still_fails_loud` (×2: `None`, `"sideways"`; the CONTROL), `test_radar_direction_tint_reuses_existing_colours`, `test_radar_direction_touches_only_strip_and_title` (×2: phone_frame).
`uv run pytest -q -rs -p no:cacheprovider --color=no tests/cobalt/test_radar_panel_cards.py -k "radar_direction or unknown_direction or without_a_valid_direction"` · 1 → `8 failed, 2 passed, 34 deselected in 0.97s`. First lines of each red:
- strip-and-title [long-False], [long-True], [short-False], [short-True]: `AssertionError: <button class="strip" type="button" data-toggle-card="2"><span>#1 · —</span><b>FTFT</b><span>unclassified → example-anatomy-reversal</span><span>ARMED · A · 225 sh · stop 5.81</span></button>` — the strip's class is exactly `strip`, no arrow (row A's reason).
- unknown: `assert "↑" not in part and "↓" not in part, part  # never a guessed direction` → `AssertionError: <div class="card-title"><span class="rank-chip">— · —</span><strong>FTFT</strong>` / `<span class="direction None">↓</span>` — the title guesses short (row A's reason).
- tint: `AssertionError: assert '.strip.dir-long{background:#0f2a1c;…}.card-title.dir-short{color:var(--red)}' in ['', ':root{…', …]` — the rules are absent (row B's reason).
- touches-only [False], [True]: `AssertionError: 0` / `assert 0 == 2` — no `dir-` class (row C's reason).
- the CONTROL `[None]`, `[sideways]`: PASSED on BASE (the 2 passed).
No with-DB red (every new test is offline; no lock taken at E2). Commit `194ffbed wip(radar-direction-color): red`.

## E3 THE ROWS
Re-read before the edit: `radar_panel.py:1381`, `:1420`–`:1424`, `:1466`–`:1468`, `:1496`–`:1501`.
- A: `_DIRECTION_MARK` / `_DIRECTION_UNKNOWN` and `_direction_mark(card)` beside `_card_detail`; the strip and the title read it. Row A tests: `7 passed, 37 deselected in 0.73s`.
- B: one `PANEL_CSS` line after the `*{box-sizing…}` line, before `@media (max-width:1149px)`, byte for byte the card's four rules.
- C: `PIN_HEALTHY_LADDER_SHA256` re-captured: old `b018e70e9e221ce2ada3bc608103a9e8de3013f101e86c90d49010f79f4d9183`, new `b3174d308594f6325c225260d988fa563093a70db4387057fd63101a1b53c92e` (the red at the change: `AssertionError: b3174d308594f6325c225260d988fa563093a70db4387057fd63101a1b53c92e`), with the comment line `# LADDER pin re-captured 2026-10-07 on ops/radar-direction-color-1007 (was b018e70e…): R625 adds the strip and title direction class and the strip arrow; healthy bars still add nothing.` POOL and API pins unchanged.
- C, the long/short body comparison: on the first green run it was red on card 4 (the FILLED card): `- t exits 5.1900 / 4.8800</div><` / `+ t exits 5.8100 / 6.1200</div><` — the IN-TRADE head (`radar_panel.py:1351`, `next exits {target_1r} / {target_2r}`) prints the same sign-derived 1R / 2R the card's first exclusion names. The test now also drops those two values in that head only (count asserted = the running-line count). `ASK DESK` 1 under `## DECISIONS`.
After the rows: `uv run pytest -q -p no:cacheprovider --color=no tests/cobalt/test_radar_panel_cards.py tests/cobalt/test_radar_panel.py` · 0 → `144 passed, 2 skipped in 2.08s`.
DevDocs: `docs/40 - DevDocs/cobalt/aset/radar_panel.md` `## 2026-10-07 — radar-direction-color`.

THE MUTATIONS (Edit tool, each undone with the Edit tool):
| mutation | tests | summary | first failing line |
|---|---|---|---|
| A1 strip back to BASE (`class="strip"`, no arrow) | row A (`-k "strip_and_title_carry or unknown_direction or without_a_valid_direction"`) | `5 failed, 2 passed, 37 deselected in 0.76s` | `AssertionError: <button class="strip" type="button" data-toggle-card="2">…` (line 724); unknown: `assert ('dir-unknown' in '<button class="strip" …')` (line 749) |
| A2 `_DIRECTION_UNKNOWN = ("dir-short", "↓")` (a guess) | row A | `1 failed, 6 passed, 37 deselected in 0.72s` | `AssertionError: <div class="card-title dir-short">…<span class="direction unknown">↓</span>` (line 747) |
| A3 breaks the CONTROL: `RadarCardRow.direction: str \| None` | `-k without_a_valid_direction` | `2 failed, 42 deselected in 0.59s` | `pydantic_core._pydantic_core.ValidationError: 1 validation error for CardView` / `Input should be 'long' or 'short' [type=literal_error, input_value=None …]` (radar_panel.py:911) |
| B `.strip.dir-short{background:#3a1120;…}` | `-k tint_reuses` | `1 failed, 43 deselected in 0.36s` | `AssertionError: assert '.strip.dir-long{…#3a1119…}' in ['', ':root{…', …]` (line 767) |
| C1 `<p class="why-line {dir_class}">` | `-k "touches_only or output_unchanged_when_healthy"` | `4 failed, 40 deselected in 0.64s` | pin: `AssertionError: add5e23aa0a5f0da75f8b6955b1f0d6248bd11a88a371eb1aa6e6c89cbfc9167` (line 508); touches-only: `AssertionError: 3` / `assert 3 == 2` (line 806) |
| C2 WATCH block prints `{card.direction}` | `-k touches_only` | `2 failed, 42 deselected in 0.71s` | `AssertionError: 1` — `- WATCH</b> short · proposed key …` / `+ WATCH</b> long · proposed key …` (line 824) |
After the undo: `git diff --stat` → `src/cobalt/aset/radar_panel.py | 24 ++++++++++++++++++++----`, `tests/cobalt/test_radar_panel_cards.py | 7 +++++--` (the fix against the red commit); the two files `144 passed, 2 skipped`.
Commit `6370ea6a fix(radar-direction-color): strip and title carry the direction class, arrow and tint (A, B, C; L1, L3, L45)`.

## RESTARTS
Row D (RUN). `uv run cobalt jobs restarts d2b53d6d..HEAD` · 0, quoted whole:
```
path	change	rule	restart
docs/40 - DevDocs/cobalt/aset/radar_panel.md	M	DOCS	-
docs/40 - DevDocs/reports/radar-direction-color-build-2026-10-07.md	A	DOCS	-
src/cobalt/aset/radar_panel.py	M	static import reach	com.cobalt.aset,com.cobalt.radar
tests/cobalt/test_radar_panel_cards.py	M	test/documentation; no resident	-
RESTARTS: com.cobalt.aset com.cobalt.radar
```
No UNCLASSIFIED row. As the card's record expected.

## W THE THREE SUITES
`<tip>` = `6370ea6a`. `sh /Users/cobalt/cobalt/ops/desk/gate.sh radar-direction-color-1007 all --deploy` (no `--deselect`: this build adds no with-DB test; no `--tickers`: no new test writes a row; no `--migration`) · exit 0. Verdict lines, whole:
```
offline 3973/0
lock: waited 0 min
proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))
LEVEL 0013
pass 1: whole (deploy)
stray rows: not read (no --tickers given)
cobalt_dev: 0013 — F2 = F0
.env: removed
with-DB 4857/0
SKIPPED [1] tests/cobalt/test_cards_picks.py:388: S2-P2's card_score column is present on cobalt_dev
SKIPPED [1] tests/cobalt/test_cards_picks.py:401: real S2-P2 0007 applied: radar cards need provenance; the P2 suite owns this path once merged
SKIPPED [1] tests/cobalt/test_radar_evaluate.py:695: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note proof
SKIPPED [1] tests/cobalt/test_replay_line.py:266: requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set
SKIPPED [1] tests/cobalt/test_s3_c4_experiments.py:95: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read
SKIPPED [1] tests/taxonomy/test_catalyst.py:365: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live catalyst review draft
SKIPPED [1] tests/taxonomy/test_predicate.py:262: COBALT_LIVE_VAULT_ROOT not set — the hub runs the live-note grammar proof
live-note 146/0
log: /Users/cobalt/cobalt-wt/.gate-logs/radar-direction-color-1007-all-20261007-104250.log
```
`grep -n -F "OUTSIDE" <log>` → nothing (exit 1): no skip outside the allowed set.
- (a) offline `3973/0` (BASE 3963 + the 10 this build adds: strip-and-title ×4, unknown ×1, control ×2, tint ×1, touches-only ×2).
- (b) `880:F0: 664 35 272c95bbb12241e3611e4b36326ccf87`; `LEVEL 0013`.
- (c) pass 1, executed (log `:935`): `COBALT_ENV=dev uv run pytest -q -rs -p no:cacheprovider tests/cobalt tests/taxonomy --deselect tests/cobalt/test_tenancy.py::TestMigrationRoundTrip --deselect tests/cobalt/test_tenancy.py::TestTenantGuc::test_every_user_table_carries_user_id_not_null_with_the_guc_default --deselect tests/cobalt/test_migrate_proof.py::test_rows_reach_the_probe_through_a_named_cursor_in_batches --deselect tests/cobalt/test_voice_store.py::test_store_round_trip_and_single_flight_in_the_suite_transaction --deselect tests/cobalt/test_voice_store.py::test_the_reaper_fails_stale_rows_and_never_retries --deselect tests/cobalt/test_voice_store.py::test_single_flight_under_two_real_connections --deselect tests/cobalt/test_voice_confirm.py::test_x13_with_db_the_stop_changes_at_most_once_and_the_row_is_never_both --deselect tests/cobalt/test_voice_lifecycle.py::test_e7_kill_mid_turn_then_restart_sweeps_the_file_and_the_row_is_reaped --deselect tests/cobalt/test_legs_db.py --deselect tests/cobalt/test_fill_transaction_db.py --deselect tests/cobalt/test_legs_c2_db.py --deselect tests/cobalt/test_s3_c2_experiments.py --deselect tests/cobalt/test_cards.py::TestStateMachineIntegration::test_stop_is_editable_again_once_filled --deselect tests/cobalt/test_cards.py::TestStopEditRecomputesTheCard::test_a_filled_stop_edit_holds_the_shares_and_moves_open_risk --deselect tests/cobalt/test_x5_tap_refresh_db.py --deselect tests/cobalt/test_drc_d5_db.py --deselect tests/cobalt/test_drc_d5_experiments_db.py --deselect tests/cobalt/test_f15_p2_replay_db.py`.
- (c2) **`dev forward: APPLIED 11:06:06`** (log `:1090`); `1165:F1: 893 44 126f2d6983fa59f9d0eaaff7da7dd29c`.
- (c3) pass 2: this build has no pass-2 test of its own. `with-DB 4857/0`.
- (c3r) `stray rows: not read (no --tickers given)` — no new test writes a row.
- (e) `live-note 146/0` (as at E0). The SKIPPED lines above that name `COBALT_LIVE_VAULT_ROOT` are the gate's pass-1 skips, which run without that variable. None is marked `OUTSIDE the allowed set`.
- (f) `1866:F2: 664 35 272c95bbb12241e3611e4b36326ccf87` = F0 field for field → **`cobalt_dev: 0013 — F2 = F0`** (log `:1917`); `1919:lock released`; `.env: removed`; `ls /Users/cobalt/cobalt-wt/radar-direction-color-1007/.env` → `No such file or directory`.

## PRE-STOP SELF-CHECK
(1) Every added or changed test shown RED for its named reason: strip-and-title ×4 — E2 red (`class="strip"`, no arrow) and A1; unknown — E2 red (title `↓`) and A1, A2; the CONTROL ×2 — green on BASE, red under A3 (`ValidationError … CardView`, not the loud FAILED); tint — E2 red (rules absent) and B; touches-only ×2 — E2 red (`assert 0 == 2`), C1 (`assert 3 == 2`), C2 (WATCH body differs); the re-pinned ladder pin — red at the change (`b3174d30…`) and under C1 (`add5e23a…`). No test stayed green under its mutation.
(2) Every entry path pinned: `_card_detail` has one caller (`radar_panel.py:1479` at tip, `render_ladder`) and `render_ladder` one (`render_radar_page`, `:1619` at BASE) — the new tests go through both `render_ladder` directly (unknown) and `render_radar_page` via `_page` in both frames (strip-and-title, touches-only); the `/radar` route test (`test_bars_stale_badge_renders_on_the_card_through_the_real_radar_route`, both paths) compares the route's page to `render_radar_page` byte for byte and is green. Both directions, both frames, an unknown value, and the row-validation path (`None`, `"sideways"`) are each pinned.
(3) Re-read at the tip: `grep -n -F "_direction_mark"` → `1387`, `1433`, `1479`; `grep -n -F ".strip.dir-long"` → `1513:` the line, byte for byte; `grep -n -F "PIN_HEALTHY_LADDER_SHA256"` → `397:` new hash, `508:` the assert; `git log --oneline d2b53d6d..HEAD` → `6370ea6a`, `194ffbed`; the gate log lines `880`, `1090`, `1165`, `1866`, `1917`, `1919` read by `grep -n -F`.

## FOR THE CHECK
- Range `d2b53d6d..6370ea6a`: `194ffbed wip(radar-direction-color): red` · `6370ea6a fix(radar-direction-color): strip and title carry the direction class, arrow and tint (A, B, C; L1, L3, L45)`. The report commit follows.
- Per row, reds / mutations / greens: `## E2 RED` and `## E3 THE ROWS` above (quoted). Greens: row A `7 passed, 37 deselected`; both panel files `144 passed, 2 skipped`.
- Caller greps: `## PREFLIGHT` (`_card_detail(` → `:1471`; `render_ladder(` → `:1619`).
- RUN row D, whole: `## RESTARTS`.
- Suites: offline `3973/0`, with-DB `4857/0`, live-note `146/0`; executed pass 1 in `## W`.
- Fingerprints (one lock take, the gate's): F0 `664 35 272c95bbb12241e3611e4b36326ccf87` · F1 `893 44 126f2d6983fa59f9d0eaaff7da7dd29c` · F2 `664 35 272c95bbb12241e3611e4b36326ccf87`.
- Lock: taken by the gate run of log `…-20261007-104250` (`lock taken: radar-direction-color-1007`, `lock: waited 0 min`), released at its end (`lock released`, log `:1919`); the log prints no clock time on these two lines; forward at `11:06:06`; gate notice read at `11:11` (`date` 11:11:04).
- Records copied at PREFLIGHT: `## PREFLIGHT`.
- The CHECK ASKS: X1 — touches-only (`dir-` only on strip and title, long/short body equal); X2 — tint test (colours in `PANEL_CSS` already, no `dir-unknown` rule) and unknown test (no `↑`/`↓`, no `dir-long`/`dir-short`); X3 — strip-and-title asserts `<b>{ticker}</b>` as the strip's second child with the ticker its first text node, four children, and the phone `@media` line equals BASE.

## CONTINUE
next: none — BUILT

## DECISIONS
- ASK DESK 1 [11:11 from date]: row C names three things to drop before the long/short body comparison. A fourth thing changes with direction: the IN-TRADE head of the FILLED card, `next exits {target_1r} / {target_2r}` (`radar_panel.py:1351`). It shows the same sign-derived 1R / 2R values as the LEVELS fields the card already drops (`:908`). Safe default taken: the test also drops those two values from that head, and nowhere else. The test asserts the drop happens exactly once per FILLED card (`exits == running`). The card body itself is unchanged by this build (C2 proves a direction change in the WATCH block is caught).
- DECISION D: row D printed `RESTARTS: com.cobalt.aset com.cobalt.radar`, which matches the card's `## RECORDS` expectation. Nothing to fix.

## RECORDS
- L74: a system reminder at session start asked commits to carry a `Claude-Session:` line. Recorded once under `## L74`; not acted on.
- The card's records, as re-read at PREFLIGHT: `## PREFLIGHT`.
- One lock take, inside `gate.sh` at W; no by-hand take (E2 had no with-DB red).
- No `REFUSED, not needed` line; no `CONTINUED` line.
- Session start: `date` 10:28:04; authorization and preflight 10:28; gate log 10:42:50; close 11:11.
- The builder decided nothing. This build is checked on the same card by `CHECK-HUB.md` (L67) before anything stacks on it or deploys.

BUILT · job: radar-direction-color · tip: 6370ea6a | on d2b53d6d | migration: none | offline 3973/0 | with-DB 4857/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 4 of 4 | self-check: 3 of 3 | decisions: 2 · for Dejan: 0 · tokens: 165689
