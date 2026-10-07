JOB: desk-stop-guard-1007
LADDER: OFF-LADDER — reports/cto-2026-10-06-words.md 2026-10-06 R590
BRANCH: deploy/desk-stop-guard-1007
WORKTREE: deploy-desk-stop-guard-1007
BASE: main
TIP: b133afb5
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-desk-stop-guard-1007.md
RULINGS: 2026-10-06 R596
TAG: deploy-2026-10-07-desk-stop-guard
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/desk-stop-guard-1006b` | `b133afb5` | `b133afb5` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-stop-guard-check-2026-10-07.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "start it:" /Users/cobalt/cobalt/ops/desk/stop-guard.py` · before `0` · after `4` (the desk-seat block sentence)
- `grep -c -F "def test_g1_the_desk_with_no_owed_block_is_blocked" /Users/cobalt/cobalt/tests/ops/test_stop_guard.py` · before `0` · after `1` (G1)

## SMOKE READS
- stop-guard desk seat in the script · `grep -c -F "start it:" /Users/cobalt/cobalt/ops/desk/stop-guard.py` · exit 0, a count of 1 or more
- G1 test present · `grep -c -F "def test_g1_the_desk_with_no_owed_block_is_blocked" /Users/cobalt/cobalt/tests/ops/test_stop_guard.py` · exit 0, a count of 1 or more

RESTARTS: none. Every path is under `ops/`, `tests/ops/` or `docs/` (the check's stop line: `RESTARTS: none`). No `src/` path, no migration, no resident. The hook is already installed for every Stop; no settings change.

## RECORDS
- desk-stop-guard: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-stop-guard-check-2026-10-07.md` last line: CHECK DONE · job: desk-stop-guard · pass: 1 · tip: b133afb5 · house A: Sol FINDINGS: 4 · findings: 9 · dropped: 0 · held: 5 · fixed: 5 · held unfixed: 0 · open: 4 · house B: Grok FINDINGS: 3 · suites: offline 3963/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 174440
- desk-stop-guard: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-stop-guard-1006b` → `b133afb5`; code tip `b133afb5`
- written by deploy-card.sh at 2026-10-07 07:13 ET (`date`); trial merge of the heads onto main in order: clean
