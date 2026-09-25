"""DRC K1 — book records, WITH-DB half (v3 §3, §6 K1; R51, R52).

Migration `0018_drc_stated_books`, `DrcStore.record_stated_book` /
`preview_stated_book`, `seed_for`'s cases (i)–(viii), `record_day`'s
`seed` / `book_close` rows and the `cobalt drc state-book` CLI end to end.

Everything runs inside `test_drc_store.py`'s never-committed migration
transaction on `cobalt_dev` (L76): nothing here commits a migration.
Every statement passes a CONSTRUCTED clock, so no test depends on the
hour it runs. Constructed symbols and dates only (L32 / L45).
"""

from __future__ import annotations

import argparse
import hashlib
import re
from datetime import date, datetime, timezone

import psycopg
import pytest
from psycopg.types.json import Jsonb

from cobalt.db import Side
from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.cli import _apply, _rollback_paths
from cobalt.db_migrations.placement import CREATED_TABLES, side_of
from cobalt.drc.detect import detect_kind
from cobalt.drc.models import Kind, PairingError, TradeStatus
from cobalt.drc.store import DrcStore
from cobalt.drc.trading_log import TradingLogSource

from test_drc_pairing import CARRIED_SHORT_DAY2
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    DAY1,
    SEED,
    _trading,
    migrated,
    requires_db,
    weekday_calendar,
)

SQL = MIGRATIONS_DIR / "0018_drc_stated_books.sql"
ROLLBACK = MIGRATIONS_DIR / "0018_drc_stated_books.rollback.sql"
D3 = date(2001, 1, 4)

TEN_ET = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
RESET_ET = datetime(2026, 9, 4, 0, 15, tzinfo=timezone.utc)
EMPTY = hashlib.sha256(b"[]").hexdigest()

GGG_SHORT = {"symbol": "GGG", "direction": "short", "shares": 40, "avg_cost": None}


def _code(path) -> str:
    return "\n".join(l for l in path.read_text().splitlines() if not l.strip().startswith("--"))


def _row(conn, day: date, kind: str):
    return conn.execute(
        'SELECT inputs, derived FROM "user".drc_rows WHERE day = %s AND kind = %s', (day, kind)
    ).fetchone()


def _stated_count(conn) -> int:
    return conn.execute('SELECT count(*) FROM "user".drc_stated_books').fetchone()[0]


def _state(day: date, kind: str = "opening", positions=(), **kw):
    kw.setdefault("via", "cli")
    kw.setdefault("now", TEN_ET)
    return DrcStore().record_stated_book(day, kind, list(positions), **kw)


def _record(path_or_bytes, day: date, seed):
    """Import one trading log for `day` and record it from `seed`."""
    from cobalt.drc.pairing import build_day

    store = DrcStore()
    if isinstance(path_or_bytes, bytes):
        data = path_or_bytes
        parsed = TradingLogSource().parse(data, day, detect_kind("t.md", data))
    else:
        data, parsed = _trading(path_or_bytes, day)
    ids = {Kind.TRADING_LOG: store.record_import(day, parsed.result, data, parsed.executions)}
    pairing = build_day(parsed, seed=None if seed is None else seed.positions)
    store.record_day(pairing, ids, seed)
    return pairing, ids


def _day1_carrying_ddd():
    """Day 1 stated flat and recorded: DDD 30 left open."""
    _state(D)
    seed = DrcStore().seed_for(D)
    pairing, _ = _record(DAY1, D, seed)
    return pairing


def _raises(exc, sql, params=None):
    """One statement through the store's proxy (USER side, tenant GUC set),
    inside its own savepoint, refused with `exc`."""
    with pytest.raises(exc):
        with DrcStore()._connect() as conn:
            conn.execute(sql, params)


# ---------------------------------------------------------------------
# OFFLINE — the registry, the placement map, the SQL
# ---------------------------------------------------------------------


