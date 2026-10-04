"""The `/drc` page (DRC D2-4) — the ASET app's second page template,
beside the sheet's (`web._render`) and the radar's (`radar_panel`).

PURE RENDERING. Everything shown comes from `cobalt.drc.imports.DayView`
(store reads and a folder listing) and, after an action, its
`PlaceResult`; nothing here reads, computes or writes anything. Every
string is escaped. No kind picker (R114), no rule checker (R101), no PDF.

The per-trade drop zones follow the trade-reporter PATTERN (drop, click
or paste an image onto a trade) — its interaction only, none of its
fields.

K3 (v3 §5): beside STARTING BOOK, the state-your-book form (`[I was
flat]`, one tap; `[List positions]`, a preview first) and RESOLVE for each
trade carried into the day; after a preview, the `Confirm` form sends the
previewed rows and their `book_sha256` back (L7). The after-drop line and
the day's resolve outcomes come from the `DayView`.
"""

from __future__ import annotations

import html
from typing import Optional

from cobalt.drc.imports import DayView, PlaceResult, StatementPreview

_CSS = """
 .drc h2{font-size:14px;letter-spacing:.06em;color:#9fafca;margin:14px 0 6px}
 .drc .status{font-size:18px;font-weight:800;padding:10px 12px;border-radius:8px;border:1px solid #28334d;margin-bottom:12px}
 .drc .line{font-size:13px;margin:3px 0;white-space:pre-wrap}
 .drc .loud{color:#ffd84d;font-weight:700}
 .drc .bad{color:#ffc3ce;font-weight:700}
 .drc .zone{border:1px dashed #28334d;border-radius:8px;padding:8px;margin:6px 0;font-size:12px;cursor:pointer}
 .drc .zone.over{border-color:#00e5ff}
 .drc form{margin:6px 0}
"""

_JS = """
 document.querySelectorAll('.zone').forEach(zone => {
   const form = zone.querySelector('form');
   const input = form.querySelector('input[type=file]');
   const send = files => { const dt = new DataTransfer();
     for (const f of files) dt.items.add(f); input.files = dt.files; form.submit(); };
   zone.addEventListener('click', () => input.click());
   input.addEventListener('change', () => form.submit());
   zone.addEventListener('dragover', e => { e.preventDefault(); zone.classList.add('over'); });
   zone.addEventListener('dragleave', () => zone.classList.remove('over'));
   zone.addEventListener('drop', e => { e.preventDefault(); send(e.dataTransfer.files); });
   zone.addEventListener('paste', e => { const f = [...e.clipboardData.files]; if (f.length) send(f); });
 });
"""


def _e(text: object) -> str:
    """An ATTRIBUTE value: quotes escaped."""
    return html.escape(str(text))


def _t(text: object) -> str:
    """TEXT content: `<`, `>`, `&` escaped; quotes kept as written (the
    R51 line's "P's close" reads as he will read it)."""
    return html.escape(str(text), quote=False)


def _lines(items: list[str], cls: str = "line") -> str:
    return "".join(f'<div class="{cls}">{_t(i)}</div>' for i in items)


def _file_class(text: str) -> str:
    if text.startswith("FAILED") or text.startswith("orphaned"):
        return "line bad"
    if "PARTIAL" in text:
        return "line loud"
    return "line"


#: Rows the `[List positions]` form offers (empty rows are ignored).
LIST_ROWS = 3


def _hidden(name: str, value: object) -> str:
    return f'<input type="hidden" name="{_e(name)}" value="{_e("" if value is None else value)}">'


def _confirm(day: str, p: StatementPreview) -> str:
    """K3-6 / K3-7: the previewed row's fields sent back with its sha (L7)."""
    if p.action == "state-book":
        fields = "".join(
            _hidden("symbol", r["symbol"]) + _hidden("direction", r["direction"]) + _hidden("shares", r["shares"])
            + _hidden("avg_cost", r["avg_cost"])
            for r in p.positions
        )
    else:
        (r,) = p.positions
        fields = _hidden("trade_id", r["trade_id"]) + _hidden("exit_price", r["exit_price"]) + _hidden(
            "exit_time", r["exit_time"])
    return (
        f'<form method="post" action="/drc/{_e(p.action)}">{_hidden("date", day)}{fields}'
        f'{_hidden("supersedes", p.supersedes)}{_hidden("sha256", p.sha256)}'
        f'<button class="primary" type="submit">Confirm — write book_sha256 {_t(p.sha256[:12])}</button></form>'
    )


def _state_book_form(day: str) -> str:
    """K3-6 (v3 §2c row A, §5): `[I was flat]` one tap; `[List positions]`."""
    rows = "".join(
        '<div class="line"><input name="symbol" placeholder="symbol">'
        '<select name="direction"><option value="long">long</option><option value="short">short</option></select>'
        '<input name="shares" placeholder="shares"><input name="avg_cost" placeholder="avg cost (optional)"></div>'
        for _ in range(LIST_ROWS)
    )
    return (
        '<div class="card"><h2>STATE YOUR BOOK</h2>'
        f'<form method="post" action="/drc/state-book">{_hidden("date", day)}'
        '<input type="hidden" name="flat" value="1"><button type="submit">I was flat</button></form>'
        f'<form method="post" action="/drc/state-book">{_hidden("date", day)}{rows}'
        '<input name="supersedes" placeholder="restates statement # (optional)">'
        '<button type="submit">List positions</button></form></div>'
    )


