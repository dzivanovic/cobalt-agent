JOB: radar-arm-disarm-1007
LADDER: S3 smoke blocker (F7, SPRINT-LADDER-v0_1.md:65; his R627)
BRANCH: deploy/radar-arm-disarm-1007
WORKTREE: deploy-radar-arm-disarm-1007
BASE: main
TIP: e9600951
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-radar-arm-disarm-1007.md
RULINGS: 2026-10-07 R627
TAG: deploy-2026-10-07-radar-arm-disarm
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/radar-arm-disarm-1007` | `0544f91d` | `e9600951` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-arm-disarm-check-2026-10-07.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "/radar/card/{card_id}/arm" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `0` · after `1` (the ARM route)
- `grep -c -F "/radar/card/{card_id}/disarm" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `0` · after `1` (the DISARM route)
- `grep -c -F "def test_radar_arm_and_disarm_taps_render_on_watch_and_armed_only" /Users/cobalt/cobalt/tests/cobalt/test_radar_panel_cards.py` · before `0` · after `1`

## SMOKE READS
- the ARM route in the page code · `grep -c -F "/radar/card/{card_id}/arm" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · exit 0, a count of 1 or more
- the DISARM route in the page code · `grep -c -F "/radar/card/{card_id}/disarm" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · exit 0, a count of 1 or more
- the control test present · `grep -c -F "def test_radar_arm_and_disarm_taps_render_on_watch_and_armed_only" /Users/cobalt/cobalt/tests/cobalt/test_radar_panel_cards.py` · exit 0, a count of 1 or more

Card 92 (radar card ARM and DISARM taps, his R627): `src/cobalt/aset/web.py` and `src/cobalt/aset/radar_panel.py` (class `static import reach` → `com.cobalt.aset,com.cobalt.radar`), plus tests and DOCS. RESTARTS: com.cobalt.aset com.cobalt.radar (the deploy restarts aset and radar, about 50 s down). The market is open; the deploy runs when READY at any hour (L43). The check ended `held unfixed: 0 · ready: YES` at tip `0544f91d`; the branch head `e9600951` adds only the build report.

## RECORDS
- radar-arm-disarm: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-arm-disarm-check-2026-10-07.md` last line: CHECK DONE · job: radar-arm-disarm · pass: 1 · tip: 0544f91d · house A: Sol FINDINGS: 2 · findings: 6 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 0 · suites: offline 3991/0 · with-DB 4875/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165017
- radar-arm-disarm: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-arm-disarm-1007` → `e9600951`; code tip `0544f91d`
- written by deploy-card.sh at 2026-10-07 15:54 ET (`date`); trial merge of the heads onto main in order: clean
