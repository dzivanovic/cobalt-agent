# Complexity routing proposal · drafter report · 2026-10-10

## §0 Headline
- Proposal written: `reports/complexity-routing-proposal-2026-10-10.md`, for the L67 tribunal.
- Data: 27 next-flow checks, 26 builds with tokens since 10-06. n<30: insufficient data (L8). All of them ran on Opus 5.5, so the data shows no difference between models.
- Rule: log a launch-time complexity score in shadow. Trial Sonnet vs Opus only on non-write drafters and preflights. Builds and checks stay unchanged.
- Money: $0 change (L27). The meter effect is UNKNOWN until drafters carry `tokens:`.

## CHANGES
- Added `docs/40 - DevDocs/reports/complexity-routing-proposal-2026-10-10.md`.
- Added `docs/40 - DevDocs/reports/complexity-propose-2026-10-10.md`.
- No commit, launch, DB or production command was run.

## DECISIONS
1. Ledger path: the prompt names `PROJECT-LEDGER.md:2704` with no folder. Read `docs/00 - Project/PROJECT-LEDGER.md:2704` (R73). Default taken.
2. Sample window: took next-flow jobs (Sol + Grok at once, `tokens:` in the stop line) from 10-06 to 10-10. Pre-10-05 jobs have no tokens (`gain-measure-survey-2026-10-05.md:14`). Default taken.
3. Drafter, preflight and hub per-job tokens: not found in the reports read. Recorded as UNKNOWN (L70), not estimated. Default taken.
4. https-only build tokens: its build report is not in main `reports/`. Recorded as UNKNOWN. Default taken.
5. Score weights and band cut points are modelled and marked as such. The tribunal and the shadow log set them (Q4). Default taken.

## RECORDS
- Inputs read: `s5-weekend-and-parked-answer-2026-10-10.md`; `PROJECT-LEDGER.md:2695-2712`; `cto-2026-10-0{5..9}.md`, `cto-2026-10-10.md` (MEASURE/touches grep); `topics/cto-desk-contract.md` `## Seats`; `areas/cobalt-houses.md:20-32`; `cto-2026-10-03.md:14`; `routing-tribunal-2026-09-22.md` (headings, rulings, experiments); `LAWS.md` L5, L8, L21–L29, L52, L67–L71; `seat-usage.md:23-48`; `gain-measure-survey-2026-10-05.md`; stop lines of every `*-build-`, `*-check-` and `*-fixround-2026-10-*.md`.
- Tribunal questions: Q1–Q8, each with a default (proposal §8).
COMPLEXITY PROPOSAL DRAFTED · decisions: 5
