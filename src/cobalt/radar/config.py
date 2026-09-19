"""Strict engine-only radar configuration."""

from __future__ import annotations

import re
from collections.abc import Mapping
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

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


#: The two shapes a Finviz `c=` declaration takes: an inclusive `a-b`
#: range (radar.yaml's `export.columns`) or an explicit comma list (what
#: a screen note may declare instead).
_COLUMN_RANGE = re.compile(r"(\d+)-(\d+)")
_COLUMN_LIST = re.compile(r"\d+(?:,\d+)*")


def screener_columns(declaration: str) -> list[int]:
    """The ONE place a Finviz column index list is produced (L3).

    `"0-150"` -> 0..150 inclusive; `"1,2,3"` -> itself. Four modules used
    to build the 151-index list for themselves, which is one export shape
    per copy the day the declaration changes.

    The function tidies nothing: anything that is not one of the two
    shapes crashes (L1). A silently wrong column set does not fail — it
    returns a differently shaped export that every parser downstream
    reads as a header mismatch, far from the config line that caused it.
    Stripping backticks and whitespace off a trader's note is the note
    parser's job, not this one's.
    """
    matched = _COLUMN_RANGE.fullmatch(declaration)
    if matched:
        start, end = int(matched.group(1)), int(matched.group(2))
        if start > end:
            raise RadarConfigError(f"column declaration {declaration!r} runs backwards")
        return list(range(start, end + 1))
    if _COLUMN_LIST.fullmatch(declaration):
        return [int(index) for index in declaration.split(",")]
    raise RadarConfigError(
        f"column declaration {declaration!r} is neither an 'a-b' range nor a comma list of indices"
    )


def screener_columns_param(declaration: str) -> str:
    """A declaration rendered as the `c=` request parameter."""
    return ",".join(str(index) for index in screener_columns(declaration))


class NotEquityConfig(BaseModel):
    """R16 "C" (ruled 2026-09-19): not-equity is read from TWO columns.

    Neither one names a fund on its own. On the evidence run over the
    retained exports, every non-blank `Asset Type` sat on an ETF-industry
    row (0 stock rows hit) — but 8 distinct funds carried a BLANK `Asset
    Type` and were named by `Industry` alone. The old one-column shape
    (`header`/`values`) is a DIFFERENT rule, not a subset of this one, so
    it is refused by name rather than read for what it has (L10).
    """

    model_config = ConfigDict(extra="forbid")
    asset_type_header: str = Field(min_length=1)
    industry_header: str = Field(min_length=1)
    industry_values: list[str] = Field(min_length=1)


def is_not_equity(row: Mapping[str, Optional[str]], config: NotEquityConfig) -> bool:
    """The ONE place the not-equity rule is decided (L3).

    A row is not equity when its `Asset Type` cell is non-blank OR its
    `Industry` cell names a fund industry. Both the radar's candidate
    gather and the replay's mover benchmark call this; a second copy of
    the OR is how the two surfaces start disagreeing about what a fund
    is on the day the rule changes.

    Blank, whitespace-only, `None` and absent are the same thing here —
    Finviz leaves the `Asset Type` cell empty for an ordinary stock. An
    absent COLUMN never reaches this function: both headers are required
    of every export, so a missing column is a FAILED parse naming the
    header (L1), never a row that quietly reads as equity.
    """
    asset_type = (row.get(config.asset_type_header) or "").strip()
    industry = (row.get(config.industry_header) or "").strip()
    return bool(asset_type) or industry in config.industry_values


class CacheConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    dir: str = Field(pattern=r"^data/[a-z0-9_/-]+$")
    retention_days: int = Field(gt=0)


class ContextConfig(BaseModel):
    """Context tickers (market/sector ETFs) polled beside the pool for the
    alignment shadow dots (S2-P2 STEP-3/5). Required, so the total-demand
    check always counts them (L53); an explicit empty list is a declared
    zero, and the alignment dots then render CHECKPOINT_MISSING."""

    model_config = ConfigDict(extra="forbid")
    tickers: list[str]

    @field_validator("tickers")
    @classmethod
    def _tickers(cls, v: list[str]) -> list[str]:
        bad = [t for t in v if not re.fullmatch(r"[A-Z][A-Z0-9.]{0,9}", t)]
        if bad or len(set(v)) != len(v):
            raise ValueError(f"context tickers must be unique uppercase symbols, got {v}")
        return v


class RadarConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")
    pool_key: str = Field(pattern=r"^[a-z0-9_]+$")
    notes: NotesConfig
    export: ExportConfig
    list_chunk_size: int = Field(gt=0)
    not_equity: NotEquityConfig
    cache: CacheConfig
    context: ContextConfig


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
        config.not_equity.asset_type_header,
        config.not_equity.industry_header,
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
    "radar.poll_bar_max_age_s": TunableUnit.DURATION,
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


__all__ = [
    "CONFIG_PATH",
    "NotEquityConfig",
    "RadarConfig",
    "RadarConfigError",
    "check",
    "is_not_equity",
    "load_config",
    "screener_columns",
    "screener_columns_param",
]
