"""CLI registration for HITL requests (F20 C4d; L10). Read only, but the dev X15 send.

There is NO approve or deny subcommand: the `/hitl` page is the one place
he approves (L37, F-21).

`x15-send` (card 977) DMs one link to the store-free `/hitl/x15-probe` page,
with a fresh key in the fragment, so a tap on his phone answers X15: does the
page script see `k`? Dev only; it writes no row and approves nothing. The key
is never printed, logged or stored.
"""

from __future__ import annotations

import secrets
import sys


def _list(args) -> None:
    from .store import HitlStore

    rows = HitlStore().recent(limit=args.limit)
    if not rows:
        print("no HITL requests")
        return
    for r in rows:
        print(f"{r['short_id']}  {r['status']:<9} {r['action']:<18} {r['created_at']:%Y-%m-%d %H:%M}  "
              f"{r['reason']}")


def _x15_send(args) -> None:
    from cobalt.env import EnvConfigError, resolve_env
    from cobalt.notify import mattermost

    from . import card

    try:
        dev = resolve_env() == "dev"
    except EnvConfigError:
        dev = False
    if not dev:
        print("REFUSED: cobalt hitl x15-send runs under COBALT_ENV=dev only", file=sys.stderr)
        sys.exit(2)
    key = secrets.token_hex(16)
    base = card.page_base_url()
    result = mattermost.send_dm(f"X15 test, approves nothing\n{base}/hitl/x15-probe#k={key}")
    if not result.sent:
        print(f"X15 NOT SENT {result.detail}")
        sys.exit(1)
    print(f"X15 SENT {result.detail}")


def add_parser(sub) -> None:
    group = sub.add_parser("hitl", help="F20 HITL requests (read only; approve on the /hitl page)")
    hsub = group.add_subparsers(dest="command", required=True)
    ls = hsub.add_parser("list", help="List recent HITL requests, pending first")
    ls.add_argument("--limit", type=int, default=50)
    ls.set_defaults(func=_list)
    x15 = hsub.add_parser("x15-send", help="DEV ONLY: DM the X15 probe link (approves nothing)")
    x15.set_defaults(func=_x15_send)
