JOB: set1-1003
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R154
BRANCH: deploy/set1-1003
WORKTREE: deploy-1003-1
BASE: main
TIP: a50ec4c8 6d9fde8c
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-set1-1003.md
RULINGS: 2026-10-02 R149, 2026-10-03 R18, 2026-10-03 R29
TAG: deploy-2026-10-03-1
MIGRATIONS: none
SET: set1

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/lock-relief-1003` | `a50ec4c8` | `a50ec4c8` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/lock-relief-check-2026-10-03.md` | `held unfixed: 0` and `ready: YES` |
| 2 | `ops/order-open-test-1003` | `4b4b9f4a` | `6d9fde8c` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/order-open-test-check-2026-10-03.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F -e "--db-only" /Users/cobalt/cobalt/tests/cobalt/conftest.py` · before `0` · after `5`
- `grep -c -F "DB: none" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/BUILD-HUB.md"` · before `0` · after `5`
- `ls /Users/cobalt/cobalt/tests/cobalt/test_db_only_selection.py` · before `No such file or directory` · after listed
- `grep -c -F "house-probe.sh" /Users/cobalt/cobalt/tests/ops/test_order_open.py` · before `1` · after `3`

## SMOKE READS
- pass-1 selection test landed · `ls /Users/cobalt/cobalt/tests/ops/test_pass1_db_only.py` · exit 0, listed
- order-open stub test · `grep -c -F "not probed" /Users/cobalt/cobalt/tests/ops/test_order_open.py` · exit 0, a count of 1 or more

## RECORDS
- lock-relief: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/lock-relief-check-2026-10-03.md` last line: CHECK DONE · job: lock-relief · pass: 1 · tip: a50ec4c8 · house A: none (overruled 2026-10-02 R47) · findings: 2 · dropped: 0 · held: 2 · fixed: 2 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3737/0 · with-DB 846/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 2 · for Dejan: 0
- lock-relief: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/lock-relief-1003` → `a50ec4c8`; code tip `a50ec4c8`
- order-open-test: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/order-open-test-check-2026-10-03.md` last line: CHECK DONE · job: order-open-test · pass: 1 · tip: 4b4b9f4a · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 0 · for Dejan: 0
- order-open-test: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/order-open-test-1003` → `6d9fde8c`; code tip `4b4b9f4a`
- written by deploy-card.sh at 2026-10-03 10:24 ET (`date`); trial merge of the heads onto main in order: clean
