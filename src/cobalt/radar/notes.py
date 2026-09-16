"""Single-read parser and user-side mirror for radar source notes."""

from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, ValidationError

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


def load_sources(
    screens_path: Path,
    lists_path: Path,
    *,
    scan_interval: int,
    poll_interval: int,
    finviz_max_rpm: int | None,
    list_chunk_size: int,
    context_tickers: int,
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
    if demand.refusal is not None:
        result.pool_error = (
            f"pool budget exceeded: {demand.refusal}; planned_rpm={demand.steady_rpm:.2f} "
            f"(pool={demand.pool_rpm:.2f}, screens={screen_count}, "
            f"lists_chunks={_total_chunks(list_blocks, list_chunk_size)}, "
            f"context={demand.context_rpm:.2f}, daily_names={demand.daily_names}), "
            f"finviz_max_rpm={finviz_max_rpm}, cap={pool.cap}, "
            f"scan_interval={scan_interval}"
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
    return load_sources(
        vault / cfg.notes.screens,
        vault / cfg.notes.lists,
        scan_interval=int(values["radar.scan_interval"].value),
        poll_interval=int(values["radar.poll_interval"].value),
        finviz_max_rpm=None if rpm is None else int(rpm),
        list_chunk_size=cfg.list_chunk_size,
        context_tickers=len(cfg.context.tickers),
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
    "ParsedBlock", "ParsedNote", "ParsedSources", "RadarNoteError",
    "configured_sources", "load_sources", "mirror_sources", "parse_note", "parse_note_bytes",
    "TransportDemand", "plan_transport_demand", "planned_context_rpm",
    "planned_lists_rpm", "planned_pool_rpm", "planned_screens_rpm", "planned_total_rpm",
]
