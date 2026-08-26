# COBALT-REQUIREMENTS.md
Single source of truth for the Cobalt Trading Agent rebuild.
Owner: Dejan · Status: approved 2026-08-21 · Supersedes all prior drafts and addendums.

---

## 1. Purpose

Cobalt is Dejan's trading wingman: a local-first, multi-agent system that runs
morning scans, identifies stocks in play per his rules and strategies, monitors
the market in real time, alerts him when one of his setups appears, grades the
opportunity, calculates expected value, and recommends size — so he takes the
trade himself, on time and sized correctly. It additionally automates research,
journaling, review cadences, and coaching, and continuously proposes
improvements to his trading logic.

Trade execution is manual and permanently out of scope.

The future of Cobalt is bigger than a day-trading copilot: swing trading and
options are coming, and the architecture must absorb them without rework.

## 2. Problem statement (why Cobalt exists)

- Bandwidth: he reacts to Scalp Radar alerts, the SMB position board, or a
  setup he *thinks* he sees, then executes without fully analyzing all factors
  or sizing correctly; missed variables change outcomes.
- Attention: he can concentrate on only 1-2 tickers and misses the right moves
  elsewhere.
- Psychology: deadline pressure and FOMO trick him into seeing trades that
  aren't there; revenge-trading pressure follows.
- Discipline systems he knows he needs but abandoned due to friction:
  automated backtesting, continuous databasing of setups and charts,
  journaling, forced systematic thinking, methodical coaching, continuous
  documentation in Obsidian.
- Friction removal is the core design principle: automation must eliminate the
  manual steps that caused good practices to be abandoned.

## 3. Hard boundaries

- Cobalt must NOT integrate with or ever touch trading platforms (DAS Trader
  Pro, Lightspeed, TradeStation, CenterPoint Securities). Read-only awareness
  of what is happening on them is acceptable.
- No trade execution, ever.
- Zero-trust security. All system-risky or trading-risky actions pass through
  the tokenized human-in-the-loop (HITL) approval pattern.
- Minimal to no hallucinations — this system runs against live accounts.
  Extracted figures require verbatim source quotes (see §8 Tier 1).
- The trading pipeline (morning briefing, game plan, alerts, reviews) works
  through Obsidian only — never Gmail/email.
- Vault contents and other gitignored material must never reach GitHub.

## 4. Architecture principles

- Mission control + background swarm: a chief-of-staff orchestrator invoked by
  voice, DM (Mattermost), or Obsidian task notes; it dispatches specialist
  agents.
- Tools fetch, agents reason: no LLM calls a data source directly.
  Deterministic Python collectors fetch and cache; LLMs operate on cached,
  validated data. All numeric computation (ratios, indicators, surprise math,
  grading arithmetic) is deterministic code.
- Local-first: own the data, server, bots, and tokens. Cloud models only for
  genuinely hard analysis.
- Anti-rigidity: agents, tiers, fields, and prompts are config-driven
  (configs/ + prompt files), modifiable on the fly. Adding a mode (swing,
  options) is a config block and a template, not a refactor.
- Obsidian is the system of record. Cobalt sits on top and automates
  ingestion. Mission-control front end: Obsidian-durable + thin real-time web
  panel over Tailscale (command center as a custom Obsidian plugin).
- Every LLM call is hot-swappable (LiteLLM routing).

## 5. Agent pod

- Orchestrator (chief of staff): routes triggers, invokes specialists,
  communicates via voice/DM/CLI.
- Premarket agent: morning scans, game prep, market context (incl.
  vitalknowledge.net podcast transcript ingestion, multi-LLM market summary
  automated into the morning day plan; prebell.laldinsoft.com is the model to
  copy and adapt — all tabs matter).
- Real-time analysis agent: stocks in play through the day, setup alerts,
  quick ASET-protocol assessment, take/no-take with EV and sizing.
- Research Analyst agent: fundamental + technical research engine (§8).
- TradingView watchlist agent: every evening after the close — add/move
  tickers to watchlist sections, high-level TA, levels for next day, morning
  report. (Detailed spec to be elaborated during/after code review.)
