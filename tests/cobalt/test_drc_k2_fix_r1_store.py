"""DRC K2 fix r1 — WITH-DB half (L75; the fix prompt
`prompts/2026-09-25/02-drc-k2-fix-r1-build.md` F3).

The store halves of F-1…F-5, each red on `09ce3742`, each naming `52`'s
`## Checked against the branch` row (`drc-k2-check-2026-09-24.md`):
F-1 the resolve's key is its trade id on any day (`:159`); F-2 a stopped
chain marks every later day on its OWN rows (`:160`, `:163`, `:165`);
F-3 `record_day` and `rebuild` store one no-trade seed (`:161`); F-4 a
paired day never stores "pairing did not run" (`:162`); F-5 one
partial-import rule (`:164`).

Everything runs inside `test_drc_store.py`'s never-committed migration
transaction on `cobalt_dev` (L76). Every statement passes the constructed
10:00 ET clock. `drc_stated_books` is written only by
`record_stated_book`; every rebuild is proven to change none of it (L7).
Constructed symbols and dates only (L32 / L45).
"""

from __future__ import annotations

import json
from datetime import date

import pytest

from cobalt.drc import trading_log
from cobalt.drc.models import Kind, PairingError
from cobalt.drc.pairing import pair_day
from cobalt.drc.store import DrcStore

from test_drc_k1_store import (  # noqa: F401 — fixtures are used by name
    D3,
    TEN_ET,
    _cli,
    _day1_carrying_ddd,
    _printed_hash,
    _stated_count,
    _state,
    at_ten,
)
from test_drc_k2_experiments import (
    _NOT_COMPUTED_PRIOR,
    EEE_ROUND,
    HHH_ROUND,
    _drop_column,
    _one_row_stats,
    _record_with_stats,
    _route,
    _row,
    _snapshot,
    _stated_rows,
)
from test_drc_pairing import CARRIED_SHORT_DAY1, CARRIED_SHORT_DAY2
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    DAY1,
    SEED,
    migrated,
    requires_db,
    weekday_calendar,
)

#: A constructed weekday under `weekday_calendar` (`51` S2's list).
D4 = date(2001, 1, 5)
STALE = {"root": "2001-01-02", "reason": _NOT_COMPUTED_PRIOR}


def _without_stale(snapshot):
    """A `_snapshot` with `book_stale` removed from its `day` row."""
    out = []
    for kind, ref, inputs, derived in snapshot:
        if kind == "day":
            d = json.loads(derived)
            d.pop("book_stale", None)
            derived = json.dumps(d, sort_keys=True)
        out.append((kind, ref, inputs, derived))
    return sorted(out)


def _rows_of(conn, day: date):
    return conn.execute(
        'SELECT kind, ref, inputs, derived FROM "user".drc_rows WHERE day = %s', (day,)
    ).fetchall()


# ---------------------------------------------------------------------
# F-1 — the resolve's key is its trade id, on any day (`:159`)
# ---------------------------------------------------------------------


def _resolve_applied_on_d_next():
    """D records `DDD 30` open; D_NEXT is a no-trade day whose resolve of
    that trade is applied by its rebuild; D3 is recorded from D_NEXT's
    close with a file that does not touch `DDD`."""
    (pos,) = _day1_carrying_ddd().open_positions
    _state(D_NEXT, kind="no_trade")
    first = _state(D_NEXT, kind="resolve", positions=[{"trade_id": pos.trade_id}])
    assert DrcStore().rebuild(D_NEXT) == [D_NEXT]
    _route(EEE_ROUND, D3)
    return pos.trade_id, first


@requires_db
def test_a_second_current_resolve_for_one_trade_on_another_day_is_refused(migrated, weekday_calendar):
    """F-1, `drc-k2-check-2026-09-24.md:159` (v3 `[F-01]` `:126`, `:134`):
    a second current resolve naming the same trade on ANOTHER day is
    refused, naming the current row and its day; nothing written."""
    (pos,) = _day1_carrying_ddd().open_positions
    first = _state(D_NEXT, kind="resolve", positions=[{"trade_id": pos.trade_id}])
    before = _stated_count(migrated)
    with pytest.raises(ValueError, match=rf"#{first.id} \(2001-01-03\)"):
        _state(D3, kind="resolve", positions=[{"trade_id": pos.trade_id}])
    assert _stated_count(migrated) == before


