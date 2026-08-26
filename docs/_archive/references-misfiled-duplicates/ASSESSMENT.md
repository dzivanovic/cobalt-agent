# Cobalt — Read-only Code Assessment: Synthesis

Date: 2026-08-22 · Baseline: `7700336` (main) · Assessor: Claude Fable 5 · Passes: `00-inventory.md` → `07-config-vault-ops.md` (all in `docs/assessment/`)

**This document is a set of PROPOSALS.** Every verdict below is a recommendation with an evidence pointer; **all dispositions — especially KILL — are Dejan's at triage.** Original intent is recorded separately and never drove the verdict. One out-of-band hotfix was applied during the assessment at Dejan's instruction (path jail, `7700336`, finding 06-H1); nothing else was changed.

## Verdict tiers
- **KEEP-AS-IS** — works, fits the requirements; minor cleanups at most.
- **KEEP-CONCEPT / REBUILD-IMPLEMENTATION** — the idea is right (and often required by `COBALT-REQUIREMENTS.md`), the code is not; rebuild on the same contract.
- **REDESIGN** — the concept itself conflicts with the requirements or with how the system actually runs; needs a design decision before code.
- **KILL-candidate** — dead, superseded, or out of scope; proposal only.

---

## 1. Executive summary (the ten things that matter)

1. **Nothing income-producing runs today.** The only scheduled job is an 08:00 Gemini briefing; the Finviz scanner pipeline (the one collector that works and has produced real data) is not invoked by anything in production; no grading/EV/sizing, no priority setup, no `daily_in_play` output exists. (02-H1, 04-H1/H2, 06-H5)
2. **The architecture skeleton is right and worth keeping**: LiteLLM role-based routing (`llm.py`), pydantic-settings config, YAML-per-concern, vault-routed secrets, the 5-Pillar schema, Mattermost-as-interface, HITL-as-gate, Obsidian-as-record. The *implementations* around that skeleton are where the debt is. (05-H1, 07-H1, 01-R4, 03)
3. **Security findings needing action before any sprint** (INFRA-0 class): plaintext GitHub PAT in `.git/config` (00-F3); full config incl. Mattermost token + all vault secrets logged at DEBUG by every dev script (03-H6/07-H5); path jail was non-functional (06-H1, **fixed**); HITL approvals have no identity/channel binding and the card shows no parameters (03-H1/H2); `read_file`/`list_directory` ungated; DB + Mattermost share one database exposed on all interfaces (01-H1, 07-H6); production vault decrypted inside pytest (01-H8).
4. **Config is the root of many silent failures**: ~20 keys/fields are dropped, ignored, unvalidated or unconsumed — including the YAML vault path, `cortex_routing` (so the deterministic triage and the security intercept never fire), `scanners`, and a silent fall-back-to-defaults on validation error. (07-H2, 04-H4, 06-H2)
5. **Three parallel ACTION grammars and three ReAct loops**, a Cortex classification LLM call at T=0.7 per message, and four dead `prompts.yaml` sections with hardcoded `.py` copies — the "config-driven agents" principle is not met. (05-H3/H5/H8, 02-H4)
6. **The memory layer is functional but wasteful and cloud-coupled**: every `add_log` decrypts the vault and calls OpenAI embeddings; ~10 DDL statements per `PostgresMemory()` × 9 construction sites; FastPathCache is dead end-to-end; graph memory is a stale AST snapshot. (01-H5/H6/H7, 02-H6)
7. **Trading logic is green-field**: the single strategy cannot execute (arity, config key, data keys, result shape all mismatch); `strategies.yaml` has two readers and a strict schema nobody consumes; the in-play filter rules live only inside a Gemini prompt. (04-H3/H5)
8. **Vault integration must be rebuilt** (as the requirements already say): one root resolver (YAML key currently ignored), explicit folder policy, templates, index.md, HITL policy for system notes; the scheduler writes bypass HITL entirely. (06-H2/H4/H5)
9. **Ops is fragile**: PID file holds `uv`'s pid, no `KeepAlive`, boot race with LM Studio/OrbStack, `docker compose` invalid without `--profile core`, 122B model still configured, four Mattermost sessions, login failure exits the process silently. (07-H4/H6, 03-H7)
10. **Tests do not protect production**: 227 collected-ish across files but two whole suites fail on a phantom `load_config` patch, one collection error, one test that decrypts prod secrets, one that would post to Mattermost, and no coverage of the income path or of config precedence. (00-F6, 01-H8, 03-H10, 05-H7, 06-H8)

