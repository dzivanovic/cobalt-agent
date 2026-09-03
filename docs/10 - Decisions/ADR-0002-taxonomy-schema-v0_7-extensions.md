# ADR-0002 — taxonomy schema v0.7 extensions (Batch 2)

Date: 2026-09-02
Status: Accepted

## Context

TRADE-DEFS-BATCH2-v0_1.md (closed 2026-09-02) rules 7 more trade_defs
(Gap Give and Go, VWAP Continuation, First VWAP Pullback, 9 EMA Scalp,
Back-Through Open, Bella Fade, Bouncy Ball) from full SMB sheets, plus
schema amendments A.1–A.8 (v0.3 → v0.7) and a variable-registry
tape-frontier law (§12). Same config-as-code decision as ADR-0001: this
is a data + schema commit, extending `src/cobalt/taxonomy/` and
`configs/cobalt/taxonomy/` in place — no engine code, no predicate
parser, no new detectors.

## Decision

- **`TradeDef.reentry_window: Tunable[str] | None`** (A.1, default
  null) — a duration string matching `<N> min` (validated by a new
  `field_validator`). Rules-gate intersection with the 08-27 re-entry
  rule (stricter wins) is a future rules-gate concern, not schema.
- **`IndicatorPlacement`** (A.2) joins `StopPlacement`
  (`structural_extreme | measured_fraction | level | indicator`):
  `indicator: VWAP | EMA9 | EMA20 | EMA21` (new `IndicatorType` enum),
  `buffer` (same `StopBuffer`, default 0.02), `snapshot: at_entry |
  live` (new `SnapshotType` enum, default `at_entry`), `floor: config`.
  Because it joins the existing `StopPlacement` union, it is
  automatically valid inside `raise_to.placement` too — no separate
  model needed there.
- **`trendline_break` / `indicator_rejection`** (A.3, A.4) join
  `SimpleTrigger`'s type literal (and `TriggerType`, for source-of-truth
  parity with the enum, though `SimpleTrigger.type` — as in Batch 1 —
  stays a raw `Literal` rather than referencing the enum directly).
  `params` stays an unstructured dict for both, consistent with every
  other simple-trigger type (`bar_break`, `range_break`,
  `indicator_cross`): `trendline_break`'s `ref`/`anchor_leg`/`pivots`
  and `indicator_rejection`'s `indicator`/`contact` are dict keys, not
  new Pydantic fields.
- **`StructuralRef` gains `recent_lower_high`** (A.7) — side-mirror of
  `recent_higher_low`, Bouncy Ball's stop.
- **Exit target `trail`** (A.7/A.8) — `ExitTargetType.TRAIL` plus four
  new condition models (`PriorBarBreakCondition {n=1}`,
  `MaCloseCondition {ma: Tunable[str]}`, `VwapCloseCondition`,
  `LevelCondition {level_ref}`) combined into a `TrailCondition`
  discriminated union, and `TrailExitParams {conditions[] (min 1),
  mode: "any"}`. Unlike every other exit target, `trail`'s `params`
  dict IS validated — a new `ExitLeg` model_validator runs
  `TrailExitParams(**params)` when `target_type == trail`, wrapping any
  `ValidationError` — so a malformed trail condition fails loud at load
  time instead of silently passing through as an opaque dict.
- **MA period resolution (A.8 note)**: new `configs/cobalt/taxonomy/
  defaults.yaml` (`working_timeframe: 2m`, `ma: {fast: 9, slow: 20}` —
  SMB sheets say 21, Dejan trades 20) and its schema,
  `src/cobalt/taxonomy/defaults.py` (`TaxonomyDefaults`). A `Tunable[str]`
  value of `"ma.fast"` / `"ma.slow"` is a resolvable ref
  (`loader.is_ma_ref` / `loader.resolve_ma_ref`); `load_trade_defs()`
  resolves every such ref against `defaults.yaml` at load time —
  fail-loud (`TaxonomyConfigError`) if a trade_def names an unknown
  `ma.*` key. A literal indicator name (`"EMA9"`) is left unresolved,
  same field, no ref.
- **A.6 stop-buffer flag law**: the default stop buffer stays fixed
  0.02; `loader.load_trade_defs()` now walks every `StopBuffer` in a
  loaded `TradeDef` (`iter_stop_buffers`, structurally identical to the
  existing `iter_tunables` walk) and `warnings.warn`s — never raises —
  when a buffer differs from 0.02, naming the file, trade id, and
  actual value. Batch 2's own sheets (Back-Through Open, Bella Fade)
  said 0.01 but were RULED to 0.02 before population, so no Batch 2
  trade_def actually triggers this warning; the path is proven by a
  synthetic fixture in `tests/taxonomy/test_trade_defs.py`.
