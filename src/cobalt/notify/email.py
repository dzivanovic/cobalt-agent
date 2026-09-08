"""The email channel — Charter §3 F18's SECOND alert path.

    from cobalt.notify import send_email
    send_email("a@b.com", "subject", "body")

WHY THIS EXISTS AT ALL, in one sentence: the Mattermost DM travels over a
service the heartbeat is watching, so it cannot be trusted to carry the
news that that service is down.

---------------------------------------------------------------------
THE DEPENDENCY CHAIN, exactly. This is the contract, not a description.
---------------------------------------------------------------------

A send REQUIRES, and requires nothing else:

  1. `COBALT_MASTER_KEY` on this process;
  2. `data/.cobalt_vault` readable, and three entries in it
     (`GOOGLE_OAUTH_CLIENT_ID` / `_CLIENT_SECRET` / `_REFRESH_TOKEN`);
  3. `configs/cobalt/notify.yaml` and `configs/cobalt/redact.yaml`
     readable from disk;
  4. `configs/cobalt/taxonomy/tunables.yaml` readable (the timeout);
  5. HTTPS to `oauth2.googleapis.com` (refresh) and
     `gmail.googleapis.com` (send).

A send DOES NOT require — and this is the property F18 is buying:

  * POSTGRES. Nothing on this path opens a connection. F19's redaction
    COUNTER writes a row, but `redact._record` swallows its own failure
    by contract and the redaction itself is pure string work that has
    already happened by then. A dead database costs the heartbeat a
    counter row and costs this channel nothing.
  * MATTERMOST. No import, no socket, no shared credential.
  * THE OBSIDIAN VAULT. Nothing here reads or writes a note. `cobalt.
    vault.resolve_vault_path()` is never called, so an unmounted or
    misconfigured vault cannot stop an alert.
  * THE MAINFRAME, the ASET sheet, or any other monitored service.

The two things it shares with the monitored world are the vault FILE and
the config files — i.e. the local disk. A host whose disk is gone cannot
alert by any means, and pretending otherwise would be theatre.

There is one honest asymmetry, recorded rather than hidden: Google's
`googleapiclient.discovery.build` will fetch a discovery document over
the network unless told not to. It is told not to (`static_discovery=
True`), so a send makes exactly two outbound calls — refresh, then send —
and cannot be taken down by a third endpoint nobody was watching.

---------------------------------------------------------------------
F19
---------------------------------------------------------------------
Same rule as `mattermost.py`, for the same reason: redaction happens
HERE, at the last point before the wire, over the subject AND the body.
A guard each caller must remember to call is a guard nobody calls.

The credential itself is enrolled in the literal half of that guard the
moment `put_secret` stores it — every vault value is — so the refresh
token this module mints cannot leak through the channel it opens.
"""

from __future__ import annotations

import base64
import contextlib
from email.message import EmailMessage
from typing import Any, Optional

from loguru import logger

from cobalt.redact import redact

from .config import (
    CLIENT_ID_KEY,
    CLIENT_SECRET_KEY,
    REFRESH_TOKEN_KEY,
    EmailConfig,
    load_notify_config,
)
from .result import SendResult

CHANNEL = "email"

#: `gmail.send` and nothing more. The narrowest scope Google publishes
#: for this: it can send as the user and cannot read a single message.
#: An alert channel that could read the inbox would be a far larger
#: blast radius than the thing it is protecting.
SCOPE = "https://www.googleapis.com/auth/gmail.send"

TOKEN_URI = "https://oauth2.googleapis.com/token"

AUTH_PORT_KEY = "notify.email.auth_port"
TIMEOUT_KEY = "notify.email.timeout_s"


class EmailError(RuntimeError):
    """An email could not be sent. Message is ALREADY redacted."""


def _tunable(key: str):
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(key)
    if row is None:
        raise EmailError(
            f"tunable {key!r} is missing from tunables.yaml — the email channel reads "
            "its numbers from config and has no built-in defaults (F16)."
        )
    return row.value


def auth_port() -> int:
    return int(_tunable(AUTH_PORT_KEY))


def timeout_s() -> float:
    return float(_tunable(TIMEOUT_KEY))


# ---------------------------------------------------------------------
# credentials
# ---------------------------------------------------------------------