**Sequencing suggestion (income-first, per §16)**: (0) INFRA-0 security list → (1) config fixes that unblock everything (`populate_by_name`, `cortex_routing`, silent-default removal, `.env.example`) → (2) scanner pipeline into `CobaltScheduler` + typed snapshot + `daily_in_play` writer + Mattermost alert (the first usable value) → (3) HITL hardening (card shows params, user binding, single store/DDL) → (4) memory cleanup (embedding via routing, DDL once, drop FastPath) → (5) vault rebuild (INFRA-2) → (6) routing/prompt consolidation → (7) setups/grading/EV once an intraday data source exists.

---

## 2. Component verdict table (proposals)

Columns: Component · Where · Proposed tier · Original intent (short; full trail in the pass doc) · Evidence.

### 2.1 Memory / Hippocampus (Pass 1)
| Component | Where | Tier | Original intent | Evidence |
|---|---|---|---|---|
| `MemoryProvider` ABC | `memory/base.py` | KEEP-AS-IS (fix `get_context` type) | JSON↔Postgres swappable store (`a366e9e`) | 01 §1, B-6 |
| `MemorySystem` JSON fallback | `memory/core.py` | KILL-candidate | early file memory; superseded by §11#9 Postgres | 01 K-3 |
| `PostgresMemory` core (`memory_logs`, `search`) | `memory/postgres.py` | KEEP-CONCEPT / REBUILD (conn-string, DDL-once, embedding via routing, scrub w/o re-unlock) | RAG memory `8463874`, Vector Librarian `8c6c5d8`, Manifest "PostgreSQL (Vector+Relational)" | 01 H-3/H-6/H-7, B-4/B-5 |
| OpenAI embeddings call sites | `postgres.py:242,761` | REDESIGN (route + local-first decision; dim migration) | RAG upgrade; conflicts with ADR-002 "zero data leakage" | 01 H-7, 05 H-2 |
| Graph memory (`graph_nodes/edges`) | `postgres.py` | KEEP-CONCEPT / REBUILD (when a consumer exists) | watcher deltas, AST graph (`333c2c3`, `37f51ed`) | 01 §1, 02 H-6 |
| `_hilt_` trio | `postgres.py:1036-1118` | KILL-candidate (dead) | persistent HITL `cf9cf4f` | 01 H-4 |
| `HITLProposalStore` | `core/proposals.py:32-215` | KEEP-CONCEPT / REBUILD (fold into memory layer, drop prints) | persistent approvals `cf9cf4f` | 01 §1, 03 |
| Runtime `hitl_proposals` DDL vs `schema.sql` DDL | both | REDESIGN (one DDL, decide shape) | tool-approval vs trade-proposal models | 01 H-2, 03 H-4 |
| `FastPathCache` (+ browser side) | `postgres.py:143-543`, `browser.py:362-479` | KILL-candidate | Playwright script reuse `b090110` ("Phase 3") | 01 H-5, 02 H-6 |
| 5-Pillar `schema.sql` | `db/schema.sql` | KEEP-AS-IS (reconcile counts/DDL; drop Ion-era `trading_accounts/order_fills`? — Dejan) | `cc14caa`; PRD-001 Math Package; task 34 journaling | 01 §1, 04 |
| `dev_utils/init_5_pillar_schema.py` | | KEEP-CONCEPT / REBUILD (guard, no DROP) | schema migration | 01 B-2 |
| `dev_utils/db_status.py` | | KEEP-AS-IS (extend to memory tables; fix logging sink) | audit utility | 01 §1, 07 H-5 |
| `dev_utils/test_5_pillar_db.py` | | KILL-candidate (or convert to guarded integration test) | DB integration check | 01 K-4 |
| `dev_utils/ingest_knowledge.py` | | KILL-candidate (replace with research-engine ingestion) | Vector Librarian | 01 B-7/K-5 |
| `tools/knowledge.py` | | KEEP-AS-IS | vector search tool | 01 R-2 |
| Memory tests | `tests/test_postgres_*`, `test_mock_debug` | REDESIGN (mock-SQL tests → real `cobalt_dev` integration) | | 01 §6 |

