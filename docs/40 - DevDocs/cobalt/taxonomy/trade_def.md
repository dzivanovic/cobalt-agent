# `src/cobalt/taxonomy/trade_def.py`

## What it does
The `trade_def` Pydantic schema (TAXONOMY-DRAFT-v0_6.md §10.1, schema
v0.3). Models only — no predicate parser, no setup detectors, no bar
logic. Enums are the single source of truth for the taxonomy
vocabulary; YAML data must match them exactly or fail loud.

## Key functions/classes
- Enums (verbatim from v0.6 §10.1/§10.2/§3.6): `Family`, `TradeClass`,
  `Relation`, `EntryMode`, `SetupRef`, `RTHWindow`, `RangeBoundType`,
  `TriggerType`, `ConfirmationPolicyType`, `EvaluationType`,
  `StructuralRef` (the flat, literal §3.6 refs only — `cross_point{a,b}`
  and `leg_end(n)` are parametrized and carried as free-text anchors
  instead), `StopManagementType`, `ExitTargetType`, `Event`,
  `OnCicActionType`.
- `Predicate {expr | text}` — `expr` stores the §10.5 grammar string
  UNPARSED; `text` is the human fallback. Exactly one is set (enforced).
  `.computable` is `True` iff `expr` is set.
- `Tunable[T] {value, dynamic, note}` — `dynamic=True` marks a v0.6 §0
  "Dynamic definitions" law value; must appear in the §13 replay
  backlog (enforced by `loader.iter_tunables` + a test, not by this
  model).
- `StopPlacement` = discriminated union of `StructuralExtremePlacement
  | MeasuredFractionPlacement | LevelPlacement` — reused by both the
  top-level `Stop.placement` and `RaiseToMgmt.placement`, so "any
  stop-placement" is one type, not two.
- `StopManagementEntry` = discriminated union over `StopManagementType`
  (`FixedMgmt`, `BreakevenAtMgmt`, `RaiseToMgmt`, `TrailMaCloseMgmt`,
  `TrailBarMgmt`, `TimeStopMgmt`, `PassiveMgmt`), each carrying `on:
  EventRef` (default `entry`).
- `Trigger` = discriminated union of `SimpleTrigger` (bar_break /
  range_break / indicator_cross) and `SequenceTrigger` (steps of
  `TriggerStep {name, predicate, confirmation_policy}` —
  `confirmation_policy` is optional: Second Chance's retest step
  carries none in the source sheet).
- `TradeDef` — the full registry entry. `class` is aliased to
  `trade_class` (Python keyword). `extra="forbid"` everywhere.
  Validators (fail loud, all `ValueError` → surfaces as a Pydantic
  `ValidationError` with field path):
  - `tf_ceiling == 15` iff `class == scalp`, else `None`.
  - `exit[].fraction` sums to `1.0 ± 0.01`.
  - `quality_factors[]` contains `setup_relation`, `market_alignment`,
    `sector_alignment`.
  - `reference_stats` carries no `ev`/`expectancy` key (case-insensitive).
  - `StopBuffer.type` is structurally `Literal["fixed"]` (no `spread` —
    v0.6 §14 ruling 3) with `cents.value > 0`.
  - `raise_to.placement` validity is structural (the `StopPlacement`
    union itself), not a separate check.

## Data flow in/out
**In:** a `dict` from `loader.load_trade_defs` (parsed YAML under a
trade_def's `trade_def:` key). **Out:** a validated `TradeDef`, or a
raised `pydantic.ValidationError`.

## Config it reads
None directly — pure schema. `configs/cobalt/taxonomy/trade_defs/*.yaml`
is read by `loader.py`, which constructs `TradeDef` instances from it.

## Cross-references
`configs/cobalt/taxonomy/cameron_grid.yaml` (valid_setups cross-check,
enforced in `loader.py` not here) · `variables.py` (quality_factors
cross-check, also `loader.py`) · `docs/00 - Project/BACKLOG.md` § "Taxonomy
replay validation (v0.6 §13)" (dynamic tunables) · ADR-0001.
