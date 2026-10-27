JOB: f4-strike-reserve
LADDER: S5-P2 · F4
BRANCH: deploy/f4-strike-reserve
WORKTREE: deploy-f4-strike-reserve
BASE: main
TIP: 48d45bed
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f4-strike-reserve.md
RULINGS: none
TAG: deploy-2026-10-26-f4-strike-reserve
MIGRATIONS: none
SET: f4-strike-reserve
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f4-strike-reserve` | `a79fca72` | `48d45bed` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-strike-reserve-check-2026-10-26.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "def radar_bucket_rpm(" /Users/cobalt/cobalt/src/cobalt/radar/collector.py` · before `0` · after `1`
- `grep -c -F "process_bucket(radar_bucket_rpm(" /Users/cobalt/cobalt/src/cobalt/radar/runner.py` · before `0` · after `1`
- `grep -c -F "key: radar.finviz_rpm" /Users/cobalt/cobalt/configs/cobalt/taxonomy/tunables.yaml` · before `0` · after `1`
- `grep -c -F "def refresh_burst_refusal(" /Users/cobalt/cobalt/src/cobalt/prefill/daily.py` · before `0` · after `1`
- `grep -c -F "REFRESH_BURST_RPM = 3" /Users/cobalt/cobalt/src/cobalt/strike/detector.py` · before `0` · after `1`

## SMOKE READS
- the refresh plist stays on disk, unloaded · `ls /Users/cobalt/cobalt/ops/com.cobalt.prefill-refresh.plist` · exit 0, listed

## RECORDS
- f4-strike-reserve: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-strike-reserve-check-2026-10-26.md` last line: CHECK DONE · job: f4-strike-reserve · pass: 1 · tip: a79fca72 · house A: Grok FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 9174/0 · with-DB 6010/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 17 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 232103
- f4-strike-reserve: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f4-strike-reserve` → `48d45bed`; code tip `a79fca72`
- written by deploy-card.sh at 2026-10-26 23:30 ET (`date`); trial merge of the heads onto main in order: clean
