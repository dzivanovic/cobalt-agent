"""X15 — the HITL carrier probe (card 977; F20 FINAL `:81` X15, `:82` X20, `:43` B).

The key rides in the link FRAGMENT. X15 asks whether the page script on his
phone sees `k`. These tests pin the pieces that question rests on: the ONE
hash-reading script (run under `node`), the store-free probe route, the
readout on the real page, and the dev-only `cobalt hitl x15-send`.

Offline: TestClient over the real app; every store is patched to raise or
faked at the seam (`hitl_support.FakeHitlStore`). Constructed values only
(L32): every key here is a constructed hex string.
"""

from __future__ import annotations

import inspect
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from hitl_support import FakeHitlStore

#: A constructed 32-hex key (L32).
KEY = "0123456789abcdef" * 2


def _raise(*_a, **_k):
    raise AssertionError("a store was reached")


@pytest.fixture
def no_store(monkeypatch):
    from cobalt.aset import web as web_module

    monkeypatch.setattr(web_module, "_hitl_store", _raise)
    monkeypatch.setattr("cobalt.hitl.store.HitlStore", _raise)
    from fastapi.testclient import TestClient

    return TestClient(web_module.app)


@pytest.fixture
def page(monkeypatch):
    """The `test_hitl_web.py` `page` fixture shape."""
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module
    from cobalt.jobs import killswitch

    store = FakeHitlStore()
    monkeypatch.setattr(web_module, "_hitl_store", lambda: store)
    monkeypatch.setattr(killswitch, "is_active", lambda *a, **k: False)
    return TestClient(web_module.app), store


# -- S1: the shared key script ------------------------------------------------


def _run_script(fragment: str) -> dict:
    node = shutil.which("node")
    if node is None:
        pytest.fail("node is not on PATH — the readout logic is proven under node only (card 977 S1)")
    from cobalt.aset import web

    script = web._hitl_key_script()
    assert script.startswith("<script>") and script.endswith("</script>")
    body = script[len("<script>"):-len("</script>")]
    harness = (
        f"const location={{hash:{json.dumps(fragment)}}};"
        "const inputs=[{value:'stale'},{value:'stale'}];"
        "const states=[{textContent:'k: missing'}];"
        "const document={querySelectorAll:(sel)=>sel==='.hitl-k'?inputs:"
        "sel==='.hitl-k-state'?states:[]};"
        f"{body}\n"
        "process.stdout.write(JSON.stringify({inputs:inputs.map(i=>i.value),"
        "states:states.map(s=>s.textContent)}));"
    )
    out = subprocess.run([node, "-e", harness], capture_output=True, text=True, timeout=30)
    assert out.returncode == 0, out.stderr
    return json.loads(out.stdout)


@pytest.mark.parametrize(
    ("fragment", "state", "value"),
    [
        (f"#k={KEY}", "k: seen", KEY),
        ("", "k: missing", ""),
        ("#k=", "k: missing", ""),
        ("#x=1", "k: missing", ""),
    ],
    ids=["present", "absent", "empty", "other-key"],
)
def test_readout_logic_k_present_absent_empty(fragment, state, value):
    got = _run_script(fragment)
    assert got["states"] == [state]
    assert got["inputs"] == [value, value]
    for text in got["states"]:
        assert KEY not in text, "the readout never carries the key"


def test_the_key_script_is_one_source():
    from cobalt.aset import web

    source = Path(web.__file__).read_text()
    assert source.count("location.hash") == 1, "the tree holds the hash read once"
    assert "location.hash" in inspect.getsource(web._hitl_key_script)
    script = web._hitl_key_script()
    for banned in ("fetch(", "XMLHttpRequest", "sendBeacon", "location=", "location.href", "submit("):
        assert banned not in script, banned


# -- P1: the probe route ------------------------------------------------------


def test_probe_route_touches_no_store(no_store):
    from cobalt.aset import web

    r = no_store.get("/hitl/x15-probe")
    assert r.status_code == 200, r.status_code
    body = r.text
    assert "hitl-k-state" in body and "k: missing" in body
    assert web._hitl_key_script() in body
    # The element, not the bare string (the script holds `.hitl-k-state` and
    # `k: missing` too), and the script after it: it runs where it is parsed.
    assert body.count('class="hitl-k-state">k: missing<') == 1
    assert body.index('class="hitl-k-state"') < body.index("<script>")
    assert "approves nothing, reads nothing, writes nothing" in body
    for banned in ("<form", "Approve", "Deny", "fetch(", "XMLHttpRequest", "sendBeacon"):
        assert banned not in body, banned


def test_probe_route_is_not_shadowed():
    from cobalt.aset import web

    paths = [getattr(r, "path", None) for r in web.app.routes]
    assert "/hitl/x15-probe" in paths
    assert paths.index("/hitl/x15-probe") < paths.index("/hitl/{row_id}")


