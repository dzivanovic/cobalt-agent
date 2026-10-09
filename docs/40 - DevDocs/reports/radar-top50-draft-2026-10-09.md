# radar-top50 draft — 2026-10-09

## §0 Headline
- MOST PROBABLE fault: the page never caps `Current admitted`. `build_pool_view` takes every open admitted episode of the day (`src/cobalt/aset/radar_panel.py:630`–`:632`) and checks only `len == pool.members` (`:633`); `render_pool` draws them all (`:1074`). So 51 rows with `members = 51` render 51 names.
- SECOND: 50 names with a sticky member showing rank `51` (rank column = `last_rank`, `radar_panel.py:511`, `:1018`; sticky RETAIN past the seats, `radar/pool.py:399`–`:427`).
- HOLD and LEAVE are not drawn twice: a row carries no action (`radar_panel.py:115`–`:141`); a HOLD is one updated row (`radar/store.py:114`–`:129`); a LEAVE moves the row to Departed (`store.py:130`–`:138`, `radar_panel.py:637`–`:639`).
- The code alone cannot tell which of the two he saw. `## DECISIONS` 1 gives the survey read.

## CARD
- `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/154-radar-top50-card.md`. Row A is red: 50 rows + `T51` past `cap` renders 50 in `Current admitted` and `T51` in `Over cap — open admitted beyond cap`. Row B is the control: 50 rows render 50, there is no over-cap section, and the pins hold. Row C is restarts.
- One seam (`PoolView.over_cap`, excluded from JSON), DB-free, one `src/` file.

## DECISIONS
1. ASK DESK: run this read-only survey read before or beside the build? [11:31 ET] It is on the system side, where `RadarStore.SIDE = Side.SYSTEM` (`radar/store.py:29`), and holds no `%`:
   `COBALT_ENV=production uv run cobalt db query --side system --prod "SELECT p.cap, p.members, p.last_scan_id AS pool_scan, m.id, m.ticker, m.last_rank, m.below_cap_streak, m.last_scan_id, m.entered_at FROM radar_pool p JOIN radar_membership m ON m.pool_key = p.pool_key AND m.entered_at IS NOT NULL AND m.left_at IS NULL AND m.trade_date = (p.last_scan_at AT TIME ZONE 'America/New_York')::date ORDER BY m.last_rank NULLS LAST, m.id"`
   How to read it:
   - 51 rows and `members = 51`: the fault is the one this card fixes, plus a store fault to open as its own item.
   - A row whose `last_scan_id` is below `pool_scan`: that episode was not touched by the last `decide`, so it is stale.
   - 50 rows with a `last_rank` of 51 or more: the second cause. The card's display is still right, but it does not change what he saw.
   DEFAULT: the desk runs the read beside the build, and the card launches as drafted.
2. ASK DESK: should over-cap names also raise a banner or appear in the red line above the ladder? [11:31 ET] DEFAULT: no. Use the section only. The `51 / 50 admitted` header (`radar_panel.py:1071`) already shows the overflow, and banner levels stay unchanged.
3. ASK DESK: which rows go past `cap`? [11:31 ET] DEFAULT: the tail of the existing order `(last_rank, id)` (`radar_panel.py:641`–`:643`). The page cannot name the held or leaving member, because the row carries no action.

## RECORDS
- Read at `0e84db6f` (`git -C /Users/cobalt/cobalt rev-parse main` → `0e84db6fdfcd17c32fa888a1e16680e82e6d2a41`). `git -C /Users/cobalt/cobalt diff --stat HEAD -- src tests configs/cobalt/jobs.yaml` printed nothing. Time: `date` → 11:31 EDT.
- Read: `src/cobalt/radar/pool.py` (whole file; `decide` `:230`–`:462`, the cap assertion `:450`–`:451`).
- Read: `src/cobalt/aset/radar_panel.py` `:90`–`:224`, `:500`–`:749`, `:1005`–`:1084`, plus a grep for admitted/held/leave/top.
- Read: `src/cobalt/radar/store.py` `:30`–`:229`, plus a grep for `SIDE =` (`:29`).
- Read: `src/cobalt/radar/runner.py` `:190`–`:479` (members count `:460`–`:463`, frozen branch `:461`).
- Read: `tests/cobalt/test_radar_panel.py` `:20`–`:244` and `:815`–`:849`.
- Grep: `tests/cobalt/test_radar_panel_cards.py` pins `:480`, `:482`; `tests/fixtures/radar/panel-pool.real-shape.json:16838` (`"cap": 50`); `src/cobalt/radar/models.py:120`, `:124`.
- RESTARTS class homes: `src/cobalt/jobs/restarts.py:220` (static import reach → `radar_panel.py`), `:246` (test/documentation → `test_radar_panel.py`), `:225`–`:228` (DOCS → reports). Units: `configs/cobalt/jobs.yaml:39` `com.cobalt.aset`, `:184` `com.cobalt.radar`, `:194` `imports: [cobalt.cli]`.
- Read: `prompts/CARD.md`, `prompts/2026-10-08/118-radar-display-fix-card.md`, `reports/cto-2026-10-09.md:9` (R716), `Memory/topics/writing-rules.md`.
- `ls` of `reports/radar-top50-build-2026-10-09.md` → no such file.
- No production read, no DB, no git write.

RADAR TOP50 CARD DRAFTED · decisions: 3
