JOB: archiver-429-1009
LADDER: OFF-LADDER — reports/cto-2026-10-09.md R808
BRANCH: deploy/archiver-429-1009
WORKTREE: deploy-archiver-429-1009
BASE: main
TIP: a4aef3a0
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-archiver-429-1009.md
RULINGS: 2026-10-08 R685
TAG: deploy-2026-10-10-archiver-429
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/archiver-429-1009` | `a4aef3a0` | `a4aef3a0` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/archiver-429-check-2026-10-10.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "class FinvizRateLimited" /Users/cobalt/cobalt/src/cobalt/archiver/collector.py` · before `0` · after `1` (the typed 429 error)

## SMOKE READS
- the typed 429 error in the archiver collector · `grep -c -F "class FinvizRateLimited" /Users/cobalt/cobalt/src/cobalt/archiver/collector.py` · exit 0, a count of 1 or more

## RECORDS
- archiver-429-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/archiver-429-check-2026-10-10.md` last line: CHECK DONE · job: archiver-429-1009 · pass: 1 · tip: a4aef3a0 · house A: Sol FINDINGS: 5 · findings: 9 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 2 · suites: offline 4145/0 · with-DB 5034/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 22 · ready: YES · decisions: 3 · for Dejan: 0 · tokens: 207006
- archiver-429-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/archiver-429-1009` → `a4aef3a0`; code tip `a4aef3a0`
- written by deploy-card.sh at 2026-10-10 01:32 ET (`date`); trial merge of the heads onto main in order: clean
