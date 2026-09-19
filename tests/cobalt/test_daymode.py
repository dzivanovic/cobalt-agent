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


#: The step-down table the shipped config carries, as the tests need it
#: — built from `SIGNAL_IDS` so a new signal cannot be added to the code
#: without this helper (and therefore every test) noticing.
_STEPDOWNS = [
    {"signal": "daily_stop_hit", "effect": "floor",
     "because": "daily stop hit on the prior trading day"},
    {"signal": "no_prior_drc", "effect": "down", "rungs": 1,
     "because": "no prior DRC"},
    {"signal": "drc_not_informative", "effect": "down", "rungs": 1,
     "because": "prior DRC exists but no headline field is filled"},
    {"signal": "early_close_today", "effect": "down", "rungs": 1,
     "because": "early close today"},
    {"signal": "first_session_after_close", "effect": "down", "rungs": 1,
     "because": "first session after a multi-day close"},
    {"signal": "trade_count_band_placeholder", "effect": "floor",
     "because": "trade_count_band is PLACEHOLDER (unruled)"},
    {"signal": "trade_count_over_band", "effect": "down", "rungs": 1,
     "because": "trade count above the ruled band"},
]


def _cfg(
    *,
    reduced_sheet="half",
    enabled_modes=("reduced",),
    reduced_grades=(Grade.A, Grade.B),
    order=("half", "full"),
    hotkey_template="{sheet}.htk",
    stepdowns=None,
) -> DayModeConfig:
    """A DayModeConfig built exactly the way the loader builds it."""
    sheets = _sheets(order)
    return DayModeConfig(
        reduced_sheet=reduced_sheet,
        reduced_enabled_grades=list(reduced_grades),
        enabled_modes=list(enabled_modes),
        hotkey_file_template=hotkey_template,
        stepdowns=[dict(s) for s in (stepdowns or _STEPDOWNS)],
        sheet_order=list(sheets.order),
        account_enabled_grades=list(sheets.enabled_grades),
    )


# =====================================================================
# The shipped config
# =====================================================================


