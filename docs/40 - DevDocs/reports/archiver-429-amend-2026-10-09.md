# archiver-429 — card 206 re-pointed, 2026-10-09

## §0 Headline
- Card 206 amended in place on preflight issues 1–7; BASE and RULINGS untouched.
- Both FAILs closed: A2 (2) asserts on `failures` without `_archive_nightly`; B (a) patches `REPORT_PATH`.
- `grep -c -F "«FILL"` → 0. No other file edited.

## CHANGES
- A1: `FinvizRateLimited(message, *, retry_after=None)` pinned (issue 5).
- A2: `requests += 1` per retry is the runner's; `record_retry` does not touch it (issue 3).
- A2 test (2): no `_archive_nightly` call; asserts `len(failures) == 1`, entry starts `<T>/<i>:` and carries `429` (issue 1).
- A2 test (3): ONE target; `Retry-After: 0` → `[1.2]` (issue 5).
- B: `retry_line()` outcome is `failed` when a `failures` entry starts `<T>/<i>:`, else `ok` (issue 4).
- B test (a): `REPORT_PATH` patched to `tmp_path` as `:284` does; `load_config` and `_run_targets` faked (issue 2).
- `## NOT IN THIS JOB`: retry budget counts waits only, bounded at 2229 s (issue 7).
- `## RECORDS`: approval row is his standing R685; direction is `reports/cto-2026-10-09.md` R808, R812 (issue 6).

## DECISIONS
- Issue 1 seam: the second option. At `f5010068` `_archive_nightly` (`runner.py:462`) opens `as_job` before `run_full` and builds the `RuntimeError` text inline (`:482`), so only `failures` is testable without a `JobStore`.

## RECORDS
- Proved against `git show f5010068`: `runner.py` `_archive_nightly :462`, `raise :482`, `run_full :429`, `_upsert_targets :237`; `report.py` `record_failure` appends `<T>/<i>: <error>` and increments `requests`.

ARCHIVER 429 CARD RE-POINTED · decisions: 1
