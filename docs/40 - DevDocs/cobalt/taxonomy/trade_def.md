# `src/cobalt/taxonomy/trade_def.py`

## What it does
The `trade_def` Pydantic schema (TAXONOMY-DRAFT-v0_6.md §10.1, schema
v0.3, extended to v0.7 by TRADE-DEFS-BATCH2-v0_1.md §A / ADR-0002).
Models only — no predicate parser, no setup detectors, no bar logic.
Enums are the single source of truth for the taxonomy vocabulary; YAML
data must match them exactly or fail loud.

## Key functions/classes
- Enums (verbatim from v0.6 §10.1/§10.2/§3.6, extended per §A): `Family`,
  `TradeClass`, `Relation`, `EntryMode`, `SetupRef`, `RTHWindow`,
  `RangeBoundType`, `TriggerType` (gains `trendline_break`,
  `indicator_rejection` — A.3/A.4), `ConfirmationPolicyType`,
  `EvaluationType`, `StructuralRef` (the flat, literal §3.6 refs only —
  `cross_point{a,b}` and `leg_end(n)` are parametrized and carried as
  free-text anchors instead; gains `recent_lower_high`, A.7),
  `StopManagementType`, `ExitTargetType` (gains `trail`, A.7/A.8),
  `Event`, `OnCicActionType`, `IndicatorType` (`VWAP | EMA9 | EMA20 |
  EMA21`, A.2), `SnapshotType` (`at_entry | live`, A.2).
- `Predicate {expr | text}` — `expr` stores the §10.5 grammar string
  UNPARSED; `text` is the human fallback. Exactly one is set (enforced).
  `.computable` is `True` iff `expr` is set. The A.13–A.18 grammar atoms
  (`dist()`, `Catalyst.grade/.polarity`, `Regime.label`,
  `Range.counter_pivot_count`, `gap_retrace_pct`, `Leg(pullback).index`)
  are unparsed strings here too — no schema change needed for them.
- `Tunable[T] {value, dynamic, note}` — `dynamic=True` marks a v0.6 §0
  "Dynamic definitions" law value; must appear in the §13 replay
  backlog (enforced by `loader.iter_tunables` + a test, not by this
  model). A `Tunable[str]` whose value matches `ma.fast`/`ma.slow` is
  resolved by `loader.resolve_ma_ref` against `defaults.py`'s
  `TaxonomyDefaults` at load time (A.8 MA-period note).
- `StopPlacement` = discriminated union of `StructuralExtremePlacement
  | MeasuredFractionPlacement | LevelPlacement | IndicatorPlacement`
  (A.2) — reused by both the top-level `Stop.placement` and
  `RaiseToMgmt.placement`, so "any stop-placement" is one type, not
  two; `IndicatorPlacement` joining the union means it is valid inside
  `raise_to` too with no extra code.
- `StopManagementEntry` = discriminated union over `StopManagementType`
  (`FixedMgmt`, `BreakevenAtMgmt`, `RaiseToMgmt`, `TrailMaCloseMgmt`,
  `TrailBarMgmt`, `TimeStopMgmt`, `PassiveMgmt`), each carrying `on:
  EventRef` (default `entry`).
- `Trigger` = discriminated union of `SimpleTrigger` (bar_break /
  range_break / indicator_cross / trendline_break / indicator_rejection
  — `params` stays an unstructured dict for all five; A.3/A.4's
  `ref`/`anchor_leg`/`pivots`/`indicator`/`contact` are dict keys, not
  new fields) and `SequenceTrigger` (steps of `TriggerStep {name,
  predicate, confirmation_policy}` — `confirmation_policy` is optional:
  Second Chance's retest step carries none in the source sheet).
- `TrailCondition` (A.7) = discriminated union of
  `PriorBarBreakCondition {n=1}`, `MaCloseCondition {ma: Tunable[str]}`,
  `VwapCloseCondition`, `LevelCondition {level_ref}`. `TrailExitParams
  {conditions[] (min 1), mode: "any"}` validates an `ExitLeg`'s `params`
  ONLY when `target_type == trail` — every other target type keeps its
  unstructured `params` dict, same as Batch 1.
- `TradeDef` — the full registry entry. `class` is aliased to
  `trade_class` (Python keyword). `extra="forbid"` everywhere.
  `reentry_window: Tunable[str] | None = None` (A.1) — validated against
  `^\d+ min$`. Validators (fail loud, all `ValueError` → surfaces as a
  Pydantic `ValidationError` with field path):
  - `tf_ceiling == 15` iff `class == scalp`, else `None`.
  - `exit[].fraction` sums to `1.0 ± 0.01`.
  - `quality_factors[]` contains `setup_relation`, `market_alignment`,
    `sector_alignment`.
  - `reference_stats` carries no `ev`/`expectancy` key (case-insensitive).
  - `StopBuffer.type` is structurally `Literal["fixed"]` (no `spread` —
    v0.6 §14 ruling 3) with `cents.value > 0`. (A buffer *value* other
    than the 0.02 default is legal here — it only WARNS, in
    `loader.py`, not a schema-level rejection; see A.6 in `loader.md`.)
  - `raise_to.placement` validity is structural (the `StopPlacement`
    union itself), not a separate check.
  - `reentry_window` format (`<N> min`).
  - `ExitLeg`'s `trail`-params-valid check (above).

`Level.type` gaining `open` (A.5) is **not** a code change here —
`Level_ref` values are already free strings everywhere they appear
(`LevelPlacement.level_ref`, trigger `params` dicts); `Level.type` is
design-tree vocabulary (`TAXONOMY-DRAFT-v0_3.md` line 27), not
Pydantic-enforced in this module. See ADR-0002.

## Data flow in/out
**In:** a `dict` from `loader.load_trade_defs` (parsed YAML under a
trade_def's `trade_def:` key). **Out:** a validated `TradeDef`, or a
raised `pydantic.ValidationError`.

## Config it reads
None directly — pure schema. `configs/cobalt/taxonomy/trade_defs/*.yaml`
is read by `loader.py`, which constructs `TradeDef` instances from it.
`defaults.yaml` (via `loader.resolve_ma_ref`) is the one indirect
config dependency, for `ma.*` refs.

## Cross-references
`configs/cobalt/taxonomy/cameron_grid.yaml` (valid_setups cross-check,
enforced in `loader.py` not here) · `variables.py` (quality_factors
cross-check, also `loader.py`) · `defaults.py` (`TaxonomyDefaults`,
resolved by `loader.py`) · `docs/00 - Project/BACKLOG.md` § "Taxonomy
replay validation (v0.6 §13)" (dynamic tunables) · ADR-0001 · ADR-0002.
