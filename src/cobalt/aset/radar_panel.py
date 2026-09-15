"""Read-only Trade Radar panel view models, builder, and HTML renderers."""

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
    model_validator,
)

from cobalt.cards import TERMINAL, CardState, CardStore, Origin
from cobalt.radar.models import PoolBlock
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


class DotView(_ViewModel):
    label: str = Field(min_length=1)
    score: Literal[0, 1, 2] | None
    grade: int = Field(ge=1, le=10)
    why: str = Field(min_length=1)


class HealthView(_ViewModel):
    label: str = Field(min_length=1)
    status: Literal["ok", "warn", "bad"]
    note: str = Field(min_length=1)


class CardView(_ViewModel):
    id: int
    ticker: str = Field(min_length=1)
    direction: Literal["long", "short"]
    state: CardState
    setup: str = Field(min_length=1)
    trade: str = Field(min_length=1)
    why: str = Field(min_length=1)
    trigger: Decimal
    last: Decimal
    stop: Decimal
    target_1r: Decimal | None = None
    target_2r: Decimal | None = None
    grade: str = Field(min_length=1)
    proposed_key: str = Field(min_length=1)
    enabled_grades: list[str]
    shares: int = Field(ge=0)
    owner: Literal["COBALT", "YOU", "N/A MANUAL"]
    source: str = Field(min_length=1)
    card_score: int = Field(ge=0)
    conviction: float = Field(ge=0, le=1)
    proximity: float = Field(ge=0, le=1)
    pool_position: int = Field(ge=1)
    dots: list[DotView]
    health: list[HealthView]
    trails: list[str]
    default_trail: str | None
    trail_why: list[str]
    attempt: int = Field(ge=0)
    attempt_max: int = Field(ge=1)
    news: str
    notes: str
    state_at: datetime
    degraded: bool
    contract: str | None = None

    @field_validator("state_at")
    @classmethod
    def _state_at_aware(cls, value: datetime) -> datetime:
        return _aware(value, "state_at")  # type: ignore[return-value]

    @model_validator(mode="after")
    def _targets(self) -> CardView:
        if self.contract is not None:
            if self.target_1r is None or self.target_2r is None:
                raise ValueError("contract cards must supply target_1r and target_2r")
            return self
        distance = abs(self.trigger - self.stop)
        sign = Decimal(1) if self.direction == "long" else Decimal(-1)
        self.target_1r = self.trigger + sign * distance
        self.target_2r = self.trigger + sign * distance * 2
        return self

    @property
    def display_state(self) -> str:
        return "IN-TRADE" if self.state is CardState.FILLED else self.state.value

    @classmethod
    def from_contract(cls, row: dict[str, Any], **presentation: Any) -> CardView:
        """Adapt a hub-cut sizing-shape row plus its supplied UI contract.

        The fixture deliberately retains the real ``aset_sizings`` column
        shape.  UI-only fields are explicit arguments so this adapter cannot
        silently invent WHY, dots, health, or trails.
        """
        required = {
            "setup",
            "trade",
            "why",
            "dots",
            "health",
            "trails",
            "default_trail",
            "trail_why",
            "attempt",
            "attempt_max",
            "news",
            "notes",
        }
        missing = sorted(required - presentation.keys())
        if missing:
            raise RadarPanelError(
                f"contract card presentation fields missing: {', '.join(missing)}"
            )
        try:
            return cls(
                id=row["id"],
                ticker=row["ticker"],
                direction=row["direction"],
                state=row["state"],
                trigger=row["entry"],
                last=row["last_price"],
                stop=row["stop"],
                target_1r=row["target_1r"],
                target_2r=row["target_2r"],
                grade=row["grade"],
                proposed_key=row["grade"],
                enabled_grades=["A", "B"],
                shares=row["shares"],
                owner=row["owner"],
                source=row.get("price_source") or f"{row['origin']}:fixture",
                card_score=row["card_score"],
                conviction=row["conviction"],
                proximity=row["proximity"],
                pool_position=row["pool_position"],
                state_at=row["state_at"],
                degraded=row["degraded"],
                contract=row.get("_contract"),
                **presentation,
            )
        except (KeyError, ValidationError, TypeError) as exc:
            raise RadarPanelError(f"invalid contract card: {exc}") from exc


