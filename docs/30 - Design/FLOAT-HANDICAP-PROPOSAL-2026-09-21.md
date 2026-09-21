# Low-float / small-cap handicap: design PROPOSAL, 2026-09-21

Proposing house: Anthropic (Opus 5). Seat `float-handicap-design-0921`. Ruling: `docs/40 - DevDocs/reports/cto-2026-09-21.md` §4 R28, cited and not quoted with numbers. Ladder: OFF-LADDER. It touches `S2 · F2` pool rank, `F3` focus rank and `F10` score.

This file is the input to a four-house tribunal (L67, L52). Nothing is built from it. It contains none of his values. His thresholds and the penalty appear only as KEYS under his pool block (`handicap.*`, §3 and §5). Every claim carries `file:line`. Paths are relative to `~/cobalt`.

---

## 0. The fact base, in brief

| # | Fact | Evidence |
|---|---|---|
| F1 | Pool rank does not come from one score. It is a lexicographic key: (priority group, `first_from` flag, **position of the name inside the source that ranks it best**, note order, ticker). The position is the name's place in one screen, sorted by that screen's metric (volume or rvol). The key compares positions ACROSS screens, never metric values. | `src/cobalt/radar/pool.py:94-106`, `:131-209` (the tuple at `:209`) |
| F2 | The 50 are `ordered[:cap − held]`, adjusted by stickiness (`below_cap_streak` against `stickiness_scans`). A name that loses its seat gets `EXCLUDE` or `LEAVE` with `excluded_by = config_cap`. | `pool.py:332-334`, `:349-378`, `:393-398` |
| F3 | When the pool is ranked, each candidate carries only `{volume, rvol}` per source, plus the `not_equity` verdict. Float and market cap are **not parsed**. | `src/cobalt/radar/runner.py:139-145`; `SourceSet.metrics` at `src/cobalt/radar/models.py:184` |
| F4 | Screens and lists are both fetched with the same full export, columns `0-150` (`c=`). **Every source's CSV therefore carries `Market Cap` and `Shares Float`**, but neither is in `required_headers`. | `src/cobalt/radar/collector.py:158-162`, `:199-208`; `configs/cobalt/radar.yaml:18-24` |
| F5 | Units, verified on the real-shape fixture: `Market Cap` is in **$ millions** and `Shares Float` is in **millions of shares**. Row `AA` has `Market Cap 12659.74`, `Shares Outstanding 263.91`, `Shares Float 262.49`, `Price 47.97`, and 263.91 × 47.97 = 12,659.8. | `tests/fixtures/radar/pool-metrics.real-shape.csv:1` (header), `:2` |
| F6 | Some real equity rows are blank. In the real-shape fixtures, 4 non-fund rows have a blank float (1 in gainers, 3 in losers) and 1 also has a blank cap. In the retained production cache, equity (source, ticker) pairs with a blank float / blank cap were 3/1 of 409 on 2026-09-18 and 4/2 of 383 on 2026-09-21, from both screens and lists. **So the data is present for almost every candidate, but not every one.** | `tests/fixtures/replay/movers-gainers.real-shape.csv`, `movers-losers.real-shape.csv`; `data/radar-cache/2026-09-18/`, `2026-09-21/` (read 2026-09-21) |
| F7 | The raw CSVs are kept for **7 days** only. No DB row stores float or cap. | `configs/cobalt/radar.yaml:30-32`; `src/cobalt/db_migrations/0004_radar_pool.sql:29-51` |
| F8 | The S5 receipt stores `pool_unit`, which holds the pool block and every `SourceSet`, including `metrics`. Once float and cap are in `metrics`, they are stored inputs (L57) at no extra cost. | `runner.py:319-323`; `src/cobalt/radar/evaluate.py:920-921` |
| F9 | `card_score = round(conviction × proximity × 100)` is documented as THE one ranking authority on the card. Conviction is the mean of HIS taps only. An untapped card has no score. | `src/cobalt/cards/scoring.py:1-4`, `:27-28`, `:238-244`, `:264-267`; ADR-0009 D4 (`docs/10 - Decisions/ADR-0009-…md:28`) |
| F10 | A card is born with no taps, so `card_score` is null at creation. It becomes a number only when he taps, through `store.py:1219`, or on refresh through `evaluate.py:777`. | `evaluate.py:1383-1395`; `src/cobalt/cards/store.py:1185-1227` |
| F11 | The ladder sorts WATCH cards by (`card_score` desc NULLS LAST, **`pool_position`**, ticker). It sorts PINNED cards by (**`pool_position`**, score). `pool_position` is `radar_membership.last_rank`. **Before any tap, the ladder order IS the pool rank.** | `src/cobalt/cards/radar.py:23-33`, `:174-183`; `src/cobalt/db_migrations/0007_radar_cards.sql:227`; `evaluate.py:1225` |
| F12 | F3 focus (`FOCUS_TOP_N = 4`) ranks open cards by `card_score` only. | `src/cobalt/cards/picks.py:59`, `:226-233` |
| F13 | No scored dot reads float today. No computer exists for it (`FACTOR_COMPUTERS` = atrs_from_open, rvol, leg_count, htf_level_proximity). One strategy note carries a HUMAN short-interest-of-float dot, which is hollow and counts only when tapped. F10's charter lists "float" among possible screener-field dots. | `evaluate.py:429`; `scoring.py:163-165`; `docs/00 - Project/SPRINT-LADDER-v0_1.md:453` |
| F14 | The pool block is strict (`extra="forbid"`). An unknown key makes the note fail to parse, so `pool_error` is set and the pool FREEZES, loudly. | `models.py:99-107`; `src/cobalt/radar/notes.py:107-109`, `:408-415`, `:64-65` |
| F15 | `excluded_by` is CHECK-constrained in two tables and one Python set. The miss line counts by it. | `0004_radar_pool.sql:42-43`; `0009_picks_missed.sql:76`; `src/cobalt/replay/models.py:30-34`; `src/cobalt/replay/movers.py:102`; `src/cobalt/replay/line.py:97` |
| F16 | The `/radar` pool view orders its rows by `last_rank`. The card face shows score, conviction, proximity and pool under owner badges. | `src/cobalt/aset/radar_panel.py:542-544`, `:998`; `cards/radar.py:51-68` |