### 2.2 Browser / Playwright / scanners (Pass 2)
| Component | Where | Tier | Original intent | Evidence |
|---|---|---|---|---|
| `BrowserTool` plain URL→text + llms.txt pre-flight | `tools/browser.py` | KEEP-AS-IS (enforce whitelist; drop DSL) | initial agent; Scout "Web Browsing" | 02 §1 |
| Browser action DSL, `AOMExtractor`, `Maps` | `browser.py`, `aom.py`, `maps.py` | KILL-candidate | AOM agentic loop `b090110` (never completed) | 02 H-4 |
| Domain whitelist (`is_url_allowed`) | `aom.py:46-85` | KEEP-CONCEPT / REBUILD (apply to all navigation; subdomains) | zero-trust "Airlock" | 02 H-5 |
| Vault credential injection | `browser.py:276-360` | KEEP-CONCEPT / REBUILD (`config.vault_manager` bug) | zero-trust | 02, 07 H-2 |
| `UniversalExtractor` + `compute_delta` | `tools/extractor.py` | REDESIGN (or KILL; depends on research-engine graph need) | watcher daemon `333c2c3` | 02 §1 |
| `DaemonTool` watchers | `tools/daemon.py` | KILL-candidate (replace with scheduled collectors) | watcher daemon; task 33 alerts | 02 H-7 |
| `FinvizExtractor` (Playwright scraper) | `skills/research/finviz_extractor.py` | KILL-candidate (superseded by API) | Recon Scout `8a69874` | 02 H-2 |
| `FinvizApiClient` | `finviz_api.py` | KEEP-AS-IS (presets → YAML, columns → config) | Macro Engine `cc14caa`; Req §7 | 02 §1 |
| `ScannerOrchestrator` + `scanners.yaml` | | KEEP-CONCEPT / REBUILD (schedule wiring, typing, conn factory) | PRD-001 Story A; Req §1/§5 | 02 H-1/H-8, §4 |
| `MetadataEnricher` | `enrich_metadata.py` | KEEP-AS-IS | Tier-1 fundamentals | 02 §1 |
| `SemanticTagger` + `themes` + `sync_taxonomy` | | KEEP-CONCEPT / REBUILD (status vocab, wrapper) | theme tagging; Req §8 context | 02, 04 H-7 |
| `dev_utils/live_run_orchestrator.py` | | KEEP-CONCEPT / REBUILD (signature) | pipeline stress test | 02 H-3 |
| `dev_utils/live_run_{finviz,finviz_quote,dynamic_scanners}.py` | | KEEP-AS-IS (manual smoke) | | 02 §1 |
| Registered non-runnable tools (`aom/maps/extractor/daemon`) | `tool_manager.py:86-100` | KILL-candidate | "dangerous tools" `4f44d94` | 02 H-7 |
| Browser tests | `tests/test_browser_*`, `test_daemon`, `test_universal_extractor`, `test_finviz_extractor` | REDESIGN (fix import, drop DSL tests, add collector tests) | | 02 H-10 |

