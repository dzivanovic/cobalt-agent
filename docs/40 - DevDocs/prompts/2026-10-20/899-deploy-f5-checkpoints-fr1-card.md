JOB: f5-checkpoints-fr1
LADDER: S5-P2 · F5
BRANCH: deploy/f5-checkpoints-fr1
WORKTREE: deploy-f5-checkpoints-fr1
BASE: main
TIP: 3c96ad2e
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f5-checkpoints-fr1.md
RULINGS: 2026-10-11 R1055, 2026-10-18 R1833
TAG: deploy-2026-10-20-f5-checkpoints-fr1
MIGRATIONS: 0027 · production at 0028 (469's vectors deployed 10-20 with 0027 unassigned; this fills the gap, FORWARD now reads 0026, 0027, 0028) · creates: the table `system.market_checkpoints` (owner cobalt_system, UNIQUE (trade_date, slot)) and DML plus sequence USAGE grants to cobalt_apply_system · old code on the new schema: additive, no existing object is touched and the old code never names the table, so a code revert alone runs on 0027; the rollback drops the table and every stored checkpoint row (the daily-note units stay) — changed against main: src/cobalt/db_migrations/0027_market_checkpoints.rollback.sql src/cobalt/db_migrations/0027_market_checkpoints.sql src/cobalt/db_migrations/__init__.py src/cobalt/db_migrations/placement.py»
SET: f5-checkpoints
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f5-checkpoints-fr1` | `3c96ad2e` | `3c96ad2e` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-checkpoints-fr1-check-2026-10-20.md` | `held unfixed: 0` and `ready: YES` | |

## READ-BACK
`COBALT_ENV=production uv run cobalt db query --side system --prod "SELECT count(*) AS m0027 FROM information_schema.tables WHERE table_schema = 'system' AND table_name = 'market_checkpoints'"`
- BEFORE `0` (the table does not exist)
- AFTER `1` (the table exists)

## MARKERS
- `grep -c -F "checkpoints:" /Users/cobalt/cobalt/configs/cobalt/prefill.yaml` · before `0` · after `1`
- `grep -c -F "checkpoint.narrative:" /Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml` · before `0` · after `1`
- `grep -c -F "label: com.cobalt.checkpoint-0715" /Users/cobalt/cobalt/configs/cobalt/jobs.yaml` · before `0` · after `1`

## SMOKE READS
- f5 offline · `uv run pytest -q tests/cobalt/test_checkpoints_offline.py tests/cobalt/test_checkpoints_registry.py tests/cobalt/test_finviz_consumers.py` · green: `0 failed`
- readers · `uv run cobalt jobs readers configs/cobalt/prefill.yaml` · green: `RESTARTS: com.cobalt.aset`, exit 0

## RECORDS
- f5-checkpoints-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-checkpoints-fr1-check-2026-10-20.md` last line: CHECK DONE · job: f5-checkpoints-fr1 · pass: 1 · tip: 3c96ad2e · house A: grok FINDINGS: 0 · findings: 2 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 1 · house B: gemini FINDINGS: 0 · suites: offline 8929/0 · with-DB 5828/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 17 · ready: YES · decisions: 2 · for Dejan: 0 · tokens: 238202
- f5-checkpoints-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-checkpoints-fr1` → `3c96ad2e`; code tip `3c96ad2e`
- written by deploy-card.sh at 2026-10-20 06:08 ET (`date`); trial merge of the heads onto main in order: clean
