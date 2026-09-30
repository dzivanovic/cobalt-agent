"""DRC K2 — WITH-DB half (v3 §2b, §3, §4; R51, R52; the build prompt's
K2 CONTRACT C3–C7).

R51's rebuild of a stated later day from the earlier close, the forward
re-pair (`[F-03]`), the no-trade carry (`[F-05]`), RESOLVE and its reader
(`[F-06]`), the H3 row, `stated_difference` and the CLI's rebuild after
`--apply`. His statements stay history: every sequence asserts
`drc_stated_books` byte-identical across `record_day` / `rebuild`.

Everything runs inside `test_drc_store.py`'s never-committed migration
transaction on `cobalt_dev` (L76). Every statement passes the constructed
10:00 ET clock. Constructed symbols and dates only (L32 / L45).
"""

from __future__ import annotations

import pytest
from psycopg.types.json import Jsonb

from cobalt.drc.models import Kind, PairingError
from cobalt.drc.pairing import pair_day
from cobalt.drc.store import _STATED_COLUMNS, DrcStore, _stated

from test_drc_k1_store import (  # noqa: F401 — fixtures are used by name
    D3,
    GGG_SHORT,
    _cli,
    _day1_carrying_ddd,
    _printed_hash,
    _row,
    _state,
    _stated_count,
    at_ten,
)
from test_drc_k2_experiments import (
    D_DDD_LATER,
    D_FLAT,
    DDD_COVER,
    EEE_ROUND,
    HHH_ROUND,
    _NOT_COMPUTED_PRIOR,
    _import,
    _route,
    _snapshot,
    _stated_rows,
    _without_stale,
)
from test_drc_pairing import CARRIED_SHORT_DAY1, CARRIED_SHORT_DAY2
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    DAY1,
    migrated,
    requires_db,
    weekday_calendar,
)

D4 = D3.replace(day=5)
EXIT_NOT_IN_ANY_EXPORT = "not computed — exit not in any export"


def _trade(conn, day, trade_id):
    return conn.execute(
        """SELECT inputs, derived FROM "user".drc_rows WHERE day = %s AND kind = 'trade' AND ref = %s""",
        (day, trade_id),
    ).fetchone()


def _r51_setup(opening=()):
    """R51's order: D_NEXT stated and recorded first (a `GGG` buy), then D
    stated flat and recorded leaving a `GGG` short open."""
    stated = _state(D_NEXT, positions=list(opening))
    _route(CARRIED_SHORT_DAY2 if not opening else HHH_ROUND, D_NEXT)
    _state(D)
    pairing, _, _ = _route(CARRIED_SHORT_DAY1, D)
    (pos,) = pairing.open_positions
    return stated, pos


# ---------------------------------------------------------------------
# R51 — the rebuild of a stated later day (C3 (iv), C4)
# ---------------------------------------------------------------------


@requires_db
def test_the_difference_survives_a_re_import_of_the_later_day(migrated, weekday_calendar):
    stated, pos = _r51_setup()
    books = _stated_rows(migrated)
    before = _row(migrated, D_NEXT, "seed")
    _route(CARRIED_SHORT_DAY2, D_NEXT)
    seed_inputs, seed_derived = _row(migrated, D_NEXT, "seed")
    assert (seed_inputs, seed_derived) == before
    assert seed_inputs["stated_book_id"] == stated.id and seed_derived["stated_differs"] == [pos.trade_id]
    assert _stated_rows(migrated) == books


@requires_db
def test_the_current_statement_is_the_one_compared(migrated, weekday_calendar):
    """A restatement (`supersedes`) made before D is recorded is the one
    R51 compares; the first statement stays history, never compared."""
    first = _state(D_NEXT)
    _route(HHH_ROUND, D_NEXT)
    second = _state(D_NEXT, positions=[GGG_SHORT], supersedes=first.id)
    _state(D)
    books = _stated_rows(migrated)
    _route(CARRIED_SHORT_DAY1, D)
    seed_inputs, seed_derived = _row(migrated, D_NEXT, "seed")
    assert seed_inputs["stated_book_id"] == second.id and seed_derived["stated_differs"] == []
    assert DrcStore().stated_difference(D_NEXT) is None
    assert _stated_rows(migrated) == books


