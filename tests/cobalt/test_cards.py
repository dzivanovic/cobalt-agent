"""F7 card state machine — Charter §3 F7, SPRINT-LADDER §S1.

The five things S1-P2 has to prove:

1. the full walk WATCH -> ARMED -> TRIGGERED -> FILLED -> CLOSED, with
   FOUR transition rows behind it (the genesis row makes five);
2. the disarm round-trip, the one backwards edge;
3. EVERY illegal edge refused, by name — enumerated from the edge table
   itself rather than a hand-picked few, so a future edit to `ALLOWED`
   cannot quietly widen the machine without a test noticing;
4. expiry at 16:05 on a full day and at 13:05 on the 2026-11-27 early
   close;
5. a card in `market_reset` refused by F1 BEFORE any state logic runs.

Pure-machine tests (1-3's edge algebra, the window resolver) need no
database. The rest are integration tests inside the rolled-back
`cobalt_dev` transaction the conftest provides.
"""

import os
from datetime import datetime, timezone
from decimal import Decimal
from zoneinfo import ZoneInfo

import pytest

from cobalt.aset.engine import compute_sizing
from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput
from cobalt.aset.store import AsetStore
from cobalt.cards import expire as expire_mod
from cobalt.cards.models import (
    ALLOWED,
    STOP_EDITABLE,
    TERMINAL,
    Actor,
    CardState,
    IllegalTransition,
    assert_edge,
    edge_table_markdown,
    is_legal,
)
from cobalt.cards.store import BACKFILL_MARKER, CardStateError, CardStore
from cobalt.session import SessionBlocked
from cobalt.session import clock as clock_mod

ET = ZoneInfo("America/New_York")

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


def _et(y, m, d, hh, mm=0) -> datetime:
    return datetime(y, m, d, hh, mm, tzinfo=ET)


# =====================================================================
# 1. The edge table itself — no database needed
# =====================================================================


class TestEdgeTable:
    def test_the_ruled_edges_are_exactly_what_is_allowed(self):
        """The edge set from the S1-P2 ruling, transcribed once, here."""
        assert ALLOWED[CardState.WATCH] == frozenset(
            {CardState.ARMED, CardState.PASSED, CardState.EXPIRED, CardState.MISSED}
        )
        assert ALLOWED[CardState.ARMED] == frozenset(
            {CardState.WATCH, CardState.TRIGGERED, CardState.EXPIRED}
        )
        assert ALLOWED[CardState.TRIGGERED] == frozenset(
            {CardState.FILLED, CardState.PASSED, CardState.EXPIRED}
        )
        assert ALLOWED[CardState.FILLED] == frozenset({CardState.CLOSED})

    def test_terminal_states_are_exactly_the_four_ruled(self):
        assert TERMINAL == frozenset(
            {CardState.CLOSED, CardState.PASSED, CardState.EXPIRED, CardState.MISSED}
        )

    def test_every_state_is_reachable(self):
        """A state nothing can enter is a state that will never be
        counted — and F7's acceptance is that the DRC counts match."""
        for state in CardState:
            if state is CardState.WATCH:
                continue  # the genesis state, entered by creation
            assert any(state in targets for targets in ALLOWED.values()), state

    def test_every_illegal_edge_is_refused_and_names_itself(self):
        """ALL of them, enumerated from the table — not a sample."""
        refused = 0
        for frm in CardState:
            for to in CardState:
                if to in ALLOWED[frm]:
                    continue
                refused += 1
                assert not is_legal(frm, to)
                with pytest.raises(IllegalTransition) as excinfo:
                    assert_edge(frm, to, card_id=7)
                message = str(excinfo.value)
                assert frm.value in message and to.value in message
                assert "REFUSED" in message
        # 8 states x 8 targets = 64 pairs, 11 of which are legal.
        assert refused == 64 - sum(len(t) for t in ALLOWED.values()) == 53

    def test_terminal_refusal_explains_that_it_is_terminal(self):
        with pytest.raises(IllegalTransition) as excinfo:
            assert_edge(CardState.CLOSED, CardState.WATCH)
        assert "TERMINAL" in str(excinfo.value)

    def test_stop_editable_matches_decision_11(self):
        """Stop editable in WATCH and in-trade (FILLED); key frozen from
        ARMED onward."""
        assert STOP_EDITABLE == frozenset({CardState.WATCH, CardState.FILLED})
        assert CardState.ARMED not in STOP_EDITABLE

    def test_edge_table_markdown_is_generated_from_allowed(self):
        """The DevDocs page renders THIS — it cannot drift from the code."""
        table = edge_table_markdown()
        for state in CardState:
            assert f"`{state.value}`" in table
        assert "| `FILLED` | `CLOSED` | no |" in table
        assert "| `CLOSED` | — (none) | yes |" in table


