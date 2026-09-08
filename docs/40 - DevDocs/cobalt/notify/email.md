# `src/cobalt/notify/email.py`

## What it does
`send_email(to, subject, body, cfg=None) -> SendResult`. Charter §3 F18's
**second** alert channel: a Gmail `users.messages.send` on OAuth *user*
credentials, so a red heartbeat can reach Dejan without Mattermost.

## The dependency chain — this is the whole feature
F18's requirement is not "email works", it is **alert path ≠ monitored
path**. A send REQUIRES:

1. `COBALT_MASTER_KEY` on the process;
2. `data/.cobalt_vault` + three entries (`GOOGLE_OAUTH_CLIENT_ID`,
   `_CLIENT_SECRET`, `_REFRESH_TOKEN`);
3. `configs/cobalt/notify.yaml`, `redact.yaml`, `taxonomy/tunables.yaml`;
4. HTTPS to `oauth2.googleapis.com` and `gmail.googleapis.com`.

It does **not** require Postgres, Mattermost, the Obsidian vault, the
mainframe, or the ASET sheet. `test_send_survives_postgres_mattermost_
and_the_vault_all_being_dead` sabotages all three and asserts the send
still goes — that test *is* the F18 claim.

The one honest overlap is the local disk (vault file + config files). A
host with no disk cannot alert by any means; pretending otherwise would
be theatre.

## No token file, anywhere
The library's usual pattern writes `token.json` next to the code and
refreshes in place. That would put a live refresh token in a plaintext
file inside a git repo. Instead the three values live in the vault and
an access token is minted per send and thrown away — one extra HTTPS
round trip, and one fewer file to gitignore, back up, rotate and
remember.

## `static_discovery=True` is not an optimisation
`googleapiclient.discovery.build` fetches a discovery document over the
network unless told not to. Without this flag the alert path grows a
**third** endpoint that nothing monitors. With it, a send makes exactly
two outbound calls.

## `http=` rather than `credentials=`
`build(credentials=...)` builds its own `httplib2.Http` with **no
timeout** — an alert about a dead service could itself hang forever on a
half-open socket. `AuthorizedHttp(credentials, http=Http(timeout=...))`
binds `notify.email.timeout_s` to *both* calls, the refresh and the send.

## F19
Redaction happens here, at the last point before the wire, over the
**subject as well as the body** — the subject is what appears in a phone
notification and in every mail-server log on the way. The credential this
module mints is itself enrolled in the literal guard the moment
`put_secret` stores it (`put_secret` clears the guard's cache on write,
so enrolment is immediate rather than at the next restart): the refresh
token cannot leak through the channel it opens.

`EmailError`'s message is **already redacted** — a Google error body can
quote the request that produced it, bearer token included, and that
message goes straight into a Mattermost DM.

## `SendResult`, not an exception, on a disabled channel
Same rule as `mattermost.py`: the heartbeat has to say *in its own block*
that the second channel did not go. `enabled: false` is a loud, logged
no-op; every other failure raises.

## `_gmail_service()` is the mock boundary
Deliberately one function, deliberately at the network. Everything above
it — message assembly, base64url, the subject prefix, config handling,
error mapping — is real code under test.

## `run_consent_flow()` — `cobalt notify email-auth`
Reads the Desktop client JSON, stores `client_id` + `client_secret`
**before** the browser step (the browser step is the one that can fail,
and a retry should not also need the JSON to still be there), runs the
loopback flow headless on the fixed `notify.email.auth_port`, stores the
refresh token, then overwrites-and-unlinks the JSON.

Two non-obvious requirements, both load-bearing:
- **A fixed port.** Google requires every redirect URI to be
  pre-registered, so the library's `port=0` default produces
  `redirect_uri_mismatch`. The port has to be knowable by a human editing
  the Google console *before* the client exists — hence a tunables row.
- **`access_type=offline` + `prompt=consent`.** Without the second, a
  re-consent on an already-authorised account returns an access token
  *alone* and the flow silently produces a credential that dies in an
  hour. `run_consent_flow` raises rather than storing one.

## `channel_status()` never sends
It reads vault key **names** (no values, no network) and the last row of
`cobalt_email_sends`. A probe that mailed a test every 15 minutes would
put 96 messages a day in the inbox and train its reader to filter the
channel — defeating the thing it was checking.

## Tunables (F16)
| key | value | why it is a row |
|---|---|---|
| `notify.email.auth_port` | 8765 | must match the OAuth client's registered redirect URI, entered by a human |
| `notify.email.timeout_s` | 20 | longer than `heartbeat.probe_timeout_s`: this is the alert itself, not a probe |

## Related
`notify/config.py` (schema + the three vault key names), `notify/store.py`
(`cobalt_email_sends`), `notify/result.py` (`SendResult`),
`heartbeat/probes.py::email`, `heartbeat/runner.py::out_of_band`.
