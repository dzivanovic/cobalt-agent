"""Single-read parser and user-side mirror for radar source notes."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, model_validator

from cobalt.session import session_clock
from cobalt.session.clock import now_utc
from cobalt.session.models import Session
from cobalt.settings.store import TraderSettingsStore

from .collector import DAILY_RETRIES_PER_REQUEST
from .config import RadarConfig, load_config
from .models import ExcludeBlock, ListBlock, PoolBlock, ScreenBlock

FENCE_RE = re.compile(rb"```yaml[ \t]*\r?\n(.*?)\r?\n```", re.DOTALL)


class RadarNoteError(RuntimeError):
    """A note or one of its fenced units is missing/invalid."""


@dataclass(frozen=True)
class ParsedBlock:
    key: str
    block: ScreenBlock | PoolBlock | ListBlock | ExcludeBlock
    sha256: str


@dataclass
class ParsedNote:
    path: Path
    kind: Literal["screens", "lists"]
    note_sha256: str | None = None
    blocks: list[ParsedBlock] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    missing: bool = False

    @property
    def ok(self) -> bool:
        return not self.missing and not self.errors

    def by_key(self) -> dict[str, ParsedBlock]:
        return {block.key: block for block in self.blocks}


@dataclass
class ParsedSources:
    screens: ParsedNote
    lists: ParsedNote
    pool: PoolBlock | None
    pool_error: str | None = None
    planned_rpm: float | None = None
    demand: TransportDemand | None = None

    @property
    def frozen(self) -> bool:
        return self.pool is None or self.pool_error is not None


def _failure(kind: str, index: int, error: Exception) -> str:
    return f"{kind} block {index}: {error}"


def parse_note(path: Path, kind: Literal["screens", "lists"]) -> ParsedNote:
    """Read bytes exactly once and parse every yaml fence; none are skipped."""
    try:
        payload = path.read_bytes()
    except FileNotFoundError:
        result = ParsedNote(path=path, kind=kind)
        result.missing = True
        result.errors.append(f"{path}: missing")
        return result
    except OSError as e:
        result = ParsedNote(path=path, kind=kind)
        result.errors.append(f"{path}: unreadable: {e}")
        return result
    return parse_note_bytes(path, kind, payload)


def parse_note_bytes(
    path: Path, kind: Literal["screens", "lists"], payload: bytes
) -> ParsedNote:
    """Parse already-read bytes under the same note contract."""
    result = ParsedNote(path=path, kind=kind)
    result.note_sha256 = hashlib.sha256(payload).hexdigest()

    for index, match in enumerate(FENCE_RE.finditer(payload), start=1):
        body = match.group(1)
        digest = hashlib.sha256(body).hexdigest()
        try:
            raw = yaml.safe_load(body)
            if not isinstance(raw, dict):
                raise TypeError("fenced YAML must be a mapping")
            block_kind = raw.get("kind")
            if kind == "screens":
                if block_kind is None:
                    model = ScreenBlock(**raw)
                    key = f"screen.{model.screen}"
                elif block_kind == "pool":
                    model = PoolBlock(**raw)
                    key = "pool"
                else:
                    raise ValueError(f"unknown or wrong-note kind {block_kind!r}")
            else:
                if block_kind is None:
                    model = ListBlock(**raw)
                    key = f"list.{model.list}"
                elif block_kind == "exclude":
                    model = ExcludeBlock(**raw)
                    key = "exclude"
                else:
                    raise ValueError(f"unknown or wrong-note kind {block_kind!r}")
            if key in {item.key for item in result.blocks}:
                raise ValueError(f"duplicate block key {key!r}")
            result.blocks.append(ParsedBlock(key, model, digest))
        except (yaml.YAMLError, ValidationError, TypeError, ValueError) as e:
            result.errors.append(_failure(kind, index, e))

    if kind == "screens":
        pools = [item for item in result.blocks if item.key == "pool"]
        if len(pools) != 1:
            result.errors.append(f"screens note: expected exactly one pool block, found {len(pools)}")
        elif not result.errors:
            screen_keys = {
                item.block.screen for item in result.blocks if isinstance(item.block, ScreenBlock)
            }
            unknown = sorted(set(pools[0].block.overrides) - screen_keys)
            if unknown:
                result.errors.append(f"pool block: overrides name unknown screen key(s) {unknown}")
    else:
        excludes = [item for item in result.blocks if item.key == "exclude"]
        if len(excludes) > 1:
            result.errors.append(f"lists note: expected at most one exclude block, found {len(excludes)}")
        defaults = [
            item for item in result.blocks
            if isinstance(item.block, ListBlock) and item.block.backfill_default
        ]
        if len(defaults) != 1:
            result.errors.append(
                f"lists note: expected exactly one backfill_default list, found {len(defaults)}"
            )
    return result


# ---------------------------------------------------------------------------
# L53: ONE total Finviz demand across every consumer (S2-P4 STEP-6, R1-13/R2-5)
# ---------------------------------------------------------------------------

#: The scheduled one-shot consumers of the shared transport, by registry label.
ARCHIVER_LABEL = "com.cobalt.archiver"
REPLAY_LABEL = "com.cobalt.replay"
BACKUP_LABEL = "com.cobalt.backup"
#: The engine tunable that keeps replay's window clear of the 21:40 backup.
REPLAY_MARGIN_KEY = "replay.backup_margin_s"


class TotalDemandExceeded(RadarNoteError):
    """The total Finviz demand over a consumer's window exceeds the ceiling."""

    def __init__(self, message: str, demand: "TotalDemand | None" = None):
        super().__init__(message)
        self.demand = demand


