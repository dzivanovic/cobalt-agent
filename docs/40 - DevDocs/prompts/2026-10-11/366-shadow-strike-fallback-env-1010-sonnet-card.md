JOB: strike-fallback-env-1010-sonnet
LADDER: OFF-LADDER — reports/cto-2026-10-10.md R828
BRANCH: shadow/strike-fallback-env-1010-sonnet
WORKTREE: strike-fallback-env-1010-sonnet
BASE: 8f4bbe28
TIP: 813036e8
REPORT: /Users/cobalt/cobalt-wt/strike-fallback-env-1010-sonnet/docs/40 - DevDocs/reports/strike-fallback-env-1010-sonnet-build-2026-10-11.md
CHECK REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/strike-fallback-env-1010-sonnet-check-2026-10-11.md
HOUSE B: as needed
RULINGS: 2026-10-08 R685, 2026-10-11 R1069
SHADOW OF: /Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/215-strike-fallback-env-card.md

## ROWS

| row | what | red first | files |
|---|---|---|---|
| A | ORDER: the sheet's fallback thread starts with the DB env loaded. `src/cobalt/aset/__main__.py` loads the repo `.env` explicitly, as `src/cobalt/cli.py:52–59` does (`from dotenv import load_dotenv`, then `load_dotenv(Path(__file__).resolve().parents[2] / ".env")`), BEFORE `start_fallback_thread()` (`:54`, imported at `:52`, `uvicorn.run` at `:57`). Here the path is `Path(__file__).resolve().parents[3] / ".env"` (`__main__.py` sits in `src/cobalt/aset/`: `parents[0]` aset, `[1]` cobalt, `[2]` src, `[3]` repo root); `override` stays the default `False`, so a variable already in the environment wins, as in `cli.py`. Add the import with the file's other `# noqa: E402` imports, after the `LOGURU_LEVEL` line. Why it matters: `db._open` (`src/cobalt/db.py:160`) reads `POSTGRES_HOST` (`:168`) and `COBALT_DB_USER` / `COBALT_DB_PASSWORD` (`Credential.APP`, `:103`) from `os.environ`, and raises `DbConfigError("Missing Postgres settings for the APP credential: …")` when one is empty; `aset` loads `.env` only as a side effect of uvicorn importing `cobalt.aset.web` (chain to `src/cobalt_agent/config.py:21`, `load_dotenv()`, cwd-relative), which runs AFTER the thread starts. Backed by `aset.err` line 10373, 2026-10-10 03:24:25.092, and R828 | NEW file `tests/cobalt/test_strike_fallback_env.py`, test A1: `monkeypatch.delenv` the three names (`POSTGRES_HOST`, `COBALT_DB_USER`, `COBALT_DB_PASSWORD`: `tests/conftest.py:13` loads `.env` into the test process, so they must be cleared); stub `dotenv.load_dotenv` with a function that records its `path` argument and `monkeypatch.setenv`s the three names; stub `uvicorn.run` to a no-op; stub `cobalt.aset.strike.start_fallback_thread` with a function that builds a real `FallbackTail` over a store whose `seam_rows` calls `cobalt.db._open("cobalt_dev")` (with `cobalt.db.psycopg.connect` stubbed to return a placeholder object) and runs ONE `pass_once()`; then `runpy.run_module("cobalt.aset.__main__", run_name="__main__")`. Asserts: the run returns without `DbConfigError`; the stub saw exactly one call whose path is `<repo root>/.env` (`Path(...).name == ".env"` and `.parent` has `pyproject.toml`). RED on `BASE`: `DbConfigError: Missing Postgres settings for the APP credential`, raised from inside the stubbed start (nothing loaded the env before it). Test A2 (negative control): the same run with a `load_dotenv` stub that sets nothing and the three names cleared → `DbConfigError` propagates (`pytest.raises`); no `.env` and no env still fails loud. A2 is green on `BASE` and after | `src/cobalt/aset/__main__.py`, `tests/cobalt/test_strike_fallback_env.py` |
| B | LOUD: a failing fallback is never silent, and its recovery is said. `FallbackThread.run` (`src/cobalt/aset/strike.py:535–546`) logs an ERROR only for a NEW message (`:543`) and nothing on success (`:540` resets `last_error`), so "recovered" and "failing since 03:24" look the same. New behaviour: (1) the first failure of a streak logs ERROR `strike fallback: pass failed — the thread goes on: <Type>: <message> (failed passes: 1)`; (2) while the SAME text persists, it repeats the ERROR when at least `REPEAT_ERROR_S = 60.0` seconds have passed since the last ERROR, with the running count (`failed passes: <n>`); a different text logs at once; (3) the first success after a failure logs one INFO `strike fallback: recovered after <n> failed passes` and resets the count; (4) the first pass of the thread, when it succeeds, logs one INFO `strike fallback: first pass OK` (once per thread; a first pass that fails logs no `first pass OK`, its recovery line replaces it). `FallbackThread.__init__` gains keyword-only `monotonic: Callable[[], float] = time.monotonic`, beside `interval_s`; the loop body moves into one method `step()` (one pass, one logging decision) that `run` calls, so a test drives it without a thread or a sleep; the constant sits beside the class, not in config; `start_fallback_thread` (`:549`) is unchanged. The `FallbackTail` and every DM rule stay as they are | In `tests/cobalt/test_strike_fallback.py` (beside `test_the_thread_logs_a_failed_pass_and_goes_on`, `:202`, which stays green unchanged) or `tests/cobalt/test_strike_fallback_env.py`: a fake tail whose `pass_once` follows a script (`"ok"` or an exception) and a fake clock `[0.0]` the test advances; call `thread.step()` directly on `FallbackThread(tail, interval_s=1, monotonic=lambda: clock[0])`; a loguru sink `logger.add(records.append, level="INFO", format="{level}\|{message}")` (removed in a `finally`), asserting on `(level, message)` pairs. B1: script fail, fail, ok, clock steps of 1 s → exactly one ERROR (carrying `failed passes: 1`) and one INFO `strike fallback: recovered after 2 failed passes`, no `first pass OK`. B2: one failure, then the same failure again at +61 s → two ERRORs, the second carrying `failed passes: 2`; and a same-text failure at +30 s → no new ERROR (the count still grows: the next ERROR says 3). B3: a different failure text at +1 s → an ERROR at once. B4: a clean start: ok, ok, ok → exactly one INFO `strike fallback: first pass OK`, no ERROR. B5: fail, ok, ok → one recovered INFO, then silence. RED on `BASE`: `TypeError: __init__() got an unexpected keyword argument 'monotonic'` for every B test; after the constructor is added, B1 fails on the missing recovered INFO, B2 on the missing repeat, B4 on the missing `first pass OK` | `src/cobalt/aset/strike.py`, `tests/cobalt/test_strike_fallback.py`, `tests/cobalt/test_strike_fallback_env.py` |

