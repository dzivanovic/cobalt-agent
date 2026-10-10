# archiver-429 — card 206 preflight r2, 2026-10-09 (read-only)

Card `prompts/2026-10-09/206-archiver-429-card.md`, draft `reports/archiver-429-draft-2026-10-09.md`, spec `prompts/CARD.md`, earlier `reports/archiver-429-preflight-2026-10-09.md`, amend `reports/archiver-429-amend-2026-10-09.md`. HEAD `d8019a97`. `git diff --stat f5010068 HEAD -- src tests ops configs` is empty, so the working tree is `f5010068`'s code.

## CHECKS

| # | command | output | OK/FAIL |
|---|---|---|---|
| 1 | `ls /Users/cobalt/cobalt-wt`; `git rev-parse --verify refs/heads/ops/archiver-429-1009`; read `ops/desk/desk-launch.sh` build mode (`:895–910`) | worktree `archiver-429-1009` absent; branch absent (exit 128) → a fresh `worktree add`; JOB, BRANCH, WORKTREE one name; REPORT is `<WT>/archiver-429-1009/docs/40 - DevDocs/reports/*.md`; TIP, CHECK REPORT, HOUSE B empty | OK |
| 2 | `git merge-base --is-ancestor fa968552 main`; `git diff --stat fa968552 HEAD -- src tests ops configs` | exit 0; empty (no code change past `f5010068`) | OK |
| 3 | `grep -n "^\| R685 "` in `reports/cto-2026-10-08.md`; `git diff --stat HEAD` of it | `:38` `HIS RULING (words R685, standing) … APPROVED · HIS RULING · APPLIED`; the file is `M` in the tree (the status snapshot), the row itself is in HEAD | OK |
| 4 | `grep -c -F "«FILL"` on the card | 0 | OK |
| 5 | `collector.py` at `f5010068` | `CollectorError :57`; `finviz_get :175`; `raise_for_status :213`; `raise CollectorError(f"Finviz HTTP failed: …") :215`; `fetch_bars :219`; `except Exception :234`; `"Fetch failed for …" :236`; `__all__ :242` | OK |
| 6 | `runner.py` at `f5010068` | `GENTLE_SLEEP_SECONDS = 1.2 :30`; `_backfill_window :59`; `_check_demand :80`; `_run_targets :182`; `_upsert_targets :237`, fetch `:249`, `except CollectorError :255`, sleep `:265`; `_append_targets :303`, fetch `:309`, sleep `:342`; `run_full :429`, f-string `:439`; `run_backfill :445`, `Backfill complete: :456`; `_archive_nightly :462`, `raise RuntimeError :482` | OK |
| 7 | `report.py`, tests, `jobs.yaml`, `notes.py` | `RunSummary :103`, `duration_str :205`, `append_run_report :228`, `REPORT_PATH :14`; runner tests `run :188`, `fetcher :196`, `_no_sleep_no_token :207–216`, pinned `:284`, `:303`; collector `MockTransport` seam `:169–189`; `jobs.yaml:214 timeout_s: 2400`; `notes.py:368` `rpm=60 / GENTLE_SLEEP_SECONDS`, `:369` window to `timeout_s` | OK |
| 8 | `grep -n` `logs/archiver.err` | 27 `Run complete:` lines `:996`–`:31985`, all `210 tickers … 0 failures`, 23m04s (`:1992`) to 25m04s (`:22249`); RUNNING `:32180`; 18 `_upsert_targets:257 … 429` lines, DKNG `:32431`, EXC `:32475`, LMT `:32637`, META `:32680`; `Run complete … 18 failures, 24m13s :33220`; F17 FAILED `:33221` | OK |
| 9 | `logs/radar.err:44531–44538`; `tunables.yaml:782–783` | `paused_market_reset` 20:30:10 … 20:41:50 every ~100 s; `archiver.write_mode` `upsert` | OK |
| 10 | A1 red on BASE | `FinvizRateLimited` absent → `ImportError`; the 500 control stays `CollectorError`; the constructor is pinned (`message`, `*, retry_after=None`) | OK |
| 11 | A2 red on BASE | the test cannot import `FinvizRateLimited` on BASE (`ImportError`); "1 failure" holds once A1 is built (row order) | OK, NOTE 2 |
| 12 | A2 negative controls (5), (6) | backfill budget 0 and a plain `CollectorError` are not retried; `run` takes `mode=` (`:188`); backfill at `FETCH_AT` 16:30 ET is outside the premarket window (as `:876`) | OK |
| 13 | B red on BASE | `RunSummary` has no `record_retry` → `AttributeError`; the `:439` f-string has no `retried`; a 429 is an ERROR failure, no WARNING | OK |
| 14 | every test offline | A2 (2) no longer calls `_archive_nightly` (it asserts on `failures`); B (a) patches `REPORT_PATH` and fakes `load_config`, `_run_targets`; A1 uses `MockTransport`; `_archive_nightly`/`as_job` appear in `tests/` only in `test_smoke.py`; `asyncio.sleep` is faked by the autouse fixture | OK |
| 15 | retry bound vs the 2400 s window (X2) | 10-09: 1453 s + 600 = 2053 s → 21:04:13; worst day 25m04s = 1504 + 600 = 2104 s; worst retry GET time ≤ 725 s → 2229 s < 2400 s. All hold only if the waits sum to ≤ 600 s | FAIL (see ISSUES 1) |
| 16 | L53 pacing (X1) | every retry wait ≥ 1.2 s (clamp low end), backoff 15/30/60; a success or an exhausted target is followed by the existing `sleep(GENTLE_SLEEP_SECONDS)` (`:265`, `:342`); the rpm bound `60/1.2 = 50` is unchanged | OK |
| 17 | no config, cadence or bucket | `## NOT IN THIS JOB` fences `configs/`, `jobs.yaml`, `notes.py`, `GENTLE_SLEEP_SECONDS`; `test_finviz_consumers.py:59` scans `finviz_get(`/`fetch_bars(` and the card adds no call | OK |
| 18 | X3 `grep -rn CollectorError src` outside `archiver/` | one hit, `strike/measure.py:24`, a docstring; `except CollectorError` only at `runner.py:255,310` | OK |
| 19 | RESTARTS class home | `restarts.py:220` `static import reach`, `:228` `DOCS`, `:246` `test/documentation; no resident`; radar imports `cobalt.archiver.collector` (`radar/collector.py:17`) and `.runner` (`radar/notes.py:349`); card `## RECORDS` names the class per path and the `uv run cobalt jobs restarts` command. Not run (no `uv` in this seat) | OK |
| 20 | no new command (R411, R412) | rows use `uv run pytest` and `uv run cobalt jobs restarts` only | OK |
| 21 | card committed and unchanged | `git diff --stat HEAD -- <card>` empty; last commit `d8019a97` | OK |
| 22 | earlier preflight issues 1–7 fixed in the card | 1 seam (A2 (2) asserts on `failures`), 2 `REPORT_PATH` patch (B (a)), 3 `requests` counted by the runner only (A2), 4 outcome rule (B), 5 constructor and one-target clamp test (A1, A2 (3)), 6 R685 plus R808, R812 (`## RECORDS`), 7 waits-only (`## NOT IN THIS JOB`) | OK |

