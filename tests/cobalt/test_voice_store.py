"""C9 — migration 0017 `"user".voice_turns` and the turn store (FINAL §2, §5, §7, W10).

The row IS the task row (L18): a state machine with single-flight SQL
transitions (`UPDATE … WHERE state = ANY(<expected>) RETURNING`), a reaper,
never fire-and-forget. USER side (L32 tenancy: `user_id NOT NULL` + FK +
the GUC default, like every user table). NOT session-gated (FINAL [F-16],
the `jobs/store.py` precedent). NO bytes of any kind: no `bytea`, no large
object, no audio column — asserted over `information_schema` AND
`pg_catalog` (L35 P-e: a scoped catalog view is never proof of absence).

Offline half: the SQL text, placement, registration, the store's SQL.
`requires_db` half: apply + roll back on `cobalt_dev` inside a migration
transaction that is rolled back, the no-bytes catalog check, the store
round trip, single-flight under TWO REAL connections, the reaper.
"""

from __future__ import annotations

import os
import re
import threading
import uuid
from datetime import datetime, timedelta, timezone

import pytest

from cobalt import db, env
from cobalt.db import Side
from cobalt.db_migrations import FORWARD, MIGRATIONS_DIR, REVERSE
from cobalt.db_migrations.cli import _apply, _rollback_paths
from cobalt.db_migrations.placement import CREATED_TABLES, PLACEMENT, side_of
from cobalt.voice import store as vs
from cobalt.voice.models import TurnState

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

#: The UNPATCHED factory (conftest's `dev_db_tx` replaces `db.connect`
#: during every test; module import happens before any fixture runs).
RAW_CONNECT = db.connect

SQL = MIGRATIONS_DIR / "0017_voice_turns.sql"
ROLLBACK = MIGRATIONS_DIR / "0017_voice_turns.rollback.sql"


def _code(path) -> str:
    return "\n".join(l for l in path.read_text().splitlines() if not l.strip().startswith("--"))


# --- the migration text -------------------------------------------------------------


def test_both_files_exist_and_are_registered_last_and_first():
    assert SQL.exists() and ROLLBACK.exists()
    # S3 exits C1's 0021 now follows it (registered last / reversed first).
    assert FORWARD[-2] == SQL and REVERSE[1] == ROLLBACK
    assert [p.name for p in _rollback_paths("0015")] == [
        "0021_legs.rollback.sql", "0017_voice_turns.rollback.sql"]


def test_the_table_is_user_side_with_the_tenancy_shape():
    code = _code(SQL)
    assert 'CREATE TABLE IF NOT EXISTS "user".voice_turns' in code
    assert re.search(r"user_id\s+INTEGER NOT NULL\s+DEFAULT \(current_setting\('cobalt\.trader_id'\)::int\)\s+"
                     r'REFERENCES "user"\.traders\(id\)', code)
    assert 'ALTER TABLE "user".voice_turns OWNER TO cobalt_user;' in code
    assert side_of("voice_turns") is Side.USER and CREATED_TABLES["voice_turns"] is Side.USER
    assert PLACEMENT["voice_turns"] is Side.USER


def test_the_state_check_is_exactly_the_final_state_machine():
    m = re.search(r"state\s+TEXT NOT NULL\s+CHECK \(state IN \(([^)]*)\)\)", _code(SQL))
    assert m, "the state CHECK is the domain; it must be in the DDL"
    assert {s.strip().strip("'") for s in m.group(1).split(",")} == {s.value for s in TurnState}


def test_the_source_and_input_checks():
    code = _code(SQL)
    assert re.search(r"source\s+TEXT NOT NULL\s+CHECK \(source IN \('widget', 'cli', 'test'\)\)", code)
    assert re.search(r"input_kind\s+TEXT NOT NULL\s+CHECK \(input_kind IN \('audio', 'text'\)\)", code)


@pytest.mark.parametrize("column", [
    "turn_id", "session_id", "source", "state", "input_kind", "audio_sha256", "audio_bytes",
    "audio_duration_ms", "audio_deleted_at", "transcript", "stt_engine", "stt_model", "stt_revision",
    "stt_ms", "plan", "plan_route", "model_returned", "plan_latency_ms", "plan_usage", "resolution",
    "reply", "pending_action", "confirm_of", "expert_write_kind", "expert_write_id", "failure_class",
    "failure_detail", "received_at", "transcribing_at", "planned_at", "answered_at", "awaiting_confirm_at",
    "executing_at", "done_at", "failed_at", "cancelled_at", "expired_at", "unsupported_at", "updated_at",
])
def test_every_column_the_design_names(column):
    assert re.search(rf"^\s+{column}\s", _code(SQL), re.M), column


