"""`cobalt archiver …` — the append-only archiver's operator commands.

Spec: `docs/30 - Design/ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §3
(V3-7), §6, §8, §11, and spec O-4.

FOUR READ-ONLY COMMANDS AND TWO REPAIRS. The read-only four — `audit`,
`incidents`, `progress`, `shadow-report` — are ALWAYS available, and so
is either repair's PREVIEW. Only `restate --apply` and
`backfill-missing --apply` mutate stored bars, and both run inside the
QUIET WINDOW of `cobalt.archiver.quiet` (§8, option A, R8) while holding
the run-level advisory lock (§9).

THERE IS NO `--force`. An override of the window is the owner's word,
recorded by the desk, and is a code or config change — never a flag
(L1, L37). A test asserts the parser rejects it and that the string does
not appear in this file.

`backfill-missing` CAN ONLY DO NOTHING. Its single write path is
`BarStore.insert_new_bars` (`ON CONFLICT … DO NOTHING`); `upsert_bars`
is unreachable from it, and a test asserts the name is absent from its
handler. `restate --apply` is the ONLY command in this build that may
rewrite a stored bar, it needs a `--reason`, and its audit trail lands
on an incident row (spec O-4).
"""

from __future__ import annotations

import argparse
import sys
from datetime import date, datetime

from . import incidents as incidents_mod
from . import progress as progress_mod
from . import quiet as quiet_mod
from . import shadow as shadow_mod
from .models import Interval
from .reconcile import IncidentDraft, IncidentKind, compare, plan_candidates
from .settings import load_archiver_settings
from .store import BarStore

#: Always available (§8). Named here so a test can assert the split
#: rather than infer it from the parser's shape.
READ_ONLY_COMMANDS = ("audit", "incidents", "progress", "shadow-report")

#: Quiet-window gated (§8). Their PREVIEWS are not.
MUTATING_COMMANDS = ("restate", "backfill-missing")


def _now() -> datetime:
    from cobalt.session import clock

    return clock.now_utc()


def _interval(value: str | None) -> Interval | None:
    return None if value is None else Interval(value)


def _store() -> BarStore:
    return BarStore()


def _pool_reader():
    """The ONE pool read behind Q3, as an injectable callable.

    Read-only, on its own connection, and on the SYSTEM side: this is
    `system.radar_pool`, which the radar owns. The archiver reads it and
    writes nothing to it (R8).
    """
    from cobalt.radar.config import load_config as load_radar_config
    from cobalt.radar.store import RadarStore

    store = RadarStore()
    default_key = load_radar_config().pool_key

    def _read(pool_key: str | None = None):
        return store.pool_row(pool_key or default_key)

    return _read


def _observer(settings):
    """A zero-argument observation the quiet guard can re-run."""
    from cobalt.radar.config import load_config as load_radar_config
    from cobalt.session.clock import session_clock

    reader = _pool_reader()
    pool_key = load_radar_config().pool_key
    clock = session_clock()

    def _observe(**_kwargs):
        return quiet_mod.observe(
            now=_now(), pool_reader=reader, clock=clock, pool_key=pool_key
        )

    return _observe


# ---------------------------------------------------------------------
# Read-only commands
# ---------------------------------------------------------------------


def _cmd_progress(args) -> None:
    """Every target's watermark, oldest first. READS ONLY."""
    store = _store()
    with store.target_transaction() as conn:
        rows = progress_mod.all_rows(conn)
    if not rows:
        print("no archive_progress rows — no append night has run yet.")
        return
    print(f"{'ticker':<10} {'iv':<4} {'archived_through':<26} {'export_newest':<26} run")
    for row in rows:
        print(
            f"{row.ticker:<10} {row.interval:<4} "
            f"{row.archived_through.isoformat():<26} "
            f"{row.export_newest.isoformat():<26} {row.run_id}"
        )
    print(f"{len(rows)} target(s).")


def _cmd_incidents(args) -> None:
    """Unresolved incidents, oldest first. READS ONLY.

    This is the list the heartbeat counts: the archiver probe is not
    green while any row here is open (§11, O-7).
    """
    store = _store()
    with store.target_transaction() as conn:
        rows = incidents_mod.unresolved(conn, ticker=getattr(args, "ticker", None))
    if not rows:
        print("no unresolved archive incidents.")
        return
    print(f"{'id':>6} {'kind':<13} {'ticker':<10} {'iv':<4} {'first seen':<26} range")
    for row in rows:
        span = (
            f"{row.range_start.isoformat()} -> {row.range_end.isoformat()}"
            if row.range_start and row.range_end
            else "-"
        )
        print(
            f"{row.id:>6} {row.kind:<13} {row.ticker:<10} {row.interval:<4} "
            f"{row.first_seen_at.isoformat():<26} {span}"
        )
    print(f"{len(rows)} unresolved. Resolve one: cobalt archiver incidents resolve <id> --by <who> --note <why>")


