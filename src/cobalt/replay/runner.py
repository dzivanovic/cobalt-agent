"""The nightly replay run, in its ruled order (S2-P4 STEP-4, R3 as amended).

    (0) precondition  tonight's 20:30 `com.cobalt.archiver` occurrence is
                      `done`, exit 0, with coherent times — never a prior
                      day's run or an earlier manual one (R1-15)
    (1) movers        F13: exports -> SYSTEM commit (movers_daily) -> i1
                      archive -> benchmark -> USER commit (missed, mover)
    (2) cards         F12: USER reads + SYSTEM bar reads -> USER commit
                      (missed, card)
    (3) formations    S2-P2's own read-only replay when present and
                      compatible -> USER commit (missed, formation);
                      absent -> one exact unavailable line, no rows;
                      incompatible -> loud (R4, R1-21)
    (4) line          the DRC miss line from the reconciled current set

PER-SIDE COMMITS (R2-3). No connection or role spans the two schemas in
one transaction: every SYSTEM write commits in a SYSTEM store, every USER
write in a USER store, each step owning its own boundaries. Recovery is by
rerun: reconciliation is keyed to the receipt-owned `replay_run_id` and is
idempotent, so a retry after any commit boundary resumes cleanly.

A FAILED STEP names itself (`StepFailed.step`) and stops the run; what the
earlier steps committed stands. Per-ticker archive failures are counted and
fail the job at the END, after the line (archiver semantics).

THE DEADLINE (R1-16). `timeout_s` bounds a stall, not a healthy long run.
The run's own deadline is `replay.backup_margin_s` before the backup's
schedule: a run starting inside that margin refuses; a running step is cut
at the deadline (async work under `wait_for`); the vault write is re-checked
immediately before it lands, so no write is ever late. A run started after
the backup time has no deadline to race.

DRY RUN (R1-17) writes nothing — no DDL, no DML, no job stamp (the CLI
uses `as_job(skip=True)`), no radar-cache file, no vault byte — and prints
every row and the line's unified diff.
"""

from __future__ import annotations

import asyncio
import uuid
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from typing import Any, Callable, Optional

from loguru import logger

from cobalt.archiver.models import Interval
from cobalt.radar.notes import ARCHIVER_LABEL, BACKUP_LABEL, REPLAY_LABEL, REPLAY_MARGIN_KEY
from cobalt.session.clock import ET
from cobalt.settings.models import BenchmarkSettings

from .cards import replay_card, resolve_window
from .formations import (
    FORMATION_REQUIRED_FIELDS,
    SUPPORTED_EVALUATORS,
    FormationContext,
    FormationSources,
    formation_misses,
)
from .line import render_line, write_miss_line
from .models import (
    FORMATION_UNAVAILABLE,
    FORMATION_UNAVAILABLE_LINE,
    ArchivePartial,
    Episode,
    FormationOutcome,
    MissRow,
    ReplayError,
    ReplayResult,
    StepFailed,
    StoredMover,
)
from .movers import (
    archive_movers,
    benchmark_misses,
    export_counts,
    not_equity_verdicts,
    retained_exports,
)

STEPS = ("movers", "cards", "formations", "line")


class DeadlineExceeded(ReplayError):
    """The replay's enforced deadline passed (or the run began inside its margin)."""


def _et(instant: datetime) -> datetime:
    if instant.tzinfo is None:
        raise ReplayError(f"naive datetime {instant.isoformat()} — the replay reasons in instants")
    return instant.astimezone(ET)


def _hhmm(raw: str) -> time:
    hour, _, minute = raw.partition(":")
    return time(int(hour), int(minute))


# ---------------------------------------------------------------------------
# (0) precondition and the deadline
# ---------------------------------------------------------------------------


