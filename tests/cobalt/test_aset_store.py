"""Integration test: real INSERT/SELECT against cobalt_dev.

Runs only when Postgres env settings are present (conftest loads .env).
Never touches cobalt_brain — the connection factory refuses it.

CLEANUP (added 2026-09-03): these tests write REAL rows into the same
`aset_sizings` the production ASET sheet writes to (configs/dev/aset.yaml
sets `db_name: cobalt_dev` for both). Every run used to leave its
TEST/FORDATE rows behind, and 27 of them accumulated on 2026-09-03 —
15 of which are the rows the incident report found polluting
DRC-2026-09-03.md's "17 cards" when only 2 were real. Each test now
deletes exactly the ids it created.
"""

import os
from decimal import Decimal

import pytest

from cobalt.aset.engine import compute_sizing
from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput
from cobalt.aset.store import AsetStore

# RULING 7.1d: every DB test runs inside a cobalt_dev transaction that
# is rolled back (tests/cobalt/conftest.py). The per-test id cleanup
# below is kept as a second belt — it documents which rows a test
# owns — but it is no longer what keeps the database clean.
pytestmark = [pytest.mark.integration, pytest.mark.usefixtures("dev_db_tx")]

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


def _delete_rows(store: AsetStore, ids: list[int]) -> None:
    """Remove exactly the rows this test created — never a range, never a
    ticker match. cobalt_dev is the SAME database production ASET writes
    to, so test rows left behind become real pollution in the DRC's
    counts (2026-09-03: 15 stray TEST/FORDATE rows did exactly that)."""
    with store._connect() as conn:
        conn.execute("DELETE FROM aset_sizings WHERE id = ANY(%s)", (ids,))


