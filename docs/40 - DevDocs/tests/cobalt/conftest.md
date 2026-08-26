# `tests/cobalt/conftest.py`

## What it does
Overrides the repo-root `conftest.py`'s autouse `psycopg.connect` mock
for everything under `tests/cobalt/`. Without this, the ASET store's
integration test would silently run against a `MagicMock` instead of
real Postgres and pass/fail meaninglessly.

## Key functions/classes
- `mock_postgres_memory()` — an autouse fixture that does nothing but
  `yield` (i.e. it exists purely to shadow/neutralize the root
  fixture of the same name for this directory).

## Data flow in/out
None.

## Config it reads
None directly — `tests/conftest.py` (repo root) still runs first and
calls `load_dotenv()`, which is what makes `POSTGRES_*` env vars
available to `tests/cobalt/test_aset_store.py`'s `requires_db` skip
check.
