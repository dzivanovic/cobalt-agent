"""Trade-definition schema — TAXONOMY-DRAFT-v0_6.md §10 (schema v0.3).

Config-as-code (TRIAGE cross-cutting law): `trade_def` and its variable
registry are YAML data, Pydantic-validated on load, never hand-parsed.
This module carries the schema only — no predicate parser, no setup
detectors, no bar logic. Enums are the single source of truth for the
taxonomy vocabulary (v0.6 §10.1/§10.2/§3.6); YAML data must match them
exactly or fail loud, never silently coerce.

`Predicate.expr` stores the §10.5 grammar string UNPARSED — grammar
evaluation is a future setups-engine sprint, not this one. Anywhere the
taxonomy says "any stop-placement" (raise_to.placement, the top-level
stop itself) reuses the same `StopPlacement` union so a validator can
check shape once.
"""

from __future__ import annotations

import re
from enum import Enum
from typing import Annotated, Any, Generic, Literal, TypeVar

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
    model_validator,
)

# ---------------------------------------------------------------------------
# Enums — verbatim from v0.6 §10.1 / §10.2 / §3.6. Extend here, never coerce
# an out-of-vocabulary value from data.
# ---------------------------------------------------------------------------


class Family(str, Enum):
    OPENING_DRIVE = "opening_drive"
    CONTINUATION = "continuation"
    RANGE_BREAK = "range_break"
    REVERSION = "reversion"
    TIME_WINDOW = "time_window"


class TradeClass(str, Enum):
    """Management shape, not a timeframe (v0.6 §0 timeframe-agnostic-trigger law)."""

    SCALP = "scalp"
    MOVE2MOVE = "move2move"
    SWING = "swing"
    OPTIONS = "options"


class Relation(str, Enum):
    WITH_TREND = "with_trend"
    COUNTERTREND = "countertrend"


class EntryMode(str, Enum):
    FRONT_SIDE = "front_side"
    BACKSIDE = "backside"


class SetupRef(str, Enum):
    """The 7 setup refs behind the Cameron H grid (§C)."""

    GAP_AND_GO = "gap_and_go"
    GAP_DOWN_INTO_SUPPORT = "gap_down_into_support"
    GAP_UP_INTO_RESISTANCE = "gap_up_into_resistance"
    DAY2_CONTINUATION = "day2_continuation"
    OVEREXTENSION = "overextension"
    VOLATILITY_IN_RANGE = "volatility_in_range"
    RANGE_BREAK = "range_break"


class RTHWindow(str, Enum):
    OPEN_DRIVE = "open_drive"
    MORNING = "morning"
    MIDDAY = "midday"
    AFTERNOON = "afternoon"
    CLOSE = "close"


class RangeBoundType(str, Enum):
    """v0.6 §3.0 — the only Range shape field; `shape` was dropped (§14 ruling 1)."""

    FLAT = "flat"
    CONVERGING = "converging"
    CHANNEL = "channel"


class TriggerType(str, Enum):
    BAR_BREAK = "bar_break"
    RANGE_BREAK = "range_break"
    INDICATOR_CROSS = "indicator_cross"
    SEQUENCE = "sequence"
    TRENDLINE_BREAK = "trendline_break"  # A.3
    INDICATOR_REJECTION = "indicator_rejection"  # A.4


class ConfirmationPolicyType(str, Enum):
    INTRABAR = "intrabar"
    CLOSE_THROUGH = "close_through"
    TWO_BAR = "two_bar"
    ACCEPTANCE = "acceptance"


class EvaluationType(str, Enum):
    TOUCH = "touch"
    CLOSE_THROUGH = "close_through"


