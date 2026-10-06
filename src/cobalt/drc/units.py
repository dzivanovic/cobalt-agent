"""The DRC note's Cobalt units — render ONLY (DRC D3-2; v2 §6, §13 as ruled).

Every function here turns STORED rows into a unit body: the day's `drc_rows`
as K1 / K2 recorded them (`trade`, `stats_row`, `day`, `seed`) and the
build's own `build_trade` / `build_day` rows (L57). Nothing here reads a
file, a setting, a card or a clock, and nothing computes a figure the rows
do not hold: `build.py` computes and stores; this module renders.

THE UNITS, by section, each under HIS heading (v2 §6 table; unit ids stable):

    drc-summary / summary          directly under the date line
    drc-day     / no_trade         no-trade days only (R93), then
    drc-day     / voice-no-trades  HIS blank unit, created once
    drc-day     / premarket        the four daily-note keys (R102 O11)
    drc-risk    / pnl              under `### PnL on the day:` (R102 O16)
    drc-risk-facts / facts         planned vs actual risk, the daily stop —
                                   under `### How I managed risk:`, above
                                   his paragraph (v2 §13 A9)
    drc-risk    / risk_parameters  existing (sheet-mode dollars)
    drc-trades  / tickers          the trade count line
    drc-trades  / trade-<id>       one block per stored trade (B-rows)
    drc-trades  / voice-<id>       HIS unit next to it, created once (R99)
    drc-trades  / open_positions   the book the day left (K3-1, v3 §2a / §5)
    drc-trades  / reconcile        the export vs the card's legs, what D5
                                   wrote or why not, the unresolved items
                                   (v2 §6 `:140`, R67 / R90)
    drc-open-items / open_positions  A31 `open items carried forward` (K3-3),
                                   directly after the drc-trades section
    drc-rules   / rules_check      existing scaffold (checkboxes + cards
                                   with no trade) — `prefill.drc`'s helpers

K3: the open-position unit, the summary's `open overnight` and the A31
line render ONE stored list, `build_day.derived["open_positions"]`, which
`build.plan_note` computes once (`[F-11]`, L3, L57).

A SECTION IS ONE BLOCK (`vaultwrite.markers`: a duplicate section is
refused), so `facts` is the unit of its OWN section `drc-risk-facts`
(D3 fix r1 F-4): `drc-risk` keeps `pnl` and `risk_parameters` under `### PnL
on the day:`.

`[F-23]`: no unit writes a line the 09:00 reader reads (`Grade:` /
`Goal:`, `daymode/drc.py:116`–`:117`). R101: no rules line, no engine unit.
"""

from __future__ import annotations

import re
from decimal import Decimal
from typing import Any, Iterable, Optional

from cobalt.vaultwrite import Placement, after_pattern
from cobalt.vaultwrite.markers import find_section

NOT_GIVEN = "not given"

SUMMARY = ("drc-summary", "summary")
NO_TRADE = ("drc-day", "no_trade")
VOICE_NO_TRADES = ("drc-day", "voice-no-trades")
PREMARKET = ("drc-day", "premarket")
PNL = ("drc-risk", "pnl")
FACTS = ("drc-risk-facts", "facts")
RISK_PARAMETERS = ("drc-risk", "risk_parameters")
TICKERS = ("drc-trades", "tickers")
RECONCILE = ("drc-trades", "reconcile")
OPEN_POSITIONS = ("drc-trades", "open_positions")
OPEN_ITEMS = ("drc-open-items", "open_positions")
RULES_CHECK = ("drc-rules", "rules_check")
TRADE_PREFIX = "trade-"
VOICE_PREFIX = "voice-"
#: The Cobalt heading his no-trade answer sits under (R93).
WHY_NO_TRADES = "### Why no trades today:"


def trade_unit(trade_id: str) -> tuple[str, str]:
    return ("drc-trades", f"{TRADE_PREFIX}{trade_id}")


def voice_unit(trade_id: str) -> tuple[str, str]:
    return ("drc-trades", f"{VOICE_PREFIX}{trade_id}")


