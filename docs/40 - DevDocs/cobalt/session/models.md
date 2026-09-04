# `src/cobalt/session/models.py`

## What it does
Defines what a session **is**: the `Session` enum, plus
`BLOCKED_SESSION` — one name for "the session Cobalt refuses to write
in", imported by the guard and by everything that has to explain itself.

## Key functions/classes
- `Session(str, Enum)` — `PREMARKET`, `RTH`, `AFTERMARKET`,
  `MARKET_RESET`, `OVERNIGHT`. The `str` mixin means a value stamps
  straight into a `text` column and compares equal to its own name in
  SQL. `__str__` is overridden so `f"{session}"` is `"rth"`, not
  `"Session.RTH"` — the difference between a readable refusal message
  and a leaked repr.
- `BLOCKED_SESSION = Session.MARKET_RESET`.

## Safety properties
**Five values, total and mutually exclusive** — every instant in every
year resolves to exactly one. There is deliberately **no `UNKNOWN`
member**: an instant the calendar cannot answer for raises
`CalendarError` rather than resolving to a sixth, quiet value that would
then be stamped onto a card row and counted.

## Tests
`tests/cobalt/test_session.py::test_session_enum_stamps_as_plain_text`,
plus every other case in that module by construction.
