"""Chunk R — `cobalt.archiver.reconcile`, the pure core of the append night.

Spec `ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §3 (V2-3), §4, §6, §7.

EVERYTHING HERE IS OFFLINE AND PURE. `reconcile.py` performs no I/O,
reads no clock (the instant is an argument) and touches no database, so
the whole of the design's decision-making can be tested exactly — which
is the point of the structure the build prompt requires.

The dated sequences below are the four the houses wrote in round 2 and
the tribunal carried into the final design's §15. They are kept on the
houses' own dates and the houses' own public tickers (L32: no name from
the trader's lists in a committed fixture; constructed names use
`TESTARCH`/`THIN`).
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from zoneinfo import ZoneInfo

import pytest

from cobalt.archiver.models import Bar, Interval
from cobalt.archiver.reconcile import (
    INTERVAL_MINUTES,
    IncidentKind,
    ReconcileError,
    TargetCounts,
    TargetStatus,
    bar_closes_at,
    bar_values,
    compare,
    et_date,
    interval_duration,
    is_complete,
    normalise_price,
    normalise_volume,
    plan_candidates,
    reconcile,
    split_export,
    steady_state_dates,
)

ET = ZoneInfo("America/New_York")


# --- fixtures in the vendor's real shape -----------------------------


def et(y, m, d, hh, mm) -> datetime:
    """An ET wall clock, as the vendor's CSV writes it, as a UTC instant."""
    return datetime(y, m, d, hh, mm, tzinfo=ET).astimezone(timezone.utc)


def bar(ts, interval=Interval.I5, ticker="TESTARCH", close="100.00", volume=1234, open_="99.00",
        high="101.00", low="98.50") -> Bar:
    return Bar(
        ticker=ticker,
        interval=interval,
        ts=ts,
        open=Decimal(open_),
        high=Decimal(high),
        low=Decimal(low),
        close=Decimal(close),
        volume=volume,
    )


def stored_from(bars) -> dict:
    """The shape the store hands `reconcile`: {ts: BarValues}."""
    return {b.ts: bar_values(b) for b in bars}


def plan_for(bars, *, fetch_started_at, archived_through=None, ticker="TESTARCH",
             interval=Interval.I5):
    return plan_candidates(
        ticker=ticker,
        interval=interval,
        bars=bars,
        fetch_started_at=fetch_started_at,
        archived_through=archived_through,
    )


# =====================================================================
# V2-3 — completeness and the interval map
# =====================================================================


def test_the_interval_map_is_explicit_and_covers_every_enum_member():
    assert {i.value: INTERVAL_MINUTES[i] for i in Interval} == {
        "i1": 1, "i2": 2, "i5": 5, "i15": 15, "i30": 30
    }
    for interval in Interval:
        assert interval_duration(interval) == timedelta(minutes=INTERVAL_MINUTES[interval])


@pytest.mark.parametrize("unknown", ["i60", "d", "", None, 5, "I5"])
def test_an_unknown_interval_fails_loud(unknown):
    with pytest.raises(ReconcileError) as e:
        interval_duration(unknown)
    assert "interval" in str(e.value).lower()


def test_a_bar_closes_one_duration_after_it_opens():
    ts = et(2026, 9, 18, 12, 30)
    assert bar_closes_at(ts, Interval.I30) == ts + timedelta(minutes=30)
    assert bar_closes_at(ts, Interval.I1) == ts + timedelta(minutes=1)


def test_completeness_is_close_at_or_before_the_fetch_instant():
    ts = et(2026, 9, 18, 19, 59)
    close = ts + timedelta(minutes=1)
    assert is_complete(ts, Interval.I1, close) is True          # exactly at close
    assert is_complete(ts, Interval.I1, close - timedelta(seconds=1)) is False
    assert is_complete(ts, Interval.I1, close + timedelta(hours=1)) is True


def test_a_naive_fetch_instant_is_refused():
    with pytest.raises(ReconcileError):
        is_complete(et(2026, 9, 18, 19, 59), Interval.I1, datetime(2026, 9, 18, 20, 0))


def test_a_future_dated_row_is_incomplete_not_a_poison():
    """§7: an invalid future-dated row is excluded by V2-3, so it can
    neither set `export_newest` nor trigger a false regression."""
    fetch = et(2026, 9, 18, 20, 30)
    bars = [bar(et(2026, 9, 18, 19, 55)), bar(et(2026, 9, 19, 14, 0))]
    split = split_export(bars, Interval.I5, fetch)
    assert split.incomplete == 1
    assert [b.ts for b in split.eligible] == [et(2026, 9, 18, 19, 55)]
    assert split.export_newest == et(2026, 9, 18, 19, 55)
    assert split.raw_newest == et(2026, 9, 19, 14, 0)


# =====================================================================
# TIME — the spec's §15 list, ET dates AND UTC boundaries
# =====================================================================


def test_regular_close_the_1959_i1_bar_completes_at_2000_et():
    ts = et(2026, 9, 18, 19, 59)              # Friday aftermarket
    assert ts == datetime(2026, 9, 18, 23, 59, tzinfo=timezone.utc)
    assert bar_closes_at(ts, Interval.I1) == datetime(2026, 9, 19, 0, 0, tzinfo=timezone.utc)
    assert is_complete(ts, Interval.I1, et(2026, 9, 18, 20, 0))
    assert et_date(ts) == date(2026, 9, 18)