def test_probe_path_takes_no_post(no_store):
    for verb in ("approve", "deny"):
        r = no_store.post(f"/hitl/x15-probe/{verb}", data={"k": KEY, "sha256": "0" * 64})
        assert r.status_code == 422, (verb, r.status_code)
        assert "APPROVED" not in r.text and "DENIED" not in r.text


# -- P2: the readout on the real page -----------------------------------------


def test_real_page_shows_the_readout_above_approve(page):
    client, store = page
    row_id, _key = store.add()
    body = client.get(f"/hitl/{row_id}").text
    assert body.count('class="hitl-k-state"') == 1
    assert body.index('class="hitl-k-state"') < body.index(">Approve<")
    # The script runs where it is parsed: after the readout and both key fields.
    assert body.index('class="hitl-k-state"') < body.index("<script>")
    assert body.rindex('class="hitl-k"') < body.index("<script>")

    done_id, _ = store.add(status="approved")
    done = client.get(f"/hitl/{done_id}").text
    assert "hitl-k-state" not in done and ">Approve<" not in done


# -- P3: the dev send ---------------------------------------------------------


def _cli(monkeypatch, *argv):
    from cobalt import cli

    monkeypatch.setattr(sys, "argv", ["cobalt", *argv])
    cli.main()


@pytest.fixture
def recorder(monkeypatch):
    from cobalt.notify.result import SendResult

    sent: list[str] = []

    def _send(message, **_k):
        sent.append(message)
        return SendResult(True, "post p1 to @constructed")

    monkeypatch.setattr("cobalt.notify.mattermost.send_dm", _send)
    monkeypatch.setattr("cobalt.hitl.store.HitlStore", _raise)
    return sent


@pytest.mark.parametrize("env", ["production", None])
def test_x15_send_refuses_outside_dev(monkeypatch, capsys, env):
    monkeypatch.setattr("cobalt.notify.mattermost.send_dm", _raise)
    if env is None:
        monkeypatch.delenv("COBALT_ENV", raising=False)
    else:
        monkeypatch.setenv("COBALT_ENV", env)
    with pytest.raises(SystemExit) as exc:
        _cli(monkeypatch, "hitl", "x15-send")
    assert exc.value.code == 2
    assert "REFUSED: cobalt hitl x15-send runs under COBALT_ENV=dev only" in capsys.readouterr().err


def test_x15_send_dms_the_probe_link_once(monkeypatch, capsys, recorder):
    monkeypatch.setenv("COBALT_ENV", "dev")
    monkeypatch.setattr("cobalt.hitl.card.page_base_url", lambda: "https://sheet.example.invalid")
    _cli(monkeypatch, "hitl", "x15-send")
    assert len(recorder) == 1
    assert re.fullmatch(
        r"X15 test, approves nothing\nhttps://sheet\.example\.invalid/hitl/x15-probe#k=[0-9a-f]{32}",
        recorder[0],
    ), recorder[0]
    out = capsys.readouterr()
    assert out.out == "X15 SENT post p1 to @constructed\n"
    assert re.search(r"[0-9a-f]{32}", out.out + out.err) is None, "the key is never printed"


def test_x15_line_survives_redact(monkeypatch, recorder):
    from cobalt.hitl import card
    from cobalt.redact import redact
    from cobalt.redact.secrets import LiteralGuard

    monkeypatch.setenv("COBALT_ENV", "dev")
    monkeypatch.setattr(
        "cobalt.redact.guard.load_literals",
        lambda *a, **kw: LiteralGuard({}, available=False, reason="test"),
    )
    _cli(monkeypatch, "hitl", "x15-send")
    assert len(recorder) == 1
    base = card.page_base_url()
    built = f"X15 test, approves nothing\n{base}/hitl/x15-probe#k={KEY}"
    for msg in (recorder[0], built):
        assert msg.startswith(f"X15 test, approves nothing\n{base}/hitl/x15-probe#k=")
        safe = redact(msg, channel="test", record=False)
        assert safe.clean and safe.hits == {} and safe.text == msg, safe.describe()


def test_hitl_list_is_unchanged(monkeypatch):
    from cobalt.hitl import cli as hitl_cli

    seen = []
    monkeypatch.setattr("cobalt.notify.mattermost.send_dm", _raise)
    monkeypatch.setattr(hitl_cli, "_list", lambda args: seen.append(args.limit))
    _cli(monkeypatch, "hitl", "list")
    assert seen == [50]


# -- the check (x15-hitl-probe-check) ----------------------------------------


def test_probe_readout_pin_is_the_script_text():
    from cobalt.aset import web

    script = web._hitl_key_script()
    assert "hitl-k-state" in script and "k: missing" in script
    src = inspect.getsource(test_probe_route_touches_no_store)
    assert 'class="hitl-k-state"' in src


def test_script_after_the_nodes_is_unpinned():
    probe = inspect.getsource(test_probe_route_touches_no_store)
    real = inspect.getsource(test_real_page_shows_the_readout_above_approve)
    assert "index(" in probe and "<script>" in probe
    assert "index(" in real and "<script>" in real
