# Cobalt Assessment — Pass 1: Memory subsystem ("Hippocampus")

Date: 2026-08-21 · Baseline: `b71fc79` (main) · Assessor: Claude Fable 5 · Mode: read-only toward the system (code read; mocked tests run; live DB queried with `SELECT`/catalog reads only — zero writes)

Scope: `src/cobalt_agent/memory/{base,core,postgres}.py`, `src/cobalt_agent/db/schema.sql`, embeddings, `FastPathCache`, `tools/knowledge.py`, the HITL store that rides on the memory connection (`core/proposals.py:32-215`), DB-facing `dev_utils/*`, and `tests/test_postgres_graph.py`, `test_postgres_memory.py`, `test_mock_debug.py`, `test_browser_fast_path.py`.

Verdict legend: **RETAIN** · **BROKEN-FRICTION** (works badly / fragile / wrong but fixable) · **KILL-candidate** (proposal only — Dejan decides). **UNVERIFIED** = inferred, not read/run.

---

## 0. Headline findings (read these first)

| # | Finding | Evidence |
|---|---|---|
| H-1 | **`cobalt_brain` is shared with Mattermost.** Cobalt's memory tables live in the same database as the Mattermost server's own schema (`users`, `posts`, `sessions`, `jobs` ≈149k rows/36 MB, `db_migrations`, `ir_*`, `calls_*` …). `docker-compose.yml:40` points `MM_SQLSETTINGS_DATASOURCE` at `${POSTGRES_DB}` — the same variable Cobalt reads. Any "wipe/reset memory" utility, any `pg_dump`/restore, and the INFRA-1 `cobalt_dev` split must treat this DB as *Mattermost's* too. Also: Mattermost session tokens and Cobalt memory are one blast radius. | live catalog query (public schema: 121 tables, ~100 of them Mattermost); `docker-compose.yml:11,40` |
| H-2 | **Two incompatible DDLs for `hitl_proposals`.** Runtime DDL (`postgres.py:680-687`: `id VARCHAR(50)`, `status`, `tool_name`, `tool_kwargs JSONB`, `created_at`, `updated_at`) vs `schema.sql:159-168` (`id UUID`, `instrument_id UUID NOT NULL FK`, `proposal_type`, uppercase `status` CHECK, `execution_payload`, `mattermost_post_id`, `resolved_at`). Both are `CREATE TABLE IF NOT EXISTS`, so **whichever runs first on a fresh database wins**. Live DB has the runtime shape (verified via `information_schema`). On a fresh `cobalt_dev` where `dev_utils/init_5_pillar_schema.py` is run before the agent starts, every HITL insert (`proposals.py:63-68`) will fail (`tool_name` missing, `instrument_id NOT NULL`). | `postgres.py:674-708`, `schema.sql:159-168`, live columns |
| H-3 | **Conn-string builder does not URL-encode credentials** (the known gap): `postgres.py:612` `f"postgresql://{user}:{password}@{host}:{port}/{db}"` → an `@`, `/`, `:`, `#`, `%` or space in the password breaks parsing. Also a hardcoded password fallback `"cobalt_password"` at `:609`. All **psycopg2** callers (`dev_utils/*`, `skills/research/*`) pass keyword args and are unaffected — only `PostgresMemory` (and everything riding on `_get_conn()`, incl. the HITL store) broke. | `postgres.py:609-612,549` |
| H-4 | **`_hilt_` methods are dead code** — `store_hilt_proposal`, `get_hilt_proposal`, `update_hilt_proposal_status` (`postgres.py:1036,1063,1094`) have **zero callers** in `src/`, `dev_utils/`, `tests/`. The live HITL path is `HITLProposalStore` (`core/proposals.py:32-215`) which re-implements the same CRUD with raw SQL on `self.postgres._get_conn()`. Blast radius of the naming fix is therefore three method names + docstrings + CLAUDE.md; nothing breaks. The real issue is the duplication, not the spelling. | grep (§5) |
| H-5 | **FastPathCache's vector machinery is inert.** `lookup()` matches on exact `context_signature` only; it then embeds the *cached row's own* `task_hash` and compares it with the stored embedding of that same hash (`postgres.py:300-320`) — a tautology — and even when the threshold fails it falls through and returns the row with `similarity=1.0` (`:335-346`). `task_intent` is never used. Each lookup/write-back therefore costs one OpenAI `text-embedding-3-small` call for zero effect. `record_hit`, `invalidate_old_cache`, `get_metrics` have no callers. Live table holds **1 row** (Finviz "Morning Up Gapper", 2026-03-18, `execution_time_ms=0`). | `postgres.py:226-346,380-543`, live row |
| H-6 | **Every `PostgresMemory()` runs DDL.** Constructor executes 5 `CREATE TABLE/INDEX IF NOT EXISTS` blocks plus FastPath's 5 statements (incl. an `ivfflat` index) on **every instantiation**; it is instantiated in 9 places (`main.py:32`, `tools/browser.py:112`, `tools/knowledge.py:16`, `tools/daemon.py:60`, `tools/extractor.py:100`, `core/proposals.py:40`, `skills/research/finviz_extractor.py:86`, `interfaces/mattermost.py:513` fallback, `dev_utils/ingest_knowledge.py:28,154`). `ToolManager` alone builds 4 of them at start-up; Mattermost builds a fresh `HITLProposalStore` → `PostgresMemory()` on every `approve/reject` (`mattermost.py:479`). | grep (§5) |
| H-7 | **Embeddings go to OpenAI** (`text-embedding-3-small`, hardcoded at `postgres.py:243,762`; not routed through LiteLLM config/`active_profile`). 835 of 871 `memory_logs` rows are embedded, including **203 Obsidian-vault chunks** and **170 source-code chunks** ingested by `dev_utils/ingest_knowledge.py`, plus Mattermost/CLI conversation logs. Each `add_log` = vault decrypt + OpenAI round-trip + insert. Local-first principle (§4 requirements) is not honoured here; 1536-dim is baked into four DDLs, so switching embedder = migration. | `postgres.py:739-776`, live `memory_logs` by source |
| H-8 | **Test suite: 32 pass / 1 fail**, and the failing test (`test_scrub_secrets_with_vault_manager`) fails *because* `conftest.py` loads `.env`: `_scrub_secrets` calls `unlock(COBALT_MASTER_KEY)` on the test's fake vault, which **decrypts the production `data/.cobalt_vault` into the test process** and overwrites the fake secrets. The DB-level tests exercise a 250-line SQL-parsing mock cursor, not Postgres. | run output; `postgres.py:565-570`; `tests/test_postgres_memory.py:143-177` |

