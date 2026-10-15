# JEV shadow design — the 8 DECISIONS ruled (brain `0e848919`, 2026-10-14)

On `docs/30 - Design/jev-shadow-design-2026-10-14.md` `## DECISIONS` (:182-191), for the desk's DESK RECORD and the L67 tribunal packet. His rulings applied: R1467 (JEV alone on the OpenRouter key; shadow first; live on his word), R42 ($5 cap), 10-08 secrets (never read or sent), L29, L32.

Hold: 1, 2, 3, 5, 6, 8 KEEP DEFAULT · 4 CHANGE · 7 CHANGE (one question to him by day).

| # | ruling | reason |
|---|---|---|
| 1 spend cap | KEEP DEFAULT: the ruled $5 TOTAL (R42), trial and shadow together; no new number | Money already ruled. At the design's own rate (≈ $0.0002 per 5,000-token card) $5 is ≈ 25,000 calls, years of shadow. A new number would be his; none is needed. |
| 2 check 74 | KEEP DEFAULT: check `74` on `jev/trial-0923` first; the router card builds on its READY tip | The trial code was never checked (r3 ESCALATE 7); nothing builds on an unchecked tip. |
| 3 min_confidence | KEEP DEFAULT: no cut in shadow; every band stored with its confidence | Shadow acts on nothing, so a cut changes nothing; setting it before data would tune on the rows used to claim success ([F-13]). |
| 4 MID candidate | CHANGE: the decision row records BOTH MID candidates (`grok-4.7`, `gpt-5.6-terra`) with `rule_path: table-pending`, and names one only from the routing-table config once he rules on `reports/routing-table-answer-2026-10-14.md`. No tie-break is invented in the design. | The default's tie-break read r1 only (Grok UNSCORED); r2 has since graded Grok MID (368 AT LEVEL, 379 CLOSE BELOW), and the proposed table puts MID as "Grok or Terra by meter". The router reads the table; it never decides it. |
| 5 ledger home | KEEP DEFAULT: append-only generated JSONL in the repo, no migration | No write path (L29), readable by the tribunal and the desk. Rows hold paths, shas and typed answers only, never card text (L32). |
| 6 when it runs | KEEP DEFAULT, one condition added: the nightly-close batch step. A JEV failure (refused, http error, cap reached, wrapper missing) writes `status` rows and NEVER fails or delays the close; the close's verdict ignores the step. | The close is a standing MUST (10-05 ROW B); a shadow step may not put it at risk. |
| 7 X1 old-tree key entry | CHANGE: no seat runs `has_secret` or any vault unlock. A presence check still opens the password store, which his 10-08 rule keeps closed. X1 is closed by code, not by a question (see `## X1 — WITHDRAWN` below): the card removes the old-tree injection and proves the router never imports `cobalt_agent`. | Secrets are never read or sent; the route is his hand, by day, not a seat. |
| 8 Sonnet's role | KEEP DEFAULT: no Sonnet call in shadow; baselines `score_band` and `rows_band` | "Sonnet only as router and hub" is about builds; shadow needs no extra arm, and it costs nothing. |

## X1 — WITHDRAWN 2026-10-15 (no question to him)
`src/cobalt_agent/config.py:493-505` injects `openrouter_api_key` (and the openai, anthropic, gemini keys) into the old LLM config when the vault holds it: a pay-per-token path R1112 forbids either way. The JEV card carries a row removing the `openrouter_api_key` entry from that mapping (red: a test vault holding it gets it injected today, not after), so §7 is the exception's whole surface without anyone opening the store. The other three keys are a separate R1112 card, not JEV's.

## FOR THE CHECK
`JEV design DECISIONS: 1,2,3,5,6,8 KEEP DEFAULT; 4 both MID candidates recorded, table-pending until his word; 6 a JEV failure never fails the close; 7 no vault presence check by any seat — brain 0e848919 10-14`
`JEV X1 withdrawn: the old-tree injection of openrouter_api_key is removed by the JEV card regardless of vault contents (R1112); no vault presence check, no question to him — brain 0e848919 10-15`