def archiver_precondition(row: Optional[dict[str, Any]], *, trade_date: date, now: datetime, registry) -> str:
    """Refuse unless the archiver's occurrence for `trade_date` finished clean.

    For tonight: the row's run started at or after tonight's scheduled
    instant on tonight's ET date. For a past date (the hub's historical
    run): a clean run that started at or after THAT night's scheduled
    instant — `cobalt_jobs` keeps one row per label, so a later clean run
    is the only evidence left; bar coverage is still checked per ticker.
    """
    spec = registry.spec(ARCHIVER_LABEL)
    if spec.schedule is None or not spec.schedule.at:
        raise ReplayError(f"archiver not done: {ARCHIVER_LABEL} has no `at` schedule to anchor tonight's run")
    scheduled = datetime.combine(trade_date, _hhmm(spec.schedule.at), tzinfo=ET)
    now_et = _et(now)

    def refuse(why: str) -> ReplayError:
        return ReplayError(f"archiver not done: {why}")

    if trade_date > now_et.date():
        raise refuse(f"{trade_date} is in the future")
    if row is None:
        raise refuse(f"no cobalt_jobs row for {ARCHIVER_LABEL}")
    if row.get("state") != "done":
        raise refuse(f"state {row.get('state')!r}")
    if row.get("exit_code") != 0:
        raise refuse(f"exit code {row.get('exit_code')!r}")
    started, finished = row.get("started_at"), row.get("finished_at")
    if started is None or finished is None or finished < started or finished > now:
        raise refuse(f"incoherent run times started={started} finished={finished}")
    started_et = _et(started)
    if started_et < scheduled:
        raise refuse(
            f"its last run started {started_et:%Y-%m-%d %H:%M:%S} ET, before the {trade_date} "
            f"{spec.schedule.at} ET occurrence — not that night's run"
        )
    if trade_date == now_et.date():
        if started_et.date() != trade_date:
            raise refuse(f"its last run started on {started_et.date()}, not tonight ({trade_date})")
        return f"tonight's {spec.schedule.at} ET run: done, exit 0, finished {_et(finished):%H:%M:%S} ET"
    return (
        f"historical {trade_date}: a clean run started {started_et:%Y-%m-%d %H:%M:%S} ET, at or after "
        f"that night's {spec.schedule.at} ET occurrence"
    )


def replay_deadline(now: datetime, *, registry, tunables) -> Optional[datetime]:
    """Today's enforced deadline, or None when the run starts after the backup."""
    backup = registry.spec(BACKUP_LABEL)
    if backup.schedule is None or not backup.schedule.at:
        raise ReplayError(f"{BACKUP_LABEL} has no `at` schedule; the replay deadline cannot be derived")
    row = tunables.get(REPLAY_MARGIN_KEY)
    if row is None or row.value is None:
        raise ReplayError(f"tunables.yaml: {REPLAY_MARGIN_KEY} is missing or unmeasured")
    now_et = _et(now)
    backup_at = datetime.combine(now_et.date(), _hhmm(backup.schedule.at), tzinfo=ET)
    deadline = backup_at - timedelta(seconds=int(row.value))
    if now_et >= backup_at:
        return None
    if now_et >= deadline:
        raise DeadlineExceeded(
            f"started {now_et:%H:%M:%S} ET, inside the {row.value}s margin before the "
            f"{backup.schedule.at} ET backup (deadline {deadline:%H:%M:%S} ET)"
        )
    return deadline


# ---------------------------------------------------------------------------
# (3) formations — the S2-P2 adapter
# ---------------------------------------------------------------------------


