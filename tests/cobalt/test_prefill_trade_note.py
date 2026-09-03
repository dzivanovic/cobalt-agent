"""Trade-note tests: creates on first card, updates only Cobalt's five
frontmatter keys on a re-run, and never touches his body or his other
fields (strategy/RVOL/exit/entry_time/etc)."""

from datetime import datetime
from decimal import Decimal

import pytest

from cobalt.aset.engine import compute_sizing
from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput
from cobalt.prefill import trade_note as trade_note_module
from cobalt.prefill import vault_writer as vault_writer_module
from cobalt.prefill.config import PrefillPathsConfig
from cobalt.prefill.vault_writer import VaultWriteError

ENABLED_GRADES = (Grade.A, Grade.B)
MAX_STOP_DISTANCE_PCT = Decimal("10")


def make_result(**overrides):
    base = dict(
        ticker="NVDA",
        grade=Grade.B,
        direction=Direction.LONG,
        sheet_mode=SheetMode.FULL,
        risk_dollars=Decimal("60"),
        entry=Decimal("227.98"),
        stop=Decimal("225.00"),
    )
    base.update(overrides)
    return compute_sizing(SizingInput(**base), ENABLED_GRADES, MAX_STOP_DISTANCE_PCT)


def make_paths() -> PrefillPathsConfig:
    return PrefillPathsConfig(
        trades_dir="1 - Trading/2 - Trades",
        review_dir="1 - Trading/5 - Review",
        drc_filename_pattern="DRC-%Y-%m-%d.md",
        trade_filename_pattern="Trade-%Y-%m-%d %H-%M-%S -{ticker}.md",
    )


@pytest.fixture
def fake_vault(monkeypatch, tmp_path):
    vault_root = tmp_path / "vault"
    (vault_root / "1 - Trading" / "2 - Trades").mkdir(parents=True)
    monkeypatch.setattr(vault_writer_module, "resolve_vault_path", lambda: vault_root)
    return vault_root


def test_create_writes_expected_frontmatter_and_body(fake_vault):
    when = datetime(2026, 8, 31, 9, 31, 5)
    path, action = trade_note_module.upsert_trade_note(make_result(), when, make_paths())
    assert action == "created"
    assert path.name == "Trade-2026-08-31 09-31-05 -NVDA.md"
    content = path.read_text()
    assert "date: 2026-08-31 09:31" in content
    assert "symbol: NVDA" in content
    assert 'direction: "Long"' in content
    assert 'stop_price: "225.00"' in content
    assert 'entry_price: "227.98"' in content
    assert "exit_price:\n" in content
    assert "strategy:\n" in content
    assert "RVOL:\n" in content
    assert "tags:\n  - trade" in content
    assert "# Trade: [[Trade-2026-08-31 09-31-05 -NVDA]]" in content
    assert "[Why you entered, market conditions, mistakes]" in content


def test_rerun_same_card_updates_only_cobalt_fields(fake_vault):
    when = datetime(2026, 8, 31, 9, 31, 5)
    paths = make_paths()
    path, _ = trade_note_module.upsert_trade_note(make_result(), when, paths)

    # simulate Dejan filling in his own fields + body after the fact
    manual = path.read_text()
    manual = manual.replace('strategy:\n', 'strategy: "Big Dawg"\n')
    manual = manual.replace('RVOL:\n', 'RVOL: "2.5"\n')
    manual = manual.replace(
        "- Notes: \n\t- [Why you entered, market conditions, mistakes]",
        "- Notes: \n\tEntered on the flush, felt rushed.",
    )
    path.write_text(manual)

    # re-run with a slightly different entry (e.g. a corrected card)
    result2 = make_result(entry=Decimal("228.50"))
    path2, action = trade_note_module.upsert_trade_note(result2, when, paths)
    assert action == "updated"
    assert path2 == path

    content = path.read_text()
    assert 'entry_price: "228.50"' in content  # Cobalt's field refreshed
    assert 'strategy: "Big Dawg"' in content  # his field preserved
    assert 'RVOL: "2.5"' in content  # his field preserved
    assert "Entered on the flush, felt rushed." in content  # his body preserved


def test_refuses_to_update_a_file_with_no_frontmatter(fake_vault, tmp_path):
    when = datetime(2026, 8, 31, 9, 31, 5)
    paths = make_paths()
    filename = "Trade-2026-08-31 09-31-05 -NVDA.md"
    (fake_vault / "1 - Trading" / "2 - Trades" / filename).write_text("no frontmatter here\n")
    with pytest.raises(VaultWriteError, match="no recognizable frontmatter"):
        trade_note_module.upsert_trade_note(make_result(), when, paths)
