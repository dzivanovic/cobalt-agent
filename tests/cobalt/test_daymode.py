"""F6 two-stage day mode + `.htk` match check — Charter §3 F6, §S1.

The Charter's own acceptance test is the first one here: "he loads the
full sheet on a half day -> card refused with the reason."

The rest of S1-P2's F6 list:

* pre-09:00 on any day -> the lowest ENABLED mode, by system rule;
* the 09:00 proposal carries "no prior DRC" in its reason when there is
  none;
* an overrule persists with its reason;
* a Sunday produces NO proposal row.

And the ruling's own portability test, which is the real point of the
design: **flipping `reduced_sheet` to a mocked `quarter` repoints the
floor and every refusal message with NO CODE CHANGE.** `reduced` is a
role, the config says which sheet plays it, and these tests are what
holds that line.
"""

import os
from datetime import date, datetime, timezone
from zoneinfo import ZoneInfo

import pytest

from cobalt.aset.config import ConfigError, SheetModeGrades, SheetModesConfig
from cobalt.aset.models import Grade
from cobalt.daymode.config import REDUCED, DayModeConfig
from cobalt.daymode.match import (
    SheetMismatch,
    assert_grade_allowed,
    assert_sheet_matches,
)
from cobalt.daymode.propose import (
    NO_PRIOR_DRC,
    decided_or_stage1,
    prior_trading_day,
    propose,
    stage1_mode,
)
from cobalt.daymode.store import DayModeError, DayModeStore

ET = ZoneInfo("America/New_York")


def _at(hour: int, minute: int = 0) -> datetime:
    """An ET instant on 2026-09-03, a plain full trading day."""
    return datetime(2026, 9, 3, hour, minute, tzinfo=ET)

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

_GRADES = dict(A_plus=170, A=70, B=30, C=11, D=0)


def _sheets(order=("half", "full")) -> SheetModesConfig:
    return SheetModesConfig(
        sheets={name: SheetModeGrades(**_GRADES) for name in order},
        order=list(order),
        enabled_grades=[Grade.A, Grade.B],
    )


def _cfg(
    *,
    reduced_sheet="half",
    enabled_modes=("reduced",),
    reduced_grades=(Grade.B,),
    order=("half", "full"),
    hotkeys=None,
) -> DayModeConfig:
    """A DayModeConfig built exactly the way the loader builds it."""
    if hotkeys is None:
        hotkeys = [
            {"file": "full.htk", "mode": "full"},
            {"file": "half.htk", "mode": "half"},
            {"file": "reduced_day.htk", "mode": "reduced"},
        ]
    sheets = _sheets(order)
    return DayModeConfig(
        reduced_sheet=reduced_sheet,
        reduced_enabled_grades=list(reduced_grades),
        enabled_modes=list(enabled_modes),
        hotkey_files=hotkeys,
        sheet_order=list(sheets.order),
        account_enabled_grades=list(sheets.enabled_grades),
    )


# =====================================================================
# The shipped config
# =====================================================================


class TestShippedConfig:
    def test_the_real_config_loads_and_reads_as_ruled(self):
        from cobalt.daymode.config import load_daymode_config

        cfg = load_daymode_config()
        assert cfg.modes == ["reduced", "half", "full"], "ladder is derived, low to high"
        assert cfg.enabled_modes == ["reduced"]
        assert cfg.lowest_enabled == "reduced"
        assert cfg.sheet_for("reduced") == "half", "reduced is a ROLE; half plays it today"
        assert [g.value for g in cfg.enabled_grades_for("reduced")] == ["B"]
        assert cfg.hotkey_file_names == ["full.htk", "half.htk", "reduced_day.htk"]

    def test_sheets_are_an_ordered_list_not_a_hardcoded_pair(self):
        from cobalt.aset.config import load_sheet_modes_config

        cfg = load_sheet_modes_config()
        assert cfg.order == ["half", "full"]
        # The dollar truth is unchanged by the reshape.
        assert cfg.dollars_for("full", "B") == 60
        assert cfg.dollars_for("half", "A") == 70


