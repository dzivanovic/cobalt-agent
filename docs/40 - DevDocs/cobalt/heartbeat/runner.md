# `src/cobalt/heartbeat/runner.py`

## What it does
`run_beat()` — probe, write the note block, alert, record its own run.
`take_beat()` — probe only. `write_note_block()`, `out_of_band()`.

## One beat, in order
1. every probe + `jobs.watchdog.sweep()`;
2. the daily-note unit through `VaultWriter` — **the full unified diff
   goes into the run report** (L28.4). It writes to the live vault every
   15 minutes, and it was the one write path here whose changes could
   not be read back;
3. a DM on any red; one green summary a day at
   `heartbeat.green_summary_at`;
4. `out_of_band()` on red — which reports that the second channel does
   not exist (see the package page).

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
compared by `cobalt validate`; `heartbeat.green_summary_at`.
