# `src/cobalt/replay/movers.py`

F13 (S2-P4 STEP-6, R5 as amended by R1-12/R1-13/R1-20/R2-5). This module
finds what moved that the pool never saw.

## Collection (`MoversCollector`, behind the collector interface, L9)
- `exports(top_n, now, cache, trade_date)`: two unfiltered screener exports.
  Gainers use `o=-change`, losers `o=change`; `v` and `c` come from
  `radar.yaml`, and there is **no filter string**. Each goes through
  `finviz_get` and the process TokenBucket after
  `check_scheduled_demand("replay", replay_top_n=top_n)`. With
  `cache=True` the raw bytes land in
  `data/radar-cache/<trade_date>/movers-<side>-HHMMSS.csv`. A dry run passes
  `cache=False` and writes no file.
- `bars(tickers, top_n)`: i1 fetches through the same bucket, after the same
  gate. A per-ticker failure is returned, not raised.
- `replay_request_count(top_n) = 2 + 2 × top_n` is replay's demand in the
  L53 total.

## Parsing (`parse_movers`)
It uses `radar.collector.parse_screener_csv` with `REQUIRED_HEADERS =
[Ticker, Change, Volume]`. Rows are ranked in export order, and that order
is **verified**: gainers must not increase and losers must not decrease,
otherwise it is the wrong sort or side. `Change` must be a percentage.
`Asset Type` and RVOL are read when their columns exist.

Real shape (corrected AT-1 2.5): the movers fixtures were first cut from a
21-column default view — a shape the collector never receives — and have
been re-cut from unfiltered exports fetched at the radar's own column set.
They now carry the same 151-column header as `pool-metrics.real-shape.csv`,
byte for byte, `Asset Type` included; a test asserts that one shape across
all three fixtures. Finviz fills `Asset Type` only for funds, so most rows
are **blank** and a handful are not, and the fixture holds both. A blank
cell and an absent column both read as `None` ("unreported"), which is
never guessed to mean equity or not.

The exports are a different trading day from `membership-day.real-shape
.json`, so the fixtures' pool overlap is real but smaller than the first
cut's; each benchmark test names the row that actually carries its case.

`MoversCollector._params` takes `c` from `radar.config.screener_columns_param`
— the one column-set source (AT-1 2.3, L3) — so the fixture's shape and the
live request's shape cannot drift apart silently.

## History (`retained_exports`)
A past `--date` reads the latest retained `movers-<side>-*.csv` for that
date. If none is retained it refuses (R1-20); it never relabels a live
fetch.

## The benchmark (`benchmark_misses`, pure)
Per ticker (both sides merged, and the larger |change| carries the row):
- if |change| < `min_move_pct`, skip.
- if the asset type is in `radar.yaml` `not_equity.values`, skip. An
  unreported type stays in.
- any admitted episode (`entered_at` set) means in play: no row.
- only never-admitted episodes: `excluded_by` comes from the most recent
  one (by `first_seen_at`, then id) and must be one of `config_cap,
  not_equity, screen_inactive, manual`, else refuse.
- no episode means `not_in_any_source`.

`gate_detail` holds change_pct, side, rank, every side the ticker appeared
on, asset_type (or `unreported`), the threshold and the episodes. The
receipt inputs hold the mover rows (id, export sha), episodes, settings and
not-equity values. There is no cf-R: without a trade_def there is no trigger.

## The archive (`archive_movers`)
Each top-N ticker whose stored i1 bars do not cover RTH open → close
(`cards.coverage`) is fetched and upserted, then **re-checked**. Only a
covered ticker's movers are `archived_ids`. A fetch that still leaves a gap
is `incomplete`, and a fetch error is a `failure`. A dry run, or a
historical run, fetches nothing and lists `would_fetch`. If the fetches
cannot finish before the deadline at the bucket rate, it refuses before the
first request (R1-16).

## `MoversStore` (SYSTEM side)
- `reconcile(run_id, trade_date, exports)`: one transaction with an
  advisory lock. Per side, an unchanged active row stays (same rank, values
  and export sha256). A changed or dropped row is set `active = false` and
  never deleted, so `"user".missed.mover_id` keeps its target. New rows are
  inserted with `replay_run_id`. It returns the active set.
- `active(trade_date)`, `mark_bars_archived(ids)`.

## Tests
`tests/cobalt/test_replay_movers.py` and `test_replay_demand.py`.
