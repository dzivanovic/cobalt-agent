"""DRC K1 — the first-gate experiments X1–X6 (v3 `## First-gate
experiments (L70)`, "Before K1"), run BEFORE any K1 code.

Each X has a GATE and a PASS test (X2 and X3 have no runnable gate on
built code; the build report records why):

- a GATE test runs on the code as it stands — only `pair_day`, the
  models, `assert_writable`, the migration SQL, `DrcStore.record_import`
  and raw SQL through the store's proxy connection. It stays green after
  K1 is built.
- a PASS test states v3's pass condition against the K1 contract. Every
  K1 symbol is imported INSIDE the test body, so each is its own red
  until the K1 code exists.

Constructed symbols and dates only (L32 / L45). WITH-DB tests run inside
`test_drc_store.py`'s never-committed migration transaction (L76):
nothing here commits a migration.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import date, datetime, timezone

import psycopg
import pytest
from psycopg.types.json import Jsonb

from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.cli import _apply
from cobalt.drc.detect import detect_kind
from cobalt.drc.models import Direction, Kind, OpenPosition, TradeStatus
from cobalt.drc.pairing import pair_day
from cobalt.drc.store import DrcStore
from cobalt.drc.trading_log import TradingLogSource

from test_drc_pairing import CARRIED_SHORT_DAY2
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D,
    D_NEXT,
    DAY1,
    SEED,
    _Proxy,
    _trading,
    migrated,
    requires_db,
    weekday_calendar,
)

#: 10:00 ET on a constructed trading day — outside market_reset.
TEN_ET = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
#: 20:15 ET the same day — inside market_reset (`test_daymode.py:531-532`'s shape).
RESET_ET = datetime(2026, 9, 4, 0, 15, tzinfo=timezone.utc)

CARRIED_COST_NOT_STATED = "not computed — carried cost not stated"
OPENING_NOT_STATED = "not computed — opening book not stated"

OLD_KIND_CHECK = "CHECK (kind IN ('trade', 'open_position', 'stats_row', 'day'))"
WIDE_KIND_CHECK = "CHECK (kind IN ('trade', 'open_position', 'stats_row', 'day', 'seed', 'book_close'))"


def _encode(rows: list[dict]) -> bytes:
    """THE PINNED ENCODING (X4), written inline: canonical JSON bytes."""
    return json.dumps(rows, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _canonical(positions) -> list[dict]:
    return [p.model_dump(mode="json") for p in sorted(positions, key=lambda p: p.trade_id)]


def _parse(data: bytes, day: date):
    return TradingLogSource().parse(data, day, detect_kind("t.md", data))


def _insert_positions(positions, day: date, fn: str) -> None:
    with DrcStore()._connect() as conn:
        for p in positions:
            conn.execute(
                "INSERT INTO drc_rows (day, kind, ref, inputs, derived, fn_version) "
                "VALUES (%s, 'open_position', %s, '{}', %s, %s)",
                (day, p.trade_id, Jsonb(p.model_dump(mode="json")), fn),
            )


def _read_positions(day: date) -> list[dict]:
    with DrcStore()._connect() as conn:
        return [
            r[0]
            for r in conn.execute(
                "SELECT derived FROM drc_rows WHERE kind = 'open_position' AND day = %s ORDER BY ref",
                (day,),
            ).fetchall()
        ]


def _row(conn, day: date, kind: str):
    return conn.execute(
        'SELECT inputs, derived FROM "user".drc_rows WHERE day = %s AND kind = %s', (day, kind)
    ).fetchone()


# ---------------------------------------------------------------------
# X1 — v3 `:312`
# ---------------------------------------------------------------------


@requires_db
def test_x1_gate_a_stored_open_position_reads_back_as_the_next_days_seed(migrated):
    """X1 (v3 `:312`): "Proposal read-back (1), (2): day 1 leaves one open
    position; day 2 imports, the carried `trade_id` unchanged,
    `seed.source = carried`, `from_book_sha256` = day 1's." Result that
    changes the design: "a changed `trade_id` or source → K1's seed record
    is wrong". GATE: the built carry survives a `drc_rows` round trip."""
    _, day1 = _trading(DAY1, D)
    first = pair_day(day1.executions, D)
    (pos,) = first.open_positions
    _insert_positions(first.open_positions, D, "x1-gate")
    seed = [OpenPosition.model_validate(r) for r in _read_positions(D)]
    assert seed == first.open_positions
    _, day2 = _trading(SEED, D_NEXT)
    second = pair_day(day2.executions, D_NEXT, seed)
    (ddd,) = [t for t in second.trades if t.symbol == "DDD"]
    assert ddd.trade_id == pos.trade_id
    assert ddd.status is TradeStatus.CLOSED


