"""Strict source-note and pool-decision models."""

from __future__ import annotations

import re
from datetime import date, datetime
from enum import Enum
from typing import Annotated, List, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from cobalt.archiver.models import Interval

FILTER_RE = re.compile(r"^[a-z0-9_.]+(?:,[a-z0-9_.]+)*$")
SORT_RE = re.compile(r"^-?[a-z0-9_]+$")
KEY_RE = re.compile(r"^[a-z0-9_]+$")


def _valid_hhmm(value: str) -> str:
    try:
        hour_s, minute_s = value.split(":", 1)
        hour, minute = int(hour_s), int(minute_s)
    except (ValueError, AttributeError) as e:
        raise ValueError("must be quoted HH:MM") from e
    if len(value) != 5 or not 0 <= hour <= 23 or not 0 <= minute <= 59:
        raise ValueError("must be quoted HH:MM")
    return value


class ScreenBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")

    screen: str = Field(pattern=r"^[a-z0-9_]+$")
    f: str
    sort: str
    columns: list[Annotated[int, Field(ge=0, le=150)]] = Field(min_length=1)
    active_from: str
    active_to: str
    enabled: bool
    ft: int | None = Field(default=None, ge=0, le=99)

    @field_validator("f")
    @classmethod
    def _filter(cls, value: str) -> str:
        if not FILTER_RE.fullmatch(value) or any(x in value for x in ("%", "&", "=", "auth")):
            raise ValueError("must be comma-separated Finviz filter codes; %, &, = and auth are refused")
        return value

    @field_validator("sort")
    @classmethod
    def _sort(cls, value: str) -> str:
        if not SORT_RE.fullmatch(value):
            raise ValueError("must match ^-?[a-z0-9_]+$")
        return value

    @field_validator("active_from", "active_to")
    @classmethod
    def _time(cls, value: str) -> str:
        return _valid_hhmm(value)

    @model_validator(mode="after")
    def _window(self) -> "ScreenBlock":
        if self.active_from >= self.active_to:
            raise ValueError("active_from must be before active_to")
        if len(set(self.columns)) != len(self.columns):
            raise ValueError("columns must be unique")
        return self


class PoolOverride(BaseModel):
    model_config = ConfigDict(extra="forbid")
    rank_metric: Literal["volume", "rvol"] | None = None
    first_from: str | None = None

    @field_validator("first_from")
    @classmethod
    def _time(cls, value: str | None) -> str | None:
        return None if value is None else _valid_hhmm(value)

    @model_validator(mode="after")
    def _nonempty(self) -> "PoolOverride":
        if self.rank_metric is None and self.first_from is None:
            raise ValueError("override must set rank_metric or first_from")
        return self


class RankMetric(BaseModel):
    model_config = ConfigDict(extra="forbid")
    premarket: Literal["volume", "rvol"]
    rth: Literal["volume", "rvol"]
    aftermarket: Literal["volume", "rvol"]


class PoolBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")

    kind: Literal["pool"]
    cap: int = Field(ge=1)
    priority: list[Literal["screens", "lists"]]
    rank_metric: RankMetric
    overrides: dict[str, PoolOverride]
    stickiness_scans: int = Field(ge=0)

    @model_validator(mode="after")
    def _priority(self) -> "PoolBlock":
        if self.priority != list(dict.fromkeys(self.priority)) or set(self.priority) != {"screens", "lists"}:
            raise ValueError("priority must be a permutation of [screens, lists]")
        first = [key for key, value in self.overrides.items() if value.first_from is not None]
        if len(first) > 1:
            raise ValueError(f"at most one override may set first_from; got {first}")
        return self


class ListBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")

    list: str = Field(pattern=r"^[a-z0-9_]+$")
    description: str = Field(min_length=1)
    # ``list`` is a contract field above, so use typing.List below it.  On
    # Python 3.14 the class-local FieldInfo otherwise shadows the builtin
    # while Pydantic resolves annotations.
    tickers: List[str] = Field(min_length=1)
    radar: bool
    archive: List[Interval]
    backfill_default: bool
    enabled: bool

    @field_validator("tickers")
    @classmethod
    def _tickers(cls, values: List[str]) -> List[str]:
        if len(values) != len(set(values)):
            raise ValueError("tickers must be unique")
        bad = [value for value in values if not re.fullmatch(r"[A-Z][A-Z0-9.-]{0,11}", value)]
        if bad:
            raise ValueError(f"invalid uppercase ticker(s): {bad}")
        return values

    @model_validator(mode="after")
    def _archive_unique(self) -> "ListBlock":
        if len(self.archive) != len(set(self.archive)):
            raise ValueError("archive intervals must be unique")
        return self


class ExcludeBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")
    kind: Literal["exclude"]
    tickers: list[str]

    @field_validator("tickers")
    @classmethod
    def _tickers(cls, values: list[str]) -> list[str]:
        if len(values) != len(set(values)):
            raise ValueError("exclude tickers must be unique")
        return values


class ExcludedBy(str, Enum):
    CONFIG_CAP = "config_cap"
    NOT_EQUITY = "not_equity"
    SCREEN_INACTIVE = "screen_inactive"
    MANUAL = "manual"


class SourceHealth(str, Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    INACTIVE = "inactive"


class SourceSet(BaseModel):
    model_config = ConfigDict(extra="forbid")
    source: str
    kind: Literal["screen", "list"]
    health: SourceHealth = SourceHealth.HEALTHY
    tickers: list[str] = Field(default_factory=list)
    note_order: int = 0
    ranks: dict[str, int] = Field(default_factory=dict)
    metrics: dict[str, dict[str, float | None]] = Field(default_factory=dict)
    active: bool = True


class Candidate(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ticker: str
    sources: list[str]
    excluded_by: ExcludedBy | None = None


class OpenMember(BaseModel):
    model_config = ConfigDict(extra="forbid")
    ticker: str
    sources: list[str]
    entered_at: datetime | None
    below_cap_streak: int = Field(ge=0)
    last_rank: int | None = None
    trade_date: date | str | None = None


__all__ = [
    "Candidate", "ExcludeBlock", "ExcludedBy", "ListBlock", "OpenMember",
    "PoolBlock", "PoolOverride", "RankMetric", "ScreenBlock", "SourceHealth",
    "SourceSet",
]
