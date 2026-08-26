# `tests/cobalt/test_aset_store.py`

## What it does
The one integration test in the ASET suite — a real INSERT/SELECT
round trip against `cobalt_dev`. Marked `pytest.mark.integration` and
individually skipped (`requires_db`) if `POSTGRES_HOST`/`POSTGRES_USER`
aren't present in the environment, so the suite stays runnable without
a live database.

## Key functions/classes (what's covered, not defined)
- `test_factory_refuses_prod_db` — the one test that always runs (no DB
  needed): asserts `db.connect("cobalt_brain")` raises `DbConfigError`
  without `allow_prod=True`. This is the concrete proof that NN#16 is
  enforced in code.
- `test_save_and_read_back_roundtrip` — computes a sizing, saves it via
  `AsetStore`, reads it back via `.recent()`, and asserts the persisted
  row matches (including a hand-checked expected value: grade B, 15% of
  200 = 30 risk budget, ÷ 0.50 distance = 60 shares).

## Data flow in/out
Writes one real row to `aset_sizings` in `cobalt_dev` when the
integration test runs (not cleaned up afterward — it's a append-style
audit table by design, matching production behavior).

## Config it reads
None directly — connects via `cobalt.db.connect("cobalt_dev")`, which
reads `POSTGRES_*` from the environment (loaded by the repo-root
`conftest.py`'s `load_dotenv()`).