@requires_db
def test_x1_pass_day_two_records_the_carried_seed_with_day_ones_hash(migrated, weekday_calendar):
    """X1 (v3 `:312`) PASS: read-back (1), (2) through the K1 store — day 1
    stated flat and recorded leaves one open position; day 2 recorded from
    `seed_for(D_NEXT)` keeps the carried `trade_id`, `seed.inputs.source ==
    "carried"`, `from_book_sha256` == day 1's `book_close.derived.book_sha256`."""
    from cobalt.drc.pairing import build_day

    store = DrcStore()
    store.record_stated_book(D, "opening", [], via="cli", now=TEN_ET)
    seed1 = store.seed_for(D)
    assert seed1.source == "stated"
    data, day1 = _trading(DAY1, D)
    ids1 = {Kind.TRADING_LOG: store.record_import(D, day1.result, data, day1.executions)}
    p1 = build_day(day1, seed=seed1.positions)
    store.record_day(p1, ids1, seed1)
    _, close1 = _row(migrated, D, "book_close")
    assert close1["count"] == 1
    (carried_id,) = close1["trade_ids"]

    seed2 = store.seed_for(D_NEXT)
    assert seed2.source == "carried"
    assert seed2.from_day == D
    assert seed2.from_book_sha256 == close1["book_sha256"]
    data2, day2 = _trading(SEED, D_NEXT)
    ids2 = {Kind.TRADING_LOG: store.record_import(D_NEXT, day2.result, data2, day2.executions)}
    p2 = build_day(day2, seed=seed2.positions)
    store.record_day(p2, ids2, seed2)
    inputs, _ = _row(migrated, D_NEXT, "seed")
    assert inputs["source"] == "carried"
    assert inputs["from_book_sha256"] == close1["book_sha256"]
    (ddd,) = [t for t in p2.trades if t.symbol == "DDD"]
    assert ddd.trade_id == carried_id
    assert migrated.execute(
        """SELECT count(*) FROM "user".drc_rows WHERE day = %s AND kind = 'trade' AND ref = %s""",
        (D_NEXT, carried_id),
    ).fetchone()[0] == 1


# ---------------------------------------------------------------------
# X2 — v3 `:313` (GATE: none can run on built code — B8 is pinned as
# built, `test_drc_pairing.py:265-272`; recorded in the build report)
# ---------------------------------------------------------------------


@requires_db
def test_x2_pass_no_statement_then_a_stated_short_then_a_stated_flat(migrated, weekday_calendar):
    """X2 (v3 `:313`): "first import, no statement → `not computed`, zero
    trades, no `book_close`; state the short, drop a leading `B` → one
    CLOSED trade, `book_close` count 0; fresh chain, state flat, leading
    `B` → one OPEN long listed by the evening unit." Result that changes
    the design: "the long missing from the unit → the flat tap must FAIL
    when the file still holds a position opened that day". The evening
    UNIT is K3's (L28); K1 proves the stored row it renders from
    (`[F-11]`): the long is in `book_close.derived.trade_ids`."""
    from cobalt.drc.pairing import build_day

    store = DrcStore()
    parsed = _parse(CARRIED_SHORT_DAY2, D)
    migrated.execute("SAVEPOINT x2_fresh")

    # (a) first import, no statement
    ids = {Kind.TRADING_LOG: store.record_import(D, parsed.result, CARRIED_SHORT_DAY2, parsed.executions)}
    seed = store.seed_for(D)
    assert seed is None
    store.record_day(build_day(parsed, seed=seed), ids, seed)
    _, day_row = _row(migrated, D, "day")
    assert day_row["not_computed"]["pairing"] == OPENING_NOT_STATED
    assert migrated.execute(
        """SELECT count(*) FROM "user".drc_rows WHERE day = %s AND kind = 'trade'""", (D,)
    ).fetchone()[0] == 0
    assert _row(migrated, D, "book_close") is None

    # (b) state the short, drop the leading B
    store.record_stated_book(
        D, "opening", [{"symbol": "GGG", "direction": "short", "shares": 40, "avg_cost": None}],
        via="cli", now=TEN_ET,
    )
    seed = store.seed_for(D)
    pairing = build_day(parsed, seed=seed.positions)
    store.record_day(pairing, ids, seed)
    (ggg,) = pairing.trades
    assert ggg.status is TradeStatus.CLOSED and ggg.direction is Direction.SHORT
    _, close = _row(migrated, D, "book_close")
    assert close["count"] == 0 and close["trade_ids"] == []

    # (c) a fresh chain: state flat, the same bytes
    migrated.execute("ROLLBACK TO SAVEPOINT x2_fresh")
    ids = {Kind.TRADING_LOG: store.record_import(D, parsed.result, CARRIED_SHORT_DAY2, parsed.executions)}
    store.record_stated_book(D, "opening", [], via="cli", now=TEN_ET)
    seed = store.seed_for(D)
    pairing = build_day(parsed, seed=seed.positions)
    store.record_day(pairing, ids, seed)
    (long_,) = pairing.trades
    assert long_.status is TradeStatus.OPEN and long_.direction is Direction.LONG
    _, close = _row(migrated, D, "book_close")
    assert close["count"] == 1 and long_.trade_id in close["trade_ids"]


