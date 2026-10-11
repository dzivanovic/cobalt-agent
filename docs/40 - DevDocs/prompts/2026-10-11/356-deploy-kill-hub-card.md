JOB: kill-hub-row-1010
LADDER: OFF-LADDER — reports/cto-2026-10-10.md R937
BRANCH: deploy/kill-hub-row-1010
WORKTREE: deploy-kill-hub-row-1010
BASE: main
TIP: 13bafad7
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-kill-hub-row-1010.md
RULINGS: 2026-10-10 R855, 2026-10-11 R1009
TAG: deploy-2026-10-11-kill-hub-row
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/kill-hub-row-1010` | `b4d82ad6` | `13bafad7` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/kill-hub-row-read-2026-10-11.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F -e "ORPHAN-CLEAN, aset only" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before count `0` · after count `1` (card 284 K1, the kill sequence at 4.2; hub text only, no resident)
- `grep -c -F -e "killing the orphaned" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/STANDING-LIST.md"` · before count `0` · after count `1` (card 284 K3, the standing-list row)

## SMOKE READS
- the kill sequence is on main · `grep -c -F -e "ORPHAN-CLEAN, aset only" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · prints 1
- the standing-list row is on main · `grep -c -F -e "killing the orphaned" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/STANDING-LIST.md"` · prints 1

## RECORDS
- kill-hub-row-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/kill-hub-row-read-2026-10-11.md` last line: CHECK DONE · job: kill-hub-row-1010 · pass: 1 · tip: b4d82ad6 · house A: Grok FINDINGS: 8 · findings: 19 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 7 · house B: none (not needed) · suites: offline 4196/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 24 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 242415
- kill-hub-row-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/kill-hub-row-1010` → `13bafad7`; code tip `b4d82ad6`
- written by deploy-card.sh at 2026-10-11 11:06 ET (`date`); trial merge of the heads onto main in order: clean
