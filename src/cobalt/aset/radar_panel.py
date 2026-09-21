"""Trade Radar panel view models, builders, and HTML renderers.

The pool layer (S2-P3) is read-only. The card ladder (S2-P2 STEP-8) reads
`"user".radar_cards_v` rows through `CardStore.radar_board_cards` and
renders them with their owner badges, hollow shadow dots, the 1-10 tap
strip, the key row and promote. Every write the ladder offers is a
`fetch` POST to one of the allowlisted `/radar/card/{id}/…` routes in
`web.py`; this module itself never writes, initializes a schema, or
attests a note.
"""

from __future__ import annotations

import html
from datetime import date, datetime, timedelta
from decimal import Decimal
from typing import Any, Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    ValidationError,
    field_validator,
)

from cobalt.cards import TERMINAL, CardState, CardStore
from cobalt.cards.models import KEY_EDITABLE
from cobalt.cards.radar import FIELD_OWNERS, LadderEntry, ladder_order
from cobalt.cards.scoring import Dot, colour_thresholds, dot_colour
from cobalt.radar.models import PoolBlock, RankMetricName
from cobalt.radar.store import RadarStore
from cobalt.session.clock import now_utc, session_clock
from cobalt.session.models import Session
from cobalt.settings.store import TraderSettingsStore
from cobalt.taxonomy.loader import load_tunables

POOL_KEY = "primary"
SCANNED_SESSIONS = {Session.PREMARKET, Session.RTH, Session.AFTERMARKET}


class RadarPanelError(RuntimeError):
    """A required panel input is absent, invalid, or internally inconsistent."""


class _ViewModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


def _aware(value: datetime | None, field: str) -> datetime | None:
    if value is not None and (value.tzinfo is None or value.utcoffset() is None):
        raise ValueError(f"{field} must be timezone-aware")
    return value


class SourceDegradation(_ViewModel):
    source: str = Field(min_length=1)
    reason: str = Field(min_length=1)
    since: datetime

    @field_validator("since")
    @classmethod
    def _since_aware(cls, value: datetime) -> datetime:
        return _aware(value, "degraded source since")  # type: ignore[return-value]


class PollFailure(_ViewModel):
    ticker: str = Field(min_length=1)
    reason: str = Field(min_length=1)
    since: datetime

    @field_validator("since")
    @classmethod
    def _since_aware(cls, value: datetime) -> datetime:
        return _aware(value, "poll failure since")  # type: ignore[return-value]


class PoolRecord(_ViewModel):
    pool_key: str = Field(min_length=1)
    state: str = Field(min_length=1)
    degraded: bool
    degraded_sources: list[SourceDegradation | str]
    failed_stage: str | None
    failed_detail: str | None
    sources: list[str]
    session: Session
    cap: int = Field(ge=1)
    members: int = Field(ge=0)
    last_scan_id: int | None
    last_scan_at: datetime | None
    last_scan_ms: int | None
    last_poll_at: datetime | None
    poll_failures: list[PollFailure]
    budget: dict[str, Any] | None
    updated_at: datetime

    @field_validator("last_scan_at", "last_poll_at", "updated_at")
    @classmethod
    def _timestamps_aware(cls, value: datetime | None, info) -> datetime | None:
        return _aware(value, info.field_name)


class MembershipRecord(_ViewModel):
    id: int
    pool_key: str = Field(min_length=1)
    ticker: str = Field(min_length=1)
    trade_date: date
    first_seen_at: datetime
    entered_at: datetime | None
    left_at: datetime | None
    source: str = Field(min_length=1)
    sources: list[str]
    rank_at_entry: int | None
    last_rank: int | None
    below_cap_streak: int = Field(ge=0)
    excluded_by: str | None
    session: Session
    opened_scan_id: int
    last_scan_id: int
    closed_scan_id: int | None
    # S2-P4 R1 — required, nullable. NULL is a pre-deploy episode; a row
    # MISSING the keys is a store that did not select them, and fails.
    rank_metric: RankMetricName | None
    rank_value: Decimal | None

    @field_validator("first_seen_at", "entered_at", "left_at")
    @classmethod
    def _timestamps_aware(cls, value: datetime | None, info) -> datetime | None:
        return _aware(value, info.field_name)


class PoolMirror(BaseModel):
    """The trader-settings envelope around the strict ``PoolBlock``."""

    model_config = ConfigDict(extra="allow")

    block: dict[str, Any] | None
    status: str = Field(min_length=1)
    error: str | None = None


class BannerView(_ViewModel):
    level: Literal["degraded", "stale", "retained"]
    title: str = Field(min_length=1)
    detail: str = Field(min_length=1)


class PoolRow(_ViewModel):
    episode_id: int
    ticker: str
    position: int | None
    source: str
    sources: list[str]
    session: Session
    first_seen_at: datetime
    entered_at: datetime | None
    left_at: datetime | None
    excluded_by: str | None
    rank_metric: RankMetricName | None
    rank_value: Decimal | None
    category: Literal["current", "departed", "excluded"]
    entered_since: bool = False
    left_since: bool = False


class ChurnDelta(_ViewModel):
    since: datetime
    entered_episode_ids: list[int]
    left_episode_ids: list[int]
    entered: int
    left: int


class PoolView(_ViewModel):
    pool_key: str
    data_date: date
    clock_session: Session
    scan_session: Session
    rank_metric: Literal["volume", "rvol"]
    override_labels: list[str]
    cap: int
    members: int
    current: list[PoolRow]
    departed: list[PoolRow]
    excluded: list[PoolRow]
    last_scan_at: datetime
    observed_watermark: datetime
    scan_interval: int = Field(gt=0)
    stale: bool
    retained_prior_day: bool
    banners: list[BannerView]
    churn: ChurnDelta | None


# ---------------------------------------------------------------------
# The card ladder (S2-P2 STEP-8)
# ---------------------------------------------------------------------


class RadarCardRow(_ViewModel):
    """One `"user".radar_cards_v` row — exactly the view's columns — plus
    the card's `"user".card_dots` rows. Validated before anything renders."""

    card_id: int
    user_id: int
    created_at: datetime
    ticker: str = Field(min_length=1)
    direction: Literal["long", "short"]
    state: CardState
    state_at: datetime
    session: str = Field(min_length=1)
    account_mode: str | None
    pool_member_id: int
    trade_def_slug: str = Field(min_length=1)
    trade_def_md5: str = Field(min_length=1)
    setup_ref: str | None
    trigger_type: str | None
    trigger_price: Decimal
    stop_ref: str | None
    structural_stop: Decimal
    entry: Decimal
    stop: Decimal
    formed_at: datetime | None
    expires_at: datetime | None
    why: str | None
    proposed_key: str | None
    tapped_grade: str | None
    sized_grade: str | None
    snap_notice: str | None
    grade: str | None
    risk_budget: Decimal | None
    shares: int | None
    used_risk: Decimal | None
    conviction: Decimal | None
    proximity: Decimal | None
    card_score: int | None
    score_suppressed: str | None
    radar_score_id: int
    scan_id: int
    formula_sha256: str
    tunables_sha256: str
    settings_sha256: str
    health: dict[str, Any] | None
    promoted_at: datetime | None
    board_score_id: int | None
    board_run_id: int | None
    board_evaluation: str | None
    board_started_at: datetime | None
    outside_pool: bool
    last_price: Decimal | None
    pool_position: int | None
    dots: list[Dot]

    @field_validator("created_at", "state_at", "formed_at", "expires_at", "promoted_at", "board_started_at")
    @classmethod
    def _timestamps_aware(cls, value: datetime | None, info) -> datetime | None:
        return _aware(value, info.field_name)


