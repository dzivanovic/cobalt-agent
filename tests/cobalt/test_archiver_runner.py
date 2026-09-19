"""Chunk N — the runner: MODE ISOLATION, the shadow compare, the append night.

Spec `ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §5, §6, §7, §9.

THERE WAS NO RUNNER TEST FILE BEFORE THIS ONE. The nightly run is the
thing that writes 3.34M rows a night, and the only guard on it was the
store's two integration tests.

§5 is the promise this file exists to keep: **in `upsert` mode the
write path is today's code byte for byte.** So the first section is
DIFFERENTIAL — it asserts what the run does against what it did before
the redesign — and the additions are PINNED by a test that fails if a
fourth one appears.

Everything here is offline: a fake store that records every call and a
fake `fetch`. No database, no network, no clock read the test does not
control.
"""

from __future__ import annotations

import asyncio
import json
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from cobalt.archiver import runner as runner_mod
from cobalt.archiver import shadow as shadow_mod
from cobalt.archiver.collector import CollectorError
from cobalt.archiver.models import Bar, Interval
from cobalt.archiver.reconcile import BarValues, IncidentKind, TargetStatus, bar_values
from cobalt.archiver.settings import ArchiverSettings
from cobalt.archiver.store import ArchiveLockError

UTC = timezone.utc
FETCH_AT = datetime(2026, 9, 18, 20, 30, tzinfo=UTC)


def ts(day: int, hour: int, minute: int) -> datetime:
    return datetime(2026, 9, day, hour, minute, tzinfo=UTC)


def bar(when, close="100.00", ticker="TESTARCH", interval=Interval.I5, volume=1234) -> Bar:
    return Bar(
        ticker=ticker, interval=interval, ts=when,
        open=Decimal("99.00"), high=Decimal("101.00"), low=Decimal("98.50"),
        close=Decimal(close), volume=volume,
    )


def settings(write_mode="upsert", shadow_compare="on", **over) -> ArchiverSettings:
    payload = {
        "write_mode": write_mode,
        "shadow_compare": shadow_compare,
        "shadow_statement_timeout_s": 10,
        "shadow_retention_nights": 30,
        "repair": {
            "quiet_before_open_min": 10,
            "quiet_after_cycle_min": 5,
            "cycle_max_min": 30,
        },
    }
    payload.update(over)
    return ArchiverSettings(**payload)


# ---------------------------------------------------------------------
# The fake store — records EVERY call, in order
# ---------------------------------------------------------------------


class FakeConn:
    def __init__(self, store):
        self.store = store

    def execute(self, query, params=None):
        self.store.calls.append(("conn.execute", str(query)[:40]))
        return self

    def fetchone(self):
        return (True,)


class FakeStore:
    def __init__(self, *, stored=None, progress=None, lock_held=False, insert_rowcount=None):
        self.calls: list[tuple] = []
        self.stored: dict[tuple, dict] = dict(stored or {})
        self.progress: dict[tuple, datetime] = dict(progress or {})
        self.upserted: list[list[Bar]] = []
        self.inserted: list[list[Bar]] = []
        self.written_progress: list[tuple] = []
        self.written_incidents: list[tuple] = []
        self.lock_held = lock_held
        self.insert_rowcount = insert_rowcount
        self.rollbacks = 0

    # --- what today's run already calls --------------------------------
    def ensure_schema(self):
        self.calls.append(("ensure_schema",))

    def upsert_bars(self, bars, *, before_commit=None):
        self.calls.append(("upsert_bars", len(bars)))
        self.upserted.append(list(bars))
        return len(bars)

    # --- the append path ------------------------------------------------
    @contextmanager
    def run_lock(self, what):
        self.calls.append(("run_lock", what))
        if self.lock_held:
            raise ArchiveLockError(f"another archive/repair run holds the lock — {what}")
        yield FakeConn(self)

    @contextmanager
    def target_transaction(self):
        self.calls.append(("target_transaction",))
        conn = FakeConn(self)
        try:
            yield conn
        except BaseException:
            self.rollbacks += 1
            raise

    def bars_in_range(self, conn, ticker, interval, start, end):
        self.calls.append(("bars_in_range", ticker, interval.value if hasattr(interval, "value") else interval))
        held = self.stored.get((ticker, getattr(interval, "value", interval)), {})
        return {k: v for k, v in held.items() if start is None or (start <= k <= end)}

    def insert_new_bars(self, conn, bars):
        self.calls.append(("insert_new_bars", len(bars)))
        self.inserted.append(list(bars))
        return len(bars) if self.insert_rowcount is None else self.insert_rowcount

    @property
    def names(self) -> list[str]:
        return [c[0] for c in self.calls]

    @property
    def write_calls(self) -> list[str]:
        return [n for n in self.names if n in {"upsert_bars", "insert_new_bars"}]


