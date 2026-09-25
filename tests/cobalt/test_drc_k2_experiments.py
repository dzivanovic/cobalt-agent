"""DRC K2 — the first-gate experiments X7–X11 (v3 `## First-gate
experiments (L70)`, "Before K2"), run BEFORE any K2 code. X12 is a
hub-run read of one of his own files (v3 `:306`, `:328`): not run here.

Each X has a GATE and a PASS test:

- a GATE test runs on the code as it stands (the fact the design rests
  on). X7's, X8's and X9's stay green after K2. X10's and X11's were
  facts of the BASE that K2 replaces by design (the case (iv) raise; the
  `IndexError` of a CLOSED book with no exits): they ran at S2, their
  results are in the build report, and they were removed with the K2
  code (their placeholders below say so).
- a PASS test states v3's pass condition against THE K2 CONTRACT of the
  build prompt. Every K2 symbol is imported INSIDE the test body, so each
  is its own red until the K2 code exists.

Constructed symbols and dates only (L32 / L45): trading-log bytes are
written inline with `trading_log_carry_day1.csv`'s header and row shape.
WITH-DB tests run inside `test_drc_store.py`'s never-committed migration
transaction (L76): nothing here commits a migration.
"""

from __future__ import annotations

import csv
import io
import json
from datetime import date

import psycopg
import pytest

from cobalt.drc import stats_log
from cobalt.drc.detect import detect_kind
from cobalt.drc.models import Direction, Kind, PairingError, TradeStatus
from cobalt.drc.pairing import book_sha256, pair_day
from cobalt.drc.stats_log import StatsLogSource
from cobalt.drc.store import DrcStore
from cobalt.drc.trading_log import TradingLogSource

from test_drc_k1_store import D3, GGG_SHORT, _day1_carrying_ddd, _row, _state
from test_drc_pairing import CARRIED_SHORT_DAY1, CARRIED_SHORT_DAY2, STATS, _header, _set_stats_cell
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

EXIT_NOT_IN_ANY_EXPORT = "not computed — exit not in any export"
_NOT_COMPUTED_PRIOR = "2001-01-02 has pairing not computed — its open positions are unknown"

HEADER = _header(DAY1)


def _log(*rows: str) -> bytes:
    """A constructed trading log: the fixture's header, then `rows`
    (newest first, as the export writes them)."""
    return HEADER + "".join(f"{r}\n" for r in rows).encode()


#: The next day's file sells the carried `DDD 30` (a cover of the carry).
DDD_COVER = _log("09:35:00,DDD,S,30.8,30,ROUTE1,BRK1,ACCT1,Margin,H0000000000401,")
#: A superseding day-1 file that leaves NOTHING open.
D_FLAT = _log(
    "10:30:00,DDD,S,30.5,50,ROUTE1,BRK1,ACCT1,Margin,H0000000000403,",
    "10:00:00,DDD,B,30.1,50,ROUTE2,BRK2,ACCT1,Margin,H0000000000402,",
)
#: A superseding day-1 file that leaves `DDD 30` open at another entry time.
D_DDD_LATER = _log("10:05:00,DDD,B,30.2,30,ROUTE2,BRK2,ACCT1,Margin,H0000000000404,")
#: A day that never touches `DDD` or `GGG`: one closed `EEE` round trip.
EEE_ROUND = _log(
    "09:50:30,EEE,S,40.25,15,ROUTE1,BRK1,ACCT1,Margin,H0000000000406,",
    "09:45:00,EEE,B,40.0,15,ROUTE2,BRK2,ACCT1,Margin,H0000000000405,",
)
#: A day that never touches `GGG`: one closed `HHH` round trip.
HHH_ROUND = _log(
    "09:50:00,HHH,S,11.5,10,ROUTE1,BRK1,ACCT1,Margin,H0000000000408,",
    "09:45:00,HHH,B,11.0,10,ROUTE2,BRK2,ACCT1,Margin,H0000000000407,",
)


def _parse(data: bytes, day: date, name: str = "t.md"):
    return TradingLogSource().parse(data, day, detect_kind(name, data))