class StructuralRef(str, Enum):
    """v0.6 §3.6 flat, literal structural references (excludes the
    parametrized `cross_point{a,b}` and `leg_end(n)` anchors, which carry
    their own params and are referenced as free-text anchors instead)."""

    SNAPBACK_CANDLE = "snapback_candle"
    TURN_LOW = "turn_low"
    LOW_OF_DAY = "low_of_day"
    HIGH_OF_DAY = "high_of_day"
    CONSOLIDATION_LOW = "consolidation_low"
    RANGE_BASE = "range_base"
    TURN_CANDLE = "turn_candle"
    RECENT_HIGHER_LOW = "recent_higher_low"
    RECENT_LOWER_HIGH = "recent_lower_high"  # A.7 — side-mirror of recent_higher_low
    ENTRY = "entry"  # alias: breakeven


class StopManagementType(str, Enum):
    FIXED = "fixed"
    BREAKEVEN_AT = "breakeven_at"
    RAISE_TO = "raise_to"
    TRAIL_MA_CLOSE = "trail_ma_close"
    TRAIL_BAR = "trail_bar"
    TIME_STOP = "time_stop"
    PASSIVE = "passive"


class ExitTargetType(str, Enum):
    RR_MULTIPLE = "rr_multiple"
    VWAP = "vwap"
    LEVEL = "level"
    MEASURED_MOVE = "measured_move"
    LEG_END = "leg_end"
    BAR_BREAK_REVERSE = "bar_break_reverse"
    MA_CLOSE = "ma_close"
    WINDOW_END = "window_end"
    CIC_EVENT = "cic_event"
    TRAIL = "trail"  # A.7/A.8 — {conditions[], mode: any}


class IndicatorType(str, Enum):
    """A.2 — indicator stop-placement vocabulary."""

    VWAP = "VWAP"
    EMA9 = "EMA9"
    EMA20 = "EMA20"
    EMA21 = "EMA21"


class SnapshotType(str, Enum):
    """A.2 — default at_entry: the hard stop is the indicator price at
    fill; live (Cobalt re-warns as the indicator drifts) is not the
    default."""

    AT_ENTRY = "at_entry"
    LIVE = "live"


class Event(str, Enum):
    """For `on:`, `after:`, `event()` atoms (v0.6 §10.2)."""

    ENTRY = "entry"
    EXIT_LEG = "exit_leg"
    LEG_END = "leg_end"
    RETEST = "retest"
    STOP_HIT = "stop_hit"
    CIC = "cic"
    CONSOLIDATION = "consolidation"
    DIVERGENCE = "divergence"


class OnCicActionType(str, Enum):
    EXIT_ALL = "exit_all"
    EXIT_LEG = "exit_leg"
    TIGHTEN_TO = "tighten_to"


# ---------------------------------------------------------------------------
# Shared building blocks
# ---------------------------------------------------------------------------


class Predicate(BaseModel):
    """A precondition / radar_watch / avoid / sequence-step atom.

    `expr` holds the §10.5 grammar string UNPARSED (no grammar parsing in
    this task); `text` is the human-readable fallback for anything not yet
    expressible in the grammar. Exactly one of the two is set.
    """

    model_config = ConfigDict(extra="forbid")

    expr: str | None = None
    text: str | None = None

    @model_validator(mode="after")
    def _exactly_one(self) -> Predicate:
        if bool(self.expr) == bool(self.text):
            raise ValueError(
                "Predicate must set exactly one of `expr` or `text`, not both or neither"
            )
        return self

    @property
    def computable(self) -> bool:
        return self.expr is not None


T = TypeVar("T")


class Tunable(BaseModel, Generic[T]):
    """An editable value. `dynamic=True` marks a v0.6 §0 "Dynamic
    definitions" law value — it must stand archiver-corpus replay (§13)
    before being counted solidified, and must appear in the replay
    backlog."""

    model_config = ConfigDict(extra="forbid")

    value: T
    dynamic: bool = False
    note: str | None = None


class ValidSetup(BaseModel):
    model_config = ConfigDict(extra="forbid")

    setup_ref: SetupRef
    relation: Relation


class EventRef(BaseModel):
    """A `event(name)` / `event(name, n)` atom used in `on:` / `after:`."""

    model_config = ConfigDict(extra="forbid")

    name: Event
    n: int | None = None


