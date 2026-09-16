"""`cobalt radar evaluate` — the dry-run replay and the dev-persistence
harness (S2-P2 STEP-4, R3/R9, Astra R1-11).

    cobalt radar evaluate --replay <YYYY-MM-DD> [--trade-def <slug>]
    cobalt radar evaluate --candidate <YYYY-MM-DD> --settings-file <d2.yaml>
                          --sha256 <hash> [--taps <taps.yaml>] [--trade-def <slug>]

TWO PATHS, KEPT APART ON PURPOSE.

`--replay` WRITES NOTHING. It reads the day's admitted membership episodes
and stored i1 bars (`system.bars`), the loaded trade_defs, and daily bars
from the radar cache only (never a fetch — a fetch writes the cache),
steps a virtual clock through the day at `radar.scan_interval`, evaluates
every admitted member x def through the SAME `evaluate_member` the
resident runs, and prints each formation once (ticker, def, direction,
trigger, stop, formation bar), every path-B-only formation (not evaluable
in S2, R4), and every def's "not evaluable: missing atoms […]" line
(R2). This is the list Dejan reviews before enable.

`--candidate` PERSISTS, AND ONLY TO cobalt_dev. Before D2 the hub freezes
the exact proposed card settings (curves, bands) in a reviewed file,
and this harness runs the real `EvaluateStage` over a captured day with
those settings OVERRIDING the live card keys in memory (trader_settings
is never written), applies simulated taps from a file to every card it
creates, and so produces non-null candidate `card_score`s, every numeric
dot and every N/A path for the L52-d audit (Astra R1-11). It refuses to
run against any database but cobalt_dev, refuses settings that are not
enabled, and refuses a curve set that does not cover every computed factor
of every evaluable def ("full curve coverage").

TAPS FILE:

    taps:
      - {factor: trail_fit, grade: 6}
      - {factor: setup_relation, grade: 8}
"""

from __future__ import annotations

import argparse
import asyncio
from collections.abc import Callable, Iterable, Mapping
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

import yaml
from pydantic import AwareDatetime, BaseModel, ConfigDict, Field

from cobalt import env
from cobalt.session import Session

from .anatomy.daily import DailySeries, parse_daily_csv
from .evaluate import ET
from .anatomy.registry import evaluability
from .evaluate import FACTOR_COMPUTERS, EvaluateStage, LoadedDef, MemberInput, evaluate_member


class CandidateRefused(RuntimeError):
    """The dev-persistence harness refused before writing anything."""


