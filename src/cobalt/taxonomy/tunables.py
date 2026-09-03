"""Tunable registry schema — TAXONOMY-DRAFT-v0_7.md §13.1,
`configs/cobalt/taxonomy/tunables.yaml`.

Every `config, dynamic` quantity named by the §0 "Dynamic definitions"
law is a row here, referenced from predicate/param strings by key via
the `cfg(key)` grammar atom (loader.py's `iter_cfg_tokens` /
`resolve_cfg`). Two NON-dynamic globals (`working_timeframe`,
`ma.fast`/`ma.slow`) are deliberately NOT rows here — they stay in
`defaults.yaml` (`defaults.py`'s `TaxonomyDefaults`) per §13.1's own
instruction not to duplicate them; `resolve_cfg` falls back to
`defaults.yaml` for those. `stop.buffer` IS a row here (ruling 09-03,
superseding ADR-0003's original exclusion): it is a tunable, never a
Pydantic literal — `trade_def.py`'s `StopBuffer.cents` resolves it via
`cfg(stop.buffer)`, with per-trade override rows
(`<trade_id>.stop.buffer`) taking precedence for the trades that
reference them directly.

No engine semantics: this module is schema + a pure `dynamic and status
!= solidified` query (`replay_backlog`). Replay writes `status`, never
`value` — that stays a Dejan ruling (§0, §13.1 rules).
"""

from __future__ import annotations

import re
from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator


class TunableUnit(str, Enum):
    BARS = "bars"
    MIN = "min"
    ATR = "atr"
    CENTS = "cents"
    COUNT = "count"
    PCT = "pct"
    RATIO = "ratio"
    LABEL = "label"
    DURATION = "duration"


class TunableStatus(str, Enum):
    PROPOSED = "proposed"
    REPLAY_PENDING = "replay_pending"
    SOLIDIFIED = "solidified"
    OVERRIDDEN = "overridden"


class TunableSource(str, Enum):
    RULING = "ruling"
    SHEET = "sheet"
    DWV = "dwv"


_SCOPE_PATTERN = re.compile(
    r"^(global|per_trade\([a-z0-9_]+\)|per_indicator\([a-z0-9_.]+\))$"
)


class ReplayRecord(BaseModel):
    """§13.1 row shape's `replay?: {corpus_ref, result, date}` — written by
    a future replay session, never by this loader."""

    model_config = ConfigDict(extra="forbid")

    corpus_ref: str = Field(min_length=1)
    result: str = Field(min_length=1)
    date: str = Field(min_length=1)


class TunableRow(BaseModel):
    model_config = ConfigDict(extra="forbid")

    key: str = Field(min_length=1)
    value: Any = None
    unit: TunableUnit
    scope: str
    dynamic: bool
    status: TunableStatus
    source: TunableSource
    sheet_value: Any | None = None
    consumers: list[str] = Field(default_factory=list)
    replay: ReplayRecord | None = None

    @field_validator("scope")
    @classmethod
    def _scope_shape(cls, v: str) -> str:
        if not _SCOPE_PATTERN.match(v):
            raise ValueError(
                f"tunable scope must be global | per_trade(<id>) | "
                f"per_indicator(<ind>), got {v!r}"
            )
        return v


class TunableRegistry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    tunables: list[TunableRow] = Field(min_length=1)

    @model_validator(mode="after")
    def _unique_keys(self) -> TunableRegistry:
        keys = [t.key for t in self.tunables]
        dupes = {k for k in keys if keys.count(k) > 1}
        if dupes:
            raise ValueError(f"duplicate tunable keys in tunables.yaml: {sorted(dupes)}")
        return self

    @property
    def by_key(self) -> dict[str, TunableRow]:
        return {t.key: t for t in self.tunables}


def replay_backlog(registry: TunableRegistry) -> list[TunableRow]:
    """§13's replay backlog as a query, not a hand-maintained list
    (v0.7 change log #19): every row with `dynamic=True` and
    `status != solidified`."""
    return [
        row
        for row in registry.tunables
        if row.dynamic and row.status != TunableStatus.SOLIDIFIED
    ]
