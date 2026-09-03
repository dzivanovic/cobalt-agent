"""trade_def / variable-registry loader — config-as-code (TRIAGE
cross-cutting law). Single source per trade: `configs/cobalt/taxonomy/
trade_defs/<id>.yaml` + `configs/cobalt/taxonomy/variables/<id>.yaml`,
cross-checked against `configs/cobalt/taxonomy/cameron_grid.yaml`.

Pydantic-validated on load; a bad or missing file crashes with the file
path and field detail — no partial loads, no default fallback.
`configs/cobalt/` is a sanctioned new-core config location (CLAUDE.md's
config boundary law; see also `archiver/config.py`'s watchlists loader).
"""

from __future__ import annotations

import re
import warnings
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, ValidationError

from .defaults import TaxonomyDefaults
from .trade_def import StopBuffer, TradeDef, Tunable
from .tunables import TunableRegistry, TunableRow
from .variables import VariableRegistry

REPO_ROOT = Path(__file__).resolve().parents[3]
TAXONOMY_DIR = REPO_ROOT / "configs" / "cobalt" / "taxonomy"
TRADE_DEFS_DIR = TAXONOMY_DIR / "trade_defs"
VARIABLES_DIR = TAXONOMY_DIR / "variables"
CAMERON_GRID_PATH = TAXONOMY_DIR / "cameron_grid.yaml"
DEFAULTS_PATH = TAXONOMY_DIR / "defaults.yaml"
TUNABLES_PATH = TAXONOMY_DIR / "tunables.yaml"

DEFAULT_STOP_BUFFER_CENTS = 0.02  # v0.6 §14 ruling 3 / A.6 flag law
_MA_REF_PATTERN = re.compile(r"^ma\.(fast|slow)$")
_CFG_TOKEN_PATTERN = re.compile(r"cfg\(([a-zA-Z0-9_.]+)\)")  # v0.7 §13.1 grammar atom


class TaxonomyConfigError(RuntimeError):
    """Trade-def / variable-registry config missing or invalid — crash loudly."""


def load_cameron_grid(
    path: Path = CAMERON_GRID_PATH,
) -> dict[str, list[dict[str, str]]]:
    if not path.exists():
        raise TaxonomyConfigError(f"cameron_grid.yaml not found: {path}")
    raw = yaml.safe_load(path.read_text())
    if not isinstance(raw, dict) or not isinstance(raw.get("valid_setups"), dict):
        raise TaxonomyConfigError(
            f"{path}: expected a top-level 'valid_setups' mapping"
        )
    grid = raw["valid_setups"]
    for trade_id, rows in grid.items():
        if not isinstance(rows, list) or not rows:
            raise TaxonomyConfigError(
                f"{path}: valid_setups.{trade_id} must be a non-empty list"
            )
        for row in rows:
            if (
                not isinstance(row, dict)
                or "setup_ref" not in row
                or "relation" not in row
            ):
                raise TaxonomyConfigError(
                    f"{path}: valid_setups.{trade_id} rows must each have setup_ref + relation, got {row!r}"
                )
    return grid


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


