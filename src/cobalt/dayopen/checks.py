"""The six day-open checks (RULED 2026-09-14, A), fixed order, C1-C6.

Every check function does its own collection AND renders its own verdict
(same shape as `cobalt.heartbeat.probes`): it never raises for an
EXPECTED failure mode (missing file, launchd/DB error, unparseable
report) — those become `Verdict.ERROR` results so one broken check does
not take the rest of the sweep down with it. Every dependency (the
launchd caller, the DB connection factory, the file reader) is a keyword
argument with a real default, so tests inject fixtures without
monkeypatching module internals.

THRESHOLDS ARE NEVER LITERALS HERE (F16 / L53): `expected` and
`max_gap_min` are passed in from `dayopen.config.load_dayopen_config()`;
the premarket/aftermarket boundaries come from the session clock, which
already reads them from `tunables.yaml`.
"""

from __future__ import annotations

from datetime import date as Date
from datetime import datetime, timedelta
from pathlib import Path
from typing import Callable, Optional

from cobalt import db, env
from cobalt.db import Side
from cobalt.session.calendar import TradingCalendar
from cobalt.session.clock import ET, SessionClock, session_clock
from cobalt.settings.store import TraderSettingsStore
from cobalt.taxonomy.loader import load_tunables

from .launchd import LaunchdPrintError, LaunchdPrintStatus, launchctl_print
from .models import CheckResult, Verdict
from .parse import (
    all_beat_headers,
    failed_lines,
    last_markdown_table_row,
    newest_beat_header,
    newest_radar_probe_line,
)

REPO_ROOT = Path(__file__).resolve().parents[3]
HEARTBEAT_LOG_PATH = REPO_ROOT / "logs" / "heartbeat.log"
HEARTBEAT_ERR_PATH = REPO_ROOT / "logs" / "heartbeat.err"
ARCHIVER_RUNS_PATH = REPO_ROOT / "docs" / "30 - Design" / "archiver-runs.md"
ARCHIVER_ERR_PATH = REPO_ROOT / "logs" / "archiver.err"

#: C4's SQL, captured once so C4's own raw block quotes the exact query
#: run — the S4 bug (`ProgrammingError: only '%s' ... got '%'`) was a
#: literal `%` in a LIKE pattern colliding with psycopg's placeholder
#: parser; `~` (regex) with the pattern as a bound parameter has no `%`
#: in the SQL text at all (day-open-2026-09-14.md, S4).
C4_ACTOR_PATTERN = "^vaultwrite:heartbeat:"


def _read_lines(path: Path) -> list[str]:
    return path.read_text().splitlines()


def _read_text(path: Path) -> str:
    return path.read_text()


def _default_system_connect():
    return db.connect(env.resolve_db_name(), side=Side.SYSTEM)


def previous_trading_day(day: Date, calendar: TradingCalendar) -> Date:
    """The trading day strictly before `day`. Bounded to 14 calendar days
    back — the NYSE calendar has no closure anywhere near that long, and
    a longer run here means the calendar is wrong, not that this should
    loop further (mirrors `session.clock`'s own `MAX_CLOSED_RUN_DAYS`
    bound in spirit, at a scale that fits one week's holidays)."""
    d = day - timedelta(days=1)
    for _ in range(14):
        if calendar.is_trading_day(d):
            return d
        d -= timedelta(days=1)
    raise RuntimeError(f"no trading day found within 14 days before {day}")


# ---------------------------------------------------------------------
# C1 — radar launchd state
# ---------------------------------------------------------------------


def check_c1_radar_launchd(
    *, label: str = "com.cobalt.radar", print_fn: Callable[[str], LaunchdPrintStatus] = launchctl_print
) -> CheckResult:
    try:
        status = print_fn(label)
    except LaunchdPrintError as e:
        return CheckResult("C1", f"{label} launchd", Verdict.ERROR, f"ERROR(command failed) — {e}", str(e))

    detail = f"state={status.state}, pid={status.pid}, last exit code={status.last_exit_code}"
    if status.running_with_pid:
        return CheckResult("C1", f"{label} launchd", Verdict.PASS, f"PASS — {detail}", status.raw)
    return CheckResult(
        "C1", f"{label} launchd", Verdict.FAIL,
        f"FAIL — {detail} (expected: state=running with a pid)", status.raw,
    )


# ---------------------------------------------------------------------
# C2 — radar_membership rows for the date
# ---------------------------------------------------------------------


