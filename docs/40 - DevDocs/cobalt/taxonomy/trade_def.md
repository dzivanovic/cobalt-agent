# `src/cobalt/taxonomy/trade_def.py`

## What it does
The `trade_def` Pydantic schema (TAXONOMY-DRAFT-v0_7.md §10.1, schema
**v0.4** — `SCHEMA_VERSION = "0.4"` — extended from v0.3 by Batch 2's
§A / ADR-0002, then folded to v0.7 / v0.4 by ADR-0003: one-stop trail
slot, removed `trail_ma_close`/`trail_bar`/standalone `ma_close`, class
definitions rewritten). Models only — no predicate parser, no setup
detectors, no bar logic. Enums are the single source of truth for the
taxonomy vocabulary; YAML data must match them exactly or fail loud.

## Key functions/classes
- Enums (verbatim from v0.7 §10.1/§10.2/§3.6): `Family`, `TradeClass`
  (docstring = v0.7 §0's class definitions verbatim: trailing vs hard
  exit defines no class, legs-out count defines no class; `scalp` =
  usually sub-15-min TF, seconds to ~45 min; `move2move` = a momentum
  move surviving consolidation to a further target, usually 5-min+),
  `Relation`, `EntryMode`, `SetupRef`, `RTHWindow`, `RangeBoundType`,
  `TriggerType`, `ConfirmationPolicyType`, `EvaluationType`,
  `StructuralRef` (the flat, literal §3.6 refs only —
  `cross_point{a,b}`, `leg_end(n)`, and now `Range(micro).top`/`.base`
  are parametrized and carried as free-text anchors instead),
  `StopManagementType` (`trail_ma_close`/`trail_bar` REMOVED — ADR-0003,
  one-stop law), `ExitTargetType` (standalone `ma_close` REMOVED; `trail`
  now takes NO params — the trail slot is the only place conditions
  live), `Event`, `OnCicActionType`, `IndicatorType`, `SnapshotType`.
- `Predicate {expr | text}` — unchanged: `expr` stores the §10.5 grammar
  string UNPARSED; `text` is the human fallback. `cfg(key)` tokens (the
  v0.7 §13.1 grammar atom) are plain substrings inside `expr` — no
  parsing here, `loader.iter_cfg_tokens`/`resolve_cfg` do the
  token-scan + resolution at load time.
- `Tunable[T] {value, dynamic, note}` — unchanged mechanism for
  structured per-field values (`max_attempts`, `reentry_window`,
  `duration_bars`, MA refs). **Not** the same thing as a `tunables.py`
  `TunableRow`: this stays a per-field marker; `tunables.yaml` is now
  the canonical registry + replay-status bookkeeping for the v0.6/v0.7
  §0 "Dynamic definitions" law values (see `tunables.md`). A
  `Tunable[str]` whose value matches `ma.fast`/`ma.slow` is still
  resolved by `loader.resolve_ma_ref` against `defaults.py` at load
  time (unchanged).
- `StopPlacement` = discriminated union of `StructuralExtremePlacement
  | MeasuredFractionPlacement | LevelPlacement | IndicatorPlacement` —
  reused by both `Stop.placement` and `RaiseToMgmt.placement`.
- **`StopBuffer.cents: Tunable[str]` (ruling 09-03, was `Tunable[float]`)**
  — `cents.value` is now a `cfg(key)` reference (default
  `"cfg(stop.buffer)"`), never a literal; `_cents_is_cfg_ref` (rewritten
  from the old `_positive_cents`) rejects anything not matching
  `^cfg\([a-zA-Z0-9_.]+\)$`. Resolved the same way as every other
  `cfg()` token — generically, by `loader.iter_cfg_tokens`/`resolve_cfg`
  walking the `TradeDef` tree (no special-case code needed, since
  `Tunable[str].value` is just another string field). Per-trade
  override = the trade's own YAML referencing `cfg(<trade_id>.stop.buffer)`
  directly instead of the global `cfg(stop.buffer)` — `back_through_open`
  and `bella_fade` do this (their sheets say 0.01; `tunables.yaml`
  carries the ruled 0.02 as `value` and 0.01 as `sheet_value`, an A.6
  PROPOSAL record). See `tunables.md` and ADR-0003 (amended).