class DemandWindow(BaseModel):
    """[start, end) in ET minutes after midnight; `end` may run past 24:00."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    start_min: int = Field(ge=0, lt=1440)
    end_min: int = Field(gt=0, le=2880)

    @model_validator(mode="after")
    def _ordered(self) -> "DemandWindow":
        if self.end_min <= self.start_min:
            raise ValueError(f"demand window end {self.end_min} is not after start {self.start_min}")
        return self

    @classmethod
    def between(cls, start: str, end: str) -> "DemandWindow":
        return cls(start_min=_hhmm_minutes(start), end_min=_hhmm_minutes(end))

    @classmethod
    def from_at(cls, at: str, seconds: int) -> "DemandWindow":
        start = _hhmm_minutes(at)
        return cls(start_min=start, end_min=start + -(-seconds // 60))

    def overlaps(self, other: "DemandWindow") -> bool:
        return self.start_min < other.end_min and other.start_min < self.end_min

    def describe(self) -> str:
        return f"{_minutes_hhmm(self.start_min)}-{_minutes_hhmm(self.end_min)} ET"


class DemandConsumer(BaseModel):
    """One consumer of the shared transport and its defined rpm conversion.

    `window=None` means UNBOUNDED: it has not been proved disjoint from
    anything, so it counts against every other consumer.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    name: str = Field(min_length=1)
    rpm: float = Field(ge=0)
    window: DemandWindow | None
    basis: str = Field(min_length=1)


