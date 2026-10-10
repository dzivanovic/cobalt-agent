"""F9 delivery (S4-P2): the strike stream, the pinned tab, the ack and the
phone fallback — all inside the ASET sheet (`com.cobalt.aset`).

ONE SEAM IN (L72): S4-P1's `card_transitions` rows with actor `cobalt` and
evidence `via` = `strike.detector` (→ TRIGGERED) or `strike.missed`
(→ MISSED), the evidence keys as `strike/detector.md` `## CONTRACT` states
them. `seam_kind()` is the one rule that says which row is a seam row; his
own tap (`<source>.triggered`, actor `you`) and every other row send nothing.

* S1 `GET /strike/stream` — `text/event-stream`. Tails the seam rows by
  `card_transitions.id` every `stream_tail_ms`, the DB read and the
  `pushed_at` upsert in a thread (never on the event loop). One event per
  row: `id: <transition id>`, `event: trigger|missed`, `data: <json>`.
  `Last-Event-ID` resumes after that id; a fresh connect starts at the rows
  of today's ET date. A keepalive — a comment line followed by an
  `event: keepalive` the page can see — after `keepalive_s` of silence; none
  while the read fails, so the tab goes loud (STREAM DOWN).
* S2 `GET /strike` — the pinned tab: ARM (the gesture that unlocks sound and
  asks for notification permission), the alert (title = ticker and side;
  key · shares · stop · hotkey and nothing else), a Notification when
  permitted, a Web Audio tone, a flashing title; MISSED is one log line.
* S3 `POST /strike/ack {transition_id}` — the SERVER's clock stamps
  `shown_at`. `"user".strike_alerts` (0024) holds one row per seam
  transition, created by whichever comes first (the tail, the send, the ack)
  through ONE upsert that fills only a NULL column.
* S4 the phone fallback — `FallbackTail` in one daemon thread started by
  `aset/__main__.py`, synchronous end to end: a trigger nobody was shown
  `dm_after_s` after the seam row's `at` is claimed (`dm_at`) and DM'd once
  through `notify.mattermost.send_dm`; the result is recorded, a failure
  never raised into the sheet. MISSED never DMs.

Imports nothing of the detector (`cobalt.strike.__init__` imports nothing):
the sheet never loads the strike loop.
"""

from __future__ import annotations

import asyncio
import html
import json
import threading
import time
from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal
from typing import Any, Awaitable, Callable, Optional

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse
from loguru import logger

from cobalt import db, env
from cobalt.db import Side
from cobalt.session import clock as clock_mod
from cobalt.session.clock import ET
from cobalt.strike.delivery_config import DeliverySettings, hotkey, load_delivery_config

#: P1's two `via` values (`strike/detector.py` VIA_TRIGGERED / VIA_MISSED),
#: written here so the sheet never imports the detector; a test pins them
#: equal (`test_strike_stream.py`).
VIA_TRIGGERED = "strike.detector"
VIA_MISSED = "strike.missed"
_SEAM = {VIA_TRIGGERED: ("TRIGGERED", "trigger"), VIA_MISSED: ("MISSED", "missed")}

router = APIRouter()


@dataclass(frozen=True)
class SeamRow:
    """A `card_transitions` row joined to its card (`aset_sizings`)."""

    transition_id: int
    card_id: int
    to_state: str
    actor: str
    at: datetime
    evidence: dict
    ticker: str
    direction: str
    sized_grade: Optional[str]
    shares: Optional[int]
    stop: Optional[Decimal]
    sheet_mode: Optional[str]


def seam_kind(row: SeamRow) -> Optional[str]:
    """`trigger`, `missed`, or None for every row that is not P1's seam."""
    if row.actor != "cobalt":
        return None
    hit = _SEAM.get((row.evidence or {}).get("via"))
    if hit is None or hit[0] != row.to_state:
        return None
    return hit[1]


def _text(value) -> Optional[str]:
    return None if value is None else str(value)