@requires_db
def test_three_days_re_pair_in_date_order_each_from_the_new_close(migrated, weekday_calendar):
    _state(D_NEXT)
    _route(HHH_ROUND, D_NEXT)
    _route(EEE_ROUND, D3)
    _state(D)
    books = _stated_rows(migrated)
    pairing, _, _ = _route(CARRIED_SHORT_DAY1, D)
    (pos,) = pairing.open_positions
    _, day_row = _row(migrated, D, "day")
    assert day_row["repaired"] == ["2001-01-03", "2001-01-04"]
    _, close_n = _row(migrated, D_NEXT, "book_close")
    assert close_n["trade_ids"] == [pos.trade_id]
    seed3, _ = _row(migrated, D3, "seed")
    assert seed3["source"] == "carried" and seed3["from_book_sha256"] == close_n["book_sha256"]
    _, close3 = _row(migrated, D3, "book_close")
    assert close3["trade_ids"] == [pos.trade_id]
    assert _stated_rows(migrated) == books


# ---------------------------------------------------------------------
# THE FORWARD RE-PAIR on a superseding file (`[F-03]`)
# ---------------------------------------------------------------------


@requires_db
def test_a_failing_third_day_writes_nothing_on_any_day(migrated, weekday_calendar):
    _day1_carrying_ddd()
    _route(EEE_ROUND, D_NEXT)
    _route(DDD_COVER, D3)
    before = [_snapshot(migrated, d) for d in (D, D_NEXT, D3)]
    with pytest.raises(PairingError, match="the forward re-pair of 2001-01-04 failed"):
        _route(D_FLAT, D)
    assert [_snapshot(migrated, d) for d in (D, D_NEXT, D3)] == before


@requires_db
def test_a_later_no_trade_day_re_pairs_as_a_no_trade_carry(migrated, weekday_calendar):
    _day1_carrying_ddd()
    no_trade = _state(D_NEXT, kind="no_trade")
    assert DrcStore().rebuild(D_NEXT) == [D_NEXT]
    pairing, _, _ = _route(D_DDD_LATER, D)
    (pos,) = pairing.open_positions
    seed_inputs, _ = _row(migrated, D_NEXT, "seed")
    assert seed_inputs["source"] == "no_trade_carry" and seed_inputs["no_trade_id"] == no_trade.id
    _, close = _row(migrated, D_NEXT, "book_close")
    assert close["trade_ids"] == [pos.trade_id]


@requires_db
def test_a_pre_lane_day_is_rebuilt_and_the_next_day_then_carries(migrated, weekday_calendar):
    """v3 §4 row 4's remedy, `rebuild <P>`: a `day` row with no
    `book_close` (inserted as a pre-lane build left it)."""
    _state(D)
    _import(DAY1.read_bytes(), D)
    with DrcStore()._connect() as conn:
        conn.execute(
            "INSERT INTO drc_rows (day, kind, ref, inputs, derived, fn_version) "
            "VALUES (%s, 'day', 'day', '{}', %s, 'drc.pairing/1')",
            (D, Jsonb({"trades": 2, "open_positions": 1, "unmatched": 0, "not_computed": {}})),
        )
    with pytest.raises(PairingError, match="rebuild 2001-01-02"):
        DrcStore().seed_for(D_NEXT)
    assert DrcStore().rebuild(D) == [D]
    _, close = _row(migrated, D, "book_close")
    assert close["count"] == 1
    book = DrcStore().seed_for(D_NEXT)
    assert book.source == "carried" and [p.symbol for p in book.positions] == ["DDD"]


# ---------------------------------------------------------------------
# THE NOT-COMPUTED STOP (C4)
# ---------------------------------------------------------------------