@requires_db
def test_a_resolve_restated_on_another_day_supersedes_and_rebuilds_from_the_earlier_day(migrated, weekday_calendar):
    """F-1, `drc-k2-check-2026-09-24.md:159` (v3 `[F-06]` `:190`; R52
    `--supersedes`): a resolve restated on a later day supersedes across
    days; the rebuild runs from the earlier day, so the superseded
    resolve's effect leaves every stored row (L1)."""
    trade, first = _resolve_applied_on_d_next()
    second = _state(D3, kind="resolve", positions=[{"trade_id": trade}], supersedes=first.id)
    assert DrcStore().effect_day(D3, first.id) == D_NEXT
    books = _stated_rows(migrated)
    assert DrcStore().rebuild(D_NEXT) == [D_NEXT, D3]
    assert _stated_rows(migrated) == books

    assert trade in _row(migrated, D_NEXT, "book_close")[1]["trade_ids"]
    inputs, derived = migrated.execute(
        """SELECT inputs, derived FROM "user".drc_rows WHERE day = %s AND kind = 'trade' AND ref = %s""",
        (D3, trade),
    ).fetchone()
    assert derived["status"] == "closed" and inputs["resolve_id"] == second.id
    for day in (D_NEXT, D3):
        for _, _, i, d in _rows_of(migrated, day):
            assert i.get("resolve_id") != first.id
            assert all(o["resolve_id"] != first.id for o in d.get("resolves", []))


@requires_db
def test_the_cli_restatement_rebuilds_from_the_superseded_rows_day(migrated, capsys, at_ten, weekday_calendar):
    """F-1, `drc-k2-check-2026-09-24.md:159` (AMENDED C7): the CLI's
    `--resolve … --supersedes` names and runs the rebuild from
    `effect_day`, the superseded row's earlier day."""
    trade, first = _resolve_applied_on_d_next()
    books = _stated_count(migrated)
    argv = ("--resolve", "2001-01-04", trade, "--supersedes", str(first.id))
    code, out = _cli(capsys, *argv)
    assert code == 0 and "on --apply: rebuild 2001-01-03 and every later recorded day" in out
    code, out = _cli(capsys, *argv, "--apply", "--sha256", _printed_hash(out))
    assert code == 0, out
    assert "rebuilt: 2001-01-03, 2001-01-04" in out
    assert _stated_count(migrated) == books + 1


# ---------------------------------------------------------------------
# F-2 — a stopped chain marks every later day on its OWN rows
# (`:160`, `:163`, `:165`)
# ---------------------------------------------------------------------


def _stopped_chain(conn):
    """D_NEXT stated and recorded (a `GGG` buy), D3 recorded from its
    close (a file that does not touch `GGG`); then D recorded `not
    computed` (no statement for D). Returns the later days' snapshots
    taken before D; recording D changes no statement (L7)."""
    _state(D_NEXT)
    _route(CARRIED_SHORT_DAY2, D_NEXT)
    _route(HHH_ROUND, D3)
    before = {d: _snapshot(conn, d) for d in (D_NEXT, D3)}
    books = _stated_rows(conn)
    pairing, _, book = _route(CARRIED_SHORT_DAY1, D)
    assert book is None and "pairing" in pairing.not_computed
    assert _stated_rows(conn) == books
    return before


@requires_db
def test_every_later_day_of_a_stopped_chain_carries_the_stale_mark_and_fails_its_successor(migrated, weekday_calendar):
    """F-2, `drc-k2-check-2026-09-24.md:160`, `:163`, `:165` (L1; v3 §4
    `:214`, `:232`; L72): every day named in `not_repaired` carries
    `derived.book_stale` on its OWN `day` row, nothing else of it changes,
    and `seed_for` of the day after ANY stale day FAILS naming the root."""
    before = _stopped_chain(migrated)

    _, day_row = _row(migrated, D, "day")
    assert [n["day"] for n in day_row["not_repaired"]] == ["2001-01-03", "2001-01-04"]
    for d in (D_NEXT, D3):
        assert _row(migrated, d, "day")[1]["book_stale"] == STALE
        assert _without_stale(_snapshot(migrated, d)) == before[d]

    with pytest.raises(PairingError, match="2001-01-02 has pairing not computed"):
        DrcStore().seed_for(D_NEXT)
    with pytest.raises(PairingError, match=r"2001-01-04.*stale.*2001-01-02") as e:
        DrcStore().seed_for(D4)
    assert "2001-01-02" in str(e.value) and "stale" in str(e.value)
    with pytest.raises(PairingError, match=r"2001-01-03.*2001-01-02"):
        DrcStore().seed_for(D3)


@requires_db
def test_the_stale_mark_leaves_when_the_root_is_stated_and_rebuilt(migrated, weekday_calendar):
    """F-2, `drc-k2-check-2026-09-24.md:160`: once the root's book is
    stated and rebuilt, the forward re-pair rewrites every later day whole
    — the mark leaves with the stale book."""
    _stopped_chain(migrated)
    for d in (D_NEXT, D3):
        assert _row(migrated, d, "day")[1]["book_stale"] == STALE
    _state(D)
    books = _stated_rows(migrated)
    assert DrcStore().rebuild(D) == [D, D_NEXT, D3]
    assert _stated_rows(migrated) == books
    for d in (D_NEXT, D3):
        assert "book_stale" not in _row(migrated, d, "day")[1]
    book = DrcStore().seed_for(D4)
    assert book.source == "carried" and book.from_day == D3