def event_payload(row: SeamRow, settings: DeliverySettings) -> dict[str, Any]:
    evidence = row.evidence or {}
    return {
        "transition_id": row.transition_id, "card_id": row.card_id, "ticker": row.ticker,
        "direction": row.direction, "key": row.sized_grade, "shares": row.shares, "stop": _text(row.stop),
        "hotkey": hotkey(settings.hotkey_template, sheet_mode=row.sheet_mode, sized_grade=row.sized_grade,
                         direction=row.direction),
        "entry": evidence.get("entry"), "bar_close_at": evidence.get("bar_close_at"),
        "seen_at": evidence.get("seen_at"), "at": row.at.isoformat(),
    }


def format_event(kind: str, row: SeamRow, settings: DeliverySettings) -> str:
    data = json.dumps(event_payload(row, settings), separators=(", ", ": "), ensure_ascii=False)
    return f"id: {row.transition_id}\nevent: {kind}\ndata: {data}\n\n"


def keepalive(now: datetime) -> str:
    return f": keepalive {now.isoformat()}\nevent: keepalive\ndata: {json.dumps({'at': now.isoformat()})}\n\n"


def _na(value) -> str:
    return "n/a" if value is None else str(value)


def dm_text(row: SeamRow, settings: DeliverySettings) -> str:
    """The phone fallback's one line: `<ticker> <side> · key <k> · <shares> sh · stop <stop> · <hotkey>`."""
    p = event_payload(row, settings)
    return (f"{row.ticker} {row.direction.upper()} · key {_na(p['key'])} · {_na(p['shares'])} sh · "
            f"stop {_na(p['stop'])} · {p['hotkey']}")


# ---------------------------------------------------------------------
# the store — the seam read and `"user".strike_alerts` (S3)
# ---------------------------------------------------------------------

_SEAM_SELECT = (
    "SELECT t.id, t.card_id, t.to_state, t.actor, t.at, t.evidence, s.ticker, s.direction, s.sized_grade, "
    "s.shares, s.stop, s.sheet_mode FROM card_transitions t JOIN aset_sizings s ON s.id = t.card_id "
    "WHERE t.to_state IN ('TRIGGERED', 'MISSED') AND "
)
_ET_DAY = "(t.at AT TIME ZONE 'America/New_York')::date"
_RECORD = "transition_id, seam_at, pushed_at, shown_at, dm_at, dm_result"


