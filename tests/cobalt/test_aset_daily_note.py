"""Daily-note writer tests: safety gate + append-only + stub-on-create.

The vault resolver is monkeypatched to a pytest tmp_path for every test
here — genuinely outside the repo tree, so these tests exercise the
REAL "outside the repo" invariant without touching Dejan's real vault.

Iteration 4 (ruled by Dejan, 2026-08-28): save_card now returns
(path, when) — the canonical card timestamp threads forward to a later
save_fill_update() call for FILL UPDATE linkage. Cards carry sheet_mode,
not daily_stop/grade-percentage (retired model).
"""

from datetime import datetime
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.aset import daily_note as daily_note_module
from cobalt.aset.config import AsetConfig, REPO_ROOT
from cobalt.aset.daily_note import (
    DailyNoteRefused,
    assert_safe_target,
    save_card,
    save_fill_update,
    target_path,
)
from cobalt.aset.engine import compute_fill_recompute, compute_sizing
from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput


def make_cfg(**note_overrides) -> AsetConfig:
    note = {
        "daily_notes_dir": "1 - Trading/1- Daily Notes",
        "filename_pattern": "%Y-%m-%d.md",
    }
    note.update(note_overrides)
    return AsetConfig(
        account_size=Decimal("10000"),
        daily_note=note,
    )


ENABLED_GRADES = (Grade.A, Grade.B)


def make_result(**overrides):
    base = dict(
        ticker="TEST",
        grade=Grade.B,
        direction=Direction.LONG,
        sheet_mode=SheetMode.FULL,
        risk_dollars=Decimal("60"),
        entry=Decimal("10.00"),
        stop=Decimal("9.50"),
    )
    base.update(overrides)
    return compute_sizing(SizingInput(**base), ENABLED_GRADES)


@pytest.fixture
def fake_vault(monkeypatch, tmp_path):
    """Point the resolver at a tmp_path vault root, outside the repo."""
    vault_root = tmp_path / "vault"
    (vault_root / "1 - Trading" / "1- Daily Notes").mkdir(parents=True)
    monkeypatch.setattr(daily_note_module, "resolve_vault_path", lambda: vault_root)
    return vault_root


def test_gate_refuses_a_target_inside_the_repo():
    with pytest.raises(DailyNoteRefused, match="INSIDE the repo"):
        assert_safe_target(REPO_ROOT / "README.md")


def test_gate_passes_a_target_outside_the_repo(tmp_path):
    assert_safe_target(tmp_path / "somewhere" / "note.md")  # must not raise


def test_target_path_uses_resolved_vault_root(fake_vault):
    when = datetime(2026, 8, 26, 9, 31, 0)
    path = target_path(make_cfg(), when)
    assert path == fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-26.md"


def test_missing_daily_notes_dir_refuses(monkeypatch, tmp_path):
    vault_root = tmp_path / "vault"
    vault_root.mkdir()  # no "1 - Trading/1- Daily Notes" inside
    monkeypatch.setattr(daily_note_module, "resolve_vault_path", lambda: vault_root)
    with pytest.raises(DailyNoteRefused, match="Daily notes directory missing"):
        save_card(make_cfg(), make_result())


def test_unresolvable_vault_refuses(monkeypatch):
    from cobalt.vault import VaultConfigError

    def _raise():
        raise VaultConfigError("no vault configured")

    monkeypatch.setattr(daily_note_module, "resolve_vault_path", _raise)
    with pytest.raises(DailyNoteRefused, match="Vault path unresolved"):
        save_card(make_cfg(), make_result())


def test_stub_created_with_banner_on_first_save(fake_vault):
    when = datetime(2026, 8, 26, 9, 31, 0)
    path, returned_when = save_card(make_cfg(), make_result(), when=when)
    assert returned_when == when
    content = path.read_text()
    assert content.startswith("# 2026-08-26\n")
    assert "Created by Cobalt — apply daily template." in content
    assert "09:31:00 — TEST LONG B" in content
    assert "sheet_mode: full" in content


def test_append_only_no_banner_on_existing_note(fake_vault):
    when1 = datetime(2026, 8, 26, 9, 31, 0)
    when2 = datetime(2026, 8, 26, 10, 2, 30)

    p1, _ = save_card(make_cfg(), make_result(), when=when1)
    first = p1.read_text()

    p2, _ = save_card(make_cfg(), make_result(), when=when2)
    second = p2.read_text()

    assert p1 == p2
    # append-only: prior content byte-identical, new block after it
    assert second.startswith(first)
    assert "10:02:30 — TEST LONG B" in second
    # banner only appears once (only on creation, not on every save)
    assert second.count("Created by Cobalt") == 1


def test_pre_existing_note_gets_no_banner(fake_vault):
    # simulates today's real note already existing (Dejan's own workflow)
    when = datetime(2026, 8, 26, 9, 31, 0)
    path = target_path(make_cfg(), when)
    path.write_text("# 2026-08-26\n\n(Dejan's own content, from the Daily.md template)\n")

    save_card(make_cfg(), make_result(), when=when)
    content = path.read_text()
    assert "Created by Cobalt" not in content
    assert "Dejan's own content" in content
    assert "09:31:00 — TEST LONG B" in content


class TestFillUpdate:
    def test_fill_update_appends_linked_block(self, fake_vault):
        orig_when = datetime(2026, 8, 26, 9, 31, 0)
        card_path, orig_timestamp = save_card(make_cfg(), make_result(), when=orig_when)

        original = make_result()
        fill = compute_fill_recompute(original, actual_fill=Decimal("10.30"))
        fill_when = datetime(2026, 8, 26, 9, 45, 0)
        fill_path = save_fill_update(make_cfg(), fill, orig_timestamp, when=fill_when)

        assert fill_path == card_path
        content = fill_path.read_text()
        assert "09:45:00 — TEST FILL UPDATE" in content
        assert f"orig {orig_timestamp.isoformat(timespec='seconds')}" in content
        assert "actual_fill: 10.30" in content

    def test_structural_warning_appears_in_note(self, fake_vault):
        orig_when = datetime(2026, 8, 26, 9, 31, 0)
        _, orig_timestamp = save_card(make_cfg(), make_result(), when=orig_when)

        original = make_result()
        fill = compute_fill_recompute(original, actual_fill=Decimal("11.00"))  # big distance jump
        path = save_fill_update(make_cfg(), fill, orig_timestamp, when=orig_when)
        content = path.read_text()
        assert "stop may no longer be structural" in content

    def test_fill_update_refuses_inside_repo(self, monkeypatch):
        # Target a real, already-existing in-repo directory (this test's
        # own tests/cobalt/) so the "directory missing" check doesn't fire
        # before the "inside the repo" safety gate does — never create
        # directories under REPO_ROOT from a test.
        original = make_result()
        fill = compute_fill_recompute(original, actual_fill=Decimal("10.30"))
        monkeypatch.setattr(daily_note_module, "resolve_vault_path", lambda: REPO_ROOT)
        cfg = make_cfg(daily_notes_dir="tests/cobalt")
        with pytest.raises(DailyNoteRefused, match="INSIDE the repo"):
            save_fill_update(cfg, fill, datetime(2026, 8, 26, 9, 31, 0))