def test_the_pair_exists_and_is_registered_after_0016():
    assert SQL.exists() and ROLLBACK.exists()
    names = [p.name for p in FORWARD]
    assert names[-2:] == ["0016_drc.sql", "0018_drc_stated_books.sql"]
    assert REVERSE[0] == ROLLBACK and REVERSE[1].name == "0016_drc.rollback.sql"


def test_down_to_0016_selects_only_the_k1_rollback():
    assert [p.name for p in _rollback_paths("0016")] == ["0018_drc_stated_books.rollback.sql"]


def test_the_table_is_placed_user_side():
    assert side_of("drc_stated_books") is Side.USER
    assert CREATED_TABLES["drc_stated_books"] is Side.USER


def test_0016_is_never_edited_and_0018_creates_one_table():
    assert "drc_stated_books" not in (MIGRATIONS_DIR / "0016_drc.sql").read_text()
    code = _code(SQL)
    assert re.findall(r'CREATE TABLE IF NOT EXISTS "user"\.(\w+)', code) == ["drc_stated_books"]
    assert "'cli'" in code and "'drc_page'" in code and "'voice_widget'" in code
    assert '"user".refuse_row_update()' in code


def test_the_rollback_states_its_cost():
    text = ROLLBACK.read_text()
    assert "-- COST:" in text
    assert "his statements live ONLY here" in text


# ---------------------------------------------------------------------
# WITH-DB — 0018 forward and rollback
# ---------------------------------------------------------------------


@requires_db
def test_0018_creates_the_table_user_side_with_the_tenant_column(migrated):
    assert migrated.execute("SELECT to_regclass('\"user\".drc_stated_books')").fetchone()[0]
    assert migrated.execute("SELECT to_regclass('system.drc_stated_books')").fetchone()[0] is None
    nullable, default = migrated.execute(
        "SELECT is_nullable, column_default FROM information_schema.columns "
        "WHERE table_schema = 'user' AND table_name = 'drc_stated_books' AND column_name = 'user_id'"
    ).fetchone()
    assert nullable == "NO" and "cobalt.trader_id" in default


@requires_db
@pytest.mark.parametrize(
    "kind, positions, sha, via",
    [
        ("closing", [], EMPTY, "cli"),
        ("opening", [], EMPTY, "drc_form"),
        ("resolve", [{"trade_id": "a"}, {"trade_id": "b"}], EMPTY, "cli"),
        ("opening", {}, EMPTY, "cli"),
        ("opening", [], "NOTAHASH", "cli"),
    ],
    ids=["bad kind", "bad via", "two-position resolve", "positions not an array", "bad hash"],
)
def test_the_checks_refuse_a_bad_row(migrated, kind, positions, sha, via):
    _raises(
        psycopg.errors.CheckViolation,
        'INSERT INTO "user".drc_stated_books (day, kind, positions, book_sha256, via, reason) '
        "VALUES (%s, %s, %s, %s, %s, 'first import')",
        (D, kind, Jsonb(positions), sha, via),
    )


@requires_db
def test_a_stated_row_is_append_only(migrated):
    row = _state(D)
    _raises(
        psycopg.errors.RaiseException,
        'UPDATE "user".drc_stated_books SET reason = %s WHERE id = %s', ("x", row.id),
    )
    _raises(
        psycopg.errors.RaiseException,
        'DELETE FROM "user".drc_stated_books WHERE id = %s', (row.id,),
    )


OLD_KINDS = {"trade", "open_position", "stats_row", "day"}
NEW_KINDS = OLD_KINDS | {"seed", "book_close"}


def _kind_check(conn) -> list[tuple[str, set[str]]]:
    """Every CHECK on `drc_rows` that names `kind`, read from `pg_constraint`
    (an unscoped catalog read, L35): its name and its literals."""
    rows = conn.execute(
        "SELECT conname, pg_get_constraintdef(oid) FROM pg_constraint "
        "WHERE conrelid = '\"user\".drc_rows'::regclass AND contype = 'c' "
        "AND pg_get_constraintdef(oid) LIKE %s",
        ("%kind%",),
    ).fetchall()
    return [(name, set(re.findall(r"'(\w+)'", definition))) for name, definition in rows]