- News agents: FinancialJuice Elite (incl. squawk audio), X monitoring
  (followed accounts, windowed 4 AM-4 PM ET; news/TradingView tasks run
  around the clock), TradingView news, Finviz Elite news. Playwright scraping
  where no API/MCP exists.
- Scribe: writes to the Obsidian vault. Must be rebuilt flexible (current
  version is rigid) against the redesigned vault (INFRA-2).
- Coach agents: force the daily report card with least friction; review the
  day's setups/trades (right/wrong per setup, what to work toward); set goals
  for next day/week; hold him accountable.
- Cadence reviews (automated): end-of-day + next-day prep, end-of-week +
  next-week prep, end-of-month, end-of-year.
- Coding agent: Claude Code, with delegation of simple coding tasks to the
  local model per the tiering rules (§10).

## 6. Trading logic requirements

- Priority focus setups (all bidirectional long/short): Scalp Radar 5 + 9 EMA
  continuation, VWAP Continuation, Bouncy Ball, Big Dog. For each: automated
  continuous backtesting; current EV per trade conditioned on prevailing
  market regime; ongoing collection of live examples; support for building
  and internalizing his personal playbook.
- ASET daily position sizer (recreate and automate): opportunities start at
  grade D (no trade) and earn upgrades via a weighted-variable voting model
  (level significance 1-10, regime, internals, setup criteria, ...). Grade
  maps to risk as % of daily stop (C 5% ... B 15% ... A/A+ higher). Cobalt
  computes grade and EV itself and tracks all variables dynamically like
  traffic signals, catching what he misses in the moment.
- Oura-derived A-D morning readiness scorecard as an input to raising or
  lowering the daily stop-loss limit.
- Post-trade analysis: continuously suggest whether modifying variables would
  raise profit potential; flag when a strategy is decaying in current regime
  and should be sized down (or up).
- Self-learning scope: the system continuously PROPOSES improvements
  (regime-conditional EV updates, weight tweaks, decaying-strategy flags);
  every change to trading logic passes through the HITL approval token.

## 7. Data sources

- EDGAR official SEC APIs (free): XBRL company facts, submissions, full-text
  search, real-time 8-K / S-3 / 424B monitoring.
- FMP (paid tier — verify pricing at sprint start): fundamentals, ratios,
  EPS/revenue history, consensus estimates, earnings calendar and surprises,
  float/share structure, insider transactions.
- Finviz Elite: scanners (functional today), news, single-stock up-to-the-
  minute OHLC bars (re-verify volume availability).
- TradingView: real-time feed via account access (MCP preferred; verify),
  charts, alerts, watchlists.
- Polygon: too expensive for now; upgrade once profitable.
- News: FinancialJuice Elite (incl. squawk audio), X, TradingView news,
  Finviz Elite news.
- Education: SMB Discord + SMB training videos (platform-locked; semi-
  automatic screen capture accepted, unattended where possible) → NotebookLM.
- Storage: structured facts in Postgres; filing/press-release text chunked
  into pgvector alongside the existing 5-pillar memory schema. Fetch once,
  cache, re-query free.

## 8. Research engine (fundamental + technical)

Purpose: fully automated research on any stock — zero manual work. Agents
collect, compute, extract, synthesize; Dejan only consumes output.

Triggers: (1) ticker enters watchlist or goes in-play; (2) evening
TradingView agent run; (3) on-demand voice/DM command ("research TICKER").

Model routing: collection = tool layer (no model); extraction = local model
(filing-section summaries, catalyst tagging, guidance extraction → structured
JSON against Pydantic schemas); synthesis = cloud analyst tier (research
note: bull/bear, catalysts, dilution risk, key levels, EV-relevant flags) —
only for names that matter, never whole-market. 3 failed schema validations →
escalate one model tier.

Output: research note filed by the scribe into the vault; structured facts
into Postgres; consumed by morning game plan, grader/EV, TradingView agent.

### Tier 1 — Day trading (build now)
- Share structure and float; dilution risk: effective S-3s/ATMs, recent
  offerings, warrant overhangs, lockup expiries.
