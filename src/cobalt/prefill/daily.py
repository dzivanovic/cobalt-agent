"""Morning Daily Note prefill (Slice 2.1) — a caller of the ONE write
path since 2026-09-03 (LAW L28).

Three slots: a config-driven, mode-aware rules block; the SPY/QQQ/IWM
market table; the market calendar. Each is a marker-bounded section
holding exactly one unit:

    rules            / unit rules
    trading          / unit market_table
    market_calendar  / unit market_calendar

WHAT L28 CHANGED HERE, and why it mattered:

* **The stub-upgrade branch is DELETED.** It used to do
  `existing.split(STUB_BANNER, 1)[1]` and render a fresh template in
  front of the remainder — discarding, unconditionally and silently,
  everything above that banner: frontmatter, journal, plan, Market
  Context, Trade Ideas. It reported `action=upgraded_stub`, exit 0. On
  2026-09-03 the prefix happened to be two lines, so nothing was lost;
  had Dejan typed into the stub before 14:22 it would all have gone.
  Its trigger was worse than the branch: a bare `if STUB_BANNER in
  existing` substring test, matching that line anywhere at any depth
  for the whole life of the note. Both are gone. A note that exists
  ALWAYS takes the merge path now — 05:15 included.
* **Nothing is overwritten.** `create_if_absent` renders the template
  only into a file that does not exist. Every other write is
  `upsert_unit`, which three-way merges: Cobalt's lines update, human
  lines are carried in position, and a human edit to a Cobalt line wins
  and is recorded as an override.
* **A missing anchor is no longer a run failure.** It used to raise
  SlotAnchorNotFound and fail the whole run. Under L28 the section is
  appended at the END of the note instead — nothing above it is
  touched, and the placement used is in the run report.
* **Every write is audited and diffed.** before/after + full-file
  hashes in `vault_writes`, the unified diff in the run report, and
  `--dry-run` on the entrypoint.

Idempotency: a slot Cobalt has already written is skipped (a second run
is a zero-diff no-op). A body carrying a FAILED line from a dead source
is retried, through the merge like any other write. Notes carrying the
PRE-L28 `<!-- cobalt-slot:NAME -->` markers read as already-filled —
historical notes are not retro-marked, and a second copy of a block
Dejan already has is precisely the damage this law exists to prevent.

Market/calendar fetch failures render "FAILED: <reason>" text into the
relevant cells/lines — never blank, never silently guessed.
"""

import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader

from cobalt.aset.config import load_config as load_aset_config
from cobalt.aset.config import load_sheet_modes_config
from cobalt.aset.models import Grade
from cobalt.aset.store import AsetStore
from cobalt.prefill.calendar import (
    EarningsEvent,
    EconomicEvent,
    fetch_earnings_events,
    fetch_economic_events,
)
from cobalt.prefill.config import TEMPLATES_DIR, RuleItem, RulesConfig
from cobalt.prefill.errors import PrefillFetchError
from cobalt.prefill.market import MarketRow, fetch_market_table
from cobalt.prefill.rules_gen import regenerate_rules_config
from cobalt.prefill.vault_writer import read_if_exists, resolve_target
from cobalt.vaultwrite import VaultWriteStore, VaultWriter, WriteResult, after_pattern, wrap_span
from cobalt.vaultwrite.markers import find_section, legacy_slot_present

MARKET_TICKERS = ("SPY", "QQQ", "IWM")
SHEET_MODE_LINE = "Sheet mode: [ ] FULL [ ] HALF — .htk loaded: [ ] full [ ] half"


_GRADE_DOLLAR_RE = re.compile(r"B\s*=\s*\$\d+(?:\.\d+)?,\s*A\s*=\s*\$\d+(?:\.\d+)?")
_WILL_NOT_TOLERATE_LOSSES_RE = re.compile(
    r"^I WILL NOT TOLERATE THE MISTAKE OF HAVING MORE THAN 3 LOSSES IN A ROW IN A TRADING DAY\s*$"
)
_TRADING_HEADING_RE = re.compile(r"^### Trading\s*$")
_MARKET_CALENDAR_HEADING_RE = re.compile(r"^### Market Calendar:?\s*$")
_ANY_HEADING_RE = re.compile(r"^#{1,6}\s")
_BLANK_OR_FAILED_RE = re.compile(r"^\s*(-\s*(FAILED:.*)?)?\s*$")


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
# Slot bodies + placement (LAW L28: markers, never anchors-and-overwrite)
# ---------------------------------------------------------------------------


