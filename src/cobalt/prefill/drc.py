"""Evening DRC prefill (Slice 2, item 4): tickers traded, a
Catalyst/Set-Up/Trade scaffold per ticker with card values (grade,
entry, stop, shares, fill update if one was recorded), re-entry-rule
fields, an excitement-audit question on reversion-tagged trades, sheet-
mode risk parameters, and the same rule-adherence checklist the morning
note used. Goal/grade/learnings/selectivity/1%-better/PnL stay exactly
as DRC.md's own instructional placeholders — Cobalt never touches them.

Same create-vs-append principle as daily.py: full template render if
the DRC note doesn't exist yet, otherwise a fenced, idempotency-marked
append.

Cards (aset_sizings rows) don't carry Catalyst/Set-Up text or a
strategy tag — those live only in the Trade Ideas table (his, always
empty at prefill time) and the trade note's own `strategy` frontmatter
field (also his, may still be blank by evening). Trade-note matching is
by NEAREST timestamp within the same ticker (the DB's created_at and
the note's own filename timestamp come from two different clock reads
moments apart — see trade_note.py — so exact-second matching would
under-match); a card with no note within tolerance is still listed,
just without a strategy/fill lookup.
"""

import re
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Optional

import yaml
from jinja2 import Environment, FileSystemLoader

from cobalt.aset.config import load_config as load_aset_config, load_sheet_modes_config
from cobalt.aset.models import Grade
from cobalt.aset.store import AsetStore

from .config import RulesConfig, StrategiesConfig, TEMPLATES_DIR, load_prefill_paths, load_rules_config, load_strategies_config
from .daily import format_rules_blocks
from .vault_writer import VaultWriteError, append_block, read_if_exists, resolve_dir, resolve_target, write_new

_FILL_BLOCK_RE = re.compile(r"```aset-fill\n(.*?)\n```", re.DOTALL)
_TRADE_FILENAME_RE = re.compile(r"^Trade-(\d{4}-\d{2}-\d{2}) (\d{2}-\d{2}-\d{2}) -(.+)\.md$")
_FRONTMATTER_RE = re.compile(r"\A---\n(.*?\n)---\n", re.DOTALL)
FILL_MATCH_TOLERANCE_SECONDS = 30


def parse_fill_updates(daily_note_text: str) -> dict[str, dict[str, str]]:
    """Map naive-local-ISO orig_timestamp -> the ```aset-fill block's
    fields, for every FILL UPDATE block in a daily note's text."""
    updates: dict[str, dict[str, str]] = {}
    for block in _FILL_BLOCK_RE.findall(daily_note_text):
        fields: dict[str, str] = {}
        for line in block.splitlines():
            if ":" not in line:
                continue
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
        orig_ts_raw = fields.get("orig_timestamp")
        if not orig_ts_raw:
            continue
        try:
            orig_ts = datetime.fromisoformat(orig_ts_raw)
        except ValueError:
            continue
        updates[orig_ts.replace(tzinfo=None).isoformat(timespec="seconds")] = fields
    return updates


def _parse_trade_filename(name: str) -> Optional[tuple[str, datetime]]:
    m = _TRADE_FILENAME_RE.match(name)
    if not m:
        return None
    date_part, time_part, ticker = m.groups()
    when = datetime.strptime(f"{date_part} {time_part}", "%Y-%m-%d %H-%M-%S")
    return ticker.upper(), when


def find_trade_note_for_card(trades_dir: Path, ticker: str, created_at: datetime) -> Optional[Path]:
    """Nearest-timestamp match within tolerance — the DB row's created_at
    and the trade note's filename timestamp come from two separate
    clock reads a beat apart (store.save() vs. save_card()'s `when`),
    so exact-second equality would miss real matches."""
    if not trades_dir.is_dir():
        return None
    target = created_at.astimezone().replace(tzinfo=None)
    best_path, best_delta = None, None
    for entry in trades_dir.iterdir():
        parsed = _parse_trade_filename(entry.name)
        if parsed is None:
            continue
        file_ticker, file_when = parsed
        if file_ticker != ticker.upper():
            continue
        delta = abs((file_when - target).total_seconds())
        if delta <= FILL_MATCH_TOLERANCE_SECONDS and (best_delta is None or delta < best_delta):
            best_path, best_delta = entry, delta
    return best_path