- Cash runway (smallcaps); short interest and borrow; halt/SSR status.
- Insider transactions; institutional ownership concentration.
- Catalyst calendar.
- Earnings-event package (critical — earnings drive full reversals):
  - Triple-beat matrix: EPS vs consensus, revenue vs consensus, guidance vs
    consensus — each beat/inline/miss, composed into a classification
    (single/double/triple beat, plus mixed reversal-prone cases such as EPS
    beat + guidance cut).
  - Guidance extraction: guidance lives in press-release/call prose →
    local-model extraction with Pydantic validation; every extracted guidance
    figure MUST carry a verbatim source-quote field. No quote, no number.
  - Reaction context per ticker: historical earnings gap size, fade vs
    follow-through tendency, reversal tendency.
  - Timing: BMO/AMC, call time; consensus snapshot captured pre-print.

### Tier 2 — Swing (design now, build later)
Multi-quarter growth trajectory, margin trend, guidance history, sector/peer
relative strength, analyst revision momentum, catalyst density over the hold
window, ownership flow trends. Same collectors, longer lookbacks, one new
synthesis template.

### Tier 3 — Options (design now, build last)
IV rank/percentile, term structure, skew, expected move vs historical
earnings moves, open interest / unusual flow. Requires a new data source
(Tradier / Polygon / Unusual Whales class — decision deferred). Pydantic
schemas include optional options fields from day one.

### "Why is this ticker moving?" resolver
1. RESOLVER (deterministic, internal-first, sub-second to seconds): on any
   anomaly alert, check Cobalt's own stores in order — fresh filings →
   earnings window → news cache → X hits → halt/SSR → sector sympathy
   movers. Local model composes a one-paragraph answer with internal
   citations. This beats any web-search API on breaking events (squawk/X
   land before web indexes).
2. FALLBACK (only when the resolver is empty): retrieval-only web search API
   (Perplexity Search API ~$5/1k requests, or Brave/Exa/Tavily class —
   verify pricing at pilot), synthesized by the LOCAL model. Full Sonar
   synthesis optional, not required. Note: Perplexity's finance-data edge is
   its consumer app; Cobalt goes direct to the same sources (FMP, EDGAR).
Both stages hot-swappable behind the LLM routing layer.

## 9. Voice and interface

- Communication: DM (Mattermost over Tailscale), voice, CLI.
- 3-tier local voice stack: faster-whisper STT → small local router model →
  Tier 1 skill execution / Tier 2 instant answers from existing reports /
  Tier 3 headless Claude Code → Kokoro TTS. Hotkey works tabbed-out.
  Trading-logic Tier 3 behind HITL. Wake-word listening must be free, open
  source, fully local; device-handoff (active device takes over, others
  stop).
- Vault-as-map: index.md TOCs per folder; structure documented in CLAUDE.md.
- Skill discovery: dictation + Claude Code log mining, with
  skill → proven → automation promotion.
- Command center: custom Obsidian plugin built by Claude Code (Claude Design
  mockups, hot-reload). Thin Tailscale channel retained for sub-second
  strike alerts to the trading PC.
- Latency targets: sub-second for alerts, news, grading, sizing, EV would be
  ideal; seconds is acceptable for his setups.

## 10. LLM routing and model tiering

- Hybrid, hot-swappable (LiteLLM): smart orchestrator (Claude/Grok/GPT) →
  strong analyst tier when needed → local model for mundane/repetitive/
  high-volume tasks. If cloud is down or tokens exhausted: local handles
  everything with a big red caution flag on the front end.
- Local inference: Qwen3.8-27B dense, 8-bit MLX, MLX-native MTP speculative
  decoding (MTP drafter adapter), parallel slots enabled, per-call
  reasoning_effort tuning (default xhigh overthinks — triage calls run with
  thinking off/low). One model, two personalities; no sidecar model unless
  measurement later shows triage queuing behind reasoning jobs.
