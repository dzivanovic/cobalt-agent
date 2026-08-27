"""ASET semi-auto sheet — simplest working local form (FastAPI).

Modeled on the trade-reporter Flask pattern (single page + JSON
endpoints) using the FastAPI/uvicorn stack already in the project deps.
Fail-loud: any missing data renders a visible FAILED banner — never a
blank or guessed field. Obsidian/mission-control rendering comes later.

Iteration 4 (ruled by Dejan, 2026-08-28): daily-stop input replaced by
a FULL/HALF sheet-mode toggle (fixed dollar risk per grade, see
configs/cobalt/aset.yaml); "Compute & persist" now ALSO appends the
card to the daily note in the same action (no separate Save button —
a card that isn't in the journal didn't happen); an "actual fill"
field recomputes shares at the real fill price and appends a linked
FILL UPDATE block.

Config-completion follow-up (Dejan, 2026-08-28): the grade selector now
lists the FULL ladder (A+/A/B/C/D), not just A/B. Grades outside
`SheetModesConfig.enabled_grades` render as disabled `<option>`s with a
suffixed label ("no trade (SAW)" for C/D, "reserved" for A+) — greyed,
unselectable via the native dropdown, and refused server-side too
(`compute_sizing` takes `enabled_grades` as an explicit argument) in
case a stale hidden-field POST bypasses the dropdown entirely.
Enabling a grade is a `configs/cobalt/aset.yaml` edit only.
"""

import html
import json
from datetime import datetime
from decimal import Decimal, InvalidOperation

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse

