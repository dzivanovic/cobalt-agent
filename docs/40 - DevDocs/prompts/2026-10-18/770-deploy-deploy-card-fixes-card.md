JOB: deploy-card-fixes
LADDER: OFF-LADDER — reports/cto-2026-10-15.md HANDOVER PLAN (3) 2026-10-18 R1833
BRANCH: deploy/deploy-card-fixes
WORKTREE: deploy-deploy-card-fixes
BASE: main
TIP: 0f104d47
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-deploy-card-fixes.md
RULINGS: 2026-10-18 R1833
TAG: deploy-2026-10-18-deploy-card-fixes
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/deploy-card-fixes-1018` | `cc4995b6` | `0f104d47` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-card-fixes-1018-check-2026-10-18.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "already an ancestor of main" /Users/cobalt/cobalt/ops/desk/deploy-card.sh` · before `0` · after `2`

## SMOKE READS
- deploy-card tests · `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_card.py` · green: `0 failed` (this smoke read quotes the gate's pytest run; the hub adds no test run in production)

## RECORDS
- deploy-card-fixes-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-card-fixes-1018-check-2026-10-18.md` last line: CHECK DONE · job: deploy-card-fixes-1018 · pass: 1 · tip: cc4995b6 · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8493/0 · with-DB 0/0 · live-note 146/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 14 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 147022
- deploy-card-fixes-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/deploy-card-fixes-1018` → `0f104d47`; code tip `cc4995b6`
- written by deploy-card.sh at 2026-10-18 08:42 ET (`date`); trial merge of the heads onto main in order: clean
