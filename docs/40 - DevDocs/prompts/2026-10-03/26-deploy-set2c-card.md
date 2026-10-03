JOB: set2c-1003
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R77
BRANCH: deploy/set2c-1003
WORKTREE: deploy-1003-4
BASE: main
TIP: 8c32a8d1 f04a1d56
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-set2c-1003.md
RULINGS: 2026-10-02 R149, 2026-10-02 R157
TAG: deploy-2026-10-03-2
MIGRATIONS: none
SET: set2c

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/rename-follow-up-1003` | `393f3ad5` | `8c32a8d1` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rename-follow-up-check-2026-10-03.md` | `held unfixed: 0` and `ready: YES` |
| 2 | `ops/deploy-steps-1003` | `f04a1d56` | `f04a1d56` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-steps-check-2026-10-03.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F "The old side of a rename/copy" /Users/cobalt/cobalt/src/cobalt/jobs/restarts.py` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` · before `No such file or directory` · after listed

## SMOKE READS
- rename old-side test · `grep -c -F "def test_" /Users/cobalt/cobalt/tests/cobalt/test_jobs_restarts.py` · exit 0, a count of 1 or more
- deploy step scripts · `ls /Users/cobalt/cobalt/ops/desk/deploy-outage.sh /Users/cobalt/cobalt/ops/desk/deploy-smoke.sh` · exit 0, both listed

## RECORDS
- rename-follow-up: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rename-follow-up-check-2026-10-03.md` last line: CHECK DONE · job: rename-follow-up · pass: 1 · tip: 393f3ad5 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 7 · ready: YES · decisions: 0 · for Dejan: 0
- rename-follow-up: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/rename-follow-up-1003` → `8c32a8d1`; code tip `393f3ad5`
- deploy-steps: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-steps-check-2026-10-03.md` last line: CHECK DONE · job: deploy-steps · pass: 2 · tip: f04a1d56 · house B: Sol FINDINGS: 11 · findings: 11 · dropped: 0 · held: 9 · fixed: 9 · held unfixed: 0 · open: 0 · suites: offline 3737/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 21 · ready: YES · decisions: 0 · for Dejan: 0
- deploy-steps: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-steps-1003` → `f04a1d56`; code tip `f04a1d56`
- re-cut of card `25` (deploy `set2b-1003` FAILED at STEP-C on `05`'s plist); rows unchanged from card `23` rows 2 and 4, preflighted (R131); neither adds a plist or a `db_migrations` file. MARKERS, SMOKE READS filled by the desk at 16:49 ET.
- written by deploy-card.sh at 2026-10-03 16:49 ET (`date`); trial merge of the heads onto main in order: clean
