"""Morning Daily Note prefill (Slice 2.1) — a caller of the ONE write
path since 2026-09-03 (LAW L28).

Four slots (`SLOT_SPECS`): a config-driven, mode-aware rules block; the
day-mode unit; the SPY/QQQ/IWM market table; the market calendar. Each
is a marker-bounded section holding exactly one unit:

    rules            / unit rules
    daymode          / unit sheet_mode
    trading          / unit market_table
    market_calendar  / unit market_calendar

F4 (2026-10-10, F4 FINAL F4-1): `run_daily_refresh` re-renders the
trading and calendar units all day (`prefill refresh`), and every Cobalt
block carries an `as of HH:MM ET` stamp. See the F4 section at the
bottom of this module.

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

import asyncio
import hashlib
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Optional

from jinja2 import Environment, FileSystemLoader
from loguru import logger

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
from cobalt.prefill.config import (
    REFRESH_FIELDS,
    TEMPLATES_DIR,
    DailyRefreshConfig,
    GeneratedMeta,
    PrefillConfigError,
    RuleItem,
    RulesConfig,
    load_daily_refresh_config,
)
from cobalt.prefill.errors import PrefillFetchError
from cobalt.prefill.market import MarketRow, fetch_market_table
from cobalt.prefill.rules_gen import RULES_MD_RELATIVE_PATH, RulesSourceError, _parse_rules_md, regenerate_rules_config
from cobalt.prefill.vault_writer import read_if_exists, resolve_dir, resolve_target
from cobalt.radar.collector import SourceFailure, radar_bucket_rpm
from cobalt.radar.notes import (
    DemandConsumer,
    DemandWindow,
    RadarNoteError,
    TotalDemandExceeded,
    check_scheduled_demand,
)
from cobalt.session import SessionClock
from cobalt.settings.drc import NOT_GIVEN, DailyRisk, daily_risk_values
from cobalt.strike.detector import DemandPlan, read_plan
from cobalt.vaultwrite import (
    NoteChangedOnDisk,
    VaultWriteStore,
    VaultWriter,
    WriteResult,
    after_pattern,
    sha256_text,
    wrap_span,
)
from cobalt.vaultwrite.markers import find_section, legacy_slot_present

MARKET_TICKERS = ("SPY", "QQQ", "IWM")

#: DELETED 2026-09-04 (S1-P3, CTO review of S1-P2). `SHEET_MODE_LINE`
#: used to live here:
#:
#:     "Sheet mode: [ ] FULL [ ] HALF — .htk loaded: [ ] full [ ] half"
#:
#: — four checkboxes that read nothing, compared nothing and refused
#: nothing. It is replaced by a Cobalt-OWNED UNIT (L28) rendered by
#: `cobalt.daymode.note`, which carries the decided day mode and the
#: attestation and is read back at the next sheet request. One owner,
#: one renderer: this module calls that one rather than carrying a
#: second copy of the words (one-path rule).


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


def format_daily_stop(risk: Optional[DailyRisk], error: Optional[str] = None) -> str:
    """The template's `Daily HARD Stop:` value (DRC D4-3, R95 / R102).

    The number used to be typed into the committed template — his value in
    git, and a second place beside the settings. It now comes from the ONE
    reader (`cobalt.settings.drc`), per sheet: `full $X · half $Y`, and an
    absent key reads `not given` — never the old literal, never a blank
    that looks like a number. A failed read renders FAILED, never blank."""
    if error is not None or risk is None:
        return f"FAILED: {error or 'the daily stop was not read'}"
    return " · ".join(
        f"{sheet} {NOT_GIVEN if value is None else f'${value}'}"
        for sheet, value in risk.daily_stop.items()
    )


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
    sheet_mode_block: str,
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
        "sheet_mode_block": sheet_mode_block,
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


_RULES_SECTION_CLOSE_RE = re.compile(r"^\s*<!--\s*/cobalt:section\s+rules\s*-->\s*$")

DAYMODE_PLACEMENT = after_pattern(
    _RULES_SECTION_CLOSE_RE, "after the rules section's closing marker"
)


def _rules_slot_content(context: dict) -> str:
    return "\n".join(
        [
            context["rules_stamp"],  # F4 [F-30]: create and absent-slot fill only
            "",
            context["rules_checkbox_block"],
            "",
            context["mantras_block"],
        ]
    )


def build_sheet_mode_block(when: datetime) -> str:
    """Today's day-mode block, rendered by its OWNER (`daymode.note`).

    `when` is the create's aware instant: the ET day it reads and the
    `as of` stamp it renders, never the wall clock (check A4).

    Fail-soft ONLY in the sense L28 allows: a config or database failure
    renders as a visible FAILED line in the note rather than taking the
    whole 05:15 run down, because the market table and the calendar are
    still worth having. It is never blank and never guessed.
    """
    from cobalt.daymode import note as daymode_note
    from cobalt.daymode.config import load_daymode_config
    from cobalt.daymode.propose import decided_or_stage1
    from cobalt.daymode.store import DayModeStore

    try:
        cfg = load_daymode_config()
        day = SessionClock.to_et(when).date()
        try:
            store = DayModeStore()
            store.ensure_schema()
            row = store.for_date(day)
        except Exception as e:  # noqa: BLE001 - reported in the note, not swallowed
            logger.error("daymode block: day_modes unreadable ({}) — stage 1 rendered", e)
            row = None
        mode = decided_or_stage1(row, cfg)
        stage = (
            "stage 2 (decided)"
            if (row or {}).get("decided")
            else "stage 1 (system rule, pre-09:00)"
        )
        return daymode_note.render_body(
            cfg, mode, stage=stage, attested=(row or {}).get("attested_sheet"), row=row, when=when
        )
    except Exception as e:  # noqa: BLE001
        return f"- FAILED: day mode unresolved ({type(e).__name__}: {e})"


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
class _Fetched:
    """The Finviz reads of one run: the screener and the two calendar
    requests (`test_finviz_consumers.py:47-48`). `refused` is set when the
    shared gate refused the run, and then nothing was requested."""

    market_rows: Optional[list[MarketRow]] = None
    market_error: Optional[str] = None
    economic: Optional[list[EconomicEvent]] = None
    earnings: Optional[list[EarningsEvent]] = None
    calendar_error: Optional[str] = None
    refused: Optional[str] = None


async def _fetch(day) -> _Fetched:
    fetched = _Fetched()
    try:
        fetched.market_rows = await fetch_market_table()
    except PrefillFetchError as e:
        fetched.market_error = str(e)
    try:
        fetched.economic = await fetch_economic_events(day)
        fetched.earnings = await fetch_earnings_events(day)
    except PrefillFetchError as e:
        fetched.calendar_error = str(e)
    return fetched


def build_create_context(when: datetime, fetched: _Fetched, rules_cfg: RulesConfig) -> dict:
    """The whole-note template context — the ONE create render, shared by
    `prefill daily` and `prefill refresh` (F4 [F-01]). `when` is aware: the
    header, the stamps and the calendar day are ET (`SessionClock.to_et`).
    The ONE call of the sheet loader in this module (D4 fix r1 F-4)."""
    et = SessionClock.to_et(when)
    sheet_modes_cfg = load_sheet_modes_config()
    cards: list[dict] = []
    try:
        cards = AsetStore().for_date(et.date())
    except Exception:
        cards = []  # best-effort only — no live "current mode" to show, not a run failure

    context = build_slot_contents(
        et, fetched.market_rows, fetched.market_error, fetched.economic, fetched.earnings,
        fetched.calendar_error, rules_cfg, sheet_modes_cfg, format_mode_hint(cards),
        build_sheet_mode_block(when),
    )
    # DRC D4-3: the daily stop, from the one reader. Fail-soft in the L28
    # sense only: a settings failure is a visible FAILED line in the new
    # note, not a lost 05:15 run.
    try:
        context["daily_stop"] = format_daily_stop(daily_risk_values())
    except Exception as e:  # noqa: BLE001 - rendered in the note, never swallowed
        logger.error("daily prefill: the daily stop was not read ({})", type(e).__name__)
        context["daily_stop"] = format_daily_stop(None, f"daily stop unreadable ({type(e).__name__}: {e})")
    context.update(stamp_context(when, fetched.market_rows, fetched.market_error, fetched.calendar_error))
    return context


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
    # S1-P3: the day-mode unit. It sits right after the rules section
    # when the note already exists and has no daymode markers yet;
    # `daymode.note.write()` updates it in place from then on (the sheet,
    # the 09:00 proposal and an attestation all call that one writer).
    ("daymode", "sheet_mode", DAYMODE_PLACEMENT),
    ("trading", "market_table", TRADING_PLACEMENT),
    ("market_calendar", "market_calendar", MARKET_CALENDAR_PLACEMENT),
)


async def run_daily_prefill(
    when: Optional[datetime] = None, *, dry_run: bool = False
) -> DailyPrefillResult:
    when = when or datetime.now().astimezone()
    aset_cfg = load_aset_config()
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

    fetched = await _fetch(when.date())
    context = build_create_context(when, fetched, rules_cfg)

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
        "daymode": context["sheet_mode_block"],
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


# ---------------------------------------------------------------------------
# F4 — prefill all day, ownership flags (F4 FINAL F4-1, 2026-10-10)
#
# `prefill refresh` re-renders `trading/market_table` and
# `market_calendar/market_calendar` (`daily_refresh.units`), never another
# unit. His text is never touched: ownership is decided INSIDE
# `upsert_unit`, on every write attempt (`body_fn`, [F-26]), from that
# attempt's snapshot and the baseline read in the same call. The proposal
# is built from `last_after`, never from the disk, so `merge3` carries his
# insertions once and at their anchors. Refresh never calls
# `regenerate_rules_config`, `load_rules_config` or `run_daily_prefill`
# ([F-01], [F-08], [F-35]); its Finviz reads go through the one shared
# gate, form B (R2-4, §8 R4); a dead source keeps the last values, flags
# them `cobalt-degraded` and exits nonzero ([F-28]).
# ---------------------------------------------------------------------------

REFRESH_WRITER = "prefill.refresh"
#: Refresh's name in the L53 shared gate. Passed as `extra`, never listed in
#: `scheduled_consumers` (form B).
REFRESH_SUBJECT = "prefill-refresh"
#: One screener + two calendar requests a run (`test_finviz_consumers.py:47-48`).
REFRESH_GETS = 3
REFRESH_INTERVAL_KEY = "prefill.refresh_interval_min"
REFRESH_WINDOW_KEY = "prefill.refresh_window"
MANUAL_NA = "n/a (manual)"

_STAMP_RE = re.compile(r"^as of (\d\d:\d\d) ET")
#: The whole machine status line `format_flag_line` writes, every flag one
#: of the values a run emits — never his free-typed stamp (fix round, X12).
_FLAG_VALUE = r"(?:cobalt|human|absent|n/a \(manual\)|cobalt-degraded \([^()]*\))"
_MACHINE_STAMP_RE = re.compile(
    r"^as of \d\d:\d\d ET"
    + "".join(f" · {f} {_FLAG_VALUE}" for f in REFRESH_FIELDS)
    + f" · calendar {_FLAG_VALUE}$"
)
_FIELD_ROW_RE = re.compile(r"^\|\s*([A-Za-z]+)\s*\|")
_FETCH_FAILED = "finviz fetch failed"
_GATE_REFUSED = "finviz demand refused"


class RefreshError(RuntimeError):
    """A refresh attempt found the note in a shape it may not write — refuse."""


def format_stamp(when: datetime) -> str:
    """`as of HH:MM ET` (SEAM §2, F5 imports it). ET through
    `SessionClock.to_et`, never the host zone; a naive `when` is refused."""
    return f"as of {SessionClock.to_et(when):%H:%M} ET"


def refresh_note_path(when: datetime) -> Path:
    """Today's ET note: `daymode.note.daily_note_path`, fed the ET date of
    an aware instant ([F-31]); its `date.today()` default is never reached."""
    from cobalt.daymode.note import daily_note_path

    return daily_note_path(SessionClock.to_et(when).date())


def _degraded(reason: str, since: Optional[str]) -> str:
    """No uppercase FAILED: `slot_state` reads that word as "retry"."""
    return f"cobalt-degraded ({reason}; values as of {since or 'unknown'})"


def format_flag_line(stamp: str, flags: dict[str, str]) -> str:
    """`as of 08:45 ET · SPY cobalt · … · BTC n/a (manual) · calendar cobalt`."""
    return " · ".join([stamp, *(f"{f} {flags[f]}" for f in REFRESH_FIELDS), f"calendar {flags['calendar']}"])


def _manual_tickers(cfg: Optional[DailyRefreshConfig]) -> set[str]:
    """SPY/QQQ/IWM set to `manual` in `daily_refresh.fields` (check A1)."""
    return {t for t in MARKET_TICKERS if cfg is not None and cfg.fields[t] == "manual"}


def _create_flags(market_rows, market_error, calendar_error, cfg: Optional[DailyRefreshConfig] = None) -> dict[str, str]:
    got = {r.ticker for r in market_rows or []} if market_error is None else set()
    flags = {t: ("cobalt" if t in got else f"cobalt-degraded ({_FETCH_FAILED}; no values yet)") for t in MARKET_TICKERS}
    flags.update({t: MANUAL_NA for t in _manual_tickers(cfg)})
    flags.update(VIX=MANUAL_NA, BTC=MANUAL_NA)
    flags["calendar"] = "cobalt" if calendar_error is None else f"cobalt-degraded ({_FETCH_FAILED}; no values yet)"
    return flags


def stamp_context(
    when: datetime, market_rows, market_error, calendar_error, cfg: Optional[DailyRefreshConfig] = None
) -> dict:
    """The three stamp lines of a freshly rendered note ([F-27], [F-30])."""
    stamp = format_stamp(when)
    flags = _create_flags(market_rows, market_error, calendar_error, cfg)
    return {
        "rules_stamp": f"{stamp} · rules from Rules.md",
        "trading_stamp": format_flag_line(stamp, flags),
        "calendar_stamp": f"{stamp} · calendar {flags['calendar']}",
    }


# -- the shared Finviz gate, form B -----------------------------------------


def refresh_demand_consumer() -> DemandConsumer:
    """Refresh as ONE `extra` consumer: 3 GETs over the fixed launchd
    interval (`prefill.refresh_interval_min` is the schedule and the floor;
    form B), inside `prefill.refresh_window`."""
    from cobalt.jobs.config import parse_window
    from cobalt.taxonomy.loader import load_tunables

    rows = load_tunables().by_key
    missing = [k for k in (REFRESH_INTERVAL_KEY, REFRESH_WINDOW_KEY) if k not in rows or rows[k].value is None]
    if missing:
        raise PrefillConfigError(f"tunables.yaml: {missing} missing or unmeasured — refresh demand cannot be shown")
    interval = int(rows[REFRESH_INTERVAL_KEY].value)
    opens, closes = parse_window(str(rows[REFRESH_WINDOW_KEY].value), REFRESH_WINDOW_KEY)
    return DemandConsumer(
        name=REFRESH_SUBJECT,
        rpm=REFRESH_GETS / interval,
        window=DemandWindow.between(f"{opens:%H:%M}", f"{closes:%H:%M}"),
        basis=f"{REFRESH_GETS} GETs a refresh (1 screener + 2 calendar) over {REFRESH_INTERVAL_KEY}={interval}",
    )


def check_refresh_demand() -> Optional[str]:
    """None = admitted; else why no Finviz request may be sent this run.

    The plan is the one the strike loop reads (`strike/detector.py:313`).
    No plan, no planned rpm, or no headroom → refused HERE, and the gate is
    NOT called with `radar_rpm=None` (that fallback counts the radar at the
    ceiling, `radar/notes.py:357-363`)."""
    try:
        plan = read_plan()
    except Exception as e:  # noqa: BLE001 - an unreadable plan is a refusal, never a guess
        return f"the radar's plan is unreadable ({type(e).__name__}: {e})"
    if plan.planned_rpm is None or plan.headroom_rpm is None or plan.headroom_rpm <= 0:
        return f"no Finviz headroom (planned_rpm={plan.planned_rpm}, headroom_rpm={plan.headroom_rpm})"
    try:
        check_scheduled_demand(REFRESH_SUBJECT, radar_rpm=plan.planned_rpm, extra=[refresh_demand_consumer()])
    except (TotalDemandExceeded, RadarNoteError) as e:
        return str(e)
    from cobalt.radar import notes

    try:
        radar_cap = radar_bucket_rpm()
    except SourceFailure as e:
        return str(e)
    ceiling = notes._ceiling()
    if ceiling is None:
        return "radar.finviz_max_rpm is unmeasured — the refresh burst cannot be bounded"
    return refresh_burst_refusal(plan, ceiling=ceiling, radar_cap=radar_cap)


def refresh_burst_refusal(plan: DemandPlan, *, ceiling: int, radar_cap: int) -> Optional[str]:
    """His ruling C (2026-10-26, R2512): in refresh's one minute the radar
    sends up to its cap, the strike loop up to its headroom and refresh its
    `REFRESH_GETS`. One comparison of the headroom against the integer
    allowance `ceiling - radar_cap - REFRESH_GETS`, with `radar/notes.py`'s
    tolerance: no float sum lands on the exactly-the-ceiling hazard
    (F4-FINAL X17). None = admitted."""
    allowance = ceiling - radar_cap - REFRESH_GETS
    if plan.headroom_rpm > allowance + 1e-9:
        return (f"the radar's cap, the strike loop at its headroom and refresh's 3 GETs exceed the ceiling in one "
                f"minute: radar.finviz_rpm {radar_cap} + headroom_rpm {plan.headroom_rpm} + REFRESH_GETS "
                f"{REFRESH_GETS} > ceiling {ceiling}")
    return None


async def _gated_fetch(when: datetime) -> _Fetched:
    """The gate BEFORE any GET; a refusal fetches nothing."""
    refusal = check_refresh_demand()
    if refusal is not None:
        logger.error("prefill refresh: no Finviz request this run — {}", refusal)
        return _Fetched(market_error=refusal, calendar_error=refusal, refused=refusal)
    return await _fetch(SessionClock.to_et(when).date())


# -- the create path ([F-08], [F-31]) --------------------------------------


def read_rules_read_only() -> RulesConfig:
    """Rules.md parsed and validated by THE parser (`rules_gen._parse_rules_md`)
    and written NOWHERE — the read-only input [F-08] names. Not
    `regenerate_rules_config` (it writes the generated yaml) and not
    `load_rules_config` (it reads the committed file whatever the env)."""
    relative = Path(RULES_MD_RELATIVE_PATH)
    source = resolve_dir(str(relative.parent)) / relative.name
    if not source.exists():
        raise RulesSourceError(f"Rules.md not found at {source} — the note cannot be created.")
    raw = source.read_text(encoding="utf-8")
    rules, mantras = _parse_rules_md(raw)
    return RulesConfig(
        generated=GeneratedMeta(
            source=str(source),
            source_sha256=hashlib.sha256(raw.encode("utf-8")).hexdigest(),
            generated_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        ),
        rules=rules,
        mantras=mantras,
    )


def _ensure_note(writer: VaultWriter, when: datetime, fetched: Optional[_Fetched]) -> WriteResult:
    SessionClock.to_et(when)  # an aware instant, or a refusal
    path = refresh_note_path(when)
    if path.exists():
        text = path.read_text(encoding="utf-8")
        return WriteResult(
            path=path, action="skipped_exists", dry_run=writer.dry_run,
            hash_before=sha256_text(text), hash_after=sha256_text(text),
            notes=["file exists — ensure_daily_note never replaces it (L28.1)"],
        )
    if fetched is None:
        fetched = asyncio.run(_gated_fetch(when))
    context = build_create_context(when, fetched, read_rules_read_only())
    # Check A1: a ticker `daily_refresh.fields` sets to `manual` is his from
    # the first render — `n/a (manual)`, never the fetched value.
    cfg = load_daily_refresh_config()
    for t in _manual_tickers(cfg):
        context[f"{t.lower()}_col2"] = context[f"{t.lower()}_col3"] = MANUAL_NA
    context.update(stamp_context(when, fetched.market_rows, fetched.market_error, fetched.calendar_error, cfg))
    return writer.create_if_absent(path, _render_template(context))


def ensure_daily_note(writer: VaultWriter, when: datetime) -> WriteResult:
    """SEAM §2 (F5 imports it). Absent note → the shared create-if-absent
    render from read-only inputs, through the caller's (dry-run) writer;
    an existing note → `skipped_exists`, never replaced. No rules
    regeneration, no `run_daily_prefill`."""
    return _ensure_note(writer, when, None)


# -- ownership ([F-26], [F-27]) -----------------------------------------------


def _align(base: list[str], disk: list[str]) -> list[Optional[str]]:
    """For each `last_after` line, the on-disk line in its place (None when
    it is gone): the line is matched, never the ticker."""
    found: list[Optional[str]] = [None] * len(base)
    for tag, i1, i2, j1, j2 in SequenceMatcher(None, base, disk, autojunk=False).get_opcodes():
        if tag in ("equal", "replace"):
            for k in range(min(i2 - i1, j2 - j1)):
                found[i1 + k] = disk[j1 + k]
    return found


def _cells(line: str) -> list[str]:
    return line.split("|")[2:-1]


def _fill_manual(line: str) -> str:
    """A blank VIX/BTC value cell becomes `n/a (manual)`; a typed one stays."""
    parts = line.split("|")
    for i in range(2, len(parts) - 1):
        if parts[i].strip() == "":
            parts[i] = f" {MANUAL_NA} "
    return "|".join(parts)


def _manual_flag(line: str) -> str:
    typed = [c for c in _cells(line) if c.strip() not in ("", MANUAL_NA)]
    return "human" if typed else MANUAL_NA


def _last_success(field_name: str, bodies: list[str]) -> Optional[str]:
    """The `HH:MM` of the last stamp that had `field_name` fresh — read from
    Cobalt's own stamps in `last_after` and `recent_afters`, never from the
    latest attempt's time ([F-28])."""
    degraded = re.compile(rf"^{re.escape(field_name)} cobalt-degraded \(.*; values as of (\d\d:\d\d)\)$")
    for body in bodies:
        first = next((line for line in body.split("\n") if _STAMP_RE.match(line)), None)
        if first is None:
            continue
        for part in first.split(" · ")[1:]:
            if part == f"{field_name} cobalt":
                return _STAMP_RE.match(first).group(1)
            m = degraded.match(part)
            if m:
                return m.group(1)
    return None


