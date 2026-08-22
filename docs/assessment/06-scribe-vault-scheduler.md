# Cobalt Assessment — Pass 6: Scribe, vault integration, and scheduler

Date: 2026-08-22 · Baseline: `32c5dbd` (main) · Assessor: Claude Fable 5 · Mode: read-only (code read; mocked tests run with the one Mattermost-posting test **deselected**; two local pure-Python probes that only compute paths — **no vault writes, no scheduled jobs run, no DB writes, no messages sent**; vault contents not read — only top-level names)

Scope: `skills/productivity/scribe.py` (202), `tools/filesystem.py` (365), `services/scheduler.py` (231), `skills/productivity/briefing.py` (115), `skills/research/deep_dive.py` (109), `skills/research/sync_taxonomy.py` (vault reader), `brain/cortex.py:216-251` (`_run_ops`), `brain/ops.py`, `config.py:62-72` (`SystemConfig`), the dev_utils vault writers (`update_board.py`, `create_prd.py`, `create_missing_tasks.py`, `generate_constitution.py`, `ingest_knowledge.py`), `configs/config.yaml:3-6`, `configs/prompts.yaml` (ops/engineering examples), and `tests/test_scribe.py`, `test_scheduler.py`.

Verdict legend: **RETAIN** · **BROKEN-FRICTION** · **KILL-candidate** (proposal — Dejan decides). **UNVERIFIED** = inferred, not read/run. ORIGINAL INTENT (§8) from tracked sources only; vault ADRs not read; `cobalt_master_context.txt` absent.

---

## 0. Headline findings

