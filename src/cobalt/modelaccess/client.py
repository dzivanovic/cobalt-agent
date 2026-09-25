"""`call()` / `call_sync()` — resolve the route → guard → adapter → validate
→ `ModelResult` (seam S1 §2.1, §2.4). The ONE model-call path of the new
core (L3, L5 as cited — the routing cluster is frozen and cited, never
rewritten here).

ONE code path: `call()` is `call_sync()` under `asyncio.to_thread`, so the
FastAPI route never blocks the loop (FINAL [F-04]) and the CLI / tests run
the very same code.
"""

from __future__ import annotations

import asyncio
import json
import re
import time
from datetime import datetime, timezone
from typing import Optional

from loguru import logger

from cobalt.redact import redact

from .adapters import ADAPTERS, AdapterFailure
from .config import ModelAccessConfig, Route, load_routes
from .guard import PromptRefused, refuse_if_secret_shaped
from .models import ERROR_KINDS, ModelCallError, ModelRequest, ModelResult, Usage

NO_THINK = "/no_think"
_THINK = re.compile(r"^\s*<think>(?P<body>.*?)</think>\s*", re.S)


def _error(kind: str, req: ModelRequest, detail: str) -> ModelCallError:
    safe = redact(detail, channel="modelaccess").text
    return ModelCallError(kind, route=req.route, caller=req.caller, request_id=req.request_id, detail=safe)


def _record(req: ModelRequest, route: Optional[Route], *, started: float, result: Optional[ModelResult],
            error: Optional[str], literal_guard: Optional[bool]) -> None:
    """THE call record (L57): one line, success or error, no message text."""
    usage = result.usage if result else None
    line = (
        "modelaccess call route={} caller={} request_id={} lane={} kind={} model_returned={} "
        "latency_ms={} input_tokens={} output_tokens={} think_block={} literal_guard={} error={}"
    )
    args = (
        req.route, req.caller, req.request_id,
        route.lane if route else "-", route.kind if route else "-",
        result.model_returned if result else "-",
        result.latency_ms if result else int((time.perf_counter() - started) * 1000),
        usage.input_tokens if usage else "-", usage.output_tokens if usage else "-",
        result.think_block if result else "-",
        {True: "active", False: "INACTIVE", None: "-"}[literal_guard],
        error or "none",
    )
    if error:
        logger.error(line, *args)
    else:
        logger.info(line, *args)


def _apply_think_policy(req: ModelRequest, content: Optional[str], reasoning: Optional[str]) -> tuple[str, str]:
    """`forbid_nonempty` (seam §2.4 (2)). Returns (content, think_block)."""
    if reasoning and reasoning.strip():
        raise _error("think_leak", req, "the server returned non-empty reasoning content")
    text = content or ""
    block = "absent"
    m = _THINK.match(text)
    if m:
        if m.group("body").strip():
            raise _error("think_leak", req, "a non-empty <think> block")
        text = text[m.end():]
        block = "empty_removed"
    if "<think>" in text or "</think>" in text:
        raise _error("think_leak", req, "a <think> tag outside an empty leading block")
    if not text.strip():
        raise _error("empty", req, "no content")
    return text.strip(), block


def call_sync(req: ModelRequest, *, config: Optional[ModelAccessConfig] = None) -> ModelResult:
    started = time.perf_counter()
    cfg = config or load_routes()
    route = cfg.routes.get(req.route)
    literal_guard: Optional[bool] = None
    try:
        if route is None:
            raise _error("route_unknown", req, f"no route named {req.route!r} in the registry")
        if req.max_output_tokens is not None and req.max_output_tokens > route.max_output_tokens:
            raise ValueError(
                f"max_output_tokens {req.max_output_tokens} exceeds the route budget "
                f"{route.max_output_tokens}; a caller may only lower it")
        if req.timeout_s is not None and req.timeout_s > route.timeout_s:
            raise ValueError(
                f"timeout_s {req.timeout_s} exceeds the route budget {route.timeout_s}; "
                "a caller may only lower it")

        messages = [m.model_dump() for m in req.messages]
        response_format = None
        if req.response_schema is not None:
            if route.response_format == "json_schema":
                response_format = {"type": "json_schema", "json_schema": {
                    "name": "reply", "strict": True, "schema": req.response_schema}}
            else:
                sys_idx = next((i for i, m in enumerate(messages) if m["role"] == "system"), None)
                note = "Reply with ONE JSON object matching this JSON schema:\n" + json.dumps(req.response_schema)
                if sys_idx is None:
                    messages.insert(0, {"role": "system", "content": note})
                else:
                    messages[sys_idx]["content"] = messages[sys_idx]["content"] + "\n\n" + note
        if route.no_think:
            last_user = max((i for i, m in enumerate(messages) if m["role"] == "user"), default=None)
            if last_user is not None:
                messages[last_user]["content"] = messages[last_user]["content"] + " " + NO_THINK

        # 1. GUARD FIRST — every byte that would leave the process.
        try:
            for i, m in enumerate(messages):
                literal_guard = refuse_if_secret_shaped(m["content"], where=f"messages[{i}]").literal_guard_active
            if response_format is not None:
                refuse_if_secret_shaped(json.dumps(response_format), where="response_format")
        except PromptRefused as e:
            raise _error("prompt_refused", req, f"{e.where}: {', '.join(e.kinds)}")

        api_key = None
        if route.key_name:
            from cobalt.redact.secrets import read_secret

            api_key = read_secret(route.key_name)

        adapter = ADAPTERS[route.kind]
        try:
            raw = adapter.complete(
                route, messages=messages,
                max_tokens=req.max_output_tokens or route.max_output_tokens,
                timeout_s=req.timeout_s or route.timeout_s,
                response_format=response_format, api_key=api_key,
            )
        except AdapterFailure as e:
            raise _error(e.kind, req, e.detail)

        content, block = _apply_think_policy(req, raw.content, raw.reasoning)
        if not raw.model_returned:
            raise _error("bad_response", req, "the reply names no model")
        result = ModelResult(
            route=req.route, caller=req.caller, request_id=req.request_id,
            lane=route.lane, kind=route.kind, model_returned=raw.model_returned,
            content=content, think_block=block, finish_reason=raw.finish_reason,
            usage=Usage(input_tokens=raw.input_tokens, output_tokens=raw.output_tokens),
            latency_ms=int((time.perf_counter() - started) * 1000),
            at=datetime.now(timezone.utc),
        )
    except ModelCallError as e:
        _record(req, route, started=started, result=None, error=e.kind, literal_guard=literal_guard)
        raise e from None
    _record(req, route, started=started, result=result, error=None, literal_guard=literal_guard)
    return result


async def call(req: ModelRequest, *, config: Optional[ModelAccessConfig] = None) -> ModelResult:
    """The FastAPI path. Never blocks the event loop (FINAL [F-04])."""
    return await asyncio.to_thread(call_sync, req, config=config)


__all__ = ["ERROR_KINDS", "NO_THINK", "call", "call_sync"]
