JOB: hub-cos-restart-fr1
LADDER: OFF-LADDER — reports/deploy-f16-close-fr2.md 2026-10-19 R2067
BRANCH: deploy/hub-cos-restart-fr1
WORKTREE: deploy-hub-cos-restart-fr1
BASE: main
TIP: 6ee55933
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-cos-restart-fr1.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-19-hub-cos-restart-fr1
MIGRATIONS: none
SET: hub-cos
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/hub-cos-restart-fr1` | `0bf28619` | `6ee55933` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-cos-restart-fr1-check-2026-10-19.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "com.cobalt.cos: not loaded — skipped" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `2`
- `grep -c -F "com.cobalt.cos is loaded; its bootout and bootstrap strings are not on the deploy list (R60)" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`
- `grep -c -F "launchctl kickstart -k gui/501/com.cobalt.cos" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `0`

## SMOKE READS
- hub-cos-restart tests · `uv run pytest -q -p no:cacheprovider tests/ops/test_hub_cos_restart_1019.py` · green: `0 failed` (this smoke read quotes the gate's pytest run; the hub adds no test run in production)

## RECORDS
- hub-cos-restart-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-cos-restart-fr1-check-2026-10-19.md` last line: CHECK DONE · job: hub-cos-restart-fr1 · pass: 1 · tip: 0bf28619 · house A: Grok FINDINGS: 2 · findings: 7 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 1 · house B: none available · suites: offline 8822/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 10 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 200556
- hub-cos-restart-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-cos-restart-fr1` → `6ee55933`; code tip `0bf28619`
- written by deploy-card.sh at 2026-10-19 20:26 ET (`date`); trial merge of the heads onto main in order: clean
