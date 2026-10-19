"""CLI registration for the agent registry (F20 C4d; L10, L16). Read only."""

from __future__ import annotations


def _list(_args) -> None:
    from .registry import list_agents

    for a in list_agents():
        state = "own loader" if a.enabled is None else ("enabled" if a.enabled else "disabled")
        print(f"{a.id:<16} {state:<10} {a.path.name}")


def add_parser(sub) -> None:
    group = sub.add_parser("agents", help="F20 agent registry (configs/cobalt/agents/*.yaml; read only)")
    asub = group.add_subparsers(dest="command", required=True)
    asub.add_parser("list", help="List every registry entry by id").set_defaults(func=_list)