### 2.3 Mattermost / HITL (Pass 3)
| Component | Where | Tier | Original intent | Evidence |
|---|---|---|---|---|
| `MattermostInterface` REST helpers + native WS loop | `interfaces/mattermost.py:52-208,789-854` | KEEP-AS-IS (cache team/channel ids; per-message `get_my_user_id` → once) | task 33 "Red Phone"; `4f44d94` | 03 §1 |
| `_run_websocket_in_process`, `_handle_events` | `mattermost.py:732-787` | KILL-candidate | pre-native WS | 03 |
| Approval interceptor (approve/reject → execute) | `mattermost.py:380-500` | REDESIGN (identity binding, channel enforcement, params in card, single path) | Req §3/§11#1 tokenized HITL; Security Architecture OTET (never built) | 03 H-1/H-2/H-3 |
| Mattermost-local ReAct loop + parsers | `mattermost.py:502-725,210-325` | KILL-candidate (fold into `BaseDepartment`) | `4f44d94` parsing fixes | 03, 05 H-8 |
| `ProposalEngine.create/send/approve_and_get_payload` | `proposals.py:278-511` | KEEP-CONCEPT / REBUILD | persistent approvals | 03 |
| `ProposalEngine` dead methods (`wait_for_approval`…`create_proposal_and_send_to_mattermost`) | `proposals.py:513-652` | KILL-candidate | shared-memory callbacks `770c43b` | 03 |
| `Proposal`/`IntentAlignment` | `proposals.py:218-274` | KEEP-AS-IS (card must render params) | intent-driven loop `37f51ed` | 03 H-2 |
| `DANGEROUS_TOOLS` + `bypass_hitl` | `tool_manager.py` | KEEP-CONCEPT / REBUILD (gate `read_file`/`list_directory`? — policy) | Bouncer `4f44d94` | 03, 06 H-1 |
| `Cortex._generate_proposal` (unpersisted intercept) | `cortex.py:118-150` | REDESIGN (persist or drop) | `5becd1e` | 03 H-9, 04 H-4 |
| `MATTERMOST_CREDS` vault routing | `config.py:557-592` | KEEP-AS-IS (kill DEBUG dump) | `5becd1e` | 03 H-6 |
| `Config.unlock_vault/inject_secrets` | `config.py:407-500` | KILL-candidate | earlier naming | 03 |
| Login-failure exit / no supervisor | `main.py:175-207`, plist | REDESIGN (supervision + alert) | | 03 H-7, 07 H-4 |
| HITL tests | `tests/test_proposals_intent.py`, `test_cortex.py` | REDESIGN (fix fixture; add interface/engine tests) | | 03 H-10 |

### 2.4 Trading logic / scanners (Pass 4)
| Component | Where | Tier | Original intent | Evidence |
|---|---|---|---|---|
| `Strategos` | `brain/tactical.py` | KEEP-CONCEPT / REBUILD | Tactical dept `9c1af63`; Manifest | 04 §6 |
| `Playbook` | `brain/playbook.py` | KEEP-CONCEPT / REBUILD (one reader, validated, registry) | Configurable Strategy Engine `8463874` | 04 H-3/H-5 |
| `Strategy` ABC | `brain/strategy.py` | KEEP-CONCEPT / REBUILD (enforce) or KILL | Backtester/Live contract | 04 §6 |
| `SecondDayPlay` | `strategies/second_day_play.py` | KILL-candidate (non-priority, Ion-era Math Package) | PRD-001 §4 | 04 H-3 |
| `strategies.yaml` + `StrategyConfig` | | REDESIGN (schema for the four priority setups; one reader) | Req §4/§6 | 04 H-5 |
| `rules.yaml trading_rules` | | KEEP-AS-IS (consume fully; move in-play rules here) | `53611fe` | 04 H-4 |
| `rules.yaml cortex_routing` | | KEEP-CONCEPT / REBUILD (capture in config) | Triage Desk `87e16c7` | 04 H-4 |
| `FinanceTool` | `tools/finance.py` | KEEP-AS-IS (swing-context; not for setups) | `b01b96f`, `53611fe` | 04 H-6 |
| `MorningBriefing` skill | `skills/productivity/briefing.py` | KILL-candidate (duplicate of scheduler briefing) | `0bf87fd`; PRD-001 Story A | 04, 06 H-6 |
| In-play rules in `prompts.yaml` | `prompts.yaml:36-38` | REDESIGN (move to `rules.yaml`, deterministic) | | 04 §3 |
| Grading / EV / sizing | — | REDESIGN (new build; Req §6) | PRD-001 score; Manifest Sentinel | 04 H-2 |
| Priority setups (5/9 EMA, VWAP cont., Bouncy Ball, Big Dog) | — | REDESIGN (new build; needs intraday source) | Req §6 | 04 H-1 |
| `daily_in_play` writer | — | KEEP-CONCEPT / BUILD | schema `cc14caa`; PRD-001 Story A | 04 H-8, 02 §4 |
| `tests/test_strategies.py` | | REDESIGN | | 04 §8 |

