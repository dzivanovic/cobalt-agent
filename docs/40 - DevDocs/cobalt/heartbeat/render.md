# `src/cobalt/heartbeat/render.py`

## What it does
`Beat` — one heartbeat's whole result (`probes`, `jobs`, `notes`), with
`green`, `headline`, and three renderings.

## One renderer, two destinations
The note block and the DM are the same facts. A heartbeat whose two
channels could disagree is a heartbeat you have to check twice.

## Why the DM is not the table
`note_body()` is a markdown table (Obsidian renders it); `dm_body()` is
plain lines, red first then green. A table in a DM is unreadable on a
phone, and the phone is where a red alert is actually read.

## `summary_body()` and AMBER (2026-09-14)
The scheduled summary sent at each `heartbeat.summary_at` slot: every
RED job/probe and stage failure, then every AMBER job, or "all green". It
goes out before the beat's vault stage, so the vault unit is not in it
(its transitions alert on their own). `amber_jobs` are `ok` findings
flagged amber: 🟡 in the note table, an "Amber:" section in the DM, never
part of `green`'s negation.

## The unit id is stable
`section heartbeat` / `unit status`, the same every beat, so
`upsert_unit` updates in place. At 15-minute intervals an append-only
block would put 96 copies in the note by midnight.

## `_cell()`
A markdown table cell cannot contain a raw pipe or a newline. Job detail
text does, so it is escaped rather than trimmed — the reason a job is red
is the whole value of the row.
