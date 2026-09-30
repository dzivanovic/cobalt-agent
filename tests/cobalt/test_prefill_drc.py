"""The DRC's reused unit helpers (`cobalt.prefill.drc`) — what DRC D3 kept.

DRC D3 retired the 15:40 prefill (v2 §8 `[F-22]`): `run_drc_prefill`, the
repo template render, `format_tickers_block`, `parse_fill_updates` and
`find_trade_note_for_card` left with it, and their tests with them (named
in the D3 build report, `## E4 THE ROWS` D3-5). The create / append /
idempotent / dry-run orchestration is the DRC build's now, proven in
`test_drc_build.py` / `test_drc_build_db.py` over his template's shape.
"""

import os
from datetime import datetime, timezone

import pytest

from cobalt.prefill.drc import (
    RULES_PLACEMENT,
    TRADES_PLACEMENT,
    format_card_reconcile_block,
    format_risk_parameters,
    format_rules_check_block,
)

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: runtime sheet config and write audit need cobalt_dev",
)


@requires_db
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


def _card(ticker, hh, mm, ss, **overrides):
    """A constructed card: created at `hh:mm:ss` ET on a constructed day."""
    base = dict(id=1, ticker=ticker, grade="B", direction="long",
                created_at=datetime(2001, 1, 2, hh + 5, mm, ss, tzinfo=timezone.utc))
    base.update(overrides)
    return base


class TestFormatCardReconcileBlock:
    """Slice 2.1a (2026-08-31), re-pointed by DRC D3: a card is a written
    plan; a card the build MATCHED to a trade was taken. Every other card —
    a pass, a phantom, a premarket exploration — gets a checklist line.
    Cobalt surfaces it; Dejan answers it (never guessed, never deleted).
    The build hands this helper exactly the cards with no trade."""

    def test_no_cards_renders_nothing_to_reconcile(self):
        assert "nothing to reconcile" in format_card_reconcile_block([])

    def test_a_card_with_no_trade_gets_a_checklist_line_at_its_et_time(self):
        block = format_card_reconcile_block([_card("NVDA", 9, 31, 5)])
        assert block == "- [ ] 09:31:05 NVDA (B LONG) — taken / passed / discarded?\n"

    def test_every_card_given_is_listed_in_order(self):
        block = format_card_reconcile_block([_card("NVDA", 9, 31, 5), _card("TSLA", 10, 5, 0, direction="short")])
        assert block.splitlines() == [
            "- [ ] 09:31:05 NVDA (B LONG) — taken / passed / discarded?",
            "- [ ] 10:05:00 TSLA (B SHORT) — taken / passed / discarded?",
        ]


def test_the_rules_check_block_carries_his_checkboxes_then_the_cards_with_no_trade():
    block = format_rules_check_block({
        "rules_checkbox_block": "- [ ] Card first. #process\n",
        "card_reconcile_block": format_card_reconcile_block([_card("NVDA", 9, 31, 5)]),
    })
    assert block.splitlines() == [
        "**Rules (copied from the morning note's checklist — Rules.md is the source):**",
        "- [ ] Card first. #process",
        "",
        "**Card reconcile (cards with no trade — taken / passed / discarded?):**",
        "- [ ] 09:31:05 NVDA (B LONG) — taken / passed / discarded?",
    ]


def test_the_placements_the_build_reuses():
    lines = ["### Catalyst + Set Up + Trades", "x"]
    assert TRADES_PLACEMENT.locate(lines) == (1, 1)
    assert RULES_PLACEMENT is None  # the end of the note (L28's default)
