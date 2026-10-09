JOB: radar-top50-1009
LADDER: OFF-LADDER — reports/cto-2026-10-09.md R716
BRANCH: ops/radar-top50-1009
WORKTREE: radar-top50-1009
BASE: 0e84db6f
TIP:
REPORT: /Users/cobalt/cobalt-wt/radar-top50-1009/docs/40 - DevDocs/reports/radar-top50-build-2026-10-09.md
CHECK REPORT:
HOUSE B:
RULINGS: 2026-10-09 R716

## ROWS

WHY: the page draws every open admitted episode of the day as `Current admitted` and never compares the count to `cap`. `build_pool_view` takes every row with `entered_at` set and `left_at` NULL (`radar_panel.py:630`–`:632`). It checks only `len == pool.members` (`:633`–`:636`), and `render_pool` draws all of `view.current` (`:1074`). A pool row with `members = 51`, `cap = 50` and 51 such episodes therefore renders 51 names under a `50` cap. HOLD and LEAVE are not visible to the page. A membership row carries no action (`MembershipRecord`, `:115`–`:141`). A HOLD updates the open episode in place (`radar/store.py:114`–`:129`) and stays one row. A LEAVE sets `left_at` (`store.py:130`–`:138`), which moves the row to `Departed admitted` (`radar_panel.py:637`–`:639`). So the page cannot name the extra member as held or leaving. It can only put the rows past `cap` in their own labelled section. SIZE: one `src/` file, one test file. No store, decision, route, migration or setting changes.

| row | what | red first | files |
|---|---|---|---|
| A | THE TOP-50 LIST HOLDS AT MOST `cap` NAMES. In `build_pool_view`, after `current` is built and ordered (`radar_panel.py:644`), split it: `current[:pool.cap]` stays `current`, and `current[pool.cap:]` becomes `over_cap`. The membership check (`:633`) is unchanged, so a count mismatch still fails. Add `over_cap: list[PoolRow] = Field(default_factory=list, exclude=True)` to `PoolView` (`:195`–`:218`, beside `bars_stale_tickers`, `:213`). It is excluded, so the API JSON and the healthy pins do not change. In `render_pool`, on the line after `Current admitted` (`:1074`), render `_pool_table(view.over_cap, "Over cap — open admitted beyond cap", bars_stale=view.bars_stale_tickers)` only when `view.over_cap` is non-empty, never inside a `<details>`. Each over-cap row keeps `category="current"`. `<b>{view.members}</b> / {view.cap} admitted` (`:1071`) stays as it is, so the page still shows `51 / 50` | `test_a_pool_over_cap_renders_cap_names_and_the_rest_in_their_own_section` (in `test_radar_panel.py`, next to `test_pool_member_count_mismatch_fails_instead_of_rendering_empty`, `:838`). From `_small_snapshot()` (`:96`), deep-copy its current row 51 times. Give each copy a distinct `id` and `ticker`, with `last_rank` 1..50 on the first 50 copies and 51 on the 51st (`T51`). This is the held or sticky member past the seats. Use `pool_row.update(members=51, cap=50)`, then `_build` (`:128`). Assert `len(view.pool.current) == 50`, `[r.ticker for r in view.pool.over_cap] == ["T51"]` and `T51` not in `current`. In `render_pool`: `Current admitted <span class="count">50</span>` is present, `Over cap — open admitted beyond cap <span class="count">1</span>` is present, and the `T51` `<tr` comes after the `Over cap` heading. RED on BASE: `len(view.pool.current) == 51` | `src/cobalt/aset/radar_panel.py` (`PoolView`, `build_pool_view`, `render_pool` only), `tests/cobalt/test_radar_panel.py` |
| B | CONTROL — A FULL POOL RENDERS AS TODAY. Use the same build with 50 copies (`last_rank` 1..50) and `pool_row.update(members=50, cap=50)`. All 50 rows are in `current`, `getattr(view.pool, "over_cap", []) == []`, and the rendered pool holds `Current admitted <span class="count">50</span>` and no `Over cap`. The pins `PIN_HEALTHY_POOL_SHA256` and `PIN_HEALTHY_API_SHA256` (`test_radar_panel_cards.py:480`, `:482`) stay unchanged and green, and `test_pool_member_count_mismatch_fails_instead_of_rendering_empty` (`:838`) stays green | `test_a_full_pool_renders_fifty_and_no_over_cap_section`. GREEN on BASE and after; the build report quotes it green at BASE before any edit | `tests/cobalt/test_radar_panel.py` |
| C | RUN — asserts nothing. `uv run cobalt jobs restarts <BASE>..HEAD`; quote its output. Expected: `com.cobalt.aset com.cobalt.radar` (`## RECORDS` RESTARTS) | — (tool output quoted in the report) | none |