@requires_db
def test_the_drc_rows_kind_check_is_widened_under_its_proven_name(migrated):
    _apply(migrated, [ROLLBACK])
    assert _kind_check(migrated) == [("drc_rows_kind_check", OLD_KINDS)]
    _apply(migrated, [SQL])
    assert _kind_check(migrated) == [("drc_rows_kind_check", NEW_KINDS)]


@requires_db
def test_the_rollback_drops_the_table_restores_the_check_and_deletes_the_derived_rows(migrated):
    with DrcStore()._connect() as conn:
        for kind in ("seed", "book_close"):
            conn.execute(
                "INSERT INTO drc_rows (day, kind, ref, inputs, derived, fn_version) "
                "VALUES (%s, %s, 'book', '{}', '{}', 'k1')",
                (D, kind),
            )
    _apply(migrated, [ROLLBACK])
    assert migrated.execute("SELECT to_regclass('\"user\".drc_stated_books')").fetchone()[0] is None
    assert _kind_check(migrated) == [("drc_rows_kind_check", OLD_KINDS)]
    assert migrated.execute(
        """SELECT count(*) FROM "user".drc_rows WHERE kind IN ('seed', 'book_close')"""
    ).fetchone()[0] == 0
    _apply(migrated, [SQL])
    _apply(migrated, [SQL])
    assert migrated.execute("SELECT to_regclass('\"user\".drc_stated_books')").fetchone()[0]
    assert _kind_check(migrated) == [("drc_rows_kind_check", NEW_KINDS)]


# ---------------------------------------------------------------------
# WITH-DB — record_stated_book / preview_stated_book (C3)
# ---------------------------------------------------------------------


@requires_db
def test_a_cli_statement_stores_no_turn_and_no_readback(migrated):
    row = _state(D)
    assert (row.via, row.turn_id, row.readback_sha256) == ("cli", None, None)
    stored = migrated.execute(
        'SELECT via, turn_id, readback_sha256, book_sha256, reason FROM "user".drc_stated_books WHERE id = %s',
        (row.id,),
    ).fetchone()
    assert stored == ("cli", None, None, EMPTY, "first import")


@requires_db
def test_the_via_rules(migrated):
    with pytest.raises(ValueError, match="voice_widget"):
        _state(D, via="voice_widget")
    with pytest.raises(ValueError, match="turn_id"):
        _state(D, via="cli", turn_id="t1")
    with pytest.raises(ValueError, match="readback_sha256"):
        _state(D, via="drc_page", readback_sha256="ab" * 32)
    with pytest.raises(ValueError):
        _state(D, via="state_book_cli")
    assert _stated_count(migrated) == 0
    row = _state(D, via="voice_widget", turn_id="t1", readback_sha256="ab" * 32)
    assert (row.via, row.turn_id, row.readback_sha256) == ("voice_widget", "t1", "ab" * 32)


@requires_db
def test_a_hash_mismatch_is_refused_before_any_write(migrated):
    with pytest.raises(ValueError, match="book_sha256"):
        _state(D, positions=[GGG_SHORT], expected_sha256=EMPTY)
    assert _stated_count(migrated) == 0
    assert _state(D, expected_sha256=EMPTY).book_sha256 == EMPTY


