"""Morning Daily Note prefill tests (Slice 2.1): content builders, the
mode-aware sizing splice, and the fill-in-place create/skip/fail-loud
orchestration — against a tmp_path vault, never Dejan's real one."""

from datetime import datetime
from decimal import Decimal

import pytest

from cobalt.aset.config import AsetConfig
from cobalt.aset.daily_note import STUB_BANNER
from cobalt.prefill import daily as daily_module
from cobalt.prefill import vault_writer as vault_writer_module
from cobalt.prefill.calendar import EarningsEvent, EconomicEvent
from cobalt.prefill.config import GeneratedMeta, MantraItem, RuleItem, RulesConfig
from cobalt.prefill.daily import NoteChangedDuringPrefill, SlotAnchorNotFound
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


def make_rules_cfg(**overrides) -> RulesConfig:
    rules = overrides.get("rules") or [
        RuleItem(id="rule_01", category="process", text="Card first."),
        RuleItem(id="rule_02", category="sizing", text="Grades: B = $30, A = $70. Nothing bigger."),
    ]
    mantras = overrides.get("mantras") or [MantraItem(id="tape_check", text="Tape check: ...")]
    return RulesConfig(
        generated=GeneratedMeta(source="/vault/Rules.md", source_sha256="a" * 64, generated_at="2026-08-31T00:00:00+00:00"),
        rules=rules,
        mantras=mantras,
    )


class TestFormatMarketRow:
    def test_finds_matching_ticker(self):
        assert daily_module.format_market_row("SPY", ROWS, None) == ("$500.12", "+0.34%")
        assert daily_module.format_market_row("QQQ", ROWS, None) == ("$450.55", "-0.20%")

    def test_failure_renders_failed_never_blank(self):
        assert daily_module.format_market_row("SPY", None, "boom") == ("FAILED", "")

    def test_missing_ticker_in_successful_response_renders_failed(self):
        assert daily_module.format_market_row("IWM", ROWS[:2], None) == ("FAILED", "")


class TestFormatCalendarBlock:
    def test_renders_economic_and_earnings_sorted(self):
        economic = [EconomicEvent(event="CPI", time="08:30", impact="3", expected="0.2%", prior="0.1%")]
        earnings = [EarningsEvent(ticker="AAPL", company="Apple Inc", time="16:05")]
        block = daily_module.format_calendar_block(economic, earnings, None)
        assert "08:30 ET — CPI" in block
        assert "16:05 ET — AAPL earnings (Apple Inc)" in block
        assert block.index("CPI") < block.index("AAPL")

    def test_empty_renders_none_scheduled_not_blank(self):
        assert daily_module.format_calendar_block([], [], None) == "- (none scheduled)"

    def test_failure_renders_failed_never_blank(self):
        block = daily_module.format_calendar_block(None, None, "calendar/economic fetch failed: boom")
        assert block == "- FAILED: calendar/economic fetch failed: boom"


class FakeSheetModesConfig:
    _DOLLARS = {("half", "B"): Decimal("30"), ("full", "B"): Decimal("60"),
                ("half", "A"): Decimal("70"), ("full", "A"): Decimal("135")}

    def dollars_for(self, mode, grade):
        from cobalt.aset.models import Grade
        g = grade.value if hasattr(grade, "value") else grade
        return self._DOLLARS[(mode, g)]


class TestModeAwareSizing:
    def test_splices_mode_aware_clause_into_matching_rule(self):
        text = "Grades: **B = $30, A = $70.** Nothing bigger. C = pass."
        result = daily_module.format_sizing_rule_text(text, FakeSheetModesConfig())
        assert result == "Grades: **B = $30 half / $60 full, A = $70 half / $135 full.** Nothing bigger. C = pass."

    def test_non_matching_rule_untouched(self):
        text = "Max 5 trades."
        assert daily_module.format_sizing_rule_text(text, FakeSheetModesConfig()) == text

    def test_apply_mode_aware_sizing_only_changes_the_matching_rule(self):
        rules = [
            RuleItem(id="rule_01", category="process", text="Card first."),
            RuleItem(id="rule_02", category="sizing", text="Grades: B = $30, A = $70. Nothing bigger."),
        ]
        updated = daily_module.apply_mode_aware_sizing(rules, FakeSheetModesConfig())
        assert updated[0].text == "Card first."
        assert "half / $60 full" in updated[1].text
        # originals untouched (model_copy, not mutation)
        assert rules[1].text == "Grades: B = $30, A = $70. Nothing bigger."