- `StopManagementEntry` = discriminated union over `StopManagementType`
  (`FixedMgmt`, `BreakevenAtMgmt`, `RaiseToMgmt`, `TimeStopMgmt`,
  `PassiveMgmt` — `TrailMaCloseMgmt`/`TrailBarMgmt` deleted), each
  carrying `on: EventRef` (default `entry`).
- `Trigger` = discriminated union of `SimpleTrigger` (bar_break /
  range_break / indicator_cross / trendline_break / indicator_rejection
  — `params` stays an unstructured dict for all five) and
  `SequenceTrigger` (steps of `TriggerStep {name, predicate,
  confirmation_policy}` — optional policy).
- **`TrailSpec` (new, ADR-0003)** — `{conditions: list[TrailCondition]
  (min 1), mode: Literal["select"] = "select", on: EventRef (default
  entry)}`. `TrailCondition` = discriminated union of
  `PriorBarBreakCondition {n: Literal[1] = 1}` (pinned, not merely
  defaulted — 1-bar trail law), `MaCloseCondition {ma: Tunable[str]}`,
  `VwapCloseCondition`, `LevelCondition {level_ref}` — unchanged from
  Batch 2 except `PriorBarBreakCondition.n`'s pin and its new home.
- `TradeDef` — the full registry entry. `class` is aliased to
  `trade_class`. `extra="forbid"` everywhere. **`trail: TrailSpec | None
  = None`** (new field — ONE slot per trade_def). Validators (fail
  loud, all `ValueError` → surfaces as a Pydantic `ValidationError`
  with field path):
  - **`model_validator(mode="before")` `_reject_removed_trail_spellings`**
    (new) — scans the raw `stop_management[]`/`exit[]` dicts for
    `trail_ma_close`/`trail_bar`/standalone `ma_close` BEFORE the
    discriminated-union parse runs, so the error names the trail slot
    directly instead of Pydantic's generic discriminator message.
  - **`_trail_slot_required_for_trail_exit`** (new) — any exit leg with
    `target_type == trail` requires `self.trail is not None`.
  - `ExitLeg._trail_takes_no_params` (rewritten) — `target_type == trail`
    requires `params == {}`; conditions live only on `trade_def.trail`
    now, never per-leg (`TrailExitParams` deleted).
  - `tf_ceiling == 15` iff `class == scalp`, else `None`.
  - `exit[].fraction` sums to `1.0 ± 0.01`.
  - `quality_factors[]` contains `setup_relation`, `market_alignment`,
    `sector_alignment`.
  - `reference_stats` carries no `ev`/`expectancy` key (case-insensitive).
  - `StopBuffer.type` is structurally `Literal["fixed"]`; `cents.value`
    must be a `cfg(key)` reference (see above). The A.6 "sheet differs
    from ruled value" flag now lives structurally on the tunable row
    (`sheet_value != value` in `tunables.yaml`) — `loader.py` no longer
    warns at load time (the old `DEFAULT_STOP_BUFFER_CENTS`
    literal-comparison check is gone; ruling 09-03).
  - `reentry_window` format (`<N> min`).

`Level.type` gaining `open` (A.5) is still **not** a code change — see
ADR-0002 (unaffected by this ADR).

## Data flow in/out
**In:** a `dict` from `loader.load_trade_defs` (parsed YAML under a
trade_def's `trade_def:` key). **Out:** a validated `TradeDef`, or a
raised `pydantic.ValidationError`.

## Config it reads
None directly — pure schema. `configs/cobalt/taxonomy/trade_defs/*.yaml`
is read by `loader.py`. `defaults.yaml` (via `loader.resolve_ma_ref` /
`resolve_cfg`) and `tunables.yaml` (via `resolve_cfg`) are the indirect
config dependencies.

## Cross-references
`configs/cobalt/taxonomy/cameron_grid.yaml` (valid_setups cross-check,
in `loader.py`) · `variables.py` (quality_factors cross-check, also
`loader.py`) · `defaults.py` (`TaxonomyDefaults`) · `tunables.py`
(`TunableRegistry`, `replay_backlog`) · `docs/00 - Project/BACKLOG.md`
§ "Taxonomy replay validation (v0.7 §13/§13.1)" (now a pointer to
`tunables.yaml`) · ADR-0001 · ADR-0002 (superseded for trail) ·
ADR-0003.
