"""`cobalt smoke s2` (S2-P4 STEP-9, R6) — offline, every probe on fakes.

§4 Smoke sentences, one test each, plus one test per check KIND
(launchctl, sql, http, log_grep, job_row, vault_unit, cli). No database,
no launchd, no network, no vault: every collector is a `SmokeDeps` field
and each test hands in its own fake. The committed suite
(`configs/cobalt/smoke/s2.yaml`) is loaded for real, so a check whose
shape the code cannot run fails here, not on the S2 close evening.

The one DB-backed test (`requires_db`) runs every committed SQL/job_row
query on cobalt_dev through `cobalt db query`'s read path; the hub runs
it (L41 interim) and it skips cleanly offline.
"""

from __future__ import annotations

import ast
import json
import os
import re
import shlex
from datetime import date, datetime, timedelta, timezone
from decimal import Decimal
from pathlib import Path
from zoneinfo import ZoneInfo

import pytest

from cobalt.dayopen.launchd import LaunchdPrintError, LaunchdPrintStatus
from cobalt.db_query import QueryRows
from cobalt.smoke import checks, cli, report
from cobalt.smoke.config import SUITES_DIR, SmokeConfigError, load_suite
from cobalt.smoke.models import (
    CheckOutcome,
    CliCheck,
    HttpCheck,
    JobRowCheck,
    LaunchctlCheck,
    LogGrepCheck,
    Overall,
    SmokeContext,
    SqlCheck,
    Verdict,
    VaultUnitCheck,
    overall_verdict,
)

ET = ZoneInfo("America/New_York")
REPO = Path(__file__).resolve().parents[2]
SMOKE_SRC = REPO / "src" / "cobalt" / "smoke"

#: Tuesday 2026-09-22, 21:50 ET — after that evening's 21:10 replay + its
#: 1800 s timeout (ends 21:40), the S2 close evening (plan §6).
NOW = datetime(2026, 9, 22, 21, 50, tzinfo=ET).astimezone(timezone.utc)
DAY = date(2026, 9, 22)
CUTOFF = datetime(2026, 9, 18, 20, 5, tzinfo=ET)

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: Postgres env settings not available",
)


# ---------------------------------------------------------------------
# fakes
# ---------------------------------------------------------------------


def ctx(**overrides) -> SmokeContext:
    values = dict(
        now=NOW,
        report_date=DAY,
        session="overnight",
        cutoff=CUTOFF,
        last_trading_day=DAY,
        last_summary_slot="16:30",
        last_summary_date=DAY,
        prod=True,
        tunables={"heartbeat.radar_scan_max_age_s": 900},
    )
    values.update(overrides)
    return SmokeContext(**values)


def rows(columns, *data) -> QueryRows:
    return QueryRows(columns=tuple(columns), rows=[tuple(r) for r in data])


def _unexpected(name):
    def fail(*_a, **_k):
        raise AssertionError(f"this test did not expect a {name} call")

    return fail


def deps(**overrides) -> checks.SmokeDeps:
    values = dict(
        read_rows=_unexpected("read_rows"),
        launchctl_print=_unexpected("launchctl_print"),
        launchctl_loaded=_unexpected("launchctl_loaded"),
        http_get=_unexpected("http_get"),
        read_text=_unexpected("read_text"),
        run_cli=_unexpected("run_cli"),
        job_specs=_unexpected("job_specs"),
        drc_note_path=_unexpected("drc_note_path"),
        missed_grace=lambda: timedelta(minutes=30),
    )
    values.update(overrides)
    return checks.SmokeDeps(**values)


def _job_row(**overrides):
    base = dict(
        label="com.cobalt.replay",
        state="done",
        exit_code=0,
        # tonight's run: started just after the 21:10 occurrence (R17 moved
        # it from 21:05), finished well inside the 1800 s timeout.
        started_at=datetime(2026, 9, 22, 21, 10, 1, tzinfo=ET),
        finished_at=datetime(2026, 9, 22, 21, 14, 30, tzinfo=ET),
        updated_at=datetime(2026, 9, 22, 21, 14, 30, tzinfo=ET),
        registered_at=datetime(2026, 9, 18, 20, 10, tzinfo=ET),
        last_result={
            "trade_date": "2026-09-22", "dry_run": False, "movers": 40, "archived": 12,
            "card_misses": 2, "mover_misses": 3, "formation_replay": "unavailable",
            "line_action": "updated", "rows_written": 5,
            "summary_sent": {"07:00": "2026-09-22", "16:30": "2026-09-22"},
        },
    )
    base.update(overrides)
    columns = list(base)
    return rows(columns, [base[c] for c in columns])


# ---------------------------------------------------------------------
# §4: schema, bad file crashes with a line
# ---------------------------------------------------------------------


def _write(tmp_path, text) -> Path:
    path = tmp_path / "s9.yaml"
    path.write_text(text)
    return path


GOOD_HEAD = "suite: s9\ntitle: test\nday_anchor_job: com.cobalt.replay\nchecks:\n"


def test_smoke_checks_load_through_schema_bad_file_crashes_with_line(tmp_path):
    # The committed suite loads, whole, through the schema.
    suite = load_suite(SUITES_DIR / "s2.yaml")
    ids = [c.id for c in suite.checks]
    assert {i.split(".")[0] for i in ids} == {f"K{n}" for n in range(1, 19)}
    assert len(ids) == len(set(ids))

    # A validation error names the line of the offending value.
    bad_op = GOOD_HEAD + (
        "  - id: K1\n"                      # 5
        "    title: t\n"                     # 6
        "    kind: sql\n"                    # 7
        "    side: system\n"                 # 8
        "    query: SELECT 1 AS x\n"         # 9
        "    expect_text: x\n"               # 10
        "    expect:\n"                      # 11
        "      - {column: x, op: bogus}\n"   # 12
    )
    with pytest.raises(SmokeConfigError) as raised:
        load_suite(_write(tmp_path, bad_op))
    assert raised.value.line == 12
    assert ":12:" in str(raised.value)

    # A missing required field names the check's own line.
    missing_side = GOOD_HEAD + (
        "  - id: K1\n"                       # 5
        "    title: t\n"
        "    kind: sql\n"
        "    query: SELECT 1 AS x\n"
        "    expect_text: x\n"
        "    expect: [{column: x, op: eq, value: 1}]\n"
    )
    with pytest.raises(SmokeConfigError) as raised:
        load_suite(_write(tmp_path, missing_side))
    assert raised.value.line == 5
    assert "side" in str(raised.value)

    # A YAML syntax error carries the parser's line.
    with pytest.raises(SmokeConfigError) as raised:
        load_suite(_write(tmp_path, GOOD_HEAD + "  - id: K1\n    title: [unclosed\n"))
    assert raised.value.line is not None and ":" in str(raised.value)

    # A write statement never loads (the read path's own guard).
    write_sql = GOOD_HEAD + (
        "  - id: K1\n"
        "    title: t\n"
        "    kind: sql\n"
        "    side: user\n"
        "    query: DELETE FROM picks\n"     # 9
        "    expect_text: x\n"
        "    expect: [{column: x, op: eq, value: 1}]\n"
    )
    with pytest.raises(SmokeConfigError) as raised:
        load_suite(_write(tmp_path, write_sql))
    assert raised.value.line == 9 and "DELETE" in str(raised.value)

    # A cli argv off the read-only allowlist never loads.
    writer_cli = GOOD_HEAD + (
        "  - id: K1\n"
        "    title: t\n"
        "    kind: cli\n"
        "    argv: [cobalt, heartbeat, beat]\n"  # 8
        "    expect_text: x\n"
    )
    with pytest.raises(SmokeConfigError) as raised:
        load_suite(_write(tmp_path, writer_cli))
    assert raised.value.line == 8

    # An unknown variable never loads.
    unknown_var = GOOD_HEAD + (
        "  - id: K1\n"
        "    title: t\n"
        "    kind: sql\n"
        "    side: user\n"
        "    query: SELECT {yesterday} AS x\n"  # 9
        "    expect_text: x\n"
        "    expect: [{column: x, op: eq, value: 1}]\n"
    )
    with pytest.raises(SmokeConfigError) as raised:
        load_suite(_write(tmp_path, unknown_var))
    assert raised.value.line == 9 and "yesterday" in str(raised.value)

    # Duplicate ids never load.
    dup = GOOD_HEAD + "".join(
        f"  - id: K1\n    title: t\n    kind: http\n    url: http://127.0.0.1:1/\n    expect_text: x\n"
        for _ in range(2)
    )
    with pytest.raises(SmokeConfigError):
        load_suite(_write(tmp_path, dup))

    # An absent file crashes; it never runs an empty checklist.
    with pytest.raises(SmokeConfigError):
        load_suite(tmp_path / "absent.yaml")


