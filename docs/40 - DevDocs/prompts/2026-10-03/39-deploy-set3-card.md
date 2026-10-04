JOB: set3-1004
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: deploy/set3-1004
WORKTREE: deploy-1004-1
BASE: main
TIP: 15ba4b75 53fed116 525b5ae1 47a689a1
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-set3-1004.md
RULINGS: 2026-10-02 R157, 2026-10-03 R216
TAG: deploy-2026-10-04-1
MIGRATIONS: none
SET: set3

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/adoption-port-1003` | `685b88d6` | `15ba4b75` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/adoption-port-check-2026-10-03-r3.md` | `held unfixed: 0` and `ready: YES` |
| 2 | `ops/dev-rebuild-port-1003` | `f5689418` | `53fed116` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/dev-rebuild-port-check-2026-10-03.md` | `held unfixed: 0` and `ready: YES` |
| 3 | `ops/desk-tools-port-1003` | `5c1d629f` | `525b5ae1` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-tools-port-check-2026-10-03.md` | `held unfixed: 0` and `ready: YES` |
| 4 | `ops/close-timer-1003` | `47a689a1` | `47a689a1` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/close-timer-check-2026-10-03.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F "window (v) does not hold" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `2`
- `ls /Users/cobalt/cobalt/src/cobalt/db_migrations/dev_rebuild.py` · before `No such file or directory` · after listed
- `grep -c -F "claude-fable-5-1" /Users/cobalt/cobalt/ops/desk/desk-launch.sh` · before `0` · after `2`
- `ls /Users/cobalt/cobalt/ops/desk/close-timer.sh` · before `No such file or directory` · after listed

## SMOKE READS
- adoption-port hub-line tests · `grep -c -F "def test_" /Users/cobalt/cobalt/tests/ops/test_hub_lines.py` · exit 0, a count of 1 or more
- dev-rebuild CLI tests · `grep -c -F "def test_" /Users/cobalt/cobalt/tests/cobalt/test_dev_rebuild_cli.py` · exit 0, a count of 1 or more
- desk-tools hooks · `ls /Users/cobalt/cobalt/ops/desk/stop-guard.py /Users/cobalt/cobalt/ops/desk/idle-wake.py` · exit 0, both listed
- close-timer plist · `ls /Users/cobalt/cobalt/ops/desk/com.cobalt.close-timer.plist` · exit 0, listed

## RECORDS
- adoption-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/adoption-port-check-2026-10-03-r3.md` last line: CHECK DONE · job: adoption-port · pass: 1 · tip: 685b88d6 · house A: none (overruled 2026-10-02 R47) · findings: 8 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 16 · ready: YES · decisions: 0 · for Dejan: 0
- adoption-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/adoption-port-1003` → `15ba4b75`; code tip `685b88d6`
- dev-rebuild-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/dev-rebuild-port-check-2026-10-03.md` last line: CHECK DONE · job: dev-rebuild-port · pass: 1 · tip: f5689418 · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 1 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 8 · ready: YES · decisions: 1 · for Dejan: 0
- dev-rebuild-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/dev-rebuild-port-1003` → `53fed116`; code tip `f5689418`
- desk-tools-port: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/desk-tools-port-check-2026-10-03.md` last line: CHECK DONE · job: desk-tools-port · pass: 1 · tip: 5c1d629f · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 22 · ready: YES · decisions: 0 · for Dejan: 0
- desk-tools-port: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/desk-tools-port-1003` → `525b5ae1`; code tip `5c1d629f`
- close-timer: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/close-timer-check-2026-10-03.md` last line: CHECK DONE · job: close-timer · pass: 1 · tip: 47a689a1 · house A: none (overruled 2026-10-02 R47) · findings: 4 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3737/0 · with-DB not run (DB: none) · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 12 · ready: YES · decisions: 0 · for Dejan: 0
- close-timer: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/close-timer-1003` → `47a689a1`; code tip `47a689a1`
- written by deploy-card.sh at 2026-10-04 14:40 ET (`date`); trial merge of the heads onto main in order: clean
- MIGRATIONS none: the build stop lines say `migration: none`; `db_migrations/cli.py` and `dev_rebuild.py` are code, no `.sql`. MARKERS, SMOKE READS filled by the desk (R216); `10` cobalt-guard deploys after its check.
