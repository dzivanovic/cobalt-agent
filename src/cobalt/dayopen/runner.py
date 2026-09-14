"""`run()` — the ordered C1-C6 sweep, assembled into one `DayOpenReport`.

The one place that knows the six checks run in this order and that a
`dayopen.config.DayOpenConfig` feeds C4 and C6 their ruled numbers. CLI,
tests and any future scheduler all call this, never the individual
`checks.py` functions directly, so there is exactly one definition of
"a day-open run" (L3).
"""

from __future__ import annotations

from datetime import date as Date
from datetime import datetime

from cobalt.session.clock import SessionClock, now_utc, session_clock

from . import checks
from .config import load_dayopen_config
from .models import DayOpenReport, overall_verdict


def run(*, report_date: Date | None = None, now: datetime | None = None) -> DayOpenReport:
    now = now or now_utc()
    clock = session_clock()
    report_date = report_date or SessionClock.to_et(now).date()
    cfg = load_dayopen_config()

    results = [
        checks.check_c1_radar_launchd(),
        checks.check_c2_radar_membership(report_date, now=now, clock=clock),
        checks.check_c3_radar_beat_line(report_date=report_date, now=now, clock=clock),
        checks.check_c4_session_blocks(expected=cfg.c4_expected_session_blocks),
        checks.check_c5_archiver_last_run(report_date=report_date, calendar=clock.calendar),
        checks.check_c6_beats_since_prior_evening(
            report_date=report_date, now=now, max_gap_min=cfg.c6_max_gap_min
        ),
    ]

    return DayOpenReport(
        report_date=report_date,
        generated_at=now,
        checks=results,
        overall=overall_verdict(results),
    )


__all__ = ["run"]
