"""S3 exits C4 — E1 experiments, run BEFORE any src edit (L70).

X14  `_render_body` vs his Individual Trade Template's body, through a
     stripped real-shape fixture (L45 / L32: headings and structure lines
     byte-identical, his prose and his slug list replaced). The live leg
     reads his template READ ONLY when `COBALT_LIVE_VAULT_ROOT` is set.
X3   create-if-absent twice, a `leg-0` unit, his hand edit, a retry, and a
     retry racing a leg write on the same note.
X16  two cards, one ticker, fill instants in the same second.

Every write goes to a `tmp_path` vault through the real `VaultWriter` with
an in-memory audit store. Constructed values only.
"""

from __future__ import annotations

import os
import re
from datetime import datetime
from pathlib import Path

import pytest

from cobalt.prefill import trade_note as trade_note_module
from cobalt.vaultwrite.markers import find_section
from cobalt.vaultwrite.writer import NoteChangedOnDisk  # noqa: F401  (the race's abort type)

from trade_note_support import TRADES_DIR, MemoryWriteStore, make_paths, make_vault, memory_writer

FIXTURE = Path(__file__).resolve().parents[1] / "fixtures" / "trade_note" / "individual-trade-template.stripped.md"
TEMPLATE_REL = Path("5 - Templates") / "Individual Trade Template.md"

requires_live = pytest.mark.skipif(
    not os.getenv("COBALT_LIVE_VAULT_ROOT"),
    reason="COBALT_LIVE_VAULT_ROOT not set — the hub runs the live template read",
)


# ---------------------------------------------------------------------
# X14 — the body copy vs his template
# ---------------------------------------------------------------------

_KEY_VALUE = re.compile(r"^([A-Za-z_]+):\s*(.*)$")
_PROSE = re.compile(r"^(\t+- )\[.*\]$")
_TITLE = re.compile(r"^# Trade: \[\[.*\]\]$")


