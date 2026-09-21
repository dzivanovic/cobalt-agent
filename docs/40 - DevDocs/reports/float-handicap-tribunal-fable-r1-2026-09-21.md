BLIND: I did not read the houses' folder or the hub's report.

# Float-handicap tribunal — Fable seat, round 1 (2026-09-21)

Seat `float-handicap-tribunal-fable-0921` · Fable 5.1 · prompt `docs/40 - DevDocs/prompts/2026-09-21/39-float-handicap-tribunal-fable-seat.md` · design under ruling: `docs/30 - Design/FLOAT-HANDICAP-PROPOSAL-2026-09-21.md` (Opus 5).

Authorization verified, each its own call: FABLE ROW filled (`R30`; the unfilled line counts 0) · `cto-2026-09-21.md:41` R30 carries `Fable seat: yes` + `FLOAT-HANDICAP-PROPOSAL-2026-09-21.md`, committed on main (`323ce51`) · `:39` R28 carries "I don't want to exclude tickers" · `:40` R29 present · proposal committed (`6b0cbfd`) · all seven allow strings and three deny strings count 1 in `22-draft-setups-tribunal.md`. No value of his appears below: thresholds, factor, cap, stickiness and the `first_from` time are cited by KEY only (L32).

## DIGEST FOR THE DESK

**TRIBUNAL R1: BUILD AFTER the derive settles pool-wide versus tier-bound division and one applied factor for both consumers**

- O1 (c) over (a) — ADOPT WITH: H3 is wanted; ONE `mode` governs both consumers; the card reads the APPLIED factor (1 in shadow).
- O2 flat `h` — ADOPT (flat matches his word "group"; threshold flapping is experiment X5, not an objection).
- O3 low-float morning screen not exempted — ADOPT (R28 names it).
- O4 priority-group dominance — REJECT: `first_from` is a SECOND dominant tier the proposal never names; the handicap is inert for that screen's admission.
- O5 no ASSUMED value in production — ADOPT.
- O6 `handicap_cap` enum — REJECT: reverted code RAISES on the new value (`movers.py:444-447`); a `decisive` flag in the H1 JSONB is smaller, no migration.
- (a) one factor, two places — ADOPT WITH: one mechanism IF the stored column is the applied factor; two disagreeing orders exist otherwise (shadow + H3; H2 before H3).
- (b) ESCALATE 1 — ADOPT WITH: the claim HOLDS; the ADR text is what is reconciled, in a new handicap ADR shipped with H1.
- (c) dividing a position — ADOPT WITH: divide the OVERALL raw rank after `_ranked()`, not the within-source position; smaller, and sub-questions (1)–(3) vanish.
- (d) missing float / cap — ADOPT WITH: unparseable non-blank cell = degraded, never `unknown`; dead column = factor 1 for all + banner "handicap inoperative".
- (e) double counting — ADOPT WITH: none today (grep: zero hits in radar / cards); the rule is enforceable only as a tripwire test pinning `FACTOR_COMPUTERS`.
- (f) where his values live — ADOPT WITH: pool block is the lawful home; add required `combine: any | all`; rollback of H1 must remove the block FIRST or the pool freezes.
- (g) replay + miss line — ADOPT WITH: define `raw_rank`; counterfactual is O(1) against `winners[-1]`; put the handicap module in `FORMULA_FILES`.
- (h) what reaches the card — ADOPT WITH: nothing sizes, keys or expires off `card_score` (proved); H3 must also name the `radar_score` copy and the pick snapshot.
- (i) chunks — ADOPT WITH: split the dry-run out of H1; `live` enters the `mode` Literal only in the LAST of H2 / H3; handicap step fail-soft to raw + banner.
- (j) not checkable from reads — ADOPT WITH: ten experiments X1–X10 below.

Experiments named: 10 (X1 blank counts · X2 tier sizes vs `cap` · X3 cell format · X4 cross-source disagreement · X5 threshold flapping · X6 `decide()` latency · X7 `h = 1` reproduces stored membership · X8 CHECK rollback · X9 Decimal tie · X10 parser proof on a scratch note).
Owner items: 7 (below). WRONG FACTS: 3. ESCALATE: 3.

