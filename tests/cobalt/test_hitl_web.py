"""F20 C2c — the `/hitl` page and its two routes (FINAL §3 step 5 B, F-06, F-25; L37).

Offline: TestClient over the real app, the store faked at the seam
(`hitl_support.FakeHitlStore`, which applies the routes' own WHERE clause),
the kill switch faked at `killswitch.is_active`. T2, T2b, T2c.
"""

from __future__ import annotations

from datetime import timedelta

import pytest

from hitl_support import FakeHitlStore


@pytest.fixture
def page(monkeypatch):
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module
    from cobalt.jobs import killswitch

    store = FakeHitlStore()
    state = {"kill": False}
    # raising=False: on BASE the seam does not exist and the routes answer 404.
    monkeypatch.setattr(web_module, "_hitl_store", lambda: store, raising=False)
    monkeypatch.setattr(killswitch, "is_active", lambda *a, **k: state["kill"])
    return TestClient(web_module.app), store, state


def _approve(client, row_id, sha256, key):
    return client.post(f"/hitl/{row_id}/approve", data={"sha256": sha256, "k": key})


def test_sha_mismatch_expired_double_approve_and_kill_switch_are_refused(page):
    client, store, state = page

    row_id, key = store.add()
    r = _approve(client, row_id, "0" * 64, key)
    assert r.status_code == 200 and "REFUSED" in r.text and "sha256" in r.text
    assert store.rows[row_id]["status"] == "pending"

    old_id, old_key = store.add(expires_at=store.now - timedelta(minutes=1))
    r = _approve(client, old_id, store.rows[old_id]["sha256"], old_key)
    assert "REFUSED" in r.text and "expired" in r.text
    assert store.rows[old_id]["status"] == "pending"

    state["kill"] = True
    store.calls.clear()
    r = _approve(client, row_id, store.rows[row_id]["sha256"], key)
    assert "REFUSED" in r.text and "kill switch" in r.text.lower()
    assert store.rows[row_id]["status"] == "pending"
    assert "update_returning" not in store.calls, "the kill switch is checked before the statement"

    state["kill"] = False
    r = _approve(client, row_id, store.rows[row_id]["sha256"], key)
    assert "APPROVED" in r.text
    row = store.rows[row_id]
    assert row["status"] == "approved"
    assert row["decided_via"] == f"aset.hitl@sha256:{row['sha256']}"

    r = _approve(client, row_id, row["sha256"], key)
    assert "REFUSED" in r.text and "approved" in r.text, "a second approve reads the status back"


def test_no_key_and_wrong_key_are_refused(page):
    client, store, _state = page
    row_id, key = store.add()
    sha256 = store.rows[row_id]["sha256"]
    for bad in ("", "f" * 32):
        r = _approve(client, row_id, sha256, bad)
        assert "REFUSED" in r.text and "key" in r.text
        assert store.rows[row_id]["status"] == "pending"
    r = client.post(f"/hitl/{row_id}/deny", data={"k": "f" * 32, "reason": "constructed"})
    assert "REFUSED" in r.text and store.rows[row_id]["status"] == "pending"


def test_model_text_is_escaped(page):
    client, store, _state = page
    hostile = b"agent:\n  id: x\n  charter: <script>alert(1)</script>\n"
    row_id, _key = store.add(rendered=hostile, reason="<script>alert(2)</script>")
    detail = client.get(f"/hitl/{row_id}").text
    listing = client.get("/hitl").text
    for text in (detail, listing):
        assert "<script>alert" not in text
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in detail
    assert store.rows[row_id]["sha256"] in detail
    assert "location.hash" in detail, "the page copies k from the fragment into the form"


def test_deny_records_reason(page):
    client, store, _state = page
    row_id, key = store.add()
    r = client.post(f"/hitl/{row_id}/deny", data={"k": key, "reason": "not this one"})
    assert "DENIED" in r.text
    row = store.rows[row_id]
    assert row["status"] == "denied" and row["deny_reason"] == "not this one"

    other, other_key = store.add()
    client.post(f"/hitl/{other}/deny", data={"k": other_key})
    assert store.rows[other]["status"] == "denied" and store.rows[other]["deny_reason"] is None
