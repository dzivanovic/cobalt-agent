JOB: radar-top50-1009
LADDER: OFF-LADDER — reports/cto-2026-10-09.md R716
BRANCH: deploy/radar-top50-1009
WORKTREE: deploy-radar-top50-1009
BASE: main
TIP: b5b61eb0
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-radar-top50-1009.md
RULINGS: 2026-10-08 R685
TAG: deploy-2026-10-09-radar-top50
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/radar-top50-1009` | `109bcfc0` | `b5b61eb0` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-top50-check-2026-10-09.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "over_cap" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · before `0` · after `7` (the over-cap pool rows)
- `grep -c -F "Over cap" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · before `0` · after `1` (the over-cap table title)

## SMOKE READS
- the over-cap rows in the radar page code · `grep -c -F "over_cap" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · exit 0, a count of 1 or more
- the over-cap table title in the radar page code · `grep -c -F "Over cap" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · exit 0, a count of 1 or more

## RECORDS
- radar-top50-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/radar-top50-check-2026-10-09.md` last line: CHECK DONE · job: radar-top50-1009 · pass: 1 · tip: 109bcfc0 · house A: Sol FINDINGS: 2 · findings: 9 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 3 · house B: Grok FINDINGS: 4 · suites: offline 4039/0 · with-DB 4926/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 153816
- radar-top50-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/radar-top50-1009` → `b5b61eb0`; code tip `109bcfc0`
- written by deploy-card.sh at 2026-10-09 17:53 ET (`date`); trial merge of the heads onto main in order: clean
