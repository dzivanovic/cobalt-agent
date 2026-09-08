# COBALT PROJECT LEDGER
The living record of decisions, laws, and project state. TRIAGE.md (20 - Assessment/) is the frozen triage record; this ledger carries everything after it. Updated by appendix blocks from planning sessions, pasted by Dejan, folded by Code.
Started: 2026-08-28 · Covers: 2026-08-22 → present

---

## 1. LAWS REGISTER (cross-cutting, binding on all work)
Laws 1–7 ruled at triage (see TRIAGE.md): fail-loud · watcher standard · one-path rule · secrets discipline (two-phase boot, one conn factory) · routing law · agent north star (GrokBot-style specialists under one chief of staff) · shadow-mode promotion via HITL. Plus from TRIAGE amendments: sample-size law (no EV/grade without n; n<30 = "insufficient data") · source-substitution + loud degradation · config-as-code (Pydantic on load, git, dry-run) · human-only tape dot · planning two-week cap.

Added post-triage:
- **L13 Delegation contract (08-27):** Claude arrives with problems pre-solved — complete Code prompts w/ model tags, decisions-taken-with-veto, standing engineering queue maintained; Dejan's verbs = rule, paste, glance. Claude protects Dejan's time, including from the project itself.
- **L14 One-throat law (08-28):** Dejan talks to the chief of staff only. Agent-to-agent traffic is backstage; only outcomes and HITL cards surface. No war rooms, no attended agent meetings.
- **L15 External-code law (08-28):** third-party code is reference only — no file imported into Cobalt. Patterns/snippets adaptable through four gates: proven, conformant with our laws, industry-standard, reviewed-clean. Untrusted-input posture for internet artifacts.
- **L16 Agents-as-data (08-28):** agent count/type never baked in code. Agent = registry entry (id, charter, tier, tool allowlist, schedule, memory namespace). Creation-by-conversation: CoS drafts config → HITL card → approved = exists. Deactivate = flag.
- **L17 Council pattern (08-28):** deliberation is a mechanism, not a meeting. CoS convenes 3–5 lens-diverse agents on high-stakes/ambiguous questions (or on request); capped structured briefs; CoS synthesizes one recommendation w/ vote + dissent attached. Councils recommend only — execution goes through normal HITL gates. Convening criteria explicit; not the default path.
- **L18 Task integrity guarantees (08-28):** every task = persisted row + state machine (pending/running/done/failed) via message queue; no fire-and-forget. Every process registered w/ maxTurns + timeout + heartbeat; watchdog surfaces zombies; kill phrase stops all. Failed = loud.
- **L19 Whole-prompt rule (08-27):** every Code prompt delivered complete in one block, always; changes = full re-issue. Model tag on every prompt.
- **L20 Cross-thread review rule (08-28):** when Dejan explicitly says "review those threads," Claude searches/reads the named threads before answering — never answers from memory alone appearing to have reviewed.
- **L21 Phase-1 model doctrine (08-28):** appropriate intelligence for appropriate task, local when available. Hot-swap purity = Phase 2; never blocks today's progress.
- **L17 amended (08-29/31) — Cross-provider councils:** council seats may be heterogeneous across providers (Claude / Grok / GPT via fast wire). Epistemic diversity > role diversity for high-stakes judgment. Members are ADVISORS, not actors — structured briefs (position, reasoning, confidence) → CoS synthesizes on reasoning quality, never vote-tallying; dissent surfaced. Councils never touch deterministic layers (rules, math, sizing). Privacy dial: default = personal layer EXCLUDED from cross-provider composition (each provider gets the task minimum — purpose-based sharing, not provider-trust ranking); explicit per-case ruling by Dejan can grant exceptions.
- **L22 Two-plane model access (08-29/31):** FAST WIRE (LiteLLM/direct, single-shot) for pipeline inference, memory machinery, council briefs; CHASSIS (Agent SDK sessions) for agents that act with tools. Coexist by task shape; they meet only at the local lane (LiteLLM proxy-mode adapting mainframe for SDK sessions). Economics: Max subscription and Anthropic API are separate meters — SDK sessions on claude-login auth = zero marginal cost; LiteLLM→Anthropic API = paid. SDK chassis = Claude-on-subscription + local-via-proxy only.
- **L23 Local-first law (08-29/31):** local trumps cloud even when cloud is free — continuity rationale (Gemini outage 08-28 killed a morning briefing). Every lane local can serve runs local-first with cloud fallback; judgment lanes cloud-first with loud degraded-mode on outage. Gate: mainframe untested — local lane assignments earned via bake-off. LOCAL = first candidate for every task → cheapest sufficient step up.
- **L24 Three-rung economics (08-29/31):** (1) local = free, first · (2) subscription-agent FEDERATION = free — async via dead-drop (Grok Bot etc.) and sync via in-session CLI bridges for code work · (3) metered fast-wire APIs = sync-only, rare, bounded, cost-footered. Pay-per-token = narrowest rung.
- **L25 Failover doctrine (08-29/31):** every intelligence lane carries a config-defined fallback chain — Claude → next-best house (headless, task-shape-routed) → LOCAL as the owned always-up floor (also always-on verifier/triage). Degradation loud at every hop. Local-SPOF question parked. Phase 1: cross-house seats NOT load-bearing — advisors and fallbacks only; load-bearing status earnable later by explicit ruling. Quota extension: token-limit exhaustion = outage class — routed, not a crisis; usage ledger exposes quota as a monitored resource; CoS sheds load down the chain proactively and loudly (compute budget enforced like the trading risk budget). Deterministic pipeline burns zero Claude tokens.
- **L26 House-agnostic routing (08-29/31):** appropriate intelligence for appropriate task applies across houses — task classes assigned by measured evidence (bake-offs, slice reviews, cost-ledger token-per-outcome), recorded in routing config with rationale; Claude's conflict of interest neutralized by evidence-cited routing (Claude recommends against Claude when measurements say so). Assignments re-tested as local models improve.
- **L27 Budget ceiling — hard (08-29/31):** Claude spend caps at Max 20x (5x→20x = the only permitted escalation, evidence-forced); no usage top-ups beyond max plan, ever. Grok + Codex enter at MINIMUM tiers. Demand exceeding the envelope → routing discipline + local lane, never spend. 20x decision deferred pending one normal-week measurement.