What "score" and "rank" mean at each surface he named:

| Surface | Number that orders it today | Where |
|---|---|---|
| Pool membership (the 50) | lexicographic key with within-source **position** (F1) | `pool.py:209` |
| Ladder, untapped WATCH cards (the morning case) | `pool_position` = `last_rank` | `cards/radar.py:181-182` |
| Ladder, tapped WATCH cards | `card_score` | `cards/radar.py:181` |
| Ladder, pinned cards | `pool_position`, then score | `cards/radar.py:176-177` |
| F3 focus (top 4) | `card_score` rank | `picks.py:226-233` |
| Card dots / proposed key | conviction bands. **Not a rank, and not touched here.** | `scoring.py:273-286` |

---

## 1. WHERE THE PENALTY ENTERS

**Proposal (option c): ONE handicap factor `h`, computed ONCE per ticker per scan in the pool stage and stored on the membership row. It is consumed read-only at the two numbers that order things: the pool position (it enters the pool key) and `card_score` (it multiplies it).**

| Option | What he gets | Cost | Verdict |
|---|---|---|---|
| (a) pool rank only | The 50 move. Untapped ladder order moves, because it IS the pool rank (F11). Tapped cards and F3 focus do NOT move. | M, one migration | Rejected as the full design. The ONE ranking authority (`card_score`, F9) would not carry the handicap, so from his first tap the card would be ordered by an unhandicapped number while its secondary key is handicapped. That is two authorities disagreeing (L52 b). |
| (b) `card_score` only | Nothing moves until he taps (F10). The pool's 50 are unchanged. | S–M | Rejected. It misses his first requirement ("still within the top 50"). At first render every card is untapped, so the ladder would not change either. |
| **(c) one `h`, both places** | The 50 **and** the whole ladder (untapped through `pool_position`, tapped through `card_score`) **and** F3 focus (it reads `card_score`) | Three chunks, ~M each (§9) | **Proposed.** It is one computation. The pool position and the card score are its two consumers, and `h` is never recomputed at the second (L3). |

