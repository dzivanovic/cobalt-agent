JOB: shadow-hub-1011
LADDER: OFF-LADDER — reports/cto-2026-10-11.md R1008
BRANCH: deploy/shadow-hub-1011
WORKTREE: deploy-shadow-hub-1011
BASE: main
TIP: ba541a29
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-shadow-hub-1011.md
RULINGS: 2026-10-11 R1009, 2026-10-11 R1055
TAG: deploy-2026-10-11-shadow-hub
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/shadow-hub-1011` | `90b8faad` | `ba541a29` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/shadow-hub-check-2026-10-11.md` | `held unfixed: 0` and `ready: YES` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/shadow-hub-build-2026-10-11.md` |

## MARKERS
- `grep -c -F -e "NEEDS HIS SIGN-OFF" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · before count `0` (file absent) · after count `3` (card 324, the three builder rows, still unsigned; the install card replaces the «SIGN cells later)

## SMOKE READS
- SHADOW-HUB is on main and still unsigned (launchers refuse) · `grep -c -F -e "«SIGN: his row»" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/SHADOW-HUB.md"` · prints 3

## RECORDS
- shadow-hub-1011: fix report `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/shadow-hub-build-2026-10-11.md` at `ba541a29` last line: BUILT · job: shadow-hub-1011 · tip: 90b8faad | on 680eca0e | migration: none | offline 4199/0 | with-DB 0/0 | live-note 146/0 | cobalt_dev: not taken | .env: removed | RESTARTS: none | rows: 13 of 13 | self-check: 3 of 3 | decisions: 4 · for Dejan: 1 · tokens: 195234
- shadow-hub-1011: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/shadow-hub-check-2026-10-11.md` last line: CHECK DONE · job: shadow-hub-1011 · pass: 1 · tip: cd302109 · house A: Sol FINDINGS: 9 · findings: 21 · dropped: 0 · held: 9 · fixed: 9 · held unfixed: 0 · open: 11 · house B: Grok FINDINGS: 7 · suites: offline 4199/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 24 · ready: YES · decisions: 5 · for Dejan: 3 · tokens: 270103
- shadow-hub-1011: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/shadow-hub-1011` → `ba541a29`; code tip `90b8faad`
- written by deploy-card.sh at 2026-10-11 10:16 ET (`date`); trial merge of the heads onto main in order: clean
