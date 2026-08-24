# BACKLOG.md — Cobalt kanban + backlog

Source of truth for work state. Derived from docs/assessment/TRIAGE.md
(ruled 2026-08-22). Dispositions live THERE; this board only tracks
sequencing and progress. Sprint ladder below the pre-beta lane is NOT
locked — the MVP Charter re-derives it.

Update rule (CLAUDE.md): keep this board current as you work; move cards,
don't duplicate them.

---

## NOW (in build)

- **Pre-beta slice 1 — ASET semi-auto sheet** (days)
  Deterministic sizing engine in src/cobalt/: daily stop = account ÷ 50;
  grade→risk A+ 80% / A 30% / B 15% / C 5% / D-SAW 0%; entry/stop/direction
  → risk $ + shares. Grade and stops always Dejan's input; prefill last
  price via FinvizApiClient path. Every sizing persisted to Postgres
  (cobalt_dev; table may be reshaped by data-model ADR). Surface: simplest
  working local form (trade-reporter Flask pattern). Fail-loud. Tests +
  smoke. Spec: docs/references/aset_daily_position_sizer.html +
  Daily_Stop_Model_Card.pdf. Gate: stop and show Dejan the working sheet.

## NEXT (immediate lane, in order)

- **Pre-beta slice 2 — DRC + PlayBook prefill** (~1–2 wks)
  Prefill-first inversion of docs/references/trade-reporter/ (keep its
  reportlab DRC builder + PPTX builder nearly wholesale; Cobalt prefill
  engine feeds them). Obsidian front end: structured daily data note +
  Templater pulls. Includes daily rule-adherence checkboxes (Guardian
  baseline) + one-line replay ledger. Input to collect: Dejan's existing
  DRC/prep Templater templates.
- **Pre-beta slice 3 — Prebell-lite** (2–3 wks thin, then weekly iteration)
  Regime tiles, catalyst calendar, in-play candidates from existing scanner
  data. Fail-loud from line one.

## DESIGN SESSIONS (register — planning hard cap: two calendar weeks total)

- [ ] **1. Trading Taxonomy Session** — FIRST. Absorbs variable registries.
      Inputs: Setups & Trades xlsx, cheat-sheet library, Jure examples,
      Dejan's walkthrough. Outputs: canonical vocabulary + §6 amendment,
      playbook schema ADR, per-playbook variable registry (incl. ≥1
      human-only tape dot each). Unlocks: strategies.yaml redesign, setups
      engine, semaphore board.
- [ ] **2. Data-Model + Vault combined block** — one weekend, back-to-back.
      Outputs: data-model ADR + embedder ADR (both GATE the memory port),
      Mattermost DB-split final call (recorded position: SPLIT), vault
      structure (Karpathy write-time vs Jones query-time vs Obsidian
      linking), inbox-as-interface policy, lazy-migration scoping.
- [ ] **3. Data-Source Spike** — NOT a session; sprint-0's first Claude
      Code task. Deliverable: data-source verification memo — all ELEVEN
      Finviz export families fired end-to-end, intraday bars VERIFIED (not
      assumed), FMP pricing, TradingView MCP state. Blocks any Charter item
      depending on data sources.
- [ ] **4. Product Definition sittings** (timeboxed) — Day-in-the-Life →
      mission-control/semaphore/Trade-Radar mockups (prebell/DRC/RUBRIC
      refs; Moderna Day-2 worked example) → MoSCoW with forced subtraction
      → **MVP Charter** → sprint ladder re-derived. Validation = working
      pre-beta slices on live mornings, not static mockups. Charter must
      show capacity math, trader-metric success criteria, build/trade
      firewall, ~5-variable semaphore scope.
- [ ] **5. Rules Engine Session** — post-Charter; gates Guardian, not MVP.
      Rule schema (trigger/state/action-ladder/channel/window), authoring
      path (DM/voice → draft config → HITL-token activation; Cobalt may
      PROPOSE rules through the same gate), hot-reload, boundary vs
      playbook variables.
- [ ] **6. HITL rebuild** — spec already ratified; implementation sprint.

## PORT/BUILD CANDIDATES (unsequenced — Charter derives the ladder)

KEEP-AS-IS ports (through the test/config gate; see TRIAGE for riders):
- MemoryProvider ABC (only if new core wants the contract) · db_status.py
  (minus DEBUG dump) · tools/knowledge.py