def check_c2_radar_membership(
    report_date: Date,
    *,
    now: datetime,
    clock: Optional[SessionClock] = None,
    system_connect: Callable[[], object] = _default_system_connect,
    settings_store: Optional[TraderSettingsStore] = None,
) -> CheckResult:
    clock = clock or session_clock()
    title = "radar_membership rows"

    try:
        conn = system_connect()
        try:
            conn.execute("BEGIN READ ONLY")
            count = conn.execute(
                "SELECT count(*) FROM radar_membership WHERE trade_date = %s",
                (report_date,),
            ).fetchone()[0]
            cur = conn.execute(
                "SELECT id, pool_key, ticker, trade_date, first_seen_at, entered_at, "
                "left_at, source, rank_at_entry, last_rank, below_cap_streak, "
                "excluded_by, session FROM radar_membership WHERE trade_date = %s "
                "ORDER BY first_seen_at ASC LIMIT 5",
                (report_date,),
            )
            columns = [c.name for c in cur.description]
            first_five = [dict(zip(columns, r)) for r in cur.fetchall()]
        finally:
            conn.rollback()
            conn.close()
    except Exception as e:  # noqa: BLE001 — a broken probe is ERROR, not a crash
        return CheckResult("C2", title, Verdict.ERROR, f"ERROR(command failed) — {e}", str(e))

    store = settings_store if settings_store is not None else TraderSettingsStore()
    pool_note: Optional[str] = None
    metric: Optional[str] = None
    session = clock.session(now)
    try:
        pool_row = store.values().get("radar.pool")
    except Exception as e:  # noqa: BLE001 — the metric is supplementary, never fatal to C2
        pool_row = None
        pool_note = f"'user'.trader_settings unreadable: {e}"
    if pool_row:
        block = pool_row.get("block") or {}
        rank_metric = block.get("rank_metric") or {}
        metric = rank_metric.get(session.value)
        if metric is None and pool_note is None:
            pool_note = f"no rank_metric.{session.value} in the 'radar.pool' mirror row"
    elif pool_note is None:
        pool_note = "no 'radar.pool' row in \"user\".trader_settings"

    raw_lines = [f"count\t{count}"]
    if first_five:
        cols = list(first_five[0].keys())
        raw_lines.append("\t".join(cols))
        for row in first_five:
            raw_lines.append("\t".join("" if row[c] is None else str(row[c]) for c in cols))
    raw_lines.append(f"pool block metric ({session.value}): {metric or pool_note}")
    raw = "\n".join(raw_lines)

    if count == 0:
        return CheckResult("C2", title, Verdict.FAIL, f"FAIL — no rows for {report_date}", raw)

    first_seen_et = SessionClock.to_et(first_five[0]["first_seen_at"])
    windows = clock.windows_for(report_date)
    if windows:
        premarket_open = windows[0].start
        on_time = first_seen_et.time() >= premarket_open
        window_note = f">= session.premarket_open {premarket_open:%H:%M}"
    else:
        on_time = True
        window_note = "n/a (not a trading day)"

    if not on_time:
        return CheckResult(
            "C2", title, Verdict.FAIL,
            f"FAIL — count={count}, first_seen_at {first_seen_et:%H:%M:%S} ET is before "
            f"session.premarket_open {premarket_open:%H:%M}",
            raw,
        )
    return CheckResult(
        "C2", title, Verdict.PASS,
        f"PASS — count={count}, first_seen_at {first_seen_et:%H:%M:%S} ET ({window_note})",
        raw,
    )


# ---------------------------------------------------------------------
# C3 — radar beat line (heartbeat.log)
# ---------------------------------------------------------------------


