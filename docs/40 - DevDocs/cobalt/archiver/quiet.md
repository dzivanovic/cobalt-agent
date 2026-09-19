# `src/cobalt/archiver/quiet.py`

New 2026-09-19 with the append-only redesign (chunk Q). Spec:
`docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §8. The
ruling is `reports/cto-2026-09-19.md` §4 **R8**, 09:30 ET,
"A on archiver".

## What it does
Decides whether the radar is quiet enough for a repair to touch stored
bars. It guards `restate --apply` and `backfill-missing --apply` — and
nothing else: previews and every read-only command are always
available.

## The four rules
| # | rule | read from |
|---|---|---|
| **Q1** radar idle | the session is `OVERNIGHT` — exactly the state in which the radar's cycle returns `idle:overnight` BEFORE any read or write (`radar/runner.py:173-176`) | the session clock |
| **Q2** before the next session | the next boundary INTO a SCANNED session (premarket, RTH, aftermarket) is at least `quiet_before_open_min` away | `SessionClock.next_boundary`, walked |
| **Q3** after the last poll cycle | `now >= last_scan_at + cycle_max_min + quiet_after_cycle_min` | one read of `system.radar_pool` |
| **Q4** one mutator | the run-level advisory lock is held for the whole command | `store.run_lock`, §9 — the CALLER's job |

**`MARKET_RESET` is NOT quiet.** The radar is PAUSED there, not idle,
and 20:30 belongs to the nightly run. Its refusal line says so.

Q1–Q3 are checked at command START **and again inside the repair
transaction immediately before COMMIT** — the shape of the radar's own
`gate` (`radar/runner.py:41-48`). A start-time check alone is exactly
what Astra's open-boundary sequence defeats, and
`test_astra_open_boundary_repair_crosses_open` drives that sequence to
the second.

## Key functions/classes
- `QuietObservation` — what the reader SAW. Pure data.
- `quiet_verdict(observation, settings) -> QuietVerdict` — **pure**.
  Splitting the observation from the verdict is what makes §8 testable
  to the second without a database or a live radar.
- `observe(*, now, pool_reader, clock, pool_key)` — the only I/O, and
  `pool_reader` is INJECTED, so this module never opens a connection.
- `guarded_repair(*, observe, settings, what)` — the context manager a
  repair runs inside: START check, then the caller's work, then
  `guard.check_before_commit()` INSIDE its transaction. The caller owns
  the transaction because §4 gives the connection to the target.
- `require_quiet(...)` — the one-shot start check.
- `QuietRefused` — `exit_code = 2`.

## The refusal (§8, verbatim in shape)
One line per FAILED rule, then:

```
REFUSED — not in a quiet window. session=<s> · last radar scan started
<ts ET> (<n> min ago; need >= <cycle_max + quiet_after> min) · next
scanning session opens <ts ET> (in <n> min; need >= <quiet_before_open>
min) · earliest allowed start: <ts ET>. The preview (no --apply) is
always available.
```

Exit code 2, nothing written.

## Gotchas
- **Q3 is a DERIVATION, not a measurement, and that is the recorded
  dissent.** A scanning cycle stamps its START into
  `system.radar_pool.last_scan_at`; the COMPLETION instant is persisted
  nowhere (§2). So "the cycle has finished" is start + `cycle_max_min`,
  a STATED UPPER BOUND. Gemini and Astra both dissented on exactly that
  (spec §13); spec O-2 carries the alternative — the radar stamping a
  completion instant — which touches the live radar's write path and is
  NOT in this build.
- **Refusing is the default (L1).** A missing pool row, a NULL
  `last_scan_at` or an unreadable table REFUSES with "cannot prove the
  radar is quiet". It is never read as "no scan, therefore idle".
- **There is no `--force`.** An override of this window is the owner's
  word, recorded by the desk, and is a code or config change — never a
  flag (L1, L37). A test asserts the parser rejects it and that the
  string is absent from this module's and the CLI's CODE.
- **`earliest_allowed_start` can be `None`,** and that is an answer: the
  radar's quiet cannot be proven (no pool row), or the next overnight
  window is too short to hold the repair. Inventing a time for either is
  what L1 forbids.
- **The poller is untouched.** This module protects the repair side
  only; the poller takes no lock and checks no marker (R8).
  `git diff main -- src/cobalt/radar/` is EMPTY on this branch, and
  `test_archiver_quiet.py::test_known_limit_1_…` DEMONSTRATES the limit
  by importing the poller and driving it.
- The `_next_scanning_open` / `_next_overnight` walks bound at 16 hops.
  A weekend, a holiday and an early close are correct for free because
  `SessionClock.next_boundary` already knows them.
