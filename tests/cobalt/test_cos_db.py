"""F20 C3a — the turn and session tables on `cobalt_dev` (FINAL §2 `cos/store.py`, F-20; L18; T11).

WITH-DB, inside the suite's rollback transaction: the module tables exist
only for the test. Constructed message refs (L32).
"""

from __future__ import annotations

import os

import psycopg
import pytest

pytestmark = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


@pytest.fixture
def store():
    from cobalt.cos.store import CosStore

    s = CosStore()
    s.ensure_schema()
    return s


def test_message_ref_is_unique(store):
    from cobalt import db, env
    from cobalt.db_migrations.placement import side_of

    store.insert_turn("constructedpostid000000001")
    with pytest.raises(psycopg.errors.UniqueViolation):
        store.insert_turn("constructedpostid000000001")
    with db.connect(env.resolve_db_name(), side=db.Side.USER) as conn:
        found = dict(conn.execute(
            "SELECT table_name, table_schema FROM information_schema.tables "
            "WHERE table_name IN ('cobalt_cos_turns', 'cobalt_cos_sessions')"
        ).fetchall())
    assert found == {"cobalt_cos_turns": "user", "cobalt_cos_sessions": "user"}
    assert side_of("cobalt_cos_turns").schema == "user" and side_of("cobalt_cos_sessions").schema == "user"


def test_turn_states(store):
    turn = store.insert_turn("constructedpostid000000002")
    assert store.turn(turn)["state"] == "pending"
    store.set_turn(turn, "running")
    assert store.turn(turn)["state"] == "running" and store.turn(turn)["started_at"] is not None
    store.set_turn(turn, "done", num_turns=2, result_subtype="success", is_error=False,
                   terminal_reason="completed")
    row = store.turn(turn)
    assert row["state"] == "done" and row["finished_at"] is not None and row["num_turns"] == 2
    with pytest.raises((psycopg.errors.CheckViolation, ValueError)):
        store.set_turn(turn, "bogus")

    store.save_session("dm", "cos", "constructed-session-1", "active")
    assert store.session("dm", "cos")["session_id"] == "constructed-session-1"
    store.save_session("dm", "cos", "constructed-session-2", "active")
    assert store.session("dm", "cos")["session_id"] == "constructed-session-2"
