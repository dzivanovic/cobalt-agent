"""C1-C6: PASS / FAIL / ERROR for each, offline (no DB, no live launchd).

DB-touching checks (C2, C4) never open a real connection here — a fake
object implements just the psycopg surface `checks.py` calls
(`execute`, `rollback`, `close`, cursor `.description`/`.fetchone`/
`.fetchall`) — per this build's ruling: "no DB credentials copied;
DB-backed proof is the hub's step at merge."
"""

from datetime import date, datetime, timezone

import pytest

from cobalt.dayopen import checks
from cobalt.dayopen.launchd import LaunchdPrintError, LaunchdPrintStatus
from cobalt.dayopen.models import Verdict
from cobalt.session.clock import session_clock

MONDAY = date(2026, 9, 14)  # a real NYSE trading day (loaded calendar)
SUNDAY = date(2026, 9, 13)  # a real weekend day
SATURDAY = date(2026, 9, 19)  # the real 09-19 false alarm this guard closes
MONDAY_0705_ET = datetime(2026, 9, 14, 11, 5, tzinfo=timezone.utc)  # 07:05 ET (DST, UTC-4)


class _Col:
    def __init__(self, name):
        self.name = name


class _FakeCursor:
    def __init__(self, rows, description=None):
        self._rows = rows
        self.description = description

    def fetchone(self):
        return self._rows[0]

    def fetchall(self):
        return self._rows


def _one_row_cursor(value) -> _FakeCursor:
    """A `SELECT count(*) ...`-shaped response: one row, one column."""
    return _FakeCursor([(value,)])


def _table_cursor(rows, columns) -> _FakeCursor:
    """A `SELECT <cols> ...`-shaped response, with `.description`."""
    return _FakeCursor(rows, [_Col(c) for c in columns])


class _FakeConn:
    """Records every SQL string it is asked to run, so a test can assert
    on the exact query shape (the C4 %-free assertion). `responses` is a
    list of `(predicate, fake_cursor)` pairs, tried in order — the
    caller builds the cursor with `_one_row_cursor` / `_table_cursor` so
    there is no ambiguity between "a row of one count" and "a row of
    table cells" (both are plain tuples otherwise)."""

    def __init__(self, responses):
        self._responses = responses
        self.executed_sql: list[str] = []
        self.closed = False

    def execute(self, sql, params=None):
        self.executed_sql.append(sql)
        if sql.strip().startswith("BEGIN"):
            return _FakeCursor([])
        for predicate, cursor in self._responses:
            if predicate(sql):
                return cursor
        raise AssertionError(f"unexpected SQL: {sql}")

    def rollback(self):
        pass

    def close(self):
        self.closed = True


class _RaisingConnect:
    def __call__(self):
        raise RuntimeError("could not connect (no credentials in this worktree)")


# ---------------------------------------------------------------------
# C1
# ---------------------------------------------------------------------


def test_c1_pass_running_with_pid():
    status = LaunchdPrintStatus("com.cobalt.radar", "running", 27385, "(never exited)", 1, "raw")
    result = checks.check_c1_radar_launchd(print_fn=lambda label: status)
    assert result.verdict is Verdict.PASS
    assert "pid=27385" in result.detail


def test_c1_fail_not_running():
    status = LaunchdPrintStatus("com.cobalt.radar", "not running", None, "1", 4, "raw")
    result = checks.check_c1_radar_launchd(print_fn=lambda label: status)
    assert result.verdict is Verdict.FAIL


def test_c1_error_when_launchctl_fails():
    def _raise(label):
        raise LaunchdPrintError("launchctl print exited 1")

    result = checks.check_c1_radar_launchd(print_fn=_raise)
    assert result.verdict is Verdict.ERROR
    assert "ERROR(command failed)" in result.detail


# ---------------------------------------------------------------------
# C2
# ---------------------------------------------------------------------

_MEMBERSHIP_COLUMNS = [
    "id", "pool_key", "ticker", "trade_date", "first_seen_at", "entered_at",
    "left_at", "source", "rank_at_entry", "last_rank", "below_cap_streak",
    "excluded_by", "session",
]


class _FakeSettingsStore:
    def __init__(self, rows=None):
        self._rows = rows or {}

    def values(self):
        return self._rows


def _membership_row(first_seen_at):
    return (
        11, "primary", "AEHL", MONDAY, first_seen_at, first_seen_at, None,
        "screen:morning_low_float@a834132de4fa", 11, 12, 0, None, "premarket",
    )