def _read_strategy(trade_note_path: Optional[Path]) -> Optional[str]:
    if trade_note_path is None or not trade_note_path.exists():
        return None
    m = _FRONTMATTER_RE.match(trade_note_path.read_text(encoding="utf-8"))
    if not m:
        return None
    fm = yaml.safe_load(m.group(1)) or {}
    strategy = fm.get("strategy")
    return strategy.strip() if isinstance(strategy, str) and strategy.strip() else None


@dataclass
class EntryRender:
    number: int
    time_str: str
    grade: str
    direction: str
    sheet_mode: str
    entry: str
    stop: str
    shares: str
    risk_budget: str
    fill: Optional[dict]
    needs_written_info: bool
    stand_down: bool
    excitement_audit: bool


def _build_entries(
    cards: list[dict],
    fills: dict[str, dict],
    strategies_cfg: StrategiesConfig,
    trades_dir: Path,
) -> list[EntryRender]:
    entries = []
    for idx, card in enumerate(cards, start=1):
        created_at: datetime = card["created_at"]
        trade_note_path = find_trade_note_for_card(trades_dir, card["ticker"], created_at)
        parsed = _parse_trade_filename(trade_note_path.name) if trade_note_path else None
        local_when = parsed[1] if parsed else created_at.astimezone().replace(tzinfo=None)
        fill = fills.get(local_when.isoformat(timespec="seconds"))
        strategy = _read_strategy(trade_note_path)
        entries.append(
            EntryRender(
                number=idx,
                time_str=local_when.strftime("%H:%M:%S"),
                grade=card["grade"],
                direction=card["direction"],
                sheet_mode=(card.get("sheet_mode") or "n/a"),
                entry=str(card["entry"]),
                stop=str(card["stop"]),
                shares=str(card["shares"]),
                risk_budget=str(card["risk_budget"]),
                fill=fill,
                needs_written_info=(idx == 2),
                stand_down=(idx >= 3),
                excitement_audit=strategies_cfg.is_reversion(strategy),
            )
        )
    return entries


def _render_entry(e: EntryRender) -> str:
    lines = [f"  Entry #{e.number} — {e.time_str} ET"]
    if e.needs_written_info:
        lines.append('  - New written information (re-entry #2 rule — blank or "better price" = no trade): ')
    if e.stand_down:
        lines.append("  - STAND DOWN: entry #3+ same thesis — ticker done for the day (Rules.md).")
    lines += [
        f"  - Grade: {e.grade} · Direction: {e.direction.upper()} · Sheet mode: {e.sheet_mode.upper()}",
        f"  - Entry: ${e.entry} · Stop: ${e.stop} · Shares: {e.shares} · Risk budget: ${e.risk_budget}",
    ]
    if e.fill:
        lines.append(
            f"  - Fill update: actual ${e.fill.get('actual_fill', '?')} · "
            f"recomputed shares {e.fill.get('recomputed_shares', '?')} "
            f"(Δ{e.fill.get('share_delta', '?')}) · "
            f"distance change {e.fill.get('distance_change_pct', '?')}%"
        )
    else:
        lines.append("  - Fill update: n/a (no FILL UPDATE recorded)")
    lines += [
        "  - Catalyst: ",
        "  - Set Up: ",
        "  - Trade Notes: ",
        "  - Keys to success here: ",
        "  - Observation about the way the trade set up (type of buying, price action, etc) + observation about myself: ",
        "  - Any observations about ideal vs actual dots on chart: ",
        "  - Insert Chart with Executions: ",
    ]
    if e.excitement_audit:
        lines.append(
            "  - Excitement audit (reversion-tagged trade): in because criteria met — or because it excites me?"
        )
    lines.append("")
    return "\n".join(lines)


def format_tickers_block(grouped_entries: dict[str, list[EntryRender]]) -> str:
    if not grouped_entries:
        return "(no tickers traded today)\n"
    parts = []
    for ticker, entries in grouped_entries.items():
        parts.append(f"- Ticker: {ticker}\n")
        parts.extend(_render_entry(e) for e in entries)
    return "\n".join(parts)


