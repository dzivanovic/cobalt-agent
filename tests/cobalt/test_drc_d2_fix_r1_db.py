"""DRC D2 fix r1 — WITH-DB half (`prompts/2026-09-28/08-drc-d2-fix-r1-build.md`
`## F3`): S-1 THE EVENT HOME (`docs/30 - Design/DRC-D2-SEAM-2026-09-25.md`
§1 tests 1–8 and 12), S-2 THE SCREENSHOT WRITER (§2 tests 1–3) and F-1's
with-DB half (`drc-d2-check-2026-09-25.md:138`, `:174`).

The harness is reused BY IMPORT, never copied: `test_drc_store.py`'s
`migrated` / `weekday_calendar` / `requires_db`, `test_drc_k1_store.py`'s
`_state` / `TEN_ET` / `_cli`, `test_drc_imports_db.py`'s `lane` / `_drop`,
`test_drc_k2_experiments.py`'s constructed days. Everything runs inside
`test_drc_store.py`'s never-committed migration transaction on `cobalt_dev`
(L76): `0019` is applied only there. Constructed 2001 dates and symbols
only (L32 / L45); every vault write lands in the lane's `tmp_path` vault.
"""

from __future__ import annotations

import hashlib
import re
import sys
import types
import warnings
from pathlib import Path

import psycopg
import pytest

from cobalt.db import Side
from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.cli import _apply, _rollback_paths
from cobalt.db_migrations.placement import CREATED_TABLES, side_of
from cobalt.drc.store import DrcStore

from test_drc_imports_db import _drop, lane  # noqa: F401 — fixtures are used by name
from test_drc_k1_store import D3, RESET_ET, TEN_ET, _cli, _printed_hash, _raises, _state, at_ten, blocks  # noqa: F401
from test_drc_k2_experiments import D_FLAT, EEE_ROUND, _snapshot
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    DAY1,
    STATS,
    migrated,
    requires_db,
    weekday_calendar,
)

SQL = MIGRATIONS_DIR / "0019_drc_events.sql"
ROLLBACK = MIGRATIONS_DIR / "0019_drc_events.rollback.sql"
NOTE_PATH = "constructed/DRC-note.md"
PNG = b"\x89PNG\r\n\x1a\n" + b"\x00" * 16
DRC = "1 - Trading/5 - Review/_imports/drc"
EVENT_COLUMNS = "source, import_id, stated_book_id, state, error, note_path"
#: K2's own refusal for a no-trade day whose prior is not computed (`store.py` `_carried`).
NOT_COMPUTED_PRIOR = (
    f"{D_NEXT}: the prior trading day {D} has pairing not computed — its open positions are unknown; "
    "never assumed flat"
)


def _stub_build(monkeypatch, run):
    """D3's ONE entry as a stub (E11's shape, `test_drc_d2_experiments.py`)."""
    module = types.ModuleType("cobalt.drc.build")
    module.run_drc_build = run
    monkeypatch.setitem(sys.modules, "cobalt.drc.build", module)


def _raise_build(event):
    raise RuntimeError("constructed kill after pending")


def _events(conn, day):
    return conn.execute(
        f'SELECT {EVENT_COLUMNS} FROM "user".drc_events WHERE day = %s ORDER BY id', (day,)
    ).fetchall()


def _event_count(conn) -> int:
    return conn.execute('SELECT count(*) FROM "user".drc_events').fetchone()[0]


def _no_trade_ids(conn, day):
    return [r[0] for r in conn.execute(
        """SELECT id FROM "user".drc_stated_books WHERE day = %s AND kind = 'no_trade' ORDER BY id""", (day,)
    ).fetchall()]


def _recorded_prior():
    """D stated flat and recorded (DDD 30 left open): a chain D_NEXT joins."""
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())


def _columns(conn, table: str) -> list[str]:
    """Every live column of `table`, from `pg_attribute` (L35: unscoped)."""
    return [r[0] for r in conn.execute(
        "SELECT attname FROM pg_attribute WHERE attrelid = %s::regclass AND attnum > 0 "
        "AND NOT attisdropped ORDER BY attnum",
        (f'"user".{table}',),
    ).fetchall()]


def _checks(conn, table: str) -> set[str]:
    return {r[0] for r in conn.execute(
        "SELECT pg_get_constraintdef(oid) FROM pg_constraint WHERE conrelid = %s::regclass AND contype = 'c'",
        (f'"user".{table}',),
    ).fetchall()}


