# STALE SCORE — proposal (2026-09-21)

Proposer seat `stale-score-design-0921` (Opus 5), read-only, from `prompts/2026-09-21/59-propose-stale-score.md`. This is the INPUT to the four-house tribunal (L52 / L67). It is not the design.
Ladder: `S2-P2 · F10 Dots / ladder` (a defect in what is live). Origin: `reports/stale-marker-design-2026-09-21.md` ESCALATE 1; `reports/setups-tribunal-r2-2026-09-21.md` ESCALATE 3.
All `file:line` refs are on MAIN at `031196f`. The prompt's `cards/evaluate.py` is `src/cobalt/radar/evaluate.py` (same line numbers). PROVEN = read in the file. UNPROVEN = not checkable from reads (L70).

## 1. Fact base

### 1a. Every writer of `last`, `proximity`, `card_score`, a dot, or the ladder order

| # | Claim | file:line | |
|---|---|---|---|
| W1 | **Staleness is known at evaluation.** `intraday_stale` = no closed i1 bar today, OR the last bar's close older than `2 × radar.scan_interval` (ttl 200 s at 100) | `radar/evaluate.py:529-534`; `anatomy/freshness.py:106-120`; `tunables.yaml:467-468` | PROVEN |
| W2 | It is used three ways: no formation (`input_stale` return), stale flag on `atrs_from_open` and `Extension.leg_count` | `evaluate.py:598-599`, `:439`, `:459` | PROVEN |
| W3 | It is NOT stored as its own field on `MemberEvaluation`. `evaluation="input_stale"` has two meanings: intraday-stale (`:599`) or daily bars missing (`:624`, `:629`) | `evaluate.py:340-364`, `:599`, `:624`, `:629` | PROVEN |
| W4 | `htf_level_proximity` is computed FROM `last_price` with NO stale flag, even when intraday-stale | `evaluate.py:463-477` | PROVEN |
| W5 | **Refresh writer (stage):** every open card whose def still loads is refreshed. There is no evaluation-state guard | `evaluate.py:1317-1349` | PROVEN |
| W6 | `refresh_card` takes `last = ev.last_price`, the last closed stored bar however old. If there is no bar today it falls back to `card.entry`, which gives **proximity = 1.000000, the maximum** | `evaluate.py:776-778`; `scoring.py:254-261` | PROVEN |
| W7 | `refresh_card` returns `last_price=ev.last_price` (stale price included) | `evaluate.py:803` | PROVEN |
| W8 | **Row writer (refresh):** `refresh_radar_card` writes `proximity`, `last_price = COALESCE(new, old)`, and (no newer tap) `conviction, card_score, score_suppressed, proposed_key`. It then upserts every dot | `cards/store.py:1016-1053` | PROVEN |
| W9 | Same writer, when a tap landed after the stage read: it writes `proximity`/`last_price` and leaves `card_score` as the tap route computed it, which uses the OLD proximity. This is a one-scan inconsistency that exists today whether the bars are stale or not | `store.py:1029-1037` | PROVEN |
| W10 | **Tap writer:** `tap_dot` recomputes conviction, `suppression(dots)` and `card_score` from the stored dots and the STORED proximity. It does not know about staleness. `prox is None → card_score None` is already handled | `store.py:1182-1231` (`:1217-1219`); `scoring.py:264-267` | PROVEN |
| W11 | **Create writer:** a card forms only on `evaluation == "formed"`, so it never forms on stale intraday bars | `evaluate.py:1361-1406`, `:598` | PROVEN |
| W12 | **Seam copy writer:** `copy_card_values` copies proximity/score to `system.radar_score`. Columns are nullable | `evaluate.py:1356-1358`, `:1431`; `0006_radar_score.sql:103-106` | PROVEN |
| W13 | `aset_sizings.proximity` / `card_score` are nullable, with no CHECK on either column | `0007_radar_cards.sql:47-48`, `:66-82` | PROVEN |
| W14 | Dots: `compute_dots` marks a stale observation `input_stale` (no grade). `refresh_dots` moves the prior grade into `history` and carries taps | `scoring.py:172-176`, `:201-235` | PROVEN |
| W15 | Suppression holds only while a computed N/A dot is UNTAPPED | `scoring.py:247-251` | PROVEN |
| W16 | **Ladder order:** WATCH by `card_score desc nulls last`, then `pool_position`. Pinned cards (ARMED/TRIGGERED/FILLED) by `pool_position`, then score. ADR-0009 D4: `card_score` alone orders WATCH | `cards/radar.py:167-183`; `evaluate.py:134-138`; ADR-0009:28 | PROVEN |
| W17 | **Replay (L57):** `replay_receipt` re-runs `evaluate_member` on receipt bars + `as_of` + `scan_interval` and re-scores with the same `last` rule. Audit export refuses a run whose recompute ≠ published | `evaluate.py:1043-1089` (`:1079`); `audit_export.py:244-259` | PROVEN |
| W18 | The nightly `com.cobalt.replay` (`replay/cards.py`) replays counterfactual R of unfilled cards. It never recomputes `card_score` | `replay/cards.py:1-57`, grep | PROVEN |
| W19 | The panel renders `None` proximity/score as `—` and prints `score_suppressed` on the card | `aset/radar_panel.py:877-883`, `:957`, `:982`, `:1026` | PROVEN |
| W20 | The receipt carries nothing from `poll_failures`. The stamp's clock cannot be replayed from a receipt | grep `poll_failures` in `evaluate.py` = 0 | PROVEN |
| W21 | Only `Rubberband.md` names a computed factor among the live notes (`atrs_from_open`, `rvol`, `Extension.leg_count`, `htf_level_proximity`, `trail_fit`) | grep of `Vault/Think/1 - Trading` | PROVEN (grep scope) |

