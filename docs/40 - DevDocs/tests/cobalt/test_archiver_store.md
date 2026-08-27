# `tests/cobalt/test_archiver_store.py`

## What it does
Integration test — a real upsert round trip against `cobalt_dev`.
Marked `pytest.mark.integration`, skipped if Postgres env settings
aren't present. Doesn't re-test the prod-DB refusal (already proven
once by `test_aset_store.py`; `BarStore` shares the same `cobalt.db`
factory).

## Key functions/classes (what's covered, not defined)
- `test_upsert_is_idempotent_and_refreshes_on_conflict` — inserts one
  bar, records the total row count, then upserts the **same** `(ticker,
  interval, ts)` with a different `close`. Asserts the row count didn't
  change (no duplicate — the PK conflict fired) **and** that the stored
  `close` actually updated to the new value (proves `DO UPDATE`, not
  `DO NOTHING` — a re-pulled bar really does refresh).
- `test_upsert_empty_list_is_a_noop` — `upsert_bars([])` returns `0`
  without erroring.

## Data flow in/out
Writes real rows to `bars` in `cobalt_dev` under ticker `TESTARCH`
(not a real symbol — won't collide with archived data) when the
integration test runs. Not cleaned up afterward, matching
`test_aset_store.py`'s precedent (an append-style audit table by design).

## Config it reads
None directly — connects via `cobalt.db.connect("cobalt_dev")`, which
reads `POSTGRES_*` from the environment (loaded by the repo-root
`conftest.py`'s `load_dotenv()`).
