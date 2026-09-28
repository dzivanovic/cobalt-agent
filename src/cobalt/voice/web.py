"""The `/voice/*` routes, the peer gate, the startup sweep, and the widget.

ROUTES (an `APIRouter` the ASET app includes):
* `POST /voice/turn` — multipart: `session` + EITHER `text` OR an `audio`
  file part. The handler reads the `UploadFile` BYTES itself (never the
  sheet's form-to-string idiom); a zero-byte or non-file part FAILs named;
  `max_upload_bytes` enforced (413). `run_turn` runs in a worker thread —
  the event loop never waits on a transcribe or a Plan call (FINAL [F-04]).
* `POST /voice/confirm`, `POST /voice/cancel` — `session` + `turn_id`: the
  widget's Confirm / Cancel taps (shown only while an action is pending).
* `GET /voice/status` — the degraded lines the widget's banner shows.

THE PEER GATE (W11 [F-03]): every `/voice/*` request is allowed ONLY when
the SOCKET PEER (`request.client.host`) is in `allowed_peers`; anything
else — a LAN address included — is a named 403. No header is ever read as
the allow key. `tailscale serve`'s peer is added by the device session (E8).

STARTUP (R2-1 side B + X-X22's guard): before the first request, take the
scratch-dir lock and delete every file in it (AMBER per file, RED per
failed unlink); another holder → `ScratchLocked`, nothing deleted, the
start FAILS loud (L1). Shutdown releases the lock.

THE WIDGET (C12): one floating press-to-talk button (hold-to-talk AND
tap-to-toggle → the same start()/stop()), `MediaRecorder` with an
`isTypeSupported` chain, a text box (same endpoint), the last reply, a mute
toggle, Confirm / Cancel only while an action is pending, and the degraded
banner. Replies are spoken by the DEVICE with a `localService` voice only;
none → text + AMBER "no local voice on this device" (FINAL §2.5). The
widget sends NO card id ([F-10]). No reply audio exists on the server.
"""

from __future__ import annotations

import asyncio
import re
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from loguru import logger
from starlette.datastructures import UploadFile

from . import scratch
from .config import VoiceConfig, load_voice_config
from .turn import TurnInput, default_deps, run_turn

router = APIRouter(prefix="/voice")

_CONFIG: Optional[VoiceConfig] = None
_DEPS = None
_LOCK: Optional[scratch.DirectoryLock] = None
_SWEEP_LINES: list[dict] = []
_SESSION = re.compile(r"^[A-Za-z0-9-]{4,64}$")


def get_config() -> VoiceConfig:
    global _CONFIG
    if _CONFIG is None:
        _CONFIG = load_voice_config()
    return _CONFIG


def get_deps():
    global _DEPS
    if _DEPS is None:
        _DEPS = default_deps()
    return _DEPS


def peer_gate(request: Request) -> None:
    host = request.client.host if request.client else None
    allowed = get_config().allowed_peers
    if host not in allowed:
        logger.error("voice: REFUSED peer {} (allowed: {})", host, allowed)
        raise HTTPException(status_code=403, detail=f"voice: peer {host!r} is not an allowed peer")


def _session(value) -> str:
    if not isinstance(value, str) or not _SESSION.match(value):
        raise HTTPException(status_code=400, detail="voice: a widget session id is required")
    return value


async def _run(inp: TurnInput) -> JSONResponse:
    try:
        deps = get_deps()
    except Exception as e:  # noqa: BLE001 - a config error is named, never a blank widget
        logger.error("voice: turn dependencies unavailable: {}: {}", type(e).__name__, e)
        return JSONResponse(status_code=503, content={"state": "failed", "reply": f"Voice is down ({type(e).__name__}).",
                                                      "degraded": [{"level": "red", "text": f"voice down: {e}"}]})
    outcome = await asyncio.to_thread(run_turn, inp, deps)
    return JSONResponse(content=outcome.model_dump(mode="json"))