def test_half_day_the_i30_bar_opening_1230_completes_at_1300_et():
    """Spec §15, verbatim: 'a 13:00 half-day (an i30 bar opening 12:30
    completes at 13:00)'. The nightly run is still at 20:30, so it is
    complete by hours — the point is that the close is 13:00, not 13:30."""
    ts = et(2026, 11, 27, 12, 30)             # the Friday after Thanksgiving
    assert bar_closes_at(ts, Interval.I30) == et(2026, 11, 27, 13, 0)
    assert is_complete(ts, Interval.I30, et(2026, 11, 27, 13, 0))
    assert not is_complete(ts, Interval.I30, et(2026, 11, 27, 12, 59))


def test_extended_hours_bars_are_ordinary_bars_to_this_module():
    """i1/i5 carry premarket and aftermarket; nothing here filters by
    session (§3 V2-3: 'no open-session prohibition for the nightly run')."""
    fetch = et(2026, 9, 18, 20, 30)
    bars = [
        bar(et(2026, 9, 18, 4, 0), Interval.I1),      # premarket
        bar(et(2026, 9, 18, 10, 0), Interval.I1),     # RTH
        bar(et(2026, 9, 18, 19, 59), Interval.I1),    # aftermarket
    ]
    split = split_export(bars, Interval.I1, fetch)
    assert len(split.eligible) == 3
    assert split.export_oldest == et(2026, 9, 18, 4, 0)
    assert split.export_newest == et(2026, 9, 18, 19, 59)


def test_thanksgiving_thursday_has_no_bars_and_friday_is_a_half_day():
    """2026: Thanksgiving is Thu 11-26, Fri 11-27 closes 13:00 ET. The
    export simply carries no 11-26 date — no 24-hour arithmetic (§4)."""
    fetch = et(2026, 11, 27, 20, 30)
    bars = [
        bar(et(2026, 11, 25, 15, 55)),        # Wednesday
        bar(et(2026, 11, 27, 12, 55)),        # Friday, before the 13:00 close
    ]
    split = split_export(bars, Interval.I5, fetch)
    assert [et_date(b.ts) for b in split.eligible] == [date(2026, 11, 25), date(2026, 11, 27)]
    assert date(2026, 11, 26) not in {et_date(b.ts) for b in split.eligible}
    assert steady_state_dates(split.eligible, fetch) == (date(2026, 11, 25), date(2026, 11, 27))


def test_a_weekend_is_simply_two_dates_the_export_does_not_carry():
    fetch = et(2026, 9, 21, 20, 30)           # Monday night
    bars = [
        bar(et(2026, 9, 17, 19, 55)),         # Thursday
        bar(et(2026, 9, 18, 19, 55)),         # Friday
        bar(et(2026, 9, 21, 19, 55)),         # Monday
    ]
    dates = steady_state_dates(split_export(bars, Interval.I5, fetch).eligible, fetch)
    # Today (Monday) plus the two most recent COMPLETED sessions present.
    assert dates == (date(2026, 9, 17), date(2026, 9, 18), date(2026, 9, 21))


def test_the_0907_holiday_is_skipped_and_0908_is_the_next_session():
    """Labor Day 2026 is Mon 09-07; the export's dates run 09-04 -> 09-08."""
    fetch = et(2026, 9, 8, 20, 30)
    bars = [bar(et(2026, 9, 3, 19, 55)), bar(et(2026, 9, 4, 19, 55)), bar(et(2026, 9, 8, 19, 55))]
    dates = steady_state_dates(split_export(bars, Interval.I5, fetch).eligible, fetch)
    assert dates == (date(2026, 9, 3), date(2026, 9, 4), date(2026, 9, 8))
    assert date(2026, 9, 7) not in dates


def test_spring_forward_2026_03_08_keeps_et_dates_and_shifts_utc():
    before = et(2026, 3, 6, 9, 30)            # EST, UTC-5
    after = et(2026, 3, 9, 9, 30)             # EDT, UTC-4
    assert before == datetime(2026, 3, 6, 14, 30, tzinfo=timezone.utc)
    assert after == datetime(2026, 3, 9, 13, 30, tzinfo=timezone.utc)
    assert et_date(before) == date(2026, 3, 6) and et_date(after) == date(2026, 3, 9)
    # A bar that opens on the transition Sunday still closes one duration later.
    sunday = datetime(2026, 3, 8, 6, 55, tzinfo=timezone.utc)
    assert bar_closes_at(sunday, Interval.I5) == datetime(2026, 3, 8, 7, 0, tzinfo=timezone.utc)


def test_fall_back_2026_11_01_keeps_et_dates_and_shifts_utc():
    before = et(2026, 10, 30, 9, 30)          # EDT, UTC-4
    after = et(2026, 11, 2, 9, 30)            # EST, UTC-5
    assert before == datetime(2026, 10, 30, 13, 30, tzinfo=timezone.utc)
    assert after == datetime(2026, 11, 2, 14, 30, tzinfo=timezone.utc)
    assert et_date(before) == date(2026, 10, 30) and et_date(after) == date(2026, 11, 2)


