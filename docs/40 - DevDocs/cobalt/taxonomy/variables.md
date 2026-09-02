# `src/cobalt/taxonomy/variables.py`

## What it does
The variable-registry stub schema — one file per trade_def, one entry
per `quality_factors[]` item. Stub only: `why_template` empty,
`status="stub"` until the grading engine sprint fills these in.

## Key functions/classes
- `VariableRegistryEntry` — `name`, `scale_min: int = 1`, `scale_max:
  int = 10` (the sheet's "scale: 1-10"), `source: cobalt |
  cobalt-degraded | human` (default `human`), `tier: deterministic |
  judgment` (default `judgment`), `why_template: str = ""`, `status: str
  = "stub"`. `extra="forbid"`.
- `VariableRegistry` — `trade_id`, `variables: list[VariableRegistryEntry]`
  (non-empty). Validator: no duplicate `name` within the file.
  `.names -> set[str]` — the set of registered variable names, used by
  `loader.py` to cross-check against a trade_def's `quality_factors[]`.

## Data flow in/out
**In:** a `dict` from `loader.load_variable_registry` (parsed YAML).
**Out:** a validated `VariableRegistry`, or a raised
`pydantic.ValidationError`.

## Config it reads
None directly — pure schema. `configs/cobalt/taxonomy/variables/<trade_id>.yaml`
is read by `loader.py`.

## Cross-references
`trade_def.py`'s `TradeDef.quality_factors[]` (loader.py enforces the
two must name the same set, in both directions) · ADR-0001.