class TestFormatRulesCheckboxBlock:
    def test_single_merged_checklist_with_tags(self):
        rules = [
            RuleItem(id="rule_01", category="process", text="Card first."),
            RuleItem(id="rule_02", category="re_entry", text="Re-entry needs new info."),
        ]
        block = daily_module.format_rules_checkbox_block(rules)
        assert block == "- [ ] Card first. #process\n- [ ] Re-entry needs new info. #re_entry"


class TestFormatModeHint:
    def test_no_cards_no_hint(self):
        assert daily_module.format_mode_hint([]) == ""

    def test_most_recent_card_mode_shown(self):
        cards = [{"sheet_mode": "full"}, {"sheet_mode": "half"}]
        assert daily_module.format_mode_hint(cards) == " (today's most recent card: HALF)"

    def test_missing_sheet_mode_field_no_hint(self):
        assert daily_module.format_mode_hint([{"sheet_mode": None}]) == ""


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

    class _FakeStore:
        def __init__(self, db_name):
            pass

        def for_date(self, day):
            return []

    monkeypatch.setattr(daily_module, "fetch_market_table", _market)
    monkeypatch.setattr(daily_module, "fetch_economic_events", _econ)
    monkeypatch.setattr(daily_module, "fetch_earnings_events", _earn)
    monkeypatch.setattr(daily_module, "load_aset_config", make_aset_cfg)
    monkeypatch.setattr(daily_module, "load_sheet_modes_config", lambda: FakeSheetModesConfig())
    monkeypatch.setattr(daily_module, "regenerate_rules_config", make_rules_cfg)
    monkeypatch.setattr(daily_module, "AsetStore", _FakeStore)


DAILY_MD_SKELETON = """---
tags:
  - Daily
---
#### {date} T 05:24

## Journal

### How do you feel

Sleep:
## Today's Plan

1% goal:

Daily HARD Stop: $420
STOP TRADING AFTER 11AM until one month green 4 out of 5 days a week
I WILL NOT TOLERATE THE MISTAKE OF OVERSIZING RISK ON A SINGLE TRADE THAT I DID NOT PLAN JUST TO MAKE A LARGFE POSITION
I WILL NOT TOLERATE THE MISTAKE OF HAVING MORE THAN 3 LOSSES IN A ROW IN A TRADING DAY

### Trading

| VIX |     |     |
| --- | --- | --- |
| SPY |{spy_cells}
| QQQ |     |     |
| IWM |     |     |
| BTC |     |     |

### Market Context:
- pasted stuff

### Market Calendar:
{calendar_content}
### Game Plan:

"""


def make_note_text(date="2026-08-31", spy_filled=False, calendar_filled=False) -> str:
    spy_cells = " 767.48    | -0.24 % |" if spy_filled else "     |     |"
    calendar_content = "- real calendar content already here" if calendar_filled else "- "
    return DAILY_MD_SKELETON.format(date=date, spy_cells=spy_cells, calendar_content=calendar_content)


async def test_create_path_renders_full_template(fake_vault):
    when = datetime(2026, 8, 31, 5, 15, 0)
    result = await daily_module.run_daily_prefill(when=when)
    assert result.action == "created"
    assert set(result.filled_slots) == {"rules", "trading", "market_calendar"}
    content = result.path.read_text()
    assert content.startswith("---\ntags:\n  - Daily\n---\n")
    assert "#### 2026-08-31 T 05:15" in content
    assert "$500.12" in content
    assert "+0.34%" in content
    assert "08:30 ET — CPI" in content
    assert "half / $60 full" in content
    assert "<!-- cobalt-slot:rules -->" in content
    assert "<!-- cobalt-slot:trading -->" in content
    assert "<!-- cobalt-slot:market_calendar -->" in content
    # his empty sections stay empty/untouched
    assert "1% goal:" in content
    assert "### Trade Execution" in content


async def test_fill_in_place_skips_already_filled_trading_row(fake_vault):
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text(make_note_text(spy_filled=True))

    result = await daily_module.run_daily_prefill(when=when)
    assert result.action == "filled"
    assert "trading:SPY (already filled)" in result.skipped_slots
    assert "trading:QQQ" in " ".join(result.filled_slots)
    content = path.read_text()
    assert "| SPY | 767.48    | -0.24 % |" in content  # untouched, byte-identical
    assert "$450.55" in content  # QQQ was blank, got filled
    assert "- pasted stuff" in content  # Market Context untouched


