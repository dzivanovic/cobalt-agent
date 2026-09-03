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

- **2026-09-03 — morning prefill silent, root cause: launchd's
  posix_spawn does not resolve a bare program name via the job's own
  EnvironmentVariables PATH.** `com.cobalt.prefill-daily.plist` fired on
  schedule (05:15) and `com.cobalt.prefill-drc.plist` the evening before
  (09-02 15:40) — both loaded, both exited immediately with `78:
  EX_CONFIG` and ZERO stdout/stderr, no alert. Confirmed by an isolated
  diagnostic LaunchAgent: bare `uv` as `ProgramArguments[0]` reproduces
  the exact signature (exit 78, empty logs); an absolute path exits 0.
  The 08-31 "fix" (see the slice-2 entry below) that replaced the
  plists' wrong hardcoded `/opt/homebrew/bin/uv` with a bare `uv`
  (modeled on `ops/start_aset.sh`'s pattern) was never exercised
  end-to-end — the plists sat uninstalled from 08-31 until this
  session — so the fix's own flaw went undetected: `start_aset.sh`'s
  bare `uv` works because bash's own shebang does the PATH search
  before `exec`ing it; a bare name directly in a plist's
  `ProgramArguments` has no shell in front of it, and launchd's
  posix_spawn does not reliably do that search itself.
  `com.cobalt.archiver.plist` carried the ORIGINAL wrong-hardcoded-path
  bug (`/opt/homebrew/bin/uv` doesn't exist on this machine) and was
  also not loaded at all. Fix: all three now use the absolute
  `/Users/cobalt/.local/bin/uv`, installed and verified (see
  `docs/40 - DevDocs` / ops session recap for the day). **Standing
  rule:** any `ops/*.plist` `ProgramArguments[0]` that invokes a binary
  directly (not through a wrapper script's own shebang) must be an
  ABSOLUTE path — a bare name is a launchd footgun regardless of what
  `EnvironmentVariables.PATH` says. See the heartbeat-probe follow-up
  below.

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
  touched/new files regenerated and committed (b032691).
  STATUS 2026-08-27 (cont.) — config completion, same-day follow-up
  (ruled by Dejan): configs/cobalt/aset.yaml's grade ladder extended to
  the FULL truth — A_plus/A/B/C/D dollar figures per sheet mode (full A+
  345/A 135/B 60/C 21/D 0, half A+ 170/A 70/B 30/C 11/D 0; A/B unchanged,
  match the .htk files; A+/C derived from the canonical ASET percentage
  map at current bases; D always $0, enforced by a Pydantic field
  validator, not just convention). UI/compute availability split into a
  separate enabled_grades: [A, B] field. TRADEABLE_GRADES (the hardcoded
  models.py constant) is gone — engine.compute_sizing now takes
  enabled_grades as an explicit argument, so enabling a grade later is a
  config edit only; a new test (test_enabled_grades_is_config_driven_not_hardcoded)
  proves this by swapping which grades are enabled and watching the
  refusal follow the config, not the code. Grade dropdown now lists all
  five grades; A+/C/D render as disabled <option>s with a suffixed label
  ("reserved" / "no trade (SAW)") — greyed, structurally unselectable via
  the native dropdown, and refused server-side too if bypassed by a
  direct POST. All tests green (incl. live Postgres roundtrip). Live-
  smoke-tested: full-mode B computed unchanged ($60 budget, 60 shares);
  direct POSTs for C, A+, and D all correctly refused ("not enabled ...
  no trade (SAW)") and wrote nothing to Postgres or the daily note.
  DevDocs regenerated for models/engine/config/web.py + their tests.

- **Pre-beta slice 2 — DRC & Daily prefill engine** (src/cobalt/prefill/)
  Templates-as-config: Daily.md + DRC.md ported to Jinja
  (configs/cobalt/templates/*.md.j2), structure/section names verbatim,
  Templater `{{ }}` prompts replaced by prefilled fields. Guardian rule
  set unified into configs/cobalt/rules.yaml (the vault's own Rules.md
  "THE 12 RULES" + Daily.md's uncovered lines, quoted verbatim) — the
  single source for the morning rules block, the rule-adherence
  checklist, and (later) Guardian's own enforcement. Morning Daily Note
  (`uv run prefill daily`, scheduled 05:15 ET weekdays): SPY/QQQ/IWM via
  the confirmed Finviz /export/screener v=111; VIX/BTC render "n/a
  (manual)" loudly (neither is Finviz-servable); today's economic +
  earnings calendar via /export/calendar; day-mode checkbox line;
  rule-adherence checklist. Trade notes: every computed ASET card now
  also creates/updates "1 - Trading/2 - Trades/<Trade-...>.md" (wired
  into web.py's /size handler) so the daily note's dataview table lights
  up — Cobalt owns 5 frontmatter keys only, everything else (strategy,
  RVOL, exit, P&L) stays his, preserved verbatim on any re-run. Evening
  DRC (`uv run prefill drc`, scheduled 15:40 ET): per-ticker
  Catalyst/Set-Up/Trade scaffold from the day's cards (AsetStore.for_date,
  America/New_York boundary), re-entry-rule prompts (#2 needs written
  info, #3+ stands down), excitement-audit question on reversion-tagged
  strategies (configs/cobalt/strategies.yaml, seed list), Risk Parameters
  from today's actual sheet mode. PRINCIPLE enforced throughout:
  create-if-absent from template, else append a fenced, idempotency-
  marker-guarded "Cobalt Prefill" block — existing content never read
  for mutation. 131 tests (incl. Postgres integration for the new
  AsetStore.for_date). STATUS 2026-08-31: shipped + smoke-tested against
  the real vault — today's Daily Note (append path, since Templater had
  already created it), a trade note backfilled from a real card computed
  before the wiring landed, and a DRC draft from today's real cards (no
  Friday 08-28 cards existed in cobalt_dev to use as the spec'd smoke
  case — substituted today's date; flagged, not silently swapped).
  Known gaps, not closed this sprint: DevDocs for the new tests/cobalt/
  test_prefill_*.py files (skipped — src/cobalt/prefill/*.py DevDocs are
  complete); the two new launchd plists are committed to ops/ only, NOT
  installed to ~/Library/LaunchAgents — Dejan's call, needs a real
  05:15/15:40 unattended run to fully verify before relying on it.
  STATUS 2026-08-31 (cont.) — **Slice 2.1 correction**, from Dejan's
  review of the first live note: fill-IN-PLACE inside his actual
  sections replaces the old append-a-block-below-everything design.
  rules.yaml is now GENERATED from the vault's Rules.md (not hand-
  authored) — Rules.md migrated once (each of the 12 lines got exactly
  one trailing Obsidian tag, `#process/#sizing/#time_window/#re_entry/
  #circuit_breaker/#hard_stop`, text otherwise verbatim); Daily.md's old
  Trade Rules list dropped as a source entirely (ruled outdated 08-23,
  the six merged lines are gone); rules.yaml regenerates on every
  prefill run (daily AND drc) and fails loud naming the exact line if a
  tag's missing/wrong/duplicated. The 12 rules render exactly once, as
  a single tagged checkbox list — no more separate "Guardian rules" +
  "Rule adherence" split. Sizing rule (#2) is mode-aware at render time:
  content-detected splice (not tied to rule position) pulls "B = $30
  half / $60 full, A = $70 half / $135 full" straight from ASET's own
  sheet-mode config. Daily template rebuilt with three named Cobalt
  slots (rules/trading/market_calendar), each wrapped in its own
  `<!-- cobalt-slot:NAME -->` marker; an existing note gets per-slot
  editing (marker present → skip; blank/prior-FAILED → fill + mark;
  Dejan's real content already there → skip, report, no mark) instead
  of a bottom-of-file append. Trading table: SPY/QQQ/IWM only, per-row
  fill/skip; VIX/BTC always blank (no more "n/a (manual)" text — same
  table, no second table). A missing anchor (note doesn't match the
  expected shape at all) fails the WHOLE run loud rather than guessing
  an insertion point — edit plan built in memory first, so a failure
  never leaves a half-edited file. Validated against a copy of the real
  08-31 note in a new outside-repo dev vault (~/dev-vault-cobalt, not
  Dejan's real one) — confirmed idempotent, confirmed his hand-filled
  Trading row survives untouched, confirmed the blank Market Calendar
  slot fills correctly even though the rules slot inserts ahead of the
  OLD template's still-present stale Risk Profile prose (that prose
  itself is untouched — only the Jinja template used for fresh notes
  dropped it; Dejan's own Templater file at 5 - Templates/Daily.md was
  NOT touched, so a Templater-created note still carries it until he
  updates that file himself). Both prefill launchd plists' hardcoded
  /opt/homebrew/bin/uv fixed to a bare `uv` (same bug as archiver/
  mainframe, ops/README.md) — still not installed. 19 rewritten daily
  tests + 13 new rules-generator tests + a real DRC test-isolation bug
  found and fixed along the way (drc.py's tests were silently reading
  the REAL vault's Rules.md via an unpatched import binding — now
  patched, and a regression assertion added). 148 non-integration + 5
  integration tests green.

## NEXT (immediate lane, in order)

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

- [ ] Heartbeat probe: "every ops/ plist expected loaded is loaded" —
      `launchctl print gui/$UID/<label>` for each committed `ops/*.plist`,
      red + DM alert if a shipped job isn't bootstrapped. An uninstalled
      schedule is a silent failure by construction (this is how
      `com.cobalt.archiver` sat unloaded and the prefill plists sat
      uninstalled from 08-31 to 09-03, unnoticed). Note from the 09-03
      incident (see INCIDENT LOG): loaded-state alone is not sufficient
      — both prefill plists WERE loaded and still failed silently at the
      launchd spawn level (exit 78, no output). The probe should also
      compare each job's `last exit code` against 0/"never exited" and
      alert on a nonzero code, not just on not-loaded. Thin heartbeat
      lane (PROJECT-LEDGER 08-29/31).
- [ ] docs/00 - Project/COBALT-REQUIREMENTS.md §6 vocabulary amendment —
      after Taxonomy Session.
- [ ] Persona strings + vault-seeder content harvested as reference/intent
      history before any old-tree deletion commit.
- [x] Collect Dejan's existing Obsidian DRC/prep Templater templates
      (slice-2 prefill input) — found already in the vault's own
      5 - Templates/ (Daily.md, DRC.md, Individual Trade Template.md,
      TRADE REPORT CARD.md), ported to Jinja 2026-08-31.
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

## Taxonomy replay validation (v0.7 §13/§13.1)

Superseded 2026-09-02 (v0.7 schema v0.4 commit): the itemized list this
section used to carry is now a query, not a hand-maintained list
(v0.7 change log #19 — "Tunable slot"). Every `config, dynamic`
quantity (v0.6/v0.7 §0 "Dynamic definitions" law) is a row in
`configs/cobalt/taxonomy/tunables.yaml`
(`src/cobalt/taxonomy/tunables.py`'s `TunableRow`); the backlog is
`tunables.replay_backlog(registry)` — every row with `dynamic: true`
and `status != solidified` — surfaced by
`python -m cobalt.taxonomy.validate`'s summary line and covered by
`tests/taxonomy/test_trade_defs.py::test_dynamic_tunables_appear_in_replay_backlog`.
Corpus for every row: the Bar Archiver's minute-bar history
(`src/cobalt/archiver`, `configs/cobalt/watchlists.yaml` tickers). Pass
criterion is **TBD at n≥30** per row until a replay session sets it and
writes `status` (never `value` — a value change stays a Dejan ruling).

30 rows seeded at the v0.7 commit, all `replay_pending` or `proposed`
(none `solidified` yet) — read `tunables.yaml` directly for the current
set; do not re-duplicate it here.
