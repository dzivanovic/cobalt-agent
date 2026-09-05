"""`cobalt daymode` — F6's command surface.

    cobalt daymode show [--date YYYY-MM-DD]
    cobalt daymode propose [--date YYYY-MM-DD] [--at ISO8601] [--dry-run]
    cobalt daymode decide --mode M [--reason ...] [--date ...]
    cobalt daymode attest --file half.htk [--date ...]

`propose` is what launchd runs at 09:00 (`com.cobalt.daymode-propose`).
It gathers its four inputs — the prior trading day's FILLED count and any
daily-stop marker, the calendar, the trade-count band, and the prior DRC
note — and writes ONE `day_modes` row. On a Sunday or a holiday it
writes nothing and says so.
"""

from __future__ import annotations

import argparse
from datetime import date, datetime

from cobalt import env
from cobalt.session.clock import now_utc, session_clock
from cobalt.taxonomy.loader import load_tunables

from .config import load_daymode_config
from .drc import prior_day_inputs
from .propose import BAND_MAX_KEY, BAND_MIN_KEY, decided_or_stage1, propose, stage1_mode
from .store import DayModeStore


def _day(args: argparse.Namespace) -> date:
    if getattr(args, "date", None):
        return date.fromisoformat(args.date)
    return session_clock().to_et(_at(args)).date()


def _at(args: argparse.Namespace) -> datetime:
    if not getattr(args, "at", None):
        return now_utc()
    ts = datetime.fromisoformat(args.at)
    if ts.tzinfo is None:
        raise SystemExit(f"--at {args.at!r} has no timezone — pass an offset or 'Z'.")
    return ts


def _store() -> DayModeStore:
    store = DayModeStore()
    store.ensure_schema()
    return store


def _band() -> tuple[object, object]:
    """The trade-count band from tunables. PLACEHOLDER until ruled — a
    missing ROW is a config error (F16), a null VALUE is 'not ruled yet'
    and is an adverse signal, not a crash."""
    registry = load_tunables().by_key
    out = []
    for key in (BAND_MIN_KEY, BAND_MAX_KEY):
        row = registry.get(key)
        if row is None:
            raise SystemExit(
                f"tunable {key!r} is missing from tunables.yaml — F6 reads the band "
                "from config and has no built-in default (F16)."
            )
        out.append(row.value)
    return (out[0], out[1])


def cmd_show(args: argparse.Namespace) -> None:
    cfg = load_daymode_config()
    day = _day(args)
    row = _store().for_date(day)
    print(f"date          : {day}  ({session_clock().calendar.describe(day)})")
    print(f"ladder        : {' < '.join(cfg.modes)}   enabled={cfg.enabled_modes}")
    print(f"reduced ->    : {cfg.sheet_for('reduced')} sheet, keys "
          f"{[g.value for g in cfg.enabled_grades_for('reduced')]}")
    print(f"stage-1 mode  : {stage1_mode(cfg)}")
    if row is None:
        print("day_modes row : none (stage 1 in force — no 09:00 proposal yet)")
        return
    print(f"proposed      : {row['proposed'] or '(none)'}")
    print(f"decided       : {row['decided'] or '(undecided — stage 1 still in force)'}"
          + (f"  by {row['decided_by']}" if row["decided"] else ""))
    if row["overrule_reason"]:
        print(f"overrule      : {row['overrule_reason']}")
    print(f"attested .htk : {row['attested_sheet'] or '(none attested)'}")
    print(f"in force      : {decided_or_stage1(row, cfg)}")
    print(f"reason        : {row['reason']}")


def cmd_propose(args: argparse.Namespace) -> None:
    cfg = load_daymode_config()
    day = _day(args)
    ts = _at(args)
    store = _store()
    print(f"database  : {store.db_name}  (COBALT_ENV={env.resolve_env()})")
    print(f"date      : {day}  ({session_clock().calendar.describe(day)})")

    inputs = prior_day_inputs(day)
    proposal = propose(
        day,
        cfg=cfg,
        prior_filled=inputs.filled_count,
        daily_stop_hit=inputs.daily_stop_hit,
        drc_note=inputs.drc_note,
        drc_informative=inputs.drc_informative,
        band=_band(),
    )
    if proposal is None:
        print("NOT A TRADING DAY — no proposal, no row. (F6: a weekend is not an error.)")
        return
    print(f"proposed  : {proposal.proposed}")
    print(f"reason    : {proposal.reason}")
    if args.dry_run:
        print("DRY RUN — nothing written.")
        return
    store.upsert_proposal(day, proposed=proposal.proposed, reason=proposal.reason, now=ts)
    print("WROTE day_modes row.")


def cmd_decide(args: argparse.Namespace) -> None:
    day = _day(args)
    row = _store().decide(
        day, decided=args.mode, decided_by="you", overrule_reason=args.reason
    )
    verdict = "APPROVED" if row["decided"] == row["proposed"] else "OVERRULED"
    print(f"{day}: {verdict} — proposed {row['proposed']}, decided {row['decided']}")
    if row["overrule_reason"]:
        print(f"reason: {row['overrule_reason']}")


def cmd_attest(args: argparse.Namespace) -> None:
    cfg = load_daymode_config()
    mode = cfg.mode_for_hotkey_file(args.file)   # refuses an unknown file
    day = _day(args)
    _store().attest_sheet(day, filename=args.file)
    print(f"{day}: attested {args.file} (= {mode} rung). Attested, NOT read — "
          "Cobalt never touches DAS.")


def add_parser(sub) -> None:
    dm = sub.add_parser("daymode", help="F6 two-stage day mode (Charter §3 F6)")
    dsub = dm.add_subparsers(dest="command", required=True)

    show = dsub.add_parser("show", help="The ladder, the row, and the mode in force.")
    show.add_argument("--date")
    show.set_defaults(func=cmd_show)

    prop = dsub.add_parser("propose", help="The 09:00 proposal (launchd runs this).")
    prop.add_argument("--date")
    prop.add_argument("--at", help="ISO 8601 instant WITH offset, instead of now.")
    prop.add_argument("--dry-run", action="store_true")
    prop.set_defaults(func=cmd_propose)

    decide = dsub.add_parser("decide", help="Approve or overrule the proposal.")
    decide.add_argument("--mode", required=True)
    decide.add_argument("--reason", default=None, help="Required when overruling.")
    decide.add_argument("--date")
    decide.set_defaults(func=cmd_decide)

    attest = dsub.add_parser("attest", help="State which .htk you have loaded.")
    attest.add_argument("--file", required=True)
    attest.add_argument("--date")
    attest.set_defaults(func=cmd_attest)


__all__ = ["add_parser"]
