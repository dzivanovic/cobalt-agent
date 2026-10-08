# card 137 price floor — amend 4 · 2026-10-08

## §0 Headline
- Preflight r3 FAIL 12 fixed: three `Price` cells in `screen-handicap.real-shape.csv` rise above 5.00; fixture, `test_radar_handicap_group.py` and `test_radar_replay.py` are in F1's files.
- The sweep found one more hit r3 missed: `test_radar_replay.py:410` (`IMCC 4.23`, `QNME 0.56`). Fixed in the test.
- NOTE 2 and 3 done. SCOPE sentence added. No other row, header or `radar.yaml` design touched.

## CHANGES
Card `prompts/2026-10-08/137-price-floor-card.md`, edited in place:
- WHY (row F1 what): fixture sweep (a) and (b), `:93`–`:98` unchanged, `:83`–`:88` gains the fifth key `price`, and the SCOPE sentence.
- F1 files: `tests/fixtures/radar/screen-handicap.real-shape.csv`, `test_radar_handicap_group.py`, `test_radar_replay.py`; `test_radar_handicap_dry_run.py` and `test_radar_handicap_dead.py` named read-only (replaces "edits a fixture only if it breaks").
- Row M: `test_drc_k1_store.py` quotes new offsets: `names[-8:-5]`, `REVERSE[5]`, `REVERSE[6:8]`, proved.
- `## RECORDS`: new AMEND 4 line, the sweep.

## DECISIONS
1. Fixture, not test, for `screen-handicap`. Its only blank-float equities, `MSTZ` and `ZTG`, are the floored ones, so a test on surviving tickers has nothing to read. Cells become `12.35`, `12.18`, `11.64`. Candidates then equal BASE's, so the dry-run and dead-column tests stay green unedited.
2. Test, not fixture, for `test_radar_replay.py:410`. `movers-gainers` is shared with the movers tests and keeps its real prices. The test sets `Price` `10.00` on its four rows.
3. `movers-*` fixtures are full of sub-5.00 and blank prices but never reach `_collect`: no change.
4. `h1_support.py` builds no `MetricHeaders` by hand (`:121` reads `cfg`), contrary to F1's list. Left as written; harmless.
5. `tests/experiments/` reads the live cache and is on no gate list: noted, not edited.
6. Row R was not run (no `uv run`); not needed for this amend.

## RECORDS
- Read: card, preflight r3 (`## ISSUES`, check 12), `writing-rules.md`.
- Read: `test_radar_handicap_group.py` (whole), `test_radar_handicap_dry_run.py` (whole), `test_radar_handicap_dead.py:1`–`:194`, `test_radar_replay.py:192`–`:480`, `test_radar_runner.py:40`–`:125`, `test_radar_collector.py:60`–`:96`, `test_finviz_consumers.py:95`–`:155`, `test_drc_k1_store.py:105`–`:134`.
- Read: `handicap_dry_run.py:100`–`:250`, `collector.py:112`–`:210`, `radar/replay.py:50`–`:140`, `runner.py:500`–`:545`, `db_migrations/__init__.py` grep of `0016`–`0022`.
- Fixture scan (python, every `Ticker` CSV under `tests/fixtures/`): only `screen-handicap` (3 hits) and the movers files (many, not via `_collect`); `pool-metrics` has none; `daily-bars*` have no `Price`.
- `movers-gainers`: `IMCC 4.23`, `QNME 0.56`, `GEMG 12.03`, `SCOP 11.95`.
- Greps: `RadarRunner(|FinvizScreenerCollector(|ScreenerSnapshot(|CacheCollector|parse_screener_csv(|collect_scan(|_scan_replay|build_runner(|_collect(` over `src tests ops`; `SCREEN_FIXTURE|POOL_METRICS|_scan` over `tests`; `2.35|2.18|1.64|MSTZ|WETO` over `tests` (no pin on those prices); `"Price"` over the runner, evaluate, replay, daily test files (none); `tests/experiments` in `gate-lists.md` (0).
- HEAD `c3d5cd3c`; `git diff --stat 059da441 HEAD -- src configs tests ops` printed nothing, so every `file:line` is BASE's.

PRICE FLOOR CARD AMENDED4 · decisions: 6
