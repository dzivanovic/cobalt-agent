# archiver-429 — card 206 preflight r3, 2026-10-09 23:55 ET (read-only)

Card `prompts/2026-10-09/206-archiver-429-card.md`, spec `prompts/CARD.md`, earlier `reports/archiver-429-preflight-2026-10-09.md` and `-r2-`, amends `reports/archiver-429-amend-2026-10-09.md` and `-amend2-`. HEAD `90ac99ff`. `git diff --stat f5010068 HEAD -- src tests ops configs` is empty, so the tree is `f5010068`'s code (line numbers read in the tree and `git show f5010068:` alike).

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | read `ops/desk/desk-launch.sh` build mode (`:895–914`); `ls /Users/cobalt/cobalt-wt`; `git rev-parse --verify refs/heads/ops/archiver-429-1009` | REPORT must be `<WT>/<wt>/docs/40 - DevDocs/reports/*.md`: the card's is; worktree `archiver-429-1009` absent, branch absent (exit 128) → fresh `worktree add`; JOB, BRANCH, WORKTREE well formed; TIP, CHECK REPORT, HOUSE B empty (build); `need JOB LADDER BRANCH WORKTREE BASE REPORT RULINGS` (`:722`) all present; `DB` left out (rows touch `src/`, `tests/`) | OK |
| 2 | `git merge-base --is-ancestor fa968552 main`; `git diff --stat fa968552 HEAD -- src tests ops configs` | exit 0; empty (no code change past `f5010068`) | OK |
| 3 | `grep -n "R685 "` in `reports/cto-2026-10-08.md`; `git diff HEAD` of it; `ruling_row` `:245–272` | `:38` `HIS RULING (words R685, standing) … APPROVED · HIS RULING · APPLIED`, one row; the working-tree diff is one unrelated deleted OWED line (`:93`), the row is identical in HEAD (`grep -x -F` against `HEAD:` passes) | OK, NOTE 4 |
| 4 | `grep -c -F "«FILL"` on the card | 0 | OK |
| 5 | card committed and unchanged | `git diff --stat HEAD -- <card>` empty; last commit `f772032d` | OK |
| 6 | `reports/cto-2026-10-09.md` R808, R812 | `:34` R808 (archiver 429 a defect, bounded retry in the L53 bucket); `:30` R812 (decisions 1–7 kept, `Run complete` always carries `retried <n> (waited <s> s)`) | OK |
| 7 | `collector.py` at `f5010068` vs A1 | `CollectorError :57`; `finviz_get :175`; `raise_for_status :213`; `raise CollectorError(f"Finviz HTTP failed: …") :215`; `fetch_bars :219`; `except Exception :234`; `"Fetch failed for …" :236`; `__all__ :242` | OK |
| 8 | `runner.py` at `f5010068` vs A2, B | `GENTLE_SLEEP_SECONDS = 1.2 :30`; `_backfill_window :59`; `_check_demand :80`; `_run_targets :182`; `_upsert_targets :237`, fetch `:249`, `except CollectorError :255`, `logger.error :257`, sleep `:265`; `_append_targets :303`, fetch `:309`, sleep `:342`; `run_full :429`, f-string `:439`; `run_backfill :445`, `Backfill complete: :456`; `_archive_nightly :462`, `raise RuntimeError :482` | OK |
| 9 | `report.py`, tests, `jobs.yaml`, `notes.py` | `RunSummary :103`, `duration_str :205`, `append_run_report :228`, `REPORT_PATH :14`; runner tests `run :188`, `fetcher :196`, `_no_sleep_no_token :207–216`, pinned `:284`, `:303`; collector `MockTransport` seam `:169–189`; `jobs.yaml:214 timeout_s: 2400`; `notes.py:368` `rpm=60 / GENTLE_SLEEP_SECONDS`, `:370` basis | OK |
| 10 | `grep -n "Run complete:" logs/archiver.err` | 28 lines: 27 to 10-08 (`:996` … `:31985`), each `210 tickers … 0 failures`, 23m04s (`:1992`) to 25m04s (`:22249`, `:23466`); 10-09 `:33220` `18 failures, 24m13s`; RUNNING `:32180`; F17 FAILED `:33221` | OK |
| 11 | `grep -n "429 Too Many Requests" logs/archiver.err` | 18 `_upsert_targets:257` lines: DKNG `:32431` … EXC `:32475`, LMT `:32637` … META `:32680` (20:35:38–20:36:23, 20:40:18–20:41:12); `[n/1000]` → 1000 targets / 1453 s = 1.45 s | OK |
| 12 | `logs/radar.err:44531–44538`; `tunables.yaml:782–783` | `paused_market_reset` 20:30:10 … 20:41:50 every ~100 s; `archiver.write_mode` `upsert` | OK |
| 13 | A1 red on BASE | `FinvizRateLimited` absent from `collector.py` and `__all__` → `ImportError`; the 500 control stays plain `CollectorError`; constructor pinned (`message`, `*, retry_after=None`); seam is `module.httpx.AsyncClient` patched with `MockTransport`, offline | OK |
| 14 | A2 red on BASE, in row order | first red `ImportError` (whole runner test file); "1 failure" holds once A1 is built; (2) asserts on `failures` and never calls `_archive_nightly` (`as_job` opens a `JobStore`); (3) one target, no between-target sleep, so `1.2` is the clamp | OK |
| 15 | A2 negative controls | (5) backfill budget 0, `FETCH_AT` 16:30 ET outside premarket; (6) plain `CollectorError("No data rows …")` fetched once; (7) append 429, 200 → 0 failures, no `empty_export` | OK |
| 16 | B red on BASE | `RunSummary` has no `record_retry` (`report.py:103–208`) → `AttributeError`; `:439` f-string has no `retried`; a 429 is an ERROR failure, no WARNING; pinned `:284`, `:303` stay green (`record_retry` leaves `requests`, `job_result()`, the row untouched) | OK |
| 17 | every test offline | A1 `MockTransport`; A2 fake fetch, no `_archive_nightly`; B (a) patches `REPORT_PATH`, fakes `load_config` and `_run_targets`; `asyncio.sleep` faked by the autouse fixture; no DB, no network | OK |
| 18 | retry bound vs 2400 s (X2) | waits ≤ 600 s by rule (a retry past the budget is not taken; rule, test (4) and bound agree). 10-09: 1453 + 600 = 2053 s → 21:04:13; worst day 1504 + 600 = 2104 s; worst total retry time 500 × (1.2 + ~0.25) = 725 s → 1504 + 725 = 2229 s < 2400 s | OK, NOTE 1 |
| 19 | L53 pacing (X1) | every wait ≥ 1.2 s (clamp low end; backoff 15/30/60), measured after the previous GET returned; success or an exhausted target is followed by the existing `sleep(GENTLE_SLEEP_SECONDS)` (`:265`, `:342`); `60/1.2 = 50` unchanged | OK |
| 20 | no config, cadence, bucket; consumer scan | `## NOT IN THIS JOB` fences `configs/`, `jobs.yaml`, `notes.py`, `GENTLE_SLEEP_SECONDS`; `test_finviz_consumers.py:27,56` scans `src/` only for `finviz_get(`/`fetch_bars(`; the card adds no call | OK |
| 21 | X3 `grep -rn CollectorError src` | `except CollectorError` only at `runner.py:255,310`; `strike/measure.py:24` a docstring; radar imports only `FetchMetrics, finviz_get, scrub` (`radar/collector.py:17`); message text unchanged | OK |
| 22 | RESTARTS class home | `restarts.py:220` `static import reach`, `:228` `DOCS`, `:246` `test/documentation; no resident`; radar reaches `cobalt.archiver.collector` (`radar/collector.py:17`) and `.runner` (`radar/notes.py:349`); card `## RECORDS` names each class and the command. `uv run cobalt jobs restarts` not run (no `uv` in this seat) | OK |
| 23 | no new command (R411, R412) | rows use `uv run pytest` and `uv run cobalt jobs restarts` only | OK |
| 24 | preflight r2 FAIL and notes 2–4 fixed in the card | A2 rule: a retry whose wait would pass `RETRY_429_BUDGET_SECONDS` is NOT taken, nor past `RETRY_429_MAX`; budget lives in the runner, `record_retry` is row B's; test (4) sums retry waits only (15 s and up); red reasons stated in row order | OK |
| 25 | preflight r1 issues 1–7 fixed in the card | seam (A2 (2)), `REPORT_PATH` patch (B (a)), `requests` counted by the runner only, outcome rule (B), constructor and one-target clamp, R685 + R808/R812, waits-only | OK |

## ISSUES
1. NOTE (18) `## RECORDS` retry-bound line: "worst retry GET time ≤ 725 s" is the worst TOTAL retry time (500 × (1.2 s wait + ~0.25 s GET), waits included); 1504 + 725 = 2229 s holds. GET time past ~0.25 s (httpx timeout 30 s) is not bounded, as the card declares.
2. NOTE B: `<w>` is shown as `15.0s` by the examples only; a backoff constant is an int, so the runner must pass `float` (or `record_retry`/`retry_line` format one decimal) or a log line reads `15s`. Test (b) asserts only `7.0s`.
3. NOTE (22): `uv run cobalt jobs restarts` not run here; the classes are read from `restarts.py`.
4. NOTE (3): R685's words are about a defect he reports; it is his standing row, committed `HIS RULING` + `APPROVED` (L7a); R808 and R812 carry the archiver.

PREFLIGHT DONE · card: archiver-429-1009 · checks: 25 · fails: 0 · ready: YES
