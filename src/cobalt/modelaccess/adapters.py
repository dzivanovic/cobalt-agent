"""ONE adapter per route `kind` (seam S1 §2.1). V1 ships `openai_compatible`.

THE TRANSPORT IS THE `openai` CLIENT (already pinned, S1-F2), NOT litellm —
decided by measurement, recorded in the build report (C1):

* `import litellm` IS silent with the cost-map fetch disabled
  (`test_modelaccess_silence.py::test_litellm_import_is_probed`: zero
  non-loopback attempts) — seam §2.4 (5)'s stated condition held;
* but on the fake server litellm REWROTE THE REPLY: a server body of
  `<think>\\n\\n</think>\\n{...}` reached the module as `{...}` (the think
  policy read `absent`, not `empty_removed`), and it classified both a
  refused connection and a non-JSON 200 body as an HTTP status error.
  The seam forbids exactly that: the module "never repairs content" and
  applies ITS OWN think policy to what the server returned (§2.4 (2), (3),
  (6)). With the `openai` client the server's bytes arrive unmodified.

The INTERFACE does not change (seam §2.4 (5)). `litellm` stays a direct
dependency (the old tree imports it) and nothing in `src/cobalt` imports it.

Retries are ZERO (`max_retries=0`): a timeout or a 5xx is one typed
failure, never a second attempt the caller did not see. `trust_env=False`:
a proxy variable in the environment never reroutes a loopback call.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import httpx
import openai

from .config import Route


class AdapterFailure(RuntimeError):
    """A transport-level failure, already classified into a seam error kind."""

    def __init__(self, kind: str, detail: str):
        self.kind = kind
        self.detail = detail
        super().__init__(f"{kind}: {detail}")


@dataclass(frozen=True)
class RawReply:
    content: Optional[str]
    reasoning: Optional[str]
    model_returned: str
    finish_reason: Optional[str]
    input_tokens: Optional[int]
    output_tokens: Optional[int]


def _classify(e: Exception) -> AdapterFailure:
    """Map a transport exception onto the seam's kinds (§2.4 (6)). The
    order matters: a timeout IS an `APIConnectionError` subclass."""
    name = type(e).__name__
    if isinstance(e, openai.APITimeoutError):
        return AdapterFailure("timeout", name)
    if isinstance(e, openai.APIStatusError):
        return AdapterFailure("http_status", f"HTTP {e.status_code} ({name})")
    if isinstance(e, openai.APIConnectionError):
        return AdapterFailure("unreachable", name)
    return AdapterFailure("bad_response", name)


class OpenAICompatibleAdapter:
    """`kind: openai_compatible` — an OpenAI-shaped `/chat/completions` server."""

    kind = "openai_compatible"

    def complete(
        self,
        route: Route,
        *,
        messages: list[dict[str, str]],
        max_tokens: int,
        timeout_s: float,
        response_format: Optional[dict[str, Any]],
        api_key: Optional[str],
    ) -> RawReply:
        kwargs: dict[str, Any] = dict(model=route.model, messages=messages, max_tokens=max_tokens)
        if response_format is not None:
            kwargs["response_format"] = response_format
        with httpx.Client(trust_env=False, timeout=timeout_s) as http:
            client = openai.OpenAI(
                base_url=route.api_base,
                # LM Studio takes no key today; the client insists on a
                # non-empty string. A constant placeholder, never a secret.
                api_key=api_key or "no-key-local-lane",
                max_retries=0,
                timeout=timeout_s,
                http_client=http,
            )
            try:
                resp = client.chat.completions.create(**kwargs)
            except Exception as e:  # noqa: BLE001 - classified, re-raised typed
                raise _classify(e) from None
        try:
            if isinstance(resp, (str, bytes)):
                raise TypeError("the server returned a non-JSON body")
            choices = resp.choices or []
            model_returned = str(resp.model or "")
            if not choices:
                return RawReply(None, None, model_returned, None, None, None)
            msg = choices[0].message
            extra = getattr(msg, "model_extra", None) or {}
            reasoning = extra.get("reasoning_content", extra.get("reasoning"))
            usage = resp.usage
            return RawReply(
                content=msg.content,
                reasoning=reasoning if isinstance(reasoning, str) else None,
                model_returned=model_returned,
                finish_reason=choices[0].finish_reason,
                input_tokens=usage.prompt_tokens if usage else None,
                output_tokens=usage.completion_tokens if usage else None,
            )
        except Exception as e:  # noqa: BLE001 - an envelope we cannot read
            raise AdapterFailure("bad_response", type(e).__name__) from None


ADAPTERS = {"openai_compatible": OpenAICompatibleAdapter()}

__all__ = ["ADAPTERS", "AdapterFailure", "OpenAICompatibleAdapter", "RawReply"]
