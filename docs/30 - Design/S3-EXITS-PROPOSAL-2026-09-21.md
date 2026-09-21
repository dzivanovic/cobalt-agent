# S3 EXITS — proposal (2026-09-21 18:38 ET)

Proposer seat `s3-exits-design-0921` (Opus 5). Scope: ladder `S3-P1 · F11` + `S3-P2 · F22`. This is the INPUT to the four-house tribunal (L67). The tribunal produces the design; nothing here is built. All `file:line` refs are on MAIN at `be58530`. PROVEN = read in the file. UNPROVEN = could not be checked from reads (L70). **ASSUMED** = a value or behaviour that is his and is not in the ladder, Charter, settings or code (L53). It goes to §12 as an owner item and is never treated as settled.

Out of scope: F14 (DRC note; its template is his sitting, `cto-2026-09-21.md` R48/R52) and F15 (S3-P3). §7 and §10 name only the seams they need.

---

## 1. FACT BASE

| # | Claim | Where | |
|---|---|---|---|
| F1 | Eight states. The edge table is the single authority: TRIGGERED→{FILLED, PASSED, EXPIRED}, FILLED→{CLOSED}, and the four terminal states have no exits | `cards/models.py:37-49`, `:92-114` | PROVEN |
| F2 | The stop is editable only in WATCH and FILLED. The key is editable only in WATCH | `cards/models.py:120`, `:126` | PROVEN |
| F3 | `transition()` does four things: gates on the session (it refuses in `market_reset`), checks the edge under a row lock, refuses ARM when the card is unsized, and folds pending stop edits into the evidence. It writes the ledger row and the cached state in one transaction | `cards/store.py:239-371` | PROVEN |
| F4 | `fill()` is THE one path to FILLED. A radar card goes the strict way (it must already be TRIGGERED). A manual card gets a one-click walk, actor cobalt. The F3 pick is written under a savepoint | `cards/store.py:429-530`, `:486` | PROVEN |
| F5 | The sheet's fill-recompute keeps the same grade dollars and the same stop, then uses shares = ⌊risk$ ÷ \|fill−stop\|⌋. There is a typo guard: `max_fill_distance_pct` (config, 5). The warning fires at `distance_change_pct ≥ 25`, and that 25 is a **hard-coded constant** | `aset/engine.py:267-312`, `:43`; `configs/dev/aset.yaml:53` | PROVEN |
| F6 | `mark_filled` calls `CardStore.fill()` with the recompute in the evidence. It then UPDATEs `aset_sizings.actual_fill`, `recomputed_shares`, `recomputed_used_risk`, `share_delta`, `distance_change_pct` and `filled_at` | `aset/store.py:185-257` | PROVEN |
| F7 | `/fill` works only from the **manual sheet form**. It rebuilds the `SizingResult` from the posted form fields, and it needs `orig_timestamp` + `card_row_id` from `/size` | `aset/web.py:1046-1101` | PROVEN |
| F8 | A radar card reaches FILLED only through `/card/{id}/move` → `fill()`, and the evidence is just `{"via":"aset.sheet"}`. **No fill price and no shares are recorded.** The ladder says S2 fills radar cards "via the existing fill-recompute", but that path is not wired for radar cards | `aset/web.py:1181-1209` | PROVEN |
| F9 | The radar panel (`/radar`) has routes for key, dot, promote and release only. It has NO arm, triggered, fill, leg or stop route. Its IN-TRADE block shows the stop and 1R/2R and nothing else. NOTES says "no notes source wired to radar cards (S3)" | `aset/web.py:1294-1390`; `aset/radar_panel.py:978`, `:1001` | PROVEN |
| F10 | Radar card creation is automated. The soft attestation check refuses the **key tap** (radar) and `/size` (manual) when the attested `.htk` disagrees or nothing is attested | `aset/web.py:1314`, `:985`; `daymode/match.py:80-117` | PROVEN |
| F11 | The attestation lives on `day_modes` (`attested_sheet`, `attested_at`) | `daymode/store.py:132-169` | PROVEN |
| F12 | Stop edits go to `card_stop_edits` (from, to, actor, in_state). They are not a transition; the next transition folds them. In FILLED, the recompute changes open risk and leaves size alone | `cards/migrations/0002_card_stop_edits.sql`; `cards/store.py:643-740`; `aset/engine.py:126` | PROVEN |
| F13 | A radar card stores `structural_stop` + `trigger_price` as immutable formation evidence. `entry`/`stop` are the live inputs. `last_price` = the last closed working-TF bar close. A reset has no marker column | `db_migrations/0007_radar_cards.sql:3-8`, `:36-38`; `radar/evaluate.py:502`, `:776` | PROVEN |
| F14 | There is at most one open radar card per (member, def, direction), and FILLED counts as open | `0007_radar_cards.sql:90-92` | PROVEN |
| F15 | The radar resident expires radar cards from WATCH, ARMED and TRIGGERED via `expires_at`/avoid | `cards/expire.py:71`; `radar/evaluate.py:1351`; `cards/store.py:1055` | PROVEN |
| F16 | No code moves a radar card to TRIGGERED. The S4 detector (F9) is owed. Today TRIGGERED is only his sheet button | grep `TRIGGERED` in `radar/`, `cards/` | PROVEN |
| F17 | Health pills are computed on FILLED radar cards from an entry snapshot and `card.stop` | `radar/evaluate.py:780-797` | PROVEN |
| F18 | Two ATRs are stored. `atr_working` = ATR(working TF, 14) Wilder, and it is in the receipt observations. The daily ATR(14) is an input of `htf_level_proximity` | `radar/evaluate.py:437-444`, `:467-475`, `:568`; `radar/anatomy/daily.py:122-126` | PROVEN |
| F19 | F12's counterfactual R: risk = \|card entry − stop in force at trigger\|, `cf_r = (exit − fill)/risk × sign`. There is one formula, shared | `replay/cards.py:223-288`; `replay/models.py:185-213` | PROVEN |
| F20 | `vaultwrite.VaultWriter` provides `create_if_absent`, `upsert_unit` (marker-bounded, human wins, override rows), `upsert_region` (frontmatter via `frontmatter_span`) and `restore` | `vaultwrite/writer.py:559`, `:644-680`, `:895`, `:1066` | PROVEN |
| F21 | **Slice-2's trade-note writer exists**: `prefill/trade_note.upsert_trade_note`. Cobalt owns five keys (date, symbol, direction, stop_price, entry_price). exit_price, entry_time, exit_time, profit_loss, trade_def and RVOL are his. The body is his template's | `prefill/trade_note.py:1-41`, `:118-169` | PROVEN |
| F22 | It is called at **`/size` (card sizing)**, not at FILLED, and only on the manual sheet. Radar cards never create a note | `aset/web.py:1019-1021` | PROVEN |
| F23 | Path is `1 - Trading/2 - Trades/Trade-%Y-%m-%d %H-%M-%S -{ticker}.md` | `configs/cobalt/prefill.yaml:8`, `:14` | PROVEN |
| F24 | The DRC prefill finds a card's note by **nearest filename timestamp to the card's `created_at`**. For a radar card, created at formation and filled later, it would miss | `prefill/drc.py:101-121` | PROVEN |
| F25 | His template is `5 - Templates/Individual Trade Template.md`, with the same 12 frontmatter keys as `FIELD_ORDER`. His daily table is `TABLE symbol, profit_loss, strategy, entry_time, direction … FROM "1 - Trading/2 - Trades" WHERE file.cday = this.file.day` | `5 - Templates/Individual Trade Template.md`; `5 - Templates/Daily.md:49-54` | PROVEN (text) · lights in Obsidian UNPROVEN |
| F26 | The daily table selects `strategy`, but new notes carry `trade_def` (ADR-0008 D4) | `Daily.md:50`; `trade_note.py:30-41` | PROVEN |
| F27 | **There is no inbound DM path.** `notify/mattermost.py` is outbound HTTP only, "no websocket". The kill-phrase matcher is waiting "for the Mattermost DM listener the moment one lands" | `notify/mattermost.py:6-11`, `:130`; `jobs/killswitch.py:106-116` | PROVEN |
| F28 | `legs` and `fills` are declared USER-side but not built | `db_migrations/placement.py:103-111` | PROVEN |
| F29 | Main's last migration is `0011`. `bars/chunk-2-0920` adds `0012`. The setups one-build prompt names `0013` as possible | `db_migrations/`; `git log main..bars/chunk-2-0920`; prompt `65-setups-one-build.md:67` | PROVEN |
| F30 | `setups/seven-0921` and `s2/stale-marker-0921` do not exist as local branches tonight | `git branch --list` | PROVEN (absence) · their final file set UNPROVEN |
| F31 | The mock shows TRIGGERED with three numbers. IN-TRADE has an editable stop (YOURS amber + delta + ↺ reset), ½ off / ⅓ off / flat / reset compounding off running shares, and a fill recompute that warns at >20 % | mock `card-spec.md:18`, `:53-62`; `decisions.md:25`, `:29`, `:33` | PROVEN |
| F32 | Charter §5 answers mock #16 as "single fill at MVP, partials post-MVP". F11 (amended 09-04) adds scale-out legs. The reading used here: **one entry fill, many exit legs** | `MVP-CHARTER-v0_2.md` §5; F11 `:135-147` | PROVEN (text) · reading ASSUMED |
| F33 | The "ATR scaling (his 09-03 defect)" has no source text in the ladder, BACKLOG or LEDGER (grep `ATR`/`drift`) | ladder `:590` | UNPROVEN |

