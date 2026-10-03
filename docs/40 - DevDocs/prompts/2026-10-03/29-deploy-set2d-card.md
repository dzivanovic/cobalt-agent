JOB: set2d-1003
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: deploy/set2d-1003
WORKTREE: deploy-1003-5
BASE: main
TIP: 59ef8d48
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-set2d-1003.md
RULINGS: 2026-10-02 R149, 2026-10-02 R157
TAG: deploy-2026-10-03-3
MIGRATIONS: none
SET: set2d

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/deploy-hub-text-1003` | `59ef8d48` | `59ef8d48` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-text-check-2026-10-03.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F "trap on every exit" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "[0-9][0-9][0-9][0-9]_*.sql" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `2`

## SMOKE READS
- deploy hub text on main · `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · exit 0, listed

## RECORDS
- deploy-hub-text: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-text-check-2026-10-03.md` last line: CHECK DONE · job: deploy-hub-text · pass: 1 · tip: 59ef8d48 · house A: none (overruled 2026-10-02 R47) · findings: 5 · dropped: 0 · held: 3 · fixed: 3 · held unfixed: 0 · open: 0 · house B: not needed · suites: offline 3739/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 0 · for Dejan: 0
- deploy-hub-text: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-hub-text-1003` → `59ef8d48`; code tip `59ef8d48`
- written by deploy-card.sh at 2026-10-03 19:26 ET (`date`); trial merge of the heads onto main in order: clean
