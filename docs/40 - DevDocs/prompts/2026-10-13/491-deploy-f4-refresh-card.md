JOB: f4-refresh-1010
LADDER: OFF-LADDER — reports/cto-2026-10-10.md R849
BRANCH: deploy/f4-refresh-1010
WORKTREE: deploy-f4-refresh-1010
BASE: main
TIP: b1ba47d8
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f4-refresh-1010.md
RULINGS: 2026-10-10 R849, 2026-10-10 R969
TAG: deploy-2026-10-13-f4-refresh
MIGRATIONS: none
SET: radar
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f4-refresh-1010` | `edd5c076` | `b1ba47d8` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-check-2026-10-10.md` | `held unfixed: 2` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md` |

## MARKERS
- «FILL: markers for f4-refresh-1010 (its job card has no ## DEPLOY PROOF)»

## SMOKE READS
- «FILL: smoke reads for f4-refresh-1010 (its job card has no ## DEPLOY PROOF)»

## RECORDS
- f4-refresh-1010: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-build-2026-10-10.md` at `b1ba47d8` last line: BUILT · job: f4-refresh-1010 · tip: edd5c076 | on d78c66a2 | migration: none | offline 4245/0 | with-DB 5173/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: com.cobalt.aset com.cobalt.radar | rows: 15 of 15 | self-check: 3 of 3 | decisions: 14 · for Dejan: 3 · tokens: 86732
- f4-refresh-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f4-refresh-check-2026-10-10.md` last line: CHECK DONE · job: f4-refresh-1010 · pass: 1 · tip: 98174119 · house A: Sol FINDINGS: 7 · findings: 16 · dropped: 0 · held: 7 · fixed: 5 · held unfixed: 2 · open: 11 · house B: Grok FINDINGS: 5 · suites: offline 4244/0 · with-DB 5169/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 21 · ready: NO · decisions: 7 · for Dejan: 2 · tokens: 323185
- f4-refresh-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f4-refresh-1010` → `b1ba47d8`; code tip `edd5c076`
- written by deploy-card.sh at 2026-10-13 08:23 ET (`date`); trial merge of the heads onto main in order: clean
