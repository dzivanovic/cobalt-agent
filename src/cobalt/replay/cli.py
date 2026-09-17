"""`cobalt replay nightly [--date YYYY-MM-DD] [--dry-run]` — com.cobalt.replay.

The scheduled 21:05 ET entry point (S2-P4 R3), wrapped by
`as_job("com.cobalt.replay")`. `--dry-run` runs `as_job(..., skip=True)`
— no jobs row is touched — and every store call it makes is a read; the
vault writer runs its own dry-run diff path. `--date` replays a past day
from what was retained (exports in the radar cache, bars in system.bars);
it never relabels a live fetch as history.

`job.result` = `ReplayResult`: movers, archived, card_misses,
mover_misses, formation_replay, line_action, plus the coverage counts
(input_stale, archive_failures, archive_incomplete) and the line diff.
"""

from __future__ import annotations

import argparse
from datetime import date, datetime
from pathlib import Path

from cobalt.session.clock import ET

from .models import ReplayError
from .runner import ReplayDeps, run_nightly


def now_et() -> datetime:
    from cobalt.session import clock

    return clock.now_utc().astimezone(ET)


def default_deps(*, dry_run: bool) -> ReplayDeps:
    """The production wiring. Nothing here writes on construction; a dry
    run never reaches an `ensure_schema`."""
    from cobalt.archiver.collector import resolve_token
    from cobalt.archiver.store import BarStore
    from cobalt.jobs.config import load_job_registry
    from cobalt.jobs.store import JobStore
    from cobalt.radar.collector import process_bucket
    from cobalt.radar.store import RadarStore
    from cobalt.session import Session, session_clock
    from cobalt.session import clock as clock_mod
    from cobalt.settings.store import TraderSettingsStore
    from cobalt.taxonomy.loader import load_tunables
    from cobalt.vaultwrite import VaultWriter, VaultWriteStore

    from .cards import MissedStore
    from .line import WRITER, drc_note_path
    from .movers import MoversCollector, MoversStore, load_radar_config

    tunables = load_tunables().by_key
    raw = tunables["radar.finviz_max_rpm"].value
    ceiling = None if raw is None else int(raw)
    config = load_radar_config()
    cache_root = Path(config.cache.dir)

    def session_bounds(day: date):
        clock = session_clock()
        rth = next((w for w in clock.windows_for(day) if w.session is Session.RTH), None)
        if rth is None:
            raise ReplayError(f"{day} is not a trading day ({clock.calendar.describe(day)})")
        return datetime.combine(day, rth.start, tzinfo=ET), datetime.combine(day, rth.end, tzinfo=ET)

    async def collector_factory():
        if ceiling is None:
            raise ReplayError("radar.finviz_max_rpm is unmeasured")
        return MoversCollector(await resolve_token(), config=config, bucket=process_bucket(ceiling),
                               cache_root=cache_root)

    def writer_factory(is_dry: bool):
        store = VaultWriteStore()
        if not is_dry:
            store.ensure_schema()
        return VaultWriter(WRITER, store=store, dry_run=is_dry)

    return ReplayDeps(
        job_store=JobStore(), registry=load_job_registry(), tunables=tunables, now=clock_mod.now_utc,
        session_bounds=session_bounds, settings_values=TraderSettingsStore().values, missed=MissedStore(),
        movers_store=MoversStore(), bar_store=BarStore(), radar_store=RadarStore(), radar_config=config,
        collector_factory=collector_factory, cache_root=cache_root, writer_factory=writer_factory,
        drc_path=drc_note_path, out=print, ceiling=ceiling,
    )


def cmd_nightly(args: argparse.Namespace) -> None:
    from cobalt.jobs.entrypoint import as_job
    from cobalt.radar.notes import REPLAY_LABEL

    trade_date = date.fromisoformat(args.date) if args.date else now_et().date()
    with as_job(REPLAY_LABEL, skip=args.dry_run) as job:
        deps = default_deps(dry_run=args.dry_run)
        try:
            result = run_nightly(trade_date, dry_run=args.dry_run, deps=deps)
        except ReplayError as e:
            partial = getattr(e, "result", None)
            if partial is not None:
                job.result = partial.job_result()
            raise
        job.result = result.job_result()
    print(
        f"replay {trade_date}{' DRY RUN' if args.dry_run else ''}: movers {result.movers} · archived "
        f"{result.archived} · card misses {result.card_misses} · mover misses {result.mover_misses} · "
        f"input_stale {result.input_stale} · formations {result.formation_replay} · line {result.line_action}"
    )


def _add_commands(sub) -> None:
    nightly = sub.add_parser("nightly", help="The 21:05 ET replay: movers, card misses, the DRC miss line.")
    nightly.add_argument("--date", help="Replay a past ET trade date from retained inputs (YYYY-MM-DD).")
    nightly.add_argument("--dry-run", action="store_true", help="Write nothing; print rows and the line diff.")
    nightly.set_defaults(func=cmd_nightly)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="replay")
    _add_commands(parser.add_subparsers(dest="command", required=True))
    return parser


def add_parser(sub) -> None:
    group = sub.add_parser("replay", help="The nightly replay (S2-P4, com.cobalt.replay)")
    _add_commands(group.add_subparsers(dest="command", required=True))


__all__ = ["add_parser", "build_parser", "cmd_nightly", "default_deps", "now_et"]
