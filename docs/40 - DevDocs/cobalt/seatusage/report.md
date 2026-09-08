# `src/cobalt/seatusage/report.py`

## What it does
Renders one day of seat usage as an L28 marked unit, plus the human
cells that sit beside it, plus the file template.

## The shape on disk
```
<!-- cobalt:section seat-usage:2026-09-08 -->
### 2026-09-08                         <- seeded once, human-owned
                                          |
weekly_pct_open:                          | clause 2a template cells
weekly_pct_close:                         |
                                          |
<!-- cobalt:unit seat-usage:2026-09-08 -->
| model | role hint | ... |             <- rewritten every hour
<!-- /cobalt:unit seat-usage:2026-09-08 -->
<!-- /cobalt:section seat-usage:2026-09-08 -->
```

## One section per day — a mechanical decision
`upsert_unit` appends a new unit at the **end** of its section, and the
newest day has to be at the **top**. A per-day section can be *placed*
(the writer takes a `placement` locator for a missing section), so
newest-on-top comes from the write path itself rather than from
re-sorting the whole file every hour. `days_anchor()` is that locator:
new sections land immediately below the `<!-- cobalt:days -->` comment,
and nothing above or below is touched.

## The human cells are seeded once and then left alone
Not "written with a merge that lets the human win" — **actually left
alone**, checked before the write.

The merge's baseline lives in Postgres. When it is missing the writer
falls back to treating the on-disk body as the baseline, which makes
Cobalt's blank template win — and that would wipe a filled cell on any
run that could not reach the database. So `human_cells_present()` reads
the **file**, which is always available, and the runner does not call
`upsert_region` at all once the cells are there.

## The columns
`model · role hint · cache read · cache write · output · API-equivalent
$ · Δ since last run`.

* **role hint** — observed seat, then configured role, in that order and
  separated, so a reader can tell which half is evidence.
* **API-equivalent $** — labelled as such in the file's own preamble. The
  seats run on consumer plans (L29); this is what the same tokens would
  have cost at published API rates. A size, not an amount owed.
* **Δ** — change in that column since the previous run, from the job
  row's own snapshot. An em dash means *no comparable figure* (first run
  of the day, a new model, either side unpriced). Never a zero: a zero
  claims the number held steady, which is a different statement from not
  knowing.
* **Input tokens** are not a column — they are a rounding error beside
  cache reads — but they are printed under the table rather than lost.

## `snapshot()` / `previous_snapshot()`
The Δ state lives in `cobalt_jobs.last_result`, not in a table of its
own: this job is the only writer and the only reader of it, and a table
to remember one dictionary an hour is a table to migrate later for
nothing. `previous_snapshot()` refuses a snapshot from a different day —
a Δ against yesterday's totals looks like a change and is a calendar
boundary.
