JOB: f5-checkpoints-fr2
LADDER: S5-P2 · F5
BRANCH: deploy/f5-checkpoints-fr2
WORKTREE: deploy-f5-checkpoints-fr2
BASE: main
TIP: 6f31552f
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f5-checkpoints-fr2.md
RULINGS: 2026-10-11 R1055, 2026-10-18 R1833
TAG: deploy-2026-10-20-f5-checkpoints-fr2
MIGRATIONS: 0029 · production at 0028 (469's vectors deployed 10-20); the new migration is last in FORWARD and first in REVERSE · creates: the table `system.market_checkpoints` (owner cobalt_system, UNIQUE (trade_date, slot)) and DML plus sequence USAGE grants to cobalt_apply_system · old code on the new schema: additive, no existing object is touched and the old code never names it — changed against main: src/cobalt/db_migrations/0029_market_checkpoints.rollback.sql src/cobalt/db_migrations/0029_market_checkpoints.sql src/cobalt/db_migrations/__init__.py src/cobalt/db_migrations/placement.py
SET: f5-checkpoints
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f5-checkpoints-fr2` | `d910d45c` | `6f31552f` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-checkpoints-fr2-check-2026-10-20.md` | `held unfixed: 0` and `ready: YES` | |

## READ-BACK
`COBALT_ENV=production uv run cobalt db query --side system --prod "SELECT count(*) AS m0029 FROM information_schema.tables WHERE table_schema = 'system' AND table_name = 'market_checkpoints'"`
- BEFORE `0` (the table does not exist)
- AFTER `1` (the table exists)

## LAUNCHD
com.cobalt.checkpoint-0715 · deferred · prompts/2026-10-18/731-f5-card.md:PORT · dry run: none · gate: X2, X3, X4, X5, X6, X7, X10, X12, X13, values card
com.cobalt.checkpoint-0745 · deferred · prompts/2026-10-18/731-f5-card.md:PORT · dry run: none · gate: X2, X3, X4, X5, X6, X7, X10, X12, X13, values card
com.cobalt.checkpoint-0815 · deferred · prompts/2026-10-18/731-f5-card.md:PORT · dry run: none · gate: X2, X3, X4, X5, X6, X7, X10, X12, X13, values card
com.cobalt.checkpoint-0845 · deferred · prompts/2026-10-18/731-f5-card.md:PORT · dry run: none · gate: X2, X3, X4, X5, X6, X7, X10, X12, X13, values card

## MARKERS
- `grep -c -F "checkpoints:" /Users/cobalt/cobalt/configs/cobalt/prefill.yaml` · before `0` · after `1`
- `grep -c -F "checkpoint.narrative:" /Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml` · before `0` · after `1`
- `grep -c -F "label: com.cobalt.checkpoint-0715" /Users/cobalt/cobalt/configs/cobalt/jobs.yaml` · before `0` · after `1`
- `grep -c -F "label: com.cobalt.checkpoint-0745" /Users/cobalt/cobalt/configs/cobalt/jobs.yaml` · before `0` · after `1`
- `grep -c -F "label: com.cobalt.checkpoint-0815" /Users/cobalt/cobalt/configs/cobalt/jobs.yaml` · before `0` · after `1`
- `grep -c -F "label: com.cobalt.checkpoint-0845" /Users/cobalt/cobalt/configs/cobalt/jobs.yaml` · before `0` · after `1`

## SMOKE READS
(No suite line here: `deploy-smoke.sh` `shape()` maps only `ls`, `grep -c -F`, `curl` and `db query`, so a `uv run pytest` line is RED `no mapped shape`; STEP-G runs the suites. The `-0715` marker is the third line above, in the same form.)

## RECORDS
- f5-checkpoints-fr2: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-checkpoints-fr2-check-2026-10-20.md` last line: CHECK DONE · job: f5-checkpoints-fr2 · pass: 1 · tip: d910d45c · house A: Grok FINDINGS: 0 · findings: 3 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8929/0 · with-DB 5828/0 · live-note 148/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 10 · ready: YES · decisions: 1 · for Dejan: 0 · tokens: 235665
- f5-checkpoints-fr2: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f5-checkpoints-fr2` → `6f31552f`; code tip `d910d45c`
- house B: met by fr1's Gemini read (FINDINGS 0) on identical note-writing code, PROOF rows in `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f5-checkpoints-fr2-build-2026-10-20.md` (on `ops/f5-checkpoints-fr2`); fr2's delta is the migration number only (brain 2026-10-20 09:45, L79).
- written by deploy-card.sh at 2026-10-20 09:44 ET (`date`); trial merge of the heads onto main in order: clean