@requires_db
def test_a_second_opening_for_one_day_is_refused_until_it_supersedes(migrated):
    first = _state(D)
    with pytest.raises(ValueError, match=f"#{first.id}"):
        _state(D, positions=[GGG_SHORT])
    second = _state(D, positions=[GGG_SHORT], supersedes=first.id)
    assert second.supersedes == first.id
    current = migrated.execute(
        """SELECT id FROM "user".drc_stated_books s WHERE day = %s AND kind = 'opening'
           AND id NOT IN (SELECT supersedes FROM "user".drc_stated_books WHERE supersedes IS NOT NULL)""",
        (D,),
    ).fetchall()
    assert current == [(second.id,)]
    with pytest.raises(ValueError, match=f"#{first.id}"):
        _state(D, supersedes=first.id)


@requires_db
def test_a_supersedes_that_names_no_current_row_is_refused(migrated):
    with pytest.raises(ValueError, match="supersedes"):
        _state(D, supersedes=999_999)
    other = _state(D, kind="no_trade")
    with pytest.raises(ValueError, match="supersedes"):
        _state(D, supersedes=other.id)


@requires_db
def test_the_reason_is_derived_first_import_then_chain_broken(migrated, weekday_calendar):
    assert _state(D).reason == "first import"
    _record(DAY1, D, DrcStore().seed_for(D))
    assert _state(D3).reason == "chain broken at 2001-01-03"
    assert _state(D3, kind="no_trade").reason == "no-trade DRC"


@requires_db
def test_an_opening_is_refused_while_its_prior_trading_day_is_recorded(migrated, weekday_calendar):
    """H2 (`drc-k1-check-2026-09-24.md:150`; L1; v3 §2c `:108`, `:139`;
    R51 "the close wins"): with D recorded, an `opening` for D_NEXT is
    refused — by the writer and by the preview — and no row is stored, so
    no false `chain broken at <P>` text is ever written to the append-only
    table. The lawful cases stay: a real broken chain, and `no_trade`."""
    _day1_carrying_ddd()
    before = _stated_count(migrated)
    with pytest.raises(ValueError, match="is recorded"):
        _state(D_NEXT)
    with pytest.raises(ValueError, match="is recorded"):
        DrcStore().preview_stated_book(D_NEXT, "opening", [], via="cli")
    assert _stated_count(migrated) == before
    assert migrated.execute(
        'SELECT count(*) FROM "user".drc_stated_books WHERE day = %s', (D_NEXT,)
    ).fetchone()[0] == 0
    assert _state(D3).reason == "chain broken at 2001-01-03"
    assert _state(D3, kind="no_trade").reason == "no-trade DRC"


@requires_db
def test_a_resolve_names_exactly_one_trade(migrated):
    with pytest.raises(ValueError):
        _state(D, kind="resolve", positions=[{"trade_id": "a"}, {"trade_id": "b"}])
    with pytest.raises(ValueError):
        _state(D, kind="resolve", positions=[])
    row = _state(D, kind="resolve", positions=[{"trade_id": "a", "exit_price": "19.5"}])
    assert row.reason == "closed outside export"
    assert row.positions == [{"trade_id": "a", "exit_price": "19.5", "exit_time": None}]
    with pytest.raises(ValueError, match=f"#{row.id}"):
        _state(D, kind="resolve", positions=[{"trade_id": "a"}])
    _state(D, kind="resolve", positions=[{"trade_id": "b"}])


@requires_db
def test_a_no_trade_statement_is_stored_with_an_empty_book(migrated):
    row = _state(D, kind="no_trade")
    assert (row.kind, row.positions, row.book_sha256) == ("no_trade", [], EMPTY)
    with pytest.raises(ValueError):
        _state(D_NEXT, kind="no_trade", positions=[GGG_SHORT])


@requires_db
def test_an_opening_refuses_a_repeated_symbol_and_non_positive_figures(migrated):
    for bad in (
        [GGG_SHORT, GGG_SHORT],
        [{**GGG_SHORT, "shares": 0}],
        [{**GGG_SHORT, "avg_cost": "0"}],
        [{**GGG_SHORT, "direction": "sideways"}],
    ):
        with pytest.raises(ValueError):
            _state(D, positions=bad)
    assert _stated_count(migrated) == 0