_ROW_COLUMNS = set(RadarCardRow.model_fields) - {"dots"}
if _ROW_COLUMNS != set(FIELD_OWNERS):  # pragma: no cover - import-time contract
    raise RadarPanelError(
        f"radar card row columns and FIELD_OWNERS disagree: {sorted(_ROW_COLUMNS ^ set(FIELD_OWNERS))}"
    )

#: The fields the card face and detail pane display, each with its badge.
BADGED_FIELDS: tuple[str, ...] = (
    "ticker", "direction", "state", "setup_ref", "trade_def_slug", "why", "entry", "stop",
    "trigger_price", "structural_stop", "last_price", "proposed_key", "tapped_grade", "sized_grade",
    "snap_notice", "grade", "shares", "risk_budget", "conviction", "proximity", "card_score",
    "score_suppressed", "pool_position", "formed_at", "expires_at", "health", "outside_pool", "scan_id",
)


class DotView(_ViewModel):
    factor: str = Field(min_length=1)
    position: int = Field(ge=0)
    source: Literal["cobalt", "cobalt-degraded", "human"]
    tier: Literal["deterministic", "judgment"]
    role: Literal["shadow", "live", "human"]
    #: Hollow = nothing counts toward conviction yet: an untapped shadow,
    #: desk or human dot. A tap fills it.
    hollow: bool
    engine_grade: int | None = Field(default=None, ge=1, le=10)
    trader_grade: int | None = Field(default=None, ge=1, le=10)
    #: The grade the dot shows as its own: the tap, or a LIVE engine grade.
    shown_grade: int | None = Field(default=None, ge=1, le=10)
    colour: Literal[0, 1, 2] | None
    na_reason: str | None
    why: str = Field(min_length=1)
    owner: Literal["COBALT", "YOU"]
    tappable: bool


class KeyView(_ViewModel):
    grade: str
    dollars: Decimal
    enabled: bool
    proposed: bool
    tapped: bool
    sized: bool


class HealthView(_ViewModel):
    label: str = Field(min_length=1)
    status: Literal["ok", "warn", "bad", "n/a"]
    note: str = Field(min_length=1)


class CardView(_ViewModel):
    id: int
    ticker: str = Field(min_length=1)
    direction: Literal["long", "short"]
    state: CardState
    setup: str
    trade: str = Field(min_length=1)
    why: str
    trigger: Decimal
    trigger_evidence: Decimal
    stop: Decimal
    structural_stop: Decimal
    last: Decimal | None
    target_1r: Decimal
    target_2r: Decimal
    grade: str | None
    tapped_grade: str | None
    sized_grade: str | None
    snap_notice: str | None
    proposed_key: str | None
    score_suppressed: str | None
    keys: list[KeyView]
    key_editable: bool
    shares: int | None
    risk_budget: Decimal | None
    card_score: int | None
    conviction: Decimal | None
    proximity: Decimal | None
    pool_position: int | None
    rank_chip: int | None
    promoted: bool
    outside_pool: bool
    dots: list[DotView]
    health: list[HealthView]
    badges: dict[str, str]
    state_at: datetime
    formed_at: datetime | None
    expires_at: datetime | None
    scan_id: int
    board_evaluation: str | None

    @property
    def display_state(self) -> str:
        return "IN-TRADE" if self.state is CardState.FILLED else self.state.value


class LadderView(_ViewModel):
    active: list[CardView]
    terminal: list[CardView]
    empty_message: str | None
    rung: str | None = None


class RadarPanelView(_ViewModel):
    pool: PoolView
    ladder: LadderView


def parse_since(value: str, *, now: datetime) -> datetime:
    """Parse the untrusted refresh cursor; no default and no zone guessing."""
    if not value or not value.strip():
        raise RadarPanelError("since is required")
    try:
        parsed = datetime.fromisoformat(value.strip())
    except ValueError as exc:
        raise RadarPanelError("since must be an ISO-8601 datetime") from exc
    try:
        _aware(parsed, "since")
        _aware(now, "now")
    except ValueError as exc:
        raise RadarPanelError(str(exc)) from exc
    if parsed > now:
        raise RadarPanelError("since cannot be in the future")
    return parsed


def _validated_interval(loader) -> int:
    registry = loader()
    row = registry.by_key.get("radar.scan_interval")
    if row is None:
        raise RadarPanelError("FAILED: tunable radar.scan_interval is missing")
    if isinstance(row.value, bool):
        raise RadarPanelError("FAILED: radar.scan_interval must be a positive integer")
    try:
        interval = int(row.value)
    except (TypeError, ValueError) as exc:
        raise RadarPanelError("FAILED: radar.scan_interval must be a positive integer") from exc
    if interval <= 0:
        raise RadarPanelError("FAILED: radar.scan_interval must be a positive integer")
    return interval


def _source_name(value: SourceDegradation | str) -> str:
    return value.source if isinstance(value, SourceDegradation) else value


def _row(
    record: MembershipRecord,
    category: Literal["current", "departed", "excluded"],
    since: datetime | None,
) -> PoolRow:
    admitted = record.entered_at is not None
    return PoolRow(
        episode_id=record.id,
        ticker=record.ticker,
        position=record.last_rank,
        source=record.source,
        sources=record.sources,
        session=record.session,
        first_seen_at=record.first_seen_at,
        entered_at=record.entered_at,
        left_at=record.left_at,
        excluded_by=record.excluded_by,
        rank_metric=record.rank_metric,
        rank_value=record.rank_value,
        category=category,
        entered_since=bool(admitted and since is not None and record.entered_at > since),
        left_since=bool(
            admitted and since is not None and record.left_at is not None and record.left_at > since
        ),
    )


