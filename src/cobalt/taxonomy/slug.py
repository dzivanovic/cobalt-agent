"""The trade slug — one identity per trade (ADR-0008 D3 ruling a).

THE SLUG IS THE ID. A strategy note's frontmatter `trade_def:` key names
the trade, and that string is the `TradeDef.id` the loader injects. There
is no second identifier: the YAML unit no longer authors `id:`, and a
unit that still carries one fails loud.

SHAPE. Lowercase kebab — `[a-z][a-z0-9]*(-[a-z0-9]+)*`. A display name
may contain anything a human wants to type (a `$`, a digit, spaces,
capitals); the slug may not, because it is an identity and identities are
matched, joined and put in URLs. So `9 EMA Scalp` is `nine-ema-scalp`: no
`$`, no leading digit, no underscores, no spaces, no trailing or doubled
hyphens.

AND THE GRAMMAR-SAFE SPELLING. The v0.7 §13.1 tunable-key grammar and the
`per_trade(<id>)` scope accept `[a-z0-9_]` only, so a kebab slug cannot
appear verbatim in a `cfg()` key — and to a future predicate parser
`big-dog.range_duration_band` reads as subtraction. `trade_key()` is the
ONE conversion, used everywhere a slug has to enter that grammar:

    trade_key("nine-ema-scalp") == "nine_ema_scalp"

It is deliberately not the inverse of anything: `-` maps to `_` and
nothing maps back, because the slug is the identity and the key is a
spelling of it.
"""

from __future__ import annotations

import re

#: Lowercase kebab, no leading digit, no doubled or trailing hyphen.
SLUG_PATTERN = re.compile(r"^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$")

#: What a slug looks like once it enters the `cfg()` / `per_trade()`
#: grammar. Kept next to the slug pattern so the two never drift.
TRADE_KEY_PATTERN = re.compile(r"^[a-z][a-z0-9]*(?:_[a-z0-9]+)*$")


class SlugError(ValueError):
    """A trade slug is malformed — crash, never normalise it quietly."""


def validate_slug(slug: str, *, where: str = "") -> str:
    """Return `slug` or raise. `where` names the note in the message."""
    prefix = f"{where}: " if where else ""
    if not isinstance(slug, str) or not slug:
        raise SlugError(
            f"{prefix}the frontmatter `trade_def:` key is missing or empty. "
            "It IS the trade's id (ADR-0008 D3 ruling a) — there is no other "
            "identifier to fall back to."
        )
    if not SLUG_PATTERN.match(slug):
        raise SlugError(
            f"{prefix}invalid trade slug {slug!r}. A slug is lowercase kebab "
            f"({SLUG_PATTERN.pattern}): no '$', no leading digit, no "
            "underscores, no spaces, no doubled or trailing hyphen. The "
            "frontmatter `name:` is where a display spelling belongs — a "
            "trade may be called anything; its id may not."
        )
    return slug


def is_slug(value: str) -> bool:
    return bool(isinstance(value, str) and SLUG_PATTERN.match(value))


def trade_key(slug: str) -> str:
    """The grammar-safe spelling of `slug` for `cfg()` keys and
    `per_trade(...)` scopes. The one conversion; never inlined."""
    return validate_slug(slug).replace("-", "_")


def per_trade_scope(slug: str) -> str:
    """The tunables `scope` a per-trade row of `slug` must carry."""
    return f"per_trade({trade_key(slug)})"


__all__ = [
    "SLUG_PATTERN",
    "TRADE_KEY_PATTERN",
    "SlugError",
    "is_slug",
    "per_trade_scope",
    "trade_key",
    "validate_slug",
]