---

## 1. Component map

| Component | File:lines | Lines | Verdict | Notes |
|---|---|---:|---|---|
| `MemoryProvider` ABC | `memory/base.py` | 29 | RETAIN | Contract `add_log / get_context / search`. `get_context` is typed `List[Dict]`; Postgres impl returns `str` (`postgres.py:808-833`), JSON impl returns list. Only consumer `cli.py:179` does `str(...)`, so it works by accident. |
| `MemorySystem` (JSON) | `memory/core.py` | 97 | KILL-candidate | `data/memory.json` fallback used only when `PostgresMemory()` raises (`main.py:31-35`). Keyword search, 10-item RAM. Is the only thing `memory/__init__.py` exports. Keeps a second, silently-diverging memory store alive. If retained: make the fallback loud (Mattermost alert), not a warning log. |
| `PostgresMemory` core (`memory_logs`) | `postgres.py:546-892` | ~350 | RETAIN (fix H-3/H-6/H-7) | `add_log` → `_scrub_secrets` → embed → `INSERT`; `get_context` last-N as chat string; `search` cosine `<=>` with 0.3 floor. Connection-per-call, `autocommit=True`, no pool (fine at this scale). No vector index on `memory_logs` (seq scan; 871 rows — fine; becomes a problem ≫50k). |
| Graph memory (`graph_nodes`/`graph_edges`) | `postgres.py:621-672, 896-1034, 1120-1168` | ~200 | RETAIN (content stale) | Upsert/get node & edge; cascades; unique constraints. Live content = **one AST snapshot of `src/` taken 2026-03-08 07:01 (12 s window)**: 655 nodes (Function 261 / Method 250 / Class 99 / File 45), 610 edges **all `CONTAINS`**. Writers: `tools/extractor.py:258-293` (UniversalExtractor delta) and `dev_utils/ingest_knowledge.py`. No other entity types exist → the extractor path has never persisted a graph in prod (UNVERIFIED whether it ever ran). |
| HITL methods on `PostgresMemory` | `postgres.py:674-708, 1036-1118` | ~110 | KILL-candidate (dead) | See H-4. Table creation `_init_hitl_tables` is live and needed; the three `_hilt_` methods are not. |
| `HITLProposalStore` | `core/proposals.py:32-215` | 184 | RETAIN → fold into memory layer | Live path. Uses `print()` debug lines (`:61,69,75,171,177`) and manual `commit()/close()`; instantiates a full `PostgresMemory` (all DDL) just for a connection. Functionally the replacement for the dead `_hilt_` trio. |
| `FastPathCache` | `postgres.py:143-543` | 400 | BROKEN-FRICTION → KILL-candidate (embedding half) | See H-5. Exact-signature cache itself is a reasonable idea; `browser.py:393` builds the signature from **URL only** (`compute_context_signature(url, "", "")`), so "context" = URL. Recommend: keep `(task_hash, context_signature) → script` exact cache; drop `task_hash_embedding`, ivfflat index, `_generate_task_hash_embedding`, `_cosine_similarity`; wire `record_hit` or drop metrics. |
| Hash helpers | `postgres.py:38-140` | 100 | RETAIN | `compute_context_signature` (SHA-256 of url/title/text), `compute_task_hash` (SHA-256→UUID), `extract_visible_text` (HTMLParser). Pure, tested. |
| `KnowledgeSearchTool` | `tools/knowledge.py` | 65 | RETAIN | Thin wrapper over `search(limit=5)`; its own `PostgresMemory()`. |
| `schema.sql` (5-Pillar) | `db/schema.sql` | 229 | RETAIN w/ reconciliation | 13 `CREATE TABLE` (header says "14", init script says "12", expects 11). Only applied by `dev_utils/init_5_pillar_schema.py`. Live rows: `instruments` 345, `themes` 21, `market_snapshots` 2 209, everything else 0 (`daily_in_play`, `news_events`, `news_mentions`, `trades`, `strategy_signals`, `system_alerts`, `trading_accounts`, `order_fills`, `key_levels`). Writers in `src/`: only `scanner_orchestrator.py:85,98` (instruments, market_snapshots) and `semantic_tagger`/`sync_taxonomy` (themes/instruments) — Pass 4. `news_events`/`news_mentions`/`daily_in_play.catalyst`/`trades.trader_note_embedding` have **no writers anywhere**. |
| `dev_utils/init_5_pillar_schema.py` | 212 | | BROKEN-FRICTION (unguarded destructive) | `DROP TABLE IF EXISTS tickers CASCADE` (`:126-128`) then applies `schema.sql`; no prod-DB guard; would create the *wrong* `hitl_proposals` on a fresh DB (H-2); `expected_tables` (`:171-183`) omits `themes`' sibling `hitl_proposals` and `strategy_signals`… (11 of 13). |
| `dev_utils/db_status.py` | 333 | | RETAIN | Read-only audit; keyword-arg connection (safe); derives table list from `schema.sql` so it never audits `memory_logs`/`graph_*`/`browser_fast_path`. |
| `dev_utils/test_5_pillar_db.py` | 308 | | BROKEN-FRICTION | Mutating integration test (inserts/deletes `TEST_NVDA`) against whatever DB config resolves — i.e. **prod** — outside pytest, no guard. Not run. |
| `dev_utils/ingest_knowledge.py` | 172 | | BROKEN-FRICTION | Embeds `src/**/*.py`, `configs/*.yaml`, **entire `docs/` vault** into `memory_logs` via OpenAI (H-7). `IMPORTS` edge branch (`:68-82`) can never fire: it tests `target_path.parent / "cobalt_agent/…"` (= repo root, not `src/`) → explains 0 `IMPORTS` edges in the live graph. Re-running it appends duplicate chunks (no upsert/dedup on `memory_logs`). |
| Tests | `tests/test_postgres_graph.py` 573, `test_postgres_memory.py` 177, `test_mock_debug.py` 128, `test_browser_fast_path.py` 309 | 1 187 | BROKEN-FRICTION | See §6. |

