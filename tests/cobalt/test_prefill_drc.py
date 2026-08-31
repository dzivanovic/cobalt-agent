"""DRC prefill tests: fill-block parsing, nearest-timestamp trade-note
matching, formatting helpers, and the create/append/idempotent-skip
orchestration — all against a tmp_path vault, no real Postgres."""

from datetime import date, datetime
from decimal import Decimal

import pytest

from cobalt.aset.config import AsetConfig
from cobalt.prefill import drc as drc_module
from cobalt.prefill import vault_writer as vault_writer_module
from cobalt.prefill.drc import (
    EntryRender,
    find_trade_note_for_card,
    format_risk_parameters,
    format_tickers_block,
    parse_fill_updates,
)


def make_aset_cfg() -> AsetConfig:
    return AsetConfig(
        account_size=Decimal("10000"),
        daily_note={
            "daily_notes_dir": "1 - Trading/1- Daily Notes",
            "filename_pattern": "%Y-%m-%d.md",
        },
    )


FILL_BLOCK = (
    "### 09:45:00 — NVDA FILL UPDATE (orig 2026-08-28T09:31:05-04:00)\n"
    "```aset-fill\n"
    "ticker: NVDA\n"
    "orig_timestamp: 2026-08-28T09:31:05-04:00\n"
    "actual_fill: 228.50\n"
    "stop: 225.00\n"
    "planned_shares: 20\n"
    "recomputed_shares: 19\n"
    "share_delta: -1\n"
    "recomputed_used_risk: 61.75\n"
    "distance_change_pct: 3.20\n"
    "timestamp: 2026-08-28T09:45:00-04:00\n"
    "```\n"
)


class TestParseFillUpdates:
    def test_extracts_fields_keyed_by_naive_local_orig_timestamp(self):
        updates = parse_fill_updates(FILL_BLOCK)
        assert "2026-08-28T09:31:05" in updates
        assert updates["2026-08-28T09:31:05"]["actual_fill"] == "228.50"
        assert updates["2026-08-28T09:31:05"]["share_delta"] == "-1"

    def test_no_blocks_returns_empty(self):
        assert parse_fill_updates("# just a daily note\n\nno fills here\n") == {}


class TestFindTradeNoteForCard:
    def test_matches_nearest_within_tolerance(self, tmp_path):
        trades_dir = tmp_path / "trades"
        trades_dir.mkdir()
        (trades_dir / "Trade-2026-08-28 09-31-07 -NVDA.md").write_text("---\nsymbol: NVDA\n---\nbody\n")
        (trades_dir / "Trade-2026-08-28 10-00-00 -NVDA.md").write_text("---\nsymbol: NVDA\n---\nbody\n")

        created_at = datetime(2026, 8, 28, 9, 31, 5).astimezone()
        found = find_trade_note_for_card(trades_dir, "NVDA", created_at)
        assert found is not None
        assert found.name == "Trade-2026-08-28 09-31-07 -NVDA.md"

    def test_wrong_ticker_not_matched(self, tmp_path):
        trades_dir = tmp_path / "trades"
        trades_dir.mkdir()
        (trades_dir / "Trade-2026-08-28 09-31-07 -MU.md").write_text("---\nsymbol: MU\n---\nbody\n")
        created_at = datetime(2026, 8, 28, 9, 31, 5).astimezone()
        assert find_trade_note_for_card(trades_dir, "NVDA", created_at) is None

    def test_beyond_tolerance_not_matched(self, tmp_path):
        trades_dir = tmp_path / "trades"
        trades_dir.mkdir()
        (trades_dir / "Trade-2026-08-28 09-40-00 -NVDA.md").write_text("---\nsymbol: NVDA\n---\nbody\n")
        created_at = datetime(2026, 8, 28, 9, 31, 5).astimezone()
        assert find_trade_note_for_card(trades_dir, "NVDA", created_at) is None

    def test_missing_dir_returns_none(self, tmp_path):
        created_at = datetime(2026, 8, 28, 9, 31, 5).astimezone()
        assert find_trade_note_for_card(tmp_path / "nope", "NVDA", created_at) is None


class TestFormatRiskParameters:
    def test_full_mode_renders_grade_dollars(self):
        from cobalt.aset.config import load_sheet_modes_config

        cfg = load_sheet_modes_config()
        cards = [{"sheet_mode": "full"}, {"sheet_mode": "full"}]
        line = format_risk_parameters(cards, cfg)
        assert "FULL —" in line
        assert "B:$" in line

    def test_no_cards_renders_explanatory_line_not_blank(self):
        from cobalt.aset.config import load_sheet_modes_config

        cfg = load_sheet_modes_config()
        assert "no sheet-mode cards today" in format_risk_parameters([], cfg)


