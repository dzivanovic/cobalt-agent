"""Typed values for the nightly replay (S2-P4 STEP-4..7).

Every structured value the replay reads, computes or publishes is one of
these models (Pydantic for all structured data). Numbers are `Decimal`
end to end: a counterfactual R that went through a float is a number
that does not replay to the same four decimals (L57).
"""

from __future__ import annotations

import hashlib
import json
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Literal, Optional

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

#: The one counterfactual-R formula's version. Stored in every receipt; a
#: change to the formula is a new version, never a silent recompute.
FORMULA_VERSION = "s2p4.cf_r.1"

#: `formation_replay` in `job.result` and the miss line while S2-P2's
#: evaluator is not in this tree (R4). The log line is exact.
FORMATION_UNAVAILABLE = "unavailable"
FORMATION_UNAVAILABLE_LINE = "trade_def replay: not available until S2-P2"

#: The exclusion values a `"user".missed` row may carry (0009's CHECK).
ExcludedBy = Literal[
    "unarmed", "passed", "not_filled", "no_card", "window", "rule_10",
    "not_in_any_source", "config_cap", "not_equity", "screen_inactive", "manual",
]

Direction = Literal["long", "short"]
MissKind = Literal["card", "formation", "mover"]
Side = Literal["gainers", "losers"]


class ReplayError(RuntimeError):
    """The replay refused. Names what and why; never a partial success."""


class ReplayInputError(ReplayError):
    """An input the formula needs is missing, ambiguous or contradictory."""


class StepFailed(ReplayError):
    """One replay step failed. Earlier steps' commits stand."""

    def __init__(self, step: str, error: BaseException):
        self.step = step
        self.error = error
        super().__init__(f"step {step} failed — {type(error).__name__}: {error}")


def canonical_json(payload: Any) -> str:
    """Sorted keys, no whitespace, Decimals and datetimes as strings."""
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)


def sha256_json(payload: Any) -> str:
    return hashlib.sha256(canonical_json(payload).encode("utf-8")).hexdigest()