### 2.5 LLM routing / Cortex / prompts (Pass 5)
| Component | Where | Tier | Original intent | Evidence |
|---|---|---|---|---|
| `LLM` routing class | `llm.py` | KEEP-AS-IS (+ retries/timeouts/fallback/reasoning_effort/usage capture) | hybrid routing `91edb24`, `eef5bdf`, `4f44d94`; Req §10 | 05 H-1/H-4/H-6 |
| `config.yaml models/active_profile/network` | | KEEP-AS-IS (validate; drop Ion nodes) | switchboard `4f44d94` | 05, 07 |
| `Cortex` classification + departments | `brain/cortex.py` | KEEP-CONCEPT / REBUILD (deterministic triage restored; T=0; intercept persisted) | intent routing `eef5bdf`, triage `87e16c7` | 05 H-3 |
| `OrchestratorEngine` | `core/orchestrator.py` | KEEP-CONCEPT / REBUILD (reachable; prompt to config) | split-brain `8c6c5d8` | 05 §2 |
| `BaseDepartment` + Engineering/Ops | `brain/base.py`, `engineering.py`, `ops.py` | KEEP-CONCEPT / REBUILD (one loop, one grammar, prompts from YAML, ToolManager once) | Unified ReAct `05b0617` | 05 H-8 |
| `PromptEngine` | `prompt.py` | KEEP-CONCEPT / REBUILD (tool listing, dedupe directives, prompts to YAML) | memory protocol | 05 H-5 |
| `Persona` class (`get_system_prompt`, `create_override`) | `persona.py` | KILL-candidate (config stays) | persona injection `eef5bdf` | 05 |
| `prompts.yaml` | | KEEP-AS-IS (remove dead sections or wire them) | "centralized prompts"; `.clinerules` | 05 H-5 |
| `UniversalExtractor` LLM call | `extractor.py:182` | REDESIGN (route) | watcher | 05 H-2 |
| Out-of-band embedding calls | `postgres.py` | REDESIGN (route) | | 05 H-2 |
| `dev_utils/test_routing.py` | | KEEP-AS-IS (manual) | switchboard test | 05 |
| `dev_utils/check_gemini_models.py` | | KILL-candidate (not Python) | | 00 F-8 |
| `tests/test_llm.py` | | REDESIGN (fixture) | | 05 H-7 |

