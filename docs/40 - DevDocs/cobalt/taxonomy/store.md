# `src/cobalt/taxonomy/store.py`

## What it does
`TradeDefStore`, `SIDE = Side.USER`. Persists the loaded copy of the
vault's defs into `"user".trade_defs` / `"user".tunables`, and reads
`"user".setup_trade_matrix`.

## Key functions/classes
- `ensure_schema()` — runs `migrations/0001_trade_defs.sql`.
- `sync(result) -> SyncCounts` — one transaction for defs and tunables
  together (a per-trade row references its def).
- `slugs()`, `get(slug)`, `matrix()`, `tunable_keys()`.

## `sync` is a REPLACE, not a merge
Every def in the read is upserted, and every slug in the table the read
did not produce is DELETED. A def a trader removed from their note is a
def that stops existing — a row that outlived its note would be a
strategy the radar still fires on and the vault no longer documents. Both
counts AND the deleted slugs are named, because a delete nobody was told
about is the failure mode of a replace.

## Gotchas
`setup_trade_matrix` is a VIEW over `trade_defs.def`, so it covers
DEFINED trades only — a draft has no row in `trade_defs`. It was a second
YAML file the loader had to keep equal to the def; a view cannot disagree
with what it selects from.
