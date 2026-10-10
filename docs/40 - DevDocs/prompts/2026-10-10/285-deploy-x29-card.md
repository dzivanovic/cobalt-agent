JOB: x29-fixture-1010
LADDER: OFF-LADDER — reports/cto-2026-10-06.md X29
BRANCH: deploy/x29-fixture-1010
WORKTREE: deploy-x29-fixture-1010
BASE: main
TIP: 3c00e204
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-x29-fixture-1010.md
RULINGS: 2026-10-08 R685
TAG: deploy-2026-10-10-x29-fixture
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/x29-fixture-1010` | `3c00e204` | `3c00e204` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/x29-fixture-check-2026-10-10.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `ls /Users/cobalt/cobalt/tests/cobalt/test_experiment_conftests.py` · before exit `1` (no such file) · after exit `0` (the new conftest-guard test, tests only)

## SMOKE READS
- the new test file exists on main · `ls /Users/cobalt/cobalt/tests/cobalt/test_experiment_conftests.py` · exit 0

## RECORDS
- x29-fixture-1010: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/x29-fixture-check-2026-10-10.md` last line: CHECK DONE · job: x29-fixture-1010 · pass: 1 · tip: 3c00e204 · house A: Sol FINDINGS: 1 · findings: 6 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: Grok FINDINGS: 0 · suites: offline 4199/0 · with-DB 5096/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 16 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 167561
- x29-fixture-1010: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/x29-fixture-1010` → `3c00e204`; code tip `3c00e204`
- written by deploy-card.sh at 2026-10-10 15:17 ET (`date`); trial merge of the heads onto main in order: clean