## ISSUES
1. FAIL (15) A2: the rule says a 429 "after the budget is spent" is recorded as today, so a wait taken while any budget remains may overshoot `RETRY_429_BUDGET_SECONDS` (up to 659 s with a 60 s wait on 599 s used), but test (4) asserts the sum of retry waits ≤ 600 and the X2 bound (2229 s) assumes 600. The card must say a retry whose wait would take the used total past the budget is not taken (the 429 is recorded as a failure), so rule, test and bound agree.
2. NOTE (11) A2 (1), (2) and B (b) read "RED on BASE: 1 failure / no WARNING", but on BASE the test module's import of `FinvizRateLimited` fails first (`ImportError`, collection error for the whole runner test file); the stated red holds only after A1 is built (row order).
3. NOTE A2: where the budget used lives is not named (the helper's `summary` or a local); `record_retry` is row B's and A2's `files` omit `report.py`, so A2 cannot call it. State the budget in the runner (a local or a `summary` attribute set by the runner) and let B add `record_retry`.
4. NOTE A2 test (4): the recording `asyncio.sleep` also records the 1.2 s between-target sleeps; the test must sum only the retry waits (those from 15 s up, or a filter on the helper), not every recorded sleep.

PREFLIGHT DONE · card: archiver-429-1009 · checks: 22 · fails: 1 · ready: NO
