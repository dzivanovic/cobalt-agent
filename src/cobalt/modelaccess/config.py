"""The route registry: `configs/cobalt/modelaccess.yaml` (seam S1 §2.3).

L10: Pydantic schema, `extra="forbid"`, a bad file crashes naming its line
(YAML) or its key path (schema); L1: every key is REQUIRED — a missing key
crashes the load, there is no default to fall back to.

V1 accepts exactly one lane (`local`), one kind (`openai_compatible`) and
one think policy (`forbid_nonempty`). A `lane: local` route must point at a
LOOPBACK host. There is NO `fallback` key anywhere: whether any lane
carries a fallback is the routing lane's (L23 / L25, frozen — FINAL
[F-23]); the day it rules, the fallback is configured here, never in a
caller. `key_name` is a VaultManager NAME, fetched at call time — never a
value (L4).
"""

from __future__ import annotations

import ipaddress
import re
from pathlib import Path
from typing import Literal, Optional
from urllib.parse import urlsplit

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "modelaccess.yaml"

_LOOPBACK_NAMES = frozenset({"localhost"})
#: A VaultManager key name: letters, digits, `_ . : -` — nothing that
#: could be a token (no base64 run, no `sk-` shape).
_KEY_NAME = re.compile(r"^[A-Z][A-Z0-9_]{2,63}$")


class ModelAccessConfigError(RuntimeError):
    """Missing / invalid route registry — crash, never fall back."""


class Route(BaseModel):
    model_config = ConfigDict(extra="forbid")

    lane: Literal["local"]
    kind: Literal["openai_compatible"]
    api_base: str
    model: str = Field(min_length=1)
    no_think: bool
    think_policy: Literal["forbid_nonempty"]
    timeout_s: float = Field(gt=0)
    max_output_tokens: int = Field(gt=0)
    #: How a caller's `response_schema` travels: `json_schema` = the
    #: OpenAI-compatible `response_format` (only where X-E4 shows the
    #: server honours it); `in_prompt` = appended to the system message.
    #: Either way the CALLER validates the content (seam §2.4 (3)).
    response_format: Literal["json_schema", "in_prompt"]
    key_name: Optional[str]

    @field_validator("api_base")
    @classmethod
    def _loopback_only(cls, v: str) -> str:
        parts = urlsplit(v)
        if parts.scheme not in ("http", "https") or not parts.hostname:
            raise ValueError(f"api_base must be an http(s) URL with a host, got {v!r}")
        host = parts.hostname
        if host in _LOOPBACK_NAMES:
            return v
        try:
            ip = ipaddress.ip_address(host)
        except ValueError:
            ip = None
        if ip is None or not ip.is_loopback:
            raise ValueError(
                f"lane local requires a loopback host (127.0.0.1, ::1, localhost); got {host!r}. "
                "A non-local lane is the routing tribunal's to add (L23/L25 frozen)."
            )
        return v

    @field_validator("key_name")
    @classmethod
    def _a_name_not_a_value(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not _KEY_NAME.match(v):
            raise ValueError(
                "key_name must be a VaultManager key NAME (UPPER_SNAKE), never a value"
            )
        return v


class ModelAccessConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    routes: dict[str, Route] = Field(min_length=1)


def _find_fallback(data, path="") -> Optional[str]:
    if isinstance(data, dict):
        for k, v in data.items():
            here = f"{path}.{k}" if path else str(k)
            if str(k) == "fallback":
                return here
            found = _find_fallback(v, here)
            if found:
                return found
    return None


def load_routes(path: Path = CONFIG_PATH) -> ModelAccessConfig:
    """The registry, validated, or a loud `ModelAccessConfigError`."""
    path = Path(path)
    if not path.exists():
        raise ModelAccessConfigError(
            f"model-access registry not found: {path}. There is no built-in route: "
            "a model call nobody declared is a model call nobody audits."
        )
    try:
        raw = yaml.safe_load(path.read_text())
    except yaml.YAMLError as e:
        mark = getattr(e, "problem_mark", None)
        where = f" at line {mark.line + 1}, column {mark.column + 1}" if mark else ""
        raise ModelAccessConfigError(f"{path}: YAML error{where}: {e}") from None
    if not isinstance(raw, dict):
        raise ModelAccessConfigError(f"{path}: expected a mapping with 'routes'")
    fb = _find_fallback(raw)
    if fb:
        raise ModelAccessConfigError(
            f"{path}: '{fb}' — a fallback key is refused. Fallback is the routing lane's "
            "(L23/L25 frozen, FINAL [F-23]); V1 builds the local lane only."
        )
    try:
        return ModelAccessConfig(**raw)
    except ValidationError as e:
        raise ModelAccessConfigError(f"{path}: invalid model-access registry:\n{e}") from None


__all__ = ["CONFIG_PATH", "ModelAccessConfig", "ModelAccessConfigError", "Route", "load_routes"]
