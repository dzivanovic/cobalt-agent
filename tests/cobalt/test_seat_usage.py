"""The seat-usage report — collector, renderer, write path, probe.

What is proven, in order:

1. the pinned tool's JSON becomes the unit text, including the two
   things the offline pricing gate forces: a used-but-unpriced model is
   NEVER printed as $0, and a genuinely free model is;
2. the same unit id updates in place — one table per day, however many
   times an hour it runs;
3. the human cells are seeded once and then never written again, and
   the guard for that reads the FILE, so it holds on a run that cannot
   reach Postgres;
4. newest day on top;
5. the freshness probe is green inside its window, red when the report
   goes stale, and silent outside the window.
"""

import json
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import pytest

from cobalt.jobs.config import JobConfigError, Schedule, parse_window
from cobalt.seatusage import ccusage, report
from cobalt.seatusage.config import (
    SeatUsageConfig,
    SeatUsageConfigError,
    ToolSpec,
    load_seat_usage_config,
)
from cobalt.vaultwrite import VaultWriter
from cobalt.vaultwrite.markers import find_section

DAY = date(2026, 9, 8)

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)


# ---------------------------------------------------------------------
# the fixture: one real `ccusage daily --json --breakdown --by-agent`
# day, trimmed. `claude-fable-5-1` and `gpt-6-astra` carry the exact
# shape the offline pricing table produced on 2026-09-08 — real tokens,
# cost 0.0 — because that is the case the guard exists for.
# ---------------------------------------------------------------------

FIXTURE = {
    "daily": [
        {
            "period": "2026-09-08",
            "metadata": {"agents": ["claude", "codex", "grok", "qwen"]},
            "agents": [
                {
                    "agent": "claude",
                    "modelBreakdowns": [
                        {"modelName": "claude-opus-5"},
                        {"modelName": "claude-fable-5-1"},
                    ],
                },
                {"agent": "codex", "modelBreakdowns": [{"modelName": "gpt-6-astra"}]},
                {"agent": "qwen", "modelBreakdowns": [{"modelName": "mainframe"}]},
            ],
            "modelBreakdowns": [
                {
                    "modelName": "claude-opus-5",
                    "cacheReadTokens": 219058828,
                    "cacheCreationTokens": 1987227,
                    "inputTokens": 1110,
                    "outputTokens": 446511,
                    "cost": 134.28128149999995,
                },
                {
                    "modelName": "claude-fable-5-1",
                    "cacheReadTokens": 17237638,
                    "cacheCreationTokens": 354319,
                    "inputTokens": 2026,
                    "outputTokens": 118151,
                    "cost": 0.0,
                },
                {
                    "modelName": "gpt-6-astra",
                    "cacheReadTokens": 11904,
                    "cacheCreationTokens": 0,
                    "inputTokens": 2707,
                    "outputTokens": 82,
                    "cost": 0.0,
                },
                {
                    "modelName": "mainframe",
                    "cacheReadTokens": 0,
                    "cacheCreationTokens": 0,
                    "inputTokens": 64272,
                    "outputTokens": 129,
                    "cost": 0.0,
                },
            ],
        }
    ]
}


@pytest.fixture
def cfg():
    return SeatUsageConfig(
        tool=ToolSpec(
            name="ccusage", version="20.0.20",
            binary="/nowhere/ccusage", license="MIT", offline=True,
        ),
        report_path="docs/40 - DevDocs/reports/seat-usage.md",
        unpriced_is_loud=True,
        zero_cost_models={"mainframe": "the local lane, genuinely free"},
        roles={"claude-opus-5": "write seat", "mainframe": "local lane"},
    )


@pytest.fixture
def usage(cfg):
    return ccusage.parse(cfg, FIXTURE, DAY, version="20.0.20")


NOW = datetime(2026, 9, 8, 18, 0, tzinfo=timezone.utc)


# =====================================================================
# 1. the shipped config is loadable and says what it claims
# =====================================================================