# =====================================================================
# 2. The window resolver — no database needed
# =====================================================================


class TestWindowResolution:
    """Every `preferred_windows_ref` currently in the trade_defs.

    The asymmetry under test: falling back expires a card LATE
    (harmless), mis-resolving expires it EARLY (kills a live card). Both
    ambiguous refs must fall back.
    """

    @pytest.mark.parametrize(
        "ref,expected",
        [
            ("sheet: 10:00-13:30", "13:30"),
            ("Open 9:35-9:45 AM", "09:45"),
            ("Opening Auction 9:35-9:45 AM · Morning 9:45-11 AM", "11:00"),
            ("sheet: sets up before 9:59", "09:59"),
            ("sheet: break 11:00-13:30; DELL exemplar broke 14:00 — fit variable only", "14:00"),
        ],
    )
    def test_unambiguous_refs_resolve(self, ref, expected):
        got = expire_mod._resolve_window_end(ref)
        assert got is not None and got[0].strftime("%H:%M") == expected

    @pytest.mark.parametrize(
        "ref",
        [
            "First 15 minutes of the trading day",   # no clock time at all
            "First 5 minutes of the trading day",
            "sheet: 9:59-4:00",                       # "4:00" is 16:00 to a trader
            "Late morning 10:30-11:59 · Mid-day 12-2 PM · Power hour 3 PM-close",  # open tail
            None,
            "",
        ],
    )
    def test_ambiguous_refs_fall_back_rather_than_expire_early(self, ref):
        assert expire_mod._resolve_window_end(ref) is None

    def test_fallback_is_the_days_own_rth_close(self):
        """16:00 on a full day, 13:00 on an early close — read from the
        session clock's windows, so a half day needs no special case."""
        full = expire_mod.window_end_for(None, _et(2026, 9, 3, 0).date())
        early = expire_mod.window_end_for(None, _et(2026, 11, 27, 0).date())
        assert full.at.strftime("%H:%M") == "16:00" and full.source == "session_close"
        assert early.at.strftime("%H:%M") == "13:00" and early.source == "session_close"

    def test_expirable_states_all_have_an_expired_edge(self):
        """The job's target list cannot drift from the edge table."""
        for state in expire_mod.EXPIRABLE:
            assert CardState.EXPIRED in ALLOWED[state], state


# =====================================================================
# 3. The store — integration, inside the rolled-back transaction
# =====================================================================


def _make_card(store: AsetStore, ticker="TESTF7", *, now=None) -> int:
    result = compute_sizing(
        SizingInput(
            ticker=ticker,
            grade=Grade.B,
            direction=Direction.LONG,
            sheet_mode=SheetMode.FULL,
            risk_dollars=Decimal("60"),
            entry=Decimal("10.00"),
            stop=Decimal("9.50"),
            last_price=Decimal("10.01"),
            price_source="f7-test",
        ),
        [Grade.A, Grade.B],
        Decimal("10"),
    )
    card_id = store.save(result, now=now)
    if now is not None:
        # `created_at` carries a server-side now() default on purpose
        # (aset/store.py: both clocks are on this host, and a client
        # timestamp would trade a nonexistent skew for a real one). The
        # expiry job keys off the card's own TRADE DAY, so a test that
        # places a card on a specific day has to move `created_at` too —
        # `now=` only steers the session stamp and the ledger clock.
        with store._connect() as conn:
            conn.execute(
                "UPDATE aset_sizings SET created_at = %s WHERE id = %s", (now, card_id)
            )
    return card_id


@pytest.fixture
def stores():
    aset = AsetStore("cobalt_dev")
    cards = CardStore("cobalt_dev")
    cards.ensure_schema()
    return aset, cards


