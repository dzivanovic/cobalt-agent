# `src/cobalt/taxonomy/validate.py`

## What it does
`python -m cobalt.taxonomy.validate` — the CLI entry point. Loads every
trade_def via `loader.load_trade_defs`, prints a summary table, exits
non-zero on any failure. No partial output: a load failure prints the
error to stderr and returns before any table is drawn.

## Key functions/classes
- `main() -> int` — 0 on success, 1 on `TaxonomyConfigError`.
- Table columns: `id | class | families | #preconditions |
  #text-fallbacks | #tunables`. `#text-fallbacks` counts non-computable
  `Predicate`s (i.e. `text`-only) across `preconditions` + `radar_watch`
  + `avoid`. `#tunables` counts every `Tunable` found by
  `loader.iter_tunables`.
- **Tunables summary line (new, ADR-0003)** — after the table and the
  "N trade_def(s) validated OK." line, `main()` loads
  `tunables.yaml` (`loader.load_tunables`) and prints total row count
  plus `len(tunables.replay_backlog(registry))` — the §13 replay
  backlog size at a glance, no separate command needed.

## Data flow in/out
**In:** nothing (reads the default `configs/cobalt/taxonomy/` paths via
`loader.py`). **Out:** stdout table + tunables summary + exit code;
stderr + exit 1 on failure. A.6 stop-buffer warnings (non-fatal,
ADR-0002) print to stderr via Python's default `warnings` handler,
alongside the table — they never change the exit code. The trailer line
still reads "13 trade_def(s) validated OK." (schema v0.4, ADR-0003 —
trade count unchanged).

## Config it reads
Indirectly, via `loader.load_trade_defs()`'s defaults — see
`loader.md`.
