JOB: radar-direction-color-1007
LADDER: OFF-LADDER — reports/cto-2026-10-07-words.md 2026-10-07 R625
BRANCH: deploy/radar-direction-color-1007-attempt2
WORKTREE: deploy-radar-direction-color-1007-attempt2
BASE: main
TIP: 541adf0c
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-radar-direction-color-1007-attempt2.md
RULINGS: 2026-10-07 R625
TAG: deploy-2026-10-07-radar-direction-color-attempt2
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/radar-direction-color-1007` | `541adf0c` | `541adf0c` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-direction-color-check-2026-10-07.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "dir-long" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · before `0` · after `2` (the long tint class in the CSS and the markup map)
- `grep -c -F "def test_radar_direction_touches_only_strip_and_title" /Users/cobalt/cobalt/tests/cobalt/test_radar_panel_cards.py` · before `0` · after `1`

## SMOKE READS
- the long tint class in the page code · `grep -c -F "dir-long" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · exit 0, a count of 1 or more
- the control test present · `grep -c -F "def test_radar_direction_touches_only_strip_and_title" /Users/cobalt/cobalt/tests/cobalt/test_radar_panel_cards.py` · exit 0, a count of 1 or more

Card 89 (radar card direction colour, his R625: the strip and title are green for long, red for short, with an arrow). One `src/` file, `src/cobalt/aset/radar_panel.py`, class `static import reach` → `com.cobalt.aset,com.cobalt.radar`; plus its test file and DOCS. RESTARTS: com.cobalt.aset com.cobalt.radar (the deploy restarts aset and radar, about 50 s down). The market is open; the deploy runs when READY at any hour (L43). The check ended `held unfixed: 0 · ready: YES` at tip `541adf0c`.

## RECORDS
- radar-direction-color: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-direction-color-check-2026-10-07.md` last line: CHECK DONE · job: radar-direction-color · pass: 1 · tip: 541adf0c · house A: Sol FINDINGS: 2 · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 1 · suites: offline 3975/0 · with-DB 4859/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 148149
- radar-direction-color: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-direction-color-1007` → `541adf0c`; code tip `541adf0c`
- written by deploy-card.sh at 2026-10-07 12:30 ET (`date`); trial merge of the heads onto main in order: clean