def test_a_fetch_that_crosses_a_bar_close_excludes_that_bar():
    """`fetch_started_at` is captured BEFORE the request (§3 V2-3). A bar
    that closes while the response is in flight is NOT eligible tonight —
    tomorrow's run picks it up, which is what makes the rule replayable."""
    fetch = et(2026, 9, 18, 19, 59, )
    forming = et(2026, 9, 18, 19, 59)
    split = split_export([bar(forming, Interval.I1)], Interval.I1, fetch)
    assert split.eligible == ()
    assert split.incomplete == 1
    assert split.export_newest is None


# =====================================================================
# §4 — the candidate range
# =====================================================================


def test_bootstrap_takes_the_whole_eligible_export():
    fetch = et(2026, 9, 18, 20, 30)
    bars = [bar(et(2026, 9, d, 19, 55)) for d in (1, 2, 3, 4, 8, 9, 10, 17, 18)]
    plan = plan_for(bars, fetch_started_at=fetch, archived_through=None)
    assert plan.bootstrap is True
    assert len(plan.candidates) == len(bars)
    assert plan.below_range == 0


def test_steady_state_is_the_union_of_newer_than_progress_and_range_b():
    fetch = et(2026, 9, 18, 20, 30)
    bars = [bar(et(2026, 9, d, 19, 55)) for d in (3, 4, 8, 9, 10, 17, 18)]
    # Progress sits at 09-17's newest bar, so (a) is 09-18 alone; (b) adds
    # 09-18 (today) plus the two most recent completed sessions: 09-10, 09-17.
    plan = plan_for(bars, fetch_started_at=fetch, archived_through=et(2026, 9, 17, 19, 55))
    assert plan.bootstrap is False
    assert [et_date(b.ts) for b in plan.candidates] == [
        date(2026, 9, 10), date(2026, 9, 17), date(2026, 9, 18)
    ]
    assert plan.below_range == 4
    assert plan.range_dates == (date(2026, 9, 10), date(2026, 9, 17), date(2026, 9, 18))


def test_range_b_reaches_back_even_when_progress_is_ahead_of_it():
    """(a) can be empty and (b) still selects: an illiquid target whose
    progress already covers the newest bar is still RE-COMPARED over the
    last two sessions, which is what catches a vendor restatement."""
    fetch = et(2026, 9, 18, 20, 30)
    bars = [bar(et(2026, 9, d, 19, 55)) for d in (10, 17, 18)]
    plan = plan_for(bars, fetch_started_at=fetch, archived_through=et(2026, 9, 18, 19, 55))
    assert [b.ts for b in plan.candidates] == [b.ts for b in bars]
    assert plan.below_range == 0


def test_todays_date_is_in_range_b_even_with_no_completed_session_in_the_export():
    fetch = et(2026, 9, 18, 20, 30)
    bars = [bar(et(2026, 9, 18, 19, 55))]
    assert steady_state_dates(bars, fetch) == (date(2026, 9, 18),)


def test_duplicate_input_keys_are_counted_once_and_not_offered_twice():
    fetch = et(2026, 9, 18, 20, 30)
    ts = et(2026, 9, 18, 19, 55)
    split = split_export([bar(ts), bar(ts, close="101.00")], Interval.I5, fetch)
    assert split.fetched == 2
    assert split.duplicate_input_keys == 1
    assert len(split.eligible) == 1


# =====================================================================
# §7 — regression, gap, empty export
# =====================================================================


def test_a_strict_regression_fails_with_the_evidence_kept():
    fetch = et(2026, 9, 18, 20, 30)
    bars = [bar(et(2026, 9, 17, 19, 55))]
    plan = plan_for(bars, fetch_started_at=fetch, archived_through=et(2026, 9, 18, 19, 55))
    outcome = reconcile(plan, {})
    assert outcome.status is TargetStatus.FAILED
    assert [i.kind for i in outcome.incidents] == [IncidentKind.REGRESSION]
    incident = outcome.incidents[0]
    assert incident.detail["export_newest"] == et(2026, 9, 17, 19, 55).isoformat()
    assert incident.detail["archived_through"] == et(2026, 9, 18, 19, 55).isoformat()
    assert outcome.archived_through_after is None      # progress unchanged
    assert outcome.to_insert == ()


def test_an_equal_newest_bar_is_not_a_regression_illiquid_thin_three_sessions():
    """Grok's objection, answered by §7: 'an illiquid name whose last
    print does not move can fail that same clock check every night'. It
    does not — EQUAL is fine, and the target SUCCEEDS with zero inserts."""
    newest = et(2026, 9, 16, 15, 55)
    for day in (16, 17, 18):
        fetch = et(2026, 9, day, 20, 30)
        plan = plan_for(
            [bar(newest, ticker="THIN")], fetch_started_at=fetch, archived_through=newest,
            ticker="THIN",
        )
        outcome = reconcile(plan, stored_from([bar(newest, ticker="THIN")]))
        assert outcome.status is TargetStatus.SUCCESS, day
        assert outcome.incidents == ()
        assert outcome.to_insert == ()
        assert outcome.counts(inserted=0, concurrent_conflicts=0).inserted == 0


