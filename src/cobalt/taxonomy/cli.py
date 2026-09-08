"""`cobalt taxonomy load [--dry-run]` — vault -> `"user".trade_defs`.

The one command that moves a trader's strategy notes into the database.
It reads the vault (`taxonomy/vault_loader`), prints exactly what
`cobalt validate` prints — defs, drafts, warnings — and then either stops
(`--dry-run`) or syncs and prints what changed.

`--dry-run` FIRST, ALWAYS, IN THE OPERATOR'S HEAD. `sync()` is a replace:
a slug that has left the vault has its row deleted (and its per-trade
tunables with it, by cascade). That is the correct semantics — a def
removed from a note is a def gone from the system — but it is not a
semantics anyone should discover from a row count afterwards. The dry run
shows which defs the vault currently produces; the apply names every slug
it deleted.
"""

from __future__ import annotations

import argparse

from .store import TradeDefStore
from .validate import print_result
from .vault_loader import load_vault_trade_defs


def cmd_load(args: argparse.Namespace) -> None:
    result = load_vault_trade_defs()
    print_result(result)

    if args.dry_run:
        print(
            f"\nDRY RUN — nothing written. {len(result.defs)} def(s) and "
            f"{len(result.user_tunables)} tunable row(s) would be synced into "
            '"user".trade_defs / "user".tunables. Re-run without --dry-run to apply.'
        )
        return

    store = TradeDefStore()
    store.ensure_schema()
    before = set(store.slugs())
    counts = store.sync(result)
    print("\nsynced:")
    print(counts.report())
    added = sorted({d.slug for d in result.defs} - before)
    if added:
        print(f"  new slugs: {added}")
    print(f"  setup_trade_matrix now has {len(store.matrix())} row(s).")


def add_parser(sub) -> None:
    group = sub.add_parser(
        "taxonomy", help="Trade definitions, read from the vault (ADR-0008 D3)"
    )
    gsub = group.add_subparsers(dest="command", required=True)

    load = gsub.add_parser(
        "load",
        help='Load every strategy note into "user".trade_defs / "user".tunables.',
    )
    load.add_argument(
        "--dry-run",
        action="store_true",
        help="Read and report; write nothing.",
    )
    load.set_defaults(func=cmd_load)


__all__ = ["add_parser", "cmd_load"]
