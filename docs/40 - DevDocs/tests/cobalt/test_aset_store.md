# `tests/cobalt/test_aset_store.py`

## What it does
The one integration test in the ASET suite — a real INSERT/SELECT
round trip against `cobalt_dev`. Marked `pytest.mark.integration` and
individually skipped (`requires_db`) if `POSTGRES_HOST`/`POSTGRES_USER`
aren't present in the environment, so the suite stays runnable without
a live database.

**Iteration 4 (2026-08-28):** this is the test that caught the real
`ensure_schema()` comment-splitting bug (see `store.md`) — it's the
only ASET test that runs `AsetStore.ensure_schema()` against a live,
already-`0001`-migrated `cobalt_dev` table, so it's the one place a bad
multi-statement migration would actually surface as a `SyntaxError`
instead of passing silently against mocks.

## Key functions/classes (what's covered, not defined)
- `test_factory_refuses_prod_db` — the one test that always runs (no DB
  needed): asserts `db.connect("cobalt_brain")` raises `DbConfigError`
  without `allow_prod=True`. This is the concrete proof that NN#16 is
  enforced in code.
- `test_save_and_read_back_roundtrip` — computes a sheet-mode sizing
  (full B, $60 risk), saves it via `AsetStore`, reads it back via
  `.recent()`, and asserts the persisted row matches (including a
  hand-checked expected value: $60 ÷ $0.50 distance = 120 shares,
  `sheet_mode == "full"`).

## Data flow in/out
Writes one real row to `aset_sizings` in `cobalt_dev` when the
integration test runs (not cleaned up afterward — it's an append-style
audit table by design, matching production behavior). Also runs
`ensure_schema()` against the live table, applying `0002_...` if it
hasn't been applied yet.

## Config it reads
None directly — connects via `cobalt.db.connect("cobalt_dev")`, which
reads `POSTGRES_*` from the environment (loaded by the repo-root
`conftest.py`'s `load_dotenv()`).