class FakeProgress:
    """Stands in for `cobalt.archiver.progress`, recording every write."""

    def __init__(self, store: FakeStore):
        self.store = store

    def read_archived_through(self, conn, ticker, interval):
        self.store.calls.append(("read_progress", ticker))
        return self.store.progress.get((ticker, getattr(interval, "value", interval)))

    def upsert_progress(self, conn, *, plan, run_id, now):
        if plan.archived_through_after is None:
            raise RuntimeError("not accepted")
        self.store.calls.append(("upsert_progress", plan.ticker, plan.archived_through_after))
        self.store.written_progress.append((plan.ticker, plan.archived_through_after, run_id))


class FakeIncidents:
    def __init__(self, store: FakeStore):
        self.store = store
        self._next = 1

    def open_or_refresh(self, conn, draft, *, run_id, now):
        self.store.calls.append(("open_incident", draft.kind.value, draft.ticker))
        self.store.written_incidents.append((draft.kind, draft.ticker, run_id))
        self._next += 1
        return self._next - 1


@pytest.fixture
def wired(monkeypatch, tmp_path):
    """A runner wired to fakes, with the shadow artifact in tmp_path."""
    monkeypatch.setattr(shadow_mod, "SHADOW_DIR", tmp_path / "archiver-shadow")

    def _wire(store: FakeStore):
        monkeypatch.setattr(runner_mod, "progress", FakeProgress(store))
        monkeypatch.setattr(runner_mod, "incidents", FakeIncidents(store))
        return store

    return _wire


def run(targets, *, store, fetch, cfg, mode="full", now=FETCH_AT):
    return asyncio.run(
        runner_mod._run_targets(
            targets, mode=mode, store=store, fetch=fetch, settings=cfg, now=lambda: now
        )
    )


def fetcher(mapping):
    async def _fetch(ticker, interval, token, **kwargs):
        key = (ticker, getattr(interval, "value", interval))
        value = mapping[key]
        if isinstance(value, Exception):
            raise value
        return list(value)

    return _fetch


@pytest.fixture(autouse=True)
def _no_sleep_no_token(monkeypatch):
    async def _instant(_seconds):
        return None

    async def _token():
        return "TEST-TOKEN"

    monkeypatch.setattr(runner_mod.asyncio, "sleep", _instant)
    monkeypatch.setattr(runner_mod, "resolve_token", _token)


# =====================================================================
# §5 — MODE ISOLATION, differential against today's behaviour
# =====================================================================


NIGHT_1 = [bar(ts(17, 19, 55)), bar(ts(18, 19, 50)), bar(ts(18, 19, 55))]
#: the latest bar has NOT closed at 20:30? it has — this one is the
#: forming bar a fetch at 19:56 would carry.
FORMING = bar(ts(18, 20, 29), close="101.00")


@pytest.mark.parametrize("night", [1, 2])
def test_upsert_sends_the_whole_export_on_every_night(wired, night):
    store = wired(FakeStore(progress={("TESTARCH", "i5"): ts(18, 19, 50)}))
    export = NIGHT_1 + [FORMING]
    run([("TESTARCH", Interval.I5)], store=store,
        fetch=fetcher({("TESTARCH", "i5"): export}), cfg=settings(shadow_compare="off"))
    if night == 2:
        run([("TESTARCH", Interval.I5)], store=store,
            fetch=fetcher({("TESTARCH", "i5"): export}), cfg=settings(shadow_compare="off"))
    for sent in store.upserted:
        assert sent == export, "the whole export, unfiltered — no completeness cut"
    assert len(store.upserted) == night


def test_upsert_keeps_the_incomplete_latest_bar(wired):
    store = wired(FakeStore())
    run([("TESTARCH", Interval.I5)], store=store,
        fetch=fetcher({("TESTARCH", "i5"): NIGHT_1 + [FORMING]}),
        cfg=settings(shadow_compare="off"))
    assert FORMING in store.upserted[0]


