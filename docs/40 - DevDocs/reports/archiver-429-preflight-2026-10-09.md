# archiver-429 — card 206 preflight, 2026-10-09 23:46 ET (read-only)

Card `prompts/2026-10-09/206-archiver-429-card.md`, draft `reports/archiver-429-draft-2026-10-09.md`, spec `prompts/CARD.md`. Code read from the working tree; `git diff --stat fa968552 HEAD -- src tests ops` is empty at HEAD `041c627e`, so it is `f5010068`'s code.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read `ops/desk/desk-launch.sh` build mode (`:722–735`, `:896–910`); `ls /Users/cobalt/cobalt-wt/archiver-429-1009`; `rev-parse --verify refs/heads/ops/archiver-429-1009` | JOB `[a-z0-9-]`; BRANCH plain; WORKTREE one name; REPORT is `<WT>/archiver-429-1009/docs/40 - DevDocs/reports/*.md`; TIP/CHECK REPORT/HOUSE B empty (build); worktree and branch absent (fresh `worktree add`); build report absent | OK |
| 2 | `git merge-base --is-ancestor fa968552 main`; `git diff --stat fa968552 HEAD -- src tests ops` | exit 0; empty | OK |
| 3 | `grep -n "^\| R685 \|" reports/cto-2026-10-08.md`; `git diff HEAD` of that file | `:38` `HIS RULING … standing` · `APPROVED · HIS RULING`; the only uncommitted change in that file is an unrelated OWED line (`:93`) | OK |
| 4 | `grep -c "«FILL"` on the card | 0 | OK |
| 5 | `collector.py` vs card | `CollectorError :57`; `finviz_get :175`, `raise_for_status :213`, `raise CollectorError(f"Finviz HTTP failed: …") :215`; `fetch_bars :219`, `"Fetch failed for …" :236`, wrap `:234–237`; `__all__ :242` | OK |
| 6 | `runner.py` vs card | `GENTLE_SLEEP_SECONDS = 1.2 :30`; `_backfill_window :59`; `_check_demand :80`; `_run_targets :182`; `_upsert_targets :237`, fetch `:249`, sleep `:265`; `_append_targets :303`, fetch `:309`; `run_full :429`, f-string `:439`; `Backfill complete: :456`; `_archive_nightly :462`, `raise RuntimeError :482` | OK |
| 7 | `report.py`, tests, `jobs.yaml`, `notes.py` vs card | `RunSummary :103–208`, `append_run_report :228`; runner tests `run :188`, `fetcher :196`, `_no_sleep_no_token :207–216`, pinned tests `:284`, `:303`; collector `MockTransport` seam `:169–189`; `jobs.yaml` `timeout_s: 2400` `:214`; `notes.py:368` `rpm=60 / GENTLE_SLEEP_SECONDS`, `:369` window to `timeout_s` | OK |
| 8 | `grep -n` `logs/archiver.err`, `logs/radar.err`, `tunables.yaml` | DKNG `:32431`, EXC `:32475`, LMT `:32637`, META `:32680` (all 429 ERROR at `_upsert_targets:257`); `Run complete … 18 failures, 24m13s` `:33220`; F17 FAILED `:33221`; 28 `Run complete:` lines (27 to 10-08 + 10-09); radar `paused_market_reset` `:44531–44538`; `archiver.write_mode` `upsert` `:782–783` | OK |
| 9 | A1 red on BASE | `FinvizRateLimited` absent from `collector.py` → `ImportError`; the 500 control is `CollectorError`, not the subclass, after the fix | OK |
| 10 | A2 red on BASE | on BASE the fake cannot raise `FinvizRateLimited` (`ImportError` at the import); the card's "1 failure" red holds only after A1 is built, which the row order gives (see ISSUES 2) | OK, NOTE |
| 11 | A2 negative controls (6) plain `CollectorError("No data rows …")`; (5) backfill | not retried: the helper retries only `FinvizRateLimited`; backfill budget 0 | OK |
| 12 | B red on BASE | `RunSummary` has no `record_retry` (`report.py:103–208`) → `AttributeError`; `:439` f-string has no `retried`; a 429 is an ERROR failure, no WARNING | OK |
| 13 | every test offline | A1 `MockTransport` and B report test: offline. A2 (2) calls `_archive_nightly` (`runner.py:462`) → `as_job` → `job_run` → `JobStore()` → `db.connect` (`jobs/entrypoint.py:54`, `jobs/wrapper.py:135`, `jobs/store.py:49–53`); no test in `tests/` calls `_archive_nightly`. B (a) calls `run_full`, whose `append_run_report` writes `REPORT_PATH` (`docs/30 - Design/archiver-runs.md`) unless the test patches it (`:284` does) | FAIL |
| 14 | retry bound and waits vs the 2400 s window | 10-09: 1453 s + 600 s = 2053 s → 21:04:13 < 21:10:00; worst day 25m04s = 1504 s + 600 = 2104 s; worst retry GET time with `Retry-After: 0` (500 retries × 1.2 s wait + ~0.25 s GET) is ≤ 725 s → 2229 s < 2400 s | OK |
| 15 | L53 pacing (X1) | every retry wait ≥ `GENTLE_SLEEP_SECONDS` (clamp low end 1.2, backoff 15/30/60); a success or an exhausted target is followed by the existing `sleep(GENTLE_SLEEP_SECONDS)` (`:265`, `:342`); no two GETs closer than 1.2 s; rpm bound `60/1.2 = 50` unchanged (`notes.py:368`) | OK |
| 16 | no config, cadence or bucket; consumer scan | NOT IN THIS JOB fences `configs/`, `jobs.yaml`, `notes.py`; `test_finviz_consumers.py:27` scans `finviz_get(`/`fetch_bars(`/host; the card adds no call (the raise sits inside `finviz_get`) | OK |
| 17 | RESTARTS class home (`restarts.py:178–264`) | `src/…` → `static import reach`; residents with `imports`: aset, agent, radar (`jobs.yaml:90,150,194`); radar reaches `cobalt.archiver.collector` (`radar/collector.py:17`), `.runner` (`radar/notes.py:349`) via `cobalt.cli`→`archiver.cli` (`cli.py:81`); `tests/…` → `test/documentation; no resident`; `docs/…` → `DOCS`. `uv run cobalt jobs restarts` not run (no `uv` in this seat) | OK, not run |
| 18 | no new command (R411, R412) | rows use `uv run pytest` and `uv run cobalt jobs restarts` only | OK |
| 19 | card committed and unchanged | `git diff --stat HEAD -- <card>` empty; last commit `9246af12` | OK |
| 20 | X3: `grep -rn CollectorError src` | `except CollectorError` only at `archiver/runner.py:255,310`; `strike/measure.py:24` is a docstring; radar, replay, strike have none; the message text is unchanged | OK |

