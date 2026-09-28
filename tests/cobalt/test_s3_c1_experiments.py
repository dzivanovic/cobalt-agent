"""S3 exits C1 — the first-gate experiments (v3 First-gate table; L70).

Run BEFORE any src edit. Each test is one experiment row of the C1 build
report (`## E1 EXPERIMENTS`): X9, X6, X10, X15 and X-S. Constructed values
only (L32): ticker `TEST`, entry 10.0000 / stop 9.9000 are the design's own
X15 figures, not his.

X9, X6 and X10 are with-DB (inside the suite's rollback transaction); X15
and X-S are offline.
"""

from __future__ import annotations

import os
from decimal import Decimal

import pytest

from cobalt.aset.engine import compute_fill_recompute, compute_sizing
from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


def _sizing(entry: str = "10.0000", stop: str = "9.9000", risk: str = "60"):
    return compute_sizing(
        SizingInput(
            ticker="TEST", grade=Grade.B, direction=Direction.LONG,
            sheet_mode=SheetMode.FULL, risk_dollars=Decimal(risk),
            entry=Decimal(entry), stop=Decimal(stop),
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )


# ---------------------------------------------------------------------
# X15 — offline: the Charter's "27 % past plan" figure
# ---------------------------------------------------------------------


@pytest.mark.parametrize("fill", ["10.0270", "9.9730"])
def test_x15_distance_change_pct_is_27_on_both_sides(fill):
    original = _sizing()
    # C1-5: the P is the caller's (his setting); X15 is about the figure,
    # so P is left unevaluated here.
    recompute = compute_fill_recompute(original, Decimal(fill), Decimal("5"), drift_warning_pct=None)
    assert recompute.distance_change_pct == Decimal("27.00")


# ---------------------------------------------------------------------
# X-S — offline: can `cobalt settings load` carry fills.drift_warning_pct
# without an edit to settings/models.py?
# ---------------------------------------------------------------------


def test_xs_the_optional_load_path_refuses_the_drift_key(tmp_path):
    from cobalt.settings.cli import load_optional_file
    from cobalt.settings.models import TraderSettingsError

    path = tmp_path / "optional.yaml"
    path.write_text("optional_settings:\n  fills.drift_warning_pct: 20\n", encoding="utf-8")
    with pytest.raises(TraderSettingsError, match="unknown optional setting 'fills.drift_warning_pct'"):
        load_optional_file(path, sha256=None, require_hash=False)


def test_xs_the_card_load_path_refuses_the_drift_key(tmp_path):
    from cobalt.settings.card import load_card_file
    from cobalt.settings.models import TraderSettingsError

    path = tmp_path / "card.yaml"
    path.write_text("fills.drift_warning_pct: 20\n", encoding="utf-8")
    with pytest.raises(TraderSettingsError, match="unknown card setting 'fills.drift_warning_pct'"):
        load_card_file(path, expected_sha256=None)


# ---------------------------------------------------------------------
# X9 — with-DB: create_state is genesis only
# ---------------------------------------------------------------------


@requires_db
def test_x9_create_state_refuses_a_card_that_already_has_a_state():
    import psycopg

    from cobalt.aset.store import AsetStore
    from cobalt.cards.models import CardState
    from cobalt.cards.store import CardStore

    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    card_id = store.save(_sizing())
    cards = CardStore("cobalt_dev")
    assert cards.state_of(card_id) is CardState.WATCH
    with pytest.raises(psycopg.errors.UniqueViolation):
        cards.create_state(card_id, CardState.FILLED)
    assert cards.state_of(card_id) is CardState.WATCH
    assert [h["to_state"] for h in cards.history(card_id)] == ["WATCH"]


# ---------------------------------------------------------------------
# X6 — with-DB: a manual card has no structural stop
# ---------------------------------------------------------------------


@requires_db
def test_x6_a_manual_card_has_a_null_structural_stop():
    from cobalt.aset.store import AsetStore

    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    card_id = store.save(_sizing())
    with store._connect() as conn:
        origin, structural_stop = conn.execute(
            "SELECT origin, structural_stop FROM aset_sizings WHERE id = %s", (card_id,)
        ).fetchone()
    assert origin == "manual"
    assert structural_stop is None


# ---------------------------------------------------------------------
# X10 — with-DB: from_card equals compute_sizing of the stored inputs
# ---------------------------------------------------------------------


@requires_db
def test_x10_from_card_equals_compute_sizing_of_the_stored_inputs():
    from cobalt.aset.models import SizingResult
    from cobalt.aset.store import AsetStore

    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    card_id = store.save(_sizing(entry="10.0000", stop="9.9000", risk="60"))
    with store._connect() as conn:
        cur = conn.execute("SELECT * FROM aset_sizings WHERE id = %s", (card_id,))
        row = dict(zip([d.name for d in cur.description], cur.fetchone()))

    rebuilt = SizingResult.from_card(row)
    recomputed = compute_sizing(
        SizingInput(
            ticker=row["ticker"], grade=Grade(row["grade"]), direction=Direction(row["direction"]),
            sheet_mode=SheetMode(row["sheet_mode"]), risk_dollars=row["risk_budget"],
            entry=row["entry"], stop=row["stop"],
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )
    assert rebuilt.per_share_risk == recomputed.per_share_risk
    assert rebuilt.shares == recomputed.shares
