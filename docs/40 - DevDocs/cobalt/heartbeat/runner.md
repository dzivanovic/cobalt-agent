# `src/cobalt/heartbeat/runner.py`

`take_beat` now includes the radar probe in the standard heartbeat result set.

## What it does
`run_beat()` — probe, write the note block, alert, record its own run.
`take_beat()` — probe only. `write_note_block()`.

## One beat, in order
1. every probe + `jobs.watchdog.sweep()`;
2. the daily-note unit through `VaultWriter` — **the full unified diff
   goes into the run report** (L28.4). It writes to the live vault every
   15 minutes, and it was the one write path here whose changes could
   not be read back;
3. on a **transition** — something entered RED or recovered since the
   prior beat — a DM. An unchanged RED is silent (ruled 2026-09-14,
   option B);
4. a standing-state summary DM at every `heartbeat.summary_at` slot
   (07:00, 16:30 ET), sent **whether or not anything is red** — a missing
   summary is the dead-heartbeat signal.

## The transition decision
`PriorBeat.from_row()` reads the previous beat's `red_jobs`, `red_probes`
and early-stage failures from the job row **before** PERSIST overwrites
it; `alert_keys()` names this beat's reds; `transitions()` returns
(entered, recovered). No migration: `last_result` already carried the
red sets. An unreadable prior fails toward alerting — every standing red
counts as entered once. The vault unit is decided after ALERTS, so its
transition is compared in FINALIZE against the prior `vault_outcome`,
and a change sends a corrective DM. The beat row, the note and the table
keep the full standing state; only the decision to send changed.
`summary_due()` picks the latest passed slot not yet sent today, deduped
in `last_result.summary_sent`.

## The second channel was retired (2026-09-14, executed 2026-09-15)
Charter §3 F18 asked for an out-of-band alert path because the DM travels
over Mattermost, one of the watched services — a Mattermost outage takes
the alert about it along. S1-P4 built that path as email over Layer-B
Google OAuth (`out_of_band()`, sent before the DM so its outcome could
ride in the DM body). Google's Publish step for the `gmail.send` scope is
gated on restricted-scope verification, so the OAuth client never left
Testing and its refresh token expired every seven days. Dejan ruled the
channel retired. Transition, corrective and summary alerts are DM-only;
the DM body no longer carries a channel-outcome line. The hole F18 named
is open again, and this page says so rather than hiding it. The code is
removed; git history keeps it (`git show 0ed37f5:src/cobalt/notify/email.py`); the
`cobalt_email_sends` table stays as history.

## A failed send never suppresses the next
`_attempt_alert()` turns an exception in one send into a stage failure,
so a broken transition DM cannot stop the summary.

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
compared by `cobalt validate`; `heartbeat.summary_at`.

## Not a resident process
`com.cobalt.heartbeat` is a launchd **one-shot** on `StartInterval 900`
(`launchctl print` shows `state = not running` between beats). New code
is therefore picked up at the next beat — deploying a change here needs
no restart of anything.