class TestTheShippedConfig:
    def test_it_loads_and_is_pinned_offline(self):
        c = load_seat_usage_config()
        assert c.tool.name == "ccusage"
        assert c.tool.version and c.tool.version != "latest"
        assert c.tool.offline, (
            "the four-gate law's 'no network at run time' is `offline: true` — "
            "turning it off silently makes an hourly launchd job reach the "
            "internet"
        )

    def test_the_report_path_is_a_repo_owned_root(self):
        from cobalt.vault import is_repo_owned

        assert is_repo_owned(load_seat_usage_config().report_file), (
            "the report is written through the L28 writer, which refuses every "
            "repo path that is not declared in REPO_OWNED_ROOTS"
        )

    def test_an_unknown_key_is_refused(self, tmp_path):
        bad = tmp_path / "seat_usage.yaml"
        bad.write_text(
            "tool: {name: c, version: '1', binary: /x, license: MIT}\n"
            "report_path: x\nnonsense: 1\n"
        )
        with pytest.raises(SeatUsageConfigError):
            load_seat_usage_config(bad)


# =====================================================================
# 2. JSON fixture -> typed rows -> unit text
# =====================================================================


class TestTheSilentZeroGuard:
    """The reason this guard exists: on 2026-09-08 ccusage's OFFLINE
    pricing table had no rate for `claude-fable-5-1` and priced $17.32
    of real usage at exactly $0.00. A used model showing zero is a
    plausible-empty artifact, which the fail-loud law forbids."""

    def test_a_used_model_priced_at_zero_is_unpriced_not_free(self, usage):
        fable = next(m for m in usage.models if m.model == "claude-fable-5-1")
        assert fable.cost is None and fable.unpriced
        assert "claude-fable-5-1" in usage.unpriced

    def test_a_declared_free_model_keeps_its_honest_zero(self, usage):
        main = next(m for m in usage.models if m.model == "mainframe")
        assert main.free and main.cost == 0.0
        assert "mainframe" not in usage.unpriced, (
            "the local lane is genuinely free — it must never raise the hourly "
            "unpriced warning"
        )

    def test_the_day_total_is_a_floor_when_anything_is_unpriced(self, cfg, usage):
        body = report.unit_body(cfg, usage, now=NOW)
        assert "≥ $134.28" in body
        assert "UNPRICED MODELS" in body

    def test_the_guard_can_be_turned_off_only_in_config(self, cfg):
        cfg.unpriced_is_loud = False
        u = ccusage.parse(cfg, FIXTURE, DAY)
        assert u.unpriced == []
        assert next(m for m in u.models if m.model == "gpt-6-astra").cost == 0.0


class TestUnitText:
    def test_every_column_is_present(self, cfg, usage):
        body = report.unit_body(cfg, usage, now=NOW)
        header = body.splitlines()[0]
        for column in ("model", "role hint", "cache read", "cache write",
                       "output", "API-equivalent $", "Δ since last run"):
            assert column in header

    def test_numbers_are_grouped_and_dollars_are_labelled(self, cfg, usage):
        body = report.unit_body(cfg, usage, now=NOW)
        assert "219,058,828" in body
        assert "$134.28" in body
        assert "**unpriced**" in body
        assert "$0.00 [^free]" in body

    def test_the_role_hint_prints_observed_seat_then_configured_role(self, cfg, usage):
        opus = next(m for m in usage.models if m.model == "claude-opus-5")
        assert report.role_hint(cfg, opus) == "claude · write seat"

    def test_an_unmapped_model_gets_a_dash_never_a_guess(self, cfg, usage):
        astra = next(m for m in usage.models if m.model == "gpt-6-astra")
        assert report.role_hint(cfg, astra) == "codex · —"

    def test_input_tokens_are_reported_even_though_they_are_not_a_column(self, cfg, usage):
        assert "Fresh input tokens:** 70,115" in report.unit_body(cfg, usage, now=NOW)

    def test_a_day_with_no_activity_says_so_rather_than_rendering_empty(self, cfg):
        empty = ccusage.parse(cfg, {"daily": []}, DAY)
        body = report.unit_body(cfg, empty, now=NOW)
        assert "no seat activity recorded" in body

    def test_unexpected_output_crashes_rather_than_reporting_zero(self, cfg):
        with pytest.raises(ccusage.CcusageError):
            ccusage.parse(cfg, {"nothing": True}, DAY)