def _import(data: bytes, day: date, name: str = "t.md"):
    """Store one trading log for `day` (its import row commits first,
    `[F-25]`); returns the parse and the import ids."""
    parsed = _parse(data, day, name)
    ids = {Kind.TRADING_LOG: DrcStore().record_import(day, parsed.result, data, parsed.executions)}
    return parsed, ids


def _apply(parsed, ids, day: date, stats=None):
    """The route shape of `## SEAM FOR D2` (1)–(3), as K2 amends it:
    `seed_for` → `build_day(…, resolves=book.resolves)` → `record_day`."""
    from cobalt.drc.pairing import build_day

    store = DrcStore()
    book = store.seed_for(day)
    pairing = build_day(
        parsed,
        stats,
        seed=None if book is None else book.positions,
        resolves=() if book is None else book.resolves,
    )
    store.record_day(pairing, ids, book)
    return pairing, book


def _route(data: bytes, day: date, name: str = "t.md"):
    parsed, ids = _import(data, day, name)
    pairing, book = _apply(parsed, ids, day)
    return pairing, ids, book


def _snapshot(conn, day: date) -> list[tuple[str, str, str, str]]:
    """Every `drc_rows` row of `day` as `(kind, ref, inputs, derived)` —
    ids, `created_at` and `fn_version` excluded."""
    return sorted(
        (kind, ref, json.dumps(i, sort_keys=True), json.dumps(d, sort_keys=True))
        for kind, ref, i, d in conn.execute(
            'SELECT kind, ref, inputs, derived FROM "user".drc_rows WHERE day = %s', (day,)
        ).fetchall()
    )


def _fn_versions(conn, day: date) -> list[str]:
    return [
        r[0]
        for r in conn.execute(
            'SELECT DISTINCT fn_version FROM "user".drc_rows WHERE day = %s ORDER BY 1', (day,)
        ).fetchall()
    ]


def _stated_rows(conn) -> list[tuple]:
    return conn.execute('SELECT * FROM "user".drc_stated_books ORDER BY id').fetchall()


def _current_import(conn, day: date, kind: str = "trading_log") -> list[int]:
    return [
        r[0]
        for r in conn.execute(
            """SELECT id FROM "user".drc_imports WHERE import_date = %s AND kind = %s
               AND id NOT IN (SELECT supersedes FROM "user".drc_imports WHERE supersedes IS NOT NULL)""",
            (day, kind),
        ).fetchall()
    ]


def _one_row_stats(symbol: str, side: str, day: date, open_time: str) -> bytes:
    """`stats_log_e1.csv`'s header and first row, its symbol / side / open
    cells set to a constructed trade (the fixture's own shape, L45)."""
    data = b"".join(STATS.read_bytes().splitlines(keepends=True)[:2])
    for column, value in (
        (stats_log.SYMBOL, symbol),
        ("Instrument", symbol),
        (stats_log.SIDE, side),
        (stats_log.OPEN_DATE, day.isoformat()),
        (stats_log.OPEN_TIME, open_time),
        ("Close Date", day.isoformat()),
    ):
        data = _set_stats_cell(data, 2, column, value)
    return data


def _drop_column(data: bytes, column: str) -> bytes:
    """The same file with one named column removed (a `partial` file)."""
    records = list(csv.reader(io.StringIO(data.decode(), newline="")))
    i = records[0].index(column)
    out = io.StringIO()
    csv.writer(out, lineterminator="\n", quoting=csv.QUOTE_MINIMAL).writerows(
        [r[:i] + r[i + 1:] for r in records if r]
    )
    return out.getvalue().encode()


# ---------------------------------------------------------------------
# X7 — v3 `:323`
# ---------------------------------------------------------------------


@requires_db
def test_x7_gate_record_day_is_one_transaction(migrated, weekday_calendar, monkeypatch):
    """X7 (v3 `:323`): "Proposal read-back (3), both halves: re-import day 1
    with a file that closes the swing while day 2's re-pair fails (day 1's
    and day 2's old `drc_rows` both present, import FAILED naming day 2);
    then every day pairs, the database commits, and the day-2 note upsert
    fails (database has the new hashes, day-2 unit stale, `/drc` shows the
    database book)." Result that changes the design: "any day
    half-replaced, or the page showing the old note, or the database
    rolling back with the note → `[F-03]`'s one-transaction / stale-mark
    shape changes". GATE: `record_day`'s DELETE and INSERT are one
    transaction today — an insert that raises after the DELETE leaves the
    day's old rows byte-identical."""
    first = _day1_carrying_ddd()
    before = _snapshot(migrated, D)
    assert before

    def _boom(self, *a, **kw):
        raise RuntimeError("x7: injected after the DELETE")

    seed = DrcStore().seed_for(D)
    monkeypatch.setattr(psycopg.Cursor, "executemany", _boom)
    with pytest.raises(RuntimeError, match="injected after the DELETE"):
        DrcStore().record_day(first, {Kind.TRADING_LOG: 1}, seed)
    monkeypatch.undo()
    assert _snapshot(migrated, D) == before