def build_pool_view(
    *,
    since: datetime | None,
    snapshot: bool,
    pool_key: str = POOL_KEY,
    radar_store: RadarStore | None = None,
    settings_store: TraderSettingsStore | None = None,
    clock=None,
    now: datetime | None = None,
    tunables_loader=load_tunables,
) -> PoolView:
    """Read and validate one internally consistent pool snapshot."""
    if snapshot != (since is None):
        raise RadarPanelError("snapshot must omit since; refresh must supply since")
    instant = now or now_utc()
    try:
        _aware(instant, "now")
    except ValueError as exc:
        raise RadarPanelError(str(exc)) from exc
    if since is not None:
        try:
            _aware(since, "since")
        except ValueError as exc:
            raise RadarPanelError(str(exc)) from exc
        if since > instant:
            raise RadarPanelError("since cannot be in the future")
    radar_store = radar_store or RadarStore()
    settings_store = settings_store or TraderSettingsStore()
    clock = clock or session_clock()

    try:
        raw_pool = radar_store.pool_row(pool_key)
    except Exception as exc:
        raise RadarPanelError(
            f"FAILED: radar pool read failed: {type(exc).__name__}: {exc}"
        ) from exc
    if raw_pool is None:
        raise RadarPanelError(f"FAILED: radar pool {pool_key!r} is missing")
    try:
        pool = PoolRecord.model_validate(raw_pool)
    except ValidationError as exc:
        raise RadarPanelError(f"FAILED: invalid radar pool row: {exc}") from exc
    if pool.last_scan_at is None:
        raise RadarPanelError("FAILED: radar pool has no last_scan_at")
    if pool.failed_stage:
        detail = pool.failed_detail or "no failure detail recorded"
        raise RadarPanelError(f"FAILED: radar {pool.failed_stage}: {detail}")

    try:
        settings = settings_store.values()
    except Exception as exc:
        raise RadarPanelError(
            f"FAILED: radar.pool settings read failed: {type(exc).__name__}: {exc}"
        ) from exc
    if "radar.pool" not in settings:
        raise RadarPanelError("FAILED: trader setting radar.pool is missing")
    try:
        mirror = PoolMirror.model_validate(settings["radar.pool"])
    except ValidationError as exc:
        raise RadarPanelError(f"FAILED: invalid radar.pool setting: {exc}") from exc
    if mirror.status != "ok":
        detail = mirror.error or "no mirror error recorded"
        raise RadarPanelError(f"FAILED: radar.pool mirror status {mirror.status}: {detail}")
    if mirror.block is None:
        raise RadarPanelError("FAILED: radar.pool block is missing")
    try:
        block = PoolBlock.model_validate(mirror.block)
    except ValidationError as exc:
        raise RadarPanelError(f"FAILED: malformed radar.pool block: {exc}") from exc

    try:
        interval = _validated_interval(tunables_loader)
    except RadarPanelError:
        raise
    except Exception as exc:
        raise RadarPanelError(f"FAILED: tunables read failed: {type(exc).__name__}: {exc}") from exc

    scan_day = clock.to_et(pool.last_scan_at).date()
    try:
        raw_members = radar_store.members_for_day(pool_key, scan_day)
    except Exception as exc:
        raise RadarPanelError(
            f"FAILED: radar membership read failed: {type(exc).__name__}: {exc}"
        ) from exc
    try:
        records = [MembershipRecord.model_validate(item) for item in raw_members]
    except ValidationError as exc:
        raise RadarPanelError(f"FAILED: invalid radar membership row: {exc}") from exc
    if any(item.pool_key != pool_key or item.trade_date != scan_day for item in records):
        raise RadarPanelError(
            "FAILED: membership store returned a row outside the requested pool/day"
        )

    current_records = [
        item for item in records if item.entered_at is not None and item.left_at is None
    ]
    if len(current_records) != pool.members:
        raise RadarPanelError(
            f"FAILED: radar_pool.members={pool.members} but {len(current_records)} open admitted episodes were read"
        )
    departed_records = [
        item for item in records if item.entered_at is not None and item.left_at is not None
    ]
    excluded_records = [item for item in records if item.entered_at is None]
    ordered = lambda rows: sorted(
        rows, key=lambda item: (item.last_rank is None, item.last_rank or 10**9, item.id)
    )
    current = [_row(item, "current", since) for item in ordered(current_records)]
    departed = [_row(item, "departed", since) for item in ordered(departed_records)]
    excluded = [_row(item, "excluded", since) for item in ordered(excluded_records)]

    timestamps = [pool.last_scan_at]
    for item in records:
        timestamps.extend(
            x for x in (item.first_seen_at, item.entered_at, item.left_at) if x is not None
        )
    watermark = max(timestamps)
    if pool.last_scan_at > instant or watermark > instant:
        raise RadarPanelError("FAILED: radar snapshot contains a future timestamp")
    churn = None
    if since is not None:
        entered_ids = [
            item.id for item in records if item.entered_at is not None and item.entered_at > since
        ]
        left_ids = [
            item.id
            for item in records
            if item.entered_at is not None and item.left_at is not None and item.left_at > since
        ]
        churn = ChurnDelta(
            since=since,
            entered_episode_ids=entered_ids,
            left_episode_ids=left_ids,
            entered=len(entered_ids),
            left=len(left_ids),
        )

    clock_session = clock.session(instant)
    if pool.session not in SCANNED_SESSIONS:
        raise RadarPanelError(
            f"FAILED: stored scan session {pool.session.value!r} cannot name a rank metric"
        )
    rank_metric = getattr(block.rank_metric, pool.session.value)
    retained = scan_day != clock.to_et(instant).date()
    stale = instant - pool.last_scan_at > timedelta(seconds=2 * interval)
    banners: list[BannerView] = []
    if pool.degraded:
        names = (
            ", ".join(_source_name(value) for value in pool.degraded_sources) or "unknown source"
        )
        banners.append(BannerView(level="degraded", title="DEGRADED", detail=f"Sources: {names}"))
    if stale:
        banners.append(
            BannerView(
                level="stale",
                title="STALE",
                detail=f"Last scan is older than {2 * interval} seconds",
            )
        )
    if retained:
        banners.append(
            BannerView(
                level="retained",
                title="RETAINED PRIOR-DAY DATA",
                detail=f"Showing trading day {scan_day.isoformat()}",
            )
        )

    override_labels = []
    for key, override in block.overrides.items():
        pieces = []
        if override.rank_metric:
            pieces.append(f"metric {override.rank_metric}")
        if override.first_from:
            pieces.append(f"first from {override.first_from}")
        override_labels.append(f"{key} {' · '.join(pieces)}")
    return PoolView(
        pool_key=pool.pool_key,
        data_date=scan_day,
        clock_session=clock_session,
        scan_session=pool.session,
        rank_metric=rank_metric,
        override_labels=override_labels,
        cap=pool.cap,
        members=pool.members,
        current=current,
        departed=departed,
        excluded=excluded,
        last_scan_at=pool.last_scan_at,
        observed_watermark=watermark,
        scan_interval=interval,
        stale=stale,
        retained_prior_day=retained,
        banners=banners,
        churn=churn,
    )


def _decided_rung(instant: datetime, daymode_cfg) -> str:
    """Today's day-mode rung, READ-ONLY: the stored decision (no schema
    init, no note attestation) through the one `decided_or_stage1` rule."""
    from cobalt.daymode import DayModeStore, decided_or_stage1

    row = DayModeStore().for_date(session_clock().to_et(instant).date())
    return decided_or_stage1(row, daymode_cfg, now=instant)