# ---------------------------------------------------------------------
# §4: the roll-up
# ---------------------------------------------------------------------


def _outcome(verdict: Verdict, cid="K1") -> CheckOutcome:
    return CheckOutcome(
        id=cid, title="t", kind="http", verdict=verdict, detail="d",
        command="c", expected="e", raw="r",
    )


def test_verdict_red_on_error_amber_on_fail_known_never_lowers():
    P, F, K, E = Verdict.PASS, Verdict.FAIL, Verdict.KNOWN, Verdict.ERROR
    assert overall_verdict([_outcome(P)]) is Overall.GREEN
    assert overall_verdict([_outcome(P), _outcome(K)]) is Overall.GREEN
    assert overall_verdict([_outcome(K), _outcome(K)]) is Overall.GREEN
    assert overall_verdict([_outcome(P), _outcome(F)]) is Overall.AMBER
    assert overall_verdict([_outcome(K), _outcome(F)]) is Overall.AMBER
    assert overall_verdict([_outcome(F), _outcome(E)]) is Overall.RED
    assert overall_verdict([_outcome(K), _outcome(E)]) is Overall.RED
    # An empty check list is not GREEN: nothing looked.
    with pytest.raises(ValueError):
        overall_verdict([])


# ---------------------------------------------------------------------
# §4: sentinels — imports no writer, calls no write
# ---------------------------------------------------------------------

#: Every name that opens a write in the new core. The smoke package's own
#: source may not import or reference one.
WRITER_NAMES = {
    "VaultWriter", "VaultWriteStore", "upsert_unit", "create_if_absent", "write_miss_line",
    "JobStore", "job_run", "as_job", "sweep", "run_beat", "take_beat",
    "TraderSettingsStore", "CardStore", "AsetStore", "RadarStore", "BarStore",
    "MissedStore", "MoversStore", "SessionBlockStore", "ensure_schema", "connect_migration",
}
WRITER_MODULES = {
    "cobalt.vaultwrite.writer", "cobalt.vaultwrite.store", "cobalt.jobs.store",
    "cobalt.jobs.wrapper", "cobalt.settings.store", "cobalt.replay.line",
    "cobalt.replay.runner", "cobalt.prefill.vault_writer", "cobalt.cards.store",
    "cobalt.aset.store", "cobalt.radar.store", "cobalt.archiver.store",
}


def test_smoke_imports_no_writer_and_calls_no_write(tmp_path, monkeypatch):
    # 1) static: no writer module imported, no writer name referenced.
    offenders = []
    for path in sorted(SMOKE_SRC.glob("*.py")):
        tree = ast.parse(path.read_text(), filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node, ast.ImportFrom):
                module = node.module or ""
                if module in WRITER_MODULES or module == "cobalt.vaultwrite":
                    offenders.append(f"{path.name}: from {module} import …")
                offenders += [f"{path.name}: imports {a.name}" for a in node.names if a.name in WRITER_NAMES]
            elif isinstance(node, ast.Import):
                offenders += [f"{path.name}: import {a.name}" for a in node.names if a.name in WRITER_MODULES]
            elif isinstance(node, ast.Name) and node.id in WRITER_NAMES:
                offenders.append(f"{path.name}: references {node.id}")
            elif isinstance(node, ast.Attribute) and node.attr in WRITER_NAMES:
                offenders.append(f"{path.name}: references .{node.attr}")
    assert offenders == []

    # 2) runtime: the whole committed suite, run through the CLI entry,
    # with every write surface in the new core armed to explode.
    tripped: list[str] = []

    def sentinel(name):
        def boom(*_a, **_k):
            tripped.append(name)
            raise AssertionError(f"smoke called a write: {name}")

        return boom

    from cobalt import db
    from cobalt.jobs.store import JobStore
    from cobalt.settings.store import TraderSettingsStore
    from cobalt.vaultwrite.store import VaultWriteStore
    from cobalt.vaultwrite.writer import VaultWriter

    for cls, names in (
        (VaultWriter, ["upsert_unit", "upsert_region", "create_if_absent", "restore"]),
        (VaultWriteStore, ["ensure_schema", "pending_write", "purge_expired"]),
        (JobStore, ["ensure_schema", "register", "register_all", "mark_running", "beat",
                    "mark_finished", "mark_wrapper_finished", "record_heartbeat_result",
                    "mark_zombie", "mark_probe", "set_kill_switch"]),
        (TraderSettingsStore, ["ensure_schema", "put"]),
    ):
        for name in names:
            # A renamed write method must fail here, not silently un-arm.
            assert hasattr(cls, name), f"{cls.__name__}.{name} no longer exists"
            monkeypatch.setattr(cls, name, sentinel(f"{cls.__name__}.{name}"))
    monkeypatch.setattr(db, "connect", sentinel("db.connect"))
    monkeypatch.setattr(db, "connect_migration", sentinel("db.connect_migration"))
    import subprocess

    monkeypatch.setattr(subprocess, "run", sentinel("subprocess.run"))
    monkeypatch.setattr(subprocess, "Popen", sentinel("subprocess.Popen"))

    drc = tmp_path / "drc.md"
    drc.write_text(
        "# DRC\n<!-- cobalt:section drc-misses -->\n<!-- cobalt:unit miss_line -->\n"
        "Misses …\n<!-- /cobalt:unit miss_line -->\n<!-- /cobalt:section drc-misses -->\n"
    )
    seen_sql: list[str] = []

    def read_rows(statement, side):
        seen_sql.append(statement)
        return rows(["x"], [1])

    fakes = deps(
        read_rows=read_rows,
        launchctl_print=lambda label: LaunchdPrintStatus(label, "running", 1, "(never exited)", 1, "state = running"),
        launchctl_loaded=lambda label: True,
        http_get=lambda url: (200, "<th>value</th>"),
        read_text=lambda path: "HEARTBEAT GREEN — x (2026-09-22 21:45:00 EDT)\nOK   database  ok\nOK   sheet HTTP  ok\n",
        run_cli=lambda argv: (0, "ok"),
        job_specs=lambda: checks.load_job_specs(),
        drc_note_path=lambda day: drc,
    )
    result = cli.run("s2", cutoff=CUTOFF, now=NOW, prod=True, deps=fakes)
    assert tripped == []
    assert seen_sql, "the sql checks never reached the read path"
    # Every outcome came from a probe that ran (fakes answer loosely, so
    # FAIL/ERROR verdicts are expected) — never from a tripped sentinel.
    assert all("smoke called a write" not in o.detail for o in result.checks)


# ---------------------------------------------------------------------
# §4: the report file
# ---------------------------------------------------------------------


def _report(verdicts=(Verdict.PASS, Verdict.KNOWN, Verdict.FAIL)):
    outcomes = [_outcome(v, cid=f"K{i + 1}") for i, v in enumerate(verdicts)]
    return report.build_report("s2", "S2 smoke", ctx(), outcomes)