# =====================================================================
# THE RULING'S PORTABILITY TEST
# =====================================================================


class TestReducedIsARoleNotASheet:
    """Flip the pointer; the floor and the messages follow. No code edit."""

    def test_a_mocked_quarter_sheet_repoints_the_floor(self):
        today = _cfg()
        assert today.sheet_for(REDUCED) == "half"

        tomorrow = _cfg(
            order=("quarter", "half", "full"),
            reduced_sheet="quarter",
            hotkeys=[
                {"file": "full.htk", "mode": "full"},
                {"file": "half.htk", "mode": "half"},
                {"file": "quarter.htk", "mode": "quarter"},
                {"file": "reduced_day.htk", "mode": "reduced"},
            ],
        )
        assert tomorrow.modes == ["reduced", "quarter", "half", "full"]
        assert tomorrow.sheet_for(REDUCED) == "quarter"
        assert stage1_mode(tomorrow) == "reduced"
        # Nothing in the assertion above names `half` or `full`; the
        # ladder grew by one rung and the code did not change.

    def test_the_refusal_message_follows_the_pointer(self):
        quarter = _cfg(
            order=("quarter", "half", "full"),
            reduced_sheet="quarter",
            hotkeys=[
                {"file": "full.htk", "mode": "full"},
                {"file": "quarter.htk", "mode": "quarter"},
                {"file": "reduced_day.htk", "mode": "reduced"},
            ],
        )
        with pytest.raises(SheetMismatch) as excinfo:
            assert_grade_allowed(Grade.A, REDUCED, cfg=quarter)
        assert "QUARTER sheet" in str(excinfo.value), (
            "the message names the sheet the pointer resolves to, not a literal"
        )

    def test_a_dangling_pointer_is_refused_not_defaulted(self):
        with pytest.raises(Exception) as excinfo:
            _cfg(reduced_sheet="quarter")   # no quarter sheet declared
        assert "reduced_sheet" in str(excinfo.value)

    def test_the_reduced_rung_cannot_widen_the_account_ladder(self):
        with pytest.raises(Exception) as excinfo:
            _cfg(reduced_grades=(Grade.A_PLUS,))   # not in the account's [A, B]
        assert "WIDEN" in str(excinfo.value)


# =====================================================================
# Stage 1 — the system rule
# =====================================================================


class TestStage1:
    def test_pre_0900_is_the_lowest_enabled_mode(self):
        assert stage1_mode(_cfg()) == "reduced"

    def test_lowest_enabled_is_not_simply_the_lowest_rung(self):
        """With only the top rung permitted, the floor IS the top rung —
        'lowest ENABLED', never 'lowest'."""
        cfg = _cfg(enabled_modes=("full",))
        assert cfg.modes[0] == "reduced"
        assert stage1_mode(cfg) == "full"

    def test_an_undecided_proposal_leaves_stage_1_in_force(self):
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        row = {"proposed": "full", "decided": None}
        assert decided_or_stage1(row, cfg, _at(10, 30)) == "reduced"

    def test_a_decision_takes_over_from_stage_1(self):
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        assert decided_or_stage1(
            {"proposed": "half", "decided": "half"}, cfg, _at(10, 30)
        ) == "half"

    def test_no_row_at_all_is_stage_1(self):
        assert decided_or_stage1(None, _cfg(), _at(10, 30)) == "reduced"

    def test_before_0900_the_floor_holds_even_against_a_decision(self):
        """The premarket floor is a SYSTEM RULE — no stop can rest
        premarket — so a later decision does not reach back and override
        the session in which it could not have applied. The boundary is
        the `daymode.stage2_open` tunable, read by the code, not a
        literal (F16)."""
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        decided_full = {"proposed": "reduced", "decided": "full"}
        assert decided_or_stage1(decided_full, cfg, _at(8, 59)) == "reduced"
        assert decided_or_stage1(decided_full, cfg, _at(9, 0)) == "full"
        assert decided_or_stage1(decided_full, cfg, _at(5, 15)) == "reduced"

    def test_stage2_open_comes_from_tunables(self):
        from cobalt.daymode.propose import stage2_open

        assert stage2_open().strftime("%H:%M") == "09:00"


