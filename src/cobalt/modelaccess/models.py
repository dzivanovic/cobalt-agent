"""The typed contract every model caller shares (seam S1 §2.2).

A caller names a ROUTE and gets a `ModelResult` or a `ModelCallError` —
never `None`, never an empty string presented as an answer (L1: `empty`
is an error kind). It never sees a URL, a key, a provider or a model file.
"""

from __future__ import annotations

from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, ConfigDict, Field

#: Seam §2.2, verbatim. A new kind is a seam change, not a caller's choice.
ERROR_KINDS = frozenset({
    "route_unknown",
    "prompt_refused",
    "unreachable",
    "timeout",
    "http_status",
    "bad_response",
    "empty",
    "think_leak",
    "schema_refused",
})


class ModelMessage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    role: Literal["system", "user", "assistant"]
    content: str


class ModelRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    #: A ROUTE NAME from `configs/cobalt/modelaccess.yaml` — never a
    #: provider, a model id or a URL.
    route: str = Field(min_length=1)
    #: Who is calling (e.g. "voice.plan") — recorded on the call line.
    caller: str = Field(min_length=1)
    #: The caller's own id for this call (voice: the turn id).
    request_id: str = Field(min_length=1)
    messages: list[ModelMessage] = Field(min_length=1)
    #: A JSON schema the caller validates against anyway (with Pydantic).
    response_schema: Optional[dict] = None
    #: None = the route's budget; a caller may only LOWER either.
    max_output_tokens: Optional[int] = Field(default=None, gt=0)
    timeout_s: Optional[float] = Field(default=None, gt=0)


class Usage(BaseModel):
    model_config = ConfigDict(extra="forbid")

    input_tokens: Optional[int] = None
    output_tokens: Optional[int] = None


class ModelResult(BaseModel):
    model_config = ConfigDict(extra="forbid")

    route: str
    caller: str
    request_id: str
    lane: Literal["local"]
    kind: Literal["openai_compatible"]
    #: AS RETURNED by the server, never the configured alias.
    model_returned: str
    #: The reply text after the route's think policy (§2.4).
    content: str
    think_block: Literal["absent", "empty_removed"]
    finish_reason: Optional[str]
    usage: Usage
    #: request built → validated result (time.perf_counter).
    latency_ms: int
    at: datetime


class ModelCallError(RuntimeError):
    """One typed failure. `detail` has passed `redact()`; raised `from None`
    so no chained traceback can carry request text into a log."""

    def __init__(self, kind: str, *, route: str, caller: str, request_id: str, detail: str):
        if kind not in ERROR_KINDS:  # pragma: no cover - a programming error
            raise ValueError(f"unknown ModelCallError kind {kind!r}")
        self.kind = kind
        self.route = route
        self.caller = caller
        self.request_id = request_id
        self.detail = detail
        super().__init__(f"model call {kind} (route={route}, caller={caller}, request_id={request_id}): {detail}")


__all__ = [
    "ERROR_KINDS",
    "ModelCallError",
    "ModelMessage",
    "ModelRequest",
    "ModelResult",
    "Usage",
]
