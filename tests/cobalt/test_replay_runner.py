"""S2-P4 STEP-4 — `com.cobalt.replay`: precondition, deadline, ordered steps
with per-side commits, dry run, and the formation adapter.

The run is driven over the hub-cut real-shape fixtures through fake stores
that record every call, so "writes nothing" and "earlier steps stand" are
asserted on the calls themselves. The fixture day is an EDT day shifted to
2026-02-10 (hub report §STEP-1), so its session bounds are passed as the
anchor's real 09:30/16:00 EDT instants rather than read from a February
calendar.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
import types
from datetime import date, datetime, time, timedelta, timezone
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.archiver.models import Bar, Interval
from cobalt.jobs.config import load_job_registry
from cobalt.replay import cli as cli_mod
from cobalt.replay import runner as runner_mod
from cobalt.replay.line import SECTION, UNIT
from cobalt.replay.models import (
    FORMATION_UNAVAILABLE_LINE,
    CardCandidate,
    PositionSpan,
    ReplayError,
    StepFailed,
    StoredMover,
    TransitionRow,
)
from cobalt.replay.runner import (
    DeadlineExceeded,
    ReplayDeps,
    archiver_precondition,
    formation_replay,
    replay_deadline,
    run_nightly,
)
from cobalt.session.clock import ET
from cobalt.taxonomy.loader import load_tunables

FIX = Path(__file__).resolve().parents[1] / "fixtures"
DAY = date(2026, 2, 10)
RTH_OPEN = datetime(2026, 2, 10, 13, 30, tzinfo=timezone.utc)
CLOSE = datetime(2026, 2, 10, 20, 0, tzinfo=timezone.utc)
#: The replay "tonight": 21:10 ET on the fixture day (S2-P4 R17).
NOW = datetime(2026, 2, 10, 21, 10, tzinfo=ET)

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: Postgres env settings not available",
)


# =====================================================================
# Precondition (R3, R1-15)
# =====================================================================


def _row(state="done", exit_code=0, started=None, finished=None):
    started = started or datetime(2026, 2, 10, 20, 30, 2, tzinfo=ET)
    return {"label": "com.cobalt.archiver", "state": state, "exit_code": exit_code, "started_at": started,
            "finished_at": finished or started + timedelta(minutes=23)}


REGISTRY = load_job_registry()


def test_replay_refuses_when_archiver_not_done_today():
    with pytest.raises(ReplayError, match="archiver not done"):
        archiver_precondition(_row(state="failed", exit_code=1), trade_date=DAY, now=NOW, registry=REGISTRY)
    deps, calls = fake_deps(job_row=_row(state="running", exit_code=None))
    with pytest.raises(ReplayError, match="archiver not done"):
        run_nightly(DAY, dry_run=False, deps=deps)
    assert calls == ["job_store.get"]                 # refused before any other read or write


@pytest.mark.parametrize("case,row", [
    ("previous-day done", _row(started=datetime(2026, 2, 9, 20, 30, 2, tzinfo=ET))),
    ("same-day early manual run", _row(started=datetime(2026, 2, 10, 16, 35, tzinfo=ET))),
    ("running", _row(state="running", exit_code=None)),
    ("failed", _row(state="failed", exit_code=1)),
    ("done with a nonzero exit", _row(exit_code=3)),
    ("incoherent times", _row(finished=datetime(2026, 2, 10, 20, 0, tzinfo=ET))),
    ("absent row", None),
])
def test_r1_15_precondition_refuses(case, row):
    with pytest.raises(ReplayError, match="archiver not done"):
        archiver_precondition(row, trade_date=DAY, now=NOW, registry=REGISTRY)


def test_r1_15_tonights_occurrence_passes_across_the_utc_date_line():
    # 20:35 ET is 01:35 UTC the NEXT day: the ET date is what counts.
    started = datetime(2026, 2, 11, 1, 35, tzinfo=timezone.utc)
    detail = archiver_precondition(_row(started=started), trade_date=DAY, now=NOW, registry=REGISTRY)
    assert "tonight" in detail
    # and a run stamped 20:35 UTC on the trade date (15:35 ET) is early, not tonight's
    with pytest.raises(ReplayError, match="archiver not done"):
        archiver_precondition(_row(started=datetime(2026, 2, 10, 20, 35, tzinfo=timezone.utc)),
                              trade_date=DAY, now=NOW, registry=REGISTRY)


# =====================================================================
# Deadline (R1-16)
# =====================================================================


def test_r1_16_deadline_is_the_backup_less_the_margin_and_the_margin_itself_refuses():
    tunables = load_tunables().by_key
    deadline = replay_deadline(NOW, registry=REGISTRY, tunables=tunables)
    assert deadline == datetime(2026, 2, 10, 21, 35, tzinfo=ET)
    with pytest.raises(DeadlineExceeded, match="backup"):
        replay_deadline(datetime(2026, 2, 10, 21, 36, tzinfo=ET), registry=REGISTRY, tunables=tunables)
    assert replay_deadline(datetime(2026, 2, 10, 22, 30, tzinfo=ET), registry=REGISTRY, tunables=tunables) is None


def test_r1_16_a_slow_but_heartbeating_collector_is_cut_at_the_deadline_with_no_vault_write():
    class Slow(FakeCollector):
        async def exports(self, **kw):
            await asyncio.sleep(5)
            return await super().exports(**kw)

    clock = Clock(datetime(2026, 2, 10, 21, 34, 59, 900000, tzinfo=ET))
    deps, calls = fake_deps(collector=Slow(), now=clock)
    with pytest.raises(StepFailed) as failed:
        run_nightly(DAY, dry_run=False, deps=deps, live=True)
    assert failed.value.step == "movers"
    assert isinstance(failed.value.error, DeadlineExceeded)
    assert not any(c.startswith("writer") for c in calls)


def test_r1_16_a_deadline_passing_between_steps_stops_before_the_vault_write():
    clock = Clock(NOW)
    deps, calls = fake_deps(now=clock)
    original = deps.missed.reconcile

    def reconcile_then_late(**kw):
        counts = original(**kw)
        if kw["kind"] == "card":
            clock.at = datetime(2026, 2, 10, 21, 36, tzinfo=ET)
        return counts

    deps.missed.reconcile = reconcile_then_late
    with pytest.raises(StepFailed) as failed:
        run_nightly(DAY, dry_run=False, deps=deps)
    assert failed.value.step in {"formations", "line"}
    assert isinstance(failed.value.error, DeadlineExceeded)
    assert not any(c.startswith("writer") for c in calls)


# =====================================================================
# The run
# =====================================================================


def test_nightly_report_lists_misses_with_the_gate_or_variable_that_excluded_them():
    deps, calls = fake_deps()
    result = run_nightly(DAY, dry_run=False, deps=deps)
    printed = "\n".join(deps.printed)
    assert "MISS card 302 CRWD short excluded_by=unarmed cf_r=-1.0139" in printed
    assert "MISS card 308 MU short excluded_by=rule_10 cf_r=-1.0000" in printed
    assert "MISS mover CTNT excluded_by=not_in_any_source" in printed
    assert "MISS mover DAIC excluded_by=config_cap" in printed
    assert (result.card_misses, result.no_trigger, result.input_stale) == (5, 1, 0)
    assert result.steps_done == ["movers", "cards", "formations", "line"]
    assert result.line_action == "updated"
    assert calls.index("movers_store.reconcile") < calls.index("missed.reconcile:mover") < \
        calls.index("missed.reconcile:card") < calls.index("writer.upsert_unit")
    line = deps.written[-1]
    assert line.startswith("Misses 2026-02-10: cards 5 (unarmed 4 · passed 0 · not_filled 0 · window 0 · rule_10 1)")
    assert "formations: unavailable until S2-P2" in line


def test_step_failure_names_step_and_earlier_steps_stand():
    deps, calls = fake_deps()

    def broken(day):
        raise RuntimeError("card read failed")

    deps.missed.candidates = broken
    with pytest.raises(StepFailed, match="step cards failed") as failed:
        run_nightly(DAY, dry_run=False, deps=deps)
    result = failed.value.result
    assert result.failed_step == "cards"
    assert result.steps_done == ["movers"]
    assert "movers_store.reconcile" in calls and "missed.reconcile:mover" in calls   # committed, standing
    assert "missed.reconcile:card" not in calls and not any(c.startswith("writer") for c in calls)


def test_r2_3_a_retry_after_a_commit_boundary_resumes_idempotently():
    deps, calls = fake_deps()
    deps.missed.candidates_error = RuntimeError("killed after the SYSTEM commit")
    with pytest.raises(StepFailed):
        run_nightly(DAY, dry_run=False, deps=deps)
    deps.missed.candidates_error = None
    result = run_nightly(DAY, dry_run=False, deps=deps)
    assert result.reconcile["mover"].unchanged == result.mover_misses       # the mover rows stood
    assert result.reconcile["mover"].inserted == 0
    assert deps.movers_store.inserted_total == result.movers                # no second copy


def test_archive_failures_are_counted_and_fail_the_job_at_the_end():
    deps, calls = fake_deps(collector=FakeCollector(fail={"CTNT"}))
    with pytest.raises(ReplayError, match="1 movers archive failure") as failed:
        run_nightly(DAY, dry_run=False, deps=deps, live=True)
    assert failed.value.result.steps_done == ["movers", "cards", "formations", "line"]
    assert failed.value.result.archive_failures == 1


def test_benchmark_absent_fails_the_movers_step_loud():
    deps, calls = fake_deps(settings={})
    with pytest.raises(StepFailed, match="step movers failed.*radar.benchmark"):
        run_nightly(DAY, dry_run=False, deps=deps)


def test_drc_note_absent_fails_the_line_step_and_creates_nothing():
    deps, calls = fake_deps(drc_missing=True)
    with pytest.raises(StepFailed, match="DRC note absent — prefill-drc owns creation") as failed:
        run_nightly(DAY, dry_run=False, deps=deps)
    assert failed.value.step == "line"
    assert not any(c.startswith("writer") for c in calls)


# =====================================================================
# Formations (R4, R1-21)
# =====================================================================


def test_formation_replay_unavailable_logs_exact_line_no_rows(monkeypatch):
    printed: list[str] = []
    monkeypatch.delitem(sys.modules, "cobalt.radar.evaluate_cli", raising=False)
    status, rows = formation_replay(DAY, out=printed.append)
    assert status == "unavailable"
    assert rows == []
    assert printed == [FORMATION_UNAVAILABLE_LINE]
    assert FORMATION_UNAVAILABLE_LINE == "trade_def replay: not available until S2-P2"


def test_r1_21_a_present_but_incompatible_p2_fails_loud(monkeypatch):
    from pydantic import BaseModel

    class ReplayFormation(BaseModel):          # P2's shipped fields (recorded in the build report)
        seen_at: datetime
        ticker: str
        slug: str
        direction: str
        trigger: str
        stop: str
        formed_bar_ts: datetime

    module = types.ModuleType("cobalt.radar.evaluate_cli")
    module.ReplayFormation = ReplayFormation
    module.replay_formations = lambda *a, **k: None
    monkeypatch.setitem(sys.modules, "cobalt.radar.evaluate_cli", module)
    with pytest.raises(ReplayError, match="incompatible.*membership_id"):
        formation_replay(DAY, out=lambda line: None)


# =====================================================================
# Dry run (R1-17) — through the CLI
# =====================================================================


def test_dry_run_through_the_cli_writes_nothing_and_prints_rows_and_the_line_diff(monkeypatch, capsys, tmp_path):
    deps, calls = fake_deps()
    seen = {}

    def build(*, dry_run):
        seen["dry_run"] = dry_run
        return deps

    monkeypatch.setattr(cli_mod, "default_deps", build)

    def no_job_row(*a, **k):
        raise AssertionError("a dry run touched the jobs table")

    import cobalt.jobs.wrapper as wrapper

    monkeypatch.setattr(wrapper, "job_run", no_job_row)
    monkeypatch.setattr(cli_mod, "now_et", lambda: NOW)
    args = cli_mod.build_parser().parse_args(["nightly", "--date", "2026-02-10", "--dry-run"])
    args.func(args)
    out = capsys.readouterr().out
    assert seen["dry_run"] is True
    assert "MISS card 302 CRWD short excluded_by=unarmed" in out
    assert "[DRY-RUN]" in out and f"+<!-- cobalt:unit {UNIT} -->" in out
    writes = [c for c in calls if c.split(":")[0] in {
        "movers_store.reconcile", "movers_store.mark_bars_archived", "missed.reconcile", "bar_store.upsert_bars",
        "collector.cache", "ensure_schema"}]
    assert writes == []
    assert deps.writer_dry_runs == [True]
    assert deps.drc.read_text() == deps.drc_before


# =====================================================================
# Side roles on each phase (R2-3) — hub, cobalt_dev
# =====================================================================


@requires_db
def test_r2_3_each_phase_runs_on_its_own_side_and_the_wrong_side_is_refused(real_connect):
    import psycopg

    from cobalt import db

    system = real_connect(side=db.Side.SYSTEM)
    user = real_connect(side=db.Side.USER)
    assert user.execute("SELECT count(*) FROM system.movers_daily").fetchone() is not None
    with pytest.raises(psycopg.Error):
        system.execute('SELECT count(*) FROM "user".missed')
    system.rollback()
    with pytest.raises(psycopg.Error):
        user.execute("INSERT INTO system.movers_daily (trade_date, side, rank, ticker, change_pct, "
                     "export_sha256, fetched_at, replay_run_id) VALUES "
                     "('2026-02-10', 'gainers', 1, 'X', 1, 'x', now(), 'r')")
    user.rollback()


def test_registry_and_ops_carry_the_replay_job_with_matching_schedule():
    import plistlib

    spec = REGISTRY.spec("com.cobalt.replay")
    assert (spec.kind.value, spec.timeout_s, spec.schedule.at, sorted(spec.schedule.weekdays)) == (
        "one-shot", 1800, "21:10", [1, 2, 3, 4, 5])
    data = plistlib.loads(spec.plist_path.read_bytes())
    assert data["EnvironmentVariables"]["COBALT_ENV"] == "production"
    assert data["EnvironmentVariables"]["COBALT_VAULT_PATH"] == "/Users/cobalt/Vault/Think"
    assert data["ProgramArguments"][-3:] == ["cobalt", "replay", "nightly"]
    assert {(e["Hour"], e["Minute"]) for e in data["StartCalendarInterval"]} == {(21, 10)}


# =====================================================================
# fakes
# =====================================================================


class Clock:
    def __init__(self, at):
        self.at = at

    def __call__(self):
        return self.at


def _load_bars():
    return [Bar(ticker=b["ticker"], interval=Interval.I1, ts=datetime.fromisoformat(b["ts"]), open=Decimal(b["open"]),
                high=Decimal(b["high"]), low=Decimal(b["low"]), close=Decimal(b["close"]), volume=b["volume"])
            for b in json.loads((FIX / "replay" / "bars-day.real-shape.json").read_text())]


def _load_cards():
    raw = json.loads((FIX / "replay" / "cards-day.real-shape.json").read_text())
    trs = [TransitionRow(card_id=t["card_id"], from_state=t["from_state"], to_state=t["to_state"],
                         at=datetime.fromisoformat(t["at"])) for t in raw["transitions"]]
    filled = {t.card_id for t in trs if t.to_state == "FILLED"}
    candidates = [
        CardCandidate(id=s["id"], ticker=s["ticker"], direction=s["direction"], entry=Decimal(s["entry"]),
                      stop=Decimal(s["stop"]), created_at=datetime.fromisoformat(s["created_at"]),
                      transitions=tuple(t for t in trs if t.card_id == s["id"]))
        for s in raw["sizings"] if s["id"] not in filled
    ]
    positions = []
    for cid in sorted(filled):
        f = min(t.at for t in trs if t.card_id == cid and t.to_state == "FILLED")
        c = [t.at for t in trs if t.card_id == cid and t.to_state == "CLOSED"]
        positions.append(PositionSpan(card_id=cid, filled_at=f, closed_at=min(c) if c else None))
    return candidates, positions


class FakeCollector:
    def __init__(self, fail=()):
        self.fail = set(fail)
        self.calls = None

    async def exports(self, *, top_n, now, cache, trade_date=None):
        from cobalt.replay.movers import load_radar_config, parse_movers

        self.calls.append("collector.exports")
        if cache:
            self.calls.append("collector.cache")
        return [parse_movers((FIX / "replay" / f"movers-{side}.real-shape.csv").read_bytes(), side=side,
                             top_n=top_n, content_type="text/csv", config=load_radar_config(),
                             fetched_at=now, source="live") for side in ("gainers", "losers")]

    async def bars(self, tickers, *, top_n):
        self.calls.append("collector.bars")
        return ({t: [] for t in tickers if t not in self.fail}, {t: "CollectorError: 429" for t in tickers if t in self.fail})


def fake_deps(*, job_row="default", settings="default", collector=None, now=None, drc_missing=False):
    import tempfile

    from cobalt.prefill.drc import _render_template
    from cobalt.replay.cards import MissedStore
    from cobalt.replay.models import ReconcileCounts
    from cobalt.replay.movers import load_radar_config

    calls: list[str] = []
    bars = _load_bars()
    candidates, positions = _load_cards()
    membership = json.loads((FIX / "replay" / "membership-day.real-shape.json").read_text())["membership"]

    class JobStore:
        def get(self, label):
            calls.append("job_store.get")
            return _row() if job_row == "default" else job_row

    class Missed:
        candidates_error = None

        def __init__(self):
            self.current_rows: dict[str, dict[tuple, dict]] = {"card": {}, "mover": {}}

        def candidates(self, day):
            calls.append("missed.candidates")
            if self.candidates_error:
                raise self.candidates_error
            return candidates

        def positions(self, day):
            calls.append("missed.positions")
            return positions

        def reconcile(self, *, run_id, trade_date, kind, rows, before_commit=None):
            calls.append(f"missed.reconcile:{kind}")
            prior = self.current_rows[kind]
            unchanged = sum(1 for r in rows if r.subject() in prior and prior[r.subject()]["inputs_sha256"] == r.inputs_sha256)
            self.current_rows[kind] = {r.subject(): {**r.model_dump(), "replay_run_id": run_id} for r in rows}
            return ReconcileCounts(inserted=len(rows) - unchanged, unchanged=unchanged)

        def current(self, trade_date, kind=None):
            calls.append(f"missed.current:{kind}")
            return list(self.current_rows[kind].values())

    class Movers:
        inserted_total = 0

        def __init__(self):
            self.rows: dict[tuple, StoredMover] = {}

        def reconcile(self, *, run_id, trade_date, exports):
            calls.append("movers_store.reconcile")
            wanted = {}
            for export in exports:
                for row in export.rows:
                    key = (export.side, row.ticker, row.rank, row.change_pct, export.export_sha256)
                    existing = next((m for k, m in self.rows.items() if k == key), None)
                    if existing is None:
                        Movers.inserted_total += 1
                        existing = StoredMover(id=len(self.rows) + 1, trade_date=trade_date, side=export.side,
                                               rank=row.rank, ticker=row.ticker, change_pct=row.change_pct,
                                               asset_type=row.asset_type, volume=row.volume, rvol=row.rvol,
                                               export_sha256=export.export_sha256, fetched_at=export.fetched_at)
                    wanted[key] = existing
            self.rows = wanted
            return list(wanted.values())

        def mark_bars_archived(self, ids):
            calls.append("movers_store.mark_bars_archived")

    class Bars:
        def bars_between(self, ticker, interval, start, end):
            calls.append("bar_store.bars_between")
            return [b for b in bars if b.ticker == ticker and start <= b.ts < end]

        def upsert_bars(self, rows):
            calls.append("bar_store.upsert_bars")
            return len(rows)

    class Radar:
        def members_for_day(self, pool_key, day):
            calls.append("radar_store.members_for_day")
            return membership

    folder = Path(tempfile.mkdtemp())
    drc = folder / "DRC-2026-02-10.md"
    if not drc_missing:
        drc.write_text(_render_template({"date_str": "2026-02-10", "risk_parameters_line": "x",
                                         "tickers_unit": "y", "rules_check_block": "z"}))

    from test_replay_line import MemoryWriteStore

    collector = collector or FakeCollector()
    collector.calls = calls
    deps = ReplayDeps(
        job_store=JobStore(), registry=REGISTRY, tunables=load_tunables().by_key,
        now=now or Clock(NOW), session_bounds=lambda day: (RTH_OPEN, CLOSE),
        settings_values=lambda: ({"radar.benchmark": {"top_n": 60, "min_move_pct": 30}} if settings == "default" else settings),
        missed=Missed(), movers_store=Movers(), bar_store=Bars(), radar_store=Radar(),
        radar_config=load_radar_config(), collector_factory=None, cache_root=folder,
        writer_factory=None, drc_path=lambda day: drc, out=None, ceiling=40,
    )
    deps.printed = []
    deps.written = []
    deps.writer_dry_runs = []
    deps.drc = drc
    deps.drc_before = drc.read_text() if drc.exists() else None
    deps.out = lambda line: (deps.printed.append(line), print(line))

    async def factory():
        return collector

    deps.collector_factory = factory

    # retained exports for a historical --date run, like production's cache
    day_dir = folder / DAY.isoformat()
    day_dir.mkdir()
    for side in ("gainers", "losers"):
        (day_dir / f"movers-{side}-210500.csv").write_bytes((FIX / "replay" / f"movers-{side}.real-shape.csv").read_bytes())

    from cobalt.vaultwrite import VaultWriter

    store = MemoryWriteStore()

    class RecordingWriter(VaultWriter):
        def upsert_unit(self, path, section, unit_id, body, **kw):
            calls.append("writer.upsert_unit")
            deps.written.append(body)
            return super().upsert_unit(path, section, unit_id, body, **kw)

    def writer_factory(dry_run):
        deps.writer_dry_runs.append(dry_run)
        return RecordingWriter("replay.nightly", store=store, dry_run=dry_run)

    deps.writer_factory = writer_factory
    return deps, calls
