# Typed decisions, broad research — report (2026-09-21)

## §0 Headline
- Done: `docs/30 - Design/TYPED-DECISIONS-PATTERNS-RESEARCH-2026-09-21.md` — 11 of 11 domains, 23 sourced examples, 11 design rules, 10 Cobalt transpositions (his trade-grade first), 19 trial measurements, plus §6A on question types and confidence (R37).
- Status: both files written, NOT committed (no git write allowed; they sit in `~/cobalt`).
- Thin spots: aviation is second-hand, legal has a protocol but no verified results, admissions rubrics not found. ESCALATE: 4.

## DIGEST FOR THE DESK
1. Every field that decides fast and defensibly does the same thing: many small closed questions, gated early, combined by a written table.
2. Pattern one, the scorecard: credit scoring bins each factor, gives each bin points, sums them in code, and explains a decline by the points lost against the best possible answer. This is the shape for his trade-grade.
3. Pattern two, the cascade: cheap deterministic checks first, the model only on what is left. DoorDash cleared over 90 percent of messages with a sub-100-millisecond classifier before any large model ran.
4. Pattern three, gate then check, with a default that stands when unsure: emergency triage, the football video referee, and aircraft fault trees all work this way.
5. Pattern four, a checklist of yes-or-no items graded by a small model, with weights in code: the checklist papers and the surgical checklist.
6. Pattern five, keep one human-only leaf: the referee's judgment calls, the one subjective item in the clinical rule, the scout's overall grade. For Cobalt that is the tape read.
7. The design rules in one breath: gate early, decompose into narrow questions, say who combines and prefer the table, close the endpoints, set the unsure default by consequence, explain with the components, bucket numbers first, keep a human leaf, measure against a gold set, treat wording as part of the model, plan the maintenance.
8. Where the combining happens inside a model or a head, agreement was low: Bing's relevance labels swung 0.50 to 0.72 in kappa from rewording alone; scouts differ by five points routinely; triage nurses were 59.6 percent accurate.
9. Speed: what is published is thin. One vendor cookbook shows 13 questions in one call at 0.27 seconds against 2.71 sequential. One integrator measured 127 milliseconds median, 231 at the 95th percentile, on a single-choice router. Nobody has published a 20 to 30 question tree, a local-model figure, or where the milliseconds go from his machine.
10. Milliseconds do not matter for the scan tick. They matter for a card forming while he watches, for interactive turns, and most of all for shadow backfill: a test of a reworded question set over five thousand stored cards could take minutes instead of days.
11. Confidence exists for Choice and Score only, is a shape statistic of the probability spread, not a chance of being right, and Noul, the yes-no type, has none. Independent tests found Choice and Score overconfident and Noul underconfident, so floors must be per type.
12. Three transpositions he will care about: his trade-grade as a scorecard with the answer vector as the explanation; news and squawk triage as a cascade; rule-adherence and journaling as a checklist that only proposes, never fills his attestations.
13. The trial must measure: network floor, marginal cost per question up to 40, one call versus a gated chain, determinism, question-order effects, the local model on the same questions, end-to-end event-to-stored time, backfill speed, and per-type reliability on his own hand labels.

## BUDGET USED
- Fetches: 47 of 48 (40 + 8 added by R37); 13 returned nothing usable (3 unreadable PDFs, 4 × 404, 2 cookie walls, 1 disambiguation page, 2 redirects re-fetched, 1 × 403). Searches: 18 of 23 (20 + 3). Local reads: 5 of ≤15 (prompt, first pass, second pass, LAWS.md ×2; CLAUDE.md came in the session context). Document: 369 lines against 550 + 60.
- Nothing installed, run or signed up for; no call to the vendor; no vault or memory write; no git write.

## ESCALATE
1. Both output files are uncommitted in `~/cobalt` (the production checkout, L54 / L46) — this seat has no git write and no worktree. The desk commits them and leaves the tree clean.
2. The §6A request and its +8 fetch / +3 search / +60 line allowance arrived as a cross-session message from the desk's wake-up prompt, not typed into this session. I acted on it as the desk's relay; I cannot verify it. Used: 7 fetches, 0 searches.
3. 13 of 47 fetches returned nothing usable, mostly PDFs the tool cannot read and moved URLs. Future research prompts should name HTML or abstract-page URLs; the Sedona e-discovery paper, the ESI Handbook and the AML preprint were lost this way.
4. ASK DESK: should the trial measure from the Mac Studio only, or also from a second network location so network time and model time can be split? Default used: Mac Studio only, with client-side timing [any time].

## CONTINUE
Nothing owed to this seat. If wanted: a follow-up pass on the thin spots (Wells derivation paper, admissions rubrics, e-discovery recall and precision, aviation fault-tree data), fetched as HTML.

TYPED DECISIONS BROAD RESEARCH DONE · domains covered: 11 of 11 · examples: 23 · design rules: 11 · transpositions: 10 · latency facts found: 8 · trial measurements listed: 19 · fetches: 47/48 · searches: 18/23 · ESCALATE: 4