@requires_db
def test_a_not_computed_prior_keeps_the_later_day_and_its_seed_still_fails(migrated, weekday_calendar):
    """K2 fix r1 F-2: the later day's rows are unchanged but for the
    `book_stale` mark its own `day` row now carries."""
    _state(D_NEXT)
    _route(CARRIED_SHORT_DAY2, D_NEXT)
    books = _stated_rows(migrated)
    before = _snapshot(migrated, D_NEXT)
    _route(CARRIED_SHORT_DAY1, D)
    assert _without_stale(_snapshot(migrated, D_NEXT)) == before
    assert _row(migrated, D_NEXT, "day")[1]["book_stale"] == {"root": "2001-01-02", "reason": _NOT_COMPUTED_PRIOR}
    _, day_row = _row(migrated, D, "day")
    assert [n["day"] for n in day_row["not_repaired"]] == ["2001-01-03"]
    with pytest.raises(PairingError, match="2001-01-02 has pairing not computed"):
        DrcStore().seed_for(D_NEXT)
    assert _stated_rows(migrated) == books


# ---------------------------------------------------------------------
# `[F-05]` — the no-trade input
# ---------------------------------------------------------------------


@requires_db
def test_a_day_with_no_trading_log_needs_its_no_trade_row(migrated, weekday_calendar):
    _day1_carrying_ddd()
    store = DrcStore()
    book = store.seed_for(D_NEXT)
    pairing = pair_day([], D_NEXT, book.positions)
    with pytest.raises(ValueError, match="no-trade"):
        store.record_day(pairing, {}, book)
    assert migrated.execute(
        'SELECT count(*) FROM "user".drc_rows WHERE day = %s', (D_NEXT,)
    ).fetchone()[0] == 0
    with pytest.raises(PairingError, match=r"nothing to re-pair \(\[F-05\]\)"):
        store.rebuild(D_NEXT)
    no_trade = _state(D_NEXT, kind="no_trade")
    store.record_day(pairing, {}, book)
    day_inputs, _ = _row(migrated, D_NEXT, "day")
    assert day_inputs["no_trade_id"] == no_trade.id


# ---------------------------------------------------------------------
# `[F-06]` — RESOLVE
# ---------------------------------------------------------------------


@requires_db
def test_a_resolve_with_an_exit_price_and_time_realizes_the_fifo_figure(migrated, weekday_calendar):
    (pos,) = _day1_carrying_ddd().open_positions
    resolve = _state(D_NEXT, kind="resolve", positions=[
        {"trade_id": pos.trade_id, "exit_price": "31.1", "exit_time": "2001-01-03T15:00:00-05:00"},
    ])
    _route(EEE_ROUND, D_NEXT)
    inputs, derived = _trade(migrated, D_NEXT, pos.trade_id)
    assert inputs["resolve_id"] == resolve.id
    assert derived["gross_pnl"] == "30.0" and len(derived["legs"]) == 1
    _, day_row = _row(migrated, D_NEXT, "day")
    assert [(o["resolve_id"], o["status"]) for o in day_row["resolves"]] == [(resolve.id, "applied")]


@requires_db
def test_an_export_touching_the_symbol_supersedes_the_resolve(migrated, weekday_calendar):
    (pos,) = _day1_carrying_ddd().open_positions
    resolve = _state(D_NEXT, kind="resolve", positions=[{"trade_id": pos.trade_id}])
    _route(DDD_COVER, D_NEXT)
    inputs, derived = _trade(migrated, D_NEXT, pos.trade_id)
    assert "resolve_id" not in inputs and derived["gross_pnl"] == "21.0"
    _, day_row = _row(migrated, D_NEXT, "day")
    assert day_row["resolves"] == [{
        "resolve_id": resolve.id,
        "trade_id": pos.trade_id,
        "status": "superseded",
        "reason": "superseded — 2001-01-03's export touches DDD (R67: the export is the truth)",
    }]


@requires_db
def test_a_resolve_of_a_trade_an_earlier_export_closed_is_superseded(migrated, weekday_calendar):
    (pos,) = _day1_carrying_ddd().open_positions
    _route(DDD_COVER, D_NEXT)
    resolve = _state(D3, kind="resolve", positions=[{"trade_id": pos.trade_id}])
    _route(EEE_ROUND, D3)
    _, day_row = _row(migrated, D3, "day")
    assert day_row["resolves"] == [{
        "resolve_id": resolve.id,
        "trade_id": pos.trade_id,
        "status": "superseded",
        "reason": "superseded — closed by the export of 2001-01-03",
    }]


