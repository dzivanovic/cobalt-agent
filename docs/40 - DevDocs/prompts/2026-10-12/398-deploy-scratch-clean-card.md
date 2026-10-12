JOB: scratch-clean-1012
LADDER: OFF-LADDER — reports/cto-2026-10-12.md R1138
BRANCH: deploy/scratch-clean-1012
WORKTREE: deploy-scratch-clean-1012
BASE: main
TIP: 581d7b3a
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-scratch-clean-1012.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-12-scratch-clean
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/scratch-clean-1012` | `581d7b3a` | `581d7b3a` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/scratch-clean-check-2026-10-12.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F -e "scratch-clean.sh" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before count `0` · after count `1` (the BUILD-HUB E2 clutter line)

## SMOKE READS
- The clutter line is on main · `grep -c -F -e "scratch-clean.sh" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · prints 1
- The script is on main · `grep -c -F -e "scratch-clean" "/Users/cobalt/cobalt/ops/desk/scratch-clean.sh"` · prints a count of 1 or more

## RECORDS
- scratch-clean-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/scratch-clean-check-2026-10-12.md` last line: CHECK DONE · job: scratch-clean-1012 · pass: 1 · tip: 581d7b3a · house A: Grok FINDINGS: 2 · findings: 6 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 155480
- scratch-clean-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/scratch-clean-1012` → `581d7b3a`; code tip `581d7b3a`
- written by deploy-card.sh at 2026-10-12 07:36 ET (`date`); trial merge of the heads onto main in order: clean