def format_risk_parameters(cards: list[dict], sheet_modes_cfg) -> str:
    modes_used = sorted({c["sheet_mode"] for c in cards if c.get("sheet_mode")})
    if not modes_used:
        return "no sheet-mode cards today (configs/cobalt/aset.yaml has the ladder)"
    parts = []
    for mode in modes_used:
        grade_parts = ", ".join(
            f"{g.value}:${sheet_modes_cfg.dollars_for(mode, g)}"
            for g in Grade
            if sheet_modes_cfg.is_enabled(g)
        )
        parts.append(f"{mode.upper()} — {grade_parts}")
    return "; ".join(parts)


def _group_cards_by_ticker(cards: list[dict]) -> dict[str, list[dict]]:
    grouped: dict[str, list[dict]] = {}
    for card in cards:
        grouped.setdefault(card["ticker"], []).append(card)
    return grouped


def _render_template(context: dict) -> str:
    env = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR)), keep_trailing_newline=True)
    return env.get_template("drc.md.j2").render(**context)


def _idempotency_marker(for_date_: date) -> str:
    return f"<!-- cobalt-prefill:drc:{for_date_.isoformat()} -->"


def _render_append_block(for_date_: date, context: dict) -> str:
    lines = [
        "",
        "## Cobalt Prefill — DRC draft",
        _idempotency_marker(for_date_),
        "",
        f"Risk Parameters: {context['risk_parameters_line']}",
        "",
        "### Catalyst + Set Up + Trades (Cobalt-prefilled)",
        context["tickers_block"].rstrip("\n"),
        "",
        "**Rule adherence (copied from the morning note's checklist — configs/cobalt/rules.yaml):**",
        context["rule_adherence_block"].rstrip("\n"),
        "",
    ]
    return "\n".join(lines)


@dataclass
class DrcPrefillResult:
    path: Path
    action: str  # "created" | "appended" | "skipped_idempotent"
    card_count: int


async def run_drc_prefill(for_date_: Optional[date] = None) -> DrcPrefillResult:
    for_date_ = for_date_ or datetime.now().astimezone().date()
    aset_cfg = load_aset_config()
    sheet_modes_cfg = load_sheet_modes_config()
    rules_cfg: RulesConfig = load_rules_config()
    strategies_cfg = load_strategies_config()
    prefill_paths = load_prefill_paths()

    store = AsetStore(aset_cfg.db_name)
    store.ensure_schema()
    cards = store.for_date(for_date_)

    daily_filename = for_date_.strftime(aset_cfg.daily_note.filename_pattern)
    try:
        daily_note_path = resolve_target(aset_cfg.daily_note.daily_notes_dir, daily_filename)
        daily_note_text = read_if_exists(daily_note_path) or ""
    except VaultWriteError:
        daily_note_text = ""
    fills = parse_fill_updates(daily_note_text)

    trades_dir_path = resolve_dir(prefill_paths.trades_dir)
    grouped_cards = _group_cards_by_ticker(cards)
    grouped_entries = {
        ticker: _build_entries(ticker_cards, fills, strategies_cfg, trades_dir_path)
        for ticker, ticker_cards in grouped_cards.items()
    }

    _, adherence_block, _ = format_rules_blocks(rules_cfg)
    context = {
        "date_str": for_date_.isoformat(),
        "risk_parameters_line": format_risk_parameters(cards, sheet_modes_cfg),
        "tickers_block": format_tickers_block(grouped_entries),
        "rule_adherence_block": adherence_block,
    }

    filename = for_date_.strftime(prefill_paths.drc_filename_pattern)
    path = resolve_target(prefill_paths.review_dir, filename)
    existing = read_if_exists(path)

    if existing is None:
        write_new(path, _render_template(context))
        return DrcPrefillResult(path=path, action="created", card_count=len(cards))

    marker = _idempotency_marker(for_date_)
    if marker in existing:
        return DrcPrefillResult(path=path, action="skipped_idempotent", card_count=len(cards))

    append_block(path, _render_append_block(for_date_, context))
    return DrcPrefillResult(path=path, action="appended", card_count=len(cards))
