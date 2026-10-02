"""C11 / C12 — the `/voice/*` routes, the peer gate (W11 [F-03]), the startup
sweep + lock, and the widget partial on `/` and `/radar`.

THE PEER GATE: a request is allowed ONLY when the SOCKET PEER
(`request.client.host`) is in `allowed_peers`; any other peer — a LAN
address included — is a named 403; no header is ever the allow key (a
spoofed `X-Forwarded-For: 127.0.0.1` from a LAN peer is still 403).
THE UPLOAD: the handler reads the `UploadFile` bytes itself (never the
`str(v)` form idiom); a zero-byte or non-file part FAILs named;
`max_upload_bytes` enforced. `run_turn` runs off the event loop.
"""

from __future__ import annotations

import asyncio
import re
import threading
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from cobalt.aset import web as aset_web
from cobalt.voice import config as vc
from cobalt.voice import scratch as sc
from cobalt.voice import web as vw
from cobalt.voice.models import DegradedLine, TurnOutcome, TurnState

LOOP = ("127.0.0.1", 51000)
LAN = ("192.168.1.5", 51000)


@pytest.fixture
def cfg(tmp_path, monkeypatch):
    monkeypatch.setenv(vc.SCRATCH_ENV, str(tmp_path / "scratch"))
    monkeypatch.setenv(vc.MODEL_ENV, str(tmp_path / "models"))
    c = vc.load_voice_config()
    monkeypatch.setattr(vw, "get_config", lambda: c)
    return c


@pytest.fixture
def seen(cfg, monkeypatch):
    calls = []

    def fake_run_turn(inp, deps):
        try:
            asyncio.get_running_loop()
            on_loop = True
        except RuntimeError:
            on_loop = False
        calls.append({"inp": inp, "on_loop": on_loop, "thread": threading.current_thread().name})
        return TurnOutcome(turn_id="turn-constructed", state=TurnState.DONE, reply="constructed reply",
                           degraded=[DegradedLine(level="amber", text="constructed line")])

    monkeypatch.setattr(vw, "run_turn", fake_run_turn)
    monkeypatch.setattr(vw, "get_deps", lambda: object())
    return calls


def _client(peer=LOOP):
    return TestClient(aset_web.app, client=peer)


# --- the peer gate -------------------------------------------------------------------


def test_loopback_is_allowed_and_the_turn_runs_off_the_loop(seen):
    r = _client().post("/voice/turn", data={"session": "sess-web1", "text": "what are my open cards"})
    assert r.status_code == 200, r.text
    assert r.json()["reply"] == "constructed reply" and r.json()["state"] == "done"
    assert seen[0]["inp"].text == "what are my open cards" and seen[0]["inp"].source == "widget"
    assert seen[0]["on_loop"] is False, "run_turn must never run on the event loop"


@pytest.mark.parametrize("peer", [LAN, ("100.64.0.9", 51000), ("testclient", 50000), ("10.0.0.2", 1)])
def test_any_other_peer_is_a_named_403(seen, peer):
    r = _client(peer).post("/voice/turn", data={"session": "sess-web1", "text": "x"})
    assert r.status_code == 403 and "not an allowed peer" in r.json()["detail"]
    assert seen == []


@pytest.mark.parametrize("host", ["100.104.48.21", "100.70.206.126", "100.73.178.42", "100.66.219.53",
                                  "100.82.85.27"])
def test_v1_every_tailnet_device_is_an_allowed_socket_peer(seen, host):
    """voice-peers V1 (2026-09-28 R95, 2026-10-01 R14): the committed config
    admits each tailnet device's socket peer; fedora (100.104.48.21) first."""
    r = _client((host, 51000)).get("/voice/status")
    assert r.status_code == 200, r.text


@pytest.mark.parametrize("host", ["192.168.1.5", "100.70.206.127"])
def test_v1_a_near_miss_or_lan_peer_is_still_refused(seen, host):
    """V1's negative control: a LAN peer and a one-off tailnet neighbour stay 403."""
    r = _client((host, 51000)).get("/voice/status")
    assert r.status_code == 403 and "not an allowed peer" in r.json()["detail"]


def test_a_spoofed_forwarded_header_is_never_the_allow_key(seen):
    r = _client(LAN).post("/voice/turn", data={"session": "sess-web1", "text": "x"},
                          headers={"X-Forwarded-For": "127.0.0.1", "X-Real-IP": "127.0.0.1",
                                   "Forwarded": "for=127.0.0.1"})
    assert r.status_code == 403 and seen == []


@pytest.mark.parametrize("path", ["/voice/status", "/voice/confirm", "/voice/cancel"])
def test_every_voice_route_is_gated(seen, path):
    c = _client(LAN)
    r = c.get(path) if path.endswith("status") else c.post(path, data={"session": "sess-web1", "turn_id": "t-x"})
    assert r.status_code == 403


