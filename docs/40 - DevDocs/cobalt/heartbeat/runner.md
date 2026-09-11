# `src/cobalt/heartbeat/runner.py`

`take_beat` now includes the radar probe in the standard heartbeat result set.

## What it does
`run_beat()` — probe, write the note block, alert, record its own run.
`take_beat()` — probe only. `write_note_block()`, `out_of_band()`.

## One beat, in order
1. every probe + `jobs.watchdog.sweep()`;
2. the daily-note unit through `VaultWriter` — **the full unified diff
   goes into the run report** (L28.4). It writes to the live vault every
   15 minutes, and it was the one write path here whose changes could
   not be read back;
3. on red, `out_of_band()` — a real email since S1-P4 (2026-09-08),
   over `cobalt.notify.email`;
4. a DM on any red, carrying `email channel DOWN: <reason>` when step 3
   failed; one green summary a day at `heartbeat.green_summary_at`.
   The green summary is **DM-only** — a daily all-clear in the alert
   inbox is how an alert inbox stops being read.

## Why the second channel goes FIRST
The DM's body is rendered from `beat.notes`, so the email outcome has to
be in that list before `send_dm` reads it. That ordering is what puts
`email channel DOWN: <reason>` into the red DM. The reverse order would
report a failed second channel only to the log — where it would be found
by whoever went looking, which is nobody.

Only one direction works: the DM can carry a report *about* the email
channel; the email channel cannot carry a report about itself.

## `out_of_band()` never raises
A beat that died sending the **backup** alert would take the primary
alert with it — the exact coupling this channel exists to break. A
failure becomes a note; a disabled channel reports `email channel OFF`,
so "no email arrived" is never ambiguous between *off* and *broken*.

## A missing daily note is not created here
L28.1: only `create_if_absent` with a template may create a note, and
the 05:15 prefill is what does. A missing note is reported loudly and
the beat continues.

## Never raises on a red
A red beat exits 0 and says RED loudly. It raises only when the beat
itself could not run.

## It watches itself
It records its own `com.cobalt.heartbeat` run like any other job — it is
the one job nobody else is watching, so a stalled heartbeat surfaces as
its own MISSED row (measured against two of its own 15-minute
intervals; see `jobs/watchdog.md`).

## Tunables it reads (F16)
`heartbeat.interval_min` — also the plist's `StartInterval` mirror,
compared by `cobalt validate`; `heartbeat.green_summary_at`. The email
path adds `notify.email.timeout_s` (see `notify/email.md`).

## Not a resident process
`com.cobalt.heartbeat` is a launchd **one-shot** on `StartInterval 900`
(`launchctl print` shows `state = not running` between beats). New code
is therefore picked up at the next beat — deploying a change here needs
no restart of anything.
