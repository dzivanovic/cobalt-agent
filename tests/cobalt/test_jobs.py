"""F17 task integrity — Charter §3 F17, L18, SPRINT-LADDER §S1.

The acceptance test is one sentence: "a hung poller is surfaced as a
zombie within one heartbeat interval." Everything here serves it, plus
the kill phrase.

What is proven, in order:

1. the registry matches the plists that actually exist in ops/ — a
   registry that has drifted from launchd reports green for a job that
   is no longer there;
2. the wrapper marks running/done/failed with the exit code, and stamps
   a heartbeat;
3. ZOMBIE needs BOTH halves: past its timeout AND a stale heartbeat. The
   archiver runs 23 minutes on a normal night, so "started and did not
   finish" cannot be the test;
4. MISSED, for both schedule shapes — and the interval shape separately,
   because it is where the first draft of this code was wrong;
5. the kill phrase, both directions.
"""

import os
from datetime import datetime, timedelta, timezone

import pytest

from cobalt.jobs import killswitch
from cobalt.jobs.config import (
    CONFIG_PATH,
    OPS_DIR,
    JobRegistry,
    JobSpec,
    Schedule,
    load_job_registry,
)
from cobalt.jobs.models import JobKind, JobState, Supervisor
from cobalt.jobs.store import JobStore, JobStoreError
from cobalt.jobs.watchdog import is_missed, last_due, sweep
from cobalt.jobs.wrapper import JobStopped, job_run
from cobalt.session.clock import ET

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


def _spec(**over) -> JobSpec:
    base = dict(
        label="com.cobalt.test",
        kind=JobKind.ONE_SHOT,
        supervisor=Supervisor.SELF,
        timeout_s=300,
        what="a test job",
        schedule=Schedule(at="05:15", weekdays=[1, 2, 3, 4, 5]),
    )
    base.update(over)
    return JobSpec(**base)


# =====================================================================
# 1. The registry and the plists agree
# =====================================================================


class TestTheShippedRegistry:
    def test_every_registered_job_has_a_plist_in_ops(self):
        for spec in load_job_registry().jobs:
            assert spec.plist_path.exists(), (
                f"{spec.label} is registered in {CONFIG_PATH.name} but has no "
                f"{spec.plist_path.name} in ops/ — F18 would report a job that "
                "launchd has never heard of"
            )

    def test_every_plist_in_ops_is_registered(self):
        labels = set(load_job_registry().by_label)
        for plist in sorted(OPS_DIR.glob("com.cobalt.*.plist")):
            label = plist.stem
            assert label in labels, (
                f"{label} is installed in ops/ but not registered in "
                f"{CONFIG_PATH.name} — an unwatched job is exactly what F17 exists "
                "to make impossible"
            )

    def test_the_scheduled_times_match_the_plists(self):
        """launchd cannot read the registry and the registry cannot read
        launchd. This is the only thing standing between them."""
        import plistlib

        for spec in load_job_registry().jobs:
            if spec.schedule is None or spec.schedule.at is None:
                continue
            data = plistlib.loads(spec.plist_path.read_bytes())
            intervals = data.get("StartCalendarInterval")
            assert intervals, f"{spec.label}: registry has a time, plist has no schedule"
            hh, _, mm = spec.schedule.at.partition(":")
            for entry in intervals:
                assert entry["Hour"] == int(hh) and entry["Minute"] == int(mm), (
                    f"{spec.label}: registry says {spec.schedule.at}, plist says "
                    f"{entry['Hour']:02d}:{entry['Minute']:02d}"
                )
            assert sorted(e["Weekday"] for e in intervals) == sorted(spec.schedule.weekdays)

    def test_every_plist_carries_cobalt_env(self):
        """Charter §8.4. A job that loses it fails loud at boot rather
        than writing live trading data into the dev database."""
        import plistlib

        for spec in load_job_registry().jobs:
            data = plistlib.loads(spec.plist_path.read_bytes())
            env_vars = data.get("EnvironmentVariables", {})
            assert env_vars.get("COBALT_ENV") == "production", (
                f"{spec.label}: plist does not declare COBALT_ENV=production"
            )

    def test_the_agent_is_registered_as_a_pidfile_resident(self):
        """com.cobalt.agent's plist runs `cobalt.sh start`, which spawns
        the old-tree agent detached and EXITS 0 — so launchd holds no PID
        for it and `launchctl list` shows `- 0` whether it is alive or
        dead. The PID file is the only truthful liveness signal."""
        spec = load_job_registry().spec("com.cobalt.agent")
        assert spec.kind is JobKind.RESIDENT
        assert spec.supervisor is Supervisor.PIDFILE
        assert spec.pidfile_path is not None and spec.pidfile_path.name == "cobalt.pid"


