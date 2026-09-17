"""S2-P4 STEP-7 — the ONE miss line, unit `drc-misses/miss_line` (R5, L28, L8).

The DRC note is never copied into the repo (P2 fixture ruling B): committed
tests render `configs/cobalt/templates/drc.md.j2` exactly as
test_prefill_drc.py does, and write through the real `VaultWriter` into a
tmp dir with an in-memory audit store standing in for `vault_writes` (the
store's own contract is proved in test_vaultwrite.py). The live DRC shape
is read — never written — by the `requires_vault` test the hub runs.
"""

from __future__ import annotations

import os
from contextlib import contextmanager
from datetime import date, datetime, timezone
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.prefill.drc import _render_template
from cobalt.replay import line as line_mod
from cobalt.replay.line import (
    ANCHOR_SECTION,
    SECTION,
    UNIT,
    DrcNoteAbsent,
    after_drc_rules,
    render_line,
    write_miss_line,
)
from cobalt.settings.models import BenchmarkSettings
from cobalt.vaultwrite import VaultWriter
from cobalt.vaultwrite.markers import find_section
from cobalt.vaultwrite.writer import NoteChangedOnDisk, VaultWriteError

DAY = date(2026, 9, 3)
SETTINGS = BenchmarkSettings(top_n=20, min_move_pct=Decimal("10"))

requires_vault = pytest.mark.skipif(
    not os.getenv("COBALT_TEST_LIVE_DRC"),
    reason="requires_vault: COBALT_TEST_LIVE_DRC (a live DRC note path, read only) not set",
)


class MemoryWriteStore:
    """`VaultWriteStore`'s read/write contract, in memory."""

    def __init__(self):
        self.rows: list[dict] = []
        self.overrides: list[dict] = []

    def last_after(self, note, section, unit):
        for row in reversed(self.rows):
            if (row["note"], row["section"], row["unit"]) == (note, section, unit):
                return row["unit_after"]
        return None

    def recent_afters(self, note, section, unit, limit=10):
        hits = [(r["id"], r["unit_after"]) for r in reversed(self.rows)
                if (r["note"], r["section"], r["unit"]) == (note, section, unit)]
        return hits[:limit]

    def get_write(self, write_id):
        return next((r for r in self.rows if r["id"] == write_id), None)

    def purge_expired(self, days=30):
        return 0

    @contextmanager
    def pending_write(self, *, overrides=None, **row):
        row = {**row, "id": len(self.rows) + 1, "ts": datetime(2026, 9, 3, 21, 6, tzinfo=timezone.utc)}
        yield row["id"]
        self.rows.append(row)
        self.overrides.extend(overrides or [])


def drc_text(day: date = DAY) -> str:
    return _render_template({
        "date_str": day.isoformat(),
        "risk_parameters_line": "FULL — A $120 · B $60",
        "tickers_unit": "Cards written: 2 · Trades taken (FILLED): 1",
        "rules_check_block": "- [ ] Card first. #process",
    })


@pytest.fixture
def note(tmp_path):
    path = tmp_path / "DRC-2026-09-03.md"
    path.write_text(drc_text())
    return path


def outside_unit(text: str) -> str:
    """Every byte of the note except the miss-line section."""
    lines = text.split("\n")
    sec = find_section(lines, SECTION)
    if sec is None:
        return text
    return "\n".join(lines[: sec.open_line] + lines[sec.close_line + 1:])


CARDS = [{"excluded_by": "unarmed", "cf_r": Decimal("-1.0139")},
         {"excluded_by": "rule_10", "cf_r": Decimal("-1.0000")},
         {"excluded_by": "unarmed", "cf_r": Decimal("2.5000")}]
MOVERS = [{"ticker": "CTNT", "excluded_by": "not_in_any_source", "gate_detail": {"change_pct": "164.99"}},
          {"ticker": "SNYR", "excluded_by": "config_cap", "gate_detail": {"change_pct": "-58.38"}}]


