# `ops/cobalt_app_role_provision.py`

## What it does
Mints `cobalt_app` — the non-superuser login the application uses.
Run once, on 2026-09-09.

```
uv run python ops/cobalt_app_role_provision.py
```

## The weakness it closes
ADR-0008 D1 Revision 2, stated in `db_migrations/0001_schemas.sql` and
escalated as item 3 of the 09-08 ADR report:

> The login role is still the docker superuser, and a superuser bypasses
> every grant check. After the factory's SET ROLE the session's CURRENT
> role is a non-superuser and the grants bite, so per-store enforcement
> is real — **but a connection that skips the factory keeps full power.**

`cobalt_app` is that closure. `LOGIN NOINHERIT`, member of
`cobalt_system` / `cobalt_user` / `cobalt_backup`, holding nothing of its
own. Under NOINHERIT a session that has not called `SET ROLE` — one that
skipped `cobalt.db.connect()` — **can read nothing**. The one-factory
lint test stops being the only thing holding that line; the server is.

Every negative attribute is written out rather than left to a default,
so `\du` shows exactly what was asked for: `NOSUPERUSER`, `NOCREATEDB`,
`NOCREATEROLE`, `NOREPLICATION`, `NOBYPASSRLS`. The script prints back
what `pg_roles` says the role **is**, not what it asked for.

## Cluster-wide role, per-database grant — and the fence between them
`CREATE ROLE` writes a shared catalog, so one run gives the role to every
database on the server. The GRANTs are per-database and are not: this
script grants `CONNECT` on **`cobalt_dev` and nothing else**.

`GRANT CONNECT ON DATABASE cobalt_brain TO cobalt_app` is deliberately
**left out**, so a dev-side provisioning run cannot by itself give a new
credential a path into production (NN#16). Until that named LIVE step
runs, `psql -U cobalt_app -d cobalt_brain` answers *permission denied for
database "cobalt_brain"* — proven in the 09-09 ops report.

That fence is real rather than accidental because the 09-05 Mattermost
work revoked `PUBLIC`'s CONNECT on both databases; otherwise Postgres's
default grant would have made the explicit one redundant.

## Where the secret lands
`.env` (bootstrap tier — `cobalt.db._open()` composes its DSN from the
environment) **and** VaultManager as `COBALT_DB_PASSWORD`, which is the
F19 literal-guard enrolment. Belt and braces: the name ends in
`PASSWORD`, so F19's `env_assignment_secret` pattern catches it by name
even with the vault locked.

The mechanism — local SCRAM verifier, never an argv, add-only preflight —
is `ops/pg_role.py`.

## It uses `connect_migration`
`CREATE ROLE` and `GRANT` are superuser-class acts on a shared catalog,
which is exactly what the BOOTSTRAP credential is for. Against the
`postgres` database, because a shared-catalog write belongs nowhere in
particular.

## Neighbours
`ops/pg_role.py`, `src/cobalt/db.py` (`Credential`), 
`src/cobalt/db_migrations/0001_schemas.sql`, `.env.example`.
