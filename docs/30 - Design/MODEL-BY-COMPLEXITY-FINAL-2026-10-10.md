# MODEL-BY-COMPLEXITY — DRAFT FINAL — ROUND 2 OWED (S5, S6, S7) · 2026-10-10

PROPOSED DESIGN — NO MODEL AND NO LAW IS CHANGED BY THIS TRIBUNAL. L29 is amended only on Dejan's word on the result (R919, L77); every merged build stays Opus 5.5 until then.
NOT LAUNCHED until the SHADOW-HUB card is built, checked and approved (S11); the desk drafts that card from the section SHADOW TRIAL PLAN.
Insufficient data (n=3), L8: every result line of this trial is an indication for his word, never a tier.

- Derived by: Opus 5.5 derive seat `model-tribunal-derive-1010` (prompt `prompts/2026-10-10/272-model-tribunal-derive.md`; derive seat by R109 `cto-2026-09-22.md:56` "Make all Opus 5.5 for now" and launch row R942 `cto-2026-10-10.md:50`). The Anthropic house proposed, ruled round 1 blind and derives: it holds a side (L37) and recommends nothing.
- Amends: `docs/40 - DevDocs/reports/complexity-routing-proposal-r2-2026-10-10.md` (proposal r2, reproduced below §0–§4 with each amended paragraph tagged `[F-nn]`; struck text is proposal text whose claim does not hold or that a fold replaces). Round 1: `reports/complexity-routing-proposal-2026-10-10.md` (its Q1–Q8 carried by S10).
- His rulings, never re-opened: R919, R920, R921, R908 (`cto-2026-10-10.md`; `brain-direction-2026-10-02.md` `## RULED 2026-10-10`), R109 (`cto-2026-09-22.md`), R95, R97 (`cto-2026-09-23.md`), and R8 (`cto-2026-10-03.md:14`, read because Q7 turns on it).
- Round-1 rulings (3 of 3 seated houses ruled; floor MET):
  - Astra (OpenAI): `/Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/model-tribunal/r1/astra-ruling.md` — 18 of 18.
  - Gemini: `…/r1/gemini-ruling.md` is a STUB (hub ESCALATE 1); Gemini's full answer read from the task output file the stub names (lines 1-272) — 18 of 18, every item ADOPT.
  - Grok: `…/r1/grok-ruling.md` — counted on 14 items; S1, S5, S6, S9 (its own tier) RECORDED APART and counted nowhere (R919).
  - Anthropic seat (blind Opus 5.5, R109 / launch row R942): `docs/40 - DevDocs/reports/model-tribunal-opus-2026-10-10.md`; its claims file-checked by the hub (12 HOLD of 12 checked).
  - Hub collation and file-check: `docs/40 - DevDocs/reports/model-tribunal-2026-10-10.md`.
- Absent houses: none.
- Fold table: `docs/40 - DevDocs/reports/model-tribunal-derive-2026-10-10.md` `## Fold table`.
- ROUND 2 OWED (S5, S6, S7): the counted houses split on whether those mechanisms are correct; carried, never voted (L37, L39). Each goes to him as one A/B (derive report `## FOR DEJAN`), or to a round 2 for those items only. Their lines below are tagged `UNSETTLED (<item>)`.

# Model-by-complexity rule, round 2: the Grok SHADOW trial · proposal for the model tribunal · 2026-10-10

Proposer: Opus 5.5 drafter `complexity-propose-r2` (prompt `prompts/2026-10-10/265-propose-complexity-shadow.md`). L67: one house proposes and the tribunal rules.
Builds on: `reports/complexity-routing-proposal-2026-10-10.md` (round 1). Its §1 data, §2 score, §5.1 shadow log and Q1–Q8 hold unchanged unless this file says otherwise.
Frame (HIS RULING, R919, `cto-2026-10-10.md:12`; words at `brain-direction-2026-10-02.md:186-198`; LAWS L67 `[stated 2026-10-10 · Dejan, R919 via brain L79]`, `LAWS.md:347`):
- His hypothesis: `grok-4.7` builds at Opus 5.5's level or slightly below it, and above Sonnet and Haiku.
- Where a non-Anthropic model builds, Grok is preferred over Sol.
- Astra is RESERVED for tribunals and multi-house reviews.
- Every merged build stays Opus 5.5 until his word on this tribunal's result. Only that word amends L29.
This file tests the hypothesis. It does not argue for or against it.

## §0 Headline
- Round 1's classes stand. Two corrections: (a) three of the 27 checked jobs have card fields that place them LOW, MID and HIGH; (b) Grok has been house B on these checks, so it has its own record as a checker.
- SHADOW TRIAL: Grok 4.7 rebuilds three already-checked cards from their own BASE: `strike-fallback-env` (LOW), `radar-display-fix` (MID) and `s4-p1` (HIGH). Each rebuild goes on a `shadow/` branch that is never merged. Each is judged by the existing CHECK-HUB flow and compared with its Opus original.
- Grok cannot run commands (L67), so a fresh Opus 5.5 GATE SEAT runs Grok's CLI and the three suites. That seat writes no code.
- STOP (R411): the gate seat is a write-path launch, so it needs `dontAsk` mode. `desk-launch.sh prompt` runs only `auto` or `plan` (`desk-launch.sh:454-457`). The seat therefore needs a new fixed file plus a new launcher kind. That is a new command, so this proposal stops there with `decisions: 1`. ~~Everything else uses existing strings.~~ `[F-21]` (claim DOES NOT HOLD, hub C9: the standing `Bash(grok *)` writes only under scratch, never the repo; Astra, ITEM (c), verbatim:) "The R411 stop belongs before installing or launching the new procedure and changed builder authorization. Reusing flag names does not itself approve the broader write target. Prove file and command permission boundaries in scratch as L29 requires."
- n=3 is insufficient data (L8). The trial gives an indication for his word. It cannot prove a tier.

