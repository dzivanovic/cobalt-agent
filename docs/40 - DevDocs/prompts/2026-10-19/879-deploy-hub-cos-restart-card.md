JOB: hub-cos-restart-1019
LADDER: OFF-LADDER — reports/deploy-f16-close-fr2.md 2026-10-19 R2067
BRANCH: deploy/hub-cos-restart-1019
WORKTREE: deploy-hub-cos-restart-1019
BASE: main
TIP: d0d458c9
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-cos-restart-1019.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-19-hub-cos-restart-1019
MIGRATIONS: none
SET: hub-cos
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/hub-cos-restart-1019` | `d59fac71` | `d0d458c9` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-cos-restart-1019-check-2026-10-19.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "com.cobalt.cos: not loaded — skipped" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "launchctl kickstart -k gui/501/com.cobalt.cos" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `0`

## SMOKE READS
- hub-cos-restart tests · `uv run pytest -q -p no:cacheprovider tests/ops/test_hub_cos_restart_1019.py` · green: `0 failed` (this smoke read quotes the gate's pytest run; the hub adds no test run in production)

## RECORDS
- hub-cos-restart-1019: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-cos-restart-1019-check-2026-10-19.md` last line: CHECK DONE · job: hub-cos-restart-1019 · pass: 1 · tip: d59fac71 · house A: Grok FINDINGS: 0 · findings: 6 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 2 · house B: none (not needed) · suites: offline 8822/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 13 · ready: YES · decisions: 4 · for Dejan: 0 · tokens: 190519
- hub-cos-restart-1019: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-cos-restart-1019` → `d0d458c9`; code tip `d59fac71`
- written by deploy-card.sh at 2026-10-19 17:16 ET (`date`); trial merge of the heads onto main in order: clean
