JOB: f21-genesis-fr1
LADDER: S5-P4 · F21
BRANCH: deploy/f21-genesis-fr1
WORKTREE: deploy-f21-genesis-fr1
BASE: main
TIP: b83bf7df
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f21-genesis-fr1.md
RULINGS: 2026-10-11 R1055
TAG: deploy-2026-10-19-f21-genesis-fr1
MIGRATIONS: 0026 · production at 0025 · creates: the table `"user".genesis_chunk` (one row per structural chunk of an imported source; `user_id` with the tenant GUC default and FK to `"user".traders`, `tsv` generated from `body`, owner `cobalt_user`) and its gin index `genesis_chunk_tsv` · old code on the new schema: additive, touches no existing object; the old code never reads or writes the table, so a code revert alone runs on 0026; the rollback drops the table and every imported chunk (re-import restores them) — changed against main: src/cobalt/db_migrations/0026_genesis_chunk.rollback.sql src/cobalt/db_migrations/0026_genesis_chunk.sql src/cobalt/db_migrations/__init__.py src/cobalt/db_migrations/placement.py
SET: f21-genesis
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f21-genesis-fr1` | `2cd0219a` | `b83bf7df` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f21-genesis-fr1-check-2026-10-19.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `ls /Users/cobalt/cobalt/src/cobalt/genesis/cli.py` · before `No such file or directory` · after the path
- `ls /Users/cobalt/cobalt/src/cobalt/genesis/store.py` · before `No such file or directory` · after the path

## SMOKE READS
- genesis CLI · `uv run cobalt genesis --help` · green: exits 0 and names the `import` and `search` verbs
- genesis tests · `uv run pytest -q tests/cobalt/test_genesis_offline.py` · green: `0 failed`

## RECORDS
- f21-genesis-fr1: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f21-genesis-fr1-check-2026-10-19.md` last line: CHECK DONE · job: f21-genesis-fr1 · pass: 1 · tip: 2cd0219a · house A: Grok FINDINGS: 0 · findings: 10 · dropped: 0 · held: 0 · fixed: 0 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8775/0 · with-DB 5715/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.radar · files opened: 15 · ready: YES · decisions: 0 · for Dejan: 0 · tokens: 179218
- f21-genesis-fr1: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f21-genesis-fr1` → `b83bf7df`; code tip `2cd0219a`
- written by deploy-card.sh at 2026-10-19 10:51 ET (`date`); trial merge of the heads onto main in order: clean