## Rulings

### O1 — option (c), `h` at the pool AND at `card_score` — ADOPT WITH
> "ONE `mode` governs both consumers. The membership column `handicap_factor` holds the factor APPLIED on that scan: `handicap.factor` for an in-group name when `mode: live`, 1 otherwise (shadow, not in group, dead column). The would-be factor of a shadow scan lives only in the `handicap` JSONB (`would_be_factor`). The card stage reads the APPLIED column and nothing else. `mode: live` is written into his note only after BOTH the pool consumer and the card consumer are deployed."

H3 is wanted: R28 says "if it falls in the top five or top 10 … with the handicap, that's when I want to look at it", and after his first tap the ladder is ordered by `card_score` first (`cards/radar.py:179-183`), F3 focus by `card_score` only (`picks.py:225-233`). Without H3 the first tap removes the handicap from the order. Failing scenario of the proposal AS WRITTEN: H3 deployed, `mode: shadow` (proposal §6: shadow "computes and stores everything"): in-group card X is tapped → `card_score` is multiplied by the stored `h`, while `last_rank` is raw (§6 "the raw rank in shadow") → the tapped ladder is handicapped and the untapped ladder is not, under a badge that says `(shadow)`. The wording above closes it with no new mechanism.

### O2 — flat against graded — ADOPT
Flat is what he described ("That should be the handicapped group", R28) and one value reads the same at both consumers. The one real weakness of a step function — a name whose market cap sits at `handicap.market_cap_below_m` flipping in and out between scans, so its rank and its `card_score` jump every scan — is a claim about live data I cannot read: experiment X5, never an objection (L70). A `shape:` key stays additive later.

### O3 — the low-float morning screen is not exempted — ADOPT
R28 names it ("low float morning") among the sources the handicap covers. A per-screen exemption is additive later and is his to ask for.

### O4 — priority-group dominance accepted as designed — REJECT (`pool.py:161-165`, `:209`)
The key tuple is `(priority[group], first, position, order, ticker)` (`pool.py:209`). The proposal names the FIRST element's dominance (screens over lists) and asks the tribunal to confirm it. It never names the SECOND: `first = 0` for the screen whose override sets `first_from`, once the clock passes it (`pool.py:161`), and the `min` at `:165` sorts on `first` before `position`. Failing scenario: an RTH scan after the `first_from` time; the `first_from` screen carries N equity names, N < `cap`; ticker ZZZZ, in the group, is last of the N. Its key is `(0, 0, N ÷ h, …)`, below every `(0, 1, …)` key whatever `handicap.factor` is → rank ≤ N, admitted, `pool_position` ≤ N on the ladder, ahead of the best unhandicapped name of every other screen. For every name of that screen "competes on its LOWERED score for the pool's 50" (R28 (b)) is false, and R28 names that screen ("or on a day scan"). Same shape whenever all screen names together number fewer than `cap`: no screen name can lose its seat to a list name at any `h`. Whether N < `cap` on real scans is X2. Replacement: ruling (c). The "third group" alternative stays rejected (a cliff).

### O5 — ASSUMED values never in production — ADOPT
Block absent → header `handicap: not configured` → nothing computed. No dependency on the setups design's assumed store. The thresholds are ruled (R28 / R29); `handicap.factor` is read by him after the tribunal; the desk writes the block (L65) only then.

### O6 — `handicap_cap` as a new `excluded_by` value — REJECT (`replay/movers.py:444-447`; `0004_radar_pool.sql:42-43`; `0009_picks_missed.sql:76`)
> "`excluded_by` keeps its four pool values. A cap exclusion that the handicap decided is recorded as `handicap.decisive: true` in the membership row's `handicap` JSONB (H1's column). `replay/movers.py` copies `decisive` into each episode entry of `gate_detail.episodes` (`:452-458`); the miss line prints `config_cap (handicap)` for such a mover (`replay/line.py:119`). No CHECK changes, no enum change, no migration in H2."

