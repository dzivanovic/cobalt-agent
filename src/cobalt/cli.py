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

    cobalt db migrate [--allow-prod] [--rollback]
    cobalt taxonomy load [--dry-run]

    cobalt jobs list/register/check/run
    cobalt heartbeat beat/show
    cobalt notify email-auth/email-test/email-status
    cobalt backup run/status/restore
    cobalt stop / cobalt resume        (F17d kill phrase)

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
from cobalt.db_migrations import cli as db_cli  # noqa: E402
from cobalt.backup import cli as backup_cli  # noqa: E402
from cobalt.heartbeat import cli as heartbeat_cli  # noqa: E402
from cobalt.jobs import cli as jobs_cli  # noqa: E402
from cobalt.jobs.wrapper import JobStopped  # noqa: E402
from cobalt.notify import cli as notify_cli  # noqa: E402
from cobalt.session import cli as session_cli  # noqa: E402
from cobalt.taxonomy import cli as taxonomy_cli  # noqa: E402
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

    # KNOWN COUPLING, made loud here rather than discovered live.
    # `sheet_modes` is now an ordered config list, but `SizingInput.
    # sheet_mode` is still the `SheetMode` enum (full/half) — it is on
    # the live sizing path and was not reshaped this sprint. So a sheet
    # declared in config with no enum member would pass every day-mode
    # check and then fail at card-creation time, at 09:31 on a live
    # morning. This turns that into a config-gate failure.
    # TODO (whenever the quarter sheet lands): either add its enum member
    # in the same change as its config row, or retire the enum in favour
    # of a config-validated string on SizingInput.
    from cobalt.aset.models import SheetMode

    unmodelled = [s for s in sheets.order if s not in {m.value for m in SheetMode}]
    if unmodelled:
        print(
            f"FAILED: sheet(s) {unmodelled} are declared in configs/cobalt/aset.yaml "
            f"but have no SheetMode enum member (have: "
            f"{sorted(m.value for m in SheetMode)}). A card sized on one would be "
            "refused by Pydantic at creation time. Add the member in the same change "
            "as the config row."
        )
        sys.exit(1)

    dm = load_daymode_config(sheets)
    print(
        f"Day modes: ladder {' < '.join(dm.modes)}; enabled {dm.enabled_modes}; "
        f"stage-1 floor {dm.lowest_enabled} -> {dm.sheet_for(dm.lowest_enabled)} sheet, "
        f"keys {[g.value for g in dm.enabled_grades_for(dm.lowest_enabled)]}."
    )
    print(
        f"Hotkey files (derived from the sheets via "
        f"daymode.hotkey_file_template={dm.hotkey_file_template!r}): "
        f"{', '.join(f'{dm.hotkey_file_for_sheet(s)}={s}' for s in dm.sheet_order)} "
        "(attested, never read — Cobalt does not touch DAS)."
    )
    print(
        "Step-downs: "
        + "; ".join(
            f"{r.signal}={r.effect}" + (f"({r.rungs})" if r.effect == "down" else "")
            for r in dm.stepdowns
        )
        + f" — {len(dm.stepdowns)} row(s), every computable signal ruled."
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

    # ---- F16 sweep, S1-P3: the three config families this prompt adds.
    # Same rule as everything above — building the object IS the check,
    # and the cross-checks below are the ones no single loader can do
    # because they compare two files that cannot read each other.
    import plistlib

    from cobalt.jobs.config import load_job_registry
    from cobalt.notify.config import load_notify_config
    from cobalt.redact.config import load_redact_config

    redact_cfg = load_redact_config()
    print(
        f"\nRedaction (F19): {len(redact_cfg.patterns)} pattern(s) compiled, "
        f"placeholder {redact_cfg.placeholder!r}, literal floor "
        f"{redact_cfg.literal_min_length} chars."
    )
    from cobalt.redact.secrets import load_literals

    guard = load_literals(redact_cfg.literal_min_length)
    print(
        f"  literal guard: {'ACTIVE' if guard.available else 'INACTIVE'} — "
        + (f"{len(guard)} vault value(s), names only: {', '.join(guard.names)}"
           if guard.available else guard.reason)
    )

    notify_cfg = load_notify_config()
    print(
        f"Notify: mattermost {'enabled' if notify_cfg.mattermost.enabled else 'DISABLED'}, "
        f"DM -> @{notify_cfg.mattermost.dm_username}, credential from vault key "
        f"{notify_cfg.mattermost.vault_key!r} (never printed)."
    )

    # F16 sweep, S1-P4: the email channel's two numbers and its three
    # vault keys. NAMES ONLY — `secret_names()` is the vault's whole
    # public listing and it returns keys, never values.
    from cobalt.notify.config import CLIENT_ID_KEY, CLIENT_SECRET_KEY, REFRESH_TOKEN_KEY
    from cobalt.notify.email import AUTH_PORT_KEY, TIMEOUT_KEY, auth_port, timeout_s

    email_cfg = notify_cfg.email
    print(
        f"        email {'enabled' if email_cfg.enabled else 'DISABLED'}, "
        f"alerts -> {email_cfg.to}, subject prefix {email_cfg.subject_prefix!r}."
    )
    registry = load_tunables().by_key
    for key in (AUTH_PORT_KEY, TIMEOUT_KEY):
        row = registry.get(key)
        if row is None:
            print(
                f"FAILED: tunable {key!r} is missing — the email channel has no "
                "built-in defaults (F16)."
            )
            sys.exit(1)
        print(f"        tunable {key} = {row.value} {row.unit.value}, "
              f"consumers {row.consumers}")
    # Building both IS the check: a row present but unparseable as a port
    # or a timeout fails here rather than at 03:00 on a red beat.
    auth_port(), timeout_s()

    # The credential itself: present or absent, never printed. A host
    # that has never run `email-auth` is a host whose out-of-band alert
    # path does not work, and that is a config-gate fact, not a runtime
    # surprise.
    absent = [
        k for k in (CLIENT_ID_KEY, CLIENT_SECRET_KEY, REFRESH_TOKEN_KEY)
        if k not in set(guard.names) and not any(n.startswith(k) for n in guard.names)
    ] if guard.available else None
    if absent is None:
        print("        OAuth credential: UNVERIFIABLE (vault locked on this process).")
    elif absent:
        print(
            f"        OAuth credential: NOT STORED — vault is missing "
            f"{', '.join(absent)}. `cobalt notify email-auth` (one time, interactive). "
            "The F18 `email` probe reports this red."
        )
    else:
        print("        OAuth credential: all three vault keys present (values never read here).")

    registry = load_job_registry()
    print(
        f"Jobs (F17): {len(registry.jobs)} registered — "
        f"{sum(1 for j in registry.jobs if j.kind.value == 'resident')} resident, "
        f"{sum(1 for j in registry.jobs if j.kind.value == 'one-shot')} one-shot. "
        f"Kill phrase {registry.kill_phrase!r}."
    )

    # CROSS-CHECK 1: the registry and ops/ name the same jobs. A registry
    # that has drifted from launchd reports green for a job that is not
    # there any more; a plist with no row is a job nobody watches.
    from cobalt.jobs.config import OPS_DIR

    declared = set(registry.by_label)
    installed = {p.stem for p in OPS_DIR.glob("com.cobalt.*.plist")}
    if declared != installed:
        print(
            f"FAILED: configs/cobalt/jobs.yaml and ops/ disagree.\n"
            f"  registered with no plist: {sorted(declared - installed) or 'none'}\n"
            f"  installed with no row   : {sorted(installed - declared) or 'none'}"
        )
        sys.exit(1)
    print(f"  registry <-> ops/: {len(declared)} label(s), exact match.")

    # CROSS-CHECK 2: the schedules. launchd cannot read a tunables row or
    # a YAML file, so every plist mirrors its schedule — and a mirror
    # nobody compares is a mirror that drifts.
    for spec in registry.jobs:
        try:
            data = plistlib.loads(spec.plist_path.read_bytes())
        except Exception as e:
            print(f"FAILED: {spec.plist_path.name} is not readable as a plist: {e}")
            sys.exit(1)
        if data.get("EnvironmentVariables", {}).get("COBALT_ENV") != "production":
            print(f"FAILED: {spec.plist_path.name} does not declare COBALT_ENV=production (Charter §8.4).")
            sys.exit(1)
        if spec.schedule is None:
            continue
        if spec.schedule.at:
            intervals = data.get("StartCalendarInterval") or []
            hh, _, mm = spec.schedule.at.partition(":")
            drift = [
                e for e in intervals
                if e.get("Hour") != int(hh) or e.get("Minute") != int(mm)
            ]
            if drift or sorted(e.get("Weekday") for e in intervals) != sorted(spec.schedule.weekdays):
                print(
                    f"FAILED: {spec.label} — registry says {spec.schedule.describe()}, "
                    f"{spec.plist_path.name} says {intervals}."
                )
                sys.exit(1)
        else:
            minutes = spec.schedule.interval_minutes()
            plist_seconds = data.get("StartInterval")
            if plist_seconds != minutes * 60:
                print(
                    f"FAILED: {spec.label} — the tunable resolves to {minutes} min "
                    f"({minutes * 60} s) but {spec.plist_path.name} says "
                    f"StartInterval {plist_seconds}. Every 'red within one interval' "
                    "claim is measured against a number these two must agree on."
                )
                sys.exit(1)
    print("  registry <-> plists: schedules and COBALT_ENV agree on every job.")

    from cobalt.heartbeat.runner import green_summary_at, interval_min

    print(
        f"Heartbeat (F18): every {interval_min()} min, one green summary a day at "
        f"{green_summary_at():%H:%M} ET."
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
    db_cli.add_parser(sub)
    taxonomy_cli.add_parser(sub)
    jobs_cli.add_parser(sub)
    heartbeat_cli.add_parser(sub)
    backup_cli.add_parser(sub)
    notify_cli.add_parser(sub)
    jobs_cli.add_stop_parsers(sub)

    validate = sub.add_parser(
        "validate", help="Validate every config family (F16 sweep gate)."
    )
    validate.set_defaults(func=_cmd_validate)

    args = parser.parse_args()
    try:
        args.func(args)
    except JobStopped as e:
        # EXIT 0. A job turned away by the kill switch did not fail — an
        # operator stopped it on purpose, and a non-zero exit would paint
        # F18 red for a state he deliberately caused (F17d).
        print(f"NOT RUN — {e}")
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