def _check_rows(conn, table: str) -> list[tuple[str, str]]:
    """D2 fix r2 F-5: EVERY CHECK on `table` — `(conname,
    pg_get_constraintdef)`, a list (duplicates kept), compared whole."""
    return conn.execute(
        "SELECT conname, pg_get_constraintdef(oid) FROM pg_constraint "
        "WHERE conrelid = %s::regclass AND contype = 'c' ORDER BY conname",
        (f'"user".{table}',),
    ).fetchall()


def _to_0018(conn) -> None:
    """D2 fix r2 F-5: the tree forwarded to `0018` WITHOUT `0019`, inside the
    transaction — down to `0015`, then `0016`, `0017`, `0018` in order."""
    _apply(conn, _rollback_paths("0015"))
    _apply(conn, [p for p in FORWARD if p.name[:4] in ("0016", "0017", "0018")])


def _hashes_of(conn, statement: int, day) -> tuple[str, str]:
    """D2 fix r2 F-6: the statement's stored `book_sha256` and `day`'s stored
    `seed` row's `inputs.from_book_sha256`, read by id / day."""
    ((book,),) = conn.execute(
        'SELECT book_sha256 FROM "user".drc_stated_books WHERE id = %s', (statement,)
    ).fetchall()
    ((inputs,),) = conn.execute(
        """SELECT inputs FROM "user".drc_rows WHERE day = %s AND kind = 'seed'""", (day,)
    ).fetchall()
    return book, inputs["from_book_sha256"]


def _event_source_assertions(event, statement: int) -> None:
    """The `returns` branch's OLD assertions (the source and the kind)."""
    assert event.stated_book_id == statement and event.import_id is None
    assert event.kind == "no_trade" and event.seed_from_day == D


def _stored_hash_assertions(event, conn, statement: int) -> None:
    """The `returns` branch's NEW assertions (D2 fix r2 F-6): the event's
    two hashes against the stored rows."""
    book_sha256, seed_sha256 = _hashes_of(conn, statement, D_NEXT)
    assert event.stated_book_sha256 == book_sha256
    assert event.seed_from_book_sha256 == seed_sha256 and seed_sha256 is not None


# ---------------------------------------------------------------------
# §1 test 12 — the registry, the placement map, the SQL (offline)
# ---------------------------------------------------------------------


def test_s1_12_the_pair_is_registered_last_and_first_and_placed_user_side():
    """§1 test 12 (`DRC-D2-SEAM-2026-09-25.md:161`, `:180`; R64 (5)): `0019`
    is `FORWARD[-1]`, its rollback `REVERSE[0]`, `drc_events` USER side,
    `store.TABLES` names it."""
    from cobalt.drc import store

    assert SQL.exists() and ROLLBACK.exists()
    # DRC D3 (`0020_drc_build_kinds`) and S3 exits C1 (`0021_legs`) now follow it: 0019 is third-last.
    assert FORWARD[-3] == SQL and FORWARD[-4].name == "0018_drc_stated_books.sql"
    assert REVERSE[2] == ROLLBACK and REVERSE[3].name == "0018_drc_stated_books.rollback.sql"
    assert side_of("drc_events") is Side.USER and CREATED_TABLES["drc_events"] is Side.USER
    assert "drc_events" in store.TABLES


def test_s1_12_the_sql_is_the_seams_sketch_and_the_rollback_states_its_cost():
    code = "\n".join(l for l in SQL.read_text().splitlines() if not l.strip().startswith("--"))
    assert re.findall(r'CREATE TABLE IF NOT EXISTS "user"\.(\w+)', code) == ["drc_events"]
    assert 'ALTER TABLE "user".drc_events OWNER TO cobalt_user;' in code
    assert "CREATE INDEX IF NOT EXISTS drc_events_day" in code
    for column in ("event_state", "event_updated_at", "event_error"):
        assert f"DROP COLUMN IF EXISTS {column}" in code
    back = ROLLBACK.read_text()
    assert "-- COST:" in back and 'DROP TABLE IF EXISTS "user".drc_events;' in back
    assert "to_regclass('\"user\".drc_imports')" in back
    assert [p.name for p in _rollback_paths("0018")] == [
        "0021_legs.rollback.sql", "0020_drc_build_kinds.rollback.sql", "0019_drc_events.rollback.sql"]