| # | Finding | Evidence |
|---|---|---|
| **H-1** | **The vault path jail is non-functional — every filesystem tool can read/list/write anywhere the process can.** `BaseFileTool._validate_path` calls `resolved_target.is_relative_to(self.base_path)` inside a `try` and **discards the boolean** (`filesystem.py:119-127`; `is_relative_to` never raises, so the `except ValueError` fallback that would actually enforce the jail is dead). **Reproduced locally (no writes):** `'../../etc/hosts'` → accepted (`/Users/cobalt/etc/hosts`), `'/etc/hosts'` → accepted, `'/tmp/outside_vault.md'` → accepted. Consequences: `read_file` and `list_directory` are *safe* tools that execute **without HITL** (`tool_manager.py:32-40`), so an LLM `ACTION: read_file {"filepath": "/Users/cobalt/cobalt/.env"}` returns the secrets file into the conversation/Mattermost; `write_file`/`append_to_file` outside the vault are gated only by an approval card that **does not show the path** (Pass 3 H-2). The system prompts advertise `data/`, `src/`, `configs/` as the "system map" (`prompt.py:78-83`, `orchestrator.py:110-115`), inviting exactly such paths. | `filesystem.py:91-129`; probe |
| **H-2** | **Vault-root discrepancy resolved: `config.yaml` is silently ignored; `.env OBSIDIAN_VAULT_PATH` wins; both point at `docs/` today.** `SystemConfig.obsidian_vault_path` declares `validation_alias=AliasChoices("OBSIDIAN_VAULT_PATH","COBALT_SYSTEM__OBSIDIAN_VAULT_PATH")` without `populate_by_name` (`config.py:68-71`) → the YAML key `obsidian_vault_path` is **dropped** and `default_factory` → `os.getenv("OBSIDIAN_VAULT_PATH", "/Users/cobalt/cobalt/docs")` applies (`load_dotenv()` at `config.py:21` has already loaded `.env`). **Reproduced:** `SystemConfig(obsidian_vault_path="/FROM_YAML_KEY")` → env value; `SystemConfig(OBSIDIAN_VAULT_PATH="/X")` → `/X`; `get_config()` with a sentinel env → sentinel, not YAML. Real resolution today: `/Users/cobalt/cobalt/docs` (from `.env`; the YAML value is identical, and CLAUDE.md's `docs/Cobalt/` appears nowhere in code or config). **Three readers, two sources**: (a) `config.system.obsidian_vault_path` → `BaseFileTool.base_path` (`filesystem.py:89`, i.e. **all** LLM/Scribe writes), `CobaltScheduler` (`scheduler.py:90`), `sync_taxonomy.py:119`; (b) raw `os.getenv("OBSIDIAN_VAULT_PATH")` with fallback `~/Documents/Think` → `Scribe.vault_path` (`scribe.py:34-41`) used only for **reads/search**; (c) `project_root / "docs"` hard-coded → `dev_utils/ingest_knowledge.py:164`. `docs/` contains no `.obsidian/` → it is a folder tree, **not** an Obsidian vault (UNVERIFIED whether Obsidian opens the repo root or a parent as the vault). | `config.py:68-71`; probe |
| **H-3** | **Moving the vault out of the repo**: setting `OBSIDIAN_VAULT_PATH` (or `COBALT_SYSTEM__OBSIDIAN_VAULT_PATH`) moves (a) and (b) together; editing `config.yaml` alone does **nothing**; `ingest_knowledge.py` keeps ingesting the repo's `docs/` (or nothing); the hardcoded default `/Users/cobalt/cobalt/docs` remains the fallback; `.gitignore`'s `docs/*` + `!docs/assessment/` exception, `generate_context.py`'s scope problem (Pass 0 F-2) and `docs/assessment/` living inside the vault all become moot; `Scribe(vault_path=…)` constructor arg affects reads only — writes always go to the config vault (**`tests/test_scribe.py::test_write_note` fails for exactly this reason** plus the HITL gate, §7). Nothing else in `src/` references the vault location. | file:line |
| **H-4** | **Scribe rigidity — what it can write today**: Markdown only (`.md` auto-appended, `scribe.py:59-61,95-98`); `write_note(filename, content, folder="0 - Inbox")` → full overwrite of `<folder>/<file>.md` (no frontmatter handling, no templates, no merge); `append_to_daily_note(content)` → appends `\n\n### HH:MM - Cobalt Log\n<content>` to `0 - Inbox/Daily_Log_YYYY-MM-DD.md` (`:150-161`); `read_note(name)` → first `rglob` basename match anywhere in the vault (ambiguous) else direct path (H-1-style leak, `:120-128`); `search_vault(q)` → case-insensitive substring scan of every `.md`, returns basenames only (`:186-202`). **Every write returns a `requires_approval` dict** (ToolManager `DANGEROUS_TOOLS` → `scribe.py:104-109,168-173`), so each journal line / note needs an "Approve <id>" — the friction the requirements call out. No index.md/TOC maintenance, no wikilinks, no frontmatter schema, no folder policy beyond the `0 - Inbox` default. A flexible replacement must preserve: vault-relative paths resolved against **one** configured root; Markdown output; the daily-log append semantics (journaling/coaching); HITL only where the write is genuinely risky (Dejan's call whether system-generated notes need approval at all); search/read for the INTEL/OPS flows. | `scribe.py` |
| **H-5** | **Scheduler: one job, local-tz cron, direct file write, Gemini-only.** `CobaltScheduler._setup_jobs` registers **only** `morning_briefing` (`cron`, `day_of_week='mon-fri'`, `hour=8`, `minute=0`, no `timezone` → APScheduler uses the Mac's local zone; comment says "EST", `scheduler.py:26-38`). Job: `BriefingAgent(role="researcher")` (Gemini 3.1 Pro preview) + `tools=[{"googleSearch": {}}]` ReAct ≤4 loops (`:74-86`) → `open(<vault>/0 - Inbox/Morning_Briefing_<date>.md,'w')` **directly** (bypasses `ToolManager`, the jail and HITL, `:89-99`) → new `MattermostInterface()` + `connect()` + `send_message("town-square", …)` (`:104-107`). Any exception is logged and swallowed (`:109-110`); if the agent returns a `requires_approval` dict the job raises and writes nothing (`:83-86`). A second `BackgroundScheduler` exists in `DaemonTool` and is never started (Pass 2). `main.py` starts one `CobaltScheduler` at boot (`main.py:213-214`); the dead `CobaltAgent.main()` would start another. | `scheduler.py` |
| **H-6** | **Duplicate briefing**: (A) `skills/productivity/briefing.py` `MorningBriefing` — Cortex INTEL "briefing" → yfinance `NVDA/SPY/BTC-USD` + DuckDuckGo "top technology and finance news today" → `LLM(...)` (mainframe; `model_name=` kwarg ignored) `ask_structured(BriefingReport)` → Markdown `Briefing_<date>.md` via `Scribe.write_note` → **HITL approval required** (`briefing.py:47-57,113`). (B) `CobaltScheduler.generate_morning_briefing` — Gemini + googleSearch prompt from `prompts.yaml` with the in-play hard rules → `Morning_Briefing_<date>.md` written directly, Mattermost notify. Different models, prompts, data sources, filenames, write paths, approval semantics. Only (B) runs automatically; (A) is reachable only by asking Cortex for a "briefing". | file:line |
| **H-7** | **Driving schedules from `scanners.yaml`**: `CobaltScheduler` is a sync `BackgroundScheduler`; `ScannerOrchestrator.run_ingestion_cycle` is async (`asyncio.run` per job, or switch to `AsyncIOScheduler`); needs `CronTrigger(minute='*/N', hour='start-end', day_of_week='mon-fri', timezone='America/New_York')` per active scanner (the YAML's `"HH:MM"` strings → hour ranges; 2-min recurrence at 04:00–10:00 = ~180 Finviz calls/day/scanner), a DB connection factory, idempotent upserts (already `ON CONFLICT`), and a completion hook (enrich → tag → `daily_in_play` writer, Pass 4 §5). Roughly 80–120 lines plus config parsing; the hard part (collector) exists. | Pass 2 §4; `scheduler.py` |
| **H-8** | **Tests**: `test_scribe.py` **1 of 3 fails** (`test_write_note` asserts a file in `tmp_path` — but `write_note` routes to the *config* vault and returns a `requires_approval` dict, so nothing is written anywhere); `test_scheduler.py` 6 pass (job registration mocked); `test_generate_morning_briefing` **not run** — it patches `scheduler.LLM/os/open/get_config` but `MattermostInterface()` inside the job uses the real config → would attempt a real login and post to `town-square`; with a MagicMock LLM response it would also "write" the briefing via the patched `open`. As written the test is a live-side-effect test. | run output |

---

## 1. Hardcoded vault path & structure-assumption inventory (INFRA-2 input)

### 1.1 Root resolution
| Where | Value |
|---|---|
| `config.py:68-71` | `SystemConfig.obsidian_vault_path`: env `OBSIDIAN_VAULT_PATH` → default `"/Users/cobalt/cobalt/docs"`; alias `COBALT_SYSTEM__OBSIDIAN_VAULT_PATH`; **YAML key ignored** (H-2) |
| `configs/config.yaml:6` | `obsidian_vault_path: /Users/cobalt/cobalt/docs` (dead key) |
| `scribe.py:34-39` | `os.getenv("OBSIDIAN_VAULT_PATH")` → fallback `~/Documents/Think` |
| `filesystem.py:89` | `Path(config.system.obsidian_vault_path).resolve()` |
| `scheduler.py:90-92` | `os.path.join(vault, "0 - Inbox", "Morning_Briefing_<date>.md")` |
| `sync_taxonomy.py:119` | `vault / "0 - Projects/Cobalt/00 - Master Plan/Master_Taxonomy.md"` |
| `dev_utils/ingest_knowledge.py:164` | `project_root / "docs"` |
| `tests/test_scheduler.py` (×6) | `"/test/vault"` |
| CLAUDE.md | `docs/Cobalt/` (not in code); `.gitignore:7-9` `docs/*`, `!docs/assessment/**`, `docs/Cobalt/` |

### 1.2 Folder names assumed to exist
`0 - Inbox` (scribe default `scribe.py:63,68,153`; `cortex.py:237`; `scheduler.py:92`; `briefing.py:113`; `deep_dive.py:108`; `update_board.py:40`; `ops.py:25-39`; `prompts.yaml:67-81`) · `0 - Projects/Cobalt/Tasks` (`create_missing_tasks.py:172`) · `0 - Projects/Cobalt/90 - Project Management` + `/Requirements` (`create_prd.py:111`; `generate_constitution.py:259,287`) · `0 - Projects/Cobalt/00 - Master Plan` + `/ADR` (`generate_constitution.py:99,181,228-247`; `sync_taxonomy.py:119`) · `docs/` as a prompt example (`ops.py:33`, `prompts.yaml:75`, `prompt.py:82`? no — `prompt.py:82` lists `data/`; `orchestrator.py:115` lists `docs/`).

### 1.3 File-name patterns and formats
| Pattern | Producer | Format assumptions |
|---|---|---|
| `Daily_Log_YYYY-MM-DD.md` | `scribe.append_to_daily_note` (`:150-161`) | append-only; `### HH:MM - Cobalt Log` section headers |
| `Morning_Briefing_YYYY-MM-DD.md` | scheduler (`:91`) | raw LLM Markdown |
| `Briefing_YYYY-MM-DD.md` / `Briefing_Failed_YYYY-MM-DD.md` | `briefing.py:109,112` | `# 🌤️ Morning Briefing: …` sections |
| `Research_<topic_with_underscores>.md` | `deep_dive.py:107` | `# title / ## Executive Summary / ## Key Findings / ## Strategic Outlook`; "**Date:** Today" literal |
| `AutoNote_YYYY-MM-DD_HH-MM.md` | `cortex.py:233-238` | free text |
| `NN Title.md` task notes | `update_board.py:17-38`, `create_missing_tasks.py` | YAML frontmatter `status/priority/module/complexity/tags/created` (two different tag styles: `cobalt/task` vs `[cobalt, task, chat]`) |
| `PRD-001 Cobalt-Ion Tactical HUD.md`, `00 Cobalt Master Plan.md`, `System Manifest.md`, `Security Architecture.md`, `ADR-00N ….md`, `Roadmap.md`, `Backlog.md` | `create_prd.py`, `generate_constitution.py` | frontmatter + `[[wikilinks]]` to each other (`generate_constitution.py:82-85`) |
| `Master_Taxonomy.md` | read by `sync_taxonomy.py` | 4-column Markdown table (`:3,25-60`) |
| any `*.md` | `scribe.search_vault`, `read_note` (`:120,186`), `ingest_knowledge` | dot-folders skipped; basename-only results; whole vault embedded to OpenAI (Pass 1 H-7) |
| `.md` suffix | `scribe._resolve_path/write_note` | auto-appended; no other file types supported |
| `index.md` TOCs (Requirements §9) | **nobody** | — |

### 1.4 Behavioural assumptions
- Writes go through `ToolManager.execute_tool("write_file"/"append_to_file")` → HITL (`scribe.py:101-109,164-173`) — except the scheduler (direct `open`) and the dev_utils scripts (which call `Scribe.write_note` → HITL dict → they `print()` the dict and write nothing; UNVERIFIED whether they predate the gate).
- `Scribe(vault_path=…)` affects reads only; writes ignore it (H-3).
- `read_note` prefers the first `rglob` hit by basename across the whole vault.
- Cortex OPS routing is keyword-based on the raw message (`"log"/"journal"`, `"save"/"note"`, `"search"/"find"`, `cortex.py:225-249`) — e.g. any sentence containing "note" becomes an `AutoNote_*` write proposal.

---

## 2. Vault-root discrepancy — verdict
Code uses **`.env OBSIDIAN_VAULT_PATH`** (and would accept `COBALT_SYSTEM__OBSIDIAN_VAULT_PATH`); `config.yaml` is inert for this key; hardcoded fallback `/Users/cobalt/cobalt/docs`; `Scribe` reads the env var directly with a different fallback (`~/Documents/Think`); `ingest_knowledge` hardcodes repo `docs/`. CLAUDE.md's `docs/Cobalt/` is wrong (already corrected in Pass 0 commit; the OPEN ITEM there is now answered). Recommendation for INFRA-2: one resolver (`config.system.obsidian_vault_path`), make the YAML key actually work (`populate_by_name=True` or drop the alias), delete the two side-channel reads, fail loudly if the path doesn't exist or lacks `.obsidian/`.

## 3. Scribe — what a flexible replacement must preserve (H-4)
Vault-relative addressing under one root; Markdown notes with optional frontmatter (the task/PRD writers already emit it); daily-log append with timestamped sections (journaling/coaching input); read/search for INTEL/OPS; HITL only for risky writes (policy decision); explicit folder policy from config (not `"0 - Inbox"` literals in 8 places); index.md/TOC maintenance and wikilinks per Requirements §9; templates per note type (briefing, research, journal, in-play list) — today each producer formats its own Markdown inline.

## 4. Scheduler — jobs, wiring, gaps (H-5/H-7)
Jobs: 1 (`morning_briefing`). Wiring: `main.py:213-214` → `CobaltScheduler().start()` → APScheduler thread → `generate_morning_briefing` → `BriefingAgent` → vault write (direct) → Mattermost. Not wired: scanners (`scanners.yaml` schedule blocks), cadence reviews (EOD/EOW/EOM/EOY, Requirements §5), TradingView evening agent, news windows (04:00–16:00 ET). Timezone: none set (local). Observability: none (no job history, no failure alert — failure is a log line). Duplicate briefing: H-6 — keep one (the scheduler path is closer to the requirements' premarket agent but is Gemini-locked and bypasses HITL/jail; the skill path is local-first but content-poor).

## 5. Leak paths outside the vault root (H-1)
- `write_file` / `append_to_file` → anywhere, after an approval whose card omits the path (`filesystem.py:291-297,224-237`).
- `read_file` / `list_directory` → anywhere, **no approval** (`:165-183,341-358`).
- `Scribe.read_note` direct-path fallback → absolute or `../` paths readable (`scribe.py:127-133`).
- Scheduler direct `open()` — system-controlled name, vault-relative; safe as long as `vault_path` is sane.
- Prompt context advertises repo paths (`prompt.py:78-83`, `orchestrator.py:110-115`).
Fix shape (not applied): `if not resolved.is_relative_to(base): raise SecurityError` — one line — plus reject absolute paths outright, plus include the resolved path in the approval card.

---

## 6. RETAIN / BROKEN-FRICTION / KILL-candidate summary
**RETAIN**: `BaseFileTool` design (single jail point, Pydantic inputs) once the check is fixed; `Scribe.append_to_daily_note` semantics (journaling); `CobaltScheduler` as the place for all cron jobs; `prompts.yaml scheduler.morning_briefing` content (the only pre-market spec); `DeepResearch` note output; dev_utils' frontmatter conventions as a seed for note templates.
**BROKEN-FRICTION**: jail (H-1, security); YAML vault key ignored + three resolvers (H-2/H-3); `Scribe` writes ignore its own `vault_path`; HITL on every note/log line; `0 - Inbox` literal in 8 places; `read_note` basename ambiguity; no tz on cron; direct `open()` bypass in scheduler; Mattermost session per briefing; swallowed job errors; `test_write_note` wrong by design; `test_generate_morning_briefing` live-side-effect test; cortex OPS keyword routing.
**KILL-candidates**: `MorningBriefing` skill **or** the scheduler briefing (one must go — H-6); `~/Documents/Think` fallback; `dev_utils/{update_board,create_prd,create_missing_tasks,generate_constitution}.py` (one-shot vault seeders that now only produce approval dicts; their *content* is intent history worth preserving in the vault, the scripts are not); `ingest_knowledge.py` vault ingestion (Pass 1 K-5); `Scribe.read_note` direct-path fallback.

---

## 7. Tests run
`uv run pytest tests/test_scribe.py tests/test_scheduler.py -k "not generate_morning_briefing" -q` → **7 passed, 1 failed** (`test_write_note`, `tests/test_scribe.py:33`), 1 deselected (would post to Mattermost). Probes: `BaseFileTool._validate_path` on four inputs (H-1); `SystemConfig` precedence with a sentinel env var (H-2). No files created.

## 8. Component map — ORIGINAL INTENT

| Component | File | Verdict | ORIGINAL INTENT (documentation trail) |
|---|---|---|---|
| `Scribe` | `scribe.py` | BROKEN-FRICTION → rebuild | System Manifest "Scribe (Ops): Documentation & Knowledge Management, Automated Journaling & Logging, Project Management (Kanban Updates)"; stack `obsidian-api`, `jinja2` (`generate_constitution.py:132-135,176`) — neither library is used; task 34 "Automated Trade Journaling… Append to the Daily Note in Obsidian via Scribe" (`create_missing_tasks.py:142-161`); docstring "Refactored to use Environment Variables for portability. STRICT RULE: All automated writes go to '0 - Inbox'" (`5cca1aa` 02-27 "OS-agnostic architecture", UNVERIFIED mapping); "All write operations MUST route through ToolManager" ← `770c43b` (02-25) Zero-Trust HITL; Requirements §4 "Obsidian is the system of record… Cobalt automates ingestion", §5 "Scribe… must be rebuilt flexible (current version is rigid)". |
| Filesystem tools (`read/write/append/list`) + jail | `filesystem.py` | BROKEN (security) | `87e16c7` (02-25) "Registered filesystem tools (read, write, list) in ToolManager… Verified successful read-only directory listing via Mattermost"; docstring "safe read, write, and directory listing"; `770c43b` HITL gating of writes. The jail itself: UNVERIFIED commit; no ADR. |
| `SystemConfig.obsidian_vault_path` | `config.py:62-71` | BROKEN-FRICTION | `61f300d` (02-19) Pydantic Settings env overrides; `5715465` (02-20) "native Pydantic V2 logic… strict directory architecture"; alias added: UNVERIFIED. |
| `CobaltScheduler` + `morning_briefing` job | `scheduler.py:14-110` | BROKEN-FRICTION | `0bf87fd` (02-09) "implemented morning briefing skill"; docstring "Background job scheduler for automated tasks like Morning Briefing"; `scheduler.py:54-58` "Runs the Gemini 3.1 Pro query… googleSearch grounding" (`8a69874`/`cc14caa`, UNVERIFIED which); Requirements §5 premarket agent, §5 cadence reviews (not built). |
| `BriefingAgent` | `scheduler.py:113-231` | BROKEN-FRICTION (Pass 5) | Docstring "Temporary agent… ReAct loop and ToolManager… researcher role (Gemini 2.5 Pro)"; `05b0617` Unified ReAct. |
| `MorningBriefing` skill | `briefing.py` | KILL-candidate (duplicate) | `0bf87fd`; PRD-001 Story A "Morning Briefing (Context)… curated list of opportunities" (`create_prd.py:55-59`); docstring "Orchestrates Tools to create a daily digest… Pydantic Models and LLM Synthesis". |
| `DeepResearch` note writer | `deep_dive.py:106-110` | RETAIN | Docstring "Plan → Search → Analyze → Report"; System Manifest Scout; Requirements §8 research note "filed by the scribe into the vault". |
| `Cortex._run_ops` | `cortex.py:216-251` | BROKEN-FRICTION | `eef5bdf` intent routing; docstring "Handles Operations (Scribe, Medical, Scheduling)"; Ops dept description `config.yaml:123-125` "Medical Admin (Billing/Coding), Journaling (Scribe), Scheduling"; tasks 28/29 "Ops Medical Stub", "Privacy Guardrails" (`update_board.py:63-67`). |
| `sync_taxonomy.py` (vault → `themes`) | | RETAIN (Pass 4) | `cc14caa`; docstring "Parses the 4-column Master_Taxonomy.md"; vault note as the theme source of truth (Requirements §4 "Obsidian is the system of record"). |
| dev_utils vault seeders (`update_board`, `create_prd`, `create_missing_tasks`, `generate_constitution`) | | KILL-candidate (scripts) | Docstrings "populate the Obsidian Project Board with Phase 4 & 5 tasks", "Cobalt Requirements Generator", "Cobalt Constitution Generator (Master Version)"; `9c1af63` (02-11) "PRD-001"; `8a69874` (03-17) "align PRDs and task board"; Requirements §11#7 backlog/kanban always current — the mechanism was these scripts. |
| `ingest_knowledge.py` vault ingestion | | KILL-candidate | `8c6c5d8` Vector Librarian (Pass 1). |
| `0 - Inbox` convention | many | RETAIN as *a* policy, not a literal | Scribe docstring "STRICT RULE"; `update_board.py:39` "Save to 0 - Inbox (You can drag them to your board later)"; Requirements §9/INFRA-2 Karpathy raw → wiki → output model would replace it. |

## 9. Inputs to other passes / INFRA
- **INFRA-0 / immediate**: the jail (H-1) is a one-line fix with outsized risk; the approval card should show the resolved path (Pass 3 H-2). Recommend treating as the first fix after the assessment, before any vault redesign.
- **INFRA-2**: §1 is the inventory; one resolver; `populate_by_name`; note templates; index.md generation; folder policy in config; decide HITL policy for system-generated notes; live vs test vault = two values of one env var, not two code paths.
- **Pass 7 (config)**: `SystemConfig` alias bug; `load_dotenv` at import; `.env.example` empty so `OBSIDIAN_VAULT_PATH` is undocumented.
- **Sprint planning**: scanners → `CobaltScheduler` (H-7) is the cheapest high-value job after the collector fix.

## 10. UNVERIFIED
- Where the real (Obsidian Sync) vault with `.obsidian/` lives and whether Obsidian currently indexes `docs/` (vault not read; no `.obsidian` under `docs/`).
- Whether the dev_utils seeders were run before the HITL gate existed (their notes exist under `docs/0 - Projects` by name only).
- The commit that introduced the `validation_alias` and the broken `is_relative_to` check (history is coarse: `61f300d`/`5715465`/`87e16c7`).
- Whether `test_generate_morning_briefing` has ever posted to Mattermost during a test run (not executed here).
