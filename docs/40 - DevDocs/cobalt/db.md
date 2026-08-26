# `src/cobalt/db.py`

## What it does
The **one connection factory** for the entire new core (TRIAGE secrets
law: DSNs composed at runtime from parts, URL-encoded, never logged).
Every module under `src/cobalt/` that touches Postgres goes through
`connect()` — no second copy of DSN-building logic is allowed to exist
(one-path rule).

## Key functions/classes
- `DbConfigError(RuntimeError)` — missing/invalid DB settings; raised
  instead of silently defaulting.
- `PROD_DB_NAME = "cobalt_brain"` — the name `connect()` refuses by
  default.
- `connect(dbname: str, *, allow_prod: bool = False) -> psycopg.Connection`
  — builds `postgresql://user:pass@host:port/dbname` from four env vars,
  URL-encoding user/password/dbname (closes the `@`-in-password bug
  class that broke Mattermost's DSN — see the 2026-08-25 incident in
  BACKLOG.md), and opens an autocommit connection.

## Data flow in/out
**In:** `POSTGRES_HOST`, `POSTGRES_USER`, `POSTGRES_PASSWORD` (required —
raises `DbConfigError` if any is missing), `POSTGRES_PORT` (optional,
default `5432`). All read from `os.environ` (populated by `.env` via
whatever loads it upstream — this module doesn't load `.env` itself).
**Out:** a live `psycopg.Connection`, or raises.

**Safety property:** calling `connect("cobalt_brain")` without
`allow_prod=True` raises immediately — NN#16 (build work never touches
prod) enforced in code, not just by convention. Every ASET call site
(`AsetStore`) calls this with `db_name="cobalt_dev"`, never prod.

## Config it reads
No YAML config — reads Postgres connection parts directly from the
process environment.