# ---------------------------------------------------------------------
# §1 test 12 — with-DB: tenancy and the round trip
# ---------------------------------------------------------------------


@requires_db
def test_s1_12_the_table_is_user_side_with_the_tenant_column(migrated):
    assert migrated.execute("SELECT to_regclass('\"user\".drc_events')").fetchone()[0]
    assert migrated.execute("SELECT to_regclass('system.drc_events')").fetchone()[0] is None
    nullable, default = migrated.execute(
        "SELECT is_nullable, column_default FROM information_schema.columns "
        "WHERE table_schema = 'user' AND table_name = 'drc_events' AND column_name = 'user_id'"
    ).fetchone()
    assert nullable == "NO" and "cobalt.trader_id" in default


@requires_db
def test_s1_12_the_rollback_round_trips_and_is_a_no_op_when_its_objects_are_absent(migrated):
    """The round trip inside the rollback: `0019` applied → rolled back
    (the table gone, the three `drc_imports` columns and both CHECKs back)
    → re-applied (the columns gone again); a second rollback, and one on a
    tree whose `drc_imports` is gone, are no-ops (the rollback contract)."""
    assert not [c for c in _columns(migrated, "drc_imports") if c.startswith("event_")]
    _apply(migrated, [ROLLBACK])
    assert migrated.execute("SELECT to_regclass('\"user\".drc_events')").fetchone()[0] is None
    assert [c for c in _columns(migrated, "drc_imports") if c.startswith("event_")] == [
        "event_state", "event_updated_at", "event_error"]
    _to_0018(migrated)
    before = _check_rows(migrated, "drc_imports")
    _apply(migrated, [SQL, ROLLBACK])
    after = _check_rows(migrated, "drc_imports")
    warnings.warn(
        f"RUN-6: CHECK names before 0019 = {sorted(n for n, _ in before)}; "
        f"after 0019 + rollback = {sorted(n for n, _ in after)}",
        UserWarning,
    )
    assert sorted(d for _, d in after) == sorted(d for _, d in before)
    _apply(migrated, [ROLLBACK])  # repeated: a no-op
    _apply(migrated, [SQL])
    _apply(migrated, [SQL])  # idempotent
    assert migrated.execute("SELECT to_regclass('\"user\".drc_events')").fetchone()[0]
    assert not [c for c in _columns(migrated, "drc_imports") if c.startswith("event_")]
    _apply(migrated, _rollback_paths("0015"))  # 0019 → 0016 in order: drc_imports gone
    assert migrated.execute("SELECT to_regclass('\"user\".drc_imports')").fetchone()[0] is None
    _apply(migrated, [ROLLBACK])  # its objects absent: a no-op
    _apply(migrated, FORWARD)
    assert migrated.execute("SELECT to_regclass('\"user\".drc_events')").fetchone()[0]


# ---------------------------------------------------------------------
# §1 test 7 — the retired columns are gone
# ---------------------------------------------------------------------


@requires_db
def test_s1_7_drc_imports_has_no_event_column_after_the_migration(migrated):
    """§1 test 7 (`:175`): read from `pg_catalog`, unscoped (L35)."""
    columns = _columns(migrated, "drc_imports")
    assert "import_date" in columns and "trade_key" in columns
    assert [c for c in columns if c.startswith("event")] == []


# ---------------------------------------------------------------------
# §1 test 1 — the file-less happy path
# ---------------------------------------------------------------------


@requires_db
@pytest.mark.parametrize("build", ["returns", "raises", "absent"])
def test_s1_1_a_file_less_no_trade_day_fires_one_stated_book_event(lane, migrated, monkeypatch, build):
    """§1 test 1 (`:164`): a recorded prior, then "No trades today" (no
    file) → ONE `drc_events` row, `source = stated_book`, the statement's
    id. With E11's stub: return → `done` + `note_path`; raise → `failed`,
    never `done`; no stub → `failed: build not built (D3)`."""
    from cobalt.drc import imports

    _recorded_prior()
    if build == "returns":
        _stub_build(monkeypatch, lambda event: NOTE_PATH)
    elif build == "raises":
        _stub_build(monkeypatch, _raise_build)
    result = imports.no_trade(D_NEXT, now=TEN_ET)
    (statement,) = _no_trade_ids(migrated, D_NEXT)
    expected = {
        "returns": ("done", None, NOTE_PATH),
        "raises": ("failed", "RuntimeError: constructed kill after pending", None),
        "absent": ("failed", "build not built (D3)", None),
    }[build]
    assert _events(migrated, D_NEXT) == [("stated_book", None, statement, *expected)]
    event = DrcStore().event_for(D_NEXT)
    assert (event["source"], event["import_id"], event["stated_book_id"]) == ("stated_book", None, statement)
    assert (event["state"], event["error"], event["note_path"]) == expected
    if build == "returns":
        assert result.status_line == f"no-trade day recorded → DRC built: {NOTE_PATH}"
        # D3 row 0d (`58` `## FOR DEJAN` 4, a NAMED EDIT): the same
        # assertions, moved into two helpers so F-6's control can call each.
        _event_source_assertions(result.event, statement)
        _stored_hash_assertions(result.event, migrated, statement)
    else:
        assert result.status_line == f"DRC build FAILED: build — {expected[1]}"
        assert "DRC built" not in imports.render_status(imports.day_view(D_NEXT))