@requires_db
@pytest.mark.integration
class TestStateMachineIntegration:
    def test_a_new_card_is_born_in_watch_with_a_genesis_row(self, stores):
        """'No card exists without a state', at the write path."""
        aset, cards = stores
        card_id = _make_card(aset)
        assert cards.state_of(card_id) is CardState.WATCH
        history = cards.history(card_id)
        assert len(history) == 1
        assert history[0]["from_state"] is None
        assert history[0]["to_state"] == "WATCH"
        assert history[0]["actor"] == "cobalt"
        assert history[0]["session"] == "rth"     # the frozen clock's session

    def test_full_walk_watch_to_closed_writes_four_transition_rows(self, stores):
        aset, cards = stores
        card_id = _make_card(aset)
        for target in (CardState.ARMED, CardState.TRIGGERED, CardState.FILLED, CardState.CLOSED):
            cards.transition(card_id, target, actor=Actor.YOU, evidence={"step": target.value})

        assert cards.state_of(card_id) is CardState.CLOSED
        history = cards.history(card_id)
        moves = [r for r in history if r["from_state"] is not None]
        assert len(moves) == 4, "the walk is four transitions"
        assert [(r["from_state"], r["to_state"]) for r in moves] == [
            ("WATCH", "ARMED"),
            ("ARMED", "TRIGGERED"),
            ("TRIGGERED", "FILLED"),
            ("FILLED", "CLOSED"),
        ]
        assert len(history) == 5, "four moves plus the genesis row"
        assert all(r["session"] for r in history), "every row carries its session (F1)"
        assert all(r["actor"] in ("cobalt", "you") for r in history)

    def test_disarm_round_trip(self, stores):
        aset, cards = stores
        card_id = _make_card(aset)
        cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
        cards.transition(card_id, CardState.WATCH, actor=Actor.YOU, reason="level broke")
        assert cards.state_of(card_id) is CardState.WATCH
        # and it can be armed again
        cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
        assert cards.state_of(card_id) is CardState.ARMED
        moves = [r for r in cards.history(card_id) if r["from_state"]]
        assert [(r["from_state"], r["to_state"]) for r in moves] == [
            ("WATCH", "ARMED"), ("ARMED", "WATCH"), ("WATCH", "ARMED")
        ]

    def test_disarm_without_a_reason_is_refused(self, stores):
        aset, cards = stores
        card_id = _make_card(aset)
        cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
        with pytest.raises(CardStateError, match="reason is required"):
            cards.transition(card_id, CardState.WATCH, actor=Actor.YOU)
        assert cards.state_of(card_id) is CardState.ARMED, "the refused move changed nothing"

    def test_missed_requires_a_reason_and_is_counted_not_hidden(self, stores):
        aset, cards = stores
        card_id = _make_card(aset)
        with pytest.raises(CardStateError, match="reason is required"):
            cards.transition(card_id, CardState.MISSED, actor=Actor.YOU)
        cards.transition(
            card_id, CardState.MISSED, actor=Actor.YOU,
            reason="triggered while unarmed", evidence={"entry": "manual"},
        )
        assert cards.state_of(card_id) is CardState.MISSED
        row = cards.history(card_id)[-1]
        assert row["to_state"] == "MISSED" and row["reason"] == "triggered while unarmed"

    def test_an_illegal_move_leaves_no_row_and_no_state_change(self, stores):
        """Refused, never coerced — and nothing partial is written."""
        aset, cards = stores
        card_id = _make_card(aset)
        before = len(cards.history(card_id))
        with pytest.raises(IllegalTransition, match="WATCH -> FILLED"):
            cards.transition(card_id, CardState.FILLED, actor=Actor.YOU)
        assert cards.state_of(card_id) is CardState.WATCH
        assert len(cards.history(card_id)) == before

    def test_a_terminal_card_cannot_be_reopened(self, stores):
        aset, cards = stores
        card_id = _make_card(aset)
        cards.transition(card_id, CardState.PASSED, actor=Actor.YOU)
        with pytest.raises(IllegalTransition, match="TERMINAL"):
            cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)

    def test_stop_edit_is_not_a_state_change_but_rides_the_next_transition(self, stores):
        """Decision 11, both halves."""
        aset, cards = stores
        card_id = _make_card(aset)
        before = len(cards.history(card_id))
        cards.record_stop_edit(card_id, from_stop=Decimal("9.50"), to_stop=Decimal("9.62"))
        assert len(cards.history(card_id)) == before, "a stop edit writes NO transition row"
        assert cards.state_of(card_id) is CardState.WATCH

        cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
        evidence = cards.history(card_id)[-1]["evidence"]
        assert "stop_edits" in evidence
        assert evidence["stop_edits"][0]["to_stop"] == "9.6200"
        assert evidence["stop_edits"][0]["in_state"] == "WATCH"

    def test_stop_is_locked_from_armed_onward(self, stores):
        aset, cards = stores
        card_id = _make_card(aset)
        cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
        with pytest.raises(CardStateError, match="not editable in ARMED"):
            cards.record_stop_edit(card_id, from_stop=Decimal("9.50"), to_stop=Decimal("9.60"))

    def test_stop_is_editable_again_once_filled(self, stores):
        """In-trade: stops move with structure (decision 11)."""
        aset, cards = stores
        card_id = _make_card(aset)
        cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
        cards.transition(card_id, CardState.TRIGGERED, actor=Actor.YOU)
        cards.transition(card_id, CardState.FILLED, actor=Actor.YOU)
        cards.record_stop_edit(card_id, from_stop=Decimal("9.50"), to_stop=Decimal("9.80"))
        cards.transition(card_id, CardState.CLOSED, actor=Actor.YOU)
        evidence = cards.history(card_id)[-1]["evidence"]
        assert evidence["stop_edits"][0]["in_state"] == "FILLED"


