# `src/cobalt/aset/strike.py`

F9 delivery inside the ASET sheet (`com.cobalt.aset`), reading ONE seam: S4-P1's `card_transitions` rows with actor `cobalt` and evidence `via` = `strike.detector` (→ TRIGGERED) or `strike.missed` (→ MISSED), `strike/detector.md` `## CONTRACT`. `seam_kind(row)` is the one rule; his own tap (`<source>.triggered`, actor `you`) and every other row send nothing. The module imports nothing of the detector; `VIA_TRIGGERED` / `VIA_MISSED` are pinned equal to P1's by a test.

- `GET /strike/stream` (S1) — `text/event-stream`. `event_stream(deps, last_event_id, stop)` reads `StrikeAlertStore.seam_rows(cursor, today ET)` every `stream_tail_ms` in a thread; one event per seam row: `id: <transition id>`, `event: trigger|missed`, `data: {transition_id, card_id, ticker, direction, key, shares, stop, hotkey, entry, bar_close_at, seen_at, at}`. `Last-Event-ID` resumes after that id (a non-numeric one → 400); a fresh connect starts at today's ET rows. Each send upserts `pushed_at`. After `keepalive_s` of silence: `: keepalive <iso>` then `event: keepalive` (the page can see a named event, never a comment); no keepalive while the read fails.
- `GET /strike` (S2) — `render_strike_page(settings)`: ARM (unlocks the Web Audio tone, asks `Notification.requestPermission` in a secure context), the alert (`alert_html`: title = ticker and side, then key · shares · stop · hotkey and nothing else), a Notification when granted, a flashing title until a click, today's events newest first; MISSED is one log line. Loud states: `STREAM DOWN · since <hh:mm:ss>`, `NOTIFICATIONS OFF — <reason>`, `SOUND LOCKED — press ARM`. A trigger whose `at` is older than the tab's load less `dm_after_s` is listed, not alerted.
- `POST /strike/ack {transition_id}` (S3) — `ack(store, id, now)` with the SERVER's `now_utc`; 404 for an id that is not a seam row, nothing written; a second ack changes nothing.
- `StrikeAlertStore` (SIDE user) — the seam read (`seam_rows`, `seam_rows_between`, `transition`) and `"user".strike_alerts` (0024): `upsert` (ONE write, fills only a NULL column), `claim_dm` (`dm_at` where `dm_at IS NULL AND shown_at IS NULL`), `record_dm_result`, `records_for`.
- `FallbackTail` / `FallbackThread` / `start_fallback_thread` (S4) — the sheet's own tail, synchronous, one daemon thread from `aset/__main__.py`: creates each trigger's record (`seam_at`), and `dm_after_s` after the seam row's `at` claims and sends ONE `send_dm(dm_text(row))` (`<ticker> <SIDE> · key <k> · <shares> sh · stop <stop> · <hotkey>`) when nobody was shown it; `SendResult.report()` or `DM FAILED — <error>` is recorded; a pass that raises is logged and the thread goes on. MISSED never DMs.

Config: `configs/cobalt/strike.yaml` via `strike/delivery_config.py`; `configs/cobalt/notify.yaml` via `send_dm`.

## 2026-10-09 — s4-p2-1009
New module (S4-P2 S1, S2, S3, S4).

## 2026-10-10 — s4-p2-1009 check
The stream's and the fallback tail's cursor moves only past a seam row (the last sent), never past his tap or another row: a detector row committed after a higher-id tap is no longer skipped (check O1, O2). A sent DM whose `dm_result` write fails is written again on the next pass and never sent twice (check A4).

## 2026-10-10 — strike-fallback-env-1010
`FallbackThread.step()` holds one pass and its logging decision (`run` calls it; `monotonic` is a keyword-only seam): a failure streak logs ERROR `… (failed passes: <n>)` at its first failure, at once for a new text, and again every `REPEAT_ERROR_S = 60.0` s while the same text persists; its end logs INFO `strike fallback: recovered after <n> failed passes`; a first pass that succeeds logs INFO `strike fallback: first pass OK` once (row B, R828).
