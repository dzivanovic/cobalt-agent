JOB: gate-alignment-1012
LADDER: OFF-LADDER — reports/cto-2026-10-12.md R1138
BRANCH: deploy/gate-alignment-1012
WORKTREE: deploy-gate-alignment-1012
BASE: main
TIP: 1178554e
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-gate-alignment-1012.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-12-gate-alignment
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/gate-alignment-1012` | `1178554e` | `1178554e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gate-alignment-check-2026-10-12.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "card 397" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` · before `0` · after `1`
- `grep -c -F "card 397" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `1`
- `grep -c -F "card 397" /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` · before `0` · after `1`
- `grep -c -F "SETTLED: <id> — R<n>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before `0` · after `1`

## SMOKE READS
- The gate reads the card line on main · `grep -c -F "card 397" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` · prints 1
- The hub wording is on main · `grep -c -F "SETTLED: <id> — R<n>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · prints 1

## RECORDS
- gate-alignment-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/gate-alignment-check-2026-10-12.md` last line: CHECK DONE · job: gate-alignment-1012 · pass: 1 · tip: 1178554e · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: none (not needed) · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 182141
- gate-alignment-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/gate-alignment-1012` → `1178554e`; code tip `1178554e`
- written by deploy-card.sh at 2026-10-12 08:57 ET (`date`); trial merge of the heads onto main in order: clean
