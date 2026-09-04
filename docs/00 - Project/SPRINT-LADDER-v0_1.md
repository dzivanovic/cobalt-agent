# COBALT SPRINT LADDER — v0.1 (order RULED 09-04: radar before exits)

**Derived from:** MVP-CHARTER v0.2 (ratified 09-04) §3 F1–F23, §5, §7, §8,
§12, §13; PROJECT-LEDGER through the incident-thread close (rulings 6–9
folded, env-law/migration report DONE). Not derived from the 08-22 ladder.
**Laws applied:** each sprint only adds · sprint acceptance = full smoke of
all delivered functionality on dev vault + cobalt_dev, then one live morning
· L28 writers first · L29 model rule · F9 one-week cap · 19a before 19b ·
§8.7 building inside the window accepted until MVP.
**Sequencing rule (ruled 09-04):** radar (selection + awareness) precedes
exits/DRC automation. Reasoning on record: the radar has no manual
substitute (two names by eye vs 50 in the pool); the exit-coaching loop
already runs by hand in the DRC chat; the expectancy corpus must sample the
playbook's population (radar cards), not what Dejan spotted by eye; sim /
shadow-card training (R2 rung) needs the radar. Hand-logged legs cover the
gap until F11 lands.
**Timebox:** 9 build weeks 09-08 → 11-06, acceptance run 11-09 → 11-13.
Charter says ~2 months; this is 2 months + 1 week — flagged, not hidden.

**Starting state (from the ledger, proven):** cobalt_brain live, cobalt_dev
dev/test, COBALT_ENV law in code, vaultwrite one path (L28) with
vault_writes/overrides, ASET sheet iter 4 (fixed-dollar keys, mode toggle,
fill recompute, FILLED status), prefill-daily 05:15 + prefill-drc 15:40 +
archiver 20:30 plists loaded on the resolver, bars migrated (4.56M rows),
com.cobalt.obsidian supervised, boot contract met, tunables.yaml 30 rows +
validate, taxonomy v0.7 + trade_defs batches 1–2 in DB, heartbeat probes
built (host not yet), 92 real cards in cobalt_brain.

---

## Ladder at a glance

| Sprint | Weeks | Adds (Charter F-ids) | §7 metric served |
|---|---|---|---|
| S1 Foundation + firewall | 09-08 → 09-18 (2) | F1 · F7 (manual cards) · F6 · F18 · F17 · F19 · F16 sweep · bars.ts ADR | adherence, prep (nothing silent again) |
| S2 Radar 19a | 09-21 → 10-02 (2) | F2 · F8 · F10 · F3 · Radar panel (§5) · F12 · F13 | selection quality, awareness; expectancy corpus starts on the right population |
| S3 Exits + DRC on radar cards | 10-05 → 10-16 (2) | F11 · F22 · F14 · F15 | exit efficiency, adherence measurement, expectancy |
| S4 19b strike alert — CAPPED | 10-19 → 10-23 (1) | F9 | bandwidth (+ adherence under fire) |
| S5 Prep + platform + playbook | 10-26 → 11-06 (2) | F4 · F5 · F20 · F21 · F23 · F16 close | prep, bandwidth |
| Acceptance | 11-09 → 11-13 | §12: every MUST on live vault + DB, 5 days green, ≥3 live mornings | — |

**Expectation set with the ruling:** the radar raises candidates, not the
trade count — rule 10 and the trade-count band still cap what is taken.
Expect the miss line and cost-of-discipline rows (`excluded_by: rule_10 |
trade_count_band | window`, with counterfactual R from archived bars) to
grow first; that tally is the Friday-review input for loosening rule 10.
Reasoning over that corpus (Guardian advisory, replay + shadow configs) is
post-MVP lane; the MVP builds the corpus only.

---

## S1 — Foundation + firewall (09-08 → 09-18) — UNCHANGED

**Precondition folds:** env-law report DONE (rulings 6–9) — S1 starts from
cobalt_brain live. Open items inherited into S1: TESTARCH row delete;
`bars.ts` ET-under-+00 (Data-Model ADR rules it before any join — the 19a/19b
detectors join bars, so it lands here). Tailscale on the trading PC = his;
S1-P1 line 0 reports peer status, nothing more.

