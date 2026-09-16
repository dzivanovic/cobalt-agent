# `src/cobalt/settings/store.py`

`put` accepts an optional callback invoked after all upserts and immediately before commit for transactional session gating.

## What it does
`TraderSettingsStore`, `SIDE = Side.USER`. Reads and upserts
`"user".trader_settings`. DDL in `migrations/0001_trader_settings.sql`,
executed, not re-typed.

## Key functions/classes
- `rows()` / `values()` — what `TraderSettings.from_db` builds from.
- `put(rows, source=, delete=())` — one transaction, returning
  `{key: created|updated|unchanged|deleted}`. An unchanged value is NOT
  re-dated: a `source` and `updated_at` that move on a no-op run stop
  meaning anything. `delete` (S2-P2) removes keys in the SAME
  transaction: the card-settings file is a whole set, and a key it omits
  must vanish atomically with the keys it writes. A key in both `rows`
  and `delete` is refused.

## Why user side
How much a trader risks on a B, which grades he takes, what makes today a
smaller day — none of it engine, all of it one person's ruling, none of
it ever visible to another Cobalt user (L32).

## Gotchas
`user_id` carries the tenant-GUC default, so a connection that skipped
the factory cannot write a setting for nobody. PK is `(user_id, key)`:
two traders on one install hold different answers to the same key.
