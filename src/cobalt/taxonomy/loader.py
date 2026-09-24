"""Engine-side taxonomy config: defaults, tunables, and the `cfg()`
resolver — config-as-code (TRIAGE cross-cutting law).

WHAT LIVES HERE AFTER ADR-0008. The SYSTEM side of the taxonomy:
`configs/cobalt/taxonomy/defaults.yaml` and `tunables.yaml`, both of them
engine data that ships identically to every Cobalt install. Pydantic-
validated on load; a bad or missing file crashes with the path and the
field detail — no partial loads, no default fallback.

WHAT LEFT. The repo-side trade_def loader, the setup-matrix loader and
the variable-registry loader are GONE, with the three config families
behind them (ADR-0008 D3). A trade_def is USER data and its one home is
the strategy note in `1 - Trading/4 - Strategies/` — read by
`taxonomy/vault_loader.py`, loaded into `"user".trade_defs`. There is no
second loader and no repo copy to disagree with the vault; the setup x
trade matrix is a VIEW over the defs' own `valid_setups[]`, and each
trade's variable registry folded into `quality_factors[]` itself.

TUNABLES ARE NOW TWO SETS, AND THEY ARE UNIONED HERE. Engine rows stay in
`tunables.yaml`; a trader's per-trade rows live in their strategy note's
`tunables:<slug>` unit and load into `"user".tunables`. `merge_tunables`
is the union and it is loud in both directions: a user row that shadows
an engine key is a collision, not an override.

`configs/cobalt/` is a sanctioned new-core config location (CLAUDE.md's
config boundary law; see also `archiver/config.py`'s watchlists loader).
"""

from __future__ import annotations

import re
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, ValidationError

from .defaults import TaxonomyDefaults
from .trade_def import StopBuffer, Tunable
from .tunables import TunableRegistry, TunableRow

REPO_ROOT = Path(__file__).resolve().parents[3]
TAXONOMY_DIR = REPO_ROOT / "configs" / "cobalt" / "taxonomy"
DEFAULTS_PATH = TAXONOMY_DIR / "defaults.yaml"
TUNABLES_PATH = TAXONOMY_DIR / "tunables.yaml"

#: The one synthetic strategy note the repo ships (ADR-0008 D3). Anatomy
#: terms only — no trade name, no sheet rule. It is the loader's test
#: fixture AND the worked example behind
#: `docs/40 - DevDocs/taxonomy-authoring-a-trade-def.md`.
EXAMPLE_NOTE_PATH = TAXONOMY_DIR / "examples" / "example_trade_def.md"

_MA_REF_PATTERN = re.compile(r"^ma\.(fast|slow)$")
_CFG_TOKEN_PATTERN = re.compile(r"cfg\(([a-zA-Z0-9_.]+)\)")  # v0.7 §13.1 grammar atom


class TaxonomyConfigError(RuntimeError):
    """Taxonomy config missing or invalid — crash loudly."""


def load_defaults(path: Path = DEFAULTS_PATH) -> TaxonomyDefaults:
    if not path.exists():
        raise TaxonomyConfigError(f"defaults.yaml not found: {path}")
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict):
        raise TaxonomyConfigError(
            f"{path}: expected a YAML mapping, got {type(raw).__name__}"
        )
    try:
        return TaxonomyDefaults(**raw)
    except ValidationError as e:
        raise TaxonomyConfigError(f"{path}: invalid defaults:\n{e}") from e


def load_tunables(path: Path = TUNABLES_PATH) -> TunableRegistry:
    if not path.exists():
        raise TaxonomyConfigError(f"tunables.yaml not found: {path}")
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict):
        raise TaxonomyConfigError(
            f"{path}: expected a YAML mapping, got {type(raw).__name__}"
        )
    try:
        return TunableRegistry(**raw)
    except ValidationError as e:
        raise TaxonomyConfigError(f"{path}: invalid tunables registry:\n{e}") from e


def merge_tunables(
    engine: dict[str, TunableRow], user: dict[str, TunableRow]
) -> dict[str, TunableRow]:
    """Engine rows ∪ user rows, with a collision made LOUD (ADR-0008 D3).

    A user row whose key already exists in `tunables.yaml` is refused
    rather than allowed to shadow it. Shadowing sounds convenient and is
    exactly the failure the split exists to prevent: the engine row is
    what every Cobalt install runs on, and a trader's note quietly
    replacing one would mean two installs computing different answers
    from configs that both look right. If a trader needs a different
    value for an engine key, that is a ruling on the engine row, not a
    private copy of it.
    """
    collisions = sorted(set(engine) & set(user))
    if collisions:
        raise TaxonomyConfigError(
            f"user tunable row(s) {collisions} shadow engine keys in "
            f"{TUNABLES_PATH.name}. A per-trade row in a strategy note may only "
            "ADD keys (scope per_trade(...)), never redefine an engine key — "
            "change the engine row if the value is wrong."
        )
    return {**engine, **user}