class StrikeAlertStore:
    #: ADR-0008 D2: the seam rows, the cards and the alert records are one
    #: trader's, all on the user side.
    SIDE = Side.USER

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or env.resolve_db_name()

    def _connect(self):
        return db.connect(self.db_name, side=self.SIDE)

    def _rows(self, where: str, params: tuple) -> list[SeamRow]:
        with self._connect() as conn:
            rows = conn.execute(_SEAM_SELECT + where + " ORDER BY t.id", params).fetchall()
        return [
            SeamRow(transition_id=int(r[0]), card_id=int(r[1]), to_state=r[2], actor=r[3], at=r[4],
                    evidence=r[5] if isinstance(r[5], dict) else json.loads(r[5] or "{}"), ticker=r[6],
                    direction=str(r[7]).lower(), sized_grade=r[8], shares=r[9], stop=r[10], sheet_mode=r[11])
            for r in rows
        ]

    def seam_rows(self, after_id: Optional[int], day: date) -> list[SeamRow]:
        """Rows with id > `after_id`; with no id, every row of ET `day`."""
        if after_id is None:
            return self._rows(f"{_ET_DAY} = %s", (day,))
        return self._rows("t.id > %s", (after_id,))

    def seam_rows_between(self, start: date, end: date) -> list[SeamRow]:
        return self._rows(f"{_ET_DAY} BETWEEN %s AND %s", (start, end))

    def transition(self, transition_id: int) -> Optional[SeamRow]:
        rows = self._rows("t.id = %s", (transition_id,))
        return rows[0] if rows else None

    def upsert(self, transition_id: int, *, seam_at: datetime, pushed_at: Optional[datetime] = None,
               shown_at: Optional[datetime] = None) -> dict[str, Any]:
        """THE one write that creates or fills a record: a column already set
        is never changed."""
        with self._connect() as conn:
            cur = conn.execute(
                "INSERT INTO strike_alerts (transition_id, seam_at, pushed_at, shown_at) VALUES (%s, %s, %s, %s) "
                "ON CONFLICT (transition_id) DO UPDATE SET "
                "seam_at = COALESCE(strike_alerts.seam_at, EXCLUDED.seam_at), "
                "pushed_at = COALESCE(strike_alerts.pushed_at, EXCLUDED.pushed_at), "
                "shown_at = COALESCE(strike_alerts.shown_at, EXCLUDED.shown_at) "
                f"RETURNING {_RECORD}",
                (transition_id, seam_at, pushed_at, shown_at),
            )
            row = cur.fetchone()
            names = [d.name for d in cur.description]
            conn.commit()
        return dict(zip(names, row))

    def claim_dm(self, transition_id: int, now: datetime) -> bool:
        """The DM claim on the unique row: never twice, never once shown."""
        with self._connect() as conn:
            row = conn.execute(
                "UPDATE strike_alerts SET dm_at = %s WHERE transition_id = %s AND dm_at IS NULL "
                "AND shown_at IS NULL RETURNING transition_id",
                (now, transition_id),
            ).fetchone()
            conn.commit()
        return row is not None

    def record_dm_result(self, transition_id: int, result: str) -> None:
        with self._connect() as conn:
            conn.execute("UPDATE strike_alerts SET dm_result = %s WHERE transition_id = %s",
                         (result, transition_id))
            conn.commit()

    def records_for(self, transition_ids: list[int]) -> dict[int, dict[str, Any]]:
        if not transition_ids:
            return {}
        with self._connect() as conn:
            cur = conn.execute(f"SELECT {_RECORD} FROM strike_alerts WHERE transition_id = ANY(%s)",
                               (list(transition_ids),))
            names = [d.name for d in cur.description]
            return {int(r[0]): dict(zip(names, r)) for r in cur.fetchall()}


# ---------------------------------------------------------------------
# S1 — the stream
# ---------------------------------------------------------------------


@dataclass
class StreamDeps:
    store: Any
    settings: DeliverySettings
    now: Callable[[], datetime] = field(default_factory=lambda: clock_mod.now_utc)
    monotonic: Callable[[], float] = time.monotonic
    sleep: Callable[[float], Awaitable[None]] = asyncio.sleep
    #: Ends the stream when true (tests); the route also ends it when the
    #: client disconnects.
    stop: Optional[Callable[[], bool]] = None


def _mark_pushed(store, row: SeamRow, now: datetime) -> None:
    try:
        store.upsert(row.transition_id, seam_at=row.at, pushed_at=now)
    except Exception as e:  # the event still goes out; the record is said missing
        logger.error("strike stream: pushed_at NOT recorded for transition {}: {}", row.transition_id, e)


async def event_stream(deps: StreamDeps, *, last_event_id: Optional[int], stop: Callable[[], Awaitable[bool]]):
    cursor = last_event_id
    last_out = deps.monotonic()
    while not await stop():
        now = deps.now()
        try:
            rows = await asyncio.to_thread(deps.store.seam_rows, cursor, now.astimezone(ET).date())
        except Exception as e:
            # No keepalive while the read fails: the tab says STREAM DOWN.
            logger.error("strike stream: seam read failed — no keepalive until it reads: {}", e)
            await deps.sleep(deps.settings.stream_tail_ms / 1000)
            continue
        for row in rows:
            kind = seam_kind(row)
            if kind is None:
                # Never past a row not sent: his tap, written by the sheet, can
                # take a higher id than a detector row not yet committed.
                continue
            cursor = max(cursor or 0, row.transition_id)
            await asyncio.to_thread(_mark_pushed, deps.store, row, deps.now())
            yield format_event(kind, row, deps.settings)
            last_out = deps.monotonic()
        if deps.monotonic() - last_out >= deps.settings.keepalive_s:
            yield keepalive(deps.now())
            last_out = deps.monotonic()
        await deps.sleep(deps.settings.stream_tail_ms / 1000)


