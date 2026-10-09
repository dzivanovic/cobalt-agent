JOB: arm-unsized-1009
LADDER: OFF-LADDER — reports/cto-2026-10-09.md R719
BRANCH: deploy/arm-unsized-1009
WORKTREE: deploy-arm-unsized-1009
BASE: main
TIP: 46c96204
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-arm-unsized-1009.md
RULINGS: 2026-10-08 R685
TAG: deploy-2026-10-09-arm-unsized
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/arm-unsized-1009` | `676abb60` | `46c96204` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/arm-unsized-check-2026-10-09.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "ARM_UNSIZED_BUTTON" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · before `0` · after `2` (the inert ARM button for an unsized card)
- `grep -c -F "sized=all(" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · before `0` · after `1` (the card view's sized flag)

## SMOKE READS
- the inert ARM button in the radar page code · `grep -c -F "ARM_UNSIZED_BUTTON" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · exit 0, a count of 1 or more
- the sized flag in the radar page code · `grep -c -F "sized=all(" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · exit 0, a count of 1 or more

## RECORDS
- arm-unsized-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/arm-unsized-check-2026-10-09.md` last line: CHECK DONE · job: arm-unsized-1009 · pass: 1 · tip: 676abb60 · house A: Sol FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: Grok FINDINGS: 0 · suites: offline 4051/0 · with-DB 4938/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 182250
- arm-unsized-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/arm-unsized-1009` → `46c96204`; code tip `676abb60`
- written by deploy-card.sh at 2026-10-09 16:43 ET (`date`); trial merge of the heads onto main in order: clean