def _credentials():
    """Build OAuth user credentials from the three vault entries.

    No token file on disk, anywhere. `google-auth-oauthlib`'s usual
    pattern writes `token.json` next to the code and refreshes it in
    place; that would put a live refresh token in a plaintext file inside
    a git repo, which is precisely the thing the vault exists to prevent.
    The access token this mints lives in memory for one send and is
    thrown away — re-minting it costs one HTTPS round trip and removes a
    file that would otherwise have to be gitignored, backed up, rotated
    and remembered.
    """
    from cobalt.redact.secrets import VaultAccessError, read_secret

    try:
        client_id = read_secret(CLIENT_ID_KEY)
        client_secret = read_secret(CLIENT_SECRET_KEY)
        refresh_token = read_secret(REFRESH_TOKEN_KEY)
    except VaultAccessError as e:
        raise EmailError(f"vault unreadable: {e}") from None

    missing = [
        name
        for name, value in (
            (CLIENT_ID_KEY, client_id),
            (CLIENT_SECRET_KEY, client_secret),
            (REFRESH_TOKEN_KEY, refresh_token),
        )
        if not value
    ]
    if missing:
        raise EmailError(
            f"vault has no {', '.join(missing)} — consent has never been granted on "
            "this host. Run `cobalt notify email-auth` (one time, interactive)."
        )

    from google.oauth2.credentials import Credentials

    return Credentials(
        None,  # no access token: minted from the refresh token on use
        refresh_token=refresh_token,
        client_id=client_id,
        client_secret=client_secret,
        token_uri=TOKEN_URI,
        scopes=[SCOPE],
    )


def _gmail_service(credentials) -> Any:
    """THE MOCK BOUNDARY. Everything below this line is Google's.

    Tests replace this one function, which means the message assembly,
    the redaction, the config handling and the error mapping above and
    around it are all exercised for real — the seam is at the network,
    not halfway up our own logic.
    """
    import httplib2
    from google_auth_httplib2 import AuthorizedHttp
    from googleapiclient.discovery import build

    # `http=` RATHER THAN `credentials=`, and only for the timeout.
    # `build(credentials=...)` constructs its own httplib2.Http with
    # NO timeout, which on this path means an alert about a dead service
    # can itself hang forever on a half-open socket. AuthorizedHttp wraps
    # the same credentials and refreshes through the same Http, so
    # `notify.email.timeout_s` binds BOTH outbound calls — the token
    # refresh and the send — not just the second one.
    return build(
        "gmail",
        "v1",
        http=AuthorizedHttp(credentials, http=httplib2.Http(timeout=timeout_s())),
        cache_discovery=False,
        # See the module docstring: without this, `build` fetches a
        # discovery document over the network and the alert path grows a
        # third endpoint that nothing monitors.
        static_discovery=True,
    )


# ---------------------------------------------------------------------
# send
# ---------------------------------------------------------------------


def _rfc2822(to: str, subject: str, body: str) -> dict:
    """An RFC 2822 message, base64url-encoded as `users.messages.send`
    wants it. `From` is omitted deliberately: Gmail fills in the
    authenticated user, and hardcoding an address here would silently
    break the day the account changes."""
    message = EmailMessage()
    message["To"] = to
    message["Subject"] = subject
    message.set_content(body)
    return {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}


def send_email(
    to: str,
    subject: str,
    body: str,
    *,
    cfg: Optional[EmailConfig] = None,
) -> SendResult:
    """Redact, then send. Same fail-loud contract as `send_dm`.

    Returns a `SendResult` on a DISABLED channel rather than raising —
    the heartbeat has to be able to say in its own output that the
    second channel did not go, which is not the same as crashing. Every
    other failure raises `EmailError` with an already-redacted message,
    because a caller that cannot tell a refused send from a sent one is
    a caller that reports green on silence.
    """
    cfg = cfg or load_notify_config().email

    # F19, over BOTH fields, before anything else touches the wire. The
    # subject matters as much as the body: it is the part that shows up
    # in a phone notification and in every mail-server log on the way.
    safe_subject = redact(subject, channel=CHANNEL)
    safe_body = redact(body, channel=CHANNEL)
    hits: dict[str, int] = dict(safe_subject.hits)
    for name, n in safe_body.hits.items():
        hits[name] = hits.get(name, 0) + n
    if hits:
        logger.warning(
            "F19: {} secret(s) redacted from an outbound email ({})",
            sum(hits.values()),
            ", ".join(f"{k} x{v}" for k, v in sorted(hits.items())),
        )

    if not cfg.enabled:
        logger.warning(
            "Email channel is DISABLED in configs/cobalt/notify.yaml — message NOT "
            "sent. This is a deliberate setting, not an outage."
        )
        return SendResult(
            False, "channel disabled in configs/cobalt/notify.yaml", hits, noun="Email"
        )

    full_subject = f"{cfg.subject_prefix} {safe_subject.text}".strip()
    credentials = _credentials()

    try:
        service = _gmail_service(credentials)
        sent = (
            service.users()
            .messages()
            .send(userId="me", body=_rfc2822(to, full_subject, safe_body.text))
            .execute(num_retries=0)
        )
    except EmailError:
        raise
    except Exception as e:  # noqa: BLE001 - every Google failure is one outcome here
        # A Google error body can quote the request that produced it,
        # bearer token included. It goes through the guard before it goes
        # anywhere a human or a log file can see it.
        detail, _ = redact(f"{type(e).__name__}: {e}", channel=CHANNEL)
        raise EmailError(detail) from None

    message_id = sent.get("id", "?")
    # THE RECIPIENT IS DELIBERATELY NOT IN `detail`. Dejan's alert address
    # is ALSO his `rt.smbtraining.com::username`, so it is a vault value
    # and therefore enrolled in F19's literal guard — putting it in a
    # report string meant every red beat redacted it out of its own DM and
    # its own email (measured: 2 hits per email, 3 per DM, 2026-09-08
    # 11:50 beat). Delivery was never at risk — `to` goes into the `To:`
    # header, which does not pass through the guard — but the noise
    # mattered: `heartbeat.probes.redactions` exists to notice a redaction
    # count that CLIMBS, and a permanent +5 per red beat poisons the one
    # instrument F19 gives F18. Where the alerts go is in notify.yaml and
    # printed by `cobalt validate`; repeating it in every report bought
    # nothing.
    return SendResult(True, f"message {message_id}", hits, noun="Email", ref=message_id)


