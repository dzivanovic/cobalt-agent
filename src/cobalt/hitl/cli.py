"""CLI registration for HITL requests (F20 C4d; L10). Read only.

There is NO approve or deny subcommand: the `/hitl` page is the one place
he approves (L37, F-21).
"""

from __future__ import annotations


def _list(args) -> None:
    from .store import HitlStore

    rows = HitlStore().recent(limit=args.limit)
    if not rows:
        print("no HITL requests")
        return
    for r in rows:
        print(f"{r['short_id']}  {r['status']:<9} {r['action']:<18} {r['created_at']:%Y-%m-%d %H:%M}  "
              f"{r['reason']}")


def add_parser(sub) -> None:
    group = sub.add_parser("hitl", help="F20 HITL requests (read only; approve on the /hitl page)")
    hsub = group.add_subparsers(dest="command", required=True)
    ls = hsub.add_parser("list", help="List recent HITL requests, pending first")
    ls.add_argument("--limit", type=int, default=50)
    ls.set_defaults(func=_list)
