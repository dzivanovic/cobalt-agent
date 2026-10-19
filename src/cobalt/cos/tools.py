"""The CoS tool server: seven tools, no approve verb (F20 FINAL §2 `cos/tools.py`, §3; L37).

READ TOOLS answer from Cobalt's own stores through the readers the sheet
and voice already use (`voice/tools.py` `read_open_cards`, `read_pool`): no
second query path, and code renders every figure.

REQUEST TOOLS only ask: `request_action` and `draft_agent` (the model's view
of `agents.create`) call `hitl.actions.request_action`, which writes a
`pending` row and the card. There is NO approve, decide or execute tool —
only his tap on the `/hitl` page approves (T3).

Every tool returns TEXT. A refusal is a tool result (`refused: …`), never an
exception into the SDK. This module never imports the SDK: `cos/session.py`
wraps these handlers into the in-process MCP server when a session opens.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Callable

from cobalt.agents.registry import TOOL_CATALOG


@dataclass(frozen=True)
class ToolDef:
    name: str
    description: str
    #: JSON Schema of the arguments, as the MCP server advertises it.
    schema: dict
    handler: Callable[[dict], str]


def _cards_open(_args: dict) -> str:
    from cobalt.voice.tools import read_open_cards, render_open_cards

    return render_open_cards(read_open_cards())


def _radar_pool(_args: dict) -> str:
    from cobalt.voice.tools import read_pool, render_pool

    return render_pool(read_pool())


def _jobs_status(_args: dict) -> str:
    from cobalt.jobs.store import JobStore

    rows = JobStore().all()
    if not rows:
        return "No jobs are registered."
    return "\n".join(
        f"{r['label']}: {r['state']}" + (f" (exit {r['exit_code']})" if r.get("exit_code") is not None else "")
        for r in rows
    )


def _hitl_list(_args: dict) -> str:
    from cobalt.hitl.store import HitlStore

    rows = HitlStore().recent(limit=20)
    if not rows:
        return "No HITL requests."
    return "\n".join(f"{r['short_id']}: {r['action']} · {r['status']}" for r in rows)


def _agents_list(_args: dict) -> str:
    from cobalt.agents.registry import list_agents

    return "\n".join(
        f"{a.id}: " + ("enabled" if a.enabled else "disabled" if a.enabled is False else "own loader")
        for a in list_agents()
    )


def _request_action(args: dict) -> str:
    from cobalt.hitl import actions

    if not isinstance(args.get("action"), str):
        return "refused: request_action needs an action name"
    return actions.request_action(args["action"], args.get("args", {}), str(args.get("reason", "")))


def _draft_agent(args: dict) -> str:
    from cobalt.hitl import actions

    if not isinstance(args.get("yaml"), str) or not args["yaml"].strip():
        return "refused: draft_agent needs the agent's YAML"
    return actions.request_action("agents.create", {"yaml": args["yaml"]}, str(args.get("reason", "")))


_NO_ARGS = {"type": "object", "properties": {}, "additionalProperties": False}

TOOLS: dict[str, ToolDef] = {t.name: t for t in (
    ToolDef("cards.open", "List the open cards (ticker, direction, state, stop).", _NO_ARGS, _cards_open),
    ToolDef("radar.pool", "Read the current radar pool.", _NO_ARGS, _radar_pool),
    ToolDef("jobs.status", "Read every Cobalt job's state.", _NO_ARGS, _jobs_status),
    ToolDef("hitl.list", "List the recent HITL requests and their status.", _NO_ARGS, _hitl_list),
    ToolDef("agents.list", "List the registered agents.", _NO_ARGS, _agents_list),
    ToolDef(
        "request_action",
        "Ask for one catalogued action (agents.create, agents.deactivate). Returns 'pending <id>' — "
        "only the trader's tap on the /hitl page approves it.",
        {"type": "object", "properties": {"action": {"type": "string"}, "args": {"type": "object"},
                                          "reason": {"type": "string"}},
         "required": ["action", "args", "reason"], "additionalProperties": False},
        _request_action,
    ),
    ToolDef(
        "draft_agent",
        "Draft a new registry agent from its YAML (one `agent:` mapping). Returns 'pending <id>'; "
        "the agent exists only after the trader approves the card.",
        {"type": "object", "properties": {"yaml": {"type": "string"}, "reason": {"type": "string"}},
         "required": ["yaml", "reason"], "additionalProperties": False},
        _draft_agent,
    ),
)}
assert set(TOOLS) == set(TOOL_CATALOG), "cos.tools and agents.registry.TOOL_CATALOG disagree"


def call(name: str, args: Any) -> str:
    """Run one tool. Never raises: a failure is a `refused: …` result."""
    tool = TOOLS.get(name)
    if tool is None:
        return f"refused: no tool {name!r}"
    if not isinstance(args, dict):
        return f"refused: {name} args must be an object, got {json.dumps(args, default=str)[:80]}"
    try:
        return tool.handler(args)
    except Exception as e:  # noqa: BLE001 - a refusal is a tool result, never an exception
        return f"refused: {name} failed ({type(e).__name__}: {e})"


__all__ = ["TOOLS", "ToolDef", "call"]