@requires_db
def test_the_preview_is_the_row_without_its_id_and_writes_nothing(migrated):
    positions = [{"symbol": "HHH", "direction": "long", "shares": 10, "avg_cost": "11.0"}, GGG_SHORT]
    preview = DrcStore().preview_stated_book(D, "opening", positions, via="cli")
    assert preview.id is None and _stated_count(migrated) == 0
    assert [p["symbol"] for p in preview.positions] == ["GGG", "HHH"]
    row = _state(D, positions=positions, expected_sha256=preview.book_sha256)
    assert (row.positions, row.book_sha256, row.reason) == (preview.positions, preview.book_sha256, preview.reason)


# ---------------------------------------------------------------------
# WITH-DB — seed_for (C4)
# ---------------------------------------------------------------------


@requires_db
def test_seed_i_a_prior_day_not_computed_fails(migrated, weekday_calendar):
    _record(DAY1, D, None)
    assert "pairing" in _row(migrated, D, "day")[1]["not_computed"]
    with pytest.raises(PairingError, match="2001-01-02 has pairing not computed"):
        DrcStore().seed_for(D_NEXT)


@requires_db
def test_seed_ii_a_prior_day_recorded_before_the_lane_fails_naming_the_rebuild(migrated, weekday_calendar):
    with DrcStore()._connect() as conn:
        conn.execute(
            "INSERT INTO drc_rows (day, kind, ref, inputs, derived, fn_version) "
            "VALUES (%s, 'day', 'day', '{}', %s, 'drc.pairing/1')",
            (D, Jsonb({"trades": 0, "open_positions": 0, "unmatched": 0, "not_computed": {}})),
        )
    with pytest.raises(PairingError, match=r"2001-01-02 was recorded before the overnight-position lane \(no book_close\) — rebuild 2001-01-02"):
        DrcStore().seed_for(D_NEXT)


@requires_db
def test_seed_iii_a_close_row_that_does_not_match_its_positions_fails(migrated, weekday_calendar):
    _day1_carrying_ddd()
    migrated.execute(
        """UPDATE "user".drc_rows SET derived = jsonb_set(derived, '{book_sha256}', to_jsonb(%s::text))
           WHERE day = %s AND kind = 'book_close'""",
        ("0" * 64, D),
    )
    with pytest.raises(PairingError, match="seed for 2001-01-03: 2001-01-02's stored book does not match its own close row"):
        DrcStore().seed_for(D_NEXT)


@requires_db
def test_seed_v_a_recorded_prior_day_is_carried_with_its_hash(migrated, weekday_calendar):
    from cobalt.drc.pairing import book_sha256

    day1 = _day1_carrying_ddd()
    seed = DrcStore().seed_for(D_NEXT)
    assert seed.source == "carried" and seed.from_day == D and seed.stated_book_id is None
    assert seed.positions == day1.open_positions
    assert seed.from_book_sha256 == book_sha256(day1.open_positions) == _row(migrated, D, "book_close")[1]["book_sha256"]


@requires_db
def test_seed_vi_a_stated_book_seeds_a_first_import(migrated, weekday_calendar):
    """H1 (`drc-k1-check-2026-09-24.md:149`; K1 fix r1): the stated
    position's open day is NOT STATED (`None`), never the stated day (L1)."""
    stated = _state(D, positions=[GGG_SHORT])
    seed = DrcStore().seed_for(D)
    assert seed.source == "stated" and seed.stated_book_id == stated.id and seed.from_day is None
    assert seed.from_book_sha256 == stated.book_sha256
    (pos,) = seed.positions
    assert pos.trade_id == "GGG-short-stated-2001-01-02" and pos.held_shares == 40
    assert pos.opened_on is None and pos.day == D and pos.entry_time is None