def _cmd_incidents_resolve(args) -> None:
    """Close one incident, on the record. Explicit and audited (§11)."""
    store = _store()
    now = _now()
    with store.target_transaction() as conn:
        incidents_mod.resolve(
            conn, args.incident_id, by=args.by, note=args.note, now=now
        )
    print(f"incident {args.incident_id} resolved by {args.by} at {now.isoformat()}.")


def _cmd_audit(args) -> None:
    """READ-ONLY coverage report over the stored range (§3 V3-7).

    It states its ACTUAL bounds and says plainly that older vendor
    additions or corrections need a wider audit — the horizon IS the
    candidate range, and a report that implied otherwise would be
    claiming coverage nobody measured.
    """
    store = _store()
    with store.target_transaction() as conn:
        rows = progress_mod.all_rows(conn)
        open_incidents = incidents_mod.unresolved(conn)
    since = args.from_date
    print(f"archiver audit — from {since.isoformat() if since else 'the stored range'}")
    print(f"{'ticker':<10} {'iv':<4} {'archived_through':<26} {'incidents':<10} status")
    by_target: dict[tuple[str, str], int] = {}
    for incident in open_incidents:
        key = (incident.ticker, incident.interval)
        by_target[key] = by_target.get(key, 0) + 1
    for row in rows:
        if since and row.archived_through.date() < since:
            status = "BEHIND"
        else:
            status = "ok"
        count = by_target.get((row.ticker, row.interval), 0)
        print(
            f"{row.ticker:<10} {row.interval:<4} {row.archived_through.isoformat():<26} "
            f"{count:<10} {status if not count else 'INCIDENT'}"
        )
    print(
        f"{len(rows)} target(s), {len(open_incidents)} unresolved incident(s). "
        "This audit covers the stored range only: older vendor additions or "
        "corrections need a wider audit (spec §3 V3-7)."
    )


def _cmd_shadow_report(args) -> None:
    """The nights the shadow compare recorded. READS FILES ONLY.

    Across nights it says which differing keys PERSISTED, VANISHED or
    APPEARED — the retained baseline Astra and Grok required, because
    refreshed storage alone cannot show revision frequency.
    """
    nights = shadow_mod.recent_nights(args.nights)
    if not nights:
        print(f"no shadow artifacts under {shadow_mod.SHADOW_DIR}.")
        return
    print(f"{'night':<12} {'targets':>8} {'withhold':>9} {'late':>6} {'new':>6}")
    for label, records in nights:
        withhold = sum(
            1 for r in records if r.get("bootstrap", {}).get("would_withhold")
        )
        late = sum(r.get("bootstrap", {}).get("late", 0) for r in records)
        fresh = sum(r.get("bootstrap", {}).get("new", 0) for r in records)
        print(f"{label:<12} {len(records):>8} {withhold:>9} {late:>6} {fresh:>6}")
    verdict = shadow_mod.persisted_vanished_appeared(nights)
    for name in ("persisted", "vanished", "appeared"):
        keys = verdict[name]
        print(f"{name}: {len(keys)}")
        for key in keys[:20]:
            print(f"    {key[0]}/{key[1]} @ {key[2]}")
    print(
        "A difference that VANISHED was healed by the very nightly overlay "
        "`append` would stop doing — which is why this baseline is retained "
        "and why a post-write audit cannot answer the question."
    )


# ---------------------------------------------------------------------
# Repairs — quiet-window gated
# ---------------------------------------------------------------------


def _preview_header(ticker: str, interval, what: str) -> None:
    print(f"{what} PREVIEW — {ticker}/{interval or 'every archived interval'}")
    print("Nothing is written. Re-run with --apply inside a quiet window to execute.")