class TestFormatTickersBlock:
    def test_empty_renders_no_tickers_traded(self):
        assert format_tickers_block({}) == "(no tickers traded today)\n"

    def test_renders_entry_numbering_and_reentry_prompts(self):
        e1 = EntryRender(
            number=1, time_str="09:31:05", grade="B", direction="long", sheet_mode="full",
            entry="227.98", stop="225.00", shares="20", risk_budget="60.00",
            fill=None, needs_written_info=False, stand_down=False, excitement_audit=False,
        )
        e2 = EntryRender(
            number=2, time_str="10:05:00", grade="B", direction="long", sheet_mode="full",
            entry="228.10", stop="225.50", shares="18", risk_budget="60.00",
            fill=None, needs_written_info=True, stand_down=False, excitement_audit=True,
        )
        block = format_tickers_block({"NVDA": [e1, e2]})
        assert "- Ticker: NVDA" in block
        assert "Entry #1" in block and "Entry #2" in block
        assert "New written information" in block
        assert "Excitement audit" in block


@pytest.fixture
def fake_vault(monkeypatch, tmp_path):
    vault_root = tmp_path / "vault"
    (vault_root / "1 - Trading" / "1- Daily Notes").mkdir(parents=True)
    (vault_root / "1 - Trading" / "2 - Trades").mkdir(parents=True)
    (vault_root / "1 - Trading" / "5 - Review").mkdir(parents=True)
    monkeypatch.setattr(vault_writer_module, "resolve_vault_path", lambda: vault_root)
    return vault_root


class _FakeStore:
    def __init__(self, cards):
        self._cards = cards

    def ensure_schema(self):
        pass

    def for_date(self, day):
        return self._cards


def make_card(ticker, created_at, **overrides):
    base = dict(
        id=1, created_at=created_at, ticker=ticker, grade="B", direction="long",
        sheet_mode="full", risk_budget=Decimal("60.00"), entry=Decimal("227.98"),
        stop=Decimal("225.00"), per_share_risk=Decimal("2.98"), shares=20, used_risk=Decimal("59.60"),
    )
    base.update(overrides)
    return base


@pytest.fixture(autouse=True)
def fake_config(monkeypatch):
    monkeypatch.setattr(drc_module, "load_aset_config", make_aset_cfg)


async def test_create_path_renders_full_template_with_cards(fake_vault, monkeypatch):
    when = datetime(2026, 8, 28, 9, 31, 5).astimezone()
    cards = [make_card("NVDA", when)]
    monkeypatch.setattr(drc_module, "AsetStore", lambda db_name: _FakeStore(cards))

    result = await drc_module.run_drc_prefill(for_date_=date(2026, 8, 28))
    assert result.action == "created"
    assert result.card_count == 1
    content = result.path.read_text()
    assert result.path.name == "DRC-2026-08-28.md"
    assert "### 2026-08-28" in content
    assert "- Ticker: NVDA" in content
    assert "Entry #1" in content
    assert "$227.98" in content
    assert "FULL —" in content
    assert "- [ ] Card first" in content
    # his sections stay untouched placeholders
    assert "Grade: (A+, A, B, C, etc..)" in content
    assert "### PnL on the day:  $XXXX" in content


async def test_append_path_when_drc_already_exists(fake_vault, monkeypatch):
    when = datetime(2026, 8, 28, 9, 31, 5).astimezone()
    cards = [make_card("NVDA", when)]
    monkeypatch.setattr(drc_module, "AsetStore", lambda db_name: _FakeStore(cards))

    path = fake_vault / "1 - Trading" / "5 - Review" / "DRC-2026-08-28.md"
    path.write_text("# Dejan's own DRC draft\n\nAlready started writing this.\n")

    result = await drc_module.run_drc_prefill(for_date_=date(2026, 8, 28))
    assert result.action == "appended"
    content = path.read_text()
    assert content.startswith("# Dejan's own DRC draft\n\nAlready started writing this.\n")
    assert "Cobalt Prefill — DRC draft" in content
    assert "- Ticker: NVDA" in content


async def test_second_run_same_day_is_idempotent(fake_vault, monkeypatch):
    when = datetime(2026, 8, 28, 9, 31, 5).astimezone()
    cards = [make_card("NVDA", when)]
    monkeypatch.setattr(drc_module, "AsetStore", lambda db_name: _FakeStore(cards))

    first = await drc_module.run_drc_prefill(for_date_=date(2026, 8, 28))
    before = first.path.read_text()
    second = await drc_module.run_drc_prefill(for_date_=date(2026, 8, 28))
    assert second.action == "skipped_idempotent"
    assert second.path.read_text() == before


async def test_no_cards_renders_no_tickers_traded(fake_vault, monkeypatch):
    monkeypatch.setattr(drc_module, "AsetStore", lambda db_name: _FakeStore([]))
    result = await drc_module.run_drc_prefill(for_date_=date(2026, 8, 29))
    content = result.path.read_text()
    assert "(no tickers traded today)" in content
    assert "no sheet-mode cards today" in content
