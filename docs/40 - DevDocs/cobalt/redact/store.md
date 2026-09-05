# `src/cobalt/redact/store.py`

## What it does
`cobalt_redactions` — one row per (event, pattern), carrying the channel
and the pattern **name**. `count_since`, `count_over_minutes`,
`by_pattern_since`, `recent`.

## The schema has nowhere to put a secret
Deliberate. The table is read by whoever is debugging an alert, and a
schema with no column for the material cannot leak it by accident.

## Why the table is prefixed
`cobalt_brain` is the same Postgres database Mattermost runs in — 129
tables, 103 of them Mattermost's — until 2026-09-04, when Mattermost
moved to its own database (ADR-0006). Generic names collide; see
`cobalt/jobs/migrations/0001_cobalt_jobs.sql` for the one that did.

## What F18 reads
`count_over_minutes(heartbeat.interval_min)` — redactions since the last
beat. Not red on its own: the guard firing is the guard working. It is
on the block because a count that suddenly climbs means something
started putting credentials into outbound text, and that is worth seeing
the day it starts.
