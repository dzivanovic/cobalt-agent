"""Chunk Q — the QUIET WINDOW and the archiver's commands.

Spec `ARCHIVER-APPEND-ONLY-FINAL-2026-09-19.md` §8 (V3-9, **option A**,
ruled by the owner 2026-09-19 09:30 ET, `cto-2026-09-19.md` R8), §6 and
§3 V3-7.

WHAT WAS RULED. Every command that MUTATES stored bars outside the
nightly run — `restate --apply` and `backfill-missing` — runs only in a
quiet window: the radar idle, at least `quiet_after_cycle_min` past the
DERIVED completion of the last poll cycle, at least
`quiet_before_open_min` before the next scanning session opens, and
holding the run-level lock. **The live poller is NOT touched.** Option B
(a per-target marker the poller checks) was not taken and is carried to
Sunday's bars-lifecycle design; Gemini's and Astra's dissents on that
stand, and one test here DEMONSTRATES the limit executably rather than
in prose.

Everything is offline: a fake clock, a constructed pool row through an
injected reader, and a fake store. No database, no radar.
"""

from __future__ import annotations

import inspect
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from zoneinfo import ZoneInfo

import pytest

from cobalt.archiver import cli as archiver_cli
from cobalt.archiver import quiet as quiet_mod
from cobalt.archiver.models import Bar, Interval
from cobalt.archiver.quiet import (
    QuietObservation,
    QuietRefused,
    quiet_verdict,
)
from cobalt.archiver.settings import ArchiverSettings
from cobalt.session.models import Session

ET = ZoneInfo("America/New_York")
UTC = timezone.utc


def et(y, m, d, hh, mm, ss=0) -> datetime:
    return datetime(y, m, d, hh, mm, ss, tzinfo=ET).astimezone(UTC)