def get_stream_deps() -> StreamDeps:
    return StreamDeps(store=StrikeAlertStore(), settings=load_delivery_config())


@router.get("/strike/stream")
async def strike_stream(request: Request, deps: StreamDeps = Depends(get_stream_deps)):
    raw = request.headers.get("last-event-id")
    last_event_id = None
    if raw is not None and raw.strip():
        if not raw.strip().isdigit():
            return JSONResponse({"error": f"REFUSED: Last-Event-ID {raw!r} is not a transition id."},
                                status_code=400)
        last_event_id = int(raw.strip())

    async def stop() -> bool:
        if deps.stop is not None and deps.stop():
            return True
        return await request.is_disconnected()

    return StreamingResponse(event_stream(deps, last_event_id=last_event_id, stop=stop),
                             media_type="text/event-stream",
                             headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})


# ---------------------------------------------------------------------
# S3 — the ack
# ---------------------------------------------------------------------


def ack(store, transition_id: int, now: datetime) -> Optional[dict[str, Any]]:
    """`shown_at` for a seam row (first ack wins); None when the id is not one."""
    row = store.transition(transition_id)
    if row is None or seam_kind(row) is None:
        return None
    return store.upsert(transition_id, seam_at=row.at, shown_at=now)


def get_alert_store() -> StrikeAlertStore:
    return StrikeAlertStore()


@router.post("/strike/ack")
async def strike_ack(request: Request, store=Depends(get_alert_store)):
    try:
        body = await request.json()
        transition_id = body["transition_id"]
        if isinstance(transition_id, bool) or not isinstance(transition_id, int):
            raise TypeError(type(transition_id).__name__)
    except Exception as e:
        return JSONResponse({"error": f"REFUSED: body must be {{\"transition_id\": <int>}} ({e!r}). Nothing written."},
                            status_code=422)
    record = await asyncio.to_thread(ack, store, transition_id, clock_mod.now_utc())
    if record is None:
        return JSONResponse({"error": f"REFUSED: transition {transition_id} is not a strike seam row. "
                                      "Nothing written."}, status_code=404)
    return JSONResponse({"transition_id": transition_id, "shown_at": record["shown_at"].isoformat()})


# ---------------------------------------------------------------------
# S2 — the pinned tab
# ---------------------------------------------------------------------

_LABELS = ("key", "shares", "stop", "hotkey")


def alert_values(payload: dict[str, Any]) -> dict[str, str]:
    """The alert's title and its four values — nothing else of the event."""
    return {"title": f"{payload['ticker']} {str(payload['direction']).upper()}", "key": _na(payload["key"]),
            "shares": _na(payload["shares"]), "stop": _na(payload["stop"]), "hotkey": _na(payload["hotkey"])}


def alert_html(values: Optional[dict[str, str]] = None) -> str:
    """The alert box: the page's template (values None, hidden) or a sample."""
    v = values or {name: "" for name in ("title", *_LABELS)}
    hidden = " hidden" if values is None else ""
    items = "".join(f'<div><dt>{name}</dt><dd data-field="{name}">{html.escape(v[name])}</dd></div>'
                    for name in _LABELS)
    return (f'<section class="strike-alert" id="strike-alert"{hidden}>'
            f'<div class="alert-title" data-field="title">{html.escape(v["title"])}</div><dl>{items}</dl></section>')


