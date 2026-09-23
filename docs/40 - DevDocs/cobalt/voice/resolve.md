# `src/cobalt/voice/resolve.py`

## What it does
Answers "which card" and "which value" with code (FINAL §4).

## Cards
`card_candidates` turns the open-card rows into the closed candidate list
(`card-<id>` + the label `TICKER direction STATE (card N)`).
`resolve_card` binds the Plan's `card` argument: a candidate id from that
list, or a verbatim span whose letters (spoken `X Y Z`, `x.y.z.`) normalize
to a ticker. With two-plus matches, the transcript's own side word (long /
short) and then an ordinal (first / second / …, in card-id order) narrow.
Exactly one → bound; zero or two-plus → a clarify line that reads the
candidates back. No argument → clarify, even with one open card: the
floating widget sends no card id and nothing is picked for him ([F-10]).

## Values
- `parse_price`: digits with up to four decimals (`$` and "dollars"
  ignored) or a spoken form WITH "point" ("four point five zero" → 4.50).
  Refused (the turn clarifies): a clock shape `H:MM` / am / pm (X-X5), a
  spoken form without "point" ("four fifty" — 4.50 or 450, X-X12), zero,
  negatives, more than four decimals, anything with other words around it.
- `parse_shares`: digits or number words ("two hundred fifty"), positive.
- `parse_time`: `H:MM` with optional am / pm only.
Every refusal is `Unparseable`; the read-back only ever speaks a PARSED
value.