### 1b. The sequence that produces a live score on a stale `last` today

1. S4 stores no new bar for ticker X, or X's newest bar is older than 200 s.
2. S5 `evaluate_member`: `intraday_stale = True`, `last_price` = the old close, and the function returns `input_stale` (W1, W2).
3. The stage refreshes X's open card anyway (W5). `refresh_card` computes proximity from the old close (W6).
4. The dots: the stale computed dots are `input_stale`, but any dot he has TAPPED is exempt (W15). A def with NO computed factor (every live note except Rubberband, W21) has nothing to suppress, so one tap is enough.
5. `card_score = conviction × proximity(old close) × 100` is written (W8) and orders WATCH (W16).
6. His next tap on any dot recomputes from the stored stale proximity (W10). A score suppressed by an untapped stale dot therefore comes back the moment he taps that dot. This is the r2 ESCALATE 3 mechanism.
7. If X has NO bar at all today: proximity = 1.0, the maximum (W6). Any conviction then scores at its ceiling.
8. The replay reproduces all of it exactly (W17). L57 holds as reproducibility; the replayed number is still stale.

### 1c. Can it ARM, EXPIRE or REORDER on stale input? (this sets the size of the problem)

| Act | On stale input? | Why | |
|---|---|---|---|
| ARM | **No.** | `src/cobalt/radar/` has no `→ARMED` transition (grep). Arming is his button (`aset/web.py:640-655`), and the COBALT-actor hops at `store.py:496-505` run only inside his one-click fill. He may arm off a stale score, but that is his act | PROVEN (grep `ARMED`) |
| FORM | **No.** | W11 | PROVEN |
| EXPIRE: stop-before-arm | **No false expiry. Can be LATE.** | It reads real stored bars (`evaluate.py:1340-1344`, `cards/expire.py:287-299`). Stale means no new bar, so a touch is found late, never invented | PROVEN |
| EXPIRE: avoid | **No false expiry. Can be LATE.** | An intraday-stale evaluation returns before avoid is evaluated (`evaluate.py:598` vs `:626`) | PROVEN |
| EXPIRE: deadline | **Correct.** | Wall clock (`expire.py:305`) | PROVEN |
| REORDER | **Yes.** | WATCH order is `card_score` (W16). The stale score is live | PROVEN path |
| Health pills (FILLED) | **Computed on stale bars.** | `evaluate.py:780-797`. Not a score; out of scope (§5, Q5) | PROVEN |
| Shadow dot grade | **`htf_level_proximity` graded on a stale price** | W4; `engine_grade_at_tap` is recorded at tap (`store.py:1209`) and feeds `shadow_agreement_v` (`0007:255`), which is L7 data | PROVEN path · rows UNPROVEN |

**Size:** the score and the WATCH order are wrong while bars are stale. Arm, form and expire are not (expiry can only be late). Production occurrence is UNPROVEN (L70); X9 counts it. **Timing:** after C1 deploys, every new formation carries the untappable `assumed_formation` dot, so its score is null for life (`reports/setups-c1-draft-2026-09-21.md` E5). That makes the defect DORMANT for new cards from C1 until his first `A-01` ruling. Until then it is LIVE today, and for cards opened before C1.