def test_a_half_day_is_not_truncation_and_not_a_regression():
    """Grok: '13:00/16:00 is "older" than last night's 19:59'. Compared as
    BAR TIMESTAMPS, Friday 12:55 is NEWER than Wednesday 19:59."""
    fetch = et(2026, 11, 27, 20, 30)
    bars = [bar(et(2026, 11, 25, 19, 55)), bar(et(2026, 11, 27, 12, 55))]
    plan = plan_for(bars, fetch_started_at=fetch, archived_through=et(2026, 11, 25, 19, 55))
    outcome = reconcile(plan, stored_from([bar(et(2026, 11, 25, 19, 55))]))
    assert outcome.status is TargetStatus.SUCCESS
    assert not any(i.kind is IncidentKind.REGRESSION for i in outcome.incidents)
    assert outcome.archived_through_after == et(2026, 11, 27, 12, 55)


def test_the_imcc_case_a_future_dated_row_then_a_valid_unchanged_export():
    """A failed night's observation is NEVER the baseline (§7). The
    future-dated row is excluded as incomplete, and the next valid export
    with an unchanged newest bar succeeds."""
    fetch1 = et(2026, 9, 17, 20, 30)
    poisoned = [bar(et(2026, 9, 17, 15, 55)), bar(et(2027, 1, 4, 10, 0))]
    plan1 = plan_for(poisoned, fetch_started_at=fetch1, archived_through=et(2026, 9, 17, 15, 55))
    out1 = reconcile(plan1, stored_from([bar(et(2026, 9, 17, 15, 55))]))
    assert out1.status is TargetStatus.SUCCESS
    assert out1.export_newest == et(2026, 9, 17, 15, 55)
    assert out1.raw_export_newest == et(2027, 1, 4, 10, 0)

    fetch2 = et(2026, 9, 18, 20, 30)
    plan2 = plan_for(
        [bar(et(2026, 9, 17, 15, 55))], fetch_started_at=fetch2,
        archived_through=et(2026, 9, 17, 15, 55),
    )
    out2 = reconcile(plan2, stored_from([bar(et(2026, 9, 17, 15, 55))]))
    assert out2.status is TargetStatus.SUCCESS


def test_a_gap_opens_when_the_export_starts_after_the_watermark():
    fetch = et(2026, 9, 18, 20, 30)
    bars = [bar(et(2026, 9, 17, 19, 55)), bar(et(2026, 9, 18, 19, 55))]
    plan = plan_for(bars, fetch_started_at=fetch, archived_through=et(2026, 9, 4, 19, 55))
    outcome = reconcile(plan, {})
    assert outcome.status is TargetStatus.DEGRADED
    gap = next(i for i in outcome.incidents if i.kind is IncidentKind.GAP)
    assert gap.range_start == et(2026, 9, 4, 19, 55)
    assert gap.range_end == et(2026, 9, 17, 19, 55)
    assert "unavailable from the tested export interface" in gap.detail["wording"]
    assert gap.detail["suspected_unavailable"] is True
    assert gap.detail["proven_missing"] is False
    # The usable range is still appended, and progress still advances.
    assert len(outcome.to_insert) == 2
    assert outcome.archived_through_after == et(2026, 9, 18, 19, 55)


def test_no_gap_on_a_bootstrap_the_report_says_unassessed_instead():
    fetch = et(2026, 9, 18, 20, 30)
    bars = [bar(et(2026, 9, 18, 19, 55))]
    outcome = reconcile(plan_for(bars, fetch_started_at=fetch, archived_through=None), {})
    assert not any(i.kind is IncidentKind.GAP for i in outcome.incidents)
    assert outcome.bootstrap is True
    assert outcome.unassessed_before == et(2026, 9, 18, 19, 55)


def test_an_export_with_rows_but_no_eligible_bar_is_an_empty_export_failure():
    fetch = et(2026, 9, 18, 19, 59)
    plan = plan_for([bar(et(2026, 9, 18, 19, 55))], fetch_started_at=fetch,
                    archived_through=et(2026, 9, 17, 19, 55))
    outcome = reconcile(plan, {})
    assert outcome.status is TargetStatus.FAILED
    assert [i.kind for i in outcome.incidents] == [IncidentKind.EMPTY_EXPORT]
    assert outcome.archived_through_after is None


def test_an_export_with_no_rows_at_all_is_an_empty_export_failure():
    outcome = reconcile(plan_for([], fetch_started_at=et(2026, 9, 18, 20, 30)), {})
    assert outcome.status is TargetStatus.FAILED
    assert [i.kind for i in outcome.incidents] == [IncidentKind.EMPTY_EXPORT]


def test_an_empty_export_does_not_establish_progress_so_the_next_night_bootstraps():
    empty = reconcile(plan_for([], fetch_started_at=et(2026, 9, 17, 20, 30)), {})
    assert empty.archived_through_after is None
    good = reconcile(
        plan_for([bar(et(2026, 9, 18, 19, 55))], fetch_started_at=et(2026, 9, 18, 20, 30)), {}
    )
    assert good.bootstrap is True


# =====================================================================
# §6 — the four-way comparison, normalisation and withholding
# =====================================================================


def test_normalisation_is_numeric_14_4_and_integer_volume():
    assert normalise_price("100.1") == Decimal("100.1000")
    assert normalise_price(Decimal("100.10000")) == Decimal("100.1000")
    assert normalise_price(Decimal("100.10004")) == Decimal("100.1000")
    assert normalise_volume(Decimal("1234")) == 1234
    assert normalise_volume(1234) == 1234


