"""`cobalt` — the new core's top-level CLI.

Two command groups:

    cobalt vault restore --write-id N [--dry-run]
    cobalt vault writes [--limit N]
    cobalt vault overrides --note PATH

    cobalt session now [--at ISO8601]
    cobalt session backfill [--dry-run]
    cobalt session blocks [--limit N]

    cobalt cards state/history/move/backfill/expire/edges

    cobalt daymode show/propose/decide/attest

    cobalt validate

`restore` puts a section back to the before-state recorded in
`vault_writes` id N, and it does so THROUGH THE SAME WRITER — same
markers, same mtime/hash guard, same atomic rename, and its own audit
row. There is no second write path, not even for undo.

`session` is the F1 clock (Charter §3 F1); `cards` is the F7 state
machine (Charter §3 F7); `daymode` is F6's two-stage mode.
`validate` is the config gate
(F16) — the same `python -m cobalt.taxonomy.validate` the tests run,
given a name an operator can remember.
"""

import os

os.environ.setdefault("LOGURU_LEVEL", "INFO")

import argparse  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

from dotenv import load_dotenv  # noqa: E402

# The Postgres parts db.connect() composes its DSN from live in the repo
# .env today (TRIAGE 2.7's vault-parts redesign replaces this). The
# prefill/aset entrypoints get them by ACCIDENT — a transitive old-tree
# import calls load_dotenv() somewhere down their chain. This CLI has no
# such chain, so it loads the same file deliberately and visibly.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

from cobalt.aset.config import load_config as load_aset_config  # noqa: E402
from cobalt.cards import cli as cards_cli  # noqa: E402
from cobalt.daymode import cli as daymode_cli  # noqa: E402
from cobalt.session import cli as session_cli  # noqa: E402
from cobalt.taxonomy import validate as taxonomy_validate  # noqa: E402
from cobalt.vaultwrite import VaultWriter, VaultWriteStore  # noqa: E402


def _store() -> VaultWriteStore:
    store = VaultWriteStore()
    store.ensure_schema()
    return store


def _cmd_restore(args: argparse.Namespace) -> None:
    store = _store()
    writer = VaultWriter("vault.restore", store=store, dry_run=args.dry_run)
    result = writer.restore(args.write_id)
    print(result.report())


def _cmd_writes(args: argparse.Namespace) -> None:
    for row in _store().recent(limit=args.limit):
        print(
            f"{row['id']:>6}  {row['ts']:%Y-%m-%d %H:%M:%S}  {row['writer']:<20} "
            f"{row['section'] or '-':<18} {row['unit'] or '-':<28} {row['note']}"
        )


def _cmd_overrides(args: argparse.Namespace) -> None:
    rows = _store().overrides_for(args.note)
    if not rows:
        print(f"no overrides recorded for {args.note}")
        return
    for row in rows:
        kind = "conflict" if row["conflict"] else "human edit"
        print(
            f"{row['id']:>6}  {row['ts']:%Y-%m-%d %H:%M:%S}  {kind}  "
            f"{row['section']}/{row['unit']}\n"
            f"        cobalt: {row['cobalt_text']!r}\n"
            f"        human : {row['human_text']!r}"
        )


