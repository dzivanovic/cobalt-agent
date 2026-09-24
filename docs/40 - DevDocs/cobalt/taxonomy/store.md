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
- `loaded_for_evaluation() -> (list[LoadedDef], {key: TunableRow})`
  (S2-P2) — what the radar S5 stage consumes. Every stored def is
  re-validated (its predicates re-parse) with its md5, and the trader's
  per-trade tunable rows come with them. A row that no longer validates
  fails the read loud.

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

**2026-09-21 — setups one build STEP-2.** `sync` code is unchanged. A
`global` assumed row reaches it with `slug = None` and is stored as NULL.
That needs migration `db_migrations/0013_tunables_slug_nullable`: X20
showed that without it the INSERT raises `NotNullViolation` and the WHOLE
sync rolls back. `taxonomy/migrations/0001_trade_defs.sql` is untouched,
because a rollback cannot live in a folder `ensure_schema` runs forward.
A per-trade row keeps its slug and the foreign key.
