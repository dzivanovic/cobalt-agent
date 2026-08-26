"""Daily-note writer tests: safety gate + append-only + stub-on-create.

The vault resolver is monkeypatched to a pytest tmp_path for every test
here — genuinely outside the repo tree, so these tests exercise the
REAL "outside the repo" invariant without touching Dejan's real vault.
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
    target_path,
)
from cobalt.aset.engine import compute_sizing
from cobalt.aset.models import Direction, Grade, SizingInput


def make_cfg(**note_overrides) -> AsetConfig:
    note = {
        "daily_notes_dir": "1 - Trading/1- Daily Notes",
        "filename_pattern": "%Y-%m-%d.md",
    }
    note.update(note_overrides)
    return AsetConfig(
        account_size=Decimal("10000"),
        broker_hard_stop=Decimal("430"),
        daily_note=note,
    )


def make_result():
    return compute_sizing(
        SizingInput(
            ticker="TEST",
            grade=Grade.B,
            direction=Direction.LONG,
            daily_stop=Decimal("200"),
            entry=Decimal("10.00"),
            stop=Decimal("9.50"),
        )
    )


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
    path = save_card(make_cfg(), make_result(), when=when)
    content = path.read_text()
    assert content.startswith("# 2026-08-26\n")
    assert "Created by Cobalt — apply daily template." in content
    assert "09:31:00 — TEST LONG B" in content


def test_append_only_no_banner_on_existing_note(fake_vault):
    when1 = datetime(2026, 8, 26, 9, 31, 0)
    when2 = datetime(2026, 8, 26, 10, 2, 30)

    p1 = save_card(make_cfg(), make_result(), when=when1)
    first = p1.read_text()

    p2 = save_card(make_cfg(), make_result(), when=when2)
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