@requires_db
class TestShippedConfig:
    def test_the_real_config_loads_and_reads_as_ruled(self):
        from cobalt.daymode.config import load_daymode_config

        cfg = load_daymode_config()
        assert cfg.modes == ["reduced", "half", "full"], "ladder is derived, low to high"
        assert cfg.enabled_modes == ["reduced"]
        assert cfg.lowest_enabled == "reduced"
        assert cfg.sheet_for("reduced") == "half", "reduced is a ROLE; half plays it today"
        # RE-RULED by the CTO review of S1-P2: the reduced rung is a SIZE
        # rung, not a grade ban. A is taken at reduced size; A+ is out
        # because the ACCOUNT ladder does not enable it. That sentence IS
        # the invariant — `reduced ⊆ account` — and it is what this
        # asserts. The ladder's members are the trader's own setting (L32
        # user data) and are not pinned here: grade C was re-enabled by
        # his ruling of 2026-09-14 (weekly review with his trading
        # psychologist) and applied by his own `settings load --apply` at
        # 07:59, which turned a pinned `["A", "B"]` red —
        # PROJECT-LEDGER.md line 1393 overrules the "reduced keeps A, B"
        # assumption by name. A test that reads the live settings table
        # and pins his current choice breaks on his next one.
        reduced = cfg.enabled_grades_for("reduced")
        account = cfg.enabled_grades_for("full")
        assert reduced, "the reduced rung always permits at least one grade"
        assert set(reduced) <= set(account), (
            "the reduced rung NARROWS the account ladder and can never widen it"
        )
        assert reduced == [g for g in Grade if g in set(reduced)], "in ladder order"
        # DERIVED from the declared sheets, in ladder order — no
        # hand-named file, and no `reduced_day.htk` (a name that
        # corresponded to no key table in configs/cobalt/aset.yaml).
        assert cfg.hotkey_file_names == ["half.htk", "full.htk"]
        assert cfg.hotkey_file_for_mode("reduced") == "half.htk"

    def test_every_computable_signal_is_ruled_in_the_table(self):
        from cobalt.daymode.config import SIGNAL_IDS, load_daymode_config

        cfg = load_daymode_config()
        assert sorted(r.signal for r in cfg.stepdowns) == sorted(SIGNAL_IDS)

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

        tomorrow = _cfg(order=("quarter", "half", "full"), reduced_sheet="quarter")
        assert tomorrow.modes == ["reduced", "quarter", "half", "full"]
        assert tomorrow.sheet_for(REDUCED) == "quarter"
        assert stage1_mode(tomorrow) == "reduced"
        # Nothing in the assertion above names `half` or `full`; the
        # ladder grew by one rung and the code did not change.

    def test_the_refusal_message_follows_the_pointer(self):
        quarter = _cfg(
            order=("quarter", "half", "full"),
            reduced_sheet="quarter",
            reduced_grades=(Grade.B,),
        )
        with pytest.raises(SheetMismatch) as excinfo:
            assert_grade_allowed(Grade.A, REDUCED, cfg=quarter)
        assert "QUARTER sheet" in str(excinfo.value), (
            "the message names the sheet the pointer resolves to, not a literal"
        )

    def test_a_sheet_added_in_config_appears_in_the_selector(self):
        """CTO review of S1-P2: the attested-sheet selector is DERIVED.

        Adding a rung is a `configs/cobalt/aset.yaml` edit and nothing
        else — no hand-named file, no code change here or in src/. The
        assertion below names `quarter.htk`, and nothing produced it but
        the template applied to the declared sheet id.
        """
        before = _cfg()
        assert before.hotkey_file_names == ["half.htk", "full.htk"]

        after = _cfg(order=("quarter", "half", "full"), reduced_sheet="quarter")
        assert after.hotkey_file_names == ["quarter.htk", "half.htk", "full.htk"]
        assert after.sheet_for_hotkey_file("quarter.htk") == "quarter"
        assert after.hotkey_file_for_mode(REDUCED) == "quarter.htk"

    def test_a_template_with_no_placeholder_is_refused(self):
        with pytest.raises(Exception) as excinfo:
            _cfg(hotkey_template="keys.htk")
        assert "hotkey_file_template" in str(excinfo.value)

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
        assert any(s.startswith(f"{NO_PRIOR_DRC} -> one rung down") for s in p.signals)

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
        assert p.signals == ["early close today -> one rung down (half)"]
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
        assert message == (
            "sheet FULL loaded, day mode REDUCED (= the HALF sheet) — "
            "reload half.htk or overrule"
        )

    def test_the_matching_sheet_passes(self):
        """The attestation is compared SHEET to SHEET (CTO review of
        S1-P2). `reduced` sizes from `half`, so `half.htk` matches — and
        there is no `reduced_day.htk` any more, because no key table in
        configs/cobalt/aset.yaml ever corresponded to that name."""
        assert assert_sheet_matches({"attested_sheet": "half.htk"}, "reduced", cfg=_cfg()) \
            == "half.htk"

    def test_a_file_naming_no_declared_sheet_is_refused(self):
        with pytest.raises(ConfigError, match="unknown hotkey file"):
            assert_sheet_matches({"attested_sheet": "reduced_day.htk"}, "reduced", cfg=_cfg())

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
        assert "['A', 'B']" in message

    def test_a_is_accepted_on_the_reduced_rung(self):
        """RE-RULED by the CTO review of S1-P2: the reduced rung is a
        SIZE rung, not a grade ban. An A setup on a reduced day is still
        an A, taken at reduced size."""
        assert_grade_allowed(Grade.A, "reduced", cfg=_cfg())    # no raise

    def test_a_narrower_rung_still_refuses_by_config_alone(self):
        """The narrowing mechanism is unchanged — only the value moved.
        A config that puts B alone on the rung still refuses A, with no
        code edit either way."""
        cfg = _cfg(reduced_grades=(Grade.B,), enabled_modes=("reduced", "half", "full"))
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
        store.attest_sheet(day, filename="half.htk")
        assert store.for_date(day)["attested_sheet"] == "half.htk"
        store.attest_sheet(day, filename="full.htk")
        assert store.for_date(day)["attested_sheet"] == "full.htk"

    def test_a_card_is_refused_while_the_attested_sheet_disagrees(self, store):
        """End to end: attest FULL, day mode REDUCED, card refused."""
        day = date(2026, 9, 3)
        store.attest_sheet(day, filename="full.htk")
        store.upsert_proposal(day, proposed="reduced", reason="r")
        row = store.decide(day, decided="reduced", decided_by="you")
        with pytest.raises(SheetMismatch, match="reload half.htk or overrule"):
            assert_sheet_matches(row, decided_or_stage1(row, _cfg()), cfg=_cfg())

    def test_writes_are_refused_in_market_reset(self, store, monkeypatch):
        from cobalt.session import SessionBlocked
        from cobalt.session import clock as clock_mod

        monkeypatch.setattr(
            clock_mod, "now_utc", lambda: datetime(2026, 9, 4, 0, 30, tzinfo=timezone.utc)
        )
        with pytest.raises(SessionBlocked):
            store.upsert_proposal(date(2026, 9, 4), proposed="reduced", reason="r")


