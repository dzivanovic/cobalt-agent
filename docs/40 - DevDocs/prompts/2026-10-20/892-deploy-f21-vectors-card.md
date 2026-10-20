JOB: f21-vectors-1013
LADDER: S5-P4 · F21
BRANCH: deploy/f21-vectors-1013
WORKTREE: deploy-f21-vectors-1013
BASE: main
TIP: c56817ec
REPORT: /Users/cobalt/cobalt/docs/40 - DevDocs/reports/deploy-f21-vectors-1013.md
RULINGS: none
TAG: deploy-2026-10-20-f21-vectors-1013
MIGRATIONS: 0028 · production at 0026 (0027 is unassigned on main; F5's port takes it later) · creates: the extension `vector` (IF NOT EXISTS, in `public`) and on `"user".genesis_chunk` the nullable columns `embedding vector(768)`, `embed_model`, `embed_dim` with the CHECK `genesis_chunk_embedding_stamped` · old code on the new schema: additive, the old code never names the columns, so a code revert alone runs on 0028; the rollback drops the three columns and every stored vector (the chunks and their FTS stay; the extension stays) — changed against main: src/cobalt/db_migrations/0028_genesis_vectors.rollback.sql src/cobalt/db_migrations/0028_genesis_vectors.sql src/cobalt/db_migrations/__init__.py»
SET: f21-vectors
TICKERS: none

## SHIPS

| # | branch | code tip | branch head | check report | its stop line must carry | fix report |
|---|---|---|---|---|---|---|
| 1 | `ops/f21-vectors-1013` | `c56817ec` | `c56817ec` | `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f21-vectors-check-r2-2026-10-19.md` | `held unfixed: 0` and `ready: YES` | |

## MARKERS
- `grep -c -F "openai_embeddings" /Users/cobalt/cobalt/configs/cobalt/modelaccess.yaml` · before `0` · after `1`
- `ls /Users/cobalt/cobalt/src/cobalt/genesis/embed.py` · before `No such file or directory` · after the path

## SMOKE READS
- embed command · `uv run cobalt genesis embed --help` · green: exits 0 and names the `embed` verb (the bare `embed` is not a smoke read: it writes vectors, the production run is its own K3 card)
- route tests · `uv run pytest -q tests/cobalt/test_modelaccess_config.py tests/cobalt/test_modelaccess_embed.py` · green: `0 failed`

## RECORDS
- f21-vectors-1013: check `/Users/cobalt/cobalt/docs/40 - DevDocs/reports/f21-vectors-check-r2-2026-10-19.md` last line: CHECK DONE · job: f21-vectors-1013 · pass: 1 · tip: c56817ec · house A: Grok FINDINGS: 0 · findings: 1 · dropped: 0 · held: 1 · fixed: 1 · held unfixed: 0 · open: 0 · house B: none available · suites: offline 8852/0 · with-DB 5751/0 · live-note 147/0 · cobalt_dev: 0013 · .env: removed · RESTARTS: com.cobalt.aset com.cobalt.cos com.cobalt.radar · files opened: 19 · ready: YES · decisions: 5 · for Dejan: 1 · tokens: 207817
- f21-vectors-1013: head `git -C /Users/cobalt/cobalt rev-parse --short=8 ops/f21-vectors-1013` → `c56817ec`; code tip `c56817ec`
- written by deploy-card.sh at 2026-10-20 00:45 ET (`date`); trial merge of the heads onto main in order: clean
