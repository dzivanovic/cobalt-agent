# BACKLOG.md — Cobalt kanban + backlog

Source of truth for work state. Derived from docs/20 - Assessment/TRIAGE.md
(ruled 2026-08-22). Dispositions live THERE; this board only tracks
sequencing and progress. Sprint ladder below the pre-beta lane is NOT
locked — the MVP Charter re-derives it.

Update rule (CLAUDE.md): keep this board current as you work; move cards,
don't duplicate them.

---

## INCIDENT LOG

- **2026-08-25 — prod agent down, misdiagnosed as strangler-boundary
  leak.** Actual root cause: `mattermost` container's baked
  `MM_SQLSETTINGS_DATASOURCE` env var (docker-compose substitutes
  `${POSTGRES_PASSWORD}` from `.env` at container CREATE time) went
  stale after the Postgres password rotation on 2026-08-24 — the
  container was never recreated, so it kept the old password, degraded
  to `Database Status: UNHEALTHY`, and the agent's Mattermost login
  failed ("Invalid or expired session"). Coincided in time with the
  ASET/role-pack commits but was unrelated — confirmed no import
  crosses src/cobalt_agent/ ↔ src/cobalt/, and the old config loader's
  glob (`configs/*.yaml`, non-recursive) never reaches `configs/dev/`.
  Fix: `docker compose --profile core up -d --no-deps mattermost`
  (recreate only, re-substitutes current `.env`) — no code or config
  moved. Also killed an orphaned pre-incident agent process (untracked
  by the PID file, running since 2026-08-21) before the clean restart.
  Standing rule from this: recreate `mattermost` (and any other service
  reading `${POSTGRES_PASSWORD}`-family vars) after every Postgres
  password rotation — `docker restart` alone does not re-read `.env`.

## NOW (in build)

