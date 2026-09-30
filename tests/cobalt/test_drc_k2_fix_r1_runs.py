"""DRC K2 fix r1 — RUNS (L70; the fix prompt
`prompts/2026-09-25/02-drc-k2-fix-r1-build.md` F5).

RUN-1 turns the build's ESCALATE 9 (`drc-k2-build-2026-09-24.md:255`,
"unreached by any test; a builder reading") into a run whose output the
report quotes. A red here is a RESULT for round 2, never fixed in fix r1
(L70 / L75). Everything runs inside `test_drc_store.py`'s never-committed
migration transaction on `cobalt_dev` (L76). Constructed values only
(L32 / L45).
"""

from __future__ import annotations

from cobalt.drc.pairing import pair_day
from cobalt.drc.store import DrcStore

from test_drc_k1_store import GGG_SHORT, _day1_carrying_ddd, _row, _state
from test_drc_k2_experiments import _stated_rows
from test_drc_store import (  # noqa: F401 — fixtures are used by name
    D_NEXT,
    migrated,
    requires_db,
    weekday_calendar,
)


@requires_db
def test_run_1_a_no_trade_day_with_a_stated_opening_beside_a_recorded_prior(migrated, weekday_calendar):
    """RUN-1 (build ESCALATE 9, `drc-k2-build-2026-09-24.md:255`): "A
    no-trade day that also has a stated opening beside a recorded prior …
    `_repair` therefore keeps `source: carried`, with the R51 statement
    link and difference. The `day` row still names `no_trade_id`".

    R51's order: an opening that differs from D's close and a no-trade DRC
    are stated for D_NEXT while D is NOT recorded (H2 allows it); D_NEXT
    is recorded as a no-trade day from its statement (so D's forward
    re-pair reaches it); then D is recorded leaving `DDD 30` open. Then
    the `record_day` path (F-3's second caller) stores the same seed."""
    op = _state(D_NEXT, positions=[GGG_SHORT])
    nt = _state(D_NEXT, kind="no_trade")
    assert DrcStore().rebuild(D_NEXT) == [D_NEXT]
    books = _stated_rows(migrated)

    (pos,) = _day1_carrying_ddd().open_positions
    after = _stated_rows(migrated)
    assert after[: len(books)] == books and len(after) == len(books) + 1  # only D's own opening

    seed_inputs, seed_derived = _row(migrated, D_NEXT, "seed")
    assert set(seed_inputs) == {"source", "from_day", "from_book_sha256", "stated_book_id"}
    assert seed_inputs["source"] == "carried" and seed_inputs["stated_book_id"] == op.id
    assert seed_inputs["from_day"] == "2001-01-02"
    assert set(seed_derived) == {"count", "trade_ids", "stated_differs"}
    assert seed_derived["stated_differs"] and pos.trade_id in seed_derived["stated_differs"]
    assert seed_derived["trade_ids"] == [pos.trade_id]
    day_inputs, _ = _row(migrated, D_NEXT, "day")
    assert day_inputs["no_trade_id"] == nt.id
    assert DrcStore().stated_difference(D_NEXT).startswith(
        "stated book for 2001-01-03 differed from 2001-01-02's close:"
    )

    store = DrcStore()
    book = store.seed_for(D_NEXT)
    store.record_day(pair_day([], D_NEXT, book.positions), {}, book)
    assert _row(migrated, D_NEXT, "seed") == (seed_inputs, seed_derived)
    assert _stated_rows(migrated) == after
