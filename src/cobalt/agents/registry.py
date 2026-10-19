"""The generic agent registry (F20 FINAL §2 `agents/registry.py`; L16, F-10, F-21).

One validated YAML file per agent under `configs/cobalt/agents/`:
`id`, `charter`, `chassis` (`{kind: sdk, auth: subscription, model}`),
`tools`, `schedule` (optional), `memory_namespace`, `enabled`.

TWO REFUSALS AT LOAD, the rule of `voice/registry.py:9-11`: a tool the code
catalog does not name, and a chassis `auth` that is not the subscription
login (R1112: no API key, no pay-per-token account anywhere). The registry
can narrow what an agent may do, never invent a capability.

`voice.yaml` keeps its own loader (`voice/registry.py:85`); this module
lists it by id and never re-validates it (one registry, F-21).

THE RENDERED BYTES. `render_entry` is the one canonical form of an entry:
the HITL card's sha256 is over these bytes, the page shows them, and the
executor writes them verbatim (F-18).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

REPO_ROOT = Path(__file__).resolve().parents[3]
AGENTS_DIR = REPO_ROOT / "configs" / "cobalt" / "agents"
#: Listed by id only; its schema and loader are `cobalt.voice.registry`.
VOICE_FILE = "voice.yaml"

#: The tools this code implements for a registry agent: the CoS tool server
#: (`cobalt.cos.tools`, which asserts it matches). No approve, decide or
#: execute verb is a tool (L37).
TOOL_CATALOG = frozenset({
    "cards.open", "radar.pool", "jobs.status", "hitl.list", "agents.list",
    "request_action", "draft_agent",
})


class AgentRegistryError(RuntimeError):
    """Missing / invalid agent registry entry — crash, never fall back."""


class Chassis(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kind: Literal["sdk"]
    #: R1112: subscription everywhere; `api_key` is refused at load.
    auth: Literal["subscription"]
    #: A model alias, a config value (C5: UNMEASURED start value, X17).
    model: str = Field(min_length=1)


class AgentEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(pattern=r"^[a-z][a-z0-9_]*$")
    charter: str = Field(min_length=1)
    chassis: Chassis
    tools: list[str] = Field(min_length=1)
    schedule: Optional[str] = None
    memory_namespace: str = Field(min_length=1)
    enabled: bool

    @field_validator("tools")
    @classmethod
    def _known(cls, v: list[str]) -> list[str]:
        unknown = sorted(set(v) - TOOL_CATALOG)
        if unknown:
            raise ValueError(f"tool(s) {unknown} are not in the code catalog {sorted(TOOL_CATALOG)}")
        if len(set(v)) != len(v):
            raise ValueError(f"a tool is listed twice: {v}")
        return v


def parse_entry(text: str, *, where: str) -> AgentEntry:
    """Validate one entry from its YAML text. `where` names it in the error."""
    try:
        raw = yaml.safe_load(text)
    except yaml.YAMLError as e:
        raise AgentRegistryError(f"{where}: YAML error: {e}") from None
    if not isinstance(raw, dict) or not isinstance(raw.get("agent"), dict) or set(raw) != {"agent"}:
        raise AgentRegistryError(f"{where}: expected exactly one top-level 'agent' mapping")
    try:
        return AgentEntry(**raw["agent"])
    except ValidationError as e:
        raise AgentRegistryError(f"{where}: invalid agent entry:\n{e}") from None


def load_entry(path: Path) -> AgentEntry:
    path = Path(path)
    if not path.exists():
        raise AgentRegistryError(f"agent registry entry not found: {path}")
    entry = parse_entry(path.read_text(), where=str(path))
    if entry.id != path.stem:
        raise AgentRegistryError(f"{path}: id {entry.id!r} does not match the file name")
    return entry


def render_entry(entry: AgentEntry) -> bytes:
    """The canonical file bytes of an entry (F-18): what the card hashes,
    the page shows and the executor writes."""
    body = entry.model_dump(exclude_none=True)
    return yaml.safe_dump({"agent": body}, sort_keys=False, allow_unicode=True,
                          default_flow_style=False).encode()


@dataclass(frozen=True)
class AgentListing:
    id: str
    path: Path
    enabled: Optional[bool]
    #: False for `voice.yaml`: listed, never re-validated here.
    validated: bool


def list_agents(agents_dir: Path = AGENTS_DIR) -> list[AgentListing]:
    """Every registry entry, by id. An invalid entry raises (L1)."""
    out = []
    for path in sorted(Path(agents_dir).glob("*.yaml")):
        if path.name == VOICE_FILE:
            raw = yaml.safe_load(path.read_text()) or {}
            agent_id = (raw.get("agent") or {}).get("id") if isinstance(raw, dict) else None
            if not agent_id:
                raise AgentRegistryError(f"{path}: no agent id")
            out.append(AgentListing(str(agent_id), path, None, False))
            continue
        entry = load_entry(path)
        out.append(AgentListing(entry.id, path, entry.enabled, True))
    return sorted(out, key=lambda a: a.id)


__all__ = [
    "AGENTS_DIR", "AgentEntry", "AgentListing", "AgentRegistryError", "Chassis",
    "TOOL_CATALOG", "VOICE_FILE", "list_agents", "load_entry", "parse_entry", "render_entry",
]