def test_equal_after_normalisation_is_not_a_difference():
    ts = et(2026, 9, 18, 19, 55)
    vendor = [bar(ts, close="100.00")]
    stored = {ts: bar_values(bar(ts, close="100.0000"))}
    result = compare(vendor, stored)
    assert result.equal == (ts,)
    assert result.differing == () and result.incoming_only == () and result.stored_only == ()


def test_a_field_level_difference_is_recorded_with_both_values():
    ts = et(2026, 9, 18, 19, 55)
    vendor = [bar(ts, close="105.00", volume=2000)]
    stored = {ts: bar_values(bar(ts, close="100.00", volume=1234))}
    result = compare(vendor, stored)
    (difference,) = result.differing
    assert difference.ts == ts
    assert {f.field for f in difference.fields} == {"close", "volume"}
    close = next(f for f in difference.fields if f.field == "close")
    assert close.stored == "100.0000" and close.vendor == "105.0000"


def test_stored_only_keys_are_flagged_and_nothing_is_deleted():
    fetch = et(2026, 9, 18, 20, 30)
    kept = et(2026, 9, 18, 19, 50)
    vendor = [bar(et(2026, 9, 18, 19, 55))]
    plan = plan_for(vendor, fetch_started_at=fetch, archived_through=et(2026, 9, 18, 19, 40))
    outcome = reconcile(plan, stored_from([bar(kept)]))
    assert outcome.stored_only_keys == (kept,)
    assert outcome.status is TargetStatus.DEGRADED
    assert any(i.kind is IncidentKind.STORED_ONLY for i in outcome.incidents)
    assert outcome.to_insert and all(b.ts != kept for b in outcome.to_insert)


def test_any_ohlcv_difference_withholds_the_whole_target():
    fetch = et(2026, 9, 18, 20, 30)
    old = et(2026, 9, 18, 19, 50)
    new = et(2026, 9, 18, 19, 55)
    plan = plan_for([bar(old, close="105.00"), bar(new)], fetch_started_at=fetch,
                    archived_through=old)
    outcome = reconcile(plan, stored_from([bar(old, close="100.00")]))
    assert outcome.status is TargetStatus.FAILED
    assert [i.kind for i in outcome.incidents] == [IncidentKind.RESTATED]
    assert outcome.to_insert == ()                 # NO insert for this target tonight
    assert outcome.archived_through_after is None  # progress unchanged
    assert outcome.withheld == 1                   # the one incoming-only key
    assert "no automatic repair" in outcome.reason or "restate" in outcome.reason


@pytest.mark.parametrize("field,kwargs", [
    ("open", {"open_": "99.50"}),
    ("high", {"high": "101.50"}),
    ("low", {"low": "98.00"}),
    ("close", {"close": "100.25"}),
    ("volume", {"volume": 9999}),
])
def test_a_difference_in_any_one_of_the_five_fields_withholds(field, kwargs):
    fetch = et(2026, 9, 18, 20, 30)
    ts = et(2026, 9, 18, 19, 50)
    plan = plan_for([bar(ts, **kwargs)], fetch_started_at=fetch, archived_through=ts)
    outcome = reconcile(plan, stored_from([bar(ts)]))
    assert outcome.status is TargetStatus.FAILED
    assert outcome.incidents[0].detail["differing"][0]["fields"][0]["field"] == field


def test_nothing_is_ever_repaired_automatically():
    """§6: 'Never an automatic repair, by constant factor or otherwise.'
    A whole-export constant-factor difference — the split-like case — is
    still a withholding, never a rescale."""
    fetch = et(2026, 9, 18, 20, 30)
    keys = [et(2026, 9, 18, 19, 40 + i) for i in range(0, 15, 5)]
    plan = plan_for([bar(k, close="50.00", open_="49.50", high="50.50", low="49.25") for k in keys],
                    fetch_started_at=fetch, archived_through=keys[-1])
    stored = stored_from([bar(k, close="100.00", open_="99.00", high="101.00", low="98.50")
                          for k in keys])
    outcome = reconcile(plan, stored)
    assert outcome.status is TargetStatus.FAILED
    assert outcome.to_insert == ()
    assert len(outcome.incidents[0].detail["differing"]) == 3


# =====================================================================
# The four ROUND-2 SEQUENCES, on the houses' own dates
# =====================================================================


def test_gemini_monday_1400_restoration_seen_on_tuesday():
    """Gemini, round 2: bars for Monday 14:00-14:05 are RESTORED by the
    vendor and first appear in Tuesday 09:30's data. The poller's
    `max(ts)` has long since moved past them, so a `max(ts)` watermark
    drops them forever. `archived_through` does not: Monday's accepted
    export set it to Monday's newest bar, and the restored keys lie
    inside range (b)."""
    fetch = et(2026, 9, 22, 20, 30)                   # Tuesday night
    restored = [et(2026, 9, 21, 14, 0), et(2026, 9, 21, 14, 5)]
    monday_newest = et(2026, 9, 21, 19, 55)
    export = [bar(t, Interval.I1) for t in restored] + [
        bar(monday_newest, Interval.I1), bar(et(2026, 9, 22, 19, 55), Interval.I1)
    ]
    plan = plan_for(export, fetch_started_at=fetch, archived_through=monday_newest,
                    interval=Interval.I1)
    # Both restored keys are candidates even though they are OLDER than
    # the watermark — that is range (b) doing its job.
    assert set(restored) <= {b.ts for b in plan.candidates}
    stored = stored_from([bar(monday_newest, Interval.I1)])
    outcome = reconcile(plan, stored)
    assert outcome.status is TargetStatus.SUCCESS
    assert {b.ts for b in outcome.to_insert} == set(restored) | {et(2026, 9, 22, 19, 55)}
    counts = outcome.counts(inserted=3, concurrent_conflicts=0)
    assert counts.late == 2 and counts.new == 1


