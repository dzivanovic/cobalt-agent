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
  docs/00 - Project/BACKLOG.md), and opens an autocommit connection.

## Data flow in/out
**In:** `POSTGRES_HOST`, `POSTGRES_USER`, `POSTGRES_PASSWORD` (required —
raises `DbConfigError` if any is missing), `POSTGRES_PORT` (optional,
default `5432`). All read from `os.environ` (populated by `.env` via
whatever loads it upstream — this module doesn't load `.env` itself).
**Out:** a live `psycopg.Connection`, or raises.

**Safety property (revised by RULING 7, 2026-09-04 — ADR-0005):**
calling `connect("cobalt_brain")` raises unless this process has
declared `COBALT_ENV=production`, or the caller passes
`allow_prod=True`. The declaration is what makes a production
entrypoint a production entrypoint — previously it was an `allow_prod`
kwarg each call site had to remember, and no call site did, because
there was no production database to reach.

`allow_prod=True` remains for migration tooling that must reach
production deliberately without flipping the whole process into
production mode. A dev run, a test, or a process with `COBALT_ENV`
unset cannot open `cobalt_brain` (unset is definitively not production:
`connect()` catches `EnvConfigError` and refuses).

**No call site names a database any more.** `AsetStore` and
`VaultWriteStore` default `db_name=None` and ask
`cobalt.env.resolve_db_name()`. The old shape —
`AsetStore(aset_cfg.db_name)` reading `configs/dev/aset.local.yaml` —
is what routed PRODUCTION writes into `cobalt_dev`; `db_name` is now
deleted from `AsetConfig` entirely and re-adding the key is a loud
crash.

## Config it reads
No YAML config — reads Postgres connection parts directly from the
process environment.