**Why `h` must enter the POSITION and not the metric value.** Pool rank compares positions across screens (F1). Multiplying a name's volume or rvol by `h` only reorders that name inside its own screen. If every name in a screen is in the group, which is the case for the morning low-float screen by construction, a metric multiplier changes **nothing**: the relative order is identical, so the positions are identical. The handicap must act on the cross-source comparable, which is the position.

Mechanism at the pool: `effective_position = position ÷ h`. This replaces `position` in the key tuple at `pool.py:209` for screen-group names, and the union position for list-group names (`pool.py:179-206`). The priority group (`screens` before `lists`, his pool block) is untouched. `rank_value` stays the raw metric (F-S2-P4 R1, `pool.py:50-55`). The penalty is not hidden inside the metric.

Mechanism at the card: `card_score = round(conviction × proximity × h × 100)`, rounded ONCE (`scoring.py:39-41`). Conviction, proximity, dots and `proposed_key` are **unchanged**. His taps stay his grades, and the key he is offered and the size come from conviction alone (`scoring.py:273-286`). Only the ORDER changes.

**Proof that nothing else re-ranks around it (L52 b).** Every consumer of an order, checked:

| Consumer | Reads | After the change |
|---|---|---|
| Pool 50 + stickiness | key with `effective_position`; `ranks` | carries `h` (`pool.py:326`, `:349-378`) |
| `/radar` pool view | `last_rank` | carries `h` (`radar_panel.py:542-544`) |
| Ladder, WATCH + pinned | `card_score`, `pool_position` (= `last_rank`) | both carry the same `h` |
| F3 focus | `card_score` | carries `h` |
| Poller | `rank`, polling ORDER only (every member is polled) | carries `h`. It orders polling and never reaches the card (`src/cobalt/radar/poller.py:84`). |
| Proposed key / sizing | conviction | **untouched by design** |

`card_score` stays the ONE authority. `pool_position` is the admission number and the ladder's existing secondary key. Both are handicapped by the same stored `h`, so neither can re-rank around the other. (See ESCALATE 1 in the report: ADR-0009 D4 says `last_rank` "only admits", but `ladder_order` already uses it as a sort key. That is a pre-existing discrepancy, surfaced and not fixed here.)

---

## 2. THE SHAPE

**Flat multiplier `h = handicap.factor` (0 < h ≤ 1) for the whole group. ASSUMED by key. One value serves both consumers.**

- Pool: position ÷ h. Card: score × h. "A handicapped name counts h as much" reads the same at both.
- Flat, not graded. A graded shape (h rising from a floor at tiny float to 1 at the threshold) needs two more values of his and is harder to explain aloud. It is listed as an alternative (Open 2).
- A rank offset (+N positions) was rejected. It has no meaning on `card_score`, so it would need a second mechanism and a second value (L3).
- A point deduction on `card_score` was rejected. It has no meaning on a position.

