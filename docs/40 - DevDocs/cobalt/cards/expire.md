# `src/cobalt/cards/expire.py`

## What it does
`cobalt cards expire` — moves `WATCH`/`ARMED`/`TRIGGERED` cards to
`EXPIRED` once their window has closed. Run by
`com.cobalt.cards-expire` at **16:05 ET, Mon–Fri**.

## Why expiry is a job, not a predicate
"Is this card still live?" *could* be computed on read — but then no
transition row would ever be written for it, and F7's law is that no
state changes without one. A card that quietly stopped counting is
exactly the card that makes the DRC's "unfilled cards reconciled"
column wrong. So expiry is an **act**, with an actor (`cobalt`), a
clock, and evidence naming the window that elapsed.

## The window, and the one judgement call
Mock open-question #9: "window per `trade_def` via
`preferred_windows_ref`". That field is **free prose written for
humans** — the thirteen shipped trade_defs carry things like
`"sheet: 9:59-4:00"` and `"Power hour 3 PM-close"`. It is not a machine
contract.

The asymmetry that drives the design: falling back to the session close
expires a card **late** (harmless — the job runs again), while
mis-resolving expires it **early** (it kills a live card still inside its
window). So `_resolve_window_end` returns a time **only** when the string
is unambiguous, and returns `None` (meaning "use the session close") for:

| Case | Example | Why |
|---|---|---|
| no clock time at all | `First 15 minutes of the trading day` | nothing to read |
| open-ended tail | `Power hour 3 PM-close` | max time is 15:00 but the window runs to the bell |
| ambiguous bare hour | `sheet: 9:59-4:00` | `4:00` is 16:00 to a trader, 04:00 to a parser |

A bare `H:MM` is accepted only when the hour is ≥ 9
(`UNAMBIGUOUS_HOUR_FLOOR`), which on the ET trading clock cannot be read
two ways. Every fallback is logged at `INFO` with the string that
defeated it, so the list of refs worth making machine-readable is
*observable* rather than guessed at.

**This module is written to be deleted.** Making the refs machine-
readable is a taxonomy change (a `preferred_windows` schema with real
times), and it belongs to the Rules Engine session.

## The fallback is the day's own RTH close
16:00 on a full day, **13:00 on an early close** — read from the session
clock's windows, not from a literal, so a half day needs no special
case. A card is measured against **its own trading day**, so a `WATCH`
card left over from Tuesday is past its window on Wednesday regardless
of Wednesday's shape.

## Why 16:05 and not 16:00
The window *ends* at 16:00 and the comparison is strict (`et > deadline`);
firing exactly at the boundary would race its own definition. Five
minutes is slack, not a threshold. On a half day the 13:00 close has
already passed by the time this run fires, so the same schedule covers
both — no second plist.

## The S2 seam
`trade_def_ref_for` is a callable `(card) -> ref | None`. At S1 no card
carries a `trade_def` (cards are manual; the detector lands in S2/S4),
so it defaults to `None` and every window is the session close. The seam
exists now so S2 attaches the trade_def and **nothing in this module
changes**.