class TestDelta:
    def test_no_previous_run_is_a_dash_not_a_zero(self, cfg, usage):
        assert "| — |" in report.unit_body(cfg, usage, now=NOW, previous=None)

    def test_a_change_since_the_last_run_is_signed(self, cfg, usage):
        prior = {"day": DAY.isoformat(), "models": {"claude-opus-5": {"cost": 130.0}}}
        body = report.unit_body(cfg, usage, now=NOW, previous=prior)
        assert "+$4.28" in body

    def test_yesterdays_snapshot_is_not_used(self, cfg):
        prior = {"day": "2026-09-07", "models": {"claude-opus-5": {"cost": 1.0}}}
        assert report.previous_snapshot(prior, DAY) is None, (
            "a Δ against yesterday's totals looks like a change and is a calendar "
            "boundary"
        )

    def test_the_snapshot_round_trips_into_the_next_runs_delta(self, cfg, usage):
        snap = report.snapshot(usage)
        assert snap["day"] == DAY.isoformat()
        assert snap["models"]["claude-fable-5-1"]["cost"] is None
        body = report.unit_body(cfg, usage, now=NOW, previous=snap)
        assert "$0.00" in body  # unchanged since "the last run" is itself


# =====================================================================
# 3. the write path — update in place, human cells, newest on top
# =====================================================================


