"""S2-P2 STEP-10 — `cobalt cards shadow-report [--since]` over
`"user".shadow_agreement_v` (09-14 group-2 ruling; R6).

Per factor: sessions, pairs, median |Δ| and share within 2 against the
`card.shadow_promotion_bar` trader setting. It prints GATE MET / NOT MET
and never flips anything. Offline rows here are the view's exact shape;
the view itself is proven on cobalt_dev by the `requires_db` test.
"""

from __future__ import annotations

import argparse
import inspect
import os
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal

import pytest

from cobalt.cards import cli as cards_cli
from cobalt.cards import shadow_report as sr
from cobalt.db_migrations import MIGRATIONS_DIR
from cobalt.settings.card import ShadowPromotionBar

BAR = ShadowPromotionBar(sessions=10, pairs=30, median_max=Decimal("1"), within2_min=Decimal("0.90"))
DAY0 = date(2026, 9, 21)


def _row(factor: str, day: date, deltas: list[int]) -> dict:
    return {"user_id": 1, "factor": factor, "trade_date": day, "pairs": len(deltas),
            "median_abs_delta": float(sorted(deltas)[len(deltas) // 2]),
            "within2_share": sum(d <= 2 for d in deltas) / len(deltas), "deltas": deltas}


def _rows_met() -> list[dict]:
    return [_row("rvol", DAY0 + timedelta(days=i), [0, 1, 1]) for i in range(10)]


def test_the_view_groups_by_factor_and_et_trading_day_and_keeps_every_delta():
    sql = (MIGRATIONS_DIR / "0007_radar_cards.sql").read_text()
    view = sql.split('CREATE OR REPLACE VIEW "user".shadow_agreement_v AS', 1)[1].split(";", 1)[0]
    assert "AT TIME ZONE 'America/New_York')::date AS trade_date" in view
    assert "array_agg(abs(t.grade - t.engine_grade_at_tap) ORDER BY t.id) AS deltas" in view
    assert "WHERE t.engine_grade_at_tap IS NOT NULL" in view
    assert 'DROP VIEW IF EXISTS "user".shadow_agreement_v;' in sql  # a changed column list is not OR REPLACE-able


def test_report_counts_sessions_pairs_median_and_within_two_per_factor():
    rows = [*_rows_met(), _row("atrs_from_open", DAY0, [0, 3, 4, 5])]
    report = sr.shadow_report(rows, bar=BAR, since=None)
    by = {f.factor: f for f in report.factors}
    assert (by["rvol"].sessions, by["rvol"].pairs) == (10, 30)
    assert by["rvol"].median_abs_delta == Decimal("1") and by["rvol"].within2_share == Decimal("1")
    assert by["rvol"].gate_met and by["rvol"].misses == []
    atr = by["atrs_from_open"]
    assert (atr.sessions, atr.pairs, atr.median_abs_delta, atr.within2_share) == (1, 4, Decimal("3.5"), Decimal("0.25"))
    assert not atr.gate_met
    assert atr.misses == ["sessions 1 < 10", "pairs 4 < 30", "median |Δ| 3.5 > 1", "within-2 share 0.25 < 0.90"]


def test_the_median_is_over_all_pairs_not_a_median_of_daily_medians():
    rows = [_row("rvol", DAY0, [0, 0, 0]), _row("rvol", DAY0 + timedelta(days=1), [5]),
            _row("rvol", DAY0 + timedelta(days=2), [5])]
    assert sr.shadow_report(rows, bar=BAR, since=None).factors[0].median_abs_delta == Decimal("0")


def test_since_filters_by_trading_day():
    report = sr.shadow_report(_rows_met(), bar=BAR, since=DAY0 + timedelta(days=5))
    assert report.factors[0].sessions == 5 and not report.factors[0].gate_met


def test_rendered_report_prints_gate_status_text_per_factor():
    rows = [*_rows_met(), _row("atrs_from_open", DAY0, [0, 3, 4, 5])]
    text = sr.render_report(sr.shadow_report(rows, bar=BAR, since=None))
    assert "rvol" in text and "GATE MET" in text
    assert "atrs_from_open" in text and "GATE NOT MET (sessions 1 < 10; pairs 4 < 30" in text
    assert "never flips" in text


def test_no_pairs_is_said_plainly_not_rendered_as_an_empty_table():
    text = sr.render_report(sr.shadow_report([], bar=BAR, since=None))
    assert "no tap/shadow pairs recorded" in text and "GATE NOT MET" in text


def test_a_row_that_disagrees_with_its_own_deltas_is_refused():
    bad = _row("rvol", DAY0, [0, 1, 1]) | {"pairs": 4}
    with pytest.raises(sr.ShadowReportError, match="pairs"):
        sr.shadow_report([bad], bar=BAR, since=None)


def test_the_bar_is_required_never_defaulted(monkeypatch, capsys):
    class Reader:
        def current(self):
            from cobalt.settings.card import CardSettings

            return CardSettings.from_rows({"radar.cards_enabled": False})

    monkeypatch.setattr(sr, "CardSettingsReader", Reader)
    monkeypatch.setattr(sr, "CardStore", lambda: (_ for _ in ()).throw(AssertionError("store read before the bar")))
    with pytest.raises(SystemExit, match="card.shadow_promotion_bar"):
        sr.cmd_shadow_report(argparse.Namespace(since=None))


def test_the_report_never_flips_anything(monkeypatch, capsys):
    class Store:
        def shadow_agreement(self, since):
            return _rows_met()

    class Reader:
        def current(self):
            from cobalt.settings.card import CardSettings

            return CardSettings.from_rows({"radar.cards_enabled": False, "card.shadow_promotion_bar": BAR.model_dump()})

    monkeypatch.setattr(sr, "CardStore", Store)
    monkeypatch.setattr(sr, "CardSettingsReader", Reader)
    sr.cmd_shadow_report(argparse.Namespace(since="2026-09-21"))
    assert "GATE MET" in capsys.readouterr().out
    source = inspect.getsource(sr)
    for write in (".put(", "INSERT", "UPDATE", "transition(", "upsert", "TraderSettingsStore", "VaultWriter"):
        assert write not in source
    parser = argparse.ArgumentParser()
    cards_cli.add_parser(parser.add_subparsers(dest="group"))
    args = parser.parse_args(["cards", "shadow-report", "--since", "2026-09-21"])
    assert args.since == "2026-09-21"
