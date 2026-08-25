"""ASET semi-auto sheet — simplest working local form (FastAPI).

Modeled on the trade-reporter Flask pattern (single page + JSON
endpoints) using the FastAPI/uvicorn stack already in the project deps.
Fail-loud: any missing data renders a visible FAILED banner — never a
blank or guessed field. Obsidian/mission-control rendering comes later.
"""

import html

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

from .config import ConfigError, load_config
from .daily_note import DailyNoteRefused, save_card
from .engine import (
    SizingError,
    compute_sizing,
    daily_stop_from_account,
    enforce_broker_cap,
)
from .models import GRADE_RISK_PCT, Direction, Grade, SizingInput
from .prefill import PrefillError, fetch_last_price
from .store import AsetStore

app = FastAPI(title="Cobalt ASET Sheet", docs_url=None, redoc_url=None)

CSS = """
 body{font-family:system-ui,sans-serif;background:#0b1020;color:#eef5ff;margin:0;padding:24px}
 .wrap{max-width:640px;margin:0 auto}
 h1{font-size:22px;letter-spacing:.06em}
 .card{background:#111729;border:1px solid #20283c;border-radius:12px;padding:18px;margin-bottom:16px}
 label{display:block;font-size:11px;text-transform:uppercase;color:#9fafca;margin:10px 0 4px}
 input,select{width:100%;padding:10px;border-radius:8px;border:1px solid #232d44;background:#0b1020;color:#eef5ff;font-size:15px;box-sizing:border-box}
 .row{display:flex;gap:12px} .row>div{flex:1}
 button{padding:10px 16px;border-radius:8px;border:1px solid #28334d;background:#0b1020;color:#8d9bb6;font-weight:700;cursor:pointer;margin-top:12px}
 button.primary{border-color:#00e5ff;color:#00e5ff}
 .toggle{display:flex;gap:10px} .toggle button{flex:1;margin-top:0}
 .toggle button.active-long{color:#24d986;border-color:#24d986;background:rgba(36,217,134,.12)}
 .toggle button.active-short{color:#ff4f71;border-color:#ff4f71;background:rgba(255,79,113,.12)}
 .failed{background:#3a0d18;border:1px solid #ff4f71;color:#ffc3ce;padding:12px;border-radius:8px;margin-bottom:16px;font-weight:700;white-space:pre-wrap}
 .saved{background:#0d2a1c;border:1px solid #24d986;color:#b8f5d9;padding:12px;border-radius:8px;margin-bottom:16px;font-weight:700}
 .result{border-color:#24d986}
 .shares{font-size:52px;font-weight:900;color:#24d986}
 .warn{color:#ffd84d;font-size:13px;margin-top:6px}
 #capWarn{display:none}
 table{width:100%;font-size:13px;border-collapse:collapse} td{padding:4px 8px;border-bottom:1px solid #20283c}
 .muted{color:#7f8ca8;font-size:12px}
"""

JS = """
 const CAP = window.BROKER_CAP;
 const $ = id => document.getElementById(id);
 let lastFetched = null;
 let entryDirty = $('entry').value !== '';

 function setDir(d){
   $('direction').value = d;
   $('longBtn').classList.toggle('active-long', d === 'long');
   $('shortBtn').classList.toggle('active-short', d === 'short');
 }

 async function prefill(){
   const t = $('ticker').value.trim();
   if(!t) return;
   const out = $('last_price');
   out.value = '...';
   try {
     const r = await fetch('/api/prefill?ticker=' + encodeURIComponent(t));
     const j = await r.json();
     if (!r.ok) throw new Error(j.error || r.status);
     out.value = j.price;
     $('price_source').value = j.source;
     if (!entryDirty) $('entry').value = j.price;
     lastFetched = t.toUpperCase();
   } catch (e) {
     out.value = 'FAILED';
     $('price_source').value = '';
     alert('Prefill FAILED: ' + e.message);
   }
 }

 function clampStop(){
   const ds = $('daily_stop');
   const v = parseFloat(ds.value);
   if (!isFinite(v)) { $('capWarn').style.display = 'none'; return; }
   if (v > CAP) ds.value = CAP;
   $('capWarn').style.display = parseFloat(ds.value) >= CAP ? 'block' : 'none';
 }

 window.addEventListener('DOMContentLoaded', () => {
   setDir($('direction').value || 'long');
   $('ticker').addEventListener('blur', () => {
     const t = $('ticker').value.trim().toUpperCase();
     if (t && t !== lastFetched) prefill();
   });
   $('entry').addEventListener('input', () => { entryDirty = true; });
   $('daily_stop').addEventListener('input', clampStop);
   clampStop();
 });
"""

