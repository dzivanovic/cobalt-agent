"""Chunk H — the archiver probe sees unresolved archive incidents.

Spec `ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §11 and spec **O-7**:
"the heartbeat's archiver probe is not green while any [incident] is
unresolved", with the DESK's safe default for the wording and colour —
"not green = the probe's existing FAIL form, detail names the incident
count".

WHY THE HEARTBEAT HAS TO CARRY THIS. Known limit 3 (spec §12): a
withheld target's new bars age out of the vendor window (i5 ≈ 21 days)
if nobody repairs it. The incident list and the heartbeat ARE the alarm.
A dashboard that stayed green through a fortnight of withholding would
make the append mode worse than the overlay it replaces.

Offline: the probe's existing `_FakeStore` pattern plus an injected
incident reader. No database.
"""

from __future__ import annotations

from datetime import datetime, timezone

import pytest

from cobalt.heartbeat.probes import (
    _archiver_run_probe,
    _with_archive_incidents,
    archiver_freshness,
)

UTC = timezone.utc
RECENT = datetime(2026, 9, 5, 0, 53, tzinfo=UTC)      # Fri 20:53 ET
NOW = datetime(2026, 9, 5, 1, 0, tzinfo=UTC)


class _FakeStore:
    def __init__(self, row):
        self._row = row

    def get(self, label):
        assert label == "com.cobalt.archiver"
        return self._row


def _row(finished=RECENT, exit_code=0, rows_written=3164539):
    return {
        "label": "com.cobalt.archiver",
        "registered_at": datetime(2026, 9, 5, 2, 19, 45, tzinfo=UTC),
        "finished_at": finished,
        "exit_code": exit_code,
        "last_result": {"rows_written": rows_written},
    }


class _Incident:
    def __init__(self, kind, ticker="TESTARCH", interval="i5", first_seen_at=None):
        self.kind = kind
        self.ticker = ticker
        self.interval = interval
        self.first_seen_at = first_seen_at or datetime(2026, 9, 1, 0, 30, tzinfo=UTC)


def _reader(*incidents):
    def _read():
        return list(incidents)

    return _read


def _broken_reader(error):
    def _read():
        raise error

    return _read


# ---------------------------------------------------------------------
# Zero incidents changes nothing
# ---------------------------------------------------------------------


def test_zero_incidents_is_exactly_todays_result():
    """Mode isolation, again: until an `append` night runs there are no
    incidents, and the probe must be BYTE-IDENTICAL to what it has
    always reported. Asserted by IDENTITY — the same object comes back,
    not a rebuilt equal one."""
    base = _archiver_run_probe(_row(), NOW)
    assert _with_archive_incidents(base, _reader()) is base
    probe = archiver_freshness(store=_FakeStore(_row()), now=NOW, incidents=_reader())
    assert (probe.ok, probe.detail) == (base.ok, base.detail)
    assert probe.ok is True


def test_a_red_run_stays_red_with_its_own_reason():
    base = _archiver_run_probe(_row(exit_code=1), NOW)
    probe = archiver_freshness(
        store=_FakeStore(_row(exit_code=1)), now=NOW, incidents=_reader()
    )
    assert probe.ok is False
    assert probe.detail == base.detail
    assert "last run FAILED" in probe.detail


# ---------------------------------------------------------------------
# An unresolved incident is never green
# ---------------------------------------------------------------------


def test_one_unresolved_incident_is_not_green():
    probe = archiver_freshness(
        store=_FakeStore(_row()), now=NOW, incidents=_reader(_Incident("restated"))
    )
    assert probe.ok is False


def test_the_detail_names_the_count_and_the_oldest_kind():
    probe = archiver_freshness(
        store=_FakeStore(_row()),
        now=NOW,
        incidents=_reader(
            _Incident("gap", first_seen_at=datetime(2026, 9, 3, 1, 0, tzinfo=UTC)),
            _Incident("restated", ticker="THIN",
                      first_seen_at=datetime(2026, 9, 1, 1, 0, tzinfo=UTC)),
            _Incident("gap", ticker="TESTARCH", interval="i1",
                      first_seen_at=datetime(2026, 9, 4, 1, 0, tzinfo=UTC)),
        ),
    )
    assert probe.ok is False
    assert "3 unresolved archive incident(s)" in probe.detail
    assert "oldest restated" in probe.detail            # 09-01, the oldest
    assert "THIN/i5" in probe.detail
    assert "2026-09-01" in probe.detail
    assert "gap=2" in probe.detail and "restated=1" in probe.detail
    # The run's own line survives, so an operator still sees both facts.
    assert "last run" in probe.detail


def test_the_detail_points_at_the_command_that_lists_them():
    probe = archiver_freshness(
        store=_FakeStore(_row()), now=NOW, incidents=_reader(_Incident("gap"))
    )
    assert "cobalt archiver incidents" in probe.detail


def test_an_incident_outranks_a_healthy_run_but_not_a_stale_one():
    """A stale run is the bigger fact; the incident line is appended, and
    neither reading is green."""
    stale = archiver_freshness(
        store=_FakeStore(_row(finished=None)),
        now=datetime(2026, 9, 8, 1, 15, tzinfo=UTC),
        incidents=_reader(_Incident("gap")),
    )
    assert stale.ok is False
    assert "NEVER" in stale.detail or "STALE" in stale.detail


# ---------------------------------------------------------------------
# A missing table is LOUD, never green, and never a crash
# ---------------------------------------------------------------------


@pytest.mark.parametrize("error", [
    RuntimeError('relation "archive_incidents" does not exist'),
    Exception("connection refused"),
])
def test_an_unreadable_incident_table_is_a_loud_probe_failure(error):
    probe = archiver_freshness(
        store=_FakeStore(_row()), now=NOW, incidents=_broken_reader(error)
    )
    assert probe.ok is False
    assert "archive_incidents" in probe.detail
    assert "0011_archive_incidents.sql" in probe.detail
    assert "cobalt db migrate" in probe.detail


def test_an_unreadable_incident_table_does_not_crash_the_heartbeat_run():
    """L1 says fail loud — it does NOT say take the whole heartbeat down.
    The probe returns a red Probe; it does not raise."""
    probe = archiver_freshness(
        store=_FakeStore(_row()),
        now=NOW,
        incidents=_broken_reader(RuntimeError("boom")),
    )
    assert probe.name == "archiver"
    assert probe.ok is False


def test_the_run_detail_survives_an_unreadable_incident_table():
    probe = archiver_freshness(
        store=_FakeStore(_row()), now=NOW, incidents=_broken_reader(RuntimeError("boom"))
    )
    assert "rows written 3164539" in probe.detail


# ---------------------------------------------------------------------
# The probe reads incidents by itself in production
# ---------------------------------------------------------------------


def test_the_default_reader_is_the_archivers_own_unresolved_query():
    import inspect

    source = inspect.getsource(archiver_freshness)
    assert "incidents" in source
    assert "unresolved" in source
    # It must not reach for a writer.
    for writer in ("open_or_refresh", "resolve(", "upsert_bars", "insert_new_bars"):
        assert writer not in source, f"the probe reaches {writer}"
