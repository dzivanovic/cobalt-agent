"""Taxonomy-wide defaults — `configs/cobalt/taxonomy/defaults.yaml`
(TRADE-DEFS-BATCH2-v0_1.md §A.9, §A.8 MA-period note). Config-as-code,
same fail-loud convention as the rest of `src/cobalt/taxonomy/`: no
predicate parsing, no engine semantics — just the two knobs Batch 2's
trade_defs reference (`working_timeframe`, `ma.fast`/`ma.slow`).
"""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class MaDefaults(BaseModel):
    model_config = ConfigDict(extra="forbid")

    fast: int = Field(gt=0)
    slow: int = Field(gt=0)


class TaxonomyDefaults(BaseModel):
    model_config = ConfigDict(extra="forbid")

    working_timeframe: str = Field(min_length=1)
    ma: MaDefaults
