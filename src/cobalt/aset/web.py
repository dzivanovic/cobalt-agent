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
from loguru import logger
from fastapi.responses import HTMLResponse, JSONResponse

from cobalt.prefill.config import PrefillConfigError, load_prefill_paths
from cobalt.prefill.trade_note import upsert_trade_note
from cobalt.prefill.vault_writer import VaultWriteError
from cobalt import env
from cobalt.session import SessionBlocked, assert_writable
from cobalt.session.clock import now_utc, session_clock
from cobalt.cards import (
    ALLOWED,
    FILL_TARGET,
    STOP_EDITABLE,
    Actor,
    CardState,
    CardStateError,
    CardStore,
    IllegalTransition,
    Origin,
    fill_path,
)
from cobalt.daymode import (
    DayModeStore,
    SheetMismatch,
    assert_grade_allowed,
    assert_sheet_matches,
    decided_or_stage1,
    load_daymode_config,
    stage2_open,
)
from cobalt.daymode import note as daymode_note
from cobalt.vault import VaultConfigError, dev_entry_allowed, is_production, resolve_vault_path

from .config import ConfigError, load_config, load_sheet_modes_config
from .daily_note import DailyNoteRefused, save_card, save_fill_update
from .engine import KeyRefused, SizingError, compute_sizing, size_at_key
from .models import Direction, Grade, SizingInput
from cobalt.settings import TraderSettingsError
from cobalt.settings.card import CardSettingsReader
from cobalt.settings.fills import DRIFT_NOT_EVALUATED
from .prefill import PrefillError, fetch_last_price
from .radar_panel import (
    RadarPanelError,
    build_radar_panel,
    parse_since,
    pool_api_payload,
    render_failed_page,
    render_radar_page,
)
from .store import AsetStore
from .account_mode import AccountModeUnresolved, resolve as resolve_account_mode
from .card_stop import set_card_stop
from cobalt.voice import web as voice_web

app = FastAPI(title="Cobalt ASET Sheet", docs_url=None, redoc_url=None)

# Voice V1 (voice v3 FINAL §9): the `/voice/*` routes, and — before the
# first request — the scratch-dir lock + side-B start sweep; a lock held by
# another process fails this start loud (X-X22's guard).
app.include_router(voice_web.router)
app.add_event_handler("startup", voice_web.voice_startup)
app.add_event_handler("shutdown", voice_web.voice_shutdown)


class DevEntryRefused(RuntimeError):
    """Non-production instance, no explicit COBALT_ALLOW_DEV_ENTRY=1 opt-in —
    refuse ticker fetch / sizing / fill so a stale dev tab can't take live
    entries (2026-09-02 incident follow-up). Mirrors cobalt.vault's inverse
    guard but at the request layer, since a dev instance whose vault
    resolves safely to ~/dev-vault-cobalt would otherwise sail through
    resolve_vault_path() with no refusal at all."""