@requires_db
def test_x7_pass_a_failing_forward_re_pair_writes_nothing_then_one_commit_replaces_both(migrated, weekday_calendar):
    """X7 (v3 `:323`) PASS, THE THREE-DAY FAILURE HALF then THE SUCCESS
    HALF (the note half is K3's, L28). Superseding D with a file that
    leaves nothing open makes D_NEXT's re-pair meet a sell with no long:
    `PairingError` naming 2001-01-03, both days' old rows byte-identical,
    the superseding import stored and current (`[F-25]`). Then a file that
    leaves `DDD 30` open at another time: ONE commit replaces D and
    D_NEXT, D_NEXT seeded from D's NEW close."""
    _day1_carrying_ddd()
    _route(DDD_COVER, D_NEXT)
    before_d, before_n = _snapshot(migrated, D), _snapshot(migrated, D_NEXT)

    parsed, ids = _import(D_FLAT, D)
    with pytest.raises(PairingError, match="2001-01-03"):
        _apply(parsed, ids, D)
    assert _snapshot(migrated, D) == before_d
    assert _snapshot(migrated, D_NEXT) == before_n
    assert _current_import(migrated, D) == [ids[Kind.TRADING_LOG]]

    pairing, _, _ = _route(D_DDD_LATER, D)
    (pos,) = pairing.open_positions
    _, close = _row(migrated, D, "book_close")
    assert close["trade_ids"] == [pos.trade_id]
    seed_inputs, _ = _row(migrated, D_NEXT, "seed")
    assert seed_inputs["from_book_sha256"] == close["book_sha256"]
    closed = migrated.execute(
        """SELECT ref, derived->>'status' FROM "user".drc_rows WHERE day = %s AND kind = 'trade'""",
        (D_NEXT,),
    ).fetchall()
    assert closed == [(pos.trade_id, "closed")]
    _, day_row = _row(migrated, D, "day")
    assert day_row["repaired"] == ["2001-01-03"]


# ---------------------------------------------------------------------
# X8 — v3 `:324`
# ---------------------------------------------------------------------


def test_x8_gate_an_empty_day_returns_the_seed_on_the_new_day():
    """X8 (v3 `:324`): "Proposal read-back (5), (6): a no-trade day between
    carries `source: no_trade_carry` and the same `trade_id`; a missing
    trading day FAILs naming it and writes no seed." Result that changes
    the design: "a miss → K2's empty-day record is wrong". GATE:
    `pair_day([], D_NEXT, seed)` returns the one carried position with
    `day == D_NEXT` and the SAME `trade_id`, lots and `opened_on`
    (`[F-21]`: the `day` changes, so the two books' hashes differ — not a
    defect)."""
    _, day1 = _trading(DAY1, D)
    (pos,) = pair_day(day1.executions, D).open_positions
    empty = pair_day([], D_NEXT, [pos])
    (carried,) = empty.open_positions
    assert carried.day == D_NEXT
    assert (carried.trade_id, carried.lots, carried.opened_on) == (pos.trade_id, pos.lots, pos.opened_on)
    assert book_sha256([carried]) != book_sha256([pos])
    (trade,) = empty.trades
    assert trade.status is TradeStatus.OPEN and trade.trade_id == pos.trade_id