def _cmd_validate(args: argparse.Namespace) -> None:
    """F16: `cobalt validate`. One name for the config gate, wrapping the
    taxonomy validator (which owns the checks) plus the two config
    families it does not cover — the NYSE calendar and the session
    boundaries, both introduced by F1. No second implementation: this
    calls the same loaders the runtime does, so a config that passes here
    is a config the runtime can boot on."""
    from cobalt.session.calendar import load_calendar
    from cobalt.session.clock import BOUNDARY_KEYS, SessionClock
    from cobalt.taxonomy.loader import load_tunables

    rc = taxonomy_validate.main()
    if rc != 0:
        sys.exit(rc)

    calendar = load_calendar()
    print(
        f"\nNYSE calendar: years {calendar.covered_years} loaded OK "
        f"({calendar.holiday_count} holidays, "
        f"{calendar.early_close_count} early closes)."
    )
    # Building the clock IS the check: from_config() fails loud on a
    # missing row, a wrong unit, an unparseable time, or an ordering that
    # would produce a negative-length window.
    SessionClock.from_config(calendar)
    print(
        f"Session boundaries: {len(BOUNDARY_KEYS)} tunables rows resolved, "
        "ordering OK."
    )

    # F16 sweep, S1-P2: the two config families this sprint introduced.
    # Same rule as above — building the object IS the check, because the
    # loaders fail loud on a dangling pointer, an unknown mode, a grade
    # that would WIDEN the account ladder, or a sheet missing from
    # `order`. A config that passes here is one the runtime can boot on.
    from cobalt.aset.config import load_sheet_modes_config
    from cobalt.cards.models import ALLOWED, TERMINAL, CardState
    from cobalt.daymode.config import load_daymode_config
    from cobalt.daymode.propose import BAND_MAX_KEY, BAND_MIN_KEY

    sheets = load_sheet_modes_config()
    print(
        f"\nSheets: {len(sheets.order)} declared, low to high "
        f"{' < '.join(sheets.order)} (ordered list, not a hardcoded pair)."
    )

    dm = load_daymode_config(sheets)
    print(
        f"Day modes: ladder {' < '.join(dm.modes)}; enabled {dm.enabled_modes}; "
        f"stage-1 floor {dm.lowest_enabled} -> {dm.sheet_for(dm.lowest_enabled)} sheet, "
        f"keys {[g.value for g in dm.enabled_grades_for(dm.lowest_enabled)]}."
    )
    print(
        f"Hotkey files: {', '.join(f'{h.file}={h.mode}' for h in dm.hotkey_files)} "
        "(attested, never read — Cobalt does not touch DAS)."
    )

    registry = load_tunables().by_key
    for key in (BAND_MIN_KEY, BAND_MAX_KEY):
        row = registry.get(key)
        if row is None:
            print(f"FAILED: tunable {key!r} is missing — F6 has no built-in default (F16).")
            sys.exit(1)
        state = "PLACEHOLDER (unruled)" if row.value is None else repr(row.value)
        print(f"Tunable {key}: {state}, consumers {row.consumers}")

    # The edge table is data; a state with no way in or out is a config
    # error in code form, and it is worth catching in the same gate.
    unreachable = [
        s.value for s in CardState
        if s is not CardState.WATCH and not any(s in to for to in ALLOWED.values())
    ]
    if unreachable:
        print(f"FAILED: card state(s) with no inbound edge: {unreachable}")
        sys.exit(1)
    print(
        f"Card states: {len(CardState)} states, "
        f"{sum(len(t) for t in ALLOWED.values())} legal edges, "
        f"{len(TERMINAL)} terminal, every state reachable."
    )


def main() -> None:
    parser = argparse.ArgumentParser(prog="cobalt", description="Cobalt new-core CLI")
    sub = parser.add_subparsers(dest="group", required=True)

    vault = sub.add_parser("vault", help="Vault write-path tools (LAW L28)")
    vsub = vault.add_subparsers(dest="command", required=True)

    restore = vsub.add_parser("restore", help="Restore a section to a recorded before-state.")
    restore.add_argument("--write-id", type=int, required=True, help="vault_writes row id")
    restore.add_argument("--dry-run", action="store_true", help="Show the diff, write nothing.")
    restore.set_defaults(func=_cmd_restore)

    writes = vsub.add_parser("writes", help="List recent vault writes.")
    writes.add_argument("--limit", type=int, default=20)
    writes.set_defaults(func=_cmd_writes)

    overrides = vsub.add_parser("overrides", help="List recorded human overrides for a note.")
    overrides.add_argument("--note", required=True, help="Absolute note path as recorded")
    overrides.set_defaults(func=_cmd_overrides)

    session_cli.add_parser(sub)
    cards_cli.add_parser(sub)
    daymode_cli.add_parser(sub)

    validate = sub.add_parser(
        "validate", help="Validate every config family (F16 sweep gate)."
    )
    validate.set_defaults(func=_cmd_validate)

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
