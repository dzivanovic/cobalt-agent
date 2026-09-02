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
  = "stub"`, `frontier: bool = False` (TRADE-DEFS-BATCH2-v0_1.md §12 —
  a capability-frontier flag for a human-only tape-class read that
  flips to `source: cobalt` once an L2/T&S feed is ingested, no schema
  change; `bids_hold`/`tape_flip`/`tape_read` set it `True`, ADR-0002).
  `extra="forbid"`.
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
two must name the same set, in both directions) · ADR-0001 · ADR-0002
(`frontier` field).
