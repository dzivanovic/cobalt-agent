# Survey C5 — archiver Finviz HTTP 400 (2026-10-21)

## §0 Headline
- Finviz rejects the ticker WBD, not the request shape: all 5 WBD intervals (i1, i2, i5, i15, i30) return 400 on 10-19 and again on 10-20. The prompt named only i30 and i5; the err tail shows two of the five.
- The other 209 tickers fetch fine in the same runs; WBD was clean on 10-16.
- Why Finviz rejects WBD is UNPROVEN: a symbol change or delisting fits, but no log line or file says so, and Finviz was not called.
- WBD is still a target (`Radar Lists.md:238`), so it fails again every night and the job exits 1.

| candidate | verdict | proof |
|---|---|---|
| ticker rejected by endpoint (WBD symbol change or delisting) | UNPROVEN, best fit | `logs/archiver.err:40450-40458` and `:41677-41685`: WBD 400 on all 5 intervals, 10-19 and 10-20. `:39221-39227`: WBD OK on 10-16 (i1 10012 rows). `:40552`, `:41779`: "210 tickers … 5 failures", so only WBD failed. Cause of the rejection UNREAD (no Finviz call allowed). |
| malformed interval parameter | RULED OUT | `src/cobalt/archiver/collector.py:265` builds `{"t": ticker, "p": interval.value}` from the validated `Interval` enum; the same code gets all 5 intervals for the other 209 tickers; WBD itself succeeded on all 5 intervals on 10-16. `collector.py:8` notes `p=` is an enum. |
| rate or ceiling effect (L53) | RULED OUT | A rate limit returns 429. `collector.py:246-250` types 429 as `FinvizRateLimited`, and the run line reports `retried 0 (waited 0.0 s)` on 10-19 and 10-20 (`archiver.err:40552`, `:41779`). The 5 failures are 400, a different status. |
| token or session issue | RULED OUT | The same token is used by every request in the run; 3.37M rows were written for the other 209 tickers (`archiver.err:41779`). A bad token would fail all tickers. |
| code change in the fetch path | RULED OUT | `git log` of `collector.py` and `runner.py`: last change 2026-10-10 (a4aef3a0, 188190dc, the 429 retry work). The 10-13 to 10-16 runs had 0 failures after it. No change between 10-16 and 10-19. |

## FIX
- Smallest fix: remove WBD from the Lists note `1 - Trading/Radar Lists.md:238`, or replace it with the new symbol if Finviz renamed it. No code change.
- Test: after the edit, run `cobalt archiver` for ticker WBD only (or wait for tonight's 20:50 run) and expect `0 failures` in the `Run complete` line of `logs/archiver.err`.
- Before editing, confirm the WBD status on the Finviz site by hand (UNREAD: not checked here).
- Hardening (separate card, optional): a per-ticker 400 should not exit the whole job 1. `runner.py` collects it as a failure and `jobs/wrapper.py` raises RuntimeError (`archiver.err:41780`). UNREAD: the runner failure-collection code was not opened here.

## DECISIONS
- ASK DESK: remove WBD from `Radar Lists.md` now, or check its Finviz status first? [17:00 ET] Default: check status by hand, then remove or rename before tonight's 20:50 run.
- ASK DESK: open a card to make a single-ticker 400 non-fatal for the job exit code? [end of day] Default: no card until WBD is resolved; reopen if a second ticker fails the same way.

## RECORDS
- Report written: 2026-10-21 15:03 EDT (`date`).
- Read: day-open-2026-10-21.md, writing-rules.md, `archiver/collector.py:203-282`, `logs/archiver.err` (grep WBD, grep "Run complete"), `git log` of collector.py and runner.py, Vault grep for WBD.
- Not read: Finviz (not called), `runner.py` body, `jobs/wrapper.py`, any WBD news or ticker-change source.

SURVEY DONE · cause: Finviz rejects the WBD ticker (reason UNPROVEN) · decisions: 2
