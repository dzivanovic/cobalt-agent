JOB: s4-p1-1009
LADDER: S4-P1 · F9
BRANCH: deploy/s4-p1-1009
WORKTREE: deploy-s4-p1-1009
BASE: main
TIP: 444e32b5
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-s4-p1-1009.md
RULINGS: 2026-10-06 R598
TAG: deploy-2026-10-09-s4-p1
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/s4-p1-1009` | `444e32b5` | `444e32b5` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/s4-p1-check-2026-10-09.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "def start_strike_thread" /Users/cobalt/cobalt/src/cobalt/radar/runner.py` · before `0` · after `1` (the strike loop thread starter)

## SMOKE READS
- the strike loop starter in the radar runner code · `grep -c -F "def start_strike_thread" /Users/cobalt/cobalt/src/cobalt/radar/runner.py` · exit 0, a count of 1 or more

## RECORDS
- s4-p1-1009: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/s4-p1-check-2026-10-09.md` last line: CHECK DONE · job: s4-p1-1009 · pass: 1 · tip: 444e32b5 · house A: Sol FINDINGS: 5 · findings: 11 · dropped: 0 · held: 4 · fixed: 4 · held unfixed: 0 · open: 7 · house B: Grok FINDINGS: 4 · suites: offline 4117/0 · with-DB 5006/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.radar · files opened: 23 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 259254
- s4-p1-1009: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/s4-p1-1009` → `444e32b5`; code tip `444e32b5`
- written by deploy-card.sh at 2026-10-09 22:47 ET (`date`); trial merge of the heads onto main in order: clean
