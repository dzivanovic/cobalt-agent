# `src/cobalt/notify/mattermost.py`

## What it does
`send_dm(message, cfg=None) -> SendResult`. Four API calls: `/users/me`,
`/users/username/<them>`, `/channels/direct`, `/posts`.

## The order that matters
F19 runs **first**, before anything touches the wire, and its hit counts
travel back on `SendResult` so the caller can report them. A DM with six
redactions says so in the heartbeat's own notes.

## Credentials
`_creds()` reads `MATTERMOST_CREDS` out of the Fernet-encrypted vault
for the life of one send. They are never logged, never returned upward,
and a decryption failure reports only the exception **type** — its text
can echo material back.

## Errors are redacted before they are raised
`MattermostError`'s message has already been through `redact()`. A 4xx
body can contain the request that was rejected, token included.

## `SendResult`, not an exception, on a disabled channel
The heartbeat needs to say *in its own output* that the DM did not go.
That is different from crashing.

---

## 2026-09-08 — ADR-0008 (two-layer data model)

New `TIMEOUT_KEY = "notify.mattermost.timeout_s"` and `timeout_s()`,
reading the tunables row through the loader exactly as `email.py` does —
per call, with no built-in default (a timeout Cobalt invented is a hang
nobody chose the length of). All four REST call sites use it.
