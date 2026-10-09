JOB: disarm-one-tap-1008
LADDER: OFF-LADDER — reports/cto-2026-10-08-words.md 2026-10-08 R689
BRANCH: deploy/disarm-one-tap-1008
WORKTREE: deploy-disarm-one-tap-1008
BASE: main
TIP: 81816e6d
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-disarm-one-tap-1008.md
RULINGS: 2026-10-08 R689
TAG: deploy-2026-10-09-disarm-one-tap
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/disarm-one-tap-1008` | `f70f3db8` | `81816e6d` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/disarm-one-tap-check-2026-10-09.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "DISARM_REASONS" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · before `0` · after `2` (the disarm reason list, radar page code)
- `grep -c -F "DISARM_REASONS" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · before `0` · after `3` (the disarm reason check, web)

## SMOKE READS
- the disarm reason list in the radar page code · `grep -c -F "DISARM_REASONS" /Users/cobalt/cobalt/src/cobalt/aset/radar_panel.py` · exit 0, a count of 1 or more
- the disarm reason check in the web code · `grep -c -F "DISARM_REASONS" /Users/cobalt/cobalt/src/cobalt/aset/web.py` · exit 0, a count of 1 or more

Card 134 (DISARM one tap, his R689). RESTARTS: com.cobalt.aset com.cobalt.radar (the check's stop line). The deploy runs when READY at any hour (L43). The check ended `held unfixed: 0 · ready: YES` at code tip `f70f3db8`; the branch head `81816e6d` adds docs only.

## RECORDS
- disarm-one-tap-1008: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/disarm-one-tap-check-2026-10-09.md` last line: CHECK DONE · job: disarm-one-tap-1008 · pass: 1 · tip: f70f3db8 · house A: Sol FINDINGS: 2 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: Grok FINDINGS: 0 · suites: offline 4045/0 · with-DB 4932/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 172187
- disarm-one-tap-1008: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/disarm-one-tap-1008` → `81816e6d`; code tip `f70f3db8`
- written by deploy-card.sh at 2026-10-09 13:52 ET (`date`); trial merge of the heads onto main in order: clean
