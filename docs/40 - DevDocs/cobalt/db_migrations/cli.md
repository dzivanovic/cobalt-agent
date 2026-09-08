# `src/cobalt/db_migrations/cli.py`

## What it does
`cobalt db migrate [--allow-prod] [--rollback]`. Runs the migrations and
prints a per-table proof: where the table lives, its row count, and a
content digest — before and after.

## The digest, and why it is not the naive one
`md5(string_agg((to_jsonb(row) - 'user_id')::text, '|' ORDER BY <pk>))`.
It EXCLUDES `user_id` because the forward migration adds that column to
six tables, so a whole-row digest would differ by construction and prove
nothing. `to_jsonb` also makes the value independent of column order,
which both `SET SCHEMA` and `ADD COLUMN` touch. The primary key is read
from the catalog per table, never hard-coded.

## Data flow in/out
**In:** `db.connect_migration()` (no `SET ROLE` — see `db.md`), the two
`.sql` files, whole, in one transaction. **Out:** the proof table; a
non-zero exit if any digest changed.

## Gotchas
Each file is handed to the server ENTIRE rather than split on `;`: they
are `DO` blocks, and a splitter would cut them at the first semicolon
inside the body.

Running it twice is a no-op. Rollback then re-migrate lands on identical
digests — the suite asserts that round trip on `cobalt_dev`.