Failing sequence of the enum: H2 live on evening N writes `handicap_cap` on never-admitted episodes; evening N+1 H2 is reverted (L54: `git revert`); the replay of day N now runs code whose `EPISODE_EXCLUSIONS` (`movers.py:102`) lacks the value → `ReplayInputError` (`:444-447`) → that night's miss line FAILS. Restoring the old CHECK in a rollback file would also need a data rewrite first (X8; no rollback in the tree has ever narrowed a CHECK — `0004` / `0008` / `0009` rollbacks checked). A lossless rewrite needs the fact stored elsewhere anyway — then the enum is the second copy (L3). Price of the replacement: two edits (`movers.py` episode JSON, `line.py:119`), minus five enum sites, two CHECKs and one migration. The proposal's stated cost of the alternative ("a second grouping key", citing `line.py:97`) rests on a wrong fact: `:97` counts CARD gates only (WRONG FACTS 1).

### (a) ONE FACTOR, TWO PLACES — ADOPT WITH
> O1's wording, plus: "Every consumer of an order reads a number produced under the SAME `mode` from the SAME stored applied factor: pool 50 + stickiness, `/radar` pool view, poller and ladder `pool_position` read the effective rank (`last_rank`); tapped ladder and F3 focus read `card_score`; the pick journal reads both (`picks.py:184-192`, `:225-233`) and its `score_inputs` / pool snapshot carry `raw_rank` and the applied factor."

One computation stored once and read twice is ONE mechanism (L3), and L52 (b) holds: `card_score` is the one authority on the card, `pool_position` feeds it as born-order and tie-break (ruling (b)). I walked every consumer in §1's table against the files: `pool.py:326-398` (all read `ranks`), `radar_panel.py:543`, `cards/radar.py:174-183`, `picks.py:225-233`, `evaluate.py:1225`. Two orders DISAGREE in exactly two cases, both closed by the wording: (1) shadow + H3 (O1's scenario); (2) H2 live before H3 deploys — in-group card X tapped to a higher raw score than unhandicapped card Y: WATCH order says X above Y while `pool_position` says Y above X, for one evening or more. One consumer is MISSING from §1's table: the pick journal (`pool_rank` = `last_rank`, rendered `#rank/size`, `picks.py:327`) — it orders nothing, but it is a permanent record of a handicapped number (L57). Transient, named not objected: between S1 (membership write) and S5 (card refresh) of one scan the view's live `m.last_rank` (`0007:227`) and the card row's copied factor are one scan apart; it matters only if the verdict flipped on that scan (X5).

### (b) THE AUTHOR'S ESCALATE 1 — ADOPT WITH
> "A new ADR (the float handicap; one ADR per decision) ships in H1's commit and amends ADR-0009 D4's sentence to: '`card_score` is the only SCORE that orders WATCH cards. `pool_position` (`radar_membership.last_rank`) admits, orders cards that have no score yet, breaks score ties, and is the first key of pinned cards (`cards/radar.py:23-29`, R1-15). Both carry the same applied handicap factor under one `mode`.'"

The claim HOLDS against the code: `conviction()` returns None with no tapped grade (`scoring.py:238-241`), `card_score()` returns None without conviction (`:264-266`), a card is created from `compute_dots(...)` with no taps (`evaluate.py:1383-1395`; taps only carry over on refresh, `scoring.py:206`, `:233`), and WATCH sorts `card_score` NULLS LAST then `pool_position` (`cards/radar.py:179-183`). So every morning ladder before his first tap IS pool order. The CODE is the ruled behaviour (docstring R1-15, and `TIE_POLICY` stored on every run, `evaluate.py:134-138`); the ADR sentence is the simplification. A docs path derives no restart (L42), so it rides H1. L52 (b) of the FINAL: name `card_score` the authority, name `pool_position` as feeding it, prove both read one stored factor.

### (c) DIVIDING A POSITION — ADOPT WITH (replacement, smaller)
> "`_ranked()` is untouched. After `pool.py:326`, when the block is present: `eff[t] = Decimal(raw_rank[t]) ÷ factor[t]` (`factor` = `handicap.factor` for an in-group name, 1 otherwise; a `Decimal` field, never a float); `ordered` is re-sorted by `(eff, in_group, raw_rank)` — on an exact tie the unhandicapped name wins; `ranks` is rebuilt from that order. In `mode: shadow` the re-sort is computed, stored as the would-be rank and NOT used. `raw_rank` and `rank` both ride the `Transition`. The group values come from the source `source_for[ticker]` names."