@requires_db
@pytest.mark.usefixtures("dev_db_tx")
class TestTheWritePath:
    """Writes into tmp_path, which is outside the repo and outside both
    vaults — so `assert_write_target` allows it for the ordinary reason,
    and these tests are about the MERGE, not about the fences."""

    def _writer(self):
        from cobalt.vaultwrite import VaultWriteStore

        store = VaultWriteStore("cobalt_dev")
        store.ensure_schema()
        return VaultWriter("test.seatusage", store=store)

    def _seed(self, tmp_path, cfg, usage, day=DAY):
        path = tmp_path / "seat-usage.md"
        writer = self._writer()
        writer.create_if_absent(path, report.TEMPLATE)
        writer.upsert_unit(
            path, report.section_name(day), report.unit_id(day),
            report.unit_body(cfg, usage, now=NOW),
            placement=report.days_anchor(),
        )
        writer.upsert_region(
            path, report.section_name(day),
            report.human_region_id(day, path.read_text()),
            report.human_body(day), locate=report.human_region_locator(day),
        )
        return path, writer

    def test_the_same_unit_id_updates_in_place(self, tmp_path, cfg, usage):
        path, writer = self._seed(tmp_path, cfg, usage)
        prior = {"day": DAY.isoformat(), "models": {"claude-opus-5": {"cost": 130.0}}}
        writer.upsert_unit(
            path, report.section_name(DAY), report.unit_id(DAY),
            report.unit_body(cfg, usage, now=NOW, previous=prior),
            placement=report.days_anchor(),
        )
        text = path.read_text()
        assert text.count(f"<!-- cobalt:unit {report.unit_id(DAY)} -->") == 1, (
            "a second table for the same day means the id stopped being stable"
        )
        assert "+$4.28" in text

    def test_the_human_cells_are_seeded_blank_outside_the_unit(self, tmp_path, cfg, usage):
        path, _ = self._seed(tmp_path, cfg, usage)
        lines = path.read_text().split("\n")
        section = find_section(lines, report.section_name(DAY))
        unit = section.units[report.unit_id(DAY)]
        cell = next(i for i, l in enumerate(lines) if l.startswith(report.OPEN_CELL))
        assert section.open_line < cell < unit.open_line, (
            "the human cells must sit inside the day's section and OUTSIDE its "
            "generated unit, or the next run overwrites them"
        )

    def test_a_filled_cell_is_never_overwritten(self, tmp_path, cfg, usage):
        path, writer = self._seed(tmp_path, cfg, usage)
        path.write_text(path.read_text().replace(
            f"{report.OPEN_CELL}\n", f"{report.OPEN_CELL} 41%\n"
        ))
        # Every later run rewrites the unit; the cells are checked first
        # and left alone.
        assert report.human_cells_present(path.read_text(), DAY)
        writer.upsert_unit(
            path, report.section_name(DAY), report.unit_id(DAY),
            report.unit_body(cfg, usage, now=NOW),
            placement=report.days_anchor(),
        )
        assert f"{report.OPEN_CELL} 41%" in path.read_text()

    def test_the_presence_guard_reads_the_file_not_the_database(self, tmp_path, cfg, usage):
        """The merge's baseline lives in Postgres. A run that could not
        read it would treat Cobalt's blank template as the truth and wipe
        a filled cell — so the guard is the file's own content, which is
        always available."""
        path, _ = self._seed(tmp_path, cfg, usage)
        text = path.read_text()
        assert report.human_cells_present(text, DAY)
        assert not report.human_cells_present(text, date(2026, 9, 7))

    def test_newest_day_is_on_top(self, tmp_path, cfg, usage):
        older = date(2026, 9, 7)
        path, writer = self._seed(tmp_path, cfg, usage, day=older)
        writer.upsert_unit(
            path, report.section_name(DAY), report.unit_id(DAY),
            report.unit_body(cfg, usage, now=NOW),
            placement=report.days_anchor(),
        )
        text = path.read_text()
        assert text.index(report.section_name(DAY)) < text.index(report.section_name(older))

    def test_a_day_block_with_no_cells_under_it_is_a_loud_failure(
        self, tmp_path, cfg, usage
    ):
        """The one way the seed can silently do nothing: the file loses a
        day's block while that day's audit baseline survives, so the
        merge reads an empty span against a non-empty baseline as "the
        human deleted these lines". A block with nowhere to write his
        percentages, and nothing saying so, is a plausible-empty
        artifact — so the run fails instead."""
        from cobalt.seatusage.runner import _assert_cells_landed
        from cobalt.vaultwrite import VaultWriteError

        path, _ = self._seed(tmp_path, cfg, usage)
        path.write_text(
            path.read_text()
            .replace(f"{report.OPEN_CELL}\n", "")
            .replace(f"{report.CLOSE_CELL}\n", "")
        )
        with pytest.raises(VaultWriteError, match="no human cells"):
            _assert_cells_landed(path, DAY)

    def test_the_documented_recovery_is_the_one_that_works(
        self, tmp_path, cfg, usage
    ):
        """The error tells him to paste the two lines back in himself.
        They are his cells; Cobalt owning the repair would be Cobalt
        owning the cells."""
        from cobalt.seatusage.runner import _assert_cells_landed

        path, _ = self._seed(tmp_path, cfg, usage)
        path.write_text(path.read_text().replace(f"{report.OPEN_CELL}\n", ""))
        path.write_text(
            path.read_text().replace(
                f"### {DAY.isoformat()}\n",
                f"### {DAY.isoformat()}\n{report.OPEN_CELL} 41%\n",
            )
        )
        _assert_cells_landed(path, DAY)   # no raise

    def test_the_anchor_survives_every_write(self, tmp_path, cfg, usage):
        path, _ = self._seed(tmp_path, cfg, usage)
        assert path.read_text().count(report.ANCHOR) == 1


# =====================================================================
# 4. the windowed schedule
# =====================================================================