@router.post("/turn", dependencies=[Depends(peer_gate)])
async def voice_turn(request: Request):
    cfg = get_config()
    form = await request.form()
    session = _session(form.get("session"))
    text = form.get("text")
    audio = form.get("audio")
    if (text is None) == (audio is None):
        raise HTTPException(status_code=400, detail="voice: send exactly one of `text` or an `audio` file part")
    if audio is not None:
        if not isinstance(audio, UploadFile):
            raise HTTPException(status_code=400, detail="voice: the `audio` part is not a file")
        data = await audio.read()
        if not data:
            raise HTTPException(status_code=400, detail="voice: zero-byte audio — nothing was recorded")
        if len(data) > cfg.max_upload_bytes:
            raise HTTPException(status_code=413, detail=f"voice: the recording exceeds {cfg.max_upload_bytes} bytes")
        inp = TurnInput(session_id=session, source="widget", audio=data,
                        content_type=audio.content_type or "application/octet-stream")
    else:
        if not isinstance(text, str):
            raise HTTPException(status_code=400, detail="voice: `text` must be a text field")
        inp = TurnInput(session_id=session, source="widget", text=text)
    return await _run(inp)


async def _tap(request: Request, which: str):
    form = await request.form()
    session = _session(form.get("session"))
    tid = form.get("turn_id")
    if not isinstance(tid, str) or not tid:
        raise HTTPException(status_code=400, detail="voice: `turn_id` is required")
    return await _run(TurnInput(session_id=session, source="widget", tap=which, pending_turn_id=tid))


@router.post("/confirm", dependencies=[Depends(peer_gate)])
async def voice_confirm(request: Request):
    return await _tap(request, "confirm")


@router.post("/cancel", dependencies=[Depends(peer_gate)])
async def voice_cancel(request: Request):
    return await _tap(request, "cancel")


def status_lines() -> list[dict]:
    from .transcribe import model_present

    lines = list(_SWEEP_LINES)
    try:
        if not model_present(get_config()):
            lines.append({"level": "red", "text": "speech-to-text down (model missing)"})
    except Exception as e:  # noqa: BLE001
        lines.append({"level": "red", "text": f"voice config unreadable ({type(e).__name__})"})
    return lines


@router.get("/status", dependencies=[Depends(peer_gate)])
def voice_status():
    return {"lines": status_lines()}


def voice_startup() -> None:
    """Before the first request: lock, then sweep (side B). Raises on a held lock."""
    global _LOCK, _SWEEP_LINES
    cfg = get_config()
    lock = scratch.DirectoryLock(cfg.scratch_dir)  # ScratchLocked → the start fails loud
    report = scratch.start_sweep(cfg.scratch_dir, lock)
    _LOCK = lock
    _SWEEP_LINES = [l.model_dump() for l in report.lines]
    # The reaper runs at start too (FINAL §7): a row a killed process left
    # in a working state is failed, never retried. A database that cannot
    # be reached here is a RED line on the widget, not a sheet that will
    # not start (the sheet has its own DB banners).
    try:
        from cobalt.modelaccess import load_routes
        from cobalt.session import clock as clock_mod

        from .registry import load_agent
        from .store import VoiceTurnStore, reap_limits

        plan_timeout = load_routes().routes[load_agent().route].timeout_s
        reaped = VoiceTurnStore().reap(now=clock_mod.now_utc(),
                                       limits=reap_limits(stt_timeout_s=cfg.stt_timeout_s, plan_timeout_s=plan_timeout))
        for tid, state in reaped:
            _SWEEP_LINES.append({"level": "amber", "text": f"voice turn {tid} reaped from {state} at start"})
    except Exception as e:  # noqa: BLE001
        _SWEEP_LINES.append({"level": "red", "text": f"voice turn reaper could not run at start ({type(e).__name__})"})
    logger.info("voice: scratch dir {} locked by this process; start sweep deleted {} file(s), {} failed",
                cfg.scratch_dir, report.deleted, report.failed)