def _dot_view(dot: Dot, *, live_card: bool, red: int, amber: int) -> DotView:
    tapped = dot.trader_grade is not None
    shown = dot.trader_grade if tapped else (dot.engine_grade if dot.role == "live" else None)
    hollow = shown is None
    colour_grade = dot.trader_grade if tapped else dot.engine_grade
    if tapped:
        why = f"you: {dot.trader_grade}"
        if dot.engine_grade is not None:
            why += f" · {dot.role} {dot.engine_grade}"
        if dot.engine_why:
            why += f" · {dot.engine_why}"
    elif dot.engine_why:
        why = dot.engine_why
    elif dot.role == "human":
        why = "your read — tap 1-10"
    else:
        why = f"{dot.factor}: {dot.na_reason or 'no engine grade'}"
    return DotView(
        factor=dot.factor, position=dot.position, source=dot.source, tier=dot.tier, role=dot.role,
        hollow=hollow, engine_grade=dot.engine_grade, trader_grade=dot.trader_grade, shown_grade=shown,
        colour=dot_colour(colour_grade, red_max=red, amber_max=amber), na_reason=dot.na_reason, why=why,
        owner="YOU" if dot.role == "human" or tapped else "COBALT", tappable=live_card,
    )


def _health_views(health: dict[str, Any] | None) -> list[HealthView]:
    if not health:
        return []
    pills = health.get("pills")
    if not isinstance(pills, list):
        raise RadarPanelError("FAILED: card health has no pills list")
    return [HealthView(label=p["label"], status=p["status"], note=p["note"]) for p in pills]


def build_ladder_view(
    *,
    card_store: CardStore | None = None,
    settings_store: TraderSettingsStore | None = None,
    clock=None,
    now: datetime | None = None,
    tunables_loader=load_tunables,
    rung_source=None,
) -> LadderView:
    """Read `"user".radar_cards_v` for today and build the ladder.

    The rung, the sheet dollars and the dot colour thresholds are read
    only when there is a card to render; an empty ladder needs none of
    them. Every read or validation failure is a loud `RadarPanelError`."""
    from cobalt.aset.engine import key_ladder
    from cobalt.settings.models import TraderSettings

    card_store = card_store or CardStore()
    clock = clock or session_clock()
    instant = now or now_utc()
    day = clock.to_et(instant).date()
    try:
        raw = card_store.radar_board_cards(day)
    except Exception as exc:
        raise RadarPanelError(f"FAILED: radar card read failed: {type(exc).__name__}: {exc}") from exc
    try:
        rows = [RadarCardRow.model_validate(item) for item in raw]
    except ValidationError as exc:
        raise RadarPanelError(f"FAILED: invalid radar card row: {exc}") from exc
    if not rows:
        return LadderView(active=[], terminal=[], empty_message="No radar cards today")

    settings_store = settings_store or TraderSettingsStore()
    try:
        trader = TraderSettings._build(settings_store.values(), where='"user".trader_settings')
        mode = (rung_source or _decided_rung)(instant, trader.daymode)
        sheet = trader.daymode.sheet_for(mode)
        enabled = trader.daymode.enabled_grades_for(mode)
        ladder_keys = key_ladder(trader.sheet_modes, sheet, enabled)
    except Exception as exc:
        raise RadarPanelError(
            f"FAILED: day mode / sheet for the key row unresolved: {type(exc).__name__}: {exc}"
        ) from exc
    try:
        red, amber = colour_thresholds(tunables_loader().by_key)
    except Exception as exc:
        raise RadarPanelError(f"FAILED: dot colour tunables: {type(exc).__name__}: {exc}") from exc

    order = ladder_order([
        LadderEntry(card_id=r.card_id, state=r.state, card_score=r.card_score, pool_position=r.pool_position,
                    ticker=r.ticker, promoted_at=r.promoted_at, state_at=r.state_at)
        for r in rows
    ])
    by_id = {r.card_id: r for r in rows}

    def view(position) -> CardView:
        r = by_id[position.card_id]
        live = r.state not in TERMINAL
        sign = Decimal(1) if r.direction == "long" else Decimal(-1)
        distance = abs(r.entry - r.stop)
        return CardView(
            id=r.card_id, ticker=r.ticker, direction=r.direction, state=r.state, setup=r.setup_ref or "",
            trade=r.trade_def_slug, why=r.why or "", trigger=r.entry, trigger_evidence=r.trigger_price,
            stop=r.stop, structural_stop=r.structural_stop, last=r.last_price,
            target_1r=r.entry + sign * distance, target_2r=r.entry + sign * distance * 2,
            grade=r.grade, tapped_grade=r.tapped_grade, sized_grade=r.sized_grade, snap_notice=r.snap_notice,
            proposed_key=r.proposed_key, score_suppressed=r.score_suppressed,
            keys=[
                KeyView(grade=k.grade.value, dollars=k.dollars, enabled=k.enabled,
                        proposed=r.proposed_key == k.grade.value, tapped=r.tapped_grade == k.grade.value,
                        sized=r.sized_grade == k.grade.value)
                for k in ladder_keys
            ],
            key_editable=r.state in KEY_EDITABLE, shares=r.shares, risk_budget=r.risk_budget,
            card_score=r.card_score, conviction=r.conviction, proximity=r.proximity,
            pool_position=r.pool_position, rank_chip=position.rank_chip, promoted=position.promoted,
            outside_pool=r.outside_pool,
            dots=[_dot_view(d, live_card=live, red=red, amber=amber) for d in r.dots],
            health=_health_views(r.health), badges=dict(FIELD_OWNERS), state_at=r.state_at,
            formed_at=r.formed_at, expires_at=r.expires_at, scan_id=r.scan_id, board_evaluation=r.board_evaluation,
        )

    return LadderView(
        active=[view(p) for p in order.active],
        terminal=[view(p) for p in order.terminal],
        empty_message=None,
        rung=f"{mode} · {sheet} sheet · enabled {', '.join(g.value for g in enabled) or 'none'}",
    )


def build_radar_panel(
    *,
    since: datetime | None,
    snapshot: bool,
    radar_store: RadarStore | None = None,
    settings_store: TraderSettingsStore | None = None,
    card_store: CardStore | None = None,
    clock=None,
    now: datetime | None = None,
    tunables_loader=load_tunables,
    rung_source=None,
) -> RadarPanelView:
    pool = build_pool_view(
        since=since,
        snapshot=snapshot,
        radar_store=radar_store,
        settings_store=settings_store,
        clock=clock,
        now=now,
        tunables_loader=tunables_loader,
    )
    ladder = build_ladder_view(
        card_store=card_store, settings_store=settings_store, clock=clock, now=now,
        tunables_loader=tunables_loader, rung_source=rung_source,
    )
    return RadarPanelView(pool=pool, ladder=ladder)


def _fmt_dt(value: datetime | None) -> str:
    return "—" if value is None else value.isoformat(timespec="seconds")


