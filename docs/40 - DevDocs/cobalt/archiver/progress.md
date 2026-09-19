# `src/cobalt/archiver/progress.py`

New 2026-09-19 with the append-only redesign (chunk P). Spec:
`docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §4, §11.
Table: `src/cobalt/db_migrations/0010_archive_progress.sql`.

## What it does
Reads and writes `system.archive_progress`, the archiver's OWN
watermark per `(ticker, interval)` — the answer to the owner's "I want
to know where the watermark is for each ticker". Every function takes
the target's connection; none opens one (§4).

`archived_through` is a BAR timestamp: the `ts` (bar OPEN, UTC) of the
newest COMPLETE bar of an ACCEPTED export. Never a clock time, never a
bar-close time, never `fetch_started_at`. A test asserts the value sent
is the plan's `archived_through_after` and NOT the `now` passed beside
it.

## Key functions/classes
- `ProgressRow` — the row as `cobalt archiver progress` renders it.
- `read_archived_through(conn, ticker, interval) -> datetime | None` —
  `None` means BOOTSTRAP, and it is not a default standing in for a
  missing row: §4 says a target with no row reconciles its whole
  available export once and the report says so.
- `read_row` / `all_rows` — read-only; `all_rows` orders by watermark so
  the target that has fallen furthest behind is the first line an
  operator reads.
- `upsert_progress(conn, *, plan, run_id, now)` — the write.

## Data flow in/out
**In:** an accepted `reconcile.TargetPlan`, the run id, and `now`.
**Out:** one row in `system.archive_progress`, inside the caller's
transaction.

`run_id` is `<label or command>@<run started_at, UTC ISO>` (§9):
`system.cobalt_jobs` has one row per LABEL and no per-run id, so the run
report and this row share a TEXT rather than growing a new run table.

## Gotchas
- **The writer REFUSES a target that was not accepted.** §4 says
  progress never moves on a failed, withheld, empty or regressed
  target; the cheapest way to keep that true is to make it impossible
  to ask for, so `upsert_progress` raises when the plan it is handed has
  no `archived_through_after`. The rule lives with the write, not in the
  caller's discipline (L1).
- **Monotonic by `GREATEST`, in SQL.** Two runs of the same night, a
  retry after a crash, or a repair racing the nightly run must never
  move the watermark backwards, and the only place that can be
  guaranteed is the statement itself — a read-then-compare in Python is
  a race. A `requires_db` test writes an older watermark second and
  asserts the row did not move.
- **No row is ever deleted here.** A ticker leaving the trader's Lists
  note keeps its row, which is what makes the dropped-and-re-added
  sequence open a `gap` incident rather than silently skipping the
  missing days (round-2 sequence #8). The module contains no `DELETE`
  and a test asserts it — over the code, with docstrings stripped.
- `bootstrap_at` is written on insert and NOT refreshed by the
  `DO UPDATE` arm: it is when this target was first bootstrapped, and
  the report's "history before these bounds is UNASSESSED" line is
  anchored to it.