## 1. Complexity classes (round 1 §2, corrected)
The score is unchanged and is read from the card at launch:
- Formula: `R + M + S + X + H + $`. R = 1 per card row over 3. M = migration +3. S = +1 per service restarted. X = +2 per seam. H = new horizon +4. $ = money, sizing or his vault notes +3. W = write path, a gate and not a weight.
- Bands (modelled): LOW 0–2 · MID 3–6 · HIGH ≥7.
- `[F-11]` Inputs (Q2, Astra verbatim): "Keep R, M, S, X, H and $ as launch-time descriptive inputs; W remains a separate law gate. Record each raw value and its card or launch-record citation before building. H requires the drafter’s recorded absence of a precedent card or design; “new detector” alone is insufficient. X uses the stated shared-file/open-card definition unless the tribunal explicitly replaces that definition; a runtime database seam alone does not establish it. Missing evidence is UNKNOWN, not zero. Existing weights are an unvalidated shadow index and authorize no routing."
- `[F-13]` Bands (Q4, Astra verbatim): "Keep LOW 0–2, MID 3–6 and HIGH ≥7 as frozen descriptive bins for the shadow log only. They are modelled, not measured, and do not select a model. At n≥30 per band, evaluate the frozen index against row count on later, held-out outcomes. Do not reset cut points on the same observations used to claim success. Any proposed replacement requires measured out-of-sample improvement and a separately recorded validation."

Corrections from this round's reads:
1. The 26-build sample does span the three bands, so the bands can be tested once a second model builds:
   - `strike-fallback-env`: 2 rows, RESTARTS aset+radar. R0 + S2 = **2, LOW**. `[F-26]` (hub C8 HOLDS; Anthropic seat, WRONG FACTS 3, verbatim:) "r2 §1 :21, :26 S from "RESTARTS aset+radar" for strike — `215-strike-fallback-env-card.md:46` expects `com.cobalt.aset` only; `strike-fallback-env-check-2026-10-10.md:159` "the extra `com.cobalt.radar` is the build's DECISION". The card-field score is 1 (LOW either way). This also contradicts round 1 §2 :69 "none reads an outcome"."
   - `radar-display-fix`: 6 rows, one `src/` file, RESTARTS aset+radar. R3 + S2 = **5, MID**.
   - `s4-p1`: 8 rows, RESTARTS aset+radar, ONE SEAM (`card_transitions` through `CardStore.transition()`, card `72-s4-p1-card.md:14`), new detector. R5 + S2 + X2 + H4 = **13, HIGH**. `[F-19]` (hub C7: arithmetic OK, H and X UNVERIFIABLE FROM READS; Astra, ITEM (a), verbatim:) "HIGH’s arithmetic is (8−3) + 2 + 2 + 4 = **13**, but X and H remain **UNVERIFIED — shared-file/open-card evidence and the drafter’s horizon record**. The runtime seam alone does not meet R1’s X definition."
   - Build reports quoted in the check reports: `strike-fallback-env-check-2026-10-10.md:41`, `radar-display-fix-check-2026-10-08.md:42`, `s4-p1-check-2026-10-09.md:45`.
2. Held findings do not track the band in these three: LOW 1, MID 3, HIGH 4. In round 1's full sample, 1–2-row cards held 11 (`guard-g2`, `radar-ladder-refresh`). Round 1's warning stands: the band predicts cost (tokens rise with rows: 165k / 180k / 416k) better than it predicts defects.
3. Grok as a checker, house B on all three originals:
   - `strike-fallback-env`: FINDINGS 0 (`strike-fallback-env-check-2026-10-10.md:129`). `[F-23]` (hub C4 HOLDS; Gemini, WRONG FACTS 2, verbatim, its scratch links kept:) "In [10-PROPOSAL-R2.md:32](file:///Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/model-tribunal/r1/10-PROPOSAL-R2.md#L32), the citation `strike-fallback-env-check-2026-10-10.md:129` for `FINDINGS 0` references line 129, which reads `House B (Grok): no finding.` ([15-checks.excerpt.md:15](file:///Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/model-tribunal/r1/15-checks.excerpt.md#L15)); the literal text `FINDINGS: 0` appears at line 124 ([15-checks.excerpt.md:10](file:///Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/model-tribunal/r1/15-checks.excerpt.md#L10)) and stop line 223 ([15-checks.excerpt.md:28](file:///Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/model-tribunal/r1/15-checks.excerpt.md#L28))."
   - `radar-display-fix`: FINDINGS 0 (`radar-display-fix-check-2026-10-08.md:246`).
   - `s4-p1`: 4 findings, 0 held. Three were REJECTED and B2 was UNSETTLED (`s4-p1-check-2026-10-09.md:163-165`). `[F-22]` (hub C1 HOLDS; Gemini, WRONG FACTS 1, verbatim, its links kept:) "In [10-PROPOSAL-R2.md:34](file:///Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/model-tribunal/r1/10-PROPOSAL-R2.md#L34), the citation `s4-p1-check-2026-10-09.md:163-165` for Grok's four findings ("Three were REJECTED and B2 was UNSETTLED") omits finding B1, which is located at line 160 ([15-checks.excerpt.md:85](file:///Users/cobalt/cobalt-wt/agy-trial/scratch/tribunal-bars-0920/model-tribunal/r1/15-checks.excerpt.md#L85), [s4-p1-check-2026-10-09.md:160](file:///Users/cobalt/cobalt/docs/40%20-%20DevDocs/reports/s4-p1-check-2026-10-09.md#L160)); lines 163–165 contain only B4, B3, and B2."
   - Elsewhere, Grok held 2 of 2 on `stop-guard-g7` (`stop-guard-g7-check-2026-10-09.md:166-167`).
   - This is Grok's record as a reviewer. It is not evidence about Grok as a builder.