@requires_db
def test_x8_pass_a_no_trade_day_carries_the_book_and_a_missing_day_fails(migrated, weekday_calendar):
    """X8 (v3 `:324`) PASS: `_state(D_NEXT, kind="no_trade")` then
    `rebuild(D_NEXT)` → the `day` row names `no_trade_id`, the `seed` row
    is `no_trade_carry` from 2001-01-02, `book_close` holds the same `DDD`
    trade id; D3's file covering `DDD` closes that trade. A fresh chain
    with NOTHING for D_NEXT: `seed_for(D3)` FAILS naming 2001-01-03, and
    no `seed` row exists for D3."""
    migrated.execute("SAVEPOINT x8_fresh")
    day1 = _day1_carrying_ddd()
    (pos,) = day1.open_positions
    no_trade = _state(D_NEXT, kind="no_trade")
    assert DrcStore().rebuild(D_NEXT) == [D_NEXT]
    day_inputs, day_derived = _row(migrated, D_NEXT, "day")
    assert day_inputs["no_trade_id"] == no_trade.id
    assert day_derived["trades"] == 1 and day_derived["open_positions"] == 1
    seed_inputs, _ = _row(migrated, D_NEXT, "seed")
    assert seed_inputs["source"] == "no_trade_carry"
    assert seed_inputs["from_day"] == "2001-01-02"
    _, close = _row(migrated, D_NEXT, "book_close")
    assert close["count"] == 1 and close["trade_ids"] == [pos.trade_id]

    pairing, _, _ = _route(DDD_COVER, D3)
    closed = [t for t in pairing.trades if t.trade_id == pos.trade_id]
    assert [t.status for t in closed] == [TradeStatus.CLOSED]

    migrated.execute("ROLLBACK TO SAVEPOINT x8_fresh")
    _day1_carrying_ddd()
    _import(DDD_COVER, D3)
    with pytest.raises(PairingError, match="2001-01-03"):
        DrcStore().seed_for(D3)
    with pytest.raises(PairingError, match="2001-01-03"):
        DrcStore().rebuild(D3)
    assert _row(migrated, D3, "seed") is None


# ---------------------------------------------------------------------
# X9 — v3 `:325`
# ---------------------------------------------------------------------


@requires_db
def test_x9_gate_a_superseding_import_keeps_both_files_fills_and_is_current(migrated):
    """X9 (v3 `:325`): "Supersede day 1's import, re-pair day 2: day 2's
    executions are the current import's fills only; re-pair an unchanged
    later day from its fills and its stored `stats_row` rows → identical
    `derived` and `inputs`." Result that changes the design: "superseded
    fills paired again (double book), or stats rows only recoverable from
    the kept file bytes → K2 gains a D2 dependency (R2-1 (iii))". GATE:
    both imports' fills stay stored, and the CURRENT import (the id no
    other row supersedes) is the new one — the fact A1 rests on."""
    store = DrcStore()
    data, parsed = _trading(DAY1, D)
    first = store.record_import(D, parsed.result, data, parsed.executions)
    second = store.record_import(D, parsed.result, data, parsed.executions)
    counts = dict(migrated.execute(
        'SELECT import_id, count(*) FROM "user".drc_fills WHERE import_id = ANY(%s) GROUP BY import_id',
        ([first, second],),
    ).fetchall())
    assert counts == {first: 4, second: 4}
    assert _current_import(migrated, D) == [second]


@requires_db
def test_x9_pass_a_b_the_current_fills_only_and_an_unchanged_later_day(migrated, weekday_calendar):
    """X9 (v3 `:325`) PASS (a), (b): superseding D with the SAME book
    re-pairs D_NEXT to byte-identical `(kind, ref, inputs, derived)` rows
    (`fn_version` compared separately); a superseding import of D_NEXT
    itself, not yet recorded, is the one the re-pair reads — its trade
    count is its file's, never doubled, and its `day` row names it."""
    _day1_carrying_ddd()
    _route(SEED.read_bytes(), D_NEXT)
    before, fn_before = _snapshot(migrated, D_NEXT), _fn_versions(migrated, D_NEXT)

    _route(DAY1.read_bytes(), D)
    assert _snapshot(migrated, D_NEXT) == before
    assert _fn_versions(migrated, D_NEXT) == fn_before
    _, day_row = _row(migrated, D, "day")
    assert day_row["repaired"] == ["2001-01-03"]

    _, ids = _import(SEED.read_bytes(), D_NEXT)
    assert DrcStore().rebuild(D) == [D, D_NEXT]
    day_inputs, day_derived = _row(migrated, D_NEXT, "day")
    assert day_derived["trades"] == 2
    assert day_inputs["import_ids"]["trading_log"] == ids[Kind.TRADING_LOG]
    assert migrated.execute(
        """SELECT count(*) FROM "user".drc_rows WHERE day = %s AND kind = 'trade'""", (D_NEXT,)
    ).fetchone()[0] == 2