- **Variable registry `frontier: bool`** (§12 tape law, not itself one
  of A.1–A.8 but ruled the same session): `VariableRegistryEntry` gains
  `frontier: bool = False`. Every tape-class read
  (`bids_hold`, `tape_flip`, `tape_read` — populated this batch;
  `buyers_defending_zone` is named in the law's example list but is not
  an actual `quality_factors[]` item of any of the 7 Batch 2 trades, so
  no registry entry exists for it yet) gets `source: human, frontier:
  true` — a capability-frontier flag, not a permanent law; it flips to
  `source: cobalt` with no schema change once an L2/T&S feed lands.
- **`Level.type` gains `open` (A.5) — no code change.** `open` (the RTH
  opening print) is design-tree vocabulary
  (`TAXONOMY-DRAFT-v0_3.md` line 27's Level.type enum, RULED 09-01), not
  a Pydantic-enforced enum anywhere in `src/cobalt/taxonomy/` — every
  place a `Level_ref` value appears (`LevelPlacement.level_ref`,
  trigger `params` dicts) already accepts a free string. Back-Through
  Open's `bar_break {ref: Level_ref(open)}` trigger is plain data:
  `params: {ref: "Level_ref(open)"}`.
- **Predicate/atom vocabulary — no code change.** `dist()`,
  `Catalyst.grade`, `Catalyst.polarity`, `Regime.label`,
  `Range.counter_pivot_count`, `gap_retrace_pct`, `Leg(pullback).index`
  are new grammar atoms (A.13–A.18) but `Predicate.expr` is already an
  unparsed string (ADR-0001) — they appear in Batch 2 YAML as plain
  `expr` text, same as every Batch 1 atom.
- **One flagged non-verbatim encoding**: Gap Give and Go's
  `stop_management[0].raise_to.placement` — §B.1 literally writes
  `structural_extreme {ref: Range(micro).top}`, but `Range(micro).top`
  is not a `StructuralRef` enum member (it is a parametrized Range
  field, the same class of thing as `leg_end(n)`/`cross_point{a,b}`,
  which the schema already routes through free-text anchors instead of
  the closed enum — see `trade_def.py`'s `StructuralRef` docstring).
  Encoded as `{type: level, level_ref: "Range(micro).top", buffer:
  {cents: 0.02}}` — the same precedent as Rubberband's Batch 1
  `breakeven` → `level{level_ref: entry}` encoding (ADR-0001). Flagged
  in a YAML comment at the source file, not silently reworded.

## Consequences

- 13 of 21 Cameron H grid trades now populated (`configs/cobalt/
  taxonomy/cameron_grid.yaml` already carried rows for all 7 new ids
  from the Batch 1 commit — no change needed there).
- The setups engine can still be built against this schema without
  another data migration: the new discriminated unions
  (`StopPlacement`, `TrailCondition`) and the `defaults.yaml` /
  `resolve_ma_ref` resolution point are load-bearing, not placeholders.
- §A is deliberately **not** folded into `TAXONOMY-DRAFT-v0_7.md` in
  this commit — that fold is the next planning session's job per the
  population task.
- Remaining 8 grid trades (opening_drive_pmh, opening_range_break,
  first_move_down, first_move_up, spencer_scalp, off_sides,
  the_330_trade, ema9_reclaim) stay `valid_setups[]`-only until sheets
  are found; Day 3 liquidity trap stays PLACEHOLDER (§11).
- **Superseded by ADR-0003 for trail** (2026-09-02, v0.7 §14 c.1): this
  ADR's exit-target `trail` (`mode: "any"`, per-leg `TrailExitParams`
  validated out of `ExitLeg.params`) and the Second Chance retrofit it
  describes are replaced by the one-stop-law `TradeDef.trail: TrailSpec`
  slot (`mode: "select"`) — `ExitTargetType.TRAIL` legs now carry no
  params at all. Every other decision in this ADR (indicator stop
  placement, `trendline_break`/`indicator_rejection`, `recent_lower_high`,
  MA-ref resolution, the A.6 stop-buffer warn-not-fail law, the
  `frontier` flag) is unaffected and stands as written.
