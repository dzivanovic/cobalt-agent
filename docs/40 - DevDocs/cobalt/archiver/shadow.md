# `src/cobalt/archiver/shadow.py`

New 2026-09-19 with the append-only redesign (chunk N). Spec:
`docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §5, and
spec O-6.

## What it does
Records, per target and per night, what `append` WOULD have done —
without doing it. This is the evidence the owner rules on before the
write mode is switched (L7: a shadow run, agreement numbers, then his
ruling).

## Why PRE-WRITE, and why that is the whole point
The first design proposed an `audit` command run AFTER the nightly
overlay. Three houses refused it in round 3 with the same argument and
they were right: the 20:30 run's `INSERT … DO UPDATE` refreshes every
in-window bar, so an audit taken afterwards reads zeros by construction
and cannot tell the owner whether `append` would have halted any
target.

So the comparison happens INSIDE the nightly run, per target, AFTER the
fetch and BEFORE that target's `upsert_bars`. Every record carries the
literal label `pre-write`, and a test asserts the range read comes
before the write in the store's recorded call sequence.

## Key functions/classes
- `observe(store, *, ticker, interval, bars, fetch_started_at, settings,
  archived_through=None) -> ShadowRecord` — ONE read of the stored rows
  over the eligible export's range; both scopes are then computed in
  memory, so the steady-state scope costs no second query.
- `ScopeResult` — one scope's four-way comparison: candidates, equal,
  differing (field level, both values after normalisation),
  incoming-only split into `new`/`late`, stored-only, `would_withhold`,
  and `volume_only` (true when every difference is volume alone — the
  first question the owner will ask, because a volume restatement is a
  different kind of worry from a price one).
- `ShadowRecord` — one line of the artifact.
- `write_records(records, *, night, retention_nights)` / `apply_retention`
  / `read_night` / `recent_nights`.
- `persisted_vanished_appeared(nights)` — PURE: takes the sets, so the
  arithmetic is testable without a filesystem.
- `aggregate(records, *, errors)` — `job.result["shadow"]`.

## Data flow in/out
**In:** the parsed export, the fetch instant, the settings, and one
read through `store.bars_in_range` on a transaction the shadow opens
itself (the store's one range read — renamed from `_bars_in_range` when
it absorbed P4's `bars_between` on 2026-09-19; the shadow's call and
what it receives are unchanged).
**Out:** a `ShadowRecord` per target; one JSON-lines file per night at
`data/archiver-shadow/<YYYY-MM-DD>.jsonl`; the aggregate on the job row.

`data/` is gitignored (`.gitignore:6`). **No `git add` in this build
names it**, and none ever should.

## Gotchas
- **It can never fail or slow-fail a target.** The read is bounded by
  its own `statement_timeout` (`set_config(..., is_local => true)`, so
  the value reaches the server as a parameter and expires with the
  transaction rather than leaking onto a pooled session). The runner
  wraps the whole observation in one `try/except Exception` and counts
  `shadow_errors`; the target's `upsert_bars` runs whatever the shadow
  did. Tests drive an exception, a timeout and a slow read and assert
  the write and the run summary are IDENTICAL to a night with the shadow
  off. **`observe` deliberately does not catch its own exceptions** —
  swallowing here would hide a systematically broken shadow behind a
  clean-looking night.
- **It is read-only.** No bar, progress row, incident or config is
  written. The fake store records every call and the test asserts the
  only write method reached on a shadow night is the target's own
  upsert.
- **The artifact is a retained BASELINE, not a log.** Refreshed storage
  cannot show revision FREQUENCY — after tonight's overlay, last night's
  difference is gone. `shadow-report` reads across nights for
  PERSISTED / VANISHED / APPEARED, and a difference that VANISHES was
  healed by the very overlay `append` would stop doing. Astra and Grok
  both required this.
- Retention is bounded by the FILENAME's date, not by mtime: a file
  copied or restored keeps its night, and an mtime sweep would keep
  whatever was touched last rather than whatever is recent.
- `write_records` APPENDS. A `run_full` and a manual `--backfill` can
  both happen on one night and the second must not erase the first.
- **`poller_writable` is decided from the INTERVAL, not from the live
  pool.** The radar poller writes i1 and only i1
  (`radar/poller.py:88`), and the archiver's night does not query the
  radar's tables. So the field answers "could the poller write this
  target at all", not "was this ticker a pool member tonight". Named in
  the build report's SPEC vs CODE.
- In `append` mode the comparison IS the gate, so no artifact is
  written and `ArchiverSettings.shadow_enabled` is false there whatever
  the config row says.
