# ADR-0009 — Radar cards: the scoring seam and the precondition AST

Date: 2026-09-16
Status: Accepted (rulings R1–R11 of 2026-09-15, Dejan; plan reviewed by Astra ≤3 rounds); implemented on `sprint-2/cards` (S2-P2 chunks A–C), not yet merged.
Implements: plan `docs/40 - DevDocs/plans/plan-s2-p2-2026-09-15.md`. Meets L52 (tribunal before build for anything that reaches the card) through the plan's §L52 table. Relates to: ADR-0001/0003 (trade_defs as data, tunables), ADR-0004 (the one vault write path), ADR-0008 (tenancy; the placement map this ADR extends).

## Context

S2-P1 put a pool of names and their bars in `system`. S2-P3 put a read-only `/radar` page in front of it with an empty ladder that failed loud on any radar card. Two things stood between them:

- A trade_def's preconditions were `expr` strings nobody parsed (`computable = expr is not None`). Nothing could say whether a setup had formed.
- The 09-14 tribunals ruled what reaches the card — one ranking authority, `card_score = round(conviction × proximity × 100)`; dots per quality factor; desk-graded `catalyst`/alignment dots in shadow; the missing-data rules — but no seam existed to carry it, and no audit path for another house (L52-d).

## Decision

### D1 — Precondition grammar is a parsed AST (R3)
`taxonomy/predicate.py` parses every §10.5 `expr` into a frozen Pydantic AST when a `TradeDef` validates. A note that does not parse fails loud with note path, line and slug; notes are never edited to fit the parser. The AST is derived, so it never enters the stored def or its md5. `required_atoms(ast)` names what detectors must serve; a def with unserved atoms is `not_evaluable: missing atoms […]` and never produces a card (R2). Evaluation is three-valued: unmeasured is unknown, not false.

### D2 — S5 evaluate is a scan-job stage with a two-sided seam (R1, R9)
`radar/evaluate.py` runs after S4 bars behind the same market_reset gate. Each run writes, in publish order: `system.radar_score_run` (`running`) → `system.radar_score` rows (a closed, generic payload — no trade_def prose or trader settings, L32) → user-side cards/dots when enabled → `"user".radar_score_receipt` → `complete`. `system.radar_board_v` shows complete runs only, so a crash never publishes a partial. The two sides cannot share a transaction (ADR-0008); open-card uniqueness is a partial unique index, not a check-then-insert.

Placement (ADR-0008 D2 extended; enforced by `test_tenancy.py`): SYSTEM — `radar_score_run`, `radar_score`, `radar_board_v`, `desk_regime`, `desk_packet`, `desk_grade`. USER (user_id NOT NULL + FK + GUC default) — `card_dots`, `card_dot_taps`, `radar_score_receipt`, `radar_cards_v`, `shadow_agreement_v`; radar cards are `"user".aset_sizings` rows with `origin='radar'`, born unsized.

### D3 — Stored inputs, not hashes (L57, Astra R1-10)
Every run — dark included — writes one immutable receipt retaining the consumed VALUES: pool unit, tunable rows, card settings, definitions, tap versions, and every bar/daily/RVOL observation with its hash, locator and validity. Receipts chain deltas within a process (plan ESCALATE, carried). `replay_receipt` recomputes every published number from receipts alone.

### D4 — One ranking authority; shadow dots (R6, R7, R8)
`card_score` is the only number that orders WATCH cards; pool `last_rank` only admits. Computed and desk dots are `shadow`: stored, shown hollow, tappable, outside conviction until a curve tribunal and an L7 promotion. Conviction is the mean of taps; no taps → null, never zero. Curves and proposed-key bands are trader settings (`card.curves`, `card.proposed_key`), never tunables (L53). A key tap records the tapped grade and sizes at the nearest enabled key below, or refuses.

### D5 — The panel reads one user-side view (STEP-8)
`/radar` reads `"user".radar_cards_v` (system cannot read user data) through `CardStore.radar_board_cards`. Every view column carries an owner badge (`COBALT` / `YOU` / `LEDGER`); the panel refuses to import when columns and badges disagree. Writes are `fetch` POSTs to four `/radar/card/{id}/…` routes, pinned by an explicit POST allowlist test; the GET routes are guarded by fail-on-call sentinels for every sheet helper that could write.

### D6 — Taxonomy v0.8: `catalyst`, gated (R10)
Schema 0.5 adds `catalyst` to the standard quality factors; the loader enforces 0.4 until every defined note carries it. The notes move through one review file (per-row keep/drop) and one batch apply bound to the file's sha256 and each unit's sha256, preflighted before any write, resumable, and re-read at 0.5 before the gate may flip (a code change, STEP-D4). A card open when its def gains a factor refreshes against the same slug's new def and gains the dot once (Astra R2-4). The review file's default path is `docs/_inflight/catalyst-review-<date>.md`, not a committed DevDocs path — it carries note paths and factor names (user data, L32); `--out` overrides for a caller who wants it committed as the R10 record. Desk ruling, chunk C ESCALATE 3, 2026-09-16: this also surfaced that `docs/_inflight/*` was not actually gitignored beyond `README.md` (the un-ignore never re-ignored other files placed inside), fixed the same session.

### D7 — Audit and promotion evidence
`cobalt radar audit-export` writes a frozen bundle (bars window, settings, tunables, AST, definitions, published cards, seam rows, receipts, formulas, manifest of hashes) and refuses when Cobalt's own replay of the stored inputs disagrees with what it published. `cobalt cards shadow-report` scores tap-vs-engine pairs per factor against `card.shadow_promotion_bar` and flips nothing.

## Consequences

- Cards ship dark (`radar.cards_enabled=false`); the trader's own `settings load --apply` after the dev replay and the other-house audit is the enable (R9, R11).
- Only one def is evaluable end-to-end in S2; the others name their missing atoms until S3 detectors land.
- Alignment dots are N/A through S2 (no dated ruling authorizes a default map); `trail_fit` is N/A and suppresses the score until tapped or re-sourced by the trader (R5 draft).
- Migration 0007 is two rollback domains away from the sheet's own rows; the rollback procedure is the plan's §6 R1-18 amendment, proven on cobalt_dev before D1.
- Owed: curve tribunal (S3), HITL token issuance (L7 enforcement arm), desk grades (S3-P0), a cross-process Finviz demand ledger.
