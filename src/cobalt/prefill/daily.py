"""Morning Daily Note prefill (Slice 2.1, corrected 2026-08-31 from
Dejan's review of the first live note): market table (SPY/QQQ/IWM
only), market calendar, and a config-driven, mode-aware rules block —
all filled IN PLACE inside Dejan's actual section layout, never
appended below it.

PRINCIPLE (never modify existing note content): if today's note
doesn't exist yet, render the full Jinja template (configs/cobalt/
templates/daily.md.j2) and create it — every Cobalt slot is filled,
each wrapped in its own `<!-- cobalt-slot:NAME -->...<!-- /cobalt-slot:
NAME -->` marker. If the note already exists (Templater got there
first, or a prior prefill run already created it), each of the three
slots is handled independently:
  - marker already present anywhere in the file -> already handled,
    skip, report.
  - marker absent -> the slot's value is empty/still-blank (or a prior
    unmarked FAILED attempt, retryable) -> fill it in place and add the
    marker.
  - marker absent but the slot already holds real (non-blank, non-
    FAILED) content -> that's Dejan's, or an already-successful run
    predating markers -> skip, report, no marker added (leaves the
    door open for a later run if it's ever cleared).
A slot whose anchor (the fixed heading/line Cobalt looks for) can't be
found at all fails the WHOLE run loudly rather than guessing where to
insert — the edit plan is built entirely in memory first, so a failure
never leaves a partially-edited file on disk.

Market/calendar fetch failures render "FAILED: <reason>" text into the
relevant cells/lines (never blank, never silently guessed) and are
deliberately left UNMARKED so a later run retries them.
"""

import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader

from cobalt.aset.config import load_config as load_aset_config, load_sheet_modes_config
from cobalt.aset.models import Grade
from cobalt.aset.store import AsetStore
from cobalt.prefill.calendar import EarningsEvent, EconomicEvent, fetch_earnings_events, fetch_economic_events
from cobalt.prefill.config import RuleItem, RulesConfig, TEMPLATES_DIR
from cobalt.prefill.errors import PrefillFetchError
from cobalt.prefill.market import MarketRow, fetch_market_table
from cobalt.prefill.rules_gen import regenerate_rules_config
from cobalt.prefill.vault_writer import read_if_exists, resolve_target, write_new

MARKET_TICKERS = ("SPY", "QQQ", "IWM")
SHEET_MODE_LINE = "Sheet mode: [ ] FULL [ ] HALF — .htk loaded: [ ] full [ ] half"

SLOT_NAMES = ("rules", "trading", "market_calendar")

_GRADE_DOLLAR_RE = re.compile(r"B\s*=\s*\$\d+(?:\.\d+)?,\s*A\s*=\s*\$\d+(?:\.\d+)?")
_WILL_NOT_TOLERATE_LOSSES_RE = re.compile(
    r"^I WILL NOT TOLERATE THE MISTAKE OF HAVING MORE THAN 3 LOSSES IN A ROW IN A TRADING DAY\s*$"
)
_TRADING_HEADING_RE = re.compile(r"^### Trading\s*$")
_MARKET_CALENDAR_HEADING_RE = re.compile(r"^### Market Calendar:?\s*$")
_ANY_HEADING_RE = re.compile(r"^#{1,6}\s")
_BLANK_OR_FAILED_RE = re.compile(r"^\s*(-\s*(FAILED:.*)?)?\s*$")


def _slot_marker(name: str) -> str:
    return f"<!-- cobalt-slot:{name} -->"


def _slot_marker_close(name: str) -> str:
    return f"<!-- /cobalt-slot:{name} -->"


# ---------------------------------------------------------------------------
# Content builders (shared by the fresh-template render and the in-place fill)
# ---------------------------------------------------------------------------