def _record_with_stats(data: bytes, stats_bytes: bytes, day: date):
    parsed, ids = _import(data, day)
    stats = StatsLogSource().parse(stats_bytes, detect_kind("s.md", stats_bytes))
    ids[Kind.STATS_LOG] = DrcStore().record_import(day, stats.result, stats_bytes)
    return _apply(parsed, ids, day, stats)


@requires_db
def test_x9_pass_c_stored_stats_rows_are_re_matched(migrated, weekday_calendar):
    """X9 (v3 `:325`) PASS (c), `G12`: D_NEXT recorded WITH a one-row stats
    log naming its `FFF` short; the re-pair rebuilds the stats input from
    the stored `derived.row` (`missing = []`) and re-matches it to the
    same `trade_id`; the later day's rows are unchanged."""
    _day1_carrying_ddd()
    stats_bytes = _one_row_stats("FFF", "short", D_NEXT, "10:05:00 EST")
    pairing, _ = _record_with_stats(SEED.read_bytes(), stats_bytes, D_NEXT)
    (fff,) = [t for t in pairing.trades if t.symbol == "FFF"]
    assert fff.stats is not None
    before = _snapshot(migrated, D_NEXT)

    _route(DAY1.read_bytes(), D)
    assert _snapshot(migrated, D_NEXT) == before
    rows = migrated.execute(
        """SELECT derived->>'match', derived->>'trade_id' FROM "user".drc_rows
           WHERE day = %s AND kind = 'stats_row'""",
        (D_NEXT,),
    ).fetchall()
    assert rows == [("matched", fff.trade_id)]


@requires_db
def test_x9_pass_c_a_not_computed_match_is_kept(migrated, weekday_calendar):
    """X9 (v3 `:325`) PASS (c), A1 "do not invent a match": a D_NEXT whose
    stats log lacks `Side` stores `not_computed.match`; after the re-pair
    its `stats_row` rows and that key are unchanged."""
    _day1_carrying_ddd()
    stats_bytes = _drop_column(_one_row_stats("FFF", "short", D_NEXT, "10:05:00 EST"), stats_log.SIDE)
    pairing, _ = _record_with_stats(SEED.read_bytes(), stats_bytes, D_NEXT)
    assert "match" in pairing.not_computed
    before = _snapshot(migrated, D_NEXT)
    _, before_day = _row(migrated, D_NEXT, "day")

    _route(DAY1.read_bytes(), D)
    assert _snapshot(migrated, D_NEXT) == before
    _, after_day = _row(migrated, D_NEXT, "day")
    assert after_day["not_computed"]["match"] == before_day["not_computed"]["match"]


@requires_db
def test_x9_pass_d_a_failed_current_import_fails_the_re_pair(migrated, weekday_calendar):
    """X9 (v3 `:325`) PASS (d): a `failed` current import for D_NEXT →
    `rebuild(D)` FAILS naming 2001-01-03 and the file, nothing replaced
    (v3 `[F-29]` B's clause, the drafter's pin)."""
    _day1_carrying_ddd()
    _route(SEED.read_bytes(), D_NEXT)
    bad = SEED.read_bytes().replace(b"30.8,30,", b"30.8,0,", 1)
    parsed = _parse(bad, D_NEXT, "bad.md")
    assert parsed.result.outcome.value == "failed"
    DrcStore().record_import(D_NEXT, parsed.result, bad, parsed.executions)
    before_d, before_n = _snapshot(migrated, D), _snapshot(migrated, D_NEXT)
    with pytest.raises(PairingError, match="2001-01-03") as e:
        DrcStore().rebuild(D)
    assert "bad.md" in str(e.value)
    assert _snapshot(migrated, D) == before_d
    assert _snapshot(migrated, D_NEXT) == before_n


