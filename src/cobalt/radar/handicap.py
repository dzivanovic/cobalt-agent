"""The float / market-cap handicap's pure functions (FLOAT-HANDICAP-v3,
H1): the ONE group verdict (v3 §3 [F-10]).

Nothing here sorts. Thresholds, factor, combinator and the missing rule
are HIS keys, read from `HandicapBlock`; no value of his is written here
(L32, L53).
"""

from __future__ import annotations

from collections.abc import Mapping
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict

from .models import HandicapBlock

Verdict = Literal["yes", "no", "unknown"]


class GroupVerdict(BaseModel):
    """`in_group` is `yes`, `no` or `unknown` — blank, `-` and unparseable
    are `unknown`, never a silent `no` (L1, [F-10])."""

    model_config = ConfigDict(extra="forbid")
    in_group: Verdict
    float_m: Decimal | None
    market_cap_m: Decimal | None
    reason: str


def _decimal(value: float | None) -> Decimal | None:
    """The parsed export number as the stored digits (through `str`, as
    `pool._as_decimal` stores `rank_value`), never a binary expansion."""
    return None if value is None else Decimal(str(value))


def handicap_group(metrics_row: Mapping[str, float | None] | None, block: HandicapBlock) -> GroupVerdict:
    """The ONE place a name's group verdict is decided (L3), shaped like
    `config.is_not_equity`.

    `metrics_row` is the name's `SourceSet.metrics` row from the source that
    ranked it (`float_m` / `market_cap_m`, parsed by `runner._number` from
    `export.handicap_headers`). The tests are strict `<` ("below").

    `any`: `yes` when at least one known value meets its threshold; `no`
    when both are known and none meets; `unknown` when a blank could still
    change the result. `all`: `yes` only when both are known and both meet;
    `no` when both are known and one fails; `unknown` when either is blank.
    """
    row = metrics_row or {}
    float_m = _decimal(row.get("float_m"))
    cap_m = _decimal(row.get("market_cap_m"))
    float_hit = None if float_m is None else float_m < block.float_below_m
    cap_hit = None if cap_m is None else cap_m < block.market_cap_below_m
    blank = " and ".join(name for name, value in (("float", float_m), ("cap", cap_m)) if value is None)
    met = " and ".join(name for name, hit in (("float", float_hit), ("cap", cap_hit)) if hit)

    if block.combinator == "any":
        if float_hit or cap_hit:
            verdict, reason = "yes", met
        elif float_hit is False and cap_hit is False:
            verdict, reason = "no", "neither"
        else:
            verdict, reason = "unknown", f"blank {blank}"
    elif float_hit is None or cap_hit is None:
        verdict, reason = "unknown", f"blank {blank}"
    elif float_hit and cap_hit:
        verdict, reason = "yes", met
    else:
        verdict, reason = "no", "neither"
    return GroupVerdict(in_group=verdict, float_m=float_m, market_cap_m=cap_m, reason=reason)


__all__ = ["GroupVerdict", "Verdict", "handicap_group"]