def test_smoke_writes_report_file_with_table(tmp_path):
    rep = _report()
    path = report.write_report(rep, reports_dir=tmp_path)
    assert path.name == "s2-smoke-2026-09-22.md"
    text = path.read_text()
    assert "| # | check | verdict | evidence |" in text
    for outcome in rep.checks:
        assert f"| {outcome.id} | {outcome.title} | {outcome.verdict.value} |" in text
    assert "OVERALL: AMBER" in text
    # The variables the commands were rendered with head the file.
    assert f"cutoff: {CUTOFF.isoformat()}" in text
    assert "last_trading_day: 2026-09-22" in text
    # Each row's exact command and expected output are in the file (R1-24).
    assert text.count("command:") == len(rep.checks)
    assert text.count("expected:") == len(rep.checks)

    # A second run the same day lands beside the first, never over it.
    first = path.read_text()
    second = report.write_report(rep, reports_dir=tmp_path)
    assert second != path and second.name.startswith("s2-smoke-2026-09-22-")
    assert path.read_text() == first


def test_json_flag_prints_and_writes_nothing(monkeypatch, capsys, tmp_path):
    rep = _report((Verdict.PASS,))
    monkeypatch.setattr(cli, "run", lambda *a, **k: rep)
    monkeypatch.setattr(report, "REPORTS_DIR", tmp_path)
    args = cli.build_parser().parse_args(
        ["smoke", "s2", "--cutoff", CUTOFF.isoformat(), "--json"]
    )
    args.func(args)
    payload = json.loads(capsys.readouterr().out)
    assert payload["overall"] == "GREEN" and payload["checks"][0]["id"] == "K1"
    assert list(tmp_path.iterdir()) == []


def test_cutoff_is_required_and_must_carry_an_offset():
    parser = cli.build_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["smoke", "s2"])
    with pytest.raises(SystemExit):
        parser.parse_args(["smoke", "s2", "--cutoff", "2026-09-18T20:05:00"])


# ---------------------------------------------------------------------
# One test per check kind, on fakes
# ---------------------------------------------------------------------


def test_kind_launchctl_running_and_registry_match():
    running = LaunchctlCheck(id="K1", title="radar", kind="launchctl", mode="running",
                             label="com.cobalt.radar", expect_text="running")
    up = LaunchdPrintStatus("com.cobalt.radar", "running", 42, "(never exited)", 3, "state = running\npid = 42")
    down = LaunchdPrintStatus("com.cobalt.radar", "not running", None, "1", 3, "state = not running")

    out = checks.evaluate(running, ctx(), deps(launchctl_print=lambda label: up))
    assert out.verdict is Verdict.PASS and "pid = 42" in out.raw
    assert out.command == "launchctl print gui/$(id -u)/com.cobalt.radar"
    assert checks.evaluate(running, ctx(), deps(launchctl_print=lambda label: down)).verdict is Verdict.FAIL

    def broken(label):
        raise LaunchdPrintError("exited 113")

    assert checks.evaluate(running, ctx(), deps(launchctl_print=broken)).verdict is Verdict.ERROR

    match = LaunchctlCheck(id="K18", title="drift", kind="launchctl", mode="registry_match",
                           expect_text="no drift")

    class Spec:
        def __init__(self, label, enabled):
            self.label, self.enabled = label, enabled

    specs = [Spec("com.cobalt.radar", True), Spec("com.cobalt.replay", True), Spec("com.cobalt.agent", False)]
    loaded = {"com.cobalt.radar": True, "com.cobalt.replay": True, "com.cobalt.agent": False}
    out = checks.evaluate(match, ctx(), deps(job_specs=lambda: specs, launchctl_loaded=loaded.__getitem__))
    assert out.verdict is Verdict.PASS

    drift = dict(loaded, **{"com.cobalt.replay": False, "com.cobalt.agent": True})
    out = checks.evaluate(match, ctx(), deps(job_specs=lambda: specs, launchctl_loaded=drift.__getitem__))
    assert out.verdict is Verdict.FAIL
    assert "com.cobalt.replay" in out.detail and "com.cobalt.agent" in out.detail


def test_kind_sql_renders_literals_through_the_read_path_and_grades_rows():
    check = SqlCheck.model_validate({
        "id": "K6", "title": "picks", "kind": "sql", "side": "user",
        "query": "SELECT count(*) AS fills, count(*) AS missing FROM card_transitions WHERE at >= {cutoff}",
        "known_if": [{"column": "fills", "op": "eq", "value": 0}],
        "known_text": "no fill yet",
        "expect": [{"column": "missing", "op": "eq", "value": 0}],
        "expect_text": "missing = 0",
    })
    calls = []

    def answer(result):
        def read_rows(statement, side):
            calls.append((statement, side))
            return result

        return read_rows

    out = checks.evaluate(check, ctx(), deps(read_rows=answer(rows(["fills", "missing"], [3, 0]))))
    statement, side = calls[-1]
    assert side == "user"
    assert "TIMESTAMPTZ '2026-09-18T20:05:00-04:00'" in statement and "{" not in statement
    assert out.verdict is Verdict.PASS
    # The hand command is the same statement through `cobalt db query`.
    assert out.command.startswith("uv run cobalt db query --side user --prod --format json ")
    assert shlex.split(out.command)[-1] == statement

    assert checks.evaluate(check, ctx(), deps(read_rows=answer(rows(["fills", "missing"], [3, 1])))).verdict is Verdict.FAIL
    known = checks.evaluate(check, ctx(), deps(read_rows=answer(rows(["fills", "missing"], [0, 0]))))
    assert known.verdict is Verdict.KNOWN and "no fill yet" in known.detail
    # No row is a finding; two rows is a broken probe.
    assert checks.evaluate(check, ctx(), deps(read_rows=answer(rows(["fills", "missing"])))).verdict is Verdict.FAIL
    assert checks.evaluate(check, ctx(), deps(read_rows=answer(rows(["fills", "missing"], [1, 0], [2, 0])))).verdict is Verdict.ERROR
    # A predicate naming a column the query does not return is a broken probe.
    assert checks.evaluate(check, ctx(), deps(read_rows=answer(rows(["other"], [0])))).verdict is Verdict.ERROR

    def refused(statement, side):
        raise RuntimeError("connection refused")

    assert checks.evaluate(check, ctx(), deps(read_rows=refused)).verdict is Verdict.ERROR

    # requires_relation: an absent relation is a FAIL, named, and the
    # main query never runs.
    seam = SqlCheck.model_validate({
        "id": "K5.1", "title": "seam", "kind": "sql", "side": "system",
        "requires_relation": "system.radar_score_run",
        "query": "SELECT (SELECT status FROM system.radar_score_run LIMIT 1) AS latest_status",
        "expect": [{"column": "latest_status", "op": "eq", "value": "complete"}],
        "expect_text": "complete",
    })
    calls.clear()
    out = checks.evaluate(seam, ctx(), deps(read_rows=answer(rows(["present"], [False]))))
    assert out.verdict is Verdict.FAIL and "system.radar_score_run" in out.detail
    assert len(calls) == 1 and "to_regclass('system.radar_score_run')" in calls[0][0]

    # Per-predicate `known`: a failing value listed there is KNOWN, not FAIL.
    pool = SqlCheck.model_validate({
        "id": "K2", "title": "pool", "kind": "sql", "side": "system",
        "query": "SELECT failed_stage, members FROM system.radar_pool",
        "expect": [
            {"column": "failed_stage", "op": "is_null", "known": ["bars"]},
            {"column": "members", "op": "le", "value": 50},
        ],
        "expect_text": "x",
    })
    assert checks.evaluate(pool, ctx(), deps(read_rows=answer(rows(["failed_stage", "members"], ["bars", Decimal("50")])))).verdict is Verdict.KNOWN
    assert checks.evaluate(pool, ctx(), deps(read_rows=answer(rows(["failed_stage", "members"], ["mirror", 50])))).verdict is Verdict.FAIL
    assert checks.evaluate(pool, ctx(), deps(read_rows=answer(rows(["failed_stage", "members"], ["bars", 51])))).verdict is Verdict.FAIL

    # Tunables and dates render as literals; a date compares to its text.
    rendered = checks.render_sql("SELECT {tunable:heartbeat.radar_scan_max_age_s}, {last_trading_day}, {session}", ctx())
    assert rendered == "SELECT 900, DATE '2026-09-22', 'overnight'"
    assert checks.render_sql("SELECT {session}", ctx(session="o'x")) == "SELECT 'o''x'"