---

## 2. STATE MACHINE (proposed): the edge table is unchanged

The edges already exist (F1). F11 adds **rows and actors, not edges**. Every move is his. Cobalt-actor moves stay limited to expiry (F15) and the existing manual one-click hops (F4).

| Transition | Actor | Trigger | Stored row(s), same transaction | Inputs stored (L57) |
|---|---|---|---|---|
| ARMED → TRIGGERED | YOU (panel "TRIGGERED" tap) until the S4 detector, then COBALT | tap | `card_transitions` | `last_price` + its bar ts |
| TRIGGERED → FILLED | YOU | "FILLED @ [price] [shares]" tap, or DM line | `card_transitions` (via `fill()`) + entry `legs` row + `aset_sizings` fill columns (the F6 cache) + pick (F4) | price, its source (`last_poll`/`typed`/`dm`) and as-of; shares; stop in force; `structural_stop`; drift receipt (§4); attested sheet + `day_modes` id |
| TRIGGERED → PASSED | YOU | PASS tap | `card_transitions` | — |
| WATCH/ARMED/TRIGGERED → EXPIRED | COBALT | existing radar expiry (F15). The ladder's "EXPIRED timer" = verify TRIGGERED is covered; no new timer unless the tribunal finds a hole (Q10) | existing | existing |
| FILLED (leg) | YOU | ½ · ⅓ · flat · typed, or DM "out" | `legs` exit row; **no transition** (same principle as stop edits, F12) | running before/after, preset, price source + as-of, flag |
| FILLED → CLOSED | YOU (his leg that brings running to 0) | the zero-running leg | `card_transitions` evidence `{leg_id}` + that leg, one transaction | legs ids |