async def test_fill_in_place_fills_calendar_when_blank(fake_vault):
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text(make_note_text())

    result = await daily_module.run_daily_prefill(when=when)
    assert "market_calendar" in result.filled_slots
    content = path.read_text()
    assert "08:30 ET — CPI" in content


async def test_fill_in_place_skips_calendar_already_filled(fake_vault):
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text(make_note_text(calendar_filled=True))

    result = await daily_module.run_daily_prefill(when=when)
    assert "market_calendar (already filled)" in result.skipped_slots
    content = path.read_text()
    assert "- real calendar content already here" in content
    assert "CPI" not in content


async def test_second_run_same_day_is_idempotent(fake_vault):
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text(make_note_text())

    first = await daily_module.run_daily_prefill(when=when)
    assert first.action == "filled"
    before = path.read_text()

    second = await daily_module.run_daily_prefill(when=when)
    assert second.action == "skipped_idempotent"
    assert path.read_text() == before


async def test_missing_rules_anchor_fails_loud(fake_vault):
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text("# just a stub note\n\nno matching anchors here\n")

    with pytest.raises(SlotAnchorNotFound, match="I WILL NOT TOLERATE"):
        await daily_module.run_daily_prefill(when=when)


async def test_aset_bootstrap_stub_upgrades_to_full_template_preserving_cards(fake_vault):
    """Reproduces the 09-03 report: ASET's own stub-on-create fallback
    (aset/daily_note.py) creates the note before this job ever runs
    (e.g. prefill failed/was late that morning). The old code had no
    anchors to fill against and crashed (SlotAnchorNotFound) — or, if it
    hadn't crashed, generic overwrite logic risked losing the cards. The
    fix upgrades the stub to the full template AND keeps every card."""
    when = datetime(2026, 9, 3, 10, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-09-03.md"
    card_block = "\n### 10:02:06 — TSLA LONG B\n```aset\nticker: TSLA\n```\n"
    path.write_text(f"# 2026-09-03\n\n{STUB_BANNER}{card_block}")

    result = await daily_module.run_daily_prefill(when=when)
    assert result.action == "upgraded_stub"
    content = path.read_text()
    assert "<!-- cobalt-slot:rules -->" in content
    assert "<!-- cobalt-slot:trading -->" in content
    assert "<!-- cobalt-slot:market_calendar -->" in content
    assert "### 10:02:06 — TSLA LONG B" in content
    assert "ticker: TSLA" in content


async def test_card_appended_during_fetch_window_is_not_clobbered(fake_vault, monkeypatch):
    """Root-cause regression test: a card lands (via ASET's real
    append-only writer) WHILE this run is mid-fetch. The old code read
    `existing` before the fetch and blindly wrote that stale snapshot
    back after, silently discarding the card — this is exactly what
    wiped every card out of 2026-09-02's real daily note. The fix must
    see the card (re-read happens after the fetch)."""
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text(make_note_text())

    async def _market_then_append(*a, **kw):
        # Simulates ASET's real writer, which really is synchronous/
        # blocking (aset/daily_note.py's _append()) — deliberate, not
        # an oversight.
        with open(path, "a", encoding="utf-8") as f:  # noqa: ASYNC230
            f.write("\n### 08:46:00 — NVDA LONG B\n```aset\nticker: NVDA\n```\n")
        return ROWS

    monkeypatch.setattr(daily_module, "fetch_market_table", _market_then_append)

    result = await daily_module.run_daily_prefill(when=when)
    content = path.read_text()
    assert "### 08:46:00 — NVDA LONG B" in content, (
        "card appended mid-fetch was clobbered by a stale-snapshot overwrite"
    )
    assert "$450.55" in content  # the fill-in-place edit still landed
    assert result.action == "filled"


async def test_write_refuses_rather_than_clobbers_on_a_true_race(fake_vault, monkeypatch):
    """Even the narrow post-re-read window is guarded: if the file
    changes between the (now-late) read and the write itself, refuse
    loudly instead of overwriting — never a silent lost update."""
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text(make_note_text())

    real_write_if_unchanged = daily_module._write_if_unchanged

    def _racy_write(path_, baseline, new_text):
        with open(path_, "a", encoding="utf-8") as f:
            f.write("\n### 08:46:30 — LATE RACE CARD\n")
        real_write_if_unchanged(path_, baseline, new_text)

    monkeypatch.setattr(daily_module, "_write_if_unchanged", _racy_write)

    with pytest.raises(NoteChangedDuringPrefill):
        await daily_module.run_daily_prefill(when=when)
    assert "LATE RACE CARD" in path.read_text()  # the racing write survives untouched
