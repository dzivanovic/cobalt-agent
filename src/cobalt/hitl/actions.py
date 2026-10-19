"""The action catalog and `request_action` (F20 FINAL §3 steps 1-4; F-06 B, F-08, F-18; L40).

THE CATALOG IS TWO ACTIONS: `agents.create` and `agents.deactivate`, each
with one argument schema and one deterministic executor
(`hitl/executor.py`). Nothing else can be requested.

`request_action` NEVER APPROVES AND NEVER BLOCKS. It validates the action
and its arguments, refuses a secret-shaped argument
(`modelaccess.guard.refuse_if_secret_shaped`), renders the exact file bytes
B the page will show and the executor will write, stores sha256(B) and the
hash of a fresh 128-bit key, sends the card DM with the key in the link
fragment, and returns `pending <short_id>` to the model at once. A refusal
goes back to the model as text and writes no row.
"""

from __future__ import annotations

import hashlib
import json
import secrets
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Optional

from loguru import logger
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from cobalt.agents.registry import AGENTS_DIR, AgentRegistryError, load_entry, parse_entry, render_entry

from .models import ACTIONS

#: F16 / F-15: required; no house set a value (card DECISION 7).
TTL_KEY = "hitl.request_ttl_min"

#: F-08: never deactivated through a card — refused at request time.
PROTECTED_AGENTS = frozenset({"voice", "cos"})


class HitlRefused(ValueError):
    """The request is refused. The message goes back to the model."""


class CreateArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    yaml: str = Field(min_length=1)


class DeactivateArgs(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str = Field(pattern=r"^[a-z][a-z0-9_]*$")


ARG_SCHEMAS: dict[str, type[BaseModel]] = {
    "agents.create": CreateArgs,
    "agents.deactivate": DeactivateArgs,
}
assert tuple(ARG_SCHEMAS) == ACTIONS, "the catalog and its schemas disagree"


def request_ttl_min() -> int:
    """`hitl.request_ttl_min`; missing, non-integer or <= 0 raises (L1)."""
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(TTL_KEY)
    if row is None or row.value is None:
        raise RuntimeError(
            f"tunable {TTL_KEY!r} has no value in tunables.yaml — a HITL request needs a "
            "TTL and there is no built-in default (F-15, L1)."
        )
    if isinstance(row.value, bool) or not isinstance(row.value, int) or row.value <= 0:
        raise RuntimeError(f"tunable {TTL_KEY!r} must be a positive integer, got {row.value!r}")
    return row.value


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass(frozen=True)
class Prepared:
    action: str
    target: str
    payload: dict
    rendered: bytes
    sha256: str
    before_bytes: Optional[bytes]
    before_sha256: Optional[str]
    summary: str


def prepare(action: str, args: Any, *, agents_dir: Path = AGENTS_DIR) -> Prepared:
    """Validate and render one request. Raises `HitlRefused`; writes nothing."""
    schema = ARG_SCHEMAS.get(action)
    if schema is None:
        raise HitlRefused(f"unknown action {action!r}; the catalog is {list(ACTIONS)}")
    if not isinstance(args, dict):
        raise HitlRefused(f"{action}: args must be an object")
    try:
        parsed = schema(**args)
    except ValidationError as e:
        raise HitlRefused(f"{action}: bad args: {e.errors(include_url=False)}") from None

    agents_dir = Path(agents_dir)
    if action == "agents.create":
        try:
            entry = parse_entry(parsed.yaml, where="the drafted agent")
        except AgentRegistryError as e:
            raise HitlRefused(str(e)) from None
        if entry.id in PROTECTED_AGENTS:
            raise HitlRefused(f"agents.create: {entry.id!r} is a reserved agent id")
        rendered = render_entry(entry)
        return Prepared(
            action, entry.id, {"target": entry.id, "entry": entry.model_dump(exclude_none=True)},
            rendered, _sha(rendered), None, None,
            f"create agent {entry.id} (tools: {', '.join(entry.tools)})",
        )

    target = parsed.id
    if target in PROTECTED_AGENTS:
        raise HitlRefused(f"agents.deactivate: {target!r} is never deactivated through a card (F-08)")
    path = agents_dir / f"{target}.yaml"
    if not path.exists():
        raise HitlRefused(f"agents.deactivate: no registry entry {target!r}")
    before = path.read_bytes()
    try:
        entry = load_entry(path)
    except AgentRegistryError as e:
        raise HitlRefused(str(e)) from None
    if not entry.enabled:
        raise HitlRefused(f"agents.deactivate: {target!r} is already disabled")
    after = render_entry(entry.model_copy(update={"enabled": False}))
    return Prepared(
        action, target, {"target": target, "enabled": False}, after, _sha(after), before,
        _sha(before), f"deactivate agent {target}",
    )


def request_action(
    action: str,
    args: Any,
    reason: str,
    *,
    agent_id: str = "cos",
    store=None,
    agents_dir: Optional[Path] = None,
    send: Optional[Callable] = None,
) -> str:
    """The model's one way to ask. Returns `pending <short_id>` or `refused: …`."""
    from cobalt.modelaccess.guard import PromptRefused, refuse_if_secret_shaped

    try:
        refuse_if_secret_shaped(json.dumps({"args": args, "reason": reason}, sort_keys=True, default=str),
                                where="hitl.request_action")
        prepared = prepare(action, args, agents_dir=agents_dir or AGENTS_DIR)
        ttl = request_ttl_min()
    except PromptRefused as e:
        return f"refused: secret-shaped content ({', '.join(e.kinds)}); nothing written"
    except HitlRefused as e:
        return f"refused: {e}; nothing written"
    except Exception as e:  # noqa: BLE001 - a refusal is a tool result, never an exception
        return f"refused: {type(e).__name__}: {e}; nothing written"

    if store is None:
        from .store import HitlStore

        store = HitlStore()
    key = secrets.token_hex(16)
    row_id, short_id = store.insert(
        agent_id=agent_id, action=prepared.action, payload=prepared.payload,
        sha256=prepared.sha256, rendered=prepared.rendered, before_sha256=prepared.before_sha256,
        before_bytes=prepared.before_bytes, reason=reason or "", ttl_min=ttl,
        approve_key_sha256=_sha(key.encode()),
    )
    if send is None:
        from .card import send_card as send
    try:
        send(row_id, short_id, prepared, key)
    except Exception as e:  # noqa: BLE001 - the row stands; the missing card is said out loud
        logger.error("HITL {}: the card DM FAILED ({}: {}) — the request is pending with no card",
                     short_id, type(e).__name__, e)
        return f"pending {short_id} (the card DM failed: {type(e).__name__})"
    return f"pending {short_id}"


__all__ = [
    "ARG_SCHEMAS", "HitlRefused", "PROTECTED_AGENTS", "Prepared", "TTL_KEY",
    "prepare", "request_action", "request_ttl_min",
]