def test_upsert_writes_no_progress_and_no_incident(wired):
    store = wired(FakeStore())
    run([("TESTARCH", Interval.I5)], store=store,
        fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    assert store.written_progress == []
    assert store.written_incidents == []
    assert "insert_new_bars" not in store.names


def test_upsert_keeps_todays_failure_on_an_empty_export(wired):
    store = wired(FakeStore())
    summary = run(
        [("TESTARCH", Interval.I5)], store=store,
        fetch=fetcher({("TESTARCH", "i5"): CollectorError("No data rows for TESTARCH/i5.")}),
        cfg=settings(shadow_compare="off"),
    )
    assert len(summary.failures) == 1
    assert "No data rows" in summary.failures[0]
    assert store.written_incidents == []


def test_upsert_keeps_the_submitted_row_count(wired):
    """`rows_written` in `upsert` mode is rows SUBMITTED, as it has always
    been — `upsert_bars` returns `len(rows)` and the report says so."""
    store = wired(FakeStore())
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    assert summary.rows_written == len(NIGHT_1) == 3
    assert summary.requests == 1
    assert summary.tickers == {"TESTARCH"}


def test_upsert_keeps_the_run_report_row_byte_for_byte(wired, tmp_path, monkeypatch):
    from cobalt.archiver import report as report_mod

    path = tmp_path / "archiver-runs.md"
    monkeypatch.setattr(report_mod, "REPORT_PATH", path)
    store = wired(FakeStore())
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    report_mod.append_run_report(summary)
    content = path.read_text()
    assert report_mod.COLUMNS in content
    assert report_mod.APPEND_COLUMNS not in content, (
        "the append columns must not appear on an upsert night"
    )
    row = [line for line in content.splitlines() if line.startswith("| 2026")][-1]
    assert row.count("|") == 9        # 8 columns, today's shape
    assert "| full | cobalt_dev | 1 | 1 | 3 | 0 |" in row


def test_the_complete_list_of_upsert_mode_additions_is_pinned(wired):
    """§5: exactly THREE things a night in `upsert` mode now does that
    today's night does not — (1) the run-level lock, (2) the pre-write
    shadow read, (3) one `shadow` key in `job.result` plus one artifact.
    This test fails if a fourth appears."""
    off = wired(FakeStore())
    run([("TESTARCH", Interval.I5)], store=off,
        fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings(shadow_compare="off"))
    # (1) the lock, and NOTHING else beyond today's two calls.
    assert off.names == ["run_lock", "ensure_schema", "upsert_bars"]

    on = wired(FakeStore())
    summary = run([("TESTARCH", Interval.I5)], store=on,
                  fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    # (2) the shadow read: one transaction, its statement_timeout, one
    #     range read — all before the write, and nothing else.
    assert on.names == [
        "run_lock", "ensure_schema", "target_transaction", "conn.execute",
        "bars_in_range", "upsert_bars",
    ]
    assert "set_config" in on.calls[3][1], "the shadow read must be time-bounded"
    # (3) the one extra key in the job result.
    assert set(summary.job_result()) == {
        "rows_written", "tickers", "requests", "failures", "duration", "shadow"
    }
    # ...and no write method was reached by the shadow.
    assert on.write_calls == ["upsert_bars"]


def test_run_targets_mode_still_means_the_report_scope(wired):
    """Both assertions are the ones this test was written with; only the
    CLOCK moved. It drives a backfill, and from `cto-2026-09-19.md` §4
    R34 "B" a backfill declares the window it runs in and is refused
    inside 04:00-09:30 ET, so an hour a backfill may actually hold the
    transport is now part of driving one. `FETCH_AT` is 16:30 ET, inside
    the radar's 04:00-20:00 window where the radar alone already holds
    the whole ceiling; `BACKFILL_AT` is 22:00 ET, which no scheduled
    consumer holds. See `BACKFILL_AT` and the R34 section below."""
    store = wired(FakeStore())
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings(),
                  mode="backfill:TESTARCH", now=BACKFILL_AT)
    assert summary.mode == "backfill:TESTARCH"
    assert summary.write_mode == "upsert"


def test_any_other_write_mode_is_refused_before_the_run_starts():
    with pytest.raises(Exception) as e:
        settings(write_mode="both")
    assert "archiver.write_mode" in str(e.value)


def test_the_run_level_lock_is_taken_in_both_write_modes(wired):
    for mode in ("upsert", "append"):
        store = wired(FakeStore())
        run([("TESTARCH", Interval.I5)], store=store,
            fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings(write_mode=mode))
        assert store.names[0] == "run_lock"
        assert mode in store.calls[0][1]


def test_a_second_run_refuses_on_the_lock(wired):
    store = wired(FakeStore(lock_held=True))
    with pytest.raises(ArchiveLockError):
        run([("TESTARCH", Interval.I5)], store=store,
            fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    assert store.write_calls == []


# =====================================================================
# §5 — THE SHADOW COMPARE
# =====================================================================


def _stored(pairs):
    return {("TESTARCH", "i5"): {b.ts: bar_values(b) for b in pairs}}


def test_the_shadow_runs_after_the_fetch_and_before_the_write(wired):
    store = wired(FakeStore(stored=_stored(NIGHT_1[:2])))
    run([("TESTARCH", Interval.I5)], store=store,
        fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    assert store.names.index("bars_in_range") < store.names.index("upsert_bars")


def test_the_shadow_record_is_labelled_pre_write(wired, tmp_path):
    store = wired(FakeStore(stored=_stored(NIGHT_1[:2])))
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    (record,) = summary.shadow_records
    assert record.label == "pre-write"


@pytest.mark.parametrize("boom", [
    RuntimeError("the shadow read blew up"),
    TimeoutError("statement timeout"),
])
def test_a_shadow_failure_leaves_the_target_and_the_summary_identical(wired, boom, monkeypatch):
    clean = wired(FakeStore())
    expected = run([("TESTARCH", Interval.I5)], store=clean,
                   fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings(shadow_compare="off"))

    broken = wired(FakeStore())

    def _explode(*a, **k):
        raise boom

    monkeypatch.setattr(shadow_mod, "observe", _explode)
    actual = run([("TESTARCH", Interval.I5)], store=broken,
                 fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())

    assert broken.upserted == clean.upserted
    assert (actual.rows_written, actual.requests, actual.failures) == (
        expected.rows_written, expected.requests, expected.failures
    )
    assert actual.shadow_errors == 1
    assert expected.shadow_errors == 0


def test_a_slow_shadow_read_does_not_slow_the_write_path(wired, monkeypatch):
    """The read is bounded by its own `statement_timeout` (§10), and the
    target's upsert runs whatever the shadow did."""
    store = wired(FakeStore())
    seen = {}

    real = shadow_mod.observe

    def _slow(*a, **k):
        seen["called"] = True
        raise TimeoutError("canceling statement due to statement timeout")

    monkeypatch.setattr(shadow_mod, "observe", _slow)
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    assert seen["called"] and summary.rows_written == 3
    assert real is not None


def test_the_shadow_writes_nothing_to_the_database(wired):
    store = wired(FakeStore(stored=_stored(NIGHT_1)))
    run([("TESTARCH", Interval.I5)], store=store,
        fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    assert store.write_calls == ["upsert_bars"]
    assert store.written_progress == [] and store.written_incidents == []


def test_shadow_compare_off_skips_it_entirely(wired):
    store = wired(FakeStore())
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings(shadow_compare="off"))
    assert "bars_in_range" not in store.names
    assert summary.shadow_records == []
    assert "shadow" not in summary.job_result()


def test_the_shadow_reports_both_scopes(wired):
    """§5: the four-way comparison computed TWICE — the BOOTSTRAP scope
    (the whole export) and the STEADY-STATE scope (range (b))."""
    export = [bar(ts(3, 19, 55)), bar(ts(4, 19, 55)), bar(ts(17, 19, 55)), bar(ts(18, 19, 55))]
    store = wired(FakeStore(stored=_stored([export[0]])))
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): export}), cfg=settings())
    (record,) = summary.shadow_records
    assert record.bootstrap.candidates == 4
    # Range (b): today (09-18) + the two most recent completed session
    # dates the export carries (09-04, 09-17). 09-03 is below it.
    assert record.steady_state.candidates == 3
    assert record.bootstrap.already_stored_equal == 1
    assert record.steady_state.already_stored_equal == 0