class TestRegistryValidation:
    def test_a_one_shot_without_a_schedule_is_refused(self):
        with pytest.raises(Exception, match="needs a `schedule`"):
            _spec(schedule=None)

    def test_a_pidfile_supervisor_without_a_pidfile_is_refused(self):
        with pytest.raises(Exception, match="needs a `pidfile`"):
            _spec(kind=JobKind.RESIDENT, supervisor=Supervisor.PIDFILE, schedule=None)

    def test_a_schedule_must_pick_exactly_one_shape(self):
        with pytest.raises(Exception, match="exactly one of"):
            Schedule(at="05:15", weekdays=[1], every_min=15)
        with pytest.raises(Exception, match="exactly one of"):
            Schedule()

    def test_duplicate_labels_are_refused(self):
        with pytest.raises(Exception, match="duplicate job label"):
            JobRegistry(
                jobs=[_spec(), _spec()], kill_phrase="STOP", resume_phrase="GO"
            )


# =====================================================================
# 2/3. The wrapper and the zombie rule
# =====================================================================


@requires_db
@pytest.mark.integration
class TestTheWrapper:
    @pytest.fixture
    def store(self):
        store = JobStore()
        store.ensure_schema()
        store.register(_spec())
        return store

    def test_a_successful_run_lands_on_done_with_exit_zero(self, store, monkeypatch):
        monkeypatch.setattr(
            "cobalt.jobs.wrapper.load_job_registry",
            lambda: JobRegistry(jobs=[_spec()], kill_phrase="STOP", resume_phrase="GO"),
        )
        with job_run("com.cobalt.test", store=store) as run:
            run.result = {"rows_written": 7}

        row = store.get("com.cobalt.test")
        assert row["state"] == JobState.DONE.value
        assert row["exit_code"] == 0
        assert row["last_error"] is None
        assert row["started_at"] is not None and row["finished_at"] is not None
        assert row["last_result"] == {"rows_written": 7}

    def test_a_raising_run_lands_on_failed_and_re_raises(self, store, monkeypatch):
        monkeypatch.setattr(
            "cobalt.jobs.wrapper.load_job_registry",
            lambda: JobRegistry(jobs=[_spec()], kill_phrase="STOP", resume_phrase="GO"),
        )
        with pytest.raises(ValueError, match="boom"):
            with job_run("com.cobalt.test", store=store):
                raise ValueError("boom")

        row = store.get("com.cobalt.test")
        assert row["state"] == JobState.FAILED.value
        assert row["exit_code"] == 1
        assert "boom" in row["last_error"], "failed is LOUD — the reason goes in the row"

    def test_the_error_text_is_redacted_on_its_way_into_the_row(self, store, monkeypatch):
        """F19 at the point of STORAGE: F18 puts `last_error` in a DM, so
        a traceback carrying a DSN must never become a row that leaks."""
        monkeypatch.setattr(
            "cobalt.jobs.wrapper.load_job_registry",
            lambda: JobRegistry(jobs=[_spec()], kill_phrase="STOP", resume_phrase="GO"),
        )
        with pytest.raises(RuntimeError):
            with job_run("com.cobalt.test", store=store):
                raise RuntimeError("postgresql://cobalt:sup3rs3cr3tpw@h:5432/db is down")

        row = store.get("com.cobalt.test")
        assert "sup3rs3cr3tpw" not in row["last_error"]
        assert "[REDACTED:connection_string_password]" in row["last_error"]

    def test_running_a_job_with_no_row_is_refused_by_name(self, store):
        with pytest.raises(JobStoreError, match="register it first"):
            store.mark_running("com.cobalt.never-registered")

    def test_re_registering_does_not_erase_the_last_run(self, store):
        """A config edit must not wipe the exit code an operator is
        about to read."""
        store.mark_finished("com.cobalt.test", exit_code=1, error="yesterday's failure")
        store.register(_spec(timeout_s=999))
        row = store.get("com.cobalt.test")
        assert row["timeout_s"] == 999
        assert row["exit_code"] == 1 and "yesterday's failure" in row["last_error"]


