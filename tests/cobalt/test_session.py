"""F1 session clock — Charter §3 F1 and SPRINT-LADDER §S1.

TIME IS FROZEN, NEVER SLEPT. Every test builds an explicit tz-aware
instant and hands it to the resolver. Nothing here reads the system
clock, so nothing here is flaky at 09:29 or on a Sunday, and the
early-close and holiday cases are testable at all.

The Charter's own acceptance test is the first block: "a card fired at
18:30 and one at 21:30 show the right session; the 21:30 one is
blocked." Plus the boundary pair (09:29:59 / 09:30:00), an early-close
day, and a Sunday.
"""

from __future__ import annotations

import os
import shutil
from datetime import datetime, time, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml

from cobalt.session import (
    Session,
    SessionBlocked,
    SessionClock,
    SessionError,
    assert_writable,
    session_clock,
)
from cobalt.session.calendar import CalendarError, CalendarYear, load_calendar
from cobalt.session.clock import BOUNDARY_KEYS, ET

# A store that records nothing — the counter is exercised separately in
# test_session_store; these tests are about the decision, not the row.
NULL_STORE = SimpleNamespace(record=lambda **kwargs: None)


def et(y, m, d, hh=0, mm=0, ss=0) -> datetime:
    """An ET wall clock as a real instant. DST comes from the date."""
    return datetime(y, m, d, hh, mm, ss, tzinfo=ET)


@pytest.fixture(scope="module")
def clock() -> SessionClock:
    return session_clock()


# ---------------------------------------------------------------------
# Charter §3 F1 acceptance
# ---------------------------------------------------------------------


def test_charter_card_at_1830_is_aftermarket(clock):
    assert clock.session(et(2026, 9, 3, 18, 30)) is Session.AFTERMARKET


def test_charter_card_at_2130_is_overnight(clock):
    assert clock.session(et(2026, 9, 3, 21, 30)) is Session.OVERNIGHT


def test_charter_card_at_2030_is_refused(clock):
    """"the 21:30 one is blocked" — the block is the 20:00-21:00 window
    the 21:30 card had to pass through."""
    assert clock.session(et(2026, 9, 3, 20, 30)) is Session.MARKET_RESET
    with pytest.raises(SessionBlocked) as excinfo:
        assert_writable(
            "aset.card",
            target="TSLA",
            now=et(2026, 9, 3, 20, 30),
            clock=clock,
            store=NULL_STORE,
        )
    message = str(excinfo.value)
    assert "MARKET RESET" in message
    assert "20:00-21:00" in message  # the window is NAMED, per S1
    assert "21:00 ET" in message  # ...and so is when it lifts
    assert excinfo.value.session is Session.MARKET_RESET
    assert excinfo.value.actor == "aset.card"


@pytest.mark.parametrize(
    "at,expected",
    [
        (et(2026, 9, 3, 3, 59, 59), Session.OVERNIGHT),
        (et(2026, 9, 3, 4, 0, 0), Session.PREMARKET),
        (et(2026, 9, 3, 9, 29, 59), Session.PREMARKET),
        (et(2026, 9, 3, 9, 30, 0), Session.RTH),
        (et(2026, 9, 3, 15, 59, 59), Session.RTH),
        (et(2026, 9, 3, 16, 0, 0), Session.AFTERMARKET),
        (et(2026, 9, 3, 19, 59, 59), Session.AFTERMARKET),
        (et(2026, 9, 3, 20, 0, 0), Session.MARKET_RESET),
        (et(2026, 9, 3, 20, 59, 59), Session.MARKET_RESET),
        (et(2026, 9, 3, 21, 0, 0), Session.OVERNIGHT),
        (et(2026, 9, 3, 23, 59, 59), Session.OVERNIGHT),
        (et(2026, 9, 3, 0, 0, 0), Session.OVERNIGHT),
    ],
)
def test_every_boundary_is_inclusive_start_exclusive_end(clock, at, expected):
    assert clock.session(at) is expected


def test_the_0930_pair_is_one_second_apart_and_two_sessions(clock):
    before = et(2026, 9, 3, 9, 29, 59)
    after = et(2026, 9, 3, 9, 30, 0)
    assert (after - before).total_seconds() == 1
    assert clock.session(before) is Session.PREMARKET
    assert clock.session(after) is Session.RTH


# ---------------------------------------------------------------------
# Calendar: weekends, holidays, early closes
# ---------------------------------------------------------------------


