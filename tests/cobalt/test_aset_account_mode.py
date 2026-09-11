"""Account-mode resolution and no-write refusal tests with fakes."""

from datetime import date
from datetime import datetime, timezone
from types import SimpleNamespace

import pytest

from cobalt.aset.account_mode import AccountModeUnresolved, resolve
from cobalt.aset.store import AsetStore


class Cursor:
    def __init__(self, row):
        self.row = row

    def fetchone(self):
        return self.row


class Conn:
    def __init__(self, rows):
        self.rows = iter(rows)
        self.calls = []

    def execute(self, sql, params):
        self.calls.append((sql, params))
        return Cursor(next(self.rows))


@pytest.mark.parametrize(
    "rows,expected",
    [([("sim",)], "sim"), ([(None,), ("live",)], "live")],
)
def test_override_then_standing(rows, expected):
    assert resolve(Conn(rows), date(2026, 9, 3)) == expected


def test_neither_refuses_loudly_after_both_reads():
    conn = Conn([None, None])
    with pytest.raises(AccountModeUnresolved, match="both|day_modes.account_mode is empty"):
        resolve(conn, date(2026, 9, 3))
    assert len(conn.calls) == 2


def test_invalid_override_refuses_without_falling_through():
    conn = Conn([("unknown",)])
    with pytest.raises(AccountModeUnresolved, match="invalid value"):
        resolve(conn, date(2026, 9, 3))
    assert len(conn.calls) == 1


def test_attestation_sql_preserves_mode_on_readback():
    text = open("src/cobalt/daymode/store.py", encoding="utf-8").read()
    assert "account_mode = COALESCE(EXCLUDED.account_mode, day_modes.account_mode)" in text


def test_save_refuses_before_insert(monkeypatch):
    import cobalt.aset.account_mode as module

    events = []

    class SaveConn:
        autocommit = True
        def cursor(self):
            events.append("cursor")
            raise AssertionError("INSERT reached")
        def rollback(self): events.append("rollback")
        def close(self): events.append("close")

    store = AsetStore("cobalt_dev")
    monkeypatch.setattr(store, "_connect", lambda: SaveConn())
    monkeypatch.setattr(module, "resolve", lambda *_a: (_ for _ in ()).throw(AccountModeUnresolved("missing both sources")))
    with pytest.raises(AccountModeUnresolved, match="both sources"):
        store.save(SimpleNamespace(input=SimpleNamespace()), now=datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc))
    assert events == ["rollback", "close"]
