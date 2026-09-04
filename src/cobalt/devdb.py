"""Guarded destructive helper — `cobalt_dev` and nothing else (RULING 7.1c).

Every truncate/drop/reset in this codebase goes through here, and this
module refuses any database but `cobalt_dev`. The refusal is
hard-coded in `cobalt.env.assert_destructive_target()`: not read from a
config file, not keyed on `COBALT_ENV`, not overridable by an env var
or a CLI flag. A destructive helper invoked by accident from inside a
production shell — the shell where `COBALT_ENV=production` and every
other guard has already stood aside — must still refuse.

That is the whole point. `COBALT_ENV` decides where the *application*
reads and writes; it must never be able to decide where a truncate
lands, because the failure mode of getting that wrong is unbounded and
`cobalt_brain` now holds the live trading record.

Second guard, orthogonal to the first: only the three tables RULING 7
migrates may be truncated. `bars` (4.5M rows) and every Mattermost and
memory-layer table are outside the allowlist and cannot be named.

    uv run python -m cobalt.devdb --list
    uv run python -m cobalt.devdb --truncate aset_sizings,vault_writes,vault_overrides --yes-truncate-cobalt-dev
"""

import argparse
import sys

from cobalt import db, env

# The ONLY tables this helper may empty. Everything else — `bars`, the
# memory layer's five pillars, Mattermost's 116 tables — is out of reach
# by name, independent of the database guard.
TRUNCATABLE_TABLES = ("aset_sizings", "vault_writes", "vault_overrides")

CONFIRM_FLAG = "--yes-truncate-cobalt-dev"


class DestructiveRefused(RuntimeError):
    """A destructive request failed a guard — nothing was executed."""


def _check_tables(tables: list[str]) -> None:
    unknown = [t for t in tables if t not in TRUNCATABLE_TABLES]
    if unknown:
        raise DestructiveRefused(
            f"REFUSED: {', '.join(unknown)} is not in the truncate allowlist "
            f"({', '.join(TRUNCATABLE_TABLES)}). RULING 7.1c."
        )
    if not tables:
        raise DestructiveRefused("REFUSED: no tables named.")


def counts(tables: list[str], *, db_name: str = env.DEV_DB_NAME) -> dict[str, int]:
    """Row counts for `tables`. Read-only, but guarded identically so a
    typo in the database name can never even be *inspected* against
    production by this tool."""
    env.assert_destructive_target(db_name)
    _check_tables(tables)
    out: dict[str, int] = {}
    with db.connect(db_name) as conn:
        for table in tables:
            row = conn.execute(f"SELECT count(*) FROM {table}").fetchone()
            out[table] = int(row[0]) if row else 0
    return out


def truncate(
    tables: list[str],
    *,
    db_name: str = env.DEV_DB_NAME,
    confirm: bool = False,
) -> dict[str, tuple[int, int]]:
    """TRUNCATE `tables` in `cobalt_dev`. Returns {table: (before, after)}.

    Three guards, all of which must pass: the database is `cobalt_dev`,
    every table is on the allowlist, and `confirm` is explicitly True.
    """
    env.assert_destructive_target(db_name)
    _check_tables(tables)
    if not confirm:
        raise DestructiveRefused(
            f"REFUSED: destructive call without explicit confirmation "
            f"(confirm=True / {CONFIRM_FLAG})."
        )

    before = counts(tables, db_name=db_name)
    with db.connect(db_name) as conn:
        # RESTART IDENTITY resets the sequences too: after the migration
        # the ids of record live in cobalt_brain, and a dev row that
        # reuses one of them would be actively confusing in forensics.
        conn.execute(f"TRUNCATE TABLE {', '.join(tables)} RESTART IDENTITY")
    after = counts(tables, db_name=db_name)
    return {t: (before[t], after[t]) for t in tables}


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="cobalt.devdb",
        description="Guarded destructive helper — cobalt_dev only (RULING 7.1c).",
    )
    parser.add_argument("--list", action="store_true", help="Show row counts and exit.")
    parser.add_argument("--truncate", help="Comma-separated tables to TRUNCATE.")
    parser.add_argument(
        CONFIRM_FLAG, dest="confirm", action="store_true",
        help="Required for --truncate. There is no --force for another database.",
    )
    args = parser.parse_args()

    try:
        if args.list:
            for table, n in counts(list(TRUNCATABLE_TABLES)).items():
                print(f"{table:<18} {n}")
            return
        if args.truncate:
            tables = [t.strip() for t in args.truncate.split(",") if t.strip()]
            for table, (before, after) in truncate(tables, confirm=args.confirm).items():
                print(f"{table:<18} {before} -> {after}")
            return
        parser.print_help()
    except (DestructiveRefused, env.EnvConfigError) as e:
        print(f"FAILED: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
