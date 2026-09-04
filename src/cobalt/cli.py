"""`cobalt` — the new core's top-level CLI.

Today it carries one command group, `vault`, whose job is the LAW L28
rollback path:

    cobalt vault restore --write-id N [--dry-run]
    cobalt vault writes [--limit N]
    cobalt vault overrides --note PATH

`restore` puts a section back to the before-state recorded in
`vault_writes` id N, and it does so THROUGH THE SAME WRITER — same
markers, same mtime/hash guard, same atomic rename, and its own audit
row. There is no second write path, not even for undo.
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

    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
