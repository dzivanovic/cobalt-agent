"""F18's archiver probe — Charter §3 F18 "archiver freshness".

THE INCIDENT THIS FILE EXISTS FOR (2026-09-06). The F17 wrapper was
registered at 22:19 ET Friday 2026-09-04, AFTER that evening's 20:30
run had already completed via the pre-wrapper code path — so the
`cobalt_jobs` row's `finished_at` stayed NULL with nothing actually
wrong. `archiver_freshness` used to grade that against a flat
`registered_at + heartbeat.archiver_max_age_min` (26h) window, which
expired just after midnight Saturday and painted the whole weekend red
for a job not due again until Monday evening.

The fix reuses `cobalt.jobs.watchdog.is_missed` — the same cadence-aware
"should this have run by now" arithmetic F17's watchdog already has
tested (`tests/cobalt/test_jobs.py::TestMissed`,
`TestMissedStartsWhenWatchingStarts`) — instead of a second, flatter
implementation of the same question.
"""

from datetime import datetime, timezone

from cobalt.heartbeat.probes import archiver_freshness, radar
from cobalt.session.models import Session

FRIDAY_RUN_FINISHED_ET = "2026-09-04 20:53"  # the actual pre-wrapper run
REGISTERED_AT = datetime(2026, 9, 5, 2, 19, 45, tzinfo=timezone.utc)  # Fri 22:19:45 ET
SUNDAY_MORNING = datetime(2026, 9, 6, 10, 54, tzinfo=timezone.utc)  # Sun 06:54 ET — the RED
SUNDAY_LATER = datetime(2026, 9, 6, 14, 0, tzinfo=timezone.utc)  # Sun 10:00 ET
MONDAY_PAST_GRACE = datetime(2026, 9, 8, 1, 15, tzinfo=timezone.utc)  # Mon 21:15 ET


class _FakeStore:
    def __init__(self, row):
        self._row = row

    def get(self, label):
        assert label == "com.cobalt.archiver"
        return self._row


class _RadarPool:
    def __init__(self, row):
        self.row = row

    def pool_row(self, key):
        assert key == "primary"
        return self.row


class _RadarSettings:
    def __init__(self, rows=None):
        self.rows = rows or {}

    def values(self):
        return self.rows


class _RadarClock:
    def __init__(self, session):
        self.value = session

    def session(self, _now):
        return self.value


def _radar_row(now, **changes):
    row = {"last_scan_at": now, "degraded": False, "degraded_sources": [],
        "failed_stage": None, "failed_detail": None, "poll_failures": [], "members": 1}
    row.update(changes)
    return row


def test_radar_disabled_and_no_row_branches():
    now = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
    assert radar(now, enabled=False).ok
    result = radar(now, enabled=True, pool_store=_RadarPool(None), settings_store=_RadarSettings())
    assert not result.ok and "no radar_pool" in result.detail


def test_radar_paused_idle_and_scanning_branches():
    now = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
    for session, word in ((Session.MARKET_RESET, "paused"), (Session.OVERNIGHT, "idle")):
        result = radar(now, enabled=True, pool_store=_RadarPool(_radar_row(now)),
            settings_store=_RadarSettings(), clock=_RadarClock(session))
        assert result.ok and word in result.detail
    result = radar(now, enabled=True, pool_store=_RadarPool(_radar_row(now)),
        settings_store=_RadarSettings(), clock=_RadarClock(Session.RTH))
    assert result.ok and "scanning" in result.detail


def test_radar_red_findings_name_stage_mirror_and_old_poll_failure():
    now = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
    old = datetime(2026, 9, 3, 13, 0, tzinfo=timezone.utc)
    row = _radar_row(now, failed_stage="bars", failed_detail="synthetic failure",
        poll_failures=[{"ticker": "AAA", "reason": "stale", "since": old.isoformat()}])
    result = radar(now, enabled=True, pool_store=_RadarPool(row),
        settings_store=_RadarSettings({"radar.screen.synthetic": {"status": "parse_failed", "error": "bad field"}}),
        clock=_RadarClock(Session.RTH))
    assert not result.ok
    assert "failed_stage bars" in result.detail
    assert "mirror radar.screen.synthetic" in result.detail
    assert "poll AAA stale" in result.detail


