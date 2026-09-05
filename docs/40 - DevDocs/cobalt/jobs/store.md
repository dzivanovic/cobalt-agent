# `src/cobalt/jobs/store.py`

## What it does
`cobalt_jobs` (one row per launchd label) and `cobalt_kill_switch` (one
row, `id = TRUE`, so there is exactly one answer to "is Cobalt
stopped").

## The table is `cobalt_jobs`, not `jobs`
`cobalt_brain` **was** the same Postgres database Mattermost ran in —
131 tables, 103 of them Mattermost's, and one of them was `jobs` with
164,320 rows. `CREATE TABLE IF NOT EXISTS jobs` did nothing, silently,
and the first production query failed with `column "label" does not
exist`. Fail-loud turned a week of green heartbeats reporting on
Mattermost's work queue into a ten-second diagnosis.

**That collision is gone as of 2026-09-04**: Mattermost moved to its own
`mattermost` database (ADR-0006, "one database per product"), and
`cobalt_brain` now holds Cobalt's 28 tables and nothing else. The prefix
STAYS. It is not a workaround that expired — it is the reason a
`DROP`/`TRUNCATE` aimed at `jobs` can no longer reach anything Cobalt
cares about, and re-litigating a name costs a migration to save nothing.

Note the number: the S1-P3 write-up here said "116 of them Mattermost's".
That was 129 minus 13 assumed-ours, never an inventory. A pristine
Mattermost 11.4.0 install creates 103 tables; the other 13 were Cobalt's
Gemini-era tables with generic names (`themes`, `instruments`, `trades`,
`key_levels`, …). A drop guarded by "the 116" would have destroyed them,
which is why the split derived its list from a reference install instead
of from this page.

Only the tables introduced at S1-P3 take the prefix. `aset_sizings`,
`vault_writes`, `card_transitions`, `day_modes` and `bars` are specific
enough not to collide and hold live trading record — a rename there is a
migration, not a naming preference.

## Why it is not session-gated
`market_reset` exists to stop Cobalt writing **trading record** between
20:00 and 21:00. A job's own state is not trading record — and the
archiver, the one job that runs squarely inside that window by design,
is exactly the job whose failure the heartbeat most needs to see. A
`jobs` table that went blind for an hour every evening would go blind
for the hour it matters most.

## `register()` does not touch runtime columns
Re-registering after a config edit must never erase the last run's exit
code — the first thing an operator looks at.

## `mark_probe()`
For residents whose heartbeat comes from a probe rather than from
themselves. Paired with the `heartbeat_source` column so a probe's
"the process exists" is never read as a wrapper's "I am working".

## F19 at the point of storage
`last_error` is redacted on its way *into* the column. F18 puts that
text in a DM, so a traceback carrying a DSN must never become a row that
later leaks.
