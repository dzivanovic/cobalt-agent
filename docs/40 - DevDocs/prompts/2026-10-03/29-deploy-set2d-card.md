JOB: set2d-1003
LADDER: OFF-LADDER — cto-2026-10-02.md 2026-10-02 R47
BRANCH: deploy/set2d-1003
WORKTREE: deploy-1003-5
BASE: main
TIP: e8b90904
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-set2d-1003.md
RULINGS: 2026-10-02 R149, 2026-10-02 R157
TAG: deploy-2026-10-03-3
MIGRATIONS: none
SET: set2d

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry |
|---|---|---|---|---|---|
| 1 | `ops/deploy-hub-text-1003` | `3395ef68` | `e8b90904` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-text-check-2026-10-03-r4.md` | `held unfixed: 0` and `ready: YES` |

## MARKERS
- `grep -c -F "REVERSE = (…)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `2`
- `grep -c -F "a Label the read cannot find is refused" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`

## SMOKE READS
- deploy hub text on main · `ls "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · exit 0, listed

## RECORDS
- deploy-hub-text: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-text-check-2026-10-03-r4.md` last line: CHECK DONE · job: deploy-hub-text · pass: 1 · tip: 3395ef68 · house A: none (overruled 2026-10-02 R47) · findings: 9 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: not needed · suites: as built (no commit) · cobalt_dev: not taken (DB: none) · .env: removed · RESTARTS: none · files opened: 9 · ready: YES · decisions: 0 · for Dejan: 0
- deploy-hub-text: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-hub-text-1003` → `e8b90904`; code tip `3395ef68`
- written by deploy-card.sh at 2026-10-03 21:01 ET (`date`); trial merge of the heads onto main in order: clean