def _resolve_forms(day: str, carried: list[str]) -> str:
    """K3-7: RESOLVE `closed outside the export`, one form per carried trade."""
    forms = "".join(
        f'<form method="post" action="/drc/resolve">{_hidden("date", day)}{_hidden("trade_id", t)}'
        f'<div class="line">{_t(t)}</div><input name="exit_price" placeholder="exit price (optional)">'
        '<input name="exit_time" placeholder="exit time, ISO with offset (optional)">'
        '<input name="supersedes" placeholder="restates resolve # (optional)">'
        '<button type="submit">Resolve — closed outside the export</button></form>'
        for t in carried
    )
    return '<div class="card"><h2>RESOLVE</h2>' + (forms or _lines(["no position carried into this day"])) + "</div>"


def failed_page(message: str, css: str = "") -> str:
    return _page(f'<div class="failed">FAILED\n{_t(message)}</div>', css)


def _page(body: str, css: str) -> str:
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Cobalt · DRC imports</title>
<style>{css}{_CSS}</style></head><body><div class="wrap drc">
<h1>DRC IMPORTS · <a href="/">ASET sheet</a></h1>
{body}
<script>{_JS}</script>
</div></body></html>"""


def render(view: DayView, result: Optional[PlaceResult] = None, *, cards_error: Optional[str] = None,
           css: str = "") -> str:
    """The page for `view.date`, with `result` (the action just taken) on top."""
    day = view.date.isoformat()
    parts: list[str] = [
        f'<form method="get" action="/drc"><label>Date</label>'
        f'<input name="date" type="date" value="{_e(day)}"><button type="submit">Show</button></form>'
    ]
    if result is not None:
        action: list[str] = []
        if result.refused:
            action.append(result.refused)
        if result.message:
            action.append(result.message)
        action += [f.text() for f in result.files] + result.orphaned
        if result.status_line:
            action.append(result.status_line)
        parts.append('<div class="card"><h2>THIS ACTION</h2>'
                     + "".join(f'<div class="{_file_class(a)}">{_t(a)}</div>' for a in action)
                     + (_confirm(day, result.preview) if result.preview is not None else "") + "</div>")

    parts.append(f'<div class="status">{_t(view.status_line)}</div>')
    if view.event_line:
        parts.append(_lines([view.event_line]))

    morning = view.morning + ([view.stated_difference] if view.stated_difference else [])
    parts.append('<div class="card"><h2>STARTING BOOK</h2>' + _lines(morning, "line loud")
                 + (_lines([view.after_drop]) if view.after_drop else "") + "</div>")
    parts.append(_state_book_form(day))
    parts.append(_resolve_forms(day, view.carried))
    if view.resolves:
        parts.append('<div class="card"><h2>RESOLVES</h2>' + _lines(view.resolves, "line loud") + "</div>")
    notes = ([view.unpaired] if view.unpaired else []) + view.notes
    if notes:
        parts.append('<div class="card">' + _lines(notes, "line loud") + "</div>")

    files = [f.text() for f in view.files] + view.orphaned
    parts.append(
        '<div class="card"><h2>FILES</h2>'
        + ("".join(f'<div class="{_file_class(t)}">{_t(t)}</div>' for t in files) or _lines(["none yet"]))
        + "</div>"
    )

    counts = "".join(
        f"<tr><td>{_t(k)}</td><td>{_t('not given' if v is None else v)}</td></tr>"
        for k, v in view.counts.items()
    )
    parts.append(f'<div class="card"><h2>COUNTS</h2><table>{counts}</table>'
                 + (_lines([f"FAILED: cards unreadable — {cards_error}"], "line bad") if cards_error else "")
                 + "</div>")

    zones = "".join(
        f'<div class="zone" tabindex="0">{_t(t)} — drop, click or paste a screenshot'
        f'<form method="post" action="/drc/import" enctype="multipart/form-data" hidden>'
        f'<input type="hidden" name="date" value="{_e(day)}">'
        f'<input type="hidden" name="trade_key" value="{_e(t)}">'
        f'<input type="file" name="files" accept="image/png,image/jpeg"></form></div>'
        for t in view.trades
    )
    parts.append('<div class="card"><h2>TRADES</h2>' + (zones or _lines(["no trades recorded"])) + "</div>")

    pending = (
        [f"in the folder, not imported: {len(view.folder_pending)} — {', '.join(view.folder_pending)}"]
        if view.folder_pending else []
    )
    parts.append(
        '<div class="card"><h2>DROP</h2>'
        f'<form method="post" action="/drc/import" enctype="multipart/form-data">'
        f'<input type="hidden" name="date" value="{_e(day)}">'
        '<input type="file" name="files" multiple><button class="primary" type="submit">Import</button></form>'
        + _lines(pending, "line loud")
        + f'<form method="post" action="/drc/scan"><input type="hidden" name="date" value="{_e(day)}">'
        '<button type="submit">Import the files in the day\'s folder</button></form>'
        f'<form method="post" action="/drc/no-trade"><input type="hidden" name="date" value="{_e(day)}">'
        '<button type="submit">No trades today</button></form></div>'
    )
    return _page("\n".join(parts), css)


__all__ = ["failed_page", "render"]
