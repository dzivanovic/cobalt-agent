"""Shared with-DB helpers for the S3 C1 tests (legs, the one fill).

`apply_0021` runs M1 INSIDE the suite's rollback transaction (the
`test_stale_score_db._apply_0015_in_the_suite_transaction` precedent), so
these tests hold at `0013` and at `0021` alike and leave nothing applied
(L76). Every value is constructed (L32): ticker `TEST`, entry 10.0000 /
stop 9.9000 are the design's X15 figures.
"""

from __future__ import annotations

from decimal import Decimal
from typing import Any

from cobalt.aset.engine import compute_sizing
from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput

ENTRY = Decimal("10.0000")
STOP = Decimal("9.9000")


class Settings:
    """A constructed settings store (L69): `values()` only."""

    def __init__(self, values):
        self._values = dict(values)

    def values(self):
        return dict(self._values)


def offline_daymode_config():
    """The sheet tests' offline ladder: sheets half/full, reduced -> half,
    so `half.htk` is the matching attestation."""
    from cobalt.aset.models import Grade
    from cobalt.daymode.config import SIGNAL_IDS, DayModeConfig

    return DayModeConfig(
        reduced_sheet="half",
        reduced_enabled_grades=[Grade.A, Grade.B],
        enabled_modes=["reduced"],
        hotkey_file_template="{sheet}.htk",
        stepdowns=[{"signal": s, "effect": "none", "because": "offline fixture"} for s in SIGNAL_IDS],
        sheet_order=["half", "full"],
        account_enabled_grades=[Grade.A, Grade.B],
    )


def patch_daymode(monkeypatch) -> None:
    from cobalt.daymode import config as daymode_config

    monkeypatch.setattr(daymode_config, "load_daymode_config", lambda *a, **k: offline_daymode_config())


def fill_kwargs(price: str = "10.10", shares: int = 50, p=20, **over) -> dict[str, Any]:
    kwargs = dict(
        price=Decimal(price), shares=shares, flag="confirmed", price_source="typed",
        price_asof=None, source="sheet",
        drift_settings=Settings({} if p is None else {"fills.drift_warning_pct": p}),
    )
    kwargs.update(over)
    return kwargs


def apply_0021(store) -> None:
    from cobalt.db_migrations import MIGRATIONS_DIR

    with store._connect() as conn:
        conn.execute((MIGRATIONS_DIR / "0021_legs.sql").read_text())


def sizing(entry: Decimal = ENTRY, stop: Decimal = STOP, risk: str = "60"):
    return compute_sizing(
        SizingInput(
            ticker="TEST", grade=Grade.B, direction=Direction.LONG,
            sheet_mode=SheetMode.FULL, risk_dollars=Decimal(risk), entry=entry, stop=stop,
        ),
        (Grade.A, Grade.B),
        Decimal("10"),
    )


def manual_card(aset, *, triggered: bool = True) -> int:
    """A manual card saved through the sheet's own `save()`; walked to
    TRIGGERED by his taps when `triggered`."""
    from cobalt.cards.models import Actor, CardState
    from cobalt.cards.store import CardStore

    card_id = aset.save(sizing())
    if triggered:
        cards = CardStore(aset.db_name)
        cards.transition(card_id, CardState.ARMED, actor=Actor.YOU)
        cards.transition(card_id, CardState.TRIGGERED, actor=Actor.YOU)
    return card_id


def card_row(store, card_id: int) -> dict[str, Any]:
    with store._connect() as conn:
        cur = conn.execute("SELECT * FROM aset_sizings WHERE id = %s", (card_id,))
        return dict(zip([d.name for d in cur.description], cur.fetchone()))


def legs_of(store, card_id: int) -> list[dict[str, Any]]:
    with store._connect() as conn:
        cur = conn.execute("SELECT * FROM legs WHERE card_id = %s ORDER BY id", (card_id,))
        return [dict(zip([d.name for d in cur.description], r)) for r in cur.fetchall()]


def insert_leg_sql(conn, card_id: int, **over) -> int:
    """A raw INSERT (the DDL tests only — the store writes through
    `cobalt.cards.legs`)."""
    from cobalt.session import clock

    values = dict(
        card_id=card_id, seq=0, kind="entry", shares=100, price=ENTRY, at=clock.now_utc(),
        flag="confirmed", price_source="typed", price_asof=None, preset=None, running_before=0,
        stop_in_force=STOP, source="sheet", source_import_id=None, held_stated=None,
        corrects=None, session="rth", account_mode="sim", day_mode_id=None,
        attested_sheet=None, sheet_mismatch=True,
    )
    values.update(over)
    columns = list(values)
    row = conn.execute(
        f"INSERT INTO legs ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))}) "
        "RETURNING id",
        [values[c] for c in columns],
    ).fetchone()
    return int(row[0])


def exit_leg(**over) -> dict[str, Any]:
    base = dict(seq=1, kind="exit", shares=50, preset="half", running_before=100,
                sheet_mismatch=None, flag="estimated", price_source="last_poll", source="panel")
    base.update(over)
    return base