@requires_db
@pytest.mark.integration
class TestTheZombieRule:
    @pytest.fixture
    def registry(self):
        return JobRegistry(
            jobs=[_spec(timeout_s=600)], kill_phrase="STOP", resume_phrase="GO"
        )

    @pytest.fixture
    def store(self, registry):
        store = JobStore()
        store.ensure_schema()
        store.register(registry.jobs[0])
        return store

    def _running_since(self, store, *, started_min: int, beat_min: int, now):
        store.mark_running("com.cobalt.test", now=now - timedelta(minutes=started_min))
        store.beat("com.cobalt.test", now=now - timedelta(minutes=beat_min))

    def test_a_long_job_with_a_fresh_heartbeat_is_not_a_zombie(self, store, registry):
        """The archiver runs 23 minutes on a normal night. 'Started and
        did not finish' is true of a healthy long job and useless as a
        test — which is exactly why `heartbeat_at` exists."""
        now = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
        self._running_since(store, started_min=30, beat_min=1, now=now)

        findings = {f.label: f for f in sweep(store=store, registry=registry, now=now, probe=False)}
        assert findings["com.cobalt.test"].ok
        assert store.get("com.cobalt.test")["state"] == JobState.RUNNING.value

    def test_past_the_timeout_with_a_stale_heartbeat_is_a_zombie(self, store, registry):
        now = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
        self._running_since(store, started_min=30, beat_min=20, now=now)

        finding = {f.label: f for f in sweep(store=store, registry=registry, now=now, probe=False)}[
            "com.cobalt.test"
        ]
        assert not finding.ok
        assert finding.state == JobState.ZOMBIE.value
        assert store.get("com.cobalt.test")["state"] == JobState.ZOMBIE.value

    def test_a_stale_heartbeat_inside_the_timeout_is_not_yet_a_zombie(self, store, registry):
        now = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
        self._running_since(store, started_min=5, beat_min=4, now=now)

        finding = {f.label: f for f in sweep(store=store, registry=registry, now=now, probe=False)}[
            "com.cobalt.test"
        ]
        assert finding.ok, "both halves are required, not either"

    def test_a_hung_job_is_surfaced_within_one_heartbeat_interval(self, store, registry):
        """Charter §3 F17's acceptance sentence, measured.

        `heartbeat.interval_min` is 15. A job that hangs is caught by the
        FIRST sweep more than its timeout past the hang — with a 10-minute
        test timeout, that is inside one interval.
        """
        from cobalt.taxonomy.loader import load_tunables

        interval = int(load_tunables().by_key["heartbeat.interval_min"].value)
        hung_at = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
        self._running_since(store, started_min=0, beat_min=0, now=hung_at)

        caught = None
        for minutes in range(1, 120):
            probe_at = hung_at + timedelta(minutes=minutes)
            f = {x.label: x for x in sweep(store=store, registry=registry, now=probe_at, probe=False)}[
                "com.cobalt.test"
            ]
            if f.state == JobState.ZOMBIE.value:
                caught = minutes
                break
        assert caught is not None, "a hung job was never surfaced"
        assert caught <= registry.jobs[0].timeout_s / 60 + interval, (
            f"surfaced after {caught} min — later than one heartbeat interval "
            f"({interval} min) past its timeout"
        )


# =====================================================================
# 4. MISSED — a fact about an absent run, not a state
# =====================================================================