def _rank_value_cell(row: PoolRow) -> str:
    """The metric that ranked this row and its stored value, e.g.
    `volume 1234567` or `rvol 3.25`. A pre-deploy row (both NULL) is a
    dash; a metric with no value prints the name and a dash. The value is
    the stored NUMERIC with trailing zeros dropped — never rounded."""
    if row.rank_metric is None:
        return "—"
    if row.rank_value is None:
        return f"{row.rank_metric} —"
    return f"{row.rank_metric} {format(row.rank_value.normalize(), 'f')}"


def _pool_table(rows: list[PoolRow], title: str) -> str:
    e = html.escape

    def render_row(row: PoolRow) -> str:
        entered_badge = '<b class="churn-in">ENTERED</b>' if row.entered_since else ""
        left_badge = '<b class="churn-out">LEFT</b>' if row.left_since else ""
        return (
            f'<tr data-episode-id="{row.episode_id}" data-category="{row.category}">'
            f'<td class="mono">{e(str(row.position or "—"))}</td><td class="ticker">{e(row.ticker)}</td>'
            f'<td class="mono rank-value">{e(_rank_value_cell(row))}</td>'
            f"<td>{e(row.session.value)}</td><td>{e(row.source)}</td>"
            f"<td>{e(_fmt_dt(row.entered_at))} {entered_badge}</td>"
            f"<td>{e(_fmt_dt(row.left_at))} {left_badge}</td>"
            f"<td>{e(row.excluded_by or '—')}</td></tr>"
        )

    body = "".join(render_row(row) for row in rows)
    if not body:
        body = '<tr><td colspan="8" class="muted">none</td></tr>'
    return (
        f'<h3>{e(title)} <span class="count">{len(rows)}</span></h3>'
        "<table><thead><tr><th>rank</th><th>ticker</th><th>value</th><th>session</th><th>source</th>"
        f"<th>entered</th><th>left</th><th>excluded by</th></tr></thead><tbody>{body}</tbody></table>"
    )


def render_pool(view: PoolView) -> str:
    """Pure HTML renderer for the complete refreshable pool layer."""
    e = html.escape
    banners = "".join(
        f'<div class="panel-banner {banner.level}"><b>{e(banner.title)}</b> · {e(banner.detail)}</div>'
        for banner in view.banners
    )
    churn = ""
    if view.churn is not None:
        churn = (
            f'<span id="churn">since {e(_fmt_dt(view.churn.since))}: '
            f'<b class="churn-in">+{view.churn.entered}</b> entered · '
            f'<b class="churn-out">−{view.churn.left}</b> left</span>'
        )
    overrides = " · ".join(e(value) for value in view.override_labels)
    classes = "pool-layer stale-data" if view.stale else "pool-layer"
    return f'''<section id="pool-layer" class="{classes}" data-watermark="{e(view.observed_watermark.isoformat())}">
<div id="refresh-status"></div>{banners}
<header class="layer-head"><div><span class="eyebrow">POOL VIEW · LIVE</span><h2>{e(view.pool_key.upper())}</h2></div>
<div class="pool-stats"><b>{view.members}</b> / {view.cap} admitted · clock {e(view.clock_session.value)} · scan {e(view.scan_session.value)} · rank by {e(view.rank_metric)}</div></header>
<div class="pool-meta">Trading day {view.data_date.isoformat()} · last scan {e(_fmt_dt(view.last_scan_at))} · refresh {view.scan_interval}s {churn}</div>
<div class="override-line">{overrides}</div>
{_pool_table(view.current, "Current admitted")}
<details><summary>Departed admitted · {len(view.departed)}</summary>{_pool_table(view.departed, "Departed admitted")}</details>
<details><summary>Never-admitted exclusions · {len(view.excluded)}</summary>{_pool_table(view.excluded, "Never-admitted exclusions")}</details>
</section>'''


def _badge(owner: str) -> str:
    return f'<span class="badge badge-{html.escape(owner.lower())}">{html.escape(owner)}</span>'


def _field(card: CardView, field: str, label: str, value: Any, *, tag: str = "span") -> str:
    """One displayed card field: its label, its owner badge, its value."""
    shown = "—" if value is None or value == "" else str(value)
    return (
        f'<{tag} class="field" data-field="{field}">{html.escape(label)} {_badge(card.badges[field])} '
        f'<b>{html.escape(shown)}</b></{tag}>'
    )


def _dot_html(card: CardView, dot: DotView) -> str:
    e = html.escape
    fill = "hollow" if dot.hollow else "filled"
    colour = "" if dot.colour is None else f" colour-{dot.colour}"
    if dot.shown_grade is not None:
        value = str(dot.shown_grade)
    elif dot.engine_grade is not None:
        value = f"{dot.role} {dot.engine_grade}"
    elif dot.na_reason:
        value = f"n/a {dot.na_reason}"
    else:
        value = "tap"
    button = (
        f'<button class="dot {fill} role-{dot.role}{colour}" type="button" data-dot-toggle="1" '
        f'data-card-id="{card.id}" data-factor="{e(dot.factor)}" title="{e(dot.why)}">'
        f"{e(dot.factor)} · {e(value)} {_badge(dot.owner)}</button>"
    )
    strip = ""
    if dot.tappable:
        taps = "".join(
            f'<button class="tap" type="button" data-grade="{n}">{n}</button>' for n in range(1, 11)
        )
        strip = (
            f'<div class="tap-strip" data-card-id="{card.id}" data-factor="{e(dot.factor)}" hidden>{taps}</div>'
        )
    return f'<div class="dot-cell">{button}<span class="dot-why">{e(dot.why)}</span>{strip}</div>'


def _key_row(card: CardView) -> str:
    e = html.escape
    if not card.key_editable:
        return (
            f'<div class="key-row frozen">key {e(card.grade or "—")} · tapped {e(card.tapped_grade or "—")} · '
            f"frozen in {e(card.display_state)}</div>"
        )
    buttons = []
    for key in card.keys:
        classes = ["key"]
        if not key.enabled:
            classes.append("key-disabled")
        if key.proposed:
            classes.append("key-proposed")
        if key.sized:
            classes.append("key-sized")
        note = "enabled today" if key.enabled else "not enabled today — a tap sizes at the nearest enabled key below"
        buttons.append(
            f'<button class="{" ".join(classes)}" data-card-id="{card.id}" data-key="{e(key.grade)}" '
            f'type="button" title="{e(note)}">{e(key.grade)} · ${e(str(key.dollars))}</button>'
        )
    buttons.append(
        f'<button class="key key-pass" data-card-id="{card.id}" data-key="pass" type="button">pass</button>'
    )
    return f'<div class="key-row">{"".join(buttons)}</div>'