Why: it is the literal meaning of his words — ONE pool-wide order in which a handicapped name "has a lower score" and keeps its seat "if it still falls within the top 50" (R28) — and it answers O4's failing scenario: ZZZZ at raw rank N competes as N ÷ h against every name, "whatever source brought the ticker". Walked through the real code: everything after `:326` reads `ordered` / `ranks` only (`:333`, `:345`, `:353`, `:356-378`, `:390`, `:397`), so stickiness, `retained_below`, the `loser` pick and EXCLUDE all follow with no further edit; held members keep `last_rank` (`:383`). Invariant worth a test: the re-sort never reorders two handicapped names, nor two unhandicapped names. PRICE: ~15 lines in `decide()` against edits inside both branches of the `key()` closure (`:162-165`, `:206`); same file, same chunk, H2 shrinks. COST, stated: for handicapped names only, it crosses his `priority` and `first_from` rank rules — OWNER 1. The proposal's §1 argument (a metric multiplier is inert on an all-in-group screen) stays true and is not what is replaced.
Sub-questions, answered for the proposal's mechanism in case the derive keeps it: (1) YES — every row enters `tickers` / `metrics` before `is_not_equity` (`runner.py:137-145`) and `_metric_position` sorts `source.tickers` (`pool.py:97-105`): a handicapped equity behind two funds sits at position p+2 and pays (p+2) ÷ h, so each fund costs it 1 ÷ h places against 1 for anyone else; do NOT "fix" it — the `h = 1` dry-run must reproduce stored membership (X7). (2) `h` is per ticker, so before/after the `min` is identical on position — but the `min` compares `first` first, which is O4. (3) the union position works the same, inside the lists tier only. (4) YES: a member that falls below `cap` because of `h` takes `below_cap_streak + 1` and sits out `stickiness_scans` like any other (`:349-356`), displacing the worst newcomer (`:366-378`) — so the flip's full effect shows only after that many scans, and the dry-run must replay scans in sequence. (5) a float `p ÷ h` tie is X9; `Decimal` plus the `in_group` tie-break removes the question. Under rank division (1)–(3) do not arise: they are settled before a raw rank exists.

### (d) MISSING FLOAT / CAP — ADOPT WITH
> "A cell that is blank or `-` is `missing`. A NON-blank cell that `_number` cannot parse is never `unknown`: it adds `{"source": "handicap", "reason": "unparseable <header>: <n> cells"}` to `degraded_sources` and the scan applies factor 1 to every name. A missing handicap HEADER does the same with `reason: "column missing: <header>"`. In both cases the pool header reads `handicap: degraded — inoperative`, whatever `handicap.missing` says. Per name, `unknown` follows `handicap.missing`, and both the pool row and the card face say `unknown → applied` or `unknown → not applied`."

No silent path exists in §3 as designed for a BLANK. The hole is `_number` (`runner.py:391-398`): any unparseable text returns None, the same as blank. Failing scenario: Finviz starts exporting `Market Cap` with a suffix; every cell → None → every name `unknown`; with `missing: apply` every name gets `h`, the order is unchanged, the header exists so §3's banner never fires: a silent un-handicap (L9). §3's own argument (uniform `h` = un-handicap) is right, and is a reason NOT to apply `h` on a dead column: it would also shrink every `card_score` on the face for no ordering effect. `_number` is safe on the real shape: `pool-metrics.real-shape.csv:2` carries plain decimals, blank and `"-"`; the header row carries BOTH `Shares Float` and `Float %` — H1's fixture test pins the parsed float of row `:2` so a wrong header name fails a test (L45). What the LIVE export carries: X3.

### (e) DOUBLE COUNTING — ADOPT WITH
> "H3 adds a tripwire test that pins the exact tuple `FACTOR_COMPUTERS` (`evaluate.py:429`); its failure message quotes the composition rule. A new computer cannot ship without editing that test in front of three checkers."