# --- the upload ------------------------------------------------------------------------


def test_an_audio_part_is_read_as_bytes(seen):
    blob = b"\x1aE\xdf\xa3synthesized"
    r = _client().post("/voice/turn", data={"session": "sess-web1"},
                       files={"audio": ("clip.webm", blob, "audio/webm;codecs=opus")})
    assert r.status_code == 200, r.text
    assert seen[0]["inp"].audio == blob and seen[0]["inp"].content_type == "audio/webm;codecs=opus"


def test_a_zero_byte_audio_part_fails_named(seen):
    r = _client().post("/voice/turn", data={"session": "sess-web1"}, files={"audio": ("c.webm", b"", "audio/webm")})
    assert r.status_code == 400 and "zero-byte" in r.json()["detail"] and seen == []


def test_a_non_file_audio_part_fails_named(seen):
    r = _client().post("/voice/turn", data={"session": "sess-web1", "audio": "not a file"})
    assert r.status_code == 400 and "not a file" in r.json()["detail"] and seen == []


def test_an_oversized_upload_is_refused(seen, cfg):
    big = b"x" * (cfg.max_upload_bytes + 1)
    r = _client().post("/voice/turn", data={"session": "sess-web1"}, files={"audio": ("c.webm", big, "audio/webm")})
    assert r.status_code == 413 and seen == []


@pytest.mark.parametrize("data", [{"session": "sess-web1"}, {"text": "x"}, {"session": "x", "text": "y"},
                                  {"session": "sess-web1", "text": "a", "audio": "b"}])
def test_a_malformed_turn_is_a_named_400(seen, data):
    r = _client().post("/voice/turn", data=data)
    assert r.status_code == 400 and seen == []


def test_taps_reach_the_turn_function(seen):
    r = _client().post("/voice/confirm", data={"session": "sess-web1", "turn_id": "turn-abc"})
    assert r.status_code == 200 and seen[0]["inp"].tap == "confirm" and seen[0]["inp"].pending_turn_id == "turn-abc"
    _client().post("/voice/cancel", data={"session": "sess-web1", "turn_id": "turn-abc"})
    assert seen[1]["inp"].tap == "cancel"


def test_the_handler_never_uses_the_str_v_form_idiom():
    import inspect

    assert "str(v)" not in inspect.getsource(vw)


# --- startup: the sweep behind the lock ---------------------------------------------------


def test_startup_sweeps_every_file_under_the_lock_and_shutdown_releases(cfg):
    left = sc.write_scratch(cfg.scratch_dir, "turn-left0001", b"synthesized", "audio/webm")
    try:
        vw.voice_startup()
        assert not left.exists()
        assert vw.status_lines()[0]["level"] == "amber"
        with pytest.raises(sc.ScratchLocked):
            sc.DirectoryLock(cfg.scratch_dir)  # this process holds it
    finally:
        vw.voice_shutdown()
    sc.DirectoryLock(cfg.scratch_dir).release()  # released → takeable


def test_startup_fails_loud_when_another_holder_has_the_lock(cfg):
    other = sc.DirectoryLock(cfg.scratch_dir)
    left = sc.write_scratch(cfg.scratch_dir, "turn-left0002", b"synthesized", "audio/webm")
    try:
        with pytest.raises(sc.ScratchLocked):
            vw.voice_startup()
        assert left.exists(), "a held lock deletes nothing"
    finally:
        other.release()
        vw.voice_shutdown()


def test_the_app_wires_startup_shutdown_and_the_router():
    assert vw.voice_startup in aset_web.app.router.on_startup
    assert vw.voice_shutdown in aset_web.app.router.on_shutdown
    paths = {r.path for r in aset_web.app.routes}
    assert {"/voice/turn", "/voice/confirm", "/voice/cancel", "/voice/status"} <= paths


def test_status_names_a_missing_model_red(cfg, monkeypatch):
    monkeypatch.setattr(vw, "_SWEEP_LINES", [])
    r = _client().get("/voice/status")
    assert r.status_code == 200
    assert {"level": "red", "text": "speech-to-text down (model missing)"} in r.json()["lines"]


# --- C12: the widget ---------------------------------------------------------------------------


def _stub_sheet(monkeypatch):
    monkeypatch.setattr(aset_web, "_daymode_state", lambda: {"cfg": None, "day": None, "row": None, "mode": None,
                                                             "stage": "x", "error": "constructed"})
    monkeypatch.setattr(aset_web, "_daymode_banner", lambda dm: "")
    monkeypatch.setattr(aset_web, "_open_cards_section", lambda: "")
    from test_aset_web import _offline_sheet_modes_config

    monkeypatch.setattr(aset_web, "load_sheet_modes_config", _offline_sheet_modes_config)