def test_kind_http_status_and_body():
    check = HttpCheck(id="K4.3", title="radar", kind="http", url="http://127.0.0.1:5010/radar",
                      status=200, contains=["<th>value</th>"], expect_text="200")
    out = checks.evaluate(check, ctx(), deps(http_get=lambda url: (200, "<table><th>value</th>")))
    assert out.verdict is Verdict.PASS
    assert "curl" in out.command and "http://127.0.0.1:5010/radar" in out.command
    assert checks.evaluate(check, ctx(), deps(http_get=lambda url: (200, "<th>rank</th>"))).verdict is Verdict.FAIL
    assert checks.evaluate(check, ctx(), deps(http_get=lambda url: (500, "<th>value</th>"))).verdict is Verdict.FAIL

    def down(url):
        raise ConnectionRefusedError("refused")

    assert checks.evaluate(check, ctx(), deps(http_get=down)).verdict is Verdict.ERROR


def test_kind_log_grep_reads_only_the_newest_block():
    check = LogGrepCheck(id="K11.2", title="db", kind="log_grep", path="logs/heartbeat.log",
                         block_start="^HEARTBEAT ", pattern="^OK +database ", present=True,
                         expect_text="OK database")
    log = (
        "HEARTBEAT GREEN — all (2026-09-22 21:30:00 EDT)\n\nOK   database                 cobalt_brain reachable\n"
        "HEARTBEAT RED — 1 (2026-09-22 21:45:00 EDT)\n\nRED  database                 unreachable\n"
    )
    seen = []

    def read_text(path):
        seen.append(path)
        return log

    out = checks.evaluate(check, ctx(), deps(read_text=read_text))
    # The older block's OK line does not rescue the newest block's RED.
    assert out.verdict is Verdict.FAIL
    assert seen == [checks.REPO_ROOT / "logs" / "heartbeat.log"]
    assert "logs/heartbeat.log" in out.command and "grep -E" in out.command

    healthy = log.replace("RED  database                 unreachable", "OK   database                 cobalt_brain reachable")
    assert checks.evaluate(check, ctx(), deps(read_text=lambda p: healthy)).verdict is Verdict.PASS

    absent = LogGrepCheck(id="K9", title="no failed", kind="log_grep", path="logs/replay.err",
                          pattern="FAILED", present=False, expect_text="none")
    assert checks.evaluate(absent, ctx(), deps(read_text=lambda p: "ok\n")).verdict is Verdict.PASS
    assert checks.evaluate(absent, ctx(), deps(read_text=lambda p: "x FAILED y\n")).verdict is Verdict.FAIL

    assert checks.evaluate(check, ctx(), deps(read_text=lambda p: "no beats\n")).verdict is Verdict.ERROR

    def unreadable(path):
        raise FileNotFoundError(path)

    assert checks.evaluate(check, ctx(), deps(read_text=unreadable)).verdict is Verdict.ERROR

    with pytest.raises(ValueError):
        LogGrepCheck(id="K1", title="t", kind="log_grep", path="../secrets", pattern="x", expect_text="x")


def test_kind_job_row_state_cadence_age_and_result():
    from cobalt.jobs.config import load_job_registry

    registry = load_job_registry()
    spec_of = lambda: registry.jobs  # noqa: E731
    check = JobRowCheck.model_validate({
        "id": "K7", "title": "replay", "kind": "job_row", "label": "com.cobalt.replay",
        "state": "done", "exit_code": 0, "not_missed": True,
        "result_keys": ["movers", "card_misses"],
        "result_equals": {"trade_date": "{last_trading_day}", "dry_run": False},
        "expect_text": "done",
    })
    calls = []

    def answer(result):
        def read_rows(statement, side):
            calls.append((statement, side))
            return result

        return read_rows

    out = checks.evaluate(check, ctx(), deps(read_rows=answer(_job_row()), job_specs=spec_of))
    assert out.verdict is Verdict.PASS, out.detail
    statement, side = calls[-1]
    assert side == "system" and "FROM cobalt_jobs WHERE label = 'com.cobalt.replay'" in statement
    assert out.command.startswith("uv run cobalt db query --side system --prod --format json ")

    assert checks.evaluate(check, ctx(), deps(read_rows=answer(_job_row(state="failed", exit_code=1)), job_specs=spec_of)).verdict is Verdict.FAIL
    # Yesterday's run tonight is MISSED (21:10 + the 30 min grace passed by
    # 21:50, and no finish after tonight's due moment).
    stale = _job_row(finished_at=datetime(2026, 9, 21, 21, 9, tzinfo=ET))
    out = checks.evaluate(check, ctx(), deps(read_rows=answer(stale), job_specs=spec_of))
    assert out.verdict is Verdict.FAIL and "missed" in out.detail.lower()
    wrong_day = _job_row(last_result={**_job_row().rows[0][-1], "trade_date": "2026-09-21"})
    assert checks.evaluate(check, ctx(), deps(read_rows=answer(wrong_day), job_specs=spec_of)).verdict is Verdict.FAIL
    no_keys = _job_row(last_result={"trade_date": "2026-09-22", "dry_run": False})
    assert checks.evaluate(check, ctx(), deps(read_rows=answer(no_keys), job_specs=spec_of)).verdict is Verdict.FAIL
    assert checks.evaluate(check, ctx(), deps(read_rows=answer(rows(["label"])), job_specs=spec_of)).verdict is Verdict.FAIL

    beat = JobRowCheck(id="K11.1", title="beat", kind="job_row", label="com.cobalt.heartbeat",
                       max_age_min=20, expect_text="fresh")
    fresh = _job_row(label="com.cobalt.heartbeat", updated_at=NOW - timedelta(minutes=5))
    old = _job_row(label="com.cobalt.heartbeat", updated_at=NOW - timedelta(minutes=25))
    assert checks.evaluate(beat, ctx(), deps(read_rows=answer(fresh))).verdict is Verdict.PASS
    assert checks.evaluate(beat, ctx(), deps(read_rows=answer(old))).verdict is Verdict.FAIL

    summary = JobRowCheck.model_validate({
        "id": "K15", "title": "summary", "kind": "job_row", "label": "com.cobalt.heartbeat",
        "result_equals": {"summary_sent.{last_summary_slot}": "{last_summary_date}"},
        "expect_text": "sent",
    })
    assert checks.evaluate(summary, ctx(), deps(read_rows=answer(fresh))).verdict is Verdict.PASS
    unsent = _job_row(last_result={"summary_sent": {"07:00": "2026-09-22", "16:30": "2026-09-21"}})
    assert checks.evaluate(summary, ctx(), deps(read_rows=answer(unsent))).verdict is Verdict.FAIL

    archiver = JobRowCheck(id="K13", title="archiver", kind="job_row", label="com.cobalt.archiver",
                           exit_code=0, result_positive=["rows_written"], expect_text="rows")
    empty = _job_row(label="com.cobalt.archiver", last_result={"rows_written": 0})
    assert checks.evaluate(archiver, ctx(), deps(read_rows=answer(empty))).verdict is Verdict.FAIL


