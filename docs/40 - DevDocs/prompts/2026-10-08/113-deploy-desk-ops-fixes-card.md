JOB: desk-ops-fixes-1008
LADDER: OFF-LADDER — reports/cto-2026-10-08.md R657
BRANCH: deploy/desk-ops-fixes-1008
WORKTREE: deploy-desk-ops-fixes-1008
BASE: main
TIP: 9aca7680
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-desk-ops-fixes-1008.md
RULINGS: 2026-10-08 R657
TAG: deploy-2026-10-08-desk-ops-fixes
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/desk-ops-fixes-1008` | `2413dbec` | `9aca7680` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-ops-fixes-check-2026-10-08.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "NOTIFY FAILED" /Users/cobalt/cobalt/ops/desk/close-timer.sh` · before `0` · after `4` (F2, the unsent notify)
- `grep -c -F "session list unreadable" /Users/cobalt/cobalt/ops/desk/stop-guard.py` · before `0` · after `3` (G2, fail closed)
- `grep -c -F "REPLACED:" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `2` (G3, install-ops)

## SMOKE READS
- close-timer notify present · `grep -c -F "NOTIFY FAILED" /Users/cobalt/cobalt/ops/desk/close-timer.sh` · exit 0, a count of 1 or more
- stop-guard fail-closed text present · `grep -c -F "session list unreadable" /Users/cobalt/cobalt/ops/desk/stop-guard.py` · exit 0, a count of 1 or more
- install-ops replace line present · `grep -c -F "REPLACED:" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · exit 0, a count of 1 or more

RESTARTS: none. Every path is under `ops/`, `tests/ops/`, `prompts/` or `docs/` (the check's stop line: `RESTARTS: none`). No `src/` path, no migration, no resident.

## RECORDS
- desk-ops-fixes: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-ops-fixes-check-2026-10-08.md` last line: CHECK DONE · job: desk-ops-fixes · pass: 1 · tip: 2413dbec · house A: Sol FINDINGS: 6 · findings: 11 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 6 · house B: Grok FINDINGS: 0 · suites: offline 3991/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 20 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 101004
- desk-ops-fixes: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-ops-fixes-1008` → `9aca7680`; code tip `2413dbec`
- written by deploy-card.sh at 2026-10-08 09:37 ET (`date`); trial merge of the heads onto main in order: clean
