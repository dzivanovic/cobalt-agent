"""Daily-note writer tests: safety gate + append-only behavior.

The roundtrip test writes into the real playground inbox (docs/ vault)
under a test-prefixed filename pattern, exercising the REAL git-ignore
gate, then removes the file.
"""

from datetime import datetime
from decimal import Decimal
from pathlib import Path

import pytest

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
        "vault_path": "docs",
        "inbox_dir": "0 - Inbox",
        "filename_pattern": "aset-test-%Y-%m-%d.md",
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


def test_gate_refuses_tracked_file():
    with pytest.raises(DailyNoteRefused, match="TRACKED"):
        assert_safe_target(REPO_ROOT / "README.md")


def test_gate_refuses_unignored_untracked_path():
    # repo root is not ignored; a hypothetical new file there is committable
    with pytest.raises(DailyNoteRefused, match="not git-ignored"):
        assert_safe_target(REPO_ROOT / "definitely-not-ignored-xyz.md")


def test_gate_passes_playground_inbox_path():
    when = datetime(2026, 8, 25, 9, 31, 0)
    path = target_path(make_cfg(), when)
    assert path.parent == REPO_ROOT / "docs" / "0 - Inbox"
    assert_safe_target(path)  # must not raise


def test_missing_inbox_dir_refuses():
    cfg = make_cfg(inbox_dir="no-such-dir-xyz")
    with pytest.raises(DailyNoteRefused, match="Inbox directory missing"):
        save_card(cfg, make_result())


def test_append_only_roundtrip_real_gate():
    cfg = make_cfg()
    when1 = datetime(2026, 8, 25, 9, 31, 0)
    when2 = datetime(2026, 8, 25, 10, 2, 30)
    path = target_path(cfg, when1)
    assert not path.exists(), f"stale test note {path} — remove it first"
    try:
        p1 = save_card(cfg, make_result(), when=when1)
        assert p1 == path
        first = path.read_text()
        assert first.startswith("# 2026-08-25\n")
        assert "09:31:00 — TEST LONG B" in first
        assert "shares: 60" in first

        save_card(cfg, make_result(), when=when2)
        second = path.read_text()
        # append-only: prior content byte-identical, new block after it
        assert second.startswith(first)
        assert "10:02:30 — TEST LONG B" in second
        assert second.count("# 2026-08-25\n") == 1  # header only on create
    finally:
        path.unlink(missing_ok=True)