def test_kind_vault_unit_reads_markers_and_never_creates(tmp_path):
    check = VaultUnitCheck(id="K10.1", title="miss line", kind="vault_unit", note="drc",
                           day="last_trading_day", section="drc-misses", unit="miss_line",
                           expect_text="present")
    note = tmp_path / "2026-09-22 DRC.md"
    body = (
        "# DRC\n<!-- cobalt:section drc-rules -->\n<!-- /cobalt:section drc-rules -->\n"
        "<!-- cobalt:section drc-misses -->\n<!-- cobalt:unit miss_line -->\n"
        "Misses 2026-09-22: cards 2\n<!-- /cobalt:unit miss_line -->\n"
        "<!-- /cobalt:section drc-misses -->\n"
    )
    note.write_text(body)
    asked = []

    def path_for(day):
        asked.append(day)
        return note

    out = checks.evaluate(check, ctx(), deps(drc_note_path=path_for, read_text=lambda p: p.read_text()))
    assert out.verdict is Verdict.PASS and "Misses 2026-09-22" in out.raw
    assert asked == [DAY]
    assert "grep -n -F" in out.command and str(note) in out.command
    assert note.read_text() == body

    no_unit = body.replace("<!-- cobalt:unit miss_line -->\n", "").replace("<!-- /cobalt:unit miss_line -->\n", "")
    note.write_text(no_unit)
    assert checks.evaluate(check, ctx(), deps(drc_note_path=path_for, read_text=lambda p: p.read_text())).verdict is Verdict.FAIL

    note.write_text(body.replace("<!-- /cobalt:section drc-misses -->\n", "<!-- /cobalt:section drc-misses -->\n<!-- /cobalt:section drc-misses -->\n"))
    assert checks.evaluate(check, ctx(), deps(drc_note_path=path_for, read_text=lambda p: p.read_text())).verdict is Verdict.ERROR

    absent = tmp_path / "absent.md"
    out = checks.evaluate(check, ctx(), deps(drc_note_path=lambda d: absent, read_text=lambda p: p.read_text()))
    assert out.verdict is Verdict.FAIL and not absent.exists()


def test_kind_cli_exit_code_through_the_allowlist():
    check = CliCheck(id="K17", title="validate", kind="cli", argv=["cobalt", "validate"],
                     exit_code=0, expect_text="exit 0")
    ran = []

    def run_cli(argv):
        ran.append(argv)
        return 0, "Placement (docs/PLACEMENT.md): tree clean."

    out = checks.evaluate(check, ctx(), deps(run_cli=run_cli))
    assert out.verdict is Verdict.PASS and ran == [["cobalt", "validate"]]
    assert out.command == "uv run cobalt validate"
    assert checks.evaluate(check, ctx(), deps(run_cli=lambda argv: (1, "FAILED: x"))).verdict is Verdict.FAIL

    def missing(argv):
        raise FileNotFoundError("uv")

    assert checks.evaluate(check, ctx(), deps(run_cli=missing)).verdict is Verdict.ERROR
    with pytest.raises(ValueError):
        CliCheck(id="K1", title="t", kind="cli", argv=["cobalt", "jobs", "check"], expect_text="x")


# ---------------------------------------------------------------------
# R1-24: every committed K row carries its exact command and expected output
# ---------------------------------------------------------------------


def test_every_committed_check_renders_an_exact_command_and_expected_output():
    suite = load_suite(SUITES_DIR / "s2.yaml")
    for check in suite.checks:
        command = checks.command_for(check, ctx())
        assert command and "{" not in command.replace("'%{http_code}'", ""), check.id
        assert check.expect_text.strip(), check.id
    by_id = {c.id: c for c in suite.checks}
    assert by_id["K6"].known_text == "no fill yet"
    assert by_id["K5.1"].requires_relation == "system.radar_score_run"
    assert by_id["K3"].known_if and by_id["K3"].expect


# ---------------------------------------------------------------------
# K3 reaches BOTH paths that write the value pair (R1-19)
# ---------------------------------------------------------------------

#: What K3's statement must name to grade both writers of
#: `rank_metric`/`rank_value`. The INSERT path is keyed on `first_seen_at`
#: — an episode BORN after the deploy. The RETAIN path is not: a
#: pre-deploy episode retained tonight keeps its old `first_seen_at`, and
#: `radar/store.py`'s RETAIN branch writes `rank_metric = %s`
#: unconditionally, so a defect there is reachable only through the pool's
#: own `last_scan_id`, gated on that scan having run after the cutoff.
K3_REQUIRED_CLAUSES = (
    "first_seen_at >= {cutoff}",
    "left_at IS NULL",
    "last_scan_id",
    "system.radar_pool",
    "last_scan_at >= {cutoff}",
)
#: One graded column per set, and one `known_if` count per set — the
#: "no admitted row yet → KNOWN" semantics hold for the UNION, so both
#: counts must be zero before the check goes quiet.
K3_GRADED = ("metric_missing", "rescanned_metric_missing")
K3_KNOWN_COUNTS = ("post_deploy_admitted", "rescanned_admitted")


def k3_gaps(check) -> list[str]:
    """Every clause or predicate K3 needs and does not have."""
    query = " ".join(check.query.split())
    gaps = [f"query does not name {needle!r}" for needle in K3_REQUIRED_CLAUSES
            if needle not in query]
    graded = {p.column for p in check.expect}
    gaps += [f"no expect predicate on {column}" for column in K3_GRADED if column not in graded]
    known = {p.column for p in check.known_if}
    gaps += [f"no known_if predicate on {column}" for column in K3_KNOWN_COUNTS
             if column not in known]
    return gaps


def _k3():
    return {c.id: c for c in load_suite(SUITES_DIR / "s2.yaml").checks}["K3"]


def test_k3_covers_the_insert_path_and_the_retain_path():
    check = _k3()
    assert k3_gaps(check) == []
    # It stays on the system side: both relations it reads are system's.
    assert check.kind == "sql" and check.side == "system"
    assert '"user".' not in check.query
    # Both cutoff gates render as the same literal in the hand command.
    assert check.query.count("{cutoff}") == 2
    assert checks.command_for(check, ctx()).count(CUTOFF.isoformat()) == 2


def test_the_k3_coverage_check_refuses_the_first_seen_at_only_shape():
    """The bite proof: K3 as it read before this fix — only the INSERT
    path — is refused, and so is dropping either half of the grading."""
    old_k3 = SqlCheck.model_validate({
        "id": "K3", "title": "membership value column (post-deploy admissions)",
        "kind": "sql", "side": "system",
        "query": (
            "SELECT count(*) AS post_deploy_admitted, "
            "count(*) FILTER (WHERE rank_metric IS NULL) AS metric_missing, "
            "count(*) FILTER (WHERE rank_value IS NULL) AS value_null "
            "FROM system.radar_membership "
            "WHERE entered_at IS NOT NULL AND first_seen_at >= {cutoff}"
        ),
        "known_if": [{"column": "post_deploy_admitted", "op": "eq", "value": 0}],
        "known_text": "no admitted row first seen after the deploy yet",
        "expect": [{"column": "metric_missing", "op": "eq", "value": 0}],
        "expect_text": "metric_missing = 0",
    })
    gaps = k3_gaps(old_k3)
    assert any("last_scan_id" in gap for gap in gaps)
    assert "no expect predicate on rescanned_metric_missing" in gaps
    assert "no known_if predicate on rescanned_admitted" in gaps

    # The shipped shape with its RETAIN grading removed is refused too.
    shipped = _k3()
    ungraded = shipped.model_copy(update={
        "expect": [p for p in shipped.expect if p.column != "rescanned_metric_missing"]
    })
    assert k3_gaps(ungraded) == ["no expect predicate on rescanned_metric_missing"]