FORM_FIELDS = (
    "ticker", "grade", "direction", "daily_stop", "entry", "stop",
    "last_price", "price_source",
)


def _options(pairs, selected):
    return "".join(
        f'<option value="{html.escape(v)}"{" selected" if v == selected else ""}>'
        f"{html.escape(label)}</option>"
        for v, label in pairs
    )


def _render(banner: str = "", result: str = "", form: dict | None = None) -> str:
    cfg = load_config()
    form = form or {}
    requested = cfg.daily_stop_default or daily_stop_from_account(cfg.account_size)
    prefill_stop = min(requested, cfg.broker_hard_stop)
    daily = form.get("daily_stop") or str(prefill_stop)
    grade_pairs = [(g.value, f"{g.value} · {int(GRADE_RISK_PCT[g])}%") for g in Grade]
    direction = form.get("direction", "long")

    e = html.escape
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cobalt · ASET Sheet</title>
<style>{CSS}</style></head><body><div class="wrap">
<h1>ASET SEMI-AUTO SHEET <span class="muted">pre-beta slice 1 · dev</span></h1>
{banner}
{result}
<form class="card" method="post" action="/size">
 <div class="row"><div>
  <label>Ticker <span class="muted">(tab out to fetch)</span></label>
  <input name="ticker" id="ticker" required autocomplete="off" value="{e(form.get("ticker", ""))}">
 </div><div>
  <label>Last price <span class="muted">(prefill)</span></label>
  <input name="last_price" id="last_price" readonly placeholder="—" value="{e(form.get("last_price", ""))}">
  <input type="hidden" name="price_source" id="price_source" value="{e(form.get("price_source", ""))}">
 </div></div>
 <button type="button" onclick="prefill()">Re-fetch last price</button>
 <div class="row"><div>
  <label>Grade (yours, always)</label>
  <select name="grade">{_options(grade_pairs, form.get("grade", "B"))}</select>
 </div><div>
  <label>Direction</label>
  <div class="toggle">
   <button type="button" id="longBtn" onclick="setDir('long')">LONG</button>
   <button type="button" id="shortBtn" onclick="setDir('short')">SHORT</button>
  </div>
  <input type="hidden" name="direction" id="direction" value="{e(direction)}">
 </div></div>
 <div class="row"><div>
  <label>Entry $ <span class="muted">(prefilled from last price, edit freely)</span></label>
  <input name="entry" id="entry" type="number" step="0.0001" required value="{e(form.get("entry", ""))}">
 </div><div>
  <label>Stop $ (yours, always)</label>
  <input name="stop" type="number" step="0.0001" required value="{e(form.get("stop", ""))}">
 </div></div>
 <label>Daily stop $ <span class="muted">(prefill {e(str(prefill_stop))} · broker hard cap {e(str(cfg.broker_hard_stop))})</span></label>
 <input name="daily_stop" id="daily_stop" type="number" step="0.01" max="{e(str(cfg.broker_hard_stop))}" required value="{e(daily)}">
 <div class="warn" id="capWarn">⚠ Daily stop is AT the broker hard cap (${e(str(cfg.broker_hard_stop))}). Anything above is refused.</div>
 <button class="primary" type="submit">Compute &amp; persist</button>
