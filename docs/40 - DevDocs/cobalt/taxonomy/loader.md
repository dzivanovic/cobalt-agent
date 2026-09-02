# `src/cobalt/taxonomy/loader.py`

## What it does
Loads and cross-validates the taxonomy's YAML data: every trade_def,
its variable registry, the taxonomy-wide defaults, and the Cameron H
grid — config-as-code (TRIAGE cross-cutting law). A bad or missing file
crashes with the file path and field detail; no partial loads, no
default fallback. (Batch 2 / ADR-0002 additions below are the only
exception to "crashes" — the A.6 buffer check WARNS, deliberately.)

## Key functions/classes
- `TaxonomyConfigError(RuntimeError)` — the one error type.
- `load_cameron_grid(path) -> dict[str, list[dict]]` — reads
  `cameron_grid.yaml`'s `valid_setups` mapping; validates shape
  (non-empty list of `{setup_ref, relation}` rows per trade_id).
- `load_defaults(path=DEFAULTS_PATH) -> TaxonomyDefaults` — reads
  `defaults.yaml` (`working_timeframe`, `ma.fast`/`ma.slow`), same
  fail-loud pattern as `load_cameron_grid`.
- `is_ma_ref(value) -> bool` / `resolve_ma_ref(value, defaults) -> int`
  (A.8 MA-period note) — `is_ma_ref` matches `^ma\.(fast|slow)$`;
  `resolve_ma_ref` looks the key up on a `TaxonomyDefaults`, raising
  `TaxonomyConfigError` for anything else (callers check `is_ma_ref`
  first). A literal indicator string (`"EMA9"`) is not an `ma.*` ref
  and is left untouched wherever it appears.
- `load_variable_registry(trade_id, directory) -> VariableRegistry` —
  reads `<trade_id>.yaml`, raises if missing or invalid.
- `load_trade_defs(trade_defs_dir, variables_dir, cameron_grid_path)
  -> dict[id, TradeDef]` — for every `*.yaml` in `trade_defs_dir`:
  parses, constructs `TradeDef`, then cross-checks (a) `valid_setups[]`
  == its `cameron_grid.yaml` row exactly (as a set of `(setup_ref,
  relation)` pairs), (b) `quality_factors[]` == its variable registry's
  names exactly, in both directions, (c) every `Tunable[str]` value
  that looks like an `ma.*` ref actually resolves against
  `defaults.yaml` (loaded once up front), and (d) — WARN, not raise —
  every `StopBuffer` in the trade_def matches the 0.02 default (A.6
  flag law); a differing buffer is legal data, just flagged. First
  *raising* failure crashes immediately — nothing partial is returned;
  buffer warnings never abort a load.
- `iter_tunables(obj) -> Iterator[Tunable]` — recursively walks a
  `TradeDef` (or any nested Pydantic model / list / dict) yielding every
  `Tunable` found. Pure introspection, no engine semantics. Used by
  `validate.py`'s CLI table, the dynamic-tunables-in-backlog test, and
  `load_trade_defs`'s `ma.*` ref resolution.
- `iter_stop_buffers(obj) -> Iterator[StopBuffer]` — same walk shape as
  `iter_tunables`, yielding `StopBuffer` instances instead; used only
  by the A.6 warning check.

## Data flow in/out
**In:** `configs/cobalt/taxonomy/trade_defs/*.yaml`,
`configs/cobalt/taxonomy/variables/*.yaml`,
`configs/cobalt/taxonomy/cameron_grid.yaml`,
`configs/cobalt/taxonomy/defaults.yaml`.
**Out:** `dict[id, TradeDef]`, or a raised `TaxonomyConfigError`; a
`UserWarning` on an A.6 buffer mismatch (non-fatal).

## Config it reads
`configs/cobalt/taxonomy/` (four sub-paths above) — `configs/cobalt/`
is the sanctioned new-core config location (CLAUDE.md's config boundary
law; same pattern as `archiver/config.py`'s watchlists loader).