def test_a_sunday_is_overnight_all_day(clock):
    sunday = datetime(2026, 9, 6)
    assert sunday.strftime("%A") == "Sunday"
    for hour in (4, 9, 12, 16, 20, 23):
        assert clock.session(et(2026, 9, 6, hour, 30)) is Session.OVERNIGHT
    assert clock.windows_for(sunday.date()) == []


def test_a_saturday_is_overnight_all_day(clock):
    assert clock.session(et(2026, 9, 5, 12, 0)) is Session.OVERNIGHT


def test_a_holiday_is_overnight_even_at_1030(clock):
    """Labor Day 2026-09-07 — a Monday that looks like a trading day to
    anything that only checks the weekday."""
    assert clock.calendar.holiday_name(datetime(2026, 9, 7).date()) == "Labor Day"
    assert clock.session(et(2026, 9, 7, 10, 30)) is Session.OVERNIGHT
    assert clock.session(et(2026, 9, 8, 10, 30)) is Session.RTH  # the day after


@pytest.mark.parametrize(
    "at,expected",
    [
        (et(2026, 11, 27, 10, 0), Session.RTH),  # half day, still open
        (et(2026, 11, 27, 12, 59, 59), Session.RTH),
        (et(2026, 11, 27, 13, 0), Session.AFTERMARKET),  # rth ends 13:00
        (et(2026, 11, 27, 16, 59, 59), Session.AFTERMARKET),
        (et(2026, 11, 27, 17, 0), Session.OVERNIGHT),  # aftermarket ends 17:00
        (et(2026, 11, 27, 19, 0), Session.OVERNIGHT),  # the half-day gap
        (et(2026, 11, 27, 20, 30), Session.MARKET_RESET),  # archiver still runs
        (et(2026, 11, 27, 21, 30), Session.OVERNIGHT),
    ],
)
def test_early_close_day_ends_rth_at_1300_and_aftermarket_at_1700(clock, at, expected):
    assert clock.calendar.is_early_close(at.date())
    assert clock.session(at) is expected


def test_a_full_day_has_no_gap_between_aftermarket_and_market_reset(clock):
    """The half-day gap is real; a full day must NOT have one."""
    assert clock.session(et(2026, 9, 3, 19, 59, 59)) is Session.AFTERMARKET
    assert clock.session(et(2026, 9, 3, 20, 0, 0)) is Session.MARKET_RESET


# ---------------------------------------------------------------------
# DST: sessions are ET, storage is UTC (ADR-0007)
# ---------------------------------------------------------------------


def test_the_same_utc_hour_is_a_different_session_in_the_two_regimes(clock):
    """13:30 UTC is the RTH open in summer and still premarket in winter.
    This is the whole reason no feature may key off wall-clock."""
    summer = datetime(2026, 9, 3, 13, 30, tzinfo=timezone.utc)
    winter = datetime(2026, 1, 15, 13, 30, tzinfo=timezone.utc)
    assert clock.session(summer) is Session.RTH
    assert clock.session(winter) is Session.PREMARKET
    assert clock.session(datetime(2026, 1, 15, 14, 30, tzinfo=timezone.utc)) is Session.RTH


def test_a_naive_datetime_is_refused_not_guessed(clock):
    with pytest.raises(SessionError, match="naive datetime"):
        clock.session(datetime(2026, 9, 3, 9, 30))


def test_a_non_datetime_is_refused(clock):
    with pytest.raises(SessionError, match="needs a datetime"):
        clock.session("2026-09-03T09:30:00+00:00")


# ---------------------------------------------------------------------
# next_boundary
# ---------------------------------------------------------------------


@pytest.mark.parametrize(
    "at,expected_session,expected_et",
    [
        (et(2026, 9, 3, 9, 0), Session.RTH, et(2026, 9, 3, 9, 30)),
        (et(2026, 9, 3, 10, 0), Session.AFTERMARKET, et(2026, 9, 3, 16, 0)),
        (et(2026, 9, 3, 18, 30), Session.MARKET_RESET, et(2026, 9, 3, 20, 0)),
        (et(2026, 9, 3, 20, 30), Session.OVERNIGHT, et(2026, 9, 3, 21, 0)),
        # Friday night -> skips the weekend AND Labor Day Monday
        (et(2026, 9, 4, 21, 30), Session.PREMARKET, et(2026, 9, 8, 4, 0)),
        # Christmas Day (Friday) -> the following Monday
        (et(2026, 12, 25, 11, 0), Session.PREMARKET, et(2026, 12, 28, 4, 0)),
    ],
)
def test_next_boundary_walks_over_weekends_and_holidays(
    clock, at, expected_session, expected_et
):
    when, nxt = clock.next_boundary(at)
    assert nxt is expected_session
    assert when == expected_et


