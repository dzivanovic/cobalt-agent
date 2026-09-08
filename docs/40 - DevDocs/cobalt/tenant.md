# `src/cobalt/tenant.py`

## What it does
Says which local trader this install serves. One committed file,
`configs/cobalt/tenant.yaml` (`trader_id: 1`), Pydantic-validated, and
the value the one connection factory sets as the `cobalt.trader_id`
session GUC on every connection it opens.

## Key functions/classes
- `TRADER_GUC = "cobalt.trader_id"` — written in exactly one place in
  Python and one in SQL (`db_migrations/0002_move_tables.sql`).
- `TenantConfig` — `trader_id: int` with `ge=1`; 0 or negative names no
  trader (`"user".traders` is seeded at 1).
- `load_tenant_config(path=None, refresh=False)` / `trader_id()` — cached
  per process. The identity of an install is not a runtime knob, and
  re-reading it per connection would let a mid-run edit change which
  trader the second half of a job writes as.

## Data flow in/out
**In:** `configs/cobalt/tenant.yaml`. **Out:** an int, into
`db.apply_side()`'s `set_config`.

## Why it exists
Every user-side table's `user_id` defaults to
`current_setting('cobalt.trader_id')::int` — never a literal. A
connection that did not pass through the factory has no GUC and every
INSERT fails loud. This file is the only thing that decides what that
value is.

## Gotchas
Committed on purpose: it is which SEAT this install is, not a secret and
not a preference. The trader's own settings live in
`"user".trader_settings`, not here.
