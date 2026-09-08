# `src/cobalt/notify/store.py`

## What it does
`cobalt_email_sends` — one row per email send attempt (`ok`, `caller`,
`message_id`, `detail`). Read by the F18 `email` probe, written by every
sender.

## Why a table and not the heartbeat's job row
F18 asks the probe for "token present + **last send result**". Presence
needs no database. The second half needs memory across processes: the
sends happen in the heartbeat's 15-minute one-shot, in `cobalt notify
email-test`, and in any future alerting caller. `cobalt_jobs.last_result`
is written by the heartbeat and only by the heartbeat — so `email-test`,
the exact command used to *prove* the channel, would leave no trace the
probe could read. A channel whose proof is invisible to its own monitor
is not proven.

## `record_attempt()` never raises
Same rule, and the same reason, as `redact.guard._record`: by the time it
runs the mail has already left (or already failed), and a dead Postgres
must not turn a delivered alert into an exception. **This is also what
keeps Postgres off `send_email`'s dependency chain.** Loud, and
non-blocking, in that order.

## No column can hold a secret
Same discipline as `cobalt_redactions`. `detail` is written from an
already-redacted string (`EmailError`'s contract); `message_id` is
Google's opaque id, which is not a credential and is what an operator
pastes into a support thread.
