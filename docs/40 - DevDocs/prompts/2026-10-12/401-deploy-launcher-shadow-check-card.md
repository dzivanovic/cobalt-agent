JOB: launcher-shadow-check-1011
LADDER: OFF-LADDER — reports/cto-2026-10-11.md R1130
BRANCH: deploy/launcher-shadow-check-1011
WORKTREE: deploy-launcher-shadow-check-1011
BASE: main
TIP: ef754d0b
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-launcher-shadow-check-1011.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-12-launcher-shadow-check
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/launcher-shadow-check-1011` | `66c4fefc` | `ef754d0b` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-shadow-check-check-2026-10-11.md` | `held unfixed: 1` and `ready: NO` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md` |

## MARKERS
- `grep -c -F -e "On a shadow card the check counts and holds findings exactly as on any card" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · before count `0` · after count `1`
- `grep -c -F -e "SHADOW BUILT · job:" "/Users/cobalt/cobalt/ops/desk/preflight.sh"` · before count `0` · after count `1`

## SMOKE READS
- The shadow check wording is on main · `grep -c -F -e "On a shadow card the check counts and holds findings exactly as on any card" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CHECK-HUB.md"` · prints 1
- The preflight takes a shadow stop line on main · `grep -c -F -e "SHADOW BUILT · job:" "/Users/cobalt/cobalt/ops/desk/preflight.sh"` · prints 1

## RECORDS
- launcher-shadow-check-1011: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-shadow-check-build-2026-10-11.md` at `ef754d0b` last line: BUILT · job: launcher-shadow-check-1011 · tip: 66c4fefc | on a76d8855 | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 10 of 10 | self-check: 3 of 3 | decisions: 3 · for Dejan: 0 · tokens: 115749
- launcher-shadow-check-1011: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/launcher-shadow-check-check-2026-10-11.md` last line: CHECK DONE · job: launcher-shadow-check-1011 · pass: 1 · tip: a8c18242 · house A: Grok FINDINGS: 5 · findings: 6 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 1 · open: 1 · house B: none (not needed) · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: NO · decisions: 3 · for Dejan: 0 · tokens: 236094
- launcher-shadow-check-1011: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/launcher-shadow-check-1011` → `ef754d0b`; code tip `66c4fefc`
- written by deploy-card.sh at 2026-10-12 09:36 ET (`date`); trial merge of the heads onto main in order: clean