def _unit_body(text: str, section: str, unit: str) -> Optional[str]:
    lines = text.split("\n")
    block = find_section(lines, section)
    if block is None or unit not in block.units:
        return None
    return "\n".join(block.units[unit].body(lines))


@dataclass
class RefreshResult:
    path: Path
    dry_run: bool
    stamp: str
    action: str = "refreshed"  # refreshed | created | failed
    writes: list[WriteResult] = field(default_factory=list)
    flags: dict[str, str] = field(default_factory=dict)
    #: The fresh machine status line, ALWAYS in the report — the only place
    #: it lands when his edit owns the in-note stamp ([F-27]).
    status_line: str = ""
    degraded: list[str] = field(default_factory=list)
    failures: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    @property
    def exit_code(self) -> int:
        """Nonzero on any degraded field or failure ([F-28], [F-36+])."""
        return 1 if (self.degraded or self.failures) else 0

    def summary(self) -> str:
        parts = self.failures + [f"degraded: {d}" for d in self.degraded]
        return "; ".join(parts) or "ok"

    def report(self) -> str:
        lines = [
            f"Daily refresh [{'DRY-RUN' if self.dry_run else 'WRITE'}]: {self.action} — {self.path}",
            f"  status: {self.status_line or '(none)'}",
        ]
        lines.extend(f"  {f}" for f in self.failures)
        lines.extend(f"  DEGRADED: {d}" for d in self.degraded)
        lines.extend(f"  NOTE: {n}" for n in self.notes)
        lines.extend(w.report() for w in self.writes)
        return "\n".join(lines)


