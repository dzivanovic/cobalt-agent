"""Trade notes from ASET cards (Slice 2, item 3): every computed sizing
creates/updates a note in "1 - Trading/2 - Trades/" using the Individual
Trade Template's frontmatter shape, so the daily note's dataview table
lights up.

Cobalt owns exactly five frontmatter fields — date, symbol, direction,
stop_price, entry_price — the grunt data straight off the card.
strategy/RVOL/exit_price/entry_time/exit_time/profit_loss are Dejan's:
created blank, and on any later re-run (same card, e.g. a retried
prefill), the existing file's values for those fields are read back and
preserved verbatim — Cobalt refreshes only its own five keys, never his
body text or his fields. RVOL is always blank today: ASET's sizing
engine does not fetch it (see aset/prefill.py) — blank is the honest
answer, not a guess.
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Optional

import yaml

from cobalt.aset.models import SizingResult

from .config import PrefillPathsConfig
from .vault_writer import VaultWriteError, overwrite, read_if_exists, resolve_target, write_new

COBALT_OWNED_FIELDS = ("date", "symbol", "direction", "stop_price", "entry_price")
FIELD_ORDER = (
    "date", "symbol", "direction", "stop_price", "entry_price", "exit_price",
    "entry_time", "exit_time", "profit_loss", "strategy", "RVOL", "tags",
)
_FRONTMATTER_RE = re.compile(r"\A---\n(.*?\n)---\n", re.DOTALL)


def _trade_note_filename(prefill_paths: PrefillPathsConfig, ticker: str, when: datetime) -> str:
    return when.strftime(prefill_paths.trade_filename_pattern).format(ticker=ticker)


def _cobalt_fields(result: SizingResult, when: datetime) -> dict:
    i = result.input
    return {
        "date": when.strftime("%Y-%m-%d %H:%M"),
        "symbol": i.ticker,
        "direction": i.direction.value.capitalize(),
        "stop_price": str(i.stop),
        "entry_price": str(i.entry),
    }


def _render_value(key: str, value) -> str:
    if value is None or value == "":
        return f"{key}:"
    if key in ("date", "symbol"):
        return f"{key}: {value}"
    return f'{key}: "{value}"'


def _render_frontmatter(fields: dict) -> str:
    lines = ["---"]
    for key in FIELD_ORDER:
        if key == "tags":
            lines.append("tags:")
            for tag in fields.get("tags") or ["trade"]:
                lines.append(f"  - {tag}")
            continue
        lines.append(_render_value(key, fields.get(key)))
    # any extra keys Dejan (or a future template revision) added, preserved after the known ones
    for key, value in fields.items():
        if key not in FIELD_ORDER:
            lines.append(_render_value(key, value))
    lines.append("---")
    return "\n".join(lines) + "\n"


def _render_body(title: str) -> str:
    return (
        f"# Trade: [[{title}]]\n"
        "**Details**:\n"
        "\n"
        "- Notes: \n"
        "\t- [Why you entered, market conditions, mistakes]\n"
        "- What did I do well:\n"
        "\t- [Things I did well in the trade]\n"
        "- What can I do better next time:\n"
        "\t- [Things I can improve or observe next time]\n"
    )


def _split_frontmatter(content: str) -> tuple[Optional[dict], str]:
    m = _FRONTMATTER_RE.match(content)
    if not m:
        return None, content
    parsed = yaml.safe_load(m.group(1))
    return (parsed or {}), content[m.end():]


def upsert_trade_note(
    result: SizingResult, when: datetime, prefill_paths: PrefillPathsConfig
) -> tuple[Path, str]:
    """Create or update the trade note for one computed card. Returns
    (path, action) where action is "created" or "updated"."""
    ticker = result.input.ticker
    filename = _trade_note_filename(prefill_paths, ticker, when)
    title = filename[:-3] if filename.endswith(".md") else filename
    path = resolve_target(prefill_paths.trades_dir, filename)
    fresh = _cobalt_fields(result, when)

    existing = read_if_exists(path)
    if existing is None:
        write_new(path, _render_frontmatter(fresh) + _render_body(title))
        return path, "created"

    fm, body = _split_frontmatter(existing)
    if fm is None:
        raise VaultWriteError(
            f"{path}: existing file has no recognizable frontmatter block — "
            "refusing to guess at its shape, not touching it."
        )
    merged = dict(fm)
    merged.update(fresh)  # Cobalt's five keys refreshed; every other key/value untouched
    overwrite(path, _render_frontmatter(merged) + body)
    return path, "updated"
