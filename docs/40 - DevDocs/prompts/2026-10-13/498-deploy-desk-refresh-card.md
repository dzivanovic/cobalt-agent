JOB: desk-refresh-1013
LADDER: OFF-LADDER — reports/cto-2026-10-13.md R1323
BRANCH: deploy/desk-refresh-1013
WORKTREE: deploy-desk-refresh-1013
BASE: main
TIP: 824e478b
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-desk-refresh-1013.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-13-desk-refresh
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/desk-refresh-1013` | `824e478b` | `824e478b` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-refresh-check-2026-10-13.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "card 458" /Users/cobalt/cobalt/ops/desk/stop-guard.py` · before `0` · after `1` or more
- `grep -c -F "WRITE HANDOVER NOW" /Users/cobalt/cobalt/ops/desk/stop-guard.py` · before `0` · after `1` or more
- `grep -c -F "STATE AT" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/CTO-DESK-WAKEUP.md"` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/tests/ops/test_desk_refresh_wakeup.py` · before `absent` · after `present`

## SMOKE READS
- Live (census, not a gate): the desk's first turn after the merge shows `DESK SIZE <n> / 300,000` from the hook; the desk records it as one §4 row.

## RECORDS
- desk-refresh-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-refresh-check-2026-10-13.md` last line: CHECK DONE · job: desk-refresh-1013 · pass: 1 · tip: 824e478b · house A: Grok FINDINGS: 3 · findings: 5 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 2 · house B: none available · suites: offline 4317/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 182458
- desk-refresh-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-refresh-1013` → `824e478b`; code tip `824e478b`
- written by deploy-card.sh at 2026-10-13 08:29 ET (`date`); trial merge of the heads onto main in order: clean