# ---------------------------------------------------------------------
# X3 — v3 `:314` (GATE: none can run — `models.py:98` `Lot.price` and
# `:110` `OpenPosition.entry_time` are required today; recorded)
# ---------------------------------------------------------------------


def test_x3_pass_a_stated_short_without_cost_or_time_closes_not_computed():
    """X3 (v3 `:314`): "Stated position, cost null and entry time null,
    next day's file closes it: realized is the literal `not computed —
    carried cost not stated`, `_reduce` not applied, no exception at
    `pairing.py:69`, `:105`, `:235`." Result that changes the design: "an
    exception or any numeric P&L → the stated-position model is incomplete
    (the named gap of `[F-04]`)"."""
    from cobalt.drc.models import StatedPosition
    from cobalt.drc.pairing import stated_open_positions

    seed = stated_open_positions(
        D_NEXT, [StatedPosition(symbol="GGG", direction="short", shares=40, avg_cost=None)]
    )
    (pos,) = seed
    assert pos.entry_time is None and pos.lots[0].price is None and pos.lots[0].time is None
    parsed = _parse(CARRIED_SHORT_DAY2, D_NEXT)
    pairing = pair_day(parsed.executions, D_NEXT, seed)
    (ggg,) = pairing.trades
    assert ggg.status is TradeStatus.CLOSED and ggg.direction is Direction.SHORT
    assert ggg.trade_id == pos.trade_id
    assert ggg.gross_pnl == CARRIED_COST_NOT_STATED
    assert ggg.held_shares == 0 and ggg.avg_entry is None and ggg.hold_seconds is None
    assert pairing.open_positions == []


# ---------------------------------------------------------------------
# X4 — v3 `:315`
# ---------------------------------------------------------------------

_SECOND_PROCESS = (
    "import hashlib, json, sys\n"
    "rows = json.loads(sys.stdin.read())\n"
    "data = json.dumps(rows, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf-8')\n"
    "print(hashlib.sha256(data).hexdigest())\n"
)


@requires_db
def test_x4_gate_the_pinned_encoding_hashes_equal_in_memory_read_back_and_a_second_process(migrated):
    """X4 (v3 `:315`): "Hash the same `open_position` rows twice in two
    processes (canonical JSON sorted by `trade_id`); compare with the
    stored `book_close`." Result that changes the design: "different hex →
    the canonical encoding is fixed before K1, or the morning check
    false-FAILs"."""
    _, day1 = _trading(DAY1, D)
    positions = pair_day(day1.executions, D).open_positions
    assert positions
    in_memory = _canonical(positions)
    _insert_positions(positions, D, "x4-gate")
    read_back = sorted(_read_positions(D), key=lambda r: r["trade_id"])
    assert read_back == in_memory
    h_memory = hashlib.sha256(_encode(in_memory)).hexdigest()
    h_read = hashlib.sha256(_encode(read_back)).hexdigest()
    proc = subprocess.run(
        [sys.executable, "-c", _SECOND_PROCESS],
        input=json.dumps(read_back),
        capture_output=True,
        text=True,
        check=True,
    )
    h_other = proc.stdout.strip()
    assert h_memory == h_read == h_other, (h_memory, h_read, h_other)


@requires_db
def test_x4_pass_book_sha256_is_the_pinned_encoding_and_the_stored_close_recomputes(migrated, weekday_calendar):
    """X4 (v3 `:315`) PASS: K1's `pairing.book_sha256(positions)` equals the
    inline encoding, and a recorded day's `book_close.derived.book_sha256`
    equals a recomputation over its `open_position` rows read back."""
    from cobalt.drc.pairing import book_sha256, build_day

    _, day1 = _trading(DAY1, D)
    positions = pair_day(day1.executions, D).open_positions
    assert book_sha256(positions) == hashlib.sha256(_encode(_canonical(positions))).hexdigest()

    store = DrcStore()
    store.record_stated_book(D, "opening", [], via="cli", now=TEN_ET)
    seed = store.seed_for(D)
    data, day1 = _trading(DAY1, D)
    ids = {Kind.TRADING_LOG: store.record_import(D, day1.result, data, day1.executions)}
    store.record_day(build_day(day1, seed=seed.positions), ids, seed)
    _, close = _row(migrated, D, "book_close")
    read_back = sorted(_read_positions(D), key=lambda r: r["trade_id"])
    assert close["book_sha256"] == hashlib.sha256(_encode(read_back)).hexdigest()