def resolve_cfg(
    key: str, tunables: dict[str, TunableRow], defaults: TaxonomyDefaults
) -> Any:
    """The ONE `cfg(key)` resolver (v0.7 §13.1).

    `tunables` is the UNION of the engine rows and the trader's own rows
    (`merge_tunables`) — the resolver does not care which side a key came
    from, only that exactly one side defined it. Then defaults.yaml's two
    non-dynamic globals, else fail loud. Never silently falls back to a
    made-up value.
    """
    row = tunables.get(key)
    if row is not None:
        return row.value
    if key == "working_timeframe":
        return defaults.working_timeframe
    if is_ma_ref(key):
        return resolve_ma_ref(key, defaults)
    raise TaxonomyConfigError(
        f"cfg({key}) has no row in tunables.yaml, no row in the vault's "
        "per-trade tunables units, and no defaults.yaml fallback"
    )


def iter_cfg_tokens(obj: Any) -> Iterator[str]:
    """Token-scan (not parsing) every string reachable from `obj` for
    `cfg(<key>)` atoms — used to fail loud on an unknown key at load
    time (v0.7 §13.1)."""
    if isinstance(obj, str):
        yield from _CFG_TOKEN_PATTERN.findall(obj)
    elif isinstance(obj, BaseModel):
        for field_name in type(obj).model_fields:
            yield from iter_cfg_tokens(getattr(obj, field_name))
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            yield from iter_cfg_tokens(item)
    elif isinstance(obj, dict):
        for item in obj.values():
            yield from iter_cfg_tokens(item)


def resolve_ma_ref(value: str, defaults: TaxonomyDefaults) -> int:
    """Resolve an `ma.fast` / `ma.slow` ref string (A.8 MA-period note)
    against `defaults.yaml`. Any other string is not an `ma.*` ref —
    callers should check `is_ma_ref` first."""
    match = _MA_REF_PATTERN.match(value)
    if not match:
        raise TaxonomyConfigError(f"not an 'ma.*' ref: {value!r}")
    return getattr(defaults.ma, match.group(1))


def is_ma_ref(value: str) -> bool:
    return bool(_MA_REF_PATTERN.match(value))


def iter_tunables(obj: Any) -> Iterator[Tunable]:
    """Walk a TradeDef (or any nested Pydantic/list/dict structure) and
    yield every Tunable found. Used by the CLI table and by the
    dynamic-tunables-in-backlog test — no engine semantics, just
    introspection."""
    if isinstance(obj, Tunable):
        yield obj
    elif isinstance(obj, BaseModel):
        for field_name in type(obj).model_fields:
            yield from iter_tunables(getattr(obj, field_name))
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            yield from iter_tunables(item)
    elif isinstance(obj, dict):
        for item in obj.values():
            yield from iter_tunables(item)


def iter_stop_buffers(obj: Any) -> Iterator[StopBuffer]:
    """Walk a TradeDef and yield every StopBuffer found — introspection
    helper (CLI table, tests). The A.6 PROPOSAL flag (sheet_value !=
    value) now lives on the tunable row itself (ruling 09-03:
    stop.buffer is a tunable, not a Pydantic constant) — visible via
    `load_tunables()`, not a load-time warning here."""
    if isinstance(obj, StopBuffer):
        yield obj
    elif isinstance(obj, BaseModel):
        for field_name in type(obj).model_fields:
            yield from iter_stop_buffers(getattr(obj, field_name))
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            yield from iter_stop_buffers(item)
    elif isinstance(obj, dict):
        for item in obj.values():
            yield from iter_stop_buffers(item)


__all__ = [
    "DEFAULTS_PATH",
    "EXAMPLE_NOTE_PATH",
    "TAXONOMY_DIR",
    "TUNABLES_PATH",
    "TaxonomyConfigError",
    "is_ma_ref",
    "iter_cfg_tokens",
    "iter_stop_buffers",
    "iter_tunables",
    "load_defaults",
    "load_tunables",
    "merge_tunables",
    "resolve_cfg",
    "resolve_ma_ref",
]