class _Frozen(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


# ---------------------------------------------------------------------------
# F12 — cards
# ---------------------------------------------------------------------------


class TransitionRow(_Frozen):
    """One `card_transitions` row. `id` is the tiebreak for equal `at`."""

    id: Optional[int] = None
    card_id: int
    from_state: Optional[str] = None
    to_state: str
    at: AwareDatetime


class StopEdit(_Frozen):
    """One `card_stop_edits` row — the stop as of any instant replays."""

    id: Optional[int] = None
    at: AwareDatetime
    from_stop: Decimal
    to_stop: Decimal


class CardCandidate(_Frozen):
    """A card created on the replay day whose history never reached FILLED."""

    id: int
    ticker: str
    direction: Direction
    entry: Decimal
    stop: Decimal
    created_at: AwareDatetime
    window_ref: Optional[str] = None
    transitions: tuple[TransitionRow, ...]
    stop_edits: tuple[StopEdit, ...] = ()


class PositionSpan(_Frozen):
    """A card that was FILLED — open from `filled_at` until `closed_at`."""

    card_id: int
    filled_at: AwareDatetime
    closed_at: Optional[AwareDatetime] = None

    def open_at(self, instant: datetime) -> bool:
        return self.filled_at <= instant and (self.closed_at is None or self.closed_at > instant)


class WindowResolution(_Frozen):
    """The card's window end as the public resolver returned it."""

    resolved_end: AwareDatetime
    source: str
    detail: str


class MissRow(_Frozen):
    """One `"user".missed` row, before the database assigns its id."""

    trade_date: date
    kind: MissKind
    ticker: str
    direction: Optional[Direction] = None
    card_id: Optional[int] = None
    trade_def_md5: Optional[str] = None
    formation_at: Optional[AwareDatetime] = None
    pool_member_id: Optional[int] = None
    mover_id: Optional[int] = None
    excluded_by: ExcludedBy
    gate_detail: dict[str, Any]
    entry: Optional[Decimal] = None
    stop: Optional[Decimal] = None
    trigger_ts: Optional[AwareDatetime] = None
    fill_price: Optional[Decimal] = None
    horizon_end: Optional[AwareDatetime] = None
    exit_ts: Optional[AwareDatetime] = None
    exit_price: Optional[Decimal] = None
    exit_reason: Optional[Literal["stop", "horizon_end"]] = None
    cf_r: Optional[Decimal] = None
    mfe_r: Optional[Decimal] = None
    bars_watermark: Optional[AwareDatetime] = None
    formula_version: Optional[str] = None
    receipt: dict[str, Any]
    inputs_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")

    def subject(self) -> tuple:
        """The `missed_one_current_per_subject` key, in Python."""
        return (
            self.trade_date, self.kind, self.ticker, self.card_id or 0,
            self.trade_def_md5 or "",
            self.formation_at.isoformat() if self.formation_at else "",
            self.pool_member_id if self.kind == "formation" else 0,
        )


class CardReplay(_Frozen):
    """What replaying one candidate produced."""

    card_id: int
    ticker: str
    status: Literal["miss", "no_trigger", "input_stale"]
    reason: str
    miss: Optional[MissRow] = None


# ---------------------------------------------------------------------------
# F13 — movers
# ---------------------------------------------------------------------------


class MoverRow(_Frozen):
    """One ranked row of an unfiltered export, as `movers_daily` stores it."""

    side: Side
    rank: int = Field(ge=1)
    ticker: str = Field(min_length=1)
    change_pct: Decimal
    asset_type: Optional[str] = None
    volume: Optional[int] = None
    rvol: Optional[Decimal] = None


class MoversExport(_Frozen):
    """One side's export: the parsed top rows and the raw bytes' hash."""

    side: Side
    fetched_at: AwareDatetime
    export_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    header: tuple[str, ...]
    rows: tuple[MoverRow, ...]
    source: Literal["live", "retained"]
    cache_path: Optional[str] = None


class StoredMover(_Frozen):
    """An active `system.movers_daily` row."""

    id: Optional[int] = None
    trade_date: date
    side: Side
    rank: int
    ticker: str
    change_pct: Decimal
    asset_type: Optional[str] = None
    volume: Optional[int] = None
    rvol: Optional[Decimal] = None
    export_sha256: str
    fetched_at: AwareDatetime
    bars_archived: bool = False


class Episode(_Frozen):
    """One `system.radar_membership` episode the benchmark diffs against."""

    model_config = ConfigDict(extra="ignore", frozen=True)

    id: Optional[int] = None
    ticker: str
    trade_date: date
    entered_at: Optional[AwareDatetime] = None
    left_at: Optional[AwareDatetime] = None
    first_seen_at: Optional[AwareDatetime] = None
    excluded_by: Optional[str] = None
    source: Optional[str] = None


# ---------------------------------------------------------------------------
# The run
# ---------------------------------------------------------------------------


class ReconcileCounts(_Frozen):
    inserted: int = 0
    superseded: int = 0
    retired: int = 0
    unchanged: int = 0


class ReplayResult(BaseModel):
    """`job.result` (STEP-4) plus the coverage counts R1-12 surfaces."""

    model_config = ConfigDict(extra="forbid")

    trade_date: date
    replay_run_id: str
    dry_run: bool
    movers: int = 0
    archived: int = 0
    archive_failures: int = 0
    archive_incomplete: int = 0
    card_candidates: int = 0
    card_misses: int = 0
    mover_misses: int = 0
    input_stale: int = 0
    no_trigger: int = 0
    formation_replay: str = FORMATION_UNAVAILABLE
    line_action: Optional[str] = None
    line_diff: Optional[str] = None
    steps_done: list[str] = Field(default_factory=list)
    failed_step: Optional[str] = None
    precondition: Optional[str] = None
    reconcile: dict[str, ReconcileCounts] = Field(default_factory=dict)

    def job_result(self) -> dict[str, Any]:
        return self.model_dump(mode="json")


__all__ = [
    "CardCandidate", "CardReplay", "Direction", "Episode", "ExcludedBy",
    "FORMATION_UNAVAILABLE", "FORMATION_UNAVAILABLE_LINE", "FORMULA_VERSION",
    "MissKind", "MissRow", "MoverRow", "MoversExport", "PositionSpan",
    "ReconcileCounts", "ReplayError", "ReplayInputError", "ReplayResult", "Side",
    "StepFailed", "StopEdit", "StoredMover", "TransitionRow", "WindowResolution",
    "canonical_json", "sha256_json",
]