def body():
    return render_line(DAY, card_rows=CARDS, mover_rows=MOVERS, settings=SETTINGS,
                       formation_replay="unavailable", input_stale=0)


# =====================================================================
# §4 Miss line
# =====================================================================


def test_miss_line_sum_carries_n_and_average_insufficient_below_30():
    text = body()
    assert text == (
        "Misses 2026-09-03: cards 3 (unarmed 2 · passed 0 · not_filled 0 · window 0 · rule_10 1) "
        "· cf-R Σ +0.5R, n=3 · avg: insufficient data (n<30) "
        "· movers ≥ 10%: 2 not in play — CTNT +165.0% not_in_any_source · SNYR −58.4% config_cap "
        "· formations: unavailable until S2-P2"
    )
    thirty = [{"excluded_by": "window", "cf_r": Decimal("-0.5")}] * 30
    full = render_line(DAY, card_rows=thirty, mover_rows=[], settings=SETTINGS,
                       formation_replay="unavailable", input_stale=0)
    assert "cf-R Σ −15.0R, n=30 · avg −0.50R" in full
    assert "insufficient" not in full


def test_line_lists_three_movers_then_counts_the_rest_and_surfaces_input_stale():
    many = [{"ticker": f"T{i}", "excluded_by": "not_in_any_source", "gate_detail": {"change_pct": str(50 - i)}}
            for i in range(5)]
    text = render_line(DAY, card_rows=[], mover_rows=many, settings=SETTINGS,
                       formation_replay="unavailable", input_stale=2)
    assert "5 not in play — T0 +50.0% not_in_any_source · T1 +49.0% not_in_any_source · T2 +48.0% not_in_any_source (+2 more)" in text
    assert "cards 0 (unarmed 0" in text and "input_stale 2" in text


def test_miss_line_upserts_drc_misses_unit_idempotent(note):
    store = MemoryWriteStore()
    first = write_miss_line(note, body(), writer=VaultWriter("replay.nightly", store=store))
    assert first.action == "updated"
    text = note.read_text()
    assert f"<!-- cobalt:section {SECTION} -->" in text and f"<!-- cobalt:unit {UNIT} -->" in text
    second = write_miss_line(note, body(), writer=VaultWriter("replay.nightly", store=store))
    assert second.action == "unchanged"
    assert note.read_text() == text
    assert len(store.rows) == 1


def test_human_edit_to_miss_line_wins_and_logs_override(note):
    store = MemoryWriteStore()
    write_miss_line(note, body(), writer=VaultWriter("replay.nightly", store=store))
    edited = note.read_text().replace("cf-R Σ +0.5R", "cf-R Σ +0.5R (his note: CRWD was news)")
    note.write_text(edited)
    newer = render_line(DAY, card_rows=CARDS[:2], mover_rows=MOVERS, settings=SETTINGS,
                        formation_replay="unavailable", input_stale=0)
    result = write_miss_line(note, newer, writer=VaultWriter("replay.nightly", store=store))
    assert "his note: CRWD was news" in note.read_text()
    assert result.overrides and store.overrides
    assert outside_unit(note.read_text()) == outside_unit(edited)


def test_drc_note_absent_fails_loud_and_creates_nothing(tmp_path, monkeypatch):
    review = tmp_path / "1 - Trading" / "5 - Review"
    review.mkdir(parents=True)
    monkeypatch.setattr(line_mod, "resolve_vault_path", lambda: tmp_path)
    with pytest.raises(DrcNoteAbsent, match="DRC note absent — prefill-drc owns creation"):
        line_mod.drc_note_path(DAY)
    with pytest.raises(DrcNoteAbsent):
        write_miss_line(review / "DRC-2026-09-03.md", body(), writer=VaultWriter("replay.nightly", store=MemoryWriteStore()))
    assert list(review.iterdir()) == []