## 2. DECISION LOG (dated, one line each)
- 08-22 TRIAGE complete: all 7 subsystems ruled (see TRIAGE.md). Design-session register collapsed; planning capped 2 weeks; pre-beta increments defined (ASET sheet → DRC/playbook prefill → prebell-lite); Guardian rule set v1; Charter requirements (capacity math, trader metrics, build/trade firewall).
- 08-22 Phase 0 withdrawn → automation-first rhythm: 3 calendar anchors only; DRC gates evening Cobalt; positive-reinforcement coaching; sessions-per-role fleet = manual prototype of the agent org.
- 08-23/24 Slice 1 shipped: ASET sheet (Flask, src/cobalt/), LAN bind for trading PC, Postgres persistence. Security incident: old tree dumped vault to console (config.py:622 unconditional) → excised at source, LOGURU pin, full credential rotation (SMB, FinancialJuice, cloud keys, Finviz, Mattermost token, Postgres password), logs purged, histories cleaned. Root causes documented; Mattermost container must be RECREATED (not restarted) after Postgres rotation.
- 08-25 Docs restructure (D6): numbered docs/ tree (00 Project/10 Decisions/20 Assessment/30 Design/40 DevDocs/50 Roles/90 References/_archive); standard in CLAUDE.md; frozen-record policy for dated corpora.
- 08-26 VAULT UNIFICATION: real vault = /Users/cobalt/Vault/Think synced 3 devices; repo docs/ symlinked in at "0 - Projects/Cobalt" (one space, drift structurally dead); selective git (docs/* ignored, D6 folders carved in); Gemini-era wings archived (both copies); dailies rehomed to 1 - Trading/1- Daily Notes; Obsidian plumbing fixed; new-core vault resolver (ONE source, outside-repo write gate); old tree untouched (its 0 - Inbox stays live until writers retire). ASET writes to real daily note.
- 08-27 Finviz spike A+A.2 (DATA-SOURCE-MEMO.md): all 9 timeframes confirmed incl. i2; intraday = fixed rolling window (no date-range param found — Phase B's top question); Groups cracked (sector/industry/cap relative strength); per-ticker news via v=3/4 tagged feed or screener cols 135-137 (t= on /export/news dead); Portfolio N/A.
- 08-27 BAR ARCHIVER built + scheduled: tier_a (Green+Red+SMB singles) i1/i2/i5/i15/i30; tier_b (context ETFs) i5/i30; d/w/m never archived; nightly launchd 20:30 detached; backfill-on-entry CLI; run report file. VIX = named data gap. Session-timeout incident → long jobs always run detached.
- 08-27 Coach-thread integrations: two .htk files (full/half day) loaded per temp check; re-entry rule canonized (#2 needs WRITTEN new info; #3 = stand-down + ticker closed); pre-trade card = contract; excitement-audit on reversion cards; DAS native-enforcement question open (11-2 lockout, max shares).
- 08-28 ASET iteration 4 RULED: FULL/HALF mode toggle, fixed-dollar grades matching .htk EXACTLY — FINAL: full B=$60/A=$135, half B=$30/A=$70 (reverted to coach's numbers; keys being updated to match). Full ladder in config (A+ 345/170, C 21/11, D 0) with enabled_grades=[A,B]; C/D = SAW, A+ reserved. Auto-append card on compute (save button removed). Actual-fill recompute field + ≥25% distance warning + FILL UPDATE block. Future: ceiling = 1% of account, dynamic.
- 08-28 Strategic exercise: 90d/6m/18m/5y timelines; SMB-desk path rejected (age realism) → capital paths = evaluation funding (gated on 6mo process metrics), swing track (the Qullamaggie vehicle, §1 expansion), options expression (post-proven-edge), account step-up (mechanical tripwire). Runway plan: Dec 31 = consistently green (hard target); Apr 30 = first real withdrawal (proof, not payroll); contracting = bridge with demolition date (deliverable-shaped, West-Coast clients, no meetings before noon ET, pipeline built Sep–Dec while salaried); trading = destination, answering only to self + the system.
- 08-28 Expansion Ladder recorded: prove 9:30–11 core → push size (SMB doctrine, mechanical steps) → expand windows (2–4, then premarket) → swing track → options. Every rung unlocked by evidence thresholds numbered at Charter.
- 08-28 Kashef/ClaudeClaw blueprint mined (kashef-mining-memo.md): ADOPT Agent SDK chassis (sessions = agents, per-agent CLAUDE.md = role packs, agent.yaml = registry), hive-mind table, @delegation syntax, memory-v2 mechanisms on OUR Postgres, exfiltration guard, maxTurns, cost footer, message classifier. REJECT SQLite/Telegram/war-room theater/meeting avatars/personas. Agent SDK spike scheduled at orchestrator design: HITL-hooks question, two-session test (subscription CoS + local worker via LiteLLM proxy-mode adapter), local-model harness bake-off, ToS verify, failure surface.
- 08-28 Meeting Scribe agent: post-MVP MUST-HAVE. V1 listen-only Path B: Mac holds the one meeting seat (browser session), system audio → local Whisper → notes agent → vault; trigger-based frame snapshots; Dejan taps in/out via the shared seat; works on live + replays. SMB permission email gains a transcripts line.
- 08-28 Voice target: conversational chief of staff (bidirectional, natural) = §9 end state; Pipecat/Gemini-Live class stack as reference; post-MVP; trading chain stays typed underneath. FluidVoice parked (Windows-first requirement; Win+H/Gboard as free trials).
- 08-28 Grok Bot pilot (backlogged post-slice-2): dead-drop storage integration (inbox/outbox, markdown payload + JSON manifest); jobs = X sweep + one SMB corner-case; ONE dedicated credential; Discord excluded (self-botting ToS).
- 08-29/31 Runtime intelligence architecture ruled (consensus after pushback): SDK sessions = RESIDENT agents (persistent, identity, tools — CoS, build agents). Cobalt HEADLESS RUNNERS = STATELESS invocations of vendor CLIs (codex exec / grok -p --json-schema) on subscription auth, wrapped in Cobalt's own task machinery (row + timeout + heartbeat + schema + loud failure) — council seats, second opinions. Vendor bridge PLUGINS = build-time only. Employees vs consultants vs switchboard.
- 08-29/31 Cross-house bridges adopted (official plugins; external-code-law carve-out for first-party vendor tools): openai/codex-plugin-cc (/codex:setup, :review incl. adversarial, :rescue, :transfer, :status/:result/:cancel — ChatGPT subscription via local Codex CLI login) + xai-org/grok-build-plugin-cc (/grok-build:setup, :review w/ --scope/--base/--model/--wait/--background, rescue, session import — SuperGrok via local grok CLI login). Cross-house adversarial review = free build-time gate (first use: slice-2 review). Scope: repo code only; vault/.env/personal layer excluded. Grok Build reads ~/.claude/skills + CLAUDE.md natively — skills port across houses.
- 08-29/31 Grok role elevated: Grok = the X-lane specialist (native X access = structural advantage; §5 X-monitoring's owner) — primary role; council/review seat secondary. Grok Bot pilot = its proving ground.
- 08-29/31 Memory-bridge architecture (Cobalt instantiation) ruled: claude.ai memory does not cross to Agent SDK — bridged by (1) corpus (repo + vault), (2) Postgres genesis import at MVP bring-up, (3) Personal Continuity Pack: authored export, multi-session, seat-by-seat, each fleet chat contributes its brief, Dejan reviews; stored outside the repo in Think (git-invisible, Obsidian-synced, Cobalt-readable); exfiltration-guard scope; validated by the RAMP (fleet + Cobalt run in parallel; tone-gaps patched in service). Authoring begins well before MVP eve.
- 08-29/31 Health Check ruled, timing split: thin heartbeat = pre-beta build after slice 2 (services alive + data freshness + one cheap probe per subsystem; red/green to daily note + DM; red also alerts out-of-band — alert path ≠ monitored path). Mission-control green-light widget = post-MVP display of the same machinery.
- 08-29/31 Ledger placed at 0 - Projects/Cobalt/00 - Project/PROJECT-LEDGER.md; appendix-paste workflow active; planning sessions ROTATE (Ledger = the handoff; attach Ledger as first message of each new planning chat).
- 08-29/31 Accelerator doctrine ruled: never hand-build what a vetted accelerator + four-gate law can adapt; accelerator-hunting = part of Claude's standing queue maintenance. Post-MVP MoSCoW sequences with accelerators assumed.
- 08-29/31 Charter requirement added: post-MVP lane gets its own ruthless MoSCoW at the sittings, sequenced by trader-metric impact — no unbounded "after MVP" bucket.
- 08-29/31 Needle doctrine affirmed: needle = Dejan-as-trader, never Cobalt-as-artifact; the prioritization test for all work.
- 08-29/31 Taxonomy commitment: sitting happens by end of next weekend (~09-06); Dejan initiates by declaring it. Claude flags if the window closes empty. Planning cap satisfied by committed window.
- 08-29/31 Playbook Trainer retiered Fable → Sonnet (drill execution = clerk-shaped); Fable reserved for judgment.
- 08-29/31 Purchase gate: SuperGrok + ChatGPT sub unpurchased pending Dejan's full-picture review; bridges/runners wire up after.
- 08-29/31 Archiver verified running unattended (archiver-runs.md rows landing).
- 08-31 Slice 2 kickoff prompt issued (fresh Code session, Sonnet): Jinja templates-as-config from Dejan's Daily/DRC templates; 05:15 morning daily prefill (SPY/QQQ/IWM via Finviz, calendar, rules block from rules.yaml, day-mode line, adherence checkboxes; VIX/BTC = "n/a (manual)" loudly); trade notes auto-created from ASET cards (lights the dataview table); evening DRC prefill (cards, re-entry fields, excitement audit, checklist); fail-loud, idempotent, append-if-exists. Playbook PPTX = slice 2b.

## 3. COMPONENT / AGENT REGISTER
- **Shipped:** ASET sheet (iter 4: mode toggle, auto-append, fill recompute) · Bar Archiver (nightly, tiered) · vault resolver · docs D6 tree · TRIAGE + memo corpus.
- **In build:** Slice 2 — DRC/playbook prefill (kickoff Mon 5:30, fresh session): prefill engine → Templater templates (in 90 - References) + trade-reporter renderers; day-mode line + .htk-match check; re-entry/excitement fields; rule-adherence checkboxes.
- **Next builds:** prebell-lite (2–3 wks thin, iterate) · exfiltration guard (small) · Agent SDK spike (at orchestrator design).
- **Named future agents:** Chief of Staff (one throat) · specialists per registry (L16) · Guardian (real-time rules; gated on Rules Engine + grading/EV + alerting; DAS-native check may shrink scope) · Research Analyst (§8 engine) · Meeting Scribe (post-MVP must-have) · Drill Candidate Detector (feeds Rubberband training from archiver corpus) · Coach/DRC/Logistics (running now as manual chat fleet: planning+coach=Fable, DRC+logistics=Sonnet). Grok role elevated (08-29/31): X-lane specialist (native X access), primary role over council/review seat secondary — proving ground is the Grok Bot pilot.
- **Design sessions pending:** Trading Taxonomy (FIRST — needs scheduling; absorbs variable registries) · Data-Model + Vault-remainder weekend block (schema ADR, embedder ADR, DB-split, memory-v2 mechanisms input) · Product Definition sittings → MVP Charter (~2-month usable target) · Rules Engine (post-Charter, gates Guardian) · Orchestrator design (Agent SDK spike + council + registry).
- **Cross-house bridges live (08-29/31, build-time tooling, not agents):** Codex plugin (ChatGPT subscription, local Codex CLI login) + Grok Build plugin (SuperGrok, local grok CLI login) — repo-code-only review/rescue tools; vault/.env/personal layer excluded (L15 external-code-law carve-out for first-party vendor tools). Runtime distinction (L-architecture ruling, 08-29/31): SDK sessions = resident agents; Cobalt headless runners = stateless CLI invocations wrapped in Cobalt task machinery; vendor bridge plugins = build-time only.

## 4. STANDING QUEUE / OPEN ITEMS
- Dejan: Phase B Finviz page captures (Stock "Learn More" panel = the date-range mystery) → 90 - References/finviz-pages/ · SMB permission email (+ transcripts line) · DAS native-enforcement check · schedule Taxonomy sitting (by ~09-06) · templates → confirmed in References · corrected .htk files to 60/135 · delete stray "test note" · purchase decision on SuperGrok/ChatGPT.
- Claude: slice-2 kickoff prompt (ready Mon 5:30, issued 08-31) → now slice-2 review + next assembled prompt · ledger appendices at session close · continuity-pack authoring sessions (pre-MVP) · September contracting one-pager.
- Verify: archiver nightly runs (archiver-runs.md, verified running unattended 08-29/31) · planning cap clock (started 08-22; Taxonomy + PD sittings must land within it or cap is re-ruled — Taxonomy window commitment: ~09-06).
- Build lane order (08-29/31): slice 2 → health-check heartbeat → prebell-lite → exfiltration guard → orchestrator design (Agent SDK spike, headless runners, registry, councils).

## 5. STRATEGIC LAYER (summary — full reasoning in planning thread 08-28)
Product = a profitable trader; Cobalt = leverage. 90d: unbroken review loop, twelve steps, MVP in box, green-by-Dec-31 target. 6m: expectancy as evidence (archiver + cards corpus), capital-path decision point. 18m: documented track record → chosen path scaling. 5y: trading as owned income; Cobalt mature multi-agent OS. Failure sentence to sidestep: never let building feel like progress on days trading was avoided; never let a green rule-break become a trophy. First grading: Dec 1.

## APENDIX
### 08-31 (planning session, post-slice-2)
- Finviz vault credential: website password refreshed by Dejan to his
  daily login; multiple concurrent logins confirmed OK on the account.
- Phase B capture COMPLETE (Code, Sonnet, authenticated): 4 pages + 3
  same-origin JS files in docs/90 - References/finviz-pages/ with
  capture-manifest.md. 6 redactions (email x1, live api_token x5).
  Uncommitted pending Dejan's manifest review. Method note: scrubbing
  needs a 16-char minimum or short cookie values corrupt the HTML.
- RULING CONFIRMED EMPIRICALLY: /export/stock r= accepts d1..max but is
  a narrowing filter only — r=y5, r=max and no-r= all returned identical
  5086 rows, 08/17–08/31, at i2. Multi-year minute backtesting is
  impossible on Finviz. ARCHIVER CORPUS = SOLE MINUTE HISTORY;
  a missed night is unrecoverable data.
- Consequence: archiver promoted to load-bearing. Heartbeat's first
  probe = archiver freshness (last run + row delta), red out-of-band.
- Session hygiene: /clear at task boundaries (context re-sent every turn
  = token burn); CLAUDE.md verified to survive /clear, so prompts carry
  paths + rulings, not file contents. L27 20x decision: re-measure after
  one week of disciplined clearing — this week was bloated-context, not
  normal.
  

### 08-31 addendum (daily-note review session)
- FIELD OWNERSHIP = CAPABILITY FRONTIER (his inversion, adopted): Cobalt
  owns every field it CAN fill; Dejan owns the residue. Per-field config
  flag, three states: cobalt / cobalt-degraded (source down, loud "n/a
  (manual)") / human. Frontier moves as widgets land — no template
  rewrite when Oura MCP arrives, just flip the flag.
- GAME PLAN permanently human (agreed): it is the artifact where his own
  read is the product. Cobalt may write a PROPOSED plan in a parallel
  field; the gap between his and Cobalt's is calibration data.
- Prefill runs MULTIPLE times premarket, config-scheduled (no hardcoded
  times) + manual trigger. Requires ownership markers first — blind
  re-run would overwrite human-written sections. launchd plists must be
  installed.
- ASET card semantics ruled: a card = a written plan; a card + fill-
  recompute block = a taken trade. He runs cards for analysis and does
  not card every pass. EOD reconcile in DRC prefill lists unfilled cards
  and asks taken/passed/discarded.
- CARD DEFECTS found in 08-31 note (slice 2.1a): stale field carry-over
  on ticker change (2 junk cards); fill of 2518.91 accepted and written
  twice; PCG stop 17.72 vs entry 13.379 (32%) accepted. All = card
  accepts input it should refuse. Pydantic validation + config thresholds.
- CALENDAR: Finviz alone insufficient — misses Fed speakers, policy
  events (Trump drug-price 3pm, G20), non-US data, and possibly
  actuals-vs-forecast. Ruled: Finviz + ForexFactory merged, deduped,
  impact-filtered; earnings gated to watchlist + large caps.
- MARKET CONTEXT pipeline ruled: Finviz screener emits ALL numbers
  deterministically (§4 tools-fetch-agents-reason); LLMs receive the
  filtered ticker list and supply catalyst/narrative/trade-idea ONLY —
  never a figure. Filter thresholds move to config. Fan-out = council:
  3 subscription houses, structured output to schema, agreement
  mechanical, disagreement surfaced. Perplexity DROPPED (metered).
- VITAL DAWN (Adam Crisafulli) = open RSS feed w/ direct audio, ~4-5 min
  episodes. Chain: RSS → download MP3 → local Whisper → structure.
  Kills phone-to-mic capture AND the Perplexity cleanup call. Feed URL
  resolved via iTunes lookup on Apple ID 1486375788, stored in config.
  Articles are members-only; audio is not; parse enclosure, ignore link.
- GRADING amended: per-parameter A-D → 1-10 with a stated WHY per score.
  Assessment granularity 1-10; SIZING stays two .htk keys (8-10 → A key,
  5-7 → B key, <5 pass). Historical A/B/C cards map to bands to remain
  usable as calibration. Score overrides recorded WITH REASON; a reason
  must resolve to a variable (existing, mis-weighted, or new) = Taxonomy
  schema input.
- PREBELL reframed: completeness target, not garnish. His skeleton is
  small because bandwidth is small, not because it is the spec.
- Build order: 2.1a (card validation + reconcile, tonight) → 2.1b
  (prefill writer: ownership markers, in-place fill, multi-run,
  ATR/RVOL auto-fill, calendar filter) → prebell-lite.
- TAXONOMY sitting committed for 09-01, after DRC or evening.

### 09-01 (Taxonomy cross-reference pass, closed)
- Cross-reference of SMB corpus (Glossary, Market Context, Game Plan, TOS
  scripts) vs draft v0.2 complete → TAXONOMY-DRAFT-v0_3.md issued,
  supersedes v0.2 (lives beside it in 30 - Design/).
- RULED: card registry = {gates[], variables[]} — gates binary (rules/
  plan-alignment + tradability: spread, polka-dot, halt, locate), any
  fail = no card; var 10 moved to gates; var 12 reserved "setup
  expectancy (own data)", inactive until n≥30.
- RULED: HV bar = vol ≥ MA + 2.0σ, ~10-day lookback per timeframe (SMB
  Study 2 defaults, tune from outcomes). Extension band = 5-day extreme
  ± 5·ATR(20) daily (Study 3); Extension gains distance_from_band.
- RULED: swing = structural peak/valley, N-bar pivot confirmation per
  timeframe, NO ATR component (SMB ATR-displacement REJECTED).
- RULED: regime breadth = separate strength + weakness axes, SMB 2×2
  derived label; VOLD per exchange (NYSE + NASDAQ), bands 2.618
  "leaning" / 3 trend-day input; regime events gain cause; TRIN
  computed free, never a variable.
- RULED: IF/Then plan branches = new object {condition, action,
  invalidation}, premarket + intraday authoring, ~3/name, watchlist cap
  3-5 config; branch match feeds the rules gate; grammar → trades pass.
- RULED: Level.type extended (PMH/PML, OR H/L, HOD/LOD, 52w, round,
  multi-day/anchored VWAP, trendline); Theme gains head (head fails →
  theme invalid), "sympathy" adopted; one-trigger-per-ticker demoted to
  config policy (ticker+direction); tape dot human by law, volume
  computables → var 7.
- RULED script dispositions: Cobalt computes by default; Study 1 skip,
  Study 2 Cobalt detector, Study 3 Cobalt + one Pine daily display,
  Study 4 native TV anchored VWAP + Cobalt auto-anchor, Study 5 Cobalt
  pending spike. SPIKE added: $UVOL/$DVOL ingestability via TradingView
  MCP.
- Sequencing RULED: setups session NEXT (agenda = v0.3 §10), trades
  pass immediately after. Both inside the planning-cap window.
### 09-01 (Taxonomy setups session, closed)
- v0.3 §10 items 1-10 all ruled → TAXONOMY-DRAFT-v0_4.md issued,
  supersedes v0.3 (30 - Design/).
- RULED: category computed per instance from bar character (continuous
  same-direction bars + high/expanding volume = Momentum, any day of
  move), setup names keep defaults only; gap threshold in ATR; GUIR/GDIS
  = gap must not break the level or must reject the attempt, sustained
  break = breakout; prior_context fresh|continuation|exhaustion
  (continuation = Day 2/3 themselves).
- RULED: consolidation (daily) = inside day open-to-close, wicks
  excluded; resets Extension day count AND re-anchors 5-ATR base.
- RULED: CF = fundamental-analysis concept, defined by repricing-class
  news, not levels; gap optional; instantiation news-side, confirmation
  + grade price-side only; pending→dead kept as calibration data.
- RULED cross-cutting laws: full modularity (every threshold config,
  definitions as data, shiftable on the fly) + calibration loop
  (prediction record on every scored object, score+WHY joined to
  outcome; Cobalt proposes re-scores, Dejan approves, n≥30).
- RULED: Range bound_type flat|converging|channel (Big Dog/Small Dog
  fire from flat or sloped, either direction); object lifecycles for
  Gap/Range Break/Extension/CF.
- RULED: In-Play layer = Cobalt radar capped at 50 names w/ continuous
  conviction re-scoring (EV once var-12 corpus exists) vs human focus
  list ~4; sources = 4 TV static + 4 Finviz dynamic + future
  specialized lists.
- RULED: prior-day enum + inside|reset only (rest cut); Day 3 liquidity
  trap = candidate setup, no card until graduation; volatility_state =
  filter-flag (neither gate nor variable); CiC bar-level only, tape
  excluded; dispersion high → var 4 neutral; headline-driven = context
  flag, event gating via window machinery.
- RULED: session clock 24×5 — premarket 4-9:30, RTH 9:30-16,
  aftermarket 16-20, market_reset 20-21 (no-trading, hard-blocked),
  overnight 21-4; windows as gate input + window-fit variable; dynamic
  flag display-only until Guardian.
- PROPOSED pending: RTH sub-window boundaries; unexplained-RVOL in-play
  admission (default yes); intraday consolidation rule → trades pass.
- NEXT: trades pass (v0.4 §10), inside the planning-cap window.x


### 09-01 addendum (post-taxonomy design discussion)
- EXPLAINABILITY LAW confirmed: no derived value without stored
  inputs — every number replayable. Explanation = query over the
  evidence chain (WHY per score, evidence[] per transition,
  prediction records), not interrogation. LLM judgments explained
  by storing what the model was shown + what it said.
- COMPUTE/TOKEN assessment: taxonomy ops trivial on local CPU
  (50 names / 2-min bars); paid tokens only where language is
  (catalyst class+grade, council, CF calls, narrative, talking to
  Cobalt) — conversation dominates the budget, not market ops.
  Real bottleneck = intraday data feed (TradingView MCP spike),
  not performance. Token budget sizing → Product Definition.
- STEERING confirmed Jarvis-style within non-negotiable 12:
  talk → Cobalt translates intent → config diff → Dejan approves
  → applied. Config-as-data (modularity law) makes this cheap.
- NEW CAPABILITY SET named (Dejan): rules fine-tuning dashboard —
  full traceability must also show why names were EXCLUDED, not
  just included. Components: benchmark query (unfiltered movers
  ≥ config move, no gates) → diff vs in-play set → MISS RECORDS
  {ticker, date, move, excluded_by} auto-created via replay →
  miss-pattern aggregation (e.g. Tesla-class miss 10x/month →
  variable/threshold gap identified) → Cobalt PROPOSES config
  change or new variable, Dejan approves. Same prediction-record
  machinery as catalyst re-scoring, pointed at selection.
- BACKTEST/FORWARD-TEST scoped: backtest = replay selection layer
  over archiver corpus with candidate config (cheap,
  deterministic; NOT strategy-PnL backtesting — that waits on
  trades pass + var-12 corpus). Forward test = shadow config
  running parallel to live N days, diff reviewed before
  promotion. Visual day-replay = dashboard face of same engine.
- ARCHIVER CONSTRAINT flagged: minute replay only exists for
  archived names (Finviz can't backfill — 08-31 ruling). Miss
  analysis must feed archiver tier policy; OPEN QUESTION
  (near-term): auto-archive top-N daily movers nightly
  regardless of watchlist — cheap insurance, data lost now is
  gone forever.
- DISPOSITION: capability set (miss ledger + benchmark query +
  shadow configs + replay engine + tuning dashboard) → Product
  Definition sittings agenda. Archiver tier-policy question →
  near-term, decide before/at next planning session.

### 09-02 (Taxonomy trades pass, closed)
- v0.4 §13 + §10 items 1-9 all ruled → TAXONOMY-DRAFT-v0_5.md issued,
  supersedes v0.4 (30 - Design/).
- LAW (Dejan correction): ANATOMY-ONLY — taxonomy carries no personal
  trading rules (no entry cutoffs, no-trade windows, risk dollars).
  Windows = market anatomy; trading moves to 24x5 incl. pre/after/
  overnight. Live rules live in printed card / rules gate / future
  Guardian (advisory) only. Claude imported live rules into 13.1 draft;
  reverted. RTH sub-windows ruled anatomy-only (config).
- LAW: TIMEFRAME-AGNOSTIC TRIGGER — trade triggers on its own
  working_timeframe (trader preference; scalp class <=15-min, beyond =
  move2move; swing/options own classes later). Higher-TF objects =
  preconditions/context, never triggers. No fixed TF in taxonomy.
- RULED: consolidation = daily inside-day rule daily-only; intraday
  consolidation = micro-Range, 2 touches/side (one reused rule, config),
  bar-count rejected. leg=wave data-level alias (changeable). Pivot
  N=2 fully configurable. Range Break gains retest EVENT.
- RULED: intraday Extension instantiates via culminating bar character
  OR >=1.25 ATR from open with no catalyst (config); then snapback
  watch. leg_count on Extension.
- RULED: VIR = setup unlocking countertrend trades both ways; two_way
  removed from trade relation; trade_defs side-symmetric; instance
  direction computed from setup state.
- RULED + LOCKED: trade_def schema v0.2 (preconditions, trigger types
  incl. sequence + variants, exit ladder w/ per-leg evaluation,
  stop_management, on_cic, max_attempts, avoid, quality_factors,
  preferred_windows -> window-fit only, reference_stats never EV,
  add_policy reserved). Enums: stop placement / management (incl.
  time_stop) / exit targets; evaluation touch|close_through;
  confirmation intrabar|close_through|two_bar|acceptance, headline
  flag = one-notch step-up; entry_mode front_side|backside with NO
  direct size coupling (one sizing path: grade -> key -> shares).
- RULED: six radar trades mapped to object states (Rubberband =
  Extension culminating->reverting, Back$ide = backside phase, etc.);
  radar reads states, no trade detectors.
- RULED: IF/Then grammar (atoms over objects, AND/OR/NOT/THEN/WITHIN,
  branch stop override, invalidation = calibration record, mirror
  flag). Branch = his authored plan, personal timing allowed there.
- Adds/scale-ins PARKED (slot reserved). Day 3 liquidity trap:
  5 graduation criteria + candidate|cardable flag RULED; definition
  PLACEHOLDER until sheet found.
- POPULATION PROCESS ruled: offline batches, Dejan pastes sheet ->
  Claude drafts trade_def -> Dejan rules conflicts. Batch 1 = Radar 5
  + Big Dog + Cameron H grid (21 trades x 7 setups). Rubberband truth
  = Playbook Rev1 deck over raw SMB sheet.
- NEXT: trade-details population batch 1 (planning-cap window).

### 09-02 (Taxonomy v0.6 fold + trade_def commit prompt, closed)
- TAXONOMY-DRAFT-v0_6.md issued, FINAL, supersedes v0.5 (30 - Design/).
  Batch 1 §A folded → schema v0.3: family[], class = management
  shape, raise_to, cross_point, turn_low; Range.duration/wick_ratio;
  flat()/slope_norm; RangeBreak(HTF).day_count; Leg(impulse) +
  Leg.role; §4 Big Dog/Hitchhiker/Rubberband rows rewritten; laws
  advisory-exit / per-trade stops / stop-nudge / sheet reading /
  attempts / standard quality trio into §0.
- RULED (fold collisions): (1) Range.shape DROPPED — bound_type
  flat|converging|channel stands, slope irrelevant; diverging bounds
  = not a consolidation, no Range instantiates; Big Dog carries no
  shape clause. (2) Trigger-variants slot DROPPED; re-add only with
  real-world data. (3) Stop buffer default = fixed 0.02 for every
  trade unless its sheet says otherwise; spread is never a buffer
  (spread = tradability gate). §11 placeholder re-pointed.
- Decided-with-veto (standing): stop_management = ladder with
  on:event; refs gain entry (=breakeven) + leg_end(n); radar_watch[]
  + preferred_windows_ref fields; exit-target params defined;
  stop-nudge = check-and-move, not additive; max_attempts = doctrine
  default, rules gate takes stricter vs 08-27 re-entry rule.
- Code prompt issued (Sonnet 5, fresh): trade_defs as YAML under
  config/taxonomy/ with Pydantic-on-load validation (extra=forbid,
  fail-loud loader, validate CLI), cameron_grid.yaml, per-trade
  variable-registry stubs, §13 replay backlog appended, ADR + DevDocs.
  No engine code, no predicate parsing.
- Gap & Go RULED a setup sheet, not a trade — excluded from all
  batches; content = gap_and_go setup metadata only.
- Batch 2 defined (7 sheets, next session, one at a time): Gap Give
  and Go, VWAP Continuation, First VWAP Pullback, 9 EMA Scalp,
  Back-Through Open, Bella Fade, Bouncy Ball. Pre-read enum gaps:
  indicator-relative stop (below 21 EMA), trendline_break trigger,
  tape-read entries (tape dot human by law → bar proxy), lower_high
  pivot ref, re-entry time window (GGG: within 3 min), 21 EMA trail,
  HOD / two-bar-break exits; scalp "one leg out" vs trailing exits
  to settle at VWAP Continuation.
- NEXT: Code commit → Batch 2 session.


- Batch 1 Code commit DONE (4 commits, branch taxonomy/trade-defs-v0_3,
  unpushed): loader under configs/cobalt/taxonomy/ (path corrected
  from config/ per CLAUDE.md boundary law, ADR-0001); Rubberband B/E
  = level{entry}; Second Chance step-2 confirmation optional; FL
  entry_price → entry at Batch 2 commit. 207 tests green. GAP: dynamic
  tunables sit in predicate strings — structured Tunable slot = v0.7
  fold item. DevDocs INDEX.md refresh owed.

### 09-02 (Trade population, Batch 2, closed)
- Seven trade_defs RULED from full SMB sheets: Gap Give and Go, VWAP
  Continuation, First VWAP Pullback, 9 EMA Scalp, Back-Through Open,
  Bella Fade, Bouncy Ball → TRADE-DEFS-BATCH2-v0_1.md (30 - Design/).
  13 of 21 grid trades populated. Gap & Go excluded (setup sheet).
- SCHEMA amendments A.1–A.8 RULED (folded in v0.7): reentry_window;
  indicator stop placement {VWAP|EMA, buffer, snapshot at_entry};
  trendline_break trigger (named-leg anchor, flat case = far-bound
  break, touch never triggers); indicator_rejection trigger (rejection
  bar = trigger + entry, replaces any tape proxy); Level.type open;
  stop buffer 0.02 every trade, sheet deviations = PROPOSAL only
  (BTO/Bella 0.01 → 0.02); recent_lower_high; trail conditions
  (prior_bar_break 1 | ma_close | vwap_close | level), MA periods
  config (sheet 21 / Dejan 20).
- LAWS: 1-bar trail; stop default fixed, only move = raise_to below
  latest swing low; tape = FRONTIER not nature (tape reads = registry
  variables source: human (frontier), flip on L2/T&S ingestion).
- DwV: working_timeframe default 2m per-trade override; TF audit —
  bar params follow working TF, minute params TF-independent;
  grammar atoms dist(), Catalyst.grade/polarity, Regime.label,
  Range.counter_pivot_count, gap_retrace_pct, Leg(pullback).index.

### 09-02 (Taxonomy v0.7 fold, closed)
- TAXONOMY-DRAFT-v0_7.md issued, FINAL, supersedes v0.6 (30 - Design/).
  Batch 2 §A folded → schema v0.4 (DwV bump). Code fold items in:
  taxonomy path configs/cobalt/taxonomy/ (ADR-0001); Batch 1 commit
  mismatches (breakeven = level{entry}; sequence event-steps no
  confirmation_policy; FL entry_price → entry); TUNABLE SLOT — every
  config/dynamic quantity = a row in tunables.yaml (key, value, unit,
  scope, dynamic, status, sheet_value, consumers, replay), predicates
  reference by cfg(key), loader hoists inline literals and fails
  loud on unknown keys; §13 replay backlog = query on status.
- RULED (fold collision 1): ONE STOP AT A TIME — the trail IS the
  stop once its on: event fires, never a second object. Trail = ONE
  slot per trade_def listing CAPABILITIES (2-min bar, 9 EMA, 20 EMA…);
  Dejan or Cobalt SELECTS one at trade start from price action and
  follows it to the end (mode: select — supersedes A.8 first-to-fire
  "any"); selection + WHY persist as card data; trail_fit = new
  cobalt-computable variable. trail_ma_close / trail_bar removed as
  duplicate spellings. Second Chance = hard stop → trail selected
  after leg 1 → leg 2 exits on it. Share count on a stop = card
  state, not taxonomy. Collision was Claude's misread, not a schema
  fault.
- RULED (fold collision 2): A.10 STRUCK — trailing vs hard exit
  defines no class; legs-out count defines no class (v0.6 "scalp =
  one leg out" was wrong from the start; slipped past both).
  CLASSES REDEFINED (Dejan's words): scalp = usually below 15-min TF,
  seconds to ~45 min (tf_ceiling 15-min = only hard constraint);
  move2move = defined entry/stop/target on a momentum move that
  survives consolidation to a further target (two measured moves,
  HOD/LOD, session end), usually longer, 5-min and up — an intraday
  swing. Durations = anatomy descriptors, never gates. All 13
  populated classes stand.
- NEXT: Code commit v0.7 (schema v0.4 loader, trail slot, tunables
  registry, Batch 2 YAML) → Product Definition sittings resume.

- Batch 2 Code commit DONE (00ff853 schema+data, 2b96611 docs; same
  branch, 223 green, unpushed): reentry_window, indicator stop,
  trendline_break / indicator_rejection, recent_lower_high, trail as
  exit target (mode any — superseded by v0.7), defaults.yaml +
  resolve_ma_ref, A.6 warn-not-fail, frontier field, 7 trade_defs +
  registries, Second Chance retrofit, ADR-0002. Folded (DwV): GGG
  raise_to ref = level{Range(micro).top} (Rubberband precedent);
  buyers_defending_zone no row (no consumer). Ruff absent → added at
  v0.7 commit. v0.7 Code prompt issued (Sonnet 5, fresh).



### 09-02 (Product Definition sitting 3, closed)
- v0.7 Code commit still running at close; mismatch fold owed at
  next opener.
- DAY-IN-THE-LIFE frame: Track A = Dejan's day narrated; Track B =
  Cobalt 24x5 background, surfaces only when it hands Track A
  something. LAW restated: preferred_windows = fit variable only;
  radar detects and cards fire in EVERY session incl. premarket,
  aftermarket, overnight; personal gates are Dejan's until Guardian
  (advisory). Claude conflated live rules with system design a
  second time; corrected.
- In-play 50 = cap on a ROTATING pool, continuous churn from
  scanners/news/volume/any tracked parameter.
- DAY MODE: Cobalt proposes full/half w/ reason from prior DRC +
  running goal + context/calendar/readiness; Dejan approves or
  overrules w/ reason (persisted); Cobalt sets that risk everywhere
  except the DAS .htk (his hand; match check refuses mismatch).
  Future modes full/half/quarter...; 1%-dynamic much later.
- IF/THEN BRANCHES OUT of MVP: placeholder slot in card + daily
  template for visual context; arrive with the setups engine.
- CARD LIFECYCLE ruled: WATCH (lands at radar_watch/precondition,
  all cobalt fields filled) -> ARMED -> TRIGGERED (strike alert:
  key+shares+stop) -> FILLED (fill-recompute) -> CLOSED/PASSED/
  EXPIRED. Card never lands at trigger. Trigger on an unarmed card =
  missed record, counted not hidden. Card = contract before trigger.
- CONVICTION VIEW: design question = "what do I need to see to pull
  the trigger", not "what does the system need". Entry/sizing needs
  only grade + day mode + trade_def stop; trail type, exits, WHYs =
  trade management. PRE-ENTRY = accept / up / down on a proposed
  key; POST-ENTRY = management view (trail type etc.) then reason
  for up/downgrade; slide-and-reason = optional slow path; reasons
  skipped mid-trade collected at DRC. Cobalt ranks watch cards by
  conviction x proximity-to-trigger, two-up layout.
- PROPOSED GRADE at MVP: computable dots scored w/ WHY, judgment
  dots neutral; amends 08-22 "human fills grade" -> "human RULES
  grade"; his taps = the calibration set. Ladder A+/A/B/C/pass;
  keys outside enabled_grades shown greyed w/ would-be dollars, tap
  records grade, sizes at nearest enabled key, loud (DwV).
- trail_fit = management-view field, human at MVP, cobalt suggestion
  when live bar engine lands, no card change.
- RULES FINE-TUNING MoSCoW: MUST = miss records + nightly benchmark
  query + top-N mover auto-archive; SHOULD = miss-pattern aggregation
  -> proposed config change, only if cheap, else post-MVP (never
  dropped); COULD = replay engine + shadow configs, post-MVP; WON'T
  (MVP) = day-replay dashboard, post-MVP lane.
- TIMEBOX: sittings used 08-26, 08-31, 09-02 = 3 of 5. Sitting 4 =
  feature inventory + MVP MoSCoW + post-MVP MoSCoW by trader-metric
  impact + Expansion Ladder rung criteria; sitting 5 = Charter
  ratification; extension only by explicit call at 5. Card mock ->
  Claude Design between sittings; validation mornings before 5.

- 09-03: v0.7 Code commit DONE (43a0e31 schema/data/tests,
  89b627b docs; 33+199 green, validate 13/13, 30 tunables, ruff
  added). MISMATCH: stop.buffer left as Pydantic constant →
  re-ruled: tunables row, 0.02 preset, per-trade override,
  never hardcoded (follow-up prompt issued). Per-trade tunable
  keys split (hitchhiker.range_duration_band…) accepted; §13.1
  table wording catches up at next bump.
- 09-03 morning prefill silent again (no note, no alert) →
  RULED: Code installs and proves every scheduled job; Dejan's
  only human task at code-done = git push. Heartbeat gains
  "expected plists loaded" probe (backlog).

- 09-03 Code permission posture RULED: auto mode per session
  (Shift+Tab from the Mac terminal; not selectable from Remote
  Control), never bypassPermissions on the host; ask rule
  Bash(git push *) keeps push human; classifier = the zero-trust
  layer between Manual's prompt fatigue and Cline-era auto-approve.

- 09-03 follow-up commits DONE + PUSHED (248b587 stop.buffer rows,
  410b054 ops plists, 1872a34 docs; 37 green, ruff clean).
  ROOT CAUSE of 09-03 silence: both prefill plists loaded but exit 78
  silent — bare `uv` in ProgramArguments (posix_spawn does no PATH
  search); archiver plist had a dead hardcoded uv path AND was never
  loaded. All three fixed to /Users/cobalt/.local/bin/uv, loaded;
  prefill-daily next fire 09-04 05:15, prefill-drc 09-03 15:40,
  archiver 09-03 20:30. Dev-vault kickstart proof passed.
- CONTRADICTION flagged: ledger 08-29/31 "archiver verified running"
  vs never-loaded plist → gap audit + Finviz-window backfill prompt
  issued 09-03 (recoverable only inside the ~2-week minute window).
- Heartbeat probe "every ops plist loaded + last exit code" promoted
  to next build after this audit (silent launchd failure is below
  app-level fail-loud).
- Working tree carries pre-existing uncommitted ASET/prefill/ops
  changes (untouched by Code) — next prompt names them for commit
  or deliberate discard.


### 09-03 (Product Definition sitting 4, closed)
- FOLDED from Code reports: archiver gap audit COMPLETE — 210/210
  tickers backfilled, 1,377,618 rows recovered, nothing permanently
  lost; "08-29/31 archiver verified running" was a documentation
  error (plist never loaded, last real run 08-27). Working-tree
  slices committed + pushed (af83c6f vault gates, 6d7f6b9 2.1a card
  validation, 6104fd6 docs). Docs housekeeping committed on branch
  taxonomy/trade-defs-v0_3, UNPUSHED: 3075b45 taxonomy chain
  v0.2–v0.7 + batches (frozen record; v0.7 = amendment layer over
  v0.4/v0.6, not standalone; v0.8 consolidation queued in BACKLOG),
  e93dcf4 ClaudeClaw kit → 90 - References/claudeclaw-kit (L15
  reference only, never executed) + kashef-mining-memo, 4a85c36
  cheat-sheet rename, finviz-pages commit (redactions verified,
  manifest review closed). Push = Dejan.
- RULED: v0.7 stays the attached taxonomy; no v0.8 bump until the
  consolidation (carries §13.1 wording + stop.buffer re-rule).
- Gemini-era folders: retire old writers, never retarget them into
  the clean tree; read-only writer/folder audit prompt issued,
  per-folder rulings on its report. Interim: Obsidian Excluded
  files hides _archive. gemini-era-vault-side scanned clean,
  commit-for-record then git rm after audit confirms no reader.
- INVENTORY: 45 features from Day-in-the-Life scenes 1–4, each at
  its moment or OUT (sitting-4 chat, ruling 3). Timing corrections:
  Vital Dawn lands 05:30–06:00 or not at all → trigger-based fill
  + loud "no episode today" by config cutoff; prefill refreshes ALL
  DAY on config cadence, cobalt blocks stamped "as of HH:MM"; council
  = the 3-house tribunal at checkpoints 07:15/07:45/08:15/08:45,
  delta vs previous, full view by 09:00; .htk + card risk at 09:00.
- DAY MODE re-ruled: modes = quarter/half/full = 25/50/100% of one
  config max ($430 = daily risk budget) until rolling 1%. Pre-09:00
  = LOWEST enabled sheet by system rule (no stop can rest premarket
  = market mechanics, not a personal gate): half today, quarter
  once it exists, quarter of 1% later. 09:00 checkpoint: Cobalt
  proposes, Dejan approves/overrules w/ reason. Fixed-dollar keys
  per sheet stand (08-28 FINAL).
- MVP MoSCoW RULED (ruling 5). Splits: 19a WATCH-grade detection on
  polled Finviz = MUST; 19b trigger-grade + strike alert = SHOULD-
  pending-spike; single-house narrative at checkpoints MUST, three-
  house council SHOULD (purchase gate). MUST: session clock · radar
  pool 24x5 · heartbeat · prefill all-day w/ ownership flags · two-
  stage day mode + match check · focus list w/ conviction WHY, pick-
  vs-rank logged · card state machine · 19a · card at precondition ·
  dots/ladder/accept-up-down · fill recompute · missed records via
  nightly archiver replay · auto-archive + benchmark + miss line ·
  DRC prefill/reconcile/DRC→mode · prediction records · tunables
  consumers · task integrity minimal · exfiltration guard · CoS-thin
  (one resident session, HITL cards, registry-as-data) · genesis
  import + continuity pack. SHOULD: Vital Dawn · 3-house council ·
  proposed game plan · management view beyond trail+reason · ranking
  two-up · aggregation. COULD: replay + shadow configs. WON'T: X
  lane · Oura · branches · trail_fit suggestion · Guardian · full
  orchestrator · voice/Scribe/widget · day-replay dashboard.
- LIVE FEED RULED (ruling 6): no official TradingView MCP exists;
  community CDP/scrapers ranked below owned feeds. TradeStation API
  OUT ($10K deposit). Massive: free tier = EOD, WebSockets paid-only.
  SPIKE (one Code session before sitting 5): Finviz-lite (5 armed
  names, 10-s loop, freshness + rate) and TradingView Premium
  alert→webhook (Cobalt writes condition, Dejan creates alert, TV
  detects server-side, webhook delivers; lag + extended hours +
  alert slots). Winner = 19b at focus scale. Massive Advanced
  ($160 annual / $200 monthly, non-pros only) = pool-scale post-MVP
  item or fallback if both fail, entered as a $200 one-month spike
  at bar-engine readiness, annual only on evidence; Massive
  Developer ($64, 15-min delayed, 10y minute history) = separate
  corpus-insurance item. Nothing bought before the spike reports.
  Charter gains a data-budget line.
- POST-MVP MoSCoW RULED by trader-metric impact (adherence > exit
  efficiency > selection > expectancy > prep > bandwidth): MUST in
  order — Guardian advisory · Meeting Scribe (cheap: Vital Dawn
  Whisper chain) · 19b pool-scale · corpus insurance. SHOULD:
  trail_fit suggestion · miss aggregation · IF/Then w/ setups
  engine · Drill Candidate Detector · 3-house council. COULD:
  replay+shadow · Oura · Grok X lane · 1%-dynamic mode · voice CoS.
  WON'T: day-replay dashboard · green-light widget. CONSEQUENCE:
  Rules Engine design session moves ahead of orchestrator design.
- EXPANSION LADDER criteria RULED (all config; n<30 = insufficient
  data; demotion symmetric, tripwire = one rung back). R1 push
  size: n≥30 cards · adherence ≥90%/20 days · no breaker/20 days ·
  expectancy >0 at n≥30 · trade-count goal met ≥80% days; two
  consecutive stop-outs = step back. R2 windows (afternoon, then
  premarket): R1 held 20 days · one month green 4/5 days · written
  window plan; premarket adds n≥30 WATCH-only shadow cards first;
  adherence <90%/10 days closes the window. R3 swing: 6-mo review
  passed · intraday expectancy ≥ threshold at n≥100 · swing spec ·
  n≥30 replay drills · size from step-up tripwire. R4 options: R3
  live one quarter at n≥30 · per-setup options expression w/ own
  stop+sizing · Options program complete.
- CLAUDE DESIGN: brief re-issued at close; inputs = sizer HTML + 2
  prebell "today" screenshots; run in an evening (Max meter, no
  extra usage); export → docs/references, sitting-5 attachment.
- TIMEBOX: sitting 4 of 5 closed on agenda. Sitting 5 = MVP Charter
  draft (Claude, top of session) + ratification. Between: spike
  report, audit report, card mock, validation mornings.

- AMENDED at close (ruling 9): inventory +46 trade-note auto-
  creation from cards (slice 2, MUST, corpus writer); +47 Playbook
  PPTX renderer (slice 2b, moment = weekly review / drill session,
  MUST ). Missed at inventory time: not a daily-scene moment.


### 09-03/04 (Incident thread — daily-note overwrite, folded at sitting 5)
- INCIDENT: ASET/prefill fix pass (0dbc207) replaced the 09-02 and 09-03
  daily notes with the template; both recovered by Dejan via Obsidian File
  Recovery. Forensic report docs/00 - Project/INCIDENT-2026-09-03-notes.md
  (writer inventory in §Containment §1 — closes the Gemini-era audit item;
  com.cobalt.agent + archiver write only inside repo docs/, never the vault).
- Root pattern (77d7740): Cobalt DID write 2026-09-04.md at 05:15; Obsidian's
  Daily-notes create-on-open from the trading PC wrote the bare template over
  it at 06:29/06:30 via Sync because the Mac's Obsidian was not running after
  the 15.7.9 reboot. No nightly restart exists on the Mac.
- L28 VAULT-WRITE LAW: create-if-absent · section + unit ownership (markers,
  stable ids, update-in-place) · version every write (vault_writes 30-day +
  vault_overrides non-expiring) · diff in every report · live vault + DB never
  a test target · restart-on-deploy · writers off until proven. Clause 2a:
  Cobalt may fill an empty template cell outside markers (blank → value only).
- L29 MODEL RULE: any Code session on a vault/DB write path, migration,
  delete, recovery or forensics = Opus 5; Sonnet/Haiku non-write mechanical
  only, never auto mode on a write path. Auto mode stays (per session).
- CONTAINMENT f06b34e; FIX DONE (8 commits + ledger, unpushed): one write path
  src/cobalt/vaultwrite/, five write sites converted, ASET status column
  (FILLED on fill-recompute; DRC counts FILLED only), rows 171–185 deleted,
  ADR-0004, 245 green, `cobalt vault restore --write-id N` rollback proven.
- Ruling 7 APPROVED: TWO databases — cobalt_brain live, cobalt_dev for dev-vault
  runs + test suite (transaction rollback); COBALT_ENV unset → fail loud; every
  plist carries it; migration = dump → schema → restore ids preserved →
  checksum → probe round-trip → truncate dev (dump = rollback).
- Ruling 6 RULED: Obsidian "Default file to open" = Last opened on every
  device (per-device setting); Daily-notes plugin stays on; Obsidian on the Mac
  = supervised service (com.cobalt.obsidian, RunAtLoad+KeepAlive, heartbeat
  probe, writer report fails loud "written; not syncing"); Mac Studio boot
  contract = never sleeps · auto-login · lock screen allowed. start_mainframe.sh
  → registered ops job.
- Opus 5 prompt ISSUED 09-04 (after 16:00 ET): env law in code, cobalt_dev →
  cobalt_brain migration, com.cobalt.obsidian agent, mainframe script into
  ops/, boot-contract settings reported. Report pending at sitting-5 close.
- macOS 15.7.9 installed 09-03; Tahoe GATED (L28 proven + one clean week,
  backup with proven restore first — restic → B2 + SSD, NOT Time Machine —
  compatibility check). No vault backup exists today.
- Still his: sudo crontab -l · boot-contract settings · git push.

### 09-04 (Product Definition sitting 5, closed — MVP CHARTER RATIFIED)
- MVP-CHARTER-v0_2.md RATIFIED section by section → docs/00 - Project/
  MVP-CHARTER.md. 13 sections, 23 MUST features F1–F23 with moment +
  acceptance test. Sitting 5 of 5 used; PD phase closed on agenda, no
  extension.
- LIVE FEED (spike 424ce33 folded): both sources pass ≤5 s at focus scale
  (Finviz-lite median 2.2–5.3 s at 10 s poll, TV webhook median 1.71 s).
  RULED (re-ruled from SHOULD after cost review): 19b = MUST at focus scale
  (≤5 armed, Finviz-lite, price-cross trigger only), CAPPED AT ONE WEEK —
  re-measure at 2–3 s cadence first; if throttled, criterion re-rules to 10 s
  cadence (~8 s); at week end whatever is proven ships, rest → post-MVP.
  Data budget at MVP = $0 new. TV webhook = post-MVP SHOULD (free, gated on
  alert-slot cap + extended-hours test).
- STRIKE-ALERT DELIVERY RULED: Mattermost OUT of the strike path (too slow;
  phone fallback only). Channel = ASET Flask sheet grown into the Radar panel
  (reuse plumbing, no new app) + SSE push + browser notification + sound in a
  pinned tab on the trading PC over Tailscale. Trading PC joins Tailscale
  (Dejan). Toast listener = post-week option. No Claude CLI/Desktop on the
  trading PC.
- FILL/EXIT CAPTURE RULED (F11): TRIGGERED shows FILLED @ [price] (prefilled
  last poll, editable) + PASS; every scale-out tap records a leg — mid-trade
  legs at prefilled price flagged `estimated`, final exit `confirmed`;
  realized R provisional until legs confirmed; DRC lists estimated legs for
  one-pass correction; DAS execution-log reconcile = post-MVP SHOULD #1.
  DM/voice fallback line writes the same rows.
- DRC RULED: separate note DRC-YYYY-MM-DD.md, SMB format, prefilled; daily
  note gets a 3-line stub + link only. Pre-slice template review (his docx +
  SMB template → live Templater template). drc_builder PDF render = SHOULD.
  Playbook PPTX = F23, Sunday 18:00 weekly review.
- CARD MOCK v0.1 ratified as design of record; collisions: fixed-dollar keys
  (day budget × grade % = far-future 1%-dynamic runtime only); no quarter
  sheet until ~$1,000+ daily stop, half = premarket floor; single ladder
  #1+#2 open stands over two-up; .htk label check = his. 19a scan cadence =
  tunables radar.scan_interval (60 s start). F6 mismatch REFUSES cards.
  Heartbeat red out-of-band = email (Layer-B OAuth) at MVP.
- Trade-count goal = config band (FILLED, min/max), editable per period along
  his goal timeline; value at the Rules Engine session (daily process goal,
  not P&L).
- §8 item 7 trading-day protection = OPTIONAL practice until MVP (building
  inside the window accepted to reach a buildable MVP sooner); hardens once
  Cobalt assists in building.
- POST-MVP LANE re-ranked: MUST = Guardian → Scribe; SHOULD led by DAS
  reconcile, then TV webhook; BOTH Massive purchases moved to the END behind a
  value gate (large spend; not entered while the interim process covers the
  need).
- MVP acceptance = every MUST passes on live vault + DB over five consecutive
  trading days, heartbeat green, card used in ≥3 live mornings. Then sprint
  ladder RE-DERIVED from the Charter.
- Validation mornings: ASET card used beside DAS every morning (rocky, DB
  writes failed some days, fixed); Radar layout still owed 2–3 live mornings.
- Gemini-era audit CLOSED (folders removed; inventory in incident report).
  Push of taxonomy/trade-defs-v0_3 still owed (Dejan).

### 2026-09-03/04 — INCIDENT THREAD: vault-write (closed 09-04)

Trigger: 09-02 and 09-03 daily notes found replaced by the default
template after commit 0dbc207 (Sonnet). Forensics (Opus, read-only)
inverted the premise: no Cobalt path wrote 09-02; 09-03 was a 44-line
ASET stub at 14:09; the destructive writes (09-02 Sep-2 16:44, 09-03
17:36, 09-04 06:30) were Obsidian — a trading-PC template/buffer
winning through Sync because Mac Obsidian was not running to carry
Cobalt's version. Cobalt did carry a live time bomb (daily.py:483
discarded everything above the stub banner, invisible to tests) and
0dbc207's report asserted a root cause the evidence did not support
and a cleanup that had not happened.

LAWS
- L28 Vault-write law: create-if-absent only (05:15 included);
  section + unit ownership with stable ids, in-place update, human
  text preserved, human-changed line wins + override record;
  deterministic diff, no LLM in the write path; every write versioned
  to Postgres (vault_writes 30-day, vault_overrides non-expiring),
  atomic write + mtime guard; unified diff in every report and run
  log; live vault + live DB never test targets; restart-on-deploy;
  off until proven. 2a: template cell/bullet outside markers may be
  filled only when empty. Carve-out: com.cobalt.archiver (append-only
  run report, nightly batch).
- L29 Model rule: any session touching a vault/DB write path,
  migration, delete, recovery or forensics = Opus 5; Sonnet/Haiku on
  non-write mechanical work only, never auto mode on a write path.
  Enforced twice on 09-04 by the models themselves (time gate; Sonnet
  refusing the migration).

RULINGS
1 writers off until proven · 2 write model (A create-if-absent,
B unit merge) · 3 rows 171–185 deleted; cards ≠ trades — counts use
FILLED only, fill-recompute stamps FILLED on the same row · 4 L28 ·
5 L29 · 6 Obsidian side: "Default file to open" = Last opened on
every device; com.cobalt.obsidian (RunAtLoad+KeepAlive) proven;
heartbeat probe built; writer errors loud when Obsidian is down;
boot contract MET (never sleeps, auto-login on, FileVault off —
accepted) · 7 two databases: cobalt_brain live, cobalt_dev dev-vault
runs + suite (transaction-rollback fixture); COBALT_ENV unset = fail
loud; aset_sizings/vault_* migrated to cobalt_brain, md5-proven ·
8 test residue deleted from cobalt_brain (853 vault_writes, 85
aset_sizings; 92 real cards remain) · 9 bars migrated to cobalt_brain
(4,563,539 rows, md5-proven; +191,939 landed same night), archiver
on the resolver, cobalt_dev empty · Spike (19b): Finviz-lite is the
focus-scale feed (median 2.2–5.3 s); TV webhook (1.71 s) shelved for
pool scale · macOS: 15.7.9 installed; Tahoe gated on one clean week,
restic+B2/SSD backup with proven restore, compat check.

COMMITS (all pushed by Dejan): f06b34e containment · 8 fix commits
incl. fdb7c4a · 77d7740 nightly-restart forensics · 424ce33 spike ·
11 Ruling-7 commits · 4 Ruling-8/9 commits. ADR-0004 (vaultwrite),
ADR-0005 (environment law), ADR-0006 (bars).

OPEN (queued, not blocking)
- TESTARCH row in cobalt_brain.bars — delete next write session.
- bars.ts = ET values under +00 — Data-Model ADR rules it before any
  join; prerequisite for 19b detector.
- No vault/DB backup — restic nightly → B2 + fast SSD; Ansible host
  rebuild playbook. Gates Tahoe.
- Heartbeat host — after slice 2 (probe already built).
- §7 #14 (stub banner into an existing note) unexplained; §7 #9c
  sidecar not adopted (unit merge chosen instead).
- DRC-2026-09-03.md "17 cards" — hand fix.
- Mainframe model unloaded itself ~14:45 09-04; self-heal added,
  cause unknown.
- Tailscale on trading PC — first line of next dev-run prompt.
- rules.yaml (generated_at only) and docs/_archive/gemini-era-
  vault-side/ still uncommitted — ruling pending.
- Spike: extended-hours webhook untested; TV alert-slot cap unread.

09-04 SPRINT LADDER v0.1 derived from Charter §3/§12; order RULED radar (S2) before exits/DRC (S3) — reasoning: no manual substitute for the radar, expectancy corpus must sample the playbook's population, sim/shadow training needs it; S1 foundation → S2 19a → S3 exits+DRC → S4 19b capped → S5 platform; 9 weeks + acceptance week, timebox overrun flagged.

09-04 attestation check = soft, sheet-relative, at fill price — never card-literal; non-blocking prompt only; silent below a share floor; S3 F11.

**Attestation check (ruled 09-04, soft):** at every fill, shares are recomputed for _each sheet's_ key at the actual fill price and the card's stop — never against the card's own count, since DAS sizes at the live price and a share or two of rounding is normal. Only if the filled count sits clearly nearer another sheet's sizing than the attested one (margin = tunables row; sheets differ by ~2×, so ambiguity is real only at tiny counts — below a config share floor the check stays silent) does the card show a non-blocking prompt: "Are you sure you loaded the {attested} key file? {n} shares is closer to the {other} sheet." No refusal, no state change, no grade; dismiss or re-attest; the prompt is logged so the DRC can show it. DAS exposes no loaded-file state, so reading it is not an option; overwriting the default `.htk` per day-mode is a possible future approach, explicitly deferred.

**09-05 HANDOFF to the memory-upgrade build session.** The multi-tenant ruling raised 09-04 (trader-specific settings — enabled sheets, `reduced_enabled_grades`, rung, daily stop, trade-count band, `.htk` template, step-downs — currently live in global config/tunables) is NOT ruled here; it passes whole to the two-layer Data-Model ADR (user data vs system data) so the full scope is visible in one place. That ADR must also place the S1 tables: `day_modes` (user), `card_transitions` (user data about system events), `cobalt_jobs` / `cobalt_kill_switch` / `cobalt_redactions` / `session_blocks` (system), plus `trade_defs` per the 09-05 research ruling (user layer). **S2-P1 (radar pool + Finviz poller) is gated on that ADR** — the radar's tables must land on the right side from day one; the memory-upgrade session owns S2-P1's line 0 and hands the ladder back with the ADR number cited. S1 status at handoff: build complete (P1–P3, 650 tests, smoke green), live acceptance Tue 09-08; ops done — Mattermost off `cobalt_brain` (103/28 split, oracle-proven), backup arming in progress on `/Volumes/COBALT-BACKUP` (SSD leg; B2 pending credentials), Mattermost Postgres role still to create (ruled go, next Code prompt). S3 F11 attestation-check ruling (soft, sheet-relative, at fill price) is on the ladder as pasted 09-05. Open on Dejan: Tailscale on both Windows PCs by 10-19; `.htk` label check before S4; OAuth client walkthrough when P4 is drafted.

_09-05 Mattermost on role `mattermost` (owner of its DB, LOGIN only, CONNECT revoked on cobalt_brain/cobalt_dev, PUBLIC CONNECT revoked); password minted as SCRAM verifier, in .env (bootstrap tier, ruled) + VaultManager, never in transcript; REASSIGN OWNED ruled unsafe — per-object ALTER OWNER instead; 15 s downtime, Postgres container untouched; fence one-directional — next ruling: `cobalt` superuser demotion._

Ledger line: _09-06 SSD dead (enclosure or drive, no enumerate anywhere); replaced by WD Passport Ultra 1 TB HDD, same mount name, repo re-initialised, snapshot + restore proven, heartbeat green; nothing lost — the source was live and the password was in the vault._

### 2026-09-05 — Research session: accelerators, memory, capture (Fable 5.1 chat) — CLOSED
Session type: research. Nothing entered code. Issued 09-05 as LEDGER-APPENDIX-2026-09-05-research.md; pasted 09-08 (had been missed). STATUS AT PASTE: the "pending build-session rulings" below were taken 09-05/06 — user/system law → L32 + R2/R3 (09-05/06 appendix); code-architect spike → Prompt 2's architect-session shape; herdr → adopted 09-06. AGPL question still open.

RULINGS
- R1 RULED — L17 privacy default flipped. Vault and personal layer exposable to any vendor or local model at Dejan's choice; secrets excluded on every channel (F19). Supersedes the 08-29 "personal layer excluded by default" dial; per-case mechanism becomes opt-out.
- R2 RULED — L30 friction law. Remove friction that moves no needle; keep friction that makes the trader (rules, sim, playbook study). Test for every accelerator: which kind does it add or remove.
- R4 RULED (DwV, confirmed) — memory home. `Think/6 - Permanent/Memory/`: INDEX.md (only file loaded by default; one line per file), profile.md, preferences.md, people/ topics/ areas/ living files seeded from the export, export frozen under `_imports/anthropic-2026-09-05/`. Always-loaded block ≤ ~4K chars, enforced by failing the write, never truncation. Provenance on every line; superseded lines marked, not deleted. Consolidation ("dream") = Cobalt nightly job + pre-compact flush in Code, volume-driven cadence; Cobalt-side placement = F21/S5.
- R3, R5 WITHDRAWN. Video-ingestion routing and dictation-plugin spike not ruled; capture/transcription stays research; no spikes on any deck pre-MVP.
- CODE FREEZE (Dejan, 09-05): no Cobalt code outside the Ladder until S1 live acceptance (Tue 09-08) passes. Claude holds him to it.

PENDING BUILD-SESSION RULINGS (as issued; see STATUS above)
- User-data vs system-data law: system = schema/engine making any trader's strategies pluggable (taxonomy anatomy, card engine, radar, alerts); user = named trades and cheat-sheet-derived content, his strategies/settings, SMB-derived material, Oura/psychology/DRCs/Memory — never shipped or visible to other users. Consequences: trade_defs batches leave the repo for the user layer; Data-Model ADR becomes two-layer; naming pass over the taxonomy; trade names not baked into system code.
- AGPL acceptability for the product line (gates Honcho-class components).
- Code-architect spike: read-only role pack, plan mode, L29, Fable 5.1; first task = the two-layer ADR.
- herdr test after acceptance.

CANDIDATE VERDICTS (research, not rulings)
- Honcho — PARK: patterns extracted (provenance per memory, domain as tag not partition, peers first-class, scheduled conservative consolidation, levels of recall); component rejected (own always-on LLM workers; AGPL).
- Screenpipe — REJECT on the Cobalt host (24/7 recorder of the secrets machine; licence now source-available). Pattern kept under L15: event-driven capture + accessibility tree over OCR.
- HoverNotes — research only (cloud Gemini generates the notes, closed source).
- Obsidian local-Whisper class (Audio Transcription, Local Dictation, Minute) — research only; DRC dictation candidate; human-side.
- Meeting front-ends (Meetily, Anarlog, OpenWhispr, Vibe, Scriberr) + engines (whisper.cpp, faster-whisper, WhisperX, Parakeet) — research only; Kashef kit stays the reference.
- Obsidian Web Clipper + Interpreter (Defuddle → Turndown; Interpreter on local model) — the capture reference; Defuddle usable headless by Cobalt.

STANCES RECORDED (Dejan's, his risk)
- SMB material: personal-use rights to everything he acquired; method of acquisition doesn't limit use; never sold or shared. Claude's repeated "not SMB" caution withdrawn.
- Capture: never downloads video from anywhere. Method = web-clip pages (SMB, Discord, X) + still-frame screenshots of paused video + local summarization into linked markdown. Principle: a bot doing exactly his browser steps logged in as him = his hand. Tool-vs-build per site decided by that site's terms, as a design feature.
- Transcription targets: SMB training, SMB real-time, X — via Cobalt or a Grok bot feeding Cobalt.

OPEN ITEMS
- Memory export complete (21 files, three parts). Research note filed: docs/30 - Design/RESEARCH-2026-09-05-memory-and-capture.md.
- Timeline: two-layer ADR costs S1 ~1–2 mornings now vs ~a week after S2. Cobalt-side memory = S5, not before.
### 2026-09-05/06 — Memory-upgrade build session (Fable 5.1 chat, Dejan as CTO) — CLOSED
Session type: build (documents + vault hand-work). Code freeze intact: nothing entered Cobalt code.

RULINGS
- R1 DONE — memory home `6 - Permanent/Memory/`: INDEX/profile/preferences (always-loaded block 3,993 chars, cap 4,000 held) + people/topics/areas living files; export frozen at `_imports/anthropic-2026-09-05/` (21 files, one level). preferences.md = terse rules only; reasons/history in `topics/working-contract.md`. Provenance on every line; undated export lines = `[stated ≤2026-09-05 · export]`. Cobalt-side (budget enforcement, consolidation job, pre-compact flush, MCP exposure) = S5/F21, not before.
- R2 RULED A — two-layer Data-Model ADR tenancy: one DB `cobalt_brain`, Postgres schemas `system` + `user`; `user_id NOT NULL` + FK on every user table; per-schema grants (wrong-side query fails loud); search_path in the one connection factory; suite test asserts every table sits on exactly one side; tunables split (engine rows stay, trader rows → `user.trader_settings`). Placement: user = trade_defs, day_modes, card_transitions, cards, legs/fills, missed records, vault_writes/overrides, DRC rows, trader_settings; system = bars, radar pool/membership, taxonomy anatomy objects, cobalt_jobs, kill switch, redactions, session_blocks, heartbeat.
- R3 RULED A — ownership by unit, not by folder (L28 generalized): Cobalt owns no folders in the human vault tree; it owns marked units inside notes, plus Postgres, the repo, `_imports/`. trade_def = `cobalt:section definition` unit INSIDE each `1 - Trading/4 - Strategies/<Trade>.md`; shared key = frontmatter `trade_def:` slug (lowercase kebab, no `$`, no leading digit) carried by strategy notes, trade notes (F22), DRC rows, DB; vault note = truth, DB = loaded validated copy (config-as-code). Repo ships ONE synthetic anatomy-only example def; the 13 committed YAMLs leave the repo after md5 proof. `status: draft → defined → playbook` (playbook earned at n≥30, never typed).
- R4 RULED A + DONE — full 22-slug strategy-note set created by Code (Opus, vault only): 4 amended in place (prose byte-identical; one typo fix `Second Chance Scalp.md strategy:`), 18 created, 13 Definition units populated from committed v0.4 defs, 9 draft, `5 - Templates/Strategy.md` Templater. Report: `40 - DevDocs/reports/strategy-notes-2026-09-06.md`. Rollback = restic snapshot 09-05 21:40 (notes pre-date the edit). A Sonnet run refused the task per L29 — correct behaviour, recorded.
- L31 Names rule — person or vendor names never in code identifiers, schema, config keys, enum values or system design docs (cite the artifact, e.g. "setup×trade matrix", never the author); citations live in reference material and user data only. Known offender: `cameron_grid` in code → rename in ADR-0008 spike.
- herdr VERDICT — adopted as interactive Claude Code host, tmux retired to fallback (installed, not running). Passed: multi-session visible in the app with no /rc typed (Claude Code 2.1.263 auto-starts remote control); idle/working/blocked detection accurate and JSON-queryable (`herdr agent list`); SSH reattach + `herdr --remote` thin client from Fedora with text AND image paste (replaces VNC for Code work); server restart restored 1 of 2 panes (other = one `claude --resume`). Rule kept: never rely on restore — state to vault/DB before `/clear`. One seat now: herdr tab `Claude1` in ~/cobalt = the /rc-exposed session. SESSION: fresh still = `/clear` in that seat.

FINDINGS
- Claude Code 2.1.263 runs a background daemon (`claude.exe daemon run`) hosting app-spawned forks independent of any terminal, with a spare-process pool; "the seat" = daemon + transcript, not a terminal. Forks spawned by the desktop app ran `--permission-mode auto` with computer-use tools allowed — Dejan's settings decision before Prompt 2 runs in auto mode.
- Empty paste into an auto-mode pane = "do something": the session freelanced (messaged a peer session, diffed the ledger, considered editing it). Rule: never paste without a text instruction.
- Repo is on branch `ops/triage-2026-09-06` with ~279 uncommitted PROJECT-LEDGER.md lines — Dejan: `git status`, commit or discard before Tuesday.
- L28 and L29 exist only in appendix blocks — fold into §1 Laws Register at next paste (this appendix adds L31).
- Claude Code tabs can spawn/call other Claude, Codex or local-model sessions — input to the S5 F20 orchestrator/chassis design (L16/L22), not a ruling.

CODE PROMPTS
- Prompt 1 (strategy notes) — DONE 09-06.
- Prompt 2 — ISSUED, gated on S1 live acceptance 09-08: architect session (plan mode, read-only, rulings a–g one at a time) → Opus subagent: ADR-0008 (tenancy A, table placement, vault-backed trade_def loader, slug re-key, 64 trade-note `strategy:`→`trade_def:` migration with L28 write records, `category:`→schema field, names rename), S2-P1 line 0 rewritten citing ADR-0008.
- Prompt 3 — OWED post-freeze: herdr server as ops-registered launchd job (RunAtLoad, heartbeat probe), named session for the seat.

OPEN ON DEJAN (I think these are already done, check in text above, ask me at session start if done and tell me to remove this message so it does not become task for each new session)
- git status / branch decision (above) · desktop-app computer-use grant on spawned sessions · RESTIC_PASSWORD into a password manager off both devices · S1 live acceptance Tue 09-08 · B2 credentials for the offsite leg. 
  

### 2026-09-06/07 — Seats & Ops workstream (Fable 5.1 chat, Dejan as CTO) — CLOSED
Session type: standing SEATS workstream — outside the Ladder, free-time, no sprint budget
(ruled 09-07). Code freeze intact for Cobalt code; ONE exception ruled 09-07: ops incident
fix (mainframe crash loop). All Code work reported, none committed; Dejan pushes.

A. HERDR ADOPTED (09-06) — replaces tmux as the interactive Claude Code host.
- Passed: multiple sessions visible in the desktop app with no /rc typed (Claude Code
  2.1.263 auto-starts remote control); agent state idle/working/blocked accurate and
  JSON-queryable (`herdr agent list`); SSH reattach + `herdr --remote cobalt@cobalt`
  thin client from Fedora with text AND image paste bridged (replaces VNC for Code work);
  server restart restored 1 of 2 panes (other = one `claude --resume`).
- One seat = herdr tab Claude1 in ~/cobalt = the /rc-exposed session. SESSION: fresh
  still = /clear in that seat. tmux installed, not running, fallback only.
- Rule kept: never rely on restore — state to vault/DB before /clear.
- Finding: Claude Code 2.1.263 runs a background daemon (`claude.exe daemon run`) with
  a spare-process pool; desktop-app sessions are forks of a transcript hosted there,
  independent of any terminal. "The seat" = daemon + transcript. App-spawned forks ran
  `--permission-mode auto` with computer-use tools allowed → Dejan's settings call.
- Rule: never paste into an auto-mode pane without a text instruction (an image alone
  made a session freelance: messaged a peer, diffed the ledger, considered editing it).
- herdr server as an ops-registered launchd job (RunAtLoad + heartbeat probe) = Prompt 3,
  post-freeze.

B. SEAT LAW (ruled 09-07, "my repo, my rules") + L29 AMENDMENT
- Any agent house may hold any seat, including write paths. No house privileged, Claude
  included. Two tests per seat: (1) the house's top implementation model or higher on
  writes — L29 restated as a house-agnostic FLOOR (Opus floor for Claude; Fable, available
  in Claude Code, on writes at Dejan's call per prompt); (2) a permission gate proven to
  stop file AND command writes in a scratch test before the seat stands.
- Plans, not API: every human-facing seat runs on the house's consumer plan (Max / Google
  AI Pro / ChatGPT Plus / SuperGrok). API keys are for Cobalt's engine under L27.
- Seat test standard (used 4×): auth persists headless · strictest-mode file + command
  gates hold · default-mode gate recorded · features (context file, skill, hook, MCP,
  subagent-by-trace, plugin, model switch, web search) · herdr detection per approval
  type · cleanup with rc-file hashes unchanged. Reports in 40 - DevDocs/reports/.

C. SEATS — verdicts and standing rules
- agy (Antigravity CLI 1.1.27, Google AI Pro, tab Gemini1): ELIGIBLE. Gemini CLI no
  longer serves personal plans (since 06-18). All features PASS; global hooks fire
  headless, project-local ones interactive only. herdr misses agy FILE-WRITE approvals
  (manifest wants "requesting permission for:"; file cards say "Allow creation of this
  file?") → shows idle. Rule: file-edit work in agy watched in-pane or headless
  (headless auto-denies). Upstream issue to file. Installer edits shell rc → next time
  `agy install --skip-path --skip-aliases`. agy's /model also offers Claude models on the
  Google plan (noted, no decision).
- codex (0.153.4 Homebrew, ChatGPT Plus, GPT-6 Astra default `gpt-6-astra`, reasoning
  none…max, tab Codex1): ELIGIBLE with rules: NEVER launch bare (defaults don't gate
  workspace writes) — always `-a on-request` with `-s read-only` (review) or
  `-s workspace-write` in a worktree (writes); `--approve-for-me` BANNED on Cobalt seats
  (an LLM judge auto-approved `curl | sh` with network on; there is no separate Astra
  safety pause on this plan); Codex sub-agents/delegation BANNED in Cobalt flows
  (reported "SUB-OK" from a sub-agent that never spawned — empty wait, fabricated
  result). herdr detects both approval types via window title (OSC) not hook →
  re-verify after every Codex upgrade. Editing ~/.codex/hooks.json invalidates its
  trusted_hash and Codex silently disables the herdr hook. Cloud tasks UNTESTED (no env).
- qwen / local (Qwen Code 0.23.0 npm, LM Studio OpenAI-compatible endpoint, tab Qwen1):
  ELIGIBLE, WORKER ROLES ONLY, never a write path (L29 floor is cloud top-tier).
  9/9 tool calls correct, 0 malformed, 0 hallucinated, 0 fabricated success; two-step
  4/4; 3/12 raw losses were the server crashing (see E). Read-only worker until the 27B
  shows 24 h clean. Harness pick: Qwen Code (first-party, Gemini-CLI lineage, herdr
  `qwen` hook); OpenCode = alternate; Hermes = reference architecture, NOT installed.
- grok (Grok Build CLI 1.0.13, SuperGrok acquired 09-07, tab Grok1): ELIGIBLE. Edit
  gates hold in plan AND default; default's risk classifier auto-approves benign shell
  commands (`touch` ran, `rm` asked) → seat launches `--permission-mode plan` (review)
  until the sandbox works; `--sandbox read-only` currently refuses to start because the
  profile can't resolve OrbStack's /var/run/docker.sock symlink (fail-loud, correct) →
  custom ~/.grok/sandbox.toml = Prompt 4. Grok INHERITS Claude Code config by default
  (skills/rules/agents/MCP/hooks/SESSIONS; a Claude hook fired inside a Grok run) → switch
  all Harness Compatibility toggles OFF (Prompt 4). Plugin PreToolUse hooks don't fire in
  1.0.13. Installer edits ~/.zshrc → run with SHELL unset. X search PASS in-seat (5 posts,
  x.com citations, 24 s, subscription login).
- Local model throughput on the 122B (pre-swap): ~55 tok/s decode, ~606 tok/s prefill,
  4.8 s TTFT floor; 27B numbers in the swap report.

D. COS / ORCHESTRATION RULES (ruled 09-07; laws to number at fold, after L31)
- Hub, not group: Cobalt code is the hub (L22). Deliberation is free; execution is
  accountable.
 1 CoS calls ROLES, never flags or binaries; roles are fixed launcher profiles
   (reviewer = read-only no network; writer = workspace-write in a worktree, on-request;
   researcher = read-only + web).
 2 Every spawn = a cobalt_jobs row: house, role, model, worktree, required artifact.
 3 Completion = artifact verified by the hub (tests, diff, log). A worker's own claim is
   never accepted. ("Trust the artifact, never the report.")
 4 No worker spawns workers; CoS is the only planner, the hub the only spawner.
 5 No model-judged approvals anywhere (`--approve-for-me` and equivalents banned);
   approvals are Dejan's or deterministic rules.
 6 Peer asks are free; acts are jobs. Any agent may ask any other BY ROLE; all asks
   route through the hub and are logged; an ask implying a side effect becomes a job for
   the expert that owns that side effect, under that path's gate.
 7 Council 3-turn rule: a council answers in ≤3 turns — agree, or vote on turn 3 with
   dissent recorded in the artifact. No fourth turn; unresolved → escalate to Dejan.
 8 Expertise is owned, not shared: each side effect (vault writes, DB writes, orders,
   alerts) has exactly one expert role; others reach it by asking, never by doing.
- Council = a hub job type (first instance: the 4-house tribunal): hub opens a room,
  seats N models with a question + turn/token budget; artifact = the room's output.
- Memory infusion (Part C inventory, all four harnesses): every harness re-fires its
  start hook on clear and none preserves the session id → /clear is a clean re-infusion
  point everywhere; only claude and qwen expand @-includes, so one pointer file cannot aim
  all four at 6 - Permanent/Memory/ → the start HOOK is the portable route (and the only
  one that can call the vault resolver); agy's event is PreInvocation (per model call) and
  it reads no instruction file without --add-dir. Design item for the F21 spike.
- xAI engine path (Part B PASS): Cobalt's own xAI adapter = bearer from ~/.grok/auth.json
  (file, 0600) → POST https://api.x.ai/v1/responses
  {"model":"grok-4.6","input":<q>,"tools":[{"type":"x_search"}]}; read
  output[message].content[].output_text + annotations[url_citation]. Requirements: cite
  ONLY from annotations (reasoning block fabricated five post IDs); handle expires_at +
  refresh_token; BILLING UNCONFIRMED — response carried cost_in_usd_ticks and the token a
  team_id → Dejan checks the xAI console before anything schedules; if it bills, the
  adapter runs on an explicit XAI_API_KEY under L27. Build as OAuth-preferred / key-
  fallback (Hermes pattern), xAI as a second base URL on the OpenAI adapter.

E. INCIDENT — mainframe crash loop (found 09-07 during the local-seat test)
- Truth on 09-07 morning: `mainframe` = qwen3.5-122b-a10b MLX 4-bit 69.6 GB on all four
  layers (server, ops job, router, disk). No 27B/3.8 existed on the host; the 09-04 ops
  note recording the 27B as serving was WRONG (intention filed as fact). CLAUDE.md model
  line wrong on every clause.
- Since 09-04 14:45: ~800+ SIGSEGV crashes of LM Studio's MLX worker ~340 s after every
  load, traffic-independent; heartbeat self-healed in ~24 s; L23 probe green (bare TCP).
  Runtime was mlx-llm 1.3.0 with 1.11.0 available. Separate defect: heartbeat `curl
  --max-time 30` < normal generation (33–41 s) → false DOWN + reload of a healthy model.
- Triage (Sonnet, read-only + bounded, per triage rule): H1 heartbeat confirmed-narrow
  (10 of 820), H2 idle-TTL ruled out (3600 s), H3 memory ruled out, H4 competing job
  ruled out. F1 = timeout 120 s + cheap liveness; inference probe KEPT as the reload
  trigger (model endpoints report "loaded" straight through a crash — Claude's literal
  spec would have broken self-heal; Code's deviation accepted).
- Ruling 2 (A amended): runtime 1.3.0 → 1.11.0 + swap to mlx-community/Qwen3.8-27B-8bit
  in one restart, 122B kept on disk until 24 h clean.
- SWAP LIVE 09-07 21:36 EDT: mainframe = qwen3.8-27b (8-bit, 29.5 GB, pulled from
  Hugging Face — LM Studio's hub carries only the 4-bit), engine 1.11.0 proven in the
  live worker, context 262144 (KV ~17 GB; only 16/64 layers full attention), load 10 s,
  F1 active, E4 fixed (config.yaml context = served). MTP head (253 MB draft model, not a
  standalone) downloaded, NOT wired (Prompt 5 benchmark). A 4-bit lmstudio-community
  build landed by accident (kept, no-deletion rule).
- Self-inflicted outage 21:31:52–21:36:22 (4.5 min): `lms load` blocked on an interactive
  "3 models match" menu under launchd — LATENT DEFECT in the original script (122B key
  was unique); fixed with `-y` + fail-loud post-load check on arch+quantization.
- reasoning_effort, enable_thinking AND a no-think system prompt are all ignored on the
  27B: thinking always on, inlined in content → Cobalt's local-tier adapter must strip
  <think>…</think>; report useful tok/s post-strip (ADR item, Tuesday).
- 30-min soak, throughput, tool-calling on the 27B: PENDING → swap report
  40 - DevDocs/reports/mainframe-swap-2026-09-07.md (morning). 122B deletion = ruling
  after 24 h clean. heartbeat.log 9 MB of spinner output → follow-up.

F. CODE PROMPTS
- DONE: Prompt 1 strategy notes (09-06) · agy seat · codex seat · local seat + Part B/C ·
  mainframe triage · mainframe swap (soak pending) · grok seat + X-search adapter proof.
- ISSUED, gated on 09-08 acceptance: Prompt 2 — architect session (plan mode, rulings a–g
  one at a time) → Opus subagent: ADR-0008 two-layer data model, vault-backed trade_def
  loader, slug re-key, trade-note migration, names rename.
- OWED post-freeze: Prompt 3 herdr launchd job · Prompt 4 seats follow-up (grok
  sandbox.toml + Claude-inheritance off; agy herdr manifest issue upstream; codex OSC
  re-verify; CLAUDE.md model line) · Prompt 5 MTP speculative-decoding benchmark
  (with/without table) · local adapter <think> strip (ADR-0008 item).

G. FIREWALL NOTE (coaching lane, not for code): 09-07 weekly review retired rule 10 and
  replaced it with a two-position rule; rules.yaml prefill picks up the card as usual —
  no code change unless Dejan rules one.

H. OPEN ON DEJAN
- git: repo on ops/triage-2026-09-06 with uncommitted PROJECT-LEDGER.md lines (~279) and
  the 09-07 ops/ + config.yaml edits — commit or discard BEFORE Prompt 2.
- Fold L28, L29 (amended), L31 + D-rules into §1 Laws Register at this paste.
- xAI console billing check · desktop-app computer-use grant on spawned sessions ·
  RESTIC_PASSWORD off both devices · B2 credentials · S1 live acceptance Tue 09-08.

- SOAK PASSED 09-07 22:25 EDT: 29/29 probes, 0 failures, 0 reloads, 0 crash reports; by
  23:02 82/0 heartbeats, worker uptime 1h27 continuous (122B died every ~5.8 min). E1 CLOSED.
- 27B vs 122B: decode 22.1 vs 55.4 tok/s (2.5× slower — dense 27B reads ~27 GB/token vs MoE
  ~5 GB); TTFT 0.82 s vs 4.76 s (short), 1.22 s vs 11.6 s (4K); prefill 10,419 vs 606 tok/s
  (17×); tool-calling 14/14 valid glob calls, 0 malformed, 0 hallucinated, 10/10 exit 0, 0
  runs lost to crashes (122B lost 3/12). Net: better worker for read-heavy/tool work, slower
  for long generation; max_tokens now costs ~2× wall clock.
- MTP speculative decoding NOT AVAILABLE: LM Studio raises
  SpeculativeDecodingNotSupportedError for batched MLX models; `--parallel 1` escape untested
  (needs a maintenance-window reload). CLAUDE.md's "with MTP speculative decoding" describes
  a config LM Studio won't serve. `reasoningParsing` does nothing on this build; SDK gotcha:
  Python SDK strips the opening <think> tag but keeps the closing one — strip logic must
  handle both endpoint and SDK shapes.
- Memory truth: 103 GB total, ~46 GB usable with the 27B loaded; no second 29.5 GB instance
  on the production box.


- **L17 amended (09-05) — privacy default flipped:** vault and personal layer are exposable to any vendor or local model at Dejan's choice (opt-out, not opt-in); secrets excluded on every channel (F19). Supersedes the 08-29 "personal layer excluded by default" dial.
- **L28 Vault-write law (09-03/04):** create-if-absent only (05:15 included — never replace-once) · Cobalt writes only inside marker-bounded sections as units with stable ids (same id = update in place; human text preserved verbatim in position; a Cobalt line he changed → human wins, logged as override) · deterministic diff, no LLM in the write path · every write versioned to Postgres (vault_writes 30-day, vault_overrides non-expiring) · diff in every report · live vault + live DB never a test target · restart-on-deploy (a config-shape change and its service restart are one action) · writers off until proven on the dev vault with a diff. Clause 2a: Cobalt may fill an empty template cell outside markers (blank → value only, versioned). Generalized 09-06 (R3): ownership by unit, never by folder — Cobalt owns no folders in the human vault tree; it owns marked units, Postgres, the repo, `_imports/`.
- **L29 Model rule (09-03/04, amended 09-07 seat law):** any Code session touching a vault/DB write path, migration, delete, recovery or forensics runs on the house's top implementation model or higher — Claude: Opus 5 floor, Fable at Dejan's call per prompt. Any house may hold any seat, write paths included, once (1) that floor is met and (2) a permission gate is proven in a scratch test to stop file AND command writes. Sonnet/Haiku and their equivalents: non-write mechanical work only. Auto mode stays, granted per session, never blanket. Human-facing seats run on consumer plans; API keys are for Cobalt's engine under L27. No house privileged, Claude included.
- **L30 Friction law (09-05):** remove friction that moves no needle; keep friction that makes the trader (rules, sim, playbook study). Every accelerator is tested on which kind it adds or removes.
- **L31 Names rule (09-06):** person or vendor names never in code identifiers, schema, config keys, enum values or system design docs — cite the artifact ("setup×trade matrix"), never the author. Names live in reference material and user data only. Known offender `cameron_grid` → rename in ADR-0008.
- **L32 User-data / system-data law (09-05, tenancy 09-06):** Cobalt-the-system = only the schema and engine that make any trader's strategies pluggable — taxonomy anatomy (regime, range, gap, extension, leg, session clock: common trader knowledge), card engine, radar, alerts, rules-engine schema. User data = named trades and trade_def content, strategies/settings, anything SMB- or cheat-sheet-derived, 1 - Trading (DRCs, playbooks, trades, research), Oura/psychology, the Memory folder — never shipped to or visible to other Cobalt users; other users build their own. Tenancy (R2): one DB `cobalt_brain`, Postgres schemas `system` + `user`, `user_id NOT NULL` + FK on every user table, per-schema grants (wrong-side query fails loud), search_path set in the one connection factory, suite asserts every table sits on exactly one side. Repo ships one synthetic anatomy-only trade_def; the vault note is truth, the DB row a loaded validated copy. ADR-0008 implements.
- **L33–L40 Hub law (09-07) — Cobalt code is the hub (L22); deliberation is free, execution is accountable:**
  - **L33** CoS calls ROLES, never flags or binaries; roles are fixed launcher profiles (reviewer = read-only, no network; writer = workspace-write in a worktree, on-request; researcher = read-only + web).
  - **L34** Every spawn = a `cobalt_jobs` row: house, role, model, worktree, required artifact.
  - **L35** Completion = artifact verified by the hub (tests, diff, log); a worker's own claim is never accepted — "trust the artifact, never the report."
  - **L36** No worker spawns workers; CoS is the only planner, the hub the only spawner.
  - **L37** No model-judged approvals anywhere (`--approve-for-me` and equivalents banned); approvals are Dejan's or deterministic rules.
  - **L38** Peer asks are free; acts are jobs. Any agent may ask any other BY ROLE; asks route through the hub and are logged; an ask implying a side effect becomes a job for the expert that owns it, under that path's gate.
  - **L39** Council 3-turn rule (amends L17): a council answers in ≤3 turns — agree, or vote on turn 3 with dissent recorded in the artifact; no fourth turn; unresolved → Dejan. Council = a hub job type (first instance: the 4-house tribunal).
  - **L40** Expertise is owned, not shared: each side effect (vault writes, DB writes, orders, alerts) has exactly one expert role; others reach it by asking, never by doing.


- 09-08 S1 LIVE ACCEPTANCE — GREEN. One live session on the ASET sheet with the new controls: attestation + rung→sheet gating applied; cards ARMED→TRIGGERED→FILLED on a real trade; daily note intact (no overwrite); heartbeat green (12:05, 11 jobs / 9 probes). S1-P4 email channel landed the same day (F18 proven RED→GREEN in production, DM + email). CODE FREEZE LIFTED. S1 delivered 09-04/08 vs 09-18 plan — ~10 days of slack; S2 starts on ADR-0008 done, not 09-21. Friday's 4 FILLED cards needed a manual CLOSE (expected until F11). Known debt: OAuth app in Testing status → refresh token expires ~09-15 unless Publish succeeds and email-auth is re-run.