class TestWindowParsing:
    def test_a_window_round_trips(self):
        assert parse_window("06:00-23:00", "k") == (
            datetime(2026, 1, 1, 6, 0).time(), datetime(2026, 1, 1, 23, 0).time()
        )

    @pytest.mark.parametrize("raw", ["0600-2300", "06:00", "23:00-06:00", "6-7"])
    def test_a_window_that_does_not_parse_crashes(self, raw):
        with pytest.raises(JobConfigError):
            parse_window(raw, "seat_usage.window")

    def test_a_window_needs_an_interval_and_weekdays(self):
        with pytest.raises(Exception, match="INTERVAL"):
            Schedule(at="06:00", weekdays=[1], window_tunable="seat_usage.window")
        with pytest.raises(Exception, match="needs `weekdays`"):
            Schedule(every_min=60, window_tunable="seat_usage.window")


class TestTheShippedSchedule:
    def _spec(self):
        from cobalt.jobs.config import load_job_registry

        return load_job_registry().spec("com.cobalt.seat-usage")

    def test_the_plist_calendar_matches_the_registry_entry_for_entry(self):
        """launchd has no 'hourly between 06:00 and 23:00'. The window is
        expanded into moments, and the two can only stay honest if
        something compares them."""
        import plistlib

        spec = self._spec()
        data = plistlib.loads(spec.plist_path.read_bytes())
        assert [dict(e) for e in data["StartCalendarInterval"]] == \
            spec.schedule.calendar_entries()

    def test_it_is_due_inside_the_window_and_not_outside(self):
        from cobalt.session.clock import ET

        schedule = self._spec().schedule
        assert schedule.due_now(datetime(2026, 9, 8, 6, 0, tzinfo=ET))
        assert schedule.due_now(datetime(2026, 9, 8, 22, 59, tzinfo=ET))
        assert not schedule.due_now(datetime(2026, 9, 8, 5, 59, tzinfo=ET))
        assert not schedule.due_now(datetime(2026, 9, 9, 3, 0, tzinfo=ET))


class TestWindowedMissed:
    """The failure this arithmetic prevents: an hourly job that stops at
    23:00 would be reported MISSED at 01:05 every single night."""

    def _row(self, finished_et=None):
        from cobalt.session.clock import ET

        registered = datetime(2026, 9, 1, 6, 0, tzinfo=ET)
        return {
            "finished_at": finished_et.astimezone(timezone.utc) if finished_et else None,
            "registered_at": registered.astimezone(timezone.utc),
        }

    def _spec(self):
        from cobalt.jobs.config import load_job_registry

        return load_job_registry().spec("com.cobalt.seat-usage")

    def test_an_overnight_gap_is_not_a_miss(self):
        from cobalt.jobs.watchdog import is_missed
        from cobalt.session.clock import ET

        last = datetime(2026, 9, 8, 23, 0, tzinfo=ET)
        missed, _ = is_missed(
            self._spec(), self._row(last),
            now_et=datetime(2026, 9, 9, 3, 0, tzinfo=ET), grace=timedelta(minutes=30),
        )
        assert not missed

    def test_the_first_run_of_the_day_is_measured_from_the_window_opening(self):
        from cobalt.jobs.watchdog import is_missed
        from cobalt.session.clock import ET

        last = datetime(2026, 9, 8, 23, 0, tzinfo=ET)
        missed, _ = is_missed(
            self._spec(), self._row(last),
            now_et=datetime(2026, 9, 9, 6, 30, tzinfo=ET), grace=timedelta(minutes=30),
        )
        assert not missed, (
            "07:30 is one interval into the window; measuring from last night's "
            "23:00 would report a miss every morning"
        )

    def test_two_skipped_runs_inside_the_window_are_a_miss(self):
        from cobalt.jobs.watchdog import is_missed
        from cobalt.session.clock import ET

        last = datetime(2026, 9, 9, 9, 0, tzinfo=ET)
        missed, detail = is_missed(
            self._spec(), self._row(last),
            now_et=datetime(2026, 9, 9, 12, 1, tzinfo=ET), grace=timedelta(minutes=30),
        )
        assert missed and "two intervals" in detail


# =====================================================================
# 5. the freshness probe
# =====================================================================