def _card_detail(card: CardView) -> str:
    e = html.escape
    health = "".join(
        f'<span class="health {item.status.replace("/", "-")}" title="{e(item.note)}">'
        f"{e(item.label)} · {item.status}</span>"
        for item in card.health
    )
    troubled = sum(item.status in ("warn", "bad") for item in card.health)
    if not card.health:
        health_summary = "no pills — health is checked once the card is in trade"
    else:
        health_summary = "all holding" if troubled == 0 else f"{troubled} deteriorating"
    dots = "".join(_dot_html(card, dot) for dot in card.dots)
    snap = f'<div class="snap-notice">{e(card.snap_notice)}</div>' if card.snap_notice else ""
    proposed = card.proposed_key or "tap to propose"
    suppressed = (
        f'<div class="suppressed">score suppressed: {e(card.score_suppressed)}</div>' if card.score_suppressed else ""
    )
    if card.state is CardState.WATCH:
        state_body = (
            f'<div class="state-block watch-state"><b>WATCH</b> · proposed key {e(proposed)} · '
            f"trigger {e(str(card.trigger))} · stop {e(str(card.stop))}</div>"
        )
    elif card.state is CardState.ARMED:
        state_body = (
            f'<div class="state-block armed-state"><b>ARMED · LOCKED</b>'
            f'<div class="trigger-distance">last {e(str(card.last or "—"))} · trigger {e(str(card.trigger))}</div>'
            f"<div>key {e(card.grade or '—')} · {card.shares if card.shares is not None else '—'} sh · stop {e(str(card.stop))}</div></div>"
        )
    elif card.state is CardState.TRIGGERED:
        state_body = (
            f'<div class="state-block triggered-state"><b>TRIGGERED</b>'
            f'<div class="strike-numbers"><span>KEY {e(card.grade or "—")}</span>'
            f"<span>SHARES {card.shares if card.shares is not None else '—'}</span><span>STOP {e(str(card.stop))}</span></div></div>"
        )
    else:
        state_body = (
            f'<div class="state-block in-trade-state"><b>IN-TRADE</b> · stop {e(str(card.stop))} · '
            f"next exits {e(str(card.target_1r))} / {e(str(card.target_2r))}</div>"
        )
    outside = '<span class="outside-pool">OUTSIDE POOL</span>' if card.outside_pool else ""
    chip = "—" if card.card_score is None else str(card.card_score)
    rank = "—" if card.rank_chip is None else f"#{card.rank_chip}"
    return f'''<div class="expanded" data-state="{e(card.display_state)}">
<div class="card-pane">
 <div class="card-title"><span class="rank-chip">{rank} · {chip}</span><strong>{e(card.ticker)}</strong>
 <span class="direction {card.direction}">{"↑" if card.direction == "long" else "↓"}</span>
 <span>{e(card.setup)} → {e(card.trade)}</span>{outside}</div>
 <p class="why-line">{_field(card, "why", "why", card.why)}</p>
 <div class="semaphore">{dots}</div>
 <div class="health-line">{health}<b>{e(health_summary)}</b></div>
 {state_body}
 {_key_row(card)}{snap}{suppressed}
 <div class="card-status" data-card-id="{card.id}"></div>
</div>
<aside class="detail-pane">
 <section data-detail="levels"><h4>LEVELS</h4><div class="fields">{_field(card, "entry", "trigger", card.trigger)}{_field(card, "stop", "stop", card.stop)}{_field(card, "trigger_price", "trigger at formation", card.trigger_evidence)}{_field(card, "structural_stop", "structural stop at formation", card.structural_stop)}{_field(card, "last_price", "last", card.last)}<span class="field">1R <b>{e(str(card.target_1r))}</b></span><span class="field">2R <b>{e(str(card.target_2r))}</b></span></div></section>
 <section data-detail="rank"><h4>RANK + WHY</h4><div class="fields">{_field(card, "card_score", "score", card.card_score)}{_field(card, "conviction", "conviction", card.conviction)}{_field(card, "proximity", "proximity", card.proximity)}{_field(card, "pool_position", "pool", card.pool_position)}{_field(card, "proposed_key", "proposed key", card.proposed_key or "tap to propose")}{_field(card, "tapped_grade", "tapped", card.tapped_grade)}{_field(card, "sized_grade", "sized", card.sized_grade)}{_field(card, "grade", "key", card.grade)}{_field(card, "shares", "shares", card.shares)}{_field(card, "risk_budget", "risk $", card.risk_budget)}{_field(card, "snap_notice", "snap", card.snap_notice)}{_field(card, "score_suppressed", "suppressed", card.score_suppressed)}</div></section>
 <section data-detail="card"><h4>CARD</h4><div class="fields">{_field(card, "ticker", "ticker", card.ticker)}{_field(card, "direction", "direction", card.direction)}{_field(card, "state", "state", card.display_state)}{_field(card, "setup_ref", "setup", card.setup)}{_field(card, "trade_def_slug", "trade", card.trade)}{_field(card, "formed_at", "formed", _fmt_dt(card.formed_at))}{_field(card, "expires_at", "expires", _fmt_dt(card.expires_at))}{_field(card, "health", "health", health_summary)}{_field(card, "outside_pool", "outside pool", "yes" if card.outside_pool else "no")}{_field(card, "scan_id", "scan", card.scan_id)}</div></section>
 <section data-detail="news"><h4>NEWS</h4><p>no news source wired to radar cards (S3)</p></section>
 <section data-detail="notes"><h4>NOTES</h4><p>no notes source wired to radar cards (S3)</p></section>
 <section data-detail="chart"><h4>CHART</h4><p>reserved · empty</p></section>
</aside></div>'''


def render_ladder(view: LadderView) -> str:
    """Pure HTML renderer for the card ladder."""
    e = html.escape
    if view.empty_message:
        active_html = f'<div class="empty-state">{e(view.empty_message)}</div>'
    else:
        rows = []
        for index, card in enumerate(view.active, start=1):
            open_class = " open" if index <= 2 else ""
            promote = ""
            if card.promoted:
                promote = (
                    f'<button class="promote" data-card-id="{card.id}" data-promote="release" '
                    'type="button">release ↓</button>'
                )
            elif card.state is CardState.WATCH and index >= 3:
                promote = (
                    f'<button class="promote" data-card-id="{card.id}" data-promote="promote" '
                    'type="button" title="pin to #2">promote ↑</button>'
                )
            score = "—" if card.card_score is None else str(card.card_score)
            rows.append(
                f'<article class="ladder-item{open_class}" data-card-id="{card.id}">'
                f'<button class="strip" type="button" data-toggle-card="{card.id}"><span>#{index} · {score}</span>'
                f"<b>{e(card.ticker)}</b><span>{e(card.setup)} → {e(card.trade)}</span>"
                f"<span>{e(card.display_state)} · {e(card.grade or 'no key')} · "
                f"{card.shares if card.shares is not None else '—'} sh · stop {e(str(card.stop))}</span></button>"
                f"{_card_detail(card)}{promote}</article>"
            )
        active_html = "".join(rows)
    terminal_groups = []
    for state in (CardState.CLOSED, CardState.PASSED, CardState.EXPIRED, CardState.MISSED):
        cards = [card for card in view.terminal if card.state is state]
        if not cards:
            continue
        group_rows = "".join(
            f'<div class="terminal-row"><span>{e(card.display_state)}</span><b>{e(card.ticker)}</b>'
            f"<span>{e(card.direction)} · {e(card.grade or 'no key')} · "
            f"{card.shares if card.shares is not None else '—'} sh · stop {e(str(card.stop))}</span>"
            f"<time>{e(_fmt_dt(card.state_at))}</time></div>"
            for card in cards
        )
        terminal_groups.append(f"<h4>{state.value} · {len(cards)}</h4>{group_rows}")
    terminal_rows = "".join(terminal_groups) or '<div class="muted">none</div>'
    rung = f'<div class="rung-line">{e(view.rung)}</div>' if view.rung else ""
    return f"""<section id="ladder-layer"><header class="layer-head"><div><span class="eyebrow">CARD LADDER</span><h2>TRADE RADAR</h2>{rung}</div>
<div class="ladder-actions"><button id="collapse-all" type="button">collapse all</button><button id="top-two" type="button">top 2</button></div></header>
<div id="ladder">{active_html}</div>
<details class="terminal"><summary>TERMINAL · {len(view.terminal)}</summary>{terminal_rows}</details></section>"""


