"""`cobalt notify` — the outbound channels' command surface.

    cobalt notify email-auth [--client-json PATH]   one-time consent
    cobalt notify email-test                        prove the channel
    cobalt notify email-status                      names, never values

`email-auth` is INTERACTIVE and runs once per host. It reads the Desktop
OAuth client JSON, puts its two halves in the vault, runs the loopback
consent flow on the fixed `notify.email.auth_port`, stores the refresh
token, and shreds the client JSON. Nothing it prints is a secret: the
authorisation URL carries a client id and a scope, and the vault writes
are announced by NAME.

`email-test` is the proof, and it is a real send — a channel that has
only ever been mocked is a channel nobody has tested.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_CLIENT_JSON = Path("~/.cobalt/google-oauth-client.json")


def cmd_email_auth(args: argparse.Namespace) -> None:
    from cobalt.notify.email import auth_port, run_consent_flow

    path = Path(args.client_json).expanduser()
    print(
        f"Reading the Desktop OAuth client from {path}\n"
        f"Loopback flow will bind port {auth_port()} (tunable notify.email.auth_port).\n"
        "The client JSON is SHREDDED once its two halves are in the vault.\n"
    )
    print(run_consent_flow(path))


def cmd_email_test(args: argparse.Namespace) -> None:
    """One real message, and the row that proves it to the F18 probe."""
    from cobalt.notify.config import load_notify_config
    from cobalt.notify.email import EmailError, send_email
    from cobalt.notify.store import record_attempt
    from cobalt.redact import install_log_guard

    install_log_guard()
    cfg = load_notify_config().email
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    body = (
        f"Cobalt email channel proven {stamp}\n\n"
        "This is Charter §3 F18's out-of-band alert path. If you are reading it, a "
        "red heartbeat can reach you without Mattermost, Postgres or the vault "
        "being healthy.\n"
    )
    try:
        result = send_email(cfg.to, f"email channel proven {stamp}", body)
    except EmailError as e:
        record_attempt(ok=False, caller="email-test", detail=str(e))
        raise
    record_attempt(
        ok=result.sent, caller="email-test", detail=result.detail, message_id=result.ref
    )
    print(result.report())
    if result.sent:
        print(f"Gmail message id: {result.ref}")


def cmd_email_status(args: argparse.Namespace) -> None:
    from cobalt.notify.email import channel_status
    from cobalt.notify.store import EmailSendStore

    ok, detail = channel_status()
    print(f"email channel: {'OK' if ok else 'RED'} — {detail}")
    try:
        last = EmailSendStore().last()
    except Exception as e:  # noqa: BLE001
        print(f"last send: UNKNOWN — history unreadable ({type(e).__name__}: {e})")
        return
    if last is None:
        print("last send: never")
        return
    print(
        f"last send: {'OK' if last['ok'] else 'FAILED'} at "
        f"{last['ts']:%Y-%m-%d %H:%M:%S %Z} by {last['caller']} — {last['detail']}"
    )


def add_parser(sub) -> None:
    notify = sub.add_parser("notify", help="Outbound alert channels (F18/F19)")
    nsub = notify.add_subparsers(dest="command", required=True)

    auth = nsub.add_parser(
        "email-auth", help="One-time Google OAuth consent for the email channel."
    )
    auth.add_argument(
        "--client-json",
        default=str(DEFAULT_CLIENT_JSON),
        help=f"Desktop OAuth client JSON (default {DEFAULT_CLIENT_JSON}); shredded after use.",
    )
    auth.set_defaults(func=cmd_email_auth)

    test = nsub.add_parser("email-test", help="Send one real message and print its id.")
    test.set_defaults(func=cmd_email_test)

    status = nsub.add_parser(
        "email-status", help="Is the channel armed? Names and outcomes, never values."
    )
    status.set_defaults(func=cmd_email_status)


__all__ = ["add_parser"]
