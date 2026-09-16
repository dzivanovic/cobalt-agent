"""A radar card: its creation spec, who owns each field, and the ladder
order (S2-P2 STEP-4/STEP-6; Astra R1-7, R1-15).

A radar card is an `"user".aset_sizings` row with `origin = 'radar'`,
born UNSIZED in WATCH. This module is pure — the store writes what
`RadarCardSpec` validates, and the panel orders what `ladder_order`
returns.

TWO PRICE REPRESENTATIONS, NAMED (R1-7). `trigger_price` and
`structural_stop` are the IMMUTABLE formation evidence — what the
detector saw, replayed from the receipt, never edited. `entry` and
`stop` are the LIVE sizing inputs: they start equal to the evidence and
`stop` moves when he edits it. Sizing (the key tap), proximity and the
stop-touched expiry read the live pair; replay and audit read the
evidence.

FIELD OWNERS. Every column of `"user".radar_cards_v` carries one badge:
`COBALT` (the engine wrote it), `YOU` (his tap or edit decides it) or
`LEDGER` (the actor of the card's last transition decides it — a state
he moved is his, a state Cobalt expired is Cobalt's). The test reads the
view's SQL and refuses a column without a badge.

LADDER ORDER (R1-15), deterministic end to end:

* pinned = ARMED / TRIGGERED / FILLED, first, by (pool position, nulls
  last; score desc, nulls last; ticker; card id);
* WATCH by (card_score desc, NULLS LAST — an untapped card has no score
  and sinks, it does not scatter; pool position, nulls last; ticker;
  card id). The rank chip is the card's place in THIS order;
* at most one promoted WATCH card moves up to #2 — or to just below the
  pinned cards when two or more are pinned (pinned priority holds) — and
  is never moved DOWN by being promoted. Its rank chip does not change;
  release restores the natural order because nothing else was touched;
* terminal cards are a separate list.
"""

from __future__ import annotations

from datetime import datetime
from decimal import Decimal
from typing import Any, Literal

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, model_validator

from .models import TERMINAL, CardState
from .scoring import Dot

OWNER_BADGES = frozenset({"COBALT", "YOU", "LEDGER"})

#: `"user".radar_cards_v` column -> owner badge.
FIELD_OWNERS: dict[str, str] = {
    "card_id": "COBALT", "user_id": "COBALT", "created_at": "COBALT", "ticker": "COBALT",
    "direction": "COBALT", "state": "LEDGER", "state_at": "LEDGER", "session": "COBALT",
    "account_mode": "YOU", "pool_member_id": "COBALT",
    "trade_def_slug": "COBALT", "trade_def_md5": "COBALT", "setup_ref": "COBALT",
    "trigger_type": "COBALT", "trigger_price": "COBALT", "stop_ref": "COBALT",
    "structural_stop": "COBALT", "entry": "COBALT", "stop": "YOU", "formed_at": "COBALT",
    "expires_at": "COBALT", "why": "COBALT",
    "proposed_key": "COBALT", "tapped_grade": "YOU", "sized_grade": "COBALT", "snap_notice": "COBALT",
    "grade": "COBALT", "risk_budget": "COBALT", "shares": "COBALT", "used_risk": "COBALT",
    "conviction": "YOU", "proximity": "COBALT", "card_score": "COBALT", "score_suppressed": "COBALT",
    "radar_score_id": "COBALT", "scan_id": "COBALT", "formula_sha256": "COBALT",
    "tunables_sha256": "COBALT", "settings_sha256": "COBALT",
    "health": "COBALT", "promoted_at": "YOU",
    "board_score_id": "COBALT", "board_run_id": "COBALT", "board_evaluation": "COBALT",
    "board_started_at": "COBALT", "outside_pool": "COBALT",
}

TradeDirection = Literal["long", "short"]


