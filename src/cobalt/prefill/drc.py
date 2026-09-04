"""Evening DRC prefill (Slice 2, item 4): tickers traded, a
Catalyst/Set-Up/Trade scaffold per ticker with card values (grade,
entry, stop, shares, fill update if one was recorded), re-entry-rule
fields, an excitement-audit question on reversion-tagged trades, sheet-
mode risk parameters, and the same rule-adherence checklist the morning
note used. Goal/grade/learnings/selectivity/1%-better/PnL stay exactly
as DRC.md's own instructional placeholders — Cobalt never touches them.

Same ONE write path as daily.py since 2026-09-03 (LAW L28): the full
template render only when the DRC note does not exist, otherwise
marker-bounded unit upserts through `cobalt.vaultwrite` — merged, never
appended blind, never overwritten. Three units:

    drc-risk   / risk_parameters  the computed sheet-mode risk line
    drc-trades / tickers          the counts + traded-ticker scaffold
    drc-rules  / rules_check      rule checklist + card reconcile

`_render_append_block`'s fenced "## Cobalt Prefill — DRC draft" block
and its `<!-- cobalt-prefill:drc:DATE -->` marker are retired: the
markers now carry identity, so a re-run updates the same three units
instead of appending a second block. Notes already carrying the old
marker are skipped whole (`legacy_marker`) — historical notes are not
retro-marked.

COUNTS (L28 step 3): "cards written" and "trades taken" are two
numbers, shown as two. Trades taken counts `aset_sizings.status =
'FILLED'` only. DRC-2026-09-03 reported "17 cards" when 2 were real
and none were filled.

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
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path
from typing import Optional

import yaml
from jinja2 import Environment, FileSystemLoader

from cobalt.aset.config import load_config as load_aset_config, load_sheet_modes_config
from cobalt.aset.models import Grade
from cobalt.aset.store import AsetStore

from .config import RulesConfig, StrategiesConfig, TEMPLATES_DIR, load_prefill_paths, load_strategies_config
from .daily import apply_mode_aware_sizing, format_rules_checkbox_block
from .rules_gen import regenerate_rules_config
from .vault_writer import VaultWriteError, read_if_exists, resolve_dir, resolve_target
from cobalt.vaultwrite import VaultWriteStore, VaultWriter, WriteResult, Placement, after_pattern
from cobalt.vaultwrite.markers import find_section

_FILL_BLOCK_RE = re.compile(r"```aset-fill\n(.*?)\n```", re.DOTALL)
_PNL_HEADING_RE = re.compile(r"^###\s*PnL on the day.*$")
_RISK_PARAMS_LINE_RE = re.compile(r"^Risk Parameters:.*$")
_TRADES_HEADING_RE = re.compile(r"^###\s*Catalyst \+ Set Up \+ Trades\s*$")
LEGACY_MARKER_TEMPLATE = "<!-- cobalt-prefill:drc:{date} -->"
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


def format_card_reconcile_block(grouped_entries: dict[str, list[EntryRender]]) -> str:
    """Slice 2.1a (2026-08-31): a card is a written plan; a card with a
    matching aset-fill block is a taken trade. Everything else is a
    pass, a phantom, or premarket exploration — and Cobalt does not
    guess which. One checklist line per card with no matching fill
    (EntryRender.fill is already None for those — see _build_entries);
    Dejan answers taken / passed / discarded by hand."""
    lines = [
        f"- [ ] {e.time_str} {ticker} ({e.grade} {e.direction.upper()}) — taken / passed / discarded?"
        for ticker, entries in grouped_entries.items()
        for e in entries
        if e.fill is None
    ]
    if not lines:
        return "(every card today has a matching fill — nothing to reconcile)\n"
    return "\n".join(lines) + "\n"


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




def legacy_marker(for_date_: date) -> str:
    """The PRE-L28 idempotency marker. Read-only compatibility: a DRC
    note already prefilled by the old writer is left completely alone —
    historical notes are not retro-marked (L28), and a second copy of a
    block Dejan already has is the damage this law prevents."""
    return LEGACY_MARKER_TEMPLATE.format(date=for_date_.isoformat())


def format_rules_check_block(context: dict) -> str:
    return "\n".join(
        [
            "**Rules (copied from the morning note's checklist — Rules.md is the source):**",
            context["rules_checkbox_block"].rstrip("\n"),
            "",
            "**Card reconcile (cards with no matching fill — taken / passed / discarded?):**",
            context["card_reconcile_block"].rstrip("\n"),
        ]
    )


def format_tickers_unit(context: dict) -> str:
    """The traded-tickers scaffold, headed by the two counts.

    "Cards written" and "trades taken" are DIFFERENT numbers and are
    shown as two (L28 step 3). Trades taken counts aset_sizings rows
    with status='FILLED' ONLY — a card is a written plan; it becomes a
    trade when the fill recompute says so. DRC-2026-09-03 reported
    "17 cards" when 2 were real and 0 were filled; that conflation is
    what this line replaces."""
    return "\n".join(
        [
            f"Cards written: {context['cards_written']} · "
            f"Trades taken (FILLED): {context['trades_taken']}",
            "",
            context["tickers_block"].rstrip("\n"),
        ]
    )


# ---------------------------------------------------------------------------
# Placement of each section the first time it lands in an existing note
# ---------------------------------------------------------------------------


def _risk_span(lines: list[str]) -> Optional[tuple[int, int]]:
    """Wrap DRC.md's own `Risk Parameters: A:5R, B:1R, C:0.5R` default
    line so Cobalt's computed line replaces it (recorded, diffed and
    restorable) instead of sitting beside a stale one. If the template's
    line isn't there, insert under the PnL heading."""
    for i, line in enumerate(lines):
        if _RISK_PARAMS_LINE_RE.match(line):
            return (i, i + 1)
    for i, line in enumerate(lines):
        if _PNL_HEADING_RE.match(line):
            return (i + 1, i + 1)
    return None


