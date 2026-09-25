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

## 2026-09-24 — float handicap H1 (shadow; his R26 "B")

When the pool block carries a `handicap:` sub-block, `decide()` makes ONE
call to `handicap.shadow_rank` right after `_ranked()` (`pool.py:358`),
inside ONE `try`. The step computes each ranked name's would-be POOL-WIDE
rank — `Decimal(raw_rank) ÷ factor`, re-sorted by `(eff, handicapped,
raw_rank)` — and nothing else in `decide()` reads it: `_ranked()`,
`_metric_position`, `ordered`, `ranks`, stickiness and every admission are
byte-for-byte what they were, so in shadow the pool's order is unchanged.
Every `Transition` whose `rank` comes from `ranks` now also carries
`raw_rank` (equal to `rank` in H1) and, when the step ran, the name's
`handicap_factor` and `HandicapRecord`; a HOLD carries none (held members
are not re-ranked). If the step raises, the catch logs one ERROR, stores
the two handicap fields NULL, ranks raw, and appends `handicap` with the
exception class to `Decision.degraded_sources` / `Decision.reasons` — the
resident never loses a cycle to a feature that sorts nothing (L9). A
`mode: live` block is stored exactly like shadow and flagged `handicap`
(`mode live needs H2 — ranking raw`). The pool-level `degraded` flag stays
the sources': a handicap problem leaves every raw rank valid. `decide()`
takes `handicap_headers` (keyword) for the dead-column reason's header
names.