def _pool_settings(metric="volume"):
    return _FakeSettingsStore(
        {
            "radar.pool": {
                "status": "ok",
                "block": {
                    "kind": "pool", "cap": 5,
                    "rank_metric": {"premarket": metric, "rth": "rvol", "aftermarket": "volume"},
                },
            }
        }
    )


def test_c2_pass_real_shape_row_on_time():
    # 2026-09-14 08:00:58.880260+00:00 UTC = 04:00:58 ET — the real first
    # row from day-open-2026-09-14.md S2b.
    first_seen = datetime(2026, 9, 14, 8, 0, 58, 880260, tzinfo=timezone.utc)
    conn = _FakeConn(
        [
            (lambda sql: "count(*)" in sql, _one_row_cursor(417)),
            (lambda sql: "ORDER BY first_seen_at" in sql, _table_cursor([_membership_row(first_seen)], _MEMBERSHIP_COLUMNS)),
        ]
    )
    result = checks.check_c2_radar_membership(
        MONDAY, now=MONDAY_0705_ET, clock=session_clock(),
        system_connect=lambda: conn, settings_store=_pool_settings(),
    )
    assert result.verdict is Verdict.PASS
    assert "count=417" in result.detail
    assert conn.closed
    assert "pool block metric (premarket): volume" in result.raw


def test_c2_fail_zero_rows():
    conn = _FakeConn(
        [
            (lambda sql: "count(*)" in sql, _one_row_cursor(0)),
            (lambda sql: "ORDER BY first_seen_at" in sql, _table_cursor([], _MEMBERSHIP_COLUMNS)),
        ]
    )
    result = checks.check_c2_radar_membership(
        MONDAY, now=MONDAY_0705_ET, clock=session_clock(),
        system_connect=lambda: conn, settings_store=_pool_settings(),
    )
    assert result.verdict is Verdict.FAIL
    assert "no rows" in result.detail


@pytest.mark.parametrize("non_trading_day", [SUNDAY, SATURDAY])
def test_c2_non_trading_day_with_zero_rows_is_pass(non_trading_day):
    """No scanning session exists on a weekend, so zero rows is the
    correct state, not a defect: 2026-09-19 (Saturday) day-open went
    AMBER on C2 alone for exactly this reason. C3 already carries the
    same calendar guard (`test_c3_weekend_red_is_idle`)."""
    conn = _FakeConn(
        [
            (lambda sql: "count(*)" in sql, _one_row_cursor(0)),
            (lambda sql: "ORDER BY first_seen_at" in sql, _table_cursor([], _MEMBERSHIP_COLUMNS)),
        ]
    )
    result = checks.check_c2_radar_membership(
        non_trading_day, now=MONDAY_0705_ET, clock=session_clock(),
        system_connect=lambda: conn, settings_store=_pool_settings(),
    )
    assert result.verdict is Verdict.PASS
    assert result.detail == f"PASS — no session today ({non_trading_day} is not a trading day)"
    # the raw block is still produced — the operator still sees the probe
    assert "count\t0" in result.raw
    assert "pool block metric" in result.raw
    assert conn.closed


def test_c2_trading_day_zero_rows_still_fails():
    """The guard is a calendar guard, not a zero-rows amnesty: a trading
    day with no membership rows stays FAIL (same shape as
    `test_c2_fail_zero_rows`, kept beside it so the pair is legible)."""
    conn = _FakeConn(
        [
            (lambda sql: "count(*)" in sql, _one_row_cursor(0)),
            (lambda sql: "ORDER BY first_seen_at" in sql, _table_cursor([], _MEMBERSHIP_COLUMNS)),
        ]
    )
    result = checks.check_c2_radar_membership(
        MONDAY, now=MONDAY_0705_ET, clock=session_clock(),
        system_connect=lambda: conn, settings_store=_pool_settings(),
    )
    assert result.verdict is Verdict.FAIL
    assert result.detail == f"FAIL — no rows for {MONDAY}"


def test_c2_fail_first_row_before_premarket_open():
    too_early = datetime(2026, 9, 14, 7, 30, tzinfo=timezone.utc)  # 03:30 ET
    conn = _FakeConn(
        [
            (lambda sql: "count(*)" in sql, _one_row_cursor(5)),
            (lambda sql: "ORDER BY first_seen_at" in sql, _table_cursor([_membership_row(too_early)], _MEMBERSHIP_COLUMNS)),
        ]
    )
    result = checks.check_c2_radar_membership(
        MONDAY, now=MONDAY_0705_ET, clock=session_clock(),
        system_connect=lambda: conn, settings_store=_pool_settings(),
    )
    assert result.verdict is Verdict.FAIL
    assert "before session.premarket_open" in result.detail


