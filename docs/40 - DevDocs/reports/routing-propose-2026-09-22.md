# routing-propose-2026-09-22 — seat `routing-propose-0922` (Opus 5.5, `claude-opus-5-5`)

## §0 Headline
- **Wrote:** `docs/30 - Design/ROUTING-PROPOSAL-2026-09-22.md` (24,950 bytes, cap 25 KB), the one house's proposal for the routing tribunal (L67; `cto-2026-09-22.md` R81). Started 18:33 EDT, finished 18:39 EDT (`date`). Nothing committed. No vault, DB or memory writes.
- **Core finding:** "routing" names two subjects. ENGINE routing: `src/cobalt/` makes 0 model calls (grep), so L5 binds nothing in new-core. SEAT routing: all of today's routing, made by rulings, with no seat table anywhere. The proposal separates the two and puts every seat assignment in one seat table. Model ids stay out of the law (L31).
- **Clause count:** 10 clauses covered (6 frozen + 4 cluster laws). 8 rewritten. 3 OPEN FOR DEJAN. 15 seat-map rows. 12 items open to the tribunal. ESCALATE 1.

## Clauses

| clause | disposition | key evidence (measured) |
|---|---|---|
| L5 | REWRITTEN: covers engine calls only; seats go to L26/L29 | 0 model calls in `src/cobalt/`; only bypasses are old-tree (TRIAGE:43, :125) |
| L24 | REWRITTEN: rungs are a cost order, not an assignment; vendor name out | local used 684–1,067 output tokens/day 09-16→22; paid-API rung never used |
| L26 | REWRITTEN: seat table; MEASURED vs RULED evidence; spec-class key | no routing config exists; bake-off queued since 09-10; Terra has 15,605 output tokens ever |
| L27 routing sentence | OPEN FOR DEJAN (D2), with house-neutral option A | Codex ran out mid-week twice (09-16, 09-22); Astra and Sol hold standing seats (L67, R46) |
| L29 | REWRITTEN: write-path conditions (1)(2)(3); clause trace, .6 kept; D1 open | 4 Sonnet 5 production deploys with no write path = DONE, 0 rollbacks (`11-panel-order-deploy.md` "WHY NOT OPUS") |
| L49 | marker removed, text kept | practice matches exactly: day-open verdict only, GREEN daily |
| L21 | unchanged | — |
| L22 | wording only (vendor names out) | L31 |
| L23 | "first candidate ASSESSED", not assigned; resolves audit C11 | C11 |
| L25 | pointer "ADR-0008's bake-off table" → seat table; vendor name out | ADR-0008 has no bake-off table |

## Open for Dejan (A/B, recommendation)

| # | question | recommendation |
|---|---|---|
| D1 | Production write paths: always the top implementation model (A), or earnable by trial like dev paths (B)? | A |
| D2 | L27's Codex-overflow sentence: replace with the house-neutral allowance sentence (A), or keep it (B)? | A |
| D3 | Local seat as Cobalt's hub: keep as plan of record, gated on a measured trial (A), or retire it (B)? | A |

## ESCALATE (1)
1. **L25 points at nothing.** It moves task classes "in ADR-0008's bake-off table". `grep -i bake-off "docs/10 - Decisions/"` returns no match, and ADR-0008 (23,552 bytes) has no such table, only D6's local adapter contract. Until the tribunal repoints it (T9), a worker who follows L25 cannot comply.

## Notes
- **Not produced:** the retrospective validation LEDGER:1325 ordered. The proposal lists 5 known data points and makes the full table tribunal item T6, a hub job. The rubric does not bind until T6 is done.
- **Stale document, not law:** `docs/50 - Roles/MODELS.md` still lists `claude-fable-5` and has no seat map (R32's ops item). T4 proposes rendering it from the seat table.
- **Measurement gaps:** agy usage is not in `ccusage`; the Codex meter is known only by probe; `claude-opus-5-5` and `claude-fable-5-1` are UNPRICED (T12).
- **Untouched:** the files already dirty or untracked in `~/cobalt` at launch (`configs/cobalt/rules.yaml`, the two `reports/` edits, `day-open-2026-09-22.md`, the grok stdout tmp) are not from this seat.

ROUTING PROPOSED · clauses: 10 · rewritten: 8 · open for Dejan: 3 · seat-map rows: 15 · open to the tribunal: 12 · ESCALATE: 1
