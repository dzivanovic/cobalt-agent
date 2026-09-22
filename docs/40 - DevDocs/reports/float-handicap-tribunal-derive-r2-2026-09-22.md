# Float handicap tribunal — derive round 2 (v3) — 2026-09-22

Seat: `float-handicap-tribunal-derive-r2-0922` · model: claude-fable-5-1 (row R30, `cto-2026-09-21.md:41`, committed `323ce51`) · prompt: `prompts/2026-09-22/21-handicap-tribunal-derive-r2.md` · run 11:54–12:06 ET

## §0 Headline

- v3 written: `docs/30 - Design/FLOAT-HANDICAP-v3-2026-09-21.md` — v2 whole, 4 questions folded (`[R2F-01]`–`[R2F-04]`), 3 house wordings taken verbatim, 0 values of his, `ASTRA PENDING (R13)` in the header and at every fold.
- **R2-2 CONVERGED** (both questions, 3 of 3 seats): storage = Fable's round-1 O6 replacement (JSONB `handicap.decisive`, no enum, no CHECK, no H2 migration); counterfactual = grok's round-1 O6 predicate (a second full `decide()`, stickiness and held seats included). **H2's miss-line half is unblocked.**
- **R2-1 OPEN FOR DEJAN** — R2-1.1: grok `ADOPT B`, gemini `OWNER`, Fable `OWNER`; a house answered `OWNER` → his (L53), never settled by count. R2-1.2 converged (`_metric_position` stays). **H1 is NOT unblocked**: it waits on his ONE A/B (tier-bound or pool-wide); the houses' named default if he says nothing is A.
- No `DO NOT BUILD` → no round 3 (L39). Astra `SKIPPED — METER at probe` (R13): reads the FINAL Sat 2026-09-26.
- ESCALATE: 6 (one `ASK DESK`).

## DIGEST FOR THE DESK