Refusals, all loud: a leg on a non-FILLED card; a leg whose shares exceed running; a preset result of 0 shares ("½ of 1 is 0 — use flat or type"); a fill in `market_reset` (the existing gate). A fill on a radar card that is not TRIGGERED stays refused by `fill()`'s strict path. Whether to relax that before S4 is owner item O7.

**The one fill path (L3).** `AsetStore.mark_filled` + `compute_fill_recompute` are REUSED for both origins. A new `SizingResult.from_card(row)` rebuilds the input from the card row (entry, stop, grade, risk_budget, direction), replacing the form rebuild. `/fill` (manual) and the new panel fill route both call it. There is no second recompute. The hard-coded `FILL_DISTANCE_WARNING_PCT` (F5) **dies** and is replaced by his setting (§4).

---

## 3. THE `legs` TABLE (`"user"`, L32)

One table covers the entry fill and the exits. `fills` is struck from `DECLARED_TABLES`, or kept for post-MVP partial entries (Q2).

| Column | Type | Note |
|---|---|---|
| id | bigint identity PK | |
| user_id | int NOT NULL DEFAULT GUC FK `"user".traders` | tenancy, same as `0007:120` |
| card_id | bigint NOT NULL FK `"user".aset_sizings` | |
| seq | smallint NOT NULL | 0 = entry, 1..n = exits; UNIQUE (card_id, seq) among current rows |
| kind | text CHECK ∈ {entry, exit} | partial UNIQUE: one `entry` per card (single fill at MVP, F32) |
| shares | int NOT NULL > 0 | his broker's shares |
| price | numeric(14,4) NOT NULL > 0 | |
| at | timestamptz NOT NULL | when he tapped or sent |
| flag | text CHECK ∈ {estimated, confirmed} | |
| price_source | text CHECK ∈ {last_poll, typed, dm} | |
| price_asof | timestamptz NULL | the `last_price` bar ts when `last_poll`, else NULL |
| preset | text NULL CHECK ∈ {half, third, flat, typed} | exits only |
| running_before, running_after | int NOT NULL | CHECK after = before − shares (exit) / = shares (entry) |
| stop_in_force, cobalt_stop | numeric(14,4) NOT NULL | R38 gap on every leg (§5) |
| source | text CHECK ∈ {panel, sheet, dm} | |
| corrects | bigint NULL FK legs(id) | a correction is a NEW row; the old row is never updated |
| session, account_mode | text NOT NULL | same stamps as the card |
| day_mode_id, attested_sheet | FK / text | entry row only (§8) |

