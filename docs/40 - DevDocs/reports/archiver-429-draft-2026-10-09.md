# archiver-429 — drafter report, 2026-10-09

## §0 Headline
- Card `prompts/2026-10-09/206-archiver-429-card.md` written: rows A1 (typed 429 in the collector), A2 (bounded retry in the runner), B (retries named in the `Run complete:` line).
- Every brain fact proved in `logs/archiver.err` and `logs/radar.err`; the code read at `f5010068` is main's (no `src`/`tests`/`ops` diff to HEAD `1670f191`).
- 7 decisions, each its default; nothing waits for him.
- Uncommitted: the desk commits the card and fills `BASE`.

## CHANGES
- Added `docs/40 - DevDocs/prompts/2026-10-09/206-archiver-429-card.md`.
- Added this report.

## DECISIONS
1. 429 signal: a `FinvizRateLimited(CollectorError)` raised by `finviz_get` with `retry_after`, rather than the runner walking `__cause__` to the `httpx` response. Subclass keeps every other `except CollectorError` unchanged; message text unchanged.
2. Bounds, as module constants beside `GENTLE_SLEEP_SECONDS` (a tunable would be a config change): 3 retries; backoff 15/30/60 s; `Retry-After` clamped to [1.2, 60] s; 600 s retry budget per full run, so 24m13s + 600 s stays inside the 2400 s declared window.
3. "Inside the L53 bucket": the archiver has no `TokenBucket`; its L53 demand is the pacing bound `60 / GENTLE_SLEEP_SECONDS` (`radar/notes.py:368`). Every wait ≥ `GENTLE_SLEEP_SECONDS` keeps the send rate under it; each retry GET counts in `requests`.
4. A backfill gets budget 0 (no retry): its declared window is exact (`_backfill_window`) and a retry would run past it.
5. The retry helper covers `_append_targets` too (same fetch seam; a 429 there would otherwise open a false `empty_export` incident). Production runs `upsert` (`tunables.yaml:783`).
6. "The run report" = the `Run complete:` log line plus one WARNING per retry. The `archiver-runs.md` table and `job_result()` stay byte for byte: two existing tests pin them (`test_archiver_runner.py:284`, `:303`).
7. `DB` key left out, not `none`: `CARD.md` allows `none` only when every file sits under `ops/`, `tests/ops/` or `docs/`; this card touches `src/`. The rows' tests use fakes.

## RECORDS
- `git -C /Users/cobalt/cobalt show f5010068:src/cobalt/archiver/runner.py`, `…/collector.py`, `…/report.py`, `configs/cobalt/jobs.yaml` (23:20–23:35 ET): the cited symbols and lines; `f5010068` adds only `docs/…/deploy-s4-p1-1009.md`.
- `git -C /Users/cobalt/cobalt diff --stat f5010068 HEAD -- src tests ops`: empty, HEAD `1670f191` (23:40 ET).
- `grep -n` on `logs/archiver.err` (23:38 ET): 27 `Run complete:` lines 09-03 to 10-08, all `0 failures`, 23m04s–25m04s; 10-09: 18 × `429 Too Many Requests` at `runner:_upsert_targets:257`, 20:35:38–20:36:23 (12) and 20:40:18–20:41:12 (6); `Run complete: 210 tickers, 3308843 rows, 18 failures, 24m13s` at 20:54:15; F17 FAILED, `RuntimeError`. 1000 targets in 1453 s = ~41 rpm.
- `grep -n` on `logs/radar.err` (23:39 ET): `paused_market_reset` every ~100 s, 20:30:10–20:41:50 on 10-09.
- `grep` of `src/` for `429`/`Too Many`: only `strike/measure.py:16,51` (metrics status, not the exception).
- `src/cobalt/jobs/restarts.py:178–264`: a `src/` path derives by static import reach; radar reaches `cobalt.archiver.collector` (`radar/collector.py:17`) and `cobalt.archiver.runner` (`radar/notes.py:349`). Expected: `com.cobalt.radar`. Not run here (no `uv` in this seat).
- `reports/cto-2026-10-09.md:27`: R808.
- Fold R812 (`reports/archiver-429-decisions-2026-10-09.md` (6)): card 206 row B now pins `retried <n> (waited <s> s)` on every `Run complete:` line (`runner.py:439`), 0 included, and one WARNING per retry naming target, attempt, wait; red reasons updated; `Backfill complete:` (`:456`), `RunSummary` (`report.py:103`) re-proved, `git -C /Users/cobalt/cobalt diff --stat f5010068 HEAD -- src tests ops` empty at HEAD `fa968552`; BASE `fa968552` and RULINGS `2026-10-08 R685` kept as the desk set them.

ARCHIVER 429 CARD DRAFTED · decisions: 7 · fold R812 done