def format_market_row(ticker: str, rows: Optional[list[MarketRow]], error: Optional[str]) -> tuple[str, str]:
    """(col2, col3) for one of SPY/QQQ/IWM. FAILED text on fetch failure,
    never blank — VIX/BTC are handled nowhere in this module (Dejan's,
    always, per the template's own blank cells)."""
    if error is not None:
        return "FAILED", ""
    row = next((r for r in (rows or []) if r.ticker == ticker), None)
    if row is None:
        return "FAILED", ""
    return f"${row.price:.2f}", f"{row.change_pct:+.2f}%"


def format_calendar_block(
    economic: Optional[list[EconomicEvent]],
    earnings: Optional[list[EarningsEvent]],
    error: Optional[str],
) -> str:
    if error is not None:
        return f"- FAILED: {error}"

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
        return "- (none scheduled)"
    lines.sort(key=lambda line: line[2:7])  # sort by the "HH:MM" that follows "- "
    return "\n".join(lines)


def format_sizing_rule_text(text: str, sheet_modes_cfg) -> str:
    """Splice a mode-aware grade/dollar clause into whichever rule text
    matches the "B = $N, A = $N" shape — content-detected, not tied to a
    rule id/position, so it still finds the right line if Rules.md gets
    reordered. Every other rule's text is untouched."""
    if not _GRADE_DOLLAR_RE.search(text):
        return text
    half_b = int(sheet_modes_cfg.dollars_for("half", Grade.B))
    full_b = int(sheet_modes_cfg.dollars_for("full", Grade.B))
    half_a = int(sheet_modes_cfg.dollars_for("half", Grade.A))
    full_a = int(sheet_modes_cfg.dollars_for("full", Grade.A))
    replacement = f"B = ${half_b} half / ${full_b} full, A = ${half_a} half / ${full_a} full"
    return _GRADE_DOLLAR_RE.sub(replacement, text, count=1)


def apply_mode_aware_sizing(rules: list[RuleItem], sheet_modes_cfg) -> list[RuleItem]:
    return [r.model_copy(update={"text": format_sizing_rule_text(r.text, sheet_modes_cfg)}) for r in rules]


def format_rules_checkbox_block(rules: list[RuleItem]) -> str:
    """The 12 rules render exactly once, as a single tagged checkbox
    list — the rules ARE the adherence boxes (SLICE 2.1). No separate
    read-only list, no separate adherence list."""
    return "\n".join(f"- [ ] {r.text} #{r.category}" for r in rules)


def format_mantras_block(rules_cfg: RulesConfig) -> str:
    return "\n".join(f"- {m.text}" for m in rules_cfg.mantras)


def format_mode_hint(cards: list[dict]) -> str:
    """If aset exposes the current mode at run time (today's cards are
    the only real "current mode" signal aset has — there's no separate
    live mode field anywhere), show it beside the checkboxes. Empty
    string (no hint) when there are no cards yet — true most mornings
    at 05:15, before the market opens."""
    if not cards:
        return ""
    mode = cards[-1].get("sheet_mode")
    if not mode:
        return ""
    return f" (today's most recent card: {mode.upper()})"


def build_slot_contents(
    when: datetime,
    market_rows: Optional[list[MarketRow]],
    market_error: Optional[str],
    economic: Optional[list[EconomicEvent]],
    earnings: Optional[list[EarningsEvent]],
    calendar_error: Optional[str],
    rules_cfg: RulesConfig,
    sheet_modes_cfg,
    mode_hint: str,
) -> dict:
    mode_aware_rules = apply_mode_aware_sizing(rules_cfg.rules, sheet_modes_cfg)
    spy_col2, spy_col3 = format_market_row("SPY", market_rows, market_error)
    qqq_col2, qqq_col3 = format_market_row("QQQ", market_rows, market_error)
    iwm_col2, iwm_col3 = format_market_row("IWM", market_rows, market_error)
    return {
        "date_str": when.strftime("%Y-%m-%d"),
        "time_str": when.strftime("%H:%M"),
        "rules_checkbox_block": format_rules_checkbox_block(mode_aware_rules),
        "mantras_block": format_mantras_block(rules_cfg),
        "mode_hint": mode_hint,
        "sheet_mode_line": SHEET_MODE_LINE + mode_hint,
        "spy_col2": spy_col2, "spy_col3": spy_col3,
        "qqq_col2": qqq_col2, "qqq_col3": qqq_col3,
        "iwm_col2": iwm_col2, "iwm_col3": iwm_col3,
        "market_calendar_block": format_calendar_block(economic, earnings, calendar_error),
    }