# ---------------------------------------------------------------------
# §1 test 2 — the rebuild refuses
# ---------------------------------------------------------------------


@requires_db
def test_s1_2_a_refused_rebuild_fails_the_event_naming_record_and_keeps_the_statement(lane, migrated):
    """§1 test 2 (`:165`): D recorded with no book (not computed), so the
    no-trade day's rebuild refuses → the event is `failed` with K2's text
    verbatim, the status line names `record — …`, the statement is kept,
    `drc_rows` unchanged."""
    from cobalt.drc import imports

    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    rows_before = _snapshot(migrated, D) + _snapshot(migrated, D_NEXT)
    result = imports.no_trade(D_NEXT, now=TEN_ET)
    (statement,) = _no_trade_ids(migrated, D_NEXT)
    assert _events(migrated, D_NEXT) == [("stated_book", None, statement, "failed", NOT_COMPUTED_PRIOR, None)]
    assert result.status_line == f"DRC build FAILED: record — {NOT_COMPUTED_PRIOR}"
    assert result.message == f"not rebuilt: {NOT_COMPUTED_PRIOR}"
    assert _snapshot(migrated, D) + _snapshot(migrated, D_NEXT) == rows_before


# ---------------------------------------------------------------------
# §1 test 3 — the event survives a re-pair
# ---------------------------------------------------------------------


@requires_db
def test_s1_3_a_done_file_less_event_survives_an_earlier_days_re_pair(lane, migrated, monkeypatch):
    """§1 test 3 (`:166`; option (C)'s rejection, proven): the file-less
    day `done`, then a superseding trading log for the EARLIER day re-pairs
    it forward — its `drc_events` row is byte-unchanged (state, note_path,
    updated_at) while its `drc_rows` are rewritten."""
    from cobalt.drc import imports

    _stub_build(monkeypatch, lambda event: NOTE_PATH)
    _recorded_prior()
    imports.no_trade(D_NEXT, now=TEN_ET)
    row = 'SELECT id, state, note_path, updated_at, error FROM "user".drc_events WHERE day = %s'
    before = migrated.execute(row, (D_NEXT,)).fetchall()
    rows_before = _snapshot(migrated, D_NEXT)
    ids_before = migrated.execute('SELECT array_agg(id ORDER BY id) FROM "user".drc_rows WHERE day = %s',
                                  (D_NEXT,)).fetchone()[0]
    assert [r[1:3] for r in before] == [("done", NOTE_PATH)]
    _drop(D, D_FLAT)  # a superseding day-1 file that leaves nothing open
    assert migrated.execute(row, (D_NEXT,)).fetchall() == before
    assert _snapshot(migrated, D_NEXT) != rows_before
    ids_after = migrated.execute('SELECT array_agg(id ORDER BY id) FROM "user".drc_rows WHERE day = %s',
                                 (D_NEXT,)).fetchone()[0]
    assert not set(ids_before) & set(ids_after)


# ---------------------------------------------------------------------
# §1 test 4 — the file-day event re-pointed
# ---------------------------------------------------------------------