def test_the_shadow_records_field_level_differences_after_normalisation(wired):
    export = [bar(ts(18, 19, 55), close="105.00", volume=2000)]
    store = wired(FakeStore(stored=_stored([bar(ts(18, 19, 55), close="100.00")])))
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): export}), cfg=settings())
    (record,) = summary.shadow_records
    assert record.bootstrap.would_withhold is True
    (difference,) = record.bootstrap.differing
    assert difference["ts"] == ts(18, 19, 55).isoformat()
    assert {f["field"] for f in difference["fields"]} == {"close", "volume"}
    assert next(f for f in difference["fields"] if f["field"] == "close")["stored"] == "100.0000"


def test_an_equal_rendering_is_not_recorded_as_a_difference(wired):
    export = [bar(ts(18, 19, 55), close="100.0")]
    store = wired(FakeStore(stored=_stored([bar(ts(18, 19, 55), close="100.0000")])))
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): export}), cfg=settings())
    (record,) = summary.shadow_records
    assert record.bootstrap.differing == []
    assert record.bootstrap.would_withhold is False


#: 00:30 UTC = 20:30 EDT the PRECEDING day. A run at the nightly hour
#: lands on a different UTC calendar day than the ET trading night it is
#: naming, and `FETCH_AT` (20:30 UTC = 16:30 ET, same date) never
#: exercises it — which is how tribunal round 1's F6 survived.
FETCH_AT_ET_NIGHT = datetime(2026, 9, 19, 0, 30, tzinfo=UTC)


def test_the_artifact_night_is_the_ET_trading_date_not_the_UTC_date(wired, tmp_path):
    """Tribunal round 1, F6.

    The nightly archiver runs at 20:30 ET. `night=clock().date()` took
    the `.date()` of a UTC instant, so on every such run the artifact
    was named for the NEXT calendar day — `2026-09-19.jsonl` for the
    night of 2026-09-18. Spec §5 names the file
    `data/archiver-shadow/<YYYY-MM-DD>.jsonl` and states no timezone;
    this round resolves it to ET per the verdict row (recorded as an
    ESCALATE — the desk may still rule otherwise).
    """
    store = wired(FakeStore(stored=_stored(NIGHT_1[:1])))
    run([("TESTARCH", Interval.I5)], store=store,
        fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings(),
        now=FETCH_AT_ET_NIGHT)

    et_night = shadow_mod.SHADOW_DIR / "2026-09-18.jsonl"
    utc_night = shadow_mod.SHADOW_DIR / "2026-09-19.jsonl"
    assert et_night.exists(), (
        "the artifact must be named for the ET trading night; files present: "
        f"{sorted(p.name for p in shadow_mod.SHADOW_DIR.glob('*.jsonl'))}"
    )
    assert not utc_night.exists(), (
        "the UTC calendar date of the run instant named the artifact"
    )