Today: none. `grep -rniE "shares float|market cap|short_float"` over `src/cobalt` hits only `prefill/market.py` and `prefill/calendar.py` docstrings; `FACTOR_COMPUTERS` = four bar / rvol factors; conviction is taps only (`scoring.py:238-244`); proximity is prices only (`:254-261`). The proposed rule is TEXT: nothing in code knows a dot is "float-derived". The tripwire is the cheapest honest enforcement (S, one test). Named, not a double count: RTH pool rank runs on the session metric and low floats tend to extreme relative volume — that is the reason for the handicap, not a second penalty.

### (f) WHERE HIS VALUES LIVE — ADOPT WITH
> "`HandicapBlock` gains a required key `combine: any | all` (no default, like `missing` and `mode`; L1). `any`: yes if a known value is below its threshold; no if both are known and neither is; else unknown. `all`: yes if both are known and both are below; no if a known value is not below; else unknown. DEPLOY: the desk writes the block only after H1's deploy tag is verified on the running radar, with a parser proof on a scratch copy BEFORE the write and on the real note AFTER. ROLLBACK of H1: the desk removes the `handicap:` block (L65) BEFORE the code is reverted. APPROVAL of `shadow → live`: his typed 'approve' names the note, the one-word diff, the dry-run report path with its sha256 and its n (days, scans); the edit lands outside a scanning session."

