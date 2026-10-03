"""S3 exits C4 — the ONE trade-note writer, offline (F22, v3 §7; L3, L28).

`upsert_trade_note` takes the CARD ROW (+ `when` and the entry price to
write) and serves both origins: `/size` (the sizing note, O4 A) and the
FILL (the fill note, with ONE `cobalt-legs` section after his template
body). His keys are filled ONLY while blank and never overwritten
(O5 / O6 = A, 09-28 R35 (3)): `entry_time` ← the FILLED transition time
(ET), `exit_time` ← the CLOSED transition time (ET), `exit_price` ← the
one confirmed exit leg's price, `trade_def` ← a radar card's slug.
`profit_loss` and `RVOL` stay blank; an absent key is never added.

Every write goes to a `tmp_path` vault through the real `VaultWriter`
with an in-memory audit store. Constructed values only (L32).
"""

from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from types import SimpleNamespace

import pytest

from cobalt.prefill import trade_note as trade_note_module
from cobalt.session import SessionBlocked
from cobalt.vaultwrite.frontmatter import split_frontmatter
from cobalt.vaultwrite.markers import find_section

from trade_note_support import TRADES_DIR, MemoryWriteStore, make_paths, make_vault, memory_writer

FILLED_AT = datetime(2026, 9, 3, 14, 0, 7, tzinfo=timezone.utc)     # 10:00:07 ET
EXIT_AT = datetime(2026, 9, 3, 14, 5, 0, tzinfo=timezone.utc)       # 10:05 ET
CLOSED_AT = datetime(2026, 9, 3, 14, 31, 0, tzinfo=timezone.utc)    # 10:31 ET
RESET = datetime(2026, 9, 3, 0, 30, tzinfo=timezone.utc)            # 20:30 ET — market_reset
FILENAME = "Trade-2026-09-03 10-00-07 -ZZPB.md"
SLUG = "example-range-break"


def card(**over):
    base = dict(id=7, ticker="ZZPB", direction="long", stop=Decimal("5.2000"), entry=Decimal("5.4500"),
                origin="radar", trade_def_slug=SLUG, state="FILLED", filled_transition_at=FILLED_AT,
                closed_transition_at=None, trade_note_path=None)
    base.update(over)
    return base


def manual(**over):
    return card(ticker="ZZPB", origin="manual", trade_def_slug=None, **over)


def leg(**over):
    base = dict(id=1, seq=0, kind="entry", shares=100, price=Decimal("5.4800"), flag="confirmed",
                at=FILLED_AT, preset=None, held_stated=None)
    base.update(over)
    return base


def exit_leg(**over):
    base = dict(id=2, seq=1, kind="exit", shares=50, price=Decimal("5.6000"), flag="confirmed",
                at=EXIT_AT, preset="half", held_stated=None)
    base.update(over)
    return base


def when_of(c):
    from cobalt.session import session_clock

    return session_clock().to_et(c["filled_transition_at"])


def write(c, legs, store, *, create_only=False, legs_section=True, entry_price=Decimal("5.4800"), **kw):
    return trade_note_module.upsert_trade_note(
        c, when_of(c), make_paths(), entry_price=entry_price,
        fills=trade_note_module.his_fills(c, legs), legs_section=legs_section,
        create_only=create_only, writer=memory_writer(store, **kw),
    )


def fm(path):
    front, _ = split_frontmatter(path.read_text())
    return front


@pytest.fixture
def vault(monkeypatch, tmp_path):
    return make_vault(monkeypatch, tmp_path)


# ---------------------------------------------------------------------
# C4-1 — the note created at a fill
# ---------------------------------------------------------------------