# ---------------------------------------------------------------------
# placements — the first time a section lands in a note
# ---------------------------------------------------------------------


def date_line_placement(iso_day: str) -> Placement:
    """Directly under his date line (`### <date>` once the token is
    replaced)."""
    return after_pattern(re.compile(rf"^###\s+{re.escape(iso_day)}\s*$"), f"under the date line ### {iso_day}")


def _after_section(name: str):
    def locate(lines: list[str]):
        sec = find_section(lines, name)
        return None if sec is None else (sec.close_line + 1, sec.close_line + 1)

    return locate


#: `drc-day`: directly under the summary section.
DAY_PLACEMENT = Placement("under the drc-summary section", _after_section(SUMMARY[0]))
#: `drc-risk`: under `### PnL on the day:` (his heading carries a U+00A0;
#: `\s` matches it).
PNL_PLACEMENT = after_pattern(re.compile(r"^###\s*PnL on the day"), "under '### PnL on the day:'")
#: `drc-risk-facts`: directly under `### How I managed risk:`, above his
#: paragraph (v2 §13 A9; D3 fix r1 F-4). Its own section: a section is one
#: block, and `drc-risk` stays under `### PnL on the day:`.
RISK_FACTS_PLACEMENT = after_pattern(re.compile(r"^###\s*How I managed risk"), "under '### How I managed risk:'")
#: `drc-open-items` (A31, K3-3): directly after the drc-trades section, so
#: no line lands outside a section.
OPEN_ITEMS_PLACEMENT = Placement("after the drc-trades section", _after_section(OPEN_POSITIONS[0]))


# ---------------------------------------------------------------------
# small formatting
# ---------------------------------------------------------------------


def money(value: Any) -> str:
    d = Decimal(str(value))
    return f"-${abs(d)}" if d < 0 else f"${d}"


def given(value: Any) -> str:
    return NOT_GIVEN if value is None or value == "" else str(value)


def _clock(iso: Optional[str]) -> str:
    """`HH:MM:SS ET` from a stored ISO time (the trading log's own zone)."""
    return NOT_GIVEN if not iso else f"{iso[11:19]} ET"


# ---------------------------------------------------------------------
# the units
# ---------------------------------------------------------------------


def summary(day_row: dict) -> str:
    d = day_row["derived"]
    lines: list[str] = list(d["partial_lines"])
    if d.get("pairing"):
        lines.append(f"pairing {d['pairing']}")
    if d.get("not_repaired"):
        lines.extend(d["not_repaired"])
    if d.get("miss_line") == "pending":
        lines.append("miss line: pending (replay inputs not stored)")
    lines.append(f"P&L: {d['pnl_text']}")
    lines.append(f"W/L: {d['wl_text']}")
    lines.append(f"open overnight: {d['open_overnight']}")
    lines.append(f"cards written: {d['cards_written']} · taken: {d['cards_taken']}")
    lines.append(f"screenshots bound / trades: {d['screenshots_text']}")
    unmapped = f"unmapped playbooks: {d['unmapped_playbooks']}"
    if d.get("strategies_readable") is False:
        unmapped += " — strategies folder not readable"
    lines.append(unmapped)
    return "\n".join(lines)


def no_trade(day_row: dict) -> str:
    d = day_row["derived"]
    return "\n".join([f"no trades — {day_row['inputs']['day']} · cards written: {d['cards_written']}", WHY_NO_TRADES])


def premarket(day_row: dict) -> str:
    p = day_row["inputs"]["premarket"]
    return (
        f"premarket — sleep: {given(p.get('Sleep'))} · readiness: {given(p.get('Readiness'))} · "
        f"RHR: {given(p.get('RHR'))} · 1% goal: {given(p.get('1% goal'))} · "
        f"meditated: {NOT_GIVEN} · tone: {NOT_GIVEN} · hotkey: {NOT_GIVEN}"
    )


def pnl(day_row: dict) -> str:
    return f"PnL: {day_row['derived']['pnl_text']}"