def resolve_cfg(
    key: str, tunables: dict[str, TunableRow], defaults: TaxonomyDefaults
) -> Any:
    """The ONE `cfg(key)` resolver (v0.7 §13.1): tunables.yaml first,
    then defaults.yaml's non-dynamic globals, else fail loud. Never
    silently falls back to a made-up value."""
    row = tunables.get(key)
    if row is not None:
        return row.value
    if key == "working_timeframe":
        return defaults.working_timeframe
    if is_ma_ref(key):
        return resolve_ma_ref(key, defaults)
    raise TaxonomyConfigError(
        f"cfg({key}) has no row in tunables.yaml and no defaults.yaml fallback"
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


def load_variable_registry(
    trade_id: str, directory: Path = VARIABLES_DIR
) -> VariableRegistry:
    file = directory / f"{trade_id}.yaml"
    if not file.exists():
        raise TaxonomyConfigError(
            f"variable registry not found for trade_id={trade_id!r}: {file}"
        )
    raw = yaml.safe_load(file.read_text())
    if not isinstance(raw, dict):
        raise TaxonomyConfigError(
            f"{file}: expected a YAML mapping, got {type(raw).__name__}"
        )
    try:
        return VariableRegistry(**raw)
    except ValidationError as e:
        raise TaxonomyConfigError(f"{file}: invalid variable registry:\n{e}") from e


def load_trade_defs(
    trade_defs_dir: Path = TRADE_DEFS_DIR,
    variables_dir: Path = VARIABLES_DIR,
    cameron_grid_path: Path = CAMERON_GRID_PATH,
) -> dict[str, TradeDef]:
    """Load + validate every trade_def, cross-checked against the Cameron
    H grid and each trade's variable registry. Fails loud on the first
    error — no partial loads."""
    if not trade_defs_dir.exists() or not trade_defs_dir.is_dir():
        raise TaxonomyConfigError(f"trade_defs directory not found: {trade_defs_dir}")

    grid = load_cameron_grid(cameron_grid_path)
    defaults = load_defaults()
    tunables = load_tunables().by_key
    result: dict[str, TradeDef] = {}

    for file in sorted(trade_defs_dir.glob("*.yaml")):
        raw = yaml.safe_load(file.read_text())
        if not isinstance(raw, dict) or "trade_def" not in raw:
            raise TaxonomyConfigError(
                f"{file}: expected a mapping with a top-level 'trade_def' key"
            )
        try:
            td = TradeDef(**raw["trade_def"])
        except ValidationError as e:
            raise TaxonomyConfigError(f"{file}: invalid trade_def:\n{e}") from e

        if td.id in result:
            raise TaxonomyConfigError(
                f"{file}: duplicate trade_def.id {td.id!r} (already loaded)"
            )

        grid_rows = grid.get(td.id)
        if grid_rows is None:
            raise TaxonomyConfigError(
                f"{file}: trade_def.id {td.id!r} has no row in {cameron_grid_path} — "
                "every trade's valid_setups[] must equal its Cameron H grid row"
            )
        expected = {(row["setup_ref"], row["relation"]) for row in grid_rows}
        actual = {(vs.setup_ref.value, vs.relation.value) for vs in td.valid_setups}
        if expected != actual:
            raise TaxonomyConfigError(
                f"{file}: valid_setups {sorted(actual)} does not match "
                f"{cameron_grid_path} row for {td.id!r}: {sorted(expected)}"
            )

        registry_file = variables_dir / f"{td.id}.yaml"
        registry = load_variable_registry(td.id, variables_dir)
        qf = set(td.quality_factors)
        missing_in_registry = qf - registry.names
        missing_in_quality_factors = registry.names - qf
        if missing_in_registry:
            raise TaxonomyConfigError(
                f"{file}: quality_factors not present in {registry_file}: {sorted(missing_in_registry)}"
            )
        if missing_in_quality_factors:
            raise TaxonomyConfigError(
                f"{registry_file}: variable(s) not referenced by {file}'s quality_factors: "
                f"{sorted(missing_in_quality_factors)}"
            )

        for tunable in iter_tunables(td):
            if isinstance(tunable.value, str) and is_ma_ref(tunable.value):
                resolve_ma_ref(tunable.value, defaults)  # fail-loud on an unknown ma.* key

        for cfg_key in iter_cfg_tokens(td):
            try:
                resolve_cfg(cfg_key, tunables, defaults)
            except TaxonomyConfigError as e:
                raise TaxonomyConfigError(f"{file}: trade_def {td.id!r}: {e}") from e

        for buf in iter_stop_buffers(td):
            if buf.cents.value != DEFAULT_STOP_BUFFER_CENTS:
                warnings.warn(
                    f"{file}: trade_def {td.id!r} stop buffer {buf.cents.value} "
                    f"differs from default {DEFAULT_STOP_BUFFER_CENTS} (A.6 flag law)",
                    stacklevel=2,
                )

        result[td.id] = td

    return result


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
    """Walk a TradeDef and yield every StopBuffer found — used by the A.6
    flag law (loader.load_trade_defs warns when a buffer differs from
    the 0.02 default)."""
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
