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
    STOP_EDITABLE,
    Actor,
    CardState,
    CardStateError,
    CardStore,
    IllegalTransition,
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
from cobalt.vault import VaultConfigError, dev_entry_allowed, is_production, resolve_vault_path

from .config import ConfigError, load_config, load_sheet_modes_config
from .daily_note import DailyNoteRefused, save_card, save_fill_update
from .engine import SizingError, compute_fill_recompute, compute_sizing
from .models import Grade, SizingInput
from .prefill import PrefillError, fetch_last_price
from .store import AsetStore

app = FastAPI(title="Cobalt ASET Sheet", docs_url=None, redoc_url=None)


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
<h1>ASET SEMI-AUTO SHEET <span class="muted">pre-beta slice 1 · {e(env_label)}</span></h1>
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
</div></body></html>"""



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


def _daymode_state() -> dict:
    """Everything the sheet needs about the day mode, resolved once.

    Never raises: a config or database failure renders as a LOUD banner
    rather than a 500, because a sheet that will not paint is a sheet he
    cannot trade beside. `error` being set is itself the refusal — every
    card write re-checks through `assert_sheet_matches`, so a degraded
    banner can never let a card through.
    """
    try:
        cfg = load_daymode_config()
        day = _today_et()
        store = DayModeStore()
        store.ensure_schema()
        row = store.for_date(day)
        mode = decided_or_stage1(row, cfg)
        return {
            "cfg": cfg, "day": day, "row": row, "mode": mode, "error": None,
            "stage": _stage_label(row),
        }
    except Exception as e:  # noqa: BLE001 - rendered, never swallowed
        return {"cfg": None, "day": None, "row": None, "mode": None,
                "stage": "UNRESOLVED", "error": f"{type(e).__name__}: {e}"}


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
        f'{e(str(card["shares"]))} sh · {e(str(card["session"]))}</span>{key_lock}</div>'
        f'{stop_html}<div class="acts">{"".join(buttons)}</div></div>'
    )


def _open_cards_section() -> str:
    try:
        store = CardStore()
        store.ensure_schema()
        cards = store.open_cards()
    except Exception as e:  # noqa: BLE001
        return (f'<div class="card"><div class="failed">FAILED\nOpen cards unreadable: '
                f'{html.escape(f"{type(e).__name__}: {e}")}</div></div>')
    if not cards:
        return ('<div class="card"><label>Open cards (F7)</label>'
                '<div class="muted">No card is in a live state. Terminal cards '
                '(CLOSED / PASSED / EXPIRED / MISSED) are not listed.</div></div>')
    rows = "".join(_card_controls(c) for c in cards)
    return (f'<div class="card"><label>Open cards (F7) — every button writes a '
            f'transition</label><div class="cards">{rows}</div></div>')

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
        trade_path, trade_action = upsert_trade_note(result, when, prefill_paths)
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
        sheet_modes_cfg = load_sheet_modes_config()
        inp = _parse_input(form, sheet_modes_cfg)
        original = compute_sizing(
            inp, sheet_modes_cfg.enabled_grades, cfg.validation.max_stop_distance_pct
        )  # deterministic recompute; no re-persist

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

        fill_result = compute_fill_recompute(
            original, actual_fill, cfg.validation.max_fill_distance_pct
        )

        # L28 step 3 (2026-09-03): the recompute is an UPDATE to the card
        # row it belongs to — status FILLED + the actual-fill figures.
        # Before this it created no row at all, which is why the 09-03
        # TSLA FILL UPDATE (10:02:36) was unrecoverable from Postgres.
        # DB first: a fill reported in the note but missing from the DB
        # is exactly the failure mode being closed.
        card_row_raw = form.get("card_row_id", "")
        if not card_row_raw.isdigit():
            raise SizingError(
                "No aset_sizings row id on this form — compute & persist a card "
                "first, then recompute its actual fill. (Refusing to write a fill "
                "update that cannot be tied to its card row.)"
            )
        store = AsetStore()
        store.ensure_schema()
        # F7: a fill is TRIGGERED -> FILLED and nothing else. If the card
        # has not been armed and marked triggered, mark_filled raises
        # IllegalTransition naming the edge — it is NOT coerced, because
        # a card that reached FILLED without ever being TRIGGERED makes
        # the MISSED count (Charter §3 F7) meaningless.
        store.mark_filled(int(card_row_raw), fill_result)

        note_path, note_write = save_fill_update(cfg, fill_result, orig_timestamp)
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
    try:
        cfg = load_daymode_config()
        if not filename:
            raise SheetMismatch(
                "Pick the .htk you have loaded — an unstated hotkey file is exactly "
                "the state in which a full-size key gets pressed on a reduced day.",
                attested=None, mode="(none)",
            )
        mode = cfg.mode_for_hotkey_file(filename)
        store = DayModeStore()
        store.ensure_schema()
        store.attest_sheet(_today_et(), filename=filename)
    except (SheetMismatch, ConfigError, SessionBlocked) as e:
        return _render(banner=_failed(str(e)))
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"))
    return _render(
        banner=f'<div class="saved">Attested {html.escape(filename)} '
        f"(= {html.escape(mode)} rung). Cards are checked against this until you "
        "change it.</div>"
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
        store = CardStore()
        store.ensure_schema()
        before = store.state_of(card_id)
        tid = store.transition(
            card_id,
            CardState(form.get("to", "")),
            actor=Actor.YOU,
            evidence={"via": "aset.sheet"},
            reason=(form.get("reason") or "").strip() or None,
        )
    except (IllegalTransition, CardStateError, SessionBlocked, DevEntryRefused) as e:
        logger.error("card {} move REFUSED: {}", card_id, e)
        return _render(banner=_failed(str(e)))
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"))
    return _render(
        banner=f'<div class="saved">card {card_id}: {before} → '
        f'{html.escape(form.get("to", ""))} (card_transitions id {tid})</div>'
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
        _check_entry_allowed()
        store = CardStore()
        store.ensure_schema()
        before = store.open_cards()
        current = next((c for c in before if c["id"] == card_id), None)
        if current is None:
            raise CardStateError(f"card {card_id} is not open — its stop is settled.")
        new_stop = Decimal(form.get("stop", ""))
        store.record_stop_edit(card_id, from_stop=current["stop"], to_stop=new_stop)
    except (CardStateError, SessionBlocked, DevEntryRefused, InvalidOperation) as e:
        logger.error("card {} stop edit REFUSED: {}", card_id, e)
        return _render(banner=_failed(str(e)))
    except Exception as e:
        return _render(banner=_failed(f"{type(e).__name__}: {e}"))
    return _render(
        banner=f'<div class="saved">card {card_id}: stop {current["stop"]} → {new_stop} '
        "(YOURS — not a state change; it rides in the next transition\'s evidence)</div>"
    )
