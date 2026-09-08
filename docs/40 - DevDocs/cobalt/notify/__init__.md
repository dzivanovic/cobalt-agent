# `src/cobalt/notify/` — outbound channels

## What it does
Two channels, and they are deliberately independent:

| | | |
|---|---|---|
| `send_dm(text)` | Mattermost | the primary |
| `send_email(to, subject, body)` | Gmail / OAuth | the out-of-band one |

`send_dm` opens a direct channel with `notify.mattermost.dm_username` and
posts. `send_email` sends as the authenticated Google user on a
`gmail.send`-only scope.

## Why there are two
Charter §3 F18 requires the second **because of** the first: the DM
travels over Mattermost, which is one of the services the heartbeat
watches, so it cannot carry the news that Mattermost is down. `email.md`
states that channel's exact dependency chain — what a send needs, and the
longer list of what it deliberately does not (Postgres, Mattermost, the
Obsidian vault, the mainframe, the sheet).

The `email` probe in `heartbeat/probes.py` watches the watcher: an alert
channel that quietly lost its refresh token would take every red with it
and leave the beat looking exactly as green as before.

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
(`MATTERMOST_CREDS`, rotated 2026-08-23) and nothing else. The email
channel does not even name its keys there — `GOOGLE_OAUTH_CLIENT_ID` /
`_CLIENT_SECRET` / `_REFRESH_TOKEN` are constants in `config.py`, because
a config file that named its own secret keys would invite someone to
paste the values next to them one day. `cobalt validate` reports whether
each resolves without printing what it resolves to.

## Config carries no threshold either (F16)
The email channel's two numbers — the consent flow's loopback port and
the send timeout — are `tunables.yaml` rows
(`notify.email.auth_port`, `notify.email.timeout_s`), each with a named
consumer. Mattermost's own `timeout_s` predates that sweep and is left
where it is: moving a live production field is a change with no proof
attached to it.

## `enabled: false` is loud
A disabled channel returns `SendResult(sent=False, ...)` and logs a
warning, and F18 says "DM channel disabled" in its own block. Never the
silent state.

## A DM, not a channel
Charter §3 F18 says "red/green to daily note + DM", and L14's one-throat
law means alerts reach Dejan directly rather than a room he has to
think to open.