# ---------------------------------------------------------------------
# Config: the boundaries are rows, the calendar is a file, both fail loud
# ---------------------------------------------------------------------


def test_every_boundary_is_a_tunables_row_with_a_named_consumer():
    """F16: no inline literal in a predicate. The session module is
    nothing BUT boundary predicates, so this is its F16 test."""
    from cobalt.taxonomy.loader import load_tunables
    from cobalt.taxonomy.tunables import TunableUnit

    rows = load_tunables().by_key
    for key in BOUNDARY_KEYS:
        assert key in rows, f"{key} is not a tunables row"
        row = rows[key]
        assert row.unit is TunableUnit.TIME
        assert row.consumers, f"{key} has no named consumer"
        assert isinstance(row.value, str) and ":" in row.value


def test_a_missing_boundary_row_crashes_rather_than_defaulting(monkeypatch):
    """Delete `session.rth_open` from the registry and the clock refuses
    to boot. There is no built-in 09:30 anywhere in the module."""
    import cobalt.session.clock as clock_mod
    from cobalt.taxonomy.loader import load_tunables

    registry = load_tunables()
    registry.tunables = [t for t in registry.tunables if t.key != "session.rth_open"]
    monkeypatch.setattr(clock_mod, "load_tunables", lambda: registry)

    with pytest.raises(SessionError, match="session.rth_open"):
        SessionClock.from_config()


def test_a_boundary_row_with_the_wrong_unit_crashes(monkeypatch):
    import cobalt.session.clock as clock_mod
    from cobalt.taxonomy.loader import load_tunables
    from cobalt.taxonomy.tunables import TunableUnit

    registry = load_tunables()
    for row in registry.tunables:
        if row.key == "session.rth_open":
            row.unit = TunableUnit.MIN
    monkeypatch.setattr(clock_mod, "load_tunables", lambda: registry)

    with pytest.raises(SessionError, match="expected 'time'"):
        SessionClock.from_config()


def test_out_of_order_boundaries_crash():
    boundaries = {
        "session.premarket_open": time(4, 0),
        "session.rth_open": time(9, 30),
        "session.rth_close": time(9, 0),  # before the open
        "session.aftermarket_close": time(20, 0),
        "session.market_reset_open": time(20, 0),
        "session.market_reset_close": time(21, 0),
        "session.early_close.rth_close": time(13, 0),
        "session.early_close.aftermarket_close": time(17, 0),
    }
    clock = SessionClock(boundaries, load_calendar())
    with pytest.raises(SessionError, match="out of order"):
        clock._assert_ordered()


def test_market_reset_must_start_when_aftermarket_ends_on_a_full_day():
    boundaries = {
        "session.premarket_open": time(4, 0),
        "session.rth_open": time(9, 30),
        "session.rth_close": time(16, 0),
        "session.aftermarket_close": time(19, 0),  # diverged
        "session.market_reset_open": time(20, 0),
        "session.market_reset_close": time(21, 0),
        "session.early_close.rth_close": time(13, 0),
        "session.early_close.aftermarket_close": time(17, 0),
    }
    clock = SessionClock(boundaries, load_calendar())
    with pytest.raises(SessionError, match="must equal"):
        clock._assert_ordered()


def test_an_uncovered_year_raises_and_never_guesses_a_weekday(clock):
    """A Tuesday in 2031 looks exactly like a trading day to anything
    that checks the weekday. The calendar refuses to answer instead."""
    with pytest.raises(CalendarError, match="no NYSE calendar for 2031"):
        clock.session(et(2031, 6, 10, 10, 30))


def test_calendar_rejects_a_date_outside_its_own_year(tmp_path):
    with pytest.raises(ValueError, match="not in year 2026"):
        CalendarYear(year=2026, holidays=[{"date": "2025-12-25", "name": "Christmas"}])


def test_calendar_rejects_a_day_that_is_both_closed_and_half_closed():
    with pytest.raises(ValueError, match="BOTH a holiday and an early close"):
        CalendarYear(
            year=2026,
            holidays=[{"date": "2026-12-25", "name": "Christmas"}],
            early_closes=[{"date": "2026-12-25", "name": "Christmas Eve"}],
        )