def _cmd_restate(args) -> None:
    """Rewrite stored bars for ONE target from the vendor's export.

    The ONLY command in this build that may overwrite a stored bar, and
    the reason `upsert_bars` still exists outside the poller. PREVIEW
    first, always; `--apply` needs a `--reason`, runs inside the quiet
    window with a pre-commit re-check, and leaves its audit on an
    incident row (spec O-4).
    """
    settings = load_archiver_settings()
    store = _store()
    ticker = args.ticker.strip().upper()
    interval = _interval(args.interval)

    if not args.apply:
        _preview_header(ticker, args.interval, "restate")
        _print_differences(store, ticker, interval)
        print(
            "The vendor window covers only the exported range; stored history "
            "outside it stays UNRESOLVED by this command."
        )
        return

    observe = _observer(settings)
    with store.run_lock(f"restate --apply {ticker}"):
        with quiet_mod.guarded_repair(
            observe=observe, settings=settings, what="restate --apply"
        ) as guard:
            now = _now()
            with store.target_transaction() as conn:
                written = _apply_restate(store, conn, ticker, interval)
                incidents_mod.open_or_refresh(
                    conn,
                    IncidentDraft(
                        kind=IncidentKind.RESTATED,
                        ticker=ticker,
                        interval=(interval.value if interval else "*"),
                        detail={
                            "repair": "restate --apply",
                            "reason": args.reason,
                            "rows_rewritten": written,
                            "at": now.isoformat(),
                        },
                    ),
                    run_id=f"restate@{now.isoformat()}",
                    now=now,
                )
                # THE PRE-COMMIT RE-CHECK (§8). Raising here rolls the
                # whole repair back — a start-time check alone is what
                # Astra's open-boundary sequence defeats.
                guard.check_before_commit()
    print(f"restate --apply: {written} row(s) rewritten for {ticker}. Reason: {args.reason}")


def _cmd_backfill_missing(args) -> None:
    """Insert bars the export carries and storage does not. DO NOTHING only.

    This command can NEVER overwrite: its single write path is
    `insert_new_bars` (`ON CONFLICT … DO NOTHING`). A differing key is
    left exactly as it is and stays a `restate` decision for a person.
    """
    settings = load_archiver_settings()
    store = _store()
    ticker = args.ticker.strip().upper()
    interval = _interval(args.interval)

    if not args.apply:
        _preview_header(ticker, args.interval, "backfill-missing")
        _print_missing(store, ticker, interval)
        return

    observe = _observer(settings)
    with store.run_lock(f"backfill-missing {ticker}"):
        with quiet_mod.guarded_repair(
            observe=observe, settings=settings, what="backfill-missing"
        ) as guard:
            with store.target_transaction() as conn:
                inserted = store.insert_new_bars(conn, _missing_bars(store, ticker, interval))
                guard.check_before_commit()
    print(f"backfill-missing: {inserted} row(s) inserted for {ticker} (existing rows untouched).")


# ---------------------------------------------------------------------
# The pieces the repairs share
# ---------------------------------------------------------------------


def _fetch_for(ticker: str, interval: Interval):
    import asyncio

    from .collector import fetch_bars, resolve_token

    async def _run():
        token = await resolve_token()
        return await fetch_bars(ticker, interval, token)

    return asyncio.run(_run())


def _intervals_for(store, ticker: str, interval: Interval | None) -> list[Interval]:
    if interval is not None:
        return [interval]
    with store.target_transaction() as conn:
        rows = progress_mod.all_rows(conn)
    return [Interval(row.interval) for row in rows if row.ticker == ticker] or [Interval.I1]


def _compared(store, ticker: str, interval: Interval):
    bars = _fetch_for(ticker, interval)
    plan = plan_candidates(
        ticker=ticker, interval=interval, bars=bars, fetch_started_at=_now(),
        archived_through=None,
    )
    with store.target_transaction() as conn:
        held = store._bars_in_range(
            conn, ticker, interval, plan.range_start, plan.range_end
        )
    return plan, compare(plan.candidates, held)


def _print_differences(store, ticker: str, interval: Interval | None) -> None:
    for one in _intervals_for(store, ticker, interval):
        plan, result = _compared(store, ticker, one)
        print(
            f"  {ticker}/{one.value}: {len(plan.candidates)} candidate(s), "
            f"{len(result.differing)} differing, {len(result.incoming_only)} missing, "
            f"{len(result.stored_only)} stored-only"
        )
        for difference in result.differing[:20]:
            fields = ", ".join(
                f"{f.field} {f.stored} -> {f.vendor}" for f in difference.fields
            )
            print(f"      {difference.ts.isoformat()}  {fields}")


def _print_missing(store, ticker: str, interval: Interval | None) -> None:
    for one in _intervals_for(store, ticker, interval):
        plan, result = _compared(store, ticker, one)
        print(
            f"  {ticker}/{one.value}: {len(result.incoming_only)} key(s) would be "
            f"inserted; {len(result.differing)} differing key(s) would be LEFT "
            "ALONE (this command can only DO NOTHING)."
        )


def _missing_bars(store, ticker: str, interval: Interval | None) -> list:
    out = []
    for one in _intervals_for(store, ticker, interval):
        plan, result = _compared(store, ticker, one)
        missing = set(result.incoming_only)
        out.extend(b for b in plan.candidates if b.ts in missing)
    return out