def strip_template(text: str) -> list[str]:
    """His template reduced to its shape: frontmatter keys kept, every value
    replaced; the title link, and every bracketed prose line, replaced."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    out, fences = [], 0
    for line in lines:
        if line.strip() == "---":
            fences += 1
            out.append(line)
            continue
        if fences == 1:
            m = _KEY_VALUE.match(line)
            if m and m.group(2):
                out.append(f"{m.group(1)}: <stripped>")
                continue
            out.append(line)
            continue
        if _TITLE.match(line):
            out.append("# Trade: [[<title>]]")
            continue
        m = _PROSE.match(line)
        out.append(f"{m.group(1)}[<prose>]" if m else line)
    return out


def _body_of(lines: list[str]) -> list[str]:
    closing = [i for i, line in enumerate(lines) if line.strip() == "---"][1]
    return lines[closing + 1:]


def test_x14_the_code_body_is_the_templates_body_shape():
    fixture = FIXTURE.read_text(encoding="utf-8").split("\n")
    if fixture[-1] == "":
        fixture = fixture[:-1]
    rendered = strip_template(trade_note_module._render_body("Trade-2026-09-03 10-00-00 -TEST"))
    assert rendered == _body_of(fixture)


def test_x14_the_frontmatter_key_order_is_field_order():
    fixture = FIXTURE.read_text(encoding="utf-8").split("\n")
    closing = [i for i, line in enumerate(fixture) if line.strip() == "---"][1]
    keys = [m.group(1) for line in fixture[1:closing] if (m := _KEY_VALUE.match(line))]
    assert tuple(keys) == trade_note_module.FIELD_ORDER


@requires_live
def test_x14_live_his_template_strips_to_the_committed_fixture():
    """READ ONLY: his template, stripped, equals the committed fixture — a
    change to his template fails here before it reaches production (L45)."""
    template = Path(os.environ["COBALT_LIVE_VAULT_ROOT"]) / TEMPLATE_REL
    fixture = FIXTURE.read_text(encoding="utf-8").split("\n")
    if fixture[-1] == "":
        fixture = fixture[:-1]
    assert strip_template(template.read_text(encoding="utf-8")) == fixture


# ---------------------------------------------------------------------
# X3 — create twice, a unit, his edit, a retry, a retry racing a leg write
# ---------------------------------------------------------------------

SECTION = "cobalt-legs"
TEMPLATE = "---\nsymbol: TEST\n---\n# Trade: [[t]]\n\n<!-- cobalt:section cobalt-legs -->\n<!-- /cobalt:section cobalt-legs -->\n"


def test_x3_create_twice_unit_edit_retry_and_race(monkeypatch, tmp_path):
    vault = make_vault(monkeypatch, tmp_path)
    path = vault / TRADES_DIR / "Trade-2026-09-03 10-00-00 -TEST.md"
    store = MemoryWriteStore()
    writer = memory_writer(store)

    first = writer.create_if_absent(path, TEMPLATE)
    second = writer.create_if_absent(path, TEMPLATE + "a second body\n")
    assert (first.action, second.action) == ("created", "skipped_exists")
    assert path.read_text().count("# Trade:") == 1

    writer.upsert_unit(path, SECTION, "leg-0", "entry · 100 sh @ 10.0000 · 10:00 · confirmed")
    # his hand edit of Cobalt's line
    path.write_text(path.read_text().replace("100 sh @ 10.0000", "100 sh @ 10.0100 (my fill)"))

    # the retry (C4-4's path): the same create + the same unit, once more
    retry_writer = memory_writer(store)
    assert retry_writer.create_if_absent(path, TEMPLATE).action == "skipped_exists"
    retried = retry_writer.upsert_unit(path, SECTION, "leg-0", "entry · 100 sh @ 10.0000 · 10:00 · confirmed")
    text = path.read_text()
    assert "100 sh @ 10.0100 (my fill)" in text          # his edit survives
    assert text.count("<!-- cobalt:unit leg-0 -->") == 1
    assert [o.human for o in retried.overrides] == [("entry · 100 sh @ 10.0100 (my fill) · 10:00 · confirmed",)]
    overrides_after_retry = len(store.overrides)

    # the retry racing a leg write: a leg-1 write lands in the gap of the
    # retry's leg-0 write -> the retry aborts loudly, re-reads, retries once
    leg_writer = memory_writer(store)

    def racer(_path):
        racer.fired += 1
        if racer.fired == 1:
            leg_writer.upsert_unit(path, SECTION, "leg-1", "exit half · 50 sh @ 10.2000 · 10:05 · confirmed")

    racer.fired = 0
    racing = memory_writer(store, precommit_hook=racer)
    raced = racing.upsert_unit(path, SECTION, "leg-0", "entry · 100 sh @ 10.0000 · 10:00 · confirmed")
    text = path.read_text()
    sec = find_section(text.split("\n"), SECTION)
    assert sorted(sec.units) == ["leg-0", "leg-1"]
    assert text.count("<!-- cobalt:unit leg-0 -->") == 1 and text.count("<!-- cobalt:unit leg-1 -->") == 1
    assert text.count("# Trade:") == 1                   # no duplicated body
    assert racer.fired == 2                              # aborted once, re-read, retried once
    assert len(store.overrides) == overrides_after_retry  # the recorded override row is kept
    his_line_kept = "100 sh @ 10.0100 (my fill)" in text
    print(f"\nX3 race: {raced.action} · racer fired {racer.fired} · override rows {len(store.overrides)} · "
          f"write rows {len(store.rows)} · his leg-0 line kept: {his_line_kept} · final leg-0 "
          f"{sec.units['leg-0'].body(text.split(chr(10)))!r}")
    # MEASURED (design-changing: yes, ESCALATE): human wins ONCE. The write
    # that records his override stores HIS text as the unit's baseline
    # (`unit_after` = the merged body), so the NEXT write of the same unit
    # — here the second retry, carrying Cobalt's unchanged body — sees
    # base == on-disk, takes Cobalt's body, and replaces his line with no
    # new override row. Not the race: the same holds without the racer.
    assert not his_line_kept
    assert "entry · 100 sh @ 10.0000 · 10:00 · confirmed" in text


def test_x3_human_wins_once_without_a_race(monkeypatch, tmp_path):
    """The X3 finding with no racer: his edit, the first retry (override
    recorded, his line kept), the second retry (his line replaced)."""
    vault = make_vault(monkeypatch, tmp_path)
    path = vault / TRADES_DIR / "Trade-2026-09-03 10-00-00 -TEST.md"
    store = MemoryWriteStore()
    body = "entry · 100 sh @ 10.0000 · 10:00 · confirmed"
    memory_writer(store).create_if_absent(path, TEMPLATE)
    memory_writer(store).upsert_unit(path, SECTION, "leg-0", body)
    path.write_text(path.read_text().replace("10.0000", "10.0100 (my fill)"))
    first = memory_writer(store).upsert_unit(path, SECTION, "leg-0", body)
    kept_after_first = "(my fill)" in path.read_text()
    second = memory_writer(store).upsert_unit(path, SECTION, "leg-0", body)
    kept_after_second = "(my fill)" in path.read_text()
    print(f"\nX3 no race: retry 1 {first.action} kept={kept_after_first} overrides={len(first.overrides)} · "
          f"retry 2 {second.action} kept={kept_after_second} overrides={len(second.overrides)}")
    assert (kept_after_first, kept_after_second) == (True, False)
    assert (len(first.overrides), len(second.overrides)) == (1, 0)


# ---------------------------------------------------------------------
# X16 — two cards, one ticker, the same second
# ---------------------------------------------------------------------


def test_x16_two_cards_same_ticker_same_second(monkeypatch, tmp_path):
    """X16, run at E1 on `<base>` with the `SizingResult` signature:
    `created …` then `updated …` — the second card MERGED into the first
    card's note (quoted in the build report). Kept on the converted writer:
    without `create_only` the writer still merges; the fill event passes
    `create_only`, and the second card is refused, never merged (C4-2)."""
    from decimal import Decimal

    make_vault(monkeypatch, tmp_path)
    when = datetime(2026, 9, 3, 10, 12, 30)
    store = MemoryWriteStore()
    first = {"ticker": "TEST", "direction": "long", "stop": Decimal("9.9000")}
    second = {"ticker": "TEST", "direction": "long", "stop": Decimal("10.9000")}
    write = trade_note_module.upsert_trade_note
    path1, action1 = write(first, when, make_paths(), entry_price=Decimal("10.0000"), writer=memory_writer(store))
    path2, action2 = write(second, when, make_paths(), entry_price=Decimal("11.0000"), writer=memory_writer(store))
    print(f"\nX16 writer: {action1} {path1.name} · {action2} {path2.name}")
    assert path1 == path2 and (action1, action2) == ("created", "updated")
    with pytest.raises(trade_note_module.TradeNoteRefused, match="already exists"):
        write(second, when, make_paths(), entry_price=Decimal("11.0000"), create_only=True,
              writer=memory_writer(store))