def test_k3_grades_each_set_and_is_known_only_when_both_are_empty():
    check = _k3()

    def answer(**values):
        row = {
            "post_deploy_admitted": 0, "metric_missing": 0, "value_null": 0,
            "rescanned_admitted": 0, "rescanned_metric_missing": 0,
        }
        row.update(values)
        columns = list(row)
        return lambda statement, side: rows(columns, [row[c] for c in columns])

    quiet = checks.evaluate(check, ctx(), deps(read_rows=answer()))
    assert quiet.verdict is Verdict.KNOWN
    # Re-scanned rows exist and carry their metric: the check is live and green.
    live = checks.evaluate(check, ctx(), deps(read_rows=answer(rescanned_admitted=40)))
    assert live.verdict is Verdict.PASS
    # THE DEFECT THIS EXISTS FOR: a row the post-deploy scan retained with
    # no metric. Its `first_seen_at` is pre-cutoff, so the INSERT-path
    # counters stay clean and only the RETAIN counter bites.
    retained = checks.evaluate(check, ctx(), deps(
        read_rows=answer(rescanned_admitted=40, rescanned_metric_missing=1)))
    assert retained.verdict is Verdict.FAIL and "rescanned_metric_missing" in retained.detail
    # The INSERT path still bites on its own.
    inserted = checks.evaluate(check, ctx(), deps(
        read_rows=answer(post_deploy_admitted=3, metric_missing=1)))
    assert inserted.verdict is Verdict.FAIL and "metric_missing" in inserted.detail
    # A set that is empty does not make the other set KNOWN.
    half = checks.evaluate(check, ctx(), deps(read_rows=answer(post_deploy_admitted=3)))
    assert half.verdict is Verdict.PASS


# ---------------------------------------------------------------------
# L32: a check never reads across the tenancy wall it declares
# ---------------------------------------------------------------------

MIGRATIONS = REPO / "src" / "cobalt" / "db_migrations"

#: `GRANT <privs> ON [TABLE|SEQUENCE] <schema>.<relation> TO <roles>;` —
#: bounded to one statement (`[^;]`), so a `GRANT … ON SCHEMA …` or a
#: `GRANT <role> TO <role>` never bleeds into the next statement's name.
GRANT_RE = re.compile(
    r"\bGRANT\s+(?P<privs>[^;]+?)\s+ON\s+(?:TABLE\s+|SEQUENCE\s+)?"
    r'(?P<relation>"?[a-z_]+"?\.[a-z_][a-z0-9_]*)\s+TO\s+(?P<roles>[^;]+);',
    re.IGNORECASE | re.DOTALL,
)
SQL_COMMENT_RE = re.compile(r"--[^\n]*")
#: A `system.`/`"user".`-qualified relation named in a query.
QUALIFIED_RE = re.compile(r'("user"|system)\.([a-z_][a-z0-9_]*)')
SIDE_ROLE = {"system": "cobalt_system", "user": "cobalt_user"}


def granted_relations() -> dict[str, set[str]]:
    """`{role: {schema.relation, …}}`, parsed from the shipped migrations.

    Only PER-RELATION grants count, and that is deliberate. `GRANT … ON
    ALL TABLES IN SCHEMA …` (0001) reaches only the relations that
    existed when it ran — `system` was empty at that point — and `ALTER
    DEFAULT PRIVILEGES` reaches only relations CREATED later by the roles
    it names. Neither reaches a relation MOVED into the schema afterwards
    by `ALTER TABLE … SET SCHEMA` (0002), which keeps the ACL it had in
    `public`. `system.cobalt_jobs` is exactly such a moved relation.
    """
    granted: dict[str, set[str]] = {}
    for path in sorted(MIGRATIONS.glob("*.sql")):
        for match in GRANT_RE.finditer(SQL_COMMENT_RE.sub("", path.read_text())):
            relation = match.group("relation").replace('"', "")
            for role in match.group("roles").split(","):
                granted.setdefault(role.strip(), set()).add(relation)
    return granted


def cross_side_reads(suite_checks) -> list[str]:
    """Every `kind: sql` check that names a relation on the OTHER side
    without a migration granting it to the side's role — both directions."""
    granted = granted_relations()
    offenders = []
    for check in suite_checks:
        if check.kind != "sql":
            continue
        role = SIDE_ROLE[check.side]
        for schema, name in sorted(set(QUALIFIED_RE.findall(check.query))):
            relation = f"{schema.replace(chr(34), '')}.{name}"
            if relation.split(".")[0] == check.side:
                continue  # its own side
            if relation not in granted.get(role, set()):
                offenders.append(
                    f"{check.id} (side: {check.side}) reads {relation}, "
                    f"which no migration GRANTs to {role}"
                )
    return offenders


def test_no_smoke_check_reads_across_the_tenancy_wall_it_declares():
    granted = granted_relations()
    # The one documented, migration-backed crossing: `0008` grants the user
    # role SELECT/REFERENCES on `system.movers_daily` for `missed.mover_id`'s
    # FK, which is what lets K9 read it from `side: user`.
    assert "system.movers_daily" in granted["cobalt_user"]
    # `cobalt_jobs` is system-side by declaration (0003) and was MOVED there
    # by 0002; no migration ever grants it to the user role.
    assert "system.cobalt_jobs" not in granted["cobalt_user"]

    offenders = cross_side_reads(load_suite(SUITES_DIR / "s2.yaml").checks)
    assert offenders == [], (
        "a smoke check would hit `permission denied` on a real connection "
        "(L32: `cobalt db query` SET ROLEs to the side's role and asserts it).\n"
        + "\n".join(offenders)
        + "\nThe only migration-backed crossing today is system.movers_daily "
        "(0008_radar_value_movers.sql, granted to cobalt_user for missed.mover_id). "
        "A cross-side read is split into two checks, never granted across."
    )


def test_the_tenancy_wall_check_refuses_a_cross_side_query():
    """The bite proof: the shape K8 had before the split is refused."""
    old_k8 = SqlCheck.model_validate({
        "id": "K8", "title": "missed — card rows complete and equal job.result",
        "kind": "sql", "side": "user",
        "query": (
            "SELECT count(*) FILTER (WHERE m.kind = 'card') AS card_rows, "
            "(SELECT (j.last_result ->> 'card_misses')::int FROM system.cobalt_jobs j "
            "WHERE j.label = 'com.cobalt.replay') AS job_card_misses "
            "FROM \"user\".missed m WHERE m.trade_date = {last_trading_day}"
        ),
        "expect": [{"column": "card_rows", "op": "not_null"}],
        "expect_text": "counts agree",
    })
    offenders = cross_side_reads([old_k8])
    assert len(offenders) == 1 and "system.cobalt_jobs" in offenders[0]
    assert "cobalt_user" in offenders[0]

    # The reverse direction bites the same way: the system role has no
    # reach into `"user"` at all (0001 REVOKEs it).
    system_side = SqlCheck.model_validate({
        "id": "K8.9", "title": "reverse", "kind": "sql", "side": "system",
        "query": 'SELECT count(*) AS card_rows FROM "user".missed m',
        "expect": [{"column": "card_rows", "op": "not_null"}],
        "expect_text": "x",
    })
    offenders = cross_side_reads([system_side])
    assert len(offenders) == 1 and "user.missed" in offenders[0]
    assert "cobalt_system" in offenders[0]

    # The granted crossing stays legal: K9 reads system.movers_daily from
    # the user side because 0008 grants exactly that.
    granted_crossing = SqlCheck.model_validate({
        "id": "K9", "title": "movers", "kind": "sql", "side": "user",
        "query": "SELECT count(*) AS n FROM system.movers_daily WHERE active",
        "expect": [{"column": "n", "op": "not_null"}],
        "expect_text": "x",
    })
    assert cross_side_reads([granted_crossing]) == []


