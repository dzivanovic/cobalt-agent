"""What a session IS. Charter §3 F1.

Five values, total and mutually exclusive: every instant in every year
resolves to exactly one of them. There is no "unknown" member on
purpose — an instant a calendar cannot answer for raises
`CalendarError` rather than resolving to a sixth, quiet value that
would then be stamped onto a card row (fail-loud law).
"""

from __future__ import annotations

from enum import Enum


class Session(str, Enum):
    """The session an instant falls in, on Dejan's ET trading clock.

    `str` mixin so a value stamps straight into a `text` column and
    compares equal to its own name in SQL and in a template.
    """

    PREMARKET = "premarket"
    RTH = "rth"
    AFTERMARKET = "aftermarket"
    MARKET_RESET = "market_reset"
    OVERNIGHT = "overnight"

    def __str__(self) -> str:  # so f"{session}" is "rth", not "Session.RTH"
        return self.value


#: The session in which Cobalt refuses to write (Charter §3 F1: "the
#: 21:30 one is blocked" — the 20:00-21:00 window, SPRINT-LADDER §S1
#: "market_reset 20:00-21:00 hard-block"). One name, imported by the
#: guard and by every caller that needs to explain itself.
BLOCKED_SESSION = Session.MARKET_RESET