STRIKE_CSS = """
 body{font-family:system-ui,sans-serif;background:#0b1020;color:#eef5ff;margin:0;padding:16px}
 main{max-width:720px;margin:0 auto}
 h1{font-size:18px;letter-spacing:.06em;margin:0 0 12px}
 nav a{color:#9fafca}
 button#arm{width:100%;padding:16px;font-size:20px;font-weight:800;border-radius:10px;border:2px solid #00e5ff;background:#0b1020;color:#00e5ff;cursor:pointer}
 .loud{background:#3a0d18;border:1px solid #ff4f71;color:#ffc3ce;padding:10px;border-radius:8px;margin:10px 0;font-weight:800}
 .strike-alert{background:#11331f;border:3px solid #24d986;border-radius:14px;padding:18px;margin:14px 0}
 .alert-title{font-size:34px;font-weight:900;letter-spacing:.04em}
 .strike-alert dl{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:12px 0 0}
 .strike-alert dt{font-size:12px;text-transform:uppercase;color:#9fafca}
 .strike-alert dd{margin:0;font-size:30px;font-weight:900}
 #events{list-style:none;padding:0;font-family:ui-monospace,monospace;font-size:13px;color:#c7d3ea}
 #events li{padding:4px 0;border-bottom:1px solid #20283c}
 #events li.missed{color:#8d9bb6}
"""

STRIKE_JS = r"""
(function(){
 const cfg=JSON.parse(document.body.dataset.strike);
 const loadedAt=Date.now();
 const TITLE='Cobalt · Strike';
 let armed=false, audio=null, lastBeat=Date.now(), downSince=null, flashTimer=null;
 const $=function(id){return document.getElementById(id);};
 function state(id,text){const el=$(id); el.textContent=text||''; el.hidden=!text;}
 function hhmmss(d){return d.toTimeString().slice(0,8);}
 function notifState(){
   if(!window.isSecureContext){return 'NOTIFICATIONS OFF — insecure origin';}
   if(!('Notification' in window)){return 'NOTIFICATIONS OFF — not supported by this browser';}
   if(Notification.permission!=='granted'){return 'NOTIFICATIONS OFF — permission '+Notification.permission;}
   return '';
 }
 function refreshStates(){
   state('notif-state',notifState());
   state('sound-state',armed?'':'SOUND LOCKED — press ARM');
   if(downSince===null&&Date.now()-lastBeat>2*cfg.keepalive_s*1000){downSince=new Date(lastBeat);}
   state('stream-state',downSince===null?'':'STREAM DOWN · since '+hhmmss(downSince));
 }
 $('arm').addEventListener('click',async function(){
   try{audio=audio||new (window.AudioContext||window.webkitAudioContext)(); await audio.resume(); armed=audio.state==='running';}catch(e){armed=false;}
   if(window.isSecureContext&&('Notification' in window)&&Notification.permission==='default'){try{await Notification.requestPermission();}catch(e){}}
   refreshStates();
 });
 function tone(){
   if(!armed||!audio){return;}
   const o=audio.createOscillator(), g=audio.createGain(); o.type='square'; o.frequency.value=880; g.gain.value=0.25;
   o.connect(g); g.connect(audio.destination); const t=audio.currentTime; o.start(t); o.stop(t+0.7);
 }
 function stopFlash(){if(flashTimer){clearInterval(flashTimer); flashTimer=null;} document.title=TITLE;}
 function flash(text){stopFlash(); let on=false; flashTimer=setInterval(function(){on=!on; document.title=on?text:TITLE;},700);}
 document.addEventListener('click',function(event){if(!event.target.closest('#arm')){stopFlash();}});
 function na(v){return (v===null||v===undefined)?'n/a':String(v);}
 function values(p){return {title:p.ticker+' '+String(p.direction).toUpperCase(),key:na(p.key),shares:na(p.shares),stop:na(p.stop),hotkey:na(p.hotkey)};}
 function body(v){return 'key '+v.key+' · '+v.shares+' sh · stop '+v.stop+' · '+v.hotkey;}
 function line(kind,text){const li=document.createElement('li'); li.className=kind; li.textContent=hhmmss(new Date())+' '+text; $('events').prepend(li);}
 function draw(p){
   const v=values(p); const box=$('strike-alert');
   box.querySelectorAll('[data-field]').forEach(function(el){el.textContent=v[el.dataset.field];});
   box.hidden=false;
   if(!notifState()){try{new Notification(v.title,{body:body(v),requireInteraction:true,tag:'strike-'+p.transition_id});}catch(e){line('missed','NOTIFICATION FAILED · '+String(e));}}
   tone(); flash(v.title+' · TRIGGERED');
   fetch('/strike/ack',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify({transition_id:p.transition_id})})
     .then(function(r){if(!r.ok){line('missed','ACK REFUSED '+r.status+' · transition '+p.transition_id);}})
     .catch(function(e){line('missed','ACK FAILED · '+String(e));});
 }
 function beat(){lastBeat=Date.now(); downSince=null; refreshStates();}
 const source=new EventSource('/strike/stream');
 source.addEventListener('open',beat);
 source.addEventListener('keepalive',beat);
 source.addEventListener('trigger',function(e){
   beat(); const p=JSON.parse(e.data); const v=values(p);
   const fresh=Date.parse(p.at)>=loadedAt-cfg.dm_after_s*1000;
   line('trigger','TRIGGERED '+v.title+' · '+body(v)+(fresh?'':' · before this tab opened, not alerted'));
   if(fresh){draw(p);}
 });
 source.addEventListener('missed',function(e){beat(); const p=JSON.parse(e.data); line('missed','MISSED '+values(p).title);});
 source.addEventListener('error',function(){if(downSince===null){downSince=new Date();} refreshStates();});
 window.setInterval(refreshStates,1000);
 refreshStates();
})();
"""