# =====================================================================
# Stage 2 — the 09:00 proposal
# =====================================================================


class TestProposal:
    def test_a_sunday_produces_no_proposal_and_no_row(self):
        assert propose(date(2026, 9, 6), cfg=_cfg()) is None    # Sunday

    def test_a_saturday_and_a_holiday_produce_none_too(self):
        assert propose(date(2026, 9, 5), cfg=_cfg()) is None    # Saturday
        assert propose(date(2026, 9, 7), cfg=_cfg()) is None    # Labor Day

    def test_no_prior_drc_appears_verbatim_in_the_reason(self):
        p = propose(date(2026, 9, 3), cfg=_cfg(), drc_note=None, band=(3, 6))
        assert p is not None
        assert NO_PRIOR_DRC in p.reason
        assert f"{NO_PRIOR_DRC} -> one rung down" in p.signals

    def test_a_drc_that_exists_but_is_unfilled_still_costs_a_rung(self):
        """The real 2026-09-03 DRC parsed as `grade (A+, A, B, C, etc..)`
        — the template's own placeholder, not a grade he wrote. Treated
        as a value it would have suppressed the step-down on a DRC that
        carries no information at all. Same rung cost as no DRC, but a
        different sentence: "you did not write one" and "you wrote one
        and left it blank" are different facts about his day."""
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        p = propose(
            date(2026, 9, 3), cfg=cfg,
            drc_note="DRC-2026-09-02.md (grade not filled, goal not filled)",
            drc_informative=False, band=(3, 6),
        )
        assert p.proposed == "half", "one rung down, same as no DRC"
        assert any("no headline field is filled" in s for s in p.signals)
        assert NO_PRIOR_DRC not in p.reason, "the note exists and is named"
        assert "DRC-2026-09-02.md" in p.reason

    def test_a_present_drc_is_cited_instead(self):
        p = propose(
            date(2026, 9, 3), cfg=_cfg(), drc_note="DRC-2026-09-02.md (grade B, goal 2)",
            drc_informative=True, band=(3, 6),
        )
        assert "DRC-2026-09-02.md" in p.reason
        assert NO_PRIOR_DRC not in p.reason

    def test_at_s1_the_proposal_is_always_the_floor_and_says_why(self):
        """reduced-only enabled -> reduced, every time, with the clamp
        named in the reason."""
        for day in (date(2026, 9, 1), date(2026, 9, 2), date(2026, 9, 3), date(2026, 11, 27)):
            p = propose(day, cfg=_cfg(), drc_note="DRC.md", drc_informative=True, band=(3, 6))
            assert p.proposed == "reduced", day
            assert "enabled ['reduced']" in p.reason

    def test_the_ladder_still_exercises_the_higher_rungs(self):
        """With all three enabled and a clean day, the top rung wins."""
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        p = propose(date(2026, 9, 3), cfg=cfg, drc_note="DRC.md", drc_informative=True, band=(3, 6))
        assert p.proposed == "full"
        assert p.signals == []

    def test_no_prior_drc_steps_down_one_rung(self):
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        p = propose(date(2026, 9, 3), cfg=cfg, drc_note=None, band=(3, 6))
        assert p.proposed == "half"

    def test_a_daily_stop_on_the_prior_day_drops_to_the_floor(self):
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        p = propose(
            date(2026, 9, 3), cfg=cfg, drc_note="DRC.md", drc_informative=True,
            band=(3, 6), daily_stop_hit=True,
        )
        assert p.proposed == "reduced"
        assert any("daily stop" in s for s in p.signals)

    def test_an_early_close_steps_down(self):
        """2026-12-24: an early close whose prior trading day is the day
        before, so the early-close signal is the ONLY one firing."""
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        p = propose(date(2026, 12, 24), cfg=cfg, drc_note="DRC.md", drc_informative=True, band=(3, 6))
        assert p.signals == ["early close today -> one rung down"]
        assert p.proposed == "half"

    def test_signals_compound_downwards(self):
        """2026-11-27 is BOTH an early close and the first session after
        Thanksgiving, so it steps down twice: full -> half -> reduced.
        Adverse signals accumulate; they never cancel out."""
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        p = propose(date(2026, 11, 27), cfg=cfg, drc_note="DRC.md", drc_informative=True, band=(3, 6))
        assert any("early close" in s for s in p.signals)
        assert any("after a" in s for s in p.signals)
        assert p.proposed == "reduced"

    def test_the_first_session_after_a_holiday_steps_down(self):
        """2026-09-08, the Tuesday after Labor Day weekend."""
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        p = propose(date(2026, 9, 8), cfg=cfg, drc_note="DRC.md", drc_informative=True, band=(3, 6))
        assert any("after a" in s for s in p.signals)

    def test_an_unruled_band_pins_the_proposal_to_the_floor(self):
        """PLACEHOLDER tunables are themselves an adverse signal — an
        invented number must never justify a bigger rung."""
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        p = propose(date(2026, 9, 3), cfg=cfg, drc_note="DRC.md", drc_informative=True, band=(None, None))
        assert p.proposed == "reduced"
        assert any("PLACEHOLDER" in s for s in p.signals)
        assert "PLACEHOLDER (unruled" in p.reason

    def test_prior_trading_day_skips_the_weekend_and_the_holiday(self):
        assert prior_trading_day(date(2026, 9, 8)) == date(2026, 9, 4)   # over Labor Day
        assert prior_trading_day(date(2026, 9, 3)) == date(2026, 9, 2)