class TotalDemand(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    subject: str
    ceiling: int | None
    peak_rpm: float
    peak_at_min: int | None
    counted: tuple[str, ...]

    def describe(self) -> str:
        at = f" at {_minutes_hhmm(self.peak_at_min)} ET" if self.peak_at_min is not None else ""
        return (
            f"total Finviz demand for {self.subject}: peak {self.peak_rpm:.2f} rpm{at} "
            f"over [{', '.join(self.counted)}], finviz_max_rpm={self.ceiling}"
        )


def _hhmm_minutes(raw: str) -> int:
    hour, _, minute = str(raw).partition(":")
    return int(hour) * 60 + int(minute)


def _minutes_hhmm(minutes: int) -> str:
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def total_demand(consumers, *, subject: str, ceiling: int | None) -> TotalDemand:
    """Peak CONCURRENT demand over `subject`'s window.

    A consumer counts wherever its window overlaps the subject's; one
    proved disjoint contributes zero (and only then). The peak is taken at
    every instant a counted window opens inside the subject's window.
    """
    by_name = {c.name: c for c in consumers}
    if subject not in by_name:
        raise RadarNoteError(f"total demand: subject {subject!r} is not among the consumers {sorted(by_name)}")
    own = by_name[subject].window
    counted = [
        c for c in consumers
        if c.window is None or own is None or c.window.overlaps(own)
    ]
    points = {own.start_min} if own is not None else {0}
    for c in counted:
        if c.window is not None and (own is None or own.start_min <= c.window.start_min < own.end_min):
            points.add(c.window.start_min)

    def active(c: DemandConsumer, at: int) -> bool:
        return c.window is None or c.window.start_min <= at < c.window.end_min

    peak, peak_at = 0.0, None
    for at in sorted(points):
        load = sum(c.rpm for c in counted if active(c, at))
        if load > peak:
            peak, peak_at = load, at
    return TotalDemand(subject=subject, ceiling=ceiling, peak_rpm=peak, peak_at_min=peak_at,
                       counted=tuple(c.name for c in counted))


def check_total_demand(consumers, *, subject: str, ceiling: int | None) -> TotalDemand:
    """THE shared gate (L53). Refuses — before any request — when the
    total over `subject`'s window exceeds the ceiling."""
    if ceiling is None:
        raise TotalDemandExceeded(f"{subject}: radar.finviz_max_rpm is unmeasured — no demand can be proved")
    demand = total_demand(consumers, subject=subject, ceiling=ceiling)
    if demand.peak_rpm > ceiling:
        raise TotalDemandExceeded(f"REFUSED: {demand.describe()} exceeds the ceiling", demand)
    return demand


def _ceiling() -> int | None:
    from cobalt.taxonomy.loader import load_tunables

    raw = load_tunables().by_key["radar.finviz_max_rpm"].value
    return None if raw is None else int(raw)


def radar_window(tunables=None) -> DemandWindow:
    """The resident radar scans premarket through aftermarket."""
    if tunables is None:
        from cobalt.taxonomy.loader import load_tunables

        tunables = load_tunables().by_key
    return DemandWindow.between(tunables["session.premarket_open"].value, tunables["session.aftermarket_close"].value)


def replay_window(registry=None, tunables=None) -> DemandWindow:
    """`com.cobalt.replay`'s window: its schedule to its enforced deadline,
    `replay.backup_margin_s` before the backup (R1-16)."""
    from cobalt.jobs.config import load_job_registry

    registry = registry or load_job_registry()
    if tunables is None:
        from cobalt.taxonomy.loader import load_tunables

        tunables = load_tunables().by_key
    replay, backup = registry.spec(REPLAY_LABEL), registry.spec(BACKUP_LABEL)
    if replay.schedule is None or not replay.schedule.at or backup.schedule is None or not backup.schedule.at:
        raise RadarNoteError(f"{REPLAY_LABEL}/{BACKUP_LABEL}: both need an `at` schedule for the replay deadline")
    row = tunables.get(REPLAY_MARGIN_KEY)
    if row is None or row.value is None:
        raise RadarNoteError(f"tunables.yaml: {REPLAY_MARGIN_KEY} is missing or unmeasured")
    deadline_s = _hhmm_minutes(backup.schedule.at) * 60 - int(row.value)
    try:
        return DemandWindow(start_min=_hhmm_minutes(replay.schedule.at), end_min=deadline_s // 60)
    except ValidationError as e:
        raise RadarNoteError(
            f"{REPLAY_LABEL} at {replay.schedule.at} leaves no window before its deadline "
            f"({BACKUP_LABEL} {backup.schedule.at} - {REPLAY_MARGIN_KEY} {row.value}s)"
        ) from e


def scheduled_consumers(
    *,
    ceiling: int | None,
    radar_rpm: float | None = None,
    replay_top_n: int | None = None,
    registry=None,
    tunables=None,
) -> list[DemandConsumer]:
    """Every consumer of the shared transport, with its defined rpm conversion.

    * radar — its planned total (pool + screens + list chunks) when known,
      else its own TokenBucket bound (the ceiling), 04:00-20:00 ET.
    * archiver — its pacing bound, 60 / GENTLE_SLEEP_SECONDS rpm (every
      request is followed by that sleep), from `at` to `at + timeout_s`:
      the watchdog bound, the only proved end. Never omitted because a job
      precondition serializes it (R2-5).
    * replay — 2 exports + one i1 fetch per top-N mover per side, paced by
      the process bucket: min(2 + 2 x top_n, ceiling); the bucket bound
      when the benchmark is not known. Schedule to deadline.
    """
    from cobalt.archiver.runner import GENTLE_SLEEP_SECONDS
    from cobalt.jobs.config import load_job_registry

    registry = registry or load_job_registry()
    if tunables is None:
        from cobalt.taxonomy.loader import load_tunables

        tunables = load_tunables().by_key
    bound = float(ceiling) if ceiling is not None else 0.0
    consumers = [
        DemandConsumer(
            name="radar", window=radar_window(tunables),
            rpm=float(radar_rpm) if radar_rpm is not None else bound,
            basis="planned total" if radar_rpm is not None else "bucket bound (ceiling)",
        )
    ]
    archiver = registry.by_label.get(ARCHIVER_LABEL)
    if archiver is not None and archiver.schedule is not None and archiver.schedule.at:
        consumers.append(DemandConsumer(
            name="archiver", rpm=60 / GENTLE_SLEEP_SECONDS,
            window=DemandWindow.from_at(archiver.schedule.at, archiver.timeout_s),
            basis=f"pacing bound 60/{GENTLE_SLEEP_SECONDS}s, window to timeout_s",
        ))
    if REPLAY_LABEL in registry.by_label:
        if replay_top_n is not None:
            from cobalt.replay.movers import replay_request_count

            rpm = float(min(replay_request_count(replay_top_n), ceiling if ceiling is not None else 10**9))
            basis = f"min(2 + 2 x top_n={replay_top_n}, ceiling)"
        else:
            rpm, basis = bound, "bucket bound (benchmark not read)"
        consumers.append(DemandConsumer(name="replay", rpm=rpm, window=replay_window(registry, tunables), basis=basis))
    return consumers


def check_scheduled_demand(subject: str, *, radar_rpm: float | None = None,
                           replay_top_n: int | None = None, extra=()) -> TotalDemand:
    """The gate as every pre-request site calls it: the registry's
    consumers, this site's own known numbers, the tunable ceiling.
    `extra` adds an unscheduled consumer (a manual backfill)."""
    ceiling = _ceiling()
    consumers = [*scheduled_consumers(ceiling=ceiling, radar_rpm=radar_rpm, replay_top_n=replay_top_n), *extra]
    return check_total_demand(consumers, subject=subject, ceiling=ceiling)


def load_sources(
    screens_path: Path,
    lists_path: Path,
    *,
    scan_interval: int,
    poll_interval: int,
    finviz_max_rpm: int | None,
    list_chunk_size: int,
    context_tickers: int,
    radar_window: DemandWindow | None = None,
    other_consumers=(),
) -> ParsedSources:
    screens = parse_note(screens_path, "screens")
    lists = parse_note(lists_path, "lists")
    pool_item = next((item for item in screens.blocks if item.key == "pool"), None)
    pool = pool_item.block if pool_item and isinstance(pool_item.block, PoolBlock) else None
    result = ParsedSources(screens=screens, lists=lists, pool=pool)
    if not screens.ok:
        result.pool_error = "; ".join(screens.errors)
        return result
    if pool is None:
        result.pool_error = "pool block missing"
        return result
    if not lists.ok:
        # A list failure degrades that source, but a valid pool still governs.
        return result
    if finviz_max_rpm is None:
        result.pool_error = "radar.finviz_max_rpm is unmeasured"
        return result
    screen_count = sum(1 for item in screens.blocks if isinstance(item.block, ScreenBlock))
    list_blocks = [item.block for item in lists.blocks if isinstance(item.block, ListBlock)]
    demand = plan_transport_demand(
        pool,
        screen_count=screen_count,
        list_blocks=list_blocks,
        list_chunk_size=list_chunk_size,
        scan_interval=scan_interval,
        context_tickers=context_tickers,
        daily_names=pool.cap,
        retries_per_request=DAILY_RETRIES_PER_REQUEST,
        ceiling_rpm=finviz_max_rpm,
    )
    result.planned_rpm = demand.steady_rpm
    result.demand = demand
    # L53: that ONE radar demand — never a second computation — joins every
    # other consumer's over the radar's own window, through the shared gate.
    radar = DemandConsumer(
        name="radar", rpm=demand.steady_rpm, window=radar_window, basis="planned total"
    )
    others = [c for c in other_consumers if c.name != "radar"]
    refused: TotalDemandExceeded | None = None
    try:
        check_total_demand([radar, *others], subject="radar", ceiling=finviz_max_rpm)
    except TotalDemandExceeded as error:
        refused = error
    if demand.refusal is not None or refused is not None:
        reason = demand.refusal or "the total across every consumer exceeds the ceiling"
        result.pool_error = (
            f"pool budget exceeded: {reason}; planned_rpm={demand.steady_rpm:.2f} "
            f"(pool={demand.pool_rpm:.2f}, screens={screen_count}, "
            f"lists_chunks={_total_chunks(list_blocks, list_chunk_size)}, "
            f"context={demand.context_rpm:.2f}, daily_names={demand.daily_names}), "
            f"finviz_max_rpm={finviz_max_rpm}, cap={pool.cap}, "
            f"scan_interval={scan_interval}"
            + (f"; {refused}" if refused is not None else "")
        )
    return result


def planned_pool_rpm(pool: PoolBlock, scan_interval: int) -> float:
    """Pool-only component of the resident scan cadence's request rate."""
    if scan_interval <= 0:
        raise RadarNoteError("radar.scan_interval must be positive")
    return pool.cap * 60 / scan_interval


def _total_chunks(list_blocks: list[ListBlock], list_chunk_size: int) -> int:
    if list_chunk_size <= 0:
        raise RadarNoteError("radar.list_chunk_size must be positive")
    return sum(-(-len(block.tickers) // list_chunk_size) for block in list_blocks)


def planned_screens_rpm(screen_count: int, scan_interval: int) -> float:
    """Screen-scan component: one request per screen per resident cycle."""
    if scan_interval <= 0:
        raise RadarNoteError("radar.scan_interval must be positive")
    return screen_count * 60 / scan_interval


def planned_lists_rpm(list_blocks: list[ListBlock], list_chunk_size: int, scan_interval: int) -> float:
    """List-collection component: one request per ticker chunk per resident cycle."""
    if scan_interval <= 0:
        raise RadarNoteError("radar.scan_interval must be positive")
    return _total_chunks(list_blocks, list_chunk_size) * 60 / scan_interval


def planned_context_rpm(context_tickers: int, scan_interval: int) -> float:
    """Context-ticker polling (S2-P2): one bar request per ticker per cycle."""
    if scan_interval <= 0:
        raise RadarNoteError("radar.scan_interval must be positive")
    if context_tickers < 0:
        raise RadarNoteError("context ticker count cannot be negative")
    return context_tickers * 60 / scan_interval


class LifecycleDemand(BaseModel):
    """S5's departed-member polling on top of the planned steady demand."""

    model_config = ConfigDict(extra="forbid")

    planned_rpm: float | None
    lifecycle_names: int
    lifecycle_rpm: float
    total_rpm: float | None
    ceiling_rpm: int
    refusal: str | None


def lifecycle_poll_demand(
    planned_rpm: float | None, names: int, *, scan_interval: int, ceiling_rpm: int
) -> LifecycleDemand:
    """Can S4 also poll `names` departed-member tickers whose radar cards
    are still open (S2-P2, Astra R1-15)? Counted CONSERVATIVELY on top of
    the whole planned steady demand — which already budgets the full pool
    cap — at the pool's own per-cycle rate, never against the pool alone
    (L53: the total across every consumer of the transport is the rule).
    An unplanned source (a frozen or failed note) has no total and is
    refused, not assumed."""
    lifecycle_rpm = planned_context_rpm(names, scan_interval) * (1 + DAILY_RETRIES_PER_REQUEST)
    if planned_rpm is None:
        return LifecycleDemand(planned_rpm=None, lifecycle_names=names, lifecycle_rpm=lifecycle_rpm,
                               total_rpm=None, ceiling_rpm=ceiling_rpm,
                               refusal="no planned demand to add lifecycle polling to (sources unplanned)")
    total = planned_rpm + lifecycle_rpm
    refusal = (
        f"total demand {total:.2f} rpm (planned {planned_rpm:.2f} + lifecycle {lifecycle_rpm:.2f}) "
        f"exceeds the ceiling {ceiling_rpm}"
        if total > ceiling_rpm + 1e-9 else None
    )
    return LifecycleDemand(planned_rpm=planned_rpm, lifecycle_names=names, lifecycle_rpm=lifecycle_rpm,
                           total_rpm=total, ceiling_rpm=ceiling_rpm, refusal=refusal)


def planned_total_rpm(
    pool: PoolBlock,
    screen_count: int,
    list_blocks: list[ListBlock],
    list_chunk_size: int,
    scan_interval: int,
    *,
    context_tickers: int,
) -> float:
    """Steady Finviz transport demand: pool bar-polling + screens + list
    chunks + context-ticker polling (S2-P2). Daily bars are not steady — a
    once-per-day cold burst — and are planned by `plan_transport_demand`.

    All three consumers share the single resident scan cadence (RadarRunner
    runs _collect and the bar poller in the same cycle); a pool-only budget
    check gives false assurance, the same shape as the pre-fix `radar
    sources` command validating only Lists. Dejan's 2026-09-12 ruling
    (amending the same-day pool-only 90s/33.33rpm ruling after Sol's
    objection): cap 50 unchanged, ceiling 40rpm unchanged, scan interval
    90s -> 100s so the combined total clears the ceiling with headroom.
    """
    return (
        planned_pool_rpm(pool, scan_interval)
        + planned_screens_rpm(screen_count, scan_interval)
        + planned_lists_rpm(list_blocks, list_chunk_size, scan_interval)
        + planned_context_rpm(context_tickers, scan_interval)
    )


class TransportDemand(BaseModel):
    """Every consumer of the shared Finviz transport, planned together (L53).

    THE RULE: a budget that measures one consumer is not a budget. The
    steady consumers (pool bars, screens, list chunks, context tickers)
    run every scan cycle; daily bars are a once-per-ET-day cold burst of
    one request per pool name. Every request may be retried
    `retries_per_request` times, so each consumer's worst case is
    multiplied by (1 + retries).

    ACTUAL PACING, NOT AN IDEALISED REFUSAL (Astra R1-13). At runtime the
    shared `TokenBucket` never refuses — it WAITS, so real traffic never
    exceeds the ceiling; excess demand shows up as slower cycles. This
    plan is where refusal happens, before a scan starts:

    * steady demand above the ceiling → refused (cycles would fall behind
      the ruled cadence forever);
    * any daily names with no headroom left after steady demand → refused
      (the cold burst would never drain);
    * otherwise the plan states how long the cold burst takes to drain
      (`cold_drain_minutes`) and how long the first cold cycle really
      takes when the bucket paces pool + daily requests together
      (`cold_cycle_seconds`, `cold_cycle_overruns_scan_interval`). Those
      are reported, not refused: the ceiling and cadence are Dejan's to
      set, never settled here.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    ceiling_rpm: int
    scan_interval: int
    retries_per_request: int
    pool_rpm: float
    screens_rpm: float
    lists_rpm: float
    context_rpm: float
    daily_names: int
    steady_rpm: float
    headroom_rpm: float
    cycle_requests: int
    cold_drain_minutes: float | None
    cold_cycle_seconds: float
    cold_cycle_overruns_scan_interval: bool
    pacing: Literal["token_bucket_waits"] = "token_bucket_waits"
    refusal: str | None


def plan_transport_demand(
    pool: PoolBlock,
    *,
    screen_count: int,
    list_blocks: list[ListBlock],
    list_chunk_size: int,
    scan_interval: int,
    context_tickers: int,
    daily_names: int,
    retries_per_request: int,
    ceiling_rpm: int,
) -> TransportDemand:
    if ceiling_rpm <= 0:
        raise RadarNoteError("radar.finviz_max_rpm must be positive")
    if retries_per_request < 0 or daily_names < 0:
        raise RadarNoteError("retries and daily names cannot be negative")
    factor = 1 + retries_per_request
    pool_rpm = planned_pool_rpm(pool, scan_interval) * factor
    screens_rpm = planned_screens_rpm(screen_count, scan_interval) * factor
    lists_rpm = planned_lists_rpm(list_blocks, list_chunk_size, scan_interval) * factor
    context_rpm = planned_context_rpm(context_tickers, scan_interval) * factor
    steady = pool_rpm + screens_rpm + lists_rpm + context_rpm
    headroom = ceiling_rpm - steady
    cycle_requests = (
        pool.cap + screen_count + _total_chunks(list_blocks, list_chunk_size) + context_tickers
    )
    cold_requests = daily_names * factor
    cold_cycle_seconds = (cycle_requests * factor + cold_requests) * 60 / ceiling_rpm
    refusal: str | None = None
    drain: float | None = None
    if steady > ceiling_rpm + 1e-9:
        refusal = f"total steady demand {steady:.2f} rpm exceeds the ceiling {ceiling_rpm}"
    elif cold_requests > 0 and headroom <= 1e-9:
        refusal = (
            f"no headroom for {daily_names} daily-bar name(s): steady demand {steady:.2f} rpm "
            f"leaves {headroom:.2f} of {ceiling_rpm}"
        )
    elif cold_requests > 0:
        drain = cold_requests / headroom
    return TransportDemand(
        ceiling_rpm=ceiling_rpm, scan_interval=scan_interval,
        retries_per_request=retries_per_request, pool_rpm=pool_rpm,
        screens_rpm=screens_rpm, lists_rpm=lists_rpm, context_rpm=context_rpm,
        daily_names=daily_names, steady_rpm=steady, headroom_rpm=headroom,
        cycle_requests=cycle_requests, cold_drain_minutes=drain,
        cold_cycle_seconds=cold_cycle_seconds,
        cold_cycle_overruns_scan_interval=cold_cycle_seconds > scan_interval,
        refusal=refusal,
    )


def configured_sources(config: RadarConfig | None = None) -> ParsedSources:
    from cobalt.taxonomy.loader import load_tunables
    from cobalt.vault import resolve_vault_path

    cfg = config or load_config()
    values = load_tunables().by_key
    vault = resolve_vault_path()
    rpm = values["radar.finviz_max_rpm"].value
    ceiling = None if rpm is None else int(rpm)
    return load_sources(
        vault / cfg.notes.screens,
        vault / cfg.notes.lists,
        scan_interval=int(values["radar.scan_interval"].value),
        poll_interval=int(values["radar.poll_interval"].value),
        finviz_max_rpm=ceiling,
        list_chunk_size=cfg.list_chunk_size,
        context_tickers=len(cfg.context.tickers),
        radar_window=radar_window(values),
        other_consumers=scheduled_consumers(ceiling=ceiling, tunables=values),
    )


def _mirror_rows(parsed: ParsedSources, before: dict[str, Any]) -> dict[str, Any]:
    rows: dict[str, Any] = {}
    for note in (parsed.screens, parsed.lists):
        note_key = f"radar.note.{note.kind}"
        note_status = "missing" if note.missing else ("parse_failed" if note.errors else "ok")
        rows[note_key] = {
            "block": None,
            "block_sha256": None,
            "note_sha256": note.note_sha256,
            "status": note_status,
            "error": "; ".join(note.errors) or None,
        }
        for item in note.blocks:
            key = f"radar.{item.key}"
            status = "ok"
            error = None
            if item.key == "pool" and parsed.pool_error:
                status, error = "parse_failed", parsed.pool_error
            rows[key] = {
                "block": item.block.model_dump(mode="json"),
                "block_sha256": item.sha256,
                "note_sha256": note.note_sha256,
                "status": status,
                "error": error,
            }
    current_keys = set(rows)
    for key in before:
        if key.startswith("radar.") and key not in current_keys:
            rows[key] = {
                "block": None,
                "block_sha256": None,
                "note_sha256": None,
                "status": "removed",
                "error": None,
            }
    return rows


def mirror_sources(
    parsed: ParsedSources,
    *,
    store: TraderSettingsStore | None = None,
    before_commit=None,
    now=None,
) -> dict[str, str]:
    instant = now or now_utc()
    if session_clock().session(instant) is Session.MARKET_RESET:
        raise RadarNoteError("radar mirror refused in market_reset before opening a transaction")
    target = store or TraderSettingsStore()
    before = target.values()
    if all(
        isinstance(before.get(f"radar.note.{note.kind}"), dict)
        and before[f"radar.note.{note.kind}"].get("note_sha256") == note.note_sha256
        for note in (parsed.screens, parsed.lists)
    ):
        return {
            f"radar.note.{note.kind}": "unchanged"
            for note in (parsed.screens, parsed.lists)
        }
    rows = _mirror_rows(parsed, before)
    note_hash = parsed.screens.note_sha256 or parsed.lists.note_sha256 or "missing"
    return target.put(
        rows,
        source=f"vault:radar-notes@{note_hash[:12]}",
        before_commit=before_commit,
    )


__all__ = [
    "DemandConsumer", "DemandWindow", "ParsedBlock", "ParsedNote", "ParsedSources",
    "RadarNoteError", "TotalDemand", "TotalDemandExceeded", "TransportDemand",
    "check_scheduled_demand", "check_total_demand", "configured_sources", "load_sources",
    "mirror_sources", "parse_note", "parse_note_bytes", "plan_transport_demand",
    "planned_context_rpm", "planned_lists_rpm", "planned_pool_rpm", "planned_screens_rpm",
    "planned_total_rpm", "radar_window", "replay_window", "scheduled_consumers", "total_demand",
]