class ConfirmationPolicy(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: ConfirmationPolicyType
    bars: int | None = None
    time: str | None = None

    @model_validator(mode="after")
    def _params_only_for_acceptance(self) -> ConfirmationPolicy:
        if self.type != ConfirmationPolicyType.ACCEPTANCE and (
            self.bars is not None or self.time is not None
        ):
            raise ValueError(
                "bars/time are only valid when confirmation_policy.type == acceptance"
            )
        return self


class StopBuffer(BaseModel):
    """v0.6 §14 ruling 3 / RULINGS IN FORCE: `fixed` is the only buffer
    type; `spread` is not valid. Default 0.02."""

    model_config = ConfigDict(extra="forbid")

    type: Literal["fixed"] = "fixed"
    cents: Tunable[float] = Field(
        default_factory=lambda: Tunable[float](value=0.02, dynamic=False)
    )

    @model_validator(mode="after")
    def _positive_cents(self) -> StopBuffer:
        if self.cents.value <= 0:
            raise ValueError(
                f"stop buffer cents must be positive, got {self.cents.value}"
            )
        return self


# --- Stop placement (reused by the top-level `stop` and by `raise_to`) ----


class StructuralExtremePlacement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["structural_extreme"] = "structural_extreme"
    ref: StructuralRef
    buffer: StopBuffer = Field(default_factory=StopBuffer)
    floor: Literal["config"] | None = "config"


class MeasuredFractionPlacement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["measured_fraction"] = "measured_fraction"
    anchor_a: str = Field(min_length=1)
    anchor_b: str = Field(min_length=1)
    fraction: float = Field(gt=0, le=1)


class LevelPlacement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["level"] = "level"
    level_ref: str = Field(min_length=1)
    buffer: StopBuffer | None = None


class IndicatorPlacement(BaseModel):
    """A.2 — VWAP/EMA-anchored stop. Default `snapshot: at_entry`."""

    model_config = ConfigDict(extra="forbid")

    type: Literal["indicator"] = "indicator"
    indicator: IndicatorType
    buffer: StopBuffer = Field(default_factory=StopBuffer)
    snapshot: SnapshotType = SnapshotType.AT_ENTRY
    floor: Literal["config"] | None = "config"


StopPlacement = Annotated[
    StructuralExtremePlacement
    | MeasuredFractionPlacement
    | LevelPlacement
    | IndicatorPlacement,
    Field(discriminator="type"),
]


class Stop(BaseModel):
    model_config = ConfigDict(extra="forbid")

    placement: StopPlacement
    evaluation: EvaluationType


# --- Stop management ladder -------------------------------------------------


class _StopManagementBase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    on: EventRef = Field(default_factory=lambda: EventRef(name=Event.ENTRY))


class FixedMgmt(_StopManagementBase):
    type: Literal["fixed"] = "fixed"


class BreakevenAtMgmt(_StopManagementBase):
    type: Literal["breakeven_at"] = "breakeven_at"
    r: float = Field(gt=0)


class RaiseToMgmt(_StopManagementBase):
    type: Literal["raise_to"] = "raise_to"
    placement: StopPlacement


class TrailMaCloseMgmt(_StopManagementBase):
    type: Literal["trail_ma_close"] = "trail_ma_close"
    ma: Tunable[str]
    tf: str = Field(min_length=1)


class TrailBarMgmt(_StopManagementBase):
    type: Literal["trail_bar"] = "trail_bar"
    n: int = Field(gt=0)


class TimeStopMgmt(_StopManagementBase):
    type: Literal["time_stop"] = "time_stop"
    duration_bars: Tunable[int]
    condition: str = Field(min_length=1)


class PassiveMgmt(_StopManagementBase):
    type: Literal["passive"] = "passive"


StopManagementEntry = Annotated[
    FixedMgmt
    | BreakevenAtMgmt
    | RaiseToMgmt
    | TrailMaCloseMgmt
    | TrailBarMgmt
    | TimeStopMgmt
    | PassiveMgmt,
    Field(discriminator="type"),
]


# --- Exit --------------------------------------------------------------------

# A.7/A.8 — trail exit conditions[]. `first condition to fire exits`; MA
# periods route through Tunable[str] so a condition can carry either a
# literal indicator ("EMA9") or an `ma.*` ref resolved against
# defaults.yaml (loader.resolve_ma_ref).


class PriorBarBreakCondition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["prior_bar_break"] = "prior_bar_break"
    n: int = Field(default=1, gt=0)


class MaCloseCondition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["ma_close"] = "ma_close"
    ma: Tunable[str]


class VwapCloseCondition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["vwap_close"] = "vwap_close"


class LevelCondition(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["level"] = "level"
    level_ref: str = Field(min_length=1)


TrailCondition = Annotated[
    PriorBarBreakCondition | MaCloseCondition | VwapCloseCondition | LevelCondition,
    Field(discriminator="type"),
]


class TrailExitParams(BaseModel):
    """A.7 — `trail {conditions[], mode: any}`; first condition to fire
    exits. Validated out of `ExitLeg.params` only when
    `target_type == trail` (every other target type keeps its
    unstructured params dict, as in Batch 1)."""

    model_config = ConfigDict(extra="forbid")

    conditions: list[TrailCondition] = Field(min_length=1)
    mode: Literal["any"] = "any"


class ExitLeg(BaseModel):
    model_config = ConfigDict(extra="forbid")

    fraction: float = Field(gt=0, le=1)
    target_type: ExitTargetType
    params: dict[str, Any] = Field(default_factory=dict)
    evaluation: EvaluationType
    computable: Literal["cobalt", "human"] = "cobalt"

    @model_validator(mode="after")
    def _trail_params_valid(self) -> ExitLeg:
        if self.target_type == ExitTargetType.TRAIL:
            try:
                TrailExitParams(**self.params)
            except ValidationError as e:
                raise ValueError(
                    f"exit leg target_type=trail has invalid params: {e}"
                ) from e
        return self


class OnCic(BaseModel):
    model_config = ConfigDict(extra="forbid")

    triggers: list[int] = Field(min_length=1)
    action: OnCicActionType
    tighten_to: Literal["breakeven", "trail_bar"] | None = None

    @field_validator("triggers")
    @classmethod
    def _triggers_in_range(cls, v: list[int]) -> list[int]:
        if any(t < 1 or t > 4 for t in v):
            raise ValueError(f"on_cic.triggers must be within 1..4, got {v}")
        return v

    @model_validator(mode="after")
    def _tighten_to_only_with_action(self) -> OnCic:
        if self.action == OnCicActionType.TIGHTEN_TO and self.tighten_to is None:
            raise ValueError("on_cic.tighten_to is required when action == tighten_to")
        if self.action != OnCicActionType.TIGHTEN_TO and self.tighten_to is not None:
            raise ValueError(
                "on_cic.tighten_to is only valid when action == tighten_to"
            )
        return self


# --- Trigger -------------------------------------------------------------


class TriggerStep(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    predicate: Predicate
    # Second Chance step 2 (retest) carries no confirmation_policy in
    # TRADE-DEFS-BATCH1-v0_1.md §B.3 — flagged in the population report;
    # left optional rather than inventing a default.
    confirmation_policy: ConfirmationPolicy | None = None


class SimpleTrigger(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal[
        "bar_break",
        "range_break",
        "indicator_cross",
        "trendline_break",
        "indicator_rejection",
    ]
    params: dict[str, Any] = Field(default_factory=dict)
    confirmation_policy: ConfirmationPolicy


class SequenceTrigger(BaseModel):
    model_config = ConfigDict(extra="forbid")

    type: Literal["sequence"] = "sequence"
    steps: list[TriggerStep] = Field(min_length=1)


Trigger = Annotated[SimpleTrigger | SequenceTrigger, Field(discriminator="type")]


class AddPolicy(BaseModel):
    """Reserved, default none (§10.6 PARKED)."""

    model_config = ConfigDict(extra="forbid")

    type: Literal["none"] = "none"
    params: dict[str, Any] | None = None


# ---------------------------------------------------------------------------
# trade_def registry (v0.6 §10.1)
# ---------------------------------------------------------------------------

_STANDARD_QUALITY_FACTORS = {"setup_relation", "market_alignment", "sector_alignment"}
_FORBIDDEN_REFERENCE_STATS_KEYS = {"ev", "expectancy"}
_DURATION_PATTERN = re.compile(r"^\d+ min$")  # A.1 — e.g. "3 min"


class TradeDef(BaseModel):
    model_config = ConfigDict(extra="forbid", populate_by_name=True)

    id: str = Field(min_length=1)
    name: str = Field(min_length=1)
    aliases: list[str] = Field(default_factory=list)
    family: list[Family] = Field(min_length=1)
    trade_class: TradeClass = Field(alias="class")
    sides: Literal["long+short (inverted)"] = "long+short (inverted)"
    valid_setups: list[ValidSetup] = Field(min_length=1)
    instance_direction: Literal["computed"] = "computed"
    working_timeframe: Literal["config"] = "config"
    tf_ceiling: int | None = None
    entry_mode: EntryMode
    preconditions: list[Predicate] = Field(default_factory=list)
    radar_watch: list[Predicate] = Field(default_factory=list)
    trigger: Trigger
    stop: Stop
    stop_management: list[StopManagementEntry] = Field(min_length=1)
    exit: list[ExitLeg] = Field(min_length=1)
    on_cic: OnCic
    max_attempts: Tunable[int]
    reentry_window: Tunable[str] | None = None  # A.1 — duration, e.g. "3 min"
    add_policy: AddPolicy = Field(default_factory=AddPolicy)
    avoid: list[Predicate] = Field(default_factory=list)
    quality_factors: list[str] = Field(min_length=1)
    preferred_windows: list[RTHWindow] = Field(default_factory=list)
    preferred_windows_ref: str | None = None
    reference_stats: dict[str, Any] | None = None

    @field_validator("reentry_window")
    @classmethod
    def _reentry_window_format(cls, v: Tunable[str] | None) -> Tunable[str] | None:
        if v is not None and not _DURATION_PATTERN.match(v.value):
            raise ValueError(f"reentry_window must match '<N> min', got {v.value!r}")
        return v

    @model_validator(mode="after")
    def _tf_ceiling_matches_class(self) -> TradeDef:
        if self.trade_class == TradeClass.SCALP:
            if self.tf_ceiling != 15:
                raise ValueError(
                    f"{self.id}: class == scalp requires tf_ceiling == 15, got {self.tf_ceiling!r}"
                )
        elif self.tf_ceiling is not None:
            raise ValueError(
                f"{self.id}: tf_ceiling is only valid for class == scalp (class == {self.trade_class.value!r})"
            )
        return self

    @model_validator(mode="after")
    def _exit_fractions_sum_to_one(self) -> TradeDef:
        total = sum(leg.fraction for leg in self.exit)
        if abs(total - 1.0) > 0.01:
            raise ValueError(
                f"{self.id}: exit fractions sum to {total}, must be 1.0 +/- 0.01"
            )
        return self

    @model_validator(mode="after")
    def _standard_quality_factors_present(self) -> TradeDef:
        missing = _STANDARD_QUALITY_FACTORS - set(self.quality_factors)
        if missing:
            raise ValueError(
                f"{self.id}: quality_factors missing standard trio: {sorted(missing)}"
            )
        return self

    @field_validator("reference_stats")
    @classmethod
    def _no_ev_in_reference_stats(
        cls, v: dict[str, Any] | None
    ) -> dict[str, Any] | None:
        if v is None:
            return v
        bad = {k for k in v if k.lower() in _FORBIDDEN_REFERENCE_STATS_KEYS}
        if bad:
            raise ValueError(
                f"reference_stats must not carry ev/expectancy keys, found: {sorted(bad)}"
            )
        return v
