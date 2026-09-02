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

from collections.abc import Iterator
from pathlib import Path
from typing import Any

import yaml
from pydantic import BaseModel, ValidationError

from .trade_def import TradeDef, Tunable
from .variables import VariableRegistry

REPO_ROOT = Path(__file__).resolve().parents[3]
TAXONOMY_DIR = REPO_ROOT / "configs" / "cobalt" / "taxonomy"
TRADE_DEFS_DIR = TAXONOMY_DIR / "trade_defs"
VARIABLES_DIR = TAXONOMY_DIR / "variables"
CAMERON_GRID_PATH = TAXONOMY_DIR / "cameron_grid.yaml"


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