class LadderView(_ViewModel):
    active: list[CardView]
    terminal: list[CardView]
    empty_message: str | None


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


def order_cards(cards: list[CardView]) -> LadderView:
    pinned_states = {CardState.ARMED, CardState.TRIGGERED, CardState.FILLED}
    terminal = sorted(
        (card for card in cards if card.state in TERMINAL),
        key=lambda card: (card.state.value, card.state_at, card.ticker),
    )
    pinned = sorted(
        (card for card in cards if card.state in pinned_states),
        key=lambda card: (card.pool_position, -card.card_score, card.ticker),
    )
    watch = sorted(
        (card for card in cards if card.state is CardState.WATCH),
        key=lambda card: (-card.card_score, card.pool_position, card.ticker),
    )
    return LadderView(
        active=[*pinned, *watch],
        terminal=terminal,
        empty_message=None if cards else "No radar cards — F8 lands in S2-P2",
    )


def build_ladder_view(*, card_store: CardStore | None = None) -> LadderView:
    card_store = card_store or CardStore()
    try:
        rows = card_store.open_cards()
    except Exception as exc:
        raise RadarPanelError(
            f"FAILED: radar card read failed: {type(exc).__name__}: {exc}"
        ) from exc
    radar_rows = [row for row in rows if str(row.get("origin")) == Origin.RADAR.value]
    if radar_rows:
        raise RadarPanelError(
            "FAILED: radar cards exist but the card contract is not wired — S2-P2"
        )
    return order_cards([])


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
    return RadarPanelView(pool=pool, ladder=build_ladder_view(card_store=card_store))


def _fmt_dt(value: datetime | None) -> str:
    return "—" if value is None else value.isoformat(timespec="seconds")