4. ~~The Opus check session's OWN held findings are the only source that sat on every original:~~ `[F-25]` (hub C3 HOLDS; Astra, WRONG FACTS, verbatim:) "**“Only source”:** `10-PROPOSAL-R2.md:37` contradicts :31–35 and Grok’s records in `15-checks.excerpt.md`, strike:129, radar:246 and s4:130. Opus is the consistently independent reviewer, not the only recurring source."
   - `strike-fallback-env`: 1 (O1, `strike-fallback-env-check-2026-10-10.md:137`).
   - `radar-display-fix`: 2 (O1, O2, `radar-display-fix-check-2026-10-08.md:158-159`).
   - `s4-p1`: 2 distinct defects (O1, O3, `s4-p1-check-2026-10-09.md:155,157`; Sol's A3 and A2 are the same two defects).
   - The trial uses this as its primary comparable figure (§2.3).
5. `[F-24]` Round 1's §1.3 totals (carried by S10; hub C2 HOLDS; Astra, WRONG FACTS, verbatim:) "**R1 build total and median:** `12-PROPOSAL-R1.md:58` contradicts its table at :29–54. Grouped sums are 1,168,555 + 947,571 + 1,187,743 + 717,647 + 1,382,920 + 165,478 = **5,569,914**, excluding the separate fix. Including 128,005 gives **5,697,919**. The middle sorted values yield **195,971.5**, not ≈181,000. Recompute :120’s aggregate using a declared inclusion rule."

## 2. The SHADOW trial

### 2.1 The three cards (each checked, each built by Opus 5.5)

**strike-fallback-env · LOW (2)**
- Card: `prompts/2026-10-09/215-strike-fallback-env-card.md`, BASE `8f4bbe28` (`:5`).
- Proof it was checked: CARD COMMITTED `bc051c44` (`strike-fallback-env-check-2026-10-10.md:16`). Stop line `CHECK DONE … held: 1 … ready: YES` (`:223`).
- Opus build tokens: 165,478 (`:41`). Check tokens: 138,173 (`:223`).
- Held: 1, O1 (`step()` raises on an unprintable exception, `:137`).

**radar-display-fix · MID (5)**
- Card: `prompts/2026-10-08/118-radar-display-fix-card.md`, BASE `50b0cd87` (`:5`).
- Proof it was checked: CARD COMMITTED `0deb06fc` (`radar-display-fix-check-2026-10-08.md:16`). Stop line `held: 3 … ready: YES` (`:246`).
- Opus build tokens: 179,901 (`:42`). Check tokens: 176,294 (`:246`).
- Held: 3, O1, O2 and A3 (`:158-159,163`).

**s4-p1 · HIGH (13)** — `[F-19]` X and H UNVERIFIED (§1 item 1); HIGH on any reading the houses gave (13, 9 or ≥7).
- Card: `prompts/2026-10-06/72-s4-p1-card.md`, BASE `e4586978` (`:5`).
- Proof it was checked: CARD COMMITTED `d35d6841` (`s4-p1-check-2026-10-09.md:18`). Stop line `held: 4 … open: 7 … ready: YES` (`:279`).
- Opus build tokens: 415,769 (`:45`). Check tokens: 259,254 (`:279`).
- Held: 4 findings, 2 distinct defects: O1=A3 and O3=A2 (`:155-158`).

Why these three (`[F-02]` S2: ADOPT, proposal kept):
- Each is in a different band.
- All three were checked in the next flow (house A and house B at once).
- None of the three has a migration. A shadow migration would move `cobalt_dev` off `0013` for a branch that never lands. `s4-p2` (migration 0024) and `price-floor` (0023) are excluded for that reason.
- None of the three is a MANDATORY-HOUSE-B card (all three are `HOUSE B: as needed`, `:9` of each card).
- `s4-p1` writes `card_transitions` through the existing store. That is a DB write path under L29. It runs only in tests under the L76 lock, on a branch that is never merged.

### 2.2 How one shadow build runs
1. **Shadow card.** The desk commits a copy of the original card:
   - The ROWS stay byte for byte.
   - Changed header fields: `JOB: <job>-grok`, `BRANCH: shadow/<job>-grok`, `WORKTREE: <job>-grok`, the same `BASE`, and `RULINGS: 2026-10-10 R919`.
   - No `TIP` or `CHECK REPORT` of the original.
   - New header line: `SHADOW OF: <original card path>`.
   - `[F-18]` The header pointers are governed by S11's fold (§3, R411 STOP): the shadow's own TIP, REPORT and CHECK REPORT paths are recorded and committed before each shadow check, answer-bearing pointers of the original are removed, and the original card requirements and applicable rulings are retained (the original REPORT line points at Opus's build: card `215` `:7`, read by the derive).
2. **Worktree.** `git -C /Users/cobalt/cobalt worktree add -b shadow/<job>-grok /Users/cobalt/cobalt-wt/<job>-grok <BASE>`. This is BUILD-HUB LAUNCH (0) as it stands (`BUILD-HUB.md:9`), run by the launcher. Gated by X4 and X14 (below).
3. **Gate seat, start.** `UNSETTLED (S7)` The gate seat (§3) writes `<WT>/SHADOW-INSTRUCTIONS.md` and never commits it. It holds the shadow card's ROWS verbatim, BUILD-HUB `## E2` and `## E3` verbatim, and the fence: `src/` and `tests/` only, the rows' files only. Grok's sandbox reads only its workspace, so the card is copied in. CHECK-HUB copies files for its houses the same way (`CHECK-HUB.md:91`).
4. **Grok pass T (tests only).** `UNSETTLED (S7)` The gate seat runs the Grok builder line (§2.6). Grok writes the rows' tests under `tests/`. The gate seat then:
   - runs `git diff --stat` and quotes it;
   - commits with `git add tests/…` and `git commit -m "wip(<job>-grok): red"`;
   - runs the new tests to show them red.
   - If a test is green before the fix, that is recorded. The gate does not repair it.
5. **Grok pass S (the rows).** `UNSETTLED (S7)` The same line, now asking for the `src/` rows. The gate seat quotes `git diff --stat` and commits `feat(<job>-grok): rows`. A path outside the rows' files is recorded as `SCOPE` and is not reverted.
6. **Gate.** `UNSETTLED (S6)` BUILD-HUB `## RESTARTS` and `## W` as they stand: offline, with-DB under THE LOCK, and live-note.
   - If a suite is red, the gate seat sends Grok ONE re-pass (pass S2) with the failing lines quoted verbatim, then reruns the suites.
   - The cap is 2 re-passes. After that the build stops `SHADOW BUILT … suites: red`, and the build is scored, not repaired.
   - Settled by every counted house (S6): the cap is 2 and the gate seat never repairs `src/` or `tests/`. Open: how a third red that the environment caused is scored.
7. **Build report.** The gate seat writes `<WT>/docs/40 - DevDocs/reports/<job>-grok-build-<date>.md` in BUILD-HUB's REPORT shape. Its stop line is BUILD-HUB's BUILT line with these extra fields: `builder: grok-4.7 · gate: <seat> · grok passes: <n> · suites at first run: <green|red>`.
8. ~~**Check.** `desk-launch.sh check <shadow card>`: the existing CHECK-HUB, unchanged (fresh Opus plus house A by R921). Grok sits as house A on its own build. Its findings are run like any other and tallied apart (§2.3, T3). The check fixes what holds, as CHECK-HUB says. Those fixes are Opus's and are never counted for Grok.~~ `[F-03]` (hub C5 HOLDS: unchanged CHECK-HUB seats Sol first when UP and probes Codex; C12 HOLDS: R920/R921 override it; Grok, S3, verbatim:) "Grok is house A on the check of its own build. The shadow check does not run the Sol/Codex probe (L67 R920: no Codex probe outside the model tribunal's own seats; this check is a build check). Gemini is not seated unless Grok returns no list (L67 R921). These cards are `HOUSE B: as needed`. A Grok session already running is not a wait (L67 R908). CHECK-HUB.md is not edited. Grok's held findings are tallied in §2.3 and do not enter the §2.4 bar." Gated by X12 (below).
9. **Never merged.**
   - No deploy card ever names a `shadow/` branch.
   - The worktree stays until the tribunal's result is recorded, then it goes by the desk's usual worktree salvage.
   - The original check's report and fix commits are on `main`. The shadow check prompt (CHECK-HUB) reads the shadow card, which does not name them.

### 2.3 Metric (per card, recorded beside the Opus original)

`[F-04]` The first four rows and the primary-metric definition are replaced (S4, Astra verbatim): "Report all-source held findings, independently recorded Opus-own held findings, Grok-sourced held findings, all-source distinct defects, and Opus-own distinct defects separately. The primary comparison is Opus-own held findings recorded before opening house findings; the scored distinct-defect comparison uses only those Opus-own HELD rows, deduplicated by stated common cause. Grok-only findings affect neither scored count. Original scored baselines are held 1 / 2 / 2 and distinct defects 1 / 2 / 2. All-source descriptive baselines remain held 1 / 3 / 4 and distinct defects 1 / 3 / 2." Gated by X7 (review provenance).

| metric | how measured | Opus original (LOW / MID / HIGH) |
|---|---|---|
| ~~held findings, all sources~~ | ~~the shadow CHECK DONE line `held:`~~ | ~~1 / 3 / 4~~ `[F-04]` |
| ~~held, Opus check's own (primary)~~ | ~~`O<n>` rows with verdict HELD~~ | ~~1 / 2 / 2~~ `[F-04]` |
| ~~held, Grok-sourced (on its own build)~~ | ~~house-A rows HELD; tallied apart and not counted~~ | ~~n/a~~ `[F-04]` |
| ~~distinct defects~~ | ~~held rows merged where the check says "same defect as"~~ | ~~1 / 3 / 2~~ `[F-04]` |
| fix rounds | `ready: NO` → the card's FIX ROUND count to `ready: YES` | 0 / 0 / 0 |
| suites at first green | `suites at first run` plus `grok passes` on the BUILT line | ~~green at build / green / green (all three originals BUILT on the first gate)~~ `[F-27]` (hub FC1: a W red then a fix after s4-p1's build report; Astra, ITEM (a), verbatim:) "R2 :105’s first-gate assertion is **UNVERIFIED — original gate-attempt histories would settle it**. Final BUILT green does not establish first-attempt green." |
| scope breaks | a path outside the rows' files (CHECK-HUB `## 7` (ii)) | 0 / 0 / 0 (A2, A5 and B4 rejected as docs/precedent) — `UNSETTLED (S7)`: whether the fence admits the originals' docs and test exceptions |
| tokens | Opus: gate seat plus check `tokens:`. Grok: UNKNOWN (§2.5) | build 165,478 / 179,901 / 415,769 · check 138,173 / 176,294 / 259,254 — `UNSETTLED (WRONG FACTS, FC5)`: whether a stop line's `tokens:` is meter use or end-of-run context size |

Known-answer side run (T5): after the shadow check, the gate seat's report lists the original check's red tests:
- `strike-fallback-env`: `245f3fd6`.
- `s4-p1`: `720cc29f`.
- `radar-display-fix`: its red commit, read at launch (X13).
For each test it says whether that test applies to Grok's tree: same function name, or not applicable. It is recorded only and does not count toward the bar. Gated by X6 (replay on the frozen pre-check TIP).

### 2.4 Pass bar (proposed; each card, then the set) — `UNSETTLED (S5)`; the line "a build that stops with `suites: red`" also `UNSETTLED (S6)`
The proposal's text stands below only as the text the split is about; it is not ruled. Both positions are carried verbatim in the derive report `## OPEN AFTER ROUND 1`.
- **AT LEVEL** on a card, when all of these hold:
  - `ready: YES` with no fix round;
  - Opus-own held ≤ the original's + 1;
  - distinct defects ≤ the original's + 1;
  - suites green at first run, or after 1 Grok re-pass;
  - 0 scope breaks.
- **CLOSE BELOW** on a card: `ready: YES` after at most 1 fix round, distinct defects ≤ the original's + 3, and at most 2 Grok re-passes.
- **BELOW** on a card: anything else, or a build that stops with `suites: red`.
- SET result: AT LEVEL when all three cards are AT LEVEL. CLOSE BELOW when none is BELOW. Otherwise BELOW.
- The tribunal reads the set result against his hypothesis. Only his word turns it into a seat rule (R919).
- The trial cannot show "above Sonnet and Haiku", because neither is in the trial. That half of the hypothesis stays untested (Q5). `[F-09]` (S9: ADOPT, proposal kept.)
- Under `[F-04]`, any "distinct defects" count that enters a bar is the scored one (Opus-own HELD rows, baselines 1 / 2 / 2).

### 2.5 Cost
- **Anthropic meter.**
  - Shadow checks: about 575k by analogy with the three original checks (138k + 176k + 259k).
  - Gate seats: about 300–450k MODELLED (three seats). Each one reads BUILD-HUB and the card, runs the suites, and authors no code. No measured row exists for such a seat. Gated by X3.
  - Total: about 0.9–1.0 M tokens. That compares with 1.33 M for the originals' builds plus checks. `[F-19]` (hub C13 HOLDS; Astra, ITEM (a), verbatim:) "Adding the unmeasured gate estimate gives 573,721 + 300,000–450,000 = **873,721–1,023,721**. This is not a measured saving." `UNSETTLED (WRONG FACTS, FC5)`: the unit of the stop lines' `tokens:` (meter use or context size) is not settled by reads.
- **Grok meter.** 3 cards × at least 2 passes (T and S), plus up to 2 re-passes each, so 6–12 calls. Gated by X2.
  - Tokens: UNKNOWN (L70). Grok's session `summary.json` records `num_messages`, `created_at` and `updated_at`, but no token field (read of `~/.grok/sessions/…agy-trial/01a126f9…/summary.json`).
  - The gate seat records messages and wall time per pass instead.
  - Grok's own check seat: 3 more calls.
- **Dollars:** $0 (L27; minimum tiers, no top-up).
- **OpenAI:** none. Sol does not sit (R920). Astra's meter is kept for this tribunal.

### 2.6 Grok builder launch line (run by the gate seat; ~~only existing strings~~ `[F-21]`)
- `[F-21]` (hub C9 HOLDS: `STANDING-LIST.md:98` scopes the standing `Bash(grok *)` to scratch writes, never the repo; Astra, ITEM (c), verbatim:) "The R411 stop belongs before installing or launching the new procedure and changed builder authorization. Reusing flag names does not itself approve the broader write target. Prove file and command permission boundaries in scratch as L29 requires." Gated by X1.
- `Bash(grok *)` is a STANDING house string (`LAWS.md:321`).
- The flags are CHECK-HUB's Grok seat (`CHECK-HUB.md:91`): `-m grok-4.7` (his 10-03 R3), `--sandbox cobalt-job` (`ops/grok-sandbox.toml`: the workspace profile; `.env`, `~/.cobalt` and the agent homes are denied) and one `--allow "Write(…)"` glob.
- `--always-approve` is never passed, so Grok runs no shell command. That keeps L67's "a house cannot run a command".
- cwd: `/Users/cobalt/cobalt-wt/<job>-grok`. The line:

`grok -m grok-4.7 --sandbox cobalt-job --allow "Write(/Users/cobalt/cobalt-wt/<job>-grok/**)" -p "You are GROK (xAI), building a card. Read SHADOW-INSTRUCTIONS.md in this folder whole first and follow it exactly. Pass <T|S|S2>: <tests only under tests/ | the src/ rows | fix the failing lines quoted under PASS S2>. Write only the rows' files. Run no command. Reply with the list of files you wrote."`

## 3. THE GATE SEAT
- **Seat:** a fresh Opus 5.5 session, `<job>-grok-gate`, launched by the desk.
  - It is never the builder, which is Grok.
  - It is never the shadow check session, which is a separate fresh Opus under CHECK-HUB.
  - L29: a session on a DB write path (the with-DB suite) runs on Opus or higher and never in auto mode.
- **Its line:** BUILD-HUB's 26 allow strings and 4 deny strings unchanged (`BUILD-HUB.md:12-14`), in `--permission-mode dontAsk`, plus the standing `Bash(grok *)` — `[F-21]` whose standing scope is scratch writes only (C9); the builder's worktree write target is a changed builder authorization (§2.6).
  - The fixed file tells it to Edit only `SHADOW-INSTRUCTIONS.md` and its report, never `src/` or `tests/`.
  - Its report quotes `git diff --stat` before each commit, so the check can match every commit to a Grok pass.
- **How its result is recorded:**
  1. The BUILT stop line in its build report (§2.2 step 7) is the record. CHECK-HUB reads it like any build report.
  2. The desk adds one row per card to a new table `reports/complexity-shadow-results-2026-10-<dd>.md`: §2.3's columns with the shadow value beside the original.
  3. The model tribunal's hub reads that table.
- **R411 STOP:** this seat needs `dontAsk` on a write path, so it must be a FIXED file launched by a launcher kind (L29; `desk-launch.sh:445-457` refuses every mode but `auto` and `plan` on a prompt). Neither exists:
  - `SHADOW-HUB.md` (the gate seat's procedure);
  - `desk-launch.sh shadow <card>`: BUILD-HUB's LAUNCH (0)–(2) with SHADOW-HUB and the line above.
  - ~~That is a new command. The shadow trial cannot launch until a card builds it and he approves its line (the BUILD-HUB pattern: one approval of the list).~~ `[F-18]` (S11, Astra verbatim:) "Build, check and obtain the required approval for SHADOW-HUB and `desk-launch.sh shadow <card>` before launching the trial. The implementation card incorporates the tribunal’s metric, provenance, RED FIRST, scope and stopping rules. Before each shadow check, the desk records and commits the shadow’s own TIP, REPORT and CHECK REPORT paths; it removes original answer-bearing pointers from material supplied to the builder and checker, while retaining original card requirements and applicable rulings. Freeze the pre-check Grok commit as the scored build and keep subsequent Opus fixes separately attributable. The launcher follows R919–R921, including no OpenAI probes. The tribunal rules the design now and reads measured results in a later sitting within its existing round cap. This design changes no merged-build model."
  - Precedent for "a fixed file plus a launcher kind, not a prompt": `ops-hand-draft-2026-10-10.md:17`.
  - Until that card exists, the tribunal can still rule on §1, §2.1–§2.5 and §4.

## 4. Questions for the model tribunal (each with a default) — with the round-1 fold
SEATS: Astra (OpenAI; his reserved meter is spent here, R919/R920; one OpenAI seat at a time, F4 holds it first, `LAWS.md:346`), Gemini, and the blind Anthropic seat (Opus 5.5, `LAWS.md:344` desk reading). Grok also sits. Its ruling on any item about Grok's own tier (S1, S5, S6, S9) is RECORDED APART and not counted (R919 "self-interest", `LAWS.md:349`).
No item below is an owner item. A tier assignment is not his money, data or law. The L29 amendment is his word on the result, as R919 already says, so it is not a question here (`LAWS.md:345`).

- **S1. Are three cards (LOW, MID, HIGH) enough to read his hypothesis, given L8's n≥30?** Default: YES, as an indication only. The result is reported as "insufficient data (n=3)", and his word decides. *(Grok: recorded apart.)* → `[F-01]` ADOPT, default kept (Astra, Gemini, Anthropic seat).
- **S2. Card choice: `strike-fallback-env`, `radar-display-fix`, `s4-p1`, no migration cards.** Default: keep. A migration card would move `cobalt_dev` for a branch that never lands. → `[F-02]` ADOPT, default kept (Astra, Gemini, Grok); BASE health is gated by X4.
- **S3. Grok sits as house A on the check of its own build (R921 seat order, CHECK-HUB unchanged).** ~~Default: YES. Its findings are run by Opus like any other, and held ones are tallied apart and not counted toward the bar. No hub change is needed.~~ → `[F-03]` Grok's wording (§2.2 step 8).
- **S4. Primary figure = the Opus check session's OWN held findings, because it is the only source on every original and every shadow.** Default: YES. All-source held and distinct defects are reported beside it. → `[F-04]` Astra's wording (§2.3).
- **S5. Pass bar AT LEVEL / CLOSE BELOW / BELOW (§2.4).** Default: keep as written. *(Grok: recorded apart.)* → `[F-05]` OPEN: Astra replaces the bar; Gemini adopts it as written; the Anthropic seat keeps the tolerances and drops distinct defects from the bar.
- **S6. Grok re-pass cap: 2 per card, and the gate seat never repairs code.** Default: keep. A third red stops the build and scores it BELOW. *(Grok: recorded apart.)* → `[F-06]` OPEN on the scoring of a third red the environment caused (Astra: INCOMPLETE; Gemini: BELOW). Cap 2 and "never repairs" are agreed.
- **S7. Two Grok passes (tests, then rows) to keep BUILD-HUB's RED FIRST.** Default: YES. → `[F-07]` OPEN on what the gate seat puts before Grok (Astra: the complete card, rulings and the docs/test exceptions; Grok: rows, E2, E3 and one fence line only). Two passes, T then S, are agreed.
- **S8. Grok's reasoning effort.** CLI headless runs show `"reasoning_effort": "medium"` (`summary.json` above). Default: leave the CLI default and record it. A pinned effort would be a new flag on the line (R411). → `[F-08]` ADOPT, default kept; the `medium` reading rests on one session file and is UNVERIFIABLE FROM READS (C21), gated by X2.
- **S9. "Above Sonnet and Haiku" is untested by this trial.** Default: leave it untested. His R919 states it, and a Sonnet arm on a write path is barred (L29). *(Grok: recorded apart.)* → `[F-09]` ADOPT, default kept.
- **S10. Round 1's Q1–Q8 (shadow log, inputs, bands, non-write Sonnet trial, HIGH → Fable, JEV, retire rule).** Default: carried as round 1's defaults. This tribunal rules them in the same sitting. → ruled item by item:
  - Q1 `[F-10]` ADOPT, round 1 default kept: "YES, shadow first (L7 pattern)."
  - Q2 `[F-11]` Astra's wording (§1).
  - Q3 `[F-12]` ADOPT, round 1 default kept: "NO; L29 reads "mechanical work only", and these builds run the full gate (L68)."
  - Q4 `[F-13]` Astra's wording (§1).
  - Q5 `[F-14]` Astra verbatim: "The Sonnet–Opus non-write trial is exploratory and limited to independently established mechanical work; LOW score alone does not establish eligibility. Separate drafter and preflight outcomes, record assignment order and task class, and retain each planted-mismatch result. Any missed planted mismatch fails that observed case. Report first-run-ready differences and uncertainty at the stated sample floor; do not call a five-percentage-point observed difference a validated noninferiority margin. Promotion requires a prospectively specified, measured quality-loss criterion and adequate precision, settled by the houses before evaluating promotion data. This trial grants no automatic seat changes and does not launch as part of the three-card Grok trial."
  - Q6 `[F-15]` Astra verbatim: "HIGH does not trigger a Fable escalation or an owner question. Keep the presently ruled model. The houses may present measured task-fit evidence in a subsequent routing design, while honoring the standing model floor and Dejan’s existing rulings. No automatic or per-job model change follows from this unvalidated score." (Round 1's default "name per job via the brain" is not folded: RE-OPENS A RULING (R919), derive report `## ESCALATE`.)
  - Q7 `[F-16]` ADOPT, round 1 default kept: "compare blind; the score is the baseline it must beat to 80% agreement (R8)." (His R8, `cto-2026-10-03.md:14`, states the 80% agreement; read by the derive.)
  - Q8 `[F-17]` Astra verbatim: "Evaluate the frozen score after the stated per-band sample floor, against a row-count-only baseline using the same held-out jobs and separately reported token, held-defect and FIX ROUND outcomes. Predeclare the prediction method and loss before reading evaluation outcomes. If the score provides no demonstrated improvement, retire it as a routing candidate and retain the raw observations. Insufficient precision is inconclusive and authorizes no routing. Do not tune the score on the evaluation sample or combine unlike outcomes into an unmeasured weighted number."
- **S11. Order: the shadow trial launches only after the `SHADOW-HUB` card is built, checked and approved (§3).** ~~Default: YES. The tribunal rules the design now and reads the results in a second sitting, within L67's three rounds.~~ → `[F-18]` Astra's wording (§3, R411 STOP).

## First-gate experiments (L70)
Each is a claim nobody ran (UNVERIFIABLE FROM READS in the hub's file-check, or named by a house as missing). None is a defect. Each runs before the trial step it gates, on dev scratch worktrees, through the approved gate seat; the "changes the design" column is the house's own.

| X | experiment | named by | placed before | result that changes the design |
|---|---|---|---|---|
| X1 | Grok CLI under `--sandbox cobalt-job` with the worktree glob: writes only the glob; no shell command runs without `--always-approve`; denied homes and a worktree `.env` unreadable; reads outside the worktree | Astra X1, Gemini X1/X2, Grok X1, Anthropic seat X1 | any shadow pass (L29(2) permission gate) | any write outside the worktree or a shell run: no shadow build launches |
| X11 | Launcher dry-run on the LOW scratch card: authorization, current report paths, file exceptions, model/permission mode, R921 probes/seats | Astra X8 | the first `desk-launch.sh shadow` | stale pointers, Codex probes or unapproved commands: template/launcher correction |
| X12 | CHECK-HUB dry reading against a shadow card that cites R920 | Grok X5 | the first shadow check (§2.2 step 8) | the file still launches `codex exec` for Sol: the skip becomes a launcher change inside the SHADOW-HUB card |
| X9 | An ignored path inside the worktree for SHADOW-INSTRUCTIONS.md (`git check-ignore -v`) | Anthropic seat X4 | the first shadow check's PREFLIGHT | no ignored path: SHADOW-HUB adds one `rm` string |
| X4 | Dev lock, `cobalt_dev` schema level and BASE health (BUILD-HUB E0 on each untouched BASE) | Grok X3, Anthropic seat X3, Astra X3 | pass T on each card | base red or level ≠ 0013: S6's false-BELOW risk; the S2 card choice |
| X14 | Suite isolation/restoration and live-note effects on `s4-p1` at BASE | Astra X3 | the first with-DB gate | restoration failure or unexpected real-note writes: gate-isolation correction |
| X2 | Cost of one Grok pass T and S on LOW: messages, wall time, CLI/model version, `reasoning_effort` | Astra X2, Gemini X3, Grok X2, Anthropic seat X2 | MID and HIGH passes | effort ≠ medium, or one pass near CHECK-HUB's 45 min: own timeout / cost unit |
| X3 | One gate seat's own `tokens:` on LOW | Gemini X4, Grok X4 | MID and HIGH gate seats | far outside the modelled 300–450k: §2.5's meter paragraph |
| X5 | RED-FIRST / attribution rehearsal on LOW: green-before-fix test, unrelated-red test, out-of-stage edit, untracked file, environmental failure | Astra X4, Grok X7 | the scored LOW run | misclassification changes SHADOW-HUB |
| X10 | Can headless Grok edit a large file without rewriting it whole (radar `PANEL_JS`) | Anthropic seat X6 | the scored MID run | whole-file rewrite: a column, and that card's result kept apart |
| X15 | Repair convergence and cost: every pass, failure cause, gate/check tokens | Astra X7 | reading any card's re-pass record | assesses the two-repair allowance; infrastructure failure alone is not inferiority |
| X7 | Review provenance: OWN findings before Grok's list; pre/post-fix TIPs kept | Astra X6 | reading any shadow check (§2.3 primary) | contamination: an uncontaminated check |
| X6 | Known-answer replay on the frozen pre-check Grok TIP | Astra X5 | the T5 side run | a pass only after Opus repair: report corrected |
| X13 | `radar-display-fix`'s check red commit hash | Gemini X5, Grok X6 | the T5 side run on MID | recorded only |
| X8 | A fresh Opus check's run-to-run spread on one original tip | Anthropic seat X5 | reading the S5 bar | a difference ≥ 2: "+1" is below the checker's noise (bears on OPEN S5) |

## SHADOW TRIAL PLAN
The desk drafts the `SHADOW-HUB` card from this section. Its two artifacts: the new fixed file `SHADOW-HUB.md` (the gate seat's procedure) and the launcher kind `desk-launch.sh shadow <card>` (BUILD-HUB's LAUNCH (0)–(2) with SHADOW-HUB and §2.6's line) — a new command needing his approval of its line (R411, the BUILD-HUB pattern). Requirements of that card: `[F-18]` (§3).
- Cards: §2.1 — `strike-fallback-env` (LOW), `radar-display-fix` (MID), `s4-p1` (HIGH); no migration cards `[F-02]`.
- Steps, per card, in order:
  0. Gates before any card: X1, X11, X12, X9.
  1. Shadow card committed, pointers per `[F-18]` (§2.2 step 1).
  2. Worktree at BASE (§2.2 step 2); X4 and (s4-p1) X14 before pass T.
  3–5. Instructions file and passes T, S: two passes, T then S (agreed) — content of the instructions file, provenance capture and the fence: `UNSETTLED (S7)`.
  6. Gate: cap 2 re-passes, the gate never repairs (agreed) — scoring of a third red the environment caused: `UNSETTLED (S6)`.
  7. Build report and BUILT line (§2.2 step 7); pre-check Grok commit frozen as the scored build `[F-18]`.
  8. Check: `[F-03]` (Grok house A, no Sol/Codex probe, Gemini only if Grok returns no list, CHECK-HUB not edited, Grok's held findings out of the bar).
  9. Never merged (§2.2 step 9). T5 side run after the check: X6, X13.
- Metric: §2.3 with `[F-04]` (primary = Opus-own held, recorded before opening house findings; scored distinct defects = Opus-own; baselines held 1 / 2 / 2, distinct 1 / 2 / 2) and `[F-27]`; scope-break definition `UNSETTLED (S7)`; tokens unit `UNSETTLED (WRONG FACTS, FC5)`.
- Pass bar: `UNSETTLED (S5)` and its `suites: red` line `UNSETTLED (S6)`; every result printed beside "insufficient data (n=3)".
- Gate seat: §3 — fresh Opus 5.5, BUILD-HUB's 26 allow / 4 deny in `dontAsk`, plus `Bash(grok *)` with the builder's worktree write target as a changed builder authorization `[F-21]`.
- Results: one row per card in `reports/complexity-shadow-results-2026-10-<dd>.md`; the tribunal reads them in a second sitting within its round cap `[F-18]`.
- R411 stop: nothing launches until the SHADOW-HUB card is built, checked and approved with his sign-off on its command line.

## Dissents, verbatim
No counted house REJECTED or wrote DO NOT ADOPT on any item. Carried here, not folded, because each would re-open a ruling of his (L77):
- Q7 — Astra (ADOPT WITH), verbatim: "Compare the JEV picker blind against the frozen score baseline. Do not feed it the score during that comparison. Record agreement descriptively, but select neither router by agreement with the other. Compare their decisions against held-out task outcomes and measured cost under the same law gates. This design authorizes no JEV launch, merge or routing promotion; those remain in JEV’s own trial." — RE-OPENS A RULING (R8: "a JEV shadow run beside an Anthropic seat to 80% agreement, then JEV decides").
- Q7 — Grok (ADOPT WITH), verbatim: "The JEV picker routes blind and is compared with this score. It does not decide until it beats the score. `jev_agreement` = 80 is modelled. This packet's gloss of R8 does not state 80 (`12-PROPOSAL-R1.md:4`), so the key is not cited as his ruling." — RE-OPENS A RULING (R8); its supporting claim does not hold against R8's row (`cto-2026-10-03.md:14`).
- Q6 — round 1's own default (Gemini and Grok ADOPT it), verbatim: "name per job via the brain, no automatic seat." — RE-OPENS A RULING (R919: every merged build stays Opus 5.5 until his word on this tribunal's result; R109).

## Reading of the hypothesis
- What the trial can show (as the folds leave it): for three cards, one per band, whether Grok 4.7 building through this gate seat lands near the Opus original on the Opus check's own held findings `[F-04]`, fix rounds, suites and scope — as an indication only, "insufficient data (n=3)" (L8, `[F-01]`).
- What it cannot show: a tier; anything at n≥30; "above Sonnet and Haiku" — untested, neither is in the trial `[F-09]`; Grok's checker record — not builder evidence (§1 item 3); Grok's tokens — UNKNOWN (§2.5).
- What is not yet fixed: the verdict words themselves (`UNSETTLED (S5)`), how an environmental red is scored (`UNSETTLED (S6)`), and what Grok is shown (`UNSETTLED (S7)`).
- No verdict on Grok's tier is given here.

## The bar
- L5: the trial routes no LLM call outside the routing layer; Grok runs only through the gate seat's approved line.
- L8: n=3 — every result line reads "insufficient data (n=3)"; no grade renders as a number.
- L26: no tier assignment comes from this design; Grok's self-tier rulings are apart; unmeasured self-assignments are not folded (derive report, fold table).
- L27: $0; Claude stays on Max; Grok at its minimum tier; meter figures modelled or UNKNOWN as marked.
- L29: FROZEN — unchanged by this design; the gate seat is Opus 5.5 in `dontAsk` on a fixed file; every merged build stays Opus 5.5 until his word; L29(2)'s permission gate is X1.
- L32: no user data in this file or its results table; the live-note suite is the existing read-only gate.
- L70: every unread claim is an X above, never a defect.
- L77: R8, R109, R919–R921 are not re-opened; the three carried texts are his to take up, never the derive's.

## OWNER ITEMS
none — every house's owner section reads `none`; S5, S6 and S7 are design splits carried as A/Bs, not owner items.
