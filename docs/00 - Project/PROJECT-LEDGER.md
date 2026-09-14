# COBALT PROJECT LEDGER
The living record of decisions, laws, and project state. TRIAGE.md (20 - Assessment/) is the frozen triage record; this ledger carries everything after it. Updated by appendix blocks from planning sessions, pasted by Dejan, folded by Code.
Started: 2026-08-28 · Covers: 2026-08-22 → present

---

## 1. LAWS REGISTER (cross-cutting, binding on all work)
[2026-09-13] Current law is `6 - Permanent/Memory/LAWS.md` as of 2026-09-13; this register is the fold record — a ruling below is not law until the hub folds it into LAWS.md.

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
- **L25 amended (09-09) — Cloud fallback is an exception handler, not a route:** permitted only for an UNFORESEEN local failure (crash, host down, unrecoverable timeout) and bounded: every fallback logs a reason class (crash / timeout / capability / quality), is counted per class in the seat-usage report, and turns the heartbeat AMBER when a class recurs on the same day. A recurring class becomes a fix ticket with an owner before the next sprint; it never stays a route. A KNOWN local defect never gets a cloud bypass — fix local, or move that task class to cloud explicitly in ADR-0008's bake-off table, by ruling, not by fallback. Disaster continuity (host dead) is the one open-ended case, bounded by the rebuild. L23 is the directive; L25 is its exception handler, not its replacement. (Reason-class column in the seat-usage report = Ops report ESCALATE, not the 09-09 build.)
- **L28 amended (09-09) — sync-revert carve-out to human-wins:** when the on-disk unit text differs from the baseline but equals any of Cobalt's last 10 `unit_after` values for that unit, the change is a SYNC REVERT (Obsidian Sync putting an older Cobalt write back), not a human edit: Cobalt's new text wins, no override rows, the write row records `sync_revert_of = <matched write id>`, one loud log line. Known false positive, named: a human manually restoring a byte-identical copy of one of those 10 blocks is overwritten — visible after the fact through `sync_revert_of`. Ruled from the 09-09 heartbeat-unit evidence (writes 2127/2132 identical). LIVE in production 17:12 09-09 (migration 0004).
- **L33 note (09-09):** the Codex reviewer launcher is `codex exec -m <model> -s read-only` — `codex exec` takes no `-a/--ask-for-approval` (TUI-only flag); "never bare" for exec means the sandbox flag. Headless Grok and agy auto-deny shell commands: a reviewer task must be answerable from reads alone; hashing/verification belongs to the hub (L35).

## 2. DECISION LOG (dated, one line each)
[2026-09-13] Decisions after 08-31 are in the appendices below, not in this section.

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
- ~~**In build:** Slice 2 — DRC/playbook prefill (kickoff Mon 5:30, fresh session): prefill engine → Templater templates (in 90 - References) + trade-reporter renderers; day-mode line + .htk-match check; re-entry/excitement fields; rule-adherence checkboxes.~~ [struck 2026-09-13, stale — Slice 2 shipped long ago; current build state is the 2026-09-13 S2-P1 LIVE appendix above; §3 refresh owed at next session close]
- ~~**Next builds:** prebell-lite (2–3 wks thin, iterate) · exfiltration guard (small) · Agent SDK spike (at orchestrator design).~~ [struck 2026-09-13, stale — build lane order superseded, see appendices; §3 refresh owed at next session close]
- ~~**Named future agents:** Chief of Staff (one throat) · specialists per registry (L16) · Guardian (real-time rules; gated on Rules Engine + grading/EV + alerting; DAS-native check may shrink scope) · Research Analyst (§8 engine) · Meeting Scribe (post-MVP must-have) · Drill Candidate Detector (feeds Rubberband training from archiver corpus) · Coach/DRC/Logistics (running now as manual chat fleet: planning+coach=Fable, DRC+logistics=Sonnet). Grok role elevated (08-29/31): X-lane specialist (native X access), primary role over council/review seat secondary — proving ground is the Grok Bot pilot.~~ [struck 2026-09-13, stale — "manual chat fleet" superseded by the L34 job-row/house registry now in force; see 2026-09-13 appendix; §3 refresh owed at next session close]
- ~~**Design sessions pending:** Trading Taxonomy (FIRST — needs scheduling; absorbs variable registries) · Data-Model + Vault-remainder weekend block (schema ADR, embedder ADR, DB-split, memory-v2 mechanisms input) · Product Definition sittings → MVP Charter (~2-month usable target) · Rules Engine (post-Charter, gates Guardian) · Orchestrator design (Agent SDK spike + council + registry).~~ [struck 2026-09-13, stale — Taxonomy sat 09-01/09-02 through TAXONOMY-DRAFT-v0_7 (LEDGER:379); §3 refresh owed at next session close]
- ~~**Cross-house bridges live (08-29/31, build-time tooling, not agents):** Codex plugin (ChatGPT subscription, local Codex CLI login) + Grok Build plugin (SuperGrok, local grok CLI login) — repo-code-only review/rescue tools; vault/.env/personal layer excluded (L15 external-code-law carve-out for first-party vendor tools). Runtime distinction (L-architecture ruling, 08-29/31): SDK sessions = resident agents; Cobalt headless runners = stateless CLI invocations wrapped in Cobalt task machinery; vendor bridge plugins = build-time only.~~ [struck 2026-09-13, stale — the "vault/.env/personal layer excluded" clause is superseded by L44; see LAWS.md L15 and LAWS-HISTORY H-L15-scope (O31); §3 refresh owed at next session close]

## 4. STANDING QUEUE / OPEN ITEMS
- ~~Dejan: Phase B Finviz page captures (Stock "Learn More" panel = the date-range mystery) → 90 - References/finviz-pages/ · SMB permission email (+ transcripts line) · DAS native-enforcement check · schedule Taxonomy sitting (by ~09-06) · templates → confirmed in References · corrected .htk files to 60/135 · delete stray "test note" · purchase decision on SuperGrok/ChatGPT.~~ [struck 2026-09-13, stale — Taxonomy sitting held 09-01/02; SuperGrok acquired 09-07 (LEDGER:907); §4 refresh owed at next session close]
- ~~Claude: slice-2 kickoff prompt (ready Mon 5:30, issued 08-31) → now slice-2 review + next assembled prompt · ledger appendices at session close · continuity-pack authoring sessions (pre-MVP) · September contracting one-pager.~~ [struck 2026-09-13, stale — slice-2 long shipped; current OWED queues are in the 2026-09-13 appendix above; §4 refresh owed at next session close]
- ~~Verify: archiver nightly runs (archiver-runs.md, verified running unattended 08-29/31) · planning cap clock (started 08-22; Taxonomy + PD sittings must land within it or cap is re-ruled — Taxonomy window commitment: ~09-06).~~ [struck 2026-09-13, stale — "archiver verified running unattended" was itself revoked as a documentation error (LAWS-HISTORY H-Archiver); planning cap disposition now at LAWS.md L12/H-L12 (O4); §4 refresh owed at next session close]
- ~~Build lane order (08-29/31): slice 2 → health-check heartbeat → prebell-lite → exfiltration guard → orchestrator design (Agent SDK spike, headless runners, registry, councils).~~ [struck 2026-09-13, stale — superseded by the actual build sequence recorded in later appendices (S2-P1 radar shipped ahead of prebell-lite); §4 refresh owed at next session close]

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



