"""Morning Daily Note prefill tests: content builders, the mode-aware
sizing splice, and the LAW L28 create/merge/skip orchestration — against
a tmp_path vault, never Dejan's real one.

Rewritten 2026-09-03 for L28. Three assertions in the old file encoded
behaviour the law deliberately removed and are replaced here:
`upgraded_stub` (the branch that discarded everything above the stub
banner — now a merge that keeps it), `SlotAnchorNotFound` failing the
whole run (now an end-of-note append), and `_write_if_unchanged` (now
the writer's own mtime+hash guard)."""

import hashlib
import os
from datetime import datetime
from decimal import Decimal

import pytest

from cobalt.aset.config import AsetConfig
from cobalt.aset.daily_note import STUB_BANNER
from cobalt.prefill import daily as daily_module
from cobalt.prefill import vault_writer as vault_writer_module
from cobalt.prefill.calendar import EarningsEvent, EconomicEvent
from cobalt.prefill.config import GeneratedMeta, MantraItem, RuleItem, RulesConfig
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
        def __init__(self, db_name=None):
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


# The daily prefill goes through the ONE write path now (LAW L28), and
# that path persists every write to Postgres before it lands. These
# orchestration tests therefore need the dev database, exactly like
# tests/cobalt/test_aset_store.py.
requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


@requires_db
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
    assert "<!-- cobalt:section rules -->" in content
    assert "<!-- cobalt:unit market_table -->" in content
    assert "<!-- cobalt:section market_calendar -->" in content
    # his empty sections stay empty/untouched
    assert "1% goal:" in content
    assert "### Trade Execution" in content


@requires_db
async def test_existing_note_never_rewritten_whole(fake_vault):
    """L28.1: an existing file ALWAYS takes the merge path — the whole-
    file template render is reachable only when the file is absent."""
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    original = make_note_text()
    path.write_text(original)

    await daily_module.run_daily_prefill(when=when)
    content = path.read_text()
    # Every line of his note survives except the three market rows and the
    # blank calendar placeholder, which are precisely what he asked Cobalt
    # to fill. Nothing else moves, nothing is re-rendered.
    cobalt_fills = ("| SPY |", "| QQQ |", "| IWM |", "- ")
    for line in original.split("\n"):
        if line.startswith(cobalt_fills):
            continue
        assert line in content, f"human line lost: {line!r}"
    assert content.index("## Journal") < content.index("### Trading")
    assert content.index("### Trading") < content.index("### Market Context:")
    assert "- pasted stuff" in content


@requires_db
async def test_fill_in_place_skips_already_filled_trading_row(fake_vault):
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text(make_note_text(spy_filled=True))

    result = await daily_module.run_daily_prefill(when=when)
    assert result.action == "filled"
    content = path.read_text()
    assert "| SPY | 767.48    | -0.24 % |" in content  # untouched, byte-identical
    assert "$450.55" in content  # QQQ was blank, got filled
    assert "- pasted stuff" in content  # Market Context untouched
    assert "| VIX |     |     |" in content  # his row, inside the section, untouched


@requires_db
async def test_fill_in_place_fills_calendar_when_blank(fake_vault):
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text(make_note_text())

    result = await daily_module.run_daily_prefill(when=when)
    assert "market_calendar" in result.filled_slots
    content = path.read_text()
    assert "08:30 ET — CPI" in content


@requires_db
async def test_fill_in_place_skips_calendar_already_filled(fake_vault):
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text(make_note_text(calendar_filled=True))

    result = await daily_module.run_daily_prefill(when=when)
    assert "market_calendar (his content — not touched)" in result.skipped_slots
    content = path.read_text()
    assert "- real calendar content already here" in content
    assert "CPI" not in content


@requires_db
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


@requires_db
async def test_missing_rules_anchor_appends_at_end_and_touches_nothing(fake_vault):
    """L28 replaced the old fail-the-whole-run behaviour: a note with no
    anchor gets the section appended at the END, nothing above it
    touched, and the placement is reported."""
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    original = "# just a stub note\n\nno matching anchors here\n"
    path.write_text(original)

    result = await daily_module.run_daily_prefill(when=when)
    content = path.read_text()
    assert content.startswith(original)
    assert "<!-- cobalt:section rules -->" in content
    assert any("anchor not found" in note for w in result.writes for note in w.notes)


@requires_db
async def test_aset_stub_takes_the_merge_path_and_keeps_everything(fake_vault):
    """The 09-03 defect, dead. The old code hit
    `existing.split(STUB_BANNER, 1)[1]` and rendered a fresh template in
    front of the remainder — discarding EVERYTHING above the banner. Here
    there is human text above it; it must survive byte-for-byte, and the
    card below it must survive too."""
    when = datetime(2026, 9, 3, 10, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-09-03.md"
    human_above = "# 2026-09-03\n\nSleep: 80\nReadiness: 81\n1% goal: exit on structure break\n\n"
    card_block = "\n### 10:02:06 — TSLA LONG B\n```aset\nticker: TSLA\n```\n"
    path.write_text(f"{human_above}{STUB_BANNER}{card_block}")

    result = await daily_module.run_daily_prefill(when=when)
    assert result.action != "upgraded_stub"  # that branch no longer exists
    content = path.read_text()
    assert content.startswith(human_above), "human text above the stub banner was destroyed"
    assert "Sleep: 80" in content
    assert "1% goal: exit on structure break" in content
    assert STUB_BANNER.rstrip("\n") in content
    assert "### 10:02:06 — TSLA LONG B" in content
    assert "ticker: TSLA" in content


@requires_db
async def test_pre_l28_slot_markers_are_not_duplicated(fake_vault):
    """Historical notes are NOT retro-marked. A note carrying the old
    `<!-- cobalt-slot:rules -->` marker must not get a second rules
    block bolted on."""
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    text = make_note_text().replace(
        "### Trading",
        "<!-- cobalt-slot:rules -->\n- [ ] old rules block\n<!-- /cobalt-slot:rules -->\n\n### Trading",
        1,
    )
    path.write_text(text)

    result = await daily_module.run_daily_prefill(when=when)
    assert "rules (already filled)" in result.skipped_slots
    content = path.read_text()
    assert "<!-- cobalt:section rules -->" not in content
    assert content.count("- [ ] old rules block") == 1


@requires_db
async def test_card_appended_during_fetch_window_is_not_clobbered(fake_vault, monkeypatch):
    """Root-cause regression test: a card lands WHILE this run is
    mid-fetch. The pre-L28 code read `existing` before the fetch and
    wrote that stale snapshot back after, silently discarding the card."""
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text(make_note_text())

    async def _market_then_append(*a, **kw):
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


@requires_db
async def test_dry_run_writes_nothing(fake_vault):
    when = datetime(2026, 8, 31, 8, 45, 0)
    path = fake_vault / "1 - Trading" / "1- Daily Notes" / "2026-08-31.md"
    path.write_text(make_note_text())
    before = hashlib.sha256(path.read_bytes()).hexdigest()

    result = await daily_module.run_daily_prefill(when=when, dry_run=True)
    assert hashlib.sha256(path.read_bytes()).hexdigest() == before
    assert any(w.diff for w in result.writes), "a dry run must still show the diff"
    assert all(w.write_id is None for w in result.writes)