## ISSUES
1. FAIL (13) A2 (2): `_archive_nightly` opens a real `JobStore` (DB connect) and nothing in `tests/` fakes it. The card must name the seam, e.g. monkeypatch `cobalt.jobs.entrypoint.as_job` with a stub context manager yielding an object with a `result` attribute, or assert the `RuntimeError` text on `failures` without calling `_archive_nightly`.
2. FAIL (13) B (a): `run_full` writes `report_mod.REPORT_PATH`; the card must say the test patches it to `tmp_path` (as `:284` does) and fakes `load_config` and `_run_targets`.
3. NOTE A2 vs B: A2 (1) asserts `requests == 3`, but `record_retry` is in row B (`report.py`), not in A2's `files`. The card must say who increments `requests` (the runner, `summary.requests += 1`, or `record_retry`), and only one of them, or a retry is counted twice.
4. NOTE B: `retry_line()` prints `(ok|failed)` but `record_retry(ticker, interval, attempt, wait)` carries no outcome and `record_success(ticker, rows)` has no interval. The card should say the outcome is `failed` when a `failures` entry starts `<T>/<i>:`, else `ok`.
5. NOTE A2: `FinvizRateLimited`'s constructor (positional message, `retry_after=`) is unpinned, and the tests build it by hand; pin it in A1. With a single target and `Retry-After: 0` the recorded wait `1.2` equals the gentle sleep, so (3) must use one target (no between-target sleep) to tell them apart.
6. NOTE R685: its words are about a defect he reports; R808 (brain) is the ladder line. The row is his standing, committed `HIS RULING` + `APPROVED`, which is all the hub proves; the desk may want a row that names the archiver.
7. NOTE: the budget counts waits only, not the retry GET time (check 14 bounds it at 2229 s).

PREFLIGHT DONE · card: archiver-429-1009 · checks: 20 · fails: 1 · ready: NO
