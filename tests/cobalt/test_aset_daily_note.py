"""Daily-note writer tests: safety gate + marker-bounded upsert.

The vault resolver is monkeypatched to a pytest tmp_path for every test
here — genuinely outside the repo tree, so these tests exercise the
REAL "outside the repo" invariant without touching Dejan's real vault.

LAW L28 (2026-09-03): this module no longer appends; it upserts a unit
with a stable id through cobalt.vaultwrite. save_card returns
(path, when, write) and save_fill_update returns (path, write) — the
third/second element is the WriteResult, or None when the note write is
disabled by config. Writes persist to Postgres before they land, so the
writing tests need the dev database.
"""

import os
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


requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


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
MAX_STOP_DISTANCE_PCT = Decimal("10")


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
    return compute_sizing(SizingInput(**base), ENABLED_GRADES, MAX_STOP_DISTANCE_PCT)


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


@requires_db
def test_stub_created_with_banner_on_first_save(fake_vault):
    when = datetime(2026, 8, 26, 9, 31, 0)
    path, returned_when, write = save_card(make_cfg(), make_result(), when=when)
    assert returned_when == when
    assert write is not None and write.unit == "card-20260826T093100"
    content = path.read_text()
    assert content.startswith("# 2026-08-26\n")
    assert "Created by Cobalt — apply daily template." in content
    assert "09:31:00 — TEST LONG B" in content
    assert "sheet_mode: full" in content
    assert "<!-- cobalt:section aset-cards -->" in content


@requires_db
def test_second_card_lands_beside_the_first_not_over_it(fake_vault):
    when1 = datetime(2026, 8, 26, 9, 31, 0)
    when2 = datetime(2026, 8, 26, 10, 2, 30)

    p1, _, _ = save_card(make_cfg(), make_result(), when=when1)
    p2, _, _ = save_card(make_cfg(), make_result(), when=when2)
    second = p2.read_text()

    assert p1 == p2
    assert "09:31:00 — TEST LONG B" in second
    assert "10:02:30 — TEST LONG B" in second
    # banner only appears once (only on creation, not on every save)
    assert second.count("Created by Cobalt") == 1
    # one section, two units — not two sections
    assert second.count("<!-- cobalt:section aset-cards -->") == 1


@requires_db
def test_same_card_three_times_is_one_card(fake_vault):
    """L28: same unit id -> update in place. Before, a re-save appended
    a second identical block with nothing tying it to the first."""
    when = datetime(2026, 8, 26, 9, 31, 0)
    for _ in range(3):
        path, _, _ = save_card(make_cfg(), make_result(), when=when)
    content = path.read_text()
    assert content.count("09:31:00 — TEST LONG B") == 1
    assert content.count("<!-- cobalt:unit card-20260826T093100 -->") == 1


@requires_db
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


@requires_db
def test_write_disabled_flag_keeps_the_sheet_alive_and_writes_nothing(fake_vault):
    """The containment lever: sheet serves, note write off, loud in the
    log. On 09-03 there was no way to do this short of stopping the
    whole LaunchAgent."""
    when = datetime(2026, 8, 26, 9, 31, 0)
    cfg = make_cfg(write_enabled=False)
    path, returned_when, write = save_card(cfg, make_result(), when=when)
    assert write is None
    assert returned_when == when
    assert not path.exists()


@requires_db
class TestVerifyAfterWrite:
    """2026-09-02 ("TSLA id 127") incident: the /size handler reported
    this write succeeded — no exception — yet the card was never on
    disk a few minutes later; forensics point to something else (most
    likely an editor with the note open in a stale buffer) rewriting
    the file out from under the append. _append() now re-reads
    immediately after writing and fails loud if the card didn't
    survive, rather than trusting a clean open()/write()/close()."""

    def test_raises_when_the_write_does_not_survive_on_disk(self, fake_vault, monkeypatch):
        # Simulate a clobber landing in the gap AFTER the atomic rename:
        # the verification re-read finds no such unit in the note. (The
        # window before the rename is the writer's own mtime+hash guard —
        # tested in test_vaultwrite.py.)
        monkeypatch.setattr(daily_note_module, "find_section", lambda lines, name: None)
        with pytest.raises(DailyNoteRefused, match="VERIFY FAILED"):
            save_card(make_cfg(), make_result())

    def test_passes_when_the_write_survives(self, fake_vault):
        # Sanity: the ordinary, unclobbered path is unaffected.
        path, _, _ = save_card(make_cfg(), make_result())
        assert "TEST LONG B" in path.read_text()


@requires_db
class TestFillUpdate:
    def test_fill_update_appends_linked_block(self, fake_vault):
        orig_when = datetime(2026, 8, 26, 9, 31, 0)
        card_path, orig_timestamp, _ = save_card(make_cfg(), make_result(), when=orig_when)

        original = make_result()
        fill = compute_fill_recompute(
            original, actual_fill=Decimal("10.30"), max_fill_distance_pct=Decimal("5")
        )
        fill_when = datetime(2026, 8, 26, 9, 45, 0)
        fill_path, _ = save_fill_update(make_cfg(), fill, orig_timestamp, when=fill_when)

        assert fill_path == card_path
        content = fill_path.read_text()
        assert "09:45:00 — TEST FILL UPDATE" in content
        assert f"orig {orig_timestamp.isoformat(timespec='seconds')}" in content
        assert "actual_fill: 10.30" in content

    def test_structural_warning_appears_in_note(self, fake_vault):
        orig_when = datetime(2026, 8, 26, 9, 31, 0)
        _, orig_timestamp, _ = save_card(make_cfg(), make_result(), when=orig_when)

        original = make_result()
        # 11.00 is 10% from entry 10.00 — beyond the 5% default hard
        # floor, so widen it here to exercise the softer >=25%
        # distance_change_pct structural warning instead.
        fill = compute_fill_recompute(
            original, actual_fill=Decimal("11.00"), max_fill_distance_pct=Decimal("20")
        )  # big distance jump
        path, _ = save_fill_update(make_cfg(), fill, orig_timestamp, when=orig_when)
        content = path.read_text()
        assert "stop may no longer be structural" in content

    def test_fill_update_refuses_inside_repo(self, monkeypatch):
        # Target a real, already-existing in-repo directory (this test's
        # own tests/cobalt/) so the "directory missing" check doesn't fire
        # before the "inside the repo" safety gate does — never create
        # directories under REPO_ROOT from a test.
        original = make_result()
        fill = compute_fill_recompute(
            original, actual_fill=Decimal("10.30"), max_fill_distance_pct=Decimal("5")
        )
        monkeypatch.setattr(daily_note_module, "resolve_vault_path", lambda: REPO_ROOT)
        cfg = make_cfg(daily_notes_dir="tests/cobalt")
        with pytest.raises(DailyNoteRefused, match="INSIDE the repo"):
            save_fill_update(cfg, fill, datetime(2026, 8, 26, 9, 31, 0))