@requires_db
def test_a_resolve_of_a_trade_no_book_held_fails(migrated, weekday_calendar):
    _day1_carrying_ddd()
    resolve = _state(D_NEXT, kind="resolve", positions=[{"trade_id": "ZZZ-long-constructed"}])
    with pytest.raises(PairingError, match=rf"resolve #{resolve.id} names ZZZ-long-constructed"):
        DrcStore().seed_for(D_NEXT)


@requires_db
def test_a_resolve_for_a_recorded_day_is_applied_by_its_rebuild(migrated, weekday_calendar):
    """`[F-06]`: "The close runs the Q3 forward re-pair so no later
    `book_close` still contains that `trade_id`"."""
    (pos,) = _day1_carrying_ddd().open_positions
    _route(EEE_ROUND, D_NEXT)
    _route(HHH_ROUND, D3)
    resolve = _state(D_NEXT, kind="resolve", positions=[{"trade_id": pos.trade_id}])
    books = _stated_rows(migrated)
    assert DrcStore().rebuild(D_NEXT) == [D_NEXT, D3]
    inputs, derived = _trade(migrated, D_NEXT, pos.trade_id)
    assert inputs["resolve_id"] == resolve.id and derived["gross_pnl"] == EXIT_NOT_IN_ANY_EXPORT
    held = migrated.execute(
        """SELECT day FROM "user".drc_rows WHERE kind = 'book_close' AND derived->'trade_ids' ? %s""",
        (pos.trade_id,),
    ).fetchall()
    assert held == [(D,)]
    assert _stated_rows(migrated) == books


@requires_db
def test_a_resolve_dated_before_the_day_still_held_names_its_rebuild(migrated, weekday_calendar):
    (pos,) = _day1_carrying_ddd().open_positions
    _route(EEE_ROUND, D_NEXT)
    resolve = _state(D_NEXT, kind="resolve", positions=[{"trade_id": pos.trade_id}])
    with pytest.raises(PairingError, match=rf"resolve #{resolve.id} for .* dated 2001-01-03 is not applied — rebuild 2001-01-03"):
        DrcStore().seed_for(D3)


@requires_db
def test_two_current_resolves_for_one_trade_fail_naming_both(migrated, weekday_calendar):
    """`40` ESCALATE 4 / v3 §4 row 15: the store filters on `day`, so both
    are stored; the reader FAILS naming both ids. The writer refuses the
    second row since K2 fix r1 F-1; the reader's FAIL is the guard for a
    row no caller can write."""
    (pos,) = _day1_carrying_ddd().open_positions
    first = _state(D_NEXT, kind="resolve", positions=[{"trade_id": pos.trade_id}])
    with DrcStore()._connect() as conn:
        second = _stated(conn.execute(
            f"""INSERT INTO drc_stated_books (day, kind, positions, book_sha256, via, reason)
                SELECT %s, kind, positions, book_sha256, via, reason FROM drc_stated_books
                 WHERE id = %s RETURNING {_STATED_COLUMNS}""",
            (D3, first.id),
        ).fetchone())
    _state(D_NEXT, kind="no_trade")
    both = rf"#{first.id}.*#{second.id}"
    with pytest.raises(PairingError, match=both):
        DrcStore().seed_for(D_NEXT)
    with pytest.raises(PairingError, match=both):
        DrcStore().rebuild(D_NEXT)


# ---------------------------------------------------------------------
# THE H3 ROW (`48` seam (2))
# ---------------------------------------------------------------------


@requires_db
def test_an_unpaired_day_is_paired_by_its_rebuild_once_stated(migrated, weekday_calendar):
    pairing, _, book = _route(DAY1.read_bytes(), D)
    assert book is None and "pairing" in pairing.not_computed
    stated = _state(D)
    books = _stated_rows(migrated)
    assert DrcStore().rebuild(D) == [D]
    seed_inputs, _ = _row(migrated, D, "seed")
    assert seed_inputs["source"] == "stated" and seed_inputs["stated_book_id"] == stated.id
    assert _row(migrated, D, "book_close")[1]["count"] == 1
    assert DrcStore().seed_for(D_NEXT).source == "carried"
    assert _stated_rows(migrated) == books