class SlotAnchorNotFound(RuntimeError):
    """Kept as a type for callers/tests that reference it. It is no longer
    raised: under L28 a missing anchor is not a run failure — the section
    is appended at the END of the note instead, nothing above it touched,
    and the writer reports which placement it used. Guessing an insertion
    point is what the law forbids; appending at the end guesses nothing."""


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


RULES_PLACEMENT = after_pattern(
    _WILL_NOT_TOLERATE_LOSSES_RE,
    "after the second 'I WILL NOT TOLERATE...' line",
)


def _trading_table_span(lines: list[str]) -> Optional[tuple[int, int]]:
    """The contiguous markdown table under '### Trading'. Wrapping it (as
    opposed to inserting beside it) is what lets the merge keep every cell
    Dejan already typed — VIX and BTC are always his."""
    heading = _find_line(lines, _TRADING_HEADING_RE)
    if heading is None:
        return None
    end = _section_end(lines, heading)
    start = None
    for i in range(heading + 1, end):
        if lines[i].lstrip().startswith("|"):
            start = i
            break
    if start is None:
        return None
    stop = start
    while stop < end and lines[stop].lstrip().startswith("|"):
        stop += 1
    return (start, stop)


TRADING_PLACEMENT = wrap_span(_trading_table_span, "the market table under '### Trading'")


def _market_calendar_span(lines: list[str]) -> Optional[tuple[int, int]]:
    """The still-blank body under '### Market Calendar:'. Trailing blank
    lines are left outside the section so the note keeps its spacing."""
    heading = _find_line(lines, _MARKET_CALENDAR_HEADING_RE)
    if heading is None:
        return None
    end = _section_end(lines, heading)
    stop = end
    while stop > heading + 1 and lines[stop - 1].strip() == "":
        stop -= 1
    return (heading + 1, stop)


MARKET_CALENDAR_PLACEMENT = wrap_span(
    _market_calendar_span, "the body under '### Market Calendar:'"
)


def calendar_body_is_available(lines: list[str]) -> bool:
    """True when the Market Calendar body is blank / '-' / a previous
    FAILED line — i.e. Cobalt's to fill. Real human text there means the
    slot is his and is skipped, exactly as before L28."""
    span = _market_calendar_span(lines)
    if span is None:
        return True  # no anchor at all -> the section appends at the end
    return all(_BLANK_OR_FAILED_RE.match(line) for line in lines[span[0] : span[1]])


def build_market_table_body(lines: list[str], row_values: dict[str, tuple[str, str]]) -> str:
    """The market table as Cobalt wants it to read.

    Derived FROM what is on disk, not from the template: only genuinely
    blank SPY/QQQ/IWM cells are filled, so a value Dejan already typed is
    never replaced (and never even reaches the merge as a change). If
    there is no table on disk at all, the three rows are rendered fresh.
    """
    span = _trading_table_span(lines)
    if span is None:
        return "\n".join(
            f"| {t} | {row_values[t][0]} | {row_values[t][1]} |" for t in MARKET_TICKERS
        )
    table = list(lines[span[0] : span[1]])
    for ticker in MARKET_TICKERS:
        row_re = re.compile(_ROW_RE_TEMPLATE.format(ticker=ticker))
        for i, line in enumerate(table):
            m = row_re.match(line)
            if not m:
                continue
            if m.group(1).strip() or m.group(2).strip():
                break  # already filled — his, or an earlier successful run
            col2, col3 = row_values[ticker]
            table[i] = f"| {ticker} | {col2} | {col3} |"
            break
    return "\n".join(table)


_ROW_RE_TEMPLATE = r"^\|\s*{ticker}\s*\|([^|]*)\|([^|]*)\|\s*$"


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


def slot_state(text: str, section: str, unit: str) -> str:
    """"absent" | "filled" | "retry".

    A slot Cobalt already wrote is left alone (that is what makes the
    05:15 job idempotent — a second run is a zero-diff no-op). The one
    exception is a body carrying a FAILED line from a dead data source:
    that is retried, and the retry goes through the merge like any other
    write, so a human note added beside it survives.

    Pre-L28 notes carrying the old `<!-- cobalt-slot:NAME -->` markers
    read as "filled": historical notes are NOT retro-marked, and adding
    a second copy of a block Dejan already has would be the exact class
    of damage this law exists to prevent.
    """
    if legacy_slot_present(text, section):
        return "filled"
    block = find_section(text.split("\n"), section)
    if block is None:
        return "absent"
    unit_block = block.units.get(unit)
    if unit_block is None:
        return "absent"
    body = "\n".join(unit_block.body(text.split("\n")))
    return "retry" if "FAILED" in body else "filled"


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