def formation_replay(
    trade_date: date,
    *,
    out: Callable[[str], None],
    sources: Optional[FormationSources] = None,
    context: Optional[FormationContext] = None,
) -> FormationOutcome:
    """Bind to S2-P2's replay, or say exactly that it is not there.

    Absent -> the exact line, `unavailable`, no rows. Present but not
    carrying the fields a miss row needs, or carrying a capability marker
    this binding was not written against -> loud refusal, never a silent
    degrade (R1-21). Present, compatible and wired -> P2's OWN read-only
    replay runs for the day and every formation it returns goes through
    `replay/formations.py`; replay never re-derives a formation itself.

    Two S2-P2 modules, two distinct roles, both imported statically: the
    entrypoint and its model ship in `cobalt.radar.evaluate_cli`, the
    capability marker in `cobalt.radar.evaluate`. The plan named the
    single module `cobalt.radar.evaluate`; the shipped layout is what the
    code follows, and no name is ever accepted in two spellings (L3).
    """
    try:
        # STATIC imports, on purpose: the restart classifier (L42) walks
        # imports by AST and treats a string-named dynamic import as
        # unresolvable, which would restart every resident.
        import cobalt.radar.evaluate as evaluator
        import cobalt.radar.evaluate_cli as module
    except ModuleNotFoundError as e:
        if e.name not in {"cobalt.radar.evaluate_cli", "cobalt.radar.evaluate"}:
            raise
        logger.warning(FORMATION_UNAVAILABLE_LINE)
        out(FORMATION_UNAVAILABLE_LINE)
        return FormationOutcome(status=FORMATION_UNAVAILABLE)
    model = getattr(module, "ReplayFormation", None)
    call = getattr(module, "replay_formations", None)
    fields = set(getattr(model, "model_fields", {}) or {})
    missing = sorted(FORMATION_REQUIRED_FIELDS - fields)
    if call is None or model is None or missing:
        raise ReplayError(
            "S2-P2 formation replay is present but incompatible: "
            + ("no replay_formations/ReplayFormation" if call is None or model is None else f"missing {missing}")
            + f" (replay needs {sorted(FORMATION_REQUIRED_FIELDS)})"
        )
    version = getattr(evaluator, "EVALUATOR_VERSION", None)
    if version not in SUPPORTED_EVALUATORS:
        raise ReplayError(
            f"S2-P2 formation replay is present but incompatible: evaluator version {version!r} is not one "
            f"this binding was written against ({sorted(SUPPORTED_EVALUATORS)})"
        )
    if sources is None or context is None:
        raise ReplayError(
            "S2-P2 formation replay is present and compatible, but replay was given no formation "
            "sources — refusing rather than running a half-wired binding (R1-21)"
        )
    report = call(
        trade_date, pool_key=sources.pool_key, slug_filter=None, radar_store=sources.radar_store,
        defs_source=sources.defs_source, daily_source=sources.daily_source, tunables=sources.tunables,
        defaults=sources.defaults, clock=sources.clock, out=out,
    )
    return formation_misses(report, context=context, evaluator_version=version)


# ---------------------------------------------------------------------------
# The run
# ---------------------------------------------------------------------------


@dataclass
class ReplayDeps:
    """Everything the run touches, so a test can record every call."""

    job_store: Any
    registry: Any
    tunables: Any
    now: Callable[[], datetime]
    session_bounds: Callable[[date], tuple[datetime, datetime]]
    settings_values: Callable[[], dict]
    missed: Any
    movers_store: Any
    bar_store: Any
    radar_store: Any
    radar_config: Any
    collector_factory: Callable[[], Any]
    cache_root: Any
    writer_factory: Callable[[bool], Any]
    drc_path: Callable[[date], Any]
    out: Callable[[str], None]
    ceiling: Optional[int]
    formation_source: Callable[..., FormationOutcome] = formation_replay
    #: S2-P2's own replay arguments, built only when the step runs.
    formation_sources: Optional[Callable[[], FormationSources]] = None


def _new_run_id(trade_date: date, now: datetime) -> str:
    return f"replay-{trade_date.isoformat()}-{_et(now):%Y%m%dT%H%M%S}-{uuid.uuid4().hex[:6]}"


