"""`cobalt cards shadow-report [--since YYYY-MM-DD]` (S2-P2 STEP-10).

The evidence half of the shadow-mode promotion law (L7). Every computed
dot runs in SHADOW through S2 (R6): the engine grades it, the card shows
it hollow, and his tap is recorded next to the engine grade that was on
screen (`"user".card_dot_taps.engine_grade_at_tap`). This report reads
`"user".shadow_agreement_v` — one row per factor × ET trading day with
every |tap − engine| delta — and, per factor, compares

    sessions (trading days with ≥1 pair) ≥ bar.sessions
    pairs                                 ≥ bar.pairs
    median |Δ| over ALL pairs             ≤ bar.median_max
    share of pairs with |Δ| ≤ 2           ≥ bar.within2_min

against `card.shadow_promotion_bar` in `"user".trader_settings` (09-14
group-2 ruling: 10 / 30 / 1 / 0.90), printing GATE MET or GATE NOT MET
with the misses named.

IT NEVER FLIPS ANYTHING. A met gate is evidence for the curve tribunal
and the HITL decision, not the decision: this module reads one view and
one setting and prints. There is no write in it.

No bar loaded → refuse loud; the bar is his setting, never defaulted.
"""

from __future__ import annotations

import argparse
import statistics
from collections.abc import Iterable, Mapping
from datetime import date
from decimal import Decimal
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

from cobalt.settings.card import CardSettingsReader, ShadowPromotionBar

from .store import CardStore


class ShadowReportError(RuntimeError):
    """A view row is inconsistent with itself — refuse, never average it in."""


class AgreementRow(BaseModel):
    """One `"user".shadow_agreement_v` row."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    user_id: int
    factor: str = Field(min_length=1)
    trade_date: date
    pairs: int = Field(ge=1)
    median_abs_delta: Decimal
    within2_share: Decimal
    deltas: list[int] = Field(min_length=1)

    @field_validator("median_abs_delta", "within2_share", mode="before")
    @classmethod
    def _decimal(cls, value: Any) -> Any:
        return Decimal(str(value)) if isinstance(value, float) else value


class FactorAgreement(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    factor: str
    sessions: int
    pairs: int
    median_abs_delta: Decimal | None
    within2_share: Decimal | None
    gate_met: bool
    misses: list[str]


class ShadowReport(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    since: date | None
    bar: ShadowPromotionBar
    factors: list[FactorAgreement]


def _fmt(value: Decimal) -> str:
    text = format(value.normalize(), "f")
    return text


def shadow_report(rows: Iterable[Mapping[str, Any]], *, bar: ShadowPromotionBar, since: date | None) -> ShadowReport:
    by_factor: dict[str, list[AgreementRow]] = {}
    for raw in rows:
        try:
            row = AgreementRow.model_validate(dict(raw))
        except ValidationError as e:
            raise ShadowReportError(f"invalid shadow_agreement_v row: {e}") from e
        if row.pairs != len(row.deltas):
            raise ShadowReportError(
                f"{row.factor} {row.trade_date}: pairs={row.pairs} but {len(row.deltas)} deltas stored"
            )
        if since is not None and row.trade_date < since:
            continue
        by_factor.setdefault(row.factor, []).append(row)
    factors = []
    for factor, days in sorted(by_factor.items()):
        deltas = [d for day in days for d in day.deltas]
        sessions = len({day.trade_date for day in days})
        pairs = len(deltas)
        median = Decimal(str(statistics.median(deltas)))
        within2 = (Decimal(sum(d <= 2 for d in deltas)) / Decimal(pairs)).quantize(Decimal("0.000001"))
        misses = []
        if sessions < bar.sessions:
            misses.append(f"sessions {sessions} < {bar.sessions}")
        if pairs < bar.pairs:
            misses.append(f"pairs {pairs} < {bar.pairs}")
        if median > bar.median_max:
            misses.append(f"median |Δ| {_fmt(median)} > {_fmt(bar.median_max)}")
        if within2 < bar.within2_min:
            misses.append(f"within-2 share {_fmt(within2)} < {format(bar.within2_min, 'f')}")
        factors.append(FactorAgreement(
            factor=factor, sessions=sessions, pairs=pairs, median_abs_delta=median.normalize(),
            within2_share=within2.normalize(), gate_met=not misses, misses=misses,
        ))
    return ShadowReport(since=since, bar=bar, factors=factors)


def render_report(report: ShadowReport) -> str:
    bar = report.bar
    lines = [
        f"shadow report{' since ' + report.since.isoformat() if report.since else ''} — bar: sessions ≥ {bar.sessions}, "
        f"pairs ≥ {bar.pairs}, median |Δ| ≤ {_fmt(bar.median_max)}, within-2 ≥ {format(bar.within2_min, 'f')}",
        "(read-only: this report never flips anything — promotion is the curve tribunal + an L7 HITL decision)",
    ]
    if not report.factors:
        lines.append("no tap/shadow pairs recorded — GATE NOT MET for every factor")
        return "\n".join(lines)
    for f in report.factors:
        status = "GATE MET" if f.gate_met else f"GATE NOT MET ({'; '.join(f.misses)})"
        lines.append(
            f"{f.factor}: sessions {f.sessions} · pairs {f.pairs} · median |Δ| {_fmt(f.median_abs_delta)} · "
            f"within-2 {_fmt(f.within2_share)} · {status}"
        )
    return "\n".join(lines)


def cmd_shadow_report(args: argparse.Namespace) -> None:
    bar = CardSettingsReader().current().shadow_promotion_bar
    if bar is None:
        raise SystemExit(
            "card.shadow_promotion_bar is not set in \"user\".trader_settings — the bar is his setting and is "
            "never defaulted; load it with `cobalt settings load --card <file> --sha256 <hash> --apply`"
        )
    since = date.fromisoformat(args.since) if args.since else None
    rows = CardStore().shadow_agreement(since)
    print(render_report(shadow_report(rows, bar=bar, since=since)))


__all__ = ["AgreementRow", "FactorAgreement", "ShadowReport", "ShadowReportError", "cmd_shadow_report",
           "render_report", "shadow_report"]