- Claude-session tiering: Fable 5 for assessment, architecture, and planning
  sessions; Opus for heavy implementation; Sonnet/Haiku for mechanical work;
  local model for gruntwork. The 3-tries rule (§11 #13) governs escalation.
- Cross-ecosystem honesty: if a task is better served by Grok/GPT/Gemini,
  say so and let Dejan choose.
- YouTube pipeline: Gemini ingests/understands YouTube natively → hands off
  to Claude (chief of staff) to route for analysis/filing.

## 11. Non-negotiables

1. Zero-trust security with the tokenized HITL approval pattern.
2. Python-first architecture.
3. Pydantic required.
4. Hybrid LLM (local + cloud), hot-swappable.
5. Voice control.
6. Code testing and architecture review after every sprint; ADRs per
   decision; PDD per module/feature; a human-readable DevDocs wiki file per
   .py file, generated by Claude Code at sprint close (the only per-file
   artifact).
7. Running backlog and kanban board, always current; no massive codebase
   before testing and approval.
8. Continuous git and GitHub commits.
9. Postgres database.
10. Communication via DM, voice, and CLI.
11. Logging with log rotation.
12. Self-learning system that PROPOSES improvements; all trading-logic
    changes behind the HITL token.
13. No runaway coding sessions: every model (local or low-level cloud) gets
    3 tries on a task before flagging a higher-level model to take over.
14. Token conservation: honest per-task assessment; route to local or lesser
    models when appropriate; top models only when needed.
15. Honest cross-ecosystem assessments (Grok/GPT/Gemini when genuinely
    better).
16. Continuous working condition: production Cobalt is never broken by
    development. Sprints are sequenced by income impact (highest value
    first; usable functionality from sprint one). Each sprint only ADDS
    functionality on top of the running system: feature-branch development
    against the dev environment, sprint acceptance requires a full smoke
    test of ALL delivered functionality (not just the new feature),
    deploys are git-tagged with one-command rollback, and deployment
    happens outside market hours only.

## 12. Infrastructure tasks

### INFRA-0: Security remediation (BLOCKING — before any commit/push)
Shell history on the Mac exposed the COBALT_MASTER_KEY and the Postgres
DATABASE_URL (with password) in plain text.
- Rotate the master key and re-encrypt the VaultManager store; rotate the
  Postgres password; update .env accordingly.
- Purge the exposed lines from ~/.zsh_history after rotation.
- Secret-handling policy: secrets are never passed as command arguments or
  exported inline; manage_vault.py and all tooling read secrets via hidden
  input (getpass pattern) only.
- Verify .gitignore covers, at minimum: .env, logs/, __pycache__/, .venv/,
  data/ (the Postgres bind-mounted data directory lives INSIDE the repo at
  ./data/postgres), docs/Cobalt/ (the playground vault lives INSIDE the repo
  per configs obsidian_vault_path), and generated context dumps
  (cobalt_context.txt, cobalt_master_context.txt). Confirm with
  `git status --ignored` before the pre-assessment tag.

### INFRA-0.5: Environment-as-code capture
Production depends on artifacts outside the repo. Copy into a repo ops/
directory and keep current:
- ~/Library/LaunchAgents/com.cobalt.node-a.plist, com.cobalt.node-b.plist,
  com.cobalt.mainframe.plist
- ~/.lmstudio/start_mainframe.sh (serves the local model aliased
  "mainframe" — the endpoint Cline/Cobalt call)
Document the service map: docker-compose db = pgvector/pg16 on :5432
(restart always, profile core), pgadmin on :18080, Mattermost on :8065;
process management via cobalt.sh start/stop/restart/status.
Backup / disaster recovery (the Mac must be losable):
- Timing: the Postgres DB currently holds development data only — nothing
  worth saving yet. Backups are therefore NOT blocking today, but MUST be
  implemented and verified before Cobalt's first production use (gate: no
  live trading data may exist without a working backup).
- The Fedora laptop is old and not on 24/7 — it is NOT a backup target
  (manual ad-hoc copies by Dejan only, as a bonus, never the plan).
- Destination 1 (whole host): external SSD attached to the Mac, Time
  Machine.
- Destination 2 (off-site, critical set): encrypted cloud copy of the
  VaultManager blob + nightly pg_dump, via restic/rclone to Backblaze B2 or
  Google Drive (Google ecosystem already in use) — dumps encrypted at rest
  (the vault blob already is; encrypt pg_dump with age/gpg or restic's
  native encryption).