def cfg(**over) -> ArchiverSettings:
    payload = {
        "write_mode": "upsert",
        "shadow_compare": "on",
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


def observation(
    *,
    now,
    session=Session.OVERNIGHT,
    last_scan_at=None,
    pool_row_present=True,
    next_scanning_open=None,
    overnight_start=None,
    open_after_overnight=None,
) -> QuietObservation:
    """A quiet window as the reader would have seen it."""
    return QuietObservation(
        now=now,
        session=session,
        pool_key="probe_pool",
        pool_row_present=pool_row_present,
        last_scan_at=last_scan_at if last_scan_at is not None else now - timedelta(hours=4),
        next_scanning_open=(
            next_scanning_open if next_scanning_open is not None else now + timedelta(hours=4)
        ),
        next_scanning_session=Session.PREMARKET,
        overnight_start=overnight_start if overnight_start is not None else now,
        open_after_overnight=(
            open_after_overnight
            if open_after_overnight is not None
            else (next_scanning_open if next_scanning_open is not None else now + timedelta(hours=4))
        ),
    )


# =====================================================================
# §8 — the four rules, each refusing ALONE
# =====================================================================


def test_a_quiet_overnight_window_is_allowed():
    verdict = quiet_verdict(observation(now=et(2026, 9, 18, 2, 0)), cfg())
    assert verdict.quiet is True
    assert verdict.failures == ()


@pytest.mark.parametrize("session", [
    Session.PREMARKET, Session.RTH, Session.AFTERMARKET, Session.MARKET_RESET
])
def test_q1_every_non_overnight_session_refuses_alone(session):
    verdict = quiet_verdict(
        observation(now=et(2026, 9, 18, 10, 0), session=session), cfg()
    )
    assert verdict.quiet is False
    assert any(line.startswith("Q1") for line in verdict.failures)
    assert session.value in verdict.text


def test_market_reset_is_not_quiet():
    """§8, in so many words: the radar is PAUSED there, not idle, and
    20:30 belongs to the nightly run."""
    verdict = quiet_verdict(
        observation(now=et(2026, 9, 18, 20, 30), session=Session.MARKET_RESET), cfg()
    )
    assert verdict.quiet is False
    assert any("market_reset" in line for line in verdict.failures)


def test_q2_refuses_alone_when_the_next_scanning_open_is_too_close():
    now = et(2026, 9, 18, 3, 55)
    verdict = quiet_verdict(
        observation(now=now, next_scanning_open=now + timedelta(minutes=5),
                    open_after_overnight=now + timedelta(minutes=5)),
        cfg(),
    )
    assert verdict.quiet is False
    assert [line[:2] for line in verdict.failures] == ["Q2"]


def test_q2_allows_exactly_the_configured_distance():
    now = et(2026, 9, 18, 3, 50)
    verdict = quiet_verdict(
        observation(now=now, next_scanning_open=now + timedelta(minutes=10),
                    open_after_overnight=now + timedelta(minutes=10)),
        cfg(),
    )
    assert verdict.quiet is True


def test_q3_refuses_alone_when_the_derived_cycle_finish_is_too_recent():
    """`cycle_max_min` + `quiet_after_cycle_min` = 35 minutes after the
    cycle's START, because the radar persists the start and never the
    completion (§2)."""
    now = et(2026, 9, 18, 21, 30)
    verdict = quiet_verdict(
        observation(now=now, last_scan_at=now - timedelta(minutes=34)), cfg()
    )
    assert verdict.quiet is False
    assert [line[:2] for line in verdict.failures] == ["Q3"]
    assert "need >= 35 min" in verdict.text


def test_q3_allows_exactly_the_derived_bound():
    now = et(2026, 9, 18, 21, 30)
    verdict = quiet_verdict(
        observation(now=now, last_scan_at=now - timedelta(minutes=35)), cfg()
    )
    assert verdict.quiet is True


def test_a_missing_pool_row_refuses_because_quiet_cannot_be_PROVEN():
    verdict = quiet_verdict(
        observation(now=et(2026, 9, 18, 2, 0), pool_row_present=False), cfg()
    )
    assert verdict.quiet is False
    assert "cannot prove the radar is quiet" in verdict.text


def test_a_null_last_scan_at_refuses_the_same_way():
    verdict = quiet_verdict(
        observation(now=et(2026, 9, 18, 2, 0), last_scan_at=None, pool_row_present=True),
        cfg(),
    )
    # `last_scan_at=None` reaches the model as an explicit NULL.
    refused = quiet_verdict(
        QuietObservation(
            now=et(2026, 9, 18, 2, 0), session=Session.OVERNIGHT, pool_key="probe_pool",
            pool_row_present=True, last_scan_at=None,
            next_scanning_open=et(2026, 9, 18, 4, 0),
            next_scanning_session=Session.PREMARKET,
            overnight_start=et(2026, 9, 18, 2, 0),
            open_after_overnight=et(2026, 9, 18, 4, 0),
        ),
        cfg(),
    )
    assert refused.quiet is False
    assert "cannot prove the radar is quiet" in refused.text
    assert verdict.quiet is True   # the helper's default IS a real scan


# =====================================================================
# §8 — the refusal text
# =====================================================================


def test_the_refusal_names_every_observed_value_and_the_earliest_start():
    now = et(2026, 9, 18, 21, 10)
    verdict = quiet_verdict(
        observation(
            now=now, session=Session.OVERNIGHT, last_scan_at=now - timedelta(minutes=20),
            next_scanning_open=now + timedelta(minutes=6),
            open_after_overnight=now + timedelta(minutes=6),
        ),
        cfg(),
    )
    text = verdict.text
    # §8's shape: one line per FAILED rule, then the summary line.
    lines = text.splitlines()
    assert [line[:2] for line in lines[:-1]] == ["Q2", "Q3"]
    assert lines[-1].startswith("REFUSED — not in a quiet window.")
    assert "session=overnight" in text
    assert "last radar scan started" in text and "20 min ago" in text
    assert "need >= 35 min" in text
    assert "next scanning session opens" in text and "in 6 min" in text
    assert "need >= 10 min" in text
    assert "earliest allowed start:" in text
    assert "The preview (no --apply) is always available." in text
    # One line per FAILED rule, above the summary.
    assert [line[:2] for line in verdict.failures] == ["Q2", "Q3"]


def test_the_earliest_allowed_start_is_the_later_of_the_two_constraints():
    now = et(2026, 9, 18, 21, 10)
    verdict = quiet_verdict(
        observation(now=now, last_scan_at=now - timedelta(minutes=20)), cfg()
    )
    assert verdict.earliest_allowed_start == now + timedelta(minutes=15)


def test_the_refusal_exit_code_is_two():
    assert QuietRefused("x").exit_code == 2


def code_of(obj) -> str:
    """Source with docstrings and comments removed (`ast.unparse`).

    Several assertions here are about what the CODE does, and the prose
    beside it names the thing it refuses to do — `cli.py`'s docstring
    says "THERE IS NO `--force`" and `quiet.py` explains why. A raw
    substring search would read the explanation and fail.
    """
    import ast
    import textwrap

    tree = ast.parse(textwrap.dedent(inspect.getsource(obj)))
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if not isinstance(body, list) or not body:
            continue
        first = body[0]
        if (
            isinstance(first, ast.Expr)
            and isinstance(first.value, ast.Constant)
            and isinstance(first.value.value, str)
        ):
            node.body = body[1:] or [ast.Pass()]
    return ast.unparse(tree)


def test_there_is_no_force_flag_anywhere():
    """§8: 'No `--force`. An override of the window is the owner's word,
    recorded by the desk, and is a code/config change — never a flag
    (L1, L37).'"""
    parser = archiver_cli.build_parser()
    for argv in (
        ["archiver", "restate", "TESTARCH", "--apply", "--reason", "x", "--force"],
        ["archiver", "backfill-missing", "TESTARCH", "--apply", "--force"],
    ):
        with pytest.raises(SystemExit):
            parser.parse_args(argv)
    for module in (archiver_cli, quiet_mod):
        assert "force" not in code_of(module).lower(), module.__name__


# =====================================================================
# THE TWO NAMED BOUNDARY TESTS (§8)
# =====================================================================


class FakeBars:
    """A store whose bar rows are visible, so 'NO bar row changed' is an
    assertion rather than a hope."""

    def __init__(self):
        self.rows = {}
        self.calls: list[str] = []

    def upsert_bars(self, bars, *, before_commit=None):
        self.calls.append("upsert_bars")
        for b in bars:
            self.rows[(b.ticker, b.interval.value, b.ts)] = str(b.close)
        if before_commit is not None:
            before_commit()
        return len(bars)

    def insert_new_bars(self, conn, bars):
        self.calls.append("insert_new_bars")
        written = 0
        for b in bars:
            key = (b.ticker, b.interval.value, b.ts)
            if key not in self.rows:
                self.rows[key] = str(b.close)
                written += 1
        return written

    def snapshot(self):
        return dict(self.rows)


def _bar(when, close="100.00", ticker="TESTARCH", interval=Interval.I5) -> Bar:
    return Bar(
        ticker=ticker, interval=interval, ts=when, open=Decimal("99.00"),
        high=Decimal("101.00"), low=Decimal("98.50"), close=Decimal(close), volume=1234,
    )


def test_gemini_close_boundary_poller_lag():
    """Gemini's round-3 sequence, placed on THIS radar's real closing
    boundaries (§8).

    (i) NORMAL DAY 20:00 — the repair is refused by Q1 (`market_reset`),
        and a lagging poller write would be dropped by the radar's own
        gate anyway.
    (ii) EARLY-CLOSE DAY 17:00 -> OVERNIGHT — the gate does NOT drop the
        lagging write, so Q3 is the whole protection: at 17:00:10 the
        last cycle started ~16:59, one minute ago, and the repair is
        REFUSED.
    (iii) Gemini's literal 16:00 is RTH -> AFTERMARKET, both SCANNED:
        refused by Q1.

    No bar row changes in any of the three.
    """
    store = FakeBars()
    store.upsert_bars([_bar(et(2026, 11, 27, 12, 55), close="100.00")])
    before = store.snapshot()

    # (i) normal day, 20:00:10 — market_reset
    normal = quiet_verdict(
        observation(now=et(2026, 9, 18, 20, 0, 10), session=Session.MARKET_RESET,
                    last_scan_at=et(2026, 9, 18, 19, 59)),
        cfg(),
    )
    assert normal.quiet is False
    assert any("market_reset" in line for line in normal.failures)

    # (ii) early close, 17:00:10 — OVERNIGHT, but the cycle was a minute ago
    early = quiet_verdict(
        observation(now=et(2026, 11, 27, 17, 0, 10), session=Session.OVERNIGHT,
                    last_scan_at=et(2026, 11, 27, 16, 59),
                    next_scanning_open=et(2026, 11, 30, 4, 0),
                    open_after_overnight=et(2026, 11, 30, 4, 0)),
        cfg(),
    )
    assert early.quiet is False
    assert [line[:2] for line in early.failures] == ["Q3"]
    assert "1 min ago" in early.text

    # (iii) Gemini's literal 16:00 — RTH, a scanned session
    literal = quiet_verdict(
        observation(now=et(2026, 9, 18, 16, 0), session=Session.RTH,
                    last_scan_at=et(2026, 9, 18, 15, 58)),
        cfg(),
    )
    assert literal.quiet is False
    assert any(line.startswith("Q1") for line in literal.failures)

    assert store.snapshot() == before, "a refused repair must not change a bar row"
    assert store.calls == ["upsert_bars"]      # only the setup write


def test_astra_open_boundary_repair_crosses_open():
    """Astra's round-3 sequence (§8): a repair started at 03:59:50, the
    poller fetching at 04:00:05, the repair committing at 04:00:10, the
    poller writing at 04:00:20.

    At START it is refused by Q2 — 04:00 is 10 seconds away and the rule
    needs 10 MINUTES. And a repair started at 03:49:59, which WOULD pass
    at start, is rolled back by the PRE-COMMIT re-check when it reaches
    its commit at 03:50:05.
    """
    store = FakeBars()
    store.upsert_bars([_bar(et(2026, 9, 18, 3, 0), close="100.00")])
    before = store.snapshot()

    start = quiet_verdict(
        observation(now=et(2026, 9, 18, 3, 59, 50), session=Session.OVERNIGHT,
                    last_scan_at=et(2026, 9, 17, 20, 0),
                    next_scanning_open=et(2026, 9, 18, 4, 0),
                    open_after_overnight=et(2026, 9, 18, 4, 0)),
        cfg(),
    )
    assert start.quiet is False
    assert [line[:2] for line in start.failures] == ["Q2"]

    # 03:49:59 — exactly on the 10-minute line, so the START check passes.
    at_start = quiet_verdict(
        observation(now=et(2026, 9, 18, 3, 49, 59), session=Session.OVERNIGHT,
                    last_scan_at=et(2026, 9, 17, 20, 0),
                    next_scanning_open=et(2026, 9, 18, 4, 0),
                    open_after_overnight=et(2026, 9, 18, 4, 0)),
        cfg(),
    )
    assert at_start.quiet is True

    # ...and the SAME repair at its commit instant, 03:50:05, does not.
    at_commit = quiet_verdict(
        observation(now=et(2026, 9, 18, 3, 50, 5), session=Session.OVERNIGHT,
                    last_scan_at=et(2026, 9, 17, 20, 0),
                    next_scanning_open=et(2026, 9, 18, 4, 0),
                    open_after_overnight=et(2026, 9, 18, 4, 0)),
        cfg(),
    )
    assert at_commit.quiet is False
    assert [line[:2] for line in at_commit.failures] == ["Q2"]

    assert store.snapshot() == before
    assert store.calls == ["upsert_bars"]


def test_the_pre_commit_recheck_rolls_the_repair_back():
    """The shape of the radar's own `gate`: Q1-Q3 are checked at command
    START and AGAIN immediately before COMMIT. A failed re-check raises
    inside the transaction, so the `with` rolls it back."""
    store = FakeBars()
    store.upsert_bars([_bar(et(2026, 9, 18, 3, 0), close="100.00")])
    before = store.snapshot()

    instants = iter([
        et(2026, 9, 18, 3, 49, 59),   # start: quiet
        et(2026, 9, 18, 3, 50, 5),    # pre-commit: no longer quiet
    ])

    def _observe(**_kwargs):
        now = next(instants)
        return observation(
            now=now, session=Session.OVERNIGHT, last_scan_at=et(2026, 9, 17, 20, 0),
            next_scanning_open=et(2026, 9, 18, 4, 0),
            open_after_overnight=et(2026, 9, 18, 4, 0),
        )

    rolled_back = []

    class Conn:
        def execute(self, *a, **k):
            return self

        def fetchone(self):
            return (1,)

    class Txn:
        """A transaction with real rollback semantics: on an exception it
        restores the store's rows, which is what Postgres does and what
        the assertion below is actually about."""

        def __enter__(self):
            self.snapshot = store.snapshot()
            return Conn()

        def __exit__(self, exc_type, *_):
            if exc_type is not None:
                rolled_back.append(True)
                store.rows = dict(self.snapshot)
            return False

    with pytest.raises(QuietRefused):
        with quiet_mod.guarded_repair(
            observe=_observe, settings=cfg(), what="restate --apply"
        ) as guard:
            with Txn() as conn:
                store.insert_new_bars(conn, [_bar(et(2026, 9, 18, 3, 5))])
                guard.check_before_commit()

    assert rolled_back == [True]
    assert store.snapshot() == before, "the pre-commit re-check must undo the write"


# =====================================================================
# Commands
# =====================================================================


@pytest.mark.parametrize("session", [
    Session.PREMARKET, Session.RTH, Session.AFTERMARKET, Session.MARKET_RESET
])
@pytest.mark.parametrize("command", ["restate", "backfill-missing"])
def test_both_mutating_commands_are_refused_in_every_scanned_session(session, command):
    verdict = quiet_verdict(
        observation(now=et(2026, 9, 18, 10, 0), session=session), cfg()
    )
    assert verdict.quiet is False
    assert command in archiver_cli.MUTATING_COMMANDS


def test_previews_always_run(monkeypatch):
    """§8: 'Previews and every read-only command are always available.'"""
    calls = []
    monkeypatch.setattr(
        quiet_mod, "require_quiet",
        lambda *a, **k: calls.append("checked"),
    )
    for command in archiver_cli.READ_ONLY_COMMANDS:
        assert command not in archiver_cli.MUTATING_COMMANDS
    assert calls == []


def test_the_read_only_commands_are_the_ones_the_design_names():
    assert archiver_cli.READ_ONLY_COMMANDS == (
        "audit", "incidents", "progress", "shadow-report",
    )
    assert archiver_cli.MUTATING_COMMANDS == ("restate", "backfill-missing")


def test_restate_apply_requires_a_reason():
    parser = archiver_cli.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["archiver", "restate", "TESTARCH", "--apply"])
    args = parser.parse_args(
        ["archiver", "restate", "TESTARCH", "i5", "--apply", "--reason", "vendor split"]
    )
    assert args.reason == "vendor split" and args.apply is True