def check_c3_radar_beat_line(
    *,
    report_date: Date,
    now: datetime,
    clock: Optional[SessionClock] = None,
    heartbeat_log_path: Path = HEARTBEAT_LOG_PATH,
    heartbeat_err_path: Path = HEARTBEAT_ERR_PATH,
    read_lines: Callable[[Path], list[str]] = _read_lines,
) -> CheckResult:
    clock = clock or session_clock()
    title = "radar beat line"

    try:
        log_lines = read_lines(heartbeat_log_path)
    except OSError as e:
        return CheckResult("C3", title, Verdict.ERROR, f"ERROR(command failed) — {e}", str(e))

    radar_line = newest_radar_probe_line(log_lines)
    beat_header = newest_beat_header(log_lines)
    try:
        err_tail = read_lines(heartbeat_err_path)[-5:]
    except OSError:
        err_tail = ["(logs/heartbeat.err unreadable)"]

    raw = "\n".join(
        [
            f"newest radar probe line: {radar_line.raw if radar_line else '(none found)'}",
            f"newest beat header: {beat_header.raw if beat_header else '(none found)'}",
            "--- heartbeat.err tail",
            *err_tail,
        ]
    )

    if radar_line is None:
        return CheckResult(
            "C3", title, Verdict.ERROR,
            "ERROR(command failed) — no 'OK|RED  radar  ...' line found in logs/heartbeat.log",
            raw,
        )

    windows = clock.windows_for(report_date)
    trading_day = bool(windows)
    past_open = trading_day and SessionClock.to_et(now).time() >= windows[0].start
    exempt = not trading_day or not past_open

    if radar_line.is_red and not exempt:
        return CheckResult("C3", title, Verdict.FAIL, f"FAIL — newest radar line is RED: {radar_line.detail}", raw)
    note = " (exempt: idle before/outside premarket on a trading day, or not a trading day)" \
        if radar_line.is_red and exempt else ""
    return CheckResult("C3", title, Verdict.PASS, f"PASS — {radar_line.state} radar: {radar_line.detail}{note}", raw)


# ---------------------------------------------------------------------
# C4 — system.session_blocks heartbeat actor count
# ---------------------------------------------------------------------


def check_c4_session_blocks(
    *,
    expected: int,
    system_connect: Callable[[], object] = _default_system_connect,
) -> CheckResult:
    title = "session_blocks heartbeat actor"
    try:
        conn = system_connect()
        try:
            conn.execute("BEGIN READ ONLY")
            count = conn.execute(
                "SELECT count(*) FROM session_blocks WHERE actor ~ %s",
                (C4_ACTOR_PATTERN,),
            ).fetchone()[0]
        finally:
            conn.rollback()
            conn.close()
    except Exception as e:  # noqa: BLE001
        return CheckResult("C4", title, Verdict.ERROR, f"ERROR(command failed) — {e}", str(e))

    raw = (
        f"count\t{count}\n"
        f"query: SELECT count(*) FROM session_blocks WHERE actor ~ '{C4_ACTOR_PATTERN}' "
        "(regex operator — never LIKE with %, see day-open-2026-09-14.md S4)"
    )
    if count == expected:
        return CheckResult("C4", title, Verdict.PASS, f"PASS — count={count} (expected {expected})", raw)
    return CheckResult("C4", title, Verdict.FAIL, f"FAIL — count={count}, expected {expected}", raw)


# ---------------------------------------------------------------------
# C5 — archiver last run
# ---------------------------------------------------------------------


def check_c5_archiver_last_run(
    *,
    report_date: Date,
    calendar: Optional[TradingCalendar] = None,
    archiver_runs_path: Path = ARCHIVER_RUNS_PATH,
    archiver_err_path: Path = ARCHIVER_ERR_PATH,
    read_text: Callable[[Path], str] = _read_text,
    read_lines: Callable[[Path], list[str]] = _read_lines,
) -> CheckResult:
    calendar = calendar or session_clock().calendar
    title = "archiver last run"

    try:
        text = read_text(archiver_runs_path)
    except OSError as e:
        return CheckResult("C5", title, Verdict.ERROR, f"ERROR(command failed) — {e}", str(e))
    try:
        err_tail = read_lines(archiver_err_path)[-3:]
    except OSError:
        err_tail = ["(logs/archiver.err unreadable)"]

    parsed = last_markdown_table_row(text)
    raw = "\n".join(
        [
            f"last row: {parsed[1] if parsed else '(no table found)'}",
            "--- archiver.err tail",
            *err_tail,
        ]
    )
    if parsed is None:
        return CheckResult(
            "C5", title, Verdict.ERROR,
            f"ERROR(command failed) — no markdown table found in {archiver_runs_path}",
            raw,
        )

    header, row = parsed
    cells = dict(zip(header, row))
    try:
        date_raw = cells["Date (UTC)"]
        failures = int(cells["Failures"])
    except (KeyError, ValueError) as e:
        return CheckResult(
            "C5", title, Verdict.ERROR,
            f"ERROR(command failed) — unexpected archiver-runs.md column shape: {e}",
            raw,
        )
    try:
        run_at = datetime.fromisoformat(date_raw.replace("Z", "+00:00"))
    except ValueError as e:
        return CheckResult(
            "C5", title, Verdict.ERROR,
            f"ERROR(command failed) — unparseable Date (UTC) {date_raw!r}: {e}",
            raw,
        )

    run_date_et = run_at.astimezone(ET).date()
    expected_date = previous_trading_day(report_date, calendar)

    if failures != 0:
        return CheckResult("C5", title, Verdict.FAIL, f"FAIL — last run {run_date_et} had {failures} failure(s)", raw)
    if run_date_et != expected_date:
        return CheckResult(
            "C5", title, Verdict.FAIL,
            f"FAIL — last run {run_date_et}, expected {expected_date} (previous trading day)",
            raw,
        )
    return CheckResult("C5", title, Verdict.PASS, f"PASS — last run {run_date_et}, 0 failures", raw)