- New master key stored in a password manager plus one offline copy — never
  only on the Mac. (This part is NOT deferred — it happens at INFRA-0 key
  rotation.)
- Code is off-site via GitHub; the live Obsidian vault via Obsidian Sync.
- Restore test: a documented, once-verified restore procedure (vault blob +
  pg_dump into a scratch DB) is part of the deliverable — an untested
  backup is not a backup.

### INFRA-1: Prod/dev separation (single host)
Current state: one environment only. Resolution: the currently running
install IS production and stays untouched; dev is built as the new,
lightweight layer on the same Mac Studio:
- Second repo checkout via git worktree (feature branches).
- Second Postgres DATABASE on the same OrbStack Postgres server (cobalt_dev)
  — not a second server.
- Dev config profile (configs/dev) + separate Mattermost bot token.
- Dev writes only to the test vault (INFRA-2), never the live vault.
- Shared LLM backends (LM Studio local endpoint + cloud APIs) are acceptable:
  they are stateless services; contention is managed by running heavy
  dev/test jobs outside market hours (per non-negotiable #16 deploy window).
Deliverable: scripted setup + a documented promote-to-prod procedure
(merge → tag → deploy → smoke test → rollback command).
Additionally: destructive dev utilities (dev_utils/wipe_memory.py,
reset_memory_table.py, and any peers) must be guarded to refuse execution
against the production database name.

### INFRA-2: Vault redesign and live/test vault policy
- Live vault: the Obsidian Sync vault. Written only by Cobalt-prod.
- Test vault: the existing Mac Studio playground copy, formalized. Written
  by Cobalt-dev; never syncs; disposable and refreshable from live.
- Redesign (after the assessment documents every hardcoded vault path and
  structural assumption in code): Karpathy raw → wiki → output model with a
  master index and index.md TOCs per folder; structure serves as Dejan's
  second brain and Cobalt's second brain combined; migration plan from the
  current structure; scribe rebuilt against the new structure.

### INFRA-3: Local inference stack refresh
Remove Qwen 3.5 122B MoE; install Qwen3.8-27B 8-bit MLX with the MTP drafter
adapter; enable parallel slots; expose per-call reasoning_effort; wire as the
LiteLLM local route; validate Claude Code delegation against the local
endpoint.

## 13. Process

- Pre-flight order: INFRA-0 security remediation → gitignore verification →
  commit outstanding working-tree changes on main → verify GitHub remote and
  push → tag pre-assessment → launch the assessment session.
- The February context snapshot (cobalt_master_context.txt) is STALE — the
  src tree has since changed (brain/core/interfaces → memory/security/
  services/skills/tools/utils). The assessment regenerates a fresh context
  with dev_utils/generate_context.py as its first act and treats the old
  snapshot as historical reference only (it preserves the Gemini-era ADRs,
  task plan, and backlog).
- Sequence: read-only code assessment (Claude Code, chunked passes,
  RETAIN / BROKEN-FRICTION / KILL with file:line evidence; no fixes, no KILL
  decisions by the model — Dejan decides) → backlog + kanban from findings →
  INFRA tasks → value-sequenced sprints.
- The assessment must additionally flag any existing code touching
  fundamentals, filings, earnings, or news retrieval, and document every
  hardcoded vault path (inputs to §8 and INFRA-2).
- Gitignored-by-design paths (vault copies, testing dirs, credentials) are
  out of scope for inventory; the assessment notes only which code
  reads/writes them.
- Docs regime per non-negotiable #6; VaultManager (COBALT_MASTER_KEY) is THE
  credential store for all API keys and site logins.
- Google integration: Layer A = Claude connectors (Gmail/Calendar/Drive) for
  admin work only; Layer B = Cobalt via Google Cloud OAuth (Gmail, Calendar,
  Drive, Docs, Sheets), minimal scopes, read/write allowed, write actions
  behind approval tokens; trading pipeline never uses Gmail; NotebookLM via
  notebooklm-py cookie auth with stale-cookie alert to Mattermost.
