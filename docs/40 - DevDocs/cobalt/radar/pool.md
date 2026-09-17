# `src/cobalt/radar/pool.py`

Pure D3 ranking and membership decision logic. It keeps metric positions separate, applies source priority and first-screen precedence, enforces a hard cap with degraded holds, preserves sticky streaks, manages never-admitted episodes, and closes prior-day episodes at aftermarket close.

The decision boundary accepts validated `PoolOverride` instances and JSON-shaped
override mappings. This matters for replay/test variants built with Pydantic's
non-validating `model_copy(update=...)`; note parsing itself remains strict.

---

## 2026-09-17 — S2-P4: rank metric value (ruling R1)

`_ranked` now returns `(ordered, ranks, source_for, values)`. For each
ticker, `values[ticker]` is `(metric, value)` for the metric that actually
ranked it:
- screen-sourced: the winning screen's override metric, else the session
  metric, with that screen's value for the ticker;
- list-sourced: the session metric and the max across its lists (the same
  expression the list ordering uses).

A missing value stays None. Values pass through `str` into `Decimal`, so
the NUMERIC column stores the digits the export carried.

`Transition` gains `rank_metric`/`rank_value`. `decide` sets them on
RETAIN, ADMIT and EXCLUDE. HOLD carries the member's prior pair from
`OpenMember`. LEAVE carries none.

Fixed alongside: the list-union sort key filtered None only in the outer
comparison. A ticker with a value on one list and none on another raised
`TypeError` inside `max`. The inner generator now drops None values.