def test_c2_error_when_db_unreachable():
    result = checks.check_c2_radar_membership(
        MONDAY, now=MONDAY_0705_ET, clock=session_clock(),
        system_connect=_RaisingConnect(), settings_store=_pool_settings(),
    )
    assert result.verdict is Verdict.ERROR


def test_c2_missing_pool_row_is_noted_not_fatal():
    first_seen = datetime(2026, 9, 14, 8, 0, 58, tzinfo=timezone.utc)
    conn = _FakeConn(
        [
            (lambda sql: "count(*)" in sql, _one_row_cursor(1)),
            (lambda sql: "ORDER BY first_seen_at" in sql, _table_cursor([_membership_row(first_seen)], _MEMBERSHIP_COLUMNS)),
        ]
    )
    result = checks.check_c2_radar_membership(
        MONDAY, now=MONDAY_0705_ET, clock=session_clock(),
        system_connect=lambda: conn, settings_store=_FakeSettingsStore({}),
    )
    assert result.verdict is Verdict.PASS
    assert "no 'radar.pool' row" in result.raw


# ---------------------------------------------------------------------
# C3
# ---------------------------------------------------------------------

FIXTURES = checks.REPO_ROOT / "tests" / "fixtures" / "dayopen"
_LOG_LINES = (FIXTURES / "heartbeat.log.excerpt").read_text().splitlines()


def test_c3_fail_red_on_a_trading_day_past_open():
    result = checks.check_c3_radar_beat_line(
        report_date=MONDAY, now=MONDAY_0705_ET, clock=session_clock(),
        read_lines=lambda p: _LOG_LINES,
    )
    assert result.verdict is Verdict.FAIL


def test_c3_pass_ok_radar_line():
    result = checks.check_c3_radar_beat_line(
        report_date=MONDAY, now=MONDAY_0705_ET, clock=session_clock(),
        read_lines=lambda p: _LOG_LINES[:200],
    )
    assert result.verdict is Verdict.PASS


def test_c3_weekend_red_is_idle():
    """RULED EXPECT: "newest radar line not RED after 04:00 ET on a
    trading day (weekend RED is idle)" — a RED line found while checking
    a genuine weekend date must PASS as exempt."""
    result = checks.check_c3_radar_beat_line(
        report_date=SUNDAY, now=MONDAY_0705_ET, clock=session_clock(),
        read_lines=lambda p: _LOG_LINES,
    )
    assert result.verdict is Verdict.PASS
    assert "exempt" in result.detail


def test_c3_error_no_radar_line_at_all():
    result = checks.check_c3_radar_beat_line(
        report_date=MONDAY, now=MONDAY_0705_ET, clock=session_clock(),
        read_lines=lambda p: ["nothing to see here"],
    )
    assert result.verdict is Verdict.ERROR


def test_c3_error_when_log_unreadable():
    def _raise(path):
        raise FileNotFoundError(path)

    result = checks.check_c3_radar_beat_line(
        report_date=MONDAY, now=MONDAY_0705_ET, clock=session_clock(), read_lines=_raise
    )
    assert result.verdict is Verdict.ERROR


# ---------------------------------------------------------------------
# C4
# ---------------------------------------------------------------------


def test_c4_pass_matches_expected():
    conn = _FakeConn([(lambda sql: "session_blocks" in sql, _one_row_cursor(8))])
    result = checks.check_c4_session_blocks(expected=8, system_connect=lambda: conn)
    assert result.verdict is Verdict.PASS
    # The S4 bug: a bare '%' in the SQL text (a LIKE pattern) collides
    # with psycopg's placeholder parser, which only accepts '%s'/'%b'/
    # '%t'. Every '%' in the query must be part of the '%s' placeholder
    # — never a LIKE wildcard — and the operator must be regex (`~`).
    for sql in conn.executed_sql:
        if sql.strip().startswith("BEGIN"):
            continue
        assert "LIKE" not in sql
        assert sql.count("%") == sql.count("%s")
    assert any("~" in sql for sql in conn.executed_sql)


def test_c4_fail_mismatch():
    conn = _FakeConn([(lambda sql: "session_blocks" in sql, _one_row_cursor(3))])
    result = checks.check_c4_session_blocks(expected=8, system_connect=lambda: conn)
    assert result.verdict is Verdict.FAIL


def test_c4_error_when_db_unreachable():
    result = checks.check_c4_session_blocks(expected=8, system_connect=_RaisingConnect())
    assert result.verdict is Verdict.ERROR


# ---------------------------------------------------------------------
# C5
# ---------------------------------------------------------------------

