"""Which card, which value — resolved by CODE, never guessed (FINAL §4, [F-10]).

CARDS. Candidates are the OPEN cards (`CardStore().open_cards()`), each
with a code-rendered label. The Plan's card argument is a verbatim span
(ticker text, spoken letters allowed) or a candidate id from that closed
list; a side word (long / short) and an ordinal (first / second / third)
INSIDE that card span narrow — the rest of the transcript never does. Exactly one → bound. Zero or two-plus → clarify,
reading the candidates back by label. Never the nearest, never the
earliest, and the floating widget sends no card id — so no argument means
clarify, even with one open card.

VALUES. Deterministic parsers per field type (price, share count, time).
Unparseable → `Unparseable` → the turn clarifies. The price parser
REFUSES a clock shape (`H:MM`, X-X5) and a spoken form without "point"
("four fifty" is 4.50 or 450 — ambiguous, X-X12): the read-back never
speaks a guessed price.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import time as dtime
from decimal import Decimal, InvalidOperation
from typing import Any, Optional

from .models import CandidateRef, CardCandidate, Span


class Unparseable(ValueError):
    """A dictated value the parser will not guess at — the turn clarifies."""


# --- cards -----------------------------------------------------------------------


def card_candidates(rows: list[dict[str, Any]]) -> list[CardCandidate]:
    """Open-card rows → the closed candidate list the prompt carries."""
    out = []
    for r in rows:
        ticker, direction, state = str(r["ticker"]).upper(), str(r["direction"]), str(r["state"])
        out.append(CardCandidate(id=f"card-{r['id']}", card_id=int(r["id"]), ticker=ticker,
                                 direction=direction, state=state,
                                 label=f"{ticker} {direction} {state} (card {r['id']})"))
    return out


@dataclass(frozen=True)
class CardResolution:
    bound: bool
    card_id: Optional[int] = None
    candidate: Optional[CardCandidate] = None
    clarify: Optional[str] = None


_ORDINALS = {"first": 0, "second": 1, "third": 2, "fourth": 3}
#: Words of a card span that qualify the card, not spell its ticker.
_SPAN_QUALIFIERS = {"the", "long", "short", *_ORDINALS}


def _ticker_of(span: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "", span).upper()


def _readback(cands: list[CardCandidate]) -> str:
    return "; ".join(c.label for c in cands)


def resolve_card(args: dict, transcript: str, candidates: list[CardCandidate]) -> CardResolution:
    if not candidates:
        return CardResolution(False, clarify="You have no open card.")
    value = args.get("card")
    if value is None:
        return CardResolution(False, clarify=f"Which card? Open: {_readback(candidates)}.")
    if isinstance(value, CandidateRef):
        hit = [c for c in candidates if c.id == value.candidate]
        if len(hit) == 1:
            return CardResolution(True, hit[0].card_id, hit[0])
        return CardResolution(False, clarify=f"Which card? Open: {_readback(candidates)}.")
    assert isinstance(value, Span)
    # The side word and the ordinal are read from the Plan's card SPAN only —
    # never from the rest of the transcript (FINAL §4 item 2; fix r1 B1).
    span_words = value.span.split()
    words = {w for t in span_words for w in re.findall(r"[a-z]+", t.lower())}
    ticker_words = [t for t in span_words if t.lower() not in _SPAN_QUALIFIERS] or span_words
    ticker = _ticker_of(" ".join(ticker_words))
    matches = [c for c in candidates if c.ticker == ticker]
    if not matches:
        return CardResolution(False, clarify=f"There is no open card on {ticker or 'that'}. Open: {_readback(candidates)}.")
    sides = {"long", "short"} & words
    if len(matches) > 1 and len(sides) == 1:
        side = next(iter(sides))
        matches = [c for c in matches if c.direction == side] or matches
    if len(matches) > 1:
        ords = [o for w, o in _ORDINALS.items() if w in words]
        if len(ords) == 1 and ords[0] < len(matches):
            matches = [sorted(matches, key=lambda c: c.card_id)[ords[0]]]
    if len(matches) == 1:
        return CardResolution(True, matches[0].card_id, matches[0])
    return CardResolution(False, clarify=f"Which {ticker} card? {_readback(matches)}.")


# --- numbers ---------------------------------------------------------------------

_UNITS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen "
    "fifteen sixteen seventeen eighteen nineteen".split())}
_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
         "eighty": 80, "ninety": 90}
_DIGIT_WORDS = {**{w: str(i) for w, i in _UNITS.items() if i < 10}, "oh": "0"}


def _int_words(tokens: list[str]) -> Optional[int]:
    """'two hundred fifty' → 250; None if any token is not a number word."""
    if not tokens:
        return None
    total, cur, seen = 0, 0, False
    for t in tokens:
        if t in ("a", "and") and seen is False and t == "a":
            cur = 1 if cur == 0 else cur
            continue
        if t == "and":
            continue
        if t in _UNITS:
            cur += _UNITS[t]
        elif t in _TENS:
            cur += _TENS[t]
        elif t == "hundred":
            cur = (cur or 1) * 100
        elif t == "thousand":
            total += (cur or 1) * 1000
            cur = 0
        else:
            return None
        seen = True
    return total + cur if seen else None


_PRICE_DIGITS = re.compile(r"^\d{1,7}(\.\d{1,4})?$")
_CLOCK = re.compile(r"\d{1,2}:\d{2}")


def parse_price(text: str) -> Decimal:
    raw = (text or "").strip().lower()
    if not raw:
        raise Unparseable("no price was said")
    if _CLOCK.search(raw) or re.search(r"\b[ap]\.?m\.?\b", raw):
        raise Unparseable(f"{text!r} is shaped like a time, not a price")
    s = raw.replace("$", " ").replace(",", "")
    s = re.sub(r"\b(dollars?|bucks?|usd)\b", " ", s)
    s = " ".join(s.split())
    if _PRICE_DIGITS.match(s):
        value = Decimal(s)
    else:
        tokens = s.replace("-", " ").split()
        if "point" not in tokens:
            if tokens and all(t in _UNITS or t in _TENS or t in ("hundred",) for t in tokens) and len(tokens) >= 2:
                raise Unparseable(f"{text!r} is ambiguous (a spoken price without 'point')")
            raise Unparseable(f"{text!r} is not a price")
        i = tokens.index("point")
        whole = _int_words(tokens[:i]) if not (len(tokens[:i]) == 1 and tokens[0].isdigit()) else int(tokens[0])
        frac_tokens = tokens[i + 1:]
        if whole is None or not frac_tokens or not all(t in _DIGIT_WORDS or t.isdigit() for t in frac_tokens):
            raise Unparseable(f"{text!r} is not a price")
        frac = "".join(_DIGIT_WORDS.get(t, t) for t in frac_tokens)
        if len(frac) > 4:
            raise Unparseable(f"{text!r} has more than four decimals")
        value = Decimal(f"{whole}.{frac}")
    if value <= 0:
        raise Unparseable(f"{text!r} is not a positive price")
    try:
        if value.as_tuple().exponent < -4:
            raise Unparseable(f"{text!r} has more than four decimals")
    except InvalidOperation:  # pragma: no cover
        raise Unparseable(f"{text!r} is not a price") from None
    return value


def parse_shares(text: str) -> int:
    raw = (text or "").strip().lower().replace(",", "")
    raw = re.sub(r"\bshares?\b", " ", raw).strip()
    if re.fullmatch(r"\d{1,7}", raw):
        n = int(raw)
    else:
        n = _int_words(raw.replace("-", " ").split())
        if n is None:
            raise Unparseable(f"{text!r} is not a share count")
    if n <= 0:
        raise Unparseable(f"{text!r} is not a positive share count")
    return n


def parse_time(text: str) -> dtime:
    raw = (text or "").strip().lower().replace(".", "")
    m = re.fullmatch(r"(\d{1,2}):(\d{2})\s*(am|pm)?", raw)
    if not m:
        raise Unparseable(f"{text!r} is not a clock time (H:MM)")
    h, mi, ap = int(m.group(1)), int(m.group(2)), m.group(3)
    if ap == "pm" and h < 12:
        h += 12
    if ap == "am" and h == 12:
        h = 0
    if not (0 <= h <= 23 and 0 <= mi <= 59):
        raise Unparseable(f"{text!r} is not a clock time")
    return dtime(h, mi)


__all__ = ["CardResolution", "Unparseable", "card_candidates", "parse_price", "parse_shares",
           "parse_time", "resolve_card"]