# =====================================================================
# The step-down table is CONFIG (S1-P3, CTO review of S1-P2)
# =====================================================================


class TestStepDownsAreData:
    """The rule SET moved out of `propose.py` into
    `configs/cobalt/daymode.yaml`. These tests change the TABLE and watch
    the proposal change — no code edit anywhere."""

    def test_ruling_a_rule_off_stops_it_firing(self):
        from cobalt.daymode.propose import propose

        rules = [dict(s) for s in _STEPDOWNS]
        cfg = _cfg(enabled_modes=("reduced", "half", "full"), stepdowns=rules)
        p = propose(date(2026, 12, 24), cfg=cfg, drc_note="DRC.md",
                    drc_informative=True, band=(3, 6))
        assert p.proposed == "half", "early close costs a rung, as shipped"

        off = [dict(s) for s in _STEPDOWNS]
        next(r for r in off if r["signal"] == "early_close_today")["effect"] = "none"
        cfg_off = _cfg(enabled_modes=("reduced", "half", "full"), stepdowns=off)
        p2 = propose(date(2026, 12, 24), cfg=cfg_off, drc_note="DRC.md",
                     drc_informative=True, band=(3, 6))
        assert p2.proposed == "full", "the same day, the same code, a different table"
        assert any("ruled off in config" in s for s in p2.signals), (
            "a rule ruled off is VISIBLE in the sentence, not absent from it"
        )

    def test_the_rung_cost_is_config_not_a_constant(self):
        from cobalt.daymode.propose import propose

        two = [dict(s) for s in _STEPDOWNS]
        next(r for r in two if r["signal"] == "early_close_today")["rungs"] = 2
        cfg = _cfg(enabled_modes=("reduced", "half", "full"), stepdowns=two)
        p = propose(date(2026, 12, 24), cfg=cfg, drc_note="DRC.md",
                    drc_informative=True, band=(3, 6))
        assert p.proposed == "reduced", "full -> (2 rungs) -> reduced"
        assert any("2 rungs down" in s for s in p.signals)

    def test_the_words_in_the_sentence_come_from_the_table(self):
        from cobalt.daymode.propose import propose

        reworded = [dict(s) for s in _STEPDOWNS]
        next(r for r in reworded if r["signal"] == "no_prior_drc")["because"] = (
            "you skipped last night's review"
        )
        cfg = _cfg(enabled_modes=("reduced", "half", "full"), stepdowns=reworded)
        p = propose(date(2026, 9, 3), cfg=cfg, drc_note=None, band=(3, 6))
        assert any("you skipped last night's review" in s for s in p.signals)

    def test_an_unknown_signal_is_a_loud_config_error(self):
        bad = [dict(s) for s in _STEPDOWNS] + [
            {"signal": "mercury_retrograde", "effect": "floor", "because": "no"}
        ]
        with pytest.raises(Exception) as excinfo:
            _cfg(stepdowns=bad)
        assert "unknown step-down signal" in str(excinfo.value)

    def test_a_signal_left_out_of_the_table_is_refused(self):
        """Silence is never how a policy hole gets made: turning a rule
        off is `effect: none`, visibly, not deleting its row."""
        short = [dict(s) for s in _STEPDOWNS if s["signal"] != "daily_stop_hit"]
        with pytest.raises(Exception) as excinfo:
            _cfg(stepdowns=short)
        assert "no row for" in str(excinfo.value)

    def test_every_signal_the_table_rules_has_a_fact_behind_it(self):
        """The other direction: a signal ruled in config that the code
        cannot compute would sit there looking like a rule and never
        fire."""
        from cobalt.daymode.config import SIGNAL_IDS
        from cobalt.daymode.propose import _facts

        facts = _facts(
            _cfg(), date(2026, 9, 3),
            daily_stop_hit=False, drc_note=None, drc_informative=False,
            prior_day=date(2026, 9, 2), band=(3, 6),
        )
        assert sorted(facts) == sorted(SIGNAL_IDS)


