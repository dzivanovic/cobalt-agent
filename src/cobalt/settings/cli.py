"""`cobalt settings load | show` — the ONE write path for the trader's
own settings (ADR-0008 D3.4).

    cobalt settings load --from configs/cobalt   --dry-run | --apply
    cobalt settings load --from-git <commit>     --dry-run | --apply
    cobalt settings show

`--from` reads the two YAML files out of a directory. `--from-git` reads
the same two files at a revision — which is how a LIVE seed works after
they have left the working tree, exactly as the taxonomy migration reads
its own deleted inputs. Both print a per-setting diff against what the
database already holds, and `--dry-run` writes nothing.

MARKET-RESET GATED, like every other write. Re-typing a sheet dollar is
a trading-logic change; 20:00-21:00 ET is the one hour when the day is
being closed out and nothing may move underneath it. `--dry-run` is not
gated: seeing what WOULD change during the window is exactly when you
want to.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from cobalt.session import assert_writable

from .models import (
    ASET_FILENAME,
    DAYMODE_FILENAME,
    SETTING_KEYS,
    TraderSettings,
    TraderSettingsError,
)
from .store import TraderSettingsStore

REPO_ROOT = Path(__file__).resolve().parents[3]


def _require_mode(args: argparse.Namespace) -> bool:
    if bool(args.dry_run) == bool(args.apply):
        raise SystemExit(
            "cobalt settings load: pass exactly one of --dry-run or --apply. "
            "There is no default: one of them changes what every card is sized on."
        )
    return bool(args.dry_run)


def _texts_from_git(commit: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for name in (ASET_FILENAME, DAYMODE_FILENAME):
        path = f"configs/cobalt/{name}"
        proc = subprocess.run(
            ["git", "show", f"{commit}:{path}"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=False,
        )
        if proc.returncode != 0:
            raise SystemExit(
                f"could not read {path} at {commit}: "
                f"{(proc.stderr or '').strip().splitlines()[-1:] or ['unknown error']}"
            )
        out[name] = proc.stdout
    return out


def cmd_load(args: argparse.Namespace) -> None:
    dry_run = _require_mode(args)
    if bool(args.from_dir) == bool(args.from_git):
        raise SystemExit(
            "cobalt settings load: pass exactly one of --from <dir> or "
            "--from-git <commit>."
        )

    if args.from_git:
        source_label = f"git:{args.from_git}"
        rows = TraderSettings.rows_from_yaml(texts=_texts_from_git(args.from_git))
    else:
        source_label = f"yaml:{args.from_dir}"
        rows = TraderSettings.rows_from_yaml(Path(args.from_dir))

    incoming = TraderSettings.from_yaml(
        texts=_texts_from_git(args.from_git) if args.from_git else None,
        directory=None if args.from_git else Path(args.from_dir),
    )

    store = TraderSettingsStore()
    store.ensure_schema()
    current = store.values()

    print(f"cobalt settings load — {'DRY RUN' if dry_run else 'APPLY'} from {source_label}\n")
    changed = 0
    for key in SETTING_KEYS:
        new = rows[key]
        old = current.get(key)
        if old == new:
            print(f"  = {key}")
            continue
        changed += 1
        print(f"  {'+' if old is None else '~'} {key}")
        print(f"      db  : {json.dumps(old, sort_keys=True) if old is not None else '(absent)'}")
        print(f"      file: {json.dumps(new, sort_keys=True)}")

    if not changed:
        print("\nno differences — the database already holds these settings.")
        return

    if dry_run:
        print(f"\nDRY RUN — {changed} setting(s) would change. Nothing written.")
        return

    assert_writable("settings.load", target='"user".trader_settings')
    outcome = store.put(rows, source=source_label)
    print(f"\napplied: {outcome}")
    # Prove the round trip before claiming success: what the runtime will
    # read must equal what the seed said.
    reloaded = TraderSettings.from_db(store)
    diff = reloaded.diff(incoming)
    if diff:
        raise SystemExit(
            f"FAILED: what the database now returns differs from the seed: "
            f"{sorted(diff)}"
        )
    print("from_db() == from_yaml() — field-by-field diff EMPTY.")


def cmd_show(args: argparse.Namespace) -> None:
    store = TraderSettingsStore()
    rows = store.rows()
    if not rows:
        raise SystemExit(
            'no rows in "user".trader_settings — run `cobalt settings load`.'
        )
    for row in rows:
        print(
            f"{row['key']:<32} {row['source']:<28} "
            f"{row['updated_at']:%Y-%m-%d %H:%M:%S}"
        )
        print(f"    {json.dumps(row['value'], sort_keys=True)}")
    try:
        settings = TraderSettings.from_db(store)
    except TraderSettingsError as e:
        raise SystemExit(f"FAILED: {e}") from e
    print(
        f"\nresolved: sheets {' < '.join(settings.sheet_modes.order)}; "
        f"account grades {[g.value for g in settings.sheet_modes.enabled_grades]}; "
        f"ladder {' < '.join(settings.daymode.modes)}; "
        f"enabled {settings.daymode.enabled_modes}."
    )


def add_parser(sub) -> None:
    group = sub.add_parser(
        "settings", help="The trader's own settings (ADR-0008 D3.4)"
    )
    gsub = group.add_subparsers(dest="command", required=True)

    load = gsub.add_parser("load", help="Seed/refresh the settings from YAML.")
    load.add_argument("--from", dest="from_dir", help="Directory holding the two YAMLs.")
    load.add_argument(
        "--from-git",
        dest="from_git",
        metavar="COMMIT",
        help="Read both YAMLs at this revision (they have left the working tree).",
    )
    load.add_argument("--dry-run", action="store_true")
    load.add_argument("--apply", action="store_true")
    load.set_defaults(func=cmd_load)

    show = gsub.add_parser("show", help="Print every setting, its source and its date.")
    show.set_defaults(func=cmd_show)


__all__ = ["add_parser", "cmd_load", "cmd_show"]
