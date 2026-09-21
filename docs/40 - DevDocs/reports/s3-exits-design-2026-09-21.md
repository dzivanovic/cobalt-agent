# S3 exits design — proposer report (s3-exits-design-0921) · 2026-09-21 18:32–18:40 ET

## §0 Headline
- The proposal is written: `docs/30 - Design/S3-EXITS-PROPOSAL-2026-09-21.md` (231 lines), covering F11 fill/legs and F22 trade note. It is the input for the L67 tribunal. Nothing was built.
- The edge table stays unchanged. It adds 6 chunks, 5 of them write paths, and 2 migrations. The panel tap path comes first. The DM line needs a NEW resident, because there is no inbound path.
- Slice-2's trade-note writer exists but fires at `/size` (sizing), and only for manual cards. It is converted, not duplicated (L3).
- **Radar fills record NO price today** (`aset/web.py:1181-1209`). The ladder's "fill via the existing fill-recompute" is not wired for radar cards.
- ESCALATE: 6. Build ≈ 35 h of seats, ≈ 50 h with one fix round per chunk.

## Fact table — UNPROVEN rows
| # | Claim | Why UNPROVEN |
|---|---|---|
| F25 | His daily dataview table lights for a Cobalt-created note by `file.cday` | text read only; Obsidian not run |
| F30 | The final file sets of `setups/seven-0921` and `s2/stale-marker-0921` | neither branch exists locally tonight |
| F32 | Reading "single fill at MVP" as one entry fill with many exit legs | Charter §5 #16 vs F11 text; a reading, not a ruling |
| F33 | Source of "drift scaled to ATR (his 09-03 defect)" | no text in the ladder, BACKLOG or LEDGER (grep ATR/drift) |

READING:
- `6 - Permanent/Memory/LAWS.md` (in full, L1–L74)
- `SPRINT-LADDER-v0_1.md` `:460-667` (S2 status 09-21, owed-before-S3, `## S3`)
- `MVP-CHARTER-v0_2.md` F11 `:135-147`, F22 `:205-207`, §5 `:224-261`, §7 `:279-294`, §12 `:371-380`
- mock `card-spec.md`, `decisions.md`, `open-questions.md`; ADR-0008 (grep), ADR-0009 (grep)
- `cards/models.py`, `cards/store.py` `:222-740`, `:847-1233` (grep), `cards/expire.py:1-70`, `cards/migrations/0002`
- `aset/web.py` `:625-700`, `:995-1140`, `:1181-1240`, `:1290-1345`; `aset/engine.py` `:36-45`, `:260-312`; `aset/store.py:180-260`; `aset/radar_panel.py:930-1005`
- `prefill/trade_note.py` (full), `prefill/drc.py:95-135`, `configs/cobalt/prefill.yaml`, `configs/dev/aset.yaml`
- `vaultwrite/writer.py` (defs, `:644-680`); `notify/mattermost.py:1-30`; `jobs/killswitch.py:100-125`; `daymode/store.py`, `daymode/match.py`
- `db_migrations/0007_radar_cards.sql`, `placement.py:100-115`; `replay/cards.py:223-288`, `replay/models.py:185-225`; `radar/evaluate.py` (grep ATR, last_price, `:780-800`)
- `git log main..bars/chunk-2-0920`, `git branch --list`, prompt `65-setups-one-build.md` (grep), `STALE-SCORE-PROPOSAL-2026-09-21.md` (grep)
- vault: `5 - Templates/Individual Trade Template.md`, `5 - Templates/Daily.md:49-54`, `1 - Trading/2 - Trades/` listing + one note's frontmatter keys (no content copied)

## ESCALATE
1. **Radar fills carry no price today.** `/card/{id}/move` → `fill()` records only `{"via":"aset.sheet"}` (`aset/web.py:1198-1209`). `/fill` needs the manual `/size` form (`:1063-1095`). Any radar fill during live mornings 1–3 (Mon–Wed) records no price or shares. The ladder already says legs are hand-logged in the DRC chat until S3; the fill price should be hand-logged there too.
2. **Drift threshold conflict.** The code warns at ≥ 25 through a HARD-CODED constant (`aset/engine.py:43`, not config). Charter and mock say > 20. The acceptance test says 27. The value is his (owner O2), and the constant dies in C1.
3. **"ATR scaling (his 09-03 defect)" has no source text** (F33). The ATR term in the proposal §4 is ASSUMED, and K is owner O3.
4. **The DRC prefill will miss radar trade notes.** It matches by nearest filename time to the card's `created_at` (`prefill/drc.py:101-121`). A radar card forms early and fills later. The proposal stores `trade_note_path` on the card. This is an F14 seam.
5. **His daily dataview table selects `strategy`, but new notes carry `trade_def`** (`Daily.md:50` vs `trade_note.py:30-41`). The column is blank for every new note. It is his template, so it is flagged, not touched.
6. **Charter §5 #16 ("single fill at MVP, partials post-MVP") vs F11 scale-out legs.** The proposal reads it as one entry fill and many exit legs (F32). The tribunal should state this reading.