def test_a_radar_fill_creates_the_note_at_the_fill_instant(vault):
    store = MemoryWriteStore()
    path, action = write(card(), [leg()], store, create_only=True)
    assert action == "created"
    assert path == vault / TRADES_DIR / FILENAME
    text = path.read_text()
    front = fm(path)
    assert front["date"] == "2026-09-03 10:00"
    assert (front["symbol"], front["direction"]) == ("ZZPB", "Long")
    assert (front["stop_price"], front["entry_price"]) == ("5.2000", "5.4800")   # the FILL price, not the plan
    assert front["entry_time"] == "2026-09-03 10:00"                             # filled while blank
    assert front["trade_def"] == SLUG                                            # a radar card's slug
    for key in ("exit_price", "exit_time", "profit_loss", "RVOL"):
        assert front[key] is None, key
    assert "# Trade: [[Trade-2026-09-03 10-00-07 -ZZPB]]" in text
    body_end = text.index("- What can I do better next time:")
    sec = find_section(text.split("\n"), trade_note_module.LEGS_SECTION)
    assert sec is not None and text.index("<!-- cobalt:section cobalt-legs -->") > body_end
    assert text.count("<!-- cobalt:section cobalt-legs -->") == 1


def test_a_manual_fill_leaves_trade_def_and_the_exit_keys_blank(vault):
    path, _ = write(manual(), [leg()], MemoryWriteStore(), create_only=True)
    front = fm(path)
    assert front["entry_time"] == "2026-09-03 10:00"
    for key in ("trade_def", "exit_price", "exit_time", "profit_loss", "RVOL"):
        assert front[key] is None, key