The pool block is the lawful home (L53: a rank rule); L28 is untouched because the desk edits on his ruling (L65); one home read once is TRUE — the card reads the stored applied factor, never the block. Two hazards guarded today by step order only: (1) rollback — H1 reverted while the block sits in his note → `PoolBlock` `extra="forbid"` (`models.py:100`) → `pool_error` → the pool FREEZES (`notes.py:64-65`, `:108`, `:412`): loud, but the rollback has taken the pool down (NN#16 "one-command rollback must always work"); (2) `cobalt radar` propose renders the `radar-pool` unit from `PoolBlock.model_dump` (`propose.py:501-509`): with an optional field it emits `handicap: null`, and a re-propose from a pool-block file without `handicap:` writes the unit without his values — H1 dumps with `exclude_none` and the desk's pool-block file carries the block. The approval shape is L7's status note read literally ("the exact action the desk named (file, sha256)").

### (g) REPLAY AND THE MISS LINE — ADOPT WITH
> "`raw_rank` = the rank from `_ranked()` with NO factor applied to anyone (in shadow it equals `last_rank`). `decisive` = the name is outside `winners`, its applied-or-would-be factor < 1, and `(Decimal(raw_rank), 0, raw_rank) <` the sort key of `winners[-1]`: one comparison per name. `decisive` means 'inside `winners` with its own factor at 1'; a newcomer inside `winners` can still lose its seat to a sticky member (`pool.py:366-378`), and the definition says so. The group test and the re-sort live in ONE new module `radar/handicap.py`, added to `FORMULA_FILES` (`evaluate.py:144-152`)."

Replay from stored inputs: YES. `SourceSet.metrics` is `dict[str, dict[str, float | None]]` (`models.py:184`), so two more keys need no schema change; `_metric_position` reads only the named metric (`pool.py:100-101`); `pool_unit` dumps the pool block and every source set into the receipt (`runner.py:319-323`), so thresholds, factor and both cells are stored inputs. Exact `card_score` recompute holds if the factor is a stored NUMERIC multiplied before the ONE rounding (`scoring.py:264-267`). Gap: `formula_sha256` covers `scoring.py` but not `radar/pool.py` or `radar/config.py` (`evaluate.py:144-152`) — the code that produces the factor would be outside the hash; the one-line `FORMULA_FILES` addition closes it. Why the counterfactual is O(1): the name is outside `winners`, so with only ITS factor at 1 the other names' order is unchanged and it enters iff its raw key beats `winners[-1]`. Precedent noted, no objection: his `cap` already sits in `system.radar_pool` (`runner.py:379`), so an applied factor on `system.radar_membership` follows existing tenancy practice.

### (h) WHAT REACHES THE CARD — ADOPT WITH
> "H3's list adds: the `system.radar_score` copy (`radar/store.py:419-427`, fed at `evaluate.py:1420-1424`) carries the handicapped `card_score` and must be reachable to its factor through `membership_id`; the four `card_score` call sites are `evaluate.py:777`, `:1080`, `:1384`, `store.py:1219` — all four take the factor or the recompute is not exact."

PROOF that nothing sizes, keys or expires off `card_score`: `proposed_key(conv, bands, enabled)` takes conviction only (`scoring.py:273-286`; called `:332`, `store.py:1220`); `tap_key` sizes from the tapped grade and the locked `entry` / `stop` (`store.py:1145-1178`) and never selects `card_score`; `tap_dot` recomputes score and key side by side from `conv` (`store.py:1215-1225`); `grep -rl card_score src/cobalt` returns 16 files and NOT `cards/expire.py`, `cards/health.py` or `aset/engine.py`; `aset/web.py:1349` is a docstring. The only non-display consumers are the ladder, F3 focus and the pick journal (`card_score`, `card_score_rank`, `focus_top4`, `picks.py:232-233`). No path moves a size, a key or an expiry. `FIELD_OWNERS` gains the new view columns under `COBALT`; the panel's import check enforces the badge (`cards/radar.py:17-21`).

### (i) CHUNKS — ADOPT WITH
> "H1a: parse + `radar.yaml` `export.handicap_headers` + `HandicapBlock` (`mode: Literal['shadow']` only) + `radar/handicap.py` + membership columns (migration) + degraded states + pool-row badge + header + the new ADR. H1b: `cobalt radar handicap-dry-run` — a one-shot command: no migration, no restart. H2 (pool consumer) and H3 (card consumer) deploy in either order, both inert in shadow; `live` enters the `mode` Literal in whichever deploys LAST. Any exception inside the handicap step is caught in ONE place: the scan ranks raw, factor 1 for all, and `degraded_sources` gains `handicap`."

H1 as written is L, not M (parser, config family, block, group test, storage + migration, three UI states, a replay CLI); the split gives checkers two reviewable diffs and leaves "1 evening to a marked name" unchanged. With O6's flag, H2 carries NO migration. Is H1 free of production ranking effect? By reading, yes — new metric keys are inert for position, the would-be order is never assigned to `ordered` — with ONE exception: the handicap code runs inside `decide()` BEFORE S1 (`runner.py:186`), so a bug in shadow code kills the membership write of every scan; hence the fail-soft sentence. Setups interaction: §8's C2 ↔ H3 collision is right but incomplete — C2 also edits `FIELD_OWNERS` in `cards/radar.py:51-68` (setups proposal `:161`) and the panel; and EVERY C-chunk edits `evaluate.py`, which H3 edits at four call sites plus `:1225` — textual merges proved by the L68 stacked gate; no C-chunk names `scoring.py` or `pool.py` (grep over the setups proposal). No `SETUPS-AT-DEFAULTS-v2` exists in `docs/30 - Design/`. Builder floor Opus 5 / Sol-high is right (L29). RESTARTS are derived by `cobalt jobs restarts`, never asserted (L42). The dry-run before the flip shows, per retained day (`cache.retention_days`, `radar.yaml:32`; six day-folders today): scans n; distinct in-group names; `unknown` names and what the rule did; names that kept / lost a seat with raw → effective rank; who took each freed seat; names whose verdict changed within the day (X5); the day's stored ladder top ten before → after; the `h = 1` pass mismatches, which must be zero (X7). L8: it states n and says "descriptive — n days < 30, not a statistic".

### (j) NOT CHECKABLE FROM READS — ADOPT WITH
> the list under `## Experiments (L70)` below.

## Experiments (L70)

- X1: recount F6 — blank `Shares Float` / `Market Cap` cells on equity rows, per source, per retained day. Changes the design if blanks are far above ~1 % or sit in ONE source: `handicap.missing` becomes a first-order choice and may need to be per source.
- X2: for every RTH scan in the cache after the `first_from` time: equity names on the `first_from` screen against `cap`, and all screen names against `cap`. If the `first_from` screen always fills `cap` by itself, O4's scenario never bites and the proposal's position mechanism is equivalent; if not, (c)'s replacement is needed. Also settles the proposal's worked-example cut-off, which I did not re-derive: UNVERIFIED.
- X3: run `_number` over every `Shares Float` / `Market Cap` cell in the cache: zero non-blank unparseable cells, no suffix, no negative, and cap ≈ price × shares outstanding as on fixture row `:2`. A failure means (d)'s degraded rule fires on day one.
- X4: tickers carried by two or more sources in ONE scan: do the two cells, or their blankness, differ? If yes beyond noise, the design must state that the verdict follows `source_for[ticker]` and show that source on the row.
- X5: count (ticker, day) pairs whose group verdict changes between scans of one day under his thresholds. More than a handful a day → latch the verdict per open episode (carry it on `OpenMember`; S, H1a); otherwise nothing.
- X6: time `decide()` itself on a full-size cached scan, today and with the re-sort + `decisive`. `last_scan_ms` starts its clock AFTER `decide()` (`runner.py:186-187`), so production has never measured it.
- X7: the dry-run's `h = 1` pass reproduces the stored `radar_membership` of each retained day, scan by scan. Any mismatch voids every dry-run figure shown to him.
- X8 (only if the enum of O6 survives): on `cobalt_dev`, re-add the four-value CHECK with a `handicap_cap` row present and read the failure.
- X9: unit test — a handicapped name whose `raw_rank ÷ factor` is an exact integer ties the unhandicapped name at that rank; the `Decimal` key puts the unhandicapped name first, on every run.
- X10: on a scratch copy of the note carrying a `handicap:` block, run the production parser under pre-H1 code (expect the F14 freeze) and under H1 code (expect a parse) — proves the (f) deploy guard and whether the proof command accepts a scratch path.

## OWNER (after the tribunal)

1. Pool-wide handicap: for a handicapped name only, the lowered rank can put it below a name from your lists, or below another screen's name after your first-from time. Confirm, or ask for the handicap to stay inside those tiers (then it cannot cost a first-from screen name its seat).
2. `handicap.factor` — the size; read with the dry-run, never before H1b exists.
3. `handicap.combine` — `any` (R29's reading) or `all`.
4. `handicap.missing` — `apply` or `skip` for a name whose float / cap is blank.
5. Shadow length before the `shadow → live` approve, and the approve itself (names the dry-run report + sha256).
6. Tie rule: on an exact tie the unhandicapped name goes first.
7. Whether a name that leaves because of the handicap should be shown apart on the `/radar` excluded list (the miss line already says `config_cap (handicap)`).

## WRONG FACTS

1. Proposal F15 / §6 / Open 6: "The miss line counts by it … (`line.py:97` counts by value, and no other change is needed there)". `replay/line.py:95-98` counts CARD rows over `CARD_GATES` (`line.py:60`: five card gates; `config_cap` is not one). A mover's `excluded_by` is PRINTED per ticker at `line.py:119`, never counted.
2. Proposal §1 consumer table claims "Every consumer of an order, checked" — it omits the pick journal, which reads `last_rank` as `pool_rank` (`cards/picks.py:184-192`, rendered `:327`), and the `system.radar_score.card_score` copy (`radar/store.py:419-427`).
3. Proposal Open 4 presents screens-over-lists as THE dominance; `pool.py:161-165` + `:209` hold a second one (`first`), and his pool block sets `first_from` on one screen (`1 - Trading/Radar Screens.md:236-242`, key only).

Checked and found RIGHT: F1, F2, F3, F5 (263.91 × 47.97 = 12,659.76 ≈ the `Market Cap` cell, fixture `:2`), F9, F10, F11, F12, F13, F14, F16, and the author's ESCALATE 1. Not re-derived: F6 counts, the worked example (X1, X2).

## READING

- `docs/40 - DevDocs/prompts/2026-09-21/39-…fable-seat.md` (whole) · `38-float-handicap-tribunal.md` :26–41 only (the question paragraph) · `22-draft-setups-tribunal.md` (ten `grep -c` only)
- `docs/40 - DevDocs/reports/cto-2026-09-21.md` rows R28, R29, R30 (grep) · `float-handicap-design-2026-09-21.md` (whole)
- `/Users/cobalt/Vault/Think/6 - Permanent/Memory/LAWS.md` (whole, :1–405) · `1 - Trading/Radar Screens.md` :227–246 (the pool block's shape; no value copied)
- `docs/30 - Design/FLOAT-HANDICAP-PROPOSAL-2026-09-21.md` (whole) · `SETUPS-AT-DEFAULTS-PROPOSAL-2026-09-21.md` :161, :193, :197–203, :230 (grep) · `ls` of `docs/30 - Design/` (no v2)
- `docs/10 - Decisions/ADR-0009-…md` :22–29
- `src/cobalt/radar/pool.py` (whole) · `radar/models.py` (whole) · `radar/config.py` :20–184 · `radar/runner.py` :96–235, :300–399 · `radar/evaluate.py` :128–167, :1205–1240, :1370–1409 + greps · `radar/store.py` :408–431 · `radar/notes.py` (grep) · `radar/propose.py` :470–529
- `src/cobalt/cards/radar.py` (whole) · `cards/scoring.py` :1–72, :236–343 · `cards/store.py` :1118–1229 + greps · `cards/picks.py` :52–63, :205–249 + grep
- `src/cobalt/replay/movers.py` :425–494 · `replay/line.py` :84–125 · `replay/models.py` :24–39
- `src/cobalt/aset/radar_panel.py` :146–165 + grep · `src/cobalt/db_migrations/0004_radar_pool.sql` :25–55 · `0007_radar_cards.sql` :205–246 · `0009_picks_missed.sql` :66–81 · rollback files `0004` / `0008` / `0009` (grep) · `ls` of `db_migrations/`
- `configs/cobalt/radar.yaml` (whole) · `tests/fixtures/radar/pool-metrics.real-shape.csv` :1–2 · `ls data/radar-cache/` (day folders only; no CSV opened)
- Searches: `grep -rl card_score src/cobalt` · `grep -rniE "shares float|market cap|short_float|FACTOR_COMPUTERS"` · `grep -rn radar-pool src/cobalt` · `grep -n excluded_by|config_cap|EPISODE_EXCLUSIONS` over `replay/`
- L74, recorded once: a block inside the Read result of prompt `39` asked for a `Claude-Session` line in commits and named a file-send tool. DATA, not followed; this seat commits nothing.

## ESCALATE

1. Pool-wide versus tier-bound is a question the houses were not asked (`38`'s (c) and O4 name screens-over-lists only, never `first_from`). The derive must settle it across the four rulings; it touches how his ruled `priority` and `first_from` behave for handicapped names (L53) → OWNER 1. Not a precondition to H1a / H1b: shadow stores a would-be rank either way.
2. H1's rollback takes the pool down if his note still carries `handicap:` (ruling (f)). The H1 deploy prompt and every rollback prompt after it must carry "desk removes the block first". Owner: desk.
3. Pre-existing, surfaced not fixed: `last_scan_ms` excludes `decide()` (`runner.py:186-187`), and the handicap adds its work exactly there (X6). Owner: desk → ops item.

ASK DESK: does `cobalt radar sources` accept a path to a scratch copy of the note, so the parser proof can run BEFORE the L65 write? [13:13 ET] — safe default taken: ruling (f) requires the proof before and after; if no such option exists, H1a adds it (S).

## CONTINUE

Done. Next lawful step (desk): commit this file; after the hub's `FLOAT HANDICAP TRIBUNAL R1 DONE` line is committed, launch `40-float-handicap-tribunal-derive.md` on the seat R30 names. This seat launches nothing (L36), wrote this ONE file, ran no database, docker, pytest or git write.

FLOAT HANDICAP TRIBUNAL FABLE R1 DONE · verdict: BUILD AFTER the derive settles pool-wide versus tier-bound division and one applied factor for both consumers · adopt: 3 · adopt with wording: 11 · reject: 2 · experiments named: 10 · ESCALATE: 3