_ARCHIVER_TEXT = (FIXTURES / "archiver-runs.md.excerpt").read_text()


def test_c5_pass_last_row_on_previous_trading_day():
    # Fixture's last row starts 2026-09-11 20:30 ET (Friday) — the
    # previous trading day before Monday 2026-09-14.
    result = checks.check_c5_archiver_last_run(
        report_date=MONDAY, calendar=session_clock().calendar,
        read_text=lambda p: _ARCHIVER_TEXT, read_lines=lambda p: [],
    )
    assert result.verdict is Verdict.PASS


def test_c5_fail_stale_last_row():
    later = date(2026, 9, 16)  # previous trading day would be 2026-09-15
    result = checks.check_c5_archiver_last_run(
        report_date=later, calendar=session_clock().calendar,
        read_text=lambda p: _ARCHIVER_TEXT, read_lines=lambda p: [],
    )
    assert result.verdict is Verdict.FAIL
    assert "expected 2026-09-15" in result.detail


def test_c5_fail_nonzero_failures():
    text = (
        "| Date (UTC) | Mode | Failures |\n"
        "|---|---|---|\n"
        "| 2026-09-11T20:30:05Z | full | 2 |\n"
    )
    result = checks.check_c5_archiver_last_run(
        report_date=MONDAY, calendar=session_clock().calendar,
        read_text=lambda p: text, read_lines=lambda p: [],
    )
    assert result.verdict is Verdict.FAIL
    assert "failure(s)" in result.detail


def test_c5_error_no_table():
    result = checks.check_c5_archiver_last_run(
        report_date=MONDAY, calendar=session_clock().calendar,
        read_text=lambda p: "no table here", read_lines=lambda p: [],
    )
    assert result.verdict is Verdict.ERROR


def test_c5_error_missing_file():
    def _raise(path):
        raise FileNotFoundError(path)

    result = checks.check_c5_archiver_last_run(
        report_date=MONDAY, calendar=session_clock().calendar,
        read_text=_raise, read_lines=lambda p: [],
    )
    assert result.verdict is Verdict.ERROR


# ---------------------------------------------------------------------
# C6
# ---------------------------------------------------------------------

MONDAY_1145_ET = datetime(2026, 9, 14, 15, 45, tzinfo=timezone.utc)  # 11:45 ET


def test_c6_pass_four_beats_no_failures():
    # heartbeat.err path also goes through read_lines; give it no FAILED lines.
    result = checks.check_c6_beats_since_prior_evening(
        report_date=MONDAY, now=MONDAY_1145_ET, max_gap_min=20,
        heartbeat_log_path="log", heartbeat_err_path="err",
        read_lines=lambda p: _LOG_LINES if p == "log" else [],
    )
    assert result.verdict is Verdict.PASS
    assert "4 beat(s)" in result.detail


def test_c6_fail_max_gap_too_wide():
    result = checks.check_c6_beats_since_prior_evening(
        report_date=MONDAY, now=MONDAY_1145_ET, max_gap_min=10,
        heartbeat_log_path="log", heartbeat_err_path="err",
        read_lines=lambda p: _LOG_LINES if p == "log" else [],
    )
    assert result.verdict is Verdict.FAIL
    assert "max gap" in result.detail


def test_c6_fail_no_beats_in_window():
    result = checks.check_c6_beats_since_prior_evening(
        report_date=MONDAY, now=MONDAY_1145_ET, max_gap_min=20,
        heartbeat_log_path="log", heartbeat_err_path="err",
        read_lines=lambda p: [],
    )
    assert result.verdict is Verdict.FAIL
    assert "no beats" in result.detail


def test_c6_fail_on_failed_line_in_window():
    failed_line = "2026-09-14 09:00:00.000 | ERROR    | x:y:1 - heartbeat: vault unit FAILED — daily-note writer returned no result"
    result = checks.check_c6_beats_since_prior_evening(
        report_date=MONDAY, now=MONDAY_1145_ET, max_gap_min=20,
        heartbeat_log_path="log", heartbeat_err_path="err",
        read_lines=lambda p: _LOG_LINES if p == "log" else [failed_line],
    )
    assert result.verdict is Verdict.FAIL
    assert "FAILED" in result.detail


def test_c6_error_when_log_unreadable():
    def _raise(path):
        raise FileNotFoundError(path)

    result = checks.check_c6_beats_since_prior_evening(
        report_date=MONDAY, now=MONDAY_1145_ET, max_gap_min=20, read_lines=_raise
    )
    assert result.verdict is Verdict.ERROR
