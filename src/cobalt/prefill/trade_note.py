"""Trade notes (Slice 2 item 3; S3 exits C4 = F22, v3 §7): the ONE
trade-note writer (L3), for both origins —

* `/size` (O4 A): every computed sizing creates / updates its note in
  "1 - Trading/2 - Trades/" at the sizing time, with the planned entry;
* the FILL: the card's trade note at the FILLED transition's time (ET),
  with the fill price, carrying ONE Cobalt section `cobalt-legs` after his
  template body — one unit `leg-<seq>` per current leg (C4-3).

Both use the Individual Trade Template's frontmatter shape, so the daily
note's dataview table lights up.

Cobalt owns exactly five frontmatter fields — date, symbol, direction,
stop_price, entry_price — the grunt data straight off the card, refreshed
on every write. The rest are Dejan's: created blank, and on any later
write the existing file's values are read back and kept verbatim. FOUR of
his keys are FILLED by Cobalt ONLY WHILE BLANK (O5 / O6 = A, 09-28 R35
(3); L28 clause 2a, blank → value only), each from one source
(`his_fills`): `entry_time` ← the FILLED transition time (ET),
`exit_time` ← the CLOSED transition time (ET), `exit_price` ← the one
current exit leg's price when the card CLOSED through exactly one
`confirmed` exit leg, `trade_def` ← a radar card's `trade_def_slug`. A key
he typed — or one Cobalt filled earlier, which is then his — is never
rewritten; an absent key is never added. `profit_loss` (its unit is
unruled) and RVOL (ASET does not fetch it — see aset/prefill.py) stay
blank: blank is the honest answer, not a guess.

The fill event, the leg units and the retry (`write_card_note`,
`write_leg_unit`) read the card through `AsetStore` and its legs through
`cards.legs.read_position` (`legs_current_v`) and write through
`VaultWriter` only (L40); `aset_sizings.trade_note_path` is set only by
`AsetStore.set_trade_note_path` (S-NOTE). No reverse parse: the DB leg is
never changed from the note (L28).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

from cobalt.aset.models import Direction

from cobalt.vaultwrite import VaultWriter, VaultWriteStore
from cobalt.vaultwrite.frontmatter import frontmatter_span, split_frontmatter
from cobalt.vaultwrite.markers import render_section

from .config import PrefillPathsConfig
from .vault_writer import VaultWriteError, read_if_exists, resolve_target

COBALT_OWNED_FIELDS = ("date", "symbol", "direction", "stop_price", "entry_price")
#: ADR-0008 D4: a NEW trade note carries `trade_def:` — the trade's ID —
#: and not `strategy:`, the free-text name D4 spent 69 notes replacing.
#: It is DEJAN'S field, blank at creation like `RVOL` and `exit_price`.
#: S3 C4 (O6 = A): Cobalt fills it from a RADAR card's `trade_def_slug`
#: while it is blank; a manual card has no slug, so it stays blank.
#: Existing notes keep whatever they already have — this is the shape of
#: a new one, not a migration (that is `cobalt taxonomy
#: migrate-trade-notes`).
FIELD_ORDER = (
    "date", "symbol", "direction", "stop_price", "entry_price", "exit_price",
    "entry_time", "exit_time", "profit_loss", "trade_def", "RVOL", "tags",
)

#: His keys Cobalt fills while blank (O5 / O6 = A); nothing else of his.
HIS_FILLED_KEYS = ("entry_time", "exit_time", "exit_price", "trade_def")

#: The `date` key's format — the fill times are written in it (ET).
NOTE_TIME_FORMAT = "%Y-%m-%d %H:%M"

#: The ONE Cobalt section of a fill note (C4-1), after his template body.
LEGS_SECTION = "cobalt-legs"

#: The writer name every trade-note write carries in `vault_writes`.
WRITER_NAME = "prefill.trade_note"


class TradeNoteRefused(VaultWriteError):
    """A trade-note write refused by name — shown verbatim, never forced."""


def _trade_note_filename(prefill_paths: PrefillPathsConfig, ticker: str, when: datetime) -> str:
    return when.strftime(prefill_paths.trade_filename_pattern).format(ticker=ticker)


def trade_note_relative_path(prefill_paths: PrefillPathsConfig, ticker: str, when: datetime) -> str:
    """The note's path relative to the vault root — `trade_note_path`'s
    value (S-NOTE)."""
    return f"{prefill_paths.trades_dir}/{_trade_note_filename(prefill_paths, ticker, when)}"


def _cobalt_fields(card: Mapping[str, Any], when: datetime, entry_price) -> dict:
    return {
        "date": when.strftime(NOTE_TIME_FORMAT),
        "symbol": card["ticker"],
        "direction": Direction(card["direction"]).value.capitalize(),
        "stop_price": str(card["stop"]),
        "entry_price": str(entry_price),
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
    """A NEW note renders every FIELD_ORDER key (his blank). An existing
    note is never re-rendered: `_merge_frontmatter_lines` keeps his lines."""
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


def _render_legs_section() -> str:
    """The empty `cobalt-legs` section a fill note is created with; its
    units are written by `upsert_unit` (one per current leg seq)."""
    return "\n" + "\n".join(render_section(LEGS_SECTION, [])) + "\n"


def _split_frontmatter(content: str) -> tuple[Optional[dict], str]:
    """Thin alias for the one shared reader (`vaultwrite.frontmatter`).
    The regex used to be written out here AND in `prefill/drc.py`; the
    ADR-0008 vault loader would have been the third copy."""
    return split_frontmatter(content)


def _is_blank(value) -> bool:
    """BLANK = present with an empty value (`key:`, `""`, null)."""
    return value is None or (isinstance(value, str) and value.strip() == "")


def _et(ts: datetime) -> datetime:
    from cobalt.session import session_clock

    return session_clock().to_et(ts)


def his_fills(card: Mapping[str, Any], legs: Sequence[Mapping[str, Any]]) -> dict[str, str]:
    """The values Cobalt may put into his blank keys (O5 / O6 = A), one
    source each — only the keys whose source exists. `card` carries its
    FILLED / CLOSED transition times (`AsetStore.card_for_note`); `legs`
    are the CURRENT legs (`legs_current_v`)."""
    fills: dict[str, str] = {}
    filled_at = card.get("filled_transition_at")
    if filled_at is not None:
        fills["entry_time"] = _et(filled_at).strftime(NOTE_TIME_FORMAT)
    if card.get("trade_def_slug"):
        fills["trade_def"] = str(card["trade_def_slug"])
    closed_at = card.get("closed_transition_at")
    if card.get("state") == "CLOSED" and closed_at is not None:
        fills["exit_time"] = _et(closed_at).strftime(NOTE_TIME_FORMAT)
        exits = [leg for leg in legs if leg["kind"] == "exit"]
        if len(exits) == 1 and exits[0]["flag"] == "confirmed":
            fills["exit_price"] = str(exits[0]["price"])
    return fills


def leg_unit_id(seq: int) -> str:
    return f"leg-{int(seq)}"


def render_leg_line(leg: Mapping[str, Any]) -> str:
    """One current leg as its unit's line (v3 §7):
    `<exit|entry> <preset> · <shares> sh @ <price> · <HH:MM> · <flag>`;
    a held-count row: `holding <held_stated> (stated) · <HH:MM>`. HH:MM is
    the leg's `at` in ET. An entry carries no preset: `entry · …`."""
    hhmm = _et(leg["at"]).strftime("%H:%M")
    if leg.get("held_stated") is not None:
        return f"holding {leg['held_stated']} (stated) · {hhmm}"
    head = leg["kind"] if not leg.get("preset") else f"{leg['kind']} {leg['preset']}"
    return f"{head} · {leg['shares']} sh @ {leg['price']} · {hhmm} · {leg['flag']}"


