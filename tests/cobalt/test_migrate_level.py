"""`cobalt db migrate --proof-only`'s two level lines (card 2026-10-03/03 adoption-scripts, row L1).

TABLES is computed from `placement.CREATED_TABLES` and the present/absent
marks the proof already takes: `<nnnn>` is the highest table-creating
migration whose tables are all present, with every lower creator's tables
present and every higher one's absent; anything else is `MIXED`. The
migration that creates a table is the one forward file whose
`CREATE TABLE IF NOT EXISTS <schema>.<table> (` names it.

FINGERPRINT is the three reads of BUILD-HUB.md THE LOCK's `<FP>` query,
byte for byte the same SQL, inside the proof-only's own READ ONLY
transaction. Both lines print facts only: no `LEVEL` word, no `0013`.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

import pytest

from cobalt import env
from cobalt.db import Side
from cobalt.db_migrations import cli
from cobalt.db_migrations.placement import CREATED_TABLES

REPO_ROOT = Path(__file__).resolve().parents[2]
HUB = REPO_ROOT / "docs" / "40 - DevDocs" / "prompts" / "BUILD-HUB.md"
FP_PREFIX = '`COBALT_ENV=dev uv run cobalt db query --side user "SELECT (SELECT'

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

#: A constructed map: creators 0004, 0007, 0011, 0016, 0017 (two tables on 0004 and 0016).
CREATORS = {
    "t_a1": "0004", "t_a2": "0004", "t_b1": "0007", "t_c1": "0011",
    "t_d1": "0016", "t_d2": "0016", "t_e1": "0017",
}


def marks(*present: str) -> dict[str, bool]:
    """Every table of the named creators present, every other absent."""
    return {table: creator in present for table, creator in CREATORS.items()}


# ---- TABLES on a constructed map ---------------------------------------------------------


def test_0011_and_below_present_0016_absent_is_tables_0011():
    assert cli._tables_line(CREATORS, marks("0004", "0007", "0011")) == "TABLES 0011"


def test_0016_present_too_is_tables_0016():
    assert cli._tables_line(CREATORS, marks("0004", "0007", "0011", "0016")) == "TABLES 0016"


def test_0017_present_without_0016_is_mixed_naming_both():
    line = cli._tables_line(CREATORS, marks("0004", "0007", "0011", "0017"))
    assert line == "TABLES MIXED — present above: 0017 · absent below: 0016"


def test_one_table_of_a_creator_absent_is_mixed_naming_that_creator():
    m = marks("0004", "0007", "0011", "0016")
    m["t_d2"] = False
    assert cli._tables_line(CREATORS, m) == "TABLES MIXED — present above: 0016 · absent below: 0016"


def test_a_lower_creator_absent_under_a_present_one_is_mixed():
    line = cli._tables_line(CREATORS, marks("0004", "0011"))
    assert line == "TABLES MIXED — present above: 0011 · absent below: 0007"


def test_no_creator_present_is_tables_none():
    assert cli._tables_line(CREATORS, marks()) == "TABLES none"


# ---- the creators, read from the forward files ---------------------------------------------


def test_every_created_table_has_exactly_one_creating_migration():
    creators = cli._table_creators()
    assert set(creators) == set(CREATED_TABLES)
    assert creators["radar_pool"] == "0004"
    assert creators["archive_incidents"] == "0011"
    assert creators["drc_imports"] == "0016"
    assert creators["prediction_records"] == "0022"


def test_the_highest_creator_at_or_below_0013_is_0011():
    """gate-lists.md `## LEVEL 0013` carries `TABLES 0011` (card L2: re-read from placement.py)."""
    assert max(m for m in cli._table_creators().values() if m <= "0013") == "0011"


def test_a_created_table_no_forward_file_creates_is_refused(monkeypatch):
    monkeypatch.setattr(cli, "CREATED_TABLES", {**CREATED_TABLES, "no_such_table": Side.USER})
    with pytest.raises(cli.MigrationError, match="no_such_table"):
        cli._table_creators()


# ---- FINGERPRINT: the hub's SQL, in the proof-only transaction ---------------------------------


def hub_fp_sql() -> str:
    (line,) = [ln for ln in HUB.read_text().splitlines() if ln.startswith(FP_PREFIX)]
    command = line.strip("`")
    head = 'COBALT_ENV=dev uv run cobalt db query --side user "'
    assert command.startswith(head) and command.endswith('"')
    return command[len(head):-1]


def test_the_fingerprint_sql_is_the_hubs_byte_for_byte():
    assert cli.FINGERPRINT_SQL == hub_fp_sql()


def test_src_prints_no_level_word_and_no_0013():
    text = Path(cli.__file__).read_text()
    assert "LEVEL" not in text
    assert "0013" not in text


class _Cursor:
    def __init__(self, row):
        self._row = row

    def fetchone(self):
        return self._row


class _Conn:
    """The proof-only connection: records statements and the order of the rollback."""

    def __init__(self):
        self.events: list[str] = []

    def execute(self, query, *args, **kwargs):
        self.events.append(str(query))
        return _Cursor((664, 35, "0123456789abcdef0123456789abcdef"))

    def rollback(self):
        self.events.append("ROLLBACK")

    def close(self):
        self.events.append("CLOSE")


def test_proof_only_ends_with_the_fingerprint_then_the_tables_line(monkeypatch, capsys):
    conn = _Conn()
    creators = cli._table_creators()
    monkeypatch.setenv(env.ENV_VAR, env.DEV)
    monkeypatch.setattr(cli, "_connect", lambda *a, **k: conn)
    monkeypatch.setattr(cli, "_probe_all", lambda c: {
        t: {"schema": "system" if creators[t] <= "0011" else None} for t in CREATED_TABLES
    })
    monkeypatch.setattr(cli, "_slot_lines", lambda conn: [])
    monkeypatch.setattr(cli, "_print_probe", lambda *a, **k: print("<proof table>"))
    monkeypatch.setattr(cli, "_code_line", lambda: "code: constructed")
    cli.cmd_migrate(argparse.Namespace(
        proof_only=True, rollback=False, down_to=None, allow_prod=False,
        lock_timeout_s=cli.DEFAULT_LOCK_TIMEOUT_S,
    ))
    lines = [ln for ln in capsys.readouterr().out.splitlines() if ln.strip()]
    assert lines[-3:] == [
        "code: constructed",
        "FINGERPRINT cols 664 · rels 35 · views_md5 0123456789abcdef0123456789abcdef",
        "TABLES 0011",
    ]
    # the hub's <FP> runs --side user: the same search_path first, then the same SQL, then the
    # rollback — pg_views.definition is rendered relative to the search_path (W, 2026-10-03)
    assert "SET LOCAL search_path TO " in conn.events[0] and "Identifier('user')" in conn.events[0]
    assert conn.events[1:] == [cli.FINGERPRINT_SQL, "ROLLBACK", "CLOSE"]


# ---- with-DB, at 0013: the two lines, and the hub's own query in the same take -------------------


def _cobalt(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "cobalt.cli", *args], cwd=REPO_ROOT,
        env={**os.environ, env.ENV_VAR: env.DEV}, capture_output=True, text=True,
        timeout=600, check=False,
    )


@requires_db
def test_with_db_the_two_lines_match_the_hubs_fingerprint_query():
    proof = _cobalt("db", "migrate", "--proof-only")
    assert proof.returncode == 0, proof.stdout + proof.stderr
    lines = proof.stdout.splitlines()
    (tables,) = [ln for ln in lines if ln.startswith("TABLES ")]
    (fingerprint,) = [ln for ln in lines if ln.startswith("FINGERPRINT ")]
    query = _cobalt("db", "query", "--side", "user", hub_fp_sql())
    assert query.returncode == 0, query.stdout + query.stderr
    rows = query.stdout.splitlines()
    header = rows.index("cols\trels\tviews_md5")
    cols, rels, views_md5 = rows[header + 1].split("\t")
    print(tables)
    print(fingerprint)
    print(f"<FP>: cols {cols} · rels {rels} · views_md5 {views_md5}")
    assert fingerprint == f"FINGERPRINT cols {cols} · rels {rels} · views_md5 {views_md5}"
    assert tables == "TABLES " + max(m for m in cli._table_creators().values() if m <= "0013")
