# TRIAGE.md — Component Disposition Record
Ruled: 2026-08-22 · Authority: Dejan (every line) · Method: subsystem-by-subsystem walk of the ASSESSMENT.md four-tier table in the planning session, with pushback per the critical-thinking-partner contract.

Governing frame: COBALT-REQUIREMENTS.md is canonical; strangler/hybrid rebuild (new `src/cobalt/` core beside the old tree). Tier meanings under the strangler: **KEEP-AS-IS** = ports through the test/config gate · **KEEP-CONCEPT / REBUILD** = rebuilt in the new core, old code as spec · **REDESIGN** = design decision (ADR/session) then new build · **KILL** = never crosses; dies in place with the old tree.

Sprint ladder is NOT locked by this document — the MVP Charter (Product Definition phase) re-derives it. Dispositions only.

---

## Cross-cutting rulings (apply everywhere)

- **Fail-loud law**: no plausible-empty artifacts, ever. No data → Pydantic validation fails → loud FAILED alert. A config error crashes; it never silently falls back to defaults.
- **Watcher standard**: deterministic watchers (cron / webhook / poller code) emit typed events; stateless agents are invoked on events; flexibility = config-defined jobs. Never an LLM sitting in a watch loop.
- **One-path rule**: no duplicate implementations of the same job (briefings, glue scripts, intercepts, DDLs). Duplicated paths rot; the second copy is killed on sight.
- **Secrets**: no secret ever printed/logged (kill every DEBUG dump found); no secret in `.env` or command args; VaultManager is the only store; DSNs composed at runtime from vault parts via ONE connection factory (URL-encoded — closes the @-bug class). Gemini-era failure post-mortem: `.env` is static and cannot call the vault — composition happens in application boot code, two-phase (settings → unlock vault → fetch password → build DSN), never in dotenv.
- **Routing law**: every LLM call goes through the routing layer; out-of-band calls (embeddings, extractor) are routing bypasses and were ruled accordingly.
- **Agent architecture north star**: Hermes-agent / BuzzBot / GrokBot pattern — persistent, self-sufficient specialist bots (own schedule, memory, config-driven behavior) organized by one chief-of-staff orchestrator. Not a monolithic ReAct switchboard.
- **Shadow-mode promotion law**: no variable, grader, or detector ever flips from human-fed to engine-fed without a shadow run (engine computes silently alongside Dejan's hand input for N sessions), agreement stats reviewed, and HITL-token approval (NN#12 — it IS a trading-logic change).
- **Sample-size law**: no EV or auto-grade renders without its n attached; n<30 displays "insufficient data", never a number. EV is ranking, not gospel.
- **Source-substitution guarantee + loud degradation**: every data source sits behind a collector interface (swap = new collector + config, nothing upstream notices). A dead/changed source = red banner + degraded-mode flag on mission control, never silent staleness. ToS-risky scraped sources feed context surfaces only, never the grading chain.
- **Config-as-code**: every config family gets a Pydantic schema validated on load (bad file crashes with a line number), lives in git (diffable, revertible), and ships with a dry-run command ("what would this rule/playbook/schedule do against yesterday's data"). No meta-framework for cross-family validation unless proven needed.
- **Human-only tape dot**: every playbook's variable registry includes at least one explicitly human-only discretionary variable (tape read / context feel) that the system renders as Dejan's and never computes. The board stays honest about what it cannot see.
- **Planning hard cap**: all remaining design work fits in two calendar weeks. When the cap hits, ship with what's decided; the rest becomes "decide during build".

---

## 2.1 Memory / Hippocampus

| Component | Ruling | Notes |
|---|---|---|
| `MemoryProvider` ABC | KEEP-AS-IS | Ports only if the new core wants the same contract — not reflexively |
| `MemorySystem` JSON fallback | KILL | Postgres is non-negotiable #9 |
| `PostgresMemory` core | KEEP-CONCEPT / REBUILD | Conn factory, DDL-once, embeddings via routing, scrub w/o vault re-unlock |
| `_hilt_` trio | KILL | Dead code |
| `HITLProposalStore` | KEEP-CONCEPT / REBUILD | Per ratified HITL rebuild spec |
| `FastPathCache` | KILL | Dead end-to-end; burned an OpenAI call per lookup |
| `init_5_pillar_schema.py` | KEEP-CONCEPT / REBUILD | Unguarded DROP TABLE on shared DB disqualifies as-is |
| `db_status.py` | KEEP-AS-IS | Minus DEBUG secret dump |
| `test_5_pillar_db.py` | KILL | May resurrect later as guarded cobalt_dev integration test |
| `ingest_knowledge.py` | KILL | Hardcoded paths; superseded by research-engine ingestion |
| `tools/knowledge.py` | KEEP-AS-IS | |
| Memory tests | REDESIGN | Real cobalt_dev integration tests; mock-SQL suites protect nothing |
| OpenAI embedding call sites | REDESIGN | **Local-vs-cloud embedder ADR GATES the memory port** (Req §4 local-first, §8 routing; 1536-dim baked into 4 tables → migration either way) |
| 5-Pillar schema (`schema.sql`) | **REDESIGN** (escalated from KEEP-AS-IS) | Concept itself questioned. Two schema universes (runtime DDL vs schema.sql), zero-writer tables, Ion-era leftovers, no design rationale ever written. → **Data-Model Design Session** |
| Dual `hitl_proposals` DDL | **REDESIGN** (escalated) | Friction point, stale, hallucination history. Folds into the schema decision — one decision, not two |

**Parked with anchors**: Mattermost shares `cobalt_brain` — resurfaces at 2.7 docker-compose (position recorded: SPLIT) and is a mandatory Data-Model Session agenda item (wipe-radius argument).

## 2.2 Browser / Playwright / scanners

| Component | Ruling | Notes |
|---|---|---|
| `BrowserTool` (Playwright fetch primitive) | KEEP-AS-IS | Scoped as fetch-primitive ONLY. §5 authenticated scraping = NEW BUILD (below) |
| Browser action DSL, `AOMExtractor`, `Maps` | KILL | Never completed, unreachable |
| Domain whitelist | KEEP-CONCEPT / REBUILD | All navigation paths, subdomain handling |
| Vault credential injection | KEEP-CONCEPT / REBUILD | Required by the authenticated-session build; `config.vault_manager` bug |
| `DaemonTool` watchers | KILL | Watcher standard replaces (see cross-cutting) |
| `FinvizExtractor` (752-line Playwright scraper) | KILL | Superseded by API client |
| `ScannerOrchestrator` + `scanners.yaml` | KEEP-CONCEPT / REBUILD | Prime MVP-pillar-1 organ; 2,209 real snapshots; needs schedule wiring, typing, conn factory |
| `MetadataEnricher` | KEEP-AS-IS | Minus secret-dumping log sink |
| `SemanticTagger` + `themes` | KEEP-CONCEPT / REBUILD | Status vocab fix |
| `live_run_orchestrator.py` | KILL (wrapper) | Concept (one-command end-to-end) absorbed into the rebuilt pipeline's own entrypoint — same code path for scheduler, dev, tests. No second glue script, ever |
| `live_run_{finviz,quote,dynamic}` smoke scripts | KEEP-AS-IS | Manual smoke |
| Registered non-runnable tools | KILL | |
| Browser tests | REDESIGN | Drop DSL tests, add collector coverage |
| `UniversalExtractor` + `compute_delta` | KILL (escalated from REDESIGN-or-KILL) | §8 resolver covers change detection; concept re-enters only via ADR if research design finds a need |
| `FinvizApiClient` | KEEP-AS-IS → grows | Ports as seed; MUST become config-driven across ALL ELEVEN export families (Screener, Portfolio, Stock/bars, Groups, Options, Latest Filings, News, Insider, Managers, Funds, Calendar). Surface barely scratched — full exploration at Data-Source Spike |

**NEW BUILD (named requirement)**: Authenticated persistent browser sessions for paid sites (smbtraining, SMB realtime board, FinancialJuice, others). Operational spec (Dejan): log in once into a persistent context; sessions live days-to-weeks unattended; no keep-alive machinery; credential-refresh flow for occasional expiry; logged-out/changed-page = typed failure + LOUD alert (never scrape a login page as content); page-structure drift = alert + redesign.

## 2.3 Mattermost / HITL

Governing: the previously ratified HITL rebuild spec (risk-tiered capability classes, one card with full params, identity binding, single-use expiring grants, fail-closed).

| Component | Ruling | Notes |
|---|---|---|
| REST helpers + native WS loop | KEEP-AS-IS | Cache IDs; drop per-message user lookups |
| Old `_run_websocket_in_process` / `_handle_events` | KILL | |
| Approval interceptor | REDESIGN | Per HITL spec |
| Mattermost-local ReAct loop + parsers | KILL | Folds into single department loop |
| `ProposalEngine` live methods | KEEP-CONCEPT / REBUILD | |
| `ProposalEngine` dead methods | KILL | |
| `Proposal` / `IntentAlignment` models | KEEP-AS-IS | Card must render params |
| `DANGEROUS_TOOLS` + `bypass_hitl` | KEEP-CONCEPT / REBUILD | Becomes the risk-tiered capability-class table; reads un-gated inside the jail |
| `MATTERMOST_CREDS` vault routing | KEEP-AS-IS | Minus DEBUG dump |
| `Config.unlock_vault` / `inject_secrets` | KILL | |
| Login-failure exit / no supervisor | REDESIGN | Supervision + out-of-band alert (the alerting channel is the dead channel) |
| HITL tests | REDESIGN | |
| `Cortex._generate_proposal` (unpersisted intercept) | KILL (escalated from REDESIGN) | Duplicates the rebuilt HITL layer; no parallel intercept paths |

## 2.4 Trading logic / scanners

| Component | Ruling | Notes |
|---|---|---|
| `Strategos` | KEEP-CONCEPT / REBUILD | |
| `Playbook` | KEEP-CONCEPT / REBUILD | One validated reader, registry |
| `Strategy` ABC | KILL (escalated from hedge) | Never worked; shaped around daily-bar world. Specialist contract designed fresh per GrokBot pattern in agent-pod work; backtester/live shared-contract idea survives as one design input |
| `SecondDayPlay` | KILL (code) | **Day 2 is a SETUP and is NOT killed** — re-enters as config via the taxonomy (below) |
| `strategies.yaml` + `StrategyConfig` | REDESIGN | Schema from Taxonomy Session output |
| `rules.yaml trading_rules` | KEEP-AS-IS | Consumed fully; in-play rules move here |
| `rules.yaml cortex_routing` | KEEP-CONCEPT / REBUILD | Actually captured by config |
| `FinanceTool` | KEEP-AS-IS | Swing-context stopgap; never a setup source; deprecated when FMP collectors land |
| `MorningBriefing` skill | KILL | Duplicate — see briefing ruling below |
| **Briefing (both implementations)** | **KEEP-CONCEPT / FULL REDESIGN** | Modeled on prebell.laldinsoft.com (all tabs). ONE briefing engine; both old code paths die (this overrules the 2.6 "keep scheduler briefing" proposal). Consumes in-play surface, market context, watchlist rendering. Designed in Product Definition sittings — it IS pillar 2's morning surface |
| In-play rules in `prompts.yaml` | REDESIGN | Deterministic, testable function over typed snapshots — MVP pillar 1's heart |
| Grading / EV / sizing | REDESIGN (new build) | Spec: §6 + ASET sizer HTML + Opportunity Framing xlsx; all arithmetic deterministic |
| Priority setups engine | REDESIGN (new build) | Dependency: intraday bar source — Finviz stock export is candidate, VERIFIED at Spike, not assumed |
| `daily_in_play` writer | KEEP-CONCEPT / BUILD | Never-built pillar-1 terminus |
| `tests/test_strategies.py` | REDESIGN | |

**Taxonomy ruling (Dejan)**: Setups = regime/context layer; Trades = entry triggers; Cameron H's `Setups & Trades Project.xlsx` = the conditional-probability heuristic (given a setup → which trades likely appear, with-trend/countertrend). Gemini treated it as a crown jewel but never operationalized it. → **Trading Taxonomy Design Session** (inputs: the spreadsheet, cheat-sheet library, Jure examples, Dejan explains the heuristic; output: playbook schema ADR). First deliverable: canonical vocabulary + one-line §6 amendment to COBALT-REQUIREMENTS.md (the doc currently calls trades "setups").

## 2.5 LLM routing / Cortex / prompts

| Component | Ruling | Notes |
|---|---|---|
| `LLM` routing class | KEEP-AS-IS | + retries, timeouts, fallback chain, reasoning_effort pass-through, usage/cost capture |
| `config.yaml` models/profiles/network | KEEP-AS-IS | Validated; Ion nodes dropped |
| `Cortex` classification | KEEP-CONCEPT / REBUILD | Deterministic triage, T=0; per north-star architecture |
| `OrchestratorEngine` | KEEP-CONCEPT / REBUILD | The one chief-of-staff; split-brain collapses |
| `BaseDepartment` + Engineering/Ops | KEEP-CONCEPT / REBUILD | One loop, one grammar, prompts from YAML; shaped by GrokBot ruling |
| `PromptEngine` | KEEP-CONCEPT / REBUILD | |
| `prompts.yaml` | KEEP-AS-IS | Dead sections removed or wired |
| `UniversalExtractor` LLM call | Moot | Tool killed in 2.2 |
| Out-of-band embedding calls | Absorbed | Into 2.1 embedder ADR |
| `dev_utils/test_routing.py` | KEEP-AS-IS | Manual |
| `check_gemini_models.py` | KILL | |
| `tests/test_llm.py` | REDESIGN | |
| `Persona` class | KILL + harvest rider | Persona/system-prompt text becomes pure YAML/template data (anti-rigidity); old persona strings harvested into prompt-design work as reference — a year of behavior tuning is not lost |

## 2.6 Scribe / vault / scheduler

| Component | Ruling | Notes |
|---|---|---|
| `Scribe` | KEEP-CONCEPT / REBUILD | Mandated by §5; blocked by Vault Design Session |
| Filesystem tools + jail | KEEP-AS-IS | Jail works post-hotfix; cards render paths; reads un-gated inside jail |
| `obsidian_vault_path` resolution | KEEP-CONCEPT / REBUILD | ONE resolver; closes CLAUDE.md's OPEN ITEM |
| `CobaltScheduler` | KEEP-CONCEPT / REBUILD | Timezone-correct; jobs in YAML (watcher standard concrete) |
| Scheduler briefing | OVERRULED → dies | Merged into the 2.4 prebell FULL REDESIGN; survives only as evidence of inputs |
| `DeepResearch` | NO PORT — dies in place | Single-shot cloud call; §8 engine replaces substance, Research Analyst bot replaces interface; old tree keeps it usable meanwhile (strangler gives the stopgap for free) |
| `Cortex._run_ops` keyword routing | REDESIGN | Folds into department rebuild |
| dev_utils vault seeders | KILL | Content archived as intent history |
| `0 - Inbox` literal policy | REDESIGN | Folder policy in config, defined by Vault Session; inbox note is MVP pillar 3's front door — an INTERFACE, not a folder |
| Scribe/scheduler tests | REDESIGN | Current write-test enshrines the bug |

**Vault ruling (Dejan)**: dedicated **Vault Design Session** settling three philosophies — Karpathy write-time (raw→wiki→output), Nate B Jones query-time counter (SQL truth + scheduled compilation agent generating the wiki), original Obsidian linking heuristic (new concepts emerge from chaos — the second-brain property). Session chooses where each data class lives on that spectrum; inherits the Postgres-vs-Markdown boundary question; runs back-to-back with the Data-Model Session.

## 2.7 Config / VaultManager / ops

| Component | Ruling | Notes |
|---|---|---|
| `CobaltSettings` + YAML loader | KEEP-AS-IS core / REBUILD edges | No silent default fallback (fail-loud); unknown keys rejected; cortex_routing/scanners captured; `.env.example` |
| `keys:` alias→env block | REDESIGN | Direct vault naming; kills double-translation bug class |
| `VaultManager` (Fernet store) | KEEP-AS-IS | Survived rotation; THE credential store |
| `manage_vault.py` | KEEP-AS-IS | getpass-only policy enforced |
| Secret-printing log sinks | KILL (blanket) | Wherever found, all files |
| `cobalt.sh` | KEEP-CONCEPT / REBUILD | PID handling, health check, dev/prod awareness |
| launchd plists | KEEP-CONCEPT / REBUILD | Into ops/ (INFRA-0.5) + supervision fix (restart policy, out-of-band alert) |
| docker-compose | KEEP-AS-IS | **DB split position recorded: SPLIT** (cobalt_brain for agent; Mattermost keeps own DB; wipe-radius decisive; INFRA-1 builds the migration muscle) — final call at Data-Model Session |
| `generate_context.py` | KEEP-AS-IS | |
| `wipe_memory.py` / `reset_memory_table.py` | KEEP-CONCEPT / REBUILD | Prod guards (refuse against production DB name); NEVER ported as-is |
| `.env` / `DATABASE_URL` handling | REDESIGN (elevated to named rule) | See Secrets cross-cutting rule: two-phase boot, DSN from vault parts, one connection factory. Gemini failure post-mortem attached |

---

## Pre-beta increments (build first — Cobalt's first shipping slices)

Reframed from "stopgaps": these are Cobalt pre-beta, built in `src/cobalt/` from day one (Pydantic-typed, config-driven, fail-loud, tested — never loose scripts). Live market-hours use IS the beta test; what sticks earns deepening. Ordered by friction-relief per effort:

1. **ASET semi-auto sheet** (days): deterministic sizing math — daily stop = account/50 (Daily-Stop Model card); grade→risk map A+ 80% / A 30% / B 15% / C 5% / D-SAW 0% ("too risky to feel like a C = zero size"); prefill everything fetchable (ticker data, daily stop, entry/stop distance → shares); Dejan reads inputs and sets the grade; every sizing persists to Postgres (future EV/Guardian training truth). This is the Trade Radar card in manual-grade fill mode.
2. **DRC + PlayBook prefill** (~1–2 weeks): prefill-first inversion of the trade-reporter reference (its rendering layer — 181-line reportlab DRC builder, 530-line PPTX builder against the licensed SMB template — is kept nearly wholesale; a Cobalt prefill engine feeds it). Obsidian front end: Python writes a structured daily data note; Templater templates pull prefilled fields; Dejan's critical thinking is the only manual input. Includes the daily rule-adherence checkboxes (Guardian baseline) and a one-line replay ledger.
3. **Prebell-lite** (2–3 weeks thin, then weekly iteration): regime tiles, catalyst calendar, in-play candidates from existing scanner data. Fail-loud from line one — a failed prep says FAILED, never renders plausible-empty.

## Guardian rule set (initial — from Dejan + the Daily-Stop Model card)

Live as DRC self-graded checkboxes until Guardian ships; Guardian later enforces in real time:
1. No entries premarket (no stops placeable; protects open psychology).
2. Prime entry window 9:30–10:30/11.
3. No new entries 11:00–2:00 (chop).
4. Second window 2:00–3:45.
5. Nothing after 3:45 (the hail-Mary rule).
6. Daily stop hit → next day is demo.
7. Two consecutive stop-outs → two days off.
Rule *deactivation* during market hours requires HITL token with a cooling delay (takes effect next session) — sober-you sets rules, tilt-you can't edit them live.

## Design-session register (collapsed — planning hard cap: two calendar weeks)

1. **Trading Taxonomy Session** (first) — ABSORBS the variable registries. Inputs: Setups & Trades xlsx, cheat-sheet library, Jure examples, Dejan's walkthrough. Outputs: canonical vocabulary + §6 amendment, playbook schema ADR, per-playbook variable registry (name, scale, computation source, cheap/expensive tier, ≥1 human-only tape dot). Unlocks `strategies.yaml` redesign + setups engine + semaphore board.
2. **Data-Model + Vault combined block** (one weekend) — they share the Postgres-vs-Markdown boundary. Outputs: data-model ADR + embedder ADR (gate the memory port), Mattermost DB-split decision (position: SPLIT), vault structure per the Karpathy/Jones/Obsidian-linking argument, inbox-as-interface policy, lazy-migration scoping (new structure for new output; old notes migrate lazily).
3. **Data-Source Spike** — NOT a session: sprint-0's first Claude Code task. Deliverable: data-source verification memo (Finviz eleven families fired end-to-end, intraday bars VERIFIED, FMP pricing, TradingView MCP state) — before the Charter locks anything depending on them.
4. **Product Definition sittings** (timeboxed): Day-in-the-Life → mission-control + semaphore-board + Trade Radar card mockups (prebell/DRC/RUBRIC references; Moderna Day-2 as worked example) → MoSCoW with forced subtraction pass → **MVP Charter** → ladder re-derived. Validation upgraded: working pre-beta slices judged on live mornings, not static mockups.
5. **Rules Engine Session** (post-Charter; gates Guardian, not MVP) — dynamic no-code trading-rules config: rule schema (trigger, tracked state, action ladder, channel, window), authoring path (DM/voice → chief-of-staff drafts config → HITL-token activation per NN#12; Cobalt may PROPOSE rules from DRC patterns through the same gate), hot-reload pickup by Guardian-class bots, boundary vs playbook variables (variables grade opportunities; rules govern the trader).
6. **HITL rebuild** — spec ratified; implementation sprint.

## Charter requirements (binding on the sittings)

- **Capacity math shown**: hours/week × weeks ≥ estimated effort, calculated, not vibed. Must fit the ~2-month usable-MVP timebox.
- **Success criteria are trader metrics, not software metrics**: DRC completion rate, rule-violation trend, sizing-correctness vs model, selectivity ratio — reviewed monthly by the coach cadence; three flat months = mandated stop-and-question.
- **Build/trade firewall**: market hours + DRC block untouchable; build lives in defined slots (weekday 5:30/6:00–8:00 hard stop; evenings gated on DRC done; weekends invitation-only, no standing claim). Build slot yields to trading prep on heavy-catalyst mornings; morning trade quality tracked on build vs non-build days.
- **MVP semaphore scope**: ~5 deterministically cheap variables auto-computed (regime vs averages, VIX, sector strength, RVOL, extension); all else manual dots.

## Operating rhythm (Phase 0, active now — automation-first, anti-friction by design)

Manual-rigor plan withdrawn (calendar saturation = designed failure for Dejan's stress/anxiety profile; missed tasks become self-attack ammunition). Replaced by: pre-beta slices remove grunt work rapidly; THREE calendar anchors only (3:45 PM weekday DRC capture alarm · loose 11:15 AM weekday sim/playbook nudge, dismissible · Saturday-morning invitation, guilt-free); DRC-done gates evening Cobalt talk (the project as reward); coaching is positive-reinforcement, forward-framed, never shame-backward; "not profitable yet" is said, understood, retired; recorded SMB meetings follow decide-at-skip-time (name the replay slot or consciously drop it — queued = debt, dropped = decision); separate chat sessions per role (project / coach / DRC debrief / day-organizer) are the manual prototypes of Cobalt's future agents.

## Standing follow-ups

- CLAUDE.md "Current phase: read-only assessment" section is stale → rewrite for build phase (folds into Pass 8 doc-baseline work).
- COBALT-REQUIREMENTS.md §6 vocabulary amendment → after Taxonomy Session.
- Old persona strings + vault-seeder content → harvested as reference/intent history before old-tree deletion commits.
- New reference artifacts → docs/references/ + INDEX entries: SMB-DRC_Template.pdf, SMB_PlayBook_Template_2024.pptx (licensed — verify it may be committed to the private repo; else keep local-only under a gitignored assets path), Daily_Stop_Model_Card.pdf, SMB_Inside_Access_Calendar.pdf, trade-reporter-src.zip (unpacked; rendering builders are the reuse target).
- Dejan's existing Obsidian DRC/prep Templater templates → collected as prefill-engine input for pre-beta slice 2.
