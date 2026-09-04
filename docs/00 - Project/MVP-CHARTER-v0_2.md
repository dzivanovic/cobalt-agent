# COBALT MVP CHARTER — v0.2 (RATIFIED)

**Status:** RATIFIED section by section at Product Definition sitting 5,
2026-09-04 (sitting 5 of 5, closed on agenda). v0.1 draft → v0.2 ratified with
amendments folded. Amendments after this date = ruling + dated line here.
**Sources:** PROJECT-LEDGER.md (through sitting-4 appendix), incident thread
09-03/04 (L28/L29, Rulings 6–7), LIVE-FEED-SPIKE.md, TAXONOMY-DRAFT-v0_7.md,
TRADE-DEFS batches 1–2, TRADE-RADAR-CARD-MOCK-v0_1, docs/references/INDEX.md.
**Lives at:** docs/00 - Project/MVP-CHARTER.md once ratified (D6 tree).
**What this document is:** the experience spec the sprint ladder is re-derived
from. Not a design doc, not a backlog. If a feature has no moment in §2 and no
acceptance line in §3, it is not in the MVP.

---

## §1 Needle doctrine and product statement — RATIFIED 09-04

- **Needle = Dejan-as-trader, never Cobalt-as-artifact.** Every item below is
  judged by whether it moves a trader metric (§7). Building is not progress on a
  day trading was avoided.
- **Product = a profitable trader; Cobalt = leverage.** MVP = the usable Obsidian
  Cobalt operating system for one trading day, end to end, with the Trade Radar
  card as its face.
- **Design standard:** "what do I need to see to have conviction to pull the
  trigger in real time" beats "what does the system need to calculate." Tesla
  road-trip model: automated, human-centric, minimal surface, full complexity
  under the hood, recalculates on deviation.
- **Anatomy vs rules:** the taxonomy and radar carry market anatomy only; Dejan's
  personal trading rules live in the printed card, the rules gate and (post-MVP)
  Guardian. Radar detects and cards fire in every session, 24×5.
- **Frontier law:** Cobalt owns every field it can fill; Dejan owns the residue;
  the frontier moves by config flag, never by rebuild. Game Plan is permanently
  his.
- **Human rules the grade:** Cobalt proposes from computable dots, judgment dots
  hollow; his taps are the calibration set.
- **Cobalt never touches a trading platform.** Read-only awareness only; the
  `.htk` is his hand; the match check refuses mismatch.
- **MVP timebox:** usable in ~2 months from ratification; further MVP additions
  fight for a slot at sprint boundaries only.

## §2 The day (moments the MVP must serve) — RATIFIED 09-04

Track A = Dejan's narrated day. Track B = Cobalt's 24×5 background, surfacing
only where it hands Track A something. Every §3 feature names its moment here.

| # | Moment (ET) | What lands / what he does |
|---|---|---|
| M1 | 05:15 | Daily note exists (create-if-absent), prefilled: rules block, market table, calendar, day-mode line, adherence checkboxes. Stamped "as of 05:15". |
| M2 | 05:30–06:00 | Vital Dawn digest lands, or loud "no episode today" by config cutoff. *(SHOULD)* |
| M3 | 07:15 / 07:45 / 08:15 / 08:45 | Market-context checkpoints: Finviz numbers + single-house narrative, delta vs previous. Full view by 09:00. |
| M4 | 09:00 | Day-mode checkpoint: Cobalt proposes quarter/half/full with reason; he approves or overrules with reason; risk set everywhere except `.htk`; match check. |
| M5 | 04:00–20:00 continuous | Radar pool (≤50 rotating) re-scores; focus list (~4) with conviction WHY; WATCH cards land at precondition with all Cobalt fields filled. |
| M6 | Any session | He grades (accept / up / down) and ARMs at a key; card locks. |
| M7 | Any session | Trigger fires → strike alert (key · shares · stop · hotkey) on phone; trigger on an unarmed card = MISSED record. |
| M8 | In trade | Fill recompute; management view = trail selection + reason; trade note auto-created. |
| M9 | 15:40 / evening | DRC prefill: cards written / trades taken, unfilled cards reconciled (taken/passed/discarded), adherence, excitement audit; DRC → next day-mode proposal. |
| M10 | 20:30 nightly | Archiver run + top-N mover auto-archive + benchmark query + miss line; heartbeat red/green. |
| M11 | Sunday 18:00 weekly review (drill sessions ad hoc) | Playbook PPTX renderer output. |
| M12 | Any time | He talks to one chief of staff (DM); outcomes and HITL cards only. |

