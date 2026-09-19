# `src/cobalt/archiver/runner.py`

## What it does
Orchestrates a full Bar Archiver run: sequential, gentle-rate, one
`(ticker, interval)` at a time, fail-loud per target — a single
ticker's failure is logged and counted, never silently skipped and
never allowed to abort the rest of the run. Also the `archiver` CLI
entry point (`[project.scripts]` in `pyproject.toml`).

## Key functions/classes
- `GENTLE_SLEEP_SECONDS = 1.2` — the rate; matches the Data-Source
  Spike probes' own rate.
- `_run_targets(targets, mode) -> RunSummary` — the shared
  engine: resolves the Finviz token once (not per-request), ensures the
  `bars` schema exists once, then for each target: `fetch_bars` →
  `upsert_bars` → record success, or catch `CollectorError` (or any
  other exception — never lets an unexpected error type escape and
  abort the loop) → record failure and log it loudly. Sleeps between
  targets, not after the last one.
- `run_full() -> RunSummary` — the nightly job:
  the enabled Lists-note archive targets, run, append the report.
- `run_backfill(ticker) -> RunSummary` — the
  on-demand path: the enabled `backfill_default` list's archive
  intervals for the requested ticker, run, append the report.
- `main()` — sets `LOGURU_LEVEL=INFO` before any import that pulls in
  loguru (same rationale as `aset/__main__.py` — cheap standing
  insurance against the old tree's since-fixed DEBUG secret dump),
  parses `--backfill TICKER`, runs the appropriate
  coroutine, and exits non-zero if the run had any failures (so a
  launchd/cron wrapper can detect a bad night from the exit code alone,
  even before a human reads the report).

## Data flow in/out
**In:** the configured Radar Lists note (via `load_config()`), the
Finviz vault token (via `collector.resolve_token()`).
**Out:** rows written to `bars` in the database `COBALT_ENV` names, one appended line in
`docs/30 - Design/archiver-runs.md`, loguru output to stdout/whatever
redirects it (the launchd plist, in production).

## Config it reads
`configs/cobalt/radar.yaml` for the Lists-note path, indirectly via
`archiver.config`. The database is **not** configurable here and is not
a parameter anywhere in this module.

## Gotchas
- **The database is not an argument (RULING 9, 2026-09-04).** This
  module used to thread `db_name="cobalt_dev"` through every entry point
  and expose it as a `--db-name` CLI flag. Those are deleted, not
  re-pointed: a per-run override of the target database is the same hole
  RULING 7 closed for `AsetConfig.db_name`, and `test_env.py`'s
  `test_archiver_runner_exposes_no_database_override` fails if either
  the parameters or the flag come back.
- `com.cobalt.archiver` is a **`StartCalendarInterval` batch job**
  (Mon–Fri 20:30 local) with `RunAtLoad=false`, not a resident
  collector. Booting it out mid-session interrupts nothing unless a run
  is actually in flight — the day's bars are fetched from Finviz history
  in one pass at 20:30, so the job only has to be loaded *by* 20:30, not
  continuously.

---

## 2026-09-17 — S2-P4: the L53 total-demand gate before the first request

`_run_targets` now calls `_check_demand(targets, mode)` before the token
is resolved or anything is fetched:
- the nightly `full` run is the registry's `archiver` consumer:
  `check_scheduled_demand("archiver")`.
- a manual `backfill:<T>` is unscheduled, so it is added as an unbounded
  consumer with `min(len(targets), 50)` rpm.

A refusal raises `TotalDemandExceeded`, so the job row goes `failed` with
the total-demand line. Pacing, targets and the report are unchanged.
**Deployment gate — CLOSED 2026-09-19 by ruling.** This entry carried an
open gate from 09-17: the archiver's own pacing bound exceeded the
ceiling then in force, and the gate refused until the ceiling or the
pacing was ruled (plan §8 item 4). The ceiling was raised to 50 on
09-17 (R17), which settled the nightly run; what remained, and what the
post-P4 rebase made fire, was the BACKFILL's unbounded consumer. Dejan
ruled it on 2026-09-19 (`cto-2026-09-19.md` §4 R34, "B"): the ceiling
stays at 50 and the backfill is bounded out of the premarket window.
See the 2026-09-19 entry below. Nothing is owed here any more.

---

## 2026-09-19 — `write_mode` dispatch (FINAL design §5, §6, §7, §9)

`_run_targets` now DISPATCHES on `archiver.write_mode` **before any
append-specific step** (Astra's rule): no new failure rule, no
completeness cut, no range read may leak into an `upsert` night. The
repo ships `upsert`.

`mode` is and stays the REPORT SCOPE (`"full"` / `"backfill:<T>"`). The
write mode is a different name everywhere, and a test asserts it.

### `upsert` mode — today's night, with exactly three additions
`_upsert_targets` is the old loop verbatim: the whole export to
`upsert_bars`, no completeness filter, no range cut, no comparison
gate, no withholding, no `archive_progress` write, no incident write,
the same submitted-row count and the same run-report row.

The COMPLETE list of what it now does that it did not:

1. the run-level advisory lock of §9 (both modes);
2. the PRE-WRITE shadow compare (reads only, `cobalt.archiver.shadow`);
3. one `shadow` key in `job.result` and one artifact file per night.

`test_archiver_runner.py::test_the_complete_list_of_upsert_mode_additions_is_pinned`
asserts the fake store's recorded call sequence EXACTLY, with the shadow
off and on, plus the key set of `job_result()`. **A fourth addition
fails that test.**

Operator-visible consequence, named in spec O-3: the advisory lock means
a manual `--backfill` DURING the nightly run now REFUSES instead of
interleaving. It is the only behaviour change before the switch.

### `append` mode — one transaction per target
`_append_targets` → `_append_one`, inside `store.target_transaction()`:
read progress → `plan_candidates` → the ONE range read (only when the
plan needs it — a refusal costs no query) → `reconcile` → insert →
incidents → progress → validated counters. A crash between any two
commits none of them.

A withheld target raises `_Withheld` INSIDE the `with`, so the
transaction rolls back; its incident is then persisted in a SECOND
small transaction by `_persist_incidents` (Astra, V3-2 — evidence
written inside the doomed transaction dies with it). A test asserts the
second transaction is opened AFTER the first was rolled back.

`Rows Written` is `inserted` in append mode, and `inserted` is the
SERVER's count: `len(to_insert) - inserted` is `concurrent_conflicts`,
and a negative difference raises rather than reporting counts that
cannot reconcile (L57).

### Health
`RunSummary.healthy` is false on any FAILED or DEGRADED target (V2-9),
and `_archive_nightly` now raises on a DEGRADED-only night too — a gap
whose usable range was appended is not a failure of the run, but the
night is not healthy and the job row must not report green.
`degraded_targets` is 0 by construction on an `upsert` night: that mode
has no such verdict and must not invent one.

### Test seams
`_run_targets(..., store=, fetch=, settings=, now=)` — the same kind of
seam as `BarStore(db_name=…)`. Production passes none of them. `now` is
what makes the whole runner testable without sleeping through a night;
`_now()` is the single `cobalt.session.clock.now_utc` read.

### The L53 gate and the dispatch, side by side (2026-09-19 rebase)
Both sections above are live. `_check_demand(targets, mode)` is still the
FIRST statement of `_run_targets` — before the settings load, the store,
the §9 lock and the token — so S2-P4's total-demand gate still runs
before anything can send a request, in both write modes. The write-mode
dispatch happens after it. Neither change replaced the other; the rebase
kept both.

---

## 2026-09-19 — R34 "B": the backfill is bounded out of the premarket window

**What was ruled.** `cto-2026-09-19.md` §4 R34, 15:4x ET, Dejan: the
ceiling `radar.finviz_max_rpm` **stays at 50** and the archiver's manual
BACKFILL is bounded out of the **04:00–09:30 ET** premarket window. The
nightly 20:30 `full` run is untouched. The long-term fix — staggering
the screens' and lists' cadences, which reclaims far more than the 1 rpm
at issue — was queued as C, separately, and is not in this change.

**What was wrong.** The 09-17 entry above declared the backfill consumer
with `window=None`. `radar/notes.py` defines that as UNBOUNDED: a
consumer that "has not been proved disjoint from" the others, counted
against every window. So a backfill that nothing schedules at 04:00 was
nevertheless added to the radar's 04:00 peak, and with P4's `replay`
consumer in the registry the L53 total reached **51.00 rpm at 04:00 ET**
against a ceiling of 50. The gate refused every backfill, at every hour,
for a collision that only existed on paper.

**What changed, both halves together.**

- `_backfill_window(targets, instant)` builds the window the run will
  ACTUALLY hold the transport for: `[instant, instant + len(targets) ×
  GENTLE_SLEEP_SECONDS)` in ET, through the same `DemandWindow.from_at`
  the nightly `archiver` consumer's window is built with. That window,
  not `None`, is what the backfill now declares to the shared gate.
- `_check_demand(targets, mode, now=None)` REFUSES with
  `BackfillWindowRefused` — loudly, before the settings load, the store,
  the §9 lock and the token, so no request is sent — when that window
  touches the premarket window, including a run that starts at 03:50 and
  paces its way into it, and including one that crosses midnight into
  the next morning's.
- The premarket bound is READ, never hardcoded (L10): `PREMARKET_OPEN_KEY
  = session.premarket_open` and `PREMARKET_CLOSE_KEY = session.rth_open`.
  Move the session in `tunables.yaml` and the bound moves with it; the
  refusal message quotes whatever it read.

The two halves are one change on purpose. A declared window the runner
did not enforce would be a lie to the demand model, and an enforced
window the model never saw would leave the 04:00 peak exactly as
overstated as `window=None` left it.

**The ceiling did not move.** `radar.finviz_max_rpm` is still `50` in
`configs/cobalt/taxonomy/tunables.yaml`, grep-proved across `src` and
`configs` before and after this change. `GENTLE_SLEEP_SECONDS`, the
radar's, archiver's and replay's consumers, every cadence and every
window but the backfill's are byte-for-byte unchanged, and
`radar/notes.py` needed no change at all — the demand model already
expressed this.

**What this does NOT fix, measured rather than assumed.** Being outside
04:00–09:30 is necessary but not sufficient for a backfill to pass the
L53 gate, because the three scheduled consumers already hold the whole
ceiling between them: radar 50 rpm over 04:00–20:00, archiver 50 rpm
over 20:30–21:10, replay 50 rpm over 21:10–21:35, each exactly at the
50 ceiling and each disjoint from the others. A backfill of even 1 rpm
inside any of those windows still totals 51 and is still refused, now
naming the hour it collided at instead of always naming 04:00. The
hours a backfill can actually run today are **20:00–20:30 and
21:35–04:00**. That is the arithmetic R34's C — the cadence stagger —
exists to change; it is not something this change may decide, because
the ceiling and the cadence are Dejan's (L53).

**Operator-visible consequence.** `archiver --backfill TICKER` now fails
fast in the premarket window with a message naming the window, the run's
own window and the ruling, instead of reaching the demand gate and
failing there with a total that blamed 04:00 whatever the clock said.
