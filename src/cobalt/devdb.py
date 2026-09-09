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

Second guard, orthogonal to the first: only the tables RULING 7 and
RULING 9 migrate may be truncated. Every Mattermost and memory-layer
table is outside the allowlist and cannot be named.

    uv run python -m cobalt.devdb --list
    uv run python -m cobalt.devdb --truncate aset_sizings,vault_writes,vault_overrides,bars --yes-truncate-cobalt-dev
"""

import argparse
import sys
from pathlib import Path

from dotenv import load_dotenv

# The Postgres parts db.connect() composes its DSN from live in the repo
# .env. The prefill/aset entrypoints get them by ACCIDENT — a transitive
# old-tree import calls load_dotenv() somewhere down their chain. This
# module has no such chain, so it loads the same file deliberately and
# visibly, exactly as cobalt/cli.py does.
#
# BOTH credentials are loaded from that one file (2026-09-09):
# `COBALT_DB_*` is the application login every `db.connect()` below uses,
# and `POSTGRES_*` is the docker SUPERUSER — MIGRATIONS AND BOOTSTRAP
# ONLY, which for this module means creating `cobalt_dev` itself and
# running `cobalt db migrate` against it. The truncates below go through
# `db.connect()` and therefore run as `cobalt_app` + `SET ROLE`, under
# exactly the grants production has; a destructive helper that quietly
# had more power than the code it rehearses would prove nothing.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

from psycopg import sql  # noqa: E402

from cobalt import db, env  # noqa: E402
from cobalt.db_migrations.placement import side_of  # noqa: E402

# The ONLY tables this helper may empty. Everything else — the memory
# layer's five pillars, and (until 2026-09-04) Mattermost's tables —
# is out of reach by
# name, independent of the database guard.
#
# `bars` joined the list under RULING 9 (2026-09-04). It was excluded
# before *because it held production data*: 4.5M rows of live market
# history lived in `cobalt_dev` while the archiver named its own
# database. Now that RULING 9 has moved `bars` to `cobalt_brain`, the
# exclusion protects nothing and only pushes the truncate outside the
# one guarded path this module exists to be. The database guard is what
# makes this safe and it is unchanged: `cobalt_dev`, hard-coded, not
# overridable — a `bars` truncate aimed at `cobalt_brain` still refuses.
TRUNCATABLE_TABLES = ("aset_sizings", "vault_writes", "vault_overrides", "bars")

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


def _by_side(tables: list[str]) -> dict[db.Side, list[str]]:
    """Group the named tables by their ruled side (ADR-0008 D2).

    The allowlist straddles the split — `aset_sizings`, `vault_writes` and
    `vault_overrides` are user data, `bars` is engine data — and there is
    no role that can reach both. So this helper exists and both functions
    below hold ONE CONNECTION PER SIDE, exactly like a launchd job that
    touches both. Every statement then names its table schema-qualified,
    which for a destructive helper is worth the extra characters: a
    TRUNCATE should never depend on a search_path being what you assumed.
    """
    grouped: dict[db.Side, list[str]] = {}
    for table in tables:
        grouped.setdefault(side_of(table), []).append(table)
    return grouped


def counts(tables: list[str], *, db_name: str = env.DEV_DB_NAME) -> dict[str, int]:
    """Row counts for `tables`. Read-only, but guarded identically so a
    typo in the database name can never even be *inspected* against
    production by this tool."""
    env.assert_destructive_target(db_name)
    _check_tables(tables)
    out: dict[str, int] = {}
    for side, names in _by_side(tables).items():
        with db.connect(db_name, side=side) as conn:
            for table in names:
                row = conn.execute(
                    sql.SQL("SELECT count(*) FROM {}").format(
                        sql.Identifier(side.schema, table)
                    )
                ).fetchone()
                out[table] = int(row[0]) if row else 0
    return {t: out[t] for t in tables}


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
    for side, names in _by_side(tables).items():
        with db.connect(db_name, side=side) as conn:
            # RESTART IDENTITY resets the sequences too: after the migration
            # the ids of record live in cobalt_brain, and a dev row that
            # reuses one of them would be actively confusing in forensics.
            conn.execute(
                sql.SQL("TRUNCATE TABLE {} RESTART IDENTITY").format(
                    sql.SQL(", ").join(
                        sql.Identifier(side.schema, t) for t in names
                    )
                )
            )
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