def test_astra_friday_1002_late_addition_appears_after_a_weekend():
    """Astra, round 2: a bar for Friday 10:02 is added by the vendor and
    is first seen on Monday 09:36. The weekend is not 72 hours of
    arithmetic — Friday is simply one of the two most recent completed
    session DATES the export carries (§4)."""
    fetch = et(2026, 9, 21, 20, 30)                   # Monday night
    late_key = et(2026, 9, 18, 10, 2)
    friday_newest = et(2026, 9, 18, 19, 55)
    export = [
        bar(et(2026, 9, 17, 19, 55), Interval.I1),
        bar(late_key, Interval.I1),
        bar(friday_newest, Interval.I1),
        bar(et(2026, 9, 21, 19, 55), Interval.I1),
    ]
    plan = plan_for(export, fetch_started_at=fetch, archived_through=friday_newest,
                    interval=Interval.I1)
    assert late_key in {b.ts for b in plan.candidates}
    assert plan.range_dates == (date(2026, 9, 17), date(2026, 9, 18), date(2026, 9, 21))
    outcome = reconcile(plan, stored_from([
        bar(et(2026, 9, 17, 19, 55), Interval.I1), bar(friday_newest, Interval.I1)
    ]))
    assert {b.ts for b in outcome.to_insert} == {late_key, et(2026, 9, 21, 19, 55)}
    counts = outcome.counts(inserted=2, concurrent_conflicts=0)
    assert counts.late == 1 and counts.new == 1


def test_grok_nvda_wednesday_1017_appears_on_thursday():
    """Grok, round 2: NVDA's Wednesday 10:17 bar appears on Thursday.
    The poller's maximum never enters the decision — it is reported
    beside the counters and used by nothing (§7)."""
    fetch = et(2026, 9, 17, 20, 30)                   # Thursday night
    late_key = et(2026, 9, 16, 10, 17)
    wed_newest = et(2026, 9, 16, 19, 55)
    export = [bar(t, Interval.I1, ticker="NVDA") for t in (
        late_key, wed_newest, et(2026, 9, 17, 19, 55)
    )]
    plan = plan_for(export, fetch_started_at=fetch, archived_through=wed_newest,
                    ticker="NVDA", interval=Interval.I1)
    outcome = reconcile(
        plan, stored_from([bar(wed_newest, Interval.I1, ticker="NVDA")]),
        poller_watermark=et(2026, 9, 17, 19, 55),
    )
    assert late_key in {b.ts for b in outcome.to_insert}
    assert outcome.poller_watermark == et(2026, 9, 17, 19, 55)
    assert outcome.archived_through_after == et(2026, 9, 17, 19, 55)


def test_the_gap_a_poller_backfill_would_have_hidden_msft_0827_to_0904():
    """Astra, round 2 (MSFT 08-27 / 09-04) and Grok's AAPL re-added: a
    poller back-fill moves `max(ts)` forward across days the archiver
    never covered, so a `max(ts)` gap test reads clean. `archived_through`
    still sits at 08-27 and the gap opens."""
    fetch = et(2026, 9, 4, 20, 30)
    export = [bar(et(2026, 9, 3, 19, 55)), bar(et(2026, 9, 4, 19, 55))]
    plan = plan_for(export, fetch_started_at=fetch, archived_through=et(2026, 8, 27, 19, 55))
    outcome = reconcile(plan, {}, poller_watermark=et(2026, 9, 4, 19, 55))
    gap = next(i for i in outcome.incidents if i.kind is IncidentKind.GAP)
    assert gap.range_start == et(2026, 8, 27, 19, 55)
    assert gap.range_end == et(2026, 9, 3, 19, 55)
    assert outcome.status is TargetStatus.DEGRADED
    assert outcome.poller_watermark == et(2026, 9, 4, 19, 55)


def test_a_progress_row_survives_a_ticker_leaving_and_returning():
    """Round-2 sequence #8. AAPL leaves the Lists note for a fortnight and
    comes back; its progress row was never deleted, so the days it missed
    are a GAP rather than silence."""
    fetch = et(2026, 9, 18, 20, 30)
    export = [bar(et(2026, 9, 17, 19, 55), ticker="AAPL"), bar(et(2026, 9, 18, 19, 55), ticker="AAPL")]
    plan = plan_for(export, fetch_started_at=fetch, archived_through=et(2026, 9, 3, 19, 55),
                    ticker="AAPL")
    outcome = reconcile(plan, {})
    assert any(i.kind is IncidentKind.GAP for i in outcome.incidents)
    assert outcome.status is TargetStatus.DEGRADED


