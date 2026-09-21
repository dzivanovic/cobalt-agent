# Stale score — design proposal report (2026-09-21)

Seat: proposer `stale-score-design-0921` · Opus 5 · read-only · started 17:33 ET, done 17:39 ET (`date`).
Proposal: `docs/30 - Design/STALE-SCORE-PROPOSAL-2026-09-21.md` (187 lines). This is the input to the four-house tribunal (L52 / L67), not the design.

## §0 Headline
- A card's score CAN be computed on stale input: PROVEN path. Arm, form and expire CANNOT act on stale input; expiry can only be LATE. WATCH can be REORDERED by a stale score.
- The problem is larger than "all computed dots tapped". Every live note except Rubberband has no computed dot, so one tap scores on a stale `last`. With no bar at all today, proximity falls back to the MAXIMUM, 1.0 (`evaluate.py:776`).
- Options: 4 (A1/A2, B, C, D). Recommended: **C** — proximity is UNKNOWN (NULL) while bars are stale. It uses the null-proximity branch every score path already has; no migration.
- Clock: the evaluator's `2 × radar.scan_interval` (replayable from the receipt). No number changed (L53).
- 2 chunks · Opus 5 (store.py writers) · build after C1 lands, before the first `A-01` ruling · ESCALATE: 4

## Fact table (condensed; the full table is proposal §1)

| Claim | file:line | |
|---|---|---|
| Staleness is known at evaluation (`intraday_stale`, 2 × scan_interval) and stops formation | `radar/evaluate.py:529-534,598`; `anatomy/freshness.py:106-120` | PROVEN |
| `evaluation="input_stale"` also means "daily bars missing". A guard must not key on it | `evaluate.py:599,624,629` | PROVEN |
| Every open card is refreshed with no state guard; proximity comes from the old close; no bar → `card.entry` → proximity 1.0 | `evaluate.py:1317-1349,776-778`; `scoring.py:254-261` | PROVEN |
| The stale price is written as `last` | `evaluate.py:803`; `store.py:1032,1040` | PROVEN |
| Suppression only while an N/A computed dot is untapped | `scoring.py:247-251` | PROVEN |
| `tap_dot` rescores from the stored proximity; `prox None → score None` is already handled | `store.py:1215-1225` | PROVEN |
| Taps-moved branch leaves a tap-computed score beside a newly written proximity | `store.py:1029-1037` | PROVEN |
| `htf_level_proximity` is graded from the stale `last` with no stale flag | `evaluate.py:463-477` | PROVEN |
| Only `Rubberband.md` names computed factors | grep of `Vault/Think/1 - Trading` | PROVEN (grep scope) |
| ARM is his act; the radar code has no `→ARMED` writer | grep; `store.py:496-505` | PROVEN |
| Expiry never fires falsely on stale input (stop and avoid can be late; deadline is the wall clock) | `evaluate.py:598,626,1340-1344`; `expire.py:287-310` | PROVEN |
| WATCH ordered by `card_score` → reorder on a stale score | `cards/radar.py:167-183`; ADR-0009:28 | PROVEN |
| Proximity and score columns are nullable; the panel renders `—` and the reason | `0007:47-48`; `0006:103-106`; `radar_panel.py:877-883,957` | PROVEN |
| Replay and audit export recompute from receipt values and refuse a mismatch; the receipt has no `poll_failures` | `evaluate.py:1043-1089`; `audit_export.py:244-259`; grep = 0 | PROVEN |
| Production occurrence | — | UNPROVEN (X9) |

## READING:
- `Vault/Think/6 - Permanent/Memory/LAWS.md` in full (1–405)
- `src/cobalt/radar/evaluate.py`: 1–150, 340–364, 425–634, 700–829, 1029–1128, 1190–1234, 1260–1497
- `src/cobalt/cards/scoring.py` (whole)
- `src/cobalt/cards/store.py`: 494–505, 1016–1075, 1145–1254 + a def/grep map
- `src/cobalt/cards/expire.py` `radar_expiry`
- `cards/radar.py` (grep)
- `radar/audit_export.py`: 225–264 + grep
- `replay/cards.py` (grep)
- `radar/anatomy/freshness.py`: 106–120
- `radar/poller.py`: 100–131
- `radar/store.py` `stamp_poll`
- `aset/radar_panel.py` (grep, `_field`)
- `aset/web.py` (grep ARMED)
- `db_migrations/0006` 95–109 and `0007` (grep)
- `tunables.yaml` (grep)
- ADR-0009 (grep D4)
- `Vault/Think/1 - Trading` (grep: computed factors)
- `Rubberband.md` (grep)
- `reports/stale-marker-design-2026-09-21.md` (whole)
- `30 - Design/STALE-MARKER-PROPOSAL-2026-09-21.md` (whole)
- `reports/setups-c1-draft-2026-09-21.md` (whole)
- `reports/setups-tribunal-r2-2026-09-21.md` 605–617 + grep
- `reports/setups-tribunal-fable-r2-2026-09-21.md` (grep R2-2.1)
- `reports/cto-2026-09-21.md` R36, R39–R42, log lines 339, 342, 351
- NOT read: the tests for each module. Test coverage is named in proposal §7 as experiments, not claimed.
- NOT read: `SETUPS-AT-DEFAULTS-FINAL` beyond what the C1 draft quotes.

