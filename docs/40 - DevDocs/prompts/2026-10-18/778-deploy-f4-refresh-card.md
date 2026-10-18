JOB: f4-refresh
LADDER: S5 · F4
BRANCH: deploy/f4-refresh
WORKTREE: deploy-f4-refresh
BASE: main
TIP: 7b291371
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f4-refresh.md
RULINGS: 2026-10-18 R1833
TAG: deploy-2026-10-18-f4-refresh
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f4-refresh-1018` | `51b03e00` | `7b291371` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-check-2026-10-18.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "label: com.cobalt.prefill-refresh" /Users/cobalt/cobalt/configs/cobalt/jobs.yaml` · before `0` · after `1`
- `grep -c -F "key: prefill.refresh_interval_min" /Users/cobalt/cobalt/configs/cobalt/taxonomy/tunables.yaml` · before `0` · after `1`
- `grep -c -F "key: prefill.refresh_window" /Users/cobalt/cobalt/configs/cobalt/taxonomy/tunables.yaml` · before `0` · after `1`
- `grep -c -F "id: K12.3" /Users/cobalt/cobalt/configs/cobalt/smoke/s2.yaml` · before `0` · after `1`

## SMOKE READS
- The refresh plist is on main · `grep -c -F "<string>com.cobalt.prefill-refresh</string>" /Users/cobalt/cobalt/ops/com.cobalt.prefill-refresh.plist` · prints 1 or more
- The refresh subcommand is registered · `grep -c -F "REFRESH_JOB = \"com.cobalt.prefill-refresh\"" /Users/cobalt/cobalt/src/cobalt/prefill/cli.py` · prints 1

## RECORDS
- f4-refresh-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-check-2026-10-18.md` last line: CHECK DONE · job: f4-refresh-1018 · pass: 1 · tip: 51b03e00 · house A: Grok FINDINGS: 1 · findings: 3 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8538/0 · with-DB 5552/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 160500
- f4-refresh-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f4-refresh-1018` → `7b291371`; code tip `51b03e00`
- written by deploy-card.sh at 2026-10-18 11:34 ET (`date`); trial merge of the heads onto main in order: clean
