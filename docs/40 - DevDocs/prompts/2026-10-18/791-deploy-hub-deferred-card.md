JOB: hub-deferred
LADDER: OFF-LADDER — reports/draft-cos-outage-2026-10-18.md DECISION 1 2026-10-18 R1863
BRANCH: deploy/hub-deferred
WORKTREE: deploy-hub-deferred
BASE: main
TIP: 77e04a2a
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-hub-deferred.md
RULINGS: 2026-10-18 R1863
TAG: deploy-2026-10-18-hub-deferred
MIGRATIONS: none
SET: none
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/hub-deferred-1018` | `79b8ac8e` | `77e04a2a` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-deferred-1018-check-2026-10-18.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "<deferred set>" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `5`
- `grep -c -F "minus every label of" "/Users/cobalt/cobalt/docs/40 - DevDocs/prompts/DEPLOY-HUB.md"` · before `0` · after `1`

## SMOKE READS
- hub-deferred tests · `uv run pytest -q -p no:cacheprovider tests/ops/test_hub_deferred_1018.py` · green: `0 failed` (this smoke read quotes the gate's pytest run; the hub adds no test run in production)

## RECORDS
- hub-deferred-1018: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/hub-deferred-1018-check-2026-10-18.md` last line: CHECK DONE · job: hub-deferred-1018 · pass: 1 · tip: 79b8ac8e · house A: Grok FINDINGS: 0 · findings: 5 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none (not needed) · suites: offline 8608/0 · with-DB 0/0 · live-note 147/0 · cobalt_dev: not taken · .env: removed · RESTARTS: none · files opened: 15 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 173800
- hub-deferred-1018: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/hub-deferred-1018` → `77e04a2a`; code tip `79b8ac8e`
- written by deploy-card.sh at 2026-10-18 18:53 ET (`date`); trial merge of the heads onto main in order: clean