class _FakeStore:
    def __init__(self, row):
        self._row = row

    def get(self, label):
        return self._row


def _job_row(*, finished=None, exit_code=0, last_result=None):
    from cobalt.session.clock import ET

    return {
        "finished_at": finished,
        "registered_at": datetime(2026, 9, 1, 6, 0, tzinfo=ET).astimezone(timezone.utc),
        "exit_code": exit_code,
        "last_result": last_result,
    }


class TestFreshnessProbe:
    def test_a_recent_run_inside_the_window_is_green(self):
        from cobalt.heartbeat.probes import seat_usage

        now = datetime(2026, 9, 8, 18, 0, tzinfo=timezone.utc)   # 14:00 ET
        probe = seat_usage(
            store=_FakeStore(_job_row(finished=now - timedelta(minutes=20))), now=now
        )
        assert probe.ok and "20 min ago" in probe.detail

    def test_a_stale_run_inside_the_window_is_red(self):
        from cobalt.heartbeat.probes import seat_usage

        now = datetime(2026, 9, 8, 18, 0, tzinfo=timezone.utc)
        probe = seat_usage(
            store=_FakeStore(_job_row(finished=now - timedelta(hours=4))), now=now
        )
        assert not probe.ok and "STALE" in probe.detail

    def test_outside_the_window_it_asks_nothing_and_stays_green(self):
        from cobalt.heartbeat.probes import seat_usage

        now = datetime(2026, 9, 9, 7, 0, tzinfo=timezone.utc)    # 03:00 ET
        probe = seat_usage(
            store=_FakeStore(_job_row(finished=now - timedelta(hours=4))), now=now
        )
        assert probe.ok and "not due" in probe.detail

    def test_a_failed_run_is_red(self):
        from cobalt.heartbeat.probes import seat_usage

        now = datetime(2026, 9, 8, 18, 0, tzinfo=timezone.utc)
        probe = seat_usage(
            store=_FakeStore(_job_row(finished=now, exit_code=1)), now=now
        )
        assert not probe.ok and "FAILED" in probe.detail

    def test_unpriced_models_are_reported_but_are_not_red(self):
        """They are loud in the report, hourly, next to the number they
        distort. A red beat for a condition fixed by a deliberate version
        bump would be a permanent alert."""
        from cobalt.heartbeat.probes import seat_usage

        now = datetime(2026, 9, 8, 18, 0, tzinfo=timezone.utc)
        probe = seat_usage(
            store=_FakeStore(
                _job_row(finished=now, last_result={"unpriced": ["claude-fable-5-1"]})
            ),
            now=now,
        )
        assert probe.ok and "UNPRICED in the report: claude-fable-5-1" in probe.detail

    def test_an_unreadable_store_is_unknown_not_green(self):
        from cobalt.heartbeat.probes import seat_usage

        class Broken:
            def get(self, label):
                raise RuntimeError("no database")

        probe = seat_usage(store=Broken(), now=datetime(2026, 9, 8, 18, 0, tzinfo=timezone.utc))
        assert not probe.ok and probe.unknown


# =====================================================================
# 6. the pin
# =====================================================================


class TestThePin:
    def test_a_version_that_does_not_match_the_pin_crashes(self, cfg, monkeypatch):
        monkeypatch.setattr(ccusage, "tool_version", lambda c: "99.0.0")
        with pytest.raises(ccusage.CcusageError, match="pinned to 20.0.20"):
            ccusage.assert_pinned(cfg)

    def test_a_missing_binary_says_so_rather_than_reporting_no_usage(self, cfg):
        with pytest.raises(ccusage.CcusageError, match="not installed"):
            ccusage.tool_version(cfg)

    def test_the_argv_never_reaches_the_network_and_never_uses_latest(self, cfg):
        argv = ccusage.argv(cfg, DAY)
        assert "--offline" in argv
        assert "--since" in argv and "--until" in argv
        assert not any("latest" in a for a in argv)