- **R2-1 (gates H1): OPEN FOR DEJAN.** R2-1.1 split in kind — grok pool-wide (`ADOPT B`, withdrawing its own round-1 tier-bound), gemini and the Fable seat `OWNER` (both: build A if he is silent). Both seats' scenarios HOLD in the hub's file-check (C1–C3, `pool.py:326`, `:332-333`); it is a choice between two of his rulings (R28 (b) vs the pool block's `priority` / `first_from`). R2-1.2 converged `ADOPT B` ×3: `_metric_position` unchanged, the `h = 1` dry-run must reproduce stored membership — Fable's round-1 sentence, verbatim `[R2F-02]`.
- **R2-2 (gates H2): CONVERGED.** R2-2.1 `ADOPT B` ×3 → `[R2F-03]` Fable's round-1 O6 replacement verbatim (grok withdrew the enum; revert raise `movers.py:444-447` HOLDS C4; `line.py:97` HOLDS C6). R2-2.2 grok `ADOPT WITH` / gemini `ADOPT A` / Fable `ADOPT A`, hub: same mechanism → `[R2F-04]` grok's round-1 O6 predicate verbatim (stickiness walk HOLDS C8). Grok's two round-2 riders NOT taken: "pool-wide re-sort" presupposes the open R2-1.1; the `FORMULA_FILES` addition is split with the Fable seat (ESCALATE 4).
- **H1: not unblocked** — the meaning of `handicap.position` / `effective_position` and the dry-run's per-scan lines differ between A and B (field NAMES are the same under both). Waits on his answer. **H2: miss-line half unblocked** (no migration, no CHECK change); its division half waits on R2-1 and on H1's columns.
- **Seats that ruled round 2:** Grok (all four), Gemini (all four), Fable seat (all four, blind); Astra SKIPPED (R13).
- **Owner items:** 13, updated (below). R2-1 is now the one that needs his word BEFORE H1's build prompt (not a value; a crossing of his tiers). Gemini's closing line makes it a precondition in words — not taken as such (ESCALATE 3), but under this derive's own rule H1 waits on the open item either way; the fastest path is one A/B message.
- **Evenings under v3:** 1 to a marked name on `/radar` (his A/B → H1's evening → the desk writes his block → next scan); 3 to full effect (H1 → H2 → H3, `live` flip after H3 is in production, no deploy for the flip); under L43 R47 chunks built and checked by the same afternoon may land in one deploy.
- **L52:** (a) MET, (b) MET, (c) NOT MET until his R2-1 answer (the JSONB field set is settled in names, split in meaning), (d) MET.
- **Next, not this seat's:** the desk commits v3 and this report; brings him ONE A/B (§1 of v3, the two cost lines); on his answer an Opus seat drafts the H1 build prompt (X2 runs first — it is his evidence); Astra reads v3 Sat 09-26.

## Fold table

| R2F-nn | question | seats that ruled it | answers | whose wording | adopted verbatim? | why (≤25 words) |
|---|---|---|---|---|---|---|
| R2F-01 | R2-1.1 | 3 (grok, gemini, Fable) | grok `ADOPT B` · gemini `OWNER` (A if silent) · Fable `OWNER` (A if silent) | none | not taken | A HOUSE answered `OWNER` → OPEN FOR DEJAN (L53). Both claims HOLD (hub C1–C3, rows `pool.py:326`, `:332-333`) — two readings of his rulings. |
| R2F-02 | R2-1.2 | 3 (grok, gemini, Fable) | `ADOPT B` ×3 | Fable, round-1 (c) sub-question (1) | yes | Unanimous, two houses. `_metric_position` over `source.tickers` HOLDS (hub row `pool.py:94-106`, C3); a basis change breaks X12's `h = 1` parity. |
| R2F-03 | R2-2.1 | 3 (grok, gemini, Fable) | `ADOPT B` ×3 | Fable, round-1 O6 replacement | yes | Unanimous; grok withdrew its enum. Revert raise HOLDS (C4, hub `movers.py:102`/`:444-447`); `line.py:97` HOLDS (C6); episode entries HOLD (C7). |
| R2F-04 | R2-2.2 | 3 (grok, gemini, Fable) | grok `ADOPT WITH` · gemini `ADOPT A` · Fable `ADOPT A` | grok, round-1 O6 predicate | yes | Hub per-item summary: same mechanism. Stickiness walk HOLDS (C8, `pool.py:332-378`); `winners[-1]` undefined at `seats = 0` HOLDS. Grok's r2 riders not taken. |
| R2F-05 | rider inside R2-2.2: `FORMULA_FILES` | 2 (grok, Fable); gemini silent | grok: add the module that computes `h` · Fable: it does not join | none | not taken | Not a question asked; split house vs seat; C9 HOLDS for both. v3 leaves `FORMULA_FILES` as today; both sentences carried verbatim. ESCALATE 4. |
| R2F-06 | v2 `## Dissents` — the Fable seat's WITHDRAWN round-1 sentences | Fable (round-2 `## Withdrawn from round 1` 1–7) | — | — | struck (~~…~~), annotated, never deleted | Fable r2 ESCALATE 2: a wrong fact of its own carried verbatim in v2 (`:295-297`); `0005 rollback:36-41`, `0006 rollback:47-49` cited instead; X16 marked MOOT under R2F-03. |

Totals: questions 4 · converged 3 (R2-1.2, R2-2.1, R2-2.2) · open for Dejan 1 (R2-1.1) · house wordings taken verbatim 3 · riders not taken 1 (split) · items converged 1 of 2.

## OPEN FOR DEJAN

**R2-1 — TIER-BOUND or POOL-WIDE division (one item; R2-1.1 is the open question; R2-1.2 converged and binds both answers: `_metric_position` stays as it is).**

**A — TIER-BOUND, grok (round-1 item (c), ADOPT WITH; item (k)); gemini round 1 ADOPT (c), (k):** "`effective_position = position / h`, in `Decimal`, quantized to the `handicap_factor` scale (`NUMERIC(6,4)`), replaces `position` in the key at `pool.py:209`. `position` is the 1-based place among names that reach ranking. On a screen that is `_metric_position` over `source.tickers` minus not-equity and minus the exclude block. On a list group it is the existing union index over candidates (`pool.py:179-206`). Apply `h` once, to the winning position after the min at `pool.py:165`. `rank_value` stays the raw metric. Stickiness and `below_cap_streak` are unchanged. A tie on the quantized position breaks by `note_order`, then `ticker`." — and grok item (k): "The handicap is TIER-BOUND. It divides the within-source position. It does not change `priority`, `first_from`, or the held-seat reservation. A handicapped name in an earlier tier still beats every name in a later tier, whatever `h` is. POOL-WIDE is not this build. Tiers, and what `h` does to each: (1) `priority`, key component 0, `pool.py:127` and `:209`, `radar-models.py:104-112` — inert for which group a name is in; active only for order inside the group. (2) `first_from`, key component 1 inside screens, `pool.py:154-165` and `:209`, `radar-models.py:78-88` and `:113-115` — after the clock, the one screen that set it sorts ahead of other screens; `h` does not cross that. Before the clock every screen has `first = 1` and the tier is flat. (3) Held members, `pool.py:283-286`, `:312-321`, `:323-324`, `:380-384` — a name whose only live source is degraded keeps its prior seat and is not re-ranked; `h` is inert. (4) Stickiness, `pool.py:336-378` — not a tier `h` may cross; `h` does change who is evicted, because the victim is the worst newcomer by the handicapped rank. The grace count is his `stickiness_scans`, unchanged. (5) Removals before ranking — manual exclude, not-equity, screen-inactive — `pool.py:269-309`; `h` never sees those names." (Under A, the basis clause "among names that reach ranking … minus not-equity and minus the exclude block" is NOT built — R2-1.2 converged on `[R2F-02]`.)

**B — POOL-WIDE, Fable (round-1 item (c), ADOPT WITH replacement); grok round 2 `ADOPT B`:** "`_ranked()` is untouched. After `pool.py:326`, when the block is present: `eff[t] = Decimal(raw_rank[t]) ÷ factor[t]` (`factor` = `handicap.factor` for an in-group name, 1 otherwise; a `Decimal` field, never a float); `ordered` is re-sorted by `(eff, in_group, raw_rank)` — on an exact tie the unhandicapped name wins; `ranks` is rebuilt from that order. In `mode: shadow` the re-sort is computed, stored as the would-be rank and NOT used. `raw_rank` and `rank` both ride the `Transition`. The group values come from the source `source_for[ticker]` names."

**Each seat's reason, one sentence, with its file:line:**
- grok (`ADOPT B`): "If `N ≤ seats` (`pool.py:332-333`) every one of those names is in `winners` whatever `handicap.factor` is, so under A it did not earn the seat." — and it names B's cost itself: a small factor places a screen name behind a list name after the re-sort at `pool.py:326`, "the requirement, not a defect … Named here, not silent (L53)."
- gemini (`OWNER`): "Since both choices compromise a requirement, only he can weigh the tier breach against the penalty's bite. If silent, I build A to strictly preserve his L53 tiers." (`pool.py:161`, `:209`)
- Fable seat (`OWNER`): "the two readings choose between two of his rulings, R28 (b) and the pool block's `priority` / `first_from`; whichever mechanism is built decides it, and a mechanism that weakens `priority` or `first_from` without his word is his item by name" (`pool.py:161-165`, `:209`) — "H1 builds A if he says nothing."

**The desk's A/B to bring him, one line each, cost in his terms:**
- **A — TIER-BOUND:** a handicapped name on the `first_from` screen (and any screen name while all screen names together number fewer than `cap − held`) can never lose its seat to a list name or to another screen, whatever the factor — the handicap only reorders it inside its tier.
- **B — POOL-WIDE:** a list name can overtake a handicapped screen name, and after `first_from` another screen's name can overtake a handicapped `first_from` name — his `priority` and `first_from` weakened for handicapped names only, without a word in his pool block.

**The one line he answers:** may a handicapped name fall behind a list name, or behind another screen's name after `first_from`? Yes = POOL-WIDE (B); no = TIER-BOUND (A).

**What waits on his answer:** H1's `handicap` JSONB meaning of `position` / `effective_position` (within-source position and its division under A; the would-be pool-wide rank under B — same field names either way) and the dry-run's per-scan lines; H2's division in `pool.py`. **Default the houses named if he says nothing before H1:** A (gemini; the Fable seat also A); grok named no default (its ruling is B). `raw_rank` (the `_ranked()` index, no factor) is stored under either answer, so the other reading stays recomputable in the dry-run. Never a vote; not this seat's preference.

## NEEDS ROUND 3

none — no house said `TRIBUNAL R2: DO NOT BUILD`.

## OWNER ITEMS (after the tribunal)

None of his VALUES is a precondition to build (R28 (c); L69: tests use constructed blocks). Item 13 is a design crossing of his tiers, not a value — it is the OPEN FOR DEJAN block above and H1's build prompt names its answer.
1. `handicap.float_below_m`, `handicap.market_cap_below_m` — his R28/R29 values, desk-written after the deployed parser accepts the block (grok, gemini, fable, proposal; grok r2, gemini r2 OWNER 2 restate).
2. `handicap.factor` — the flat size, after the H1 dry-run (all; gemini r2 OWNER 2).
3. `handicap.missing` — `apply` / `skip` (all; grok r2, gemini r2 OWNER 4).
4. `handicap.combinator` — his to flip without a build (R29); gemini r2 OWNER 3 calls it `combine` — the key is `combinator` ([F-12]). Values proposed by pointer only: grok `…/r1/grok-ruling.md:163`; gemini `…/r1/gemini-ruling.md:46`; fable `reports/float-handicap-tribunal-fable-r1-2026-09-21.md:123`.
5. `handicap.mode` — `shadow` until his typed approve of `live`, naming the note path, the post-edit sha256 and the dry-run report path; not before H3 is in production (grok (f); grok r2 OWNER 2; Fable adds "with its n" and "outside a scanning session").
6. Shadow length in sessions before the approve (all; gemini r2 OWNER 5).
7. A graded `shape:` key or a per-screen exempt, after shadow, not this build (grok; proposal Open 2/3).
8. Meaning of `missing: apply` on a DEAD column: apply `h` to every name with the banner saying the order is unchanged (grok, taken) or go inoperative at factor 1 (Fable, not taken) — the meaning of his key; raised by Fable (d). Unchanged by round 2.
9. Storage variant: `handicap_factor` = the APPLIED factor (1 in shadow), the would-be factor only in JSONB (Fable O1/(a), not taken; grok's O1 taken). Design trade-off, raised by Fable. Unchanged by round 2.
10. Chunk shape: H1 split into H1a/H1b; H2/H3 in either order; one-place fail-soft catch (Fable (i), not taken; grok's (i) taken). Raised by Fable; ESCALATE 6.
11. Whether a `decisive` name is shown apart on the `/radar` excluded list beyond the `config_cap (handicap)` suffix (Fable r2 OWNER 4; gemini r2 OWNER 7) — under `[R2F-03]`.
12. Exact-tie rule: the unhandicapped name first (Fable OWNER 6; gemini r2 OWNER 6) — lives inside position B's text; moot under A.
13. **POOL-WIDE vs TIER-BOUND** (grok r1 OWNER; Fable OWNER 1; gemini r2 OWNER 1; gemini r2 R2-1.1 `OWNER`; Fable r2 R2-1.1 `OWNER`) — the OPEN FOR DEJAN block; his ONE A/B before H1's build prompt.

## Redactions

Count: **0**. No taken wording carries a threshold, factor or number of his; every seat cited his keys by name. The hypothetical constants inside the carried round-2 scenarios (`cap = 3`, `cap = 50`, 45 held, factor 0.9 / 0.4, `stickiness_scans = 3`) are the houses' scenario values, not read from his note; "the pool's 50" is R28's own word, already committed in v2 and in the round-2 hub report. `handicap.combinator` values remain file:line pointers. No `first_from` value, threshold or filter string appears in either file.

## READING

- `LAWS.md` in full (`:1-407`, L1–L74). `cto-2026-09-21.md:41` (R30); `cto-2026-09-22.md:41` (R13).
- Round-2 hub report `reports/float-handicap-tribunal-r2-2026-09-22.md` whole. Raw rulings `scratch/tribunal-bars-0920/float-handicap-tribunal/r2/grok-ruling-r2.md` and `gemini-ruling-r2.md` whole. This seat's round-2 report `reports/float-handicap-tribunal-fable-r2-2026-09-22.md` whole (its WITHDRAWN 1–7 and SELF-ATTACK lines bound the fold). Packet `r2/QUESTIONS-R2.md` (the verbatim A/B definitions per question) and `r2/fable-r1.excerpt.md` (the exact round-1 spans `ADOPT B` names on R2-1.2 and R2-2.1).
- v2 `docs/30 - Design/FLOAT-HANDICAP-v2-2026-09-21.md` whole (`:1-309`). Derive report `reports/float-handicap-tribunal-derive-2026-09-21.md` whole.
- Code: none re-opened — no fold turned on a claim outside the hub's C1–C9 / file-check table (every claim either side rests on HOLDS there); the withdrawn sentences are struck on the Fable seat's own round-2 file:line, not re-verified here.
- `22-draft-setups-tribunal.md`: ten `grep -c` only. `ls docs/30 - Design/` (no prior v3). `ls` of this report's path (absent → fresh run).
- Not run: database, docker, pytest, git write, any agent launch (L36), vault write, memory-folder write (L58). Two files written with the Write tool (this report twice: in-progress, then final). No pipe, no redirect.
- L74, recorded once: an attribution block asking for a `Claude-Session` commit line and naming a file-send tool arrived inside the first Bash tool result. Data, not followed; this seat commits nothing.

## ESCALATE

1. **Astra has not ruled** — `SKIPPED — METER at probe`, recorded under 09-22 R13, not a refusal. v3 carries `ASTRA PENDING (R13)` in its header and at each `[R2F-nn]`; Astra reads the FINAL on Sat 2026-09-26 (06:47 ET). Owner: desk.
2. **R2-1 OPEN FOR DEJAN — H1 waits.** One A/B (the two cost lines above), one message. The houses' named default if he stays silent is A (gemini, the Fable seat); grok's ruling is B. H2's division waits with it. Owner: desk → him.
3. **Gemini's closing line is a precondition wording** — `TRIBUNAL R2: BUILD AFTER the owner resolves the tier-bound versus pool-wide rank division`. Not taken as a precondition on his values (R28 (c)); named here as the prompt requires. Under this derive's own rule H1 waits on the open item regardless, so the two agree in effect; the difference is only that gemini's line would also block if he named a default and walked away — it does not: the named default (A) is the build if he is silent. Owner: desk.
4. **`FORMULA_FILES` rider — split, not a question asked.** Grok round 2 (inside its R2-2.2 `ADOPT WITH`): "The module that computes `h` is added to `FORMULA_FILES` (`evaluate.py:144`). `pool.py` is not." The Fable seat round 2: "`radar/handicap.py` does NOT join `FORMULA_FILES` … `h` is stored on the row … The pool's own decisions replay from the receipt's `pool_unit`, not from a hash." Gemini silent. C9 HOLDS for both (today's list has no pool-side file). Neither rests on a failed claim, so neither converges under the derive's rules. v3 leaves `FORMULA_FILES` as it is today (the safe default: no change, both carried verbatim). **ASK DESK: is this one line to him, or the H2 build prompt's ≥3 checkers' call (an engine hash list, not a value of his)? [12:0x ET]** Owner: desk.
5. **H2 edit-site count not hub-checked.** Grok r2: "Two edits: the episode JSON in `movers.py` and `line.py:119`." The Fable seat r2: six — `replay/models.py:409` (`Episode` gains `handicap`; `extra="ignore"` otherwise drops the column silently), `radar/store.py:55-58` (`members_for_day` selects it), `movers.py:452-458`, `line.py:119`, `replay/runner.py:367`, `aset/radar_panel.py:832`. Same mechanism, different price; the H2 build prompt opens each site. Owner: H2 prompt author.
6. **Carried from the v2 derive, still open (ESCALATE 4–6 there):** the H1 rollback hazard (revert with `handicap:` in his note freezes the pool, F14; every H1 deploy/rollback prompt carries "desk removes the block first", L65; X4 proves it); the fail-soft guard (`decide()` runs before S1 at `runner.py:186`; the H1 prompt decides whether the handicap step is caught in one place); `last_scan_ms` starting after `decide()` (`runner.py:186-187`; X13 cannot use production's figure). Owner: desk → H1 prompt / ops.

## CONTINUE

Done. Both files written in this turn (L48). Next lawful step, not this seat's: the desk commits v3 and this report (L32); `open for Dejan: 1` → the desk brings him the ONE A/B in `## OPEN FOR DEJAN` (one message), and H1's build prompt (Opus seat, ≥3 checkers, L67) is drafted on his answer — X2 runs first, it is his evidence; R2-2 being converged, the H2 prompt's miss-line half can be drafted from `[R2F-03]` / `[R2F-04]` in parallel (L72) while its division half waits; Astra reads v3 on Sat 2026-09-26 (R13). This seat launched nothing (L36), wrote exactly two files, ran no database, docker, pytest or git write.

FLOAT HANDICAP DERIVED v3 · converged: 1 of 2 · open for Dejan: 1 · owner items: 13 · ESCALATE: 6