def test_the_widget_partial_renders_on_the_sheet(monkeypatch):
    _stub_sheet(monkeypatch)
    html = aset_web._render()
    assert vw.WIDGET_MARKER in html and html.count(vw.WIDGET_MARKER) == 1


def test_the_widget_partial_renders_on_radar(monkeypatch):
    import cobalt.aset.web as w

    monkeypatch.setattr(w, "build_radar_panel", lambda **kw: object())
    monkeypatch.setattr(w, "render_radar_page", lambda view, phone_frame=False: "<html><body>R</body></html>")
    r = _client().get("/radar")
    assert r.status_code == 200 and vw.WIDGET_MARKER in r.text and r.text.index(vw.WIDGET_MARKER) < r.text.index("</body>")


def test_the_widget_js_names_only_voice_endpoints():
    html = vw.widget_html()
    urls = re.findall(r"fetch\(\s*['\"]([^'\"]+)['\"]", html)
    assert urls and all(u.startswith("/voice/") for u in urls), urls


def test_speech_synthesis_is_local_voices_only():
    """A STRING check, stated as such: every speak() goes through the one
    helper that filters `localService` voices; no voice at all → AMBER."""
    js = vw.widget_html()
    assert js.count("speechSynthesis.speak(") == 1
    assert "getVoices().filter(v => v.localService)" in js
    assert "no local voice on this device" in js


def _status_block(js: str) -> str:
    start = js.index("fetch('/voice/status')")
    return js[start:js.index("\n", start)]


def test_the_widget_reads_a_refused_status_as_red_never_all_clear():
    """D3 (voice-v1-check-d-2026-09-24.md FOR THE CLASSIFIER 3; FINAL §7 loud
    states, L9): the `/voice/status` fetch tests `r.ok` BEFORE `r.json()`,
    and its non-OK branch pushes a RED `voice status refused (HTTP <status>)`
    line. A static pin of the widget script — there is no JS runner here."""
    block = _status_block(vw.widget_html())
    assert "r.ok" in block and "r.json()" in block
    assert block.index("r.ok") < block.index("r.json()")
    assert "level:'red', text:'voice status refused (HTTP ' + r.status + ')'" in block


def test_a_device_red_line_survives_every_status_callback():
    """D3, fix r2 (voice-v1-fix-r1-check-2026-09-24.md:141, :158; FINAL :175
    §7 "No microphone / permission denied | widget red: \"no microphone on
    this device\"", L9): the device's RED line lives in its own `device`
    array, which `banner()` always draws and the `/voice/status` callbacks
    never assign — so a refused status AND an OK status (`lines = j.lines ||
    []`) both leave it on the banner. A static pin of the widget script —
    there is no JS runner here."""
    js = vw.widget_html()
    (decl,) = [l for l in js.splitlines() if l.strip().startswith("let ") and "lines = []" in l]
    assert "device = []" in decl, decl
    assert "lines.concat(device, extra || [])" in js
    assert "device.push({level:'red', text:'no microphone on this device'})" in js
    assert "lines.push({level:'red', text:'no microphone on this device'})" not in js
    block = _status_block(js)
    assert "lines = [{level:'red', text:'voice status refused (HTTP ' + r.status + ')'}]" in block
    assert "lines = j.lines || []" in block
    assert "lines = [{level:'red', text:'voice status unreadable'}]" in block
    assert "device" not in block


def test_no_local_voice_keeps_the_turns_red_lines_on_the_banner():
    """D4 (voice-v1-check-d-2026-09-24.md FOR THE CLASSIFIER 4; FINAL §2.5 /
    §7, L1): `speak()` takes the turn's degraded lines, and its no-local-voice
    repaint is those lines PLUS the amber line — never the amber line alone.
    `show()` passes the turn's degraded lines through. A static pin."""
    js = vw.widget_html()
    assert "function speak(text, degraded){" in js
    assert "banner((degraded || []).concat([{level:'amber', text:'no local voice on this device'}]))" in js
    assert "banner([{level:'amber', text:'no local voice on this device'}])" not in js
    assert "speak(j.reply, j.degraded || []);" in js


def test_the_widget_carries_no_form_or_focus_stealing_markup():
    """The radar panel's own invariant (test_radar_panel), applied to the partial."""
    low = vw.widget_html().lower()
    for forbidden in ("<form", 'method="post"', "alert(", "prompt(", "confirm(", ".focus(", "autofocus"):
        assert forbidden not in low, forbidden


def test_the_widget_sends_no_card_id():
    js = vw.widget_html()
    assert "card_id" not in js and "cardId" not in js


def test_the_widget_has_hold_and_tap_the_container_chain_and_the_pending_buttons():
    js = vw.widget_html()
    for needle in ("audio/webm;codecs=opus", "audio/ogg;codecs=opus", "audio/mp4", "isTypeSupported",
                   "pointerdown", "pointerup", "Confirm", "Cancel", "no microphone on this device",
                   "mute"):
        assert needle in js, needle