# =====================================================================
# The match check — the Charter's own acceptance test
# =====================================================================


class TestMatchCheck:
    def test_full_sheet_attested_on_a_reduced_day_refuses_with_the_reason(self):
        """Charter §3 F6: 'he loads the full sheet on a half day -> card
        refused with the reason.'"""
        cfg = _cfg()
        row = {"attested_sheet": "full.htk"}
        with pytest.raises(SheetMismatch) as excinfo:
            assert_sheet_matches(row, "reduced", cfg=cfg)
        message = str(excinfo.value)
        assert message == "sheet FULL loaded, day mode REDUCED — reload reduced_day.htk or overrule"

    def test_the_matching_sheet_passes(self):
        assert assert_sheet_matches({"attested_sheet": "reduced_day.htk"}, "reduced", cfg=_cfg()) \
            == "reduced_day.htk"

    def test_half_htk_is_not_the_reduced_rung(self):
        """`reduced_day.htk` carries the B-only restriction; `half.htk` is
        the plain half rung. Attesting the wrong one of the two is still
        a mismatch."""
        with pytest.raises(SheetMismatch, match="sheet HALF loaded, day mode REDUCED"):
            assert_sheet_matches({"attested_sheet": "half.htk"}, "reduced", cfg=_cfg())

    def test_attesting_nothing_is_a_refusal_not_a_pass(self):
        with pytest.raises(SheetMismatch, match="No hotkey file attested"):
            assert_sheet_matches({}, "reduced", cfg=_cfg())
        with pytest.raises(SheetMismatch, match="No hotkey file attested"):
            assert_sheet_matches(None, "reduced", cfg=_cfg())

    def test_an_unknown_htk_file_is_refused(self):
        with pytest.raises(ConfigError, match="unknown hotkey file"):
            assert_sheet_matches({"attested_sheet": "made_up.htk"}, "reduced", cfg=_cfg())


