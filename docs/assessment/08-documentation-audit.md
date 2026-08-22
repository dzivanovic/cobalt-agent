# Cobalt Assessment — Pass 8: Documentation audit

Date: 2026-08-22 · Baseline: `3a659de` (main) · Assessor: Claude Fable 5 · Mode: read-only; no documentation modified. Gitignored doc trees under `docs/` were read for this pass (project/system docs only); personal/journal content (`Daily_Log_*`, `AutoNote_*`) was listed by name and **not read**; one `Morning_Briefing_*` was sampled only to characterise the artifact type.

Code is law: verdicts judge the document against the code as established in passes 00–07 (cross-referenced rather than re-verified). Verdicts: **CURRENT** · **STALE** (cites the contradiction) · **ORPHANED** (describes deleted/never-existing components) · **ASPIRATIONAL** (design never implemented; marked *wanted* per `COBALT-REQUIREMENTS.md` or *out of scope*). Many artifacts are mixed; the dominant verdict is given with the qualifier.

---

## 0. Headline findings

| # | Finding |
|---|---|
| **H-1** | **The entire design/documentation corpus lives only in the gitignored vault folder** (`docs/0 - Projects/Cobalt/…`): 16 ADRs, 14 PRDs, 6 sprint notes, Backlog, Infrastructure, a prior Architecture Assessment, Master_Taxonomy, Story-001, 47 task notes, a Bases board, and 60 DevDocs — **none version-controlled**, no `.obsidian/` marker under `docs/` (whether this tree is Obsidian-Synced elsewhere is UNVERIFIED). Version-controlled documentation is: `CLAUDE.md`, `COBALT-REQUIREMENTS.md`, `.clinerules`, an empty `README.md`, an empty `.env.example`, `docs/assessment/*`, module docstrings, and the constitution/PRD/task text embedded in `dev_utils/generate_constitution.py`, `create_prd.py`, `create_missing_tasks.py`. |
| **H-2** | **Two divergent ADR series exist.** The vault's ADR-001..003 (Hybrid Compute / Cobalt-Ion Protocol / Python-First) differ in number and content from the ADR-001..003 embedded in `generate_constitution.py` (Cobalt-Ion Protocol / Hybrid AI Compute / Python-First). Cross-references are wrong in several places: ADR-011 and ADR-012 cite "Split-Brain (ADR-007)" (ADR-007 is the HITL engine); `Backlog.md` calls the Vector Librarian "ADR-009" (it is ADR-011); PRD-010 links "PRD-013/PRD-011" to ADR files; `Split_Brain_Summary.md` itself notes a PRD-007 misreference. The constitution's outputs (`System Manifest.md`, `Security Architecture.md`, `00 Cobalt Master Plan.md`, `Roadmap.md`) are **absent** from the vault tree — their text exists only in code. |
| **H-3** | **Generated-doc artefacts and fabricated detail.** `PRD-001` and `PRD-012` contain raw LLM tool-call residue (`<task_progress>…</write_to_file>`). ADR-014 (17 KB) presents `VRAMManager`, `SequentialToolExecutor`, `LocalMoEProvider` classes and an `llm:/lm_studio:` config block "in `src/cobalt_agent/llm.py`/`orchestrator.py`" — **none exist** (Pass 5). ADR-004 describes AES-256-GCM + OS X Keychain + SQLite + TTL + audit — the code is Fernet (AES-128-CBC) on a file with the key in env (Pass 7 H-3). DevDocs `scheduler.md` documents a `SchedulerService` with `add_cron_job/add_interval_job`, vault backups and log cleanup — the code is `CobaltScheduler` with one hardcoded job (Pass 6 H-5). `tactical.md` shows an "example output" of a successful strategy scan that cannot occur (Pass 4 H-3). |
| **H-4** | **Sprint notes and "✅ Implemented" PRDs record acceptance claims the code does not support**: `Sprint_Hardening_Tech_Debt.md` — "routing keywords moved to rules.yaml… all 16 cortex tests passing… filesystem path traversal protection verified… 56/56 tests" (keywords are silently dropped, Pass 4 H-4; `test_cortex` has 16 fixture errors, Pass 3; the jail was non-functional until `7700336`, Pass 6 H-1); `Sprint_Agentic_Browser.md` — "Zero-Trust enforcement blocks 100% of unwhitelisted URLs", "Fast Path reduces latency >90%" (Pass 2 H-5/H-6); PRD-009 — "fast-path routing works without LLM call ✅", "high-risk intercept triggers HITL ✅" (neither fires in prod, Pass 5 H-3); PRD-011 — "Master key never persisted to disk ✅" (`~/.cobalt_key`), "Browser navigation: no HITL" (browser is in `DANGEROUS_TOOLS`). |
| **H-5** | **DevDocs coverage is nominally ~100% by module name but substantively stale.** 60 docs; 23 created 2026-02-23 and never updated; only `postgres.md` (2026-04-08), `semantic_tagger.md`/`live_run_*.md` (2026-04-07) post-date the last big refactor (`cc14caa`). 4 are **orphans** for scripts that do not exist (`brain_scan.md`, `test_script.md`, `wipe_memory.md`, `reset_memory_table.md` — the source of CLAUDE.md's wipe/reset mention, Pass 0 F-4). A symbol cross-check (documented `` `name(` `` vs `def` in the matching `.py`) flags 13 docs documenting functions that don't exist (e.g. `browser.md` → `inject_credentials/validate_url/compute_task_hash`; `playbook.md` → `hydrate_strategies/analyze`; `config.md`/`vault.md`/`main.md` → `load_config`; `cortex.md` → `_run_engineering`; `mattermost.md` → `handle_approval_response` on the interface; `tool_manager.md` → `run`). Only 34/60 have frontmatter; all say `status: Active`. No doc exists for `tests/`, `cobalt.sh`, plists, compose, or the assessment itself (this tree). |
| **H-6** | **Requirements §11#6 artefacts**: ADRs exist (drifted); **PDDs per module/feature do not exist** (the PRDs are product/feature requirements, three of them empty stubs); DevDocs per `.py` exist but are not regenerated at sprint close and were never verified; no DevDocs generator script exists in the repo (the sprint notes say docs were "updated", i.e. LLM-written by hand). |
| **H-7** | **What is genuinely current**: `COBALT-REQUIREMENTS.md` (authority), `CLAUDE.md` (two known corrections pending), `docs/assessment/*`, `Master_Taxonomy.md` (matches the `themes` table), `Cobalt Project Board.base`, ADR-006/007/011/012/015/016 (concept-current with noted drift), `Infrastructure.md` (plists match `ops/`; container/Docker-Desktop/122B details drifted), PRD-000's principles (not its topology), and the 100 `Morning_Briefing_*` outputs — which are the only documentary proof that a scheduled job runs in production every trading day (2026-02-26 → 2026-08-21). |

---

## 1. Inventory and version-control status

| Location | Artifacts | VC? | Notes |
|---|---|---|---|
| repo root | `CLAUDE.md` (7.1 KB), `COBALT-REQUIREMENTS.md` (21.4 KB), `.clinerules` (2.4 KB), `README.md` (0 B), `.env.example` (0 B), `orchestration_plan.json` (51 B) | yes | `cobalt_master_context.txt` referenced by CLAUDE.md/requirements is **absent**. |
| `dev_utils/` embedded docs | `generate_constitution.py` (Master Plan dashboard, System Manifest, Security Architecture, ADR-001..003, Roadmap, Backlog), `create_prd.py` (PRD-001 v1), `create_missing_tasks.py` (tasks 30–34) | yes (as code) | Their *outputs* are partly absent from the vault; content diverges from vault versions (H-2). |
| `docs/assessment/` | 00–07 + ASSESSMENT.md + this file | yes (gitignore exception) | — |
| `docs/0 - Projects/Cobalt/00 - Master Plan/ADR/` | 16 ADRs (2026-02-23 → 2026-04-07) | **no** | 2 self-marked OBSOLETE (001, 010). |
| `…/00 - Master Plan/` | `ARCHITECTURE_ASSESSMENT.md` (Feb 2026), `Master_Taxonomy.md`, `Developer Docs/` (60) | **no** | |
| `…/90 - Project Management/Requirements/` | PRD-000…PRD-013 (14; 002/003/004 are frontmatter-only) | **no** | |
| `…/90 - Project Management/Sprints/` | 6 sprint notes | **no** | |
| `…/90 - Project Management/` | `Backlog.md`, `Infrastructure.md`, `User Stories/Story-001_Initial_Brainstorm.md` | **no** | |
| `…/Cobalt/Tasks/` + `Cobalt Project Board.base` | 47 task notes (01–29, 31–48; 14 are frontmatter-only stubs) + Bases view | **no** | |
| `docs/0 - Inbox/` | 100 `Morning_Briefing_*` (scheduler output), 2 `Briefing_*` (skill output, Feb 24–25), `Split_Brain_Summary.md`, 2 `AutoNote_*`, 1 `Daily_Log_*` (not read) | **no** | System outputs / personal. |

---

## 2. Artifact-by-artifact verdicts

### 2.1 Repo-level
| Artifact | Claims | Code says | Verdict |
|---|---|---|---|
| `COBALT-REQUIREMENTS.md` | target state + non-negotiables | by definition the target; §13 says context snapshot is stale (it is absent) | **CURRENT (authority)** |
| `CLAUDE.md` | env facts, assessment rules | two stale lines remain: `wipe_memory.py`/`reset_memory_table.py` exist (they don't; only their DevDocs do); local model = 27B (ops still loads 122B) — Pass 0 F-4/F-5 | **CURRENT with 2 STALE facts** |
| `.clinerules` | "Senior SRE persona… no magic strings, prompts as config, DRY config, no bare exceptions" | violated broadly (Pass 5 H-5, Pass 4, Pass 7); written for Cline/local-LLM sessions | **ASPIRATIONAL (process rules); keep if still the coding policy** |
| `README.md` | — | empty | **ORPHANED (missing)** |
| `.env.example` | — | empty; the env contract (≈12 variables across passes) is undocumented | **ORPHANED (missing)** |
| `orchestration_plan.json` | `{"task":"default_task","status":"pending"}` | no reader | **ORPHANED** |
| `dev_utils/generate_constitution.py` texts (System Manifest, Security Architecture, ADR-001..003, Roadmap, Backlog) | 5-department org, Ion/Sentinel/Scout hardware stack, OTET token flow, DeepSeek/o3-mini/Gemini-1.5 models | Ion/Sentinel/OTET never built and now out of scope (§3); model list superseded; Scout/Scribe/Strategos names survive as department labels | **ASPIRATIONAL/historical — intent record; out of scope as design** |
| `dev_utils/create_prd.py` (PRD-001 v1), `create_missing_tasks.py` (tasks 30–34) | Ion HUD, ZMQ bridge, Mattermost C2 buttons/kill-switch, trade journaling | see PRD-001 / tasks below | **ASPIRATIONAL (out of scope except journaling/C2 approval UX, which are wanted §5/§11)** |

### 2.2 ADRs (vault)
| ADR | Claims | Code says | Verdict |
|---|---|---|---|
| 001 Hybrid Compute (OBSOLETE) | deprecated 03-07 in favour of 122B MoE | correctly marked; 122B itself now superseded by INFRA-3 | **CURRENT as historical record** |
| 002 Cobalt-Ion Distributed Protocol ("Active") | Redis/ZeroMQ, Rust Ion on Windows, channels | no redis/zmq/Rust code; `redis` dep unused; requirements keep the trading PC clean | **ASPIRATIONAL → out of scope; status field STALE** |
| 003 Python-First ("Active") | Python FastAPI + LangChain; Rust Ion | Python yes; no FastAPI/LangChain/Rust; `fastapi/uvicorn` declared unused | **STALE; Python-first still wanted (§11#2), rest out** |
| 004 Zero Trust Security | HITL w/ timeout+auto-reject+approver identity; Docker seccomp sandbox; VaultManager AES-256-GCM + Keychain + SQLite + TTL + audit; `vault:` config keys | HITL exists without timeout/identity (Pass 3 H-1); sandbox never built (task 37 To Do); vault is Fernet/file/env (Pass 7 H-3); config keys don't exist | **STALE + ASPIRATIONAL; HITL hardening & vault rotation wanted (INFRA-0, §11#1); sandbox not in requirements (Dejan)** |
| 005 Agentic RAG | 768-dim, `message/data` columns, ivfflat index, 24 h filter, memory-as-tool | 1536-dim `content/metadata`, no index, no temporal filter; `search_knowledge` exists | **STALE; concept wanted (§7)** |
| 006 Prime Directive & HITL via `persona.directives` | config-driven directive injection | true (`PromptEngine`), "cryptographic authorization" is not real | **CURRENT (minor)** |
| 007 HITL Proposal Engine | `Proposal` model; "Approve [task_id]" via Mattermost; risk-level middleware in cortex | matches, except the keyword middleware never fires (Pass 4 H-4) | **CURRENT with drift** |
| 008 JIT Secrets Vault | independent Vault daemon + socket API; `config.py` requests keys via API; scrub on serialization | in-process `VaultManager`, env master key, no daemon; scrubbing exists in memory writes | **ASPIRATIONAL (daemon) / CURRENT (vault concept)** |
| 009 Agentic Browser Loop & Zero Trust | AOM IDs stable; Fast Path; whitelist on navigation; HITL for mutations; "Files Changed: complete rewrite" | DSL unreachable (Pass 2 H-4), Fast Path dead (H-6), whitelist not on navigation (H-5); `sqlalchemy` dep unused | **STALE (claims implemented); partial concept wanted (§5 Playwright where no API) — Dejan** |
| 010 Split-Brain (OBSOLETE) | deprecated 03-07 | correctly marked | **CURRENT as historical record** |
| 011 Vector Librarian | `ingest_knowledge.py`, `search_knowledge`, `text-embedding-3-small` | exists; data stale; "automated background syncs" never built | **CURRENT (implementation) / misreference to ADR-007** |
| 012 Drone Polymorphism | `BaseDepartment` single ReAct loop; <20-line departments | true; but Mattermost duplicates the loop (Pass 5 H-8) | **CURRENT with drift** |
| 013 GraphRAG & Watcher | `nodes/edges` with `source_url/weight`; `extraction_history`; APScheduler; event bus | actual `graph_nodes/graph_edges(entity_type,name,properties)`; no history/jobs tables; daemon scheduler never started (Pass 2 H-7) | **STALE + ASPIRATIONAL; monitoring concept wanted (§5 news agents) but redesigned** |
| 014 Unified MoE (122B) | `VRAMManager`/`SequentialToolExecutor`/`LocalMoEProvider` code; `llm:`/`lm_studio:` config; 256K ctx; VRAM kernel override | none of the classes/config exist; registry is `models/active_profile`; INFRA-3 replaces the model | **STALE (fabricated implementation) → historical** |
| 015 5-Pillar Schema | 12 tables; Finviz Quote API candles on demand; `instrument_themes` | 13 tables in `schema.sql`; candle fetch not built; themes via `active_themes` JSONB | **CURRENT (schema) with drift** |
| 016 Semantic Taxonomy | Markdown taxonomy → Postgres; 20-batch; 4 fields; 5-min cron | matches code; no cron exists; `instrument_themes` absent | **CURRENT with drift** |
| `ARCHITECTURE_ASSESSMENT.md` (Feb 2026) | "secrets mgmt missing", "proposal engine missing", 122B target | both exist now; superseded by this assessment | **STALE → historical** |
| `Master_Taxonomy.md` | 11 theme rows | `themes` table populated from it (Pass 4) | **CURRENT** |

### 2.3 PRDs (vault)
| PRD | Claims | Code says | Verdict |
|---|---|---|---|
| 000 Ironman Directive | cluster with X1 Carbon worker node + Tailscale IPs; vault folder structure; Spotter/Sniper; prompts as config; OS-agnostic paths via `.env` | no worker-node code; laptop not a node (§12); principles match; prompts partly in code | **STALE topology / CURRENT principles** |
| 001 Tactical HUD (rewritten 03-17) | PyQt6 HUD, TradeStation data, JIT-token autonomous execution (Story D), AOM "Fast Path router" | no HUD; §3 forbids execution/platform touch; tool-call residue in file | **ASPIRATIONAL → out of scope (EV/grading concept survives as §6 ASET); file corrupted** |
| 002 / 003 / 004 | frontmatter only | — | **ORPHANED (empty)** |
| 005 Voice | STT/TTS/intent, Mattermost & browser by voice | none built; §9 specifies a different 3-tier stack | **ASPIRATIONAL — wanted (§9), needs rewrite** |
| 006 Agentic Browser & Fast Path ("Approved") | Pydantic actions, Maps, vault injection, Fast Path <50 ms, `AUTO_APPROVED_DOMAINS` | Pass 2; config keys don't exist | **STALE; partially wanted (Dejan)** |
| 007 Split-Brain ("Approved") | Architect plan → Worker; feedback loop on error; dynamic personas | orchestrator exists but unreachable; no feedback loop; `create_override` unused | **STALE/ASPIRATIONAL** |
| 008 Watcher & GraphRAG ("Approved") | `extraction_history`, `watcher_jobs`, whitelist, cooldown | not built | **ASPIRATIONAL; redesign if wanted (§5)** |
| 009 Local First ("✅ Implemented") | `rules: cortex_routing` in config.yaml; fast-path without LLM ✅; intercept ✅ | keywords live in `rules.yaml` and are dropped; neither fires | **STALE** |
| 010 Continuous Memory ("✅") | tables/API incl. `store_hilt_proposal`; latencies; `cobalt_memory` env | structure matches; `_hilt_` dead; DB is `cobalt_brain` | **CURRENT with drift** |
| 011 Zero Trust ("✅") | AES-256; `VAULT_MASTER_KEY`, `MATTERMOST_URL/TOKEN`; key never on disk; browser nav no HITL | Fernet; `COBALT_MASTER_KEY` + vault `MATTERMOST_CREDS`; `~/.cobalt_key`; browser gated | **STALE** |
| 012 Recon Scout (Draft) | SMB game-plan, Finviz charts, FinancialJuice extractors via AOM; tool-call residue | only Finviz scraper (superseded by API); tasks 46–48 To Do | **ASPIRATIONAL — FinancialJuice/SMB still wanted (§5/§7) but not via AOM; file corrupted** |
| 013 Market Data Engine ("Approved") | 5-Pillar; news dedup; MFE/MAE; trades/accounts; Obsidian playbook generation; 768-dim | schema only; no news/MFE/playbook code; 1536-dim | **CURRENT (schema) / ASPIRATIONAL (analytics) — journaling of manual trades wanted (§1/§5), execution-side tables out** |

### 2.4 Sprints, backlog, infrastructure, story, tasks, board
| Artifact | Verdict | Contradictions |
|---|---|---|
| `Sprint_05_The_Ion_Bridge.md` (To Do) | **ORPHANED/out of scope** | Ion; references absent `Developer Docs/ion_bridge.md`, `services/ion_bridge.py` |
| `Sprint_06_Data_Engine.md` (Planned) | **partly CURRENT** (schema + ingestion done) / **ASPIRATIONAL** (news extractor, dedup, `Playbook/Daily/` sync) | "12 tables", 768-dim |
| `Sprint_Agentic_Browser.md` (Done ✅) | **STALE** | H-4 |
| `Sprint_Hardening_Tech_Debt.md` (Complete) | **STALE** | H-4; "56/56 tests" vs today's failures; "prompts extracted" (4 YAML sections dead, Pass 5 H-5) |
| `Sprint_Watcher_Daemon.md` (Done) | **STALE** | planned files (`migrations/003_graph_schema.sql`, `models/graph.py`, `extractor/universal.py`, `services/watcher.py`, `tools/watcher.py`, `interrupts/delta.py`) don't exist under those names; built differently and partially |
| `Sprint-2026-02-25 Zero Trust HITL Engine.md` (Complete) | **historical/STALE** | memory-locked callbacks superseded by `HITLProposalStore`; `ast.literal_eval` later removed |
| `Backlog.md` | **STALE** | "Phase 7: automated vault management with AES-256 encryption" never existed; ADR-009 mislabel; "Execution Broker API" out of scope; no entries for anything in §5–§8 |
| `Infrastructure.md` | **CURRENT (plists) / STALE (details)** | Docker Desktop (it's OrbStack); container `postgres` (it's `cobalt_memory`); 122B/88 GB; no KeepAlive/dual-start facts (Pass 7 H-4) |
| `Story-001_Initial_Brainstorm.md` | **ASPIRATIONAL/historical — keep as intent record** | DeepSeek 70B, Ion, TradeStation; origin of the EV/score/playbook-hierarchy ideas |
| `Tasks/01–14` | **ORPHANED (frontmatter-only stubs)** | |
| `Tasks/15–21` (Done) | **CURRENT-ish** (components exist) | 17 says router "in main.py" (it's `cortex.py`) |
| `Tasks/22` Mac Studio Deployment (To Do, "M3 Ultra") | **STALE** | deployed on M2 Ultra via LaunchAgents |
| `Tasks/23–26` Tactical (Done) | **STALE** | scan is broken (Pass 4 H-3) |
| `Tasks/27` Backtest Engine (To Do) | **ASPIRATIONAL — wanted (§6)** | |
| `Tasks/28–29` Ops Medical / Privacy Guardrails | **ASPIRATIONAL — out of scope** (not in requirements) | |
| `Tasks/31–32` Ion Bridge / HUD | **ORPHANED/out of scope** | |
| `Tasks/33` Mattermost C2 (To Do) | **partly CURRENT** (bot exists) / **ASPIRATIONAL** (webhooks, kill switch, buttons — wanted §9/§11) | |
| `Tasks/34` Trade Journaling (To Do) | **ASPIRATIONAL — wanted (§1)** | |
| `Tasks/35` Tailscale VSCode | ops task, **out of assessment scope** | |
| `Tasks/36` Proposal Engine (Done) | **CURRENT with drift** (no 5-min timeout) | |
| `Tasks/37` Docker Sandbox (To Do) | **ASPIRATIONAL — not in requirements (Dejan)** | |
| `Tasks/38/41/42` Split-Brain (Done) | **STALE** (unreachable/unused) | |
| `Tasks/39/43` Playwright (Done) | **STALE** (DSL unreachable) | |
| `Tasks/40` LastPass (Wont-Do) | **CURRENT (closed)** | |
| `Tasks/44` Serializers (To Do) | **STALE** — `utils/serializers.py` exists | |
| `Tasks/45` LM Studio LaunchAgent (To Do) | **STALE** — `com.cobalt.mainframe.plist` exists | |
| `Tasks/46–48` Recon Scout (To Do) | **ASPIRATIONAL** (see PRD-012) | |
| `Cobalt Project Board.base` | **CURRENT** (Obsidian Bases view over `Tasks/`) | |

### 2.5 DevDocs (60) — class verdict **STALE**, per-file highlights
| File | Verdict | Contradiction |
|---|---|---|
| `scheduler.md` | STALE (fictional API) | `SchedulerService`, `add_cron_job`, vault backup, log cleanup, `scheduler:` config — none exist (`scheduler.py`) |
| `scribe.md` | STALE | `write_note` "returns success message with path" — returns `requires_approval` dict (`scribe.py:104-109`); `_resolve_path(filename) -> Path` signature wrong |
| `tactical.md` | STALE | fabricated successful scan output; FinanceTool "Finviz" sources (it's yfinance) |
| `main.md` | STALE | `LLM_API_KEY`, `python -m cobalt_agent` (no `__main__.py`), "LLM errors retried" |
| `config.md`, `vault.md` | STALE | `load_config` (now `get_config`); AES-256; `cobalt_memory` |
| `memory_core.md` | STALE | JSON memory doc carrying FastPath DDL |
| `browser.md`, `playbook.md`, `cortex.md`, `mattermost.md`, `tool_manager.md`, `extractor.md`, `serializers.md` | STALE | documented symbols absent (H-5 list) |
| `postgres.md` (2026-04-08) | mostly CURRENT | documents `store_hilt_proposal` trio as live (dead) |
| `semantic_tagger.md`, `scanner_orchestrator.md`, `enrich_metadata.md`, `finviz_api.md`, `live_run_*.md` (2026-04-07) | mostly CURRENT | `live_run_orchestrator.md` documents the broken wrapper as working |
| `brain_scan.md`, `test_script.md`, `wipe_memory.md`, `reset_memory_table.md` | ORPHANED | no such files; `wipe_memory.md` documents a script that truncates **every table in the public schema** — i.e. would have wiped Mattermost too (Pass 1 H-1) |
| `check_gemini_models.md`, `brain_base.md`, `memory_base.md`, `aom.md`, `maps.md`, `daemon.md`, `finance.md`, `llm.md`, `persona.md`, `prompt.md`, `proposals.md`, `strategy.md`, `second_day_play.md`, others | CURRENT-ish structure / STALE behaviour | describe intended behaviour (e.g. `daemon.md` scheduler running; `maps.md` stable IDs) contradicted by passes 2/5 |

### 2.6 Inbox system outputs
`Morning_Briefing_YYYY-MM-DD.md` ×100 (2026-02-26 → 2026-08-21, weekdays with gaps): **CURRENT outputs** of the scheduler job — format matches `prompts.yaml scheduler.morning_briefing` (Pass 6 sample). `Briefing_2026-02-24/25.md`: outputs of the duplicate skill path (Pass 6 H-6). `Split_Brain_Summary.md`: LLM-generated summary with a self-noted misreference — **historical**. `AutoNote_*`, `Daily_Log_*`: personal/agent scratch — not assessed.

---

## 3. Pipeline assessment
- **Where docs live**: design + DevDocs only in the gitignored vault (H-1); the two authoritative process docs in git. No backup path for the vault tree is verified; no review/diff history exists for any ADR/PRD.
- **How they were produced**: LLM-written at sprint close (sprint notes list "Documentation Updates ✅"); DevDocs carry `status: Active` regardless; no generator script, no verification against code (the symbol cross-check used here is trivial to automate).
- **Numbering/registry**: no ADR index; two series (code vs vault); misnumbered cross-references (H-2).
- **Requirement mapping**: requirements §11#6 asks for ADR-per-decision (partially met, drifted), PDD-per-module/feature (**none**), DevDocs-per-`.py` generated at sprint close (exist but stale, unverified), backlog/kanban always current (#7 — `Backlog.md`/Tasks are months stale and pre-date the requirements doc).
- **Coverage gaps**: no docs for `tests/`, `cobalt.sh`, plists (beyond `Infrastructure.md`), compose, logging policy, env contract (`.env.example` empty), runbooks (start/stop/rollback per §16), the data model as-built (runtime DDL vs `schema.sql`), or the assessment series itself.

## 4. Trustworthy documentation baseline before sprint one (proposal)
**Regenerate (from code, verified)**: DevDocs for every current `.py` (script-generated, with a symbol cross-check gate; label as *as-built*, not aspirational); `README.md` (what/how to run, links to requirements, CLAUDE.md, assessment); `.env.example` (full env contract: `COBALT_*`, `POSTGRES_*`, `OBSIDIAN_VAULT_PATH`, `COBALT_MASTER_KEY`, `LOGURU_LEVEL`); `Infrastructure.md` → an ops runbook (LaunchAgents, `cobalt.sh`, compose profiles, rollback, INFRA-3 model); an as-built data-model doc (runtime DDL + `schema.sql` + the two `hitl_proposals` shapes); an ADR index with one numbering series.
**Write new (decisions already taken in `COBALT-REQUIREMENTS.md`)**: ADRs for INFRA-3 (27B + MTP), embedder choice (Pass 1 H-7), HITL token design (Pass 3), vault redesign/folder policy (INFRA-2), config precedence fix (Pass 7), scheduler-as-job-host; PDD template + first PDDs for the sprint-one modules (scanner pipeline, `daily_in_play` writer).
**Refresh and keep as CURRENT**: `CLAUDE.md` (apply F-4/F-5 corrections), ADR-006/007/011/012/015/016 (add drift notes), PRD-000 (drop worker-node topology), PRD-005 (rewrite to §9), `Master_Taxonomy.md`, `Cobalt Project Board.base`; rebuild `Backlog.md` and the `Tasks/` set from `ASSESSMENT.md` §2 (close/relabel 01–14 stubs, Ion tasks, 44/45 as Done).
**Archive as historical record** (mark `status: Historical`, move under an `Archive/` folder, never delete — they are the intent trail used in passes 1–7): ADR-001/002/003/004/005/008/009/010/013/014, `ARCHITECTURE_ASSESSMENT.md`, PRD-001/006/007/008/009/011/012/013, all six sprint notes, `Story-001`, `Split_Brain_Summary.md`, old `Backlog.md`, the constitution texts from `generate_constitution.py` (export once, then retire the script).
**Delete** (or fold into the archive note): PRD-002/003/004 stubs; orphan DevDocs `brain_scan.md`, `test_script.md`, `wipe_memory.md`, `reset_memory_table.md`; the tool-call residue inside PRD-001/012; `orchestration_plan.json`.
**Process**: bring `docs/0 - Projects/Cobalt/` (system docs, not the personal Inbox/Daily logs) under version control — either un-ignore that subtree or a dedicated docs repo/submodule — so ADR/PRD/DevDocs diffs are reviewable and backed up (INFRA-0.5); define `status` semantics (Proposed / Accepted / Implemented-as-built / Superseded / Historical) and require a `verified_against` commit hash on Implemented docs; add the DevDocs symbol cross-check to the sprint-close checklist (or CI).

## 5. UNVERIFIED
- Whether the `docs/` tree is included in Obsidian Sync or any backup (no `.obsidian/`; Sync config lives outside the repo).
- Whether additional Cobalt documentation exists in the live (Synced) vault that is not mirrored in this playground tree (the constitution outputs may be there).
- Authorship/tooling of the ADR/PRD texts (LLM-generated per residue; which model/session is not recorded).
- Whether `Daily_Log_2026-03-01.md` / `AutoNote_*` contain anything other than Cobalt test writes (not read by design).