def test_the_artifact_is_json_lines_with_the_recorded_schema(wired, tmp_path):
    store = wired(FakeStore(stored=_stored(NIGHT_1[:1])))
    run([("TESTARCH", Interval.I5)], store=store,
        fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    # The RUN wrote it; the night is the clock's date, not the wall clock.
    path = shadow_mod.SHADOW_DIR / "2026-09-18.jsonl"
    assert path.exists()
    (line,) = path.read_text(encoding="utf-8").strip().splitlines()
    payload = json.loads(line)
    assert payload["label"] == "pre-write"
    assert payload["ticker"] == "TESTARCH" and payload["interval"] == "i5"
    for key in (
        "export_oldest", "export_newest", "raw_export_newest", "fetched",
        "poller_writable", "bootstrap", "steady_state", "fetch_started_at",
    ):
        assert key in payload, key
    for scope in ("bootstrap", "steady_state"):
        for key in (
            "candidates", "already_stored_equal", "differing", "incoming_only",
            "new", "late", "stored_only", "would_withhold",
        ):
            assert key in payload[scope], (scope, key)


def test_retention_deletes_only_nights_older_than_the_window(wired, tmp_path):
    directory = shadow_mod.SHADOW_DIR
    directory.mkdir(parents=True, exist_ok=True)
    for age in (0, 1, 29, 30, 31, 400):
        night = (FETCH_AT - timedelta(days=age)).date()
        (directory / f"{night.isoformat()}.jsonl").write_text("{}\n", encoding="utf-8")
    shadow_mod.apply_retention(retention_nights=30, today=FETCH_AT.date())
    kept = sorted(p.stem for p in directory.glob("*.jsonl"))
    assert kept == sorted(
        (FETCH_AT - timedelta(days=age)).date().isoformat() for age in (0, 1, 29)
    )


def test_shadow_report_says_which_differences_persisted_vanished_and_appeared():
    """§5: refreshed storage alone cannot show revision frequency, so the
    artifact is a RETAINED baseline and `shadow-report` reads across
    nights. Astra and Grok both required this."""
    nights = [
        ("2026-09-16", {("AAPL", "i5", "2026-09-16T13:30:00+00:00")}),
        ("2026-09-17", {("AAPL", "i5", "2026-09-16T13:30:00+00:00"),
                        ("MSFT", "i1", "2026-09-17T13:30:00+00:00")}),
        ("2026-09-18", {("MSFT", "i1", "2026-09-17T13:30:00+00:00"),
                        ("NVDA", "i5", "2026-09-18T13:30:00+00:00")}),
    ]
    verdict = shadow_mod.persisted_vanished_appeared(nights)
    assert verdict["persisted"] == [("MSFT", "i1", "2026-09-17T13:30:00+00:00")]
    assert verdict["vanished"] == [("AAPL", "i5", "2026-09-16T13:30:00+00:00")]
    assert verdict["appeared"] == [("NVDA", "i5", "2026-09-18T13:30:00+00:00")]


def test_the_shadow_aggregate_reaches_the_job_result(wired):
    export = [bar(ts(18, 19, 55), close="105.00")]
    store = wired(FakeStore(stored=_stored([bar(ts(18, 19, 55), close="100.00")])))
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): export}), cfg=settings())
    aggregate = summary.job_result()["shadow"]
    assert aggregate["targets_compared"] == 1
    assert aggregate["targets_errored"] == 0
    assert aggregate["would_withhold_by_interval"] == {"i5": 1}
    assert aggregate["would_withhold_poller_writable"] == 0
    assert aggregate["would_withhold_archiver_only"] == 1
    assert aggregate["volume_only"] == 0
    assert aggregate["any_ohlc"] == 1
    assert "late" in aggregate and "new" in aggregate


# =====================================================================
# §6, §7 — THE APPEND NIGHT
# =====================================================================


def append_run(store, export, *, progress=None, mode="full"):
    if progress:
        store.progress.update(progress)
    return run([("TESTARCH", Interval.I5)], store=store,
               fetch=fetcher({("TESTARCH", "i5"): export}),
               cfg=settings(write_mode="append"), mode=mode)