**Worked example on the real stored SHAPE** (`data/radar-cache/2026-09-18/`, an RTH scan). Four screens were active, carrying 11 / 9 / 15 / 24 equity names. Every name of the low-float morning screen is in the group by construction. A minority of the others are. Screens sort ahead of lists (his priority), and interleave by position, so about four names are admitted per position level until the small screens run out. With his `cap`, the cut-off lands at some position `c` (on this scan, around the low-float screen's last name).

- A handicapped name at within-screen position `p` competes as `p ÷ h`. **It keeps its seat iff `p ≤ h × c`.** A genuinely top name (p = 1, 2, 3) survives any reasonable `h`. With `h` near 1 only the tail of the group slides out. With `h` = ½, a handicapped name needs the position an unhandicapped name reaches at half the depth.
- The low-float screen stops taking its whole column. Its bottom `(1 − h) × c` names give their seats to the next unhandicapped names (further screen positions or lists). **That is the effect he described.**
- Ladder top ten, tapped: a handicapped card stays top ten iff `h × raw_score ≥` the tenth-best unhandicapped score. Untapped: iff its `effective_position` ranks inside the ten.

The tribunal receives the report's numeric version of this example at his ASSUMED default. This committed file carries only the shape.

---

## 3. THE GROUP TEST

`in_group = (float < handicap.float_below_m) OR (market_cap < handicap.market_cap_below_m)`. Both thresholds are his keys, in the export's own units: millions of shares and $ millions (F5). The test is strict `<`, as he said "below".

- **ONE function** (L3), shaped like `is_not_equity` (`src/cobalt/radar/config.py:100-117`): `handicap_group(row, headers, block) -> GroupVerdict{in_group: yes|no|unknown, float_m, market_cap_m, reason}`.
- **Header names and unit are engine config**, not his values. They go in `radar.yaml` under `export.handicap_headers: {float: "Shares Float", market_cap: "Market Cap"}` and are checked by `load_config` (`config.py:168-177`). They are **not** added to `required_headers`: a renamed Finviz column must degrade the handicap, not kill every source (see L9 below).
- **Values**: parsed by the existing `_number` (`runner.py:391-398`). Blank and `-` become None.
- **Missing data (L1)**: if one value is present and meets its threshold, the verdict is `yes`, because the OR is satisfied. If the known value does not meet its threshold and the other is missing, or both are missing, the verdict is `unknown`. An `unknown` ticker is handled by his declared rule `handicap.missing: apply | skip`. There is no silent default: the key is required whenever the block exists. The pool row always SHOWS it: "handicap: float unknown → applied" (or "→ not applied"). ~1 % of equity candidates hit this (F6).
- **Source of the values**: the source that ranked the name (`source_for`, `pool.py:208`), recorded with the verdict. Every source of one scan comes from the same Finviz snapshot.
- **Order**: not-equity (`runner.py:144-145`) and the `exclude` block (`pool.py:292-297`) act first. The test runs only on names that reach ranking.
- **L9, dead column**: if the export lacks either handicap header, the verdict is `unknown` for every name and the scan adds `{"source": "handicap", "reason": "column missing: …"}` to `radar_pool.degraded_sources`. That is the existing red banner path (`runner.py:371-374`). Why the banner matters even with `missing: apply`: if every name is handicapped by the same `h`, the relative order is restored, which is an un-handicap in effect. The banner says so. This is never silent.
- **Replay-from-bars** (`src/cobalt/radar/replay.py:72-81`, header `Ticker, Volume, Relative Volume`) has no float or cap. That tool reports `handicap: not replayable from bars` and does not guess.

---

## 4. VISIBLE

- **Pool row** (`PoolRow`, `radar_panel.py:148-163`): a badge **`HANDICAP`** with a hover or detail line reading `float <v>M / cap $<v>M → group (float|cap|unknown) · pos <p> → <p÷h> · rank <raw> → <effective>`. In shadow mode the badge reads **`HANDICAP (shadow)`** with the would-be rank. The badge style is `badge`, like the others (`radar_panel.py:1059` CSS), and the owner is COBALT.
- **Pool header**: `handicap: live · shadow · not configured · degraded`. "Not configured" means the block is absent. It is shown, and the state is never implied.
- **Card face**, RANK + WHY (`radar_panel.py:998`): `handicap` shows `×h (float|cap|unknown)`, and `score` shows `raw → penalised`, e.g. `64 (raw 80)`, both under the COBALT badge (`cards/radar.py:51-68`). A strip chip `H` sits next to the rank chip, so he sees at a glance that the name made the ladder WITH the handicap. That is the "that's when I want to look at it" moment.
- **Excluded list**: a name that lost its seat BECAUSE of the handicap shows `excluded: handicap_cap`, separate from `config_cap` (§6).

Nothing is hidden. The raw rank and the raw score are always one click away.

---

## 5. TUNING

**Home: his pool block**, in the Radar Screens note, as a new optional sub-block `handicap:` inside `kind: pool`. The keys are `float_below_m`, `market_cap_below_m`, `factor`, `missing`, `mode` (`shadow | live`). **Why here and not `"user".trader_settings` `card.*`:** L53 puts every "cap, rank rule, metric choice" in the vault pool block, and this is a rank rule first. The card consumer reads `h` from the membership row (§1), never from a second copy of the values. One home, one read (L3). The pool block is already mirrored to trader settings every scan with its sha256 (`runner.py:223-228`), and each source id carries the block's sha prefix (`runner.py:117`).

- **Change path**: he rules, the desk edits his note (L65), shows the before/after diff, and runs a read-only parser proof (`cobalt radar sources`). The next scan reads it. No restart, because the note is parsed every cycle (`runner.py:178`). `cobalt settings load` is NOT involved, since no `card.*` key is added. The sha256 of the note lands in the mirror and the receipt.
- **Schema (L10)**: a strict Pydantic `HandicapBlock` with `0 < factor ≤ 1`, thresholds `> 0`, `missing` and `mode` required, `extra="forbid"`. A bad value freezes the pool loudly (F14). That is the existing fail-loud path, and not a silent off.
- **Deploy order is load-bearing**: the code that accepts `handicap:` must be live BEFORE the desk writes the block. Old code would freeze the pool on the unknown key (F14).
- **ASSUMED**: no ASSUMED value ever reaches production. Until he rules, the block is absent and the header says `handicap: not configured`. The ASSUMED defaults exist only in the Owner items below, for his reading after the tribunal. A value stops being ASSUMED when he rules it and the desk writes it into his note. (Alternative: reuse the setups proposal's C2 assumed store. See Open 5.)

---

## 6. REPLAY + MISS LINE (L57)

**Stored per membership row** (one migration, additive, all nullable so pre-deploy rows stay valid):

| Column | Content |
|---|---|
| `raw_rank INTEGER` | the unhandicapped rank of this scan |
| `handicap_factor NUMERIC(6,4)` | `h` applied (1 when not in the group; NULL when the block is absent) |
| `handicap JSONB` | `{float_m, market_cap_m, verdict, reason, missing_rule, mode, position, effective_position, source, block_sha256}`, validated by a Pydantic model before write |

`last_rank` and `rank_at_entry` keep their meaning: the rank that governed admission. That is the effective rank when `mode: live`, and the raw rank in shadow, where the would-be rank sits in `handicap.effective_position`.

**Replay**: F8 means float and cap enter `SourceSet.metrics` (`runner.py:139-142` gains two keys). They are then in every receipt's `pool_unit`, together with the pool block, so `decide()` is replayable from stored inputs. The card path stores `handicap_factor` on the card row (`"user".aset_sizings`, H3). `card_score` is then recomputable exactly from the row: conviction, proximity, `h`, rounded once. `formula_sha256` changes with the formula, so an old card and a new card are distinguishable (`evaluate.py:161`).

**Miss line**: add ONE value, `handicap_cap`. This is additive and never a rename. It goes into the `radar_membership` CHECK (`0004:42-43`), the `"user".missed` CHECK (`0009:76`), `replay/models.py:33`, `EPISODE_EXCLUSIONS` (`movers.py:102`), and `ExcludedBy` (`models.py:163-167`). **Definition, deterministic and single-ticker counterfactual**: an `EXCLUDE` or `LEAVE` that would be `config_cap`, for a name with `h < 1`, whose rank with its own `h` set to 1 (everyone else unchanged) would have been inside `winners`. Otherwise it stays `config_cap`. The miss line then separates "fell out on merit" from "fell out because of the handicap" (`line.py:97` counts by value, and no other change is needed there).

---

## 7. SHADOW / PROMOTION (L7, L10)

Cards stay advisory. Nothing here promotes a dot or a grade (L7 is untouched: no variable flips from human-fed to engine-fed). **Pool membership, however, is a ranking change that alters which names get polled and can form cards.** It therefore goes through:

1. **Dry-run (L10)**: `cobalt radar handicap-dry-run --day <d>` replays `decide()` scan by scan over the retained cache CSVs (F7, ≤7 days, no DB). It runs twice, with `h = 1` and with his block. The `h = 1` pass must reproduce the stored membership of that day, which is a with-DB sanity check against `radar_membership`, read-only. The report he sees, one screen per day: members in/out delta per scan; the handicapped names that KEPT their seat and the ones that LOST it (with position → effective position); the names that took their seats; the ladder of that day's stored cards re-ordered, as top ten before → after; and n (days, scans) stated.
2. **Shadow**: `mode: shadow` computes and stores everything and shows `HANDICAP (shadow)` with the would-be rank, but ranks on raw. This runs for at least the sessions the tribunal sets (ASSUMED: 2).
3. **Promotion**: his "approve" in the desk chat (L61) for the exact edit `mode: shadow → live`. The desk edits the note (L65), logs the time, and runs the parser proof. No deploy is needed for the flip.

---

## 8. INTERACTION with `SETUPS-AT-DEFAULTS-PROPOSAL-2026-09-21.md`

- **Shared lines**: C1 and C3–C7 touch the formation stage of `evaluate.py` (`:34-37`, `:635-647`, registries). They do not touch `card_score`, conviction or the pool, which that proposal states itself at its §L52 (b) and "does NOT do". **No overlap with H1 or H2.**
- **Collision: C2 ↔ H3.** Both change `"user".radar_cards_v` (C2 adds `assumed_keys` and a chip; H3 adds `handicap_factor` and raw score) and both take a migration number. The fix is procedural: whichever lands second rebases its `CREATE OR REPLACE VIEW` onto the first and takes the next free number, proven by the L68 stacked gate. I recommend **C2 first**, because its tribunal began earlier. H1 and H2 do not wait for it (L72: not a blocker).
- **Anti-rigidity**: the group test is "export columns vs his thresholds → h". A later swing or options universe adds a sibling group (for example "open interest below X") as a list entry under `handicap:`, without a refactor. The first build ships exactly one group and refuses a second until ruled. The membership columns are universe-agnostic.

---

## 9. CHUNKS

Each chunk builds offline in its own worktree, is checkable by ≥3 houses, and deploys alone in the evening pause (L43, L66). The builder seat for all three is **Opus 5 (or Sol-high)** under L29, because each is a ranking or scoring path, and H1–H3 each carry a migration.

| Chunk | What | Delivers | Size | Restarts (L42) | Migration | Needs from `cobalt_dev` |
|---|---|---|---|---|---|---|
| **H1** | float and cap into `SourceSet.metrics`; `radar.yaml` `export.handicap_headers`; `HandicapBlock` (optional) in `PoolBlock`; `handicap_group()`; `h` computed and stored (`raw_rank`, `handicap_factor`, `handicap`), **shadow only: ranking unchanged**; degraded source `handicap`; pool-row badge + header state; `handicap-dry-run` | **He sees the marked names on `/radar`** (would-be rank). Dry-run evidence exists. | M | radar, aset | yes (membership columns) | apply the migration; with-DB suite; dry-run sanity pass against stored membership |
| **H2** | `mode: live` in `pool.py` (effective position in the key); `handicap_cap` in `ExcludedBy`, both CHECKs, the replay sets, miss line | **The 50 compete on the lowered rank.** The untapped ladder follows (F11). | M | radar (replay is a one-shot job, not a resident) | yes (two CHECKs) | migration + a replay run on a stored day |
| **H3** | `scoring.card_score(…, h)`; `handicap_factor` on `aset_sizings` (set at creation and refresh, read at tap); `radar_cards_v` columns + `FIELD_OWNERS` badges; card face `H` chip + `raw → penalised`; `picks` `score_inputs` carries `h`; receipt replay passes `h` | **Tapped ladder and F3 focus carry the handicap.** One authority holds end to end. | M | aset, radar | yes (column + view) | migration; the view test (owner badges); tap-path suite |

Tests (L45, L69): the group test runs against `pool-metrics.real-shape.csv` (all present) and the movers real-shape fixtures (blank-float and blank-cap equity rows present, F6). A redacted real-shape screen CSV containing a blank-float equity row is added from the retained cache under the L45 fixture policy. The homogeneous-screen case (every name in group) must change ranks under position ÷ h, and a test proves that a metric multiplier would NOT. A missing header produces the degraded banner, never a silent un-handicap. `handicap_cap` against `config_cap` gets a counterfactual unit test. `card_score` must be exact on recompute from the row. Thresholds live on a constructed block, never read from settings to assert a value (L69).

**Evenings, from "tribunal ruled" to "he sees a handicapped name marked on `/radar`": 1.** H1's evening, then the next scan once the desk has written his block. The handicap acting on the 50 needs H2's evening plus his approve of `mode: live`. Acting on the whole ladder needs H3's evening. That is **3 evenings to full effect**, and the flip itself needs no deploy.

---

## L52 (a)–(d)

| Bar | Answer |
|---|---|
| (a) every number traceable | Float and cap come from the Finviz export Cobalt already fetches. Headers and units are verified on the real-shape fixture (F4, F5). Missing values are named `unknown` and handled by his declared rule, with the handling shown (§3). `h`, the thresholds and the missing rule are his ruled values, carried by key. None is modelled. |
| (b) ONE ranking authority | `card_score` (ADR-0009 D4) stays the one authority, with the formula `conviction × proximity × h`. `pool_position` (`last_rank`) remains the admission number and the ladder's existing secondary key, and it carries the SAME stored `h`. Every consumer is listed in §1. None re-ranks around it. |
| (c) seam as a real artifact | The seam is the membership row (`raw_rank`, `handicap_factor`, `handicap` JSONB) written by the pool stage and read by the card stage (`evaluate.py:1225`, which already reads `last_rank` from it). It is typed by Pydantic and CHECKed in SQL. |
| (d) auditable by another house | `handicap_group()` and the key change are pure functions. The inputs are stored (receipt `pool_unit` + the membership row). The dry-run command recomputes any retained day. `formula_sha256` versions the card formula. |

## What this does NOT do

- It does not exclude anyone. The `exclude` block stays the only hard tool (`pool.py:292-297`).
- It does not touch conviction, dots, curves, `proposed_key`, sizing, or any grade he tapped.
- It does not add a float dot. If a computed float dot is ever proposed (F10's charter mentions float), that tribunal must state how it composes with `h`. A dot would feed conviction, and `h` would then also scale the result, which is a double count. The rule proposed here: **no float-derived dot may be promoted while `h` applies to the same group**, unless the tribunal rules the composition.
- It does not change the priority rule (screens before lists), the cap, the metric or stickiness. Those are his (L53).
- It does not give a per-screen exemption. See Open 3.
- It does not replay from synthesized bars (§3).

## Open to the tribunal

1. **(c) over (a).** I am least sure the card consumer (H3) is wanted: after a tap he is already looking at the name. Rejected alternative: (a) alone. The reason is L52 (b): it leaves the ONE authority unhandicapped while its secondary key is handicapped. The tribunal may still rule H3 out and accept that consequence explicitly.
2. **Flat against graded `h`.** Graded (from a floor up to 1 at the threshold) was rejected for the default because it needs two more of his values and is hard to say aloud. It is easy to add later as a `shape:` key.
3. **The low-float morning screen.** It is entirely in the group, so the handicap will systematically thin a screen he built for low floats. His words cover "any sheet … low float morning", so it is not exempted. A per-screen `handicap: exempt` override is the rejected alternative. It is additive and possible later.
4. **Priority group dominance.** With screens before lists, a handicapped SCREEN name still beats every LIST name, whatever `h` is. Rejected alternative: dropping handicapped names into a third group between screens and lists. That is a cliff, which is exclusion-like, and he said no exclusion. The tribunal should confirm he accepts that the handicap acts within a group.
5. **ASSUMED values never in production.** The block is absent until he rules (§5). Rejected alternative: ship with the setups proposal's assumed store (C2) supplying the ASSUMED `factor`. That creates a dependency on C2, and his R28 already rules the thresholds.
6. **`handicap_cap` as a new enum value.** The rejected alternative is a boolean column beside `config_cap`. It would avoid touching two CHECKs, but the miss line counts by `excluded_by` (`line.py:97`) and would need a second grouping key.

## Owner items (his by L53; read AFTER the tribunal; each carries an ASSUMED default, whose number is in the report and not in this file)

| Key (pool block `handicap:`) | What it decides | ASSUMED default |
|---|---|---|
| `float_below_m` | float threshold, in millions of shares | his R28 value (desk reading) |
| `market_cap_below_m` | market-cap threshold, in $ millions | his R28 value (desk reading) |
| `factor` | `h`, the flat multiplier | conservative: a small penalty (see report) |
| `missing` | `apply` or `skip` for `unknown` | `apply` |
| `mode` | `shadow` or `live` | `shadow` until his approve (§7) |
| shadow length | sessions in shadow before the approve | 2 sessions |