| Feature | Charter acceptance (test) | What S1 delivers |
|---|---|---|
| **F1 Session clock** | Card at 18:30 and 21:30 show the right session; the 21:30 one is blocked. | `cobalt.session`: premarket 04:00–09:30 / rth / aftermarket 16:00–20:00 / market_reset 20:00–21:00 hard-block / overnight; NYSE calendar (holidays, early closes) as config; boundaries = tunables rows; `session` column on cards, alerts, vault_writes; market_reset block enforced in the write path. |
| **F7 Card state machine** (manual cards) | DRC counts match Postgres rows; no card exists without a state. | `card_state` enum + `card_transitions` table (from, to, at, evidence JSON, actor cobalt/you); existing ASET rows mapped (card = WATCH, FILLED status = FILLED); sheet gains ARM / DISARM / TRIGGERED / FILLED / PASS / EXPIRE controls; trigger-while-unarmed = MISSED row (manual entry at S1, detector at S2/S4). |
| **F6 Two-stage day mode + match check** | He loads the full sheet on a half day → card refused with the reason. | Pre-09:00 = lowest *enabled* sheet by system rule (half today); 09:00 proposal row (mode, reason from prior DRC stub + goal band + calendar; "no prior DRC" = loud) with his approve/overrule + reason persisted; `.htk` loaded-sheet check refuses cards on mismatch. Trade-count goal band = tunables rows, value pending Rules Engine session. |
| **F18 Heartbeat** | Unload a plist → red within one interval, on the out-of-band channel. | Heartbeat host job: services alive · archiver freshness (last run + row delta) · every ops plist loaded + last exit code · Obsidian running; red/green block in daily note (L28 unit) + Mattermost DM; red also by email via Layer-B Google OAuth (alert path ≠ monitored path). |
| **F17 Task integrity, minimal** | A hung poller is surfaced as a zombie within one heartbeat interval. | `jobs` table: every launchd job = persisted row with state (pending/running/done/failed), timeout, heartbeat stamp; watchdog marks zombies; kill phrase (config) stops all; failed = loud via F18. |
| **F19 Exfiltration guard** | A token in a DM payload is redacted before send. | Outbound secret-regex redactor as one function on every channel (Mattermost, email, log lines); patterns = config; tested against the rotated-secret shapes from 08-23. |
| **F16 sweep** | `validate` passes; no inline literal in a predicate. | Every threshold introduced this sprint = tunables row with a consumer; loader fails loud on unknown keys (already). Sweep repeats every sprint. |
| **bars.ts ADR-0007** (decided-with-veto) | — | Reinterpret stored ET-as-UTC values to true UTC (`America/New_York`), dump = rollback, row-count + md5 proof, archiver writes UTC from now; run outside 20:00–21:30. |

**S1 smoke:** prefill-daily, prefill-drc, archiver, obsidian, mainframe,
heartbeat all as job rows, green; one manual card walked WATCH → ARMED →
TRIGGERED → FILLED → CLOSED with every transition in `card_transitions`;
a card attempted at 20:30 refused; a full-sheet card on a half day refused;
plist unload → red email within one interval. Then one live morning on the
ASET sheet with the new controls.

**Code prompts owed (all Opus 5 — every one touches a DB or vault write path):**
- S1-P1 · fresh · Tailscale status line 0 · TESTARCH delete · ADR-0007 bars.ts · F1 session clock + column stamps + market_reset block · F16 sweep. **(issued 09-04 · DELIVERED 09-04, branch `sprint-1/foundation`, unpushed)**
- S1-P2 · fresh · F7 card_state + transitions + sheet controls · F6 two-stage mode + proposal row + `.htk` match refusal.
- S1-P3 · fresh · F19 redactor · F17 jobs table + watchdog + kill phrase · F18 heartbeat host (note unit + DM + email) · S1 smoke script + report.

### S1-P1 outcome (2026-09-04) — what landed, what it changed

- **Tailscale (read-only, line 0):** NO Windows peer on the tailnet.
  Three devices: `cobalt` 100.70.206.126 (this Mac), `dejans-s25`
  100.66.219.53 (android, offline 1d), `fedora` 100.104.48.21 (linux,
  offline 10h). The trading PC has not joined — still his, and it gates
  the S2/S4 strike-alert path (Charter: pinned tab over Tailscale).
- **TESTARCH deleted** from `cobalt_brain.bars` under the RULING 8
  discipline: 4,755,478 → 4,755,477, `ROW_COUNT` 1, guarded transaction.
  Closes ADR-0006's first follow-up. No other test residue found.
- **ADR-0007 ruled and executed.** `bars.ts` reinterpreted ET-under-UTC
  → true UTC across 4,755,477 rows in one 42 s transaction, DST-aware,
  content md5 identical, `ts` md5 changed, PK re-added clean. Dump =
  rollback (316 MB, sha256 in the ADR). The collector now emits
  tz-aware UTC and `Bar.ts` is `AwareDatetime`; proven on the real
  production path (21,718 rows written, table grew 261 — everything
  else upserted onto reinterpreted keys). **The 19a/19b bars join is
  unblocked.**