# =====================================================================
# 4. F1 runs BEFORE any state logic
# =====================================================================


@requires_db
@pytest.mark.integration
class TestMarketResetRunsFirst:
    def test_a_transition_in_market_reset_is_refused_by_f1(self, stores, monkeypatch):
        aset, cards = stores
        card_id = _make_card(aset)
        blocked = datetime(2026, 9, 4, 0, 30, tzinfo=timezone.utc)  # 20:30 ET
        monkeypatch.setattr(clock_mod, "now_utc", lambda: blocked)

        with pytest.raises(SessionBlocked) as excinfo:
            cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
        assert "MARKET RESET" in str(excinfo.value)
        assert cards.state_of(card_id) is CardState.WATCH
        assert len(cards.history(card_id)) == 1, "no ledger row for a refused write"

    def test_f1_refuses_before_the_edge_is_even_checked(self, stores, monkeypatch):
        """The ORDER is the assertion. An ILLEGAL move inside
        market_reset must raise SessionBlocked, not IllegalTransition —
        proving F1 ran first and nothing downstream got to run at all."""
        aset, cards = stores
        card_id = _make_card(aset)
        blocked = datetime(2026, 9, 4, 0, 30, tzinfo=timezone.utc)
        monkeypatch.setattr(clock_mod, "now_utc", lambda: blocked)

        with pytest.raises(SessionBlocked):
            cards.transition(card_id, CardState.CLOSED, actor=Actor.YOU)  # WATCH->CLOSED, illegal

    def test_a_stop_edit_in_market_reset_is_refused_too(self, stores, monkeypatch):
        aset, cards = stores
        card_id = _make_card(aset)
        monkeypatch.setattr(
            clock_mod, "now_utc", lambda: datetime(2026, 9, 4, 0, 30, tzinfo=timezone.utc)
        )
        with pytest.raises(SessionBlocked):
            cards.record_stop_edit(card_id, from_stop=Decimal("9.50"), to_stop=Decimal("9.6"))


# =====================================================================
# 5. Expiry
# =====================================================================


@requires_db
@pytest.mark.integration
class TestExpiry:
    def test_expires_at_1605_on_a_full_day(self, stores):
        aset, cards = stores
        made = _et(2026, 9, 3, 10, 0)                   # Thursday, full day
        card_id = _make_card(aset, "EXPFULL", now=made)
        cards.transition(card_id, CardState.ARMED, actor=Actor.YOU, now=made)

        # 15:59 — still inside the window, nothing moves.
        assert expire_mod.expire_due(cards, now=_et(2026, 9, 3, 15, 59)) == []
        assert cards.state_of(card_id) is CardState.ARMED

        moved = expire_mod.expire_due(cards, now=_et(2026, 9, 3, 16, 5))
        assert [m["card_id"] for m in moved] == [card_id]
        assert cards.state_of(card_id) is CardState.EXPIRED
        row = cards.history(card_id)[-1]
        assert row["actor"] == "cobalt"
        assert row["evidence"]["window_source"] == "session_close"
        assert "16:00" in row["reason"]

    def test_expires_at_1305_on_the_2026_11_27_early_close(self, stores):
        aset, cards = stores
        made = _et(2026, 11, 27, 10, 0)                 # day after Thanksgiving
        card_id = _make_card(aset, "EXPHALF", now=made)

        # 12:59 — the half day's RTH is still open.
        assert expire_mod.expire_due(cards, now=_et(2026, 11, 27, 12, 59)) == []
        assert cards.state_of(card_id) is CardState.WATCH

        moved = expire_mod.expire_due(cards, now=_et(2026, 11, 27, 13, 5))
        assert [m["card_id"] for m in moved] == [card_id]
        assert cards.state_of(card_id) is CardState.EXPIRED
        assert "13:00" in cards.history(card_id)[-1]["reason"]

    def test_a_terminal_card_is_never_re_expired(self, stores):
        aset, cards = stores
        made = _et(2026, 9, 3, 10, 0)
        card_id = _make_card(aset, "EXPTERM", now=made)
        cards.transition(card_id, CardState.PASSED, actor=Actor.YOU, now=made)
        assert expire_mod.expire_due(cards, now=_et(2026, 9, 3, 16, 5)) == []

    def test_dry_run_reports_without_moving(self, stores):
        aset, cards = stores
        made = _et(2026, 9, 3, 10, 0)
        card_id = _make_card(aset, "EXPDRY", now=made)
        moved = expire_mod.expire_due(cards, now=_et(2026, 9, 3, 16, 5), dry_run=True)
        assert [m["card_id"] for m in moved] == [card_id]
        assert cards.state_of(card_id) is CardState.WATCH

    def test_a_trade_def_window_expires_earlier_than_the_session_close(self, stores):
        """The S2 seam: once a card carries a trade_def, its own window
        governs. Proven here with the resolver the detector will feed."""
        aset, cards = stores
        made = _et(2026, 9, 3, 10, 0)
        card_id = _make_card(aset, "EXPDEF", now=made)
        ref = lambda card: "sheet: 10:00-13:30"  # noqa: E731
        moved = expire_mod.expire_due(
            cards, now=_et(2026, 9, 3, 14, 0), trade_def_ref_for=ref
        )
        assert [m["card_id"] for m in moved] == [card_id]
        assert cards.history(card_id)[-1]["evidence"]["window_source"] == "trade_def"