RISK_PLACEMENT = Placement("the 'Risk Parameters:' line (or under '### PnL on the day')", _risk_span)
TRADES_PLACEMENT = after_pattern(_TRADES_HEADING_RE, "under '### Catalyst + Set Up + Trades'")
# No anchor: the rules check is the last thing in the DRC by design, and
# L28's default placement (end of note, nothing above touched) is exactly
# where it belongs.
RULES_PLACEMENT = None


@dataclass
class DrcPrefillResult:
    path: Path
    action: str  # "created" | "filled" | "skipped_idempotent"
    cards_written: int
    trades_taken: int
    writes: list[WriteResult] = field(default_factory=list)
    dry_run: bool = False

    @property
    def card_count(self) -> int:
        """Back-compat alias. Prefer cards_written/trades_taken — they
        are different numbers and conflating them is what produced
        DRC-2026-09-03's "17 cards"."""
        return self.cards_written

    def report(self) -> str:
        lines = [
            f"DRC prefill [{'DRY-RUN' if self.dry_run else 'WRITE'}]: {self.action} — {self.path}",
            f"  cards written: {self.cards_written} · trades taken (FILLED): {self.trades_taken}",
        ]
        lines.extend(w.report() for w in self.writes)
        return "\n".join(lines)


async def run_drc_prefill(
    for_date_: Optional[date] = None, *, dry_run: bool = False
) -> DrcPrefillResult:
    for_date_ = for_date_ or datetime.now().astimezone().date()
    aset_cfg = load_aset_config()
    sheet_modes_cfg = load_sheet_modes_config()
    rules_cfg: RulesConfig = regenerate_rules_config()
    strategies_cfg = load_strategies_config()
    prefill_paths = load_prefill_paths()

    store = AsetStore(aset_cfg.db_name)
    store.ensure_schema()
    cards = store.for_date(for_date_)
    cards_written, trades_taken = store.counts_for_date(for_date_)

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

    mode_aware_rules = apply_mode_aware_sizing(rules_cfg.rules, sheet_modes_cfg)
    context = {
        "date_str": for_date_.isoformat(),
        "risk_parameters_line": format_risk_parameters(cards, sheet_modes_cfg),
        "tickers_block": format_tickers_block(grouped_entries),
        "rules_checkbox_block": format_rules_checkbox_block(mode_aware_rules),
        "card_reconcile_block": format_card_reconcile_block(grouped_entries),
        "cards_written": cards_written,
        "trades_taken": trades_taken,
    }
    context["rules_check_block"] = format_rules_check_block(context)
    context["tickers_unit"] = format_tickers_unit(context)

    filename = for_date_.strftime(prefill_paths.drc_filename_pattern)
    path = resolve_target(prefill_paths.review_dir, filename)

    write_store = VaultWriteStore(aset_cfg.db_name)
    write_store.ensure_schema()
    writer = VaultWriter("prefill.drc", store=write_store, dry_run=dry_run)

    # L28.1: created whole only when absent; an existing note always
    # takes the merge path below.
    created = writer.create_if_absent(path, _render_template(context))
    if created.action == "created":
        return DrcPrefillResult(
            path=path, action="created", cards_written=cards_written,
            trades_taken=trades_taken, writes=[created], dry_run=dry_run,
        )

    existing = read_if_exists(path) or ""
    if legacy_marker(for_date_) in existing:
        return DrcPrefillResult(
            path=path, action="skipped_idempotent", cards_written=cards_written,
            trades_taken=trades_taken, dry_run=dry_run,
        )

    units = (
        ("drc-risk", "risk_parameters", f"Risk Parameters: {context['risk_parameters_line']}", RISK_PLACEMENT),
        ("drc-trades", "tickers", context["tickers_unit"], TRADES_PLACEMENT),
        ("drc-rules", "rules_check", context["rules_check_block"], RULES_PLACEMENT),
    )
    writes = [
        writer.upsert_unit(path, section, unit, body, placement=placement)
        for section, unit, body, placement in units
    ]
    action = "filled" if any(w.action == "updated" for w in writes) else "skipped_idempotent"
    return DrcPrefillResult(
        path=path, action=action, cards_written=cards_written,
        trades_taken=trades_taken, writes=writes, dry_run=dry_run,
    )
