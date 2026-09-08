# `src/cobalt/notify/cli.py`

## Commands
```
cobalt notify email-auth [--client-json PATH]   one-time, interactive
cobalt notify email-test                        one REAL send, prints the id
cobalt notify email-status                      armed? last send? names only
```

## `email-auth`
Runs once per host. Prints `WAITING: consent` and the authorisation URL,
then blocks on the loopback listener at `notify.email.auth_port`. Nothing
it prints is a secret: the auth URL carries a client id and a scope, and
the vault writes are announced by **name**.

The redirect lands on `http://localhost:<port>/` **on the host running
the command** — so open the URL on that Mac, or forward the port.

## `email-test`
A real send, deliberately: a channel that has only ever been mocked is a
channel nobody has tested. It also writes the `cobalt_email_sends` row
that turns the F18 `email` probe from "unproven" to green.

## `email-status`
Presence and outcomes, never values. Safe to paste into a report.