- **Pre-beta slice 1 — ASET semi-auto sheet** (days)
  Deterministic sizing engine in src/cobalt/: daily stop = account ÷ 50;
  grade→risk A+ 80% / A 30% / B 15% / C 5% / D-SAW 0%; entry/stop/direction
  → risk $ + shares. Grade and stops always Dejan's input; prefill last
  price via FinvizApiClient path. Every sizing persisted to Postgres
  (cobalt_dev; table may be reshaped by data-model ADR). Surface: simplest
  working local form (trade-reporter Flask pattern). Fail-loud. Tests +
  smoke. Spec: docs/90 - References/aset_daily_position_sizer.html +
  Daily_Stop_Model_Card.pdf. Gate: stop and show Dejan the working sheet.
  STATUS 2026-08-25: iteration 2 live (broker hard cap $430 enforced,
  auto-prefill on ticker tab-out, entry prepopulation, grade default B,
  LONG/SHORT toggle, append-only Save-to-Daily-Note with git-ignore
  safety gate). Awaiting Dejan review.
  STATUS 2026-08-25 (cont.): server bind is config-driven
  (configs/dev/aset*.yaml server.bind: loopback|lan); Dejan's local
  config now runs "lan" so the Windows trading PC (same home network,
  not Tailscale) can reach it — reachable URL(s) print on startup.
  Prefill token issue resolved (Finviz token in the vault now valid;
  prefill confirmed live during the 2026-08-26 smoke test).
  STATUS 2026-08-26 — vault-path migration: real Obsidian vault is now
  /Users/cobalt/Vault/Think (config: configs/dev/vault.yaml, resolver:
  src/cobalt/vault.py — TRIAGE 2.6's ONE resolver, new-core only, old
  tree's four-way ambiguity untouched). Save-to-Daily-Note now targets
  "1 - Trading/1- Daily Notes/YYYY-MM-DD.md" under that root; the
  git-check-ignore safety gate is retired — replaced by an "outside the
  repo working tree" check, which is now the actual safety property
  (the vault is genuinely outside the repo, not just gitignored inside
  it). Stub-with-banner on a missing note added. Smoke-tested end to end
  into the real vault (card landed in today's real daily note).
  Old playground-vault writes (docs/0 - Inbox) retired, left as-is —
  **flagged, not migrated**: two test ```aset cards from prior smoke
  tests sit in docs/0 - Inbox/2026-08-25.md (both ticker MRNA, fake
  sizing data) — not real trades, not auto-migrated into the real vault
  to avoid injecting synthetic entries into Dejan's real trading record.
  Dejan: delete, ignore, or say if you want them ported by hand.
  Backlogged follow-on (do not build yet): ticker field autocompletes
  from the daily in-play list once that pipeline exists; non-list
  tickers show an inline "not in today's in-play list" note (no popup),
  still allowed. Access token for the LAN-bound sheet (currently
  unauthenticated by design/acceptance, see server.bind config comments).
  STATUS 2026-08-27 — iteration 4, sizing-model replacement (ruled by
  Dejan): daily-stop x grade-percentage model RETIRED — replaced by
  fixed-dollar-per-grade sheet mode (FULL/HALF), mirroring Dejan's DAS
  hotkey files exactly (configs/cobalt/aset.yaml: full A 135/B 60, half
  A 70/B 30). Grade selector now offers only A and B (the only
  sheet-mode-tradeable grades); C/D still fail loud server-side as
  "not tradeable" if they ever reach compute_sizing, rather than
  computing a meaningless size — dropdown just never offers them.
  "Compute & persist" now ALSO appends the card to the daily note in the
  same action (the separate Save button and POST /note route are gone —
  a card that isn't in the journal didn't happen). A new "actual fill"
  field recomputes shares at the real fill price (same grade dollars,
  same stop) and appends a linked FILL UPDATE block to the note
  (>=25% distance change vs. the planned card shows a visible, non-popup
  "stop may no longer be structural" warning) — both the original card
  and every fill update stay in the audit trail. broker_hard_stop and
  daily_stop_default retired from AsetConfig (account_size kept for the
  future 1%-of-account computed mode). New migration
  0002_aset_sizings_sheet_mode.sql (sheet_mode added, daily_stop/risk_pct
  dropped); AsetStore.ensure_schema() generalized to run every
  migrations/*.sql file in order (strips full-line -- comments before
  splitting on ';' — psycopg executes one statement at a time). All
  tests updated and green (engine/config/daily_note/store, incl. the
  live Postgres roundtrip). Live-smoke-tested end to end against the
  real vault: full-mode B card computed, persisted (id 73), and
  auto-appended; a 40c-away fill recomputed cleanly with no warning
  (12.75% distance change); a second, larger fill correctly triggered
  the structural warning (134.90% distance change) and appended its own
  linked block; HALF-mode server-side dollar switch verified (B -> $30,
  correct per config) via direct POST. One piece NOT live-browser
  verified: physically clicking the FULL/HALF toggle button in this
  session's browser-automation tool — click delivery failed to reach
  the button (elementFromPoint confirms correct hit-testing; the same
  failure reproduces on the pre-existing LONG/SHORT toggle in a fresh
  tab, so it's a session/tool-level issue, not new-code regression);
  setMode()'s client logic was verified directly (correct $ hint
  swap) and the server-side compute path was verified by direct POST.
  Dejan: please do one real click of the FULL/HALF toggle by hand to
  close this out. Leftover: a TESTHALF row (id present, ticker
  TESTHALF) landed in cobalt_dev and one TESTHALF card landed in
  today's real daily note from that verification POST — flagged, not
  deleted (same policy as the earlier SMOKETEST/TESTARCH leftovers).
  Old percentage-model code (GRADE_RISK_PCT, enforce_broker_cap,
  daily_stop_from_account, temp_prefill_daily_stop) deleted outright,
  not deprecated in place — one-path rule. DevDocs for the seven
  touched/new files (models/engine/config/store/daily_note/web.py +
  the new migration and configs/cobalt/aset.yaml) are now stale and
  still need regenerating.

## NEXT (immediate lane, in order)

- **Pre-beta slice 2 — DRC + PlayBook prefill** (~1–2 wks)
  Prefill-first inversion of docs/90 - References/trade-reporter/ (keep its
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

- [ ] docs/00 - Project/COBALT-REQUIREMENTS.md §6 vocabulary amendment —
      after Taxonomy Session.
- [ ] Persona strings + vault-seeder content harvested as reference/intent
      history before any old-tree deletion commit.
- [ ] Collect Dejan's existing Obsidian DRC/prep Templater templates
      (slice-2 prefill input).
- [x] docs/50 - Roles/ role-pack template + MODELS.md fleet tiering seeded
      (2026-08-25): planning=Fable, coach=Fable, DRC=Sonnet,
      logistics=Sonnet; promotion rule = model follows function.
- [x] TRIAGE.md committed to docs/20 - Assessment/ (2026-08-24).
- [x] New reference artifacts in docs/90 - References/ + INDEX entries; licensed
      PPTX local-only under gitignored assets/ (2026-08-24).
- [x] CLAUDE.md "Current phase" rewritten for build phase (2026-08-24).

## DONE

- Assessment passes 0–8 + ASSESSMENT.md synthesis (2026-08-21/22).
- Path-jail hotfix (06-H1) (2026-08-22).
- docs/90 - References under version control; Finviz token rotation
  recorded (2026-08-22/24).
- Docs restructure to the D6 standard: docs/ reorganized into
  00 - Project / 10 - Decisions / 20 - Assessment / 30 - Design /
  40 - DevDocs / 50 - Roles / 90 - References / _archive; playground
  vault (0 - Inbox, 0 - Projects) untouched, out of scope (2026-08-26).
- TRIAGE ruling session → TRIAGE.md (2026-08-22).