---

## 2. Data-flow (what actually writes/reads memory at runtime)

```
main.py ──PostgresMemory()──► memory_logs  (add_log: "System Initialized", session start/end)
cli.py / mattermost.py ─────► memory_logs  (add_log user/assistant turns; cli: get_context, search)
tools/knowledge.py ─────────► memory_logs  (search, 0.3 floor, limit 5)
tools/extractor.py ─────────► graph_nodes/edges (upsert from LLM-extracted GraphExtractionOutput)
tools/browser.py ───────────► browser_fast_path (lookup by URL-hash; write_back)
skills/research/finviz_extractor.py ► browser_fast_path (write_back of scraped-preset scripts)
core/proposals.py HITLProposalStore ► hitl_proposals (create/get/pending/update/delete)
interfaces/mattermost.py:479 ─────► hitl_proposals via a new HITLProposalStore per approve/reject
dev_utils/ingest_knowledge.py ────► memory_logs (+ graph_*)  [manual]
skills/research/scanner_orchestrator.py (psycopg2, own conn) ► instruments, market_snapshots  [dev_utils runners only]
```
Every arrow above except the psycopg2 ones goes through `PostgresMemory._get_conn()` → the unquoted conn string (H-3).

Live activity: `memory_logs` spans 2026-02-15 → 2026-08-21; only **18 rows in the last 30 days**; `hitl_proposals` = 5 rows, all `approved`, 2026-03-04..06 (`browser` ×4, `write_file` ×1); graph untouched since 2026-03-08.