def voice_shutdown() -> None:
    global _LOCK, _CONFIG, _DEPS
    if _LOCK is not None:
        _LOCK.release()
        _LOCK = None
    _CONFIG = None
    _DEPS = None


WIDGET_MARKER = '<div id="cv-voice"'

_WIDGET = """
<style>
 #cv-voice{position:fixed;right:16px;bottom:16px;z-index:9999;width:300px;max-width:calc(100vw - 32px);
  background:#111729;border:1px solid #20283c;border-radius:14px;padding:10px;font-family:system-ui,sans-serif;
  color:#eef5ff;box-shadow:0 8px 24px rgba(0,0,0,.4)}
 #cv-voice .cv-row{display:flex;gap:6px;align-items:center}
 #cv-voice button{padding:8px 10px;border-radius:8px;border:1px solid #28334d;background:#0b1020;color:#8d9bb6;
  font-weight:700;cursor:pointer;margin:0}
 #cv-talk{flex:1;font-size:15px;color:#00e5ff!important;border-color:#00e5ff!important;touch-action:none}
 #cv-talk.cv-rec{background:rgba(255,79,113,.18)!important;color:#ff8ea4!important;border-color:#ff4f71!important}
 #cv-voice input{flex:1;padding:8px;border-radius:8px;border:1px solid #232d44;background:#0b1020;color:#eef5ff}
 #cv-reply{font-size:13px;margin:8px 0;white-space:pre-wrap;min-height:1em}
 .cv-red{background:#3a0d18;border:1px solid #ff4f71;color:#ffc3ce;border-radius:6px;padding:4px 6px;font-size:12px;margin-bottom:4px}
 .cv-amber{background:#2e2408;border:1px solid #ffd84d;color:#ffe89a;border-radius:6px;padding:4px 6px;font-size:12px;margin-bottom:4px}
</style>
<div id="cv-voice" role="region" aria-label="Cobalt voice">
 <div id="cv-banner"></div>
 <div id="cv-reply" aria-live="polite"></div>
 <div id="cv-pending" class="cv-row" hidden>
  <button id="cv-confirm" type="button">Confirm</button><button id="cv-cancel" type="button">Cancel</button>
 </div>
 <div class="cv-row"><button id="cv-talk" type="button">🎙 Hold or tap to talk</button>
  <button id="cv-mute" type="button" title="mute spoken replies">🔈</button></div>
 <div class="cv-row" style="margin-top:6px"><input id="cv-text" autocomplete="off" placeholder="…or type">
  <button id="cv-send" type="button">Send</button></div>
</div>
<script>
(function(){
 const $ = id => document.getElementById(id);
 const SESSION = 'w-' + (crypto.randomUUID ? crypto.randomUUID() : String(Date.now()) + String(Math.random()).slice(2));
 const TYPES = ['audio/webm;codecs=opus', 'audio/ogg;codecs=opus', 'audio/mp4'];
 let rec = null, chunks = [], pendingTurn = null, muted = false, downAt = 0, lines = [], device = [];

 function banner(extra){
   const all = lines.concat(device, extra || []);
   $('cv-banner').innerHTML = '';
   for (const l of all){ const d = document.createElement('div'); d.className = l.level === 'red' ? 'cv-red' : 'cv-amber'; d.textContent = l.text; $('cv-banner').appendChild(d); }
 }
 function localVoice(){
   if (!window.speechSynthesis) return null;
   const v = speechSynthesis.getVoices().filter(v => v.localService);
   return v.length ? v[0] : null;
 }
 function speak(text, degraded){
   if (muted || !text) return;
   const voice = localVoice();
   if (!voice){ banner((degraded || []).concat([{level:'amber', text:'no local voice on this device'}])); return; }
   const u = new SpeechSynthesisUtterance(text); u.voice = voice; speechSynthesis.speak(u);
 }
 function show(j){
   $('cv-reply').textContent = j.reply || '';
   pendingTurn = (j.state === 'awaiting_confirm') ? j.pending_turn_id : null;
   $('cv-pending').hidden = !pendingTurn;
   banner(j.degraded || []);
   speak(j.reply, j.degraded || []);
 }
 async function post(url, fd){
   fd.append('session', SESSION);
   try {
     const r = await fetch(url, {method: 'POST', body: fd});
     const j = await r.json();
     if (!r.ok) { show({reply: (j.detail || j.reply || ('HTTP ' + r.status)), degraded: [{level:'red', text: j.detail || 'voice request refused'}]}); return; }
     show(j);
   } catch (e) { show({reply: 'Voice request failed', degraded: [{level:'red', text: String(e)}]}); }
 }
 function pickType(){
   if (!window.MediaRecorder) return null;
   for (const t of TYPES) { if (MediaRecorder.isTypeSupported(t)) return t; }
   return null;
 }
 async function start(){
   if (rec) return;
   const type = pickType();
   if (!type || !navigator.mediaDevices){ banner([{level:'red', text:'no microphone on this device'}]); return; }
   let stream;
   try { stream = await navigator.mediaDevices.getUserMedia({audio: true}); }
   catch (e) { banner([{level:'red', text:'no microphone on this device'}]); return; }
   chunks = [];
   rec = new MediaRecorder(stream, {mimeType: type});
   rec.ondataavailable = e => { if (e.data && e.data.size) chunks.push(e.data); };
   rec.onstop = () => {
     stream.getTracks().forEach(t => t.stop());
     const blob = new Blob(chunks, {type: type});
     rec = null; $('cv-talk').classList.remove('cv-rec');
     if (!blob.size) { show({reply: 'I heard nothing.'}); return; }
     const fd = new FormData(); fd.append('audio', blob, 'clip');
     post('/voice/turn', fd);
   };
   rec.start(); $('cv-talk').classList.add('cv-rec');
 }
 function stop(){ if (rec && rec.state === 'recording') rec.stop(); }
 // hold-to-talk AND tap-to-toggle map to the same start()/stop()
 $('cv-talk').addEventListener('pointerdown', e => { e.preventDefault(); downAt = Date.now(); if (rec) { stop(); downAt = 0; } else { start(); } });
 $('cv-talk').addEventListener('pointerup', () => { if (downAt && Date.now() - downAt > 400) stop(); downAt = 0; });
 $('cv-mute').addEventListener('click', () => { muted = !muted; $('cv-mute').textContent = muted ? '🔇' : '🔈'; if (muted && window.speechSynthesis) speechSynthesis.cancel(); });
 // No form element: the radar panel carries no form markup (test_radar_panel's invariant).
 function sendText(){ const t = $('cv-text').value.trim(); if (!t) return; $('cv-text').value = ''; const fd = new FormData(); fd.append('text', t); post('/voice/turn', fd); }
 $('cv-send').addEventListener('click', sendText);
 $('cv-text').addEventListener('keydown', e => { if (e.key === 'Enter') { e.preventDefault(); sendText(); } });
 $('cv-confirm').addEventListener('click', () => { if (!pendingTurn) return; const fd = new FormData(); fd.append('turn_id', pendingTurn); post('/voice/confirm', fd); });
 $('cv-cancel').addEventListener('click', () => { if (!pendingTurn) return; const fd = new FormData(); fd.append('turn_id', pendingTurn); post('/voice/cancel', fd); });
 fetch('/voice/status').then(r => { if (!r.ok) { lines = [{level:'red', text:'voice status refused (HTTP ' + r.status + ')'}]; banner(); return null; } return r.json(); }).then(j => { if (!j) return; lines = j.lines || []; banner(); }).catch(() => { lines = [{level:'red', text:'voice status unreadable'}]; banner(); });
 if (!pickType()) { device.push({level:'red', text:'no microphone on this device'}); banner(); }
})();
</script>
"""


def widget_html() -> str:
    """The partial `_render` (the sheet) and `/radar` place on the page."""
    return _WIDGET


__all__ = ["WIDGET_MARKER", "get_config", "get_deps", "peer_gate", "router", "status_lines",
           "voice_shutdown", "voice_startup", "widget_html"]
