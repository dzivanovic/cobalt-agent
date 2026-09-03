# `src/cobalt/taxonomy/defaults.py`

## What it does
Schema for `configs/cobalt/taxonomy/defaults.yaml` — the taxonomy-wide
knobs Batch 2's trade_defs reference (TRADE-DEFS-BATCH2-v0_1.md §A.9,
§A.8 MA-period note; ADR-0002). Pure schema, same as `trade_def.py` /
`variables.py` — no engine semantics.

## Key functions/classes
- `MaDefaults {fast: int > 0, slow: int > 0}`.
- `TaxonomyDefaults {working_timeframe: str, ma: MaDefaults}`.

## Data flow in/out
**In:** a `dict` from `loader.load_defaults` (parsed
`defaults.yaml`). **Out:** a validated `TaxonomyDefaults`, or a raised
`pydantic.ValidationError`.

## Config it reads
None directly — pure schema. `configs/cobalt/taxonomy/defaults.yaml`
(`working_timeframe: 2m`; `ma: {fast: 9, slow: 20}` — SMB sheets say
21, Dejan trades 20) is read by `loader.py`.

## Cross-references
`loader.py`'s `resolve_ma_ref` / `is_ma_ref` (resolves a `Tunable[str]`
`"ma.fast"`/`"ma.slow"` value against this) and `resolve_cfg` (falls
back here for `working_timeframe`/`ma.*` when a `cfg(key)` token isn't a
`tunables.yaml` row) · `trade_def.py`'s `MaCloseCondition.ma` (the field
that can carry an `ma.*` ref — now reached via `TrailSpec.conditions`,
ADR-0003; `TrailMaCloseMgmt` was removed) · ADR-0002 · ADR-0003.
