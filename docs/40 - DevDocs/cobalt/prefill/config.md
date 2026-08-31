# `src/cobalt/prefill/config.py`

## What it does
Config-as-code loaders for the three prefill-specific config files.
Fail-loud, Pydantic-validated, no silent defaults — same discipline as
`aset/config.py`. Deliberately does NOT duplicate the daily note's own
directory/filename pattern (that stays in `AsetConfig.daily_note`,
`configs/dev/aset*.yaml`) — callers read that directly (one-path rule).

## Key functions/classes
- `RuleItem` / `MantraItem` / `RulesConfig` — `rules.yaml`'s shape
  (`id`, `category`, `text`, optional `source`).
- `StrategyItem` / `StrategiesConfig` — `strategies.yaml`'s shape;
  `StrategiesConfig.is_reversion(name)` is the one lookup callers use
  (unknown/blank strategy → `False`, never a guess).
- `PrefillPathsConfig` — `prefill.yaml`'s shape (trades_dir, review_dir,
  drc_filename_pattern, trade_filename_pattern).
- `load_rules_config()`, `load_strategies_config()`, `load_prefill_paths()`.
- `PrefillConfigError` — the one error type, raised on any missing/
  invalid file.

## Data flow in/out
**In:** `configs/cobalt/rules.yaml`, `configs/cobalt/strategies.yaml`,
`configs/cobalt/prefill.yaml`. **Out:** validated Pydantic models, or a
raised `PrefillConfigError`.

## Config it reads
All three files above — see each file's own header comment for
provenance (rules.yaml is a verbatim fold of the vault's Rules.md +
Daily.md's uncovered lines; strategies.yaml is a seed list off the
Individual Trade Template's own Strategy dropdown).
