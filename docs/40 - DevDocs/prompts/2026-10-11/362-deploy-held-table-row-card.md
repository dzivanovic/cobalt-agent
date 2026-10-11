JOB: held-table-row-1011
LADDER: OFF-LADDER — reports/cto-2026-10-11.md R1084
BRANCH: deploy/held-table-row-1011
WORKTREE: deploy-held-table-row-1011
BASE: main
TIP: 6625875e
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-held-table-row-1011.md
RULINGS: 2026-10-11 R1069
TAG: deploy-2026-10-11-held-table-row
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/held-table-row-1011` | `0188faa1` | `6625875e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/held-table-row-check-2026-10-11.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F -e "**HELD**" "/Users/cobalt/cobalt/ops/desk/deploy-card.sh"` · before count `0` · after count `2` (the table-row rule's comment and its awk test; `deploy-step0.sh` and `desk-launch.sh` the same, 0 before, 2 after)

## SMOKE READS
- the table-row held read is on main in the three scripts · `grep -c -F -e "**HELD**" "/Users/cobalt/cobalt/ops/desk/deploy-step0.sh"` · prints 2

## RECORDS
- held-table-row-1011: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/held-table-row-check-2026-10-11.md` last line: CHECK DONE · job: held-table-row-1011 · pass: 1 · tip: 0188faa1 · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: none (not needed) · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 137086
- held-table-row-1011: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/held-table-row-1011` → `6625875e`; code tip `0188faa1`
- written by deploy-card.sh at 2026-10-11 13:33 ET (`date`); trial merge of the heads onto main in order: clean