def _check_entry_allowed() -> None:
    if not is_production() and not dev_entry_allowed():
        raise DevEntryRefused(
            "Refused: this is a DEV instance (no COBALT_ENV=production). "
            "Set COBALT_ALLOW_DEV_ENTRY=1 on this process to allow ticker "
            "fetch / sizing / fill here — otherwise use the production sheet."
        )

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
 .vaultline{color:#7f8ca8;font-size:12px;margin-bottom:10px}
 .vaultline.bad{background:#3a0d18;border:1px solid #ff4f71;color:#ffc3ce;padding:8px 12px;border-radius:8px;font-weight:700}
 .envbanner{background:#3a0d18;border:1px solid #ff4f71;color:#ffc3ce;padding:8px 12px;border-radius:8px;font-weight:700;margin-bottom:10px}
 .saved{background:#0d2a1c;border:1px solid #24d986;color:#b8f5d9;padding:12px;border-radius:8px;margin-bottom:16px;font-weight:700}
 .result{border-color:#24d986}
 .shares{font-size:52px;font-weight:900;color:#24d986}
 .warn{color:#ffd84d;font-size:13px;margin-top:6px}
 .hint{color:#7f8ca8;font-size:12px;margin-top:4px;font-style:italic}
 table{width:100%;font-size:13px;border-collapse:collapse} td{padding:4px 8px;border-bottom:1px solid #20283c}
 .muted{color:#7f8ca8;font-size:12px}
 option:disabled{color:#55607a}
 .mode{background:#0d1b2e;border:1px solid #1d3557;border-radius:8px;padding:10px 12px;margin-bottom:12px;font-size:13px}
 .mode b{color:#00e5ff;letter-spacing:.04em}
 .mode .why{color:#7f8ca8;font-size:12px;margin-top:6px;line-height:1.45}
 .mode.mismatch{background:#3a0d18;border-color:#ff4f71;color:#ffc3ce}
 .attest{display:flex;gap:8px;align-items:center;margin-top:8px}
 .attest select{flex:1}
 .attest button{margin-top:0;white-space:nowrap}
 .cards{margin-top:4px}
 .crow{border:1px solid #20283c;border-radius:10px;padding:10px 12px;margin-bottom:10px;background:#0e1526}
 .crow .top{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap}
 .crow .tk{font-weight:900;font-size:16px}
 .st{font-size:11px;font-weight:800;letter-spacing:.08em;padding:2px 8px;border-radius:99px;border:1px solid}
 .st-WATCH{color:#8d9bb6;border-color:#28334d}
 .st-ARMED{color:#00e5ff;border-color:#00e5ff}
 .st-TRIGGERED{color:#ffd84d;border-color:#ffd84d}
 .st-FILLED{color:#24d986;border-color:#24d986}
 .acts{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
 .acts button{margin-top:0;padding:6px 10px;font-size:12px}
 .acts button.danger{border-color:#ff4f71;color:#ff8ea4}
 .stopedit{display:flex;gap:6px;align-items:center;margin-top:8px}
 .stopedit input{padding:6px 8px;font-size:13px;max-width:130px}
 .stopedit button{margin-top:0;padding:6px 10px;font-size:12px}
 .yours{font-size:10px;font-weight:800;letter-spacing:.06em;color:#ffd84d;border:1px solid #ffd84d;border-radius:99px;padding:1px 7px}
 .locked{color:#55607a;font-size:11px;font-style:italic}
"""

JS = """
 const MODE_DOLLARS = window.SHEET_MODE_DOLLARS;
 const $ = id => document.getElementById(id);

 // F7: MISSED and DISARM carry a reason or they do not happen
 // (cards/store.py _assert_reason). Prompt here so he types it once,
 // rather than posting an empty field and reading a refusal.
 function askReason(btn, label){
   const why = window.prompt(label + ' — reason (required):', '');
   if (why === null || !why.trim()) return false;
   btn.form.reason.value = why.trim();
   return true;
 }

 // STATE PRINCIPLE (Defect 3, 2026-09-01): the ticker box going out of
 // focus is "new card" intent, full stop — whether or not the ticker
 // text actually changed. A second trade on the SAME ticker is still a
 // new decision: card 1's grade/direction/entry/stop/fill-block/
 // warnings must never leak into it (the old logic only reset on a
 // ticker CHANGE, so a same-ticker second card kept showing card 1's
 // values until Compute was hit again — the entryDirty flag it used to
 // decide "reset or preserve" conflated two different user intents
 // into one handler). Two distinct, unconditional handlers instead of
 // one handler with a flag:
 //   - onTickerBlur     -> ALWAYS full reset, then fetch + prefill entry.
 //   - refetchLastPrice -> refreshes ONLY last_price + entry; every
 //                         other field (stop, grade, direction, fill
 //                         block) is preserved exactly.
 // Sheet mode (FULL/HALF) is the one field that survives a reset — a
 // day setting, not a card setting.
 //
 // Slice 2.1a (2026-08-31 defect D1): typing a new ticker and hitting
 // Enter submits the form immediately, with no blur ever firing, so
 // entry/stop carried over from the PREVIOUS ticker verbatim. The
 // 'input' listener below clears fields the instant the box diverges
 // from currentTicker, before Enter can fire; entry_ticker, a hidden
 // field naming which ticker the entry/stop values actually belong to,
 // is submitted with the form so the server can refuse a mismatch
 // outright — belt and suspenders, since client JS is never the only
 // guard against a stale card.
 let currentTicker = window.INITIAL_TICKER || null;

 function setDir(d){
   $('direction').value = d;
   $('longBtn').classList.toggle('active-long', d === 'long');
   $('shortBtn').classList.toggle('active-short', d === 'short');
 }

 // F6 (S1-P2): the sheet mode is no longer a toggle. It is set by the
 // day mode in force and rendered read-only, so this only refreshes the
 // dollar hint — the two FULL/HALF buttons it used to light up are gone
 // (a card sized off a mode he picked freely is the mismatch the match
 // check exists to refuse).
 function setMode(m){
   if (m) $('sheet_mode').value = m;
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

 function clearForNewCard(){
   $('grade').value = 'B';
   setDir('long');
   $('orig_timestamp').value = '';
   $('entry_ticker').value = '';
   $('resultCard').innerHTML = '';
   $('banner').innerHTML = '';
   $('entry').value = '';
   $('stop').value = '';
   $('last_price').value = '';
   $('price_source').value = '';
   updateModeHint();
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

 // TAB-OUT of the ticker field: unconditional "new card" reset (Defect
 // 3) — never gated on whether the ticker text actually changed.
 async function onTickerBlur(rawTicker){
   const t = rawTicker.trim().toUpperCase();
   if (!t) return;
   currentTicker = t;
   clearForNewCard();
   $('entry_ticker').value = t;
   const price = await doFetch(t);
   if (price !== null) {
     $('last_price').value = price;
     $('entry').value = price;
   }
 }

 // RE-FETCH LAST PRICE button: refreshes ONLY last_price + entry.
 // grade/direction/stop/fill block are left exactly as they are.
 async function refetchLastPrice(rawTicker){
   const t = rawTicker.trim().toUpperCase();
   if (!t) return;
   $('entry_ticker').value = t;  // reaffirm — fields still belong to this ticker
   const price = await doFetch(t);
   if (price === null) return;
   $('last_price').value = price;
   $('entry').value = price;
 }

 window.addEventListener('DOMContentLoaded', () => {
   setDir($('direction').value || 'long');
   setMode($('sheet_mode').value);
   $('ticker').addEventListener('blur', () => onTickerBlur($('ticker').value));
   // Fires on every keystroke, ahead of blur — closes the Enter-to-submit
   // gap where blur (and clearForNewCard) never runs at all (D1).
   $('ticker').addEventListener('input', () => {
     const t = $('ticker').value.trim().toUpperCase();
     if (t !== currentTicker) clearForNewCard();
   });
   $('fetchBtn').addEventListener('click', () => refetchLastPrice($('ticker').value));
   $('grade').addEventListener('change', updateModeHint);
 });
"""

FORM_FIELDS = (
    "ticker", "grade", "direction", "sheet_mode", "entry", "stop",
    "last_price", "price_source", "orig_timestamp",
    "entry_ticker",
    # 2026-09-03 (L28 step 3): the aset_sizings row this card created.
    # /fill UPDATEs exactly that row (status FILLED + actual-fill
    # figures) instead of matching by nearest timestamp — the fill
    # recompute used to persist nothing at all.
    "card_row_id",
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

    # Defect 1 (2026-09-01): the sheet gave no visible indication it was
    # writing to the wrong vault for 6+ hours — this line makes the
    # resolved root always visible, not just discoverable after a write
    # already went to the wrong place. See src/cobalt/vault.py.
    try:
        vault_line = f'<div class="vaultline">Vault: {e(str(resolve_vault_path()))}</div>'
    except VaultConfigError as exc:
        vault_line = f'<div class="vaultline bad">⚠ VAULT UNRESOLVED — writes will fail: {e(str(exc))}</div>'

    # 2026-09-02 incident follow-up: the header used to say "· dev" as a
    # static literal regardless of which instance was actually running —
    # the real production process (Think vault, COBALT_ENV=production)
    # printed that same "dev" label, which is exactly what made a live
    # TSLA card look like it came from a throwaway dev tab. This is now
    # the actual runtime environment, and a non-production instance gets
    # a loud red banner in addition (see DevEntryRefused).
    env_label = "PRODUCTION" if is_production() else "DEV"
    env_banner = (
        ""
        if is_production()
        else '<div class="envbanner">⚠ DEV INSTANCE — not production. Ticker fetch / '
        "sizing / fill are refused here unless COBALT_ALLOW_DEV_ENTRY=1 is set on this "
        "process.</div>"
    )

    initial_ticker = form.get("ticker", "").strip().upper()
    # Every declared sheet, not a hardcoded pair (F6: sheets are an
    # ordered config list — adding a quarter sheet adds a row here too).
    mode_dollars = {
        sheet: {g.value: float(sheet_modes_cfg.dollars_for(sheet, g)) for g in Grade}
        for sheet in sheet_modes_cfg.order
    }

    # F6: the sheet mode is no longer a free toggle. The day mode in
    # force decides which key table sizes the card ("risk set everywhere
    # except the .htk"), and the .htk he attested has to agree with it.
    dm = _daymode_state()
    daymode_html = _daymode_banner(dm)
    sheet_mode = dm["cfg"].sheet_for(dm["mode"]) if dm["cfg"] else sheet_mode
    open_cards_html = _open_cards_section()
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cobalt · ASET Sheet</title>
<style>{CSS}</style></head><body><div class="wrap">
<h1>ASET SEMI-AUTO SHEET <span class="muted">pre-beta slice 1 · {e(env_label)}</span> · <a href="/radar">Trade Radar</a></h1>
{env_banner}
{vault_line}
{daymode_html}
<div id="banner">{banner}</div>
<div id="resultCard">{result}</div>
{open_cards_html}
<form class="card" method="post" action="/size">
 <div class="row"><div>
  <label>Ticker <span class="muted">(tab out to fetch)</span></label>
  <input name="ticker" id="ticker" required autocomplete="off" value="{e(form.get("ticker", ""))}">
 </div><div>
  <label>Last price <span class="muted">(prefill)</span></label>
  <input name="last_price" id="last_price" readonly placeholder="—" value="{e(form.get("last_price", ""))}">
  <input type="hidden" name="price_source" id="price_source" value="{e(form.get("price_source", ""))}">
  <input type="hidden" name="orig_timestamp" id="orig_timestamp" value="{e(form.get("orig_timestamp", ""))}">
  <input type="hidden" name="entry_ticker" id="entry_ticker" value="{e(form.get("entry_ticker", ""))}">
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
 </div><div>
  <label>Stop $ (yours, always)</label>
  <input name="stop" id="stop" type="number" step="0.0001" required value="{e(form.get("stop", ""))}">
 </div></div>
 <label>Sheet mode <span class="muted">(set by the day mode — not a free choice)</span></label>
 <div class="hint" id="modeLine">{e(sheet_mode.upper())} sheet, from day mode {e(str(dm["mode"] or "UNRESOLVED")).upper()}. Change it by deciding or overruling the day mode above, never here.</div>
 <input type="hidden" name="sheet_mode" id="sheet_mode" value="{e(sheet_mode)}">
 <button class="primary" type="submit">Compute &amp; persist</button>
</form>
<div class="muted">Every computed sizing persists to Postgres ({e(env.resolve_db_name())} — chosen by COBALT_ENV alone, RULING 7: production writes cobalt_brain, dev writes cobalt_dev) and appends to today's daily note in the same action. Missing data = FAILED, never guessed.</div>
<script>
window.SHEET_MODE_DOLLARS = {json.dumps(mode_dollars)};
window.INITIAL_TICKER = {json.dumps(initial_ticker)};
</script>
<script>{JS}</script>
</div>{voice_web.widget_html()}</body></html>"""



# ---------------------------------------------------------------------------
# F6 day-mode banner + attestation, F7 card controls (S1-P2)
# ---------------------------------------------------------------------------


def _today_et():
    return session_clock().to_et(now_utc()).date()


def _stage_label(row: dict | None, now=None) -> str:
    """Which stage the banner reports.

    Must come from the SAME rule as the mode (`decided_or_stage1`), or
    the banner can read "stage 2 (decided)" while showing the stage-1
    floor — exactly what happens before 09:00 on a day whose proposal was
    answered. Stage 2 is in force only once the `daymode.stage2_open`
    boundary has passed AND he has answered.
    """
    in_stage2 = session_clock().to_et(now or now_utc()).time() >= stage2_open()
    if not in_stage2:
        return "stage 1 (system rule, pre-09:00)"
    if row and row.get("decided"):
        return "stage 2 (decided)"
    return "stage 2 (proposed, undecided — floor holds)"


def _read_back_note_attestation(cfg, day, row: dict | None, store) -> dict | None:
    """THE NOTE -> COBALT half of the two-way sheet-mode line (S1-P3).

    A box he ticked in today's daily note IS an attestation, read at
    every sheet request. If nothing is on record yet, the tick becomes
    the record (persisted through the same `attest_sheet` the selector
    calls — one write path). If both exist and disagree, `reconcile`
    raises and the caller refuses with both shown.

    A missing note, or a note with no day-mode unit, contributes nothing
    and is not an error: the 05:15 prefill may simply not have run yet.
    """
    path = daymode_note.daily_note_path(day)
    if not path.exists():
        return row
    note = daymode_note.read_attestation(path.read_text(encoding="utf-8"), cfg)
    if not note.ticked:
        return row
    settled = daymode_note.reconcile(note, (row or {}).get("attested_sheet"))
    if settled and settled != (row or {}).get("attested_sheet"):
        store.attest_sheet(day, filename=settled)
        logger.info(
            "daymode: attestation {} read back from the daily note {}", settled, path
        )
        return store.for_date(day)
    return row


def _daymode_state() -> dict:
    """Everything the sheet needs about the day mode, resolved once.

    Never raises: a config or database failure renders as a LOUD banner
    rather than a 500, because a sheet that will not paint is a sheet he
    cannot trade beside. `error` being set is itself the refusal — every
    card write re-checks through `assert_sheet_matches`, so a degraded
    banner can never let a card through. A note/selector CONFLICT lands
    in the same `error` for the same reason.
    """
    try:
        cfg = load_daymode_config()
        day = _today_et()
        store = DayModeStore()
        store.ensure_schema()
        row = store.for_date(day)
        row = _read_back_note_attestation(cfg, day, row, store)
        mode = decided_or_stage1(row, cfg)
        account_error = None
        try:
            with store._connect() as conn:
                account_mode = resolve_account_mode(conn, day)
        except AccountModeUnresolved as e:
            account_mode = None
            account_error = str(e)
        return {
            "cfg": cfg, "day": day, "row": row, "mode": mode, "error": None,
            "stage": _stage_label(row), "account_mode": account_mode,
            "account_error": account_error,
        }
    except daymode_note.NoteAttestationConflict as e:
        logger.error("daymode: note/selector attestation conflict: {}", e)
        return {"cfg": None, "day": None, "row": None, "mode": None,
                "stage": "CONFLICT", "error": str(e), "account_mode": None,
                "account_error": None}
    except Exception as e:  # noqa: BLE001 - rendered, never swallowed
        return {"cfg": None, "day": None, "row": None, "mode": None,
                "stage": "UNRESOLVED", "error": f"{type(e).__name__}: {e}",
                "account_mode": None, "account_error": None}


def _write_daymode_note(cfg, day, store) -> str:
    """COBALT -> NOTE half of the two-way line (S1-P3). Returns a short
    status suffix for the banner; never raises — an attestation that
    reached Postgres is recorded whether or not the note write lands, and
    a failed note write is LOUD in the log and on the page rather than a
    reason to lose the attestation."""
    try:
        row = store.for_date(day)
        result = daymode_note.write(
            daymode_note.daily_note_path(day),
            cfg,
            decided_or_stage1(row, cfg),
            stage=_stage_label(row),
            attested=(row or {}).get("attested_sheet"),
            row=row,
        )
        if result is None:
            return " ⚠ today's daily note does not exist yet — nothing written to it."
        return f" Daily note: {result.action} (write_id {result.write_id})."
    except Exception as e:  # noqa: BLE001
        logger.error("daymode note write FAILED (attestation stands): {}", e)
        return f" ⚠ daily-note write FAILED: {type(e).__name__}: {e}"


def _daymode_banner(dm: dict) -> str:
    e = html.escape
    if dm["error"]:
        return (f'<div class="mode mismatch">⚠ DAY MODE UNRESOLVED — cards are refused '
                f'until this is fixed: {e(dm["error"])}</div>')

    cfg, row, mode = dm["cfg"], dm["row"], dm["mode"]
    sheet = cfg.sheet_for(mode)
    keys = ", ".join(g.value for g in cfg.enabled_grades_for(mode))
    attested = (row or {}).get("attested_sheet")

    # The match check, rendered. Same call the write path makes — the
    # banner cannot say "matched" while the write path refuses.
    try:
        assert_sheet_matches(row, mode, cfg=cfg)
        match_html = f'<span style="color:#24d986">✓ {e(attested)} matches</span>'
        klass = "mode"
    except SheetMismatch as mismatch:
        match_html = f'<b style="color:#ff8ea4">⚠ {e(str(mismatch))}</b>'
        klass = "mode mismatch"

    reason = (row or {}).get("reason") or ""
    proposed = (row or {}).get("proposed")
    decided = (row or {}).get("decided")
    lines = [
        (
            f'<div><b>ACCOUNT {e(dm["account_mode"].upper())}</b></div>'
            if dm.get("account_mode")
            else f'<div><b>ACCOUNT MODE UNRESOLVED</b> — cards are refused: {e(dm.get("account_error") or "missing")}</div>'
        ),
        f'<div><b>DAY MODE {e(mode.upper())}</b> · {e(dm["stage"])} · sizes from the '
        f'{e(sheet.upper())} sheet · keys {e(keys)}</div>',
        f'<div style="margin-top:6px">.htk: {match_html} '
        f'<span class="muted">(attested, not read — Cobalt never touches DAS)</span></div>',
    ]
    if proposed and not decided:
        lines.append(f'<div class="why">09:00 proposal: <b>{e(proposed)}</b> — undecided, '
                     f'so stage 1 stays in force. {e(reason)}</div>')
    elif decided:
        lines.append(f'<div class="why">proposed {e(proposed or "-")} → decided '
                     f'{e(decided)} by {e((row or {}).get("decided_by") or "-")}'
                     + (f' · overrule: {e(row["overrule_reason"])}' if (row or {}).get("overrule_reason") else "")
                     + f'<br>{e(reason)}</div>')
    else:
        lines.append('<div class="why">No 09:00 proposal yet — stage 1 system rule: the '
                     f'lowest enabled rung ({e(cfg.lowest_enabled)}).</div>')

    options = "".join(
        f'<option value="{e(f)}"{" selected" if f == attested else ""}>{e(f)}</option>'
        for f in cfg.hotkey_file_names
    )
    lines.append(
        '<form class="attest" method="post" action="/attest">'
        f'<select name="file"><option value="">— which .htk have you loaded? —</option>{options}</select>'
        '<select name="account_mode">'
        f'<option value="live"{" selected" if dm.get("account_mode") == "live" else ""}>LIVE</option>'
        f'<option value="sim"{" selected" if dm.get("account_mode") == "sim" else ""}>SIM</option>'
        '</select>'
        '<button type="submit">Attest</button></form>'
    )
    return f'<div class="{klass}">' + "".join(lines) + "</div>"


def _card_controls(card: dict) -> str:
    """The action row for ONE card, derived from the edge table.

    Every button is a legal edge out of the card's CURRENT state, read
    from `cards.ALLOWED`. Nothing is listed that the store would refuse,
    and nothing legal is missing — adding an edge to the table adds its
    button here with no edit.
    """
    e = html.escape
    state = CardState(card["state"])
    cid = card["id"]
    # A label for EVERY state, keyed off the enum rather than off the
    # edges that happen to exist today: a missing entry would be a
    # KeyError at render time on whichever card first reached that
    # state, i.e. a blank sheet mid-morning rather than a caught bug.
    # `.get` is not used for the same reason — a state with no label is
    # a mistake to fix, not a button to draw with a fallback name.
    labels = {
        CardState.ARMED: "ARM", CardState.WATCH: "DISARM", CardState.TRIGGERED: "TRIGGERED",
        CardState.FILLED: "FILLED", CardState.CLOSED: "CLOSE", CardState.PASSED: "PASS",
        CardState.EXPIRED: "EXPIRE", CardState.MISSED: "MISSED",
    }
    missing = [s.value for s in CardState if s not in labels]
    if missing:  # pragma: no cover - guarded by test_every_state_has_a_button_label
        raise RuntimeError(f"no sheet button label for card state(s): {missing}")
    danger = {CardState.PASSED, CardState.EXPIRED, CardState.MISSED, CardState.WATCH}
    # MISSED and DISARM require a reason — the button prompts for one
    # rather than posting an empty field the store would refuse.
    def _needs_reason(target: CardState) -> bool:
        """The two edges the store refuses without one (store._assert_reason).
        Rendered from the same rule so the button prompts instead of the
        server rejecting."""
        return target is CardState.MISSED or (
            state is CardState.ARMED and target is CardState.WATCH
        )

    # F7 ONE-CLICK FILL (S1-P3). A manual card more than one edge away
    # from FILLED gets a single button that walks the rest of the route
    # itself; a radar card never does. The button is only drawn when the
    # store would actually accept it, so the sheet and the store agree
    # about what is possible — same rule as every other button here.
    origin = Origin(card.get("origin", Origin.MANUAL.value))
    route = fill_path(state)
    shortcut = ""
    if origin is Origin.MANUAL and len(route) > 1:
        hops = " → ".join(s.value for s in route[:-1])
        shortcut = (
            f'<form method="post" action="/card/{cid}/move" style="display:inline">'
            f'<input type="hidden" name="to" value="{FILL_TARGET.value}">'
            f'<input type="hidden" name="reason" value="">'
            f'<button type="submit" title="Cobalt writes the missing {e(hops)} '
            f'row(s) itself, actor cobalt">FILLED (1-click)</button></form>'
        )

    buttons = []
    for target in sorted(ALLOWED[state], key=lambda x: x.value):
        cls = ' class="danger"' if target in danger else ""
        onclick = (
            f" onclick=\"return askReason(this,'{e(labels[target])}')\""
            if _needs_reason(target)
            else ""
        )
        buttons.append(
            f'<form method="post" action="/card/{cid}/move" style="display:inline">'
            f'<input type="hidden" name="to" value="{target.value}">'
            f'<input type="hidden" name="reason" value="">'
            f'<button type="submit"{cls}{onclick}>{e(labels[target])}</button></form>'
        )

    # Decision 11: stop editable in WATCH and FILLED, key frozen from
    # ARMED onward. Both halves are rendered, so the lock is visible
    # rather than merely enforced.
    if state in STOP_EDITABLE:
        stop_html = (
            f'<form class="stopedit" method="post" action="/card/{cid}/stop">'
            f'<span class="muted">stop</span>'
            f'<input name="stop" type="number" step="0.0001" value="{e(str(card["stop"]))}">'
            f'<button type="submit">commit</button>'
            f'<span class="yours">YOURS</span>'
            f'<span class="muted">↺ reset = re-enter the card stop</span></form>'
        )
    else:
        stop_html = (
            f'<div class="stopedit"><span class="muted">stop</span> '
            f'<b>{e(str(card["stop"]))}</b> '
            f'<span class="locked">🔒 locked in {e(state.value)} — the key is a risk '
            f'commitment (decision 11)</span></div>'
        )

    key_lock = (
        '<span class="locked">🔒 key frozen from ARMED onward</span>'
        if state is not CardState.WATCH else ""
    )
    return (
        f'<div class="crow"><div class="top">'
        f'<span class="tk">{e(card["ticker"])}</span>'
        f'<span class="st st-{state.value}">{state.value}</span>'
        f'<span class="muted">#{cid} · {e(str(card["grade"]))} · {e(str(card["direction"]))} · '
        f'{e(str(card["shares"]))} sh · {e(str(card["session"]))} · ACCOUNT '
        f'{e(str(card.get("account_mode") or "UNSTAMPED").upper())}</span>{key_lock}</div>'
        f'{stop_html}<div class="acts">{"".join(buttons)}{shortcut}</div></div>'
    )


def _open_cards_section() -> str:
    try:
        store = CardStore()
        store.ensure_schema()
        cards = store.open_cards()
    except Exception as e:  # noqa: BLE001
        return (f'<div class="card"><div class="failed">FAILED\nOpen cards unreadable: '
                f'{html.escape(f"{type(e).__name__}: {e}")}</div></div>')
    # S3 C3 fix r1 F3: below the live cards, today's CLOSED manual cards'
    # estimated legs, listed for correction — even when no card is live.
    closed = _sheet_closed_estimated(store)
    if closed:
        closed = (f'<label>Closed manual cards — estimated legs to confirm</label>'
                  f'<div class="cards">{closed}</div>')
    if not cards:
        return ('<div class="card"><label>Open cards (F7)</label>'
                '<div class="muted">No card is in a live state. Terminal cards '
                f'(CLOSED / PASSED / EXPIRED / MISSED) are not listed.</div>{closed}</div>')
    # S3 C3-4: a FILLED manual card's IN-TRADE controls follow its row.
    rows = "".join(_card_controls(c) + _sheet_in_trade(c) for c in cards)
    return (f'<div class="card"><label>Open cards (F7) — every button writes a '
            f'transition</label><div class="cards">{rows}</div>{closed}</div>')

def _failed(message: str) -> str:
    return f'<div class="failed">FAILED\n{html.escape(message)}</div>'


def _pick_banner(card_id: int, filled) -> str:
    """S2-P4 R2: the red "pick not recorded" banner, APPENDED after a fill's
    success banner — the fill committed; only the F3 pick row is missing.
    Empty when the pick was recorded."""
    if filled.pick_recorded:
        return ""
    return _failed(
        f"card {card_id}: pick not recorded ({filled.pick_error}). The fill stands; "
        "`cobalt cards picks` reports this card MISSING."
    )


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
    ticker_norm = form.get("ticker", "").strip().upper()
    entry_ticker = (form.get("entry_ticker") or "").strip().upper()

    # Slice 2.1a (2026-08-31 defect D1): entry_ticker is the JS-tracked
    # "these entry/stop values belong to THIS ticker" marker. A mismatch
    # means the ticker field changed without the entry/stop fields
    # clearing (e.g. typed a new ticker then hit Enter, which submits
    # before the JS blur handler ever runs) — refuse outright rather
    # than compute against a stale, wrong-symbol price.
    if entry_ticker != ticker_norm:
        raise SizingError(
            f"Ticker changed to {ticker_norm or '(blank)'} but entry/stop still "
            f"belong to {entry_ticker or '(none)'} — stale carry-over. Re-enter "
            "entry and stop for the new ticker."
        )

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
       <tr><td>Account</td><td>{html.escape(form.get("account_mode", "STAMPED ON SAVE").upper())}</td></tr>
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
     <label>Shares filled <span class="muted">(what the broker filled — the entry leg)</span></label>
     <input name="fill_shares" type="number" step="1" min="1" required value="{html.escape(form.get("fill_shares", ""))}">
     <button type="submit">Recompute at actual fill</button>
    </form>"""


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return _render()


@app.get("/radar", response_class=HTMLResponse)
def radar(frame: str | None = None) -> str:
    """Read-only radar surface; deliberately bypasses every sheet helper."""
    phone_frame = frame == "phone"
    try:
        view = build_radar_panel(since=None, snapshot=True)
        page = render_radar_page(view, phone_frame=phone_frame)
    except Exception as exc:
        message = str(exc) if isinstance(exc, RadarPanelError) else f"{type(exc).__name__}: {exc}"
        logger.error("radar panel FAILED: {}", message)
        page = render_failed_page(message, phone_frame=phone_frame)
    # Voice V1: the same widget partial the sheet carries (no sheet helper runs).
    return page.replace("</body>", voice_web.widget_html() + "</body>", 1)


@app.get("/api/radar/pool")
def api_radar_pool(since: str | None = None):
    """Refresh the pool from the same builder used by the initial page."""
    instant = now_utc()
    try:
        cursor = parse_since(since or "", now=instant)
    except RadarPanelError as exc:
        return JSONResponse(status_code=422, content={"status": "FAILED", "error": str(exc)})
    try:
        view = build_radar_panel(since=cursor, snapshot=False, now=instant)
        return pool_api_payload(view.pool)
    except Exception as exc:
        message = str(exc) if isinstance(exc, RadarPanelError) else f"{type(exc).__name__}: {exc}"
        logger.error("radar pool refresh FAILED: {}", message)
        return JSONResponse(status_code=503, content={"status": "FAILED", "error": message})


@app.get("/api/health")
def api_health():
    """What the DAY-MODE BANNER says, as JSON — for the F18 probe.

    WHY THIS EXISTS. `sheet_http` asks whether the page answers 200, and
    on 2026-09-09 the page answered 200 for about thirteen hours while
    carrying "⚠ DAY MODE UNRESOLVED — cards are refused until this is
    fixed". Every card write was being refused and the heartbeat was
    green: `_daymode_state()` was raising `TaxonomyConfigError` because
    the 09-08 seat-usage deploy added a `TunableUnit.WINDOW` row and the
    sheet process — started before that code existed — re-reads
    `tunables.yaml` on every request. The page he trades beside had
    stopped working and nothing said so.

    So the probe reads the banner rather than the status line, and this
    is the banner's own state, from the SAME `_daymode_state()` call the
    page renders from. One resolver, two renderings: this endpoint
    cannot say green while the page shows the refusal.

    NO DB WRITE AND NO LLM. `_daymode_state()` reads the day-mode row and
    calls `ensure_schema()` (idempotent `CREATE TABLE IF NOT EXISTS` —
    the same call the page render already makes); it inserts nothing,
    decides nothing and reaches no model. It also NEVER RAISES: a config
    or database failure is the thing this endpoint exists to report, so
    it comes back as `ok: false` with the reason rather than as a 500 a
    probe would have to interpret.
    """
    dm = _daymode_state()
    mode = dm["mode"]
    cfg = dm["cfg"]
    return {
        # False iff the banner is a refusal: an error was caught, or
        # there is no mode — which is the same thing to a trader, since
        # `assert_sheet_matches` refuses every card either way.
        "ok": not dm["error"] and not dm.get("account_error") and mode is not None,
        "day": str(dm["day"]) if dm["day"] else None,
        "mode": mode,
        "stage": dm["stage"],
        # The sheet the sizes come from: derived, not stored, and only
        # answerable once the mode resolved.
        "sheet_mode": cfg.sheet_for(mode) if (cfg and mode) else None,
        "error": dm["error"] or dm.get("account_error"),
        "account_mode": dm.get("account_mode"),
    }


@app.get("/api/prefill")
async def api_prefill(ticker: str):
    try:
        _check_entry_allowed()
        price, source = await fetch_last_price(ticker)
    except DevEntryRefused as e:
        return JSONResponse({"error": str(e)}, status_code=403)
    except PrefillError as e:
        return JSONResponse({"error": str(e)}, status_code=502)
    return {"ticker": ticker.strip().upper(), "price": str(price), "source": source}


@app.post("/size", response_class=HTMLResponse)
async def size(request: Request) -> str:
    form = {k: str(v) for k, v in (await request.form()).items()}
    try:
        _check_entry_allowed()
        # F1 market_reset hard block (Charter §3 F1): no card is created
        # in the 20:00-21:00 ET window. Checked BEFORE the sizing math so
        # the refusal is the only thing that happens — a card refused
        # here leaves no aset_sizings row and no note write to unwind.
        assert_writable("aset.card", target=form.get("ticker") or None)

        # F6, part 1: the day mode decides which key table sizes this
        # card ("risk set everywhere except the .htk"). It is resolved
        # BEFORE parsing because the parse needs the sheet — but the
        # REFUSALS wait until after the card has been validated and
        # priced, so a typo'd stop still reports as a typo'd stop rather
        # than hiding behind a hotkey-file complaint.
        dm = _daymode_state()
        if dm["error"]:
            raise SheetMismatch(
                f"Day mode unresolved — no card can be written: {dm['error']}",
                attested=None, mode="(unresolved)",
            )
        form["sheet_mode"] = dm["cfg"].sheet_for(dm["mode"])

        cfg = load_config()
        sheet_modes_cfg = load_sheet_modes_config()
        inp = _parse_input(form, sheet_modes_cfg)
        result = compute_sizing(
            inp, sheet_modes_cfg.enabled_grades, cfg.validation.max_stop_distance_pct
        )

        # F6, part 2: the MATCH CHECK — "the loaded .htk is checked
        # against the mode and mismatch refuses cards" (Charter §3 F6).
        # Still ahead of every write: nothing has been persisted at this
        # point, so a refusal here leaves no row and no note to unwind.
        # Two separate refusals — the attested sheet must BE the mode in
        # force, and the key must be one the rung permits (reduced is
        # B-only). Both are logged: a refusal nobody can count is a rule
        # nobody can review at the DRC.
        assert_sheet_matches(dm["row"], dm["mode"], cfg=dm["cfg"])
        assert_grade_allowed(inp.grade, dm["mode"], cfg=dm["cfg"])
    except SheetMismatch as e:
        logger.error("aset.card REFUSED (F6 match check): {}", e)
        return _render(banner=_failed(str(e)), form=form)
    except (SizingError, ConfigError, DevEntryRefused, SessionBlocked) as e:
        return _render(banner=_failed(str(e)), form=form)
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"), form=form)

    try:
        store = AsetStore()
        store.ensure_schema()
        row_id = store.save(result)
        form["account_mode"] = store.account_mode_for(row_id)
    except Exception as e:
        return _render(
            banner=_failed(f"Persistence FAILED: {type(e).__name__}: {e}"), form=form
        )

    try:
        note_path, when, note_write = save_card(cfg, result)
    except DailyNoteRefused as e:
        form["orig_timestamp"] = ""
        form["card_row_id"] = str(row_id)
        banner = _failed(
            f"Persisted: aset_sizings id {row_id} ({store.db_name}) — but "
            f"daily-note write FAILED: {e}"
        )
        return _render(banner=banner, result=_result_card(result, form), form=form)

    form["orig_timestamp"] = when.isoformat()
    form["card_row_id"] = str(row_id)

    try:
        prefill_paths = load_prefill_paths()
        # S3 C4 (O4 A): the ONE trade-note writer takes the card; the
        # sizing note keeps the sizing time and the planned entry.
        inp = result.input
        card = {"id": row_id, "ticker": inp.ticker, "direction": inp.direction.value, "stop": inp.stop,
                "trade_def_slug": None}
        trade_path, trade_action = upsert_trade_note(card, when, prefill_paths, entry_price=inp.entry)
    except (PrefillConfigError, VaultWriteError) as e:
        banner = _failed(
            f"Persisted: aset_sizings id {row_id} ({store.db_name}) — daily note "
            f"appended to {note_path} — but trade-note write FAILED: {e}"
        )
        return _render(banner=banner, result=_result_card(result, form), form=form)

    if note_write is None:
        banner = (
            f'<div class="warn">Persisted: aset_sizings id {row_id} '
            f"({html.escape(store.db_name)}) · trade note {trade_action}: "
            f"{html.escape(str(trade_path))} · ⚠ DAILY-NOTE WRITE IS DISABLED "
            "(daily_note.write_enabled=false) — this card is NOT in the journal.</div>"
        )
    else:
        banner = (
            f'<div class="saved">Persisted: aset_sizings id {row_id} ({html.escape(store.db_name)}) '
            f"· {html.escape(note_write.action)} in {html.escape(str(note_path))} "
            f"(unit {html.escape(note_write.unit or '')}) "
            f"· trade note {trade_action}: {html.escape(str(trade_path))}</div>"
        )
    return _render(banner=banner, result=_result_card(result, form), form=form)


@app.post("/fill", response_class=HTMLResponse)
async def fill(request: Request) -> str:
    form = {k: str(v) for k, v in (await request.form()).items()}
    try:
        _check_entry_allowed()
        # Same block as /size, and for a sharper reason: a fill is a DB
        # UPDATE *plus* a note write. The note write would be refused by
        # the vaultwrite gate anyway, which would leave the card marked
        # FILLED in Postgres with nothing in the journal. Refuse the whole
        # thing up front instead of half of it.
        assert_writable("aset.fill", target=form.get("ticker") or None)
        cfg = load_config()

        # S3 C1 (v3 §2 [F-22]): the form contributes the typed PRICE and
        # the typed SHARES, nothing else. The sizing is the card's own row,
        # rebuilt by `SizingResult.from_card` inside THE fill under the
        # card lock — never a re-size of the posted fields.
        card_row_raw = form.get("card_row_id", "")
        if not card_row_raw.isdigit():
            raise SizingError(
                "No aset_sizings row id on this form — compute & persist a card "
                "first, then recompute its actual fill. (Refusing to write a fill "
                "update that cannot be tied to its card row.)"
            )
        orig_ts_raw = form.get("orig_timestamp", "")
        if not orig_ts_raw:
            raise SizingError(
                "No original card timestamp on this form — compute & persist a "
                "card first, then recompute its actual fill."
            )
        orig_timestamp = datetime.fromisoformat(orig_ts_raw)

        raw_price = form.get("actual_fill", "").strip()
        if not raw_price:
            raise SizingError(
                "REFUSED: a fill with no price. Type the price the broker filled you at. "
                "Nothing written."
            )
        try:
            actual_fill = Decimal(raw_price)
        except InvalidOperation as e:
            raise SizingError(f"Invalid actual fill price: {raw_price!r}. Nothing written.") from e
        raw_shares = form.get("fill_shares", "").strip()
        if not raw_shares.isdigit() or int(raw_shares) == 0:
            raise SizingError(
                f"REFUSED: a fill with no share count ({raw_shares!r}). Type the shares the "
                "broker filled. Nothing written."
            )

        # DB first (L28 step 3, 2026-09-03): a fill reported in the note
        # but missing from the DB is the failure mode being closed. THE
        # fill is one transaction — the FILLED transition, the entry leg
        # and the fill cache land together or not at all; a card that is
        # not TRIGGERED (radar) raises IllegalTransition naming the edge.
        store = AsetStore()
        store.ensure_schema()
        outcome = store.mark_filled(
            int(card_row_raw),
            price=actual_fill,
            shares=int(raw_shares),
            flag="confirmed",
            price_source="typed",
            price_asof=None,
            source="sheet",
        )
        filled, fill_result = outcome.result, outcome.recompute
        original = fill_result.original
    except IllegalTransition as e:
        return _render(
            banner=_failed(
                f"{e}\n\nARM the card and mark it TRIGGERED first — the buttons are "
                "on the open-cards list below."
            ),
            form=form,
        )
    except (SizingError, ConfigError, DailyNoteRefused, DevEntryRefused, SessionBlocked,
            CardStateError) as e:
        return _render(banner=_failed(str(e)), form=form)
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"), form=form)

    # THE fill has committed. A daily-note failure from here on must not
    # hide what the database now holds (L1): the failure, that the card
    # IS FILLED, and the fill's drift outcome exactly as on success.
    try:
        note_path, note_write = save_fill_update(cfg, fill_result, orig_timestamp)
    except Exception as e:
        refused = isinstance(e, (SizingError, ConfigError, DailyNoteRefused, DevEntryRefused,
                                 SessionBlocked, CardStateError))
        banner = _failed(str(e) if refused else f"{type(e).__name__}: {e}")
        banner += (
            f'<div class="warn">aset_sizings id {html.escape(card_row_raw)} marked '
            "FILLED — the daily-note write failed after the DB commit; the FILL "
            "UPDATE is NOT in the journal.</div>"
        )
    else:
        if note_write is None:
            banner = (
                f'<div class="warn">aset_sizings id {html.escape(card_row_raw)} marked '
                "FILLED · ⚠ DAILY-NOTE WRITE IS DISABLED (daily_note.write_enabled="
                "false) — the FILL UPDATE is NOT in the journal.</div>"
            )
        else:
            banner = (
                f'<div class="saved">aset_sizings id {html.escape(card_row_raw)} marked '
                f"FILLED · fill update {html.escape(note_write.action)} in "
                f"{html.escape(str(note_path))}</div>"
            )
    # S3 C4 (F22, v3 §7): the card's trade note, after the fill committed,
    # in this request. A failure leaves the card FILLED and says so (L1).
    note, note_failed = _fill_note(int(card_row_raw))
    if note is not None:
        banner += f'<div class="saved">{html.escape(_note_saved(note))}</div>'
    else:
        banner += f'<div class="warn">⚠ {html.escape(note_failed)}</div>'
    banner += _pick_banner(int(card_row_raw), filled)
    if fill_result.drift_warned is None:
        # v3 §4 / L1: his drift P is missing — the fill IS recorded; the
        # warning was not evaluated, and that is said, never implied.
        banner += f'<div class="warn">⚠ {html.escape(DRIFT_NOT_EVALUATED)}</div>'
    return _render(
        banner=banner,
        result=_result_card(original, form, fill=fill_result),
        form=form,
    )


@app.post("/attest", response_class=HTMLResponse)
async def attest(request: Request) -> str:
    """Record which `.htk` he states he has loaded (F6).

    ATTESTED, NOT READ. Cobalt never touches DAS Trader Pro (CLAUDE.md's
    first absolute boundary), and the trading PC is not on the tailnet
    anyway — so his word is the only input there is, and holding him to
    it is the whole mechanism.
    """
    form = {k: str(v) for k, v in (await request.form()).items()}
    filename = form.get("file", "").strip()
    account_mode = form.get("account_mode", "").strip()
    try:
        cfg = load_daymode_config()
        if not filename:
            raise SheetMismatch(
                "Pick the .htk you have loaded — an unstated hotkey file is exactly "
                "the state in which a full-size key gets pressed on a reduced day.",
                attested=None, mode="(none)",
            )
        if account_mode not in {"live", "sim"}:
            raise SheetMismatch(
                f"Pick account mode LIVE or SIM; got {account_mode!r}",
                attested=None,
                mode="(none)",
            )
        sheet = cfg.sheet_for_hotkey_file(filename)
        store = DayModeStore()
        store.ensure_schema()
        day = _today_et()
        store.attest_sheet(day, filename=filename, account_mode=account_mode)
        note_line = _write_daymode_note(cfg, day, store)
    except (SheetMismatch, ConfigError, SessionBlocked) as e:
        return _render(banner=_failed(str(e)))
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"))
    return _render(
        banner=f'<div class="saved">Attested {html.escape(filename)} '
        f"(= the {html.escape(sheet)} sheet). Cards are checked against this until "
        f"you change it.{html.escape(note_line)}</div>"
    )


@app.post("/card/{card_id}/move", response_class=HTMLResponse)
async def card_move(card_id: int, request: Request) -> str:
    """One state transition, from a button whose edge was already legal.

    Every button on the sheet is rendered FROM the edge table, so a
    refusal here means either a stale tab (the card moved underneath him)
    or a missing reason — and both are worth saying out loud rather than
    swallowing.
    """
    form = {k: str(v) for k, v in (await request.form()).items()}
    try:
        _check_entry_allowed()
        to_state = CardState(form.get("to", ""))
        if to_state is FILL_TARGET:
            # ONE PATH TO FILLED (S3 C1, v3 §2 [F-22]): a fill carries his
            # price and shares and lands with its entry leg, so it is
            # written only by THE fill (`AsetStore.mark_filled`). A FILLED
            # from here would be the priceless fill of F8.
            raise CardStateError(
                f"REFUSED card {card_id}: {FILL_TARGET.value} — this route never fills. "
                "A fill is written only by the fill (POST /fill with the price and shares "
                "the broker filled)."
            )
        if to_state is CardState.CLOSED:
            # CLOSED ONLY BY THE ZERO-RUNNING LEG (S3 C2 fix r1, v3 §2):
            # FILLED -> CLOSED is written by the leg writer whose exit,
            # correction or held count brings running to 0 (`cards.legs`).
            # A CLOSED from here would close a card still holding shares.
            raise CardStateError(
                f"REFUSED card {card_id}: {CardState.CLOSED.value} — this route never closes. "
                "A card closes only when an exit leg, a correction or a held count brings "
                "running to 0."
            )
        store = CardStore()
        store.ensure_schema()
        before = store.state_of(card_id)
        filled = None
        tids = [
            store.transition(
                card_id,
                to_state,
                actor=Actor.YOU,
                evidence={"via": "aset.sheet"},
                reason=(form.get("reason") or "").strip() or None,
            )
        ]
    except (IllegalTransition, CardStateError, SessionBlocked, DevEntryRefused) as e:
        logger.error("card {} move REFUSED: {}", card_id, e)
        return _render(banner=_failed(str(e)))
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"))
    extra = (
        f" · Cobalt inserted {len(tids) - 1} missing transition row(s) itself "
        "(one-click fill on a manual card — actor cobalt, evidence auto=manual_fill)"
        if len(tids) > 1
        else ""
    )
    return _render(
        banner=f'<div class="saved">card {card_id}: {before} → '
        f'{html.escape(form.get("to", ""))} (card_transitions id(s) '
        f'{", ".join(str(i) for i in tids)}){extra}</div>'
        + (_pick_banner(card_id, filled) if filled is not None else "")
    )


@app.post("/card/{card_id}/stop", response_class=HTMLResponse)
async def card_stop(card_id: int, request: Request) -> str:
    """A stop edit — decision 11. NOT a state change.

    No transition row is written; the edit is logged and folded into the
    NEXT transition's evidence. The amber YOURS badge and the lock in the
    other states are rendered by `_card_controls`.
    """
    form = {k: str(v) for k, v in (await request.form()).items()}
    try:
        # ONE card-stop function for the sheet and for voice (FINAL [F-06]).
        edit = set_card_stop(card_id, form.get("stop", ""))
    except (CardStateError, SessionBlocked, DevEntryRefused, InvalidOperation) as e:
        logger.error("card {} stop edit REFUSED: {}", card_id, e)
        return _render(banner=_failed(str(e)))
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"))
    return _render(
        banner=f'<div class="saved">card {card_id}: stop {edit.from_stop} → {edit.to_stop} '
        "(YOURS — not a state change; it rides in the next transition\'s evidence)</div>"
    )


# ---------------------------------------------------------------------
# Radar card taps (S2-P2 STEP-6). JSON for the panel's fetch POSTs; every
# refusal is a named 4xx with the reason, never a silent no-op. The locks
# and the ARM invariant live in `CardStore`, so every caller gets them.
# ---------------------------------------------------------------------


def _refused(status: int, reason: str) -> JSONResponse:
    logger.error("radar card route REFUSED ({}): {}", status, reason)
    return JSONResponse(status_code=status, content={"status": "REFUSED", "reason": reason})


async def _radar_form(request: Request) -> dict:
    return {k: str(v) for k, v in (await request.form()).items()}


def _todays_rung() -> tuple:
    dm = _daymode_state()
    if dm["error"] or dm["cfg"] is None or dm["mode"] is None:
        raise SheetMismatch(
            f"Day mode unresolved — no key can be sized: {dm['error']}", attested=None, mode="(unresolved)",
        )
    return dm


@app.post("/radar/card/{card_id}/key")
async def radar_card_key(card_id: int, request: Request):
    """Tap a key (R8): record the tapped grade, size at the nearest enabled
    key BELOW it with a loud notice, refuse when nothing is enabled below.
    `pass` is WATCH -> PASSED by you."""
    form = await _radar_form(request)
    raw = form.get("grade", "").strip()
    try:
        _check_entry_allowed()
        assert_writable("aset.radar.key", target=str(card_id))
        store = CardStore()
        if raw == "pass":
            tid = store.transition(card_id, CardState.PASSED, actor=Actor.YOU, evidence={"via": "radar.key"})
            return {"status": "ok", "card_id": card_id, "state": CardState.PASSED.value, "transition_id": tid}
        try:
            tapped = Grade(raw)
        except ValueError:
            return _refused(422, f"not a key: {raw!r} (keys: A+, A, B, C, pass)")
        dm = _todays_rung()
        # F6 unchanged: the attested .htk must be the sheet in force.
        assert_sheet_matches(dm["row"], dm["mode"], cfg=dm["cfg"])
        cfg = load_config()
        card = store.radar_card(card_id)
        sizing = size_at_key(
            tapped, ticker=card["ticker"], entry=card["entry"], stop=card["stop"],
            direction=Direction(card["direction"]), sheet_modes=load_sheet_modes_config(),
            sheet=dm["cfg"].sheet_for(dm["mode"]), enabled=dm["cfg"].enabled_grades_for(dm["mode"]),
            max_stop_distance_pct=cfg.validation.max_stop_distance_pct,
        )
        written = store.tap_key(card_id, sizing)
    except DevEntryRefused as e:
        return _refused(403, str(e))
    except (KeyRefused, SheetMismatch, CardStateError, IllegalTransition, SessionBlocked) as e:
        return _refused(409, str(e))
    except SizingError as e:
        return _refused(422, str(e))
    except ConfigError as e:
        return _refused(503, str(e))

    # The daily-note card block, bound to ONE stable unit per card (its
    # creation instant) — a re-tap updates that block, a scan never writes.
    try:
        note_path, _when, note_write = save_card(cfg, sizing.result, when=card["created_at"])
    except DailyNoteRefused as e:
        return JSONResponse(status_code=500, content={
            "status": "FAILED", "persisted": written,
            "reason": f"key sized and persisted, but the daily-note write FAILED: {e}",
        })
    return {"status": "ok", **written, "note": str(note_path),
            "note_write": None if note_write is None else note_write.action}


@app.post("/radar/card/{card_id}/dot/{factor}")
async def radar_card_dot(card_id: int, factor: str, request: Request):
    """Tap a dot 1-10: append the tap, set the trader grade, recompute
    conviction / card_score / proposed key under the card's row lock."""
    form = await _radar_form(request)
    try:
        grade = int(form.get("grade", ""))
    except ValueError:
        return _refused(422, f"a dot grade is an integer 1-10, got {form.get('grade')!r}")
    if not 1 <= grade <= 10:
        return _refused(422, f"a dot grade is 1-10, got {grade}")
    try:
        _check_entry_allowed()
        assert_writable("aset.radar.dot", target=str(card_id))
        settings = CardSettingsReader().current()
        dm = _todays_rung()
        return CardStore().tap_dot(
            card_id, factor, grade, bands=settings.proposed_key,
            enabled=dm["cfg"].enabled_grades_for(dm["mode"]),
        )
    except DevEntryRefused as e:
        return _refused(403, str(e))
    except (SheetMismatch, CardStateError, SessionBlocked) as e:
        return _refused(409, str(e))
    except (ConfigError, TraderSettingsError) as e:
        return _refused(503, str(e))


async def _promote(card_id: int, promoted: bool):
    try:
        _check_entry_allowed()
        assert_writable("aset.radar.promote", target=str(card_id))
        return CardStore().set_promoted(card_id, promoted)
    except DevEntryRefused as e:
        return _refused(403, str(e))
    except (CardStateError, SessionBlocked) as e:
        return _refused(409, str(e))


@app.post("/radar/card/{card_id}/promote")
async def radar_card_promote(card_id: int):
    return await _promote(card_id, True)


@app.post("/radar/card/{card_id}/release")
async def radar_card_release(card_id: int):
    return await _promote(card_id, False)


# ---------------------------------------------------------------------
# S3 exits C3 — the trade taps (v3 §2 / §3 / §5; R67, R38). One block,
# directly after `/release` (S-WEB). A route owns no side effect (L40): it
# parses the form and calls C1 / C2's writers — `AsetStore.mark_filled`
# (THE fill), `cards.legs.record_exit` / `record_held` / `record_correction`,
# `CardStore.transition`, the one card-stop function and
# `CardStore.record_stop_edit` — and the stores' reads, nothing else. Every
# refusal those writers raise reaches the page VERBATIM with a 4xx: JSON
# `{"status": "REFUSED", "reason": …}` for the panel's fetch, the sheet's
# page with the FAILED banner for `source=sheet` (C3-4). The session gate
# runs first, exactly as the other radar tap routes run it.
# ---------------------------------------------------------------------

#: Where he tapped — the panel, or the sheet's open-cards list (C3-4).
S3_TAP_SOURCES = ("panel", "sheet")


class _TapInputRefused(ValueError):
    """A posted field the writers cannot be called with. Nothing written."""


def _tap_price(raw: str | None, *, what: str) -> Decimal | None:
    raw = (raw or "").strip()
    if not raw:
        return None
    try:
        price = Decimal(raw)
    except InvalidOperation as e:
        raise _TapInputRefused(f"REFUSED: {what} {raw!r} is not a price. Nothing written.") from e
    # S3 C4-06 (L1): a leg price is a finite number > 0 — the `legs.price`
    # rule `CHECK (price > 0)`, refused here before any writer.
    if not price.is_finite() or price <= 0:
        raise _TapInputRefused(f"REFUSED: {what} {raw!r} is not a positive price. Nothing written.")
    return price


def _tap_int(raw: str | None, *, what: str) -> int | None:
    raw = (raw or "").strip()
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError as e:
        raise _TapInputRefused(f"REFUSED: {what} {raw!r} is not a whole number. Nothing written.") from e


def _tap_price_source(price: Decimal | None, prefill: str) -> tuple[str, str]:
    """(price_source, flag): the untouched prefill is the poll's price,
    `estimated` (v3 §3 — a tap with no keystroke); a price he typed or
    edited is his, `confirmed`."""
    if price is not None and prefill.strip() and price == Decimal(prefill.strip()):
        return "last_poll", "estimated"
    return "typed", "confirmed"


def _tap_board_row(store, card_id: int) -> dict | None:
    """The card's `radar_cards_v` row (its `last_price`, `structural_stop`),
    or None for a card that is not a radar card. A read."""
    return next((r for r in store.radar_board_cards(_today_et()) if r["card_id"] == card_id), None)


def _tap_reply(source: str, status: int, *, reason: str | None = None, payload: dict | None = None,
               banner: str = ""):
    if source == "sheet":
        if reason is not None:
            logger.error("card tap REFUSED ({}): {}", status, reason)
            return HTMLResponse(_render(banner=_failed(reason)), status_code=status)
        return HTMLResponse(_render(banner=f'<div class="saved">{html.escape(banner)}</div>'))
    if reason is not None:
        return _refused(status, reason)
    return {"status": "ok", **(payload or {})}


#: S3 C4 (v3 §7): what a failed note write shows. The DB write has
#: committed; the note is the one thing missing, said with its retry (L1).
NOTE_NOT_WRITTEN = "FILLED — trade note NOT written"
UNIT_NOT_WRITTEN = "leg saved, note unit NOT written"


def _note_reason(e: BaseException) -> str:
    from cobalt.prefill.trade_note import TradeNoteRefused

    known = (TradeNoteRefused, VaultWriteError, SessionBlocked, PrefillConfigError)
    return str(e) if isinstance(e, known) else f"{type(e).__name__}: {e}"


def _fill_note(card_id: int):
    """The card's trade note at the fill (C4-2), called only after THE fill
    returned (its transaction committed): `(CardNoteResult, None)` or
    `(None, failure line)`. Never raises — the card IS FILLED either way;
    on failure `trade_note_path` is NULL and the line names the retry."""
    from cobalt.prefill.trade_note import write_card_note

    try:
        return write_card_note(card_id), None
    except Exception as e:
        logger.error("card {}: trade note NOT written after the fill: {}", card_id, e)
        return None, (f"{NOTE_NOT_WRITTEN}: {_note_reason(e)} · trade_note_path NULL · "
                      f"retry: cobalt cards trade-note {card_id}")


def _note_saved(note) -> str:
    units = " · ".join(f"{unit} {action}" for unit, action in note.units)
    return f"trade note {note.action}: {note.relative} · {units}"


def _leg_note(card_id: int, leg_id: int, *, closed: bool) -> str | None:
    """The leg's unit in the card's trade note (C4-3), after the leg
    writer committed: None, or the notice naming why nothing was written
    in the vault. Never raises — the leg IS saved."""
    from cobalt.prefill.trade_note import write_leg_unit

    try:
        write_leg_unit(card_id, leg_id, closed=closed)
    except Exception as e:
        logger.error("card {}: leg {} saved, note unit NOT written: {}", card_id, leg_id, e)
        return f"{UNIT_NOT_WRITTEN}: {_note_reason(e)} · retry: cobalt cards trade-note {card_id}"
    return None


async def _card_tap(card_id: int, request: Request, gate: str, work):
    """Run one tap: the dev-entry guard and the session gate FIRST, then
    `work(form, source) -> (payload, banner)`; every refusal verbatim."""
    form = await _radar_form(request)
    source = form.get("source", "").strip() or "panel"
    if source not in S3_TAP_SOURCES:
        return _refused(422, f"REFUSED: source {source!r} is not one of {S3_TAP_SOURCES}. Nothing written.")
    try:
        _check_entry_allowed()
        assert_writable(gate, target=str(card_id))
        payload, banner = work(form, source)
    except DevEntryRefused as e:
        return _tap_reply(source, 403, reason=str(e))
    except (_TapInputRefused, SizingError) as e:
        return _tap_reply(source, 422, reason=str(e))
    except InvalidOperation as e:
        return _tap_reply(source, 422, reason=f"REFUSED: not a number ({e!r}). Nothing written.")
    except (CardStateError, IllegalTransition, SessionBlocked) as e:
        return _tap_reply(source, 409, reason=str(e))
    except ConfigError as e:
        return _tap_reply(source, 503, reason=str(e))
    return _tap_reply(source, 200, payload={"card_id": card_id, **payload}, banner=banner)


@app.post("/radar/card/{card_id}/triggered")
async def radar_card_triggered(card_id: int, request: Request):
    """ARMED -> TRIGGERED, his tap (v3 §2; O7 A). Evidence: the card's
    `last_price` and its bar time — no column stores that time (X6-R), so
    `last_price_at` is null, said, never guessed."""
    def work(form, source):
        store = CardStore()
        row = _tap_board_row(store, card_id)
        last = None if row is None else row["last_price"]
        tid = store.transition(
            card_id, CardState.TRIGGERED, actor=Actor.YOU,
            evidence={"via": f"{source}.triggered", "last_price": None if last is None else str(last),
                      "last_price_at": None},
        )
        return ({"state": CardState.TRIGGERED.value, "transition_id": tid},
                f"card {card_id}: TRIGGERED (card_transitions id {tid})")
    return await _card_tap(card_id, request, "aset.radar.triggered", work)


@app.post("/radar/card/{card_id}/fill")
async def radar_card_fill(card_id: int, request: Request):
    """FILLED @ [price] [shares] through THE fill (`mark_filled`, S-FILL).
    The untouched prefill → `last_poll` / `estimated`; a typed or edited
    price → `typed` / `confirmed`; no price → the fill's own refusal."""
    def work(form, source):
        price = _tap_price(form.get("price"), what="the fill price")
        shares = _tap_int(form.get("shares"), what="the share count")
        price_source, flag = _tap_price_source(price, form.get("prefill", ""))
        outcome = AsetStore().mark_filled(
            card_id, price=price, shares=shares, flag=flag, price_source=price_source,
            price_asof=None, source=source,
        )
        payload = {"state": CardState.FILLED.value, "leg_id": outcome.leg_id, "price_source": price_source,
                   "flag": flag, "pick_recorded": outcome.result.pick_recorded}
        notices = []
        if outcome.recompute.drift_warned is None:
            notices.append(DRIFT_NOT_EVALUATED)
        if not outcome.result.pick_recorded:
            notices.append(f"pick not recorded ({outcome.result.pick_error})")
        # S3 C4: the trade note, after THE fill committed (never inside it).
        note, note_failed = _fill_note(card_id)
        payload["trade_note_path"] = None if note is None else note.relative
        if note_failed:
            notices.insert(0, note_failed)
        if notices:
            payload["notice"] = " · ".join(notices)
        return payload, " · ".join([f"card {card_id}: FILLED ({flag}, entry leg {outcome.leg_id})", *notices])
    return await _card_tap(card_id, request, "aset.radar.fill", work)


@app.post("/radar/card/{card_id}/pass")
async def radar_card_pass(card_id: int, request: Request):
    """TRIGGERED -> PASSED, his tap (v3 §2)."""
    def work(form, source):
        tid = CardStore().transition(card_id, CardState.PASSED, actor=Actor.YOU,
                                     evidence={"via": f"{source}.pass"})
        return ({"state": CardState.PASSED.value, "transition_id": tid},
                f"card {card_id}: PASSED (card_transitions id {tid})")
    return await _card_tap(card_id, request, "aset.radar.pass", work)


@app.post("/radar/card/{card_id}/exit")
async def radar_card_exit(card_id: int, request: Request):
    """½ · ⅓ · flat · typed through `legs.record_exit` (R67). The tap posts
    the `running_before` its screen rendered. Flat commits `confirmed` only
    with his ✓ (`confirm=1`) — its price then his (`typed`); an untouched
    flat stays `estimated` and is listed for correction (v3 §3)."""
    def work(form, source):
        from cobalt.cards import legs
        from cobalt.session import clock as session_clock_mod

        preset = form.get("preset", "").strip()
        price = _tap_price(form.get("price"), what="the exit price")
        if price is None:
            raise _TapInputRefused(
                f"REFUSED card {card_id}: an exit with no price. Type the price you took. Nothing written."
            )
        running_before = _tap_int(form.get("running_before"), what="running_before")
        if running_before is None:
            raise _TapInputRefused(
                f"REFUSED card {card_id}: the tap carries no running_before — reload the card. Nothing written."
            )
        prefill = form.get("prefill", "")
        price_source, flag = _tap_price_source(price, prefill)
        if preset == "flat":
            confirmed = form.get("confirm", "").strip() == "1"
            flag = "confirmed" if confirmed else "estimated"
            if confirmed:
                price_source = "typed"
        result = legs.record_exit(
            card_id, preset=preset, shares=_tap_int(form.get("shares"), what="the typed share count"),
            price=price, price_source=price_source, price_asof=None, flag=flag, source=source,
            running_before=running_before, now=session_clock_mod.now_utc(),
        )
        payload = {"leg_id": result.leg_id, "shares": result.shares, "running_before": result.running_before,
                   "running_after": result.running_after, "closed": result.closed,
                   "transition_id": result.transition_id, "flag": flag}
        banner = (f"card {card_id}: exit {preset} {result.shares} sh @ {price} ({flag}) · running "
                  f"{result.running_before} → {result.running_after}")
        if result.closed:
            banner += " · CLOSED"
        notices = []
        if flag == "estimated":
            notices.append("estimated — listed for correction")
        # S3 C4: the leg's unit in the trade note, after the commit.
        unit_failed = _leg_note(card_id, result.leg_id, closed=result.closed)
        if unit_failed:
            notices.append(unit_failed)
        if notices:
            payload["notice"] = " · ".join(notices)
            banner += " · " + " · ".join(notices)
        return payload, banner
    return await _card_tap(card_id, request, "aset.radar.exit", work)


@app.post("/radar/card/{card_id}/held")
async def radar_card_held(card_id: int, request: Request):
    """HOLDING X — his held count through `legs.record_held` (R67 (1), S-HELD)."""
    def work(form, source):
        from cobalt.cards import legs
        from cobalt.session import clock as session_clock_mod

        held = _tap_int(form.get("held"), what="the held count")
        if held is None:
            raise _TapInputRefused(f"REFUSED card {card_id}: HOLDING names the shares you hold. Nothing written.")
        result = legs.record_held(card_id, held, source=source, now=session_clock_mod.now_utc())
        payload = {"leg_id": result.leg_id, "corrects": result.corrects, "running_after": result.running_after,
                   "closed": result.closed, "transition_id": result.transition_id}
        banner = f"card {card_id}: holding {held} · running {result.running_after}" + (
            " · CLOSED" if result.closed else "")
        # S3 C4: the held count rewrites the entry leg's unit (`leg-0`).
        unit_failed = _leg_note(card_id, result.leg_id, closed=result.closed)
        if unit_failed:
            payload["notice"] = unit_failed
            banner += f" · {unit_failed}"
        return payload, banner
    return await _card_tap(card_id, request, "aset.radar.held", work)


@app.post("/radar/card/{card_id}/correct")
async def radar_card_correct(card_id: int, request: Request):
    """A correction of one leg through `legs.record_correction` (R67): a
    typed price names its source (`typed`, L57) and is `confirmed`. The
    URL's card binds the leg (fix r1 F2): a leg that is not one of its
    current legs is refused before the writer — a read, rolled back."""
    def work(form, source):
        from cobalt.cards import legs
        from cobalt.session import clock as session_clock_mod

        leg_id = _tap_int(form.get("leg_id"), what="leg_id")
        if leg_id is None:
            raise _TapInputRefused(f"REFUSED card {card_id}: a correction names its leg. Nothing written.")
        if leg_id not in {leg["id"] for leg in legs.read_position(card_id).legs}:
            raise _TapInputRefused(
                f"REFUSED card {card_id}: leg {leg_id} is not a current leg of card {card_id} — reload the card. "
                "Nothing written."
            )
        price = _tap_price(form.get("price"), what="the corrected price")
        result = legs.record_correction(
            leg_id, price=price, price_source=None if price is None else "typed",
            shares=_tap_int(form.get("shares"), what="the corrected share count"), source=source,
            now=session_clock_mod.now_utc(),
        )
        payload = {"leg_id": result.leg_id, "corrects": result.corrects, "running_after": result.running_after,
                   "closed": result.closed, "transition_id": result.transition_id}
        banner = (f"card {card_id}: leg {result.corrects} corrected by leg {result.leg_id} · running "
                  f"{result.running_after}" + (" · CLOSED" if result.closed else ""))
        # S3 C4: a correction rewrites the SAME `leg-<seq>` unit (v3 §7).
        unit_failed = _leg_note(card_id, result.leg_id, closed=result.closed)
        if unit_failed:
            payload["notice"] = unit_failed
            banner += f" · {unit_failed}"
        return payload, banner
    return await _card_tap(card_id, request, "aset.radar.correct", work)


@app.post("/radar/card/{card_id}/stop")
async def radar_card_stop(card_id: int, request: Request):
    """His stop edit (R38: his stop is the plan until he resets it), through
    the one card-stop function — `record_stop_edit(kind='edit')`."""
    def work(form, source):
        from cobalt.aset import card_stop

        edit = card_stop.set_card_stop(card_id, form.get("to_stop", ""))
        return ({"stop_edit_id": edit.stop_edit_id, "from_stop": str(edit.from_stop), "to_stop": str(edit.to_stop)},
                f"card {card_id}: stop {edit.from_stop} → {edit.to_stop} (YOURS)")
    return await _card_tap(card_id, request, "aset.radar.stop", work)


@app.post("/radar/card/{card_id}/stop/reset")
async def radar_card_stop_reset(card_id: int, request: Request):
    """↺ — the stop back to Cobalt's structural stop, `kind='reset'` (R38,
    v3 §5 [F-11]). A card with no structural stop (a manual card) is not
    offered ↺ (O19 A); posted anyway, the writer refuses it by name."""
    def work(form, source):
        store = CardStore()
        current = next((c for c in store.open_cards() if c["id"] == card_id), None)
        if current is None:
            raise CardStateError(f"card {card_id} is not open — its stop is settled.")
        row = _tap_board_row(store, card_id)
        structural = None if row is None else row["structural_stop"]
        to_stop = current["stop"] if structural is None else structural
        edit_id = store.record_stop_edit(card_id, from_stop=current["stop"], to_stop=to_stop, kind="reset")
        return ({"stop_edit_id": edit_id, "from_stop": str(current["stop"]), "to_stop": str(to_stop)},
                f"card {card_id}: stop {current['stop']} → {to_stop} (↺ Cobalt's)")
    return await _card_tap(card_id, request, "aset.radar.stop_reset", work)


def _sheet_in_trade(card: dict) -> str:
    """C3-4: a FILLED MANUAL card is not on `/radar` (X-M: `radar_cards_v`
    is `origin = 'radar'`), so its IN-TRADE controls render here, on the
    sheet's open-cards list, posting to the SAME routes with
    `source=sheet` — never a second set of writers. A manual card has no
    structural stop: no ↺ (O19 A), gap `NULL — no Cobalt stop`. No last
    price is read here, so every price field is empty and he types."""
    from .radar_panel import read_in_trade, render_in_trade, render_stop_block

    if card.get("state") != CardState.FILLED.value or card.get("origin") != Origin.MANUAL.value:
        return ""
    try:
        position = read_in_trade(card["id"])
    except Exception as e:  # noqa: BLE001 — said on the card
        # fix r1 F4: the stop line stays — his stop, `Cobalt stop NULL`, no ↺
        # — as the panel's failed read keeps it (the one stop renderer).
        return _failed(f"card {card['id']}: position unreadable: {type(e).__name__}: {e}") + render_stop_block(
            card["id"], stop=card["stop"], structural_stop=None, owner=None, source="sheet",
        )
    return render_in_trade(
        card["id"], position, direction=str(card["direction"]), stop=card["stop"], structural_stop=None,
        last=None, source="sheet",
    )


def _sheet_closed_estimated(store) -> str:
    """fix r1 F3 (v3 §3: an untouched flat "stays `estimated` and is listed
    for correction"): each MANUAL card filled today (ET) that is now
    CLOSED, with its `estimated` legs and their `✓ correct` forms posting
    to `/radar/card/{id}/correct` with `source=sheet` — the SAME route, the
    one leg-row renderer. Read through `filled_with_picks` (a read); a card
    with no estimated leg renders nothing; a failed read is said on that
    card."""
    from .radar_panel import read_in_trade, render_estimated_legs

    try:
        filled = store.filled_with_picks(_today_et())
    except Exception as e:  # noqa: BLE001 — said on the sheet
        return _failed(f"closed manual cards unreadable: {type(e).__name__}: {e}")
    seen: set[int] = set()
    blocks = []
    for row in filled:
        card_id = row["card_id"]
        if card_id in seen or row.get("state") != CardState.CLOSED.value or row.get("origin") != Origin.MANUAL.value:
            continue
        seen.add(card_id)
        head = (f'<div class="top"><span class="tk">{html.escape(str(row["ticker"]))}</span>'
                f'<span class="st st-CLOSED">CLOSED</span><span class="muted">#{card_id} · estimated — '
                "confirm the price</span></div>")
        try:
            legs_html = render_estimated_legs(card_id, read_in_trade(card_id), structural_stop=None, source="sheet")
        except Exception as e:  # noqa: BLE001 — said on the card
            legs_html = (f'<div class="failed">FAILED · position unreadable: '
                         f"{html.escape(f'{type(e).__name__}: {e}')}</div>")
        if legs_html:
            blocks.append(f'<div class="crow">{head}{legs_html}</div>')
    return "".join(blocks)