FRONTMATTER_SECTION = "trade-frontmatter"
FRONTMATTER_REGION = "frontmatter"


def upsert_trade_note(
    card: Mapping[str, Any],
    when: datetime,
    prefill_paths: PrefillPathsConfig,
    *,
    entry_price,
    fills: Optional[Mapping[str, str]] = None,
    legs_section: bool = False,
    create_only: bool = False,
    writer: Optional[VaultWriter] = None,
    db_name: Optional[str] = None,
    dry_run: bool = False,
) -> tuple[Path, str]:
    """Create or update the trade note of ONE card. Returns (path, action).

    `card` is the card row (its `ticker`, `direction`, `stop`); `when`
    names the file and fills `date` (`/size`: the sizing time; the fill:
    the FILLED transition time in ET); `entry_price` is the price written
    (`/size`: the planned entry; the fill: the entry leg's price). `fills`
    are his keys' values (`his_fills`), each written ONLY while his key is
    blank. `legs_section` adds the empty `cobalt-legs` section after his
    template body to a NEW note. `create_only` (the fill event): a note
    already at the path is another card's — refused, never merged (X16).

    Converted to the ONE write path 2026-09-03 (LAW L28): a note that
    does not exist is created whole; one that does takes the merge path
    through `VaultWriter.upsert_region`, guarded, audited and diffed like
    every other vault write. Dejan's own frontmatter lines are kept byte
    for byte (`_merge_frontmatter_lines`), and the writer's three-way merge is the
    second line of defence — if he edited one of Cobalt's own five keys,
    HIS value wins and an override row records it.
    """
    ticker = card["ticker"]
    filename = _trade_note_filename(prefill_paths, ticker, when)
    title = filename[:-3] if filename.endswith(".md") else filename
    path = resolve_target(prefill_paths.trades_dir, filename)
    fresh = _cobalt_fields(card, when, entry_price)
    fills = {k: v for k, v in (fills or {}).items() if k in HIS_FILLED_KEYS and not _is_blank(v)}

    if writer is None:
        store = VaultWriteStore(db_name)
        store.ensure_schema()
        writer = VaultWriter(WRITER_NAME, store=store, dry_run=dry_run)

    existing = read_if_exists(path)
    if existing is None:
        body = _render_body(title) + (_render_legs_section() if legs_section else "")
        writer.create_if_absent(path, _render_frontmatter({**fresh, **fills}) + body)
        return path, "created"
    if create_only:
        raise TradeNoteRefused(
            f"REFUSED: {path} already exists — another card's note (same ticker, same second, "
            "X16). Nothing merged, nothing written."
        )

    fm, _body = _split_frontmatter(existing)
    if fm is None:
        raise VaultWriteError(
            f"{path}: existing file has no recognizable frontmatter block — "
            "refusing to guess at its shape, not touching it."
        )
    writer.upsert_region(
        path,
        FRONTMATTER_SECTION,
        FRONTMATTER_REGION,
        _merge_frontmatter_lines(path, existing, fm, fresh, fills),
        locate=frontmatter_span,
    )
    return path, "updated"


