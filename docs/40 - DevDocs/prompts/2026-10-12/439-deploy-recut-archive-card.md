JOB: recut-archive-1012
LADDER: OFF-LADDER — reports/cto-2026-10-12.md R1138
BRANCH: deploy/recut-archive-1012
WORKTREE: deploy-recut-archive-1012
BASE: main
TIP: df775390
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-recut-archive-1012.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-12-recut-archive
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/recut-archive-1012` | `df775390` | `df775390` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/recut-archive-check-2026-10-12.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F -e "archive/pre-" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` · before count `0` · after a count of `1` or more (the recut arm's archive step)

## SMOKE READS
- The recut archive step is on main · `grep -c -F -e "archive/pre-" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` · prints 1 or more

## RECORDS
- recut-archive-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/recut-archive-check-2026-10-12.md` last line: CHECK DONE · job: recut-archive-1012 · pass: 1 · tip: df775390 · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4309/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 176420
- recut-archive-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/recut-archive-1012` → `df775390`; code tip `df775390`
- written by deploy-card.sh at 2026-10-12 21:07 ET (`date`); trial merge of the heads onto main in order: clean
