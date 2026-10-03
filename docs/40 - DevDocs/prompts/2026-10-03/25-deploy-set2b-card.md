JOB: set2b-1003
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R77
BRANCH: deploy/set2b-1003
WORKTREE: deploy-1003-3
BASE: main
TIP: 8c32a8d1 47a689a1 f04a1d56
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-set2b-1003.md
RULINGS: 2026-10-02 R149, 2026-10-02 R157
TAG: deploy-2026-10-03-2
MIGRATIONS: none
SET: set2b

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/rename-follow-up-1003` | `393f3ad5` | `8c32a8d1` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rename-follow-up-check-2026-10-03.md` | `held unfixed: 0` and `ready: YES` |
| 2 | `ops/close-timer-1003` | `47a689a1` | `47a689a1` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/close-timer-check-2026-10-03.md` | `held unfixed: 0` and `ready: YES` |
| 3 | `ops/deploy-steps-1003` | `f04a1d56` | `f04a1d56` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-steps-check-2026-10-03.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F "The old side of a rename/copy" /Users/cobalt/cobalt/src/cobalt/jobs/restarts.py` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/ops/desk/close-timer.sh` · before `No such file or directory` · after listed
- `ls /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` · before `No such file or directory` · after listed

## SMOKE READS
- rename old-side test · `grep -c -F "def test_" /Users/cobalt/cobalt/tests/cobalt/test_jobs_restarts.py` · exit 0, a count of 1 or more
- close-timer plist in the tree · `ls /Users/cobalt/cobalt/ops/desk/com.cobalt.close-timer.plist` · exit 0, listed
- deploy step scripts · `ls /Users/cobalt/cobalt/ops/desk/deploy-outage.sh /Users/cobalt/cobalt/ops/desk/deploy-smoke.sh` · exit 0, both listed

## RECORDS
- rename-follow-up: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/rename-follow-up-check-2026-10-03.md` last line: CHECK DONE · job: rename-follow-up · pass: 1 · tip: 393f3ad5 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 7 · ready: YES · decisions: 0 · for Dejan: 0
- rename-follow-up: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/rename-follow-up-1003` → `8c32a8d1`; code tip `393f3ad5`
- close-timer: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/close-timer-check-2026-10-03.md` last line: CHECK DONE · job: close-timer · pass: 1 · tip: 47a689a1 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3737/0 · with-DB not run (DB: none) · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0
- close-timer: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/close-timer-1003` → `47a689a1`; code tip `47a689a1`
- deploy-steps: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-steps-check-2026-10-03.md` last line: CHECK DONE · job: deploy-steps · pass: 2 · tip: f04a1d56 · house B: Sol FINDINGS: 11 · findings: 11 · dropped: 0 · held: 9 · fixed: 9 · held unfixed: 0 · open: 0 · suites: offline 3737/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 21 · ready: YES · decisions: 0 · for Dejan: 0
- deploy-steps: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-steps-1003` → `f04a1d56`; code tip `f04a1d56`
- re-cut of card `23` (deploy `set2-1003` FAILED PREFLIGHT: P7 on `cli.py`, row 1 only); rows 2–4 of `23` unchanged, preflighted in `reports/set2-card-preflight-2026-10-03.md` (R131); no range touches `src/cobalt/db_migrations`. MARKERS, SMOKE READS filled by the desk at 16:45 ET.
- written by deploy-card.sh at 2026-10-03 16:45 ET (`date`); trial merge of the heads onto main in order: clean
