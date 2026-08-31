"""Morning Daily Note prefill (Slice 2, item 2): market table, market
calendar, config-driven rules block, sheet-mode line, and a rule-
adherence checklist. Journal / temp-check / 1% goal / Trade Ideas /
Trade Execution stay exactly as Dejan's template has them — Cobalt never
touches those.

PRINCIPLE (never modify existing note content): if today's note doesn't
exist yet, render the full Jinja template (configs/cobalt/templates/
daily.md.j2) and create it. If it already exists — Templater got there
first, or a prior prefill run already created it — append a clearly
fenced "Cobalt Rules Check" block instead, guarded by an idempotency
marker HTML comment so a second run the same day is a no-op, not a
duplicate append.
"""

from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader

from cobalt.aset.config import load_config as load_aset_config
from cobalt.prefill.calendar import EarningsEvent, EconomicEvent, fetch_earnings_events, fetch_economic_events
from cobalt.prefill.config import RulesConfig, TEMPLATES_DIR, load_rules_config
from cobalt.prefill.errors import PrefillFetchError
from cobalt.prefill.market import MarketRow, UNSERVABLE, fetch_market_table
from cobalt.prefill.vault_writer import append_block, read_if_exists, resolve_target, write_new

MANUAL_TICKERS = ("VIX", "BTC")
SHEET_MODE_LINE = "Sheet mode: [ ] FULL [ ] HALF — .htk loaded: [ ] full [ ] half"


def _idempotency_marker(for_date: date) -> str:
    return f"<!-- cobalt-prefill:daily:{for_date.isoformat()} -->"


def format_market_cells(
    rows: Optional[list[MarketRow]], error: Optional[str]
) -> dict[str, str]:
    cells: dict[str, str] = {}
    for ticker in MANUAL_TICKERS:
        cells[f"{ticker.lower()}_col2"] = UNSERVABLE[ticker].split(" — ")[0]
        cells[f"{ticker.lower()}_col3"] = ""

    if rows is not None:
        for row in rows:
            key = row.ticker.lower()
            cells[f"{key}_col2"] = f"${row.price:.2f}"
            cells[f"{key}_col3"] = f"{row.change_pct:+.2f}%"
        cells["market_error"] = ""
    else:
        for ticker in ("spy", "qqq", "iwm"):
            cells[f"{ticker}_col2"] = "FAILED"
            cells[f"{ticker}_col3"] = ""
        cells["market_error"] = error or "unknown error"
    return cells


def format_calendar_block(
    economic: Optional[list[EconomicEvent]],
    earnings: Optional[list[EarningsEvent]],
    error: Optional[str],
) -> str:
    if error is not None:
        return f"- FAILED: {error}\n"

    lines: list[str] = []
    for e in economic or []:
        detail = []
        if e.impact:
            detail.append(f"impact {e.impact}")
        if e.expected:
            detail.append(f"expected {e.expected}")
        if e.prior:
            detail.append(f"prior {e.prior}")
        suffix = f" ({', '.join(detail)})" if detail else ""
        lines.append(f"- {e.time} ET — {e.event}{suffix}")
    for e in earnings or []:
        lines.append(f"- {e.time} ET — {e.ticker} earnings ({e.company})")

    if not lines:
        return "- (none scheduled)\n"
    lines.sort(key=lambda line: line[2:7])  # sort by the "HH:MM" that follows "- "
    return "\n".join(lines) + "\n"


def format_rules_blocks(rules_cfg: RulesConfig) -> tuple[str, str, str]:
    rules_block = "\n".join(f"- [{r.category}] {r.text}" for r in rules_cfg.rules) + "\n"
    adherence_block = "\n".join(f"- [ ] {r.text}" for r in rules_cfg.rules) + "\n"
    mantras_block = "\n".join(f"- {m.text}" for m in rules_cfg.mantras) + "\n"
    return rules_block, adherence_block, mantras_block


def build_context(
    when: datetime,
    market_rows: Optional[list[MarketRow]],
    market_error: Optional[str],
    economic: Optional[list[EconomicEvent]],
    earnings: Optional[list[EarningsEvent]],
    calendar_error: Optional[str],
    rules_cfg: RulesConfig,
) -> dict:
    rules_block, adherence_block, mantras_block = format_rules_blocks(rules_cfg)
    context = {
        "date_str": when.strftime("%Y-%m-%d"),
        "time_str": when.strftime("%H:%M"),
        "market_calendar_block": format_calendar_block(economic, earnings, calendar_error),
        "rules_block": rules_block,
        "rule_adherence_block": adherence_block,
        "mantras_block": mantras_block,
    }
    context.update(format_market_cells(market_rows, market_error))
    return context


def _render_template(context: dict) -> str:
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), keep_trailing_newline=True)
    template = env.get_template("daily.md.j2")
    return template.render(**context)


def _render_append_block(when: datetime, context: dict) -> str:
    marker = _idempotency_marker(when.date())
    lines = [
        "",
        f"## Cobalt Prefill — {when:%H:%M:%S}",
        marker,
        "",
        "### Market",
        f"| VIX | {context['vix_col2']} | {context['vix_col3']} |",
        f"| SPY | {context['spy_col2']} | {context['spy_col3']} |",
        f"| QQQ | {context['qqq_col2']} | {context['qqq_col3']} |",
        f"| IWM | {context['iwm_col2']} | {context['iwm_col3']} |",
        f"| BTC | {context['btc_col2']} | {context['btc_col3']} |",
    ]
    if context.get("market_error"):
        lines.append(f"> ⚠️ Market fetch FAILED: {context['market_error']}")
    lines += [
        "",
        "### Market Calendar",
        context["market_calendar_block"].rstrip("\n"),
        "",
        SHEET_MODE_LINE,
        "",
        "**Guardian rules (configs/cobalt/rules.yaml):**",
        context["rules_block"].rstrip("\n"),
        "",
        "**Rule adherence (check off through the day):**",
        context["rule_adherence_block"].rstrip("\n"),
        "",
        "**Mantras:**",
        context["mantras_block"].rstrip("\n"),
        "",
    ]
    return "\n".join(lines)


@dataclass
class DailyPrefillResult:
    path: Path
    action: str  # "created" | "appended" | "skipped_idempotent"


async def run_daily_prefill(when: Optional[datetime] = None) -> DailyPrefillResult:
    when = when or datetime.now().astimezone()
    aset_cfg = load_aset_config()
    rules_cfg = load_rules_config()

    market_rows: Optional[list[MarketRow]] = None
    market_error: Optional[str] = None
    try:
        market_rows = await fetch_market_table()
    except PrefillFetchError as e:
        market_error = str(e)

    economic: Optional[list[EconomicEvent]] = None
    earnings: Optional[list[EarningsEvent]] = None
    calendar_error: Optional[str] = None
    try:
        economic = await fetch_economic_events(when.date())
        earnings = await fetch_earnings_events(when.date())
    except PrefillFetchError as e:
        calendar_error = str(e)

    context = build_context(
        when, market_rows, market_error, economic, earnings, calendar_error, rules_cfg
    )

    filename = when.strftime(aset_cfg.daily_note.filename_pattern)
    path = resolve_target(aset_cfg.daily_note.daily_notes_dir, filename)
    existing = read_if_exists(path)

    if existing is None:
        write_new(path, _render_template(context))
        return DailyPrefillResult(path=path, action="created")

    marker = _idempotency_marker(when.date())
    if marker in existing:
        return DailyPrefillResult(path=path, action="skipped_idempotent")

    append_block(path, _render_append_block(when, context))
    return DailyPrefillResult(path=path, action="appended")
