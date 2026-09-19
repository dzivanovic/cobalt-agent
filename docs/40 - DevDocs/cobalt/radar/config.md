# `src/cobalt/radar/config.py`

Loads strict engine-only `configs/cobalt/radar.yaml` and cross-checks all radar tunables and units. Unknown keys, missing headers, missing tunables, and wrong units fail naming their source file or row.

## The column set (AT-1 2.3)

`screener_columns()` is the ONE place a Finviz `c=` index list is produced, and `screener_columns_param()` renders it as the request parameter. It takes a declaration in either of the two shapes Finviz accepts — an inclusive `a-b` range, which is what `export.columns` ships, or an explicit comma list, which is what a screen note may declare instead — and returns the index list. Anything else raises `RadarConfigError`: a silently wrong column set does not fail where it is written, it returns a differently shaped export and surfaces as a header mismatch in whichever parser reads it next.

Four modules used to build the 151-index list for themselves (`radar/collector.py`, `radar/throttle.py`, `radar/propose.py`, `replay/movers.py`) — one export shape per copy the day the declaration changes, which is exactly the L3 failure. All four now call this function; `tests/cobalt/test_finviz_consumers.py` scans `src/cobalt` and fails if a fifth appears, and pins that the radar screen, both movers exports and the throttle probe send the same `c=`. The function deliberately tidies nothing: stripping backticks and whitespace off a trader's note belongs to `radar/propose.py`, which does that and then calls here.

`ContextConfig` (S2-P2) declares the context tickers — market and sector ETFs polled beside the pool for the alignment shadow dots. The `context` block is REQUIRED, so the total-demand check always has a number to count; an explicit empty `tickers: []` is a declared zero, and the alignment dots then render `CHECKPOINT_MISSING`. Tickers must be unique uppercase symbols. The list ships empty: STEP-0 found 11 of 14 context tickers without current bars, so no ticker is added until coverage is verified.