def test_a_fill_note_that_exists_is_a_collision_never_a_merge(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    before = path.read_text()
    with pytest.raises(trade_note_module.TradeNoteRefused, match="already exists"):
        write(card(id=8, stop=Decimal("5.1000")), [leg(id=9)], store, create_only=True)
    assert path.read_text() == before


# ---------------------------------------------------------------------
# the leg lines (C4-3's unit bodies)
# ---------------------------------------------------------------------


def test_the_leg_lines():
    render = trade_note_module.render_leg_line
    assert render(leg()) == "entry · 100 sh @ 5.4800 · 10:00 · confirmed"
    assert render(exit_leg(flag="estimated")) == "exit half · 50 sh @ 5.6000 · 10:05 · estimated"
    assert render(leg(held_stated=60, shares=110)) == "holding 60 (stated) · 10:00"
    assert trade_note_module.leg_unit_id(3) == "leg-3"


# ---------------------------------------------------------------------
# O5 / O6 = A — filled only while blank, never overwritten
# ---------------------------------------------------------------------


def _closed(c, **over):
    return {**c, "state": "CLOSED", "closed_transition_at": CLOSED_AT, **over}


def test_a_close_through_one_confirmed_exit_leg_fills_exit_price_and_exit_time(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    exits = [exit_leg(shares=100, preset="flat")]
    _, action = write(_closed(card()), [leg(), *exits], store)
    front = fm(path)
    assert action == "updated"
    assert (front["exit_price"], front["exit_time"]) == ("5.6000", "2026-09-03 10:31")
    assert front["profit_loss"] is None and front["RVOL"] is None


def test_a_close_through_two_exit_legs_fills_exit_time_only(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    exits = [exit_leg(), exit_leg(id=3, seq=2, preset="flat", price=Decimal("5.7000"))]
    write(_closed(card()), [leg(), *exits], store)
    front = fm(path)
    assert front["exit_time"] == "2026-09-03 10:31"
    assert front["exit_price"] is None


def test_a_close_through_one_estimated_exit_leg_leaves_exit_price_blank(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    write(_closed(card()), [leg(), exit_leg(shares=100, preset="flat", flag="estimated")], store)
    assert fm(path)["exit_price"] is None


def test_his_exit_price_is_never_overwritten(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    path.write_text(path.read_text().replace("exit_price:\n", 'exit_price: "5.5100"\n'))
    for _ in range(3):   # every later write, the close included
        write(_closed(card()), [leg(), exit_leg(shares=100, preset="flat")], store)
        assert fm(path)["exit_price"] == "5.5100"
    assert 'exit_price: "5.5100"' in path.read_text()


def test_a_value_cobalt_filled_is_never_rewritten(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    later = card(filled_transition_at=datetime(2026, 9, 3, 14, 20, tzinfo=timezone.utc))
    fills = trade_note_module.his_fills(later, [leg()])
    assert fills["entry_time"] == "2026-09-03 10:20"
    trade_note_module.upsert_trade_note(card(), when_of(card()), make_paths(), entry_price=Decimal("5.4800"),
                                        fills=fills, writer=memory_writer(store))
    assert fm(path)["entry_time"] == "2026-09-03 10:00"


def test_his_trade_def_is_never_overwritten(vault):
    store = MemoryWriteStore()
    path, _ = write(manual(), [leg()], store, create_only=True)
    path.write_text(path.read_text().replace("trade_def:\n", "trade_def: example-his-own\n"))
    write(_closed(card()), [leg(), exit_leg(shares=100, preset="flat")], store)
    assert fm(path)["trade_def"] == "example-his-own"


def test_a_key_absent_from_the_file_is_never_added(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    path.write_text(path.read_text().replace("exit_time:\n", ""))
    write(_closed(card()), [leg(), exit_leg(shares=100, preset="flat")], store)
    front = fm(path)
    assert "exit_time" not in front
    assert front["exit_price"] == "5.6000"


def test_profit_loss_and_rvol_are_never_written(vault):
    fills = trade_note_module.his_fills(_closed(card()), [leg(), exit_leg(shares=100, preset="flat")])
    assert set(fills) <= {"entry_time", "exit_time", "exit_price", "trade_def"}


# ---------------------------------------------------------------------
# /size (O4 A) through the SAME writer; the session gate
# ---------------------------------------------------------------------


def test_the_sizing_note_is_written_by_the_same_writer_from_the_card(vault):
    """/size's call: the card's values, the planned entry, no fills, no
    legs section — the sizing note exactly as before C4."""
    when = datetime(2026, 8, 31, 9, 31, 5)
    sized = {"ticker": "NVDA", "direction": "long", "stop": Decimal("225.00"), "trade_def_slug": None}
    path, action = trade_note_module.upsert_trade_note(sized, when, make_paths(), entry_price=Decimal("227.98"),
                                                       writer=memory_writer())
    text = path.read_text()
    assert (action, path.name) == ("created", "Trade-2026-08-31 09-31-05 -NVDA.md")
    assert 'stop_price: "225.00"' in text and 'entry_price: "227.98"' in text
    assert "entry_time:\n" in text and "trade_def:\n" in text
    assert "cobalt:section" not in text


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
def test_size_route_passes_the_card_to_the_one_writer(monkeypatch, vault):
    """POST /size → `upsert_trade_note(card, when, paths, entry_price=…)`."""
    from fastapi.testclient import TestClient

    from cobalt.aset import web as web_module
    from test_aset_web import BASE_SIZE_FORM, _offline_daymode_config, _offline_sheet_modes_config

    cfg = _offline_daymode_config()
    monkeypatch.setenv("COBALT_ALLOW_DEV_ENTRY", "1")
    monkeypatch.setattr(web_module, "load_sheet_modes_config", _offline_sheet_modes_config)
    monkeypatch.setattr(web_module, "_daymode_state", lambda: {
        "cfg": cfg, "day": None, "row": {"attested_sheet": cfg.hotkey_file_for_mode(cfg.lowest_enabled)},
        "mode": cfg.lowest_enabled, "stage": "stage 1", "error": None})

    class Store:
        db_name = "cobalt_dev"

        def __init__(self, db_name=None):
            pass

        def ensure_schema(self):
            pass

        def save(self, result):
            return 4242

        def account_mode_for(self, row_id):
            return "sim"

    seen = {}

    def one_writer(c, when, paths, **kw):
        seen.update(card=c, when=when, **kw)
        return vault / TRADES_DIR / "sizing.md", "created"

    monkeypatch.setattr(web_module, "AsetStore", Store)
    monkeypatch.setattr(web_module, "save_card", lambda cfg, result: (
        "/dev/daily.md", datetime(2026, 9, 3, 10, 0, 7), SimpleNamespace(action="appended", unit="u")))
    monkeypatch.setattr(web_module, "upsert_trade_note", one_writer)
    r = TestClient(web_module.app).post("/size", data=BASE_SIZE_FORM)
    assert "trade note created" in r.text, r.text[-2000:]
    assert seen["card"]["ticker"] == "NVDA" and seen["card"]["id"] == 4242
    assert seen["entry_price"] == Decimal("218.595")
    assert not seen.get("fills") and not seen.get("legs_section")


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
def test_market_reset_refuses_the_note_write(vault):
    store = MemoryWriteStore()
    with pytest.raises(SessionBlocked):
        write(card(), [leg()], store, create_only=True, now=lambda: RESET)
    assert list((vault / TRADES_DIR).iterdir()) == []
    assert store.rows == []


# ---------------------------------------------------------------------
# C4 fix r1 — F1: the test guard (conftest `trade_note_path_guard`)
# ---------------------------------------------------------------------


def test_a_trade_note_path_outside_tmp_path_fails_loud(trade_note_path_guard):
    with pytest.raises(AssertionError, match="outside tmp_path"):
        trade_note_module.resolve_target(TRADES_DIR, "x.md")
    assert len(trade_note_path_guard) == 1
    trade_note_path_guard.clear()   # tripped on purpose; the teardown then passes


# ---------------------------------------------------------------------
# C4 fix r1 — RUN U2 (L70): run, never argued. It PRINTS what happened
# and asserts NOTHING about the outcome.
# ---------------------------------------------------------------------


def _line(path, key):
    return next((line for line in path.read_text().split("\n") if line.startswith(f"{key}:")), None)


def test_run_u2_a_typed_exit_price_after_a_later_write(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    path.write_text(path.read_text().replace("exit_price:\n", "exit_price: 5.10\n"))   # the test's hand edit
    before = _line(path, "exit_price")
    _, action = write(_closed(card()), [leg(), exit_leg(shares=100, preset="flat")], store)
    print(f"\nRUN U2 · close write {action} (one confirmed exit leg @ 5.6000)")
    print(f"U2 exit_price before: {before!r}")
    print(f"U2 exit_price after:  {_line(path, 'exit_price')!r}")
    print(f"U2 entry_time after:  {_line(path, 'entry_time')!r}")
    print(f"U2 exit_time after:   {_line(path, 'exit_time')!r}")


# ---------------------------------------------------------------------
# C4 fix r2 — B1: a later Cobalt write keeps every byte of his
# frontmatter lines (L28 "human text preserved verbatim"; R35 (3)).
# Only Cobalt's five and a blank key it fills are rendered.
# ---------------------------------------------------------------------


def _block(path):
    """The frontmatter's raw lines, between the two `---`."""
    lines = path.read_text().split("\n")
    return lines[1:lines.index("---", 1)]


def _set_line(path, old, new):
    text = path.read_text()
    assert text.count(old) == 1, old
    path.write_text(text.replace(old, new))


def _replace_block(path, block):
    lines = path.read_text().split("\n")
    path.write_text("\n".join(["---", *block, *lines[lines.index("---", 1):]]))


def _his_lines(block):
    return [line for line in block if line.split(":", 1)[0] not in trade_note_module.COBALT_OWNED_FIELDS]


def _close(store, c=None):
    return write(_closed(c or card()), [leg(), exit_leg(shares=100, preset="flat")], store)


#: His block (constructed): `trade_def` above `date`, his own keys, a
#: comment, flow lists, numbers YAML would re-read as floats.
HIS_BLOCK = [
    f"trade_def: {SLUG}",
    "date: 2026-09-03 10:00",
    "symbol: ZZPB",
    "direction: Long",
    "# a constructed comment",
    'stop_price: "5.2000"',
    'entry_price: "5.4800"',
    "exit_price:",
    'entry_time: "2026-09-03 10:00"',
    "exit_time:",
    "profit_loss: -120.50",
    "setup: [a, b]",
    "RVOL: 3.50",
    "tags: [trade, example]",
]
HIS_OWN = [f"trade_def: {SLUG}", "# a constructed comment", "profit_loss: -120.50", "setup: [a, b]",
           "RVOL: 3.50", "tags: [trade, example]"]


def test_his_typed_exit_price_keeps_its_bytes_after_the_close_write(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    _set_line(path, "exit_price:\n", "exit_price: 5.10\n")
    before = _block(path)
    _, action = _close(store)
    assert action == "updated"
    assert _line(path, "exit_price") == "exit_price: 5.10"
    # every line but Cobalt's five as before — the blank exit_time filled (N pins that side)
    expected = [line if line != "exit_time:" else 'exit_time: "2026-09-03 10:31"' for line in _his_lines(before)]
    assert _his_lines(_block(path)) == expected


def test_his_edit_of_a_value_cobalt_filled_keeps_its_bytes(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    assert _line(path, "entry_time") == 'entry_time: "2026-09-03 10:00"'   # Cobalt filled it at creation
    _set_line(path, 'entry_time: "2026-09-03 10:00"\n', "entry_time: 2026-09-03 10:02\n")
    _close(store)
    assert _line(path, "entry_time") == "entry_time: 2026-09-03 10:02"


def test_his_typed_exit_time_keeps_its_bytes(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    _set_line(path, "exit_time:\n", "exit_time: 10:31\n")
    _close(store)
    assert _line(path, "exit_time") == "exit_time: 10:31"


def test_his_own_lines_keep_their_bytes_and_order(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    _replace_block(path, HIS_BLOCK)
    _close(store)
    assert [line for line in _block(path) if line in HIS_OWN] == HIS_OWN


def test_the_size_write_keeps_his_typed_exit_price_bytes(vault):
    """/size's call shape (`web.py:1047`): no fills, no legs section."""
    store = MemoryWriteStore()

    def size():
        return trade_note_module.upsert_trade_note(card(), when_of(card()), make_paths(),
                                                   entry_price=Decimal("5.4500"), writer=memory_writer(store))

    path, action = size()
    assert action == "created"
    _set_line(path, "exit_price:\n", "exit_price: 5.10\n")
    before = _block(path)
    size()
    assert _line(path, "exit_price") == "exit_price: 5.10"
    assert _block(path) == before


def test_a_frontmatter_the_line_merge_cannot_map_is_refused_untouched(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    _replace_block(path, ['{date: "2026-09-03 10:00", symbol: ZZPB, exit_price: 5.10}'])   # a flow mapping
    before = path.read_bytes()
    with pytest.raises(trade_note_module.VaultWriteError, match="refusing to guess at its shape"):
        _close(store)
    assert path.read_bytes() == before


def test_the_merge_still_refreshes_cobalts_five_and_fills_a_blank(vault):
    """The negative control: B1-4's block, Cobalt's side still written."""
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    _replace_block(path, HIS_BLOCK)
    _close(store, card(stop=Decimal("5.1000")))
    assert _line(path, "stop_price") == 'stop_price: "5.1000"'
    assert _line(path, "exit_price") == 'exit_price: "5.6000"'
    assert _line(path, "exit_time") == 'exit_time: "2026-09-03 10:31"'


# ---------------------------------------------------------------------
# E1 (09-30 R3) — a comment he INDENTS under an entry Cobalt replaces or
# fills is his and is kept, like a column-0 comment and a blank line.
# ---------------------------------------------------------------------

#: His block (constructed): an indented comment before any entry, under a
#: Cobalt-owned entry (with a blank line), under a blank key Cobalt fills;
#: a Cobalt-owned entry and a filled key with a column-0 comment or nothing
#: under them.
E1_BLOCK = [
    "  # a constructed comment before any entry",
    f"trade_def: {SLUG}",
    "date: 2026-09-03 10:00",
    "symbol: ZZPB",
    'direction: "Long"',
    'stop_price: "5.2000"',
    "  # typed at close",
    "",
    'entry_price: "5.4800"',
    "exit_price:",
    "  # a constructed comment under a blank key",
    'entry_time: "2026-09-03 10:00"',
    "exit_time:",
    "# a constructed column-0 comment",
    "profit_loss: -120.50",
    "RVOL: 3.50",
    "tags: [trade, example]",
]


def test_an_indented_comment_under_a_replaced_entry_is_kept(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    _replace_block(path, E1_BLOCK)
    _close(store, card(stop=Decimal("5.1000")))
    replaced = {'stop_price: "5.2000"': 'stop_price: "5.1000"', "exit_price:": 'exit_price: "5.6000"',
                "exit_time:": 'exit_time: "2026-09-03 10:31"'}
    assert _block(path) == [replaced.get(line, line) for line in E1_BLOCK]


def test_a_value_line_he_typed_that_starts_with_a_hash_stays_as_a_line(vault):
    """A Cobalt-owned key he retyped as a block scalar whose text starts
    with `#`: the entry is refreshed, his `#` line stays under it (YAML
    then reads it as a comment) — no line of his that starts with `#` is
    deleted."""
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    block = [line for line in E1_BLOCK if line != "symbol: ZZPB"]
    block[3:3] = ["symbol: |", "  #ZZPB"]
    _replace_block(path, block)
    assert fm(path)["symbol"] == "#ZZPB\n"
    _close(store)
    assert _block(path)[3:5] == ["symbol: ZZPB", "  #ZZPB"]
    assert fm(path)["symbol"] == "ZZPB"


# ---------------------------------------------------------------------
# E1 follow-up (09-30 R74) — a comment he types at the END of the line of
# an entry Cobalt replaces or fills is his and is kept after the new value,
# spacing as he typed it. A `#` inside quotes is his value, never a comment.
# ---------------------------------------------------------------------


def test_an_inline_comment_on_a_replaced_entrys_line_is_kept(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    _set_line(path, 'stop_price: "5.2000"\n', 'stop_price: "5.2000"  # typed by him\n')
    _set_line(path, "exit_time:\n", "exit_time:   # typed by him\n")   # a blank key Cobalt fills
    _close(store, card(stop=Decimal("5.1000")))
    assert _line(path, "stop_price") == 'stop_price: "5.1000"  # typed by him'
    assert _line(path, "exit_time") == 'exit_time: "2026-09-03 10:31"   # typed by him'
    assert fm(path)["stop_price"] == "5.1000"


def test_a_hash_inside_quotes_is_his_value_and_never_a_comment(vault):
    """The negative control: the ` #` inside his quotes is text, so the
    replaced line gains no comment and his own quoted value keeps every byte."""
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    _set_line(path, 'stop_price: "5.2000"\n', 'stop_price: "5.2000 # not a comment"\n')
    _set_line(path, "profit_loss:\n", "profit_loss: 'a # b'  # his note\n")
    assert fm(path)["stop_price"] == "5.2000 # not a comment"
    _close(store, card(stop=Decimal("5.1000")))
    assert _line(path, "stop_price") == 'stop_price: "5.1000"'
    assert _line(path, "profit_loss") == "profit_loss: 'a # b'  # his note"


def test_a_hash_inside_quotes_after_a_tag_is_never_taken_as_a_comment(vault):
    store = MemoryWriteStore()
    path, _ = write(card(), [leg()], store, create_only=True)
    _set_line(path, 'stop_price: "5.2000"\n', 'stop_price: !!str "5.2000 # not a comment"\n')
    assert fm(path)["stop_price"] == "5.2000 # not a comment"
    _close(store, card(stop=Decimal("5.1000")))
    assert _line(path, "stop_price") == 'stop_price: "5.1000"'
