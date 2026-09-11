"""Pure tests for the SELECT-only database query guard."""

import argparse

import pytest

from cobalt import db_query
from cobalt.db_query import QueryRefused, guard_select


@pytest.mark.parametrize(
    "sql,token",
    [
        ("delete from t", "DELETE"),
        ("select 1; select 2", "multiple"),
        ("with x as (update t set a=1 returning *) select * from x", "UPDATE"),
        ("select set_config('role','x',false)", "SET_CONFIG"),
        ("select * from t for update", "FOR UPDATE"),
        ("select pg_advisory_lock(1)", "PG_ADVISORY_LOCK"),
        ("select 1 /*", "unterminated comment"),
    ],
)
def test_refused_classes_name_the_token(sql, token):
    with pytest.raises(QueryRefused, match=token):
        guard_select(sql)


def test_keywords_inside_literals_comments_and_identifiers_pass():
    sql = "select 'delete; set role', \"update\" -- drop\nfrom safe_view;"
    assert guard_select(sql).startswith("select")


def test_production_name_without_flag_refuses_before_connect(monkeypatch, capsys):
    monkeypatch.setattr(db_query.env, "resolve_db_name", lambda: db_query.db.PROD_DB_NAME)
    monkeypatch.setattr(db_query.db, "connect", lambda *_a, **_k: (_ for _ in ()).throw(AssertionError("connected")))
    with pytest.raises(SystemExit) as raised:
        db_query.command(argparse.Namespace(sql="select 1", side="system", prod=False, format="table", limit=1))
    assert raised.value.code == 2
    assert "cobalt_brain" in capsys.readouterr().err