def _merge_frontmatter_lines(path: Path, existing: str, fm: Mapping, fresh: dict, fills: Mapping[str, str]) -> str:
    """His frontmatter block written back LINE BY LINE, in HIS order,
    every byte of his kept (L28; C4 fix r2 B1). The YAML read (`fm`) only
    says which keys exist and which are blank; it is never re-rendered —
    `5.10` stays `5.10`, `10:31` stays `10:31`, his comments and list
    shapes stay.

    A top-level entry starts at a line with no leading whitespace whose
    text before its first `:` (stripped, unquoted) is a key of `fm`; every
    other line (indented, a `- ` item, a `#` comment, blank) belongs to the
    entry above it, or to a prefix kept before the first entry. Rendered
    are only: a Cobalt-owned key (its value lines replaced by
    `_render_value`), and a key of his that is blank and has a fill
    (blank → value only, R35 (3)). A comment or blank line under a
    replaced entry is his and is kept. A Cobalt-owned key absent from his
    block is appended before the closing `---`, in FIELD_ORDER; an absent
    key of his is never added. A parsed key with no top-level line of its
    own (a flow mapping, a repeated key) is refused, nothing written (L1).
    """
    lines = existing.split("\n")
    span = frontmatter_span(lines)
    keys = {str(key) for key in fm}
    refused = VaultWriteError(
        f"{path}: its frontmatter block does not map line by line onto its keys — "
        "refusing to guess at its shape, not touching it."
    )
    if span is None:
        raise refused
    start, end = span
    prefix: list[str] = []
    entries: list[tuple[str, list[str]]] = []
    for line in lines[start + 1:end - 1]:
        key = None
        if line and not line[0].isspace() and not line.startswith(("#", "- ")) and ":" in line:
            key = line.split(":", 1)[0].strip().strip("\"'")
        if key in keys:
            if any(seen == key for seen, _ in entries):
                raise refused
            entries.append((key, [line]))
        elif entries:
            entries[-1][1].append(line)
        else:
            prefix.append(line)
    if {key for key, _ in entries} != keys:
        raise refused

    out = [lines[start], *prefix]
    for key, entry in entries:
        if key in COBALT_OWNED_FIELDS:
            rendered = _render_value(key, fresh[key])
        elif key in fills and _is_blank(fm[key]):
            rendered = _render_value(key, fills[key])
        else:
            out.extend(entry)
            continue
        # his comment / blank lines under the entry stay; the value's own lines go
        tail = [line for line in entry[1:] if line.strip() == "" or line.lstrip().startswith("#")]
        out.extend([rendered, *tail])
    out.extend(_render_value(key, fresh[key]) for key in FIELD_ORDER
               if key in COBALT_OWNED_FIELDS and key not in keys)
    out.append(lines[end - 1])
    return "\n".join(out)