## CONTINUE
Done. Next is the desk's: launch the four-house tribunal (L67) on the proposal, and bring O1–O8 to him in one message.

## DIGEST FOR THE DESK
**What is proposed, in plain words.** A radar card goes from TRIGGERED to FILLED when he taps "FILLED @ price, shares" on the panel. The price is prefilled from the last poll and editable. The fill writes a `legs` row (entry) in the same transaction as the FILLED transition, through the SAME `fill()` + `mark_filled` + `compute_fill_recompute` the manual sheet uses (one path; a `SizingResult.from_card` replaces the form rebuild). Mid-trade ½ · ⅓ · flat · typed taps write exit legs off running shares. A preset tap takes the last-poll price flagged `estimated` (no keystroke). The closing price is his, `confirmed` on a ✓. Running shares at 0 closes the card in the same transaction. Realized R is a pure function over the legs and is `provisional` while any leg is estimated. Corrections are new rows, never updates. The drift warning keeps today's pct formula, adds an ATR term from the stored `atr_working`, and fires on both. Both thresholds are HIS settings; a missing setting refuses loudly. Stop override (R38): his stop is the live `stop` (already true), Cobalt's `structural_stop` is always shown beside it, and ↺ reset is a stop edit marked `reset`. Every leg stores both stops, so the DRC reads the gap. The DM line is `TSLA filled 372.82 10` / `TSLA out 374.50 all`. It writes the same rows through a NEW resident poller, is built last, and is not needed for the panel path. Lines it cannot read, or ambiguous tickers, get a NOT RECORDED reply and nothing is written. F22: the trade note is written at FILLED, right after the DB commit, by the converted slice-2 writer. It uses his template's keys, with `entry_price` = the fill, one marker unit per leg updated in place, and human wins. Its path is stored on the card.

**What exists already.** The edge table (no new edges), `fill()`, the sheet fill-recompute, stop edits with fold-into-evidence, radar expiry incl. TRIGGERED, the soft attestation on card creation, `day_modes.attested_sheet`, the vaultwrite writer, the slice-2 trade-note writer (at `/size`, manual only), both ATRs in receipts, and F12's R formula. MISSING: any radar fill price (ESCALATE 1), any panel fill/leg/stop control, any inbound DM path, `legs`.

**Chunks + hours.** C1 legs/fill/drift/migration 7 h → C2 exits/CLOSED/realized R 5 h → then in parallel C3 panel 7 h ∥ C4 trade note 5 h ∥ C5 DM resident 8 h → C6 smoke/DevDocs/ADR 3 h. 5 write-path chunks (Opus 5 floor), 2 migrations (numbers after 0012/0013). Build-seat total 35 h, ≈ 50 h with a fix round each. RESTARTS guess: aset + radar in the pause; C5 bootstraps a new resident. Cut after the setups one-build and stale-score land; re-decide neither.

**What is HIS (O1–O8, each A/B).** ⅓ rounding · the drift pct (20 everywhere vs 20 radar / 25 sheet) · the ATR floor K (none until he names it) · manual notes at sizing vs only at FILLED · Cobalt fills exit_price / times / P&L while blank, or never · `trade_def` from the card while blank, or never · radar fill before S4 as two taps vs one · DM in S3 or after.

**What the tribunal must settle (12).** The key ones: the R unit (planned, comparable with F12, vs actual) · one `legs` table and `fills` struck · append-only corrections · whether `aset_sizings.actual_fill` stays a cache · record vs refuse on an attestation mismatch at fill · the reading of "27 % past plan" · DM ambiguity rule · a note leg edit is an override only, no reverse parse · synchronous note write · the TRIGGERED expiry cover · the ↺ target · DM poll vs websocket.

**L52:** reaches scoring/ranking/admission: NO. It reaches the card's display only, so it goes through the L67 tribunal anyway.

S3 EXITS PROPOSED · chunks: 6 · write-path chunks: 5 · migrations: 2 · inbound DM path exists: no · trade-note writer exists: partial · reaches scoring: no · build estimate: 50 h · open to the tribunal: 12 · owner items: 8 · ESCALATE: 6