# ---------------------------------------------------------------------
# consent — `cobalt notify email-auth`
# ---------------------------------------------------------------------


def _shred(path) -> None:
    """Overwrite, then unlink. The client JSON has served its purpose the
    moment its two fields are in the vault, and a copy left in
    `~/.cobalt/` is a second, unencrypted home for a credential that is
    supposed to have exactly one."""
    import os

    try:
        length = path.stat().st_size
        with open(path, "r+b") as fh:
            fh.write(os.urandom(length))
            fh.flush()
            os.fsync(fh.fileno())
    except OSError as e:
        logger.warning("client JSON could not be overwritten ({}) — unlinking anyway.", type(e).__name__)
    path.unlink(missing_ok=True)


@contextlib.contextmanager
def _fast_local_bind():
    """Stop `wsgiref` spending 35 seconds on a reverse DNS lookup.

    MEASURED ON THIS HOST, 2026-09-08: `socket.getfqdn("localhost")` takes
    **35 seconds**. `http.server.HTTPServer.server_bind` calls it to fill
    in `server_name`, and `run_local_server` binds BEFORE it prints the
    authorisation URL — so the command sat silent for 35 s looking
    hung, with the one thing the operator needed still unprinted.

    `server_name` becomes the WSGI environ's `SERVER_NAME` and nothing
    else. This flow serves exactly one request, to a loopback redirect,
    from a URL that already carries the host and port literally — nothing
    in it reads `SERVER_NAME`. So the lookup buys nothing and costs the
    whole delay.

    Patched for the bind and restored immediately, rather than left
    monkeypatched: `getfqdn` is a shared builtin and a global override
    that outlived this function would be a surprise for every later
    caller in the process. Forward DNS is untouched (0.01 s here), so the
    SEND path never went near this.
    """
    import socket

    original = socket.getfqdn
    socket.getfqdn = lambda name="": name or "localhost"
    try:
        yield
    finally:
        socket.getfqdn = original


