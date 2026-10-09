# `src/cobalt/strike/policy.py`

`crossed(policy, direction, entry, bars, since, now) -> Cross | Unwatchable | None`, pure, over i1 bars (bar ts = start, UTC). Only bars starting at or after `since` count.

- `intrabar`: the first bar whose high ≥ entry (long) / low ≤ entry (short), the forming bar included — the F12 replay's trigger rule, through the same `replay.cards._touches_entry` (L3); only the start differs (replay `created_at`, detector the ARMED `at`, MISSED sweep `created_at`).
- `close_through`: the first completed bar (`ts + 1 min ≤ now`) closing beyond entry (strictly). `two_bar`: two consecutive completed closes beyond. `acceptance`: `bars` consecutive completed closes beyond, or `time` (`"<n> min"`) as n consecutive completed i1 closes; both → the longer.
- `Cross` carries `policy`, `bar_ts` (the bar completing the confirmation), `bar_close_at` (ts + 1 min) and `cross_price` (intrabar: the bar's high/low; close-based: the confirming close).
- `policy_of(trigger)`: a `SequenceTrigger` or no policy → `Unwatchable(reason)`; an acceptance with nothing to count or an unparseable time → `Unwatchable` (DECISION D5).

## 2026-10-09 — s4-p1-1009
New module (S4-P1 C1).