def render_strike_page(settings: DeliverySettings) -> str:
    cfg = html.escape(json.dumps({"keepalive_s": settings.keepalive_s, "dm_after_s": settings.dm_after_s}))
    return (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1"><title>Cobalt · Strike</title>'
        f"<style>{STRIKE_CSS}</style></head>"
        f'<body data-strike="{cfg}"><main><nav><a href="/">ASET sheet</a> · <a href="/radar">Trade Radar</a></nav>'
        "<h1>STRIKE · pinned tab</h1>"
        '<button id="arm" type="button">ARM</button>'
        '<div class="loud" id="stream-state" hidden></div>'
        '<div class="loud" id="notif-state" hidden></div>'
        '<div class="loud" id="sound-state">SOUND LOCKED — press ARM</div>'
        f"{alert_html()}"
        '<h2>Today</h2><ul id="events"></ul>'
        f"</main><script>{STRIKE_JS}</script></body></html>"
    )


@router.get("/strike", response_class=HTMLResponse)
def strike_page():
    return HTMLResponse(render_strike_page(load_delivery_config()))


# ---------------------------------------------------------------------
# S4 — the phone fallback, the sheet's own tail
# ---------------------------------------------------------------------


class FallbackTail:
    """One pass: read the new seam rows, create each trigger's S3 row, DM
    every trigger nobody was shown `dm_after_s` after its `at`. Synchronous."""

    def __init__(self, *, store, send: Callable[[str], Any], settings: DeliverySettings,
                 now: Callable[[], datetime]):
        self.store = store
        self.send = send
        self.settings = settings
        self.now = now
        self._cursor: Optional[int] = None
        self._pending: dict[int, SeamRow] = {}
        #: A DM sent whose `dm_result` write failed: written again next pass,
        #: never sent again.
        self._unrecorded: dict[int, str] = {}

    def pass_once(self) -> list[int]:
        now = self.now()
        for tid, outcome in list(self._unrecorded.items()):
            self.store.record_dm_result(tid, outcome)
            del self._unrecorded[tid]
        for row in self.store.seam_rows(self._cursor, now.astimezone(ET).date()):
            kind = seam_kind(row)
            if kind is None:
                # Never past a row that is not P1's seam: his tap can take a
                # higher id than a detector row not yet committed.
                continue
            if kind == "trigger":
                self.store.upsert(row.transition_id, seam_at=row.at)
                self._pending[row.transition_id] = row
            # Past the row only once its record exists: a failed upsert is read again.
            self._cursor = max(self._cursor or 0, row.transition_id)
        sent: list[int] = []
        for tid, row in list(self._pending.items()):
            if (now - row.at).total_seconds() < self.settings.dm_after_s:
                continue
            claimed = self.store.claim_dm(tid, now)
            del self._pending[tid]
            if not claimed:
                continue  # shown, or already DM'd
            try:
                outcome = self.send(dm_text(row, self.settings)).report()
            except Exception as e:
                outcome = f"DM FAILED — {type(e).__name__}: {e}"
                logger.error("strike fallback: transition {} {}", tid, outcome)
            self._unrecorded[tid] = outcome
            sent.append(tid)
            self.store.record_dm_result(tid, outcome)
            del self._unrecorded[tid]
        return sent