Append-only via the existing `"user".refuse_row_update()` trigger (`0007:105-111`). A view `"user".legs_current_v` takes the last correction per (card, seq). The next free migration number is taken at build (after `0012`/`0013`, F29); the L68 gate re-derives it.

**Compounding.** Presets run off `running_before` (DAS semantics, mock decision 13). **Rounding (ASSUMED, O1):** ½ = ⌊running/2⌋ and ⅓ = ⌊running/3⌋. flat = running. typed = his count ≤ running. What his broker does is his fact, not ours.

**Estimated vs confirmed.** A mid-trade preset tap takes `last_price` → `estimated`, with no keystroke (Charter test 2). A typed price or a DM price → `confirmed`. The closing leg's price is his (Charter F11): the flat control shows the prefilled price in an editable field and commits `confirmed` only on his explicit ✓. A plain flat tap with the untouched prefill stays `estimated` and is listed for correction. A later correction row with a typed price → `confirmed`.

**Realized R.** This is a pure function over `legs_current_v` + the entry row, versioned like F12's formula. It is not stored as a number, so it is always replayable (L57). Per exit: `sign × (exit − fill) × shares ÷ (entry_shares × R_unit)`, summed. **R_unit** is Q1: F19's planned unit `|card entry − stop in force at fill|` (comparable with counterfactual R) or the actual `|fill − stop|`. `provisional = any current leg estimated`. No statistic is rendered here; §7 exit efficiency is F14's to render, with n and n≥30 (L8).

---

## 4. DRIFT WARNING, scaled to ATR

Today (F5): `drift_pct = |new_dist − planned_dist| ÷ planned_dist × 100`, warn at ≥ 25 (constant). Charter and mock say >20 %. The ladder adds "scaled to ATR" without a source (F33).

Proposed shape (ASSUMED until the tribunal and he agree):
- `drift_pct` as today (one formula, F5).
- `drift_atr = |new_dist − planned_dist| ÷ ATR` where **ATR = `atr_working`** from the card's latest `radar_score_receipt` observation (F18). The receipt id, value and bar ts are stored in the fill's evidence.
- Warn "re-read stop" when `drift_pct > P` **and** `drift_atr ≥ K`. The ATR term stops a 1¢ move on a 4¢ stop from shouting. The pct term keeps the charter wording.
- **P and K are HIS values**, and they live in `"user".trader_settings` beside `card.curves` (L53: never committed config). Missing setting → the fill is refused loudly with the setting named (L1). There is no silent default.
- A manual card has no receipt → `drift_atr` = n/a, shown as "ATR n/a — pct only". It is never blank and never guessed.
- Charter test "fill 27 % past plan → warning": read as `drift_pct = 27 > P = 20` (Q6). The test fixture's ATR is chosen so that `drift_atr ≥ K`.
- The warning is a display on the fill plus a stored field. It never blocks the fill, which is already done in DAS.

---

## 5. STOP OVERRIDE (R38, "B with your addition")

