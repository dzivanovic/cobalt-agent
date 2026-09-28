# `src/cobalt/voice/web.py`

## What it does
The `/voice/*` routes (an `APIRouter` the ASET app includes), the peer
gate, the start-up sweep, the status lines and the widget partial.

## Routes
- `POST /voice/turn` — `session` + exactly one of `text` or an `audio`
  file part. The handler reads the upload's bytes itself; a zero-byte part
  or a part that is not a file is a named 400; more than
  `max_upload_bytes` is 413. The turn runs in a worker thread
  (`asyncio.to_thread`) — the event loop never waits on speech-to-text or
  the Plan call.
- `POST /voice/confirm` / `POST /voice/cancel` — `session` + `turn_id`:
  the widget's taps.
- `GET /voice/status` — the start sweep's lines, the start reaper's lines,
  and RED `speech-to-text down (model missing)` when the pinned model is
  not on disk.

## The peer gate (W11 [F-03])
Allowed only when the SOCKET PEER is in `allowed_peers` (loopback in dev;
the `tailscale serve` peer is added by the device session, E8). Any other
peer — a LAN address included — is a named 403. No header is read, so a
spoofed `X-Forwarded-For` changes nothing.

## Start-up / shutdown
`voice_startup` takes the scratch-dir lock, runs side B's sweep (every
file, AMBER each) and the reaper; a lock held elsewhere raises
`ScratchLocked` and the ASET start fails loud (X-X22's guard). A database
that cannot be reached for the reaper is a RED status line, not a failed
sheet. `voice_shutdown` releases the lock.

## The widget (C12)
`widget_html()` — one floating box: a press-to-talk button (hold-to-talk
and tap-to-toggle call the same start / stop), `MediaRecorder` with the
`isTypeSupported` chain webm/opus → ogg/opus → mp4, a text box to the same
endpoint, the last reply, a mute toggle, Confirm / Cancel only while an act
is pending, and the degraded banner (no microphone, speech-to-text down,
Cobalt can't think, a refusal, no local voice, scratch RED). Replies are
spoken by the device with a `localService` voice only; none → text plus an
AMBER "no local voice on this device" — added to the turn's own RED /
AMBER lines, never replacing them (fix r1). A `/voice/status` answer that is
not OK (a 403, a 500) is a RED "voice status refused (HTTP <status>)", never
an empty all-clear banner (fix r1). The device's own RED line ("no
microphone on this device") lives in a separate `device` list that
`banner()` always draws and the status callbacks never assign, so neither
a refused nor an OK status answer wipes it (fix r2). It sends no card id; the widget
session id is random per page load. No reply audio exists on the server.