def _row(*, finished=None, registered=REGISTERED_AT, exit_code=None, last_result=None):
    return {
        "finished_at": finished,
        "registered_at": registered,
        "exit_code": exit_code,
        "last_result": last_result,
    }


class TestNoJobsRow:
    def test_an_unregistered_archiver_is_red(self):
        probe = archiver_freshness(store=_FakeStore(None), now=SUNDAY_MORNING)
        assert not probe.ok
        assert "not registered" in probe.detail


class TestTheWeekendIsNotRed:
    """The exact incident: registered Friday night, after Friday's run,
    with no wrapped run since — checked over the weekend."""

    def test_registered_after_fridays_run_is_not_red_on_sunday(self):
        probe = archiver_freshness(
            store=_FakeStore(_row(finished=None)), now=SUNDAY_MORNING
        )
        assert probe.ok, probe.detail
        assert "none due since registration" in probe.detail

    def test_still_not_red_later_the_same_sunday(self):
        probe = archiver_freshness(
            store=_FakeStore(_row(finished=None)), now=SUNDAY_LATER
        )
        assert probe.ok, probe.detail

    def test_a_completed_fridays_run_does_not_go_stale_over_the_weekend(self):
        """A flat 26h window would call this STALE by Saturday night —
        the archiver isn't due again until Monday 20:30 ET."""
        finished = datetime(2026, 9, 5, 0, 53, tzinfo=timezone.utc)  # Fri 20:53 ET
        probe = archiver_freshness(
            store=_FakeStore(
                _row(finished=finished, exit_code=0, last_result={"rows_written": 100})
            ),
            now=SUNDAY_LATER,
        )
        assert probe.ok, probe.detail


class TestAGenuineMissIsStillRed:
    def test_no_run_past_mondays_due_time_plus_grace_is_red(self):
        probe = archiver_freshness(
            store=_FakeStore(_row(finished=None)), now=MONDAY_PAST_GRACE
        )
        assert not probe.ok
        assert "NEVER" in probe.detail

    def test_fridays_run_does_not_satisfy_mondays_schedule(self):
        finished = datetime(2026, 9, 5, 0, 53, tzinfo=timezone.utc)  # Fri 20:53 ET
        probe = archiver_freshness(
            store=_FakeStore(
                _row(finished=finished, exit_code=0, last_result={"rows_written": 100})
            ),
            now=MONDAY_PAST_GRACE,
        )
        assert not probe.ok
        assert probe.detail.startswith("STALE —")


class TestOnceARunHasCompleted:
    RECENT = datetime(2026, 9, 5, 0, 53, tzinfo=timezone.utc)  # Fri 20:53 ET

    def test_a_healthy_run_is_green(self):
        probe = archiver_freshness(
            store=_FakeStore(
                _row(finished=self.RECENT, exit_code=0, last_result={"rows_written": 3164539})
            ),
            now=datetime(2026, 9, 5, 1, 0, tzinfo=timezone.utc),
        )
        assert probe.ok, probe.detail

    def test_a_nonzero_exit_is_red_even_when_not_stale(self):
        probe = archiver_freshness(
            store=_FakeStore(
                _row(finished=self.RECENT, exit_code=1, last_result={"rows_written": 0})
            ),
            now=datetime(2026, 9, 5, 1, 0, tzinfo=timezone.utc),
        )
        assert not probe.ok
        assert "FAILED" in probe.detail

    def test_exit_zero_with_zero_rows_is_red(self):
        """Looks green in every state column and is quietly not
        collecting the corpus — the failure mode `rows_written` exists
        to catch."""
        probe = archiver_freshness(
            store=_FakeStore(
                _row(finished=self.RECENT, exit_code=0, last_result={"rows_written": 0})
            ),
            now=datetime(2026, 9, 5, 1, 0, tzinfo=timezone.utc),
        )
        assert not probe.ok
        assert "wrote NOTHING" in probe.detail
