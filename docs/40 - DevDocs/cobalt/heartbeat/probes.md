# `src/cobalt/heartbeat/probes.py`

## What it does
One function per question, each returning a `Probe(name, ok, detail,
unknown)`.

`sheet_http` · `database` · `obsidian` · `mainframe` ·
`archiver_freshness` · `vaultwrite_blocks` · `redactions`.

## `unknown` is red, and separately marked
A probe that could not run renders `??` rather than `RED`, so an
operator knows they are looking at ignorance rather than at a diagnosis
— but it still fails the beat.

## `obsidian` reads the same call the writer reads
`cobalt.obsidian.sync_status()`. The heartbeat and the vault writer can
never disagree about the wording of "Obsidian is not running — will not
sync".

## `archiver_freshness`, and the day-one rule
Reads the job row's `finished_at` **and** `last_result.rows_written`.
Red on: stale past `heartbeat.archiver_max_age_min`, a non-zero exit, or
zero rows written.

A row that has **never** completed a run and is younger than one
archiver window is **not** red: the archiver has run every night for
weeks, what it has never done is run while a table existed to notice.
Calling that red would DM a false alarm every 15 minutes until the next
night's run — the same lesson as the MISSED probe's registration cutoff.

## `vaultwrite_blocks` reports two numbers, never summed
`refused` (the guard working) and `ungated_run` (the migration/repair
carve-out being used — RULED 2026-09-04). They share a counter because
both are "a write met the market_reset window tonight", but reading five
repairs as five refusals would send someone hunting a bug that is not
there.

## Thresholds are tunables rows (F16)
`heartbeat.probe_timeout_s`, `heartbeat.archiver_max_age_min`. No
literal in a predicate.