def test_the_k8_split_keeps_every_assertion_on_its_own_side():
    """K8 became K8.1 (system) + K8.2 (user). Nothing it asserted was
    dropped, and each half still grades the way the single check did."""
    by_id = {c.id: c for c in load_suite(SUITES_DIR / "s2.yaml").checks}
    assert "K8" not in by_id
    k81, k82 = by_id["K8.1"], by_id["K8.2"]

    # K8.1 owns the job row, through the one path that reads cobalt_jobs.
    assert k81.kind == "job_row" and k81.label == "com.cobalt.replay"
    assert k81.result_equals["input_stale"] == 0
    assert k81.result_equals["trade_date"] == "{last_trading_day}"
    assert "card_misses" in k81.result_keys
    # K8.2 owns the corpus and names no system relation at all.
    assert k82.kind == "sql" and k82.side == "user"
    assert "system." not in k82.query and '"user".missed' in k82.query
    assert [(p.column, p.op.value, p.value) for p in k82.expect] == [("incomplete", "eq", 0)]
    # The equality that can no longer be one STATEMENT is K8.3's, a machine
    # assertion again (`kind: compare`). Neither half asks for an eye
    # comparison any more, and each names the number K8.3 reads.
    k83 = by_id["K8.3"]
    assert k83.kind == "compare" and (k83.left, k83.right) == ("K8.1", "K8.2")
    assert (k81.result_number, k82.result_number) == ("card_misses", "card_rows")
    for check in (k81, k82):
        assert "by eye" not in check.expect_text

    def answer(result):
        return lambda statement, side: result

    def job(**result):
        base = {"trade_date": "2026-09-22", "card_misses": 2, "input_stale": 0}
        return _job_row(last_result={**base, **result})

    assert checks.evaluate(k81, ctx(), deps(read_rows=answer(job()))).verdict is Verdict.PASS
    stale = checks.evaluate(k81, ctx(), deps(read_rows=answer(job(input_stale=2))))
    assert stale.verdict is Verdict.FAIL and "input_stale" in stale.detail
    wrong_day = checks.evaluate(k81, ctx(), deps(read_rows=answer(job(trade_date="2026-09-21"))))
    assert wrong_day.verdict is Verdict.FAIL and "trade_date" in wrong_day.detail
    no_count = _job_row(last_result={"trade_date": "2026-09-22", "input_stale": 0})
    out = checks.evaluate(k81, ctx(), deps(read_rows=answer(no_count)))
    assert out.verdict is Verdict.FAIL and "card_misses" in out.detail

    complete = rows(["card_rows", "incomplete"], [2, 0])
    out = checks.evaluate(k82, ctx(), deps(read_rows=answer(complete)))
    assert out.verdict is Verdict.PASS and "2" in out.raw  # card_rows printed
    holed = rows(["card_rows", "incomplete"], [2, 1])
    assert checks.evaluate(k82, ctx(), deps(read_rows=answer(holed))).verdict is Verdict.FAIL
    # The user-side statement it runs is the one it prints, and it names
    # no system table (the hand fallback runs as cobalt_user).
    assert "system." not in out.command


# ---------------------------------------------------------------------
# `kind: compare` — the assertion the K8 split lost, restored as a row
# ---------------------------------------------------------------------

#: Two checks that each name THE number of their own result, and a compare
#: row over them. Written as YAML text so every test below goes through the
#: real loader — the same path the close evening runs.
LEFT_SQL = (
    "  - id: K1\n"
    "    title: left\n"
    "    kind: sql\n"
    "    side: user\n"
    "    query: SELECT count(*) AS card_rows FROM picks\n"
    "    result_number: card_rows\n"
    "    expect: [{column: card_rows, op: ge, value: 0}]\n"
    "    expect_text: card_rows\n"
)
RIGHT_JOB = (
    "  - id: K2\n"
    "    title: right\n"
    "    kind: job_row\n"
    "    label: com.cobalt.replay\n"
    "    result_keys: [card_misses]\n"
    "    result_number: card_misses\n"
    "    expect_text: card_misses\n"
)
NUMBERLESS_LAUNCHCTL = (
    "  - id: K1\n"
    "    title: radar\n"
    "    kind: launchctl\n"
    "    mode: running\n"
    "    label: com.cobalt.radar\n"
    "    expect_text: running\n"
)


def _compare_row(cid="K3", left="K1", right="K2", op="eq") -> str:
    return (
        f"  - id: {cid}\n"
        "    title: the two counters agree\n"
        "    kind: compare\n"
        f"    left: {left}\n"
        f"    right: {right}\n"
        f"    op: {op}\n"
        "    expect_text: the two numbers are equal\n"
    )


def _pair_deps(card_rows=2, card_misses=2, left_raises=False):
    def read_rows(statement, side):
        if "cobalt_jobs" in statement:
            return _job_row(last_result={"card_misses": card_misses})
        if left_raises:
            raise RuntimeError("connection refused")
        return rows(["card_rows"], [card_rows])

    return deps(read_rows=read_rows)


def test_compare_refuses_an_unknown_id_a_self_reference_and_an_operand_with_no_number(tmp_path):
    suite = load_suite(_write(tmp_path, GOOD_HEAD + LEFT_SQL + RIGHT_JOB + _compare_row()))
    k3 = {c.id: c for c in suite.checks}["K3"]
    assert (k3.kind, k3.left, k3.right, k3.op.value) == ("compare", "K1", "K2", "eq")

    def refused(text) -> str:
        with pytest.raises(SmokeConfigError) as raised:
            load_suite(_write(tmp_path, text))
        return str(raised.value)

    # An id no check in the file carries.
    assert "K7" in refused(GOOD_HEAD + LEFT_SQL + RIGHT_JOB + _compare_row(right="K7"))
    # A check that names itself on either side.
    assert "K3" in refused(GOOD_HEAD + LEFT_SQL + RIGHT_JOB + _compare_row(left="K3"))
    # One check compared with itself: nothing is asserted.
    assert "K1" in refused(GOOD_HEAD + LEFT_SQL + RIGHT_JOB + _compare_row(right="K1"))
    # An operand BELOW the compare row has not run when the compare runs.
    assert "K1" in refused(GOOD_HEAD + _compare_row() + LEFT_SQL + RIGHT_JOB)
    # An operand that names no number of its own.
    numberless = LEFT_SQL.replace("    result_number: card_rows\n", "")
    message = refused(GOOD_HEAD + numberless + RIGHT_JOB + _compare_row())
    assert "K1" in message and "result_number" in message
    # A kind that has no numeric result at all.
    message = refused(GOOD_HEAD + NUMBERLESS_LAUNCHCTL + RIGHT_JOB + _compare_row())
    assert "K1" in message and "launchctl" in message
    # An operator the evaluator does not implement: the refusal names the
    # field and the one operator that exists.
    message = refused(GOOD_HEAD + LEFT_SQL + RIGHT_JOB + _compare_row(op="gt"))
    assert "op" in message and "'eq'" in message


def test_compare_grades_equal_pass_unequal_fail_and_errors_on_a_bad_operand(tmp_path):
    suite = load_suite(_write(tmp_path, GOOD_HEAD + LEFT_SQL + RIGHT_JOB + _compare_row()))

    def run(**overrides):
        return {o.id: o for o in checks.run_suite(suite, ctx(), _pair_deps(**overrides))}

    equal = run(card_rows=2, card_misses=2)
    assert equal["K3"].verdict is Verdict.PASS
    # One row, both values printed (L57).
    assert all(token in equal["K3"].detail for token in ("K1", "K2", "2"))
    # The hand fallback prints the two ids and the operator (R6 A).
    assert all(token in equal["K3"].command for token in ("K1", "K2", "eq"))

    unequal = run(card_rows=2, card_misses=3)
    assert unequal["K3"].verdict is Verdict.FAIL
    assert "2" in unequal["K3"].detail and "3" in unequal["K3"].detail
    # The operands' own verdicts are untouched by the comparison.
    assert unequal["K1"].verdict is Verdict.PASS and unequal["K2"].verdict is Verdict.PASS

    # An operand that ERRORed is never a silent PASS.
    errored = run(left_raises=True)
    assert errored["K1"].verdict is Verdict.ERROR
    assert errored["K3"].verdict is Verdict.ERROR and "K1" in errored["K3"].detail

    # A non-numeric result is ERROR, naming the operand that carries it.
    text = run(card_misses="two")["K3"]
    assert text.verdict is Verdict.ERROR and "K2" in text.detail
    # So is a result key the job row never wrote.
    missing = {o.id: o for o in checks.run_suite(
        suite, ctx(), deps(read_rows=lambda statement, side: (
            _job_row(last_result={"other": 1}) if "cobalt_jobs" in statement
            else rows(["card_rows"], [2]))))}
    assert missing["K3"].verdict is Verdict.ERROR and "K2" in missing["K3"].detail