</form>
<div class="muted">Every computed sizing persists to Postgres ({e(cfg.db_name)}). Missing data = FAILED, never guessed.</div>
<script>window.BROKER_CAP = {float(cfg.broker_hard_stop)};</script>
<script>{JS}</script>
</div></body></html>"""


def _failed(message: str) -> str:
    return f'<div class="failed">FAILED\n{html.escape(message)}</div>'


def _parse_input(form: dict) -> SizingInput:
    return SizingInput(
        ticker=form.get("ticker", ""),
        grade=form.get("grade", ""),
        direction=form.get("direction", ""),
        daily_stop=form.get("daily_stop", "0"),
        entry=form.get("entry", "0"),
        stop=form.get("stop", "0"),
        last_price=form.get("last_price") or None,
        price_source=form.get("price_source") or None,
    )


def _result_card(result, row_note: str, form: dict) -> str:
    inp = result.input
    warnings_html = "".join(
        f'<div class="warn">⚠ {html.escape(w)}</div>' for w in result.warnings
    )
    hidden = "".join(
        f'<input type="hidden" name="{f}" value="{html.escape(form.get(f, ""))}">'
        for f in FORM_FIELDS
    )
    return f"""<div class="card result">
      <div class="shares">{result.shares:,} <span style="font-size:18px">shares</span></div>
      <table>
       <tr><td>Ticker / grade / direction</td><td>{html.escape(inp.ticker)} · {inp.grade.value} ({result.risk_pct}%) · {inp.direction.value.upper()}</td></tr>
       <tr><td>Risk budget</td><td>${result.risk_budget}</td></tr>
       <tr><td>Risk / share</td><td>${result.per_share_risk}</td></tr>
       <tr><td>Total used risk</td><td>${result.used_risk}</td></tr>
       <tr><td>Target 1R / 2R</td><td>${result.target_1r} / ${result.target_2r}</td></tr>
       <tr><td>{html.escape(row_note.split(":", 1)[0])}</td><td>{html.escape(row_note.split(":", 1)[1].strip())}</td></tr>
      </table>
      {warnings_html}
      <form method="post" action="/note">{hidden}
       <button type="submit">Save to Daily Note</button>
      </form>
    </div>"""


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return _render()


@app.get("/api/prefill")
async def api_prefill(ticker: str):
    try:
        price, source = await fetch_last_price(ticker)
    except PrefillError as e:
        return JSONResponse({"error": str(e)}, status_code=502)
    return {"ticker": ticker.strip().upper(), "price": str(price), "source": source}


@app.post("/size", response_class=HTMLResponse)
async def size(request: Request) -> str:
    form = {k: str(v) for k, v in (await request.form()).items()}
    try:
        cfg = load_config()
        inp = _parse_input(form)
        cap_warnings = enforce_broker_cap(inp.daily_stop, cfg.broker_hard_stop)
        result = compute_sizing(inp)
        result.warnings.extend(cap_warnings)
        store = AsetStore(cfg.db_name)
        store.ensure_schema()
        row_id = store.save(result)
    except (SizingError, ConfigError) as e:
        return _render(banner=_failed(str(e)), form=form)
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"), form=form)
    return _render(
        result=_result_card(result, f"Persisted: aset_sizings id {row_id} ({cfg.db_name})", form),
        form=form,
    )


@app.post("/note", response_class=HTMLResponse)
async def note(request: Request) -> str:
    form = {k: str(v) for k, v in (await request.form()).items()}
    try:
        cfg = load_config()
        inp = _parse_input(form)
        cap_warnings = enforce_broker_cap(inp.daily_stop, cfg.broker_hard_stop)
        result = compute_sizing(inp)  # deterministic recompute; no re-persist
        result.warnings.extend(cap_warnings)
        path = save_card(cfg, result)
    except (SizingError, ConfigError, DailyNoteRefused) as e:
        return _render(banner=_failed(str(e)), form=form)
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"), form=form)
    banner = f'<div class="saved">Appended to {html.escape(str(path))}</div>'
    return _render(
        banner=banner,
        result=_result_card(result, "Saved: appended to today's daily note", form),
        form=form,
    )