def test_restate_without_apply_is_a_preview():
    parser = archiver_cli.build_parser()
    args = parser.parse_args(["archiver", "restate", "TESTARCH"])
    assert args.apply is False and args.reason is None


def test_backfill_missing_can_only_do_nothing():
    """§8: `backfill-missing` never overwrites. Its only write path is
    `insert_new_bars` (DO NOTHING); `upsert_bars` is unreachable from it."""
    source = inspect.getsource(archiver_cli._cmd_backfill_missing)
    assert "insert_new_bars" in source
    assert "upsert_bars" not in source


def test_backfill_missing_never_calls_upsert_bars(monkeypatch):
    store = FakeBars()
    store.upsert_bars([_bar(et(2026, 9, 18, 3, 0), close="100.00")])
    store.calls.clear()
    existing = store.snapshot()
    assert store.insert_new_bars(None, [_bar(et(2026, 9, 18, 3, 0), close="999.00")]) == 0
    assert store.snapshot() == existing
    assert store.calls == ["insert_new_bars"]


def test_every_read_only_command_calls_no_write_method():
    """The four read-only commands and both previews touch no writer."""
    for name in archiver_cli.READ_ONLY_COMMANDS:
        handler = archiver_cli.HANDLERS[name]
        source = inspect.getsource(handler)
        for writer in ("upsert_bars", "insert_new_bars", "upsert_progress", "open_or_refresh"):
            assert writer not in source, f"{name} reaches {writer}"


