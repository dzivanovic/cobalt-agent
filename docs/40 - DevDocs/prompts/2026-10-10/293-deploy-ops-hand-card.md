JOB: ops-hand-1010
LADDER: OFF-LADDER — reports/cto-2026-10-10.md R855
BRANCH: deploy/ops-hand-1010
WORKTREE: deploy-ops-hand-1010
BASE: main
TIP: 64d3049f
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-ops-hand-1010.md
RULINGS: 2026-10-10 R855
TAG: deploy-2026-10-10-ops-hand
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/ops-hand-1010` | `1a8614cc` | `64d3049f` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/ops-hand-check-2026-10-10.md` | `held unfixed: 0` and `ready: YES` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/ops-hand-build-2026-10-10.md` |

## MARKERS
- `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/OPS-HAND.md"` · before exit `1` (no such file) · after exit `0` (the ops-hand seat's fixed file, new; desk scripts and docs only, no resident)

## SMOKE READS
- the ops-hand fixed file is on main · `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/OPS-HAND.md"` · exit 0

## RECORDS
- ops-hand-1010: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/ops-hand-build-2026-10-10.md` at `64d3049f` last line: BUILT · job: ops-hand-1010 · tip: 1a8614cc | on 1eb47b59 | migration: none | offline 4196/0 | with-DB 5093/0 | live-note 146/0 | cobalt_dev: 0013 | .env: removed | RESTARTS: none | rows: 7 of 7 | self-check: 3 of 3 | decisions: 3 · for Dejan: 1 · tokens: 125383
- ops-hand-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/ops-hand-check-2026-10-10.md` last line: CHECK DONE · job: ops-hand-1010 · pass: 1 · tip: 6a18ff95 · house A: Sol FINDINGS: 1 · findings: 7 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 3 · suites: offline 4196/0 · with-DB 5093/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 1 · tokens: 195546
- ops-hand-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/ops-hand-1010` → `64d3049f`; code tip `1a8614cc`
- written by deploy-card.sh at 2026-10-10 17:33 ET (`date`); trial merge of the heads onto main in order: clean
