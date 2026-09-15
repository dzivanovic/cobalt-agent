# `src/cobalt/notify/` — outbound channels

## What it does
One channel:

| | | |
|---|---|---|
| `send_dm(text)` | Mattermost | the only one |

`send_dm` opens a direct channel with `notify.mattermost.dm_username` and
posts.

## The second channel was retired (2026-09-14, executed 2026-09-15)
Charter §3 F18 asked for a second, out-of-band channel **because of** the
first: the DM travels over Mattermost, which is one of the services the
heartbeat watches, so it cannot carry the news that Mattermost is down.
S1-P4 built it as `send_email` over Gmail / Layer-B Google OAuth, with an
`email` heartbeat probe and `cobalt notify email-auth|email-test|email-status`.
Google's Publish step for the `gmail.send` scope is gated on
restricted-scope verification, so the OAuth client never left Testing and
its refresh token expired every seven days. Dejan ruled it retired. The
module, its send store, its CLI, their DevDocs and its tests are removed;
git history keeps them (`git show 0ed37f5:src/cobalt/notify/email.py`); the
`cobalt_email_sends` table stays as history (dropping it is a separate
HITL). The three `GOOGLE_OAUTH_*` vault entries are Dejan's to remove.

## Every line goes through F19, inside the sender
The redaction happens at the **last point before the socket**, not at
each caller. A guard every caller must remember to call is a guard that
eventually nobody calls. Even the sender's own HTTP error text is
redacted before it is raised: a 401 body can echo the token back.

## Why not `cobalt_agent.interfaces.mattermost`
The strangler rule (CLAUDE.md): the old tree stays runnable and
untouched, and no new-core module imports it. That file is ~800 lines of
websocket listener, proposal parsing and brain callbacks; what the
heartbeat needs is "open a DM channel, post a string". This is that,
over plain HTTP — no `mattermostdriver`, no websocket, no shared state
with the running agent.

## Config carries no credential
`configs/cobalt/notify.yaml` names the vault **key**
(`MATTERMOST_CREDS`, rotated 2026-08-23) and nothing else. `cobalt
validate` reports whether it resolves without printing what it resolves
to.

## Config carries no threshold either (F16)
The Mattermost timeout is the `notify.mattermost.timeout_s` row in
`tunables.yaml` (ADR-0008 D7), with a named consumer.

## `enabled: false` is loud
A disabled channel returns `SendResult(sent=False, ...)` and logs a
warning, and F18 says "DM channel disabled" in its own block. Never the
silent state.

## A DM, not a channel
Charter §3 F18 says "red/green to daily note + DM", and L14's one-throat
law means alerts reach Dejan directly rather than a room he has to
think to open.