def test_dry_run_writes_nothing_and_prints_diff(note):
    before = note.read_text()
    store = MemoryWriteStore()
    result = write_miss_line(note, body(), writer=VaultWriter("replay.nightly", store=store, dry_run=True))
    assert result.dry_run and result.diff
    assert "+<!-- cobalt:unit miss_line -->" in result.diff
    assert note.read_text() == before
    assert store.rows == []


# =====================================================================
# R1-18 — zero-width placement and the L28 cases
# =====================================================================


def test_r1_18_first_unit_lands_zero_width_right_after_the_drc_rules_close_marker(note):
    before = note.read_text()
    write_miss_line(note, body(), writer=VaultWriter("replay.nightly", store=MemoryWriteStore()))
    lines = note.read_text().split("\n")
    rules = find_section(lines, ANCHOR_SECTION)
    misses = find_section(lines, SECTION)
    assert misses.open_line == rules.close_line + 1
    assert outside_unit(note.read_text()) == before


def test_r1_18_missing_anchor_appends_at_the_end_and_touches_nothing_above(tmp_path):
    path = tmp_path / "DRC.md"
    human = "# his DRC\n\nNo Cobalt sections yet.\n"
    path.write_text(human)
    result = write_miss_line(path, body(), writer=VaultWriter("replay.nightly", store=MemoryWriteStore()))
    assert path.read_text().startswith(human)
    assert any("anchor not found" in n for n in result.notes)
    assert after_drc_rules().locate(human.split("\n")) is None


def test_r1_18_malformed_marker_refuses_and_changes_no_byte(tmp_path):
    path = tmp_path / "DRC.md"
    broken = drc_text().replace("<!-- /cobalt:section drc-rules -->", "")
    path.write_text(broken)
    with pytest.raises((VaultWriteError, Exception)):
        write_miss_line(path, body(), writer=VaultWriter("replay.nightly", store=MemoryWriteStore()))
    assert path.read_text() == broken


def test_r1_18_sync_revert_takes_cobalt_text_without_an_override(note):
    store = MemoryWriteStore()
    v1 = body()
    write_miss_line(note, v1, writer=VaultWriter("replay.nightly", store=store))
    after_v1 = note.read_text()
    v2 = render_line(DAY, card_rows=CARDS[:1], mover_rows=[], settings=SETTINGS,
                     formation_replay="unavailable", input_stale=0)
    write_miss_line(note, v2, writer=VaultWriter("replay.nightly", store=store))
    note.write_text(after_v1)                                 # Sync puts v1 back
    v3 = render_line(DAY, card_rows=CARDS, mover_rows=[], settings=SETTINGS,
                     formation_replay="unavailable", input_stale=0)
    result = write_miss_line(note, v3, writer=VaultWriter("replay.nightly", store=store))
    assert v3 in note.read_text()
    assert not result.overrides and store.overrides == []
    assert any("SYNC REVERT" in n for n in result.notes)
    assert outside_unit(note.read_text()) == outside_unit(after_v1)


def test_r1_18_mtime_conflict_aborts_and_never_clobbers_the_concurrent_edit(note):
    human_line = "\nhis line typed while the replay ran\n"

    def racer(path: Path) -> None:
        path.write_text(path.read_text() + human_line)

    with pytest.raises(NoteChangedOnDisk):
        write_miss_line(note, body(), writer=VaultWriter("replay.nightly", store=MemoryWriteStore(),
                                                          precommit_hook=racer))
    text = note.read_text()
    assert text.endswith(human_line * 2)
    assert f"cobalt:section {SECTION}" not in text


@requires_vault
def test_live_drc_shape_accepts_the_unit_placement():
    """Hub-run, READ ONLY: the live DRC note has a well-formed drc-rules
    section after which the miss line would land zero-width."""
    live = Path(os.environ["COBALT_TEST_LIVE_DRC"])
    lines = live.read_text(encoding="utf-8").split("\n")
    span = after_drc_rules().locate(lines)
    rules = find_section(lines, ANCHOR_SECTION)
    assert rules is not None, "the live DRC has no drc-rules section"
    assert span == (rules.close_line + 1, rules.close_line + 1)