def test_append_bootstrap_offers_the_whole_eligible_export(wired):
    store = wired(FakeStore())
    summary = append_run(store, NIGHT_1 + [FORMING])
    assert store.upserted == []                              # never DO UPDATE
    assert [b.ts for b in store.inserted[0]] == [b.ts for b in NIGHT_1]
    assert FORMING not in store.inserted[0]                  # incomplete, excluded
    assert store.written_progress == [("TESTARCH", ts(18, 19, 55), summary.run_id)]
    assert summary.bootstraps == 1


def test_append_steady_state_offers_only_what_is_missing(wired):
    store = wired(FakeStore(stored=_stored(NIGHT_1[:2])))
    summary = append_run(store, NIGHT_1, progress={("TESTARCH", "i5"): ts(18, 19, 50)})
    assert [b.ts for b in store.inserted[0]] == [ts(18, 19, 55)]
    assert summary.rows_written == 1
    assert summary.bootstraps == 0


def test_a_withheld_target_inserts_nothing_freezes_progress_and_fails(wired):
    store = wired(FakeStore(stored=_stored([bar(ts(18, 19, 50), close="50.00")])))
    summary = append_run(store, NIGHT_1, progress={("TESTARCH", "i5"): ts(18, 19, 50)})
    assert store.inserted == []
    assert store.written_progress == []
    assert len(summary.failures) == 1
    assert "restated" in summary.failures[0]
    assert summary.restated_targets == 1


def test_a_withheld_targets_incident_is_persisted_after_the_rollback(wired):
    store = wired(FakeStore(stored=_stored([bar(ts(18, 19, 50), close="50.00")])))
    append_run(store, NIGHT_1, progress={("TESTARCH", "i5"): ts(18, 19, 50)})
    assert store.rollbacks == 1
    kinds = [k for k, _, _ in store.written_incidents]
    assert IncidentKind.RESTATED in kinds
    # ...in a SECOND transaction, opened after the first was rolled back.
    opens = [i for i, name in enumerate(store.names) if name == "open_incident"]
    transactions = [i for i, name in enumerate(store.names) if name == "target_transaction"]
    assert len(transactions) == 2
    assert opens[0] > transactions[1]


def test_a_gap_incident_is_written_before_progress_advances(wired):
    store = wired(FakeStore())
    summary = append_run(store, NIGHT_1, progress={("TESTARCH", "i5"): ts(4, 19, 55)})
    order = store.names
    assert order.index("open_incident") < order.index("upsert_progress")
    assert [k for k, _, _ in store.written_incidents] == [IncidentKind.GAP]
    assert summary.gap_targets == 1
    assert summary.degraded_targets == 1
    assert store.inserted, "the usable range is still appended"


def test_a_regression_fails_the_target_and_freezes_progress(wired):
    store = wired(FakeStore())
    summary = append_run(store, [bar(ts(17, 19, 55))],
                         progress={("TESTARCH", "i5"): ts(18, 19, 55)})
    assert store.inserted == [] and store.written_progress == []
    assert [k for k, _, _ in store.written_incidents] == [IncidentKind.REGRESSION]
    assert len(summary.failures) == 1


def test_inserted_zero_because_everything_was_stored_is_a_success(wired):
    store = wired(FakeStore(stored=_stored(NIGHT_1)))
    summary = append_run(store, NIGHT_1, progress={("TESTARCH", "i5"): ts(18, 19, 55)})
    assert summary.failures == []
    assert summary.rows_written == 0
    assert summary.degraded_targets == 0
    assert store.written_progress, "an accepted night still records progress"


def test_an_empty_export_fails_and_opens_an_empty_export_incident(wired):
    store = wired(FakeStore())
    summary = append_run(store, CollectorError("No data rows for TESTARCH/i5."))
    assert len(summary.failures) == 1
    assert [k for k, _, _ in store.written_incidents] == [IncidentKind.EMPTY_EXPORT]
    assert store.written_progress == []


def test_two_failed_nights_then_a_success_inserts_the_keys_still_in_the_window(wired):
    store = wired(FakeStore(progress={("TESTARCH", "i5"): ts(16, 19, 55)}))
    for _ in range(2):
        append_run(store, CollectorError("No data rows for TESTARCH/i5."))
    assert store.written_progress == []
    summary = append_run(store, NIGHT_1)
    assert {b.ts for b in store.inserted[0]} == {b.ts for b in NIGHT_1}
    assert summary.failures == []


def test_the_run_continues_after_a_failed_target(wired):
    store = wired(FakeStore())
    summary = run(
        [("TESTARCH", Interval.I5), ("THIN", Interval.I5)],
        store=store,
        fetch=fetcher({
            ("TESTARCH", "i5"): CollectorError("No data rows for TESTARCH/i5."),
            ("THIN", "i5"): [bar(ts(18, 19, 55), ticker="THIN")],
        }),
        cfg=settings(write_mode="append"),
    )
    assert len(summary.failures) == 1
    assert summary.requests == 2
    assert [b.ticker for batch in store.inserted for b in batch] == ["THIN"]