def facts(day_row: dict, builds: list[dict]) -> str:
    d = day_row["derived"]
    if d.get("pairing"):
        return f"risk: {d['pairing']}"
    lines = [f"daily stop: {d['daily_stop_text']}"]
    for b in builds:
        lines.append(f"- {b['derived']['label']}: {b['derived']['risk_text']}")
    return "\n".join(lines)


def tickers(day_row: dict) -> str:
    return day_row["derived"]["tickers_text"]


def trade_block(trade: dict, build: dict) -> str:
    """One stored trade row + its `build_trade` row → the B-rows block."""
    b = build["derived"]
    lines = [f"- Ticker: {trade['symbol']} · {trade['direction']} · {trade['status']} · trade {trade['trade_id']}"]
    lines.extend(f"  - {line}" for line in b["lines"])
    return "\n".join(lines)


def orphaned(trade_id: str) -> str:
    return f"orphaned — trade {trade_id} is not in the current trading log"


def unresolved_line(item: dict) -> str:
    """D5-3 (R90): the one wording of an unresolved item — the note's two
    units and the page."""
    return f"unresolved: card {item['card_id']} — {item['refusal']}"


def _unresolved(d: dict) -> list[str]:
    return [unresolved_line(i) for i in d.get("unresolved") or []]


def _leg_text(shares: Any, price: Any, at: Optional[str]) -> str:
    return f"{shares}@{given(price)} {_clock(at)}"


_STATES = {"match": "match", "export_only": "DAS exit with no Cobalt leg",
           "cobalt_only": "Cobalt leg with no DAS execution", "entry_not_written": "no Cobalt entry leg"}


def _diff_line(row: dict) -> str:
    exp, cob = row["export"], row["cobalt"]
    exp_text = "none" if exp is None else _leg_text(exp["shares"], exp["price"], exp["time"])
    cob_text = "none" if cob is None else (
        f"{_leg_text(cob['shares'], cob['price'], cob['at'])} (leg #{cob['leg_id']}, {cob['flag']}, {cob['source']})"
    )
    fields = row["fields"]
    state = (f"{', '.join(fields)} differ{'s' if len(fields) == 1 else ''}" if row["state"] == "mismatch"
             else _STATES[row["state"]])
    held = (f" · held after: DAS {'—' if exp is None else exp['held_after']} · "
            f"Cobalt {'—' if cob is None else cob['held_after']}")
    return f"  seq {row['seq']} {row['kind']}: DAS {exp_text} · Cobalt {cob_text} — {state}{held}"


def _history_line(h: dict) -> str:
    text = f"  history: leg #{h['leg_id']} seq {h['seq']} {h['kind']} {_leg_text(h['shares'], h['price'], h['at'])} " \
           f"{h['source']} ({h['flag']})"
    if h.get("held_stated") is not None:
        text += f" · held stated {h['held_stated']}"
    if h.get("corrects") is not None:
        text += f" · corrects #{h['corrects']}"
    return text


def reconcile(day_row: dict, builds: Iterable[dict]) -> str:
    """D5 (v2 §6 `:140`, R67 / R90): per matched trade, the export against
    the card's legs as found (the "before"), his taps and held statements as
    history, then what was written (`adjusted to DAS: <k> rows (<ids>)`, and
    `… — then refused: <refusal>` when a later write was refused) or
    why nothing was; then every unresolved item. From the stored
    `build_trade.derived["reconcile"]` and `build_day.derived["unresolved"]`
    only."""
    d = day_row["derived"]
    if d.get("pairing"):
        return "\n".join([f"reconcile: {d['pairing']}"] + _unresolved(d))
    lines: list[str] = []
    for b in builds:
        r = b["derived"].get("reconcile")
        if r is None:
            continue
        basis = f" · running read from {r['basis']}" if r.get("basis") else ""
        lines.append(f"{b['derived']['label']} · card #{r['card_id']}{basis}")
        if r.get("read_refused"):
            lines.append(f"  legs: not read — {r['read_refused']}")
        if r.get("entry_leg"):
            lines.append(f"  {r['entry_leg']}")
        lines.extend(_diff_line(row) for row in r["before"])
        lines.extend(_history_line(h) for h in r["history"])
        lines.append(f"  {r['status']}")
        if r.get("running_after") is not None:
            lines.append(f"  running after: {r['running_after']} · DAS position: {r['export_held']}")
    if not lines:
        lines.append("no trade matched a card — nothing to reconcile")
    return "\n".join(lines + _unresolved(d))