## §3 MVP MUST features — experience-phrased acceptance criteria — RATIFIED 09-04 (F1–F23, with F8/F11/F14/F18 amendments)

Format: **F-n name** (moment) — *Acceptance:* what Dejan experiences; the test.
All counts of n count FILLED cards only (cards ≠ trades). Sample-size law:
n<30 = insufficient data.

**F1 Session clock** (all) — *Acceptance:* every card, alert and note carries
the session (premarket 04–09:30 / RTH / aftermarket 16–20 / market_reset 20–21
hard-blocked / overnight); no feature keys off wall-clock. Test: a card fired at
18:30 and one at 21:30 show the right session; the 21:30 one is blocked.

**F2 Radar pool 24×5** (M5) — *Acceptance:* the pool holds ≤50 names, churns
continuously from 4 TV static + 4 Finviz dynamic lists, and never freezes
premarket. Test: a name entering on RVOL at 14:10 appears in the pool within one
scan cycle; pool count never exceeds config cap.

**F3 Focus list with conviction WHY** (M5) — *Acceptance:* ~4 names ranked by
conviction × proximity, each with one WHY line; when he picks against the rank,
pick-vs-rank is logged. Test: DRC shows his pick and Cobalt's rank for every
card.

**F4 Prefill, all day, ownership flags** (M1, M3) — *Acceptance:* the note
exists at 05:15 with Cobalt blocks stamped "as of HH:MM"; refreshes on config
cadence and on manual trigger; his text is never touched (L28 units, markers,
diff). VIX/BTC show loud "n/a (manual)" until owned. Test: he writes in the game
plan at 06:00, prefill re-runs at 08:45, his text is byte-identical; diff row in
`vault_writes`.

**F5 Market-context checkpoints, single-house narrative** (M3) — *Acceptance:*
four checkpoints land on schedule with Finviz numbers (deterministic, no LLM
figure) and a narrative delta vs the previous checkpoint; a missed checkpoint is
loud. Test: 08:15 block cites what changed since 07:45; a source outage shows as
degraded, never blank.

**F6 Two-stage day mode + match check** (M4) — *Acceptance:* before 09:00 the
lowest enabled sheet applies by system rule (half today, quarter once it
exists); at 09:00 Cobalt proposes with reason from prior DRC + running goal +
context; his approve/overrule with reason persists; the loaded `.htk` is checked
against the mode and mismatch refuses cards. Test: he loads the full sheet on a
half day → card refused with the reason.

**F7 Card state machine** (M5–M8) — *Acceptance:* WATCH → ARMED → TRIGGERED →
FILLED → CLOSED / PASSED / EXPIRED / MISSED, every transition persisted with
evidence; trigger while unarmed = MISSED, counted not hidden. Test: DRC counts
match Postgres rows; no card exists without a state.

**F8 Card lands at precondition (19a)** (M5) — *Acceptance:* when a
`trade_def`'s preconditions form on polled Finviz bars, a WATCH card lands with
setup → trade, trigger, structural stop, proposed key, dots with WHY. The card is
the contract before the trigger. Scan cadence = tunables row `radar.scan_interval` (start 60 s for 50 names).
Test: a Rubberband precondition on a pool name produces a card within one scan
interval; every card field is badge-owned.

**F9 Trigger detection + strike alert (19b, focus scale)** (M7) — *Acceptance:*
≤5 ARMED names polled on Finviz-lite; price-cross of the card's trigger (with
its confirmation policy) fires a strike alert showing key · shares · stop ·
hotkey and nothing else. **Delivery:** the Radar panel (the ASET Flask sheet
grown into it, same plumbing) pushes TRIGGERED over an SSE stream to a pinned
browser tab on the trading PC via Tailscale, with browser notification + sound;
Mattermost DM to phone = fallback only (too slow for the strike path); Python
toast listener on the PC = post-week option. Criterion: alert on the panel
≤5 s after bar close, premarket + RTH, re-measured at 2–3 s cadence as the first
build step; if Finviz throttles at 3 s, criterion re-rules to what 10 s cadence
delivers (~8 s). **One-week cap;** at week end whatever is proven ships, the
remainder joins the post-MVP lane. Trade_def trigger types beyond price-cross =
setups engine, post-MVP.

