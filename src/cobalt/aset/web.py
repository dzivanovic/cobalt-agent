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
from .engine import SizingError, compute_sizing, daily_stop_from_account
from .models import GRADE_RISK_PCT, Direction, Grade, SizingInput
from .prefill import PrefillError, fetch_last_price
from .store import AsetStore

app = FastAPI(title="Cobalt ASET Sheet", docs_url=None, redoc_url=None)

PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cobalt · ASET Sheet</title>
<style>
 body{{font-family:system-ui,sans-serif;background:#0b1020;color:#eef5ff;margin:0;padding:24px}}
 .wrap{{max-width:640px;margin:0 auto}}
 h1{{font-size:22px;letter-spacing:.06em}}
 .card{{background:#111729;border:1px solid #20283c;border-radius:12px;padding:18px;margin-bottom:16px}}
 label{{display:block;font-size:11px;text-transform:uppercase;color:#9fafca;margin:10px 0 4px}}
 input,select{{width:100%;padding:10px;border-radius:8px;border:1px solid #232d44;background:#0b1020;color:#eef5ff;font-size:15px;box-sizing:border-box}}
 .row{{display:flex;gap:12px}} .row>div{{flex:1}}
 button{{padding:10px 16px;border-radius:8px;border:1px solid #28334d;background:#0b1020;color:#8d9bb6;font-weight:700;cursor:pointer;margin-top:12px}}
 button.primary{{border-color:#00e5ff;color:#00e5ff}}
 .failed{{background:#3a0d18;border:1px solid #ff4f71;color:#ffc3ce;padding:12px;border-radius:8px;margin-bottom:16px;font-weight:700;white-space:pre-wrap}}
 .result{{border-color:#24d986}}
 .shares{{font-size:52px;font-weight:900;color:#24d986}}
 .warn{{color:#ffd84d;font-size:13px}}
 table{{width:100%;font-size:13px;border-collapse:collapse}} td{{padding:4px 8px;border-bottom:1px solid #20283c}}
 .muted{{color:#7f8ca8;font-size:12px}}
</style></head><body><div class="wrap">
<h1>ASET SEMI-AUTO SHEET <span class="muted">pre-beta slice 1 · dev</span></h1>
{banner}
{result}
<form class="card" method="post" action="/size">
 <div class="row"><div>
  <label>Ticker</label><input name="ticker" required value="{ticker}">
 </div><div>
  <label>Last price <span class="muted">(prefill)</span></label>
  <input name="last_price" id="last_price" readonly placeholder="—" value="{last_price}">
  <input type="hidden" name="price_source" id="price_source" value="{price_source}">
 </div></div>
 <button type="button" onclick="prefill()">Fetch last price</button>
 <div class="row"><div>
  <label>Grade (yours, always)</label>
  <select name="grade">{grade_options}</select>
 </div><div>
  <label>Direction</label>
  <select name="direction">{direction_options}</select>
 </div></div>
 <div class="row"><div>
  <label>Entry $</label><input name="entry" type="number" step="0.0001" required value="{entry}">
 </div><div>
  <label>Stop $ (yours, always)</label><input name="stop" type="number" step="0.0001" required value="{stop}">
 </div></div>
 <label>Daily stop $ <span class="muted">(prefilled: account {account} ÷ 50)</span></label>
 <input name="daily_stop" type="number" step="0.01" required value="{daily_stop}">
 <button class="primary" type="submit">Compute &amp; persist</button>
</form>
<div class="muted">Every computed sizing persists to Postgres ({db_name}). Missing data = FAILED, never guessed.</div>
<script>
async function prefill() {{
  const t = document.querySelector('[name=ticker]').value;
  const out = document.getElementById('last_price');
  out.value = '...';
  try {{
    const r = await fetch('/api/prefill?ticker=' + encodeURIComponent(t));
    const j = await r.json();
    if (!r.ok) throw new Error(j.error || r.status);
    out.value = j.price;
    document.getElementById('price_source').value = j.source;
  }} catch (e) {{
    out.value = 'FAILED';
    document.getElementById('price_source').value = '';
    alert('Prefill FAILED: ' + e.message);
  }}
}}
</script>
</div></body></html>"""


def _options(pairs, selected):
    return "".join(
        f'<option value="{html.escape(v)}"{" selected" if v == selected else ""}>'
        f"{html.escape(label)}</option>"
        for v, label in pairs
    )


def _render(
    banner: str = "",
    result: str = "",
    form: dict | None = None,
) -> str:
    cfg = load_config()
    form = form or {}
    daily = form.get("daily_stop") or str(daily_stop_from_account(cfg.account_size))
    grade_pairs = [(g.value, f"{g.value} · {int(pct)}%") for g, pct in
                   [(g, __import__('cobalt.aset.models', fromlist=['GRADE_RISK_PCT']).GRADE_RISK_PCT[g]) for g in Grade]]
    return PAGE.format(
        banner=banner,
        result=result,
        ticker=html.escape(form.get("ticker", "")),
        last_price=html.escape(form.get("last_price", "")),
        price_source=html.escape(form.get("price_source", "")),
        entry=html.escape(form.get("entry", "")),
        stop=html.escape(form.get("stop", "")),
        daily_stop=html.escape(daily),
        account=f"${cfg.account_size:,.0f}",
        db_name=html.escape(cfg.db_name),
        grade_options=_options(grade_pairs, form.get("grade", "A")),
        direction_options=_options(
            [(d.value, d.value.upper()) for d in Direction],
            form.get("direction", "long"),
        ),
    )


def _failed(message: str) -> str:
    return f'<div class="failed">FAILED\n{html.escape(message)}</div>'


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    try:
        return _render()
    except ConfigError as e:
        raise  # config errors crash loudly — uvicorn shows the traceback


@app.get("/api/prefill")
async def api_prefill(ticker: str):
    try:
        price, source = await fetch_last_price(ticker)
    except PrefillError as e:
        return JSONResponse({"error": str(e)}, status_code=502)
    return {"ticker": ticker.strip().upper(), "price": str(price), "source": source}


@app.post("/size", response_class=HTMLResponse)
async def size(request: Request) -> str:
    form_data = dict(await request.form())
    form = {k: str(v) for k, v in form_data.items()}
    try:
        cfg = load_config()
        inp = SizingInput(
            ticker=form.get("ticker", ""),
            grade=form.get("grade", ""),
            direction=form.get("direction", ""),
            daily_stop=form.get("daily_stop", "0"),
            entry=form.get("entry", "0"),
            stop=form.get("stop", "0"),
            last_price=form.get("last_price") or None,
            price_source=form.get("price_source") or None,
        )
        result = compute_sizing(inp)
        store = AsetStore(cfg.db_name)
        store.ensure_schema()
        row_id = store.save(result)
    except (SizingError, ConfigError) as e:
        return _render(banner=_failed(str(e)), form=form)
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"), form=form)

    warnings_html = "".join(
        f'<div class="warn">⚠ {html.escape(w)}</div>' for w in result.warnings
    )
    result_html = f"""<div class="card result">
      <div class="shares">{result.shares:,} <span style="font-size:18px">shares</span></div>
      <table>
       <tr><td>Ticker / grade / direction</td><td>{html.escape(inp.ticker)} · {inp.grade.value} ({result.risk_pct}%) · {inp.direction.value.upper()}</td></tr>
       <tr><td>Risk budget</td><td>${result.risk_budget}</td></tr>
       <tr><td>Risk / share</td><td>${result.per_share_risk}</td></tr>
       <tr><td>Total used risk</td><td>${result.used_risk}</td></tr>
       <tr><td>Target 1R / 2R</td><td>${result.target_1r} / ${result.target_2r}</td></tr>
       <tr><td>Persisted</td><td>aset_sizings id {row_id} ({html.escape(cfg.db_name)})</td></tr>
      </table>
      {warnings_html}
    </div>"""
    return _render(result=result_html, form=form)
