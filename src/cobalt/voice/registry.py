"""The voice agent as a REGISTRY ENTRY (L16): `configs/cobalt/agents/voice.yaml`.

Charter, the model ROUTE NAME (never a provider, a model id or a URL —
checked against the model-access registry), the tool allowlist with each
tool's kind, `trading_logic` flag and argument schema, and the confirm /
cancel words. The words are EXACTLY `["yes"]` / `["no"]` until an E4 / X1
measurement widens them (FINAL [F-08]).

A tool the code does not implement, or an argument type the code cannot
parse, is refused at load: the registry can narrow what the agent may
do, never invent a capability.
"""

from __future__ import annotations

from pathlib import Path
from typing import Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "agents" / "voice.yaml"

#: The tools this code implements (voice/tools.py asserts it matches).
KNOWN_TOOLS = frozenset({"cards.open", "radar.pool", "cards.numbers", "cards.set_stop"})
#: The argument types the resolver can bind (voice/resolve.py).
ARG_TYPES = ("card", "price")


class AgentConfigError(RuntimeError):
    """Missing / invalid agent registry entry — crash, never fall back."""


class ToolArg(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["card", "price"]
    required: bool


class ToolSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kind: Literal["read", "act"]
    #: `true` tools are NEVER executed by voice (L7; V5 drafts them).
    trading_logic: bool
    description: str = Field(min_length=1)
    args: dict[str, ToolArg]


class AgentSpec(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(pattern=r"^[a-z][a-z0-9_]*$")
    charter: str = Field(min_length=1)
    route: str = Field(min_length=1)
    tools: dict[str, ToolSpec] = Field(min_length=1)
    confirm_words: list[str]
    cancel_words: list[str]

    @field_validator("tools")
    @classmethod
    def _known(cls, v: dict) -> dict:
        unknown = sorted(set(v) - KNOWN_TOOLS)
        if unknown:
            raise ValueError(f"tool(s) {unknown} are not implemented by the voice module")
        return v

    @field_validator("confirm_words")
    @classmethod
    def _yes(cls, v: list[str]) -> list[str]:
        if v != ["yes"]:
            raise ValueError("confirm_words must be exactly ['yes'] until a measurement widens it (FINAL [F-08])")
        return v

    @field_validator("cancel_words")
    @classmethod
    def _no(cls, v: list[str]) -> list[str]:
        if v != ["no"]:
            raise ValueError("cancel_words must be exactly ['no'] until a measurement widens it (FINAL [F-08])")
        return v


def load_agent(path: Path = CONFIG_PATH) -> AgentSpec:
    path = Path(path)
    if not path.exists():
        raise AgentConfigError(f"voice agent registry not found: {path}")
    try:
        raw = yaml.safe_load(path.read_text())
    except yaml.YAMLError as e:
        raise AgentConfigError(f"{path}: YAML error: {e}") from None
    if not isinstance(raw, dict) or not isinstance(raw.get("agent"), dict):
        raise AgentConfigError(f"{path}: expected an 'agent' mapping")
    try:
        spec = AgentSpec(**raw["agent"])
    except ValidationError as e:
        raise AgentConfigError(f"{path}: invalid voice agent entry:\n{e}") from None
    from cobalt.modelaccess import load_routes

    routes = load_routes().routes
    if spec.route not in routes:
        raise AgentConfigError(
            f"{path}: route {spec.route!r} is not a route name in configs/cobalt/modelaccess.yaml "
            f"({sorted(routes)}) — the agent names a ROUTE, never a provider, a model or a URL"
        )
    return spec


__all__ = ["ARG_TYPES", "AgentConfigError", "AgentSpec", "CONFIG_PATH", "KNOWN_TOOLS",
           "ToolArg", "ToolSpec", "load_agent"]