@requires_db
def test_seed_vi_a_stated_book_mends_a_broken_chain(migrated, weekday_calendar):
    _day1_carrying_ddd()
    stated = _state(D3)
    seed = DrcStore().seed_for(D3)
    assert seed.source == "stated" and seed.stated_book_id == stated.id and seed.positions == []


@requires_db
def test_seed_vii_a_skipped_day_with_no_statement_fails_naming_it(migrated, weekday_calendar):
    _day1_carrying_ddd()
    with pytest.raises(PairingError, match="prior trading day 2001-01-03 has no import"):
        DrcStore().seed_for(D3)


@requires_db
def test_seed_viii_nothing_recorded_and_nothing_stated_is_none(migrated, weekday_calendar):
    assert DrcStore().seed_for(D) is None


@requires_db
def test_two_current_openings_for_one_day_fail_naming_both(migrated, weekday_calendar):
    first = _state(D)
    with DrcStore()._connect() as conn:  # a second current row, as no store call would write it
        second = conn.execute(
            """INSERT INTO "user".drc_stated_books (day, kind, positions, book_sha256, via, reason)
               VALUES (%s, 'opening', '[]', %s, 'cli', 'first import') RETURNING id""",
            (D, EMPTY),
        ).fetchone()[0]
    with pytest.raises(PairingError, match=rf"#{first.id}.*#{second}"):
        DrcStore().seed_for(D)


# ---------------------------------------------------------------------
# WITH-DB — record_day (C5)
# ---------------------------------------------------------------------


@requires_db
def test_a_stated_day_records_its_seed_and_its_close_with_their_inputs(migrated, weekday_calendar):
    from cobalt.drc.pairing import book_sha256

    stated = _state(D)
    seed = DrcStore().seed_for(D)
    day1, ids = _record(DAY1, D, seed)
    s_inputs, s_derived = _row(migrated, D, "seed")
    assert s_inputs == {"source": "stated", "from_day": None, "from_book_sha256": EMPTY, "stated_book_id": stated.id}
    assert s_derived == {"count": 0, "trade_ids": []}
    c_inputs, c_derived = _row(migrated, D, "book_close")
    (pos,) = day1.open_positions
    assert c_derived == {"count": 1, "trade_ids": [pos.trade_id], "book_sha256": book_sha256(day1.open_positions)}
    assert c_inputs == {
        "trading_log_import_id": ids[Kind.TRADING_LOG],
        "seed_ref": {"day": "2001-01-02", "kind": "seed", "ref": "book"},
    }
    d_inputs, _ = _row(migrated, D, "day")
    assert d_inputs["stated_book_id"] == stated.id
    assert migrated.execute(
        'SELECT DISTINCT fn_version FROM "user".drc_rows WHERE day = %s', (D,)
    ).fetchall() == [("drc.pairing/3",)]


@requires_db
def test_a_carried_trade_names_the_book_it_came_from(migrated, weekday_calendar):
    day1 = _day1_carrying_ddd()
    (pos,) = day1.open_positions
    seed = DrcStore().seed_for(D_NEXT)
    _record(SEED, D_NEXT, seed)
    inputs = migrated.execute(
        """SELECT inputs FROM "user".drc_rows WHERE day = %s AND kind = 'trade' AND ref = %s""",
        (D_NEXT, pos.trade_id),
    ).fetchone()[0]
    assert inputs["carried_from"] == {
        "day": "2001-01-02", "trade_id": pos.trade_id, "from_book_sha256": seed.from_book_sha256,
    }
    s_inputs, s_derived = _row(migrated, D_NEXT, "seed")
    assert s_inputs["source"] == "carried" and s_inputs["from_day"] == "2001-01-02"
    assert s_inputs["stated_book_id"] is None
    assert s_derived == {"count": 1, "trade_ids": [pos.trade_id]}
    assert "stated_book_id" not in _row(migrated, D_NEXT, "day")[0]
    fresh = migrated.execute(
        """SELECT inputs FROM "user".drc_rows WHERE day = %s AND kind = 'trade' AND ref LIKE 'FFF-%%'""",
        (D_NEXT,),
    ).fetchone()[0]
    assert "carried_from" not in fresh