### 2.6 Scribe / vault / scheduler (Pass 6)
| Component | Where | Tier | Original intent | Evidence |
|---|---|---|---|---|
| `Scribe` | `skills/productivity/scribe.py` | KEEP-CONCEPT / REBUILD (Req §5 says so) | Manifest Scribe; task 34 journaling | 06 H-4 |
| Filesystem tools + jail | `tools/filesystem.py` | KEEP-AS-IS (jail fixed `7700336`; card must show path; gate reads? — policy) | `87e16c7`, `770c43b` | 06 H-1 |
| `SystemConfig.obsidian_vault_path` resolution | `config.py:62-71` | KEEP-CONCEPT / REBUILD (one resolver; YAML key honoured) | Pydantic settings `61f300d` | 06 H-2/H-3 |
| `CobaltScheduler` | `services/scheduler.py` | KEEP-CONCEPT / REBUILD (tz, config-driven jobs, scanners, cadences, HITL-consistent writes) | briefing `0bf87fd`; Req §5 | 06 H-5/H-7 |
| Scheduler briefing (Gemini + googleSearch) | `scheduler.py:54-110` | KEEP-CONCEPT / REBUILD (keep as *the* briefing; provider-agnostic grounding) | Req §5 premarket agent | 06 H-6, 05 |
| `DeepResearch` | `skills/research/deep_dive.py` | KEEP-AS-IS (minor) | Req §8 precursor | 06 |
| `Cortex._run_ops` keyword routing | `cortex.py:216-251` | REDESIGN | Ops dept | 06 |
| dev_utils vault seeders (`update_board`, `create_prd`, `create_missing_tasks`, `generate_constitution`) | | KILL-candidate (content preserved as intent history) | kanban/PRD/constitution generation | 06 §8 |
| `0 - Inbox` literal policy | many | REDESIGN (INFRA-2 folder policy in config) | Scribe "STRICT RULE" | 06 §1 |
| `tests/test_scribe.py`, `test_scheduler.py` | | REDESIGN (write test wrong by design; one live-side-effect test) | | 06 H-8 |

### 2.7 Config / VaultManager / ops (Pass 7)
| Component | Where | Tier | Original intent | Evidence |
|---|---|---|---|---|
| `CobaltSettings` + YAML loader | `config.py` | KEEP-AS-IS core / REBUILD edges (populate_by_name, capture `cortex_routing`/`scanners`, no silent default, validate registries, `.env.example`) | `0b880fb`, `61f300d`, `5715465`, `cc14caa` | 07 H-1/H-2 |
| `keys:` alias→env-name block | `config.yaml:30-35` | REDESIGN (direct vault naming) | `5becd1e` | 07 H-2, 05 §3 |
| `VaultManager` | `security/vault.py` | KEEP-CONCEPT / REBUILD (atomic write, backup, rotation, path validation, docstring) | `5becd1e`; Security Architecture §3 | 07 H-3 |
| `dev_utils/manage_vault.py` | | KEEP-CONCEPT / REBUILD (getpass key, no console print, rekey command) | INFRA-0 policy | 07 H-3 |
| `cobalt.sh` | | REDESIGN (launchd-supervised; thin wrapper) | INFRA-0.5 | 07 H-4 |
| `ops/*.plist`, `start_mainframe.sh` | | KEEP-CONCEPT / REBUILD (KeepAlive, ordering, 27B per INFRA-3) | INFRA-0.5/INFRA-3 | 07 H-4, 00 F-5 |
| `docker-compose.yml` | | KEEP-CONCEPT / REBUILD (profiles, pins, 127.0.0.1, DB split or documented coupling) | `8c5c0c1`, `8acfe9a` | 07 H-6, 01 H-1 |
| Logging setup | `main.py:62-82` + defaults | REDESIGN (single policy, redaction, no DEBUG dumps) | Req §11#11 | 07 H-5, 03 H-6 |
| `get_current_node_role`, `parse_json_credentials`, `VaultConfig.enabled`, `SystemConfig.version`, `LLMConfig` defaults, Ion `network.nodes` | `config.py`, `config.yaml` | KILL-candidate | Ion-era / unused | 07 H-2 |
| `tests/test_vault.py` | | KEEP-AS-IS | | 07 H-7 |

### 2.8 Repo-level (Pass 0)
| Item | Tier | Evidence |
|---|---|---|
| `dev_utils/generate_context.py` | KEEP-CONCEPT / REBUILD (exclude ignored dirs; include `.sh/.plist/.json`) | 00 F-2 |
| `src/cobalt_agent.egg-info/` | already untracked by Dejan (`99bdf8c`) | 00 F-7 |
| `README.md`, `.env.example` (empty), `orchestration_plan.json` | REBUILD / KILL-candidate | 00 F-12 |
| `tests/test_vision.py` (no tests), `cli.py` CLI path (unreachable; calls non-existent `LLM.think`) | KILL-candidate | 00, 05 H-2 |
| CLAUDE.md corrections still pending | `wipe_memory.py`/`reset_memory_table.py` do not exist; 122B model note | 00 F-4/F-5 |