@pytest.mark.parametrize("scenario,expected", [
    ("failed", False),
    ("degraded", False),
    ("clean", True),
])
def test_failed_or_degraded_means_the_job_result_is_not_healthy(wired, scenario, expected):
    store = wired(FakeStore())
    if scenario == "failed":
        summary = append_run(store, CollectorError("No data rows for TESTARCH/i5."))
    elif scenario == "degraded":
        summary = append_run(store, NIGHT_1, progress={("TESTARCH", "i5"): ts(4, 19, 55)})
    else:
        summary = append_run(store, NIGHT_1)
    assert summary.healthy is expected


def test_an_upsert_night_stays_healthy_on_a_degraded_shaped_export(wired):
    """Mode isolation again: `degraded` is an APPEND-mode verdict. An
    `upsert` night has no such concept and must not invent one."""
    store = wired(FakeStore())
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    assert summary.healthy is True
    assert summary.degraded_targets == 0


def test_rows_written_is_inserted_in_append_mode(wired):
    store = wired(FakeStore(insert_rowcount=2))
    summary = append_run(store, NIGHT_1)
    assert summary.rows_written == 2, "§7: Rows Written = inserted in append mode"


def test_a_concurrent_conflict_is_counted_and_the_identity_closes(wired):
    store = wired(FakeStore(insert_rowcount=2))
    summary = append_run(store, NIGHT_1)
    (counts,) = summary.counts
    assert counts.inserted == 2 and counts.concurrent_conflicts == 1
    assert counts.incoming_only == counts.inserted + counts.concurrent_conflicts


def test_the_append_report_row_carries_the_append_columns(wired, tmp_path, monkeypatch):
    from cobalt.archiver import report as report_mod

    path = tmp_path / "archiver-runs.md"
    monkeypatch.setattr(report_mod, "REPORT_PATH", path)
    store = wired(FakeStore())
    summary = append_run(store, NIGHT_1)
    report_mod.append_run_report(summary)
    content = path.read_text()
    assert report_mod.APPEND_COLUMNS in content
    assert content.count("## Append mode") == 1
    row = [line for line in content.splitlines() if line.startswith("| 2026")][-1]
    assert row.count("|") == 15


def test_the_append_schema_break_is_written_once(wired, tmp_path, monkeypatch):
    from cobalt.archiver import report as report_mod

    path = tmp_path / "archiver-runs.md"
    monkeypatch.setattr(report_mod, "REPORT_PATH", path)
    for _ in range(3):
        store = wired(FakeStore())
        report_mod.append_run_report(append_run(store, NIGHT_1))
    content = path.read_text()
    assert content.count("## Append mode") == 1
    assert content.count(report_mod.APPEND_COLUMNS) == 1
    assert len([line for line in content.splitlines() if line.startswith("| 2026")]) == 3


def test_an_upsert_row_after_an_append_row_goes_back_to_its_own_table(wired, tmp_path, monkeypatch):
    """A markdown table cannot change its column count in place, and a
    rollback to `upsert` must not write 8-column rows under the 14-column
    header."""
    from cobalt.archiver import report as report_mod

    path = tmp_path / "archiver-runs.md"
    monkeypatch.setattr(report_mod, "REPORT_PATH", path)
    report_mod.append_run_report(append_run(wired(FakeStore()), NIGHT_1))
    store = wired(FakeStore())
    report_mod.append_run_report(
        run([("TESTARCH", Interval.I5)], store=store,
            fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings())
    )
    content = path.read_text()
    assert content.count("## Append mode") == 1
    assert content.count("## Back to upsert mode") == 1
    rows = [line for line in content.splitlines() if line.startswith("| 2026")]
    assert rows[0].count("|") == 15 and rows[1].count("|") == 9


# =====================================================================
# R34 "B" — THE BACKFILL IS BOUNDED OUT OF THE PREMARKET WINDOW
# (`cto-2026-09-19.md` §4 R34, 2026-09-19)
#
# The rebase onto post-P4 `main` made L53's shared gate fire on the
# archiver: with `replay` registered, the inventory at 04:00 ET reached
# 51.00 rpm against `radar.finviz_max_rpm = 50`, because the backfill
# declared `window=None` — UNBOUNDED, counted against every window.
# Dejan ruled B: the CEILING STAYS AT 50 and the backfill is bounded
# out of 04:00-09:30 ET. These tests are that bound.
# =====================================================================

#: 2026-09-18 22:00 ET — outside the premarket bound AND clear of every
#: scheduled consumer's window (radar 04:00-20:00, archiver 20:30-21:10,
#: replay 21:10-21:35), so this is an hour a backfill may actually run.
BACKFILL_AT = datetime(2026, 9, 19, 2, 0, tzinfo=UTC)
#: 2026-09-18 08:00 ET — inside 04:00-09:30, the window R34 closed.
PREMARKET_AT = datetime(2026, 9, 18, 12, 0, tzinfo=UTC)
#: 2026-09-18 03:50 ET — outside it by 10 minutes, but a long enough
#: backfill RUNS into it.
JUST_BEFORE_PREMARKET_AT = datetime(2026, 9, 18, 7, 50, tzinfo=UTC)


