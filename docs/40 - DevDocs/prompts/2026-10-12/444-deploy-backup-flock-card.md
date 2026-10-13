JOB: backup-flock-1012
LADDER: OFF-LADDER — reports/cto-2026-10-12.md R1289
BRANCH: deploy/backup-flock-1012
WORKTREE: deploy-backup-flock-1012
BASE: main
TIP: 82ae31fa
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-backup-flock-1012.md
RULINGS: 2026-10-12 R1138
TAG: deploy-2026-10-12-backup-flock
MIGRATIONS: none
SET: radar
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/backup-flock-1012` | `82ae31fa` | `82ae31fa` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/backup-flock-check-2026-10-12.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F -e "LOCK_WAIT_S" "/Users/cobalt/cobalt/src/cobalt/backup/restic.py"` · before count `0` · after a count of `1` or more (the lock wait constant)

## SMOKE READS
- The backup lock is on main · `grep -c -F -e "LOCK_WAIT_S" "/Users/cobalt/cobalt/src/cobalt/backup/restic.py"` · prints 1 or more

## RECORDS
- backup-flock-1012: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/backup-flock-check-2026-10-12.md` last line: CHECK DONE · job: backup-flock-1012 · pass: 1 · tip: 82ae31fa · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 4317/0 · with-DB 5220/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 152322
- backup-flock-1012: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/backup-flock-1012` → `82ae31fa`; code tip `82ae31fa`
- written by deploy-card.sh at 2026-10-12 23:42 ET (`date`); trial merge of the heads onto main in order: clean
