"""S-LEGS as built — `"user".legs` and `legs_current_v` (M1 `0021`; X4).

Every test applies `0021` inside the suite's rollback transaction
(`legs_db_support.apply_0021`) and writes raw rows: these are the DDL's
own guarantees, the ones no writer can be trusted to keep (the trigger,
the partial unique indexes, the CHECKs, the view, the tenant default).
"""

from __future__ import annotations

import os

import psycopg
import pytest

from legs_db_support import apply_0021, exit_leg, insert_leg_sql, manual_card

pytestmark = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


@pytest.fixture
def world():
    from cobalt.aset.store import AsetStore

    aset = AsetStore("cobalt_dev")
    aset.ensure_schema()
    apply_0021(aset)
    return aset, manual_card(aset, triggered=False)


def _refused(aset, error, fn):
    with pytest.raises(error):
        with aset._connect() as conn:
            fn(conn)


def test_an_update_is_refused_by_the_append_only_trigger(world):
    aset, card = world
    with aset._connect() as conn:
        leg = insert_leg_sql(conn, card)
    _refused(aset, psycopg.errors.RaiseException,
             lambda c: c.execute("UPDATE legs SET price = 11 WHERE id = %s", (leg,)))


def test_a_second_original_of_one_seq_is_refused_by_the_index(world):
    aset, card = world
    with aset._connect() as conn:
        insert_leg_sql(conn, card)
        insert_leg_sql(conn, card, **exit_leg())
    _refused(aset, psycopg.errors.UniqueViolation,
             lambda c: insert_leg_sql(c, card, **exit_leg(shares=10)))


def test_a_second_original_entry_is_refused_whatever_its_seq(world):
    aset, card = world
    with aset._connect() as conn:
        insert_leg_sql(conn, card)
    _refused(aset, psycopg.errors.UniqueViolation,
             lambda c: insert_leg_sql(c, card, seq=7))


def test_a_correction_and_a_correction_of_a_correction_are_accepted_and_the_view_shows_one_row_per_seq(world):
    aset, card = world
    with aset._connect() as conn:
        entry = insert_leg_sql(conn, card)
        exit1 = insert_leg_sql(conn, card, **exit_leg())
        fix1 = insert_leg_sql(conn, card, **exit_leg(corrects=exit1, price=10.2, flag="confirmed"))
        fix2 = insert_leg_sql(conn, card, **exit_leg(corrects=fix1, price=10.3, flag="confirmed"))
        rows = conn.execute(
            "SELECT seq, id FROM legs_current_v WHERE card_id = %s ORDER BY seq", (card,)
        ).fetchall()
    assert rows == [(0, entry), (1, fix2)]


def test_user_id_defaults_from_the_tenant_guc(world):
    aset, card = world
    with aset._connect() as conn:
        leg = insert_leg_sql(conn, card)
        user_id, guc = conn.execute(
            "SELECT user_id, current_setting('cobalt.trader_id')::int FROM legs WHERE id = %s", (leg,)
        ).fetchone()
    assert user_id == guc


def test_a_trading_log_row_needs_its_import_id_and_no_other_source_carries_one(world):
    aset, card = world
    _refused(aset, psycopg.errors.CheckViolation,
             lambda c: insert_leg_sql(c, card, source="trading_log"))
    _refused(aset, psycopg.errors.CheckViolation,
             lambda c: insert_leg_sql(c, card, source="sheet", source_import_id=1))
    with aset._connect() as conn:
        insert_leg_sql(conn, card, source="trading_log", price_source="trading_log", source_import_id=1)


def test_held_stated_lives_only_on_an_entry_correction(world):
    aset, card = world
    with aset._connect() as conn:
        entry = insert_leg_sql(conn, card)
    _refused(aset, psycopg.errors.CheckViolation,
             lambda c: insert_leg_sql(c, card, **exit_leg(held_stated=40)))
    _refused(aset, psycopg.errors.CheckViolation,
             lambda c: insert_leg_sql(c, card, seq=0, held_stated=40))
    with aset._connect() as conn:
        insert_leg_sql(conn, card, corrects=entry, held_stated=40, sheet_mismatch=None)


def test_sheet_mismatch_is_on_the_original_entry_and_nowhere_else(world):
    aset, card = world
    _refused(aset, psycopg.errors.CheckViolation,
             lambda c: insert_leg_sql(c, card, sheet_mismatch=None))
    with aset._connect() as conn:
        entry = insert_leg_sql(conn, card, sheet_mismatch=False)
    _refused(aset, psycopg.errors.CheckViolation,
             lambda c: insert_leg_sql(c, card, **exit_leg(sheet_mismatch=True)))
    _refused(aset, psycopg.errors.CheckViolation,
             lambda c: insert_leg_sql(c, card, corrects=entry, sheet_mismatch=False))


def test_the_value_checks_hold(world):
    aset, card = world
    for bad in (dict(shares=0), dict(price=0), dict(kind="scale"), dict(flag="maybe"),
                dict(price_source="guess"), dict(preset="quarter"), dict(running_before=-1),
                dict(source="voice")):
        _refused(aset, psycopg.errors.CheckViolation, lambda c, bad=bad: insert_leg_sql(c, card, **bad))


def test_card_stop_edits_kind_defaults_to_edit_and_refuses_anything_else(world):
    aset, card = world
    with aset._connect() as conn:
        kind = conn.execute(
            "INSERT INTO card_stop_edits (card_id, session, in_state, from_stop, to_stop, actor) "
            "VALUES (%s, 'rth', 'WATCH', 9.9, 9.8, 'you') RETURNING kind", (card,)
        ).fetchone()[0]
    assert kind == "edit"
    _refused(aset, psycopg.errors.CheckViolation, lambda c: c.execute(
        "INSERT INTO card_stop_edits (card_id, session, in_state, from_stop, to_stop, actor, kind) "
        "VALUES (%s, 'rth', 'WATCH', 9.9, 9.8, 'you', 'undo')", (card,)))


def test_0021_applies_twice(world):
    aset, _ = world
    apply_0021(aset)  # idempotent: a second forward is a no-op