## ESCALATE
1. **No bar today → proximity 1.0, the maximum** (`evaluate.py:776`, replay `:1079`). A card whose member has no closed bar today gets the maximum proximity. Once tapped, it scores at its conviction ceiling and tops WATCH. The path is PROVEN; the occurrence is UNPROVEN (L70). Proposal C deletes the fallback (X5).
2. **The defect is wider than "all computed dots tapped".** Every live note except Rubberband has no computed dot (grep), so ONE tap scores on a stale `last`. After C1 every new formation is score-null for life (C1 E5), so the defect is DORMANT for new cards from C1 until his first `A-01` ruling. It is LIVE today and on cards opened before C1. Timing is the desk's lane call; C must be live before the `A-01` ruling.
3. **L7 data: `htf_level_proximity` is graded from a stale price with no stale flag** (`evaluate.py:463-477`). A tap records that `engine_grade_at_tap` (`store.py:1209`), which feeds `shadow_agreement_v` (`0007:255`). Whether any row exists is UNPROVEN. Whether past rows are excluded from the agreement stats is his, via tribunal Q7.
4. **An existing one-scan inconsistency, independent of staleness:** a refresh after a racing tap writes the new proximity and keeps the tap route's score, which was computed on the old proximity (`store.py:1029-1037`). C closes it for the stale case only. The fresh case stays a separate item.

L74: no instruction block was observed inside a tool result this run. This seat committed nothing and sent nothing.

MEMORY: [stated 2026-09-21 · stale-score proposer] `evaluation="input_stale"` has two meanings: intraday bars stale (`evaluate.py:599`) and daily bars missing (`:624`, `:629`). Any guard on "bars are stale" must key on the intraday flag, never on the evaluation label.

## CONTINUE
None. The run is complete. The next steps belong to the desk:
- L35 on the two files.
- Lane call: tribunal packet from the proposal; four houses ≤3 rounds.
- Sequencing against C1: build after C1 lands, before the first `A-01` ruling.
- X9 (occurrence count) is hub-run, on production read-only.

## DIGEST FOR THE DESK
- **True size, in his terms:**
  - While a ticker's bars are stale, its card can show a score computed on an old price, and WATCH ranks by that score.
  - Cobalt cannot arm, create or wrongly expire a card on stale bars. An expiry on stop or avoid can only come late.
  - For every setup except Rubberband, one tap is enough to get the stale score.
  - If a ticker has no bar at all today, its proximity reads MAXIMUM (1.0).
- **When it bites:** live today. After C1, new cards have no score for life until he rules `A-01`, so it sleeps. It wakes at that ruling.
- **Options, one line each:**
  - A1: store "suppressed" on the card. Dies on his next tap. Rejected.
  - A2: an untappable "bars fresh" dot on every card. It works, but it is a second carrier, puts a new dot on every card, and still shows a stale proximity.
  - B: freeze the card until fresh. Shows old numbers as live and fails L1. Stop-gap only.
  - **C (recommended):** proximity = unknown while stale. Score `—`, with the reason "bars stale — last bar HH:MM". His conviction and key are still shown, and the score returns by itself on the next fresh scan.
  - D: C plus blanking `last`. Loses the real last print the STALE stamp marks.
- **Why C:**
  - It uses the null-proximity branch that the tap, refresh and replay paths already handle (L3). That is also why C1's untappable dot is not reused: staleness LIFTS, and an assumed value does not.
  - No migration.
  - Replayable from the existing receipt (L57).
  - L52 (a)–(d) all answered (proposal §3).
- **Clock:** the evaluator's (2 × scan_interval = 200 s, bar time, every session). No new number. The STALE stamp keeps the poller's 180 s RTH clock.
- **Build:** 2 chunks (pure + store writers). Opus 5 floor (`tap_dot` / `refresh_radar_card` write a user table). No migration.
- **RESTARTS:** radar + aset (GUESS by import rule; radar inside 20:00–21:00, L43/L66).
- **Sequencing:** off main AFTER C1 (same functions). Ride C1's version bump only in a stacked deploy. Must not wait for C2.
- **Evenings to live:** GUESS THU 09-24 at the earliest.
- **HIS (through the tribunal, not now):**
  - Q1: should a stale card sink below scored cards (reorder) or hold its slot?
  - Q2: premarket nulls under the every-session clock.
  - Q7: exclude stale-graded `htf_level_proximity` taps from the L7 agreement stats.
  - None of these blocks the tribunal starting.

STALE SCORE PROPOSED · can score on stale input: yes · can arm, expire or reorder on stale input: yes · options: 4 · recommended: C — proximity unknown while bars stale · migration: no · chunks: 2 · open to the tribunal: 10 · ESCALATE: 4
