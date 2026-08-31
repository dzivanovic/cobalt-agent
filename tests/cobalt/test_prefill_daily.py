"""Morning Daily Note prefill tests: formatting helpers + the
create-vs-append-vs-idempotent-skip orchestration, against a tmp_path
vault (never Dejan's real one)."""

from datetime import datetime
from decimal import Decimal

import pytest

from cobalt.aset.config import AsetConfig
from cobalt.prefill import daily as daily_module
from cobalt.prefill import vault_writer as vault_writer_module
from cobalt.prefill.calendar import EarningsEvent, EconomicEvent
from cobalt.prefill.config import load_rules_config
from cobalt.prefill.market import MarketRow


def make_aset_cfg() -> AsetConfig:
    return AsetConfig(
        account_size=Decimal("10000"),
        daily_note={
            "daily_notes_dir": "1 - Trading/1- Daily Notes",
            "filename_pattern": "%Y-%m-%d.md",
        },
    )


ROWS = [
    MarketRow(ticker="SPY", price=Decimal("500.12"), change_pct=Decimal("0.34")),
    MarketRow(ticker="QQQ", price=Decimal("450.55"), change_pct=Decimal("-0.20")),
    MarketRow(ticker="IWM", price=Decimal("210.03"), change_pct=Decimal("1.05")),
]


class TestFormatMarketCells:
    def test_manual_tickers_always_na(self):
        cells = daily_module.format_market_cells(ROWS, None)
        assert cells["vix_col2"] == "n/a (manual)"
        assert cells["btc_col2"] == "n/a (manual)"

    def test_success_formats_price_and_change(self):
        cells = daily_module.format_market_cells(ROWS, None)
        assert cells["spy_col2"] == "$500.12"
        assert cells["spy_col3"] == "+0.34%"
        assert cells["qqq_col3"] == "-0.20%"
        assert cells["market_error"] == ""

    def test_failure_renders_failed_never_blank(self):
        cells = daily_module.format_market_cells(None, "Finviz screener fetch failed: boom")
        assert cells["spy_col2"] == "FAILED"
        assert cells["qqq_col2"] == "FAILED"
        assert cells["iwm_col2"] == "FAILED"
        assert "boom" in cells["market_error"]
        # manual tickers stay n/a even when the equity fetch fails
        assert cells["vix_col2"] == "n/a (manual)"


class TestFormatCalendarBlock:
    def test_renders_economic_and_earnings_sorted(self):
        economic = [EconomicEvent(event="CPI", time="08:30", impact="3", expected="0.2%", prior="0.1%")]
        earnings = [EarningsEvent(ticker="AAPL", company="Apple Inc", time="16:05")]
        block = daily_module.format_calendar_block(economic, earnings, None)
        assert "08:30 ET — CPI" in block
        assert "16:05 ET — AAPL earnings (Apple Inc)" in block
        # economic (08:30) sorts before earnings (16:05)
        assert block.index("CPI") < block.index("AAPL")

    def test_empty_renders_none_scheduled_not_blank(self):
        assert daily_module.format_calendar_block([], [], None) == "- (none scheduled)\n"

    def test_failure_renders_failed_never_blank(self):
        block = daily_module.format_calendar_block(None, None, "calendar/economic fetch failed: boom")
        assert block == "- FAILED: calendar/economic fetch failed: boom\n"


class TestFormatRulesBlocks:
    def test_rules_and_adherence_and_mantras_populated(self):
        rules_cfg = load_rules_config()
        rules_block, adherence_block, mantras_block = daily_module.format_rules_blocks(rules_cfg)
        assert "card_first" not in rules_block  # ids aren't rendered, text is
        assert "Card first" in rules_block
        assert adherence_block.count("- [ ] ") == len(rules_cfg.rules)
        assert "Tape check" in mantras_block


@pytest.fixture
def fake_vault(monkeypatch, tmp_path):
    vault_root = tmp_path / "vault"
    (vault_root / "1 - Trading" / "1- Daily Notes").mkdir(parents=True)
    monkeypatch.setattr(vault_writer_module, "resolve_vault_path", lambda: vault_root)
    return vault_root


@pytest.fixture(autouse=True)
def fake_fetchers(monkeypatch):
    async def _market(*a, **kw):
        return ROWS

    async def _econ(*a, **kw):
        return [EconomicEvent(event="CPI", time="08:30", impact="3", expected="0.2%", prior="0.1%")]

    async def _earn(*a, **kw):
        return []

    monkeypatch.setattr(daily_module, "fetch_market_table", _market)
    monkeypatch.setattr(daily_module, "fetch_economic_events", _econ)
    monkeypatch.setattr(daily_module, "fetch_earnings_events", _earn)
    monkeypatch.setattr(daily_module, "load_aset_config", make_aset_cfg)


async def test_create_path_renders_full_template(fake_vault):
    when = datetime(2026, 8, 31, 5, 15, 0)
    result = await daily_module.run_daily_prefill(when=when)
    assert result.action == "created"
    content = result.path.read_text()
    assert content.startswith("---\ntags:\n  - Daily\n---\n")
    assert "#### 2026-08-31 T 05:15" in content
    assert "$500.12" in content
    assert "+0.34%" in content
    assert "n/a (manual)" in content
    assert "08:30 ET — CPI" in content
    assert "Card first: grade" in content
    assert "cobalt-prefill:daily:2026-08-31" in content
    # his empty sections stay empty/untouched
    assert "1% goal:" in content
    assert "### Trade Execution" in content


async def test_append_path_when_note_already_exists(fake_vault):
    when = datetime(2026, 8, 31, 5, 15, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text("# 2026-08-31\n\n(Dejan's own content pasted here)\n")

    result = await daily_module.run_daily_prefill(when=when)
    assert result.action == "appended"
    content = path.read_text()
    assert content.startswith("# 2026-08-31\n\n(Dejan's own content pasted here)\n")
    assert "## Cobalt Prefill — 05:15:00" in content
    assert "$500.12" in content
    assert "cobalt-prefill:daily:2026-08-31" in content


async def test_second_run_same_day_is_idempotent_noop(fake_vault):
    when = datetime(2026, 8, 31, 5, 15, 0)
    first = await daily_module.run_daily_prefill(when=when)
    assert first.action == "created"
    before = first.path.read_text()

    second = await daily_module.run_daily_prefill(when=datetime(2026, 8, 31, 15, 40, 0))
    assert second.action == "skipped_idempotent"
    assert second.path.read_text() == before