def _apply_restate(store, conn, ticker: str, interval: Interval | None) -> int:
    """The one overwrite in this build, and it is the same
    `ON CONFLICT DO UPDATE` the poller and the `upsert` night use — but
    ON `conn`, the repair's own transaction.

    That is the whole of the tribunal's F1: `upsert_bars` opens and
    commits a connection of its own, so the rows it wrote outlived the
    rollback that §8's pre-commit re-check raises, and "a failed
    re-check = ROLLBACK, no bar row surviving" was not true for the one
    command that may overwrite a bar. `upsert_bars_on` takes the
    connection, exactly as `insert_new_bars` already did for
    `backfill-missing`.
    """
    written = 0
    for one in _intervals_for(store, ticker, interval):
        plan, result = _compared(store, ticker, one)
        keys = {d.ts for d in result.differing}
        rows = [b for b in plan.candidates if b.ts in keys]
        written += store.upsert_bars_on(conn, rows)
    return written


# ---------------------------------------------------------------------
# The parser
# ---------------------------------------------------------------------


HANDLERS = {
    "audit": _cmd_audit,
    "incidents": _cmd_incidents,
    "progress": _cmd_progress,
    "shadow-report": _cmd_shadow_report,
    "restate": _cmd_restate,
    "backfill-missing": _cmd_backfill_missing,
}


def add_parser(sub) -> None:
    group = sub.add_parser(
        "archiver", help="Bar Archiver progress, incidents, audits and repairs"
    )
    asub = group.add_subparsers(dest="command", required=True)

    progress_cmd = asub.add_parser("progress", help="Every target's watermark (read-only).")
    progress_cmd.set_defaults(func=_cmd_progress)

    incidents_cmd = asub.add_parser(
        "incidents", help="Unresolved archive incidents (read-only)."
    )
    isub = incidents_cmd.add_subparsers(dest="incidents_command")
    incidents_cmd.add_argument("--ticker")
    incidents_cmd.set_defaults(func=_cmd_incidents)

    resolve = isub.add_parser("resolve", help="Close one incident, on the record.")
    resolve.add_argument("incident_id", type=int)
    resolve.add_argument("--by", required=True, help="Who resolved it — mandatory.")
    resolve.add_argument("--note", required=True, help="Why — lands on the row.")
    resolve.set_defaults(func=_cmd_incidents_resolve)

    audit = asub.add_parser("audit", help="Coverage over the stored range (read-only).")
    audit.add_argument(
        "--from", dest="from_date", type=date.fromisoformat, metavar="YYYY-MM-DD"
    )
    audit.set_defaults(func=_cmd_audit, from_date=None)

    shadow_report = asub.add_parser(
        "shadow-report", help="What the pre-write shadow compare saw (read-only)."
    )
    shadow_report.add_argument("--nights", type=int, default=5)
    shadow_report.set_defaults(func=_cmd_shadow_report)

    restate = asub.add_parser(
        "restate",
        help="Rewrite differing stored bars for ONE target. Preview by default.",
    )
    restate.add_argument("ticker")
    restate.add_argument("interval", nargs="?", choices=[i.value for i in Interval])
    restate.add_argument(
        "--apply", action="store_true", help="Execute, inside a quiet window (§8)."
    )
    restate.add_argument("--reason", help="Mandatory with --apply; lands on the incident row.")
    restate.set_defaults(func=_cmd_restate)

    backfill = asub.add_parser(
        "backfill-missing",
        help="Insert bars storage lacks. DO NOTHING only — never overwrites.",
    )
    backfill.add_argument("ticker")
    backfill.add_argument("interval", nargs="?", choices=[i.value for i in Interval])
    backfill.add_argument(
        "--apply", action="store_true", help="Execute, inside a quiet window (§8)."
    )
    backfill.set_defaults(func=_cmd_backfill_missing)


class _Parser(argparse.ArgumentParser):
    """argparse cannot say "required WITH another flag", and a check that
    only runs in `main()` would let a caller build the namespace without
    it. Validating inside `parse_args` keeps the rule where the parser
    is, which is where a test looks for it."""

    def parse_args(self, args=None, namespace=None):
        parsed = super().parse_args(args, namespace)
        _validate_args(parsed)
        return parsed


def build_parser() -> argparse.ArgumentParser:
    """The `archiver` group alone, for tests and for `--help`."""
    parser = _Parser(prog="cobalt")
    sub = parser.add_subparsers(dest="group", required=True)
    add_parser(sub)
    return parser


def _validate_args(args) -> None:
    if getattr(args, "command", None) == "restate" and args.apply and not args.reason:
        raise SystemExit(
            "restate --apply requires --reason: the repair's audit trail lands on "
            "an incident row and 'because' is not one (spec O-4)."
        )


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
    except quiet_mod.QuietRefused as refused:
        print(str(refused), file=sys.stderr)
        return refused.exit_code
    return 0


__all__ = [
    "HANDLERS",
    "MUTATING_COMMANDS",
    "READ_ONLY_COMMANDS",
    "add_parser",
    "build_parser",
    "main",
]