def _never_fetch():
    async def _fetch(*args, **kwargs):
        raise AssertionError("Finviz was contacted despite the premarket bound")

    return _fetch


def test_a_backfill_inside_the_premarket_window_is_refused_before_any_request(wired):
    """R34 "B", the loud half: 04:00-09:30 ET is closed to the backfill,
    and the refusal happens before the lock, the store and the token —
    so no request is sent and nothing is written."""
    store = wired(FakeStore())
    with pytest.raises(runner_mod.BackfillWindowRefused) as e:
        run([("TESTARCH", Interval.I5)], store=store, fetch=_never_fetch(),
            cfg=settings(), mode="backfill:TESTARCH", now=PREMARKET_AT)
    message = str(e.value)
    assert "04:00-09:30 ET" in message, message
    assert "R34" in message and "cto-2026-09-19" in message, message
    assert store.names == [], "the refusal must come before the run lock"
    assert store.write_calls == []


def test_a_backfill_that_would_RUN_into_the_premarket_window_is_refused(wired):
    """The bound is on the run's WINDOW, not on its first instant: a
    backfill that starts at 03:50 and paces 40 minutes of requests is
    inside 04:00-09:30 for most of its life."""
    targets = [("TESTARCH", Interval.I5)] * 2000
    store = wired(FakeStore())
    with pytest.raises(runner_mod.BackfillWindowRefused) as e:
        run(targets, store=store, fetch=_never_fetch(), cfg=settings(),
            mode="backfill:TESTARCH", now=JUST_BEFORE_PREMARKET_AT)
    assert "04:00-09:30 ET" in str(e.value)
    assert store.names == []


def test_the_backfill_declares_the_window_it_actually_runs_in(wired):
    """The declared `DemandWindow` is not a label: it is `[now, now +
    len(targets) x GENTLE_SLEEP_SECONDS)` in ET, the interval the runner
    then enforces. A window the runner did not enforce would be a lie to
    the shared demand model."""
    window = runner_mod._backfill_window([("TESTARCH", Interval.I5)] * 100, BACKFILL_AT)
    assert window.describe() == "22:00-22:02 ET", window.describe()
    assert window.overlaps(runner_mod._premarket_window()) is False


def test_a_backfill_outside_the_premarket_window_is_allowed_under_the_ceiling(wired):
    """The quiet half: at an hour no scheduled consumer holds, the same
    backfill runs and the L53 total stays at or under the ceiling."""
    demand = runner_mod._check_demand(
        [("TESTARCH", Interval.I5)], "backfill:TESTARCH", now=lambda: BACKFILL_AT
    )
    assert demand is not None
    assert demand.ceiling == 50
    assert demand.peak_rpm <= 50, demand.describe()
    assert "backfill" in demand.counted

    store = wired(FakeStore())
    summary = run([("TESTARCH", Interval.I5)], store=store,
                  fetch=fetcher({("TESTARCH", "i5"): NIGHT_1}), cfg=settings(),
                  mode="backfill:TESTARCH", now=BACKFILL_AT)
    assert summary.mode == "backfill:TESTARCH"
    assert store.write_calls == ["upsert_bars"]


def test_the_nightly_full_run_is_untouched_by_the_backfill_bound():
    """R34 leaves the 20:30 `full` run alone. It is the registry's own
    `archiver` consumer, it is not the backfill, and the premarket bound
    does not apply to it — not even when the clock says 08:00 ET."""
    demand = runner_mod._check_demand(
        [("TESTARCH", Interval.I5)], "full", now=lambda: PREMARKET_AT
    )
    assert demand is not None
    assert demand.subject == "archiver"
    assert demand.peak_rpm <= 50, demand.describe()


def test_the_finviz_ceiling_is_still_fifty():
    """R34 "B" changed the backfill's window and NOTHING else. The
    ceiling is Dejan's (L53) and it did not move."""
    from cobalt.taxonomy.loader import load_tunables

    assert int(load_tunables().by_key["radar.finviz_max_rpm"].value) == 50


def test_the_premarket_bound_is_read_from_the_session_tunables():
    """Config-as-code (L10): 04:00 and 09:30 are `session.premarket_open`
    and `session.rth_open`, not two literals in the runner."""
    from cobalt.taxonomy.loader import load_tunables

    tunables = load_tunables().by_key
    window = runner_mod._premarket_window()
    assert window.describe() == (
        f"{tunables['session.premarket_open'].value}-{tunables['session.rth_open'].value} ET"
    )
