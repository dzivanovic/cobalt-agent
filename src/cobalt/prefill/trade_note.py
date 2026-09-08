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

from datetime import datetime
from pathlib import Path
from typing import Optional

from cobalt.aset.models import SizingResult

from cobalt.vaultwrite import VaultWriter, VaultWriteStore
from cobalt.vaultwrite.frontmatter import frontmatter_span, split_frontmatter

from .config import PrefillPathsConfig
from .vault_writer import VaultWriteError, read_if_exists, resolve_target

COBALT_OWNED_FIELDS = ("date", "symbol", "direction", "stop_price", "entry_price")
#: ADR-0008 D4: a NEW trade note carries `trade_def:` — the trade's ID —
#: and not `strategy:`, the free-text name D4 spent 69 notes replacing.
#: It is DEJAN'S field, blank at creation like `RVOL` and `exit_price`:
#: Cobalt writes the five in COBALT_OWNED_FIELDS and nothing else, and a
#: card does not know which strategy he decided he was trading.
#: Existing notes keep whatever they already have — this is the shape of
#: a new one, not a migration (that is `cobalt taxonomy
#: migrate-trade-notes`).
FIELD_ORDER = (
    "date", "symbol", "direction", "stop_price", "entry_price", "exit_price",
    "entry_time", "exit_time", "profit_loss", "trade_def", "RVOL", "tags",
)


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


#: Rendered WITHOUT quotes. A slug is `[a-z0-9-]` by construction and a
#: date and a ticker need no quoting either — and `trade_def:` matters
#: here beyond neatness: `cobalt taxonomy migrate-trade-notes` writes the
#: slug unquoted into every existing note, so quoting it on the next
#: Cobalt write would make his line and Cobalt's differ, and every prefill
#: run would record a pointless override on a value nobody changed.
_UNQUOTED_FIELDS = ("date", "symbol", "trade_def")


def _render_value(key: str, value) -> str:
    if value is None or value == "":
        return f"{key}:"
    if key in _UNQUOTED_FIELDS:
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
    """Thin alias for the one shared reader (`vaultwrite.frontmatter`).
    The regex used to be written out here AND in `prefill/drc.py`; the
    ADR-0008 vault loader would have been the third copy."""
    return split_frontmatter(content)


FRONTMATTER_SECTION = "trade-frontmatter"
FRONTMATTER_REGION = "frontmatter"


def upsert_trade_note(
    result: SizingResult,
    when: datetime,
    prefill_paths: PrefillPathsConfig,
    *,
    writer: Optional[VaultWriter] = None,
    db_name: Optional[str] = None,
    dry_run: bool = False,
) -> tuple[Path, str]:
    """Create or update the trade note for one computed card. Returns
    (path, action).

    Converted to the ONE write path 2026-09-03 (LAW L28): a note that
    does not exist is created whole; one that does takes the merge path
    through `VaultWriter.upsert_region`, guarded, audited and diffed like
    every other vault write. Dejan's own frontmatter keys are merged
    key-wise here (as before), and the writer's three-way merge is the
    second line of defence — if he edited one of Cobalt's own five keys,
    HIS value wins and an override row records it.
    """
    ticker = result.input.ticker
    filename = _trade_note_filename(prefill_paths, ticker, when)
    title = filename[:-3] if filename.endswith(".md") else filename
    path = resolve_target(prefill_paths.trades_dir, filename)
    fresh = _cobalt_fields(result, when)

    if writer is None:
        store = VaultWriteStore(db_name)
        store.ensure_schema()
        writer = VaultWriter("prefill.trade_note", store=store, dry_run=dry_run)

    existing = read_if_exists(path)
    if existing is None:
        writer.create_if_absent(path, _render_frontmatter(fresh) + _render_body(title))
        return path, "created"

    fm, _body = _split_frontmatter(existing)
    if fm is None:
        raise VaultWriteError(
            f"{path}: existing file has no recognizable frontmatter block — "
            "refusing to guess at its shape, not touching it."
        )
    merged = dict(fm)
    merged.update(fresh)  # Cobalt's five keys refreshed; every other key/value untouched
    writer.upsert_region(
        path,
        FRONTMATTER_SECTION,
        FRONTMATTER_REGION,
        _render_frontmatter(merged).rstrip("\n"),
        locate=frontmatter_span,
    )
    return path, "updated"
