# `src/cobalt/notify/` — outbound channels

## What it does
Today: a Mattermost DM. `send_dm(message)` opens a direct channel with
`notify.mattermost.dm_username` and posts.

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
validate` checks the key resolves without printing what it resolves to.

## `enabled: false` is loud
A disabled channel returns `SendResult(sent=False, ...)` and logs a
warning, and F18 says "DM channel disabled" in its own block. Never the
silent state.

## A DM, not a channel
Charter §3 F18 says "red/green to daily note + DM", and L14's one-throat
law means alerts reach Dejan directly rather than a room he has to
think to open.
