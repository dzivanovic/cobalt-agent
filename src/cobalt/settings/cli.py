"""`cobalt settings load | show` — the ONE write path for the trader's
own settings (ADR-0008 D3.4).

    cobalt settings load --from configs/cobalt   --dry-run | --apply
    cobalt settings load --from-git <commit>     --dry-run | --apply
    cobalt settings load --card     <file> [--sha256 <hash>] --dry-run | --apply
    cobalt settings load --optional <file> [--sha256 <hash>] --dry-run | --apply
    cobalt settings show

Every apply goes through `apply_settings` — the one write function the
ASET change line (DRC D4-4) calls too.

`--card` (S2-P2, `.card`) and `--optional` (S2-P4) each load their own
reviewed file — the card settings (`radar.cards_enabled`, `card.*`) and
the optional keys (`radar.benchmark`) — whose bytes must hash to
`--sha256` before anything parses. Neither combines with the other or
with `--from` / `--from-git`.

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
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import yaml
from loguru import logger

from cobalt.session import assert_writable

from .models import (
    ASET_FILENAME,
    DAYMODE_FILENAME,
    DRC_SETTING_KEYS,
    OPTIONAL_SETTING_KEYS,
    OPTIONAL_SETTING_MODELS,
    SETTING_KEYS,
    TraderSettings,
    TraderSettingsError,
)
from .store import TraderSettingsStore

REPO_ROOT = Path(__file__).resolve().parents[3]

TARGET = '"user".trader_settings'


def payload_sha256(rows: dict[str, Any]) -> str:
    """sha256 of a settings payload's canonical JSON — what the change
    line shows for review and what its Apply must carry back."""
    body = json.dumps(rows, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def apply_settings(
    rows: dict[str, Any],
    *,
    source: str,
    actor: str = "settings.load",
    store: TraderSettingsStore | None = None,
    delete: Iterable[str] = (),
) -> dict[str, str]:
    """THE ONE APPLY (L3 / L40, DRC D4-4). `cobalt settings load --apply`
    and the ASET change line both write `"user".trader_settings` through
    this function and nothing else.

    In order: refused inside `market_reset` (L66 — `assert_writable`
    raises `SessionBlocked` naming the window before anything is written);
    ONE `put` (one transaction: every key lands or none does); a
    round-trip read — the caller may only say "saved" once what the
    database returns equals the payload; one log line naming the keys,
    the payload hash and the time. NEVER the values: they are his user
    data (L32). The store's own trace is each row's `source` and
    `updated_at`.
    """
    assert_writable(actor, target=TARGET)
    store = store or TraderSettingsStore()
    delete = list(delete)
    digest = payload_sha256(rows)
    extra = {"delete": delete} if delete else {}
    outcome = store.put(rows, source=source, **extra)
    reloaded = store.values()
    drift = sorted(key for key in rows if reloaded.get(key) != rows[key])
    lingering = sorted(key for key in delete if key in reloaded)
    if drift or lingering:
        raise TraderSettingsError(
            f"FAILED: what {TARGET} now returns differs from what was applied — "
            f"differs: {drift or 'none'}; still present after delete: {lingering or 'none'}"
        )
    logger.info(
        "settings applied: keys {} · deleted {} · sha256 {} · source {} · at {}",
        sorted(rows), delete, digest, source,
        datetime.now(timezone.utc).isoformat(timespec="seconds"),
    )
    return outcome


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


OPTIONAL_FILE_ROOT = "optional_settings"


def load_optional_file(path: Path, *, sha256: str | None, require_hash: bool) -> dict:
    """Read, hash-verify and validate an optional-settings file (S2-P4
    R5, Astra R1-14). Returns `{key: jsonable value}`.

    THE HASH IS OF THE FILE'S BYTES and is checked BEFORE anything
    parses: the file he reviewed is the file that loads, byte for byte.
    Only keys in `OPTIONAL_SETTING_KEYS` are accepted; a required sheet
    key submitted here is refused by name, because two load paths for one
    row is the one-path rule's failure.

        optional_settings:
          radar.benchmark: {top_n: 20, min_move_pct: 10}
    """
    try:
        payload = Path(path).read_bytes()
    except OSError as e:
        raise TraderSettingsError(f"{path}: cannot read optional-settings file: {e}") from e
    digest = hashlib.sha256(payload).hexdigest()
    if sha256 is None:
        if require_hash:
            raise TraderSettingsError(
                f"{path}: --apply needs --sha256 of the reviewed file (this file hashes "
                f"to {digest}). A trader-run apply names the exact bytes it loads."
            )
    elif sha256.strip().lower() != digest:
        raise TraderSettingsError(
            f"{path}: sha256 mismatch — reviewed {sha256.strip().lower()}, file is "
            f"{digest}. Nothing loaded."
        )
    try:
        raw = yaml.safe_load(payload.decode("utf-8"))
    except (UnicodeDecodeError, yaml.YAMLError) as e:
        raise TraderSettingsError(f"{path}: not valid YAML: {e}") from e
    if not isinstance(raw, dict) or set(raw) != {OPTIONAL_FILE_ROOT}:
        raise TraderSettingsError(
            f"{path}: expected exactly one top-level mapping {OPTIONAL_FILE_ROOT!r}"
        )
    body = raw[OPTIONAL_FILE_ROOT]
    if not isinstance(body, dict) or not body:
        raise TraderSettingsError(f"{path}: {OPTIONAL_FILE_ROOT} must be a non-empty mapping")
    rows: dict = {}
    for key, value in body.items():
        if key in SETTING_KEYS:
            raise TraderSettingsError(
                f"{path}: {key!r} is a required sheet/day-mode setting — it loads through "
                "--from/--from-git only"
            )
        model = OPTIONAL_SETTING_MODELS.get(key)
        if model is None:
            raise TraderSettingsError(
                f"{path}: unknown optional setting {key!r}; accepted: "
                f"{list(OPTIONAL_SETTING_KEYS)}"
            )
        rows[key] = model.from_rows({key: value}).row()
    return rows


def cmd_load_optional(args: argparse.Namespace) -> None:
    dry_run = _require_mode(args)
    try:
        rows = load_optional_file(
            Path(args.optional), sha256=args.sha256, require_hash=not dry_run
        )
    except TraderSettingsError as e:
        raise SystemExit(f"FAILED: {e}") from e

    store = TraderSettingsStore()
    current = store.values()
    source_label = f"optional:{Path(args.optional).name}"
    print(f"cobalt settings load — {'DRY RUN' if dry_run else 'APPLY'} from {source_label}\n")
    changed = [key for key in rows if current.get(key) != rows[key]]
    for key in rows:
        old = current.get(key)
        if key not in changed:
            print(f"  = {key}")
            continue
        print(f"  {'+' if old is None else '~'} {key}")
        print(f"      db  : {json.dumps(old, sort_keys=True) if old is not None else '(absent)'}")
        print(f"      file: {json.dumps(rows[key], sort_keys=True)}")
    if not changed:
        print("\nno differences — the database already holds these settings.")
        return
    if dry_run:
        print(f"\nDRY RUN — {len(changed)} setting(s) would change. Nothing written.")
        return

    try:
        outcome = apply_settings(
            {key: rows[key] for key in changed}, source=source_label, store=store
        )
    except TraderSettingsError as e:
        raise SystemExit(str(e)) from e
    print(f"\napplied: {outcome} (sha256 {args.sha256})")
    reloaded = store.values()
    for key in rows:
        OPTIONAL_SETTING_MODELS[key].from_rows(reloaded)
    print("round trip: database == file, every optional key re-validates.")


def cmd_load(args: argparse.Namespace) -> None:
    if getattr(args, "card", None):
        if args.from_dir or args.from_git or getattr(args, "optional", None):
            raise SystemExit(
                "cobalt settings load: --card loads the card-settings file only; "
                "it does not combine with --from / --from-git / --optional."
            )
        from .card import cmd_load_card

        cmd_load_card(args)
        return
    if getattr(args, "optional", None):
        if args.from_dir or args.from_git:
            raise SystemExit(
                "cobalt settings load: --optional loads the optional-settings file only; "
                "it does not combine with --from / --from-git."
            )
        cmd_load_optional(args)
        return
    if getattr(args, "sha256", None):
        raise SystemExit(
            "cobalt settings load: --sha256 verifies a --card or an --optional file only."
        )
    dry_run = _require_mode(args)
    if bool(args.from_dir) == bool(args.from_git):
        raise SystemExit(
            "cobalt settings load: pass exactly one of --from <dir>, "
            "--from-git <commit>, --card <file> or --optional <file>."
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

    try:
        outcome = apply_settings(rows, source=source_label, store=store)
    except TraderSettingsError as e:
        raise SystemExit(str(e)) from e
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
    # DRC D4-5: the dry-run of the DRC family. Every key is OPTIONAL, so an
    # absent one is printed as `not given` — never a default (L1).
    values = {row["key"]: row["value"] for row in rows}
    print("\nDRC keys (optional; absent = not given):")
    for key in DRC_SETTING_KEYS:
        shown = json.dumps(values[key], sort_keys=True) if key in values else "not given"
        print(f"  {key:<36} {shown}")


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
    load.add_argument(
        "--card",
        metavar="FILE",
        help="The reviewed card-settings file (radar.cards_enabled, card.*; S2-P2).",
    )
    load.add_argument(
        "--optional",
        metavar="FILE",
        help="The reviewed optional-settings file (radar.benchmark; S2-P4; the DRC keys, D4).",
    )
    load.add_argument(
        "--sha256",
        metavar="HASH",
        help="sha256 of the reviewed --card / --optional file's bytes; required with --apply.",
    )
    load.add_argument("--dry-run", action="store_true")
    load.add_argument("--apply", action="store_true")
    load.set_defaults(func=cmd_load)

    show = gsub.add_parser("show", help="Print every setting, its source and its date.")
    show.set_defaults(func=cmd_show)


__all__ = ["add_parser", "apply_settings", "cmd_load", "cmd_show", "payload_sha256"]
