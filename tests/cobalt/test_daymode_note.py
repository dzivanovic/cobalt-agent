"""F6 in the daily note, both directions (S1-P3, CTO review of S1-P2).

What this replaces is the point of the file: `prefill/daily.py` used to
render one static line —

    "Sheet mode: [ ] FULL [ ] HALF — .htk loaded: [ ] full [ ] half"

— four checkboxes nothing read. The unit that stands in its place is
Cobalt-owned (L28: markers, stable id, update in place, versioned,
diffed) and is read BACK: a box he ticks in Obsidian is an attestation.

The three things this has to prove:

1. Cobalt -> note: the decided mode and the attestation land in the
   note, in place, on a second write (one unit, not two copies).
2. note -> Cobalt: a tick with nothing on record IS the attestation.
3. a disagreement between the two is a REFUSAL showing both, never a
   merge — and two ticks is the same refusal for the same reason.
"""

import os
from datetime import date
from decimal import Decimal

import pytest

from cobalt.aset.config import AsetConfig, SheetModeGrades, SheetModesConfig
from cobalt.aset.models import Grade
from cobalt.daymode import note as note_mod
from cobalt.daymode.config import DayModeConfig
from cobalt.prefill import vault_writer as vault_writer_module
from cobalt.vaultwrite import VaultWriteStore

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

_GRADES = {"A_plus": 170, "A": 70, "B": 30, "C": 11, "D": 0}

_STEPDOWNS = [
    {"signal": "daily_stop_hit", "effect": "floor", "because": "daily stop"},
    {"signal": "no_prior_drc", "effect": "down", "because": "no prior DRC"},
    {"signal": "drc_not_informative", "effect": "down", "because": "blank DRC"},
    {"signal": "early_close_today", "effect": "down", "because": "early close"},
    {"signal": "first_session_after_close", "effect": "down", "because": "after a close"},
    {"signal": "trade_count_band_placeholder", "effect": "floor", "because": "band unruled"},
]


def _cfg(order=("half", "full")) -> DayModeConfig:
    sheets = SheetModesConfig(
        sheets={name: SheetModeGrades(**_GRADES) for name in order},
        order=list(order),
        enabled_grades=[Grade.A, Grade.B],
    )
    return DayModeConfig(
        reduced_sheet=order[0],
        reduced_enabled_grades=[Grade.A, Grade.B],
        enabled_modes=["reduced"],
        hotkey_file_template="{sheet}.htk",
        stepdowns=[dict(s) for s in _STEPDOWNS],
        sheet_order=list(sheets.order),
        account_enabled_grades=list(sheets.enabled_grades),
    )


NOTE_TEMPLATE = """---
tags:
  - Daily
---
## Today's Plan

<!-- cobalt:section daymode -->
<!-- cobalt:unit sheet_mode -->
(not written yet)
<!-- /cobalt:unit sheet_mode -->
<!-- /cobalt:section daymode -->

### Market Context:
- his own line, which must survive every write
"""


@pytest.fixture
def note_path(tmp_path, monkeypatch):
    vault_root = tmp_path / "vault"
    notes = vault_root / "1 - Trading" / "1- Daily Notes"
    notes.mkdir(parents=True)
    monkeypatch.setattr(vault_writer_module, "resolve_vault_path", lambda: vault_root)
    path = notes / "2026-09-03.md"
    path.write_text(NOTE_TEMPLATE, encoding="utf-8")
    return path


# =====================================================================
# 1. Cobalt -> note
# =====================================================================


class TestRenderBody:
    def test_it_names_the_mode_the_sheet_and_the_keys(self):
        body = note_mod.render_body(
            _cfg(), "reduced", stage="stage 1 (system rule, pre-09:00)"
        )
        assert "**Day mode: REDUCED**" in body
        assert "HALF sheet" in body
        assert "keys A, B" in body

    def test_one_checkbox_per_declared_sheet_derived_from_config(self):
        body = note_mod.render_body(_cfg(("quarter", "half", "full")), "reduced", stage="s")
        assert "- [ ] quarter.htk" in body
        assert "- [ ] half.htk" in body
        assert "- [ ] full.htk" in body

    def test_the_attested_file_is_the_ticked_one(self):
        body = note_mod.render_body(_cfg(), "reduced", stage="s", attested="full.htk")
        assert "- [x] full.htk" in body
        assert "- [ ] half.htk" in body