class ReplayFormation(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    seen_at: AwareDatetime
    ticker: str
    slug: str
    direction: str
    trigger: str
    stop: str
    formed_bar_ts: AwareDatetime


class ReplayReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    day: date
    scans: int = 0
    formations: list[ReplayFormation] = Field(default_factory=list)
    path_b_only: list[str] = Field(default_factory=list)
    not_evaluable: dict[str, list[str]] = Field(default_factory=dict)
    counts: dict[str, int] = Field(default_factory=dict)


def _aware(value) -> datetime | None:
    if value is None:
        return None
    return value if value.tzinfo else value.replace(tzinfo=timezone.utc)


def admitted_at(rows: Iterable[Mapping[str, Any]], instant: datetime) -> list[dict]:
    out = []
    for row in rows:
        entered, left = _aware(row.get("entered_at")), _aware(row.get("left_at"))
        if entered is not None and entered <= instant and (left is None or instant < left):
            out.append(dict(row))
    return sorted(out, key=lambda r: r["id"])


def scan_instants(day: date, clock, scan_interval: int, first: datetime | None = None) -> list[datetime]:
    windows = {w.session: w for w in clock.windows_for(day)}
    for needed in (Session.RTH,):
        if needed not in windows:
            raise SystemExit(f"{day} has no RTH session to replay ({clock.calendar.describe(day)})")
    start = datetime.combine(day, windows[Session.RTH].start, ET)
    stop = datetime.combine(day, windows[Session.RTH].end, ET)
    t = max(start, first) if first else start
    out = []
    while t <= stop:
        out.append(t.astimezone(timezone.utc))
        t += timedelta(seconds=scan_interval)
    return out


def _select(defs: list[LoadedDef], slug_filter: str | None) -> list[LoadedDef]:
    if slug_filter is None:
        return defs
    chosen = [d for d in defs if d.slug == slug_filter]
    if not chosen:
        raise SystemExit(f"no loaded trade_def {slug_filter!r}; loaded: {[d.slug for d in defs]}")
    return chosen


def replay_formations(
    day: date,
    *,
    pool_key: str,
    slug_filter: str | None,
    radar_store,
    defs_source: Callable[[], tuple[list[LoadedDef], dict]],
    daily_source: Callable[[str, date], DailySeries],
    tunables: Mapping[str, Any],
    defaults,
    clock,
    out: Callable[[str], None] = print,
) -> ReplayReport:
    """Read-only. See the module docstring."""
    from cobalt.taxonomy.loader import merge_tunables

    defs, user_rows = defs_source()
    defs = _select(defs, slug_filter)
    rows = merge_tunables(dict(tunables), user_rows)
    scan_interval = int(rows["radar.scan_interval"].value)
    report = ReplayReport(day=day)
    for ld in defs:
        ev = evaluability(ld.definition)
        if not ev.evaluable:
            report.not_evaluable[ld.slug] = list(ev.missing_atoms)
            out(f"{ld.slug}: not evaluable: missing atoms {list(ev.missing_atoms)}")
    members = radar_store.members_for_day(pool_key, day)
    if not members:
        out(f"replay {day}: no membership episodes for pool {pool_key!r}")
    admitted_ever = [m for m in members if m.get("entered_at") is not None]
    first = min((_aware(m["entered_at"]) for m in admitted_ever), default=None)
    bars_cache: dict[str, list] = {}
    daily_cache: dict[str, tuple[DailySeries | None, str]] = {}
    seen: set[tuple[str, str, str]] = set()
    b_seen: set[tuple[str, str]] = set()
    evaluable = [ld for ld in defs if ld.slug not in report.not_evaluable]
    day_start = datetime.combine(day, datetime.min.time(), ET)
    for instant in scan_instants(day, clock, scan_interval, first) if admitted_ever else []:
        report.scans += 1
        for member in admitted_at(members, instant):
            ticker = member["ticker"]
            if ticker not in bars_cache:
                bars_cache[ticker] = radar_store.i1_bars(ticker, day_start.astimezone(timezone.utc),
                                                         day_start.astimezone(timezone.utc) + timedelta(days=1))
            if ticker not in daily_cache:
                try:
                    daily_cache[ticker] = (daily_source(ticker, day), "cache-hit")
                except Exception as e:
                    daily_cache[ticker] = (None, f"absent: {e}")
            daily, status = daily_cache[ticker]
            inp = MemberInput(
                membership_id=member["id"], ticker=ticker, trade_date=day, as_of=instant,
                bars=tuple(b for b in bars_cache[ticker] if b.ts < instant), daily=daily, daily_status=status,
                rvol=None, pool_position=member.get("last_rank"),
            )
            for ld in evaluable:
                ev = evaluate_member(ld, inp, tunables=rows, defaults=defaults, scan_interval=scan_interval, clock=clock)
                report.counts[ev.evaluation] = report.counts.get(ev.evaluation, 0) + 1
                if ev.evaluation == "formed" and ev.formation is not None:
                    key = (ticker, ld.slug, ev.formation.formed_bar_ts.isoformat())
                    if key not in seen:
                        seen.add(key)
                        f = ev.formation
                        report.formations.append(ReplayFormation(
                            seen_at=instant, ticker=ticker, slug=ld.slug, direction=f.trade_direction,
                            trigger=str(f.trigger.price), stop=str(f.stop.price), formed_bar_ts=f.formed_bar_ts,
                        ))
                        out(
                            f"{clock.to_et(instant):%H:%M:%S} ET {ticker} {ld.slug} FORMED {f.trade_direction} "
                            f"trigger {f.trigger.price} stop {f.stop.price} "
                            f"(formation bar {clock.to_et(f.formed_bar_ts):%H:%M} ET)"
                        )
                elif ev.evaluation == "not_evaluable" and ev.detail.extension_path == "B_only":
                    if (ticker, ld.slug) not in b_seen:
                        b_seen.add((ticker, ld.slug))
                        line = (f"{clock.to_et(instant):%H:%M:%S} ET {ticker} {ld.slug} path B only "
                                "— not evaluable in S2 (catalyst unknown, R4)")
                        report.path_b_only.append(line)
                        out(line)
    out(
        f"replay {day}: scans={report.scans} formations={len(report.formations)} "
        f"path_b_only={len(report.path_b_only)} counts={dict(sorted(report.counts.items()))} writes: none"
    )
    return report


class CachedDailyBars:
    """Daily bars from the radar cache ONLY — the read-only half of
    `FinvizDailyBarsCollector` (same `<root>/<ET date>/daily/<T>.csv`
    path). A missing file is an error, never a fetch."""

    def __init__(self, cache_root: Path):
        self.cache_root = Path(cache_root)

    def load(self, ticker: str, day: date) -> DailySeries:
        path = self.cache_root / day.isoformat() / "daily" / f"{ticker}.csv"
        if not path.exists():
            raise FileNotFoundError(f"no cached daily bars at {path}")
        return DailySeries(ticker=ticker, bars=parse_daily_csv(path.read_text(encoding="utf-8-sig"), ticker),
                           source="cache-hit")

    async def daily(self, ticker: str, now: datetime) -> DailySeries:
        from zoneinfo import ZoneInfo

        return self.load(ticker, now.astimezone(ZoneInfo("America/New_York")).date())


# ---------------------------------------------------------------------
# Dev-persistence harness (Astra R1-11)
# ---------------------------------------------------------------------


def assert_dev_database() -> str:
    name = env.resolve_db_name()
    if name != env.DEV_DB_NAME:
        raise CandidateRefused(
            f"the candidate harness writes cobalt_dev only; COBALT_ENV resolves {name!r}. "
            "Production never receives candidate rows."
        )
    return name


def curve_coverage_gaps(defs: Iterable[LoadedDef], frozen) -> dict[str, list[str]]:
    curves = frozen.curves or {}
    gaps: dict[str, list[str]] = {}
    for ld in defs:
        if not evaluability(ld.definition).evaluable:
            continue
        missing = [
            q.name for q in ld.definition.quality_factors
            if q.source in {"cobalt", "cobalt-degraded"} and q.tier == "deterministic"
            and q.name in FACTOR_COMPUTERS and q.name not in curves
        ]
        if missing:
            gaps[ld.slug] = missing
    return gaps


def receipt_rvol(receipts: Iterable[Mapping[str, Any]]) -> list:
    """Every RVOL observation the day's receipts retained (R1-12 persists
    the screener RVOL there precisely so a bars-only replay can use it)."""
    from .anatomy.freshness import RvolObservation

    out = []
    for receipt in receipts:
        for member in receipt["observations"]["members"]:
            if member.get("rvol"):
                payload = {k: v for k, v in member["rvol"].items() if k != "sha256"}
                out.append(RvolObservation.model_validate(payload))
    return out


def rvol_as_of(observations: list, at: datetime) -> dict:
    """The latest captured observation per ticker at or before `at`."""
    latest: dict = {}
    for obs in sorted(observations, key=lambda o: o.observed_at):
        if obs.observed_at <= at:
            latest[obs.ticker] = obs
    return latest


class CandidateReport(BaseModel):
    model_config = ConfigDict(extra="forbid")

    run_ids: list[int] = Field(default_factory=list)
    receipt_ids: list[int] = Field(default_factory=list)
    cards_created: list[int] = Field(default_factory=list)
    taps_applied: int = 0
    frozen_settings_sha256: str


async def candidate_run(
    day: date,
    *,
    frozen,
    taps: list[dict],
    pool_key: str,
    radar_store,
    card_store,
    defs_source,
    settings_values: Callable[[], dict],
    daily_source,
    tunables_loader,
    defaults_loader,
    clock,
    start: datetime | None = None,
    stop: datetime | None = None,
    rvol_at: Callable[[datetime], dict] | None = None,
) -> CandidateReport:
    from cobalt.aset.models import Grade
    from cobalt.settings.models import TraderSettings

    if not frozen.cards_enabled:
        raise CandidateRefused("the frozen D2 settings must set radar.cards_enabled: true (a dark bundle has no scores)")
    defs, _user = defs_source()
    gaps = curve_coverage_gaps(defs, frozen)
    if gaps:
        raise CandidateRefused(f"card.curves does not cover every computed factor: {gaps}")
    for tap in taps:
        if not isinstance(tap, dict) or set(tap) != {"factor", "grade"} or not 1 <= int(tap["grade"]) <= 10:
            raise CandidateRefused(f"a simulated tap is {{factor, grade 1-10}}, got {tap!r}")

    instant = [start or datetime.now(timezone.utc)]
    members = radar_store.members_for_day(pool_key, day)

    def frozen_settings() -> dict:
        return {**settings_values(), **frozen.rows()}

    stage = EvaluateStage(
        radar_store=radar_store, card_store=card_store, defs_source=defs_source,
        settings_values=frozen_settings, daily_source=daily_source, tunables_loader=tunables_loader,
        defaults_loader=defaults_loader, clock=clock, now=lambda: instant[0],
        members_at=lambda _key, at: admitted_at(members, at),
    )
    trader = TraderSettings._build(frozen_settings(), where="candidate settings")
    enabled = [Grade(g) for g in trader.daymode.enabled_grades_for(trader.daymode.lowest_enabled)]
    scan_interval = int(tunables_loader()["radar.scan_interval"].value)
    report = CandidateReport(frozen_settings_sha256=frozen.sha256())
    instants = scan_instants(day, clock, scan_interval)
    instants = [t for t in instants if (start is None or t >= start) and (stop is None or t <= stop)]
    for at in instants:
        instant[0] = at
        outcome = await stage.run(
            pool_key=pool_key, scan_id=int(at.timestamp() * 1000), session=clock.session(at).value,
            instant=at, rvol=rvol_at(at) if rvol_at else {},
            pool_unit={"candidate_day": day.isoformat(), "frozen_settings_sha256": frozen.sha256()},
            gate=lambda _label: (lambda: None),
        )
        report.run_ids.append(outcome.run_id)
        report.receipt_ids.append(outcome.receipt_id)
        for card_id in outcome.created:
            report.cards_created.append(card_id)
            for tap in taps:
                card_store.tap_dot(card_id, tap["factor"], int(tap["grade"]), bands=frozen.proposed_key,
                                   enabled=enabled, now=at)
                report.taps_applied += 1
    return report


def evaluate_command(args: argparse.Namespace) -> None:
    from cobalt.cards.store import CardStore
    from cobalt.session import session_clock
    from cobalt.settings.card import load_card_file
    from cobalt.settings.store import TraderSettingsStore
    from cobalt.taxonomy.loader import load_defaults, load_tunables
    from cobalt.taxonomy.store import TradeDefStore

    from .config import load_config
    from .store import RadarStore

    if bool(args.replay) == bool(args.candidate):
        raise SystemExit("cobalt radar evaluate: pass exactly one of --replay <date> or --candidate <date>")
    config = load_config()
    clock = session_clock()
    cache = CachedDailyBars(Path(config.cache.dir))
    if args.replay:
        replay_formations(
            date.fromisoformat(args.replay), pool_key=config.pool_key, slug_filter=args.trade_def,
            radar_store=RadarStore(), defs_source=TradeDefStore().loaded_for_evaluation,
            daily_source=cache.load, tunables=load_tunables().by_key, defaults=load_defaults(), clock=clock,
        )
        return

    assert_dev_database()
    if not args.settings_file or not args.sha256:
        raise SystemExit("--candidate requires --settings-file <reviewed D2 file> and --sha256 <hash>")
    frozen, digest = load_card_file(Path(args.settings_file), expected_sha256=args.sha256)
    taps: list[dict] = []
    if args.taps:
        doc = yaml.safe_load(Path(args.taps).read_text(encoding="utf-8"))
        if not isinstance(doc, dict) or not isinstance(doc.get("taps"), list):
            raise SystemExit(f"{args.taps}: expected a top-level 'taps' list")
        taps = doc["taps"]
    defs_store = TradeDefStore()

    def defs_source():
        defs, user_rows = defs_store.loaded_for_evaluation()
        return _select(defs, args.trade_def), user_rows

    day = date.fromisoformat(args.candidate)
    card_store = CardStore()
    captured = receipt_rvol(card_store.receipts_for_day(config.pool_key, day))
    report = asyncio.run(candidate_run(
        day, frozen=frozen, taps=taps, pool_key=config.pool_key,
        radar_store=RadarStore(), card_store=card_store, defs_source=defs_source,
        settings_values=TraderSettingsStore().values, daily_source=cache.daily,
        tunables_loader=lambda: load_tunables().by_key, defaults_loader=load_defaults, clock=clock,
        rvol_at=lambda at: rvol_as_of(captured, at),
    ))
    print(f"candidate {args.candidate} on {env.DEV_DB_NAME}: settings sha256 {digest}")
    print(f"  runs {report.run_ids[:1]}..{report.run_ids[-1:]} ({len(report.run_ids)}), "
          f"receipts {len(report.receipt_ids)}, cards {report.cards_created}, taps {report.taps_applied}")


__all__ = [
    "CachedDailyBars", "CandidateRefused", "CandidateReport", "ReplayFormation", "ReplayReport",
    "admitted_at", "assert_dev_database", "candidate_run", "curve_coverage_gaps", "evaluate_command",
    "replay_formations", "scan_instants",
]