#: A failure that persists with the same text logs its ERROR again once this
#: many seconds have passed since the last one — a failing fallback is never
#: silent. A code constant, not a tunable.
REPEAT_ERROR_S = 60.0


class FallbackThread(threading.Thread):
    """`FallbackTail.pass_once` every `interval_s`; an exception in a pass is
    logged and the thread goes on — it never takes the sheet down. A failure
    streak logs an ERROR with its running count (a new text at once, the same
    text again every `REPEAT_ERROR_S`); its end logs one `recovered` INFO; a
    thread whose first pass succeeds logs one `first pass OK` INFO."""

    def __init__(self, tail, *, interval_s: float, monotonic: Callable[[], float] = time.monotonic):
        super().__init__(name="strike-fallback", daemon=True)
        self.tail = tail
        self.interval_s = interval_s
        self.monotonic = monotonic
        self.stopping = threading.Event()
        self._failed = 0
        self._last_error: Optional[str] = None
        self._last_error_at: Optional[float] = None
        self._stepped = False

    def stop(self) -> None:
        self.stopping.set()

    def step(self) -> None:
        """One pass and its one logging decision; never raises a pass's exception."""
        try:
            self.tail.pass_once()
        except Exception as e:
            try:
                text = f"{type(e).__name__}: {e}"
            except Exception:  # an exception that cannot print itself still never stops the thread
                text = f"{type(e).__name__}: <str() failed>"
            self._failed += 1
            now = self.monotonic()
            repeat_due = self._last_error_at is None or now - self._last_error_at >= REPEAT_ERROR_S
            if text != self._last_error or repeat_due:
                logger.error("strike fallback: pass failed — the thread goes on: {} (failed passes: {})",
                             text, self._failed)
                self._last_error_at = now
            self._last_error = text
        else:
            if self._failed:
                logger.info("strike fallback: recovered after {} failed passes", self._failed)
            elif not self._stepped:
                logger.info("strike fallback: first pass OK")
            self._failed = 0
            self._last_error = None
            self._last_error_at = None
        self._stepped = True

    def run(self) -> None:
        while not self.stopping.is_set():
            self.step()
            self.stopping.wait(self.interval_s)


def start_fallback_thread() -> FallbackThread:
    """The sheet's one fallback thread (`aset/__main__.py`, before uvicorn)."""
    from cobalt.notify.mattermost import send_dm

    settings = load_delivery_config()
    tail = FallbackTail(store=StrikeAlertStore(), send=send_dm, settings=settings, now=clock_mod.now_utc)
    thread = FallbackThread(tail, interval_s=settings.stream_tail_ms / 1000)
    thread.start()
    return thread


__all__ = [
    "FallbackTail", "FallbackThread", "SeamRow", "StreamDeps", "StrikeAlertStore", "VIA_MISSED", "VIA_TRIGGERED",
    "ack", "alert_html", "alert_values", "dm_text", "event_payload", "event_stream", "format_event",
    "get_alert_store", "get_stream_deps", "keepalive", "render_strike_page", "router", "seam_kind",
    "start_fallback_thread",
]