- `card_stop_edits` gains `kind ∈ {edit, reset}` (a migration column, default `edit`). **Reset** = a stop edit back to `structural_stop` by him (the mock's ↺).
- "His stop is the plan": `aset_sizings.stop` is already the live stop (F13). The edit path already recomputes open risk in FILLED (F12). Nothing new is needed for "plan".
- Owner of the stop is **derived**: `yours` = the last `card_stop_edits` row for the card has actor YOU and kind `edit`. It is not stored twice.
- Render, IN-TRADE and WATCH: his stop with an amber `YOURS` badge and delta vs Cobalt; **Cobalt's structural stop always visible beside it**, never hidden; `↺ <cobalt value>` on the note line (mock decision 11).
- The gap is recorded on the trade: every `legs` row carries `stop_in_force` + `cobalt_stop` (§3), and the FILLED/CLOSED evidence carries the folded stop edits (F3). The DRC/Friday review reads the stop path and both R figures: realized R on his stop, and "R had Cobalt's stop held" = F12's counterfactual formula applied from the fill (seam for F14/F15; not computed in S3).
- STOP_EDITABLE (WATCH, FILLED) is unchanged. There is no stop edit in ARMED/TRIGGERED (mock decision 11).

---

## 6. THE DM LINE

**No inbound path exists (F27).** The DM path therefore needs a **new resident** (L2 watcher: a deterministic poller, no LLM). **The panel tap path is built FIRST** and is complete without it.

- Grammar (case-insensitive, one line):
  `<TICKER>[#<card_id>] filled <price> <shares>` → TRIGGERED → FILLED;
  `<TICKER>[#<card_id>] out <price> <shares|all|half|third>` → exit leg.
  The price is typed, so it is `confirmed`.
- Match: exactly one card for that ticker in the required state (TRIGGERED for `filled`, FILLED for `out`). Zero or more than one → **NOT RECORDED**, with a reply listing candidate `TICKER#id` lines. It never guesses.
- The line goes through the same store functions as the panel (L3) and the same gates (session, edge, attestation record).
- Unparseable → reply `NOT RECORDED: could not read "<line>". Forms: TSLA filled 372.82 10 · TSLA out 374.50 all`. Nothing is written. Every inbound line is stored with its parse result (`"user".dm_inbound`, its own migration; dedupe by post id).
- The resident `com.cobalt.dmlisten`: it polls the DM channel over REST (`notify/mattermost.py`'s credential path, VaultManager only, F19 redaction on every reply). It also checks the kill/resume phrases (F27: one listener, not two), has a heartbeat probe, a plist, and a `reads:` declaration (L42).
- It is Mattermost-only. Voice is post-MVP.

---

## 7. F22 TRADE NOTE

- **Event:** the note is written in the same request as the FILLED fill, after the DB commit. The DB comes first (the 09-03 lesson, `aset/web.py:1081-1086`). Write failure → a red banner "FILLED — trade note NOT written: <reason>", plus `cobalt cards trade-note <card_id>` to retry (idempotent: `create_if_absent`). This meets "fill at 10:12 → note by 10:13" synchronously (Q9).
- **One writer (L3):** `prefill/trade_note.upsert_trade_note` is converted to take the card row + FILLED transition (not a `SizingResult` + form time) and serves both origins. Whether `/size` keeps writing notes at sizing time (today's slice-2 behaviour, F22) is owner item O4.
- **Path:** his pattern (F23) with **`when` = the FILLED transition time** (ET). The resulting path is stored on the card (`aset_sizings.trade_note_path`, new column). F14 reads that column instead of the nearest-timestamp search, which misses radar cards (F24).
- **Frontmatter:** his template's 12 keys, in his order (F25). Cobalt's five keys come from the card with `entry_price` = **the fill price**. His keys (exit_price, entry_time, exit_time, profit_loss, trade_def, RVOL) are created blank. Filling them from legs/card while blank via L28 clause 2a is owner item O5 / O6. Once he types a value, it is never touched.
- **Body:** his template body, verbatim (`trade_note.py:93-104`), then one Cobalt section `cobalt-legs` with one unit per leg seq (`leg-<seq>`). Each unit is a line: `exit ½ · 50 sh @ 374.50 · 10:31 · estimated`. A correction row updates the same unit in place (same id, L28.2).
- **He edited the note:** the frontmatter merge keeps his keys (F21). A changed Cobalt line in `cobalt-legs` → human wins, override row (F20). The DB leg is NOT changed from the note (no reverse parse, deterministic). The override surfaces in the DRC's "estimated legs to confirm" (Q8).
- The dataview table lights by `file.cday` = the fill day (F25). Its `strategy` column stays blank for `trade_def` notes (F26). That is his template, and it is flagged, not changed.

---

## 8. ATTESTATION, the soft check as the ladder words it

- Unchanged: card creation stays refused while the attestation disagrees or is absent. That means the key tap for radar and `/size` for manual (F10).
- New in F11: the entry leg records `day_mode_id` + `attested_sheet` (F11 row), so "a fill is recorded against that stated sheet".
- A fill is **not refused** on a mismatch (the ladder refuses only creation). It records `sheet_mismatch = true` loud on the card. Q5 asks whether to refuse instead.
- Nothing reads DAS. Nothing overwrites the attestation (CLAUDE.md; ladder `:590`).

---

## 9. DELIBERATELY NOT CHANGED

Scoring (`cards/scoring.py`), evaluation (`radar/evaluate.py`), dots, proximity, conviction, ranking and pinning (`cards/radar.py`), admission, `proposed_key`, sizing keys and dollars, health pills (F17), expiry rules, the F12 counterfactual formula, and `last_price`'s meaning (the stale-score design owns it).

**L52 finding:** nothing proposed feeds a score, a rank, an admission or what a card's score shows. The fill, legs, drift, stop owner and note are records and displays on the card. So the (a)–(d) bar is not triggered by scoring. The design still sits the L67 tribunal because it reaches the card's display. (a) holds anyway: every number is his, `system.bars`, or a stored receipt.

---

## 10. CHUNKS (dependency order)

| # | Chunk | Write path (L29 → Opus 5 floor) | Migration | Depends on | Est. h |
|---|---|---|---|---|---|
| C1 | `legs` + `legs_current_v` + `card_stop_edits.kind` + `aset_sizings.trade_note_path` + drift fields; `SizingResult.from_card`; fill writes the entry leg in `fill()`'s transaction; drift with ATR + settings keys; the constant dies | DB — yes | M1 | stale-score + setups merged or rebased over | 7 |
| C2 | exit legs, presets, running shares, zero → CLOSED, corrections, realized-R function + provisional, `cobalt cards legs` CLI | DB — yes | — | C1 | 5 |
| C3 | panel routes + render: TRIGGERED, FILLED @ [price][shares], PASS, ½ ⅓ flat typed, ✓ confirm, stop YOURS / Cobalt / ↺ | DB (routes) — yes | — | C1 (C2 for legs) | 7 |
| C4 | F22: converted `upsert_trade_note`, fill-time event, `cobalt-legs` units, `trade_note_path`, retry CLI | vault — yes | — | C1, C2 | 5 |
| C5 | `com.cobalt.dmlisten` resident: poller, parser, replies, `dm_inbound`, kill/resume, heartbeat probe, plist | DB + outbound — yes | M2 | C2 | 8 |
| C6 | S3-P1/P2 smoke, DevDocs, ADR (F11/F22 decisions) | no | — | all | 3 |

- Write-path chunks: **5** (C1–C5). Migrations: **2** (M1, M2), numbers taken at build (F29, L68).
- Parallel: after C2, **C3 ∥ C4 ∥ C5**. C6 comes last.
- **RESTARTS (a GUESS until `cobalt jobs restarts`, L42):** C1–C4 touch `cards/`, `aset/`, `prefill/` → `com.cobalt.aset` + `com.cobalt.radar` (it imports `cards.store`), restarted inside the 20:00–21:00 pause with the residents down first (L43/L66). C5 bootstraps a NEW resident.
- Rebase: S3-P1 is cut from main **after** the setups one-build (`cards/store.py`, `evaluate.py`, `scoring.py`) and the stale-score build land. It must not re-decide either design: `last_price` staleness is theirs. The fill prefill uses `last_price` + its bar ts, and if `last_price` is NULL the field is empty and he types (never `entry`, the W6 defect pattern). `radar_panel.py` was touched twice today on main (`a660a7c`, `04b0dbd`). The stale-marker branch is absent (F30).
- **Honest estimate:** 35 h of build seats. **About 50 h** including one fix round per chunk, which is the pattern of 09-19 → 09-21. S3 runs 09-24 → 10-07 and also carries S3-P3.

---

## 11. TEST PLAN (L45: real artifacts, L69 settings on a constructed config)

Charter acceptance, verbatim:
- **F11:** "Test: fill 27% past plan → warning, FILLED row, DRC counts it as a trade; a ½-off tap during the trade produces an estimated leg without a keystroke."
- **F22:** "Test: a fill at 10:12 has a trade note by 10:13."

Fixtures (real shape, personal values stripped): his `Individual Trade Template.md` frontmatter/body; one real `2 - Trades` note's frontmatter (keys, quoting); the `Daily.md` dataview block; a real `radar_score_receipt.observations` row with `atr_working` (hub copies from `cobalt_dev` or a read-only prod query); a real Mattermost `GET /channels/{id}/posts` JSON (dev bot, hub capture).

With-DB (`cobalt_dev`): radar card TRIGGERED → panel fill at a price 27 % distance drift → FILLED row, entry leg, warning stored with its ATR receipt, pick row; ½ tap → estimated leg, running halves; ⅓ on 1 share → refused; flat ✓ typed → confirmed, CLOSED in the same transaction; correction row → current view flips and realized R loses `provisional`; stop edit in FILLED then ↺ → `kind=reset`, owner derived back to Cobalt; attested-sheet mismatch → recorded, not refused; `market_reset` → refused, nothing written.

Dev vault: note created at fill with `entry_price` = fill; second leg updates unit in place; he edits a leg line → override row, DB unchanged; he typed `exit_price` → never overwritten; `trade_note_path` stored; write failure → banner + retry CLI creates it once. DM: the two Charter lines write the same rows as the panel; ambiguous ticker → NOT RECORDED + candidates; garbage → NOT RECORDED reply, zero rows; the kill phrase is still honoured. S3 smoke (ladder `:596-599`) runs the tap path end-to-end on one live morning.

---

## 12. OPEN QUESTIONS (tribunal) and OWNER ITEMS (his)

**Tribunal (12):**
1. R_unit: planned `|entry − stop at fill|` (comparable with F12's cf_r) vs actual `|fill − stop at fill|`?
2. One `legs` table with `kind`, striking `fills` from DECLARED_TABLES, vs two tables?
3. Append-only legs with correction rows + current view (proposed) vs UPDATE in place?
4. Keep `aset_sizings.actual_fill…` as a cache of the entry leg (like `state` caching `card_transitions`), or retire the columns (L3)?
5. Attestation mismatch at fill: record + flag (proposed) vs refuse?
6. "27 % past plan" = `drift_pct` 27 (proposed) vs a fill 27 % of the distance beyond the trigger?
7. DM ambiguity: refuse with candidates (proposed) vs latest card wins?
8. A human edit to a `cobalt-legs` line: override only, DB unchanged (proposed), vs parse back into a correction row?
9. Trade note synchronous in the fill request (proposed) vs a queued job with retry?
10. Does the existing radar expiry cover TRIGGERED fully, or does "EXPIRED timer" need a TRIGGERED-specific window?
11. ↺ reset target: `structural_stop` at formation (proposed) vs a Cobalt in-trade trail (none exists; M8 trail selection)?
12. DM resident: REST poll (proposed) vs websocket; poll interval is an engine tunable?

**Owner items (8), each A/B:**
- O1. ⅓ / ½ shares: A round down (⌊running/3⌋), B round to nearest?
- O2. Drift pct threshold: A 20 on radar AND the manual sheet (replaces the sheet's 25), B 20 radar, 25 sheet?
- O3. ATR floor K (working-TF ATRs): A no ATR floor until you give a number, B you give K now?
- O4. Manual sheet notes: A keep creating a note at every sizing (today), B create notes only at FILLED, same as radar?
- O5. exit_price / entry_time / exit_time / profit_loss: A Cobalt fills each only while blank, B they stay yours, never written?
- O6. `trade_def` on a radar trade note: A Cobalt fills it from the card while blank, B it stays yours?
- O7. Radar fill before the S4 detector: A two taps (TRIGGERED, then FILLED), B one tap from ARMED writes both rows with actor you?
- O8. DM line in S3: A build the listener in S3, B panel only in S3, DM after S3?