---

## 3. Hardcoded paths, names and structural assumptions

| Where | Value | Why it matters |
|---|---|---|
| `postgres.py:612` | conn string f-string | H-3; fix = `psycopg.connect(host=…, port=…, dbname=…, user=…, password=…)` or `psycopg.conninfo.make_conninfo()`. |
| `postgres.py:609` | `or os.getenv("POSTGRES_PASSWORD", "cobalt_password")` | default password in code (`.clinerules` rule 2 violation). |
| `config.py:108,614` | default db `cobalt_memory` | no such DB exists — only `cobalt_brain`; works solely because env sets it. |
| `postgres.py:613` | `table_name = "memory_logs"` | + `graph_nodes`, `graph_edges`, `hitl_proposals`, `browser_fast_path` literal in ~25 SQL strings. |
| `postgres.py:243,762` | `model="text-embedding-3-small"` | bypasses LiteLLM routing/config (non-negotiable #4). |
| `postgres.py:196,264,725`, `schema.sql:91,187` | `vector(1536)` ×4 tables, `[0.0]*1536` | embedder dimension baked into DDL. |
| `postgres.py:858` / `:270` / `browser.py:422` | similarity floor `0.3` / threshold `0.85` | magic numbers, not in `configs/`. |
| `postgres.py:465` | 30-day cache expiry | never called. |
| `postgres.py:565`, `vault.py:19`, `config.py:203,399` | `VaultManager()` → `data/.cobalt_vault` (CWD-relative) | `_scrub_secrets` re-opens and Fernet-decrypts the vault file on **every `add_log`**; CWD-dependent (OK under LaunchAgent `WorkingDirectory`, breaks when run from elsewhere). |
| `memory/core.py:22` | `data/memory.json` | JSON fallback store. |
| `postgres.py:629,644` vs `schema.sql` | `gen_random_uuid()` vs `uuid_generate_v4()` (uuid-ossp) | two UUID generators; `TIMESTAMP` (no tz) in runtime tables vs `TIMESTAMPTZ` in schema.sql tables — mixed tz semantics in one DB. |
| `postgres.py:747` | `config.keys.get("OPENAI_API_KEY")` | works only if the vault secret is literally named `OPENAI_API_KEY` (config.py:585 copies vault names verbatim); else falls to env; else `"dummy-local-key"` → OpenAI 401 → row saved **without** embedding (36 such rows exist). |
| `postgres.py:584-587` | scrubs every string in `config.keys` | correct intent; couples scrubbing to config shape. |
| `dev_utils/init_5_pillar_schema.py:147`, `db_status.py:301` | `…/src/cobalt_agent/db/schema.sql` relative to script | fine. |
| `dev_utils/ingest_knowledge.py:158-164` | `project_root/src`, `/configs`, `/docs` | `docs/` = the vault (Pass 0 F-1). |
| `core/proposals.py:48` (via `store_hilt_proposal` too) | 8-char `uuid4()[:8]` proposal IDs | ~4.3 B space; fine, but `id VARCHAR(50)` + schema.sql's `UUID` disagree. |

---

## 4. `_hilt_` / `hitl_` — full blast radius

- **Definitions**: `PostgresMemory.store_hilt_proposal` (`postgres.py:1036`), `get_hilt_proposal` (`:1063`), `update_hilt_proposal_status` (`:1094`). Inside they correctly reference table `hitl_proposals`.
- **Callers**: none in `src/`, `dev_utils/`, `tests/` (grep `hilt` outside `postgres.py` → 0 hits). CLAUDE.md is the only other mention.
- **Live path**: `HITLProposalStore` (`proposals.py:32-215`) + `ProposalEngine._get_hitl_store` (`:300-303`) + `mattermost.py:384,479`. Table/index names are consistently `hitl_*` there and in both DDLs.
- **Consequence**: renaming the three methods is zero-risk; deleting them is also zero-risk. The substantive debt is **two CRUD implementations for one table** (postgres.py trio vs HITLProposalStore) and **two DDLs** (H-2). Proposal: keep one store (HITLProposalStore semantics, moved under `memory/`), one DDL (decide runtime-shape vs schema.sql-shape — they encode different product ideas: tool-approval vs trade-proposal), delete the trio.
- Per CLAUDE.md this is *logged, not fixed* here.

---

## 5. Findings detail (RETAIN / BROKEN-FRICTION / KILL-candidate)

### RETAIN
- R-1 `MemoryProvider` contract, hash helpers, graph CRUD semantics (upsert-by-natural-key, cascade deletes, unique constraints) — `base.py`, `postgres.py:38-140,621-672,896-1034,1120-1168`.
- R-2 `search()` design (cosine via pgvector `<=>`, floor, metadata passthrough) — `postgres.py:835-872`; `KnowledgeSearchTool` — `knowledge.py`.
- R-3 Secret scrubbing *intent* before persistence/embedding — `postgres.py:551-598,784`.
- R-4 5-Pillar relational design (`schema.sql`) as the target data model; pgvector 0.8.1 + uuid-ossp present on the live DB.
- R-5 `dev_utils/db_status.py` as a read-only audit (extend to memory tables).

### BROKEN-FRICTION
- B-1 Conn string not URL-encoded + default password (H-3) — `postgres.py:609-612`.
- B-2 Dual DDL for `hitl_proposals`, order-dependent (H-2) — `postgres.py:674-708` vs `schema.sql:159-168`; `init_5_pillar_schema.py` unguarded `DROP` (`:126`).
- B-3 DDL on every construction; 9 construction sites; per-message `PostgresMemory()` in Mattermost approvals (H-6).
- B-4 Per-`add_log` vault decrypt + network embedding; embedder hardcoded, cloud-only, dimension baked in (H-7). `_scrub_secrets` silently no-ops when `COBALT_MASTER_KEY` is absent.
- B-5 `_init_db` swallows `memory_logs` DDL failure (`:730-731`) while `_init_graph_tables`/`_init_hitl_tables`/`FastPathCache._ensure_table_exists` raise → inconsistent failure semantics; object can exist with no `memory_logs`.
- B-6 `get_context` return type mismatch vs ABC (str vs list) — `postgres.py:808`, `base.py:20`, `core.py:47`.
- B-7 `ingest_knowledge.py`: dead `IMPORTS` branch (`:68-82`), appends duplicates on re-run, ingests vault into OpenAI.
- B-8 Tests: environment-dependent failure + production vault decrypted during tests (H-8); `src.`-prefixed imports in `test_browser_fast_path.py:279,284` bypass the autouse `cobalt_agent.memory.postgres.psycopg.connect` mock (different module object) — UNVERIFIED that this causes a real connection attempt (the file patches its own copy, so currently harmless); `test_postgres_graph.py` asserts against its own mock's SQL-parsing logic (`:57-262`), so schema drift cannot be detected by the suite. No pytest integration test against Postgres; the only one (`dev_utils/test_5_pillar_db.py`) is mutating and unguarded.
- B-9 `HITLProposalStore` `print()` debugging and manual commit/close on an autocommit connection (`proposals.py:61,69,75,171,177`).
- B-10 Mixed `TIMESTAMP`/`TIMESTAMPTZ` and `gen_random_uuid()`/`uuid_generate_v4()` across tables created by the two DDL sources.
- B-11 `schema.sql` header/init-script/expected-tables disagree (14 / 12 / 11 vs actual 13).

### KILL-candidates (proposals — Dejan decides)
- K-1 `PostgresMemory.store_hilt_proposal / get_hilt_proposal / update_hilt_proposal_status` — dead (H-4).
- K-2 FastPathCache embedding column, ivfflat index, `_generate_task_hash_embedding`, `_cosine_similarity`, unused `record_hit`/`invalidate_old_cache`/`get_metrics` (H-5). Keep the exact-match cache only if the browser fast path is retained in Pass 2.
- K-3 `memory/core.py` JSON `MemorySystem` fallback (silent divergence; replace with loud failure or a proper in-memory ring buffer).
- K-4 `dev_utils/test_5_pillar_db.py` (mutating, unguarded) — or convert into a guarded pytest `integration` test against `cobalt_dev` only.
- K-5 Runtime `memory_logs` seq-scan is fine now, but if `ingest_knowledge` is kept, add an HNSW index and a dedup key; otherwise drop `ingest_knowledge.py` in favour of the research-engine ingestion (§8 requirements).

---

## 6. Tests run (mocked; no DB mutation)

`uv run pytest tests/test_postgres_graph.py tests/test_postgres_memory.py tests/test_mock_debug.py tests/test_browser_fast_path.py -q` → **32 passed, 1 failed**.

- FAIL `tests/test_postgres_memory.py::TestSecretScrubber::test_scrub_secrets_with_vault_manager` — mechanism: `_scrub_secrets` (`postgres.py:565-570`) calls `unlock(os.getenv("COBALT_MASTER_KEY"))` on the injected fake vault; `VaultManager.unlock` (`vault.py:36-45`) reads the real `data/.cobalt_vault` and **replaces** `_secrets`, so the fake secret is gone. Passes only on a machine without the master key in `.env`/env. Log during the run: `🔐 Vault successfully unlocked into memory.` — i.e. production secrets were decrypted into the pytest process (read-only; nothing printed).
- `test_postgres_graph.py` (17) and `test_mock_debug.py` (1): pass against a hand-written SQL-interpreting mock cursor.
- `test_browser_fast_path.py` (12): hash functions (real), cache CRUD via `MockFastPathCache` (not the real class), `PostgresMemory` construction with patched `psycopg`.
- Also observed: the suite imports `cobalt_agent.memory.postgres` both as `cobalt_agent.*` and `src.cobalt_agent.*` → two module objects, two `PostgresMemory` classes in one process.

Coverage gaps: no test for `add_log`/`search`/`get_context` SQL, `_generate_embedding` failure modes, `HITLProposalStore`, conn-string building (B-1 would have been caught by a single `make_conninfo` test), or DDL parity with `schema.sql`.

---

## 7. Inputs to other passes / INFRA

- **INFRA-1 (`cobalt_dev`)**: do **not** switch `POSTGRES_DB` in `.env` — that variable also drives Mattermost (`docker-compose.yml:40`). Use `COBALT_POSTGRES__DB=cobalt_dev` (honoured at `config.py:104-108,611-615`). Decide the `hitl_proposals` DDL before the first `init_5_pillar_schema.py` run on dev (H-2). Guard `init_5_pillar_schema.py`, `test_5_pillar_db.py`, `ingest_knowledge.py` (and the missing `wipe_memory.py`/`reset_memory_table.py`, if they reappear) against `cobalt_brain`.
- **INFRA-0.5 backups**: `pg_dump cobalt_brain` = Mattermost + Cobalt in one dump; decide whether that is desired or whether Mattermost gets its own DB.
- **Pass 2 (browser)**: FastPath context signature = URL only (`browser.py:393`); cache has 1 row; K-2.
- **Pass 3 (HITL)**: single store decision (§4); per-message `PostgresMemory()`; `print()` debug.
- **Pass 4 (scanners)**: `scanner_orchestrator.py`/`semantic_tagger.py`/`sync_taxonomy.py` use psycopg2 with their own connections, bypassing `PostgresMemory` entirely; `news_events`/`news_mentions`/`daily_in_play.catalyst` have no writers.
- **Pass 5 (LLM routing)**: embedding model is the one LLM call that is *not* hot-swappable (H-7).
- **Pass 7 (config)**: `PostgresConfig` defaults, `.env.example` empty, conn-string builder location.
- **Research engine (§8 requirements)**: "filing/press-release text chunked into pgvector alongside the 5-pillar schema" — today's `memory_logs` is a grab-bag (system logs + code + vault + chat) with no type discipline beyond `source`/`metadata.type`; a dedicated `documents/chunks` table with a stable embedder and HNSW index is the cleaner landing zone.

---

## 8. UNVERIFIED (explicitly)

- Whether `tools/extractor.py`'s delta path has ever written to `graph_*` in prod (no non-AST entity types exist → likely never).
- Whether `.env` currently sets `OPENAI_API_KEY` or the vault holds a secret literally named `OPENAI_API_KEY` (835 embedded rows prove *one* of them is true).
- Whether the `src.`-prefixed test imports cause any real connection attempt (they patch their own module copy; autouse mock does not cover them).
- Exact Mattermost table count / size beyond the `jobs` outlier (catalog listed ~100 non-Cobalt tables; not analysed further — out of scope).