### 2026-09-08 — S1 acceptance + release planning (Fable 5.1 chat) — CLOSED
RULINGS
- R1 S1 LIVE ACCEPTANCE GREEN; CODE FREEZE LIFTED 09-08. S1 delivered 09-04/08 vs 09-18 plan; S2 starts on ADR-0008 done (done 09-08 17:55), not 09-21.
- R2 122B deletion: after 24 h clean (~21:36 09-08), folded into Prompt 5 — NOT yet run.
- R3 Morning briefing (old-tree APScheduler job, gemini-3.1-pro-preview via GEMINI_API_KEY, no cost telemetry) + old-tree Mattermost listener: LEAVE until F5/F20 replace them.
- R4 Worktree rule (amends 09-08 branch rule): ~/cobalt IS production; every Code prompt works in ~/cobalt-wt/<branch> off main; production proofs only after --ff-only merge, from ~/cobalt, as a named step; merge = deploy.
- Architect role in Code = Fable 5.1 always; implementing subagents Opus 5. Code-architect spike PASSED (ADR-0008: rulings a–g in the pane, developer subagent, 38 commits, live same day).
- Grok seat role = RESEARCHER (read-only + web), `grok --sandbox readonly-safe`; Claude-config inheritance STAYS ON, coexistence via harness-aware hook guard.
- Item d: class + family in strategy-note frontmatter, filled from the def (chat's second opinion was "drop"; Dejan ruled fill).
- §1 fold: L17 amended, L28, L29 amended, L30, L31, L32, L33–L40 issued and pasted; the 09-05 research appendix (never pasted) recovered and pasted.
FACTS
- Git: six linear branches ff'd into main and deleted; main only. main at close: post-herdr-flip commit.
- S1-P4 email: Layer-B Google OAuth gmail.send, proven RED→GREEN in prod. Google project = AI-Studio "Cobalt Project", stuck in TESTING (console bug) → refresh token expires ~09-15 unless Publish succeeds + `cobalt notify email-auth` re-run. Alert address == rt.smbtraining.com::username (vault literal; F19 redacts it from text).
- herdr handover DONE 19:21 ET: com.cobalt.herdr pid 20039 under launchd; restore brought Claude1 (with conversation, /rc auto) + Qwen1 back; Codex/Grok/agy relaunched by hand. `herdr` probe live.
- seat-usage job live, hourly 06–23 ET → docs/40 - DevDocs/reports/seat-usage.md; ccusage 20.0.20 pinned; fable-5-1 and gpt-6-astra UNPRICED offline. Chat-side usage not measurable — Dejan tracks weekly % open/close by hand.
- 09-08 Code cost (API-equiv): Opus $36.5 (S1-P4 + ADR-0008 dev), Fable $13.1 (architect), Sonnet $8.5 (Prompt 4); architect review ≈ +$0.57 across Phase B — the developer is the spend.
- 27B: thinking eats the whole budget at max_tokens=1600 (3/3 zero useful) → template-level disable (Prompt 5); adapter contract in ADR-0008.
OWED
- Prompt 5 (mainframe: template override, 4-bit vs 8-bit same test, 122B delete, spinner-log fix).
- Ops prompt: cobalt_app non-superuser login (grants bind only after SET ROLE today) · herdr probe checks SessionStart guard pointer · vault restore defects (section-wide, no frontmatter undo) · hourly report git rule.
- Seat-delegation spike (outside Ladder): architect → Codex/Grok/Qwen/agy by role, read-only, artifact-verified; agy with a Claude model selected — prove model + which quota.
- OAuth Publish retry from another browser before 09-15.
- Old-tree test_finviz_extractor collection error; MattermostConfig timeout_s DONE (ADR-0008).

### 2026-09-09 — planning session, morning ops (Fable 5.1 Code architect, plan mode) — PART 1 CLOSED, scope items 2–6 continue in the next session
RULINGS
- R1 ASET sheet: DAY MODE UNRESOLVED (TaxonomyConfigError, tunables unit `window`) cleared by `launchctl kickstart -k com.cobalt.aset` at 07:06; verified REDUCED/half/keys A,B. Cause: the 09-08 ~19:00 seat-usage deploy added `TunableUnit.WINDOW` + a tunables row; the sheet process (started 17:50 at ADR-0008 LIVE-1) re-reads tunables.yaml per request through pre-merge code. The deploy plan said "nothing else is restarted" — that was the error. Law restated (third time: 09-04, 09-08 aset.yaml, today): a config-shape change and the restart of EVERY resident that reads that file are one action; every deploy plan names the residents it restarts.
- R2 herdr fixed FORWARD, not rolled back. Root cause: `herdr --remote` from a 0.8.2 client replaces the running server (06:03 and 07:26, both from Fedora; the second attach came 27 s after the launchd start). Dejan's addendum: 0.8.2 DID prompt and he answered Yes without reading, so the replacement was human-confirmed — partly procedure, not only version. Fix: Mac + Fedora herdr 0.8.2 → 0.9.0 (0.9.0: "client updates leave compatible servers untouched … replacing a remote server asks, default No"); server restarted under launchd from the Mac keyboard (Terminal.app, not a herdr pane) 08:17 → pid 72998, run 3, version 0.9.0, endpoint_compatible yes; heartbeat GREEN 08:19:57 (13 jobs / 11 probes). Standing rules: the phone attaches via `ssh cobalt@cobalt` then `herdr` (its 0.8.2 client must never `--remote`); Fedora `--remote` on 0.9.0 answers NO to any replace prompt. ACCEPTANCE PENDING (Dejan): after a Fedora `--remote` attach, `launchctl list | grep com.cobalt.herdr` still shows pid 72998.
- R3 Qwen seat: Qwen Code 0.23 sends `cron_list` and `list_agents` with `parameters` lacking `properties`; LM Studio's OpenAI endpoint returns 400 on every turn (confirmed from LM Studio's request log, tools[5]/tools[15]). Fix: `tools.exclude: [cron_list, list_agents]` in ~/.qwen/settings.json (backup ~/.qwen/settings.json.pre-0909); headless `qwen -p` → "OK", request carries neither tool. Interactive relaunch in Qwen1 PENDING (Dejan). Upstream filing (Qwen Code should emit `properties: {}`) = Dejan's call.
- Ruling order for the day (Dejan): sheet → red heartbeat → Qwen → Codex1/Gemini1 (relaunch by hand; herdr restores shells, not agents — unless the agent reports a session reference, see 0.9.0 note below).
FACTS
- Heartbeat 19:21 09-08 → 05:54 09-09: 40 GREEN. One RED 21:07 09-08: the heartbeat itself MISSED (no beat 19:52 → 21:07, 75-min gap, cause not in the log, self-recovered 21:22). RED 06:09 → 08:05 on `com.cobalt.herdr` (launchd probe: loaded, not running, exit 0) while the socket probe stayed green — the two probes disagreeing was the correct signal; the launchd probe is the one that caught it.
- 05:15 prefill created the 2026-09-09 note (write_id 2120): rules unit, REDUCED / half sheet / keys A,B, market table, calendar. prefill-drc 15:40 09-08 created DRC-2026-09-08. archiver 00:30Z 210 symbols, 3,166,696 rows, exit 0; backup 21:40 ok; seat-usage hourly ok, fable-5-1 unpriced.
- Daily-note defect (L28 class, OPEN): the heartbeat unit was stuck on the 05:54 GREEN block from 06:25 to 08:05. The 06:09 and 06:24 beats wrote RED; at 06:25:54 the file was rewritten back to the 05:54 content (Obsidian Sync from the remote device is the likely writer); the merge then read the stale block as a human edit and let human win every beat ("unchanged", OVERRIDE conflict). Self-cleared after the 08:17 restart. A sync-revert is indistinguishable from a human edit to the current merge → Ops prompt.
- Sheet probe defect (OPEN): F18's sheet probe checks HTTP 200 only; the page served 200 with the refusal banner for ~13 h → Ops prompt: probe must read the day-mode banner.
- herdr 0.9.0 native agent restore relaunched claude / grok / qwen in their panes on restart; the Claude1 conversation continued without `--resume`. Codex1 / Gemini1 were empty shells before the restart, nothing to restore.
- Hook-guard pointer (~/.claude/settings.json → herdr-harness-guard.sh) intact after `brew upgrade herdr` and the first 0.9.0 server run; Codex and Grok hooks still labelled. herdr then offered its Claude-integration update → re-verify the pointer after installing (checklist line, codex-seat-test §10).
- ops/README "herdr handover" section is stale (0.8.2 wording, "built, not loaded", "at the Mac keyboard" reasoning) → Ops prompt rewrites it with the 0.9.0 attach rules.
- Uncommitted in ~/cobalt, deliberately left: rules.yaml `generated_at` (05:15 regen), archiver-runs.md one row, seat-usage.md hourly rewrites — the hourly-report git rule is an Ops-prompt item. Committed here: this Ledger appendix + Dejan's 09-08 appendix paste.
OWED (unchanged from 09-08, plus today's additions)
- Prompt 5 (mainframe): chat-template thinking-off override, 4-bit vs 8-bit same tool-calling test, 122B deletion (24 h clean passed 21:36 09-08), spinner-log fix — draft, approve, Opus subagent in a proposed maintenance window.
- Ops prompt: cobalt_app non-superuser login · herdr probe checks the SessionStart guard pointer · two vault-restore defects (section-wide, no frontmatter undo) · hourly seat-usage git rule · + sheet probe reads the banner · + sync-revert vs human-override · + deploy plans name residents to restart · + ops/README handover rewrite for 0.9.0 + phone/Fedora attach rules · + herdr acceptance result.
- Seat-delegation spike (outside Ladder) · S2 start ruling (dates pulled forward; S2-P1 drafted, not run) · OAuth Publish retry before 09-15 (human) · Qwen Code upstream issue (Dejan's call).
- ADDENDUM 08:33: herdr integrations updated from this pane (`herdr integration install claude` v8→v9, `antigravity-cli` v2→v3; backups ~/.claude/settings.json.pre-herdr-v9, herdr-agent-state.sh.v8). The claude install did NOT replace the SessionStart pointer — it APPENDED a second entry aimed at herdr's own script, so both would have fired. Duplicate removed; settings.json restored byte-identical to the pre-install backup (guard only). v9 still hardcodes `herdr:claude`, no harness detection → guard stays. Checklist + Ops-prompt rule: the hook check asserts exactly ONE SessionStart entry, not merely that the guard is present.

### 2026-09-09 — planning session PART 2 (Fable 5.1 Code architect, plan mode; Opus 5 subagents) — CLOSED at 09:35, three builds in flight (addendum owed at Phase B / LIVE close)
RULINGS (one per message, decided-with-veto unless noted)
- R0 Item 0 verified read-only: `com.cobalt.herdr` pid 72998 unchanged through 4 client attaches after the 08:17 launchd start; Dejan: Fedora `--remote` on 0.9.0 prompted to replace, answered No → **herdr acceptance PASS**. Heartbeat GREEN 08:35 (13 jobs / 11 probes). Hook pointer: exactly one SessionStart entry → guard. `herdr agent list` = 3 seats (claude, grok, qwen); Codex1/Gemini1 relaunch = Dejan's, after he tests Qwen1 (not yet tried). git: main == origin/main.
- R1 PROMPT 5 (mainframe) APPROVED: thinking-off = repo-owned chat template (`ops/mainframe/chat_template.jinja`, installed by `start_mainframe.sh` before every load, `.orig` kept) with an IN-BAND soft switch — `/no_think` in the system or last message disables thinking for that request, `/think_low` sets low effort; default stays thinking-on (27B tool-calling was 14/14 that way; hard-off would take per-task control from the ADR-0008 adapter). 4-bit vs 8-bit on the 09-07 tool-calling test via symlinked side instances (one at a time, `--estimate-only` memory gate, context 32768). `--parallel 1` speculative-decoding hypothesis rides in the same window. 122B deletion GO (gate evidence: 0 FAILED/reload lines and 2,087 OK beats since 09-07 21:36:22; newest crash report 09-07 15:46). Spinner fix + 5 MB log rotation + pid-message split. Three phases: A1 repo work (DONE 09:35, branch `ops/mainframe-p5`, 4 commits, 17 template tests, +17 suite), A2 side-instance tests + deletion at 11:17 (cron wake-up), Phase B production kickstart 16:37 after Dejan's ff-only merge (RESTARTS: `com.cobalt.mainframe` only; stateless HTTP clients affected ~40 s: `com.cobalt.agent`, Qwen1, F18 mainframe probe). Guard ruling (ESCALATE 4.1): a model-dir template that is neither upstream nor ours is FATAL on the main path and skips the reload in the heartbeat.
- R2 OPS PROMPT APPROVED (Opus 5, worktree `~/cobalt-wt/ops-0909`, branch `ops/2026-09-09`, running): A `cobalt_app` LOGIN NOINHERIT role (members: the three side roles; CONNECT on both DBs) under NEW names `COBALT_DB_USER` / `COBALT_DB_PASSWORD` — `POSTGRES_*` stays the docker-superuser/bootstrap credential (docker-compose substitutes it; the old tree reads it); migrations and devdb keep the superuser, pgdump moves to the app login; vault add-only + F19 enrolment (16 → 17), `.env` bootstrap tier; old tree untouched. B herdr probe asserts exactly ONE SessionStart entry → guard (+ the 4 stale `test_herdr_probe` failures on main fixed). C vault restore: unit-scoped from `unit_before`, frontmatter rows via `frontmatter_span`. D sync-revert ≠ human override: on-disk unit equal to any of the last 10 Cobalt `unit_after` values = SYNC REVERT (Cobalt wins, no override rows, `vault_writes.sync_revert_of` via migration 0004). E sheet `GET /api/health` + probe `sheet_daymode` (RESTARTS: `com.cobalt.aset`). F generated files: ONE nightly commit by `com.cobalt.generated` 23:37 daily, allowlist `configs/cobalt/generated.yaml`, refuses off-main/mid-merge/staged-index, never pushes. G `JobSpec.reads` derived from code + `cobalt jobs readers <path>`; every deploy plan carries `RESTARTS:`. H ops/README rewritten for herdr 0.9.0 under launchd (phone = ssh then herdr, never `--remote` from 0.8.2; Fedora answers No; restore = 0.9.0 native, never relied on). LIVE block 17:20–18:00 ET after merge, four rollback domains (credential / DB / code residents / registry).
- R3 SEAT-DELEGATION SPIKE DONE (outside the Ladder; report `40 - DevDocs/reports/seat-delegation-spike-2026-09-09.md` on branch `spike/seat-delegation-0909`): hub = this session, reviewer role by house, one identical read-only task, artifact verified against hub-computed `ast` + sha256. codex PASS (5/5 fields, 15 s); grok PARTIAL (line_count 172 ≠ 171 — verification caught a plausible wrong number; sha null: headless cancels shell); agy PARTIAL (all computable fields match; sha null: headless denies commands; needs `--add-dir` + absolute path); qwen FAIL on a PRODUCTION DEFECT: the upstream template's `| tojson | safe` (line 138) — LM Studio's Jinja has no `safe` filter, so any turn-2 request whose history carries a non-string tool-argument value fails (curl repro: `{"path":"x.py","limit":5}` → `Unknown StringValue filter: safe`; strings-only → OK). Fix folded into Prompt 5 (repo template drops `| safe`, test g), lands at Phase B; until then the Qwen seat cannot do multi-turn tool work with numeric/array arguments. agy + Claude model: request → `daily-cloudcode-pa.googleapis.com/v1internal`, `authMethod=consumer`, `quotaProject=` empty, no `claude-sonnet-4-6` row in ccusage → **bills the Google AI Pro entitlement, not the Claude plan**; agy's `/usage` panel not capturable over a pty → Dejan reads it in Gemini1. L33 note: reviewer = reads only; hashing/verification belongs to the hub.
- R4 S2 START: dates pulled forward — S2 09-10 → 09-23, S3 09-24 → 10-07, S4 10-08 → 10-14 (1 wk, capped), S5 10-15 → 10-28, acceptance 10-29 → 11-04 (Ladder edited; originals in git history). S2-P1 DRAFTED in the Ladder (pool job + 2m bar poller reusing the archiver collector + account-mode tag; ADR-0008 line 0; watchlists move user-side), NOT RUN — gated on Dejan's 4 Finviz dynamic screens (user data → vault note / trader_settings, never repo).
- R5 OAuth: Dejan retries Publish from another browser before 09-15, then `uv run cobalt notify email-auth` (human step, reminded). Qwen Code upstream issue: Dejan files; draft at `40 - DevDocs/reports/qwen-code-upstream-issue-2026-09-09.md`.
FACTS
- Plan-mode mechanics: entering plan mode in the parent pauses running subagents' writes (A1 stopped twice); later rulings used AskUserQuestion as the approval gate to keep builds moving — same gate, no stall.
- Working-tree rule held: `~/cobalt` on main; worktrees `ops-mainframe-p5`, `ops-0909`, `spike-seat-delegation`. Uncommitted-by-design in prod: rules.yaml `generated_at`, archiver-runs.md, seat-usage.md (Ops item F retires this).
- Cost so far (API-equiv, ccusage): the spike ≈ $0.01 grok + 4k codex tokens + 19.5k agy tokens on Google quota; the two Opus builds are the spend (addendum at close).
OWED / IN FLIGHT
- 11:17 cron → Prompt 5 Phase A2 (Opus): matrix, probes, throughput, `--parallel 1`, 122B deletion, cleanup, READY FOR MERGE.
- 16:28 cron → Phase B readiness; Dejan merges `ops/mainframe-p5` (ff-only); architect kickstarts `com.cobalt.mainframe` ~16:37 and proves (template installed, arch/quant, nothink probe, `/no_think` completion, heartbeat GREEN).
- Ops prompt report → Dejan merges `ops/2026-09-09`; architect runs the LIVE block 17:20–18:00 (four domains) and proves.
- Spike branch `spike/seat-delegation-0909` → ff-only merge at Dejan's convenience (docs only).
- Dejan: Qwen1 interactive test → relaunch Codex1/Gemini1 → read agy `/usage` → 4 Finviz screens for S2-P1 → OAuth Publish before 09-15 → file the Qwen issue → `git push` (now and after the addendum).
- Addendum tonight: Phase B result, LIVE block result, model inventory ruling (six models on disk after the 122B), ccusage day total.

### 2026-09-09 — PART 2 ADDENDUM (evening: Prompt 5 Phase B, Ops LIVE block, chat second opinion applied) — CLOSED 17:25
- CHAT SECOND OPINION (15 items) applied before the production steps: ff-only rollback = revert by commit range; renderer named @huggingface/jinja; llmster shared-daemon caveat; **122B deletion HOLD** (swap §11 step 10 never ran; 65 GB stays, 604 GiB free); side-instance keys never share the `qwen3.8-27b` prefix, cleanup proven; Ops LIVE order = credential BEFORE merge; D = L28 amendment (folded above); F amended = rebase-then-ff on every merge (README deploy checklist + report template); L33 codex profile corrected; OAuth token-clock runbook in ops/README; S2 clock ruling PENDING Dejan (no further Ladder date edits); Finviz screens filed; report discipline + `_inflight` in CLAUDE.md (this commit); LIVE-1 rollback completes the domain (DROP ROLE after revoking memberships + CONNECT).
- PROMPT 5 PHASE A2 (11:17–12:05, Opus): caught A1's soft switch half dead — LM Studio normalises user `content` to a list, so the last-message arm never fired; fixed via the template's `render_content` macro, 20 tests. Matrix 10 runs/cell, every cell 10/10 correct tool calls; `/no_think` cuts a tool turn 21.3 s → 5.8 s (8-bit), 19.5 → 4.9 s warm (4-bit); the upstream 4-bit cell lost 1/10 runs to `| safe` (Qwen Code's own list-valued `update_goal` call = the morning's seat deaths). Throughput at max_tokens 1600: thinking-on = 0 useful tokens on both quants; `/no_think` = ~780. `--parallel 1` does NOT unlock speculative decoding (`SpeculativeDecodingNotSupportedError` unchanged). Hazard 4.4: a length-truncated think block carries NO `<think>` tag → adapter must reject `finish_reason=length` with an unclosed block and default `/no_think` for non-reasoning task classes (ADR-0008 adapter contract). Product call PENDING Dejan: 4-bit (37.6 tok/s) vs 8-bit (22.4) as the served model — equal on tool-calling.
- PROMPT 5 PHASE B (16:53–16:58, architect, after Dejan's ff-only merges 3b57442 → 33fdbc2): attempt 1 served the OLD template — `lms daemon up` indexes the model dir at startup and the load reads the template from the index; the script installed the file 2 s after the daemon came up; the 16-token probe gave a FALSE PASS (tagless open-air reasoning). Attempt 2 (template on disk before the daemon): `nothink probe OK: 4`; production `/no_think` → `4` in 2 tokens, both placements; `| safe` repro renders; heartbeat GREEN 16:58; log rotated (9.26 MB → .1). Fix merged (33fdbc2): install BEFORE `lms daemon up`; probe = 64 tokens + three-way verdict (finish=stop, no think body, answer starts "4"). No third kickstart needed. RESTARTS: `com.cobalt.mainframe` ×2 (16:53:48–16:54:04, 16:56:22–16:56:33).
- OPS LIVE BLOCK (17:05–17:20, architect, after Dejan's ff-only merge → edeebcf): LIVE-1 before the merge — `GRANT CONNECT ON DATABASE cobalt_brain TO cobalt_app`, two `.env` lines copied by name from the worktree (never printed); LIVE-2 migration 0004 applied deliberately (`sync_revert_of | YES | integer`); LIVE-3 `com.cobalt.aset` kickstart → `/api/health` = `{"ok":true,"day":"2026-09-09","mode":"reduced","stage":"stage 2 (proposed, undecided — floor holds)","sheet_mode":"half","error":null}`; LIVE-4 `com.cobalt.generated` bootstrapped (23:37 daily), 14 jobs registered, `cobalt validate` exit 0, forced beat **GREEN 17:13 — 14 jobs / 12 probes**: `sheet daymode` reads the banner; `herdr` answers three questions (5 panes, seats agy/claude/codex/grok/qwen, hook guard = 1 SessionStart entry → guard, executable). PROOFS: factory identity `session_user=cobalt_app`, `current_user=cobalt_user|cobalt_system` per side; raw `psql -U cobalt_app` → `permission denied for schema user`; old tree still `cobalt`. Suite on main: 0 failed / 1092+ passed (branch figure; the 4 stale herdr tests fixed).
- FINDINGS FROM THE OPS BUILD: (1) F19's literal guard was silently INACTIVE in every worktree since R4 (vault resolved relative to the checkout; no worktree has `data/`) — fixed with a fail-loud `COBALT_VAULT_FILE` override for worktrees; the class ("a guard whose off looks like normal") is the lesson. (2) Credential leak: the subagent's `tail .env` put `MATTERMOST_DB_PASSWORD` into its local transcript; scrubbed by Dejan (1 file, 2 occurrences, nothing in git); **rotation = owed ruling** at a maintenance window once a rotation path exists (both provisioning scripts are mint-only). (3) F19 literal count 19 → 20 (`COBALT_DB_PASSWORD`).
- SEAT / QUOTA FACTS: agy `/usage` (Dejan's screenshot): Google AI Pro account carries TWO weekly buckets — "Gemini models" 99.64% and "Claude and GPT models" 98.19% remaining — so a Claude model on agy bills the Google plan, confirmed. Qwen1 interactive answers OK after `tools.exclude`. DeepSeek Harness (`dsh`, `@deepseek-ai/dsh`, MIT, preview since 2026-08-13) = QUEUED, standing seats workstream, after S2-P1, docs-only, no install while rc: score the five seat gates; extract what its append-only session log, loop-as-plugin and Claude Code/Codex delegation teach F20; verdict = seat test (a day of Opus) or reference only. Qwen Code upstream issue: Dejan files tomorrow from the drafted report; harness stays Qwen Code.
- FINVIZ SCREENS FILED (user data, L32): `1 - Trading/Radar Screens.md` — Up Gappers, Down Gappers, Day Scan (after 10:00, session-clock-gated), Morning Low Float — each with the pasted URL, decoded filters, sort, columns and the derived `/export/screener` call. NOTE: first filed under `4 - Strategies/` and it broke `cobalt validate` (the trade_def loader treats every note there as a strategy note) — moved; validate exit 0. S2-P1 reads the new path.
- `_inflight` snapshots retired for the two merged reports; remaining: the spike report (branch `spike/seat-delegation-0909`, 1 docs commit, ff-clean) and the PART 2 plan file.
- OWED: 4-bit vs 8-bit product call · S2 clock ruling (start = P1 run day vs calendar) · Mattermost DB password rotation path + rotation · `cobalt generated commit --dry-run` prints "nothing to commit" even when it lists files it would commit (display defect in `CommitOutcome.console`; detection is correct — 3 changed paths found; first real run 23:37 tonight, verify tomorrow) · DevDocs for the modified files at sprint close · ccusage pin bump · demote `cobalt` from superuser (unblocked by cobalt_app) · seat-usage fallback reason-class column + AMBER (L25) · Dejan: `git push` (21 commits), merge the spike branch, OAuth Publish + email-auth tomorrow, file the Qwen issue.

### 2026-09-10 — S2 open + heartbeat market-reset fix (Opus 5 architect pane; Opus 5 CTO chat; Codex Terra/Sol/Astra; Sonnet hub) — CLOSED

RULINGS (one per message, decided-with-veto unless noted)
- R1 SEATS FOR THE WEEK: the Fable weekly meter hit 98% (resets Sun 13:00 ET) after the 09-09 architect session replayed ~117k context ~850 times. Architect seat and the CTO-office chat run on Opus 5 until the reset; no long-lived Fable sessions this week. Astra stays the Code-side plan reviewer and is never the CTO seat (his call, not a cost call).
- R2 L29 AMENDED (§1 fold below): GPT-5.6-Sol at high effort = OpenAI's implementation floor; GPT-6-Astra = the cross-check reviewer. Plan review = architect + Astra only, ≤3 rounds, round 3 final with dissent recorded verbatim, architect's plan stands (L39). Sol's standing profile: `codex exec -s workspace-write`, `sandbox_workspace_write.network_access=true`, never `danger-full-access`; Sol cannot commit — the hub does. Code sessions are cleared every turn; durable state lives in the plan file and the report, never in session context. One scheduled small-context wake-up (a timed LIVE block) is acceptable.
- R3 L41 CROSS-HOUSE CREDENTIAL LAW (new): no DB credentials ever enter a cross-house launch environment. Sol runs non-DB work; the hub runs the DB-backed suite and the dev-vault smoke by copying `~/cobalt/.env` into the worktree BY NAME (never cat/tail/grep/echo — the 09-09 leak class), pointed at `cobalt_dev` + the dev vault, removed before commit with `git status` / `check-ignore` proof. A `--allow-prod` migration is never the first proof of a migration ("treat LIVE as the proof" rejected). Standing ops item: a guarded worktree credential path (env-file override, like `COBALT_VAULT_FILE`) so nothing is ever copied.
- R4 L42 RESTARTS DERIVATION (new, folds Ops item G): plist in the diff → that job. Config in a resident's `reads:` → that resident. Any `src/` change → every resident whose entrypoint imports the module, by static AST walk; all residents if unproven. Unclassified path → ESCALATE line, never dropped. Derived by `cobalt jobs restarts <range>` and printed in every report and deploy plan.
- R5 L43 DEPLOY CADENCE (new): one production deploy per evening.
- R6 L32 EXCEPTION — NARROW, do not widen at fold: well-known third-party screen definitions the trader adopted from public sources (the Finviz `f=` filter strings) are NOT user data. His own edits to them ARE. Supersedes the classification in the 09-09 "FINVIZ SCREENS FILED (user data, L32)" line for the adopted strings only. Consequence: ESCALATE E9 DROPPED, `reports/day-open-2026-09-10.md` commits unredacted. The vault-note contract for the screens is unaffected — it governs where he edits them, not secrecy.
- R7 RADAR SCREENS CONTRACT (R1 of the build brief): vault note `1 - Trading/Radar Screens.md` carries one fenced YAML block per screen (`screen, f, sort, columns, active_from, active_to, enabled`, optional `ft`) plus exactly one `kind: pool` block. Written ONCE by S2-P1 through the vault writer under a single HITL card; thereafter Cobalt only reads it — fenced blocks only, reload on file-hash change, block + hash mirrored into `"user".trader_settings`, `radar_membership.source` naming source + hash. Parse failure = degraded pool + `radar` probe RED naming the file. Repo ships exactly one synthetic example screen. Static lists move the same way as `1 - Trading/Radar Lists.md`.
- R8 ACCOUNT MODE (E1): standing `aset.account_mode = live` in `"user".trader_settings` (seeded by migration 0004). Per-day sim switch = a select on the morning sheet attestation writing `day_modes.account_mode` for that day. Card stamp resolves day-row → standing; neither present = card REFUSED, loud, logged, no row.
- R9 POOL RULE (E2/D3): cap 50, and the cap lives in the vault pool block — committed config carries engine tunables only, never a cap, rank rule, metric choice or stickiness. Rank metric: volume premarket (04:00–09:30), RVOL after 09:30. Morning Low Float ranks by volume in every session. Day Scan first among screens from 10:00. Screen names rank before list names. Stickiness = 3 scans before a name drops; dropped names carry `excluded_by = config_cap`. Overnight and market_reset do not scan.
- R10 HEARTBEAT FIX RULED AND SHIPPED: ordered stages PROBES → COMPOSE → ALERTS → PERSIST → VAULT → FINALIZE, each recording a redacted failure and allowing the next to run; alerts before persistence; FINALIZE separately retries the DB update and sends a corrective RED so a failed vault write can never be silent. The vault stage asks `cobalt.session` FIRST and returns `deferred_market_reset` before any writer is constructed, so it cannot add a refusal row. Durable `vault_outcome` / `vault_reason` columns. Heartbeat enrolled in the F17 wrapper via `cobalt jobs run` and is the one job EXEMPT from the kill switch; wrapper bookkeeping best-effort for it, each failure loud, the subprocess runs regardless.
- R11 ECONOMICS RESTATED: no larger Claude plan (L27's Max 20x escalation is off the table), no top-ups. A weekly meter hitting its ceiling moves work to another house, never money. Codex is the OVERFLOW valve, never the main line — local first, Claude where it is the floor or best fit, Codex when a Claude meter binds; all of the Codex weekly allowance used each week, most of it on Astra.
- R12 LOCAL MODEL — NO CHANGE: Qwen3.8-27B 8-bit stays, "use it, measure it". Rulings 3 (122B / swap §12.4) and 4 (six-model inventory) CLOSED into a measured bake-off, queued for a maintenance window, no date; all six models stay on disk until it rules. Cells: Qwen3.6-35B-A3B, gpt-oss-120b, on-disk 122B on runtime 1.11.0, Qwen3.6-27B, current 27B 8-bit and 4-bit as controls; runtime (LM Studio-MLX vs a speculative-decode engine) is its own cell. Needs the production 27B unloaded — gpt-oss-120b does not fit beside it.
- R13 S2 CLOCK: calendar. S2 = 09-10 → 09-23, with a Monday 09-14 tripwire if S2-P1 has not launched. Scope comes out; dates do not move.
- R14 GROK: news/context lane candidate on the strength of the Vitals Macro Brief (read Vital Dawn, transcribed, researched, produced the vault note). Routing ruling deferred.
- R15 DEFAULTS TAKEN, NOT VETOED (standing unless he vetoes before the S2-P1 vault write): aftermarket ranks by volume; a screen's names keep the screen's own sort, with volume/RVOL applied to the lists.

§1 LAWS FOLD (paste into §1 LAWS REGISTER)
- **L29 amended (09-10):** OpenAI house roles fixed — GPT-5.6-Sol at high effort = the implementation floor, GPT-6-Astra = the cross-check reviewer (Fable's role in that house). Plan review is architect + Astra, two parties, ≤3 rounds; round 3 is final with dissent recorded verbatim and the architect's plan standing (L39). Sol's standing writer profile: `codex exec -s workspace-write` with network on, never `danger-full-access`; Sol cannot commit. Code sessions are cleared every turn — durable state lives in the plan file and the report, never in session context; one scheduled small-context wake-up is permitted.
- **L32 exception (09-10) — narrow:** well-known third-party screen definitions the trader adopted from public sources (Finviz `f=` filter strings) are NOT user data; his own edits to them are. Everything else in L32 stands.
- **L41 Cross-house credential law (09-10):** no DB credentials ever enter a cross-house launch environment. Cross-house workers run non-DB work; the hub runs DB-backed proofs by copying `~/cobalt/.env` into the worktree BY NAME (never printed, tailed, grepped or echoed), pointed at `cobalt_dev` + the dev vault, removed before commit with proof. A `--allow-prod` migration is never the first proof of a migration.
- **L42 RESTARTS derivation (09-10, folds the 09-09 Ops item G):** restarts are derived by rule, never by judgement — plist in the diff → that job; config in a resident's `reads:` → that resident; any `src/` change → every resident whose entrypoint imports the module by static AST walk, all residents if unproven; unclassified → ESCALATE, never dropped. `cobalt jobs restarts <range>` produces the derivation table; every report and deploy plan carries the `RESTARTS:` line.
- **L43 Deploy cadence (09-10):** one production deploy per evening.

FACTS
- HEARTBEAT BLACKOUT — CAUSE CLOSED (Terra read-only triage, `reports/heartbeat-blackout-2026-09-10.md`). The 75-minute gaps on 09-08 and 09-09 were one cause: `run_beat` called `write_note_block()` unguarded at `runner.py:249`, upstream of the DB row (`:291-292`) and the alert channels (`:269-270`). The F1 market_reset gate refused the beat's own daily-note write, `SessionBlocked` unwound to the CLI's fail-loud exit, and each refusal killed the whole beat — no row, no DM, no email, probes and rendered beat discarded. Eight `system.session_blocks` rows, actor `vaultwrite:heartbeat:upsert_unit`, one per missed tick; eight `FAILED:` lines in `heartbeat.err`. H1 SUPPORTED, H2 (never launched) and H3 (hung/killed) REFUTED — launchd ran every tick, `caffeinate` held, the archiver exited 0 both nights. Control: 09-07 Labor Day, whole day `overnight`, no gate, four writes in the same window, same code and archiver run. The gate landed 09-04 (`e2acd20`); 09-08 was simply the first trading-day 20:00–21:00 window with both live. His "not in the log" was `heartbeat.log`, which by construction holds only beats that survived to render.
- SECOND DEFECT, NOT FIXED: the `vaultwrite_blocks` probe rates refusals OK by design ("a refusal is the guard working") — true of every actor except the heartbeat itself. It reported `4 refused … OK` inside the very RED beat that noticed the gap, and will stay green through any recurrence. All 8 rows F1 has ever produced are the heartbeat's.
- HEARTBEAT FIX LIVE 16:05–16:12 ET, main `16847eb` (unchanged throughout; ahead 2 at guard time). Migration `0003_heartbeat_vault_outcome` applied to `cobalt_brain` (DB-wide sequence 0001→0002→0003 in `src/cobalt/db_migrations/`; the live `0004` is vaultwrite's module-local migration — different directory, no collision), 13/13 tables equal, both columns nullable text with a check constraint, digests exclude `user_id`/`vault_outcome`/`vault_reason`. Old plist booted out, wrapper plist copied and bootstrapped, never side-by-side; `launchctl print` shows `cobalt jobs run com.cobalt.heartbeat … cobalt heartbeat beat` at 900 s. `cobalt jobs register` → 14, `cobalt validate` exit 0, registry↔ops↔plist exact match. Forced beat: `vault_outcome=written`, `vault_reason` null, `green_summary_date=2026-09-09` intact, wrapper `argv`/`returncode` merged on the same row, exit 0, beat GREEN (14 jobs / 12 probes), write_id 2309, `session_blocks` unchanged at 8.
- GAP FOUND, NOT FIXED: the per-stage `logger.info` lines (PROBES…FINALIZE) never appear in `logs/heartbeat.log` on a healthy run — only the RED `_stage_failure` prints do. The ordered-path proof is therefore indirect (no RED stage line + `vault_outcome=written` + exit 0). INFO-level logging config unverified.
- STANDING EXPECTATION: tonight's first beat after 20:00 ET must show `vault_outcome=deferred_market_reset`, keep the colour its own probes produce, and leave `session_blocks` (actor `vaultwrite:heartbeat:%`) at 8. Verified at the 09-11 day-open, read-only, on the Qwen seat.
- ROLLBACK TRIPLE: `git revert 16847eb` (or the merge commit it names) · previous direct-invocation `com.cobalt.heartbeat.plist` (no wrapper args, same env/interval) · `0003_heartbeat_vault_outcome.rollback.sql` through the approved production migration connection. `RESTARTS: com.cobalt.heartbeat` (done).
- OFF-PHASE BEAT observed, not investigated: 2026-09-08 19:22:14, 62 s after the 19:21:12 beat. Flagged, not dropped.
- CODEX SANDBOX PROVEN (day-open §1, `reports/day-open-2026-09-10.md`): Terra read-only reads anywhere, write denied, all network blocked including localhost; Sol workspace-write denies outside-worktree writes and denies commit (the L29(2) gate), network flag honoured. `codex exec` needs `--skip-git-repo-check` outside a repo and `< /dev/null` or it blocks on stdin. Terra's Unified Log queries fail (`log: Cannot run while sandboxed`) — no independent launchd-side forensics from a sandboxed run, now or later. `psql` is absent from the host (127, not a denial) — the `cobalt db query` decision stands.
- S2-P1 AT CLOSE: plan FINAL (`_inflight/plan-s2-p1-2026-09-10.md`, Astra 3 rounds, dissent recorded), branch `sprint-2/radar-pool` at `0166e69`, Sol's build uncommitted in `~/cobalt-wt/s2-p1-radar-pool`. Sol's report says NOT READY FOR HUB GATE; the hub gate actually ran **1213 passed / 1 failed** (the self-documenting `# UNVERIFIED` header gate), against a 1137/0 baseline on main — migrations round-trip clean, `validate` exit 0, `screens propose` clean, E5/E9 greps clean. Blocking: `BRK.B` fixture line must be `BRK-B` (Finviz 400); throttle probe + real header capture (E12, token resolution failed in Sol's sandbox); dev-vault smoke; and the missing O3/O4/O5 test matrices + the step-12 refusal matrix — a bounded Sol task, not a relaunch. O1/O10/E12 are hub-side by design. Nothing committed on the branch.
- CODEX METER: one Plus 5-hour window ≈ one Sol build + 2–3 Astra rounds. Astra round 1 hit the limit at ~72k tokens; Sol hit it mid-build at ~536k and was relaunched once — his call was to WAIT for the reset rather than have Opus finish another author's diff (Codex time is prepaid, Claude time is this week's scarce meter). Standing rule: one relaunch with a CONTINUE line; a second stop hands the report + diff to Opus.
- DEVDOCS: prose stays agent-authored — no generator exists, and the symbol-check gate is the acceptance test, not a generator.
- CAPTURE HYGIENE (extends the 09-09 report-discipline / `_inflight` rule in CLAUDE.md): reviewer captures and Codex session logs never enter a commit — Sol's 4.7 MB Codex log and `SOL_DONE` were amended out of the heartbeat merge and `_inflight/*.log` is gitignored. In the heartbeat diff ~11.9k of ~13k insertions were two Astra delivery snapshots; a log-size rule for `_inflight` captures is queued.
- HIS SHELL exports `COBALT_VAULT_PATH` pointing at the PRODUCTION vault — the NN#16 guard caught a dev run against it. He should unset it.
- OLD-TREE DEFECT: `FinvizApiClient` resolves its vault file CWD-relative with no env override, so it breaks from any worktree.

OWED
- §1 FOLD DEBT: L28–L32 and L33–L40 exist only inside the 09-06/07 appendix block; §1 carries their amendments and the L33 note but not their text. Fold those, plus L41–L43 and the two amendments above, into §1 at this paste.
- Ops prompt (one Sonnet or Opus session): `permissions.additionalDirectories: ["/Users/cobalt/cobalt-wt"]` in the project's `.claude/settings.json` · worktree credential override (env-file, like `COBALT_VAULT_FILE`) so nothing is copied · dev-only DB login role scoped to `cobalt_dev`, throwaway password · heartbeat stage `logger.info` lines not reaching `heartbeat.log` · old-tree `FinvizApiClient` CWD-relative vault path · `cobalt generated commit --dry-run` display defect · `_inflight` capture log-size rule.
- restic: Cobalt key store into the nightly include set + a restore proof (Opus prompt, 09-11 morning). B2 offsite leg still OFF — one local copy has already failed once (09-06).
- Bake-off prompt when a maintenance window is named.
- Dejan: OAuth Publish retry + `uv run cobalt notify email-auth` before 09-15 (token expires ~09-15) · unset `COBALT_VAULT_PATH` in his interactive shell · `git push`.
- Carried unchanged from 09-09: 4-bit vs 8-bit product call (folded into the bake-off) · Mattermost DB password rotation path + rotation · demote `cobalt` from superuser · seat-usage fallback reason-class column + AMBER (L25) · Qwen Code upstream issue (his filing).
- Ledger hygiene: §2 DECISION LOG stops at 08-31 and §3 / §4 still describe the slice-2 era. Ruling owed — refresh them or retire them in favour of the appendix.

### 2026-09-11 — heartbeat fix verified, Qwen day-open forensics, S2-P1 LIVE attempted and STOPPED (Opus 5 CTO chat; local Qwen seat; Sonnet hub; GPT-6 Astra) — OPEN, resume from OWED below

RULINGS
- R1 HEARTBEAT REGRESSION vs S2-P1, sequencing: S2-P1 LIVE takes tonight, the heartbeat regression takes Saturday morning. One production deploy per evening (L43); the regression loses nothing (beats survive, exit 0, keep cadence, and there is no note to write to); Saturday is a market holiday, all `overnight`, so a heartbeat deploy has no exclusion window to work around. Accepted cost: one night of ~21 RED beats and 21 alert emails.
- R2 §6 WINDOW WAIVED FOR 09-11 ONLY. The plan's "never 09:00–16:00" bar was waived at 13:46 ET: he had finished trading, nothing was load-bearing, and the Finviz contact in LIVE is ~4–6 requests (`--ft-compare`), not the 612-request throttle probe the bar was written for. The waiver is for that day only and does not amend §6. STANDING: the 09:00–16:00 bar is to be re-derived once the poller has run real sessions and the request rate against the 30 rpm ceiling is measurable — the shared-Finviz-login argument weakens as Cobalt becomes the primary consumer of that login.
- R3 LOCAL-SEAT DOCTRINE (new, from the Qwen run): the local seat READS AND JUDGES, never COMPOSES. Reading logs, running fixed commands, verifying, diagnosing — cheap. Generating long prose — ~7k tokens of report took 20+ minutes of a 50-minute run. Bounded read-and-judge tasks only: no report authoring, no source code, nothing whose OUTPUT is long. Every local-seat prompt carries a cost estimate up front, the way a METER line does for the paid houses, so a run that is about to be expensive can be refused BEFORE it starts, not discovered at minute 50. A long local run is acceptable when it is work that was chosen; it is not acceptable when it is work nobody authorised.
- R4 ASTRA ROUND 1 ACCEPTED, no round 2. All six findings adopted without dispute (detail in FACTS).
- R5 RESTIC DEFERRED, not owed: no cloud storage purchase while the local storage question is open. The failed disk was a different SSD; the current leg is a spinning USB drive kept permanently attached. Revisit only as restic→rclone→Google Drive (restic has no native Drive backend), and only after measuring vault + dump size against the 15 GB free tier. Removed from OWED; re-enters when that sizing is done.
- R6 LEDGER §2/§3/§4 — ON RADAR, not ruled: §2 DECISION LOG stops at 08-31; §3/§4 still describe the slice-2 era. Take it to the architect (Fable, after the Sunday reset) with Astra as reviewer — keep, refresh, or retire into the appendix. No edits until then.

FACTS — HEARTBEAT FIX VERIFIED
- The 09-10 market_reset fix HOLDS. First trading night after deploy: 4/4 in-window beats logged `vault_outcome=deferred_market_reset` and exited 0; `session_blocks` (actor `vaultwrite:heartbeat:%`) still exactly 8, newest row 2026-09-09 20:59 ET; no `FAILED: SessionBlocked` after 09-10; no gap >20 min across 19:45→21:15 (the ~75-minute hole did not recur). Verified read-only on the local Qwen seat, report `docs/40 - DevDocs/reports/day-open-2026-09-11.md`.
- NEW REGRESSION INTRODUCED BY THAT FIX, not yet repaired: 21 consecutive beats went RED 00:13→05:14 ET on `vault unit failed — daily-note writer returned no result`, each sending an alert email; recovery at 05:29, the first beat after `prefill-daily` ran ~05:15. Cause confirmed by the daily note's creation time: between midnight and prefill-daily the new day's note does not exist, the writer returns `None`, and the fix ruled `None` = `failed` (Astra round 2, item 2). It recurs every night until fixed.
- FIX SHAPE, not yet built: "note does not exist" deserves its own outcome — `deferred_note_absent`, the same shape as `deferred_market_reset` — rather than being folded into `failed`. Second defect found while diagnosing: the error string names no path, so "note missing" and "writer looking in the wrong place" were indistinguishable without a `stat`. The error must name the path it looked for.

FACTS — QWEN DAY-OPEN RUN (the seat's first real outing)
- VERDICT: a win for the 27B, and the slowness was the architect's prompt design, not the model. Judgement sound; all four adaptations disclosed and justified (`cobalt_jobs` has no timestamp column; `heartbeat_source` is a column not a JSON field; `archiver.log` empty by design with real output in `archiver.err`; the Q3 grep returned job tables with no timestamps, so it went and found per-beat lines rather than inventing a cadence). Two of those four were errors in the architect's prompt.
- It CAUGHT ITSELF FABRICATING: wrote `write_id=2328` in the report, re-read its own source output, found 2327, corrected it, and articulated the rule — never write down a number you did not see in the output. The correction is on disk (2327 and 2330 present, no 2328). Load-bearing figures are all quoted from output blocks rather than composed.
- It also flagged, unasked: main had advanced one commit past `16847eb` (`dd84d14`), and the worktree was at `d90a43b` not `7141670`. Both benign, both flagged rather than cleaned.
- 50-minute run, ~34k tokens. Breakdown: a 24,665-byte report (~7k tokens) at local generation speed, hitting the output limit and requiring chunked rewrites; 262k context at 45.8% used, slowing every token; four adaptation detours; one self-audit pass.
- MEMORY: the seat wrote two files in its OWN area, not the repo — `~/.qwen/projects/-Users-cobalt-cobalt/memory/MEMORY.md` and `memory/project/day-open-routine.md`. Content was checked and is ACCURATE (refusal baseline 8, the market_reset window, read-only discipline, the `cobalt_jobs`-is-a-registry correction). Nothing wrong is stored. Two older global files (`~/.qwen/memories/`, Warminster PA as default location) are unrelated and harmless. No agent memory file exists anywhere in `~/cobalt`.
- STRUCTURAL GAP: each house reads a different startup filename from the project root — `CLAUDE.md` (exists, committed, working as intended), `AGENTS.md` (Codex), `QWEN.md` (Qwen Code). Only Claude's exists. OWED: a thin repo-owned stub per house pointing at one shared context document, so the truth lives in git and each house holds a pointer, not a copy.
- NOT the Qwen seat: `docs/60 - Agent Output/Morning_Briefing_2026-09-11.md` (a scheduled agent job, `logs/agent_2026-09-11.log`) and `configs/cobalt/rules.yaml` (the `generated` job re-ran 05:15 and stamped a new `generated_at`; `source_sha256` unchanged, so no rule changed). That job dirties the working tree every morning with a one-line timestamp — ops-queue nuisance, not a defect.

FACTS — ASTRA ROUND 1 ON THE LIVE DEVIATION (accepted, all six)
- (a) SOUND: moving the stage-1 merge boundary through the defect-fix commit stays inside the code rollback domain; neither fix touches the migration or performs a vault write. Condition: recompute the L2 restart file AFTER the rebase against the new STAGE1_SHA — never reuse an earlier run's output; the tool derives imports from its executing checkout, so a stage-2 checkout computing a stage-1 range can legitimately disagree, and that disagreement is a STOP.
- (b) SOUND: `pre-s2-p1...STAGE1_SHA` remains meaningful post-rebase; `pre-s2-p1` at `dd84d14` is an ancestor of STAGE1_SHA.
- (c) SOUND for this history, guard insufficient in general. Uniqueness of the YAML-deleting commit does not catch a split: STAGE1_SHA could already hold the source switch, or reverting STAGE2_SHA could restore the YAML without its reader. Adopted: scope the search to `pre-s2-p1..HEAD_SHA`, verify the deletion commit ALSO contains the complete `archiver/config.py` source switch, verify every commit after it is documentation only, and pin full shas.
- (d) BLOCKER, adopted: re-run the offline gate AFTER the rebase, before the L2 merge — the rebase produces a tree the hub never tested. ~18 s. Also corrected the architect's premise: `dd84d14` is NOT docs-only, it touches `configs/cobalt/rules.yaml` (timestamp) plus `archiver-runs.md` and `seat-usage.md`. Low risk; no DB-suite rerun warranted. O10's validator is not covered by offline pytest and is proven instead by L4's `cobalt validate` on main.
- (e) SOUND as deferred: L10–L12 are provable in `overnight`, but active-session ranking is not. Adopted: preserve L13's 20:00–21:00 pause and 20:30 archiver proofs explicitly, and the S2 tripwire must not read deferred evidence as completed acceptance.
- (f) Two conditions adopted. L12's GREEN requirement is NOT waivable by the known regression (which cannot appear before ~00:13 anyway); unrelated RED remains a failure. AND — the finding of most lasting value — once Saturday's heartbeat fix lands on main ABOVE this deploy, a `reset --hard pre-s2-p1` would silently delete it; from that point any S2 rollback must be `git revert` of the stage-1..stage-2 merge range instead.
- Architect error: Astra was pointed at plan/report paths in `~/cobalt`. They exist only in the worktree — it had to hunt before finding them. Same class as the `_inflight` delivery problem.

FACTS — S2-P1 LIVE ATTEMPT, STOPPED AT L1
- STOP #1 (correct, hub): the hub refused to start, citing the dispatch's omission of §6's 09:00–16:00 bar as a conflict with the authoritative plan, on a deploy involving a live migration, a vault write and launchd changes. It ran nothing but read-only checks. Resolved by R2's written waiver, with the waiver's reasons recorded in the report.
- L0 DONE: `pre-s2-p1` tagged at `dd84d14`. Dirty set matched the known set exactly. This tag is the only change made to the repo all evening.
- STOP #2 (correct, hub): L1 `cobalt backup run` FAILED. `pg_dump` of `cobalt_brain` completed (411.1 MB); the restic snapshot to `/Volumes/COBALT-BACKUP` never finished and hit the job's own 3600 s timeout at 15:09:58 ET. No restic id. The hub halted per L1's hard-precondition rule, attempted no retry and no substitute, and escalated. Correct behaviour twice in one evening.
- NOTHING IS DEPLOYED. Main untouched at `dd84d14`. Branch `sprint-2/radar-pool` unmerged at `d90a43b`, never rebased, never pushed. No migration run, no plist installed, no vault write, no resident started.

FACTS — THE BACKUP FAILURE, ROOT CAUSE FOUND, CONSEQUENCE STILL OPEN
- ROOT CAUSE of the L1 hang: macOS TCC. `/Volumes/COBALT-BACKUP` was unreadable by every interactive process — `ls` returned `Operation not permitted` even under `sudo` (TCC sits above root). The long-running herdr server held a stale denial and every child shell, agent tab and `sudo` inherited it. Two permission dialogs clicked on the Mac during the run were the same block surfacing. Privacy & Security → Files & Folders already showed Removable Volumes ON for herdr, Terminal and `uv` — the grants were correct, but only read at process launch.
- FIXED BY: killing the herdr SERVER process (`pkill -f 'herdr server'` — the client reattaching is a second process; detaching or closing the space does NOT release the grant) and relaunching from a freshly started Terminal. `ls /Volumes/COBALT-BACKUP/` then worked.
- The launchd nightly job was NEVER affected — it has its own grant, and 09-10's 21:40 run completed normally (`7fc859ae`, 343.9 MB added, F17 DONE).
- Path correction for the record: the repository is `/Volumes/COBALT-BACKUP/restic`, NOT `/Volumes/COBALT-BACKUP/cobalt`.
- OPEN AND SERIOUS: `restic snapshots` returned EMPTY — no rows, no error, no password prompt. The hub separately measured only 438 MiB used of 931 GiB. Yet 09-10's log records a snapshot adding 343.9 MB, and the on-disk README states the repository was RE-INITIALISED 2026-09-06 after the original SSD stopped enumerating on any machine, losing the prior repository and its one snapshot. Either the empty result is a silent auth failure, or the nightly backup has been reporting success while retaining nothing. UNRESOLVED — this is the first thing to settle, ahead of the deploy.
- SECURITY, action owed: `/Volumes/COBALT-BACKUP/RESTIC-PASSWORD-README.txt` stores the repository password in cleartext ON the backup disk. It was read into a chat session on 09-11 and must be treated as EXPOSED. Rotate and update the vault key `RESTIC_PASSWORD`. Also reconsider whether that README belongs on the disk at all: it defends against losing the password with the Mac, but anyone holding the drive then holds both the backups and the key — the vault copy plus LastPass already covers recovery.

OWED — RESUME HERE
1. BACKUP INTEGRITY, before anything else: `export RESTIC_PASSWORD=$(grep RESTIC_PASSWORD= /Volumes/COBALT-BACKUP/RESTIC-PASSWORD-README.txt | cut -d= -f2); restic -r /Volumes/COBALT-BACKUP/restic snapshots; du -sh /Volumes/COBALT-BACKUP/restic`. Snapshots present → silent auth failure, repo healthy, proceed. Genuinely empty → the nightly backup has been a green light over nothing since 09-06, and that outranks the deploy entirely.
2. ROTATE `RESTIC_PASSWORD`; update the vault key; decide the README's fate.
3. S2-P1 LIVE — re-paste the full dispatch from the CTO chat (SESSION: fresh, starts at STEP 0; the existing `pre-s2-p1` tag is expected, not an error). All six Astra conditions are folded into it. Saturday daytime is a valid window per §6 and carries no exclusion. The one human step is the HITL token at STEP 8; `git push` after.
4. HEARTBEAT REGRESSION — Saturday morning: plan → Astra review → Sol builds → hub verifies → deploy. `deferred_note_absent` as its own outcome; the error must name the path.
5. `cobalt day-open` — an S2 item: the checks run in code, the command emits the report, the local seat runs one command and adds a verdict. Turns a 50-minute run into two minutes and makes fabrication impossible. Ruling owed on S2 vs S3.
6. Repo-owned house stubs: `QWEN.md` and `AGENTS.md` alongside `CLAUDE.md`, each pointing at one shared context document.
7. HIM, by 09-14: OAuth Publish retry + `uv run cobalt notify email-auth` — the refresh token expires ~09-15 and this is the channel that reports overnight failures. Also: file the Qwen Code upstream issue on HuggingFace; unset `COBALT_VAULT_PATH` from his interactive shell (it points at the production vault).
8. Ops queue, unchanged from 09-10: `additionalDirectories` for `~/cobalt-wt`; worktree credential override (env-file) so nothing is ever copied; dev-only DB role scoped to `cobalt_dev`; heartbeat stage `logger.info` lines not reaching `heartbeat.log`; old-tree `FinvizApiClient` CWD-relative vault path; `generated --dry-run` display defect; `_inflight` capture log-size rule; H1 migration round-trip flaking on a shared-DB race; the nightly `generated` job dirtying the tree daily.
9. MONDAY 09-14: L13 session acceptance (04:00 scanning, 09:30 → RVOL, 10:00 Day Scan first among screens, 16:00 → volume) — deferred, not skipped, and also the S2 tripwire date.
10. `~/cobalt/.env` CARRIES PRODUCTION CREDENTIALS (`cobalt_brain`), not `cobalt_dev`. The 09-10 DB-proof rule's phrase "pointed at cobalt_dev" was wrong and must be corrected wherever repeated: the copy cannot be aimed, and safety comes from the code's own gates (`dev_env` autouse fixture for pytest, `cobalt.devdb` for CLI work). RESOLVED 09-11: `bars` does not exist in `cobalt_brain`, so the 60-ticker backfill and replay rows landed in `cobalt_dev` as intended. No production contamination.

STANDING RULE ADDED 09-11 (from the day-open stall): evidence lands in the REPORT FILE in the same turn as the work, before it is summarised in chat. A cleared session takes its narrative with it and only the file survives — the 09-10 hub had to re-derive an entire phase's evidence from `cobalt_dev` because the previous session reported its results in chat and never wrote them down.


- **L44 Equal access (09-12):** No agent has second-class access. Every house — Anthropic, OpenAI, local, any future one — gets the same information the architect gets: repository, production vault, reports, plans, logs, ledger, memory files. No exceptions, no per-house withholding. **L45 Test against the real artifact (09-12, supersedes and revokes R2):** No parser, reader or validator is specified or tested against an invented fixture when the real artifact exists. The real artifact's shape is committed as a test fixture, and a change to it must fail a test before it reaches production. R2 ("the repo ships exactly one synthetic screen") is revoked as the root cause of the 09-12 propose failure. **L32 clarified (09-12):** Finviz `f=` filter strings ARE user data and are NOT secrets — they need no protection and may be committed. Classification and protection are distinct; do not conflate them. **Standing:** Dejan rules. Workers state objections; they do not decide against a ruling. The architect seat may be assigned to any house by his ruling, with another house reviewing — L29's default split is a default, not a fixture.

### 2026-09-12 — R2 revoked, equal access, parser design (Astra architect / Opus review) — rulings

RULINGS
- R1 **L44 EQUAL ACCESS.** No agent has second-class access. Every house — Anthropic, OpenAI, local, any future one — gets the same information the architect gets: repository, production vault, reports, plans, logs, ledger, memory files. No exceptions, no per-house withholding. Corollary added 09-12 after a dispatch error: a worker given a design or build task is issued WRITE access to its own workspace as a matter of course. Astra was launched `-s read-only` and could not write its own plan file; the hub had to extract the plan from the session capture. Read-only is for verification runs only, never for a worker that must produce an artifact.
- R2 **L45 TEST AGAINST THE REAL ARTIFACT — supersedes and revokes the old R2** ("the repo ships exactly one synthetic screen"). No parser, reader or validator is specified or tested against an invented fixture when the real artifact exists. The real artifact's shape is committed as a test fixture, and a change to it must fail a test before it reaches production. The revoked rule is the direct root cause of the 09-12 production failure: the parser was specified against an imagined note, met the real one for the first time mid-deploy, and Astra — once pointed at the real file — found SEVEN extraction defects where we knew of two.
- R3 **L32 CLARIFIED.** Finviz `f=` filter strings ARE user data. They are NOT secrets, need no protection, and may be committed. Classification and protection are distinct and must not be conflated.
- R4 **FIXTURE POLICY: real-shape, not verbatim.** `tests/fixtures/radar/radar-screens.real-shape.md` carries all four real headings, real markup, real glosses, real filter strings, real export URLs and real columns; personal attribution, dates and preset IDs are stripped. Both options exercise all seven defects identically — the only difference is whether incidental personal detail lives in git permanently. His screens' filter strategies are in git either way, which R3 permits. THE TRADER'S NOTE IS NOT EDITED: Astra's inventory ruled that every divergence is fixed in the parser, not the note.
- R5 **POOL: 50 NAMES STAYS. Scan interval 90 s. Finviz ceiling raised 30 → 40 rpm.** 50 names / 90 s = 33 rpm, inside 40 with real headroom. Astra's proposal to cut the cap to 18 is REJECTED — the pool width is a trading decision, not a technical one, and the request rate has two levers, not one. Basis for 40: the 09-10 throttle probe ran 612 real requests across four grids with zero non-200s; 30 was that measured result halved by a 0.5 safety factor, not the point of failure. 40 remains well inside demonstrated tolerance. Provisional until the poller runs real sessions — revisit with observed data, and the ceiling is his to set, never settled silently in a config file.
- R6 **DEJAN RULES.** Workers state objections; they do not decide against a ruling. The architect seat may be assigned to any house by his ruling with another house reviewing — L29's split is a default, not a fixture. This session ran Astra as architect and Opus as reviewer.
- R7 **BUILDER: GPT-5.6 Sol at high effort**, per L29's implementation floor and Astra's own recommendation. Sol receives the LIVE report and the parked-state block so it builds with deployed-state context — which answers Astra's self-argument against itself. Second choice Opus 5 if the patch grows into a write-path redesign or exceeds ~400 lines.

FACTS — THE DESIGN RUN
- SEVEN extraction defects in `src/cobalt/radar/propose.py`, not two: bold markup closing after the colon (`**Sort:**`); the `Filters (\`f=\`)` annotation; inline English glosses on every filter token, which must be PRESERVED VERBATIM; the Sort bullet carrying code plus prose plus columns plus preset commentary where the parser takes the whole remainder; `Columns` appearing inline inside the Sort bullet rather than as its own field, to be derived not defaulted; active windows expressed as prose intent ("after 10:00") rather than `- Active: HH:MM to HH:MM`; and all four real export URLs omitting the `o` parameter, which is valid and must not be an error.
- NO NOTE EDITS REQUIRED. "Morning" and "premarket" genuinely lack exact end times — D13's PROPOSED defaults stand rather than guessing 09:30 / 10:00 / noon.
- DRIFT MECHANISM: new `cobalt radar screens validate --pool-block <file>` — offline, no network, no DB, no vault writes; hashes the note bytes and compares derived fields against installed YAML. Run pre-deploy, pre-proposal, post-edit, and in the hub checklist.
- TWO PRODUCTION BLOCKERS ASTRA FOUND UNPROMPTED, both folded into scope. (1) The pool is over budget even after the parser fix — current config computes 61 rpm. Resolved by R5's 90 s interval and 40 rpm ceiling, not by cutting the pool. (2) **`radar sources` validates only the Lists note — not Screens, not the pool block.** LIVE's STEP 9 therefore cannot prove what it claims to prove; we were one ruling away from reading an empty check as a green light. This is the most consequential finding in the run and is independent of the parser.
- LIVE RESUME: the parked state is safe to hold — stage-1 schema live, ASET on a stamped card, archiver on committed `watchlists.yaml`, radar disabled and unlaunched. On resume, re-run STEP 8 (L6) through L13 in full; do NOT repeat STEPS 5–7 unless a fresh L42 derivation forces it. Target: deploy Sunday 09-13, Monday 09-14 checks at 04:00 / 09:30 / 10:00 / 16:00 / 20:30. RESTARTS provisional: `com.cobalt.radar`.
- CUT LIST if Sunday runs short: structured gloss semantics, general Markdown parsing, arbitrary English scheduling, screen-editing UI, broader taxonomy/ranking redesign, throughput experiments to justify the cap. DO NOT CUT: real-input fixtures, budget validation, archive equality, apply guards. If the gates do not finish Sunday, hold the parked state and report the tripwire missed — do not move dates and do not claim acceptance.
- METER: no figures available, the seat-usage sheet is human-entered and blank. Sol draws one 5-hour window (~90–150 min, ~15–30k tokens output), preserving scarce Anthropic capacity for rulings and the still-unbuilt heartbeat fix. Fable resets Sunday 13:00 ET.

FACTS — MEMORY LAYER WIRING, FOLDED INTO THE BUILD
- The Obsidian + Postgres memory layer is built and populated (`6 - Permanent/Memory/` with INDEX, preferences, profile, areas/, people/, topics/, and the 09-05 Anthropic import). It is meant to be THE memory for every agent; no house keeps a private store.
- BUT ONLY `CLAUDE.md` EXISTS at the repo root and only it points at the vault index. `QWEN.md` and `AGENTS.md` do not exist, so the Qwen and Codex houses wake up blind and receive whatever context a human remembers to paste. That is why the local Qwen seat wrote its own day-open routine into `~/.qwen/projects/.../memory/` instead of reading the vault.
- Same root cause as the parser defect: a design ruled once, carried by whoever remembered to say it, never written into a file the agents actually read.
- FOLDED INTO THE SOL BUILD: create `QWEN.md` and `AGENTS.md` as thin repo-owned stubs pointing at the vault INDEX, alongside `CLAUDE.md`. OPEN QUESTION for that build to answer, not assume: whether Qwen Code's private memory path can be redirected to the vault or its private store disabled — a context file alone will not stop it writing to `~/.qwen` if its configuration says otherwise. Same question for the Codex houses.

OWED — unchanged and still open
1. HEARTBEAT REGRESSION, unbuilt: nightly RED 00:13→05:14 on `vault unit failed — daily-note writer returned no result`, ~21 alert emails, recovering when prefill-daily creates the day's note ~05:15. Fix shape ruled: `deferred_note_absent` as its own outcome, and the error must name the path it looked for.
2. ROTATE `RESTIC_PASSWORD` — read into a chat session on 09-11, treat as exposed. Update the vault key; decide whether `RESTIC-PASSWORD-README.txt` belongs on the backup disk at all.
3. `cobalt day-open` — checks in code, command emits the report, local seat runs one command and adds a verdict. Ruling owed: S2 or S3.
4. HIM by 09-14: OAuth Publish + `cobalt notify email-auth` (token expires ~09-15) · Qwen Code upstream issue on HuggingFace · unset `COBALT_VAULT_PATH` from his interactive shell · `git push`.
5. MONDAY 09-14: L13 session acceptance — deferred, not skipped; also the S2 tripwire date. Deferred evidence is not completed acceptance.
6. Ops queue unchanged, plus: the restarts classifier has no carve-out for a generated-timestamp-only change to `configs/cobalt/rules.yaml`, so any range spanning a nightly `generated` commit ESCALATEs and maps to all six readers; and it is unconfirmed whether the nightly `generated` job restarts the residents that list `rules.yaml` in their `reads:` — harmless for a timestamp, not harmless the day a rule genuinely changes.



### 2026-09-13 — S2-P1 LIVE (radar shipped), heartbeat verified, equal-access aftermath (Opus 5 CTO; Astra architect; Sol builder; Sonnet hub; local Qwen seat) — CLOSED

RULINGS
- R1 **L46 ONE RUN, ONE COMMIT.** Committed to main BEFORE the next run starts. No long-lived branch while a single agent is working; a clean tree every run. `sprint-2/radar-pool` stayed open four days while main advanced, and the divergence stopped a deploy with a merge conflict that was not parallel development — it was one line of work with a stale checkpoint. A branch that outlives its own deploy is the defect, not the merge that follows it. With several agents working in parallel later this becomes unmanageable, so the discipline starts now. That branch was deleted at the end of this deploy.
- R2 **L47 METER IS NOT THE ROUTER.** A worker stopping on its usage meter is an ESCALATION TRIGGER, not a reason to wait: mid-build the hub hands the work to the other house at once, partial work left in place with a CONTINUE brief. The one exception is a handover that would cost more than the wait, stated and justified in the report. But the switch is PER-BUILD, not sticky: every build starts from the assessment of the task itself, the meter is a precondition checked BEFORE launch, and if the right model is unreachable and the alternative is a poor fit, say so rather than proceed. First exercise: Sol stopped on its meter at 10:20 with ~85 minutes left on its clock, the hub judged the wait-exception did not apply and handed the heartbeat build to headless Opus. Correct call.
- R3 **HOUSES ARE SWITCHABLE AT WILL.** A Sonnet hub can launch Opus HEADLESS (`claude -p`) exactly as `codex exec` launches Sol — an Anthropic builder does not require an attended Code session. Plans written to disk are what make the switch free: no house has privileged understanding of a plan any other house can read. The cost of switching is meter and dispatch shape, never comprehension.
- R4 **WORKERS GET WRITE ACCESS TO THEIR OWN WORKSPACE** as a matter of course. Read-only is for verification runs only, never for a worker that must produce an artifact. Astra was launched `-s read-only` for a design run, could not write its own plan file, and the hub had to extract the plan from the session capture.
- R5 **KEEP THE RENAMED L45 SCAN.** `test_screen_filter_values_live_only_in_approved_radar_fixtures` stays, at full coverage. On 09-12 the architect deleted its predecessor from main (7fe009d) believing it enforced the revoked R2 — but the branch had already re-founded the same check on L32/L45 and renamed it. The branch was ahead of the architect; deleting it removed L45's only enforcement arm. When it then flagged a real report, the remedy was to REDACT THE REPORT, not narrow the test: two edits to `day-open-2026-09-10.md` (four filter strings replaced with pointers to the approved fixture, and one line rewritten to describe a grep pattern rather than quote it). The hub refused an instruction to narrow the scan's scope, and was right to — narrowing a leak test so a failing file passes is the wrong shape regardless of the reasoning behind it.
- R6 **HITL IS A CONVENTION, NOT A MECHANISM — and the flag must stop implying otherwise.** `--hitl` checks only that the string is non-blank, then passes it through as a free-text `run_id` label. It is never looked up or verified. No `cobalt hitl issue` command exists. The OTET design was never built (`docs/20 - Assessment/03-mattermost-hitl.md`) and the `hitl_proposals` / Mattermost approval flow in the `cobalt_agent` tree has NO code path to `radar screens/lists apply`. The real gate is `--sha256`, which is genuine: it guarantees what is written is exactly what was reviewed. OWED: either build token issuance or rename the flag. Approval marker used for this deploy: `dejan-2026-09-13`.
- R7 **POOL NUMBERS AMENDED, on Sol's objection.** The 09-12 ruling computed 33 rpm as if the pool were the only consumer of the Finviz transport; the 4 screens and 7 list chunks poll on the same cadence, taking the real total to 40.67 against a 40 ceiling. Sol raised it rather than shipping over the ceiling. FINAL: cap 50 names (unchanged), scan interval 100 s, ceiling 40 rpm, verified total **36.60/40 rpm** (pool 30.00 + screens 2.40 + lists 4.20). Rejected: raising the ceiling to 45 (a second intuition-set number in one day, on the day the first was wrong) and shipping at 40.67 to let the token bucket throttle (Monday's cadence would silently fail to complete). A BUDGET CHECK THAT MEASURES ONE CONSUMER IS NOT A BUDGET CHECK — the total-demand computation is now the rule, with a test proving refusal when the total exceeds the ceiling while the pool alone would pass. Staggered cadences (screens and lists slower than the pool, since they change far more slowly) is the correct long-term fix and is queued, not built. The ceiling and the cadence are his to set and are never settled silently in a config file.
- R8 **`--ft-compare` SKIPPED for this deploy**, deliberately, not silently: it needs the vault unlocked for the Finviz token and the master key was not put into the session for an optional diagnostic. OWED as a clean follow-up.
- R9 **SEQUENCING:** heartbeat fix deployed 09-12, S2-P1 deployed 09-13. One production deploy per evening (L43) held throughout.

FACTS — WHAT SHIPPED
- **S2-P1 IS LIVE.** `com.cobalt.radar` installed, bootstrapped, registered and `enabled: true`. Tags `pre-s2-p1` (dd84d14) · `s2-p1-stage1` · `s2-p1`. Branch and worktree deleted. Radar scans the four screens on a 100 s cycle and maintains a ranked pool of up to 50 names: volume premarket, RVOL after 09:30, Morning Low Float always volume, Day Scan joining at 10:00 and ranking first among screens, stickiness 3 scans, dropped names carrying `excluded_by = config_cap`.
- **THE SCREENS NOW LIVE IN THE VAULT.** Six write_ids across `1 - Trading/Radar Screens.md` (4 screens + pool block) and `1 - Trading/Radar Lists.md` (created). Prose above the inserted blocks byte-identical. `configs/cobalt/watchlists.yaml` deleted; the archiver reads its targets from the Lists note. He edits the note in Obsidian; Cobalt reads it.
- **WHAT IS NOT SHIPPED, stated plainly:** nothing surfaces the pool to him. Monday looks identical — ASET sheet as before, plus one `radar` line in the heartbeat. Seeing the names means querying `radar_pool` / `radar_membership` directly. The Trade Radar card is the next piece of work and is what makes this visible.
- **HEARTBEAT: BOTH FIXES PROVEN OVERNIGHT.** 73 `deferred_note_absent` beats between midnight and prefill-daily with NO alert emails (before the fix: ~21 RED beats and 21 emails a night); 8 `deferred_market_reset` beats in the 20:00–21:00 window, so the new outcome did not disturb the old; `session_blocks` steady at 8 since 09-09. Three days ago the heartbeat was dying silently for 75 minutes a night and it took two days to notice.

FACTS — THE PARSER AND MARKER DEFECTS
- The 09-12 parser fix landed: SEVEN extraction defects, not the two known — bold markup closing after the colon; the `Filters (\`f=\`)` annotation; inline English glosses PRESERVED VERBATIM while codes are extracted; the Sort bullet carrying code plus prose plus columns plus preset commentary; `Columns` inline rather than standalone, derived not defaulted; active windows as prose intent ("after 10:00") with the D13 PROPOSED default where no end time exists; and export URLs omitting the `o` parameter, which is VALID. No note edits were required — every divergence was fixed in the parser.
- Then an EIGHTH, found only at `apply`: `MarkerError: Invalid section name 'Screen 1 — Up Gappers'` — the marker's section id was derived from the heading text, which carries spaces and an em-dash. Neither `validate` nor `propose` can catch it because only `apply` constructs the marker. FIXED by deriving from the heading ORDINAL: `radar-screen-N` / `radar-screen-N-definition`, immune to his editable display prose.
- **THREE DEFECTS OF ONE CLASS IN ONE WEEK** — specified against an invented artifact, met the real file in production. That is what killed R2 and what L45 exists to prevent.
- ALSO FIXED, found unprompted by Astra: `radar sources` validated ONLY the Lists note, not Screens and not the pool block — so LIVE's own proof step could not prove what it claimed. We were one ruling away from reading an empty check as a green light.

FACTS — THE DEPLOY ITSELF, six correct STOPs
The hub stopped six times and was right every time; every stop traced to a gap in the architect's dispatch, not a model failure. (1) The dispatch omitted §6's market-hours bar — waived in writing for 09-13 only. (2) `COBALT_ENV` unset at the snapshot step — the dispatch named it at the vault-write step and nowhere else; RULING 7 removed the default deliberately so nothing guesses which database and vault it points at. (3) A dirty `seat-usage.md` the architect had asserted was clean. (4) The rebase conflict from the four-day branch. (5) The L45 scan finding a real leak. (6) `screens validate` failing because stage 2 had deleted the `watchlists.yaml` it falls back on — resolved by extracting the retired file from its git blob (`bedf9bbf…`, 333 lines, matching the deletion diff exactly) and passing it explicitly. Two more followed: the locked vault refusing `--ft-compare`, and the DB credential missing from the worktree for `apply`.
PRE-APPROVALS that emerged and should become law rather than per-dispatch text: `COBALT_ENV=production` on any production command refusing for an unset environment; committing a machine-written file that dirties the tree; extracting a stage-2-retired file from its git blob.

FACTS — PROBES AND CLASSIFIERS, the recurring false-signal class
- `radar` probe (`probes.py:80-88`) checks `row is None` FIRST and returns RED before the session-aware branch is ever reached — so "no session has run, nothing to scan" and "a session ran and the resident failed to write" are indistinguishable. It will be RED every weekend. CORRECTION to the architect's assumption: `vaultwrite_blocks` does NOT have this defect, it is explicitly designed to avoid it. The actual precedent is `archiver_freshness`, already fixed once for this exact thing (`b481bd5 fix(heartbeat): archiver_freshness stops painting weekends red`). SECOND OCCURRENCE of a known pattern.
- `cobalt jobs restarts` has no classifier rule for a new top-level `.md` file, so `AGENTS.md` and `QWEN.md` ESCALATEd and mapped conservatively to all six residents. Same gap class as the `rules.yaml` timestamp incident. Ruled: restart only the residents that actually changed. Needs a real rule — documentation paths with no runtime reader derive no restart.
- `com.cobalt.herdr` has been RED since 09-12: the herdr SERVER process was killed to clear a macOS TCC block and its launchd job never came back. herdr itself runs fine, started by hand — launchd simply does not know about it. Clearing it means handing herdr to launchd, which drops every agent tab, so it waits for a moment when that costs nothing. A permanently RED beat is the alert fatigue that hid the 09-08 blackout.
- The archiver has not run in 37.6 hours and that is CORRECT — Saturday and Sunday are non-trading days. Last run Friday 20:53: 210 tickers, 3,160,954 rows, 0 failures, exit 0. The probe reports elapsed time without knowing the market is closed. Same class as the `radar` probe above.

FACTS — MEMORY LAYER AND THE LOCAL SEAT
- `QWEN.md` and `AGENTS.md` now exist at the repo root as thin stubs pointing at the vault memory index, alongside `CLAUDE.md`. Until today only `CLAUDE.md` existed, so the Qwen and Codex houses woke up blind and received whatever context a human remembered to paste — which is why the local seat wrote its own day-open routine into `~/.qwen/projects/.../memory/` instead of reading the vault. OPEN: whether Qwen Code's private memory path can be redirected to the vault or its private store disabled. A context file alone will not stop it writing there if its configuration says otherwise.
- The local seat's day-open run: correct judgement, all adaptations disclosed, and it caught itself fabricating a `write_id` and corrected it from its own source output. But 20 minutes and an API error before finishing, on ~10 greps. Under the 09-11 doctrine it READS AND JUDGES, NEVER COMPOSES — the report length is what costs it. `cobalt day-open` (checks in code, command emits the report, seat runs one command and adds a verdict) is the fix and is queued.
- `RESTIC_PASSWORD` was read into a chat session on 09-11 and must be treated as EXPOSED. The repository is healthy: 6 snapshots nightly, `/Volumes/COBALT-BACKUP/restic` (the repo path is `restic`, NOT `cobalt`). The 09-11 empty listing was a silent auth failure; 436 MiB for six ~470 MiB snapshots is deduplication working. STILL OWED: rotate the password, update the vault key, and decide whether `RESTIC-PASSWORD-README.txt` belongs on the backup disk at all given it puts the key beside the data.

FACTS — OAUTH, root cause found
The Publish failure was never a Google console bug. `gmail.send` was NOT REGISTERED AS A SCOPE AT ALL — all three scope tables on the Data Access page were empty. The console reported this as "complete your configuration on the Branding page", where every required field was in fact already filled. Scope now registered; Publish still greyed. The channel is currently healthy (`email-status` OK, last send today) but the Testing-status refresh token expires ~09-15. FALLBACK, two minutes: re-running `cobalt notify email-auth` buys another 7 days under Testing. Note `~/.cobalt/google-oauth-client.json` is shredded after every successful run by design and must be re-downloaded from Cloud Console → Credentials first; the consent flow binds a loopback listener on port 8765 and must run ON the Mac Studio or with that port forwarded.

OWED — THREE TRIBUNALS, all convene with Fable and Astra, in this order
1. **LEDGER TRIBUNAL — first, because it gates the others.** This file has grown to the point where superseded rulings sit alongside current ones with no precedence marker, and lower models have repeatedly latched onto a revoked rule and found the live one only on the second or third try. The architect did it too on 09-12, reading L32's exception instead of its clarification. Produce: the reconciled CURRENT STANDING LAW, plus a separate historical archive (moved, never deleted). ALSO RULE ON THE MECHANISM, not just the content: FOUR rules this weekend lived in prompts before they lived in a file — R2 survived past its usefulness that way, the memory-index pointer never reached the non-Claude houses that way, the routing amendment is carried in dispatch text right now, and so are the three pre-approvals above. What makes something law versus something a prompt carries? The real destination is the memory layer in `6 - Permanent`, not this file: when the local seat becomes Cobalt's hub it will arbitrate from MEMORY, and a 27B hub can apply a rule but cannot notice that two rules contradict each other.
2. **ROUTING TRIBUNAL — the right intelligence for the right job.** L29's floors ("Sol is the OpenAI implementation floor", "Opus is the implementation floor") came from his own defensiveness at a moment when he had been burned. They have since hardened into law that Astra cites to declare houses INELIGIBLE without assessing anything — it did exactly that this weekend, naming Sonnet and the local seat ineligible by rule rather than by judgement. TERRA AND SONNET HAVE FAR LONGER METERS AND HAVE NEVER BEEN TESTED AS BUILDERS. Open questions he wants answered: can Terra build what Sol builds? Is Sonnet a builder as well as a hub? Is Haiku enough for the hub seat? Produce a ROUTING RUBRIC keyed to HIS axis: **is the spec defensible against a real-world artifact and testable — then a lower model can build it, because there is nothing to infer and a wrong guess fails visibly — or is it a new horizon with undefined outcomes, where it needs a model that will notice the spec ITSELF is wrong.** Validate the rubric RETROSPECTIVELY against the last two weeks of builds in this ledger, where the outcomes are known, then reconcile the two houses' rubrics into one law replacing L29's floors. Caution to carry in: asking a model to judge another model's competence is the judgement models are worst at and most confidently wrong about, and Astra routing between OpenAI models has an incentive problem — the retrospective validation is what makes the rubric checkable rather than a guess. Evidence for it is in this weekend's record: three worker objections in one build (Sol's rate objection, Astra's `radar sources` finding, the hub's arithmetic correction), six correct hub STOPs, and one trigger-(d) handover.
   Also rule on the **LOCAL SEAT AS HUB**, which is the plan of record for Cobalt and the reason the ledger must be unambiguous. Evidence to weigh: on 09-13 the seat ran its day-open correctly — every command executed, every adaptation disclosed, verdict sound — but took 20 minutes on ~10 greps and died on an API error ("model response leaked thinking tags") before finishing its report. That is its SECOND harness-level failure (the first was a stuck background process on 09-11). The hub role is a HIGHER bar than the morning check: launching workers, waiting, verifying proofs against ground truth, and REFUSING TO PROCEED when a proof does not match — Sonnet did exactly that six times on 09-13, and every one of those stops prevented a bad deploy. Rule what the hub seat actually requires, whether a 27B can hold a dispatch's rules across a long session and stop on a mismatch, and what the fallback is when it cannot. The morning-check question is separate and already answered: `cobalt day-open` puts the checks in code so the seat runs one command and adds a verdict.
3. **GROK / CHIEF OF STAFF TRIBUNAL — third, after the two above.** Reference documents supplied separately (`GROKBOT_CHIEF_OF_STAFF_INSTRUCTIONS.md`, `PEER_REVIEW_DESK_SPEC.md`, `COS_VISUAL_AND_TWOWAY.md`) — these are a PROPOSAL and a stepping stone that proved the concept, NOT a design to be reviewed as-is. Ruled shape: **Grokbot becomes VIEW-ONLY over the Outbox** — a second Grok meter he can ask "what is moving and why is this a B", giving a double lane through one subscription; **Grok CLI does the real work**, owning EXECUTION of the scoring, writing through `vaultwrite` like every other agent; and **the three houses DESIGN the math**, because a scoring model feeding a trading card must be auditable by something other than the thing producing it. Questions the tribunal must settle: the integration seam (the spec assumes a plant writing `candidates.json`; radar writes to Postgres — that file does not exist and someone must build `radar_pool` → `candidates.json`); TWO RANKING AUTHORITIES (Cobalt's live volume/RVOL with stickiness 3 and cap 50 versus the spec's `rank_score` with hysteresis at +0.4/60s and −0.6/90s — they will disagree and the card cannot honour both); and THE NPV PROBLEM, which is the crux — `substance` depends on `materiality` depends on `NPV_base`, and NPV_base is a MODELLED number, so a scoring system built to stop numbers coming out of the air currently rests on a judgement dressed as a number. Rule whether Cobalt scores only on what it can source and verify, or carries modelled inputs explicitly marked as such.
- **STANDING, from the Grok proposal: a design that touches scoring, ranking or anything that reaches the card requires a TRIBUNAL before any build.** Not a review of the proposal as written — a tribunal PRODUCES the design, with the proposal as input. The bar it must clear before a line is built: (a) every number in the model is traceable to a source Cobalt can fetch and verify, or is explicitly marked as modelled and degrades the score accordingly; (b) exactly ONE ranking authority reaches the card, named, with the others feeding it or retired; (c) the integration seam is specified as a real artifact, not assumed — the 09-13 failures came from specifying against imagined files; (d) whatever computes the score is auditable by a house other than the one producing it. A proposal that cannot meet those is a stepping stone, not a design. Grok's Chief of Staff spec is the first thing through this gate and sets the precedent.

OWED — BUILD QUEUE
`cobalt day-open` (S2 or S3, ruling owed) · the `radar` probe cold-start/idle distinction · the `restarts` classifier rule for documentation paths · `vaultwrite_blocks`-class review of the other probes (`last_exit` displayed but not evaluated; missing herdr registry entries rendering OK) · id-less "unchanged" and dry-run vault writes still rating false RED · HITL token issuance or a flag rename · staggered screen/list cadences · the jobs that rewrite tracked files without committing them (this dirtied the tree and stopped two deploys) · `--ft-compare` follow-up · Qwen private-memory redirect.

OWED — HIM
OAuth: Publish or the 7-day re-auth fallback, before 09-15 · rotate `RESTIC_PASSWORD` · hand herdr to launchd when dropping the agent tabs costs nothing · file the Qwen Code upstream issue · unset `COBALT_VAULT_PATH` from his interactive shell (it points at the production vault) · `git push`.

MONDAY 09-14 — the real test
L13 session acceptance: 04:00 scanning, 09:30 → RVOL, 10:00 Day Scan first among screens, 16:00 → volume, plus the 20:00–21:00 pause and the 20:30 archiver run taking its targets from the Lists note for the first time. None of it was observable on a weekend, so it is DEFERRED, not skipped — deferred evidence is not completed acceptance. Monday is also the S2 tripwire date.

### 2026-09-13 — LEDGER TRIBUNAL (Fable architect / Astra reviewer / Dejan ruled)

MECHANISM RULING, verbatim (`~/tmp/tribunal-ledger/prompt-fable-r1.md:9`): "MECHANISM RULING (09-13, Dejan): standing law is split from the decision record. `6 - Permanent/Memory/LAWS.md` becomes the ONLY canonical current law: one entry per law, amendments rewrite the entry in place with a date, superseded wording moves to `LAWS-HISTORY.md`. PROJECT-LEDGER.md keeps appending as the dated RECORD — a ruling in an appendix is NOT law until folded into LAWS.md, and the fold is a hub job at every session close. Wake-up path for every house: CLAUDE.md / AGENTS.md / QWEN.md → memory INDEX → LAWS.md. The tribunal reconciles under this ruling; it does not relitigate it."

DISPOSITIONS (O1–O35, full drafts + evidence: `0 - Inbox/tribunal-ledger-2026-09-13/`)
- O1 — L28: restored the four clauses the 09-08 fold silently dropped (atomic write + mtime guard; unified diff in every report AND run log; the `com.cobalt.archiver` carve-out; "template cell/bullet") into current L28.
- O2 — L4 amended: a `.env` bootstrap tier is permitted, scoped to exactly the Postgres docker credential, the app DB login, and the Mattermost DB role — each also in VaultManager, nothing else.
- O3 — L11 amended: the invariant is "at least one human-only discretionary variable", not a fixed example; the tape read is today's, and may flip once L2/Time&Sales ingestion lands.
- O4 — L12 amended: the "ship with what's decided" principle is standing; the specific 08-22 two-week clock is spent and does not re-arm automatically → history (H-L12).
- O5 — L17/L39 reconciled, Reading B: synthesis on reasoning quality governs a council's turns 1–2; L39's turn-3 vote is the termination record, not a return to vote-tallying; a law file is never voted at all.
- O6 — L27: the 09-10 R11 merge (Max 20x escalation off the table) confirmed as folded.
- O7 — L32/L45, Reading B: L45's revocation of "one synthetic screen" does not reach L32's "repo ships one synthetic anatomy-only trade_def" shipping clause; both stand together.
- O8 — L41: moot — superseded in full by the L41 replacement below.
- O9 — L42: the "documentation paths with no runtime reader derive no restart" amendment is pre-worded into L42 now, marked PENDING, effective only when `cobalt jobs restarts` implements the classifier rule.
- O10 — L47, Reading B: the 09-10 "one relaunch with a CONTINUE line" rule is folded into L47 as the bounded form of its wait-exception, not a return to waiting as the default.
- O11 — L44: the write-access corollary stays inside L44 at its origin; no separate number assigned.
- O12 — L29: "never auto mode on a write path" restored (silently dropped by an earlier fold); L29 remains marked under review, routing tribunal, as of 09-13.
- O13 — Notation ruled: `L<n>` is reserved for laws; deploy-plan steps use `STEP-<n>`; session rulings are cited only as dated `<date> R<n>`, never bare; external documents cited by filename; the hub's fold job refuses a bare `R<n>`/`§<n>`.
- O14 — Explainability (LEDGER:223-227) is ruled INTO law; the other taxonomy-labelled rulings (anatomy-only, timeframe-agnostic trigger, modularity, calibration loop, 1-bar trail, advisory-exit) get a pointer to `TAXONOMY-DRAFT-v0_7 §0` instead of a LAWS.md entry. Explainability's own number is unassigned — see ESCALATE.
- O15 — LAW numbered L48–L56: P1, P2, P5, P7, P12, P13, P14, P15, P18 in that order. P9 and P20 returned to this record as DECISION/STATE, not law. P16 and P17 applied directly to CLAUDE.md (session hygiene; capture hygiene and DevDocs authorship).
- O16 — the mechanism ruling is now pasted verbatim above and stands as LAWS.md's preamble.
- O17 — the worktree rule (L54) stands as the earliest text; the "09-08 branch rule" it says it amends is still not found anywhere in this ledger — source remains owed.
- O18 — L15's carve-out wording (previously only in the decision log, LEDGER:48/:68) is merged into L15's own entry.
- O19 — status sentences moved out of law text into dated notes: L23's "mainframe untested, bake-off" gate and L25/L27's build-status parentheticals.
- O20 — no action: the Grok-seat and Codex `-a on-request` reversals are already resolved and historicized (H-Grok, H-L33); listed for completeness only.
- O21/O30 — L7 carries a note that the HITL token mechanism is owed; `--hitl <label>` is not verified and must not be read as satisfying the law.
- O22 — §1 kept, dated pointer to LAWS.md added below; §2 kept frozen at 08-31, dated pointer added below; §3 and §4 below have their stale lines struck with a date and pointer — no new current-state lines added tonight; the refresh itself is owed at the next session close.
- O23 — memory cap remeasured: INDEX+profile+preferences = 3,864 chars now; WAKEUP's proposed 125-char addition would land at 3,989 (11 under the 4,000 cap) — confirmed but NOT yet written (see ESCALATE, O24).
- O24 — the WAKEUP mechanism (stub → INDEX → LAWS, plus a direct LAWS line) is accepted as designed; installation into CLAUDE.md/AGENTS.md/QWEN.md/INDEX.md is held until LAWS.md actually exists at its vault path, per WAKEUP-draft's own bootstrap caveat (see ESCALATE).
- O25 — no action: Astra's citation audit found the input copies byte-identical to the originals; no copy drift.
- O26 — memory-layer convention: superseded LAW wording moves to LAWS-HISTORY.md with dated provenance; other memory files keep the existing "marked, not deleted" convention unchanged.
- O27 — L45's two companion rulings (fixture policy real-shape-not-verbatim; leak scan never narrowed) stay inside L45, not returned to the record.
- O28 — P13 confirmed as law → L53.
- O29 — DECISION, not law: the plan-template sentence "no production deploy 09:00–16:00 ET on a trading day unless waived in writing for that day" is ruled and recorded here; wiring it into an actual plan-template file is a separate, not-yet-scheduled build item.
- O31 — STRUCK: L15's "vault/.env/personal layer excluded" carve-out clause and the already-historical L17 privacy-dial clause are both fully superseded by L44 → history (H-L15-scope, H-L17a).
- O32 — the pre-MVP spike moratorium is scoped to the withdrawn R3/R5 decks (video ingestion, dictation plugin); the separate code-freeze lift (LEDGER:1045) is unaffected and stands.
- O33 — resolved by the O1/O5/O10 rulings above; no separate text needed.
- O34 — all three CLAUDE.md corrections applied: `:47` keeps its text and gains an L46 boundary sentence beside it; `:163-167` now admits AGENTS.md and QWEN.md as root markdown files; `:21-23` reworded to "never add gitignored material to git" (a commit restriction, not a read restriction — L44 unaffected).
- O35 — L39's pre-numbering text (H-Hub-numbering) is kept as comparison evidence, not treated as a revocation; no textual change to L39 itself.

CANONICAL LAW: `LAWS.md` and `LAWS-HISTORY.md` are staged FINAL at `0 - Inbox/tribunal-ledger-2026-09-13/` (56 laws, L1–L56, contiguous). No Cobalt command writes new files under `6 - Permanent/Memory/` — Dejan places both files at that path; see the hub report's ESCALATE line.

VERIFICATION: Terra (`codex exec -m gpt-5.6-terra -s read-only`) hit Codex's usage limit (retry 22:53) before it could run. Dejan ruled: substitute headless Haiku for the identical 35-row read-only citation-check task rather than wait or swap Codex models (same meter as tonight's routing-tribunal work). Haiku returned 35/35 YES, every row with a file:line citation; the hub independently spot-checked 10 of the 35 against the actual files and all were accurate. **Terra re-verification of the committed files is OWED at reset (22:53)** — any NO from that pass becomes a fix commit. Evidence copied to the routing tribunal at `~/tmp/tribunal-routing/haiku-citation-check-evidence-cobalt4f.md`.

CONCURRENCY INCIDENT (unrelated task, noted for the record): mid-session, a peer session (cobalt-b9, running a separate routing-tribunal task) mistakenly ran `git checkout -- CLAUDE.md`, silently reverting this session's in-progress CLAUDE.md edits. Confirmed and resolved by direct cross-session message; edits were reapplied and verified intact before this commit. No content difference from what is described above.

`RESTARTS: none` (documentation-only change; O9's classifier rule for this class does not exist yet — this line is asserted by the same 09-13 ruling that will become that rule).