class TestTradeCountBandRuled:
    """`daymode.trade_count_band` 2-6, ruled 2026-09-16 (Dejan): "2 - 6 and
    make it tunable". The value is his (dynamic), read from tunables."""

    _ALL = ("reduced", "half", "full")

    def test_the_shipped_band_is_the_ruled_2_to_6(self):
        from cobalt.daymode.cli import _band
        from cobalt.taxonomy.loader import load_tunables

        assert _band() == (2, 6)
        by_key = load_tunables().by_key
        for key in ("daymode.trade_count_band.min", "daymode.trade_count_band.max"):
            assert by_key[key].status == "solidified"
            assert by_key[key].source == "ruling"
            assert by_key[key].dynamic is True

    def test_a_day_with_4_trades_is_not_adverse(self):
        p = propose(
            date(2026, 9, 3), cfg=_cfg(enabled_modes=self._ALL), prior_filled=4,
            drc_note="DRC.md", drc_informative=True, band=(2, 6),
        )
        assert p.proposed == "full"
        assert p.signals == []
        assert "trade-count band: 2-6" in p.reason

    def test_an_unset_band_still_pins_to_the_floor(self):
        """Regression: an unruled (null) band is an adverse signal -> floor."""
        p = propose(
            date(2026, 9, 3), cfg=_cfg(enabled_modes=self._ALL), prior_filled=4,
            drc_note="DRC.md", drc_informative=True, band=(None, None),
        )
        assert p.proposed == "reduced"
        assert any("PLACEHOLDER" in s for s in p.signals)

    def test_a_day_with_7_trades_is_adverse(self):
        """RULED 2026-09-17 (Dejan, R13, "ruling A."): over the band =
        adverse, one rung down. Was a strict xfail until the signal and
        its step-down row existed."""
        p = propose(
            date(2026, 9, 3), cfg=_cfg(enabled_modes=self._ALL), prior_filled=7,
            drc_note="DRC.md", drc_informative=True, band=(2, 6),
        )
        assert p.signals, "7 trades is above the ruled band 2-6"
        assert p.proposed != "full"