from .config import ConfigError, load_config, load_sheet_modes_config
from .daily_note import DailyNoteRefused, save_card, save_fill_update
from .engine import SizingError, compute_fill_recompute, compute_sizing
from .models import Grade, SizingInput
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
 .toggle button.active-mode{color:#00e5ff;border-color:#00e5ff;background:rgba(0,229,255,.12)}
 .failed{background:#3a0d18;border:1px solid #ff4f71;color:#ffc3ce;padding:12px;border-radius:8px;margin-bottom:16px;font-weight:700;white-space:pre-wrap}
 .saved{background:#0d2a1c;border:1px solid #24d986;color:#b8f5d9;padding:12px;border-radius:8px;margin-bottom:16px;font-weight:700}
 .result{border-color:#24d986}
 .shares{font-size:52px;font-weight:900;color:#24d986}
 .warn{color:#ffd84d;font-size:13px;margin-top:6px}
 .hint{color:#7f8ca8;font-size:12px;margin-top:4px;font-style:italic}
 #entryHint{display:none}
 table{width:100%;font-size:13px;border-collapse:collapse} td{padding:4px 8px;border-bottom:1px solid #20283c}
 .muted{color:#7f8ca8;font-size:12px}
 option:disabled{color:#55607a}
"""

JS = """
 const MODE_DOLLARS = window.SHEET_MODE_DOLLARS;
 const $ = id => document.getElementById(id);

 // STATE PRINCIPLE: the ticker defines the decision context. Changing
 // the ticker = new decision = full reset. Within one ticker, entry
 // tracks last price until Dejan manually edits entry (entryDirty),
 // which resets only when the ticker changes.
 let currentTicker = window.INITIAL_TICKER || null;
 let entryDirty = window.INITIAL_ENTRY_DIRTY;

 function setDir(d){
   $('direction').value = d;
   $('longBtn').classList.toggle('active-long', d === 'long');
   $('shortBtn').classList.toggle('active-short', d === 'short');
 }

 function setMode(m){
   $('sheet_mode').value = m;
   $('fullBtn').classList.toggle('active-mode', m === 'full');
   $('halfBtn').classList.toggle('active-mode', m === 'half');
   updateModeHint();
 }

 function updateModeHint(){
   const mode = $('sheet_mode').value;
   const grade = $('grade').value;
   const dollars = (MODE_DOLLARS[mode] || {})[grade];
   const hint = $('modeHint');
   if (dollars === undefined) { hint.style.display = 'none'; return; }
   hint.textContent = 'risk budget: $' + dollars;
   hint.style.display = 'block';
 }

 function markEntryDirty(){
   entryDirty = true;
   $('entry_dirty').value = '1';
   $('entryHint').style.display = 'none';
 }

 function showEntryHint(freshPrice){
   $('entryHint').textContent = 'entry differs from last ($' + freshPrice + ')';
   $('entryHint').style.display = 'block';
 }

 function clearForNewTicker(){
   entryDirty = false;
   $('entry_dirty').value = '';
   $('orig_timestamp').value = '';
   $('resultCard').innerHTML = '';
   $('banner').innerHTML = '';
   $('entry').value = '';
   $('stop').value = '';
   $('last_price').value = '';
   $('price_source').value = '';
   $('entryHint').style.display = 'none';
 }

 async function doFetch(ticker){
   const out = $('last_price');
   out.value = '...';
   try {
     const r = await fetch('/api/prefill?ticker=' + encodeURIComponent(ticker));
     const j = await r.json();
     if (!r.ok) throw new Error(j.error || r.status);
     $('price_source').value = j.source;
     return j.price;
   } catch (e) {
     out.value = 'FAILED';
     $('price_source').value = '';
     alert('Prefill FAILED: ' + e.message);
     return null;
   }
 }

 async function handleTicker(rawTicker){
   const t = rawTicker.trim().toUpperCase();
   if (!t) return;

   if (t !== currentTicker) {
     // Symptom 1: ticker change = new decision = full reset, THEN fetch.
     currentTicker = t;
     clearForNewTicker();
     const price = await doFetch(t);
     if (price !== null) {
       $('last_price').value = price;
       $('entry').value = price;  // always overwritten on a ticker change
     }
   } else {
     // Symptom 2: same-ticker re-fetch.
     const price = await doFetch(t);
     if (price === null) return;
     $('last_price').value = price;
     if (!entryDirty) {
       $('entry').value = price;
       $('entryHint').style.display = 'none';
     } else if ($('entry').value !== String(price)) {
       showEntryHint(price);
     } else {
       $('entryHint').style.display = 'none';
     }
   }
 }

 window.addEventListener('DOMContentLoaded', () => {
   setDir($('direction').value || 'long');
   setMode($('sheet_mode').value || 'full');
   $('ticker').addEventListener('blur', () => handleTicker($('ticker').value));
   $('fetchBtn').addEventListener('click', () => handleTicker($('ticker').value));
   $('entry').addEventListener('input', markEntryDirty);
   $('grade').addEventListener('change', updateModeHint);
 });
"""

FORM_FIELDS = (
    "ticker", "grade", "direction", "sheet_mode", "entry", "stop",
    "last_price", "price_source", "entry_dirty", "orig_timestamp",
)


# Suffix appended to a disabled grade's option label — why it's greyed
# out, not just that it is. C/D share "no trade (SAW)" (the Daily-Stop
# Model card's framing); A+ gets its own "reserved" since it isn't a
# no-trade grade, it's just not live yet.
_GRADE_DISABLED_SUFFIX = {
    Grade.A_PLUS: "reserved",
    Grade.C: "no trade (SAW)",
    Grade.D_SAW: "no trade (SAW)",
}


def _grade_options(sheet_modes_cfg, selected: str) -> str:
    parts = []
    for g in Grade:
        enabled = sheet_modes_cfg.is_enabled(g)
        label = g.value if enabled else f"{g.value} — {_GRADE_DISABLED_SUFFIX[g]}"
        attrs = f'value="{html.escape(g.value)}"'
        if g.value == selected:
            attrs += " selected"
        if not enabled:
            attrs += " disabled"
        parts.append(f"<option {attrs}>{html.escape(label)}</option>")
    return "".join(parts)


def _render(banner: str = "", result: str = "", form: dict | None = None) -> str:
    cfg = load_config()
    sheet_modes_cfg = load_sheet_modes_config()
    form = form or {}
    direction = form.get("direction", "long")
    sheet_mode = form.get("sheet_mode", "full")

    e = html.escape
    initial_ticker = form.get("ticker", "").strip().upper()
    initial_entry_dirty = bool(form.get("entry_dirty"))
    mode_dollars = {
        "full": {g.value: float(sheet_modes_cfg.dollars_for("full", g)) for g in Grade},
        "half": {g.value: float(sheet_modes_cfg.dollars_for("half", g)) for g in Grade},
    }
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cobalt · ASET Sheet</title>
<style>{CSS}</style></head><body><div class="wrap">
<h1>ASET SEMI-AUTO SHEET <span class="muted">pre-beta slice 1 · dev</span></h1>
<div id="banner">{banner}</div>
<div id="resultCard">{result}</div>
<form class="card" method="post" action="/size">
 <div class="row"><div>
  <label>Ticker <span class="muted">(tab out to fetch)</span></label>
  <input name="ticker" id="ticker" required autocomplete="off" value="{e(form.get("ticker", ""))}">
 </div><div>
  <label>Last price <span class="muted">(prefill)</span></label>
  <input name="last_price" id="last_price" readonly placeholder="—" value="{e(form.get("last_price", ""))}">
  <input type="hidden" name="price_source" id="price_source" value="{e(form.get("price_source", ""))}">
  <input type="hidden" name="entry_dirty" id="entry_dirty" value="{e(form.get("entry_dirty", ""))}">
  <input type="hidden" name="orig_timestamp" id="orig_timestamp" value="{e(form.get("orig_timestamp", ""))}">
 </div></div>
 <button type="button" id="fetchBtn">Re-fetch last price</button>
 <div class="row"><div>
  <label>Grade (yours, always)</label>
  <select name="grade" id="grade">{_grade_options(sheet_modes_cfg, form.get("grade", "B"))}</select>
  <div class="hint" id="modeHint"></div>
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
  <div class="hint" id="entryHint"></div>
 </div><div>
  <label>Stop $ (yours, always)</label>
  <input name="stop" id="stop" type="number" step="0.0001" required value="{e(form.get("stop", ""))}">
 </div></div>
 <label>Sheet mode <span class="muted">(mirrors your DAS hotkey files)</span></label>
 <div class="toggle">
  <button type="button" id="fullBtn" onclick="setMode('full')">FULL</button>
  <button type="button" id="halfBtn" onclick="setMode('half')">HALF</button>
 </div>
 <input type="hidden" name="sheet_mode" id="sheet_mode" value="{e(sheet_mode)}">
 <button class="primary" type="submit">Compute &amp; persist</button>
</form>
<div class="muted">Every computed sizing persists to Postgres ({e(cfg.db_name)}) and appends to today's daily note in the same action. Missing data = FAILED, never guessed.</div>
<script>
window.SHEET_MODE_DOLLARS = {json.dumps(mode_dollars)};
window.INITIAL_TICKER = {json.dumps(initial_ticker)};
window.INITIAL_ENTRY_DIRTY = {json.dumps(initial_entry_dirty)};
</script>
<script>{JS}</script>
</div></body></html>"""


def _failed(message: str) -> str:
    return f'<div class="failed">FAILED\n{html.escape(message)}</div>'


def _resolve_risk_dollars(sheet_modes_cfg, mode: str, grade: str) -> Decimal:
    """Every real Grade now has a configured dollar figure (D is always
    0), so this only needs a fallback for a garbage/missing grade or
    mode string that isn't a valid enum member at all — that placeholder
    lets SizingInput construction proceed so Pydantic's own field
    validation (on `grade`/`sheet_mode`) produces the real error,
    instead of a raw ValueError from Grade()/SheetMode() coercion here."""
    try:
        return sheet_modes_cfg.dollars_for(mode, grade)
    except (ConfigError, ValueError):
        return Decimal("1")


def _parse_input(form: dict, sheet_modes_cfg) -> SizingInput:
    grade = form.get("grade", "")
    sheet_mode = form.get("sheet_mode", "")
    return SizingInput(
        ticker=form.get("ticker", ""),
        grade=grade,
        direction=form.get("direction", ""),
        sheet_mode=sheet_mode,
        risk_dollars=_resolve_risk_dollars(sheet_modes_cfg, sheet_mode, grade),
        entry=form.get("entry", "0"),
        stop=form.get("stop", "0"),
        last_price=form.get("last_price") or None,
        price_source=form.get("price_source") or None,
    )


def _result_card(result, form: dict, fill=None) -> str:
    inp = result.input
    warnings_html = "".join(
        f'<div class="warn">⚠ {html.escape(w)}</div>' for w in result.warnings
    )
    hidden = "".join(
        f'<input type="hidden" name="{f}" value="{html.escape(form.get(f, ""))}">'
        for f in FORM_FIELDS
    )

    fill_html = ""
    if fill is not None:
        fill_warn = (
            f'<div class="warn">⚠ {html.escape(fill.structural_warning)}</div>'
            if fill.structural_warning
            else ""
        )
        fill_html = f"""<div class="card result">
      <div class="shares">{fill.recomputed_shares:,} <span style="font-size:18px">shares @ fill</span></div>
      <table>
       <tr><td>Actual fill</td><td>${fill.actual_fill}</td></tr>
       <tr><td>Recomputed used risk</td><td>${fill.recomputed_used_risk}</td></tr>
       <tr><td>Share delta vs. plan</td><td>{fill.share_delta:+d}</td></tr>
       <tr><td>Distance change vs. plan</td><td>{fill.distance_change_pct}%</td></tr>
      </table>
      {fill_warn}
    </div>"""

    return f"""<div class="card result">
      <div class="shares">{result.shares:,} <span style="font-size:18px">shares</span></div>
      <table>
       <tr><td>Ticker / grade / direction</td><td>{html.escape(inp.ticker)} · {inp.grade.value} · {inp.direction.value.upper()}</td></tr>
       <tr><td>Sheet mode</td><td>{inp.sheet_mode.value.upper()}</td></tr>
       <tr><td>Risk budget</td><td>${result.risk_budget}</td></tr>
       <tr><td>Risk / share</td><td>${result.per_share_risk}</td></tr>
       <tr><td>Total used risk</td><td>${result.used_risk}</td></tr>
       <tr><td>Target 1R / 2R</td><td>${result.target_1r} / ${result.target_2r}</td></tr>
      </table>
      {warnings_html}
    </div>
    {fill_html}
    <form class="card" method="post" action="/fill">{hidden}
     <label>Actual fill $ <span class="muted">(recompute shares at the real fill; appends a FILL UPDATE block)</span></label>
     <input name="actual_fill" type="number" step="0.0001" required value="{html.escape(form.get("actual_fill", ""))}">
     <button type="submit">Recompute at actual fill</button>
    </form>"""


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
        sheet_modes_cfg = load_sheet_modes_config()
        inp = _parse_input(form, sheet_modes_cfg)
        result = compute_sizing(inp, sheet_modes_cfg.enabled_grades)
    except (SizingError, ConfigError) as e:
        return _render(banner=_failed(str(e)), form=form)
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"), form=form)

    try:
        store = AsetStore(cfg.db_name)
        store.ensure_schema()
        row_id = store.save(result)
    except Exception as e:
        return _render(
            banner=_failed(f"Persistence FAILED: {type(e).__name__}: {e}"), form=form
        )

    try:
        note_path, when = save_card(cfg, result)
    except DailyNoteRefused as e:
        form["orig_timestamp"] = ""
        banner = _failed(
            f"Persisted: aset_sizings id {row_id} ({cfg.db_name}) — but "
            f"daily-note append FAILED: {e}"
        )
        return _render(banner=banner, result=_result_card(result, form), form=form)

    form["orig_timestamp"] = when.isoformat()
    banner = (
        f'<div class="saved">Persisted: aset_sizings id {row_id} ({html.escape(cfg.db_name)}) '
        f"· appended to {html.escape(str(note_path))}</div>"
    )
    return _render(banner=banner, result=_result_card(result, form), form=form)


@app.post("/fill", response_class=HTMLResponse)
async def fill(request: Request) -> str:
    form = {k: str(v) for k, v in (await request.form()).items()}
    try:
        cfg = load_config()
        sheet_modes_cfg = load_sheet_modes_config()
        inp = _parse_input(form, sheet_modes_cfg)
        original = compute_sizing(inp, sheet_modes_cfg.enabled_grades)  # deterministic recompute; no re-persist

        orig_ts_raw = form.get("orig_timestamp", "")
        if not orig_ts_raw:
            raise SizingError(
                "No original card timestamp on this form — compute & persist a "
                "card first, then recompute its actual fill."
            )
        orig_timestamp = datetime.fromisoformat(orig_ts_raw)

        try:
            actual_fill = Decimal(form.get("actual_fill", ""))
        except InvalidOperation as e:
            raise SizingError(f"Invalid actual fill price: {form.get('actual_fill')!r}") from e

        fill_result = compute_fill_recompute(original, actual_fill)
        note_path = save_fill_update(cfg, fill_result, orig_timestamp)
    except (SizingError, ConfigError, DailyNoteRefused) as e:
        return _render(banner=_failed(str(e)), form=form)
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"), form=form)

    banner = f'<div class="saved">Fill update appended to {html.escape(str(note_path))}</div>'
    return _render(
        banner=banner,
        result=_result_card(original, form, fill=fill_result),
        form=form,
    )
