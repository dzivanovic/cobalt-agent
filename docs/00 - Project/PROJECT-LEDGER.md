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