def run_consent_flow(client_json_path, *, port: Optional[int] = None) -> str:
    """Store the client halves, run the loopback flow, store the refresh
    token, shred the client JSON. Returns the printable auth URL prompt.

    ORDER IS DELIBERATE: client_id and client_secret go into the vault
    BEFORE the browser step, not after. The browser step is the one that
    can fail — a closed tab, a wrong account, a consent screen that
    times out — and re-running the command after a failure should not
    also require the client JSON to still be there.
    """
    import json
    import sys
    from pathlib import Path

    from cobalt.redact.secrets import put_secret

    # LINE-BUFFER STDOUT BEFORE ANYTHING PRINTS. This function blocks on
    # a socket for as long as it takes a human to click through a consent
    # screen, and the ONE thing it must emit first is the URL that human
    # has to open. Python block-buffers stdout whenever it is not a tty —
    # a pipe, a log file, a background job — so without this the URL sits
    # in a 8 KB buffer until the process exits, i.e. until after the
    # thing it was needed for. Found the first time this was run
    # non-interactively (2026-09-08): the listener was up, the prompt was
    # invisible, and the command looked hung.
    try:
        sys.stdout.reconfigure(line_buffering=True)
    except (AttributeError, ValueError):  # not a TextIOWrapper — nothing to do
        pass

    path = Path(client_json_path).expanduser()
    if not path.exists():
        raise EmailError(
            f"{path} does not exist. Download the Desktop OAuth client JSON from the "
            "Google Cloud console and save it there (it is read once and shredded)."
        )

    try:
        raw = json.loads(path.read_text())
    except ValueError:
        raise EmailError(f"{path} is not valid JSON.") from None

    # Google writes the client under "installed" for a Desktop client and
    # "web" for a web one. Only "installed" can run a loopback flow.
    block = raw.get("installed")
    if block is None:
        kind = ", ".join(sorted(raw)) or "nothing"
        raise EmailError(
            f"{path} has no 'installed' block (found: {kind}). The loopback consent "
            "flow needs a DESKTOP OAuth client; a Web client cannot bind localhost."
        )
    client_id, client_secret = block.get("client_id"), block.get("client_secret")
    if not client_id or not client_secret:
        raise EmailError(f"{path}'s 'installed' block is missing client_id or client_secret.")

    put_secret(CLIENT_ID_KEY, client_id)
    put_secret(CLIENT_SECRET_KEY, client_secret)

    bind_port = port or auth_port()
    from google_auth_oauthlib.flow import InstalledAppFlow

    flow = InstalledAppFlow.from_client_config(
        {"installed": {**block, "redirect_uris": [f"http://localhost:{bind_port}/"]}},
        scopes=[SCOPE],
    )

    print("WAITING: consent", flush=True)
    with _fast_local_bind():
        credentials = flow.run_local_server(
            port=bind_port,
            # Headless by contract: this runs over SSH and Tailscale as often
            # as it runs at the keyboard, and a browser launched on the Mac
            # Studio is a browser nobody is looking at.
            open_browser=False,
            authorization_prompt_message=(
                "\nOpen this URL in a browser signed in as the sending account:\n\n{url}\n\n"
                f"It will redirect to http://localhost:{bind_port}/ on THIS host — so open "
                "it on this Mac, or forward the port. Waiting…\n"
            ),
            success_message=(
                "Consent received. You can close this tab; Cobalt has stored the token."
            ),
            # `offline` + `consent` together are what make Google return a
            # REFRESH token rather than an access token alone. Without
            # prompt='consent' a second run on an already-consented account
            # returns no refresh token at all and the flow silently produces
            # a credential that dies in an hour.
            access_type="offline",
            prompt="consent",
        )

    if not credentials.refresh_token:
        raise EmailError(
            "Google returned no refresh token. Revoke Cobalt's access at "
            "https://myaccount.google.com/permissions and run this again — a "
            "re-consent on an already-authorised account can return an access "
            "token alone, which would expire in an hour."
        )

    put_secret(REFRESH_TOKEN_KEY, credentials.refresh_token)
    _shred(path)
    return "consent stored"


# ---------------------------------------------------------------------
# what the F18 probe asks
# ---------------------------------------------------------------------


def channel_status() -> tuple[bool, str]:
    """(ok, detail) for `heartbeat.probes.email`. Reads NAMES, not values.

    Deliberately does NOT send anything. A probe that sent a test message
    every 15 minutes would be a probe that fills an inbox with 96 mails a
    day and trains its reader to ignore the channel — which is the exact
    failure mode F18 is guarding against.
    """
    from cobalt.redact.secrets import VaultAccessError, secret_names

    try:
        cfg = load_notify_config().email
    except Exception as e:  # noqa: BLE001
        return False, f"notify config unreadable: {type(e).__name__}: {e}"

    if not cfg.enabled:
        return False, "channel DISABLED in configs/cobalt/notify.yaml (deliberate, not an outage)"

    try:
        names = set(secret_names())
    except VaultAccessError as e:
        return False, f"credential UNKNOWN — {e}"

    absent = [k for k in (CLIENT_ID_KEY, CLIENT_SECRET_KEY, REFRESH_TOKEN_KEY) if k not in names]
    if absent:
        return False, (
            f"no consent on this host — vault is missing {', '.join(absent)}. "
            "Run `cobalt notify email-auth`."
        )
    # Recipient omitted for the reason in `send_email` above: it is a
    # vault literal, and this string is rendered into the DM, the email
    # and the daily note. `configs/cobalt/notify.yaml` and `cobalt
    # validate` are where an operator reads the address.
    return True, "token present, recipient set in configs/cobalt/notify.yaml"


__all__ = [
    "AUTH_PORT_KEY",
    "CHANNEL",
    "SCOPE",
    "TIMEOUT_KEY",
    "EmailError",
    "auth_port",
    "channel_status",
    "run_consent_flow",
    "send_email",
    "timeout_s",
]
