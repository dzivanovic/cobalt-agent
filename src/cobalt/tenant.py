"""Which local trader this install serves — the `cobalt.trader_id` GUC.

Config-as-code (TRIAGE cross-cutting law): one committed file,
`configs/cobalt/tenant.yaml`, Pydantic-validated on load, crashing with
the path and the detail if it is missing or wrong. No default, no silent
fallback — a Cobalt that cannot say which trader it serves must not open
a connection that would then write rows nobody owns.

`configs/cobalt/` is a sanctioned new-core config location (CLAUDE.md's
config boundary law): the old loader's glob is `configs/*.yaml`,
top-level only, and never reaches this subdirectory.

The value is read once per process and cached: it is the identity of the
install, not a runtime knob, and re-reading it per connection would make
a mid-run edit change which trader the second half of a job writes as.
"""

from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

REPO_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "tenant.yaml"

#: The session GUC the factory sets and every user-side `user_id` column
#: defaults to. Written in exactly one place in Python and one place in
#: SQL (db_migrations/0002_move_tables.sql).
TRADER_GUC = "cobalt.trader_id"


class TenantConfigError(RuntimeError):
    """Tenant config missing or invalid — crash loudly."""


class TenantConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    #: `ge=1` because `"user".traders` is seeded at id 1 and identity
    #: columns start there: 0 or a negative id names no trader.
    trader_id: int = Field(ge=1)


_cached: Optional[TenantConfig] = None


def load_tenant_config(*, path: Optional[Path] = None, refresh: bool = False) -> TenantConfig:
    """The tenant config. `path`/`refresh` are the test seam only."""
    global _cached
    if path is None and _cached is not None and not refresh:
        return _cached

    target = path or CONFIG_PATH
    if not target.exists():
        raise TenantConfigError(
            f"Tenant config not found: {target}. It says which local trader this "
            "install serves (ADR-0008 D1) and there is no default — every "
            "user-side row is stamped with it."
        )
    raw = yaml.safe_load(target.read_text())
    if not isinstance(raw, dict):
        raise TenantConfigError(
            f"{target}: expected a YAML mapping, got {type(raw).__name__}"
        )
    try:
        cfg = TenantConfig(**raw)
    except ValidationError as e:
        raise TenantConfigError(f"{target}: invalid tenant config:\n{e}") from e

    if path is None:
        _cached = cfg
    return cfg


def trader_id() -> int:
    """The id every user-side write is stamped with on this install."""
    return load_tenant_config().trader_id


__all__ = [
    "CONFIG_PATH",
    "TRADER_GUC",
    "TenantConfig",
    "TenantConfigError",
    "load_tenant_config",
    "trader_id",
]
