# `src/cobalt/db_migrations/__init__.py`

## What it does
Holds the DATABASE-WIDE migrations — the two-schema split itself
(ADR-0008). `FORWARD` is `0001_schemas.sql` then
`0002_move_tables.sql`; `REVERSE` is `0002_move_tables.rollback.sql`.

## Why it exists (and why it is the only directory like it)
A feature module's DDL lives in its own `migrations/` and is run by its
own store. These files belong to no feature: schemas, roles, grants,
ownership, and moving twelve tables from `public` onto a side. Anything
that DOES belong to a module stays with the module — `taxonomy/` and
`settings/` both keep their own.

## Gotchas
Nothing runs these implicitly. A store's `ensure_schema()` asserts the
schemas exist and tells you to run `cobalt db migrate`.

`0001` is idempotent and re-run on every invocation; it is deliberately
NOT reversed by `--rollback` (dropping a schema is not a catalog flip).
