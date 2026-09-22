# Float handicap tribunal — derive (v2) — 2026-09-21

Seat: `float-handicap-tribunal-derive-0921` · model: claude-fable-5-1 (row R30, `cto-2026-09-21.md:41`, committed `323ce51`) · prompt: `prompts/2026-09-21/40-float-handicap-tribunal-derive.md` · run: 2026-09-22 10:4x–11:1x ET

## §0 Headline

- v2 written: `docs/30 - Design/FLOAT-HANDICAP-v2-2026-09-21.md` — the proposal whole, 26 folds tagged `[F-nn]`, 18 house wordings taken verbatim, 0 values of his.
- Seats: Grok and Gemini ruled in full; Fable ruled in full (R30 `Fable seat: yes`); Astra `SKIPPED — METER at probe` → RECORDED under `cto-2026-09-22.md` R13, not a refusal; Astra reads v2 when its meter returns (2026-09-26 06:47 ET).
- **NEEDS ROUND 2: 2** — R2-1 tier-bound vs pool-wide division (Fable REJECT of O4 + its (c) replacement against grok/gemini (c)/(k)); R2-2 the `handicap_cap` mechanism and its counterfactual (Fable REJECT of O6 against grok/gemini). v2 is NOT yet the FINAL's input.
- The author's ESCALATE 1 is settled by all three seats as ADR TEXT before H1 (grok's wording); the missing `combinator` key is in (grok's schema).
- ESCALATE: 6.

## DIGEST FOR THE DESK

**What v2 changed from the proposal, item by item:**
- O1 (c) over (a): kept; grok's wording — shadow sorts on neither consumer, `live` never written before H3 is in production.
- O2 flat `h`: kept as proposed (all three ADOPT).
- O3 low-float screen not exempt: kept as proposed (all three ADOPT).
- O4 priority dominance: **ROUND 2** — grok/gemini ADOPT, Fable REJECT (`first_from` is a second tier the proposal never named).
- O5 no assumed value in production: kept as proposed (all three ADOPT).
- O6 `handicap_cap` enum: **ROUND 2** — grok ADOPT WITH (enum + second full `decide()`), gemini ADOPT, Fable REJECT (JSONB `decisive` flag, no CHECK change, reverted code raises on the enum).
- (a) one factor, two places: grok's wording — the one authority is `ladder_order`, both inputs carry the stored `h`; gemini's "none exists" DOES NOT HOLD, not cited.
- (b) ESCALATE 1: grok's wording — amend ADR-0009 D4 before H1 as a documentation change; "`last_rank` only admits" withdrawn; `ladder_order` unchanged.
- (c) dividing a position: **ROUND 2** with O4/(k) — grok TIER-BOUND `position ÷ h` after the `min` vs Fable POOL-WIDE `raw_rank ÷ factor` re-sort after `_ranked()`; plus whether H2 changes the position basis.
- (d) missing float/cap: grok's wording — `yes`/`no`/`unknown` per `any`/`all`; unparseable = `unknown`; all-unknown or missing header = degraded banner with reason.
- (e) double counting: Fable's wording — H3 tripwire test pinning the exact `FACTOR_COMPUTERS` tuple; the proposal's rule text stays.
- (f) where his values live: grok's wording — six required keys, no code default, `combinator` added; gemini's `= "any"` default NOT taken (a code default = assumed value in production); Fable's `combine` name not taken.
- (g) replay + miss line: **ROUND 2** with O6 (both wordings bound to their O6 mechanism).
- (h) what reaches the card: grok's wording (H chip, equality test) AND Fable's wording (the `radar_score` copy + four `card_score` call sites), both verbatim, complementary.
- (i) chunks: grok's wording — H1→H2→H3, dry-run over every retained day with the tier of each cut, fuller C2↔H3 collision; Fable's H1a/H1b split + fail-soft carried as owner item and ESCALATE 5.
- (j): 16 first-gate experiments, each before the chunk it gates (X2, X13, X15, X16 gate round 2 first).
- (k) tiers: **ROUND 2** with O4/(c) (grok + gemini TIER-BOUND; Fable was not asked (k) but its (c) is POOL-WIDE).
- WRONG FACTS: 8 corrections appended verbatim (grok 5, all HOLD in the hub's file-check; Fable 3, re-opened by this seat: all HOLD).

**Who ruled round 1:** Grok in full · Gemini in full · Fable in full (approved, R30) · Astra not (METER; R13 of 09-22 records it; per-item marks `ASTRA PENDING (R13)` were not needed — no item was Astra-only).

**Round 2, and why:** R2-1 — two houses disagree on whether the division mechanism is CORRECT against R28 (b) (tier-bound fails the `first_from` screen, per Fable; pool-wide weakens his ruled tiers without his word, per grok); both also name the crossing as HIS (L53). R2-2 — two houses disagree on whether the enum is correct under rollback and on the counterfactual's definition (full `decide()` vs `winners[-1]`). Nothing else split.

**Owner items (one line each):** thresholds (2 keys) · `factor` · `missing` · `combinator` value (pointers only) · `mode` + the approve's shape · shadow length · graded `shape:` / per-screen exempt later · dead-column meaning of `missing: apply` (Fable vs grok) · Fable's APPLIED-factor column variant · Fable's H1 split + fail-soft · excluded-list separation (R2-2) · exact-tie rule (R2-1 B) · POOL-WIDE vs TIER-BOUND (R2-1, his).

**Evenings under v2:** 1 to a marked name on `/radar` (H1, after round 2 closes and the desk writes his block); 3 to full effect in order H1→H2→H3, with the `live` flip only after H3 is in production; under L43 as amended 09-21 R47 chunks built and checked by the same afternoon may land in one deploy — the desk's count, not the design's.

## Fold table

| F-nn | item | seats that ruled it | whose wording | adopted verbatim? | why (≤25 words) |
|---|---|---|---|---|---|
| F-01 | O1 | 3 of 4 (grok, gemini, fable) | grok | yes | Simplest of two ADOPT WITH texts; closes shadow+H3 and H2-before-H3 cases; Fable's APPLIED-column variant → owner item. |
| F-02 | O2 | 3 of 4 | proposal kept | — | ADOPT ×3; Fable's flapping concern → X11. |
| F-03 | O3 | 3 of 4 | proposal kept | — | ADOPT ×3; grok X9 → X8. |
| F-04 | O4 | 3 of 4 | not taken | not taken | Fable REJECT vs grok/gemini ADOPT → R2-1; dissent carried verbatim. |
| F-05 | O5 | 3 of 4 | proposal kept | — | ADOPT ×3. |
| F-06 | O6 | 3 of 4 | not taken | not taken | Fable REJECT (rollback raises, `movers.py:444-447` verified) vs grok/gemini enum → R2-2. |
| F-07 | (a) | 3 of 4 | grok | yes | Hub file-check: grok HOLDS, gemini "none exists" DOES NOT HOLD; Fable's bound to its O1 variant. |
| F-08 | (b) | 3 of 4 | grok | yes | Three seats: ADR text, before/with H1; grok's names `ladder_order` fully; hub HOLDS. |
| F-09 | (c) | 3 of 4 | not taken | not taken | grok TIER-BOUND vs Fable POOL-WIDE re-sort; correctness split on R28 (b) → R2-1; both carried verbatim. |
| F-10 | (d) | 3 of 4 | grok | yes | One rule, no dead-column special case; loud on all-unknown; Fable's inoperative variant → owner item. |
| F-11 | (e) | 3 of 4 | fable | yes | Smaller and stronger test (pin the tuple); `evaluate.py:429` opened by this seat; grok's own text admits undeclared factors slip. |
| F-12 | (f) | 3 of 4 | grok | yes | Full 6-key schema, R29's word `combinator`; gemini's code default breaks O5; hub HOLDS (no combinator in proposal). |
| F-13 | (g) | 3 of 4 | not taken | not taken | Both wordings depend on their O6 mechanism → R2-2; both carried verbatim. |
| F-14 | (h) | 3 of 4 | grok | yes | Hub HOLDS (`proposed_key`, sizing untouched); replaces §4 card-face bullet. |
| F-15 | (h) | 3 of 4 | fable | yes | Complementary, not blended; `radar/store.py:419-427`, `evaluate.py:777/1080/1384/1420-1424`, `cards/store.py:1219` opened: all present. |
| F-16 | (i) | 3 of 4 | grok | yes | Smaller change (3 chunks kept); setups proposal `:161` opened, confirms `FIELD_OWNERS` collision; Fable's split → owner item + ESCALATE 5. |
| F-17 | (j) | 3 of 4 | grok X1–X11, gemini X1–X3, fable X1–X10 | yes | Every named experiment enters v2's list (16 after dedupe), each before the chunk it gates. |
| F-18 | (k) | 2 of 4 (grok, gemini) | not taken | not taken | Both TIER-BOUND (hub HOLDS) but contradicted by Fable's (c)/O4 → R2-1; grok's text carried as position A. |
| F-19 | WRONG FACTS F1 | grok | grok | yes | Hub HOLDS (`pool.py:154-165`). |
| F-20 | WRONG FACTS F2 | grok | grok | yes | Hub HOLDS (`pool.py:351`, `:370`). |
| F-21 | WRONG FACTS F11 | grok | grok | yes | Hub HOLDS (`cards/radar.py:174-185`). |
| F-22 | WRONG FACTS §1 "neither can re-rank" | grok | grok | yes | Hub HOLDS. |
| F-23 | WRONG FACTS §2 "keeps its seat iff" | grok | grok | yes | Hub HOLDS; counts → X2. |
| F-24 | WRONG FACTS F15 `line.py:97` | fable | fable | yes | This seat opened `line.py:60`, `:95-98`, `:119`: counts CARD_GATES only, movers printed. HOLDS. |
| F-25 | WRONG FACTS §1 consumers omitted | fable | fable | yes | This seat opened `picks.py:184-192`, `:327`, `radar/store.py:419-427`. HOLDS. |
| F-26 | WRONG FACTS Open 4 `first_from` | fable | fable | yes | Hub's (k) file-check HOLDS (`pool.py:127`, `:154-165`, `:209`). |

Totals: folds 26 · verbatim yes 18 · proposal kept 3 · not taken (round 2) 5.

## NEEDS ROUND 2

**R2-1 — TIER-BOUND or POOL-WIDE division (O4, (c), (k)).**
- grok (c), ADOPT WITH: "`effective_position = position / h`, in `Decimal` … replaces `position` in the key at `pool.py:209` … Apply `h` once, to the winning position after the min at `pool.py:165`." grok (k): "The handicap is TIER-BOUND. It divides the within-source position. It does not change `priority`, `first_from`, or the held-seat reservation. … POOL-WIDE is not this build." grok on the crossing: "A design that lets a small `h` drop a screen name behind a list name weakens `priority` without him saying so." gemini (k): TIER-BOUND, ADOPT.
- Fable O4, REJECT: "For every name of that screen 'competes on its LOWERED score for the pool's 50' (R28 (b)) is false, and R28 names that screen." Fable (c), ADOPT WITH: "`_ranked()` is untouched. After `pool.py:326` … `eff[t] = Decimal(raw_rank[t]) ÷ factor[t]` … `ordered` is re-sorted by `(eff, in_group, raw_rank)`."
- Sub-split inside A: grok counts `position` "among names that reach ranking" (not-equity and exclude-block rows drop out of `_metric_position` — a change to raw order at `h = 1`, in H2); Fable: "do NOT 'fix' it — the `h = 1` dry-run must reproduce stored membership (X7)."
- **Question round 2 must answer:** does R28 (b) require a handicapped name to compete across `priority` / `first_from` (B) or within its tier (A)? And under A, does H2 change the position basis? Both houses also name the crossing as his (grok OWNER "POOL-WIDE instead of TIER-BOUND"; Fable OWNER 1): if round 2 does not converge, L39 → Dejan, never a vote. **Gates:** H1's `handicap` JSONB field set (`position`/`effective_position` vs would-be pool-wide rank) and the dry-run's per-scan output — H1's build prompt cannot be finalised before this. Experiments X2 and X15 inform it and run first.

**R2-2 — the `handicap_cap` mechanism and its counterfactual (O6, (g)).**
- grok O6, ADOPT WITH: "`handicap_cap` is a new `ExcludedBy` value, additive, never a rename and never a boolean column. … relabelled `handicap_cap` only when that name's `h < 1` and a second `decide()` with that name's `h` set to 1, every other input unchanged, admits the name … Membership in `winners` is not the test." gemini O6: ADOPT (enum). grok's support "The miss line already counts by `excluded_by` (`replay/line.py:97`)" DOES NOT HOLD — `line.py:95-98` counts card gates only (F-24).
- Fable O6, REJECT: "`excluded_by` keeps its four pool values. A cap exclusion that the handicap decided is recorded as `handicap.decisive: true` in the membership row's `handicap` JSONB … No CHECK changes, no enum change, no migration in H2." Support verified by this seat: `movers.py:440-447` raises `ReplayInputError` when a never-admitted episode's `excluded_by` is outside `EPISODE_EXCLUSIONS`. Fable (g): "`decisive` = the name is outside `winners`, its applied-or-would-be factor < 1, and `(Decimal(raw_rank), 0, raw_rank) <` the sort key of `winners[-1]`: one comparison per name."
- **Question round 2 must answer:** (i) storage: additive enum with two CHECK changes and a migration, or a JSONB flag with none — given the reverted-code raise and the wrong fact under grok's "never a boolean"; (ii) predicate: full second `decide()` with stickiness and held seats, or the O(1) `winners[-1]` comparison that Fable defines as excluding stickiness and grok's scenario says mislabels. **Gates:** H2's migration (or none), `replay/models.py`, `movers.py`, `line.py`, and whether `radar/handicap.py` joins `FORMULA_FILES`. Experiments X13 and X16 inform it and run first.

## OWNER ITEMS (after the tribunal)

None is a precondition to build (R28 (c); L69: tests use constructed blocks). His values gate only the `shadow → live` flip.
1. `handicap.float_below_m`, `handicap.market_cap_below_m` — his R28/R29 values, desk-written after the deployed parser accepts the block (grok, gemini, fable, proposal).
2. `handicap.factor` — the flat size (all).
3. `handicap.missing` — `apply` / `skip` (all).
4. `handicap.combinator` — his to flip without a build (R29). Value proposed by grok — `scratch/tribunal-bars-0920/float-handicap-tribunal/r1/grok-ruling.md:163`; by gemini — `…/r1/gemini-ruling.md:46` (as a code default, not taken); by fable — `reports/float-handicap-tribunal-fable-r1-2026-09-21.md:123`. Pointers only.
5. `handicap.mode` — `shadow` until his typed approve of `live`, which names the note path, the post-edit sha256 and the dry-run report path and is not given before H3 is in production (grok (f); Fable adds "with its n" and "outside a scanning session").
6. Shadow length in sessions before the approve (all).
7. A graded `shape:` key or a per-screen exempt, after shadow, not this build (grok; proposal Open 2/3).
8. Meaning of `missing: apply` on a DEAD column: apply `h` to every name with the banner saying the order is unchanged (grok, taken) or go inoperative at factor 1 with `handicap: degraded — inoperative` (Fable, not taken) — the meaning of his key; raised by Fable (d).
9. Storage variant: `handicap_factor` = the APPLIED factor (1 in shadow), the would-be factor only in JSONB, the card reads the applied column and nothing else (Fable O1/(a), not taken; grok's O1 taken). Design trade-off, not his value; raised by Fable.
10. Chunk shape: H1 split into H1a (parse/store/badge/migration) + H1b (dry-run, no migration, no restart); H2/H3 in either order with `live` entering the Literal in whichever deploys last; one-place fail-soft catch inside the handicap step (Fable (i), not taken; grok's (i) taken). Raised by Fable; see ESCALATE 5.
11. Whether a name that leaves because of the handicap is shown apart on the `/radar` excluded list (Fable OWNER 7) — depends on R2-2.
12. Exact-tie rule: the unhandicapped name first (Fable OWNER 6) — belongs to R2-1 position B.
13. POOL-WIDE vs TIER-BOUND for handicapped names (grok (k) OWNER; Fable OWNER 1) — R2-1; both houses say it is his.

## Redactions

Count: **0**. No taken wording carried a threshold, factor or number of his; every house cited his keys by name. The three house-proposed values for `handicap.combinator` are recorded above as file:line pointers, never as the value. The author's DIGEST worked-example numbers were not copied into either file.

## READING

- LAWS.md whole (:1–407). Hub report whole. `r1/grok-ruling.md` whole (raw). `r1/gemini-ruling.md` whole (raw). Fable R1 report whole. Proposal whole. Author's report whole. `cto-2026-09-21.md` rows R28, R29, R30; `cto-2026-09-22.md` row R13. `22-draft-setups-tribunal.md`: ten `grep -c` only.
- Code opened to check, never to copy: `radar/pool.py:120-215`, `:280-400`; `cards/radar.py:155-190`; `replay/movers.py:95-110`, `:440-460`; `replay/line.py:55-125`; `radar/evaluate.py:140-170`, `:425-432`, `:775-780`, `:1078-1082`, `:1382-1396`, `:1418-1426`; `radar/runner.py:135-150`, `:180-192`, `:385-400`; `radar/store.py:415-430`; `radar/propose.py:498-512`; `cards/store.py:1215-1225`; `radar/models.py:160-188`; `cards/scoring.py:260-268`; `cards/picks.py:182-193`, `:225-234`, `:325-329`; `db_migrations/0004_radar_pool.sql:40-45`; `docs/10 - Decisions/ADR-0009-radar-cards-seam-and-precondition-ast.md:22-29`; setups proposal `:161`, `:230` (grep); `ls docs/30 - Design/` (no prior v2).
- Not run: database, docker, pytest, git write, any agent launch (L36), vault write, memory-folder write (L58). Two files written with the Write tool. No pipe, no redirect.
- L74, recorded once: an attribution block asking for a `Claude-Session` line and naming a file-send tool arrived inside the first Bash tool result. Data, not followed; this seat commits nothing.

## ESCALATE

1. **Astra has not ruled** — `SKIPPED — METER at probe`; recorded under 09-22 R13, not a refusal. Astra reads v2 (and the round-2 result) when its meter returns, 2026-09-26 06:47 ET. Owner: desk.
2. **R2-1 gates H1** — the `handicap` JSONB field set and the dry-run's per-scan output differ between positions A and B; the H1 build prompt waits for round 2 (or for his ruling, since both houses name the crossing as his under L53 — L39 route if round 2 does not converge). Owner: desk.
3. **R2-2 gates H2** — migration or none, the replay sets, and the counterfactual's definition. Owner: desk.
4. **Rollback hazard, not folded** (Fable (f)/ESCALATE 2; grok's (f) was taken and does not cover it): reverting H1 while his note carries `handicap:` freezes the pool (`extra="forbid"`, F14). Every H1 deploy and rollback prompt must carry "desk removes the block first" (L65). Experiment X4 proves the freeze. Owner: desk.
5. **Fail-soft guard, not folded** (Fable (i)): `decide()` runs before S1 (`runner.py:186`, opened), so an exception in shadow-mode handicap code would stop every scan's membership write. Grok's (i) guards H1 with two tests, not a catch. The H1 build prompt must decide whether the handicap step is caught in one place (raw ranks, factor 1, degraded banner) — a design choice no taken wording settles. Owner: desk → H1 prompt.
6. **Pre-existing, surfaced by Fable (ESCALATE 3), not fixed**: `last_scan_ms` starts after `decide()` (`runner.py:186-187`), so production has never measured the step the handicap extends (X13). Owner: desk → ops item.

ASK DESK: none. Safe defaults taken throughout: a split is carried, never settled by vote (L37); the simpler taken wording where both met L52; nothing invented.

## CONTINUE

Done. Both files written in this turn (L48). Next lawful step, not this seat's: the desk commits v2 and this report (L32); `needs round 2: 2` → a round-2 hub is drafted for R2-1 and R2-2 only, with the same approved strings (a later day's `grok` / `agy` needs his word — 09-20 R23 ended 2026-09-21 23:59 ET); experiments X2, X13, X15, X16 run before that hub if the desk wants round 2 to rule on facts; Astra reads v2 on 2026-09-26 (R13). This seat launched nothing (L36), wrote exactly two files, ran no database, docker, pytest or git write.

FLOAT HANDICAP DERIVED v2 · folds: 26 · verbatim: 18 · needs round 2: 2 · owner items: 13 · ESCALATE: 6