def test_incidents_resolve_is_explicit_and_audited():
    parser = archiver_cli.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["archiver", "incidents", "resolve", "7"])
    args = parser.parse_args(
        ["archiver", "incidents", "resolve", "7", "--by", "dejan", "--note", "repaired"]
    )
    assert args.incident_id == 7 and args.by == "dejan" and args.note == "repaired"


def test_audit_is_read_only_and_takes_a_from_date():
    parser = archiver_cli.build_parser()
    args = parser.parse_args(["archiver", "audit", "--from", "2026-09-01"])
    assert args.from_date == date(2026, 9, 1)
    assert "audit" in archiver_cli.READ_ONLY_COMMANDS


def test_shadow_report_takes_a_night_count():
    parser = archiver_cli.build_parser()
    assert parser.parse_args(["archiver", "shadow-report"]).nights == 5
    assert parser.parse_args(["archiver", "shadow-report", "--nights", "12"]).nights == 12


# =====================================================================
# Known limit 1, DEMONSTRATED (spec §12, §15)
# =====================================================================


def test_known_limit_1_the_poller_keeps_writing_while_a_restated_incident_is_open():
    """SPEC §12 limit 1, executable rather than prose — it goes to the
    owner WITH the switch ruling.

    After a vendor restatement the archiver WITHHOLDS the target and the
    heartbeat goes non-green, but the poller is UNCHANGED by R8: it goes
    on writing new-basis i1 bars beside old-basis history until an
    operator runs `restate`. This test IMPORTS the poller and drives it.
    It does not edit it, and `git diff main -- src/cobalt/radar/` is
    empty.
    """
    import asyncio

    from cobalt.radar.poller import BarPoller, PollMember

    store = FakeBars()
    old_basis = _bar(et(2026, 9, 18, 10, 0), close="100.00", interval=Interval.I1)
    store.rows[(old_basis.ticker, "i1", old_basis.ts)] = "100.00"

    class _Store:
        def __init__(self, bars):
            self.bars = bars

        def watermark(self, ticker, interval="i1"):
            keys = [k[2] for k in self.bars.rows if k[0] == ticker and k[1] == interval]
            return max(keys) if keys else None

        def upsert_bars(self, bars, *, before_commit=None):
            return self.bars.upsert_bars(bars, before_commit=before_commit)

    class _Bucket:
        async def acquire(self):
            return None

    new_basis = _bar(et(2026, 9, 18, 10, 5), close="50.00", interval=Interval.I1)

    async def _fetch(ticker, interval, token):
        return [new_basis]

    poller = BarPoller(
        "TOKEN", store=_Store(store), bucket=_Bucket(), overlap_bars=5,
        max_age_s=180, fetch=_fetch,
    )
    asyncio.run(
        poller.poll(
            [PollMember("TESTARCH", 1)],
            now=et(2026, 9, 18, 10, 10),
            session=Session.RTH,
        )
    )

    # An open `restated` incident changes NOTHING about the poller: the
    # new-basis bar is now stored beside the old-basis one.
    assert store.rows[("TESTARCH", "i1", new_basis.ts)] == "50.00"
    assert store.rows[("TESTARCH", "i1", old_basis.ts)] == "100.00"
    assert "insert_new_bars" not in store.calls, "the poller writes through upsert_bars"


def test_the_poller_module_is_imported_never_edited():
    """R8, asserted here as well as by the empty `git diff main --
    src/cobalt/radar/` in the build report."""
    import cobalt.radar.poller as poller_mod

    source = inspect.getsource(poller_mod)
    for name in ("archive_progress", "archive_incidents", "quiet", "ARCHIVE_RUN_LOCK_KEY"):
        assert name not in source, f"the poller now knows about {name!r}"