def test_calendar_directory_with_no_files_crashes(tmp_path):
    with pytest.raises(CalendarError, match="no nyse-"):
        load_calendar(tmp_path)


def test_shipped_calendar_matches_its_file(clock):
    """The config on disk IS the calendar — no hidden second copy."""
    from cobalt.session.calendar import CALENDAR_DIR

    # Every shipped year, not a hardcoded one: S1-P2 added nyse-2025.yaml
    # (S1-P1 carried it as an open item — `session()` over the 2025 third
    # of the bars corpus used to raise CalendarError by design). The
    # assertion is now "the loader's totals equal the files' totals",
    # which stays true as years are added.
    files = sorted(CALENDAR_DIR.glob("nyse-*.yaml"))
    years = [yaml.safe_load(f.read_text()) for f in files]
    assert clock.calendar.covered_years == sorted(y["year"] for y in years)
    assert clock.calendar.holiday_count == sum(len(y["holidays"]) for y in years)
    assert clock.calendar.early_close_count == sum(len(y["early_closes"]) for y in years)


# ---------------------------------------------------------------------
# The guard
# ---------------------------------------------------------------------


@pytest.mark.parametrize(
    "at",
    [
        et(2026, 9, 3, 9, 30),
        et(2026, 9, 3, 18, 30),
        et(2026, 9, 3, 21, 30),
        et(2026, 9, 6, 12, 0),
        et(2026, 11, 27, 20, 59, 59),  # last second of the block on a half day
    ],
)
def test_assert_writable_allows_every_session_but_market_reset(clock, at):
    if clock.session(at) is Session.MARKET_RESET:
        with pytest.raises(SessionBlocked):
            assert_writable("t", now=at, clock=clock, store=NULL_STORE)
    else:
        assert assert_writable("t", now=at, clock=clock, store=NULL_STORE) is clock.session(at)


def test_the_block_is_recorded_for_the_heartbeat(clock):
    recorded = []
    store = SimpleNamespace(record=lambda **kw: recorded.append(kw))
    with pytest.raises(SessionBlocked):
        assert_writable(
            "vaultwrite:prefill.daily:upsert_unit",
            target="/x/2026-09-03.md",
            now=et(2026, 9, 3, 20, 30),
            clock=clock,
            store=store,
        )
    assert len(recorded) == 1
    assert recorded[0]["session"] == "market_reset"
    assert recorded[0]["actor"] == "vaultwrite:prefill.daily:upsert_unit"
    assert recorded[0]["target"] == "/x/2026-09-03.md"
    assert "MARKET RESET" in recorded[0]["reason"]


def test_a_dead_database_loses_the_counter_row_not_the_block(clock, monkeypatch):
    """The refusal must not depend on the counter. `SessionBlockStore`
    swallows and LOGS a persistence failure — because by the time it is
    called the block has already been decided, and a database outage
    turning a hard block into a pass is the failure mode that matters."""
    from cobalt import db
    from cobalt.session.store import SessionBlockStore

    def dead(*args, **kwargs):
        raise RuntimeError("connection refused")

    monkeypatch.setattr(db, "connect", dead)
    store = SessionBlockStore(db_name="cobalt_dev")

    assert store.record(session="market_reset", actor="t", target=None, reason="r") is None

    with pytest.raises(SessionBlocked):
        assert_writable("t", now=et(2026, 9, 3, 20, 30), clock=clock, store=store)


def test_session_enum_stamps_as_plain_text():
    """It goes into a `text` column and into f-strings."""
    assert Session.RTH.value == "rth"
    assert f"{Session.MARKET_RESET}" == "market_reset"
    assert str(Session.OVERNIGHT) == "overnight"


# ---------------------------------------------------------------------
# Wiring: the gate is ON the write paths, not just importable
# ---------------------------------------------------------------------

DEV_VAULT = Path.home() / "dev-vault-cobalt"

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)
requires_dev_vault = pytest.mark.skipif(
    not DEV_VAULT.is_dir(), reason=f"dev vault {DEV_VAULT} not present"
)

MARKET_RESET_NOW = et(2026, 9, 3, 20, 30).astimezone(timezone.utc)


@pytest.fixture
def dev_dir(request):
    path = DEV_VAULT / "_f1-tests" / request.node.name.replace("/", "_")[:80]
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True)
    yield path
    shutil.rmtree(path, ignore_errors=True)