class _Refresh:
    """One run's ownership decisions, bound to its writer and store."""

    def __init__(self, writer: VaultWriter, store, path: Path, cfg: DailyRefreshConfig, fetched: _Fetched, stamp: str):
        self.writer, self.store, self.path, self.cfg = writer, store, path, cfg
        self.fetched, self.stamp = fetched, stamp
        self.reason = _GATE_REFUSED if fetched.refused else _FETCH_FAILED
        self.state: dict = {}

    def _history(self, section: str, unit: str) -> tuple[Optional[str], list[str]]:
        """`last_after` and the recent afters, read fresh on every call."""
        base = self.writer._baseline(self.path, section, unit)
        recent = [after for _, after in self.store.recent_afters(
            str(self.path), section, unit, limit=self.writer.SYNC_REVERT_WINDOW)]
        return base, recent

    def calendar_owned(self, text: str) -> bool:
        """[F-26] calendar: whole unit, Cobalt's only when the on-disk body
        equals `last_after` or a recent after."""
        body = _unit_body(text, "market_calendar", "market_calendar")
        base, recent = self._history("market_calendar", "market_calendar")
        return body is not None and base is not None and (body == base or body in recent)

    def calendar_body(self) -> str:
        f = self.fetched
        return f"{self.stamp} · calendar cobalt\n\n{format_calendar_block(f.economic, f.earnings, None)}"

    def calendar_degraded(self) -> str:
        base, recent = self._history("market_calendar", "market_calendar")
        return _degraded(self.reason, _last_success("calendar", [b for b in [base, *recent] if b]))

    def trading_in_flight(self, text: str) -> bool:
        """Fix round, X12 (no lock): the trading unit on disk opens with a
        machine status line that no visible `vault_writes` after holds —
        another refresh has replaced the file and its row is not committed
        yet (or was lost). Its rows would read as his, so this attempt
        writes nothing and records no override."""
        disk = _unit_body(text, "trading", "market_table")
        if disk is None:
            return False
        stamp = next((line for line in disk.split("\n") if _STAMP_RE.match(line)), None)
        if stamp is None or not _MACHINE_STAMP_RE.match(stamp):
            return False
        base, recent = self._history("trading", "market_table")
        return not any(stamp in after.split("\n") for after in [base, *recent] if after is not None)

    def fresh_row(self, ticker: str) -> Optional[str]:
        if self.fetched.market_error is not None:
            return None
        row = next((r for r in self.fetched.market_rows or [] if r.ticker == ticker), None)
        return None if row is None else f"| {ticker} | ${row.price:.2f} | {row.change_pct:+.2f}% |"

    def fresh_trading_body(self, calendar_flag: str) -> Optional[str]:
        """The absent unit (a stub): the template's rows, all fresh, or None
        when any Cobalt row has no value (nothing plausible-empty is written)."""
        manual = lambda t: f"| {t} | {MANUAL_NA} | {MANUAL_NA} |"  # noqa: E731
        mine = [t for t in MARKET_TICKERS if self.cfg.fields[t] == "cobalt"]
        rows = {t: (self.fresh_row(t) if t in mine else manual(t)) for t in MARKET_TICKERS}
        if any(v is None for v in rows.values()):
            return None
        flags = {t: ("cobalt" if t in mine else MANUAL_NA) for t in MARKET_TICKERS}
        flags.update(VIX=MANUAL_NA, BTC=MANUAL_NA, calendar=calendar_flag)
        self.state.update(flags=flags, status_line=format_flag_line(self.stamp, flags))
        return "\n".join([
            self.state["status_line"], "",
            manual("VIX"), "| --- | --- | --- |", *(rows[t] for t in MARKET_TICKERS), manual("BTC"),
        ])

    def trading_proposal(self, snapshot, calendar_flag: str) -> str:
        """`body_fn` for `trading/market_table`: called on EVERY attempt."""
        disk_text = _unit_body(snapshot.text or "", "trading", "market_table")
        base_text, recent = self._history("trading", "market_table")
        if disk_text is None or base_text is None:
            raise RefreshError(
                f"FAILED: the trading unit or its baseline vanished between the check and this "
                f"write attempt ({self.path}) — nothing written"
            )
        base = base_text.split("\n") if base_text != "" else []
        disk = disk_text.split("\n") if disk_text != "" else []
        sync_revert = disk_text != base_text and disk_text in recent
        overridden: set[str] = set()
        for row in self.store.overrides_for(str(self.path)):
            if row["section"] == "trading" and row["unit"] == "market_table" and row["human_text"]:
                overridden.update(row["human_text"].split("\n"))
        on_disk = _align(base, disk)

        def human(i: int) -> bool:
            line = on_disk[i]
            return line is not None and ((not sync_revert and line != base[i]) or line in overridden)

        stamp_at = next((i for i, line in enumerate(base) if _STAMP_RE.match(line)), None)
        ages = [b for b in [base_text, *recent] if b]
        flags: dict[str, str] = {}
        out: list[Optional[str]] = []
        stamp_human = False
        for i, line in enumerate(base):
            if i == stamp_at:
                stamp_human = human(i)
                out.append(on_disk[i] if stamp_human else None)  # None: the fresh stamp, below
                continue
            m = _FIELD_ROW_RE.match(line)
            name = m.group(1) if m and m.group(1) in self.cfg.fields else None
            if name is None:
                out.append(line)  # separator and every other line of last_after
                continue
            if on_disk[i] is None:
                continue  # deleted or renamed: never resurrected
            if human(i):
                out.append(on_disk[i])
                flags.setdefault(name, "human")
            elif self.cfg.fields[name] == "manual":
                filled = _fill_manual(line)
                out.append(filled)
                flags.setdefault(name, _manual_flag(filled))
            else:
                fresh = self.fresh_row(name)
                out.append(fresh if fresh is not None else line)
                flags.setdefault(name, "cobalt" if fresh is not None else _degraded(self.reason, _last_success(name, ages)))
        # Check A5: a field row he added — on disk, aligned to no line of
        # last_after — is his; the field's flag says so.
        unmatched = list(disk)
        for line in on_disk:
            if line is not None and line in unmatched:
                unmatched.remove(line)
        for line in unmatched:
            m = _FIELD_ROW_RE.match(line)
            if m and m.group(1) in self.cfg.fields:
                flags[m.group(1)] = "human"
        for name in REFRESH_FIELDS:
            flags.setdefault(name, "absent")
        flags["calendar"] = calendar_flag
        status_line = format_flag_line(self.stamp, flags)
        if stamp_at is None:
            body = [status_line, "", *out]  # a note from before F4 gets its stamp line (R6)
        else:
            body = [status_line if line is None else line for line in out]
        self.state.update(flags=flags, status_line=status_line, stamp_human=stamp_human)
        return "\n".join(body)


