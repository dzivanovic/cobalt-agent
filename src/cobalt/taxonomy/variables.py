"""Variable registry schema — one stub file per trade_def, one entry per
`quality_factors[]` item (Batch 1 population task, 2026-09-02).

Stub only: `why_template` is empty and `status` is always "stub" until the
grading engine sprint fills these in. `loader.py` cross-checks that a
trade_def's `quality_factors[]` and its registry file name the same set.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class VariableRegistryEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    scale_min: int = 1
    scale_max: int = 10
    source: Literal["cobalt", "cobalt-degraded", "human"] = "human"
    tier: Literal["deterministic", "judgment"] = "judgment"
    why_template: str = ""
    status: str = "stub"
    # §12 tape-frontier flag: True for a human-only tape-class read that
    # flips to source: cobalt once an L2/T&S feed is ingested, no schema
    # change (TRADE-DEFS-BATCH2-v0_1.md).
    frontier: bool = False


class VariableRegistry(BaseModel):
    model_config = ConfigDict(extra="forbid")

    trade_id: str = Field(min_length=1)
    variables: list[VariableRegistryEntry] = Field(min_length=1)

    @model_validator(mode="after")
    def _unique_names(self) -> VariableRegistry:
        names = [v.name for v in self.variables]
        dupes = {n for n in names if names.count(n) > 1}
        if dupes:
            raise ValueError(
                f"{self.trade_id}: duplicate variable registry names: {sorted(dupes)}"
            )
        return self

    @property
    def names(self) -> set[str]:
        return {v.name for v in self.variables}