def _render_template(context: dict) -> str:
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), keep_trailing_newline=True)
    template = env.get_template("daily.md.j2")
    return template.render(**context)


# ---------------------------------------------------------------------------
# Fill-in-place editing of an existing note
# ---------------------------------------------------------------------------


class SlotAnchorNotFound(RuntimeError):
    """An existing note doesn't have a slot's expected anchor line/heading
    — its shape doesn't match what Cobalt expects. Fail loud rather than
    guess an insertion point."""


@dataclass
class SlotFillPlan:
    filled: list[str] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)


def _find_line(lines: list[str], pattern: re.Pattern) -> Optional[int]:
    for i, line in enumerate(lines):
        if pattern.match(line):
            return i
    return None


def _section_end(lines: list[str], start: int) -> int:
    for i in range(start + 1, len(lines)):
        if _ANY_HEADING_RE.match(lines[i]):
            return i
    return len(lines)


def _fill_rules_slot(lines: list[str], content: str, plan: SlotFillPlan) -> list[str]:
    marker = _slot_marker("rules")
    if any(marker in line for line in lines):
        plan.skipped.append("rules (already filled)")
        return lines

    anchor = _find_line(lines, _WILL_NOT_TOLERATE_LOSSES_RE)
    if anchor is None:
        raise SlotAnchorNotFound(
            "rules slot: couldn't find the second 'I WILL NOT TOLERATE...' line to insert after."
        )
    insertion = ["", marker, content, _slot_marker_close("rules")]
    plan.filled.append("rules")
    return lines[: anchor + 1] + insertion + lines[anchor + 1 :]


_ROW_RE_TEMPLATE = r"^\|\s*{ticker}\s*\|([^|]*)\|([^|]*)\|\s*$"


def _fill_trading_slot(lines: list[str], row_values: dict[str, tuple[str, str]], plan: SlotFillPlan) -> list[str]:
    marker = _slot_marker("trading")
    if any(marker in line for line in lines):
        plan.skipped.append("trading (already filled)")
        return lines

    heading = _find_line(lines, _TRADING_HEADING_RE)
    if heading is None:
        raise SlotAnchorNotFound("trading slot: couldn't find the '### Trading' heading.")
    end = _section_end(lines, heading)

    any_filled = False
    out = list(lines)
    for ticker in MARKET_TICKERS:
        row_re = re.compile(_ROW_RE_TEMPLATE.format(ticker=ticker))
        row_idx = None
        for i in range(heading, end):
            if row_re.match(out[i]):
                row_idx = i
                break
        if row_idx is None:
            raise SlotAnchorNotFound(f"trading slot: couldn't find the {ticker} row under '### Trading'.")
        m = row_re.match(out[row_idx])
        col2, col3 = m.group(1), m.group(2)
        if col2.strip() or col3.strip():
            plan.skipped.append(f"trading:{ticker} (already filled)")
            continue
        new_col2, new_col3 = row_values[ticker]
        out[row_idx] = f"| {ticker} | {new_col2} | {new_col3} |"
        plan.filled.append(f"trading:{ticker}")
        any_filled = True

    if not any_filled:
        return lines  # nothing written -> no marker (see module docstring)

    out = out[: heading + 1] + [marker] + out[heading + 1 : end] + [_slot_marker_close("trading")] + out[end:]
    return out


