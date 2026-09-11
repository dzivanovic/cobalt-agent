"""Strict engine-only radar configuration."""

from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from cobalt.taxonomy.loader import load_tunables
from cobalt.taxonomy.tunables import TunableUnit

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs/cobalt/radar.yaml"


class RadarConfigError(RuntimeError):
    """Missing or malformed engine config; no runtime defaults."""


class NotesConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    screens: str = Field(min_length=1)
    lists: str = Field(min_length=1)


class MetricHeaders(BaseModel):
    model_config = ConfigDict(extra="forbid")
    volume: str = Field(min_length=1)
    rvol: str = Field(min_length=1)


class ExportConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    v: int
    columns: str = Field(pattern=r"^0-150$")
    required_headers: list[str] = Field(min_length=1)
    metric_headers: MetricHeaders


class NotEquityConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    header: str = Field(min_length=1)
    values: list[str] = Field(min_length=1)


class CacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    dir: str = Field(pattern=r"^data/[a-z0-9_/-]+$")
    retention_days: int = Field(gt=0)


class RadarConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    pool_key: str = Field(pattern=r"^[a-z0-9_]+$")
    notes: NotesConfig
    export: ExportConfig
    list_chunk_size: int = Field(gt=0)
    not_equity: NotEquityConfig
    cache: CacheConfig


def load_config(path: Path = CONFIG_PATH) -> RadarConfig:
    if not path.exists():
        raise RadarConfigError(f"radar config not found: {path}")
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as e:
        raise RadarConfigError(f"{path}: cannot read radar config: {e}") from e
    if not isinstance(raw, dict):
        raise RadarConfigError(f"{path}: expected a YAML mapping")
    try:
        config = RadarConfig(**raw)
    except ValidationError as e:
        raise RadarConfigError(f"{path}: invalid radar config:\n{e}") from e
    needed = {
        config.export.metric_headers.volume,
        config.export.metric_headers.rvol,
        config.not_equity.header,
        "Ticker",
    }
    missing = sorted(needed - set(config.export.required_headers))
    if missing:
        raise RadarConfigError(f"{path}: required_headers missing configured headers {missing}")
    return config


TUNABLE_UNITS = {
    "radar.scan_interval": TunableUnit.DURATION,
    "radar.poll_interval": TunableUnit.DURATION,
    "radar.poll_overlap_bars": TunableUnit.COUNT,
    "radar.finviz_max_rpm": TunableUnit.COUNT,
    "heartbeat.radar_max_age_s": TunableUnit.DURATION,
    "db.query.timeout_s": TunableUnit.DURATION,
}


def check() -> tuple[RadarConfig, dict[str, object]]:
    config = load_config()
    registry = load_tunables().by_key
    values: dict[str, object] = {}
    for key, unit in TUNABLE_UNITS.items():
        row = registry.get(key)
        if row is None:
            raise RadarConfigError(f"tunables.yaml: missing {key}")
        if row.unit is not unit:
            raise RadarConfigError(
                f"tunables.yaml: {key} has unit {row.unit.value}, expected {unit.value}"
            )
        values[key] = row.value
    return config, values


def command(_args) -> None:
    config, values = check()
    print(f"{CONFIG_PATH}: OK ({config.pool_key})")
    for key in TUNABLE_UNITS:
        print(f"{key} = {values[key]}")


__all__ = ["CONFIG_PATH", "RadarConfig", "RadarConfigError", "check", "load_config"]