# ---------------------------------------------------------------------
# S3 C4 — the fill note, its leg units, the retry (F22, v3 §7)
# ---------------------------------------------------------------------


@dataclass
class CardNoteResult:
    """What `write_card_note` did: the note, its path relative to the vault
    root (`trade_note_path`), the note's action, and each unit's action."""

    path: Path
    relative: str
    action: str
    units: list[tuple[str, str]] = field(default_factory=list)


def _default_writer() -> VaultWriter:
    store = VaultWriteStore()
    store.ensure_schema()
    return VaultWriter(WRITER_NAME, store=store)


def _note_inputs(card_id: int, store) -> tuple[dict[str, Any], list[dict[str, Any]], dict[str, Any], datetime]:
    """(card, current legs, current entry leg, the FILLED time in ET) — reads."""
    from cobalt.cards import legs as legs_mod

    card = store.card_for_note(card_id)
    if card["state"] not in ("FILLED", "CLOSED") or card.get("filled_transition_at") is None:
        raise TradeNoteRefused(
            f"REFUSED card {card_id}: a trade note is written for a FILLED or CLOSED card — it is "
            f"{card['state']}. Nothing written."
        )
    current = legs_mod.read_position(card_id).legs
    entry = next((leg for leg in current if leg["seq"] == legs_mod.ENTRY_SEQ), None)
    if entry is None:
        raise TradeNoteRefused(
            f"REFUSED card {card_id}: filled before C1, it has no entry leg — no fill note is "
            "written for it. Nothing written."
        )
    return card, current, entry, _et(card["filled_transition_at"])