## NOT IN THIS JOB
- `radar/pool.py` (`decide`), `radar/store.py`, `radar/runner.py` and how `members` is counted (`runner.py:460`–`:463`). A store that holds more open admitted episodes than `cap` is a separate item, opened from the desk's survey read.
- The rank column (`PoolRow.position = last_rank`, `radar_panel.py:511`, `:1018`). A sticky member may show a rank above 50 in a 50-row list (`pool.py:399`–`:427`). That is its own item if the survey read shows it.
- Banners, `BannerView` levels, `render_degraded_line`, `PANEL_JS`, `PANEL_CSS`, the ladder, `web.py` and any route.
- Any `src/` file but `radar_panel.py`; any test file but `test_radar_panel.py`.
- A red outside these rows goes under `## DECISIONS` as UNPROVEN (L70), with its output. It is never fixed here.

## READ
- `src/cobalt/aset/radar_panel.py`: `PoolRecord` (`:90`–`:107`), `MembershipRecord` (`:115`–`:141`), `PoolRow` (`:165`–`:184`), `PoolView` (`:195`–`:218`), `_row` (`:502`–`:529`), `build_pool_view` (`:532`–`:749`; current / departed / excluded `:630`–`:646`), `_pool_table` (`:1008`–`:1033`), `render_pool` (`:1042`–`:1077`).
- `src/cobalt/radar/store.py` `apply_membership` (`:81`–`:191`), `members_for_day` (`:55`–`:79`).
- `src/cobalt/radar/pool.py` `decide` seats and cap (`:382`–`:451`).
- `tests/cobalt/test_radar_panel.py`: `FakeRadarStore` (`:49`–`:63`), `_small_snapshot` (`:96`–`:125`), `_build` (`:128`–`:154`), `:838`–`:842`.

## RECORDS
- RESTARTS: expected `com.cobalt.aset com.cobalt.radar`. Class homes per `src/cobalt/jobs/restarts.py`: `src/cobalt/aset/radar_panel.py` is `static import reach` (`:220`); `tests/cobalt/test_radar_panel.py` is `test/documentation; no resident` (`:246`); the build report is `DOCS` (`:225`–`:228`). `com.cobalt.aset` (`configs/cobalt/jobs.yaml:39`) serves the page; `com.cobalt.radar` (`jobs.yaml:184`, `imports: [cobalt.cli]`, `:194`) reaches the module by import only.
- DB: every new test is offline (`FakeRadarStore`, `FakeSettingsStore`, `FakeClock`). The `DB` key is left out because `src/` and `tests/cobalt/` rows do not qualify for `none` (`CARD.md` `DB`).
- BASE at drafting: `0e84db6f` (`git -C /Users/cobalt/cobalt rev-parse main`, 2026-10-09 11:31 ET). `git -C /Users/cobalt/cobalt diff --stat HEAD -- src tests configs/cobalt/jobs.yaml` printed nothing. Every `file:line` above was read at that HEAD. The desk refills `BASE` if main moves.
- No production read at drafting. The survey read that tells the cause is `## DECISIONS` 1 in `reports/radar-top50-draft-2026-10-09.md`.