def test_the_poller_maximum_never_enters_any_decision():
    """Asserted directly: the same inputs with three different poller
    watermarks produce byte-identical decisions."""
    fetch = et(2026, 9, 18, 20, 30)
    export = [bar(et(2026, 9, 18, 19, 55))]
    outcomes = [
        reconcile(
            plan_for(export, fetch_started_at=fetch, archived_through=et(2026, 9, 17, 19, 55)),
            {},
            poller_watermark=w,
        )
        for w in (None, et(2026, 9, 1, 10, 0), et(2027, 1, 1, 10, 0))
    ]
    decisions = {
        (o.status, o.archived_through_after, tuple(b.ts for b in o.to_insert),
         tuple(i.kind for i in o.incidents))
        for o in outcomes
    }
    assert len(decisions) == 1


# =====================================================================
# §7 — the counting identities (L57)
# =====================================================================


def test_msft_1959_after_1958_is_new_not_late():
    fetch = et(2026, 9, 18, 20, 30)
    previous = et(2026, 9, 18, 19, 58)
    export = [bar(previous, Interval.I1, ticker="MSFT"), bar(et(2026, 9, 18, 19, 59), Interval.I1, ticker="MSFT")]
    plan = plan_for(export, fetch_started_at=fetch, archived_through=previous,
                    ticker="MSFT", interval=Interval.I1)
    outcome = reconcile(plan, stored_from([bar(previous, Interval.I1, ticker="MSFT")]))
    counts = outcome.counts(inserted=1, concurrent_conflicts=0)
    assert counts.incoming_only == 1 and counts.new == 1 and counts.late == 0


def test_msft_1959_already_stored_equal_is_one_one_zero():
    """§15, verbatim: 'MSFT 19:59 already stored equal = 1 / 1 / 0'
    — one candidate, one already-stored-equal, zero incoming-only."""
    fetch = et(2026, 9, 18, 20, 30)
    ts = et(2026, 9, 18, 19, 59)
    plan = plan_for([bar(ts, Interval.I1, ticker="MSFT")], fetch_started_at=fetch,
                    archived_through=ts, ticker="MSFT", interval=Interval.I1)
    outcome = reconcile(plan, stored_from([bar(ts, Interval.I1, ticker="MSFT")]))
    counts = outcome.counts(inserted=0, concurrent_conflicts=0)
    assert (counts.candidates, counts.already_stored_equal, counts.incoming_only) == (1, 1, 0)


def test_groks_hundred_key_case_reconciles():
    """Equal, differing and incoming-only candidates in one target. The
    difference withholds, so `withheld == incoming_only` and
    `inserted == 0` — and every identity still closes."""
    fetch = et(2026, 9, 18, 20, 30)
    keys = [et(2026, 9, 18, 9, 30) + timedelta(minutes=5 * i) for i in range(100)]
    export = [bar(k) for k in keys]
    export[7] = bar(keys[7], close="999.00")
    stored = stored_from([bar(k) for k in keys[:60]])
    plan = plan_for(export, fetch_started_at=fetch, archived_through=keys[59])
    outcome = reconcile(plan, stored)
    counts = outcome.counts(inserted=0, concurrent_conflicts=0)
    assert counts.candidates == 100
    assert counts.already_stored_equal == 59
    assert counts.differing == 1
    assert counts.incoming_only == 40
    assert counts.withheld == 40 and counts.inserted == 0 and counts.concurrent_conflicts == 0


def test_astras_aapl_i5_case_reconciles():
    fetch = et(2026, 9, 18, 20, 30)
    keys = [et(2026, 9, 18, 9, 30) + timedelta(minutes=5 * i) for i in range(12)]
    export = [bar(k, ticker="AAPL") for k in keys]
    stored = stored_from([bar(k, ticker="AAPL") for k in keys[:8]])
    plan = plan_for(export, fetch_started_at=fetch, archived_through=keys[7], ticker="AAPL")
    outcome = reconcile(plan, stored)
    counts = outcome.counts(inserted=4, concurrent_conflicts=0)
    assert counts.candidates == counts.already_stored_equal + counts.differing + counts.incoming_only
    assert counts.incoming_only == counts.inserted + counts.concurrent_conflicts
    assert counts.fetched == (
        counts.invalid + counts.duplicate_input_keys + counts.incomplete
        + counts.below_range + counts.candidates
    )


def test_a_counted_conflict_is_not_an_error():
    """A poller insert between the range read and this insert shows up as
    `concurrent_conflicts`, and the identity still closes."""
    fetch = et(2026, 9, 18, 20, 30)
    keys = [et(2026, 9, 18, 19, 50), et(2026, 9, 18, 19, 55)]
    plan = plan_for([bar(k) for k in keys], fetch_started_at=fetch, archived_through=keys[0])
    outcome = reconcile(plan, stored_from([bar(keys[0])]))
    counts = outcome.counts(inserted=0, concurrent_conflicts=1)
    assert counts.incoming_only == 1
    assert counts.inserted == 0 and counts.concurrent_conflicts == 1


@pytest.mark.parametrize("bad", [
    dict(inserted=5, concurrent_conflicts=0),     # more inserted than offered
    dict(inserted=0, concurrent_conflicts=5),
    dict(inserted=-1, concurrent_conflicts=0),
])
def test_a_non_reconciling_count_cannot_be_constructed(bad):
    fetch = et(2026, 9, 18, 20, 30)
    keys = [et(2026, 9, 18, 19, 50), et(2026, 9, 18, 19, 55)]
    plan = plan_for([bar(k) for k in keys], fetch_started_at=fetch, archived_through=keys[0])
    outcome = reconcile(plan, stored_from([bar(keys[0])]))
    with pytest.raises(Exception):
        outcome.counts(**bad)