@requires_db
def test_s1_4_the_file_day_event_lives_on_drc_events_and_a_new_file_gets_a_new_row(lane, migrated, monkeypatch):
    """§1 test 4 (`:167`): the file day's event is a `drc_events` row with
    `source = import` on the current trading-log import; a superseding
    file gets a NEW row for the new import, the old row stays."""
    _stub_build(monkeypatch, lambda event: NOTE_PATH)
    _state(D)
    first = _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    first_import = first.event.import_id
    assert _events(migrated, D) == [("import", first_import, None, "done", None, NOTE_PATH)]
    second = _drop(D, D_FLAT)
    assert second.event.import_id != first_import
    assert _events(migrated, D) == [
        ("import", first_import, None, "done", None, NOTE_PATH),
        ("import", second.event.import_id, None, "done", None, NOTE_PATH),
    ]
    event = DrcStore().event_for(D)
    assert (event["source"], event["import_id"], event["note_path"]) == ("import", second.event.import_id, NOTE_PATH)
    assert event["event_id"] == second.event.event_id


# ---------------------------------------------------------------------
# §1 test 5 — the CHECKs and fire_event's refusals
# ---------------------------------------------------------------------


@requires_db
def test_s1_5_the_table_refuses_a_row_the_state_machine_forbids(lane, migrated):
    """§1 test 5 (`:168`–`:173`), the table half."""
    stated = _state(D, kind="no_trade")
    other = _state(D_NEXT, kind="no_trade")
    insert = 'INSERT INTO "user".drc_events (day, source, import_id, stated_book_id, state, error, note_path) '
    _raises(psycopg.errors.CheckViolation, insert + "VALUES (%s, 'import', NULL, %s, 'pending', NULL, NULL)",
            (D, stated.id))
    _raises(psycopg.errors.CheckViolation, insert + "VALUES (%s, 'stated_book', NULL, %s, 'failed', NULL, NULL)",
            (D, stated.id))
    _raises(psycopg.errors.CheckViolation, insert + "VALUES (%s, 'stated_book', NULL, %s, 'failed', '', NULL)",
            (D, stated.id))
    _raises(psycopg.errors.CheckViolation, insert + "VALUES (%s, 'stated_book', NULL, %s, 'done', NULL, NULL)",
            (D, stated.id))
    _raises(psycopg.errors.CheckViolation,
            insert + "VALUES (%s, 'stated_book', NULL, %s, 'running', NULL, 'constructed/x.md')", (D, stated.id))
    with DrcStore()._connect() as conn:
        conn.execute(insert + "VALUES (%s, 'stated_book', NULL, %s, 'pending', NULL, NULL)", (D_NEXT, other.id))
    _raises(psycopg.errors.UniqueViolation,
            insert + "VALUES (%s, 'stated_book', NULL, %s, 'pending', NULL, NULL)", (D_NEXT, other.id))


@requires_db
def test_s1_5_fire_event_refuses_every_source_that_is_not_the_days_current_input(lane, migrated):
    """§1 test 5, `fire_event`'s half: a superseded statement, a
    non-`no_trade` statement, another day's statement, a non-trading-log
    import, another day's import, two sources and none — each refused,
    nothing written; `mark_event`'s `failed` / `done` rules too."""
    store = DrcStore()
    first = _state(D, kind="no_trade")
    restated = _state(D, kind="no_trade", supersedes=first.id)
    opening = _state(D, kind="opening")
    elsewhere = _state(D_NEXT, kind="no_trade")
    stats_only = _drop(D3, None, STATS.read_bytes()).files[0].import_id
    trading = _drop(D_NEXT, EEE_ROUND).files[0].import_id
    before = _event_count(migrated)
    for kw in (
        dict(stated_book_id=first.id),       # superseded
        dict(stated_book_id=opening.id),     # not a no_trade statement
        dict(stated_book_id=elsewhere.id),   # another day's
        dict(import_id=stats_only),          # not a trading log
        dict(import_id=trading),             # another day's import
        dict(import_id=trading, stated_book_id=restated.id),
        dict(),
    ):
        with pytest.raises(ValueError, match="nothing written"):
            store.fire_event(D, **kw)
    assert _event_count(migrated) == before
    event_id = store.fire_event(D, stated_book_id=restated.id)
    with pytest.raises(ValueError):
        store.mark_event(event_id, "failed")
    with pytest.raises(ValueError):
        store.mark_event(event_id, "running", note_path="constructed/x.md")
    with pytest.raises(ValueError):
        store.mark_event(event_id, "pending")
    store.mark_event(event_id, "running")
    with pytest.raises(ValueError):
        store.mark_event(event_id, "done")
    assert _events(migrated, D) == [("stated_book", None, restated.id, "running", None, None)]


# ---------------------------------------------------------------------
# §1 test 6 — which event is the day's
# ---------------------------------------------------------------------