class TestOverBandStepDown:
    """R13's shape, one test per branch of it: ABOVE `.max` costs one
    rung, BELOW `.min` costs nothing, inside the band changes nothing."""

    _ALL = ("reduced", "half", "full")

    def test_exactly_the_band_max_is_not_adverse(self):
        """The band is INCLUSIVE at its edge — 6 is inside 2-6."""
        p = propose(
            date(2026, 9, 3), cfg=_cfg(enabled_modes=self._ALL), prior_filled=6,
            drc_note="DRC.md", drc_informative=True, band=(2, 6),
        )
        assert p.signals == []
        assert p.proposed == "full"

    def test_one_over_the_band_max_is_one_rung_down(self):
        p = propose(
            date(2026, 9, 3), cfg=_cfg(enabled_modes=self._ALL), prior_filled=7,
            drc_note="DRC.md", drc_informative=True, band=(2, 6),
        )
        assert p.proposed == "half", "one rung down from full"
        assert any("trade count above the ruled band" in s for s in p.signals)

    def test_the_clause_cites_the_count_and_the_band(self):
        """L57: the number is replayable from the sentence he reads."""
        p = propose(
            date(2026, 9, 3), cfg=_cfg(enabled_modes=self._ALL), prior_filled=9,
            drc_note="DRC.md", drc_informative=True, band=(2, 6),
        )
        clause = next(s for s in p.signals if "above the ruled band" in s)
        assert "9 trade(s) vs band 2-6" in clause
        assert "one rung down (half)" in clause

    def test_under_the_band_min_is_not_a_signal(self):
        """His ruling, explicitly: under the band does nothing."""
        p = propose(
            date(2026, 9, 3), cfg=_cfg(enabled_modes=self._ALL), prior_filled=1,
            drc_note="DRC.md", drc_informative=True, band=(2, 6),
        )
        assert p.signals == []
        assert p.proposed == "full"

    def test_an_unruled_band_fires_the_placeholder_and_not_the_over_band_row(self):
        """Regression against a None comparison: with no band there is
        nothing to be over, so only the placeholder fires."""
        p = propose(
            date(2026, 9, 3), cfg=_cfg(enabled_modes=self._ALL), prior_filled=99,
            drc_note="DRC.md", drc_informative=True, band=(None, None),
        )
        assert p.proposed == "reduced"
        assert any("PLACEHOLDER" in s for s in p.signals)
        assert not any("above the ruled band" in s for s in p.signals)

    def test_the_effect_is_the_tables_not_the_codes(self):
        """The cost is a config row: reword and re-price it and the
        proposal follows, with no edit in src/."""
        repriced = [dict(s) for s in _STEPDOWNS]
        row = next(r for r in repriced if r["signal"] == "trade_count_over_band")
        row["effect"] = "floor"
        row["because"] = "you traded too many times yesterday"
        p = propose(
            date(2026, 9, 3),
            cfg=_cfg(enabled_modes=self._ALL, stepdowns=repriced), prior_filled=7,
            drc_note="DRC.md", drc_informative=True, band=(2, 6),
        )
        assert p.proposed == "reduced"
        assert any("you traded too many times yesterday" in s for s in p.signals)


# ---------------------------------------------------------------------
# Band validation (ops 2026-09-19, item b1 — `cto-2026-09-18.md` §18 F2)
# ---------------------------------------------------------------------

#: Every band the validator must ACCEPT, with the `day_facts` dict each
#: one produces. The dicts were computed on the UNTOUCHED code path and
#: pinned here before `validate_band` existed: this is the test that says
#: the validation chunk changes no fact for any VALID band. Validation is
#: a config gate — it is not on the fact-computing path at all.
_ACCEPTED_BANDS = [
    ((2, 6), False),      # his live, ruled band
    ((3, 3), False),      # a one-value band: min == max is a band
    ((None, None), True),  # unruled -> PLACEHOLDER, deliberately adverse
    ((2, None), True),     # HALF-SET: still "not ruled yet" today (b2 is scoped out)
    ((None, 6), True),     # HALF-SET, the other side
]


class TestABandThatIsValidChangesNothing:
    """L7 / CLAUDE.md HITL: this is the day-mode path. For every band the
    validator accepts, `day_facts` must be byte-identical to today's."""

    @pytest.mark.parametrize("band,placeholder", _ACCEPTED_BANDS)
    def test_the_facts_for_an_accepted_band_are_todays_facts(self, band, placeholder):
        from cobalt.daymode.propose import _facts

        facts = _facts(
            _cfg(), date(2026, 9, 3),
            daily_stop_hit=False, drc_note="DRC.md", drc_informative=True,
            prior_day=date(2026, 9, 2), band=band, prior_filled=2,
        )
        assert facts == {
            "daily_stop_hit": False,
            "no_prior_drc": False,
            "drc_not_informative": False,
            "early_close_today": False,
            "first_session_after_close": False,
            "trade_count_band_placeholder": placeholder,
            "trade_count_over_band": False,
        }

    @pytest.mark.parametrize("band,placeholder", _ACCEPTED_BANDS)
    def test_the_validator_accepts_it(self, band, placeholder):
        from cobalt.daymode.propose import validate_band

        assert validate_band(*band) is None


