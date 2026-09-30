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
    drc-trades  / reconcile        the diff only (R90 / R67)
    drc-rules   / rules_check      existing scaffold (checkboxes + cards
                                   with no trade) — `prefill.drc`'s helpers

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


def reconcile(day_row: dict) -> str:
    d = day_row["derived"]
    if d.get("pairing"):
        return f"reconcile: {d['pairing']}"
    return "\n".join(["legs: not built", "adjustment pending (legs writer not built)"])


def build_rows_by_ref(rows: Iterable[dict]) -> dict[str, dict]:
    return {r["ref"]: r for r in rows if r["kind"] == "build_trade"}


__all__ = [
    "DAY_PLACEMENT", "FACTS", "NOT_GIVEN", "NO_TRADE", "PNL", "PNL_PLACEMENT", "PREMARKET", "RECONCILE",
    "RISK_FACTS_PLACEMENT", "RISK_PARAMETERS", "RULES_CHECK", "SUMMARY", "TICKERS", "TRADE_PREFIX", "VOICE_NO_TRADES", "VOICE_PREFIX",
    "WHY_NO_TRADES", "build_rows_by_ref", "date_line_placement", "facts", "given", "money", "no_trade",
    "orphaned", "pnl", "premarket", "reconcile", "summary", "tickers", "trade_block",
    "trade_unit", "voice_unit",
]
