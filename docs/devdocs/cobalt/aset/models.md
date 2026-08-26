# `src/cobalt/aset/models.py`

## What it does
The Pydantic data contracts for a single sizing computation — the
vocabulary every other ASET module (`engine`, `store`, `web`,
`daily_note`) shares. No behavior beyond validation.

## Key functions/classes
- `Grade(str, Enum)` — `A_PLUS, A, B, C, D_SAW`. `D_SAW` is deliberately
  named for the Daily-Stop Model card's framing: "too risky to feel like
  a C? It's not a C — it's a SAW trade. Zero size."
- `GRADE_RISK_PCT: dict[Grade, Decimal]` — the ruled grade→risk map:
  A+ 80 / A 30 / B 15 / C 5 / D-SAW 0. This is the one place that
  mapping lives; `engine.compute_sizing` and `web.py`'s grade dropdown
  both read it, never hardcode the percentages.
- `Direction(str, Enum)` — `LONG, SHORT`.
- `SizingInput` — `ticker` (normalized to stripped-upper by a
  `field_validator`, blank rejected), `grade`, `direction`,
  `daily_stop`, `entry`, `stop` (all `Decimal > 0`), optional
  `last_price` / `price_source` (prefill metadata, never required).
  `extra="forbid"` — an unexpected field is a validation error, not a
  silently dropped one.
- `SizingResult` — the computed output: `input` (echoes the
  `SizingInput`), `risk_pct`, `risk_budget`, `per_share_risk`, `shares`,
  `used_risk`, `target_1r`, `target_2r`, `warnings: list[str]`.

## Data flow in/out
**In:** raw form fields (strings) from `web.py`, coerced to `Decimal`/
enum by Pydantic on `SizingInput(**form)`.
**Out:** validated `SizingInput` consumed by `engine.compute_sizing`,
which returns a `SizingResult` consumed by `store.py` (persistence),
`daily_note.py` (card formatting), and `web.py` (rendering).

## Config it reads
None — pure data models.