PANEL_CSS = r"""
:root{color-scheme:dark;--surface:#0d1117;--card:#11151c;--border:#1f2531;--text:#e6e9ef;--muted:#7d8595;--blue:#4f8dff;--amber:#d9a24a;--green:#35c77a;--red:#ef5b6b}
*{box-sizing:border-box}body{margin:0;background:var(--surface);color:var(--text);font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.radar-wrap{max-width:1440px;margin:auto;padding:20px}a{color:var(--blue)}h2{margin:3px 0}.eyebrow,.mono,.rank-chip,.ticker,button,th{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.08em}.eyebrow,.muted,.pool-meta,.override-line{color:var(--muted);font-size:12px}.layer-head{display:flex;align-items:center;justify-content:space-between;gap:16px;margin:18px 0}.pool-stats{text-align:right}.panel-banner,.refresh-failure{padding:10px 12px;border:1px solid var(--red);background:#351019;color:#ffd0d6;border-radius:7px;margin:7px 0}.retained{border-color:var(--amber);background:#2d2412}.stale-data{outline:2px solid var(--red);outline-offset:5px}.refresh-failed{opacity:.65}table{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--border)}th,td{text-align:left;padding:8px;border-bottom:1px solid var(--border);font-size:12px}.ticker{font-weight:800;font-size:15px}.count,.churn-in{color:var(--green)}.churn-out{color:var(--red)}details{margin:12px 0}summary{cursor:pointer;color:#aeb5c2}.ladder-actions button,.strip,.promote,.dot,.key,.tap{background:var(--card);border:1px solid var(--border);color:var(--text);border-radius:7px}.ladder-actions button{padding:8px;margin-left:7px}.ladder-item{position:relative;margin:8px 0}.strip{width:100%;height:52px;padding:0 18px;display:grid;grid-template-columns:110px 90px 1fr auto;gap:12px;align-items:center;text-align:left}.expanded{display:none;grid-template-columns:minmax(520px,1fr) minmax(360px,1fr);gap:18px;border:1px solid var(--blue);border-top:0;padding:12px;background:#0b0f15}.ladder-item.open .expanded{display:grid}.card-pane,.detail-pane{background:var(--card);border:1px solid var(--border);padding:18px}.card-title{display:flex;gap:10px;align-items:center;flex-wrap:wrap}.card-title strong{font:800 28px ui-monospace,SFMono-Regular,Menlo,monospace}.direction.long{color:var(--green)}.direction.short{color:var(--red)}.rank-chip{border:1px solid var(--border);padding:4px}.badge{font:9px ui-monospace,SFMono-Regular,Menlo,monospace;border:1px solid var(--blue);padding:1px 3px;color:var(--blue);border-radius:3px}.badge-you{color:var(--amber);border-color:var(--amber)}.badge-ledger{color:var(--muted);border-color:var(--muted)}.why-line{color:#aeb5c2}.semaphore,.health-line{display:flex;gap:7px;align-items:flex-start;flex-wrap:wrap;padding:12px 0;border-top:1px solid var(--border)}.dot-cell{display:flex;flex-direction:column;gap:4px;max-width:260px}.dot{min-height:34px}.dot.hollow{background:transparent;border-style:dashed}.dot.filled.colour-0{background:#3a1119;border-color:var(--red)}.dot.filled.colour-1{background:#2d2412;border-color:var(--amber)}.dot.filled.colour-2{background:#0f2a1c;border-color:var(--green)}.dot.hollow.colour-0{border-color:var(--red)}.dot.hollow.colour-1{border-color:var(--amber)}.dot.hollow.colour-2{border-color:var(--green)}.dot-why{font-size:11px;color:var(--muted)}.tap-strip{display:grid;grid-template-columns:repeat(10,1fr);gap:3px}.tap-strip[hidden]{display:none}.tap{min-height:36px;min-width:30px}.key-row{display:flex;gap:6px;flex-wrap:wrap;padding:10px 0}.key{min-height:44px;padding:0 12px}.key-disabled{opacity:.45}.key-proposed{border-color:var(--blue);box-shadow:0 0 0 1px var(--blue)}.key-sized{border-color:var(--green)}.key-row.frozen{color:var(--muted)}.snap-notice{border:1px solid var(--amber);background:#2d2412;color:#ffe2b0;padding:8px;border-radius:6px;font-weight:700}.suppressed{color:var(--muted);font-size:12px;padding:4px 0}.card-status{font-size:12px;min-height:16px}.card-status.refused{color:var(--red);font-weight:700}.card-status.ok{color:var(--green)}.outside-pool{border:1px solid var(--amber);color:var(--amber);padding:2px 6px;font:11px ui-monospace,SFMono-Regular,Menlo,monospace}.rung-line{font-size:12px;color:var(--muted)}.fields{display:grid;grid-template-columns:1fr;gap:4px}.field{font-size:12px;color:var(--muted)}.field b{color:var(--text)}.health{padding:4px 7px;border-radius:10px;font-size:11px}.health.ok{color:var(--green);border:1px solid var(--green)}.health.warn{color:var(--amber);border:1px solid var(--amber)}.health.bad{color:var(--red);border:1px solid var(--red)}.health.n-a{color:var(--muted);border:1px dashed var(--red)}.state-block{padding:14px 0}.trigger-distance{font:700 24px ui-monospace,SFMono-Regular,Menlo,monospace;padding:12px 0}.triggered-state{border:1px solid var(--green);padding:18px}.strike-numbers{display:flex;gap:24px;font:800 24px ui-monospace,SFMono-Regular,Menlo,monospace;margin-top:12px}.detail-pane h4,.terminal h4{font:11px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--muted);letter-spacing:.12em}.promote{position:absolute;right:-2px;top:55px;min-height:44px}.terminal{margin-top:24px}.terminal-row{height:52px;opacity:.55;border:1px solid var(--border);background:var(--card);display:grid;grid-template-columns:100px 100px 1fr auto;align-items:center;padding:0 18px;margin:6px 0}.empty-state{border:1px dashed var(--border);padding:28px;color:var(--muted)}
@media (max-width:1149px){.expanded{grid-template-columns:1fr}.detail-pane{grid-row:2}}
@media (max-width:700px){.strip{grid-template-columns:75px 70px 1fr}.strip span:nth-child(4){display:none}.radar-wrap{padding:10px}.pool-stats{text-align:left}.layer-head{align-items:flex-start;flex-direction:column}table{display:block;overflow-x:auto}}
@media (max-width:430px){body,.phone-frame{width:100%}.radar-wrap{width:366px;max-width:100%;padding:8px}.expanded{padding:5px}.card-pane,.detail-pane{padding:11px}.card-title strong{font-size:24px}.strip{padding:0 8px}.terminal-row{grid-template-columns:75px 65px 1fr}.terminal-row time{display:none}}
.phone-frame{width:390px;margin:auto;border:12px solid #05070a;border-radius:26px}.phone-frame .radar-wrap{width:366px;padding:8px}
"""


