JOB: cos-outage
LADDER: OFF-LADDER — reports/f20-fix-preflight-2026-10-18.md ISSUES 5a 2026-10-18 R1863
BRANCH: deploy/cos-outage
WORKTREE: deploy-cos-outage
BASE: main
TIP: b5d62f17
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-cos-outage.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-18-cos-outage
MIGRATIONS: none
SET: cos-outage
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/cos-outage-1018` | `de3e15c8` | `b5d62f17` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-outage-1018-check-2026-10-18.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/ops/desk/deploy-outage.sh` · before `0` · after `5`
- `grep -c -F "com.cobalt.cos" /Users/cobalt/cobalt/ops/desk/deploy-step0.sh` · before `0` · after `1`

## SMOKE READS
- deploy-outage tests · `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_outage.py` · green: `0 failed` (this smoke read quotes the gate's pytest run; the hub adds no test run in production)
- deploy-step0 tests · `uv run pytest -q -p no:cacheprovider tests/ops/test_deploy_step0.py` · green: `0 failed` (as above)

## RECORDS
- cos-outage-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/cos-outage-1018-check-2026-10-18.md` last line: CHECK DONE · job: cos-outage-1018 · pass: 1 · tip: de3e15c8 · house A: Grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8612/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 165134
- cos-outage-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/cos-outage-1018` → `b5d62f17`; code tip `de3e15c8`
- written by deploy-card.sh at 2026-10-18 19:56 ET (`date`); trial merge of the heads onto main in order: clean