## 2. Options

Common to all: formation, arm and expiry are untouched. The R36 STALE stamp renders beside the result and is not replaced. No number changes.

### (A) A card-level suppression recorded when bars are stale, lifted when they are fresh
- **A1: a stored string.** The refresh writes `card_score NULL` plus a reason. **Fails:** `tap_dot` recomputes `suppression(dots)` and the score from the stored (stale) proximity, and overwrites both (W10). This is the "stored string dies on the first tap" of Fable R2-2.1. REJECTED.
- **A2: C1's carrier, a synthetic untappable `bars_fresh` dot.** It is recomputed on every refresh from W1, is `input_stale` while stale, and is refused in `tap_dot`.
  - **Does C1's path fit?** Half of it. The *untappable* half fits: the tap path reads stored dots, so `suppression()` holds (C1's path 1).
  - The *carry-from-own-row* half does NOT fit. C1's dot is static and never lifts (`setups-c1-draft` five-path table, path 2: "re-appends from the card's OWN stored dot"). A freshness dot must be RE-DERIVED every scan, so paths 2, 3 and 5 need new code in a different shape.
  - It also puts a dot that is not a quality factor on EVERY card. That is visible, it shifts positions, it lands in `published_numbers` dot lists and it enters the tap-refusal surface. Meanwhile proximity is still computed from the stale price and shown as a number.
  - Files: `scoring.py`, `evaluate.py` (3 sites + replay), `store.py` `tap_dot`, `audit_export.py`.
  - **He sees:** an extra `bars n/a STALE` dot, score `—`, and a proximity number that is stale.
  - **Stored:** a dot row per card. **Replay:** recomputes the dot from the receipt.
  - **Cost:** M. Two recompute carriers exist for one fact (L3 concern).

### (B) Freeze the card whole while stale
- **Mechanism:** skip `refresh_card` / `refresh_radar_card` when `intraday_stale`. Expiry still runs. Files: `evaluate.py` (one guard) and replay (no card entry for that scan).
- **He sees:** the last FRESH score, proximity and `last`, shown as current. The only sign of age is the R36 stamp, which runs on the poller's clock (180 s, RTH only).
- **Stored:** nothing new. The row keeps its older values.
- **Fails L1:** an old number shown live is plausible-wrong. A tap during the freeze recomputes from the frozen proximity (W10) and publishes a score for a price that is minutes old. The WATCH order keeps ranking by it.
- **Cost:** XS. **Rejected as a design;** usable only as a stop-gap.

### (C) Proximity is UNKNOWN while stale. The score follows it, and every other value stays computed and marked — RECOMMENDED
- **Mechanism.** One rule: **no fresh last → no proximity**.
  1. `MemberEvaluation.intraday_stale: bool`, set from the W1 value that already exists. It is not keyed on `evaluation`, because of W3.
  2. `score_card(..., last: Decimal | None)`: `last is None → proximity None`. `card_score(conv, None, …) → None` already holds (`scoring.py:265`).
  3. `refresh_card` and `replay_receipt` pass `last=None` when `ev.intraday_stale` (which covers no bar today) through ONE shared helper. The `card.entry` fallback (W6) is deleted.
  4. `score_suppressed` = `bars stale — last bar <HH:MM:SS ET>, older than 2 × radar.scan_interval` (plus any dot reasons). Conviction, proposed key and dots are computed as today; he still sees what his taps say.
  5. `htf_level_proximity` gets `stale=intraday_stale` (W4). It is a function of `last`.
  6. `CardUpdate.proximity` and `CardScore.proximity` become Optional. `published_numbers` writes `null`.
  7. `store.tap_dot`: `prox is None` already gives score `None` (W10). The change keeps the stale reason when `prox is None` (constant `PROXIMITY_UNKNOWN`), so a tap cannot erase it.
  8. `store.refresh_radar_card` taps-moved branch: when `proximity IS NULL`, also null `card_score` and set the reason (closes W9 for this case).
