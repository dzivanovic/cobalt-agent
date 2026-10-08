JOB: radar-display-fix-1008
LADDER: OFF-LADDER — reports/radar-cards-survey-2026-10-08-r2.md 2026-10-08 R684
BRANCH: deploy/radar-display-fix-1008
WORKTREE: deploy-radar-display-fix-1008
BASE: main
TIP: eb14f860
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-radar-display-fix-1008.md
RULINGS: 2026-10-08 R685
TAG: deploy-2026-10-08-radar-display-fix
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/radar-display-fix-1008` | `eb14f860` | `eb14f860` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-display-fix-check-2026-10-08.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "termOpen" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · before `0` · after `2` (row B, an open TERMINAL is kept across the swap)
- `grep -c -F "def test_an_open_terminal_does_not_pause_the_tick" /Users/cobalt/cobalt/tests/cobalt/test_radar_panel.py` · before `0` · after `1`

## SMOKE READS
- the open-terminal keep in the page code · `grep -c -F "termOpen" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · exit 0, a count of 1 or more
- the control test present · `grep -c -F "def test_an_open_terminal_does_not_pause_the_tick" /Users/cobalt/cobalt/tests/cobalt/test_radar_panel.py` · exit 0, a count of 1 or more

Card 118 (`/radar` display fix, his R685). `src/cobalt/aset/radar_panel.py` and tests. RESTARTS: com.cobalt.aset com.cobalt.radar (the check's stop line). The deploy runs when READY at any hour (L43). The check ended `held unfixed: 0 · ready: YES` at tip `eb14f860`.

## RECORDS
- radar-display-fix-1008: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-display-fix-check-2026-10-08.md` last line: CHECK DONE · job: radar-display-fix-1008 · pass: 1 · tip: eb14f860 · house A: Sol FINDINGS: 3 · findings: 6 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 0 · suites: offline 4003/0 · with-DB 4887/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 13 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 176294
- radar-display-fix-1008: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-display-fix-1008` → `eb14f860`; code tip `eb14f860`
- written by deploy-card.sh at 2026-10-08 13:39 ET (`date`); trial merge of the heads onto main in order: clean
