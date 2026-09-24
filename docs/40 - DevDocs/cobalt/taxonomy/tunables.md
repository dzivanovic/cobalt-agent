# `src/cobalt/taxonomy/tunables.py`

## What it does
Schema for `configs/cobalt/taxonomy/tunables.yaml` (TAXONOMY-DRAFT-v0_7.md
§13.1, ADR-0003; `stop.buffer` added by ruling 09-03). Every
`config, dynamic` quantity named by the v0.6/v0.7 §0 "Dynamic
definitions" law is a row here — status/source/replay tracking,
referenced by key via the `cfg(key)` grammar atom from `Predicate.expr`
/ trigger `params` strings, and (as of 09-03) from any `Tunable[str]`
field's `value` too (`StopBuffer.cents` — same token, same
`loader.iter_cfg_tokens` walk, no special-casing). No engine semantics:
pure schema plus a `dynamic AND status != solidified` query
(`replay_backlog`). Replay writes `status`, never `value` — a value
change stays a Dejan ruling.

## Key functions/classes
- `TunableUnit` — `bars | min | atr | cents | count | pct | ratio |
  label | duration`.
- `TunableStatus` — `proposed | replay_pending | solidified |
  overridden`.
- `TunableSource` — `ruling | sheet | dwv`.
- `ReplayRecord {corpus_ref, result, date}` — the row's `replay?` field;
  written by a future replay session, never by this loader.
- `TunableRow {key, value: Any, unit, scope, dynamic, status, source,
  sheet_value?, consumers[], replay?}` — `scope` is regex-validated to
  `global | per_trade(<id>) | per_indicator(<ind>)`. `value` and
  `sheet_value` are `Any` (a band `[5, 20]`, a scalar, a label list, or
  `null` for a not-yet-ruled threshold).
- `TunableRegistry {tunables: list[TunableRow]}` — `model_validator`
  rejects duplicate `key`s; `.by_key` property = `{row.key: row}`.
- `replay_backlog(registry) -> list[TunableRow]` — `[row for row in
  registry.tunables if row.dynamic and row.status != solidified]`. The
  §13 backlog as a query, not a hand-maintained list
  (`docs/00 - Project/BACKLOG.md`'s old itemized section is now a
  one-paragraph pointer here).

## Data flow in/out
**In:** `configs/cobalt/taxonomy/tunables.yaml`, read once per
`load_trade_defs()` call by `loader.load_tunables()`. **Out:** a
validated `TunableRegistry`, or a raised `TaxonomyConfigError`.

## Config it reads
`configs/cobalt/taxonomy/tunables.yaml` — 33 rows: the 30 seeded at the
ADR-0003 commit from the §13.1 table's `dyn: yes` rows, plus 3 added by
ruling 09-03 (`stop.buffer` global + `back_through_open.stop.buffer` /
`bella_fade.stop.buffer` per-trade overrides — all `dynamic: false,
status: solidified`, so none add to `replay_backlog()`). Two of the
table's `dyn: no` global rows (`working_timeframe`, `ma.fast`/`ma.slow`)
remain deliberately excluded — they stay in `defaults.yaml`
(`defaults.py`); `loader.resolve_cfg` falls back there for
`working_timeframe`/`ma.*`. `stop.buffer` is IN as of 09-03, superseding
ADR-0003's original exclusion of it (see ADR-0003's amended paragraph)
— `trade_def.py`'s `StopBuffer.cents` (`Tunable[str]`) resolves it via
the same `cfg(key)` path as every other row here, with a per-trade
override row taking precedence for the two trades that reference it
directly. `catalyst.grade_min`/`_max` and `<trade>.max_attempts`/
`<trade>.reentry_window` (also `dyn: no`) remain excluded — they stay
as `Tunable[T]` fields directly on their trade_defs (`trade_def.py`),
not duplicated here.

## Cross-references
`loader.py` (`load_tunables`, `resolve_cfg`, `iter_cfg_tokens` — the
`cfg(key)` resolution path), `trade_def.py` (`Tunable[T]` — a distinct,
older per-field mechanism, not this registry), ADR-0003.