class TestMissed:
    NOW = datetime(2026, 9, 4, 12, 0, tzinfo=ET)     # a Friday, midday ET

    def test_last_due_walks_back_to_the_most_recent_weekday_occurrence(self):
        spec = _spec(schedule=Schedule(at="05:15", weekdays=[1, 2, 3, 4, 5]))
        assert last_due(spec, self.NOW) == datetime(2026, 9, 4, 5, 15, tzinfo=ET)

    def test_before_todays_time_it_walks_back_to_yesterday(self):
        spec = _spec(schedule=Schedule(at="20:30", weekdays=[1, 2, 3, 4, 5]))
        assert last_due(spec, self.NOW) == datetime(2026, 9, 3, 20, 30, tzinfo=ET)

    def test_over_a_weekend_it_walks_back_to_friday(self):
        spec = _spec(schedule=Schedule(at="05:15", weekdays=[1, 2, 3, 4, 5]))
        sunday = datetime(2026, 9, 6, 12, 0, tzinfo=ET)
        assert last_due(spec, sunday) == datetime(2026, 9, 4, 5, 15, tzinfo=ET)

    def test_an_interval_job_has_no_calendar_moment(self):
        assert last_due(_spec(schedule=Schedule(every_min=15)), self.NOW) is None

    def _row(self, finished=None, registered=None):
        return {
            "finished_at": finished,
            "registered_at": registered or (self.NOW - timedelta(days=30)),
        }

    def test_a_calendar_job_that_never_ran_is_missed(self):
        spec = _spec(schedule=Schedule(at="05:15", weekdays=[1, 2, 3, 4, 5]))
        missed, detail = is_missed(
            spec, self._row(), now_et=self.NOW, grace=timedelta(minutes=30)
        )
        assert missed and "NEVER" in detail

    def test_a_run_after_the_due_time_clears_it(self):
        spec = _spec(schedule=Schedule(at="05:15", weekdays=[1, 2, 3, 4, 5]))
        missed, _ = is_missed(
            spec,
            self._row(finished=datetime(2026, 9, 4, 5, 16, tzinfo=ET)),
            now_et=self.NOW,
            grace=timedelta(minutes=30),
        )
        assert not missed

    def test_a_run_from_before_the_due_time_does_not(self):
        spec = _spec(schedule=Schedule(at="05:15", weekdays=[1, 2, 3, 4, 5]))
        missed, _ = is_missed(
            spec,
            self._row(finished=datetime(2026, 9, 3, 5, 16, tzinfo=ET)),
            now_et=self.NOW,
            grace=timedelta(minutes=30),
        )
        assert missed, "yesterday's success does not satisfy today's schedule"

    def test_inside_the_grace_it_is_not_yet_missed(self):
        spec = _spec(schedule=Schedule(at="11:45", weekdays=[1, 2, 3, 4, 5]))
        missed, _ = is_missed(
            spec, self._row(), now_et=self.NOW, grace=timedelta(minutes=30)
        )
        assert not missed, "15 minutes late, 30 minutes of grace"

    def test_an_interval_job_is_missed_against_its_own_cadence(self):
        """THE BUG THIS TEST EXISTS FOR. `last_due` for an interval job is
        always exactly one interval ago, so a fixed 30-minute grace made a
        15-minute heartbeat UNMISSABLE — it reported green forever,
        including while stopped. Interval jobs are measured against two of
        their own intervals instead."""
        spec = _spec(schedule=Schedule(every_min=15))
        grace = timedelta(minutes=30)

        fresh, _ = is_missed(
            spec,
            self._row(finished=self.NOW - timedelta(minutes=20)),
            now_et=self.NOW, grace=grace,
        )
        assert not fresh, "20 minutes on a 15-minute cadence is one late beat, not gone"

        stale, detail = is_missed(
            spec,
            self._row(finished=self.NOW - timedelta(minutes=40)),
            now_et=self.NOW, grace=grace,
        )
        assert stale, "40 minutes on a 15-minute cadence is missed"
        assert "two intervals" in detail

    def test_a_freshly_registered_interval_job_is_not_instantly_missed(self):
        spec = _spec(schedule=Schedule(every_min=15))
        missed, _ = is_missed(
            spec,
            self._row(registered=self.NOW - timedelta(minutes=5)),
            now_et=self.NOW, grace=timedelta(minutes=30),
        )
        assert not missed


# =====================================================================
# 5. The kill phrase
# =====================================================================


