"""`realized_r.1` (S3 exits v3 §3, C2-5) — offline, on constructed legs.

R_unit = |entry.price − entry.stop_in_force|; per current exit
`sign × (exit.price − entry.price) × exit.shares ÷ (entry.shares × R_unit)`,
summed; `provisional` while any current leg is `estimated`; a zero unit is
`not computed — zero risk unit`, never a division. Never stored.
Every price here is constructed (L32).
"""

from __future__ import annotations

from decimal import Decimal


def _entry(price="10.00", stop="9.90", shares=100, flag="confirmed"):
    return dict(seq=0, kind="entry", price=Decimal(price), stop_in_force=Decimal(stop),
                shares=shares, flag=flag)


def _exit(seq, price, shares, flag="confirmed"):
    return dict(seq=seq, kind="exit", price=Decimal(price), stop_in_force=Decimal("9.90"),
                shares=shares, flag=flag)


def test_long_realized_r_sums_the_current_exits_on_the_actual_unit():
    from cobalt.cards.legs import realized_r

    r = realized_r({"direction": "long"}, [_entry(), _exit(1, "10.20", 50), _exit(2, "10.10", 50)])
    # (0.20 x 50 + 0.10 x 50) / (100 x 0.10) = 1.5
    assert r.value == Decimal("1.5")
    assert r.r_unit == Decimal("0.10")
    assert r.provisional is False and r.reason is None
    assert r.function_id == "realized_r.1"


def test_short_realized_r_takes_its_sign_from_the_card_direction():
    from cobalt.cards.legs import realized_r

    entry = _entry(price="10.00", stop="10.10")
    r = realized_r({"direction": "short"}, [entry, _exit(1, "9.80", 100)])
    # -1 x (9.80 - 10.00) x 100 / (100 x 0.10) = 2.0
    assert r.value == Decimal("2")


def test_any_estimated_current_leg_makes_it_provisional():
    from cobalt.cards.legs import realized_r

    r = realized_r({"direction": "long"}, [_entry(), _exit(1, "10.20", 50, flag="estimated")])
    assert r.provisional is True and r.value == Decimal("1")
    r = realized_r({"direction": "long"}, [_entry(flag="estimated"), _exit(1, "10.20", 50)])
    assert r.provisional is True


def test_a_zero_risk_unit_is_not_computed_never_divided():
    from cobalt.cards.legs import realized_r

    r = realized_r({"direction": "long"}, [_entry(price="10.00", stop="10.00"), _exit(1, "10.20", 50)])
    assert r.value is None and r.reason == "not computed — zero risk unit"


def test_no_entry_leg_is_not_computed():
    from cobalt.cards.legs import realized_r

    r = realized_r({"direction": "long"}, [_exit(1, "10.20", 50)])
    assert r.value is None and r.reason == "not computed — no entry leg"


def test_no_exit_yet_is_zero_realized():
    from cobalt.cards.legs import realized_r

    r = realized_r({"direction": "long"}, [_entry()])
    assert r.value == Decimal("0") and r.provisional is False