def test_the_counts_model_refuses_a_broken_identity_directly():
    with pytest.raises(Exception) as e:
        TargetCounts(
            fetched=10, invalid=0, duplicate_input_keys=0, incomplete=0, below_range=0,
            candidates=9,                       # 10 != 0+0+0+0+9
            already_stored_equal=0, differing=0, incoming_only=9, new=9, late=0,
            withheld=0, inserted=9, concurrent_conflicts=0, stored_only=0,
        )
    assert "fetched" in str(e.value)


def test_a_withheld_target_has_zero_inserted_and_zero_conflicts():
    with pytest.raises(Exception):
        TargetCounts(
            fetched=1, invalid=0, duplicate_input_keys=0, incomplete=0, below_range=0,
            candidates=1, already_stored_equal=0, differing=0, incoming_only=1, new=1, late=0,
            withheld=1, inserted=1, concurrent_conflicts=0, stored_only=0,
        )


def test_late_is_zero_on_a_bootstrap():
    fetch = et(2026, 9, 18, 20, 30)
    keys = [et(2026, 9, 18, 19, 50), et(2026, 9, 18, 19, 55)]
    outcome = reconcile(plan_for([bar(k) for k in keys], fetch_started_at=fetch), {})
    counts = outcome.counts(inserted=2, concurrent_conflicts=0)
    assert counts.late == 0 and counts.new == 2


def test_invalid_is_zero_by_construction_but_the_counter_survives():
    """§7: the collector fails a whole target on one bad row, so `invalid`
    is 0 today. The counter stays so the identity survives a collector
    change."""
    outcome = reconcile(
        plan_for([bar(et(2026, 9, 18, 19, 55))], fetch_started_at=et(2026, 9, 18, 20, 30)), {}
    )
    assert outcome.counts(inserted=1, concurrent_conflicts=0).invalid == 0
    assert "invalid" in TargetCounts.model_fields


def test_stored_only_is_reported_beside_the_identities_not_inside_them():
    fetch = et(2026, 9, 18, 20, 30)
    vendor = [bar(et(2026, 9, 18, 19, 55))]
    plan = plan_for(vendor, fetch_started_at=fetch, archived_through=et(2026, 9, 18, 19, 40))
    outcome = reconcile(plan, stored_from([bar(et(2026, 9, 18, 19, 50))]))
    counts = outcome.counts(inserted=1, concurrent_conflicts=0)
    assert counts.stored_only == 1
    assert counts.candidates == counts.already_stored_equal + counts.differing + counts.incoming_only


# =====================================================================
# Purity
# =====================================================================


def test_the_module_reads_no_clock_no_database_and_no_file():
    """Purity asserted on the AST, not on prose: the module's docstring
    explains WHY `max(ts)` is the wrong watermark and names the store
    while doing it. What must stay absent is the import."""
    import ast
    import pathlib

    import cobalt.archiver.reconcile as module

    tree = ast.parse(pathlib.Path(module.__file__).read_text(encoding="utf-8"))
    imported: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.add((node.module or "").split(".")[0] or ".")
    assert imported <= {
        "__future__", "datetime", "decimal", "enum", "typing", "zoneinfo",
        "pydantic", "models",
    }, f"reconcile.py must stay pure; it imports {sorted(imported)}"
    # The one relative import is the Pydantic models, nothing else.
    relative = {
        node.module
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom) and node.level
    }
    assert relative == {"models"}

    called = {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    } | {
        node.func.id
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    }
    for forbidden in ("now", "utcnow", "today", "open", "read_text", "execute"):
        assert forbidden not in called, f"reconcile.py calls {forbidden}()"


def test_two_failed_nights_then_a_success_inserts_the_keys_still_in_the_window():
    """§15: 'two failed nights then success (keys still in the window
    insert)'. Progress never moved on the failures, so the third night's
    range (a) still reaches back to the old watermark."""
    watermark = et(2026, 9, 16, 19, 55)
    for day in (17, 18):
        out = reconcile(plan_for([], fetch_started_at=et(2026, 9, day, 20, 30),
                                 archived_through=watermark), {})
        assert out.status is TargetStatus.FAILED
        assert out.archived_through_after is None

    fetch = et(2026, 9, 21, 20, 30)
    export = [bar(et(2026, 9, d, 19, 55)) for d in (16, 17, 18, 21)]
    plan = plan_for(export, fetch_started_at=fetch, archived_through=watermark)
    # The store read is bounded by the candidate range, and 09-16 is below
    # it (not newer than the watermark, not one of the three range dates),
    # so the read returns nothing.
    assert watermark not in {b.ts for b in plan.candidates}
    outcome = reconcile(plan, {})
    assert {b.ts for b in outcome.to_insert} == {
        et(2026, 9, 17, 19, 55), et(2026, 9, 18, 19, 55), et(2026, 9, 21, 19, 55)
    }
    assert outcome.archived_through_after == et(2026, 9, 21, 19, 55)
