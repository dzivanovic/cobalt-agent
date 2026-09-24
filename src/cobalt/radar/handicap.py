"""The float / market-cap handicap's pure functions (FLOAT-HANDICAP-v3,
H1): the ONE group verdict (v3 §3 [F-10]) and the shadow would-be rank
(his R26 "B", pool-wide).

Nothing here decides admission: the would-be rank is computed and stored,
never used to sort (shadow; L7). Thresholds, factor, combinator and the
missing rule are HIS keys, read from `HandicapBlock`; no value of his is
written here (L32, L53).
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from decimal import Decimal
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from .config import HandicapHeaders
from .models import HandicapBlock, SourceSet

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


#: The degraded reason when H1 code reads `mode: live` (`29` §6): H1 never
#: sorts on the handicap; the live division is H2's.
LIVE_NEEDS_H2 = "mode live needs H2 — ranking raw"


class HandicapRecord(BaseModel):
    """The membership row's `handicap` JSONB (v3 §6; `29` §2 under R26 B):
    exactly v3's ten keys. `decisive` is H2's and is NOT a key here.

    `position` is the name's `raw_rank` (the dividend); `effective_position`
    is the would-be POOL-WIDE rank — the 1-based place in the raw order
    re-sorted by `(Decimal(raw_rank) ÷ factor, handicapped, raw_rank)`. The
    quotient itself is not stored: it replays exactly as
    `Decimal(position) / handicap_factor` (L57)."""

    model_config = ConfigDict(extra="forbid")
    float_m: Decimal | None
    market_cap_m: Decimal | None
    verdict: Verdict
    reason: str
    missing_rule: Literal["apply", "skip"]
    mode: Literal["shadow", "live"]
    position: int = Field(ge=1)
    effective_position: int = Field(ge=1)
    source: str
    block_sha256: str


@dataclass(frozen=True)
class ShadowRank:
    """One scan's would-be rank: the factor and record per ranked name, and
    the degraded reason when the handicap is not operating as shadow."""

    factors: dict[str, Decimal]
    records: dict[str, HandicapRecord]
    degraded: str | None


def shadow_rank(
    ordered: Sequence[str],
    ranks: Mapping[str, int],
    source_for: Mapping[str, str],
    sources: Sequence[SourceSet],
    block: HandicapBlock,
    headers: HandicapHeaders,
) -> ShadowRank:
    """R26 B, computed and never used for admission: `eff = Decimal(raw) ÷
    factor`, re-sorted by `(eff, handicapped, raw)` — on an exact tie the
    unhandicapped name first (R57). `factor` is the block's for a name the
    verdict applies it to (`yes`, or `unknown` under `missing: apply`,
    R52), else 1. The group values come from the source that ranked the
    name (`source_for`)."""
    from .evaluate import canonical_sha256  # the one canonical JSON hash

    block_sha256 = canonical_sha256(block.model_dump(mode="json"))
    by_source = {source.source: source for source in sources}
    one = Decimal(1)
    factors: dict[str, Decimal] = {}
    applied: dict[str, bool] = {}
    verdicts: dict[str, GroupVerdict] = {}
    reasons: dict[str, str] = {}
    for ticker in ordered:
        source = by_source.get(source_for.get(ticker, ""))
        verdict = handicap_group(source.metrics.get(ticker) if source else None, block)
        verdicts[ticker] = verdict
        applies = verdict.in_group == "yes" or (verdict.in_group == "unknown" and block.missing == "apply")
        factors[ticker] = block.factor if applies else one
        applied[ticker] = applies
        reasons[ticker] = (
            f"{verdict.reason} — unknown → {'applied' if applies else 'not applied'}"
            if verdict.in_group == "unknown" else verdict.reason
        )
    effective = {ticker: Decimal(ranks[ticker]) / factors[ticker] for ticker in ordered}
    would_be = sorted(ordered, key=lambda t: (effective[t], applied[t], ranks[t]))
    position = {ticker: index + 1 for index, ticker in enumerate(would_be)}
    records = {
        ticker: HandicapRecord(
            float_m=verdicts[ticker].float_m,
            market_cap_m=verdicts[ticker].market_cap_m,
            verdict=verdicts[ticker].in_group,
            reason=reasons[ticker],
            missing_rule=block.missing,
            mode=block.mode,
            position=ranks[ticker],
            effective_position=position[ticker],
            source=source_for.get(ticker, ""),
            block_sha256=block_sha256,
        )
        for ticker in ordered
    }
    degraded = LIVE_NEEDS_H2 if block.mode == "live" else None
    return ShadowRank(factors=factors, records=records, degraded=degraded)


__all__ = [
    "GroupVerdict", "HandicapRecord", "LIVE_NEEDS_H2", "ShadowRank", "Verdict",
    "handicap_group", "shadow_rank",
]