- **F1 delivered** as `src/cobalt/session/` — resolver, NYSE calendar as
  config, `market_reset` hard block with a `session_blocks` counter,
  `session` column on `aset_sizings` + `vault_writes` (backfilled on
  both databases, now NOT NULL), `cobalt session now/backfill/blocks`.
  60 F1 tests, 362 green overall.
- **F16 sweep clean.** Eight `session.*` boundary rows plus
  `session.blocks.heartbeat_window` (42 tunables total); `cobalt
  validate` is now a first-class command and covers the calendar and the
  boundaries as well as the taxonomy.

**Carried out of S1-P1 (not blocking):**
- `configs/cobalt/calendar/nyse-2026.yaml` holiday/early-close dates are
  **derived, not fetched** — Dejan to confirm. Config-only correction.
- No `nyse-2025.yaml`, so `session()` over the 2025 third of the bars
  corpus raises `CalendarError` by design. Add the file when a 2025 join
  is actually needed.
- `bars` has no `session` column (derivable from `ts`); revisit if S2
  makes the derived cost real.

**Rulings/inputs owed before S2:** health thresholds (mock #8) for the panel's
IN-TRADE health line — before S2-P3. Detail-column order (mock #11) — S2-P3.
Trade-count goal band value (his; band ships as placeholder in S1).
Taxonomy v0.8 consolidation (§13.1 wording + stop.buffer re-rule) — natural
bump point is S2-P2, the precondition evaluator.

---

## S2 — Radar 19a (09-21 → 10-02)

| Feature | Charter acceptance (test) | What S2 delivers |
|---|---|---|
| **F2 Radar pool 24×5** | A name entering on RVOL at 14:10 appears within one scan cycle; pool never exceeds config cap. | Pool job: 4 TV static lists + 4 Finviz dynamic screens → ≤50 rotating names, churn every `radar.scan_interval` (60 s start), premarket included, membership history persisted (`excluded_by` on drop). |
| **F8 Card at precondition (19a)** | A Rubberband precondition on a pool name produces a card within one scan interval; every field badge-owned. | Precondition evaluator over polled Finviz bars at `working_timeframe` (2m) for the six radar trades (Rubberband first, then Back$ide, Fashionably Late, Hitchhiker, Second Chance, Big Dog); WATCH card lands with setup → trade, trigger, structural stop (buffer 0.02), proposed key, dots + WHY; expiry per `preferred_windows_ref`; account mode (live / sim) tagged on every card. |
| **F10 Dots / ladder / accept-up-down** (pulled forward: F8 lands scored cards) | An A+ tap on a half day records A+ and sizes at A $70 with the notice. | Computable dots scored 1–10 with WHY from the `trade_def`'s scored variables (Finviz screener fields: RVOL, spread, float, catalyst grade, ATR…); judgment dots (tape, conviction) hollow, 1–10 tap strip; keys A+/A/B/C/pass, fixed dollars per sheet, disabled keys greyed with would-be dollars; tap = grade recorded, sized at nearest enabled key, loud. |
| **F3 Focus list with conviction WHY** | DRC shows his pick and Cobalt's rank for every card. | Rank = conviction × proximity (opaque score); ~4 focus names each with one WHY line; promote/release; pick-vs-rank logged (row now; DRC rendering lands with F14 in S3). |
| **Radar panel (§5 host)** | Acceptance = 2–3 live mornings beside DAS on a static render before the card slice is called done. | ASET Flask sheet grown into the ladder: strips, #1 + #2 open, detail column drops below at <1150 px, ARMED/IN-TRADE pinned above WATCH, owner badges, health line (thresholds per mock #8 ruling). Front-end only = Sonnet-eligible. Fixes the 09-02 ASET-tab focus-handoff fumble (hotkey focus never on the panel). |
| **F12 Missed records via nightly replay** | Nightly report lists misses with the gate/variable that excluded them. | Archiver post-run: replay every `trade_def` trigger over the day's bars; trigger on an unarmed/absent card = MISSED row with `excluded_by` (incl. `rule_10`, `trade_count_band`, `window`) and counterfactual R from bars. |
| **F13 Auto-archive + benchmark + miss line** | A Tesla-class mover absent from the pool appears in the miss line with `excluded_by`. | Top-N movers archived nightly regardless of watchlist; benchmark query (movers ≥ config move) diffed against the in-play set; one miss line — into the existing DRC prefill now, the SMB-format DRC note at S3. |

**S2 smoke:** dev-vault day replay on a recorded session: pool churns, a
Rubberband card lands within one interval, ranked focus list, MISSED rows
with `excluded_by` and counterfactual R present; then live mornings 1–3
beside DAS on the panel (cards graded by tap, fill via the existing
fill-recompute; legs hand-logged in the DRC chat until S3).

**Code prompts owed:**
- S2-P1 · Opus 5 · fresh · F2 pool job + membership history · Finviz bar poller at working TF (reuses the spike's client path) · account-mode tag.
- S2-P2 · Opus 5 · fresh · F8 precondition evaluator, Rubberband first, then the other five · F10 dot scoring + ladder sizing + tap recording · taxonomy v0.8 bump.
- S2-P3 · Sonnet · fresh · Radar panel front-end (no write path) — ladder, strips, badges, tap strip, phone frame · F3 rank + WHY display.
- S2-P4 · Opus 5 · fresh · F3 pick-vs-rank rows · F12 nightly replay + counterfactual R · F13 top-N archive + benchmark + miss line · S2 smoke.
- Parallel, non-write: Agent SDK spike (Sonnet) — two-session test (subscription CoS + local worker via LiteLLM proxy), HITL hooks question — so S5's F20 does not start cold.

**Rulings/inputs owed before S3:** DRC template review session (Dejan +
Claude, his docx + SMB template → live Templater template) — before S3-P3.
Stop-override authority (mock #6) — before S3-P2.

---

## S3 — Exits + DRC on radar cards (10-05 → 10-16)

| Feature | Charter acceptance (test) | What S3 delivers |
|---|---|---|
| **F11 Fill recompute + fill/exit capture** | Fill 27% past plan → warning, FILLED row, DRC counts it as a trade; a ½-off tap during the trade produces an estimated leg without a keystroke. | TRIGGERED → FILLED @ [last poll, editable] + PASS; drift warning scaled to ATR (his 09-03 defect), >20% distance = "re-read stop"; `legs` table {card, shares, price, time, flag estimated/confirmed}; ½ · ⅓ · flat · typed compounding off running shares; running 0 → CLOSED; realized R provisional while any leg estimated; DM line "TSLA filled 372.82 10" / "TSLA out 374.50 all" writes the same rows. No tap by expiry → EXPIRED. |
| **F22 Trade-note auto-creation** | A fill at 10:12 has a trade note by 10:13. | On FILLED: trade note via vaultwrite (create-if-absent, frontmatter site, L28) lighting the dataview table; legs update the note in place. Verify whether slice-2's version exists; if so, convert to the state-machine event. |
| **F14 DRC prefill / reconcile / DRC→mode** | 09:00 proposal quotes the prior DRC; DRC note exists at 15:41 with every Cobalt field filled. | Separate `DRC-YYYY-MM-DD.md` in SMB format from the reviewed Templater template; prefilled 15:40: cards written / trades taken (FILLED only), every unfilled card asked taken/passed/discarded, pick-vs-rank, miss line, cost-of-discipline tally, adherence checkboxes, excitement audit, estimated legs to confirm, time blocks, PnL; daily note gets 3-line stub + link; next-morning F6 proposal cites it. `drc_builder` PDF = SHOULD, only if the sprint has room. |
| **F15 Prediction records** | Any card's grade replays from stored inputs. | Every score + WHY stored with its inputs and joined to the card outcome (legs, realized R, MISSED counterfactual); a `replay(card_id)` command recomputes the grade from stored inputs and diffs. This is the corpus the post-MVP reasoning layer trains on. |

**S3 smoke:** one live morning: radar card graded by tap, filled, ½ off,
closed; trade note at fill; DRC note at 15:41 with the estimated leg, pick-
vs-rank and miss line; next morning's 09:00 proposal quotes that DRC;
replay of the card's grade matches.

**Code prompts owed:**
- S3-P1 · Opus 5 · fresh · F11 legs, scale-out, ATR-scaled drift, DM fallback line, EXPIRED timer.
- S3-P2 · Opus 5 · fresh · F22 trade note as state event · stop editing per override ruling.
- S3-P3 · Opus 5 · fresh · F14 DRC note (after the template review) · F15 prediction records + replay · S3 smoke.

---

## S4 — 19b trigger detection + strike alert (10-19 → 10-23, ONE WEEK, CAPPED)

**Preconditions (must be true on 10-19 or the sprint slips, not stretches):**
trading PC on Tailscale (his) · `.htk` hotkey labels checked against
`{DAYMODE}-{KEY}-{SIDE}` (his, mock #3) · F8 live since S2.

| Feature | Charter acceptance (test) | Week plan |
|---|---|---|
| **F9 19b, focus scale** | Alert on the panel ≤5 s after bar close, premarket + RTH; if Finviz throttles at 3 s, criterion re-rules to what 10 s delivers (~8 s). | Day 1: re-measure at 2–3 s cadence, premarket + RTH, ≤5 names (spike script pattern, measurement only) → criterion fixed. Days 2–3: price-cross detector with the card's confirmation policy on ≤5 ARMED names; TRIGGERED transition + MISSED on unarmed. Days 4–5: SSE push → pinned browser tab on the PC over Tailscale, browser notification + sound, three numbers + hotkey; Mattermost DM phone fallback. Friday: whatever is proven ships; remainder → post-MVP lane (toast listener, other trigger types). |

**Code prompts owed:** S4-P1 · Opus 5 · fresh · re-measure + detector;
S4-P2 · Opus 5 · fresh · SSE delivery + notification + fallback + week report.

---

## S5 — Prep + platform + playbook (10-26 → 11-06)

**Flag:** this is the ladder's heaviest slot (F20/F21 are the Agent SDK
bring-up). It holds only if the S2 SDK spike ran. If S5 overflows, F4/F5
(prep, §7 rank 5) are not cut — they are MUST — but F23 PPTX renderer is the
first candidate to slip into the acceptance week, since M11 is weekly.

| Feature | Charter acceptance (test) | What S5 delivers |
|---|---|---|
| **F4 Prefill all day, ownership flags** | He writes at 06:00, prefill re-runs at 08:45, his text byte-identical; diff row in `vault_writes`. | Config cadence + manual trigger; per-field flag cobalt / cobalt-degraded / human; "as of HH:MM" stamps; VIX/BTC loud "n/a (manual)". |
| **F5 Market-context checkpoints** | 08:15 block cites what changed since 07:45; source outage = degraded, never blank. | 07:15/07:45/08:15/08:45 jobs: Finviz numbers deterministic; single-house narrative (Claude on subscription via fast wire, L22) receives the filtered list only, returns delta vs previous; missed checkpoint loud. |
| **F20 Chief of staff, thin** | A config-drafted agent appears only after an approved HITL card. | One resident SDK session on subscription auth; he talks only to it (Mattermost); HITL cards in one place, Approve/Deny; agent registry as data (L16), no agent code. |
| **F21 Genesis import + continuity pack** | Cobalt answers "why is the stop buffer 0.02" from the imported record. | Ledger + vault history through the memory pipeline into cobalt_brain; continuity briefs stored in Think outside the repo (authoring = Dejan + fleet chats, starts during S2). |
| **F23 Playbook PPTX renderer** | One deck per setup family with the latest cards. | trade-reporter renderer from playbook data; Sunday 18:00 job. |
| **F16 close** | `validate` passes; no inline literal in a predicate. | Final sweep across all consumers. |

**Code prompts owed:** S5-P1 · Opus 5 · fresh · F4 cadence + flags; S5-P2 ·
Opus 5 · fresh · F5 checkpoints; S5-P3 · Opus 5 · fresh · F20 CoS + HITL +
registry; S5-P4 · Opus 5 · fresh · F21 genesis import; S5-P5 · Sonnet · fresh ·
F23 renderer (no vault write). SHOULD Vital Dawn only if a slot frees.

---

## Acceptance week (11-09 → 11-13) — Charter §12

Every §3 MUST passes its test on the live vault + live DB, five consecutive
trading days, heartbeat green, card used in ≥3 live mornings. Then the
post-MVP lane (§11) fights for slots at sprint boundaries.

## Carried open items (owner)

- Trading PC joins Tailscale (his) — S4 precondition; S1-P1 reports status.
- `.htk` label check (his) — S4 precondition.
- Health thresholds (#8) + detail-column order (#11) — before S2-P3.
- DRC template review session (Dejan + Claude) — before S3-P3.
- Stop-override authority (#6) — before S3-P2.
- Trade-count goal band value (his, Rules Engine session) — placeholder in S1.
- Hand-logged legs in the DRC chat continue until F11 lands (S3).
- Vault backup restic → B2 + SSD (gated, before Tahoe) — schedule as an Opus write session at the S1/S2 boundary; not a Charter feature but the only thing standing between the corpus and a bad night.
- `sudo crontab -l` (his). Push of taxonomy/trade-defs-v0_3 (his). rules.yaml + gemini-era-vault-side commit ruling.
- Taxonomy v0.8 consolidation — at S2-P2.
- Spike leftovers: TV webhook extended hours + alert-slot cap — post-MVP SHOULD, untouched here.