def run_daily_refresh(
    when: datetime, *, dry_run: bool = False, store: Optional[VaultWriteStore] = None
) -> RefreshResult:
    """`prefill refresh`: the two refreshable units of today's ET note.

    `store` is a test seam only (as in `daymode.note.write`); production
    passes nothing and gets `VaultWriteStore()`.
    """
    stamp = format_stamp(when)
    cfg = load_daily_refresh_config()
    if store is None:
        store = VaultWriteStore()
        store.ensure_schema()
    writer = VaultWriter(REFRESH_WRITER, store=store, dry_run=dry_run)
    path = refresh_note_path(when)
    fetched = asyncio.run(_gated_fetch(when))
    result = RefreshResult(path=path, dry_run=dry_run, stamp=stamp)
    if fetched.refused:
        result.notes.append(f"Finviz gate: {fetched.refused} — nothing requested")

    def _finish(flags: dict[str, str], status_line: str) -> RefreshResult:
        result.flags, result.status_line = flags, status_line
        result.degraded = [f"{k} {v}" for k, v in flags.items() if v.startswith("cobalt-degraded")]
        # Check A6 ([F-28]): a dead or refused source is a nonzero run even
        # when every field it serves is his — the report names the source.
        market_flagged = any(flags.get(t, "").startswith("cobalt-degraded") for t in MARKET_TICKERS)
        if fetched.market_error is not None and not market_flagged:
            result.degraded.append(f"market source: {fetched.market_error} (no Cobalt row to degrade)")
        if fetched.calendar_error is not None and not flags.get("calendar", "").startswith("cobalt-degraded"):
            result.degraded.append(f"calendar source: {fetched.calendar_error} (no Cobalt calendar to degrade)")
        return result

    if not path.exists():
        try:
            created = _ensure_note(writer, when, fetched)
        except NoteChangedOnDisk:
            # Check A2: another writer created the note between the check
            # and this create; its file stands (L28.1) and is refreshed below.
            if not path.exists():
                raise
            result.notes.append("another writer created the note during this create — refreshed on the ownership path")
        else:
            result.writes.append(created)
            if created.action == "created":
                result.action = "created"
                flags = _create_flags(fetched.market_rows, fetched.market_error, fetched.calendar_error, cfg)
                return _finish(flags, format_flag_line(stamp, flags))
            result.notes.append("another writer created the note first — refreshed on the ownership path")

    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    run = _Refresh(writer, store, path, cfg, fetched, stamp)
    present: dict[str, Optional[bool]] = {}
    for key in cfg.units:
        section, unit = key.split("/")
        if legacy_slot_present(text, section):
            present[section] = None
            result.notes.append(f"{section}: a pre-L28 note (legacy slot marker) — not touched")
            continue
        block = find_section(lines, section)
        present[section] = block is not None and unit in block.units

    # [F-36+]: a refreshable unit already on disk with no baseline → nothing.
    missing = [s for s, here in present.items() if here and writer._baseline(path, s, _UNIT_OF[s]) is None]
    if missing:
        result.action = "failed"
        result.failures.append(
            f"FAILED: baseline_missing — {', '.join(f'{s}/{_UNIT_OF[s]}' for s in missing)} is on disk "
            "with no vault_writes baseline; nothing written"
        )
        return result

    stub = present.get("trading") is False

    # The calendar first: its live flag rides on the trading stamp line.
    if present.get("market_calendar") is None:
        calendar_flag = "human"
    elif present["market_calendar"]:
        owned = run.calendar_owned(text)
        if stub:
            calendar_flag = "cobalt" if owned else "human"
            result.notes.append("market_calendar: already present on a stub — not written in this run ([F-35])")
        elif not owned:
            calendar_flag = "human"
            result.notes.append("market_calendar: his text (the unit is not a Cobalt body) — not written")
        elif fetched.calendar_error is not None:
            calendar_flag = run.calendar_degraded()
        else:
            write = writer.upsert_unit(
                path, "market_calendar", "market_calendar", run.calendar_body(),
                skip_if=lambda t: not run.calendar_owned(t),
            )
            result.writes.append(write)
            calendar_flag = "human" if write.action == "skipped" else "cobalt"
    elif not calendar_body_is_available(lines):
        calendar_flag = "human"
        result.notes.append("market_calendar: his content under the heading — not touched")
    elif fetched.calendar_error is not None:
        calendar_flag = _degraded(run.reason, None)
    else:
        result.writes.append(writer.upsert_unit(
            path, "market_calendar", "market_calendar", run.calendar_body(),
            placement=MARKET_CALENDAR_PLACEMENT,
        ))
        calendar_flag = "cobalt"

    if present.get("trading") is None:
        flags = {f: "absent" for f in REFRESH_FIELDS}
        flags["calendar"] = calendar_flag
        return _finish(flags, format_flag_line(stamp, flags))
    if stub:
        body = run.fresh_trading_body(calendar_flag)
        if body is None:
            flags = _create_flags(None, fetched.market_error or "a row is missing", None, cfg)
            flags["calendar"] = calendar_flag
            result.notes.append("trading: absent and no fresh values — not appended this run")
            return _finish(flags, format_flag_line(stamp, flags))
        # Fix round, X16: a table he typed under '### Trading' (no Cobalt
        # unit) is his — never wrapped as a seed for Cobalt's body to win.
        write = writer.upsert_unit(
            path, "trading", "market_table", body, placement=TRADING_PLACEMENT,
            skip_if=lambda t: _trading_table_span(t.split("\n")) is not None,
        )
        result.writes.append(write)
        if write.action == "skipped":
            flags = {f: "human" for f in REFRESH_FIELDS}
            flags["calendar"] = calendar_flag
            result.notes.append("trading: his table under '### Trading' (no Cobalt unit) — not wrapped, not written")
            return _finish(flags, format_flag_line(stamp, flags))
        return _finish(run.state["flags"], run.state["status_line"])

    write = writer.upsert_unit(
        path, "trading", "market_table", "",
        skip_if=run.trading_in_flight,
        body_fn=lambda snapshot: run.trading_proposal(snapshot, calendar_flag),
    )
    result.writes.append(write)
    if write.action == "skipped":
        result.action = "failed"
        result.failures.append(
            "FAILED: write_in_flight — the trading unit on disk opens with a Cobalt status line that no "
            "visible vault_writes row holds (another refresh's commit in flight, or its row lost); "
            "nothing written, no override recorded"
        )
        flags = {f: "not written" for f in REFRESH_FIELDS}
        flags["calendar"] = calendar_flag
        return _finish(flags, format_flag_line(stamp, flags))
    if run.state.get("stamp_human"):
        result.notes.append(f"the in-note stamp is his — the fresh status is this report's: {run.state['status_line']}")
    return _finish(run.state["flags"], run.state["status_line"])


_UNIT_OF = {"trading": "market_table", "market_calendar": "market_calendar"}