@dataclass
class DailyPrefillResult:
    path: Path
    action: str  # "created" | "filled" | "skipped_idempotent"
    filled_slots: list[str]
    skipped_slots: list[str]
    writes: list[WriteResult] = field(default_factory=list)
    dry_run: bool = False

    def report(self) -> str:
        """Run report: every unified diff, every override (L28.4)."""
        lines = [
            f"Daily prefill [{'DRY-RUN' if self.dry_run else 'WRITE'}]: {self.action} — {self.path}",
            f"  filled: {', '.join(self.filled_slots) or 'none'}",
            f"  skipped (not touched): {', '.join(self.skipped_slots) or 'none'}",
        ]
        lines.extend(w.report() for w in self.writes)
        return "\n".join(lines)


SLOT_SPECS = (
    # (slot name == section name, unit id, placement)
    ("rules", "rules", RULES_PLACEMENT),
    ("trading", "market_table", TRADING_PLACEMENT),
    ("market_calendar", "market_calendar", MARKET_CALENDAR_PLACEMENT),
)


async def run_daily_prefill(
    when: Optional[datetime] = None, *, dry_run: bool = False
) -> DailyPrefillResult:
    when = when or datetime.now().astimezone()
    aset_cfg = load_aset_config()
    sheet_modes_cfg = load_sheet_modes_config()
    rules_cfg = regenerate_rules_config()

    filename = when.strftime(aset_cfg.daily_note.filename_pattern)
    path = resolve_target(aset_cfg.daily_note.daily_notes_dir, filename)

    store = VaultWriteStore()
    store.ensure_schema()
    writer = VaultWriter("prefill.daily", store=store, dry_run=dry_run)

    # Cheap early exit on the already-filled common case — skip touching
    # the network entirely. Re-read fresh below before acting; this
    # snapshot is ONLY used to decide whether it's worth fetching.
    precheck = read_if_exists(path)
    if precheck is not None and all(
        slot_state(precheck, section, unit) == "filled" for section, unit, _ in SLOT_SPECS
    ):
        return DailyPrefillResult(
            path=path,
            action="skipped_idempotent",
            filled_slots=[],
            skipped_slots=[f"{name} (already filled)" for name, _, _ in SLOT_SPECS],
            dry_run=dry_run,
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
        cards = AsetStore().for_date(when.date())
    except Exception:
        cards = []  # best-effort only — no live "current mode" to show, not a run failure

    context = build_slot_contents(
        when, market_rows, market_error, economic, earnings, calendar_error,
        rules_cfg, sheet_modes_cfg, format_mode_hint(cards),
    )

    # L28.1: a note that does not exist is created whole from the
    # template. A note that DOES exist always takes the merge path below
    # — there is no stub-upgrade branch any more, and no code path that
    # renders a template over an existing file. That branch
    # (`existing.split(STUB_BANNER, 1)[1]`) discarded everything above
    # the banner and is deleted, not repaired.
    created = writer.create_if_absent(path, _render_template(context))
    if created.action == "created":
        return DailyPrefillResult(
            path=path, action="created",
            filled_slots=[name for name, _, _ in SLOT_SPECS], skipped_slots=[],
            writes=[created], dry_run=dry_run,
        )

    existing = read_if_exists(path) or ""
    existing_lines = existing.split("\n")
    row_values = {
        "SPY": (context["spy_col2"], context["spy_col3"]),
        "QQQ": (context["qqq_col2"], context["qqq_col3"]),
        "IWM": (context["iwm_col2"], context["iwm_col3"]),
    }
    bodies = {
        "rules": _rules_slot_content(context),
        "trading": build_market_table_body(existing_lines, row_values),
        "market_calendar": context["market_calendar_block"],
    }

    filled: list[str] = []
    skipped: list[str] = []
    writes: list[WriteResult] = []
    for section, unit, placement in SLOT_SPECS:
        state = slot_state(existing, section, unit)
        if state == "filled":
            skipped.append(f"{section} (already filled)")
            continue
        if section == "market_calendar" and state == "absent" and not calendar_body_is_available(
            existing_lines
        ):
            skipped.append("market_calendar (his content — not touched)")
            continue
        result = writer.upsert_unit(path, section, unit, bodies[section], placement=placement)
        writes.append(result)
        if result.action in ("updated", "created"):
            filled.append(section if state == "absent" else f"{section} (retried)")
        else:
            skipped.append(f"{section} ({result.action})")

    action = "filled" if filled else "skipped_idempotent"
    return DailyPrefillResult(
        path=path, action=action, filled_slots=filled, skipped_slots=skipped,
        writes=writes, dry_run=dry_run,
    )