**F10 Dots / ladder / accept-up-down** (M6) — *Acceptance:* computable dots
scored 1–10 with WHY, judgment dots hollow; keys A+/A/B/C/pass with fixed
dollars per sheet (full B $60 / A $135, half B $30 / A $70; A+ and C shown
greyed with would-be dollars); tap records grade and sizes at nearest enabled
key, loud. Test: an A+ tap on a half day records A+ and sizes at A $70 with the
notice.

**F11 Fill recompute + fill/exit capture** (M8) — *Acceptance:* on TRIGGERED
the card shows **FILLED @ [price]** (prefilled with last polled price, editable;
shares editable) and **PASS**; tap → FILLED, shares recomputed, trade note
created; >20% distance drift warns "re-read stop"; no tap by expiry → EXPIRED.
Every scale-out tap (½ · ⅓ · flat · typed) records a leg {shares, price, time}:
mid-trade legs take the prefilled last-poll price flagged `estimated` (no typing
under fire); the final exit price is his, flagged `confirmed`. Running shares
0 → CLOSED, realized R provisional while any leg is estimated; DRC lists
estimated legs for one-pass correction from the DAS log (evening DAS
execution-log reconcile = post-MVP). Fallback capture: a DM/voice line to the
CoS ("TSLA filled 372.82 10" / "TSLA out 374.50 all") writes the same rows.
Test: fill 27% past plan → warning, FILLED row, DRC counts it as a trade; a
½-off tap during the trade produces an estimated leg without a keystroke.

**F12 Missed records via nightly archiver replay** (M10) — *Acceptance:* every
trigger that fired on an unarmed or absent card is a MISSED row with
`excluded_by`. Test: nightly report lists misses with the gate/variable that
excluded them.

**F13 Auto-archive + benchmark query + miss line** (M10) — *Acceptance:* top-N
daily movers archived nightly regardless of watchlist; benchmark query
(unfiltered movers ≥ config move) diffed against the in-play set; one miss line
in the DRC. Test: a Tesla-class mover absent from the pool appears in the miss
line with `excluded_by`.