@requires_db
def test_a_stated_trade_names_its_statement(migrated, weekday_calendar):
    stated = _state(D, positions=[GGG_SHORT])
    pairing, _ = _record(CARRIED_SHORT_DAY2, D, DrcStore().seed_for(D))
    (ggg,) = pairing.trades
    assert ggg.status is TradeStatus.CLOSED
    inputs, derived = migrated.execute(
        """SELECT inputs, derived FROM "user".drc_rows WHERE day = %s AND kind = 'trade'""", (D,)
    ).fetchone()
    assert inputs["carried_from"] == {"stated_book_id": stated.id}
    assert derived["gross_pnl"] == "not computed — carried cost not stated"
    assert _row(migrated, D, "book_close")[1]["count"] == 0


@requires_db
def test_a_not_computed_day_writes_no_close(migrated, weekday_calendar):
    _record(DAY1, D, None)
    assert _row(migrated, D, "book_close") is None
    assert _row(migrated, D, "seed") is None
    _, day = _row(migrated, D, "day")
    assert day["not_computed"]["pairing"] == "not computed — opening book not stated"


@requires_db
def test_the_route_records_an_unpaired_day_and_the_next_day_fails_until_it_is_stated(migrated, weekday_calendar):
    """H3 (`drc-k1-check-2026-09-24.md:151`; v3 §4 row 1 `:212`, X2 (a)
    `:313`; L72), GREEN-as-pin — the store already allows it
    (`store.py:212-217`); the seam text is the fix. An unpaired day is
    RECORDED: one `day` row, no `trade` / `seed` / `book_close`; the next
    day FAILS `pairing not computed` until D is stated and re-paired."""
    from cobalt.drc.pairing import build_day

    store = DrcStore()
    data, parsed = _trading(DAY1, D)
    ids = {Kind.TRADING_LOG: store.record_import(D, parsed.result, data, parsed.executions)}
    assert store.seed_for(D) is None
    pairing = build_day(parsed, seed=None)
    assert pairing.not_computed["pairing"] == "not computed — opening book not stated"
    store.record_day(pairing, ids, None)
    rows = migrated.execute(
        'SELECT kind, derived FROM "user".drc_rows WHERE day = %s', (D,)
    ).fetchall()
    assert [kind for kind, _ in rows] == ["day"]
    assert rows[0][1]["not_computed"]["pairing"] == "not computed — opening book not stated"
    for kind in ("trade", "seed", "book_close"):
        assert _row(migrated, D, kind) is None
    with pytest.raises(PairingError, match="2001-01-02 has pairing not computed"):
        store.seed_for(D_NEXT)

    assert _state(D).reason == "first import"
    seed = store.seed_for(D)
    assert seed.source == "stated"
    store.record_day(build_day(parsed, seed=seed.positions), ids, seed)
    assert store.seed_for(D_NEXT).source == "carried"


@requires_db
def test_a_computed_day_without_a_book_is_refused(migrated):
    from cobalt.drc.pairing import build_day

    data, parsed = _trading(DAY1, D)
    store = DrcStore()
    ids = {Kind.TRADING_LOG: store.record_import(D, parsed.result, data, parsed.executions)}
    with pytest.raises(ValueError, match="no book"):
        store.record_day(build_day(parsed, seed=[]), ids, None)
    assert migrated.execute('SELECT count(*) FROM "user".drc_rows WHERE day = %s', (D,)).fetchone()[0] == 0


# ---------------------------------------------------------------------
# WITH-DB — the CLI end to end (C7, R52)
# ---------------------------------------------------------------------


@pytest.fixture
def at_ten(monkeypatch):
    from cobalt.session import clock as clock_mod

    monkeypatch.setattr(clock_mod, "now_utc", lambda: TEN_ET)