@requires_db
def test_save_and_read_back_roundtrip():
    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    result = compute_sizing(
        SizingInput(
            ticker="TEST",
            grade=Grade.B,
            direction=Direction.LONG,
            sheet_mode=SheetMode.FULL,
            risk_dollars=Decimal("60"),
            entry=Decimal("10.00"),
            stop=Decimal("9.50"),
            last_price=Decimal("10.01"),
            price_source="integration-test",
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )
    row_id = store.save(result)
    try:
        assert row_id > 0

        rows = store.recent(limit=5)
        match = [r for r in rows if r["id"] == row_id]
        assert match, "saved row not found in recent()"
        row = match[0]
        assert row["ticker"] == "TEST"
        assert row["grade"] == "B"
        assert row["sheet_mode"] == "full"
        assert row["shares"] == 120  # 60 / 0.50 = 120
        assert row["used_risk"] == Decimal("60.00")
        assert row["status"] == "CARD"  # migration 0003: lifecycle status
    finally:
        _delete_rows(store, [row_id])


@requires_db
def test_for_date_returns_todays_cards_oldest_first():
    from datetime import datetime, timezone

    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    result = compute_sizing(
        SizingInput(
            ticker="FORDATE",
            grade=Grade.B,
            direction=Direction.LONG,
            sheet_mode=SheetMode.FULL,
            risk_dollars=Decimal("60"),
            entry=Decimal("10.00"),
            stop=Decimal("9.50"),
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )
    id1 = store.save(result)
    id2 = store.save(result)

    try:
        today_et = datetime.now(timezone.utc).astimezone().date()
        rows = store.for_date(today_et)
        ids = [r["id"] for r in rows]
        assert id1 in ids and id2 in ids
        assert ids.index(id1) < ids.index(id2)  # oldest first
        assert all(r["ticker"] != "" for r in rows)

        # migration 0003: cards written vs trades taken are two numbers
        written, taken = store.counts_for_date(today_et)
        assert written >= 2
        # `counts_for_date` counts STATE, not `status` — `status` stopped
        # being written when the F7 machine landed (aset/migrations/0006),
        # so a `status`-based expectation here agreed with it only for as
        # long as no card in `cobalt_dev` had ever been filled. The
        # 2026-09-08 sprint-close smoke wrote the first one and the two
        # numbers parted company. A card that FILLED and then CLOSED is
        # still a trade taken, so both states count.
        assert taken == sum(1 for r in rows if r["state"] in ("FILLED", "CLOSED"))
    finally:
        _delete_rows(store, [id1, id2])


@requires_db
def test_mark_filled_updates_the_card_row():
    """The fill recompute used to persist NOTHING — the 09-03 TSLA FILL
    UPDATE (10:02:36) had no DB row at all. It is an UPDATE to the card
    row now, plus a TRIGGERED -> FILLED transition.

    S1-P2 (F7): a fill is a state transition and FILLED is reachable only
    from TRIGGERED, so the card is walked there first — see
    `test_mark_filled_refuses_a_card_that_was_never_triggered` below for
    the other half. `status` is no longer written; `state` is the truth.
    """
    from cobalt.aset.engine import compute_fill_recompute
    from cobalt.cards.models import Actor, CardState
    from cobalt.cards.store import CardStore

    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    result = compute_sizing(
        SizingInput(
            ticker="TEST",
            grade=Grade.B,
            direction=Direction.LONG,
            sheet_mode=SheetMode.FULL,
            risk_dollars=Decimal("60"),
            entry=Decimal("10.00"),
            stop=Decimal("9.50"),
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )
    row_id = store.save(result)
    cards = CardStore("cobalt_dev")
    try:
        cards.transition(row_id, CardState.ARMED, actor=Actor.YOU)
        cards.transition(row_id, CardState.TRIGGERED, actor=Actor.YOU)

        fill = compute_fill_recompute(result, Decimal("10.10"), Decimal("5"))
        store.mark_filled(row_id, fill)
        row = [r for r in store.recent(limit=10) if r["id"] == row_id][0]
        assert row["state"] == "FILLED"
        assert cards.state_of(row_id) is CardState.FILLED
        # The fill's own figures ride in the transition's evidence. The
        # evidence keeps the Decimal AS GIVEN ("10.10"); the card column
        # is NUMERIC(14,4) and pads it ("10.1000"). Both are asserted so
        # the difference is documented rather than discovered later.
        assert cards.history(row_id)[-1]["evidence"]["actual_fill"] == "10.10"

        with store._connect() as conn:
            actual, shares = conn.execute(
                "SELECT actual_fill, recomputed_shares FROM aset_sizings WHERE id = %s",
                (row_id,),
            ).fetchone()
        assert actual == Decimal("10.1000")
        assert shares == fill.recomputed_shares

        with pytest.raises(Exception, match="no aset_sizings row with id -1"):
            store.mark_filled(-1, fill)
    finally:
        _delete_rows(store, [row_id])


@requires_db
def test_mark_filled_on_a_manual_card_walks_the_missing_rows_itself():
    """F7 ONE-CLICK FILL (S1-P3, CTO review of S1-P2).

    Until this prompt, filling a WATCH card was refused by name: FILLED
    is reachable only from TRIGGERED, and a card that skipped it would
    make the MISSED count (Charter §3 F7) meaningless. That reasoning
    still holds for a card the RADAR proposed — the detector's claim IS
    that it watched the arm and the trigger — and it is asserted in
    `test_mark_filled_refuses_the_shortcut_on_a_radar_card` below.

    It does not hold for a card Dejan wrote himself: the arm and the
    trigger happened, in DAS, and Cobalt was simply not asked to watch.
    So a `manual` card fills in one click and Cobalt writes the rows it
    is missing — actor cobalt, evidence `auto=manual_fill`, same
    timestamp — rather than making him tap three buttons to describe a
    trade he has already taken.
    """
    from cobalt.aset.engine import compute_fill_recompute
    from cobalt.cards.models import Actor, CardState
    from cobalt.cards.store import CardStore

    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    result = compute_sizing(
        SizingInput(
            ticker="TEST",
            grade=Grade.B,
            direction=Direction.LONG,
            sheet_mode=SheetMode.FULL,
            risk_dollars=Decimal("60"),
            entry=Decimal("10.00"),
            stop=Decimal("9.50"),
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )
    row_id = store.save(result)
    try:
        cards = CardStore("cobalt_dev")
        assert cards.state_of(row_id) is CardState.WATCH
        fill = compute_fill_recompute(result, Decimal("10.10"), Decimal("5"))
        store.mark_filled(row_id, fill)

        assert cards.state_of(row_id) is CardState.FILLED
        history = cards.history(row_id)
        # genesis + ARMED + TRIGGERED + FILLED
        assert [h["to_state"] for h in history] == [
            "WATCH", "ARMED", "TRIGGERED", "FILLED",
        ]
        armed, triggered, filled = history[1], history[2], history[3]
        assert armed["actor"] == Actor.COBALT.value
        assert triggered["actor"] == Actor.COBALT.value
        assert filled["actor"] == Actor.YOU.value, "the fill is HIS tap; the rest are not"
        assert armed["evidence"]["auto"] == "manual_fill"
        assert triggered["evidence"]["auto"] == "manual_fill"
        assert armed["at"] == triggered["at"] == filled["at"], (
            "the inserted rows carry the FILL's timestamp — they are bookkeeping "
            "about one moment, not three moments Cobalt is claiming to have seen"
        )
        with store._connect() as conn:
            actual = conn.execute(
                "SELECT actual_fill FROM aset_sizings WHERE id = %s", (row_id,)
            ).fetchone()[0]
        assert actual == Decimal("10.10")
    finally:
        _delete_rows(store, [row_id])


def test_mark_filled_refuses_the_shortcut_on_a_radar_card():
    """A card the S2 radar proposed gets NO one-click fill.

    The detector's entire claim is that it saw the arm and the trigger
    happen, so a fill that skipped them is a hole in the detector's
    record — refused by name, exactly as every fill was before the
    shortcut existed."""
    from cobalt.aset.engine import compute_fill_recompute
    from cobalt.cards.models import CardState, IllegalTransition, Origin
    from cobalt.cards.store import CardStore

    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    result = compute_sizing(
        SizingInput(
            ticker="TEST",
            grade=Grade.B,
            direction=Direction.LONG,
            sheet_mode=SheetMode.FULL,
            risk_dollars=Decimal("60"),
            entry=Decimal("10.00"),
            stop=Decimal("9.50"),
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )
    row_id = store.save(result)
    try:
        with store._connect() as conn:
            conn.execute(
                "UPDATE aset_sizings SET origin = %s WHERE id = %s",
                (Origin.RADAR.value, row_id),
            )
        fill = compute_fill_recompute(result, Decimal("10.10"), Decimal("5"))
        with pytest.raises(IllegalTransition, match="WATCH -> FILLED"):
            store.mark_filled(row_id, fill)
        assert CardStore("cobalt_dev").state_of(row_id) is CardState.WATCH
        with store._connect() as conn:
            actual = conn.execute(
                "SELECT actual_fill FROM aset_sizings WHERE id = %s", (row_id,)
            ).fetchone()[0]
        assert actual is None, "the refused fill wrote nothing to the card row"
    finally:
        _delete_rows(store, [row_id])
