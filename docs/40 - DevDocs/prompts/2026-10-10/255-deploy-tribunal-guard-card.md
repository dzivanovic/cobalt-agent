JOB: tribunal-guard-1010
LADDER: OFF-LADDER — reports/cto-2026-10-10.md R877
BRANCH: deploy/tribunal-guard-1010
WORKTREE: deploy-tribunal-guard-1010
BASE: main
TIP: 8a7a938f
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-tribunal-guard-1010.md
RULINGS: 2026-10-08 R685
TAG: deploy-2026-10-10-tribunal-guard
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/tribunal-guard-1010` | `2e680273` | `8a7a938f` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/tribunal-guard-check-2026-10-10.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "G9 (R877)" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · before `0` · after `1` (the tribunal-hub house-call comment in the guard)

## SMOKE READS
- the guard's tribunal-hub marker · `grep -c -F "G9 (R877)" /Users/cobalt/cobalt/ops/desk/bare-guard.py` · exit 0, a count of 1 or more

## RECORDS
- tribunal-guard-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/tribunal-guard-check-2026-10-10.md` last line: CHECK DONE · job: tribunal-guard-1010 · pass: 1 · tip: 2e680273 · house A: Sol FINDINGS: 0 · findings: 4 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: Grok FINDINGS: 0 · suites: offline 4196/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 11 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 168237
- tribunal-guard-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/tribunal-guard-1010` → `8a7a938f`; code tip `2e680273`
- written by deploy-card.sh at 2026-10-10 09:31 ET (`date`); trial merge of the heads onto main in order: clean
