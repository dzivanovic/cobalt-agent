JOB: guard-d2-g7-1009
LADDER: OFF-LADDER — reports/cto-2026-10-08.md 2026-10-08 R707
BRANCH: deploy/guard-d2-g7-1009
WORKTREE: deploy-guard-d2-g7-1009
BASE: main
TIP: 8c6b5f7f c8a31812
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-guard-d2-g7-1009.md
RULINGS: 2026-10-08 R686
TAG: deploy-2026-10-09-guard-d2-g7
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/guard-d2-1009` | `8c6b5f7f` | `8c6b5f7f` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-d2-check-2026-10-09.md` | `held unfixed: 0` and `ready: YES` | |
| 2 | `ops/stop-guard-g7-1009` | `c8a31812` | `c8a31812` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/stop-guard-g7-check-2026-10-09.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "def secret_part(" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `1` (D2, G3 reads every verb's words)
- `grep -c -F "def queued(" /Users/cobalt/cobalt/ops/desk/stop-guard.py` · before `0` · after `1` (G7a, a QUEUE row blocks the stop)

## SMOKE READS
- D2 function present · `grep -c -F "def secret_part(" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · exit 0, a count of 1 or more
- secret guard still present · `grep -c -F "def is_secret(" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · exit 0, a count of 1 or more
- G7 function present · `grep -c -F "def queued(" /Users/cobalt/cobalt/ops/desk/stop-guard.py` · exit 0, a count of 1 or more
- stop guard still reads the OWED block · `grep -c -F "def owed_block(" /Users/cobalt/cobalt/ops/desk/stop-guard.py` · exit 0, a count of 1 or more

## RECORDS
- guard-d2-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/guard-d2-check-2026-10-09.md` last line: CHECK DONE · job: guard-d2-1009 · pass: 1 · tip: 8c6b5f7f · house A: Sol FINDINGS: 2 · findings: 8 · dropped: 0 · held: 7 · fixed: 7 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 1 · suites: offline 4036/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 184393
- guard-d2-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/guard-d2-1009` → `8c6b5f7f`; code tip `8c6b5f7f`
- stop-guard-g7-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/stop-guard-g7-check-2026-10-09.md` last line: CHECK DONE · job: stop-guard-g7-1009 · pass: 1 · tip: c8a31812 · house A: Sol FINDINGS: 4 · findings: 11 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 2 · suites: offline 4036/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 160632
- stop-guard-g7-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/stop-guard-g7-1009` → `c8a31812`; code tip `c8a31812`
- written by deploy-card.sh at 2026-10-09 12:51 ET (`date`); trial merge of the heads onto main in order: clean