- BrowserTool as fetch-primitive · live_run_{finviz,quote,dynamic} smoke
  scripts · FinvizApiClient (seed → grows config-driven across all 11
  export families) · MetadataEnricher (minus secret-dumping sink)
- Mattermost REST helpers + native WS loop (cache IDs) ·
  Proposal/IntentAlignment models · MATTERMOST_CREDS vault routing
- rules.yaml trading_rules · FinanceTool (stopgap; deprecated when FMP
  collectors land) · LLM routing class (+retries/timeouts/fallback/effort/
  cost capture) · config.yaml models/profiles/network · prompts.yaml
  (dead sections removed/wired) · dev_utils/test_routing.py
- Filesystem tools + jail · CobaltSettings core · VaultManager ·
  manage_vault.py · docker-compose · generate_context.py
- cobalt.sh (KEEP-CONCEPT: PID/health/dev-prod awareness)

KEEP-CONCEPT / REBUILD (old code as spec):
- PostgresMemory core (conn factory, DDL-once, embeddings via routing) ·
  HITLProposalStore (per HITL spec) · init_5_pillar_schema (guarded)
- Domain whitelist · vault credential injection · ScannerOrchestrator +
  scanners.yaml (prime MVP-pillar-1 organ) · SemanticTagger + themes
- ProposalEngine live methods · DANGEROUS_TOOLS → risk-tiered capability
  classes
- Strategos · Playbook (one validated reader + registry) · rules.yaml
  cortex_routing · daily_in_play writer (never-built pillar-1 terminus)
- Cortex classification (deterministic, T=0) · OrchestratorEngine (one
  chief-of-staff) · BaseDepartment (one loop, one grammar) · PromptEngine
- Scribe (blocked by Vault Session) · obsidian_vault_path ONE resolver ·
  CobaltScheduler (timezone-correct, jobs in YAML) · launchd plists into
  ops/ + supervision · wipe/reset utilities (prod guards, never as-is)

NEW BUILDS (named requirements):
- Authenticated persistent browser sessions (smbtraining, SMB realtime
  board, FinancialJuice): persistent context, days-to-weeks unattended, no
  keep-alive, credential-refresh flow, logged-out = typed failure + LOUD
  alert, drift = alert + redesign.
- Grading/EV/sizing engine (spec: §6 + ASET sizer + Opportunity Framing
  xlsx; slice 1 is its first sliver) · Priority setups engine (dependency:
  intraday bar source VERIFIED at Spike) · Briefing engine (ONE, prebell
  model, both old paths die) · In-play rules as deterministic function over
  typed snapshots.

REDESIGN (blocked on session/ADR): 5-pillar schema + dual hitl_proposals
DDL (Data-Model Session) · embedder ADR · memory/browser/HITL/scribe/
scheduler/strategy tests · strategies.yaml schema (Taxonomy) · approval
interceptor (HITL spec) · supervision/out-of-band alerting · keys: alias
block → direct vault naming · .env/DATABASE_URL two-phase boot ·
Cortex._run_ops routing · 0-Inbox policy (inbox = interface).

## GATED (post-MVP)

- **Guardian sprint** — gates: grading/EV live + alerting + Rules Engine
  session. Content: real-time enforcement of the Guardian rule set
  (TRIAGE: 7 rules; live as DRC checkboxes until then); rule deactivation
  during market hours requires HITL token + cooling delay. Includes
  **trade-awareness spike**: read-only DAS log tail vs quick voice/DM
  trade logging — §3 boundary (no platform integration, no execution)
  absolute.

## STANDING FOLLOW-UPS

- [ ] COBALT-REQUIREMENTS.md §6 vocabulary amendment — after Taxonomy
      Session.
- [ ] Persona strings + vault-seeder content harvested as reference/intent
      history before any old-tree deletion commit.
- [ ] Collect Dejan's existing Obsidian DRC/prep Templater templates
      (slice-2 prefill input).
- [x] TRIAGE.md committed to docs/assessment/ (2026-08-24).
- [x] New reference artifacts in docs/references/ + INDEX entries; licensed
      PPTX local-only under gitignored assets/ (2026-08-24).
- [x] CLAUDE.md "Current phase" rewritten for build phase (2026-08-24).

## DONE

- Assessment passes 0–8 + ASSESSMENT.md synthesis (2026-08-21/22).
- Path-jail hotfix (06-H1) (2026-08-22).
- docs/references under version control; Finviz token rotation recorded
  (2026-08-22/24).
- TRIAGE ruling session → TRIAGE.md (2026-08-22).