# ---------------------------------------------------------------------
# C6 — beats since 20:00 the previous evening
# ---------------------------------------------------------------------


def _aftermarket_close_time():
    from datetime import time as _time

    row = load_tunables().by_key.get("session.aftermarket_close")
    if row is None:
        raise RuntimeError("tunable 'session.aftermarket_close' is missing from tunables.yaml")
    hour, _, minute = str(row.value).partition(":")
    return _time(int(hour), int(minute))


def check_c6_beats_since_prior_evening(
    *,
    report_date: Date,
    now: datetime,
    max_gap_min: int,
    heartbeat_log_path: Path = HEARTBEAT_LOG_PATH,
    heartbeat_err_path: Path = HEARTBEAT_ERR_PATH,
    read_lines: Callable[[Path], list[str]] = _read_lines,
) -> CheckResult:
    title = "beats since prior evening"
    try:
        log_lines = read_lines(heartbeat_log_path)
    except OSError as e:
        return CheckResult("C6", title, Verdict.ERROR, f"ERROR(command failed) — {e}", str(e))
    try:
        err_lines = read_lines(heartbeat_err_path)
    except OSError:
        err_lines = []

    window_start = datetime.combine(
        report_date - timedelta(days=1), _aftermarket_close_time(), tzinfo=ET
    )
    window_end = SessionClock.to_et(now)

    headers = all_beat_headers(log_lines)
    in_window = sorted(h.at for h in headers if window_start <= h.at <= window_end)
    count = len(in_window)
    gaps = [(b - a).total_seconds() / 60 for a, b in zip(in_window, in_window[1:])]
    max_gap = max(gaps) if gaps else None

    fails = [(ts, line) for ts, line in failed_lines(err_lines) if window_start <= ts <= window_end]

    raw = "\n".join(
        [
            f"window: {window_start:%Y-%m-%d %H:%M} ET .. {window_end:%Y-%m-%d %H:%M} ET",
            f"beats in window: {count}",
            *[f"  {ts:%Y-%m-%d %H:%M:%S}" for ts in in_window],
            f"max gap (min): {max_gap:.1f}" if max_gap is not None else "max gap (min): n/a (fewer than 2 beats)",
            f"FAILED lines in window: {len(fails)}",
            *[f"  {ts:%Y-%m-%d %H:%M:%S} {line}" for ts, line in fails],
        ]
    )

    if count == 0:
        return CheckResult("C6", title, Verdict.FAIL, f"FAIL — no beats since {window_start:%Y-%m-%d %H:%M} ET", raw)
    if fails:
        return CheckResult(
            "C6", title, Verdict.FAIL,
            f"FAIL — {len(fails)} FAILED line(s) in heartbeat.err since {window_start:%H:%M} ET",
            raw,
        )
    if max_gap is not None and max_gap > max_gap_min:
        return CheckResult(
            "C6", title, Verdict.FAIL,
            f"FAIL — max gap {max_gap:.1f} min > dayopen.c6_max_gap_min ({max_gap_min} min)",
            raw,
        )
    return CheckResult(
        "C6", title, Verdict.PASS,
        f"PASS — {count} beat(s), max gap {max_gap if max_gap is not None else 0.0:.1f} min, no FAILED lines",
        raw,
    )


__all__ = [
    "ARCHIVER_ERR_PATH",
    "ARCHIVER_RUNS_PATH",
    "C4_ACTOR_PATTERN",
    "HEARTBEAT_ERR_PATH",
    "HEARTBEAT_LOG_PATH",
    "check_c1_radar_launchd",
    "check_c2_radar_membership",
    "check_c3_radar_beat_line",
    "check_c4_session_blocks",
    "check_c5_archiver_last_run",
    "check_c6_beats_since_prior_evening",
    "previous_trading_day",
]