def _pool_table(rows: list[PoolRow], title: str) -> str:
    e = html.escape

    def render_row(row: PoolRow) -> str:
        entered_badge = '<b class="churn-in">ENTERED</b>' if row.entered_since else ""
        left_badge = '<b class="churn-out">LEFT</b>' if row.left_since else ""
        return (
            f'<tr data-episode-id="{row.episode_id}" data-category="{row.category}">'
            f'<td class="mono">{e(str(row.position or "—"))}</td><td class="ticker">{e(row.ticker)}</td>'
            f"<td>{e(row.session.value)}</td><td>{e(row.source)}</td>"
            f"<td>{e(_fmt_dt(row.entered_at))} {entered_badge}</td>"
            f"<td>{e(_fmt_dt(row.left_at))} {left_badge}</td>"
            f"<td>{e(row.excluded_by or '—')}</td></tr>"
        )

    body = "".join(render_row(row) for row in rows)
    if not body:
        body = '<tr><td colspan="7" class="muted">none</td></tr>'
    return (
        f'<h3>{e(title)} <span class="count">{len(rows)}</span></h3>'
        "<table><thead><tr><th>rank</th><th>ticker</th><th>session</th><th>source</th>"
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


def _owner_badge(owner: str) -> str:
    return f'<span class="owner owner-{html.escape(owner.lower().replace(" ", "-").replace("/", "-"))}">{html.escape(owner)}</span>'


def _card_detail(card: CardView) -> str:
    e = html.escape
    health = "".join(
        f'<span class="health {item.status}" title="{e(item.note)}">{e(item.label)} · {item.status}</span>'
        for item in card.health
    )
    troubled = sum(item.status != "ok" for item in card.health)
    health_summary = "all holding" if troubled == 0 else f"{troubled} deteriorating"
    dots = "".join(
        f'<button class="dot score-{item.score if item.score is not None else "judgment"}" '
        f'title="S2-P2" disabled>{e(item.label)} · {item.grade} '
        f"{_owner_badge('YOU' if item.score is None else 'COBALT')}</button>"
        for item in card.dots
    )
    trails = ", ".join(e(item) for item in card.trails) or "—"
    if card.state is CardState.WATCH:
        state_body = (
            f'<div class="state-block watch-state"><b>WATCH</b> · proposed key {e(card.proposed_key)} · '
            f"trigger {e(str(card.trigger))} · stop {e(str(card.stop))} · {card.shares} sh</div>"
        )
    elif card.state is CardState.ARMED:
        state_body = (
            f'<div class="state-block armed-state"><b>ARMED · LOCKED</b>'
            f'<div class="trigger-distance">last {e(str(card.last))} · trigger {e(str(card.trigger))}</div>'
            f"<div>key {e(card.proposed_key)} · {card.shares} sh · stop {e(str(card.stop))}</div></div>"
        )
    elif card.state is CardState.TRIGGERED:
        state_body = (
            f'<div class="state-block triggered-state"><b>TRIGGERED · COBALT</b>'
            f'<div class="strike-numbers"><span>KEY {e(card.proposed_key)}</span>'
            f"<span>SHARES {card.shares}</span><span>STOP {e(str(card.stop))}</span></div></div>"
        )
    else:
        state_body = (
            f'<div class="state-block in-trade-state"><b>IN-TRADE</b> · stop {e(str(card.stop))} · '
            f"next exits {e(str(card.target_1r))} / {e(str(card.target_2r))} · "
            f"attempt {card.attempt}/{card.attempt_max} · trail {trails}</div>"
        )
    return f'''<div class="expanded" data-state="{e(card.display_state)}">
<div class="card-pane">
 <div class="card-title"><span class="rank-chip">#{card.pool_position} · {card.card_score}</span><strong>{e(card.ticker)}</strong>
 <span class="direction {card.direction}">{"↑" if card.direction == "long" else "↓"}</span>
 <span>{e(card.setup)} → {e(card.trade)}</span>{_owner_badge(card.owner)}</div>
 <p class="why-line">{e(card.why)}</p>
 <div class="semaphore">{dots}</div>
 <div class="health-line">{health}<b>{e(health_summary)}</b></div>
 {state_body}
 <button class="judgment-tap" title="S2-P2" disabled>judgment tap · S2-P2</button>
</div>
<aside class="detail-pane">
 <section data-detail="levels"><h4>LEVELS</h4><dl><dt>trigger</dt><dd>{e(str(card.trigger))}</dd><dt>stop</dt><dd>{e(str(card.stop))}</dd><dt>1R</dt><dd>{e(str(card.target_1r))}</dd><dt>2R</dt><dd>{e(str(card.target_2r))}</dd></dl></section>
 <section data-detail="rank"><h4>RANK + WHY</h4><p>score {card.card_score} · conviction {card.conviction:.2f} · proximity {card.proximity:.2f} · pool #{card.pool_position} · {e(card.source)}</p><p>{e(card.why)}</p></section>
 <section data-detail="news"><h4>NEWS</h4><p>{e(card.news or "empty · S2-P2")}</p></section>
 <section data-detail="notes"><h4>NOTES</h4><p>{e(card.notes or "empty · S2-P2")}</p></section>
 <section data-detail="chart"><h4>CHART</h4><p>reserved · empty</p></section>
</aside></div>'''


def render_ladder(view: LadderView) -> str:
    """Pure HTML renderer for the card-ladder shell."""
    e = html.escape
    if view.empty_message:
        active_html = f'<div class="empty-state">{e(view.empty_message)}</div>'
    else:
        rows = []
        for index, card in enumerate(view.active, start=1):
            open_class = " open" if index <= 2 else ""
            promote = (
                '<button class="promote" title="S2-P2" disabled>promote ↑</button>'
                if index >= 3
                else ""
            )
            rows.append(
                f'<article class="ladder-item{open_class}" data-card-id="{card.id}">'
                f'<button class="strip" data-toggle-card="{card.id}"><span>#{index} · {card.card_score}</span>'
                f"<b>{e(card.ticker)}</b><span>{e(card.setup)} → {e(card.trade)}</span>"
                f"<span>{e(card.display_state)} · {e(card.grade)} · {card.shares} sh · stop {e(str(card.stop))}</span></button>"
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
            f"<span>{e(card.direction)} · {e(card.grade)} · {card.shares} sh · stop {e(str(card.stop))}</span>"
            f"<time>{e(_fmt_dt(card.state_at))}</time></div>"
            for card in cards
        )
        terminal_groups.append(f"<h4>{state.value} · {len(cards)}</h4>{group_rows}")
    terminal_rows = "".join(terminal_groups) or '<div class="muted">none</div>'
    return f"""<section id="ladder-layer"><header class="layer-head"><div><span class="eyebrow">CARD LADDER · SHELL</span><h2>TRADE RADAR</h2></div>
<div class="ladder-actions"><button id="collapse-all" type="button">collapse all</button><button id="top-two" type="button">top 2</button></div></header>
<div id="ladder">{active_html}</div>
<details class="terminal"><summary>TERMINAL · {len(view.terminal)}</summary>{terminal_rows}</details></section>"""


PANEL_CSS = r"""
:root{color-scheme:dark;--surface:#0d1117;--card:#11151c;--border:#1f2531;--text:#e6e9ef;--muted:#7d8595;--blue:#4f8dff;--amber:#d9a24a;--green:#35c77a;--red:#ef5b6b}
*{box-sizing:border-box}body{margin:0;background:var(--surface);color:var(--text);font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}.radar-wrap{max-width:1440px;margin:auto;padding:20px}a{color:var(--blue)}h2{margin:3px 0}.eyebrow,.mono,.rank-chip,.ticker,button,th{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;letter-spacing:.08em}.eyebrow,.muted,.pool-meta,.override-line{color:var(--muted);font-size:12px}.layer-head{display:flex;align-items:center;justify-content:space-between;gap:16px;margin:18px 0}.pool-stats{text-align:right}.panel-banner,.refresh-failure{padding:10px 12px;border:1px solid var(--red);background:#351019;color:#ffd0d6;border-radius:7px;margin:7px 0}.retained{border-color:var(--amber);background:#2d2412}.stale-data{outline:2px solid var(--red);outline-offset:5px}.refresh-failed{opacity:.65}table{width:100%;border-collapse:collapse;background:var(--card);border:1px solid var(--border)}th,td{text-align:left;padding:8px;border-bottom:1px solid var(--border);font-size:12px}.ticker{font-weight:800;font-size:15px}.count,.churn-in{color:var(--green)}.churn-out{color:var(--red)}details{margin:12px 0}summary{cursor:pointer;color:#aeb5c2}.ladder-actions button,.strip,.promote,.judgment-tap,.dot{background:var(--card);border:1px solid var(--border);color:var(--text);border-radius:7px}.ladder-actions button{padding:8px;margin-left:7px}.ladder-item{position:relative;margin:8px 0}.strip{width:100%;height:52px;padding:0 18px;display:grid;grid-template-columns:110px 90px 1fr auto;gap:12px;align-items:center;text-align:left}.expanded{display:none;grid-template-columns:minmax(520px,1fr) minmax(360px,1fr);gap:18px;border:1px solid var(--blue);border-top:0;padding:12px;background:#0b0f15}.ladder-item.open .expanded{display:grid}.card-pane,.detail-pane{background:var(--card);border:1px solid var(--border);padding:18px}.card-title{display:flex;gap:10px;align-items:center;flex-wrap:wrap}.card-title strong{font:800 28px ui-monospace,SFMono-Regular,Menlo,monospace}.direction.long{color:var(--green)}.direction.short{color:var(--red)}.rank-chip{border:1px solid var(--border);padding:4px}.owner{font:10px ui-monospace,SFMono-Regular,Menlo,monospace;border:1px solid var(--blue);padding:2px 4px;color:var(--blue)}.owner-n-a-manual{background:var(--red);color:#111;border-color:var(--red)}.owner-you{color:var(--amber);border-color:var(--amber)}.why-line{color:#aeb5c2}.semaphore,.health-line{display:flex;gap:7px;align-items:center;flex-wrap:wrap;padding:12px 0;border-top:1px solid var(--border)}.dot{min-height:34px}.health{padding:4px 7px;border-radius:10px;font-size:11px}.health.ok{color:var(--green);border:1px solid var(--green)}.health.warn{color:var(--amber);border:1px solid var(--amber)}.health.bad{color:var(--red);border:1px solid var(--red)}.state-block{padding:14px 0}.trigger-distance{font:700 24px ui-monospace,SFMono-Regular,Menlo,monospace;padding:12px 0}.triggered-state{border:1px solid var(--green);padding:18px}.strike-numbers{display:flex;gap:24px;font:800 24px ui-monospace,SFMono-Regular,Menlo,monospace;margin-top:12px}.judgment-tap{min-height:44px}.detail-pane h4,.terminal h4{font:11px ui-monospace,SFMono-Regular,Menlo,monospace;color:var(--muted);letter-spacing:.12em}.detail-pane dl{display:grid;grid-template-columns:100px 1fr}.detail-pane dt{color:var(--muted)}.promote{position:absolute;right:-2px;top:55px;min-height:44px}.terminal{margin-top:24px}.terminal-row{height:52px;opacity:.55;border:1px solid var(--border);background:var(--card);display:grid;grid-template-columns:100px 100px 1fr auto;align-items:center;padding:0 18px;margin:6px 0}.empty-state{border:1px dashed var(--border);padding:28px;color:var(--muted)}
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
 document.getElementById('collapse-all').addEventListener('click',collapseAll);
 document.getElementById('top-two').addEventListener('click',topTwo);
 document.getElementById('ladder').addEventListener('click',function(event){
   const strip=event.target.closest('[data-toggle-card]'); if(strip){strip.closest('.ladder-item').classList.toggle('open');}
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
 window.COBALT_RADAR={collapseAll:collapseAll,topTwo:topTwo,refreshPool:refreshPool};
 window.setInterval(refreshPool,interval);
})();
"""


def render_radar_page(view: RadarPanelView, *, phone_frame: bool = False) -> str:
    frame_class = "phone-frame" if phone_frame else ""
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Cobalt · Trade Radar</title><style>{PANEL_CSS}</style></head>
<body class="{frame_class}" data-refresh-seconds="{view.pool.scan_interval}"><main class="radar-wrap"><nav><a href="/">ASET sheet</a></nav>{render_pool(view.pool)}{render_ladder(view.ladder)}</main><script>{PANEL_JS}</script></body></html>'''


def render_failed_page(message: str, *, phone_frame: bool = False) -> str:
    frame_class = "phone-frame" if phone_frame else ""
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Cobalt · Trade Radar · FAILED</title><style>{PANEL_CSS}</style></head><body class="{frame_class}"><main class="radar-wrap"><nav><a href="/">ASET sheet</a></nav><div class="panel-banner degraded"><b>FAILED</b> · {html.escape(message)}</div></main></body></html>'''


def pool_api_payload(view: PoolView) -> dict[str, Any]:
    return {"pool": view.model_dump(mode="json"), "html": render_pool(view)}


__all__ = [
    "PANEL_CSS",
    "PANEL_JS",
    "BannerView",
    "CardView",
    "ChurnDelta",
    "DotView",
    "HealthView",
    "LadderView",
    "MembershipRecord",
    "PoolRow",
    "PoolView",
    "RadarPanelError",
    "RadarPanelView",
    "build_ladder_view",
    "build_pool_view",
    "build_radar_panel",
    "order_cards",
    "parse_since",
    "pool_api_payload",
    "render_failed_page",
    "render_ladder",
    "render_pool",
    "render_radar_page",
]