@requires_db
def test_s1_6_a_zero_execution_log_and_a_no_trade_statement_the_import_is_the_days_event(lane, migrated):
    """§1 test 6 (`:174`): step 1 of the three-step rule wins."""
    header = DAY1.read_bytes().splitlines(keepends=True)[0]
    _state(D)
    placed = _drop(D, header)
    statement = _state(D, kind="no_trade")
    DrcStore().fire_event(D, stated_book_id=statement.id)
    event = DrcStore().event_for(D)
    assert (event["source"], event["import_id"], event["stated_book_id"]) == ("import", placed.event.import_id, None)
    assert event["event_id"] == placed.event.event_id


# ---------------------------------------------------------------------
# §1 test 8 — the CLI fires the SAME event as the page
# ---------------------------------------------------------------------


@requires_db
def test_s1_8_the_cli_no_trade_apply_fires_the_same_event_as_the_page(lane, migrated, capsys, at_ten):
    """§1 test 8 (`:176`): `state-book --no-trade D --apply` fires ONE
    `drc_events` row, `source = stated_book`, through `imports.
    no_trade_event`; the page's row for the same day (the same inputs,
    rolled back to the same point) is equal in every column but `id`, the
    timestamps and the statement it names (each its own `no_trade` row)."""
    _recorded_prior()
    columns = "user_id, day, source, import_id, state, error, note_path"
    migrated.execute("SAVEPOINT cli_vs_page")
    code, out = _cli(capsys, "--no-trade", "2001-01-03")
    code, out = _cli(capsys, "--no-trade", "2001-01-03", "--apply", "--sha256", _printed_hash(out))
    assert code == 1, out  # the build is not built: a failed event exits non-zero
    assert "rebuilt: 2001-01-03" in out and "DRC build FAILED: build — build not built (D3)" in out
    (cli_statement,) = _no_trade_ids(migrated, D_NEXT)
    cli_rows = migrated.execute(f'SELECT {columns}, stated_book_id FROM "user".drc_events WHERE day = %s',
                                (D_NEXT,)).fetchall()
    migrated.execute("ROLLBACK TO SAVEPOINT cli_vs_page")
    lane.post("/drc/no-trade", data={"date": D_NEXT.isoformat()})
    (page_statement,) = _no_trade_ids(migrated, D_NEXT)
    page_rows = migrated.execute(f'SELECT {columns}, stated_book_id FROM "user".drc_events WHERE day = %s',
                                 (D_NEXT,)).fetchall()
    assert len(cli_rows) == len(page_rows) == 1
    assert cli_rows[0][:-1] == page_rows[0][:-1]
    assert (cli_rows[0][-1], page_rows[0][-1]) == (cli_statement, page_statement)
    assert cli_rows[0][2] == "stated_book"


# ---------------------------------------------------------------------
# S-2 §2 tests 1–3 — the screenshot writer
# ---------------------------------------------------------------------


def _bound_day(monkeypatch):
    """A READY day with a computed pairing, its trades read back."""
    _stub_build(monkeypatch, lambda event: NOTE_PATH)
    _state(D)
    _drop(D, DAY1.read_bytes(), STATS.read_bytes())
    return DrcStore().event_for(D)["trades"]


def _shots(conn, day):
    return conn.execute(
        'SELECT id, name, sha256, trade_key, parse_status, supersedes FROM "user".drc_imports '
        "WHERE import_date = %s AND kind = 'screenshot' ORDER BY id",
        (day,),
    ).fetchall()


def _folder(lane_root: Path):
    return lane_root / DRC / D.isoformat()


def _vault_root() -> Path:
    import os

    return Path(os.environ["COBALT_VAULT_PATH"])


@requires_db
def test_s2_1_a_png_on_a_trade_of_the_current_log_is_bound_and_written(lane, migrated, monkeypatch):
    """§2 test 1 (`:241`): one row `kind = screenshot`, `trade_key` set,
    the bytes under `_imports/drc/<date>/`."""
    from cobalt.drc import imports

    trades = _bound_day(monkeypatch)
    result = imports.place(D, [("shot.png", PNG)], trade_key=trades[0], now=TEN_ET)
    assert [f.text() for f in result.files] == ["✓ shot.png — screenshot parsed"]
    (shot,) = _shots(migrated, D)
    assert shot[1:] == ("shot.png", hashlib.sha256(PNG).hexdigest(), trades[0], "parsed", None)
    assert (_folder(_vault_root()) / "shot.png").read_bytes() == PNG
    assert result.event is not None and result.event.screenshot_import_ids == [shot[0]]