def _fill_market_calendar_slot(lines: list[str], content: str, plan: SlotFillPlan) -> list[str]:
    marker = _slot_marker("market_calendar")
    if any(marker in line for line in lines):
        plan.skipped.append("market_calendar (already filled)")
        return lines

    heading = _find_line(lines, _MARKET_CALENDAR_HEADING_RE)
    if heading is None:
        raise SlotAnchorNotFound("market_calendar slot: couldn't find the '### Market Calendar:' heading.")
    end = _section_end(lines, heading)
    body_lines = lines[heading + 1 : end]

    if not all(_BLANK_OR_FAILED_RE.match(line) for line in body_lines):
        plan.skipped.append("market_calendar (already filled)")
        return lines

    plan.filled.append("market_calendar")
    new_body = [marker, content, _slot_marker_close("market_calendar")]
    return lines[: heading + 1] + new_body + lines[end:]


def _fill_all_slots(existing_text: str, slots: dict) -> tuple[str, SlotFillPlan]:
    lines = existing_text.split("\n")
    plan = SlotFillPlan()
    lines = _fill_rules_slot(lines, slots["rules_content"], plan)
    lines = _fill_trading_slot(lines, slots["row_values"], plan)
    lines = _fill_market_calendar_slot(lines, slots["market_calendar_block"], plan)
    return "\n".join(lines), plan


def _all_markers_present(text: str) -> bool:
    return all(_slot_marker(name) in text for name in SLOT_NAMES)


def _rules_slot_content(context: dict) -> str:
    return "\n".join(
        [
            context["rules_checkbox_block"],
            "",
            context["sheet_mode_line"],
            "",
            context["mantras_block"],
        ]
    )


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


@dataclass
class DailyPrefillResult:
    path: Path
    action: str  # "created" | "filled" | "skipped_idempotent"
    filled_slots: list[str]
    skipped_slots: list[str]


async def run_daily_prefill(when: Optional[datetime] = None) -> DailyPrefillResult:
    when = when or datetime.now().astimezone()
    aset_cfg = load_aset_config()
    sheet_modes_cfg = load_sheet_modes_config()
    rules_cfg = regenerate_rules_config()

    filename = when.strftime(aset_cfg.daily_note.filename_pattern)
    path = resolve_target(aset_cfg.daily_note.daily_notes_dir, filename)
    existing = read_if_exists(path)

    if existing is not None and _all_markers_present(existing):
        return DailyPrefillResult(
            path=path,
            action="skipped_idempotent",
            filled_slots=[],
            skipped_slots=[f"{name} (already filled)" for name in SLOT_NAMES],
        )

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

    cards: list[dict] = []
    try:
        store = AsetStore(aset_cfg.db_name)
        cards = store.for_date(when.date())
    except Exception:
        cards = []  # best-effort only — no live "current mode" to show, not a run failure

    mode_hint = format_mode_hint(cards)
    context = build_slot_contents(
        when, market_rows, market_error, economic, earnings, calendar_error,
        rules_cfg, sheet_modes_cfg, mode_hint,
    )

    if existing is None:
        write_new(path, _render_template(context))
        return DailyPrefillResult(
            path=path, action="created",
            filled_slots=list(SLOT_NAMES), skipped_slots=[],
        )

    row_values = {
        "SPY": (context["spy_col2"], context["spy_col3"]),
        "QQQ": (context["qqq_col2"], context["qqq_col3"]),
        "IWM": (context["iwm_col2"], context["iwm_col3"]),
    }
    slots = {
        "rules_content": _rules_slot_content(context),
        "row_values": row_values,
        "market_calendar_block": context["market_calendar_block"],
    }
    new_text, plan = _fill_all_slots(existing, slots)
    if new_text != existing:
        path.write_text(new_text, encoding="utf-8")

    action = "filled" if plan.filled else "skipped_idempotent"
    return DailyPrefillResult(path=path, action=action, filled_slots=plan.filled, skipped_slots=plan.skipped)