---

## 3. Cross-cutting findings (by requirement)
| Requirement (§) | Status | Evidence |
|---|---|---|
| §3 no platform integration / no execution | Met (only `lightspeed_formatter.py` touches a platform export format, read-only) | 00 §3.3 |
| §4 tools fetch, agents reason; deterministic math | Partly: collector is deterministic; in-play rules and briefing logic are in prompts; grading absent | 04 |
| §4 anti-rigidity / config-driven | Not met: 3 ACTION grammars, hardcoded prompts, `class_map`, literals in 8+ places, dropped config keys | 05, 04, 06, 07 |
| §4 LiteLLM hot-swappable | Mostly met; 2 out-of-band call sites + provider-locked grounding | 05 H-2 |
| §4/§10 local-first | Partly: 5/6 roles local; embeddings + briefing + vault chunks go to cloud; no reasoning_effort/fallback | 01 H-7, 05 H-4 |
| §9 vault-as-map, index.md | Not started | 06 |
| §11#1 tokenized HITL | Id-based chat approval without identity binding; card content-free | 03 |
| §11#3 Pydantic everywhere | Memory/scanner rows untyped; strategies validated-but-unused | 02 H-8, 04 |
| §11#6 tests/ADR/PDD/DevDocs | Tests partly broken; ADRs in vault (not read); no DevDocs per `.py` in repo | all |
| §11#11 logging w/ rotation | Agent yes; dev tools no; secret dumps at DEBUG | 07 H-5 |
| §11#16 prod never broken / dev separation | No `cobalt_dev`, tests touch prod vault/DB, `.env` shared with Mattermost | 01 H-1, 01 H-8 |
| INFRA-0 | PAT in remote URL; DEBUG secret dumps; key printed by `manage_vault.py`; key in process env | 00 F-3, 03 H-6, 07 H-3 |
| INFRA-1 | Use `COBALT_POSTGRES__DB`, not `POSTGRES_DB`; decide `hitl_proposals` DDL first | 01 §7 |
| INFRA-2 | Inventory delivered (06 §1); one resolver; `populate_by_name` | 06 |
| INFRA-3 | `start_mainframe.sh` still 122B / 32k ctx | 00 F-5, 07 |
| §8 research engine | Finviz export already yields float/short-float/earnings-date/news fields; `news_events` tables exist with no writers; no EDGAR/FMP code | 02 H-8, 01 §1 |

## 4. Things to correct in CLAUDE.md (facts found wrong)
`dev_utils/wipe_memory.py` / `reset_memory_table.py` do not exist; `docs/Cobalt/` → `docs/` (already fixed); LaunchAgents names (fixed); local model is still the 122B MoE until INFRA-3; "5-pillar schema with memory_logs…" — `memory_logs/graph_*/browser_fast_path/hitl_proposals` come from runtime DDL, the 5-Pillar file is `schema.sql` (13 tables); cosine floor 0.3 is only in `search()`.

## 5. Unverified items carried forward (consolidated)
Vault contents/secret names; `.env` values (only `OBSIDIAN_VAULT_PATH` resolution observed); real Obsidian vault location; ADR-014 and any vault ADRs; whether `uv run` forwards SIGTERM; LM Studio think-tag behaviour; Gemini `googleSearch` via LiteLLM; whether browser structured actions were ever executed in prod; Finviz token validity; `com.cobalt.mainframe` exit 2 cause; whether dev-tool DEBUG dumps were ever persisted.

## 6. Pass documents
`00-inventory.md` · `01-memory.md` · `02-browser.md` · `03-mattermost-hitl.md` · `04-trading-logic.md` · `05-llm-routing.md` · `06-scribe-vault-scheduler.md` · `07-config-vault-ops.md` — each with file:line evidence, tests run, hardcoded-value tables, ORIGINAL INTENT columns, and UNVERIFIED lists.