def test_no_bytes_of_any_kind_in_the_ddl_or_the_voice_code():
    for text in (_code(SQL).lower(), _code(ROLLBACK).lower()):
        for forbidden in ("bytea", "lo_import", "large object", " oid", "lo_create", "blob"):
            assert forbidden not in text, forbidden


def test_every_create_is_idempotent_and_touches_nothing_else():
    code = _code(SQL)
    for kind, rest in re.findall(r"CREATE (TABLE|UNIQUE INDEX|INDEX)([^;]*);", code):
        assert "IF NOT EXISTS" in rest, rest
    for forbidden in ("DROP ", "DELETE ", "UPDATE ", "aset_sizings", "card_stop_edits"):
        assert forbidden not in code, forbidden


def test_the_rollback_drops_only_its_own_table():
    code = _code(ROLLBACK)
    assert 'DROP TABLE IF EXISTS "user".voice_turns' in code
    assert code.count("DROP") == 1


# --- the store's SQL ----------------------------------------------------------------------


def test_transitions_are_single_flight_sql():
    assert re.search(r"UPDATE voice_turns SET .* WHERE turn_id = %s AND state = ANY\(%s\) RETURNING",
                     vs.TRANSITION_SQL_TEMPLATE, re.S)


def test_the_store_is_user_side_and_not_session_gated():
    import inspect

    assert vs.VoiceTurnStore.SIDE is Side.USER
    src = inspect.getsource(vs)
    assert "assert_writable" not in src and "_session_gate" not in src


def test_the_store_names_only_its_own_side():
    import inspect

    named = re.findall(r"\b(?:FROM|JOIN|INTO|UPDATE|TABLE)\s+(\"?[A-Za-z_][A-Za-z0-9_]*\"?(?:\.\w+)?)",
                       inspect.getsource(vs), re.I)
    for raw in named:
        name = raw.strip('"')
        if name in PLACEMENT:
            assert PLACEMENT[name] is Side.USER, name


def test_update_columns_are_a_closed_list_without_bytes():
    assert "audio" not in {c for c in vs.UPDATABLE if c.startswith("audio_") and c not in (
        "audio_sha256", "audio_bytes", "audio_duration_ms", "audio_deleted_at")}
    with pytest.raises(ValueError):
        vs._set_clause({"audio_blob": b"x"})


def test_reap_limits_follow_the_state_machine():
    lim = vs.reap_limits(stt_timeout_s=20, plan_timeout_s=60)
    assert set(lim) == {TurnState.RECEIVED, TurnState.TRANSCRIBING, TurnState.PLANNED, TurnState.EXECUTING}
    assert lim[TurnState.TRANSCRIBING] > lim[TurnState.RECEIVED] > 60


# --- requires_db ---------------------------------------------------------------------------


def _migration_conn():
    conn = db.connect_migration(env.DEV_DB_NAME)
    conn.autocommit = False
    return conn


NO_BYTES_SQL_INFO = """
    SELECT column_name, data_type FROM information_schema.columns
     WHERE table_schema = 'user' AND table_name = 'voice_turns'
       AND (data_type IN ('bytea', 'oid') OR udt_name IN ('bytea', 'oid', 'lo'))
"""
NO_BYTES_SQL_CATALOG = """
    SELECT a.attname, t.typname FROM pg_catalog.pg_attribute a
      JOIN pg_catalog.pg_class c ON c.oid = a.attrelid
      JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
      JOIN pg_catalog.pg_type t ON t.oid = a.atttypid
     WHERE n.nspname = 'user' AND c.relname = 'voice_turns' AND a.attnum > 0 AND NOT a.attisdropped
"""


@requires_db
def test_forward_creates_the_table_user_side_and_rollback_drops_it_cleanly():
    conn = _migration_conn()
    try:
        _apply(conn, FORWARD)
        assert conn.execute("SELECT to_regclass('\"user\".voice_turns')").fetchone()[0]
        assert conn.execute("SELECT to_regclass('system.voice_turns')").fetchone()[0] is None
        _apply(conn, FORWARD)  # idempotent
        _apply(conn, _rollback_paths("0015"))
        assert conn.execute("SELECT to_regclass('\"user\".voice_turns')").fetchone()[0] is None
        assert conn.execute("SELECT to_regclass('\"user\".aset_sizings')").fetchone()[0], "rollback touched another table"
    finally:
        conn.rollback()
        conn.close()