**F14 DRC prefill / reconcile / DRC→mode** (M9) — *Acceptance:* the DRC is a
separate note `DRC-YYYY-MM-DD.md` in SMB format (goal, self-grade, time-segment
table, risk parameters, per-ticker writeups linking trade notes, learnings,
tomorrow's 1%), prefilled at 15:40 with cards written / trades taken, every
unfilled card asked taken/passed/discarded, adherence checkboxes, excitement
audit, estimated legs to confirm, time blocks, PnL; he fills grade, learnings,
1%. The daily note carries a three-line stub (cards/trades, adherence %, next
day-mode proposal) + link — a pointer, not a second DRC. Next morning's day-mode
proposal cites this DRC. Pre-slice: one review (Dejan + Claude) merges his docx
template and the SMB template into the live Templater template. PDF render via
trade-reporter `drc_builder` = SHOULD. Test: 09:00 proposal quotes the prior
DRC; the DRC note exists at 15:41 with every Cobalt field filled.

**F15 Prediction records** (all scored objects) — *Acceptance:* every score +
WHY is joined to its outcome; no derived value without stored inputs
(explainability law). Test: any card's grade replays from stored inputs.

**F16 Tunables consumers** — *Acceptance:* every threshold the MVP evaluates is
a `tunables.yaml` row with a consumer; loader fails loud on unknown keys; §13
replay backlog is a query on status. Test: `validate` passes; no inline literal
in a predicate.

**F17 Task integrity, minimal** (L18) — *Acceptance:* every scheduled job is a
persisted row with state, timeout, heartbeat; failed = loud; kill phrase stops
all. Test: a hung poller is surfaced as a zombie within one heartbeat interval.

**F18 Heartbeat** (M10) — *Acceptance:* services alive · archiver freshness ·
every ops plist loaded + last exit code · Obsidian running; red/green to daily
note + DM; red also out-of-band = email via Layer-B Google OAuth at MVP, push
service post-MVP (alert path ≠ monitored path). Test: unload a plist → red
within one interval, on the out-of-band channel.

**F19 Exfiltration guard** — *Acceptance:* outbound secret-regex redactor on
every channel. Test: a token in a DM payload is redacted before send.

**F20 Chief of staff, thin** (M12, L14/L16) — *Acceptance:* one resident
session; he talks only to it; HITL cards in one place with full detail and
Approve/Deny; agents exist as registry entries. Test: a config-drafted agent
appears only after an approved HITL card.

**F21 Genesis import + continuity pack** — *Acceptance:* at bring-up Cobalt's
first memories are the Ledger + vault history through its own memory pipeline;
per-seat continuity briefs stored in Think (outside repo). Test: Cobalt answers
"why is the stop buffer 0.02" from the imported record.

**F22 Trade-note auto-creation from cards** (M8, item 46) — *Acceptance:* every
FILLED card produces a trade note (frontmatter site, L28) that lights the
dataview table. Test: a fill at 10:12 has a trade note by 10:13.

**F23 Playbook PPTX renderer** (M11, item 47) — *Acceptance:* weekly review
opens a deck rendered from the playbook data. Test: one deck per setup family
with the latest cards.

## §4 SHOULD / COULD / WON'T (MVP) — RATIFIED 09-04

- **SHOULD:** Vital Dawn digest (M2) · three-house council (purchase gate) ·
  proposed game plan (parallel field) · management view beyond trail + reason ·
  ranking two-up / detail column · miss-pattern aggregation (only if cheap) ·
  DRC one-page PDF render (`drc_builder`).
- **COULD:** replay engine + shadow configs.
- **WON'T (MVP):** X lane · Oura · IF/Then branches (placeholder slot only) ·
  trail_fit suggestion · Guardian · full orchestrator · voice · Meeting Scribe ·
  green-light widget · day-replay dashboard.

## §5 Trade Radar card — mock v0.1 ratification — RATIFIED 09-04

**Ratified as the card's design of record**, four live states + terminal, one
component, owner badges (COBALT / YOU / N/A MANUAL), three-number strike alert,
hollow judgment dots, opaque rank score, ARMED/IN-TRADE pin above WATCH.

**Collisions with rulings — Charter wins, mock amends at v0.2:**
1. Keys = fixed dollars per sheet (08-28 FINAL), not `day budget × grade %`.
   The % map is the origin of the ladder, never the runtime. Far-future
   (1%-dynamic era): `day budget × grade %` becomes the runtime — not now.
2. Day modes = quarter / half / full = 25 / 50 / 100% of one config max ($430);
   pre-09:00 = lowest *enabled* sheet by system rule, not a hard ¼ floor. No
   quarter sheet exists today (his ruling 09-04: a quarter sheet becomes
   realistic only at a daily stop of ~$1,000+); half is the premarket floor
   until then. Mock's "$200 day" is sample data.
3. Ranking: mock's single ladder with #1 + #2 open replaces the ruled two-up —
   accepted as the better answer to "one-card width beside DAS" (decided-with-
   veto).
4. Hotkey name `{DAYMODE}-{KEY}-{SIDE}` must match the real `.htk` labels — his
   check.

**Open questions answered by prior rulings** (mock open-questions.md →):
#5 judgment dots = tape (human by law) + conviction · #7 attempts: PASSED is not
an attempt, MISSED is not an attempt, re-entry rule #3 = stand-down · #9 EXPIRED
exists; window per trade_def via preferred_windows_ref · #10 host at MVP = the ASET
Flask sheet grown into the Radar panel (reuse, no new app) on Tailscale, cards
persisted to daily note;
Obsidian plugin = post-MVP upgrade on the same data contract · #13 shared state
= the Postgres card row · #14 live data = Finviz-lite poller (F9) · #15
enabled_grades = per day-mode sheet · #16 single fill at MVP, partials post-MVP.
**Still open:** #1 per-dot weights (post-MVP, config) · #2 scale-out presets ·
#6 stop-override authority · #8 health thresholds · #11 detail-column order.

**Validation:** ASET sizing card used beside DAS every morning through
slice 1/2 (rocky: DB writes failed some mornings, fixed along the way) = evidence
the card form works under fire. The four-state Radar layout has had no live
morning; **acceptance = 2–3 live mornings beside DAS on a static render** before
the card slice is called done.

## §6 Capacity math — RATIFIED 09-04

| Quantity | MVP value | Source / status |
|---|---|---|
| In-play pool | ≤50 names, rotating | ruled 09-01 |
| Focus list | ~4 | ruled 09-01 |
| Armed names (19b) | ≤5 | spike scope |
| Cards written / day | observed up to 15 for 1 trade (09-02) | ASET history |
| Trades / day goal | config band (`trade_count_goal.min/max`, FILLED only), editable per period by his goal timeline (daily/weekly/monthly windows) | value: Rules Engine session |
| Daily risk budget | $430 config max; modes 25/50/100% | ruled 09-03 |
| Poll load, 19b | 5 names × 3 s = 100 GET/min; 10 s fallback = 30/min | spike: 0 errors at 30/min |
| Archiver corpus | ~210 tickers tier_a i1–i30 nightly; ~1.4M rows per ~2-week window | gap audit 09-03 |
| Deterministic pipeline tokens | zero Claude tokens | L25 |
| Paid-token moments | 4 checkpoints + DRC + conversation | 09-01 assessment |
| Claude spend | Max plan, 20x decision deferred pending one normal week | L27 |

## §7 Trader metrics (what the MVP is graded on)

Priority order (drives every MoSCoW): **rule adherence > exit efficiency >
selection quality > expectancy > prep > bandwidth.**

- Adherence: % of FILLED trades inside written rules (target ≥90% over 20 days).
- Exit efficiency: realized R vs plan R per trade (n≥30 before it is read).
- Selection quality: miss line count and pattern; pick-vs-rank hit rate.
- Expectancy: per setup, n≥30 FILLED, insufficient data below.
- Prep: checkpoints landed on schedule; note complete by 09:00.
- Bandwidth: cards graded in seconds (accept/up/down), no manual sizing.

Hard dates: consistently green by **Dec 31 2026** (any size); first grading
**Dec 1**; first real withdrawal by **Apr 30 2027** (proof, not payroll).
Failure sentence to sidestep: never let building feel like progress on days
trading was avoided; never let a green rule-break become a trophy.

## §8 Build / trade firewall — RATIFIED 09-04

1. **Non-negotiable 16:** prod never broken by development; feature-branch dev;
   git-tagged deploys with one-command rollback; deploys outside market hours
   only.
2. **L28 vault-write law:** create-if-absent · section + unit ownership ·
   version every write · diff in every report · live vault + DB never a test
   target · restart-on-deploy · off until proven.
3. **L29 model rule:** any session touching a vault/DB write path, migration,
   delete, recovery or forensics runs on Opus 5; Sonnet/Haiku only on non-write
   mechanical work, never auto mode on a write path.
4. **Environments:** two DBs — cobalt_brain live, cobalt_dev for dev-vault runs
   and tests; COBALT_ENV unset → fail loud; every plist carries it.
5. **Permissions:** auto mode per session, never bypassPermissions on the host;
   `git push` stays human; Code installs and proves every scheduled job.
6. **Mac Studio boot contract:** never sleeps · auto-login · lock screen allowed
   · Obsidian as a supervised service.
7. **Trading-day protection — OPTIONAL practice until MVP (his ruling 09-04):**
   building inside the trading window is accepted for now because reaching a
   meaningful, buildable MVP sooner is what starts the usage data he needs to
   mold the system; once Cobalt assists in building rather than him doing
   manual tasks, this hardens to: no deploys or restarts 04:00–16:00 ET on
   market days, no Code session inside his live window, fixes wait for the
   DRC. Deploys still go through the L28/#1 gates whenever they happen.
8. **Loop tripwire:** if he ferries more than a prompt down and a recap up, the
   day compresses.

## §9 Data and compute budget — RATIFIED 09-04

- **New spend at MVP: $0.** Feeds = Finviz Elite (owned), TradingView Premium
  (owned), archiver corpus (owned).
- Post-MVP gates: TV alert→webhook (free, gated on alert-slot cap +
  extended-hours test) → Massive Advanced ($160 annual / $200 monthly, one-month
  paid spike at pool-scale readiness, annual only on evidence, non-pro
  attestation) → Massive Developer ($64, 15-min delayed, 10y minute history) as
  corpus insurance.
- Claude: Max plan, L27 hard ceiling, no top-ups ever. Grok + Codex at minimum
  tiers, purchase gate pending his full-picture review.
- Local first (L23): every lane local can serve runs local; cloud fallback loud.

## §10 Expansion Ladder — rung criteria — RATIFIED 09-04 (all config; n<30 = insufficient data; demotion symmetric, tripwire = one rung back)

- **R1 push size:** n≥30 FILLED · adherence ≥90% over 20 days · no circuit
  breaker in 20 days · expectancy >0 at n≥30 · trade-count goal met ≥80% of
  days. Two consecutive stop-outs = step back.
- **R2 expand windows** (afternoon, then premarket): R1 held 20 days at new size
  · one month green 4/5 days · written window plan; premarket adds n≥30
  WATCH-only shadow cards before the first live one; adherence <90% over 10 days
  closes the window.
- **R3 swing:** 6-month review passed · intraday expectancy ≥ threshold at n≥100
  · swing spec · n≥30 replay drills · size from the step-up tripwire.
- **R4 options:** R3 live one quarter at n≥30 · per-setup options expression
  with own stop + sizing · SMB Options program complete.

## §11 Post-MVP lane (ruled MoSCoW, by trader-metric impact) — RATIFIED 09-04

- **MUST, in order:** Guardian advisory → Meeting Scribe. (19b pool-scale and
  corpus insurance re-ranked to the end — see purchase gate below.)
- **SHOULD, in order:** DAS execution-log reconcile (makes realized R
  trustworthy) · TV alert→webhook (free; first pool-scale step) · trail_fit
  suggestion · miss-pattern aggregation · IF/Then branches with the setups
  engine · Drill Candidate Detector · three-house council · 19b trade_def
  trigger types · per-dot weights.
- **COULD:** replay + shadow configs · Oura · Grok X lane · 1%-dynamic mode ·
  voice CoS.
- **WON'T:** day-replay dashboard · green-light widget.
- **Purchase gate — last (his ruling 09-04):** Massive Advanced (19b pool
  scale) and Massive Developer (corpus insurance) move to the END of the lane.
  Both are a large spend; neither is entered while an interim process (Finviz-
  lite + TV webhook + archiver corpus) covers the need. Entry condition: the
  system is bringing real, measured value to his trading and the interim
  process is the proven bottleneck. Ruling-6 mechanics unchanged when entered
  (one-month paid spike first, annual only on evidence, non-pro attestation).
- Consequence held: Rules Engine design session precedes orchestrator design.

## §12 MVP acceptance and what follows — RATIFIED 09-04

- **MVP accepted when:** every §3 MUST passes its test on the live vault and
  live DB, over five consecutive trading days, with the heartbeat green and the
  card used in at least three live mornings.
- **Then:** sprint ladder re-derived from this Charter (not from the 08-22
  ladder); each sprint only adds; sprint acceptance = full smoke of all
  delivered functionality.
- **Timebox:** ~2 months usable; extension only by explicit ruling; additions
  fight for a slot at sprint boundaries.

## §13 Open items carried into the ladder — CONFIRMED 09-04

- Trading PC joins Tailscale (his, between sittings).
- Trade-count goal value (his). Health thresholds (mock #8). Stop-override
  authority (mock #6). `.htk` hotkey label check (mock #3).
- Vault backup (restic → B2 + SSD) — gated, before Tahoe; still no backup today.
- `sudo crontab -l` (his). Env-law / migration Code report (issued for after
  16:00 today) — ruling cited here, proof pending.
- Taxonomy v0.8 consolidation at next bump. Push of taxonomy/trade-defs-v0_3.