@requires_db
def test_s2_2_a_re_drop_supersedes_and_keeps_the_old_row_and_bytes(lane, migrated, monkeypatch):
    """§2 test 2 (`:242`)."""
    from cobalt.drc import imports

    trades = _bound_day(monkeypatch)
    other = PNG + b"\x01"
    imports.place(D, [("shot.png", PNG)], trade_key=trades[0], now=TEN_ET)
    imports.place(D, [("shot.png", other)], trade_key=trades[0], now=TEN_ET)
    first, second = _shots(migrated, D)
    assert second[5] == first[0] and (first[1], second[1]) == ("shot.png", "shot.1.png")
    folder = _folder(_vault_root())
    assert (folder / "shot.png").read_bytes() == PNG and (folder / "shot.1.png").read_bytes() == other


@requires_db
def test_s2_3_every_refusal_stores_and_writes_nothing(lane, migrated, monkeypatch, blocks):
    """§2 test 3 (`:243`): a key not in the current log → FAILED; zero
    bytes, a non-image, a drop inside `market_reset` → refused; nothing
    stored, nothing written. The store refuses the same three on its own."""
    from cobalt.drc import imports

    _bound_day(monkeypatch)
    folder = _folder(_vault_root())
    names_before = sorted(p.name for p in folder.iterdir())
    result = imports.place(D, [("shot.png", PNG)], trade_key="ZZZ-long-constructed", now=TEN_ET)
    assert [f.text() for f in result.files] == [
        "FAILED: shot.png — trade ZZZ-long-constructed is not in the current trading log"]
    trade = DrcStore().event_for(D)["trades"][0]
    for data in (b"", b"not an image"):
        assert imports.place(D, [("shot.png", data)], trade_key=trade, now=TEN_ET).files[0].status == "failed"
    reset = imports.place(D, [("shot.png", PNG)], trade_key=trade, now=RESET_ET)
    assert reset.refused == "refused: market reset 20:00–21:00 — drop again after 21:00"
    assert _shots(migrated, D) == []
    assert sorted(p.name for p in folder.iterdir()) == names_before
    store = DrcStore()
    for name, data, key in (("a.png", b"", trade), ("b.png", b"GIF89a", trade), ("c.png", PNG, "")):
        with pytest.raises(ValueError, match="nothing stored"):
            store.record_screenshot(D, name, data, key)
    assert _shots(migrated, D) == []


# ---------------------------------------------------------------------
# F-1 — with-DB: an uncaught exception after `pending` is `failed` on the row
# ---------------------------------------------------------------------


@requires_db
def test_an_uncaught_exception_after_pending_is_failed_on_the_event_row(lane, migrated, monkeypatch):
    """F-1 (`08` HOLD 3, `drc-d2-check-2026-09-25.md:138`, `:174`; L18, v2
    `[F-08]`): `seed_for` raising a non-`PairingError` after `pending` →
    the row is `failed` naming `seed — RuntimeError: constructed`, never
    `pending` / `done`; the same for `no_trade_event` with `rebuild`
    raising → `failed` naming `record — RuntimeError: …`, the statement
    kept."""
    from cobalt.drc import imports

    def _raise(*args, **kwargs):
        raise RuntimeError("constructed")

    _recorded_prior()  # D stated and dropped: a chain D_NEXT joins
    with monkeypatch.context() as m:
        m.setattr(DrcStore, "rebuild", _raise)
        result = imports.no_trade(D_NEXT, now=TEN_ET)
    (statement,) = _no_trade_ids(migrated, D_NEXT)
    assert _events(migrated, D_NEXT) == [
        ("stated_book", None, statement, "failed", "record — RuntimeError: constructed", None)]
    assert result.status_line == "DRC build FAILED: record — RuntimeError: constructed"

    with monkeypatch.context() as m:
        m.setattr(DrcStore, "seed_for", _raise)
        result = _drop(D3, EEE_ROUND, STATS.read_bytes())
    event = DrcStore().event_for(D3)
    assert (event["source"], event["state"]) == ("import", "failed")
    assert event["error"] == "seed — RuntimeError: constructed"
    assert result.status_line == "DRC build FAILED: seed — RuntimeError: constructed"