PANEL_JS = r"""
(function(){
 const items=()=>Array.from(document.querySelectorAll('.ladder-item'));
 function collapseAll(){items().forEach(x=>x.classList.remove('open'));}
 function topTwo(){items().forEach((x,i)=>x.classList.toggle('open',i<2));}
 function openIds(){return items().filter(x=>x.classList.contains('open')).map(x=>x.dataset.cardId);}
 function status(cardId,text,level){
   const box=document.querySelector('.card-status[data-card-id="'+cardId+'"]');
   if(box){box.textContent=text; box.className='card-status '+level;}
 }
 async function refreshLadder(){
   const keep=openIds();
   const response=await fetch('/radar',{headers:{accept:'text/html'}});
   if(!response.ok){throw new Error('HTTP '+response.status);}
   const doc=new DOMParser().parseFromString(await response.text(),'text/html');
   const next=doc.getElementById('ladder-layer');
   if(!next){throw new Error('the /radar page returned no ladder');}
   document.getElementById('ladder-layer').replaceWith(next);
   items().forEach(x=>x.classList.toggle('open',keep.indexOf(x.dataset.cardId)>=0));
 }
 async function post(cardId,path,body){
   status(cardId,'sending','pending');
   try{
     const response=await fetch('/radar/card/'+cardId+path,{method:'POST',headers:{'content-type':'application/x-www-form-urlencoded'},body:new URLSearchParams(body||{})});
     const payload=await response.json().catch(()=>({}));
     if(!response.ok){status(cardId,'REFUSED '+response.status+' · '+(payload.reason||payload.error||'no reason given'),'refused'); return;}
     await refreshLadder();
     status(cardId,payload.snap_notice?('saved · '+payload.snap_notice):'saved','ok');
   }catch(failure){status(cardId,'FAILED · '+String(failure),'refused');}
 }
 document.addEventListener('click',function(event){
   const target=event.target;
   if(target.closest('#collapse-all')){collapseAll(); return;}
   if(target.closest('#top-two')){topTwo(); return;}
   const strip=target.closest('[data-toggle-card]');
   if(strip){strip.closest('.ladder-item').classList.toggle('open'); return;}
   const dot=target.closest('[data-dot-toggle]');
   if(dot){const tray=dot.parentElement.querySelector('.tap-strip'); if(tray){tray.hidden=!tray.hidden;} return;}
   const grade=target.closest('.tap-strip [data-grade]');
   if(grade){const tray=grade.closest('.tap-strip'); post(tray.dataset.cardId,'/dot/'+encodeURIComponent(tray.dataset.factor),{grade:grade.dataset.grade}); return;}
   const key=target.closest('[data-key]');
   if(key){post(key.dataset.cardId,'/key',{grade:key.dataset.key}); return;}
   const promote=target.closest('[data-promote]');
   if(promote){post(promote.dataset.cardId,promote.dataset.promote==='release'?'/release':'/promote'); return;}
 });
 let cursor=document.getElementById('pool-layer').dataset.watermark;
 const interval=Number(document.body.dataset.refreshSeconds)*1000;
 async function refreshPool(){
   const oldLayer=document.getElementById('pool-layer');
   try{
     const response=await fetch('/api/radar/pool?since='+encodeURIComponent(cursor),{headers:{accept:'application/json'}});
     if(!response.ok){throw new Error('HTTP '+response.status);}
     const payload=await response.json();
     const holder=document.createElement('div'); holder.innerHTML=payload.html;
     const next=holder.firstElementChild; if(!next){throw new Error('empty pool fragment');}
     oldLayer.replaceWith(next); cursor=payload.pool.observed_watermark;
   }catch(error){
     oldLayer.classList.add('refresh-failed','stale-data');
     oldLayer.querySelector('#refresh-status').innerHTML='<div class="refresh-failure"><b>REFRESH FAILED</b> · retained data is stale · '+String(error)+'</div>';
   }
 }
 window.COBALT_RADAR={collapseAll:collapseAll,topTwo:topTwo,refreshPool:refreshPool,refreshLadder:refreshLadder};
 window.setInterval(refreshPool,interval);
})();
"""


def render_radar_page(view: RadarPanelView, *, phone_frame: bool = False) -> str:
    frame_class = "phone-frame" if phone_frame else ""
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Cobalt · Trade Radar</title><style>{PANEL_CSS}</style></head>
<body class="{frame_class}" data-refresh-seconds="{view.pool.scan_interval}"><main class="radar-wrap"><nav><a href="/">ASET sheet</a></nav>{render_ladder(view.ladder)}{render_pool(view.pool)}</main><script>{PANEL_JS}</script></body></html>'''


def render_failed_page(message: str, *, phone_frame: bool = False) -> str:
    frame_class = "phone-frame" if phone_frame else ""
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Cobalt · Trade Radar · FAILED</title><style>{PANEL_CSS}</style></head><body class="{frame_class}"><main class="radar-wrap"><nav><a href="/">ASET sheet</a></nav><div class="panel-banner degraded"><b>FAILED</b> · {html.escape(message)}</div></main></body></html>'''


def pool_api_payload(view: PoolView) -> dict[str, Any]:
    return {"pool": view.model_dump(mode="json"), "html": render_pool(view)}


__all__ = [
    "BADGED_FIELDS",
    "PANEL_CSS",
    "PANEL_JS",
    "BannerView",
    "CardView",
    "ChurnDelta",
    "DotView",
    "HealthView",
    "KeyView",
    "LadderView",
    "MembershipRecord",
    "PoolRow",
    "PoolView",
    "RadarCardRow",
    "RadarPanelError",
    "RadarPanelView",
    "build_ladder_view",
    "build_pool_view",
    "build_radar_panel",
    "parse_since",
    "pool_api_payload",
    "render_failed_page",
    "render_ladder",
    "render_pool",
    "render_radar_page",
]