# ---------------------------------------------------------------------
# X5 — v3 `:316`
# ---------------------------------------------------------------------


def _insert_kind(kind: str) -> None:
    with DrcStore()._connect() as conn:
        conn.execute(
            "INSERT INTO drc_rows (day, kind, ref, inputs, derived, fn_version) "
            "VALUES (%s, %s, 'book', '{}', '{}', 'x5')",
            (D, kind),
        )


@requires_db
def test_x5_gate_an_edited_0016_applied_over_the_old_one_leaves_the_check_unchanged(migrated):
    """X5 (v3 `:316`): "Apply an edited `0016` on a `cobalt_dev` where the
    old `0016` applied; insert `kind = 'seed'`." Result that changes the
    design: "the CHECK unchanged → a new numbered file, never the fold
    (`[F-02]`'s "Otherwise")". Either result keeps `0018` (`[F-02]`'s
    default); a STORED insert here is an ESCALATE, not a stop.

    The state "old `0016` applied" is `migrated`'s FORWARD — minus K1's own
    widening once `0018` is registered, which its registered rollback takes
    back first."""
    text = (MIGRATIONS_DIR / "0016_drc.sql").read_text()
    assert text.count(OLD_KIND_CHECK) == 1
    edited = text.replace(OLD_KIND_CHECK, WIDE_KIND_CHECK)
    assert edited.count(WIDE_KIND_CHECK) == 1 and OLD_KIND_CHECK not in edited
    k1 = [p for p in REVERSE if p.name.startswith("0018_")]
    if k1:
        _apply(migrated, k1)
    migrated.execute(edited)
    with pytest.raises(psycopg.errors.CheckViolation):
        _insert_kind("seed")


@requires_db
def test_x5_pass_0018_widens_the_kind_check_and_its_rollback_narrows_it(migrated):
    """X5 (v3 `:316`) PASS: `0018` applied on `migrated` → the `seed` insert
    is STORED; `0018`'s rollback applied → refused again."""
    forward = MIGRATIONS_DIR / "0018_drc_stated_books.sql"
    rollback = MIGRATIONS_DIR / "0018_drc_stated_books.rollback.sql"
    assert forward in FORWARD and rollback in REVERSE
    _apply(migrated, [forward])
    _insert_kind("seed")
    assert migrated.execute(
        """SELECT count(*) FROM "user".drc_rows WHERE kind = 'seed'"""
    ).fetchone()[0] == 1
    _apply(migrated, [rollback])
    with pytest.raises(psycopg.errors.CheckViolation):
        _insert_kind("seed")


# ---------------------------------------------------------------------
# X6 — v3 `:317`
# ---------------------------------------------------------------------


class _Collector:
    def __init__(self):
        self.calls: list[dict] = []

    def record(self, **kw):
        self.calls.append(kw)


def test_x6_gate_the_guard_refuses_inside_market_reset_and_passes_at_ten():
    """X6 (v3 `:317`): "`record_stated_book` called inside `market_reset`
    (the widget's tool at 20:15 ET with a constructed clock included):
    refused, no row." Result that changes the design: "the row commits
    while the note write is refused → `[F-01]`'s refusal is not what was
    built". GATE: the built guard refuses 20:15 ET and passes 10:00 ET."""
    from cobalt.session import SessionBlocked, assert_writable

    collector = _Collector()
    with pytest.raises(SessionBlocked):
        assert_writable("drc.record_stated_book", target="2026-09-03", now=RESET_ET, store=collector)
    assert len(collector.calls) == 1
    assert_writable("drc.record_stated_book", target="2026-09-03", now=TEN_ET, store=collector)
    assert len(collector.calls) == 1


@requires_db
def test_x6_pass_record_stated_book_refuses_inside_market_reset_with_no_row(migrated, monkeypatch):
    """X6 (v3 `:317`) PASS: `record_stated_book(…, now=<20:15 ET>)` raises
    `SessionBlocked`, `drc_stated_books` holds 0 rows in that transaction,
    and the guard's own `session_blocks` audit call happens ONCE."""
    from cobalt.session import SessionBlocked
    from cobalt.session.store import SessionBlockStore

    calls: list[dict] = []
    monkeypatch.setattr(SessionBlockStore, "record", lambda self, **kw: calls.append(kw))
    with pytest.raises(SessionBlocked):
        DrcStore().record_stated_book(D, "opening", [], via="cli", now=RESET_ET)
    assert migrated.execute('SELECT count(*) FROM "user".drc_stated_books').fetchone()[0] == 0
    assert len(calls) == 1