def _k8_trio():
    suite = load_suite(SUITES_DIR / "s2.yaml")
    by_id = {c.id: c for c in suite.checks}
    return suite.model_copy(update={"checks": [by_id["K8.1"], by_id["K8.2"], by_id["K8.3"]]})


def _k8_deps(card_rows, card_misses):
    def read_rows(statement, side):
        if "cobalt_jobs" in statement:
            return _job_row(last_result={"trade_date": "2026-09-22", "input_stale": 0,
                                         "card_misses": card_misses})
        return rows(["card_rows", "incomplete"], [card_rows, 0])

    return deps(read_rows=read_rows)


def test_the_shipped_k8_3_asserts_the_two_counters_agree():
    trio = _k8_trio()
    agree = {o.id: o for o in checks.run_suite(trio, ctx(), _k8_deps(2, 2))}
    assert [agree[cid].verdict for cid in ("K8.1", "K8.2", "K8.3")] == [Verdict.PASS] * 3
    assert overall_verdict(list(agree.values())) is Overall.GREEN

    disagree = {o.id: o for o in checks.run_suite(trio, ctx(), _k8_deps(3, 2))}
    # Each half still passes on its own side — the disagreement is the row
    # that exists to see it, and it takes the suite off GREEN.
    assert disagree["K8.1"].verdict is Verdict.PASS and disagree["K8.2"].verdict is Verdict.PASS
    assert disagree["K8.3"].verdict is Verdict.FAIL
    assert "2" in disagree["K8.3"].detail and "3" in disagree["K8.3"].detail
    assert overall_verdict(list(disagree.values())) is Overall.AMBER


def test_the_report_renders_the_compare_row():
    outcomes = checks.run_suite(_k8_trio(), ctx(), _k8_deps(3, 2))
    rep = report.build_report("s2", "S2 smoke", ctx(), outcomes)
    table = report.render_table(rep)
    assert "| K8.3 |" in table and "FAIL" in table
    text = report.render_markdown(rep)
    assert "## K8.3" in text and "- kind: compare" in text
    # The row prints its two ids, its operator and both values, so the
    # comparison is replayable from the report alone (R6 A, L57).
    section = text.split("## K8.3")[1]
    assert all(token in section for token in ("K8.1", "K8.2", "eq", "2", "3"))
    payload = json.loads(report.render_json(rep))
    numbers = {c["id"]: c["number"] for c in payload["checks"]}
    assert numbers == {"K8.1": "2", "K8.2": "3", "K8.3": None}


def _suite_fakes(tmp_path):
    drc = tmp_path / "drc.md"
    drc.write_text(
        "# DRC\n<!-- cobalt:section drc-misses -->\n<!-- cobalt:unit miss_line -->\n"
        "Misses …\n<!-- /cobalt:unit miss_line -->\n<!-- /cobalt:section drc-misses -->\n"
    )

    def read_rows(statement, side):
        if "cobalt_jobs" in statement:
            return _job_row()
        return rows(["x"], [1])

    return deps(
        read_rows=read_rows,
        launchctl_print=lambda label: LaunchdPrintStatus(label, "running", 1, "(never exited)", 1, "state = running"),
        launchctl_loaded=lambda label: True,
        http_get=lambda url: (200, "<th>value</th>"),
        read_text=lambda path: "HEARTBEAT GREEN — x\nOK   database  ok\nOK   sheet HTTP  ok\n",
        run_cli=lambda argv: (0, "ok"),
        job_specs=lambda: checks.load_job_specs(),
        drc_note_path=lambda day: drc,
    )


def test_a_suite_with_no_compare_row_loads_and_runs_exactly_as_before(tmp_path):
    """The bound this was built inside: ONE additive kind and ONE additive
    optional field. A smoke file written before either existed — the
    shipped suite with every compare row and every `result_number` line
    stripped out — still loads, and every check it keeps runs to the same
    verdict, detail, command and evidence as in the shipped suite."""
    text = (SUITES_DIR / "s2.yaml").read_text()
    head, marker, body = text.partition("checks:\n")
    assert marker, "the shipped suite no longer has a `checks:` block"
    blocks = re.split(r"(?m)^(?=  - id: )", body)
    old = head + marker + "".join(block for block in blocks if "kind: compare" not in block)
    old = "".join(f"{line}\n" for line in old.splitlines()
                  if not line.strip().startswith("result_number:"))

    old_suite = load_suite(_write(tmp_path, old))
    shipped = load_suite(SUITES_DIR / "s2.yaml")
    assert [c.id for c in shipped.checks if c.kind != "compare"] == [c.id for c in old_suite.checks]
    assert any(c.kind == "compare" for c in shipped.checks), "nothing was stripped"
    assert all(getattr(c, "result_number", None) is None for c in old_suite.checks)

    fakes = _suite_fakes(tmp_path)
    before = {o.id: o for o in checks.run_suite(old_suite, ctx(), fakes)}
    after = {o.id: o for o in checks.run_suite(shipped, ctx(), fakes)}
    for cid, outcome in before.items():
        twin = after[cid]
        assert outcome.model_dump(exclude={"number"}) == twin.model_dump(exclude={"number"}), cid


def test_context_last_trading_day_waits_for_the_anchor_job_and_skips_holidays():
    from cobalt.jobs.config import load_job_registry

    spec = load_job_registry().spec("com.cobalt.replay")
    # 21:50 ET Tuesday: tonight's 21:10 + 1800 s (21:40) has passed -> today.
    assert checks.last_trading_day(NOW, spec) == DAY
    # 21:20 ET Tuesday: tonight's run may still be going -> Monday.
    early = datetime(2026, 9, 22, 21, 20, tzinfo=ET)
    assert checks.last_trading_day(early, spec) == date(2026, 9, 21)
    # Monday 2026-12-28 09:00 ET: tonight's run is hours away and Friday
    # 12-25 is an NYSE holiday, so the answer is Thursday 12-24.
    assert checks.last_trading_day(datetime(2026, 12, 28, 9, 0, tzinfo=ET), spec) == date(2026, 12, 24)

    built = checks.build_context(now=NOW, report_date=None, cutoff=CUTOFF, prod=True,
                                 anchor_spec=spec, tunables={"heartbeat.radar_scan_max_age_s": 900})
    assert built.report_date == DAY and built.last_trading_day == DAY
    assert built.session == "overnight"
    assert (built.last_summary_slot, built.last_summary_date) == ("16:30", DAY)
    morning = checks.build_context(now=datetime(2026, 9, 22, 6, 0, tzinfo=ET), report_date=None,
                                   cutoff=CUTOFF, prod=True, anchor_spec=spec, tunables={})
    assert (morning.last_summary_slot, morning.last_summary_date) == ("16:30", date(2026, 9, 21))


# ---------------------------------------------------------------------
# requires_db (hub, cobalt_dev): every committed query parses and runs
# ---------------------------------------------------------------------


@requires_db
def test_committed_queries_run_read_only_on_cobalt_dev():
    from cobalt.jobs.config import load_job_registry
    from cobalt.taxonomy.loader import load_tunables

    registry = load_job_registry()
    tunables = {key: row.value for key, row in load_tunables().by_key.items()}
    context = checks.build_context(now=datetime.now(timezone.utc), report_date=None, cutoff=CUTOFF,
                                   prod=False, anchor_spec=registry.spec("com.cobalt.replay"),
                                   tunables=tunables)
    live = checks.default_deps(prod=False)
    suite = load_suite(SUITES_DIR / "s2.yaml")
    for check in suite.checks:
        if check.kind not in ("sql", "job_row"):
            continue
        outcome = checks.evaluate(check, context, live)
        # A missing P2 relation or an empty dev table is a FAIL/KNOWN; a
        # query the server cannot parse or the role cannot read is ERROR.
        assert outcome.verdict is not Verdict.ERROR, (check.id, outcome.detail)
