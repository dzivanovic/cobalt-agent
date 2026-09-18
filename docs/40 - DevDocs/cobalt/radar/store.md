# `src/cobalt/radar/store.py`

System-side `RadarStore` for membership episodes and the pool status row. Membership, pool, and failure stamps are separate idempotent transactions; each checks `assert_writable` and calls the supplied commit gate immediately before commit.

## Reads

- `open_members(pool_key)` returns the open episode fields required by the radar decision engine.
- `pool_row(pool_key)` returns the complete status row or `None`.
- `members_for_day(pool_key, trade_date)` returns every membership column for every episode in exactly one pool/day, ordered by identity. It intentionally includes admitted open rows, departed admitted rows, and never-admitted exclusions. Callers distinguish admission through `entered_at`, not through `left_at` alone.

All three are plain SELECT paths. They do not initialize a schema or invoke a write guard.

## Writes

`apply_membership`, `put_pool`, `stamp_failure`, and `stamp_poll` remain the resident's guarded write transactions. `stamp_poll(..., preserve_failure=True)` updates S4 freshness without clearing the pending reset-crossing failure that S2 first made observable in the same recovery cycle. The default remains `False`, so ordinary successful polling still clears a recovered `bars` failure.
