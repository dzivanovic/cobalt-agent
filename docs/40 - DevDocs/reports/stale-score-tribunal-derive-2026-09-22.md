# Stale-score tribunal — derive (v2) — 2026-09-22

Seat: `stale-score-tribunal-derive-0922` · model: claude-fable-5-1 (the Fable seat's second job, row R51 of `cto-2026-09-21.md`, `derive seat: claude-fable-5-1`) · `date`: Tue Sep 22 13:32:19 EDT 2026 · main read at `3ceb469` (three code ranges only, named below).

## §0 Headline
- **v2 written:** `docs/30 - Design/STALE-SCORE-v2-2026-09-22.md` — option C stands; 21 folds, 11 house wordings taken verbatim (10 Grok/Gemini, 1 Fable on a derive read), the rest the proposal's text kept.
- **Round 2: EMPTY.** No house said `DO NOT BUILD` or `REJECT`; no two houses disagree on whether a mechanism is correct. The tribunal closes; v2 is the FINAL's input.
- **Astra did not rule** (`METER`, recorded under `cto-2026-09-22.md` R13, not a refusal): every item is 3 of 4 (Grok, Gemini, Fable); Astra reads v2 when the Codex meter returns, Sat 2026-09-26 06:47 ET.
- **Owner items: 9**, none a precondition to build; `## FOR DEJAN` carries each as one A/B, no recommendation from this seat (L37).
- ESCALATE: 5. Authorization verified (R51 committed `be58530`; hub stop line `5f8d6ea`; Fable stop line `be4c79b`; the ten launch strings each count 1 in `22-draft-setups-tribunal.md`).

## DIGEST FOR THE DESK
- **Seats, round 1:** Grok — in full. Gemini — in full (its (a)–(k) carry no ADOPT tag; substance counted, hub format note stands). Fable — in full, blind, approved (R51). Astra — not (METER, R13).
- **Q1 sink/hold:** proposal kept, sink; 3-0. Hold = owner item 1.
- **Q2 clock every session:** proposal kept; 3-0. RTH-only = owner item 2; thin-ticker gap-minutes = X24.
- **Q3 band:** Grok's wording verbatim replaces the proposal's wrong "200 s vs 180 s" sentence (band ≈80 s of open-age; hub HOLDS). Fable's wording same fact, not taken (this seat's own; quotes tunable values). Clocks meeting = owner item 3.
- **Q4 keep stale `last`:** proposal kept; 3-0.
- **Q5 pills:** own item; 3-0. Owner item 6.
- **Q6 tap while stale:** Grok's step-7 wording verbatim — `tap_dot` writes the stored sentence back, `PROXIMITY_UNKNOWN` only as fallback; hub HOLDS the reason drop at `store.py:1218/1222`. Meets Gemini's closing condition.
- **Q7/(g) L7 stats:** proposal's step 5 kept (forward stop); past rows his before any promotion, never before build. Grok leave / Gemini exclude / Fable his = owner item 4; X21 and X25 attached. Fable's Q7 wording not taken (UNCHECKED; mechanism already the proposal's).
- **Q8/(f) version:** Grok's Q8 wording verbatim — same-deploy ride only, else a separate bump; audit-export version gate (hub HOLDS: no receipt-version check today). Gemini and Fable rule the same gate; Fable's text not taken (cites `s2p2.2`, `radar/store.py:460-465` UNCHECKED).
- **Q9 tie-break:** not a precondition; 3-0. Owner item 5.
- **Q10/(e) the field:** Fable's (e) wording verbatim — required, no default, computed at `evaluate.py:502` before the `not_evaluable` return. UNCHECKED by a hub; read by the derive at `evaluate.py:502`, `:517-524`, `:529-534`: the early return precedes the flag, so Grok's "set from the local already computed at `:527-534` on every `result()` path" is not satisfiable on that path (Grok's own text names the cut region). Same rule in all three: guard on the field, never the label.
- **(a) fact base:** Grok's correction verbatim (W19 → `:998`/`:1023`, W21 UNVERIFIED, W22 `audit_export.py:363`); Gemini's W12 writer sentence verbatim (`radar/store.py:423-425`). Fable's W23–W25 not taken (UNCHECKED, not needed).
- **(b) helper:** Grok's `score_last` wording verbatim; the proposal's "all five paths already handle null" premise withdrawn (hub HOLDS: only `card_score()` tolerates None). Derive read `evaluate.py:1384`: create passes `last=ev.last_price`; the helper changes no formation number.
- **(c) ESCALATE 1:** placed INSIDE this design by all three; Grok's delete-three-fallbacks wording verbatim. Fable's WATCH-impact claim (FC9 UNVERIFIABLE) → X23.
- **(d) clock:** proposal kept; replay `as_of` soundness UNVERIFIABLE → X10.
- **(h) what he sees:** proposal kept; two messages + sink, 3-0; rendering lag → X29; re-render every scan = owner item 7.
- **(i) ESCALATE 4:** stays OUTSIDE (proposal, Grok, Gemini); step 8 scoped to NULL proximity. Fable's widening not taken — Fable's own text accepts step 8 alone; carried as owner item 9 with both costs.
- **(j) chunks/order:** Grok's wording verbatim (S1/S2 one branch, Opus 5 floor, no migration, off main after C1 lands, before `A-01`; stamp not a predecessor). Branch fact corrected everywhere: C1 = `58aa823` on `setups/seven-0921` (hub HOLDS). Fable's stacked-tree alternative stated as the desk's lane (L68), not ruled here.
- **(k) experiments:** X1–X9 as Grok leaves them (X1 ttl+1, X4 version refusal, X5 split a/b), X10–X22 Grok verbatim, X23–X29 Fable's X10–X16 verbatim renumbered; each placed before the chunk it gates; every UNVERIFIABLE row is an X.
- **Fable claims:** 9 hub-checked (8 HOLD, FC9 UNVERIFIABLE); 7 Fable wordings rest on claims the hub did not check (Q7, Q8, (e), (f), (i), (j), (a) W23–W25) — 1 read by the derive and taken ((e)), 6 not taken.
- **Round 2:** nothing. No `DO NOT BUILD`, no correctness split.
- **Owner items (9):** 1 hold vs sink · 2 RTH-only score clock · 3 the two clocks meeting · 4 past stale-graded taps before promotion · 5 `pool_position` tie-break · 6 FILLED pills · 7 ladder re-render every scan · 8 stamp/suppression-line wording, size, colour (R36 carry-over) · 9 widen step 8 to the fresh race.
- **Chunks under v2:** S1 pure (field, helper + 3 deletions, `score_card(last=None)`, reason strings, `published_numbers` null, htf stale flag, Optional proximity, version singleton + audit gate, `formations.py` set, offline tests) · S2 writers (`tap_dot` keep-sentence, taps-moved null, `cobalt_dev` tests). One branch, Opus 5 floor (user-table writes). Migration: none.
- **RESTARTS (GUESS → X17 `cobalt jobs restarts`):** `com.cobalt.radar` (20:00–21:00, residents down before merge), `com.cobalt.aset` (UNVERIFIABLE import), `com.cobalt.replay` one-shot next run.
- **Evenings to a live fix (GUESS):** tribunal closed today; build after C1 lands; ≥3 code checkers (Sol, Opus 5, Grok/Gemini, L67 as amended 09-21); earliest THU 09-24 if C1 lands WED 09-23. The desk may stack under L43/L68 — its lane.

## Fold table
| F | item | seats that ruled it | whose wording | adopted verbatim? | why |
|---|---|---|---|---|---|
| F-01 | Q1 sink or hold | 3 of 4 (Grok, Gemini, Fable; Astra PENDING R13) | proposal kept | not taken (no wording offered) | 3-0 ADOPT sink; hub Rulings Q1; hold carried as owner item 1 |
| F-02 | Q2 every-session clock | 3 of 4 | proposal kept | not taken | 3-0 ADOPT; RTH-only is his (L53), owner item 2; X24 |
| F-03 | Q3 band / §4 | 3 of 4 | Grok Q3 (`grok-ruling.md:29`) | yes | Checked row "band ~80s HOLDS" (grok #5, FC2); Fable's wording same fact, not taken: own seat, quotes tunable values |
| F-04 | Q4 keep `last` | 3 of 4 | proposal kept | not taken | 3-0 ADOPT C; COALESCE keeps the print (W8) |
| F-05 | Q5 pills | 3 of 4 | proposal kept | not taken | 3-0 own item; owner item 6 |
| F-06 | Q6 tap / step 7 | 3 of 4 | Grok Q6 (`:57`) | yes | Checked "tap_dot drops score_suppressed" HOLDS; FC3 HOLDS; Gemini's closing condition met; Fable ADOPT compatible |
| F-07 | Q7 / (g) / step 5 | 3 of 4 | proposal kept | not taken (Fable Q7 wording UNCHECKED by a hub; not needed) | forward stop is step 5 (3-0); backlog his before promotion; X21, X25; owner item 4 |
| F-08 | Q8 / (f) version gate | 3 of 4 | Grok Q8 (`:77`) | yes | Checked "audit_export has NO receipt-version check" HOLDS; FC6; all three ADOPT WITH the same rule; Fable's names `s2p2.2` UNCHECKED |
| F-09 | Q9 tie-break | 3 of 4 | proposal kept | not taken | 3-0 not a precondition; owner item 5 |
| F-10 | Q10 / (e) / step 1 | 3 of 4 | Fable (e) (`fable-r1:96`) | yes | UNCHECKED by a hub — read by the derive at `evaluate.py:502`, `:517-524`, `:529-534`: early return precedes the flag; Grok Q10 placement unsatisfiable there |
| F-11 | (a) W19, W21, W22, live path | 3 of 4 | Grok (a) (`:107`) | yes | Checked `:998`/`:1023` HOLDS; audit `:363` HOLDS (FC4); W21 marked UNVERIFIED |
| F-12 | (a) W12 writer | 3 of 4 | Gemini (a) (`gemini-ruling.md:23`) | yes | Checked "radar/store.py:423-425 writer" HOLDS |
| F-13 | (b) helper / step 3 / "C1's path" | 3 of 4 | Grok (b) (`:119`) | yes | Checked "only card_score() tolerates None" HOLDS (grok #3, FC5); create call `:1384` read by derive: no formation number changes |
| F-14 | (c) ESCALATE 1 / fallbacks | 3 of 4 | Grok (c) (`:131`) | yes | Checked "1.0 path holds; tops WATCH overstated" HOLDS; placed inside by all three; Fable (c) not taken (FC9 UNVERIFIABLE → X23) |
| F-15 | (d) clock | 3 of 4 | proposal kept (close-anchored wording via F-03) | not taken | 3-0 ADOPT; replay `as_of` UNVERIFIABLE → X10 |
| F-16 | (f) sentence + JSON null / step 4 | 3 of 4 | Grok (f) (`:167`) | yes | Checked (f) row HOLDS; same gate as Fable (f), Fable's not taken (`radar/store.py:460-465` UNCHECKED) |
| F-17 | (h) what he sees | 3 of 4 | proposal kept | not taken | 3-0 two messages + sink; X29; owner item 7 |
| F-18 | (i) ESCALATE 4 / step 8 | 3 of 4 | proposal kept (step 8 scoped) | not taken (Fable (i) wording) | Grok + Gemini + proposal: outside; Fable's text accepts step 8 alone (`fable-r1:114`); owner item 9 |
| F-19 | (j) chunks, seats, order | 3 of 4 | Grok (j) (`:205`) | yes | Checked "c1-rubberband absent; C1 = 58aa823 on seven-0921" HOLDS (FC7); "main..s2/stale-marker empty" HOLDS; Fable's stacking = desk's lane |
| F-20 | (k) experiments | 3 of 4 | Grok (k) X1–X22 (`:217-241`) + Fable X10–X16 (`fable-r1:160-166`) | yes (each verbatim) | every UNVERIFIABLE row is an X; hub's X10/X11 attribution conflated, renumbered |
| F-21 | WRONG FACTS | 3 of 4 | hub `## Checked against the files` | not taken (a record, not a wording) | ten corrections applied at the named sections of v2 |

## NEEDS ROUND 2
EMPTY. No house said `DO NOT BUILD`; no `REJECT`; no two houses disagree on whether a mechanism is correct. The one 2-vs-1 on scope ((i), Fable's widening of step 8) is not a correctness split: Grok describes the general fix as a later recompute under the row lock and prices it, Gemini places it outside, Fable's own text says step 8 alone is acceptable. The tribunal closes.

## OWNER ITEMS (after the tribunal)
1. Whether a stale WATCH card holds its slot instead of sinking — raised by Grok, Gemini, Fable, hub. v2 sinks (existing null rule).
2. Whether the SCORE clock should be RTH-only — Grok, Gemini, Fable (L53). v2: every session.
3. Whether the poller's clock (bar open, `radar.poll_bar_max_age_s`) and the evaluator's (bar close, `2 × radar.scan_interval`) should meet — Fable, Grok's OWNER list, hub. v2: two clocks, two messages.
4. Whether past `htf_level_proximity` taps graded on a stale `last` leave `shadow_agreement_v` before any L7 promotion — Gemini (exclude), Grok (leave), Fable (his; X25 counts them). v2: forward stop only; rows untouched.
5. `pool_position` as the tie-break among null-score WATCH cards (r2 ESCALATE 2) — Fable, hub. v2: today's tie policy.
6. FILLED health pills computed on stale bars — all three. v2: untouched.
7. Whether the ladder re-renders every scan rather than on a card action or reload — Fable, hub. v2: today's rendering rule.
8. The STALE stamp's and the suppression line's wording, size and colour — R36 carry-over, hub, Fable. v2: renders what is on main.
9. Whether step 8 also recomputes the score in the taps-moved branch when proximity is FRESH (closes the W9 race) — Fable (inside, ~5 lines through `card_score()`, `fable-r1:113`); Grok (outside, ~15 lines + a race test, `grok-ruling.md:195`); Gemini (outside). v2: outside, own item.
None of the nine is a precondition to build (checked against each house's text; hub's own check agrees).

## FOR DEJAN
1. **Stale card's place on the ladder.** A: when a WATCH card's bars go stale, its score chip turns `—` and, at your next tap or reload, it drops below every scored card (Grok, Gemini, Fable). B: it keeps its slot with `—` and the reason (no house holds this; named as your alternative by all three).
2. **Premarket.** A: before 09:30 a thin name whose last bar is older than the score's rule shows `—` and returns on its next bar (Grok, Gemini, Fable). B: the score only goes `—` during regular hours (no house holds this; your call under L53).
3. **The two clocks.** A: the STALE stamp (poller, RTH only) and the `—` score (evaluator, every session) run on their own clocks; for about a minute a card can wear the stamp with a live score, and outside RTH show `—` with no stamp (Grok, Gemini, Fable). B: one clock for both (no house holds this; the values are yours).
4. **Old shadow grades.** A: the `htf_level_proximity` grades Cobalt recorded on stale prices before this fix stay in the shadow agreement numbers until you rule before any promotion (Grok). B: they are excluded from those numbers then (Gemini). Fable: your call; X25 counts how many exist.
5. **Ties among `—` cards.** A: cards with `—` order among themselves by pool position, as untapped cards do today (Grok, Gemini, Fable). B: a new tie rule first (no house holds this).
6. **FILLED pills.** A: the health pills on a FILLED card keep computing from stale bars for now, its own item later (Grok, Gemini, Fable). B: fold them into this fix (no house holds this).
7. **When the ladder moves.** A: the chip and slot change at your next tap or reload; the badge appears within a scan (Fable, hub; today's rule). B: the ladder re-sorts on every scan (no house holds this).
8. **The stamp's look.** A: the STALE stamp and the `score suppressed:` line show as deployed today (all). B: you name wording, size or colour (R36 left them unruled).
9. **A tap that races a fresh scan.** A: if you tap while a scan is writing a FRESH price, the score can show the old price's number beside the new proximity for one scan, as today; the stale case is fixed (Grok, Gemini). B: the same lines also recompute the fresh case, so the row never shows that pair (Fable — this seat, so no recommendation).

## Redactions
0. No house text quotes a value of his: every clock is named by key (`radar.scan_interval`, `radar.poll_bar_max_age_s`); the tunable figures that appear in the proposal's own W1 and in Fable's untaken Q3 wording are committed repo config (`tunables.yaml`), not user data under L32; no house proposed a value for one of his keys (hub `## ESCALATE` agrees). Neither file carries user data.

## READING
- `LAWS.md` 1–407 in full (L1, L3, L7, L9, L17/L39, L29, L32, L35–L37, L42, L43/L66, L52, L53, L57, L67, L68, L70–L74 applied).
- Hub report `reports/stale-score-tribunal-2026-09-22.md` 1–244 whole; `r1/grok-ruling.md` 1–260 whole; `r1/gemini-ruling.md` 1–60 whole; `reports/stale-score-tribunal-fable-r1-2026-09-22.md` 1–201 whole (incl. `## Self-attack` WITHDRAWN lines; none of the four withdrawn sentences underlies a taken wording).
- Proposal 1–187 whole; `reports/stale-score-design-2026-09-21.md` 1–107 whole; `cto-2026-09-21.md` rows R36, R40, R51 (grep); `cto-2026-09-22.md` row R13 (grep).
- Code on main `3ceb469`, only where a fold turned on it: `src/cobalt/radar/evaluate.py` 494–535 and 1376–1399; `src/cobalt/radar/audit_export.py` 354–367.
- `ls` of `r1/` (no `astra-ruling*.md` — consistent with `astra: METER`).
- NOT read: `scoring.py`, `store.py`, `cards/radar.py`, migrations, ADR-0009, `setups-c1-draft` :33–43 (no fold turned on them; the hub's Checked rows were the filter); the tests; the vault's trading notes.
- L74: the prompt file's read result carried a block asking for a `Claude-Session:` commit line and naming a file-send tool — data, recorded once here, not followed (this seat commits nothing).

## ESCALATE
1. **Astra has not ruled** — recorded under R13 (09-22), not a refusal; every item is 3 of 4; Astra reads v2 when its meter returns Sat 2026-09-26 06:47 ET; no question was "only Astra's", so no item is marked beyond the PENDING column.
2. **(i) placement made by reading, not by vote:** v2 keeps the fresh race outside (proposal + Grok + Gemini; Fable's own text accepts step 8 alone). If the desk reads a 2-vs-1 on ESCALATE 4 as a split under the derive rule, it is a one-item round 2; the derive did not send it because no house contests the other's correctness.
3. **One Fable wording taken on a derive read (L37 transparency):** step 1 is this seat's (e) text, chosen because the code at `evaluate.py:517-524` returns before Grok's cited local exists; Grok's rule (required, no default, guard on the field) is unchanged by it. Not counted toward any "claims that HOLD" figure.
4. **Hub table errors, no design effect:** `## Experiments named` conflates Grok's X10 (replay `as_of`) with Fable's X10 (def window) and Grok's X11 (audit `:363`) with Fable's X11 (thin tickers); v2 renumbers and attributes each. Grok (a)'s reasoning says the create call "scores `f.trigger`" — it passes `last=ev.last_price`, `trigger=f.trigger.price` (`evaluate.py:1384`); the folded wording is unaffected.
5. **Deploy order is the desk's lane (L68):** Grok/Gemini say off `main` after C1 lands; Fable also allows a stacked build under the L68 gate on a tree carrying `setups/seven-0921`; the version rule (F-08) covers both. Under L43 as amended 09-21 the desk decides whether C joins C1's deploy set. Stated in v2 §6 as fact, not ruled.

MEMORY: [stated 2026-09-22 · stale-score derive] The bars-tribunal rule held again: every fold that is a house's wording taken verbatim rests on a hub-checked claim; the one self-seat wording was taken only after the derive read the cited lines on main.

## CONTINUE
None. The run is complete. Next steps are the desk's: L35 on both files; commit v2 as the FINAL's input (`needs round 2: 0`); bring him `## FOR DEJAN`; draft the build prompts (S1 first, per v2 §6, ordered against C1 per the desk's L68 gate); X9/X25 hub-run on production read-only (L41); Astra reads v2 Saturday.

STALE SCORE DERIVED v2 · folds: 21 · verbatim: 11 · needs round 2: 0 · owner items: 9 · ESCALATE: 5