@requires_db
def test_x9_pass_d_a_partial_current_import_re_pairs_not_computed(migrated, weekday_calendar):
    """X9 (v3 `:325`) PASS (d), `FR14`: a `partial` current import for
    D_NEXT (its `Price` column absent) → the re-pair records D_NEXT
    `not computed` with `not_computed.pairing` = the import's stored
    `reason` (the drafter's pin, C5)."""
    _day1_carrying_ddd()
    _route(SEED.read_bytes(), D_NEXT)
    half = _drop_column(SEED.read_bytes(), "Price")
    parsed, ids = _import(half, D_NEXT, "half.md")
    assert parsed.result.outcome.value == "partial"
    reason = migrated.execute(
        'SELECT reason FROM "user".drc_imports WHERE id = %s', (ids[Kind.TRADING_LOG],)
    ).fetchone()[0]
    assert DrcStore().rebuild(D) == [D, D_NEXT]
    _, day_row = _row(migrated, D_NEXT, "day")
    assert day_row["not_computed"]["pairing"] == reason
    assert _row(migrated, D_NEXT, "book_close") is None


# ---------------------------------------------------------------------
# X10 — v3 `:326` (R51 decides the pass: side A)
# ---------------------------------------------------------------------


# X10's GATE (`test_x10_gate_r51s_order_reaches_k1s_case_iv`) ran on the
# BASE at S2 — R51's order reached K1's case (iv) raise — and was removed
# with the K2 code that replaces that raise; its result is in the build
# report's `## S2 EXPERIMENTS X7–X12`.


@requires_db
def test_x10_pass_the_earlier_close_rebuilds_the_stated_later_day(migrated, weekday_calendar):
    """X10 (v3 `:326`): "Record Wed stated `flat`, then Tue (a first file)
    leaving a short open: is Wed re-paired from Tue's book, and does the
    page show the stated-vs-carried difference?" Result that changes the
    design: "the trigger stays "superseding file" only → the gap R2-1
    names remains; which side of `OPEN FOR DEJAN — R2-1` he takes decides
    which result is the pass" — he took A (R51).

    PASS, R51 side A: recording D does NOT raise ("the
    import does not stop"); D_NEXT is re-paired from D's close — its `B`
    closes the carried short; its `seed` names the statement as history
    and the difference; `drc_stated_books` is byte-identical."""
    stated = _state(D_NEXT)
    _route(CARRIED_SHORT_DAY2, D_NEXT)
    _state(D)
    books = _stated_rows(migrated)

    pairing, _, _ = _route(CARRIED_SHORT_DAY1, D)
    (pos,) = pairing.open_positions
    assert pos.symbol == "GGG" and pos.direction is Direction.SHORT
    trades = migrated.execute(
        """SELECT ref, derived->>'status' FROM "user".drc_rows WHERE day = %s AND kind = 'trade'""",
        (D_NEXT,),
    ).fetchall()
    assert trades == [(pos.trade_id, "closed")]
    assert _row(migrated, D_NEXT, "open_position") is None
    _, close = _row(migrated, D, "book_close")
    seed_inputs, seed_derived = _row(migrated, D_NEXT, "seed")
    assert seed_inputs == {
        "source": "carried",
        "from_day": "2001-01-02",
        "from_book_sha256": close["book_sha256"],
        "stated_book_id": stated.id,
    }
    assert seed_derived["stated_differs"] == [pos.trade_id]
    assert DrcStore().stated_difference(D_NEXT) == (
        f"stated book for 2001-01-03 differed from 2001-01-02's close: {pos.trade_id}"
    )
    assert _stated_rows(migrated) == books


@requires_db
def test_x10_pass_equal_books_store_the_link_and_no_difference(migrated, weekday_calendar):
    """X10 PASS, THE EQUAL CASE: a statement equal to the close by (symbol,
    direction, shares) → `stated_book_id` stored, `stated_differs == []`,
    `stated_difference` → `None`."""
    stated = _state(D_NEXT, positions=[GGG_SHORT])
    _route(HHH_ROUND, D_NEXT)
    _state(D)
    books = _stated_rows(migrated)
    _route(CARRIED_SHORT_DAY1, D)
    seed_inputs, seed_derived = _row(migrated, D_NEXT, "seed")
    assert seed_inputs["source"] == "carried" and seed_inputs["stated_book_id"] == stated.id
    assert seed_derived["stated_differs"] == []
    assert DrcStore().stated_difference(D_NEXT) is None
    assert _stated_rows(migrated) == books