class RadarCardSpec(BaseModel):
    """Everything the ONE radar creation path writes for a new WATCH card."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    ticker: str = Field(min_length=1, max_length=12)
    direction: TradeDirection
    session: str = Field(min_length=1)
    pool_member_id: int
    trade_def_slug: str = Field(min_length=1)
    trade_def_md5: str = Field(pattern=r"^[0-9a-f]{32}$")
    setup_ref: str = Field(min_length=1)
    trigger_type: str = Field(min_length=1)
    trigger_price: Decimal = Field(gt=0)
    stop_ref: str = Field(min_length=1)
    structural_stop: Decimal = Field(gt=0)
    formed_at: AwareDatetime
    expires_at: AwareDatetime
    why: str = Field(min_length=1)
    radar_score_id: int
    scan_id: int
    formula_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    tunables_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    settings_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    proximity: Decimal = Field(ge=0, le=1)
    conviction: Decimal | None = None
    card_score: int | None = None
    score_suppressed: str | None = None
    proposed_key: str | None = None
    dots: list[Dot]
    #: The genesis transition's evidence: run id, formation bar ts, atoms.
    evidence: dict[str, Any]

    @model_validator(mode="after")
    def _stop_side(self) -> RadarCardSpec:
        if self.direction == "short" and self.structural_stop <= self.trigger_price:
            raise ValueError(f"short card stop {self.structural_stop} must sit above trigger {self.trigger_price}")
        if self.direction == "long" and self.structural_stop >= self.trigger_price:
            raise ValueError(f"long card stop {self.structural_stop} must sit below trigger {self.trigger_price}")
        if self.expires_at <= self.formed_at:
            raise ValueError("a card cannot expire at or before its own formation")
        return self

    @property
    def entry(self) -> Decimal:
        return self.trigger_price

    @property
    def stop(self) -> Decimal:
        return self.structural_stop

    @property
    def per_share_risk(self) -> Decimal:
        return abs(self.trigger_price - self.structural_stop)


class LadderEntry(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    card_id: int
    state: CardState
    card_score: int | None
    pool_position: int | None
    ticker: str
    promoted_at: datetime | None = None
    state_at: datetime


class LadderPosition(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    card_id: int
    position: int
    rank_chip: int | None
    pinned: bool
    promoted: bool


class LadderOrder(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    active: list[LadderPosition]
    terminal: list[LadderPosition]


PINNED = frozenset({CardState.ARMED, CardState.TRIGGERED, CardState.FILLED})


def _nulls_last(value: int | None, *, descending: bool) -> tuple[int, int]:
    if value is None:
        return (1, 0)
    return (0, -value if descending else value)


def ladder_order(entries: list[LadderEntry]) -> LadderOrder:
    promoted = [e for e in entries if e.promoted_at is not None]
    if len(promoted) > 1:
        raise ValueError(f"at most one promoted card, got {[e.card_id for e in promoted]}")
    if promoted and promoted[0].state is not CardState.WATCH:
        raise ValueError(f"only a WATCH card can be promoted; card {promoted[0].card_id} is {promoted[0].state.value}")

    pinned = sorted(
        (e for e in entries if e.state in PINNED),
        key=lambda e: (_nulls_last(e.pool_position, descending=False),
                       _nulls_last(e.card_score, descending=True), e.ticker, e.card_id),
    )
    watch = sorted(
        (e for e in entries if e.state is CardState.WATCH),
        key=lambda e: (_nulls_last(e.card_score, descending=True),
                       _nulls_last(e.pool_position, descending=False), e.ticker, e.card_id),
    )
    chips = {e.card_id: i + 1 for i, e in enumerate(watch)}
    active = [*pinned, *watch]
    if promoted:
        card = promoted[0]
        current = active.index(card)
        target = min(current, max(len(pinned), 1))
        active.pop(current)
        active.insert(target, card)
    terminal = sorted(
        (e for e in entries if e.state in TERMINAL),
        key=lambda e: (e.state.value, e.state_at, e.ticker, e.card_id),
    )
    return LadderOrder(
        active=[
            LadderPosition(card_id=e.card_id, position=i + 1, rank_chip=chips.get(e.card_id),
                           pinned=e.state in PINNED, promoted=e.promoted_at is not None)
            for i, e in enumerate(active)
        ],
        terminal=[
            LadderPosition(card_id=e.card_id, position=i + 1, rank_chip=None, pinned=False, promoted=False)
            for i, e in enumerate(terminal)
        ],
    )


__all__ = [
    "FIELD_OWNERS", "LadderEntry", "LadderOrder", "LadderPosition", "OWNER_BADGES",
    "PINNED", "RadarCardSpec", "ladder_order",
]