# ---------------------------------------------------------------------
# F-3 — one no-trade seed rule (`:161`)
# ---------------------------------------------------------------------


@requires_db
def test_a_no_trade_day_recorded_by_record_day_stores_the_no_trade_carry(migrated, weekday_calendar):
    """F-3, `drc-k2-check-2026-09-24.md:161` (L3; v3 §2b `:97`, `[F-05]`
    `:99`): `record_day` stores the no-trade day's seed exactly as
    `rebuild` does, so an unchanged no-trade day re-pairs identical (A1)."""
    _day1_carrying_ddd()
    nt = _state(D_NEXT, kind="no_trade")
    store = DrcStore()
    book = store.seed_for(D_NEXT)
    store.record_day(pair_day([], D_NEXT, book.positions), {}, book)
    seed_inputs, _ = _row(migrated, D_NEXT, "seed")
    assert seed_inputs["source"] == "no_trade_carry" and seed_inputs["no_trade_id"] == nt.id
    before = _snapshot(migrated, D_NEXT)
    books = _stated_rows(migrated)
    store.rebuild(D)
    assert _snapshot(migrated, D_NEXT) == before
    assert _stated_rows(migrated) == books


# ---------------------------------------------------------------------
# F-4 — a paired day never stores "pairing did not run" (`:162`)
# ---------------------------------------------------------------------


@requires_db
def test_an_unpaired_day_with_a_stats_log_is_re_matched_when_it_is_paired(migrated, weekday_calendar):
    """F-4, `drc-k2-check-2026-09-24.md:162` (A1 `:179`, a DESK READING of
    R51: "Re-run `match_stats` … from those stored rows against the new
    pairing"): a first import with a stats log stores `pairing did not
    run` (true); once stated and rebuilt, its stats row is re-matched.

    The kept-match case stays a GREEN-as-pin:
    `test_drc_k2_experiments.py:397` `test_x9_pass_c_a_not_computed_match_is_kept`."""
    stats_bytes = _one_row_stats("DDD", "long", D, "10:00:00 EST")
    pairing, book = _record_with_stats(DAY1.read_bytes(), stats_bytes, D)
    assert book is None
    _, day_row = _row(migrated, D, "day")
    assert day_row["not_computed"]["match"] == "not computed — pairing did not run"

    _state(D)
    books = _stated_rows(migrated)
    assert DrcStore().rebuild(D) == [D]
    assert _stated_rows(migrated) == books
    (ddd,) = [
        r[0]
        for r in migrated.execute(
            """SELECT ref FROM "user".drc_rows WHERE day = %s AND kind = 'trade' AND ref LIKE 'DDD-%%'""",
            (D,),
        ).fetchall()
    ]
    stats = migrated.execute(
        """SELECT derived->>'match', derived->>'trade_id' FROM "user".drc_rows
           WHERE day = %s AND kind = 'stats_row'""",
        (D,),
    ).fetchall()
    assert stats == [("matched", ddd)]
    _, day_row = _row(migrated, D, "day")
    assert "match" not in day_row["not_computed"]


# ---------------------------------------------------------------------
# F-5 — one partial-import rule (`:164`)
# ---------------------------------------------------------------------


@requires_db
def test_a_partial_file_missing_only_a_non_pairing_column_stays_paired_through_a_re_pair(migrated, weekday_calendar):
    """F-5, `drc-k2-check-2026-09-24.md:164` (v3 `:181` "exactly as its
    first record did", `FR14`; L3): a partial file missing only a column
    pairing does not read is paired at its first record and stays paired
    through every re-pair — never un-paired, `book_close` kept."""
    assert trading_log.ACCOUNT not in trading_log.PAIRING_INPUTS
    _day1_carrying_ddd()
    half = _drop_column(SEED.read_bytes(), trading_log.ACCOUNT)
    _, ids, _ = _route(half, D_NEXT, "half.md")
    assert migrated.execute(
        'SELECT parse_status FROM "user".drc_imports WHERE id = %s', (ids[Kind.TRADING_LOG],)
    ).fetchone()[0] == "partial"
    assert _row(migrated, D_NEXT, "book_close") is not None
    before = _snapshot(migrated, D_NEXT)
    books = _stated_rows(migrated)
    DrcStore().rebuild(D)
    assert _snapshot(migrated, D_NEXT) == before
    assert _stated_rows(migrated) == books
