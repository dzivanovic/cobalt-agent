# `src/cobalt/taxonomy/loader.py`

## What it does
Loads and cross-validates the taxonomy's YAML data: every trade_def,
its variable registry, and the Cameron H grid — config-as-code (TRIAGE
cross-cutting law). A bad or missing file crashes with the file path
and field detail; no partial loads, no default fallback.

## Key functions/classes
- `TaxonomyConfigError(RuntimeError)` — the one error type.
- `load_cameron_grid(path) -> dict[str, list[dict]]` — reads
  `cameron_grid.yaml`'s `valid_setups` mapping; validates shape
  (non-empty list of `{setup_ref, relation}` rows per trade_id).
- `load_variable_registry(trade_id, directory) -> VariableRegistry` —
  reads `<trade_id>.yaml`, raises if missing or invalid.
- `load_trade_defs(trade_defs_dir, variables_dir, cameron_grid_path)
  -> dict[id, TradeDef]` — for every `*.yaml` in `trade_defs_dir`:
  parses, constructs `TradeDef`, then cross-checks (a) `valid_setups[]`
  == its `cameron_grid.yaml` row exactly (as a set of `(setup_ref,
  relation)` pairs) and (b) `quality_factors[]` == its variable
  registry's names exactly, in both directions. First failure raises
  immediately — nothing partial is returned.
- `iter_tunables(obj) -> Iterator[Tunable]` — recursively walks a
  `TradeDef` (or any nested Pydantic model / list / dict) yielding every
  `Tunable` found. Pure introspection, no engine semantics. Used by
  `validate.py`'s CLI table and by the dynamic-tunables-in-backlog test.

## Data flow in/out
**In:** `configs/cobalt/taxonomy/trade_defs/*.yaml`,
`configs/cobalt/taxonomy/variables/*.yaml`,
`configs/cobalt/taxonomy/cameron_grid.yaml`.
**Out:** `dict[id, TradeDef]`, or a raised `TaxonomyConfigError`.

## Config it reads
`configs/cobalt/taxonomy/` (three sub-paths above) — `configs/cobalt/`
is the sanctioned new-core config location (CLAUDE.md's config boundary
law; same pattern as `archiver/config.py`'s watchlists loader).