@requires_db
def test_no_bytes_column_in_either_catalog():
    conn = _migration_conn()
    try:
        _apply(conn, FORWARD)
        assert conn.execute(NO_BYTES_SQL_INFO).fetchall() == []
        types = conn.execute(NO_BYTES_SQL_CATALOG).fetchall()
        assert types, "pg_catalog sees no columns — the unscoped read must see the table"
        assert not [t for t in types if t[1] in ("bytea", "oid", "lo")], types
    finally:
        conn.rollback()
        conn.close()


def _now():
    return datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)


@requires_db
def test_store_round_trip_and_single_flight_in_the_suite_transaction():
    s = vs.VoiceTurnStore()
    tid = f"t-{uuid.uuid4().hex[:12]}"
    s.create(turn_id=tid, session_id="sess-constructed", source="test", input_kind="text", at=_now())
    assert s.get(tid)["state"] == "received"
    assert s.transition(tid, {TurnState.RECEIVED}, TurnState.PLANNED, at=_now(), transcript="constructed words")
    assert not s.transition(tid, {TurnState.RECEIVED}, TurnState.PLANNED, at=_now())
    assert s.transition(tid, {TurnState.PLANNED}, TurnState.AWAITING_CONFIRM, at=_now(),
                        pending_action={"tool": "cards.set_stop"}, reply="read back")
    assert s.pending_for_session("sess-constructed")["turn_id"] == tid
    assert s.transition(tid, {TurnState.AWAITING_CONFIRM}, TurnState.CANCELLED, at=_now())
    assert not s.transition(tid, {TurnState.AWAITING_CONFIRM}, TurnState.EXECUTING, at=_now())
    row = s.get(tid)
    assert row["state"] == "cancelled" and row["cancelled_at"] is not None and row["transcript"] == "constructed words"


@requires_db
def test_the_reaper_fails_stale_rows_and_never_retries(monkeypatch):
    s = vs.VoiceTurnStore()
    old = _now() - timedelta(hours=1)
    ids = {}
    for state in (TurnState.TRANSCRIBING, TurnState.PLANNED, TurnState.EXECUTING):
        tid = f"t-{uuid.uuid4().hex[:12]}"
        s.create(turn_id=tid, session_id="sess-reap", source="test", input_kind="audio", at=old)
        path = {TurnState.TRANSCRIBING: [TurnState.TRANSCRIBING],
                TurnState.PLANNED: [TurnState.PLANNED],
                TurnState.EXECUTING: [TurnState.PLANNED, TurnState.AWAITING_CONFIRM, TurnState.EXECUTING]}[state]
        prev = {TurnState.RECEIVED}
        for step in path:
            assert s.transition(tid, prev, step, at=old)
            prev = {step}
        ids[state] = tid
    reaped = s.reap(now=_now(), limits=vs.reap_limits(stt_timeout_s=20, plan_timeout_s=60))
    assert {t for t, _ in reaped} >= set(ids.values())
    for state, tid in ids.items():
        row = s.get(tid)
        assert row["state"] == "failed" and row["failure_class"] == f"reaped_{state.value}"
    # a reaped executing row is never retried: nothing moves it out of failed
    assert not s.transition(ids[TurnState.EXECUTING], {TurnState.EXECUTING}, TurnState.DONE, at=_now())


@requires_db
def test_single_flight_under_two_real_connections():
    """X-X13's SQL half: two in-flight requests race one pending row — the
    first commits, the second finds no pending action; never both."""
    real = vs.VoiceTurnStore(connect=lambda: RAW_CONNECT(env.DEV_DB_NAME, side=Side.USER))
    tid = f"t-{uuid.uuid4().hex[:12]}"
    try:
        real.create(turn_id=tid, session_id="sess-x13", source="test", input_kind="text", at=_now())
        assert real.transition(tid, {TurnState.RECEIVED}, TurnState.PLANNED, at=_now())
        assert real.transition(tid, {TurnState.PLANNED}, TurnState.AWAITING_CONFIRM, at=_now(),
                               pending_action={"tool": "cards.set_stop"})
        barrier = threading.Barrier(2)
        results = {}

        def go(name, new):
            barrier.wait()
            results[name] = real.transition(tid, {TurnState.AWAITING_CONFIRM}, new, at=_now())

        a = threading.Thread(target=go, args=("confirm", TurnState.EXECUTING))
        b = threading.Thread(target=go, args=("cancel", TurnState.CANCELLED))
        a.start(); b.start(); a.join(); b.join()
        assert sorted(results.values()) == [False, True], results
        state = real.get(tid)["state"]
        assert state in ("executing", "cancelled")
        assert (state == "executing") == results["confirm"]
    finally:
        real.delete_test_rows("sess-x13")
