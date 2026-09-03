# docs/references — Index

Reference material for the Cobalt rebuild: SMB Capital trading education (setups, trades, playbook decks), Finviz Elite export-API screenshots, ASET grading / Daily Report Card artifacts, and mission-control / Obsidian-OS UI inspiration. Everything here is *input to the product definition* — the source-of-truth for what Cobalt's trading logic, research engine, grading, and front-end must reproduce. Grouped by category; one line per file.

> ℹ️ **Credentials note — see [§ Credentials](#-credentials) at the bottom.** The Finviz token visible in the 9 Finviz screenshots was rotated dead on 2026-08-22; the images are safe in version control.

---

## Finviz APIs (Elite CSV export automation)
Screenshots of Finviz Elite's "Automating Export" panel — the deterministic HTTP-export endpoints Cobalt's collector should use (`elite.finviz.com/export/<kind>?…&auth=<token>`; legacy `.ashx` 301-redirects). These define the Tier-1/fundamentals data surface (§7/§8 of the requirements) and validate the existing `FinvizApiClient`.

- **FinvizScannerAPI.png** — Screener export (`/export/screener?v=…&f=<filters>`). The scanner backbone: proves the filter-string → CSV pattern the pipeline already uses.
- **finvizstockapi.png** — Single-stock export (`/export/stock?t=MSFT&p=d`). Per-ticker OHLC/params; note `p=d` = **daily**, confirming Finviz alone won't give intraday bars (Pass 4 gap).
- **finviznewsapi.png** — News export (`/export/news?v=1`). Direct feed for the news-monitoring agent (§5) and `daily_in_play` catalysts.
- **finvizcalendarapi.png** — Calendar export (`/export/calendar/economic|earnings|dividends?dateFrom=…`). Economic + earnings calendar → catalyst calendar / earnings-event package (§8 Tier-1).
- **finvizlatestfiningsapi.png** — Latest Filings export (`/export/latest-filings?t=…`). SEC-filing awareness per ticker (dilution/S-3 monitoring, §8).
- **finvizinsiderapi.png** — Insider-trading export (`/export/insiders?tc=7`). Insider transactions — a named §8 Tier-1 field.
- **finvizmanagersapi.png** — Institutional managers export (`/export/managers?search=…`, holdings by slug/ID). Institutional-ownership concentration (§8 Tier-1).
- **finvizfundsapi.png** — Funds export (`/export/funds?search=…`, holdings). Fund holdings/ownership flow (Tier-2 swing input, §8).
- **finvizoptionsapi.png** — Options chain export (`/export/options?t=MSFT&ty=oc&e=<expiry>`). Options data — seeds the Tier-3 options fields (§8).

## SMB cheat sheets — Setups (context/regime)
SMB Capital "Setup" one-pagers: the market conditions that put a stock *in play* (the Level-2 context layer). These plus the Trades below are the exact playbook Cobalt must encode and grade.

- **Day 2.pdf** / **Second_Day_Play_Cheat_Sheet.pdf** — Second Day Play: Day-1 >1 ATR move closing top/bottom 20% of range, gap <⅓ of range, continuation. The only setup with a (broken) code implementation; full entry/stop/2×-range-target rules.
- **Gap & Go_ (1).pdf** — Gap & Go: expects immediate continuation off the open; momentum/trend-continuation.
- **Gap Up Into Resistance.pdf** / **Gap Down Into Support.pdf** — gap-into-level reversal setups (distribution/accumulation at a daily level).
- **Overextension.pdf** — unsustainable one-directional push → mean-reversion reversal setup.
- **Volatility In Range.pdf** — two-sided auction inside a bigger range; fade the extremes.
- **Range Break (1).pdf** / **Technical+Analysis+Range+Break+Trading+Cheat+Sheet.pdf** — range identification + break/retest/failed-break trade mechanics (2:1 R:R); the deep methodology behind several trades.
- **Setups & Trades Project.xlsx** — Cameron H's master taxonomy: which SMB names are **Setups** vs **Trades** (+ with-trend/countertrend). The canonical vocabulary for Cobalt's playbook schema.
- **These are setups and all others are trades.png** — Google-Drive view of the "Setups" subfolder; visual confirmation of the setup-vs-trade split.

## SMB cheat sheets — Trades (entry triggers)
SMB "Trade" one-pagers: precise entry/stop/exit rules, ideal time-of-day, factors that increase/decrease odds, and avoid-conditions — the deterministic logic Cobalt's grader/EV engine must compute.

- **9 EMA.pdf** / **9 EMA Reclaim.pdf** — **[priority setup: Scalp Radar 5+9 EMA continuation]** algo-buy-at-9EMA momentum trade and its reclaim variant; entry near/back-above 9EMA, 21EMA stop.
- **VWAP Continuation.pdf** — **[priority setup]** pullback-to-VWAP continuation of a morning move; entry near VWAP on trendline/range break, 21EMA trail.
- **Bouncy Ball Trade.pdf** — **[priority setup: Bouncy Ball]** weak in-play stock making shallower bounces → support-break continuation; late-morning/power-hour.
- **The_Big_Dog_Consolidation_Cheat_Sheet.pdf** — **[priority setup: Big Dog]** wedge/flag/pennant above prior-day high on high RVOL; break-of-pattern entry, move2move exit; mid-day.
- **Bella Fade.pdf** — fade an aggressive opening institutional order for mean reversion; first 15 min.
- **First Move Down.pdf** / **First Move Up.pdf** — first green/red candle at support/resistance in the opening auction; move2move.
- **First VWAP Pullback.pdf** — quick pullback to VWAP after a strong opening drive; momentum, measured move.
- **Gap_Give_and_Go_Cheat_Sheet.pdf** — gap-up drops then holds a level, mini-consolidation, continuation break; the MSTR deck below is a worked example.
- **Back-Through Open.pdf** — price crossing back through the opening price in the first 5 min; momentum.
- **Premarket High Break.pdf** — aggressive break of the premarket high at the open; needs an 8+ catalyst.
- **Opening Range Break (2).pdf** — defined opening-range break → trend; two-leg exit.
- **Off Sides Scalp.pdf** / **Off\$ides+Cheat+Sheet.pdf** — range trap: join the side that traps offside traders on the range break; measured-move target.
- **back\$ide_cheat_sheet.pdf** — Backside scalp: reversal off the low of day back toward VWAP after an extension.
- **the_fashionably_late_scalp_cheat_sheet.pdf** — enter *after* momentum is established (convergence-volume > divergence-volume); inactive YAML strategy stub in code.
- **the_rubberband_scalp_cheat_sheet.pdf** — controlled grind that accelerates then snaps back; RVOL 5+, >3 ATR from open.
- **the_second_chance_scalp_cheat_sheet.pdf** — break-and-retest ("old resistance = new support"); easier, higher-prob version of a range break (50-55% win, 1.9:1).
- **hitchhiker_scalp_cheat_sheet.pdf** — ride an institutional buy program via a 5-20 min consolidation range break (55-60% win, 1.9:1).
- **Spencer Scalp.pdf** — 20 min+ consolidation in upper ⅓ of range on sustained volume → break; scaled 1:1/2:1/3:1 measured-move exits.
- **The 3_30 Trade.pdf** — low-float afternoon-consolidation break into the 3:00-4:00 power hour (short squeeze).

## Jure examples (visual trade examples)
- **3_Cheat_Sheet_Trades_Examples_JureG.pdf** — Jure Gricnik's 16-page annotated chart examples for ~15 SMB trades (2nd Chance, Fashionably Late, RubberBand, HitchHiker, ABC, Gap-Give-and-Go, Backside, ORB, Big Dog, Volume Capitulation, HOD Breakout, …). The "what it looks like" companion to the rule sheets — training data for pattern recognition / live-example collection (§6).

## SMB playbook decks (worked trade reviews — the output template)
Full SMB playbook slide decks: Big Picture (SPY/QQQ/sector) → Intraday Fundamentals → Technical Analysis → Trade Strategy → Trade/Risk Management (with **grade + % of daily stop**) → Reading the Tape → Technology → Trade Review/Scorecard. This is the *deliverable format* Cobalt's research/journaling engine should generate per trade.

- **SMB PlayBook — 2026-08-17 — \$NU — NU DAY 2 + VWAP CONTINUATION.pdf** — Trevon Baucom's NU Day-2 + VWAP-continuation short; clean example tying a priority setup to full levels/entry/stop/targets.
- **Playbook MSTR Gap Give and Go 21.8.26.pptx** — Luka B's MSTR Gap-Give-and-Go; RISK MANAGEMENT slide shows Grade **B → 20% of a \$100 daily stop = \$20 risk**, plus a "Day 2 Continuation Finder / RVOL Screener" technology slide.
- **SMCI - Earning Day - Offside Scalp.pptx** — Omar Ghias' SMCI earnings-day offside scalp; grade **B → 15%**; tech stack slide (TradingView/ToS, Claude + VPS scanners, DAS, Vital Knowledge/Briefing).
- **QQQ High Expanson Fashionably Late Flush.pptx** — Jenni C's QQQ options flush; includes the SMB deck template rules, a **TILT / risk-psychology** slide, internals (TICKQ) confirmation, and an explicit Score Card — strong coaching-agent reference.

## ASET / DRC artifacts (grading, EV, sizing, journaling)
The heart of the missing §6 ASET grader / position sizer and the §5 coaching/journaling cadence — Cobalt has **no** grading/EV/sizing code today, so these define the target behaviour.

- **aset_daily_position_sizer.html** — Working self-contained ASET Daily Position Sizer web app (Catalyst→Set-Up→Trade framing; grade **A+ 80% / A 30% / B 15% / C 5% / D 0%** of the daily risk budget; long/short, per-share distance → shares; `localStorage`). The concrete spec for the grade→risk-% mapping and the sizer UI.
- **DRC Template-Dejan.docx** — Dejan's Daily Report Card template: goal, self-grade, risk management, PnL, **Risk Parameters A:5R / B:1R / C:0.5R**, per-ticker catalyst+setup+trade, learnings, selectivity, "tomorrow's 1% better" IF/THEN. The forced-report-card format the coach agent must fill with least friction.
- **dailyreportcardexample.png** — A filled "Daily Report Card" (Day 76, −\$101.18, 16 trades): tomorrow's watchlist w/ bias+levels+grade, time-block grades, mistake log, per-trade review with lesson/what-I-did-well/improve + chart. The rendered output Cobalt should auto-produce.
- **Opportunity Framing Model(1).xlsx** — "The market is an opportunity-generating machine" framing grid (Catalyst/SetUp/Trade → Frame/Result/Purpose/Plan → stop/entry/target/risk) with worked ticker rows. The reasoning scaffold behind grading/EV.
- **Daily_Stop_Model_Card.pdf** — "The Daily-Stop Model" one-pager: **daily stop = account ÷ 50** (per day, not per trade); grade→% of daily stop **A+ 80 / A 30 / B 15 / C 5** ("too risky to feel like a C = SAW trade, zero size"); stop hit once → next day demo, twice in a row → two days off. The ruled sizing spec for pre-beta slice 1 and Guardian rules 6–7.
- **SMB-DRC_Template.pdf** — Official SMB Daily Report Card template: date/grade/goal, reminder checkboxes, time-segment table (Temp, 9:30–11, 11–12, 12–2, 2–4 × Grade/PTD-only/Sizing/In-my-favor/Comments), learnings/changes, per-ticker writeups with charts. The render target for the slice-2 DRC prefill (trade-reporter's `drc_builder.py` reproduces it).
- **SMB_Inside_Access_Calendar.pdf** — SMB Inside Access weekly live-meetings schedule (Morning GamePlan 9:00, Trader Development 11:00, The PlayBook w/ Bella Wed 1:30, evening electives 4:15+, all ET). Input to the decide-at-skip-time replay policy and the Phase-0 calendar anchors (TRIAGE operating rhythm).
- **trade-reporter/** — Source of Dejan's "BigScalp Edge" local Flask app (`app.py`, reportlab `drc_builder.py`, template-first `playbook_builder.py`, drag-drop web UI). DRC → 1-page PDF; PlayBook → PPTX filled into the licensed SMB template (hidden-not-deleted slides, Lato Bold CAPS titles, fitted chart zones). **The rendering builders are the reuse target for pre-beta slice 2 (prefill-first inversion); the simple Flask form pattern is the slice-1 surface reference.**
- **assets/SMB_PlayBook_Template_2024.pptx** — **LOCAL-ONLY, NOT in version control** (licensed SMB material; `docs/90 - References/assets/` is gitignored). The official 17-slide SMB PlayBook template consumed by `trade-reporter/utils/playbook_builder.py`. Place a licensed copy manually on any fresh checkout.

## Mission-control / Obsidian-OS inspiration
UI and architecture references for the command-center front-end (§9 Obsidian-plugin command center) and the premarket-briefing model.

- **prebell today tab top of page look and feel.png** / **prebell today tab bottom of page.png** — Prebell "Today/Daily Prep": market-regime tiles (VIX, VIX3M/VIX, expected ranges, participation, confidence), event/risk map, ranked final watchlist with per-name chart + key zones + driver/why/confirms/invalidates. **Requirements §5 names prebell.laldinsoft.com as the model to copy** for the morning day-plan.
- **Prebell market tab top of page.png** / **Prebell market tab bottom page.png** — Prebell "Market": index levels (SPY/QQQ/SOXX) with weekly-vs-today structure, sector heatmap, "The Week" macro calendar. The market-context half of the premarket agent.
- **Prebell archive tab.png** — Prebell "Archive": dated PREP/MARKET history list. Model for durable, browsable daily-plan storage in the vault.
- **Obsidian OS 2.0 idea 1 page.png** — "Agentic OS" Command Center dashboard (Claude-burn meter, socials KPIs, action buttons, today schedule/tasks, morning headlines) — the visual target for the Obsidian command center.
- **Obsidian OS Idea page 2.png** — Excalidraw "Agentic OS" map: Claude Code as conductor routing to Memory/Productivity/Research/Content/Community/Agency/Sales/Finance/Ops branches over an automation layer + integrations. Mirrors Cobalt's Cortex→departments design.
- **Different obsidian agentic os idea.png** — "RUBRIC Agentic OS": radial skills dashboard (micro-apps, calendar, email triage, skills deck by model tier, routines). Another command-center pattern (skills + scheduled routines).
- **Claude Code x Obsidian OS 2.0 youtube video transcript.rtf** — Transcript: building an Obsidian "Claude OS" command center — skills/automations, memory layer, local voice (Haiku for the cheap router). Directly informs §9 voice stack + command center.
- **Claude Fable 5 Bossed 20 Cheap AI Agents youtube video transcript.rtf** — Transcript: multi-agent team design — which model gets which job, a checker/capture agent catching hallucinations for free. Informs the tiering (§10) and self-verification pattern.
- **anothergrokbotexample.rtf** — Transcript: Cursor "Grokbot" — persistent per-role bots, always-on browser/files/logins, scheduled routines. Reference for the DM-driven persistent-agent UX (Mattermost personas).
- **GrokBotexamplesJustIdeaofworkflown.rtf** — Transcript: concrete Grokbot workflows (email/calendar agents on a 7:30am schedule, one-click actions, scoring). Ideas for scheduled agent routines and approval buttons.
- **natebjonesargueskarpatrhywiki.eml** — Nate B Jones: Karpathy's write-time LLM-Obsidian wiki fails at scale/multi-agent/high-velocity data; his "OpenBrain" is query-time (raw facts in SQL) + a scheduled compilation agent that generates the wiki. **Directly relevant to INFRA-2 vault redesign** (Karpathy raw→wiki→output) and the Postgres-as-truth vs Markdown-as-view question. (Contains Dejan's own email address in the header.)

## ClaudeClaw kit (reference only, L15 — never executed)
Third-party ClaudeClaw material, filed here as inert reference under the L15 external-code law: never opened, read, or run as instructions — content only, not process.

- **claudeclaw-kit/CLAUDECLAW_ASSESSMENT_PROMPT.md** — third-party assessment prompt.
- **claudeclaw-kit/POWER_PACKS.md** — third-party power-pack content.
- **claudeclaw-kit/POWER_PACKS_GUIDE.md** — third-party power-pack guide.
- **claudeclaw-kit/REBUILD_PROMPT_V2.md** — third-party rebuild prompt.
- **claudeclaw-kit/ClaudeClaw_v2_Visual_Guide.pdf** — third-party visual guide.

## Misc
- **.DS_Store** — macOS folder metadata; noise, not content (safe to delete/gitignore).
- **08-documentation-audit.md**, **ASSESSMENT.md** — WERE stray copies of `docs/assessment/` files dropped into this folder; moved to `docs/_archive/references-misfiled-duplicates/` in the 2026-08-26 D6 restructure (nothing under `docs/` is deleted). The canonical, current versions live in `docs/20 - Assessment/`.

---

## 🔐 Credentials
- **All 9 Finviz screenshots** (`FinvizScannerAPI.png`, `finvizstockapi.png`, `finviznewsapi.png`, `finvizcalendarapi.png`, `finvizlatestfiningsapi.png`, `finvizinsiderapi.png`, `finvizmanagersapi.png`, `finvizfundsapi.png`, `finvizoptionsapi.png`) display a Finviz Elite API token in cleartext in the "Add Authentication" field (same token across all nine; the example-URL `&auth=` portions are whited-out). **Historical note: that token was rotated dead on 2026-08-22 (Finviz "Regenerate Token"); the VaultManager entry (`finviz.com::api_token`) was updated to the new token; the images are safe in version control. Redaction of the token box is optional.** The live token lives only in VaultManager, never in a committed image.
- **natebjonesargueskarpatrhywiki.eml** contains Dejan's own Gmail address in the From/To headers (self-sent). Low sensitivity (already the repo author email), but note it if this folder is ever shared externally.
- No other API keys, passwords, or tokens were found in the extracted text of the PDFs, PPTX, XLSX, DOCX, RTF transcripts, or the ASET HTML.