- **Lifts by itself:** the first refresh with a fresh bar recomputes proximity, and the score returns with no tap (W8).
- **Files:** `radar/evaluate.py`, `cards/scoring.py`, `cards/store.py` (2 writers), `radar/audit_export.py` (signature only; formation is never stale), `replay/formations.py` if the version is bumped (C1 E3 lesson), tests, DevDocs.
- **He sees:**
  - Score chip `—`.
  - `score suppressed: bars stale — last bar 10:42:00 ET …` (W19).
  - Proximity `—`. His conviction and proposed key as before.
  - `last` = the real last print, with the R36 STALE stamp beside it when the poller agrees.
  - The WATCH card sinks below scored cards (nulls last) at the next reload or card action. The ladder is not re-sorted on the periodic refresh (`STALE-MARKER-PROPOSAL` F15).
- **Stored (L57):** `proximity NULL`, `card_score NULL`, `score_suppressed` text, and `radar_score_id` → the seam row `evaluation=input_stale`. The receipt already holds the bars, `as_of` and `scan_interval` from which staleness is recomputed (W17, W20). No new column.
- **Replay:** `evaluate_member` recomputes `intraday_stale` from receipt values, and `replay_receipt` takes the same helper, so recompute = published. Pre-change receipts that published a stale score would now mismatch, so the change bumps `EVALUATOR_VERSION` (or rides C1's), and replay refuses other versions (C1 gate 5).
- **C1's path:** C makes no new carrier and does not compete with the untappable dot. It uses the existing null-proximity branch, which all five of C1's paths already pass through: tap `store.py:1217`, refresh `scoring.py:265`, `refresh_dots` (untouched), audit export (formation only), replay (same helper). **L3: one path for "an input of the score is unknown" = proximity NULL.**
- **Cost:** S logic (~40-60 lines) + M tests.

### (D) Variant of C: null `last` too
Write `last_price NULL` while stale. **Loses the real last print** that the R36 stamp marks, and `COALESCE` would need changing. Not recommended (Q4).

## 3. Recommendation: (C)

| L52 | Answer for (C) |
|---|---|
| (a) | Every number is traceable. Proximity uses a `last` only when its bar is fresh by the rule the receipt replays. A stale input degrades the score to null with the reason, never to a modelled value |
| (b) | ONE authority, unchanged: `card_score` orders WATCH. The stale card holds `null` and falls to the existing tie policy. No second authority is added. `pool_position` as tie-break is the open r2 ESCALATE 2 (Q9) |
| (c) | The seam is real artifacts: `MemberEvaluation.intraday_stale` · `score_card(last=None)` · `aset_sizings.proximity NULL` (nullable, W13) · `tap_dot` `prox is None` branch (W10) · receipt `as_of` + bars (W17) |
| (d) | Auditable by another house: `cobalt radar audit-export` replays the receipt and refuses any mismatch (W17). The staleness is a pure function of receipt values |

## 4. Which clock

**The evaluator's clock:** last closed i1 bar older than `2 × radar.scan_interval`, by bar time, every session (W1). Why:
1. It is the clock that already decides whether this card may form on these bars (W2) and already marks its dots stale. One definition of "stale input" per card (L3).
2. It can be replayed from the receipt; the poller's `poll_failures` cannot (W20, L57).
3. The banner clock is per scan, not per ticker.

The stamp keeps the poller's clock. It is a RENDERING and is not changed.

**L53:** No number is proposed, changed or added. The score obeys the existing `2 × radar.scan_interval` rule (Astra R1-12). `radar.scan_interval` (100) and `radar.poll_bar_max_age_s` (180) stay his. Whether the score should follow a different clock is his (Q2, Q3).

## 5. Deliberately NOT changed

- The R36 stamp, `poll_failures` and `stamp_poll`. The design does not depend on the stamp, so the carried S4-over-S3 overwrite (`radar/store.py:269-273`) does not touch it.
- Formation, arm, the expiry order and causes, and the key tap.
- `ladder_order` / `TIE_POLICY` text, conviction, the proposed key, the curves and every threshold.
- C1's `assumed_formation` dot.
- Health pills on FILLED cards (Q5).
- Daily-stale `input_stale`, which does not touch `last` (Q10).
- The W9 race when the bars are fresh (a separate item).
- The panel, which already renders `—` and the reason (W19).
- His hand grades. Taps during staleness are ACCEPTED and kept.

## 6. Chunks, seats, migration, restarts, evenings

| Chunk | Scope | Seat (L29) |
|---|---|---|
| S1 | Pure: `intraday_stale` field, `score_card(last=None)`, the shared helper in `refresh_card` + `replay_receipt`, `htf_level_proximity` stale flag, Optional proximity, `published_numbers`, version bump + `replay/formations.py` set, offline tests (X1, X5, X6, X7, X8 pure) | Opus 5 (same branch as S2) |
| S2 | Writers: `store.tap_dot` reason keep, `refresh_radar_card` taps-moved null; with-DB tests on `cobalt_dev` (X2, X3, X4) | **Opus 5 floor** (user-table write path) |

- **Migration: no.** The columns are already nullable (W13).
- **RESTARTS (GUESS until `cobalt jobs restarts <range>`):**
  - `com.cobalt.radar` (imports `radar.evaluate`). The restart must fall inside 20:00–21:00 (L43), with the residents down before the merge (L66).
  - `com.cobalt.aset` (`aset/web.py:47` imports `cobalt.cards`, the same import rule as C1 E6).
  - The one-shot `com.cobalt.replay` reads the new version on its next run.
- **Sequencing:** C touches the same functions as C1 (`refresh_card`, `tap_dot`, `replay_receipt`, `compute_dots` sites). **Build it off main AFTER C1 lands.** It shares C1's version bump only if both go in one stacked deploy (L68 gate).
- **Must not wait for C2.** The defect is live today and returns at the first `A-01` ruling. C must be live no later than that ruling.
- **Evenings to live (GUESS):**
  - Tribunal: 1 to 2 evenings, 4 houses × ≤3 rounds.
  - Then build, ≥3 checkers and one deploy.
  - Earliest THU 09-24 if C1 deploys WED; FRI if the tribunal runs 3 rounds.

## 7. First-gate experiments (L70; each runnable on `cobalt_dev`, RED on main first where marked)

- **X1 (RED on main):** pure `refresh_card` with every dot tapped and a bar 201 s old gives `card_score` non-null on main. New code gives `proximity None`, `card_score None`, and a reason that names the bar time.
- **X2:** on `cobalt_dev`:
  1. Form a card and tap all its dots.
  2. Stop feeding bars and run the stage. Expect a NULL score and a NULL proximity.
  3. Tap another dot. Expect the score to stay NULL and the reason to be kept.
  4. Add a fresh bar and run the stage. Expect the score to return with no tap.
- **X3:** a tap lands between the stage read and the refresh while stale (taps-moved branch) → the row ends with a NULL score.
- **X4:** `audit-export` on a run with a stale card → recompute = published. A pre-change receipt is refused by the version, not by a mismatch.
- **X5 (RED on main):** a card whose member has zero bars today → proximity `1.000000` on main, NULL after the change.
- **X6:** `htf_level_proximity` is `input_stale` whenever `intraday_stale`.
- **X7:** `ladder_order` with one stale WATCH card → it orders after the scored WATCH cards. The pinned order is unchanged.
- **X8:** expiry is unchanged. A stale window crossing the deadline → EXPIRED `deadline`. A stored bar through the stop → EXPIRED `stop_before_arm`.
- **X9 (hub-run, L41):** count the radar cards whose `radar_score_id` seam row is `input_stale` while `card_score IS NOT NULL`. Run it on `cobalt_dev`, then by the hub on production read-only. This is the L70 occurrence proof.

## 8. Questions for the tribunal (least sure first)

1. Sink or hold? A stale WATCH card with a null score falls below the scored cards at the next reload. That is a reorder caused by staleness: the loud state wins (L1), but it moves his ladder. Should a stale card keep its last slot, marked, instead?
2. The evaluator's clock runs in every session. Thin premarket names may null most scores before 09:30. Accept, or is an RTH-only rule wanted? A new rule would be his (L53).
3. The score nulls at 200 s and the stamp shows at 180 s, RTH only. That leaves a band with a stamp and a live score, and outside RTH a null score with no stamp. Is the reason text enough, or must the two clocks meet?
4. Keep writing the stale `last` (C) or null it (D)?
5. FILLED health pills computed on stale bars: in scope here, or its own item?
6. A tap during staleness: accept it and keep the score null (proposed), or refuse the tap?
7. `htf_level_proximity` stale flag: it changes a shadow dot that feeds `shadow_agreement_v` (L7). Must earlier taps on stale-graded engine values be excluded from the agreement stats?
8. The version bump: ride C1's in a stacked deploy, or a separate bump?
9. With more null scores, more WATCH cards are ordered by `pool_position` (r2 ESCALATE 2). Does that ruling have to come first?
10. Daily-stale `input_stale` (`evaluate.py:624`): leave proximity computed (proposed), since `last` is intraday?
