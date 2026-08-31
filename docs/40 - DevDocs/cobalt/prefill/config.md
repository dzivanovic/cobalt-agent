# `src/cobalt/prefill/config.py`

## What it does
Config-as-code loaders for the three prefill-specific config files.
Fail-loud, Pydantic-validated, no silent defaults — same discipline as
`aset/config.py`. Deliberately does NOT duplicate the daily note's own
directory/filename pattern (that stays in `AsetConfig.daily_note`,
`configs/dev/aset*.yaml`) — callers read that directly (one-path rule).

## Key functions/classes
- `RECOGNIZED_TAGS` / `RuleCategory` — the six Obsidian tags Rules.md's
  lines are tagged with (`process`/`sizing`/`time_window`/`re_entry`/
  `circuit_breaker`/`hard_stop`); `RuleCategory` is `Literal[RECOGNIZED_TAGS]`.
- `RuleItem` — `id` (now `rule_NN`, positional off Rules.md's own
  numbering — no more hand-authored semantic ids), `category`, `text`.
  No more `source` field (Slice 2.1: Daily.md is not a source at all now).
- `MantraItem`, `GeneratedMeta` (`source`, `source_sha256`, `generated_at`
  — **new, Slice 2.1**: `rules.yaml` is a generated artifact, this is its
  provenance stamp) — `RulesConfig.generated` is required, so a stale/
  hand-edited `rules.yaml` missing it fails validation outright.
- `StrategyItem` / `StrategiesConfig` — `strategies.yaml`'s shape;
  `StrategiesConfig.is_reversion(name)` is the one lookup callers use
  (unknown/blank strategy → `False`, never a guess).
- `PrefillPathsConfig` — `prefill.yaml`'s shape (trades_dir, review_dir,
  drc_filename_pattern, trade_filename_pattern).
- `load_rules_config()` — reads the STATIC committed `rules.yaml` file
  as-is. Fine for tests/inspection; `daily.py`/`drc.py` don't call this
  for a live rules block anymore — see `rules_gen.regenerate_rules_config()`.
- `load_strategies_config()`, `load_prefill_paths()`.
- `PrefillConfigError` — the one error type, raised on any missing/
  invalid file (`rules_gen.RulesSourceError` subclasses nothing here —
  it's its own `RuntimeError`, see that module).

## Data flow in/out
**In:** `configs/cobalt/rules.yaml`, `configs/cobalt/strategies.yaml`,
`configs/cobalt/prefill.yaml`. **Out:** validated Pydantic models, or a
raised `PrefillConfigError`.

## Config it reads
All three files above. `rules.yaml`'s real provenance is now the
vault's Rules.md — see `rules_gen.py`, not this module, for how it gets
(re)written. `strategies.yaml` is a seed list off the Individual Trade
Template's own Strategy dropdown.