class TestKillPhraseMatching:
    def test_the_phrase_comes_from_config_and_tolerates_whitespace_and_case(self):
        phrase = load_job_registry().kill_phrase
        assert killswitch.matches_kill_phrase(phrase)
        assert killswitch.matches_kill_phrase(f"  {phrase.lower()}  ")
        assert not killswitch.matches_kill_phrase(f"{phrase} please")

    def test_resume_is_a_different_phrase(self):
        registry = load_job_registry()
        assert not killswitch.matches_kill_phrase(registry.resume_phrase)
        assert killswitch.matches_resume_phrase(registry.resume_phrase)


@requires_db
@pytest.mark.integration
class TestKillSwitch:
    @pytest.fixture
    def store(self):
        store = JobStore()
        store.ensure_schema()
        store.register(_spec())
        return store

    @pytest.fixture(autouse=True)
    def one_job_registry(self, monkeypatch):
        registry = JobRegistry(
            jobs=[_spec()], kill_phrase="COBALT STOP", resume_phrase="COBALT RESUME"
        )
        monkeypatch.setattr("cobalt.jobs.wrapper.load_job_registry", lambda: registry)
        monkeypatch.setattr("cobalt.jobs.killswitch.load_job_registry", lambda: registry)

    def test_stop_then_resume_round_trips(self, store):
        assert not killswitch.is_active(store)

        killswitch.engage(by="test", store=store)
        assert killswitch.is_active(store)
        state = killswitch.read(store)
        assert state.phrase == "COBALT STOP" and state.set_by == "test"

        killswitch.clear(by="test", store=store)
        assert not killswitch.is_active(store)

    def test_a_one_shot_refuses_to_start_while_stopped(self, store):
        killswitch.engage(by="test", store=store)
        try:
            with pytest.raises(JobStopped):
                with job_run("com.cobalt.test", store=store):
                    pytest.fail("the body must never run")
            # And it left NO trace: refusing is not the same as failing.
            assert store.get("com.cobalt.test")["state"] == JobState.PENDING.value
        finally:
            killswitch.clear(by="test", store=store)

    def test_it_runs_again_after_resume(self, store):
        killswitch.engage(by="test", store=store)
        killswitch.clear(by="test", store=store)
        with job_run("com.cobalt.test", store=store):
            pass
        assert store.get("com.cobalt.test")["state"] == JobState.DONE.value

    def test_a_resident_is_told_to_exit_cleanly(self, store):
        from cobalt.jobs.wrapper import should_keep_running

        assert should_keep_running("com.cobalt.test", store=store)
        killswitch.engage(by="test", store=store)
        try:
            assert not should_keep_running("com.cobalt.test", store=store)
        finally:
            killswitch.clear(by="test", store=store)

    def test_an_unreadable_switch_fails_OPEN_and_says_so(self, monkeypatch):
        """A database blip must not silently stop every job on the host —
        that failure would look exactly like the kill switch working."""
        class _Broken:
            def kill_switch(self):
                raise RuntimeError("database is down")

        assert killswitch.is_active(_Broken()) is False


class TestMissedStartsWhenWatchingStarts:
    NOW = datetime(2026, 9, 4, 12, 0, tzinfo=ET)

    def test_a_due_moment_before_registration_is_not_missed(self):
        """Cobalt cannot miss a run it was not watching for.

        The `jobs` table did not exist before S1-P3. Reporting this
        morning's 05:15 run as MISSED because the row was created at
        22:00 tonight would make the FIRST heartbeat after this feature
        ships red for five jobs that are all fine — and an alert that is
        wrong on day one is an alert people learn to scroll past.
        """
        spec = _spec(schedule=Schedule(at="05:15", weekdays=[1, 2, 3, 4, 5]))
        row = {"finished_at": None, "registered_at": self.NOW - timedelta(hours=1)}
        missed, _ = is_missed(spec, row, now_et=self.NOW, grace=timedelta(minutes=30))
        assert not missed

    def test_the_next_due_moment_after_registration_does_count(self):
        spec = _spec(schedule=Schedule(at="05:15", weekdays=[1, 2, 3, 4, 5]))
        row = {"finished_at": None, "registered_at": self.NOW - timedelta(days=3)}
        missed, detail = is_missed(spec, row, now_et=self.NOW, grace=timedelta(minutes=30))
        assert missed and "NEVER" in detail