def write_card_note(
    card_id: int,
    *,
    retry: bool = False,
    prefill_paths: Optional[PrefillPathsConfig] = None,
    writer: Optional[VaultWriter] = None,
    store=None,
) -> CardNoteResult:
    """THE fill note (C4-2) and its retry (C4-4) — one function.

    Called only AFTER the fill's transaction committed (never inside it).
    The session gate first (`market_reset` refuses, nothing touched). Then
    the path from the FILLED transition time and `trade_filename_pattern`,
    claimed on `aset_sizings.trade_note_path` through
    `AsetStore.set_trade_note_path` (the intent — a path another card
    already holds is refused, X16); the note through `upsert_trade_note`
    (the fill event: create only — a file already there is another card's,
    refused; the retry: create or update); one `upsert_unit` per current
    leg seq. ANY failure after the gate sets `trade_note_path` NULL and
    re-raises: the caller shows it (L1) with the retry command.
    """
    from cobalt.aset.store import AsetStore
    from cobalt.session import assert_writable

    from .config import load_prefill_paths

    assert_writable("prefill.trade_note", target=str(card_id))
    store = store or AsetStore()
    try:
        paths = prefill_paths or load_prefill_paths()
        card, current, entry, when = _note_inputs(card_id, store)
        relative = trade_note_relative_path(paths, card["ticker"], when)
        store.set_trade_note_path(card_id, relative)
        writer = writer or _default_writer()
        path, action = upsert_trade_note(
            card, when, paths, entry_price=entry["price"], fills=his_fills(card, current),
            legs_section=True, create_only=not retry, writer=writer,
        )
        units = []
        for leg in current:
            unit = leg_unit_id(leg["seq"])
            units.append((unit, writer.upsert_unit(path, LEGS_SECTION, unit, render_leg_line(leg)).action))
        return CardNoteResult(path, relative, action, units)
    except BaseException as failed:
        try:
            store.set_trade_note_path(card_id, None)
        except Exception as cleared:
            raise TradeNoteRefused(
                f"{type(failed).__name__}: {failed} — AND trade_note_path could NOT be set NULL: "
                f"{type(cleared).__name__}: {cleared}"
            ) from failed
        raise


def write_leg_unit(
    card_id: int,
    leg_id: int,
    *,
    closed: bool,
    prefill_paths: Optional[PrefillPathsConfig] = None,
    writer: Optional[VaultWriter] = None,
    store=None,
) -> list[tuple[str, str]]:
    """C4-3: after a leg / correction / held-count commit, the unit
    `leg-<seq>` of the card's note rewritten from `legs_current_v` (a
    correction rewrites the SAME unit). `trade_note_path` NULL, or its
    file absent → refused, nothing written in the vault. A commit that
    CLOSED the card also runs `upsert_trade_note` on the note, so his
    blank exit keys are filled (O5). Returns each write's (unit, action).
    """
    from cobalt.aset.store import AsetStore

    from .config import load_prefill_paths

    store = store or AsetStore()
    paths = prefill_paths or load_prefill_paths()
    card, current, entry, when = _note_inputs(card_id, store)
    relative = card.get("trade_note_path")
    if relative is None:
        raise TradeNoteRefused(f"card {card_id} has no trade note (trade_note_path NULL)")
    rel = Path(relative)
    path = resolve_target(str(rel.parent), rel.name)
    if not path.exists():
        raise TradeNoteRefused(f"card {card_id}'s trade note {relative} is absent")
    leg = next((row for row in current if row["id"] == leg_id), None)
    if leg is None:
        raise TradeNoteRefused(f"leg {leg_id} is not a current leg of card {card_id}")
    writer = writer or _default_writer()
    unit = leg_unit_id(leg["seq"])
    done = [(unit, writer.upsert_unit(path, LEGS_SECTION, unit, render_leg_line(leg)).action)]
    if closed:
        if trade_note_relative_path(paths, card["ticker"], when) != relative:
            raise TradeNoteRefused(
                f"card {card_id}: trade_note_path {relative} is not the FILLED-time note — exit keys not filled"
            )
        _, action = upsert_trade_note(card, when, paths, entry_price=entry["price"],
                                      fills=his_fills(card, current), writer=writer)
        done.append(("frontmatter", action))
    return done