# =====================================================================
# 6. Backfill
# =====================================================================


@requires_db
@pytest.mark.integration
class TestBackfill:
    def test_backfill_classifies_and_writes_one_genesis_row_each(self, stores):
        """status FILLED -> FILLED; older trade date -> EXPIRED; today ->
        WATCH. Each gets a genesis row marked as a backfill."""
        aset, cards = stores
        made = _et(2026, 9, 3, 10, 0)
        ids = {}
        for name in ("BFOLD", "BFTODAY", "BFFILL"):
            ids[name] = _make_card(aset, name, now=made)

        today = made.date()
        with cards._connect() as conn:
            # Reproduce the PRE-F7 shape these rows were written in:
            # `state` nullable and NULL. Migration 0007's NOT NULL exists
            # precisely so this shape cannot occur again, so the test has
            # to drop it to recreate the state the backfill was written
            # for. DDL is transactional in Postgres and the conftest rolls
            # the whole test back, so the constraint returns on its own.
            conn.execute("ALTER TABLE aset_sizings ALTER COLUMN state DROP NOT NULL")
            conn.execute(
                "DELETE FROM card_transitions WHERE card_id = ANY(%s)", (list(ids.values()),)
            )
            conn.execute(
                "UPDATE aset_sizings SET state = NULL, state_at = NULL WHERE id = ANY(%s)",
                (list(ids.values()),),
            )
            conn.execute(
                "UPDATE aset_sizings SET created_at = %s WHERE id = %s",
                (_et(2026, 9, 2, 10, 0), ids["BFOLD"]),
            )
            conn.execute(
                "UPDATE aset_sizings SET status = 'FILLED' WHERE id = %s", (ids["BFFILL"],)
            )

        counts = cards.backfill(today=today)
        assert counts["_total"] >= 3

        assert cards.state_of(ids["BFOLD"]) is CardState.EXPIRED
        assert cards.state_of(ids["BFTODAY"]) is CardState.WATCH
        assert cards.state_of(ids["BFFILL"]) is CardState.FILLED

        for card_id in ids.values():
            history = cards.history(card_id)
            assert len(history) == 1, "a backfilled card gets ONE genesis row, not a fake walk"
            assert history[0]["from_state"] is None
            assert history[0]["evidence"]["backfill"] == BACKFILL_MARKER
            assert history[0]["actor"] == "cobalt"

    def test_backfill_dry_run_writes_nothing(self, stores):
        aset, cards = stores
        card_id = _make_card(aset, "BFDRY", now=_et(2026, 9, 3, 10, 0))
        with cards._connect() as conn:
            conn.execute("ALTER TABLE aset_sizings ALTER COLUMN state DROP NOT NULL")
            conn.execute("DELETE FROM card_transitions WHERE card_id = %s", (card_id,))
            conn.execute("UPDATE aset_sizings SET state = NULL WHERE id = %s", (card_id,))
        cards.backfill(today=_et(2026, 9, 3, 10, 0).date(), dry_run=True)
        with cards._connect() as conn:
            row = conn.execute(
                "SELECT state FROM aset_sizings WHERE id = %s", (card_id,)
            ).fetchone()
        assert row[0] is None
