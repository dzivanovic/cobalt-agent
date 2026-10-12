JOB: prodwrite-seat-1012
LADDER: OFF-LADDER — reports/cto-2026-10-12.md R1138
BRANCH: deploy/prodwrite-seat-1012
WORKTREE: deploy-prodwrite-seat-1012
BASE: main
TIP: b96737bf
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-prodwrite-seat-1012.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-12-prodwrite-seat
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/prodwrite-seat-1012` | `b96737bf` | `b96737bf` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-seat-check-2026-10-12.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F -e "prodwrite" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` · before count `0` · after a count of `1` or more (the launcher kind)
- `grep -c -F -e "WRITTEN · job:" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/PRODWRITE-HUB.md"` · before the file is absent · after count `1` (the seat's stop line)

## SMOKE READS
- The launcher kind is on main · `grep -c -F -e "prodwrite" "/Users/cobalt/cobalt/ops/desk/desk-launch.sh"` · prints a count of 1 or more
- The seat's hub is on main · `grep -c -F -e "WRITTEN · job:" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/PRODWRITE-HUB.md"` · prints 1

## RECORDS
- prodwrite-seat-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/prodwrite-seat-check-2026-10-12.md` last line: CHECK DONE · job: prodwrite-seat-1012 · pass: 1 · tip: b96737bf · house A: Grok FINDINGS: 3 · findings: 6 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 244290
- prodwrite-seat-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/prodwrite-seat-1012` → `b96737bf`; code tip `b96737bf`
- written by deploy-card.sh at 2026-10-12 09:37 ET (`date`); trial merge of the heads onto main in order: clean