#: Every band the validator must REFUSE. `cto-2026-09-18.md` §18 F2:
#: "the over-band fact has no guard for an inverted (min > max) or
#: half-set band". b1 closes the inverted and the non-integer cases; the
#: half-set case is SCOPED OUT as a DESIGN question (see the accepted
#: list above and `validate_band`'s docstring).
_REFUSED_BANDS = [
    (6, 2),        # inverted — nothing can be inside it
    (2, "6"),      # a string is not a count
    (2.5, 6),      # a fraction of a trade is not a count
    (-1, 6),       # a negative count
    (True, 6),     # a bool IS an int to Python; it is not a count here
]


class TestTheBandValidatorRefusesWhatCannotBeABand:
    """L1 fail-loud + L10 config-as-code: a band that cannot be a band is
    caught at the deploy's `validate`, not at 09:00 by
    `com.cobalt.daymode-propose`."""

    @pytest.mark.parametrize("band", _REFUSED_BANDS)
    def test_it_is_refused_naming_both_keys_and_both_values(self, band):
        from cobalt.daymode.propose import (
            BAND_MAX_KEY,
            BAND_MIN_KEY,
            BandError,
            validate_band,
        )

        with pytest.raises(BandError) as excinfo:
            validate_band(*band)
        message = str(excinfo.value)
        # both keys AND both values, so the operator can find the rows
        assert f"{BAND_MIN_KEY}={band[0]!r}" in message
        assert f"{BAND_MAX_KEY}={band[1]!r}" in message
        assert "tunables.yaml" in message

    def test_the_inverted_band_says_why(self):
        from cobalt.daymode.propose import BandError, validate_band

        with pytest.raises(BandError) as excinfo:
            validate_band(6, 2)
        assert "min must be <= max" in str(excinfo.value)

    def test_a_non_integer_names_the_offending_key(self):
        from cobalt.daymode.propose import BAND_MAX_KEY, BandError, validate_band

        with pytest.raises(BandError) as excinfo:
            validate_band(2, "6")
        assert BAND_MAX_KEY in str(excinfo.value).split("—")[1]


class _Row:
    def __init__(self, value):
        self.value = value


class _Tunables:
    def __init__(self, by_key):
        self.by_key = by_key


def _fake_tunables(band_min, band_max):
    from cobalt.daymode.propose import BAND_MAX_KEY, BAND_MIN_KEY

    return _Tunables({BAND_MIN_KEY: _Row(band_min), BAND_MAX_KEY: _Row(band_max)})


class TestBothReadersOfTheTwoRowsValidate:
    """L3: ONE validator, two call sites. `daymode/cli.py._band()` is the
    09:00 reader; `cobalt validate` (`src/cobalt/cli.py`) is the deploy
    gate that today prints the two rows and checks nothing."""

    @pytest.mark.parametrize("band", _REFUSED_BANDS)
    def test_band_refuses_it(self, band, monkeypatch):
        from cobalt.daymode import cli as daymode_cli

        monkeypatch.setattr(daymode_cli, "load_tunables", lambda: _fake_tunables(*band))
        with pytest.raises(SystemExit) as excinfo:
            daymode_cli._band()
        assert "trade-count band" in str(excinfo.value)

    @pytest.mark.parametrize("band,placeholder", _ACCEPTED_BANDS)
    def test_band_still_returns_an_accepted_band_unchanged(self, band, placeholder, monkeypatch):
        from cobalt.daymode import cli as daymode_cli

        monkeypatch.setattr(daymode_cli, "load_tunables", lambda: _fake_tunables(*band))
        assert daymode_cli._band() == band

    def test_cobalt_validate_calls_the_same_validator(self):
        """`cobalt validate` is not run here (it is not in this offline
        run's allowlist and whether it needs a database is NOT VERIFIED —
        `facts.md` "Cross-branch facts"). Its branch is proven by the unit
        tests above plus this wiring check: the command calls the ONE
        validator and carries no second copy of the rule (L3)."""
        import inspect

        from cobalt import cli as cobalt_cli

        source = inspect.getsource(cobalt_cli._cmd_validate)
        assert "validate_band" in source
        # no second copy of the rule inside the command
        assert "min must be <= max" not in source