@requires_db
@requires_dev_vault
@pytest.mark.usefixtures("dev_db_tx")
def test_vault_writer_refuses_to_create_a_note_during_market_reset(dev_dir):
    from cobalt.vaultwrite import VaultWriter, VaultWriteStore

    store = VaultWriteStore("cobalt_dev")
    store.ensure_schema()
    writer = VaultWriter("f1.test", store=store, now=lambda: MARKET_RESET_NOW)

    with pytest.raises(SessionBlocked, match="MARKET RESET"):
        writer.create_if_absent(dev_dir / "note.md", "# hello\n")
    assert not (dev_dir / "note.md").exists()  # nothing was written


@requires_db
@requires_dev_vault
@pytest.mark.usefixtures("dev_db_tx")
def test_vault_writer_refuses_to_upsert_a_unit_during_market_reset(dev_dir):
    from cobalt.vaultwrite import VaultWriter, VaultWriteStore

    store = VaultWriteStore("cobalt_dev")
    store.ensure_schema()
    path = dev_dir / "note.md"

    open_writer = VaultWriter("f1.test", store=store)  # frozen clock = RTH
    open_writer.create_if_absent(path, "# note\n")
    before = path.read_text()

    blocked = VaultWriter("f1.test", store=store, now=lambda: MARKET_RESET_NOW)
    with pytest.raises(SessionBlocked, match="MARKET RESET"):
        blocked.upsert_unit(path, "plan", "u1", "body")
    assert path.read_text() == before  # byte-identical


@requires_db
@requires_dev_vault
@pytest.mark.usefixtures("dev_db_tx")
def test_a_dry_run_is_allowed_during_market_reset(dev_dir):
    """The one carve-out that writes nothing: `--dry-run` still works,
    because finding out what a job WOULD do is exactly what you want at
    20:30 when a job just refused."""
    from cobalt.vaultwrite import VaultWriter, VaultWriteStore

    store = VaultWriteStore("cobalt_dev")
    store.ensure_schema()
    path = dev_dir / "note.md"
    VaultWriter("f1.test", store=store).create_if_absent(path, "# note\n")

    dry = VaultWriter(
        "f1.test", store=store, dry_run=True, now=lambda: MARKET_RESET_NOW
    )
    result = dry.upsert_unit(path, "plan", "u1", "body")
    assert result.dry_run
    assert result.diff  # it computed the whole thing
    assert path.read_text() == "# note\n"  # and wrote none of it


@requires_db
@requires_dev_vault
@pytest.mark.usefixtures("dev_db_tx")
def test_every_vault_write_stamps_its_session(dev_dir):
    from cobalt.vaultwrite import VaultWriter, VaultWriteStore

    store = VaultWriteStore("cobalt_dev")
    store.ensure_schema()
    writer = VaultWriter("f1.test", store=store)  # frozen clock: 10:00 ET
    result = writer.create_if_absent(dev_dir / "note.md", "# note\n")

    row = store.get_write(result.write_id)
    assert row["session"] == "rth"


@requires_db
@pytest.mark.usefixtures("dev_db_tx")
def test_every_card_stamps_its_session():
    from cobalt.aset.store import AsetStore

    store = AsetStore("cobalt_dev")
    store.ensure_schema()
    result = compute_test_sizing()
    row_id = store.save(result)  # frozen clock: 10:00 ET Thursday

    with store._connect() as conn:
        session = conn.execute(
            "SELECT session FROM aset_sizings WHERE id = %s", (row_id,)
        ).fetchone()[0]
    assert session == "rth"

    # ...and an explicit instant overrides it, which is how the backfill
    # and the tests reach every other session.
    row_id2 = store.save(result, now=et(2026, 9, 3, 18, 30))
    with store._connect() as conn:
        session2 = conn.execute(
            "SELECT session FROM aset_sizings WHERE id = %s", (row_id2,)
        ).fetchone()[0]
    assert session2 == "aftermarket"


def compute_test_sizing():
    from decimal import Decimal

    from cobalt.aset.engine import compute_sizing
    from cobalt.aset.models import Direction, Grade, SheetMode, SizingInput

    return compute_sizing(
        SizingInput(
            ticker="F1TEST",
            grade=Grade.A,
            direction=Direction.LONG,
            sheet_mode=SheetMode.HALF,
            risk_dollars=Decimal("50"),
            entry=Decimal("10.00"),
            stop=Decimal("9.50"),
        ),
        [Grade.A],
        Decimal("10"),
    )