@pytest.fixture
def blocks(monkeypatch):
    from cobalt.session.store import SessionBlockStore

    calls: list[dict] = []
    monkeypatch.setattr(SessionBlockStore, "record", lambda self, **kw: calls.append(kw))
    return calls


def _cli(capsys, *argv: str) -> tuple[int, str]:
    from cobalt.drc import cli as drc_cli

    parser = argparse.ArgumentParser(prog="cobalt")
    sub = parser.add_subparsers(dest="group", required=True)
    drc_cli.add_parser(sub)
    args = parser.parse_args(["drc", "state-book", *argv])
    try:
        args.func(args)
        code = 0
    except SystemExit as e:
        code = e.code if isinstance(e.code, int) else 1
    out = capsys.readouterr()
    return code, out.out + out.err


def _printed_hash(out: str) -> str:
    return re.search(r"^book_sha256: ([0-9a-f]{64})$", out, re.M).group(1)


@requires_db
@pytest.mark.parametrize(
    "argv",
    [
        ("--opening", "2001-01-02", "--flat"),
        ("--opening", "2001-01-02", "--position", "GGG", "short", "40", "--position", "HHH", "long", "10", "11.0"),
        ("--no-trade", "2001-01-02"),
        ("--resolve", "2001-01-02", "GGG-short-stated-2001-01-02", "--exit-price", "19.5",
         "--exit-time", "2001-01-02T15:00:00-05:00"),
    ],
    ids=["opening flat", "opening positions", "no-trade", "resolve"],
)
def test_the_cli_dry_runs_then_writes_only_the_reviewed_hash(migrated, capsys, at_ten, argv):
    code, out = _cli(capsys, *argv)
    assert code == 0 and "DRY RUN — nothing written" in out
    assert "via: cli" in out
    assert _stated_count(migrated) == 0
    printed = _printed_hash(out)

    code, out = _cli(capsys, *argv, "--apply", "--sha256", "0" * 64)
    assert code != 0 and _stated_count(migrated) == 0

    code, out = _cli(capsys, *argv, "--apply", "--sha256", printed)
    assert code == 0, out
    m = re.search(rf"^written: drc_stated_books #(\d+) \(book_sha256 {printed}\)$", out, re.M)
    assert m, out
    via, turn, readback, sha = migrated.execute(
        'SELECT via, turn_id, readback_sha256, book_sha256 FROM "user".drc_stated_books WHERE id = %s',
        (int(m.group(1)),),
    ).fetchone()
    assert (via, turn, readback, sha) == ("cli", None, None, printed)
    assert _stated_count(migrated) == 1


@requires_db
def test_the_cli_apply_is_refused_inside_market_reset_and_the_dry_run_still_prints(migrated, capsys, monkeypatch, blocks):
    from cobalt.session import clock as clock_mod

    monkeypatch.setattr(clock_mod, "now_utc", lambda: RESET_ET)
    code, out = _cli(capsys, "--opening", "2001-01-02", "--flat")
    assert code == 0 and _printed_hash(out) == EMPTY
    code, out = _cli(capsys, "--opening", "2001-01-02", "--flat", "--apply", "--sha256", EMPTY)
    assert code != 0 and "MARKET RESET" in out
    assert _stated_count(migrated) == 0 and len(blocks) == 1


@requires_db
def test_the_cli_restates_with_supersedes(migrated, capsys, at_ten):
    first = _state(D)
    code, out = _cli(capsys, "--opening", "2001-01-02", "--flat", "--apply", "--sha256", EMPTY)
    assert code != 0 and f"#{first.id}" in out
    code, out = _cli(capsys, "--opening", "2001-01-02", "--flat", "--supersedes", str(first.id),
                     "--apply", "--sha256", EMPTY)
    assert code == 0, out
    assert _stated_count(migrated) == 2
