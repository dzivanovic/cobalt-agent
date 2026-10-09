JOB: desk-pane-by-id-1009
LADDER: OFF-LADDER — reports/cto-2026-10-09.md R779
BRANCH: deploy/desk-pane-by-id-1009
WORKTREE: deploy-desk-pane-by-id-1009
BASE: main
TIP: 3886b31e
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-desk-pane-by-id-1009.md
RULINGS: 2026-10-08 R685
TAG: deploy-2026-10-09-desk-pane-by-id
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/desk-pane-by-id-1009` | `3886b31e` | `3886b31e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-pane-by-id-check-2026-10-09.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "· pane <id>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · before `0` · after `1` (the HANDOVER line carries the pane id)
- `grep -c -F "A pane → leave it, name it in the plate as closable." "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · before `1` · after `0` (the old leave-it sentence)

## SMOKE READS
- the HANDOVER pane id in the wake-up file · `grep -c -F "· pane <id>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · exit 0, a count of 1 or more
- the old leave-it sentence is gone · `grep -c -F "A pane → leave it, name it in the plate as closable." "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · prints 0 (grep exits 1 on a zero count)

## RECORDS
- desk-pane-by-id-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-pane-by-id-check-2026-10-09.md` last line: CHECK DONE · job: desk-pane-by-id-1009 · pass: 1 · tip: 3886b31e · house A: Sol FINDINGS: 2 · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 0 · suites: offline 4054/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 17 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 141671
- desk-pane-by-id-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-pane-by-id-1009` → `3886b31e`; code tip `3886b31e`
- written by deploy-card.sh at 2026-10-09 19:54 ET (`date`); trial merge of the heads onto main in order: clean