def run_nightly(trade_date: date, *, dry_run: bool, deps: ReplayDeps, live: Optional[bool] = None) -> ReplayResult:
    """One replay of `trade_date`. See the module docstring."""
    started = deps.now()
    result = ReplayResult(trade_date=trade_date, replay_run_id=_new_run_id(trade_date, started), dry_run=dry_run)
    live = (trade_date == _et(started).date()) if live is None else live

    def attach(error: ReplayError) -> ReplayError:
        error.result = result
        return error

    try:
        result.precondition = archiver_precondition(
            deps.job_store.get(ARCHIVER_LABEL), trade_date=trade_date, now=started, registry=deps.registry
        )
        deadline = None if dry_run else replay_deadline(started, registry=deps.registry, tunables=deps.tunables)
    except ReplayError as e:
        raise attach(e)
    deps.out(f"replay {trade_date} run {result.replay_run_id}{' DRY RUN' if dry_run else ''}: {result.precondition}")

    def check_deadline(what: str) -> None:
        if deadline is not None and deps.now() >= deadline:
            raise DeadlineExceeded(f"{what}: past the deadline {deadline:%H:%M:%S} ET")

    def run_async(coro):
        if deadline is None:
            return asyncio.run(coro)
        remaining = (deadline - deps.now()).total_seconds()
        if remaining <= 0:
            coro.close()
            raise DeadlineExceeded(f"past the deadline {deadline:%H:%M:%S} ET")

        async def bounded():
            return await asyncio.wait_for(coro, timeout=remaining)

        try:
            return asyncio.run(bounded())
        except (asyncio.TimeoutError, TimeoutError) as e:
            raise DeadlineExceeded(f"cut at the deadline {deadline:%H:%M:%S} ET") from e

    state: dict[str, Any] = {"archive_failures": {}}
    rth_open, close = deps.session_bounds(trade_date)
    day_start = datetime.combine(trade_date, time(0), tzinfo=ET)
    day_end = day_start + timedelta(days=1)

    def movers_step() -> None:
        settings = BenchmarkSettings.from_rows(deps.settings_values())
        state["settings"] = settings
        collector = None
        if live:
            collector = run_async(deps.collector_factory())
            exports = run_async(collector.exports(top_n=settings.top_n, now=deps.now(), cache=not dry_run,
                                                  trade_date=trade_date))
        else:
            exports = retained_exports(deps.cache_root, trade_date, top_n=settings.top_n, config=deps.radar_config)
        # The not-equity verdicts, decided AT INGEST off the parsed
        # export rows and handed to the benchmark unchanged on BOTH
        # paths (L3). It cannot be rebuilt later: `movers_daily` stores
        # no `industry` column, so the live path's `StoredMover`s come
        # back without the second half of the R16 rule.
        verdicts = not_equity_verdicts(exports)
        # Bookkeeping, before anything is stored: what each side's export
        # really had, and how many rows that allows (`min(top_n,
        # exported)`). Selects nothing — the rows below are the same ones.
        result.movers_by_side = export_counts(exports, top_n=settings.top_n)
        if dry_run:
            stored = [
                StoredMover(trade_date=trade_date, side=e.side, rank=r.rank, ticker=r.ticker, change_pct=r.change_pct,
                            asset_type=r.asset_type, volume=r.volume, rvol=r.rvol, export_sha256=e.export_sha256,
                            fetched_at=e.fetched_at)
                for e in exports for r in e.rows
            ]
        else:
            stored = deps.movers_store.reconcile(run_id=result.replay_run_id, trade_date=trade_date, exports=exports)
        result.movers = len(stored)
        outcome = run_async(archive_movers(
            stored, collector=collector, bar_store=deps.bar_store, trade_date=trade_date, rth_open=rth_open,
            close=close, top_n=settings.top_n, dry_run=dry_run or not live, now=deps.now(), deadline=deadline,
            rpm=deps.ceiling,
        ))
        if not dry_run:
            deps.movers_store.mark_bars_archived(outcome.archived_ids)
        result.archived = len(outcome.archived_ids)
        result.archive_failures = len(outcome.failures)
        result.archive_incomplete = len(outcome.incomplete) + (0 if (live or dry_run) else len(outcome.would_fetch))
        # R113: a clean fetch short of the session is PARTIAL, named with
        # its coverage detail and counted per side for the smoke's K9.
        result.archive_partial = [
            ArchivePartial(
                ticker=ticker, sides=sorted({m.side for m in stored if m.ticker == ticker}),
                code=detail["code"], count=detail["count"], first=detail["first"], last=detail["last"],
                start=detail["start"], end=detail["end"], max_gap_min=detail["max_gap_min"],
                reason=detail["reason"],
            )
            for ticker, detail in sorted(outcome.partial.items())
        ]
        result.archive_partial_by_side = {
            side: sum(1 for p in result.archive_partial if side in p.sides) for side in ("gainers", "losers")
        }
        state["archive_failures"] = outcome.failures
        for ticker, error in sorted(outcome.failures.items()):
            logger.error("replay movers archive: {} FAILED — {}", ticker, error)
        for p in result.archive_partial:
            logger.warning("replay movers archive: {} PARTIAL — {} ({} i1 bars, {} → {})",
                           p.ticker, p.reason, p.count, p.first, p.last)
        for ticker in outcome.incomplete:
            logger.error("replay movers archive: {} INCOMPLETE — a clean fetch returned no i1 bars for {}",
                         ticker, trade_date)
        if dry_run and live and outcome.would_fetch:
            deps.out(f"DRY RUN would archive i1 bars for: {', '.join(outcome.would_fetch)}")

        episodes = [Episode(**row) for row in deps.radar_store.members_for_day(deps.radar_config.pool_key, trade_date)]
        rows = benchmark_misses(stored, episodes, settings=settings, trade_date=trade_date,
                                not_equity=deps.radar_config.not_equity, verdicts=verdicts)
        for row in rows:
            deps.out(f"MISS mover {row.ticker} excluded_by={row.excluded_by} change={row.gate_detail['change_pct']}%")
        state["mover_rows"] = [r.model_dump() for r in rows]
        if not dry_run:
            result.reconcile["mover"] = deps.missed.reconcile(
                run_id=result.replay_run_id, trade_date=trade_date, kind="mover", rows=rows)
            state["mover_rows"] = deps.missed.current(trade_date, "mover")
        result.mover_misses = len(state["mover_rows"])

    def cards_step() -> None:
        candidates = deps.missed.candidates(trade_date)
        positions = deps.missed.positions(trade_date)
        result.card_candidates = len(candidates)
        rows: list[MissRow] = []
        for card in candidates:
            check_deadline("cards")
            bars = deps.bar_store.bars_in_range(
                None, card.ticker, Interval.I1, day_start, day_end,
                end_inclusive=False, as_bars=True)
            replayed = replay_card(card, bars, trade_date=trade_date, window=resolve_window(card.window_ref, trade_date),
                                   session_close=close, positions=positions)
            if replayed.status == "input_stale":
                result.input_stale += 1
                logger.error("replay card {} {}: {}", card.id, card.ticker, replayed.reason)
                deps.out(f"STALE card {card.id} {card.ticker}: {replayed.reason}")
            elif replayed.status == "no_trigger":
                result.no_trigger += 1
            else:
                miss = replayed.miss
                rows.append(miss)
                deps.out(f"MISS card {card.id} {card.ticker} {card.direction} excluded_by={miss.excluded_by} "
                         f"cf_r={miss.cf_r} trigger={miss.trigger_ts.isoformat()} fill={miss.fill_price} "
                         f"exit={miss.exit_reason}@{miss.exit_price} mfe_r={miss.mfe_r}")
        state["card_rows"] = [r.model_dump() for r in rows]
        if not dry_run:
            result.reconcile["card"] = deps.missed.reconcile(
                run_id=result.replay_run_id, trade_date=trade_date, kind="card", rows=rows)
            state["card_rows"] = deps.missed.current(trade_date, "card")
        result.card_misses = len(state["card_rows"])

    def formations_step() -> None:
        context = FormationContext(
            trade_date=trade_date, session_close=close,
            bars_for=lambda ticker: deps.bar_store.bars_in_range(
                None, ticker, Interval.I1, day_start, day_end,
                end_inclusive=False, as_bars=True),
            radar_cards=lambda: deps.missed.radar_cards(trade_date),
        )
        outcome = deps.formation_source(
            trade_date, out=deps.out,
            sources=deps.formation_sources() if deps.formation_sources else None, context=context,
        )
        result.formation_replay = outcome.status
        result.formation_candidates = outcome.counts.candidates
        result.formation_suppressed = outcome.counts.suppressed
        result.formation_no_trigger = outcome.counts.no_trigger
        result.formation_input_stale = outcome.counts.input_stale
        rows = list(outcome.rows)
        for row in rows:
            deps.out(f"MISS formation {row.ticker} {row.direction} member={row.pool_member_id} "
                     f"formed={row.formation_at.isoformat()} excluded_by={row.excluded_by} cf_r={row.cf_r} "
                     f"trigger={row.trigger_ts.isoformat()} fill={row.fill_price} "
                     f"exit={row.exit_reason}@{row.exit_price} mfe_r={row.mfe_r}")
        state["formation_rows"] = [r.model_dump() for r in rows]
        # Keyed on P2 having RUN, never on the row count (plan STEP-1
        # R2-1). `reconcile` retires every predecessor of this run, so a
        # rerun whose formation list is now EMPTY must still reach it —
        # a row-count guard would leave yesterday's rows current forever.
        # The ONE case that skips it is P2 absent, which
        # `formation_replay` marks `FORMATION_UNAVAILABLE` with no rows:
        # nothing ran, so nothing may be retired.
        if outcome.status != FORMATION_UNAVAILABLE and not dry_run:
            result.reconcile["formation"] = deps.missed.reconcile(
                run_id=result.replay_run_id, trade_date=trade_date, kind="formation", rows=rows)
            state["formation_rows"] = deps.missed.current(trade_date, "formation")
        result.formation_misses = len(state["formation_rows"])

    def line_step() -> None:
        body = render_line(trade_date, card_rows=state["card_rows"], mover_rows=state["mover_rows"],
                           settings=state.get("settings"), formation_replay=result.formation_replay,
                           input_stale=result.input_stale,
                           formation_rows=state.get("formation_rows", []),
                           formation_suppressed=result.formation_suppressed,
                           formation_input_stale=result.formation_input_stale)
        path = deps.drc_path(trade_date)
        check_deadline("line (before the vault write)")
        written = write_miss_line(path, body, writer=deps.writer_factory(dry_run))
        result.line_action = written.action
        result.line_diff = written.diff
        deps.out(written.report())

    for name, step in zip(STEPS, (movers_step, cards_step, formations_step, line_step)):
        try:
            check_deadline(name)
            step()
        except Exception as e:  # noqa: BLE001 — named, recorded, re-raised
            result.failed_step = name
            logger.error("replay {} step {} FAILED — {}: {}", trade_date, name, type(e).__name__, e)
            failed = StepFailed(name, e)
            failed.result = result
            raise failed from e
        result.steps_done.append(name)

    if state["archive_failures"]:
        failures = state["archive_failures"]
        raise attach(ReplayError(
            f"{len(failures)} movers archive failure(s): "
            + "; ".join(f"{t}: {err}" for t, err in sorted(failures.items())[:5])
        ))
    return result


__all__ = [
    "DeadlineExceeded", "FORMATION_REQUIRED_FIELDS", "ReplayDeps", "STEPS", "SUPPORTED_EVALUATORS",
    "archiver_precondition", "formation_replay", "replay_deadline", "run_nightly",
]
