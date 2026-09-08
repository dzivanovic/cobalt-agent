# `src/cobalt/taxonomy/slug.py`

## What it does
The trade slug — one identity per trade (ADR-0008 D3 ruling a). A
strategy note's frontmatter `trade_def:` IS the `TradeDef.id`.

## Key functions/classes
- `SLUG_PATTERN` — `^[a-z][a-z0-9]*(-[a-z0-9]+)*$`. Lowercase kebab, no
  `$`, no leading digit, no underscores, no doubled or trailing hyphen.
- `validate_slug(slug, where=)` / `is_slug(value)`.
- `trade_key(slug)` — `slug.replace("-", "_")`. The ONE conversion.
- `per_trade_scope(slug)` — `per_trade(<trade_key>)`.

## Why `trade_key` exists
The v0.7 §13.1 tunable-key grammar and the `per_trade(...)` scope accept
`[a-z0-9_]` only, so a kebab slug cannot appear verbatim in a `cfg()`
key — and to a future predicate parser `big-dog.band` reads as
subtraction. It is deliberately not the inverse of anything: the slug is
the identity, the key is a spelling of it.

## Gotchas
A display name may contain anything a human types; an id may not, because
it is matched, joined and put in URLs. `9 EMA Scalp` is `nine-ema-scalp`.
`trade_key` validates first — a bad slug must not be silently converted
into a plausible key.