@requires_db
@pytest.mark.integration
class TestWriteIntoTheNote:
    def test_the_unit_is_updated_in_place_not_appended_twice(self, note_path):
        store = VaultWriteStore()
        store.ensure_schema()
        cfg = _cfg()

        first = note_mod.write(
            note_path, cfg, "reduced", stage="stage 1", attested="half.htk", store=store
        )
        assert first.action == "updated"
        assert first.diff, "L28.4: every write carries its unified diff"

        second = note_mod.write(
            note_path, cfg, "reduced", stage="stage 1", attested="full.htk", store=store
        )
        text = note_path.read_text(encoding="utf-8")
        assert second.action == "updated"
        assert text.count("<!-- cobalt:unit sheet_mode -->") == 1, (
            "the same unit id updates in place; a second copy is the damage "
            "L28 exists to prevent"
        )
        assert "- [x] full.htk" in text
        assert "his own line, which must survive every write" in text

    def test_a_missing_note_is_reported_not_created(self, tmp_path, monkeypatch):
        monkeypatch.setattr(vault_writer_module, "resolve_vault_path", lambda: tmp_path)
        missing = tmp_path / "1 - Trading" / "1- Daily Notes" / "nope.md"
        assert note_mod.write(missing, _cfg(), "reduced", stage="s") is None, (
            "L28.1: only create_if_absent may create a note; this writer never does"
        )


# =====================================================================
# 2. note -> Cobalt
# =====================================================================


class TestReadAttestation:
    def _note(self, *ticks: str) -> str:
        lines = ["<!-- cobalt:section daymode -->", "<!-- cobalt:unit sheet_mode -->"]
        for name in ("half.htk", "full.htk"):
            lines.append(f"- [{'x' if name in ticks else ' '}] {name}")
        lines += ["<!-- /cobalt:unit sheet_mode -->", "<!-- /cobalt:section daymode -->"]
        return "\n".join(lines)

    def test_a_ticked_box_is_read_back(self):
        got = note_mod.read_attestation(self._note("full.htk"), _cfg())
        assert got.file == "full.htk"
        assert got.ticked == ["full.htk"]

    def test_nothing_ticked_is_no_attestation_not_a_default(self):
        got = note_mod.read_attestation(self._note(), _cfg())
        assert got.file is None and got.ticked == []

    def test_no_unit_at_all_is_silent(self):
        assert note_mod.read_attestation("# just a note\n", _cfg()).ticked == []

    def test_a_ticked_box_outside_the_unit_is_ignored(self):
        """A checkbox in his journal is his prose. Reading it would make
        any line containing `[x] full.htk` a risk decision."""
        text = "- [x] full.htk\n" + self._note()
        assert note_mod.read_attestation(text, _cfg()).ticked == []

    def test_a_file_naming_no_declared_sheet_is_not_an_attestation(self):
        text = self._note().replace("- [ ] full.htk", "- [x] reduced_day.htk")
        assert note_mod.read_attestation(text, _cfg()).ticked == []


class TestReconcile:
    def test_a_tick_with_nothing_on_record_becomes_the_attestation(self):
        note = note_mod.NoteAttestation(file="full.htk", ticked=["full.htk"])
        assert note_mod.reconcile(note, None) == "full.htk"

    def test_silence_in_the_note_leaves_the_record_alone(self):
        note = note_mod.NoteAttestation(file=None, ticked=[])
        assert note_mod.reconcile(note, "half.htk") == "half.htk"

    def test_agreement_is_agreement(self):
        note = note_mod.NoteAttestation(file="half.htk", ticked=["half.htk"])
        assert note_mod.reconcile(note, "half.htk") == "half.htk"

    def test_a_disagreement_refuses_and_shows_both(self):
        note = note_mod.NoteAttestation(file="half.htk", ticked=["half.htk"])
        with pytest.raises(note_mod.NoteAttestationConflict) as excinfo:
            note_mod.reconcile(note, "full.htk")
        message = str(excinfo.value)
        assert "half.htk" in message and "full.htk" in message, (
            "the refusal names BOTH sides — picking one silently is how a "
            "full-size key gets pressed on a reduced-size day"
        )

    def test_two_ticks_is_no_claim_at_all(self):
        note = note_mod.NoteAttestation(file=None, ticked=["half.htk", "full.htk"])
        with pytest.raises(note_mod.NoteAttestationConflict, match="2 hotkey files"):
            note_mod.reconcile(note, None)