# ---------------------------------------------------------------------
# `stated_difference` (C6)
# ---------------------------------------------------------------------


@requires_db
def test_no_difference_line_without_a_differing_statement(migrated, weekday_calendar):
    store = DrcStore()
    assert store.stated_difference(D) is None
    _day1_carrying_ddd()
    assert store.stated_difference(D) is None  # a stated-source day
    _route(DDD_COVER, D_NEXT)
    assert store.stated_difference(D_NEXT) is None  # carried, no statement


# ---------------------------------------------------------------------
# The CLI (C7, R52)
# ---------------------------------------------------------------------


@requires_db
def test_the_cli_no_trade_apply_rebuilds_the_day(migrated, capsys, at_ten, weekday_calendar, monkeypatch):
    # D2 fix r1 (S-1): `--no-trade --apply` now runs the day's file-less
    # event through `imports.no_trade_event`, which exits non-zero on a
    # failed event; D3's entry is stubbed to return so this test keeps
    # proving the rebuild (every assertion below unchanged).
    import sys
    import types

    build = types.ModuleType("cobalt.drc.build")
    build.run_drc_build = lambda event: "constructed/DRC-note.md"
    monkeypatch.setitem(sys.modules, "cobalt.drc.build", build)
    _day1_carrying_ddd()
    before = _stated_count(migrated)
    code, out = _cli(capsys, "--no-trade", "2001-01-03")
    assert code == 0 and "on --apply: rebuild 2001-01-03 and every later recorded day" in out
    assert _stated_count(migrated) == before and _row(migrated, D_NEXT, "day") is None
    code, out = _cli(capsys, "--no-trade", "2001-01-03", "--apply", "--sha256", _printed_hash(out))
    assert code == 0, out
    assert "rebuilt: 2001-01-03" in out
    assert _stated_count(migrated) == before + 1
    assert _row(migrated, D_NEXT, "seed")[0]["source"] == "no_trade_carry"


@requires_db
def test_the_cli_resolve_keeps_the_row_when_its_rebuild_is_refused(migrated, capsys, at_ten, weekday_calendar):
    _day1_carrying_ddd()
    _state(D_NEXT, kind="no_trade")
    before = _stated_count(migrated)
    argv = ("--resolve", "2001-01-03", "ZZZ-long-constructed")
    code, out = _cli(capsys, *argv)
    assert code == 0 and "on --apply: rebuild 2001-01-03" in out
    code, out = _cli(capsys, *argv, "--apply", "--sha256", _printed_hash(out))
    assert code != 0
    assert "names ZZZ-long-constructed" in out
    assert _stated_count(migrated) == before + 1


@requires_db
def test_the_cli_opening_without_an_import_says_so(migrated, capsys, at_ten, weekday_calendar):
    code, out = _cli(capsys, "--opening", "2001-01-02", "--flat")
    assert code == 0 and "on --apply" not in out
    code, out = _cli(capsys, "--opening", "2001-01-02", "--flat", "--apply", "--sha256", _printed_hash(out))
    assert code == 0, out
    assert "stated; 2001-01-02 has no import yet" in out


@requires_db
def test_the_cli_opening_for_an_imported_unpaired_day_rebuilds_it(migrated, capsys, at_ten, weekday_calendar):
    _route(DAY1.read_bytes(), D)
    code, out = _cli(capsys, "--opening", "2001-01-02", "--flat")
    assert "on --apply: rebuild 2001-01-02 and every later recorded day" in out
    code, out = _cli(capsys, "--opening", "2001-01-02", "--flat", "--apply", "--sha256", _printed_hash(out))
    assert code == 0, out
    assert "rebuilt: 2001-01-02" in out
    assert _row(migrated, D, "book_close")[1]["count"] == 1
