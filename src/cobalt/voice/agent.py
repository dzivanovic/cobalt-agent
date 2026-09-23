"""The conversational agent: the whitelisted prompt builder and the ONE
Plan call per turn, through `cobalt.modelaccess` (FINAL §2.4, [F-01]).

THE PROMPT TAKES ONLY `PromptInputs` (L4 / L41): the transcript, this
widget session's last turns (transcript + reply, from rows), the session
clock, and the CLOSED candidate list (id + code-rendered label), plus the
registry entry's charter and tool list. No path, env value, config value
or key name has a way in — and anything secret-shaped that slips into
those fields is refused by the S1 guard before a byte leaves.

THE PLAN IS VALIDATED BY CODE, never trusted: JSON that parses into
`Plan`, a tool on the allowlist whose kind matches the plan's kind,
argument names the tool takes, every span a VERBATIM substring of the
transcript, every candidate id on the closed list. Anything else FAILS
the turn loud (`voice_plan`), nothing executes, and there is no retry —
one call per turn.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Optional

from pydantic import ValidationError

from cobalt.modelaccess import ModelCallError, ModelMessage, ModelRequest, ModelResult
from cobalt.modelaccess.client import call_sync
from cobalt.modelaccess.config import ModelAccessConfig

from .models import CandidateRef, Plan, PromptInputs, Span
from .registry import AgentSpec

CALLER = "voice.plan"


class PlanFailed(RuntimeError):
    """The Plan stage failed. `kind` is a model-access error kind or one of
    `plan_parse`, `plan_tool`, `plan_shape`, `plan_span`, `plan_candidate`."""

    failure_class = "voice_plan"

    def __init__(self, kind: str, detail: str, result: Optional[ModelResult] = None):
        self.kind = kind
        self.detail = detail
        self.result = result
        super().__init__(f"voice_plan {kind}: {detail}")


@dataclass(frozen=True)
class PlanOutcome:
    plan: Plan
    result: ModelResult


def _plan_schema(tools: list[str]) -> dict:
    arg = {
        "anyOf": [
            {"type": "object", "additionalProperties": False, "required": ["span"],
             "properties": {"span": {"type": "string", "minLength": 1}}},
            {"type": "object", "additionalProperties": False, "required": ["candidate"],
             "properties": {"candidate": {"type": "string", "minLength": 1}}},
        ]
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "required": ["kind", "tool", "args", "say"],
        "properties": {
            "kind": {"type": "string", "enum": ["answer", "act", "clarify", "unsupported", "refuse"]},
            "tool": {"type": ["string", "null"], "enum": [*tools, None]},
            "args": {"type": "object", "additionalProperties": arg},
            "say": {"type": ["string", "null"]},
        },
    }


def _registry_tools() -> list[str]:
    from .registry import load_agent

    return sorted(load_agent().tools)


#: The JSON schema the Plan call sends (as `response_format` or in the
#: system message, per the route) — built from the committed registry.
PLAN_SCHEMA = _plan_schema(_registry_tools())


def build_messages(inputs: PromptInputs, agent: AgentSpec) -> list[ModelMessage]:
    """System: the charter, the rules and the tool list. User: ONE JSON
    object of the whitelisted inputs. Nothing else."""
    tool_lines = []
    for name in sorted(agent.tools):
        t = agent.tools[name]
        args = ", ".join(f"{a} ({s.type}{'' if s.required else ', optional'})" for a, s in t.args.items()) or "none"
        tool_lines.append(f"- {name} [{t.kind}]: {t.description} Args: {args}.")
    system = "\n".join([
        agent.charter.strip(),
        "",
        "Reply with ONE JSON object and nothing else: "
        '{"kind": ..., "tool": ..., "args": {...}, "say": ...}.',
        "kind: answer (a read tool answers the question), act (an act tool changes something — "
        "the trader confirms later), clarify (the target or value is unclear), unsupported (no tool "
        "does this), refuse (an order, a trade, or anything on a trading platform).",
        "tool: one name from the list below, or null for clarify / unsupported / refuse.",
        'args: each value is {"span": "<text copied EXACTLY, character for character, from the '
        'transcript>"} or {"candidate": "<an id from candidates>"}. Never invent, round or '
        "reformat a span.",
        "say: optional short words for the trader, or null. Never state a number.",
        "Tools:",
        *tool_lines,
    ])
    user = json.dumps({
        "clock": inputs.clock,
        "candidates": [{"id": c.id, "label": c.label} for c in inputs.candidates],
        "history": [{"said": h.transcript, "reply": h.reply} for h in inputs.history],
        "transcript": inputs.transcript,
    }, ensure_ascii=False)
    return [ModelMessage(role="system", content=system), ModelMessage(role="user", content=user)]


def validate_plan(content: str, transcript: str, agent: AgentSpec, candidate_ids: set[str]) -> Plan:
    try:
        obj = json.loads(content)
    except (TypeError, ValueError):
        raise PlanFailed("plan_parse", "the reply is not a JSON object") from None
    if not isinstance(obj, dict):
        raise PlanFailed("plan_parse", "the reply is not a JSON object")
    try:
        plan = Plan(**obj)
    except (ValidationError, TypeError) as e:
        raise PlanFailed("plan_parse", f"the reply is not a Plan ({e.error_count() if isinstance(e, ValidationError) else 1} error(s))") from None

    if plan.tool is not None and plan.tool not in agent.tools:
        raise PlanFailed("plan_tool", f"tool {plan.tool!r} is not on the allowlist")
    if plan.kind in ("answer", "act"):
        if plan.tool is None:
            raise PlanFailed("plan_shape", f"kind {plan.kind} names no tool")
        want = "read" if plan.kind == "answer" else "act"
        if agent.tools[plan.tool].kind != want:
            raise PlanFailed("plan_shape", f"kind {plan.kind} on a {agent.tools[plan.tool].kind} tool")
    if plan.tool is not None:
        extra = sorted(set(plan.args) - set(agent.tools[plan.tool].args))
        if extra:
            raise PlanFailed("plan_shape", f"tool {plan.tool} takes no argument(s) {extra}")
    elif plan.args:
        raise PlanFailed("plan_shape", "arguments without a tool")
    for name, value in plan.args.items():
        if isinstance(value, Span) and value.span not in transcript:
            raise PlanFailed("plan_span", f"argument {name!r}: the span is not a verbatim substring of the transcript")
        if isinstance(value, CandidateRef) and value.candidate not in candidate_ids:
            raise PlanFailed("plan_candidate", f"argument {name!r}: candidate is not on the closed list")
    return plan


def plan_turn(
    inputs: PromptInputs,
    *,
    agent: AgentSpec,
    turn_id: str,
    config: Optional[ModelAccessConfig] = None,
) -> PlanOutcome:
    """ONE model call, through the one module, on the registry's route."""
    req = ModelRequest(route=agent.route, caller=CALLER, request_id=turn_id,
                       messages=build_messages(inputs, agent), response_schema=PLAN_SCHEMA)
    try:
        result = call_sync(req, config=config)
    except ModelCallError as e:
        raise PlanFailed(e.kind, e.detail) from None
    plan = None
    try:
        plan = validate_plan(result.content, inputs.transcript, agent, {c.id for c in inputs.candidates})
    except PlanFailed as e:
        e.result = result
        raise
    return PlanOutcome(plan=plan, result=result)


__all__ = ["CALLER", "PLAN_SCHEMA", "PlanFailed", "PlanOutcome", "build_messages", "plan_turn", "validate_plan"]
