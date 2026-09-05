# `src/cobalt/jobs/watchdog.py`

## What it does
`sweep()` — probe every job, conclude, persist, and return `Finding`s
for F18 to render.

## Is the plist even loaded? (asked first, of every job)
Charter §3 F18: *"every ops plist loaded + last exit code."*
`LaunchdStatus` separates three answers that a bare "no pid" collapses:

| answer | means |
|---|---|
| `loaded=False` | launchd has never heard of this label — it will never fire again |
| `loaded=True, pid=None` | registered, idle. Healthy for a one-shot; a **failure** for a resident |
| `last_exit` | launchd's own record of the last run (78 = EX_CONFIG, the 09-03 signature) |

**This check was missing in the first version**, and running the
Charter's own acceptance test for real is what found it: only residents
were probed, so `launchctl bootout com.cobalt.cards-expire` left the
heartbeat green. Between runs an unloaded one-shot looks identical to a
loaded one — no PID to lose, no state to change. MISSED would not have
said so until its next scheduled time plus grace, which for a
Friday-evening unload is Monday.

An unloaded **one-shot** is reported, not written: its row is the record
of its last run, and *"the plist is gone"* is a fact about launchd.
Writing it into `state`/`exit_code` destroyed that record and left a
stale `failed` after the plist came back.

## ZOMBIE
`running` past `timeout_s` **and** `heartbeat_at` stale by more than
`timeout_s / jobs.heartbeat_fraction`. Both halves required.

## MISSED — two shapes, different arithmetic
- **Calendar** (`Mon–Fri 05:15`): the last such moment passed more than
  `jobs.missed_grace_min` ago and no run finished after it.
- **Interval** (`every 15 min`): `now - interval` is *always* exactly
  one interval ago, so a fixed grace wider than the interval makes the
  job **unmissable** — the first draft reported the heartbeat green
  forever, including while stopped. Measured against two of its own
  intervals instead.

**Cobalt cannot miss a run it was not watching for.** A due moment
before `registered_at` is not MISSED: the table did not exist this
morning, and an alert that is wrong on day one is one people learn to
scroll past.

## Fail-loud
`launchctl_status` **raises** rather than reporting "not loaded" when
the probe itself cannot run, and the sweep turns that into a red
`UNKNOWN`. "The probe is broken" and "the job is gone" are different
facts; collapsing them is how a red condition becomes invisible.
