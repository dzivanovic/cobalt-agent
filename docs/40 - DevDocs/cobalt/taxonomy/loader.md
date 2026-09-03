# `src/cobalt/taxonomy/loader.py`

## What it does
Loads and cross-validates the taxonomy's YAML data: every trade_def,
its variable registry, the taxonomy-wide defaults, the tunable
registry, and the Cameron H grid — config-as-code (TRIAGE cross-cutting
law). A bad or missing file crashes with the file path and field
detail; no partial loads, no default fallback. Two deliberate
exceptions to "crashes": the A.6 buffer check WARNS, and an unresolved
`cfg(key)` token is folded into the same `TaxonomyConfigError`-raises
family (still fail-loud, not a warning).

## Key functions/classes
- `TaxonomyConfigError(RuntimeError)` — the one error type.
- `load_cameron_grid(path) -> dict[str, list[dict]]` — reads
  `cameron_grid.yaml`'s `valid_setups` mapping; validates shape
  (non-empty list of `{setup_ref, relation}` rows per trade_id).
- `load_defaults(path=DEFAULTS_PATH) -> TaxonomyDefaults` — reads
  `defaults.yaml` (`working_timeframe`, `ma.fast`/`ma.slow`), same
  fail-loud pattern as `load_cameron_grid`.
- **`load_tunables(path=TUNABLES_PATH) -> TunableRegistry`** (new,
  ADR-0003) — reads `tunables.yaml`, same fail-loud pattern.
- `is_ma_ref(value) -> bool` / `resolve_ma_ref(value, defaults) -> int`
  — `is_ma_ref` matches `^ma\.(fast|slow)$`; `resolve_ma_ref` looks the
  key up on a `TaxonomyDefaults`, raising `TaxonomyConfigError` for
  anything else. A literal indicator string (`"EMA9"`) is not an `ma.*`
  ref and is left untouched wherever it appears.
- **`resolve_cfg(key, tunables, defaults) -> Any`** (new, ADR-0003) —
  the ONE `cfg(key)` resolver (v0.7 §13.1): `tunables` dict (a
  `TunableRegistry.by_key`) first, else `defaults.working_timeframe` /
  `is_ma_ref`+`resolve_ma_ref` against `defaults`, else
  `TaxonomyConfigError`. Never silently falls back to a made-up value.
- **`iter_cfg_tokens(obj) -> Iterator[str]`** (new, ADR-0003) — same
  recursive-walk shape as `iter_tunables`/`iter_stop_buffers`, but for
  every `str` value reached it regex-scans (`cfg\(([a-zA-Z0-9_.]+)\)`,
  token scan only, no grammar parsing) and yields every key found.
- `load_variable_registry(trade_id, directory) -> VariableRegistry` —
  reads `<trade_id>.yaml`, raises if missing or invalid.
- `load_trade_defs(trade_defs_dir, variables_dir, cameron_grid_path)
  -> dict[id, TradeDef]` — for every `*.yaml` in `trade_defs_dir`:
  parses, constructs `TradeDef`, then cross-checks (a) `valid_setups[]`
  == its `cameron_grid.yaml` row exactly, (b) `quality_factors[]` == its
  variable registry's names exactly, in both directions (this is how
  the ADR-0003 `trail_fit` entries are enforced — a trade_def with a
  `trail` slot must list `trail_fit` in both places), (c) every
  `Tunable[str]` value that looks like an `ma.*` ref resolves against
  `defaults.yaml`, **(d) every `cfg(key)` token found by
  `iter_cfg_tokens` resolves via `resolve_cfg`** (new — loads
  `tunables.yaml` once up front, alongside `defaults.yaml`), and (e) —
  WARN, not raise — every `StopBuffer` matches the 0.02 default (A.6
  flag law). First *raising* failure crashes immediately; buffer
  warnings never abort a load.
- `iter_tunables(obj) -> Iterator[Tunable]` — recursively walks a
  `TradeDef` yielding every `Tunable[T]` field found (unrelated to
  `tunables.yaml`'s `TunableRow`s — see `tunables.md`). Used by
  `validate.py`'s CLI table and `load_trade_defs`'s `ma.*` ref
  resolution.
- `iter_stop_buffers(obj) -> Iterator[StopBuffer]` — same walk shape,
  yielding `StopBuffer` instances; used only by the A.6 warning check.

## Data flow in/out
**In:** `configs/cobalt/taxonomy/trade_defs/*.yaml`,
`configs/cobalt/taxonomy/variables/*.yaml`,
`configs/cobalt/taxonomy/cameron_grid.yaml`,
`configs/cobalt/taxonomy/defaults.yaml`,
`configs/cobalt/taxonomy/tunables.yaml`.
**Out:** `dict[id, TradeDef]`, or a raised `TaxonomyConfigError`; a
`UserWarning` on an A.6 buffer mismatch (non-fatal).

## Config it reads
`configs/cobalt/taxonomy/` (five sub-paths above) — `configs/cobalt/`
is the sanctioned new-core config location (CLAUDE.md's config boundary
law; same pattern as `archiver/config.py`'s watchlists loader).

## Cross-references
`trade_def.py` (schema), `tunables.py` (`TunableRegistry`, `TunableRow`,
`replay_backlog`), `defaults.py` (`TaxonomyDefaults`), `variables.py`
(`VariableRegistry`), ADR-0003.