def stale_resolve(resolve_id: int, effect_day: str) -> str:
    """K3-4 (a) (K2 fix r2 `## FOR K3`): a stored row names a resolve that
    was restated — the one wording, the note's and the page's."""
    return f"STALE — resolve #{resolve_id} was restated; rebuild {effect_day} once {effect_day}'s input is recorded"


def _stale_resolves(d: dict) -> list[str]:
    return [stale_resolve(s["resolve_id"], s["effect_day"]) for s in d.get("stale_resolves") or []]


def _position_line(p: dict) -> str:
    return " · ".join([
        p["symbol"],
        p["direction"],
        str(p["held_shares"]),
        f"avg cost {NOT_GIVEN if p['avg_cost'] is None else money(p['avg_cost'])}",
        f"opened {p['opened_on'] or 'not stated'}",
        f"day {'not stated' if p['days_held'] is None else p['days_held']}",
        p["status"],
        f"carried from {p['carried_from'] or '—'}",
        f"last execution {p['last_execution'] or 'not stored'}",
        p["trade_id"],
    ])


def open_positions(day_row: dict) -> str:
    """K3-1 (v3 §2a, §5): the book the day left — a header and one line per
    position, or ONE loud line (pairing not computed, a stale book, no
    `book_close` row); never `left open: 0` for an unknown book (L1)."""
    d = day_row["derived"]
    lines = _stale_resolves(d)
    listed = d["open_positions"]
    if listed is None:
        return "\n".join([*lines, d["open_positions_state"]])
    if not listed:
        lines.append("left open: 0 — tomorrow starts flat (stated by this DRC)")
    else:
        lines.append(
            f"left open: {len(listed)} — tomorrow's import starts from these · "
            f"book: {d['open_positions_book'][:12]}"
        )
        lines.extend(_position_line(p) for p in listed)
    return "\n".join(lines)


def open_items(day_row: dict) -> str:
    """K3-3 (v3 §5 A31, `[F-11]`): the open positions under `open items
    carried forward`, from the SAME list; then D5-3's unresolved items."""
    d = day_row["derived"]
    head = "open items carried forward — "
    listed = d["open_positions"]
    if listed is None:
        lines = [head + d["open_positions_state"]]
    elif not listed:
        lines = [head + "open positions: none"]
    else:
        lines = [f"{head}open positions: {len(listed)}"] + [
            f"{p['symbol']} {p['direction']} {p['held_shares']} · {p['trade_id']} · "
            f"day {'not stated' if p['days_held'] is None else p['days_held']}"
            for p in listed
        ]
    # D5-3 (R90): every unresolved item, carried until resolved.
    return "\n".join(lines + _unresolved(d))


def build_rows_by_ref(rows: Iterable[dict]) -> dict[str, dict]:
    return {r["ref"]: r for r in rows if r["kind"] == "build_trade"}


__all__ = [
    "DAY_PLACEMENT", "FACTS", "NOT_GIVEN", "NO_TRADE", "OPEN_ITEMS", "OPEN_ITEMS_PLACEMENT", "OPEN_POSITIONS", "PNL",
    "PNL_PLACEMENT", "PREMARKET", "RECONCILE",
    "RISK_FACTS_PLACEMENT", "RISK_PARAMETERS", "RULES_CHECK", "SUMMARY", "TICKERS", "TRADE_PREFIX", "VOICE_NO_TRADES", "VOICE_PREFIX",
    "WHY_NO_TRADES", "build_rows_by_ref", "date_line_placement", "facts", "given", "money", "no_trade",
    "open_items", "open_positions", "orphaned", "pnl", "premarket", "reconcile", "stale_resolve", "summary",
    "tickers", "unresolved_line",
    "trade_block", "trade_unit", "voice_unit",
]