@requires_db
def test_x10_pass_a_not_computed_prior_stops_the_chain(migrated, weekday_calendar):
    """X10 PASS, THE NOT-COMPUTED CASE (C4, the ESCALATE default): D
    recorded with pairing `not computed` under a stated D_NEXT → D is
    recorded, D_NEXT's rows unchanged, D's `day` row names D_NEXT in
    `not_repaired`."""
    _state(D_NEXT)
    _route(CARRIED_SHORT_DAY2, D_NEXT)
    before = _snapshot(migrated, D_NEXT)
    pairing, _, book = _route(CARRIED_SHORT_DAY1, D)
    assert book is None and "pairing" in pairing.not_computed
    assert _snapshot(migrated, D_NEXT) == before
    _, day_row = _row(migrated, D, "day")
    assert day_row["repaired"] == []
    assert day_row["not_repaired"] == [{"day": "2001-01-03", "reason": _NOT_COMPUTED_PRIOR}]


# ---------------------------------------------------------------------
# X11 — v3 `:327`
# ---------------------------------------------------------------------


# X11's GATE (`test_x11_gate_a_closed_book_with_no_exits_raises_index_error`)
# ran on the BASE at S2 — `_trade` of a CLOSED book with no exits raised
# `IndexError` at `pairing.py:155` — and was removed with the K2 `_trade`
# change that removes it; its result is in the build report.


def test_x11_pass_a_resolve_with_no_exit_price_closes_the_carried_trade_offline():
    """X11 (v3 `:327`): "A resolve with no exit price on a carried trade:
    CLOSED, `legs = []`, realized `not computed — exit not in any export`,
    no `IndexError` at `pairing.py:97`. Also gates K3." Result that
    changes the design: "an exception → the resolved trade is not built
    through `_trade`".

    PASS, offline: `build_day(…, seed=…, resolves=…)`
    on a file that does not touch the carried `DDD` → the trade CLOSED,
    `legs == []`, the literal realized figure, no exception."""
    from cobalt.drc.models import ResolveInput, StatedResolve
    from cobalt.drc.pairing import build_day

    _, day1 = _trading(DAY1, D)
    seed = pair_day(day1.executions, D).open_positions
    (pos,) = seed
    resolve = ResolveInput(id=7, resolve=StatedResolve(trade_id=pos.trade_id))
    day = build_day(_parse(EEE_ROUND, D_NEXT), seed=seed, resolves=[resolve])
    (ddd,) = [t for t in day.trades if t.symbol == "DDD"]
    assert ddd.status is TradeStatus.CLOSED and ddd.trade_id == pos.trade_id
    assert ddd.legs == [] and ddd.held_shares == 0
    assert ddd.gross_pnl == EXIT_NOT_IN_ANY_EXPORT
    assert [p.symbol for p in day.open_positions] == []
    assert [(o.resolve_id, o.trade_id, o.status) for o in day.resolves] == [(7, pos.trade_id, "applied")]


@requires_db
def test_x11_pass_a_stored_resolve_closes_the_carried_trade_on_its_day(migrated, weekday_calendar):
    """X11 (v3 `:327`) PASS, with-DB: D leaves `DDD 30` open; a resolve
    for it dated D_NEXT; D_NEXT recorded with a file that does not touch
    `DDD` → its `book_close` no longer holds the trade, and the closed
    trade's `inputs.resolve_id` is the resolve row's id."""
    day1 = _day1_carrying_ddd()
    (pos,) = day1.open_positions
    resolve = _state(D_NEXT, kind="resolve", positions=[{"trade_id": pos.trade_id}])
    _route(EEE_ROUND, D_NEXT)
    _, close = _row(migrated, D_NEXT, "book_close")
    assert pos.trade_id not in close["trade_ids"]
    inputs, derived = migrated.execute(
        """SELECT inputs, derived FROM "user".drc_rows WHERE day = %s AND kind = 'trade' AND ref = %s""",
        (D_NEXT, pos.trade_id),
    ).fetchone()
    assert inputs["resolve_id"] == resolve.id
    assert derived["status"] == "closed" and derived["gross_pnl"] == EXIT_NOT_IN_ANY_EXPORT