class TestGradeRestriction:
    def test_b_is_accepted_on_the_reduced_rung(self):
        assert_grade_allowed(Grade.B, "reduced", cfg=_cfg())   # no raise

    def test_a_plus_is_refused_on_the_reduced_rung(self):
        with pytest.raises(SheetMismatch) as excinfo:
            assert_grade_allowed(Grade.A_PLUS, "reduced", cfg=_cfg())
        message = str(excinfo.value)
        assert "key A+ is not enabled on the REDUCED rung" in message
        assert "['B']" in message

    def test_a_is_refused_on_the_reduced_rung_but_allowed_on_full(self):
        cfg = _cfg(enabled_modes=("reduced", "half", "full"))
        with pytest.raises(SheetMismatch):
            assert_grade_allowed(Grade.A, "reduced", cfg=cfg)
        assert_grade_allowed(Grade.A, "full", cfg=cfg)          # no raise


# =====================================================================
# Persistence
# =====================================================================


@requires_db
@pytest.mark.integration
class TestDayModeStore:
    @pytest.fixture
    def store(self):
        s = DayModeStore("cobalt_dev")
        s.ensure_schema()
        return s

    def test_proposal_then_approve(self, store):
        day = date(2026, 9, 3)
        store.upsert_proposal(day, proposed="reduced", reason="test reason")
        row = store.decide(day, decided="reduced", decided_by="you")
        assert row["proposed"] == "reduced" and row["decided"] == "reduced"
        assert row["decided_by"] == "you" and row["overrule_reason"] is None
        assert row["session"] == "rth"

    def test_overrule_persists_with_its_reason(self, store):
        day = date(2026, 9, 3)
        store.upsert_proposal(day, proposed="reduced", reason="test reason")
        row = store.decide(
            day, decided="full", decided_by="you",
            overrule_reason="clean tape, size back up",
        )
        assert row["decided"] == "full"
        assert row["overrule_reason"] == "clean tape, size back up"
        assert row["proposed"] == "reduced", "what Cobalt said is still on the row"

    def test_an_overrule_without_a_reason_is_refused(self, store):
        day = date(2026, 9, 3)
        store.upsert_proposal(day, proposed="reduced", reason="r")
        with pytest.raises(DayModeError, match="requires a reason"):
            store.decide(day, decided="full", decided_by="you")
        assert store.for_date(day)["decided"] is None

    def test_deciding_with_no_proposal_is_refused(self, store):
        with pytest.raises(DayModeError, match="nothing to decide"):
            store.decide(date(2026, 9, 2), decided="reduced", decided_by="you")

    def test_re_proposing_is_idempotent_and_never_unanswers_a_decision(self, store):
        day = date(2026, 9, 3)
        store.upsert_proposal(day, proposed="reduced", reason="first")
        store.decide(day, decided="reduced", decided_by="you")
        store.upsert_proposal(day, proposed="half", reason="second run")
        row = store.for_date(day)
        assert row["proposed"] == "half" and row["reason"] == "second run"
        assert row["decided"] == "reduced", "his answer survives a re-run of the job"

    def test_attestation_round_trips(self, store):
        day = date(2026, 9, 3)
        store.attest_sheet(day, filename="reduced_day.htk")
        assert store.for_date(day)["attested_sheet"] == "reduced_day.htk"
        store.attest_sheet(day, filename="full.htk")
        assert store.for_date(day)["attested_sheet"] == "full.htk"

    def test_a_card_is_refused_while_the_attested_sheet_disagrees(self, store):
        """End to end: attest FULL, day mode REDUCED, card refused."""
        day = date(2026, 9, 3)
        store.attest_sheet(day, filename="full.htk")
        store.upsert_proposal(day, proposed="reduced", reason="r")
        row = store.decide(day, decided="reduced", decided_by="you")
        with pytest.raises(SheetMismatch, match="reload reduced_day.htk or overrule"):
            assert_sheet_matches(row, decided_or_stage1(row, _cfg()), cfg=_cfg())

    def test_writes_are_refused_in_market_reset(self, store, monkeypatch):
        from cobalt.session import SessionBlocked
        from cobalt.session import clock as clock_mod

        monkeypatch.setattr(
            clock_mod, "now_utc", lambda: datetime(2026, 9, 4, 0, 30, tzinfo=timezone.utc)
        )
        with pytest.raises(SessionBlocked):
            store.upsert_proposal(date(2026, 9, 4), proposed="reduced", reason="r")