## NOT IN THIS JOB
- The fallback's DM policy, `dm_after_s`, and any config: `configs/` untouched; `REPEAT_ERROR_S` is a code constant, not a tunable.
- The phone DM proof: it stays UNPROVEN (L70) until a real trigger, with his B5.
- `FallbackTail`, `StrikeAlertStore`, the stream, the pinned tab, the ack, `start_fallback_thread`'s body: untouched.
- The alternative order (starting the thread from the app's startup after `cobalt.aset.web` is imported): named in `## DECISIONS`, not taken.
- `src/cobalt_agent/config.py` and its cwd-relative `load_dotenv()`: untouched; `cli.py` untouched.
- `.claude/settings.json.bak`: his; the launcher row is the check's line below.
- A red outside these rows: a `## DECISIONS` item, UNPROVEN (L70), with the output; never fixed here.

## READ
- `src/cobalt/aset/__main__.py` whole (57 lines): the `LOGURU_LEVEL` line, the imports, the thread start at `:50–57`.
- `src/cobalt/cli.py:50–59`: the explicit load and the comment that says why.
- `src/cobalt/aset/strike.py:485` (`FallbackTail.pass_once`), `:521–546` (`FallbackThread`), `:549–557` (`start_fallback_thread`).
- `src/cobalt/db.py:136` (`DbConfigError`), `:160` onward (`_open`, to its `psycopg.connect`).
- `tests/cobalt/test_strike_fallback.py:68–78` (`FakeStore`, `_tail`) and `:202–221` (the thread test); `tests/conftest.py:13` (the test process loads `.env`).
- `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cto-2026-10-10.md` R828.
- Test-seam style: `/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/2026-10-09/206-archiver-429-card.md` rows A2 and B (a recording fake, a loguru sink, no opening of a real store).

## CHECK ASKS
- FOR THE CHECK: strike-fallback brain 10-10 — cause read: the fallback thread starts before uvicorn imports web, whose import chain (cobalt_agent/config.py:21 load_dotenv) fills the DB env; fix = explicit .env load in aset/__main__.py before start_fallback_thread (as cli.py:59) with a red test, plus a repeating ERROR and recovered/first-pass INFO lines (L1); settings.json.bak to the D0 accepted list (launcher row).
- X1 Is `load_dotenv` called before `start_fallback_thread()` on every path through `__main__.py`, and does anything else in the file read the DB env earlier?
- X2 Can a failure of one pass ever stop the thread, or log nothing for more than 60 s while it persists?
- X3 Does `step()` keep the old rule that an exception in a pass never takes the sheet down (`FallbackThread.run`, `strike.py:535`)?

## RECORDS
- Code read at `975345f3` (the S4-P2 deploy merge): `git -C /Users/cobalt/cobalt diff --stat 975345f3 HEAD -- src tests ops` printed nothing at the desk's draft time (2026-10-10), so the lines above are main's.
- The failure: `aset.err` line 10373, 2026-10-10 03:24:25.092, `DbConfigError: Missing Postgres settings for the APP credential` (the brain's read, R828; the drafter did not open the log).
- RESTARTS: `uv run cobalt jobs restarts <BASE>..HEAD`, the builder runs it and quotes it. Expected: `src/cobalt/aset/__main__.py` and `src/cobalt/aset/strike.py` → `com.cobalt.aset` (a resident, loaded at its next restart; the deploy owns it); `tests/…` → `test/documentation; no resident`; `docs/…` → `DOCS`. Any other label or an `ESCALATE` line is a `## DECISIONS` item.
- Approval row: his standing R685 (defects); the brain's direction is `reports/cto-2026-10-10.md` R828.
- No new command: the rows use the existing `uv run pytest` suites and `uv run cobalt jobs restarts` (R411, R412).
