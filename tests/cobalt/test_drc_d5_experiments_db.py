"""DRC D5 — the first-gate experiment X11 (v2 `:203`, under R90), card
`prompts/2026-10-04/03-drc-d5-card.md` row X.

A RUN row: it ASSERTS NOTHING. It prints what it observed (`-rP` shows it)
and the report quotes it; a red (the build fails, or the refusal is forced)
is a `DECISION X11` in the report, never fixed here. Run once on the BASE
and once after the rows are built.

v2 X11, verbatim: "cobalt_dev after S3 C2 — a CLOSED card whose export exits
total less than Cobalt's → C2 refuses; the build writes the unresolved-mismatch
row, renders it, and the DRC is built (T7 (i))."

On `cobalt_dev`, inside `migrated`'s never-committed transaction (L76), with
`test_drc_d5_db.py`'s lane (BY IMPORT). Constructed 2001 dates and the
constructed `TEST` symbol only (L32 / L45).
"""

from __future__ import annotations

from cobalt.drc.store import DrcStore

from legs_db_support import card_row, legs_of
from test_drc_build import _note, _unit_body
from test_drc_d5_db import TEST_OPEN, _filled, _listed, _running, _tap, d5_lane  # noqa: F401 — fixture
from test_drc_imports_db import _drop
from test_drc_k1_store import TEN_ET
from test_drc_store import D, STATS, migrated, requires_db, weekday_calendar  # noqa: F401 — fixtures


def _say(**facts) -> None:
    for key, value in facts.items():
        print(f"X11 · {key}: {value}")


@requires_db
def test_x11_run_a_closed_card_whose_export_exits_total_less_than_cobalts(d5_lane, migrated):
    """Cobalt: filled 100, flat 100 → CLOSED. The export: 100 in, 60 out (40
    held). What does the event's build do?"""
    from cobalt.cards import legs
    from cobalt.drc import imports

    root, aset, cards = d5_lane
    card = _filled(aset)
    _tap(card, "flat", 100, "10.20")
    _listed(aset, cards, card)
    imports.state_book(D, [], now=TEN_ET)
    before = legs_of(aset, card)
    try:
        legs.record_correction(before[-1]["id"], shares=60, source="trading_log", source_import_id=1, now=TEN_ET)
        direct = "the writer ACCEPTED a 100 → 60 correction on the CLOSED card"
    except legs.LegRefused as e:
        direct = f"the writer refused: code {e.code} · {e}"
    result = _drop(D, TEST_OPEN, STATS.read_bytes())
    after = legs_of(aset, card)
    stored = next((r for r in DrcStore().rows_for(D) if r["kind"] == "build_day"), None)
    note = _note(root)
    _say(
        writer_called_directly=direct,
        build_status=result.status_line,
        event=DrcStore().event_for(D)["state"],
        legs_before=[(r["id"], r["seq"], r["kind"], r["shares"], r["source"]) for r in before],
        legs_after=[(r["id"], r["seq"], r["kind"], r["shares"], r["source"], r["corrects"]) for r in after],
        running_after=_running(aset, card),
        card_state=card_row(aset, card)["state"],
        stored_unresolved=None if stored is None else stored["derived"].get("unresolved", "no key"),
        reconcile_unit=_unit_body(note, "drc-trades", "reconcile") if note.is_file() else "no note",
        a31_unit=_unit_body(note, "drc-open-items", "open_positions") if note.is_file() else "no note",
    )
