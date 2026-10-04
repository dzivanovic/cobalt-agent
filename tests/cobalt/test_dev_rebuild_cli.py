"""dev-rebuild D2 — `cobalt db dev-rebuild <schema>.<table>`: the refusals.

Offline. Every refusal that must happen BEFORE a connection runs with
`db.connect_migration` monkeypatched to raise if it is called at all; the
database-name refusal runs on a fake connection that records every
statement sent. The three outcome lines run on the same fake with
`rebuild_table` stubbed, so the commit-only rule of the CLI is pinned
without a database.
"""

from __future__ import annotations

import argparse
import importlib

import pytest

from cobalt import db
from cobalt.db_migrations import cli


def _dev_rebuild():
    """Imported after the parse, so a missing subcommand reads as argparse's
    own refusal rather than as an import error."""
    return importlib.import_module("cobalt.db_migrations.dev_rebuild")


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="cobalt")
    cli.add_parser(parser.add_subparsers(dest="group", required=True))
    return parser


def _parse(argv, capsys):
    """Parse, or fail the test with argparse's own words."""
    try:
        return _parser().parse_args(argv)
    except SystemExit:
        pytest.fail(capsys.readouterr().err)


def _run(argv, capsys) -> int:
    args = _parse(argv, capsys)
    with pytest.raises(SystemExit) as caught:
        args.func(args)
    return caught.value.code


def _no_connection(*_a, **_k):
    raise AssertionError("db.connect_migration was called")


class FakeConn:
    def __init__(self, dbname: str):
        self.dbname = dbname
        self.statements: list[str] = []
        self.autocommit = True
        self.committed = 0
        self.rolled_back = 0
        self.closed = False

    def execute(self, stmt, params=None):
        self.statements.append(str(stmt))
        conn = self

        class _Cursor:
            def fetchone(self):
                return (conn.dbname,)

        return _Cursor()

    def commit(self):
        self.committed += 1

    def rollback(self):
        self.rolled_back += 1

    def close(self):
        self.closed = True


@pytest.mark.parametrize(
    "cobalt_env, target",
    [
        ("production", "user.aset_sizings"),
        (None, "user.aset_sizings"),
        ("dev", "system.x;drop"),
        ("dev", "public.aset_sizings"),
        ("dev", "user.Aset_Sizings"),
        ("dev", "aset_sizings"),
    ],
)
def test_refused_with_exit_2_and_no_connection(cobalt_env, target, monkeypatch, capsys):
    if cobalt_env is None:
        monkeypatch.delenv("COBALT_ENV", raising=False)
    else:
        monkeypatch.setenv("COBALT_ENV", cobalt_env)
    monkeypatch.setattr(db, "connect_migration", _no_connection)

    assert _run(["db", "dev-rebuild", target], capsys) == 2
    assert "REFUSED" in capsys.readouterr().err


def test_lock_timeout_zero_is_refused_with_exit_2_and_no_connection(monkeypatch, capsys):
    monkeypatch.setenv("COBALT_ENV", "dev")
    monkeypatch.setattr(db, "connect_migration", _no_connection)

    assert _run(["db", "dev-rebuild", "user.aset_sizings", "--lock-timeout-s", "0"], capsys) == 2


def test_a_connection_to_another_database_sends_only_the_read(monkeypatch, capsys):
    monkeypatch.setenv("COBALT_ENV", "dev")
    fake = FakeConn("cobalt_brain")
    opened = []

    def _connect(dbname, **kwargs):
        opened.append((dbname, kwargs))
        return fake

    monkeypatch.setattr(db, "connect_migration", _connect)
    args = _parse(["db", "dev-rebuild", "user.aset_sizings"], capsys)
    rebuilt = []
    monkeypatch.setattr(
        _dev_rebuild(), "rebuild_table", lambda *a, **k: rebuilt.append(a)
    )

    try:
        args.func(args)
        code = None
    except SystemExit as e:
        code = e.code
    except Exception as e:  # a path that went past the refusal
        code = repr(e)
    assert fake.statements == ["SELECT current_database()"]
    assert rebuilt == []
    assert code == 2
    assert opened == [("cobalt_dev", {"allow_prod": False})]
    assert fake.committed == 0
    assert fake.closed


def test_allow_prod_does_not_exist_on_dev_rebuild(capsys):
    with pytest.raises(SystemExit) as caught:
        _parser().parse_args(["db", "dev-rebuild", "user.aset_sizings", "--allow-prod"])
    assert caught.value.code == 2
    assert "unrecognized arguments: --allow-prod" in capsys.readouterr().err


def _state(max_attnum: int, dropped: int):
    return _dev_rebuild().TableState(
        max_attnum=max_attnum, dropped=dropped, live=4, rows=3,
        row_digest="r" * 32, sections={"grants": ("g",)},
    )


def _outcome(monkeypatch, *, raises=None):
    dev_rebuild = _dev_rebuild()
    monkeypatch.setenv("COBALT_ENV", "dev")
    fake = FakeConn("cobalt_dev")
    monkeypatch.setattr(db, "connect_migration", lambda dbname, **kw: fake)
    calls = []

    def _rebuild(conn, schema, table, *, dry_run):
        calls.append((schema, table, dry_run))
        if raises is not None:
            raise raises
        return dev_rebuild.RebuildResult(before=_state(9, 5), after=_state(4, 0), dry_run=dry_run)

    monkeypatch.setattr(dev_rebuild, "rebuild_table", _rebuild)
    return fake, calls


def test_rebuilt_commits_once_and_prints_the_line(monkeypatch, capsys):
    args = _parse(["db", "dev-rebuild", "user.scratch_t"], capsys)
    fake, calls = _outcome(monkeypatch)
    args.func(args)
    out = capsys.readouterr().out
    assert calls == [("user", "scratch_t", False)]
    assert fake.statements[:2] == ["SELECT current_database()", "SET LOCAL lock_timeout = '30s'"]
    assert fake.autocommit is False
    assert fake.committed == 1
    assert "BEFORE max_attnum 9" in out and "AFTER  max_attnum 4" in out
    assert out.strip().splitlines()[-1] == (
        "REBUILT user.scratch_t · max_attnum 9 → 4 · rows 3 = 3 · catalog digest equal"
    )


def test_dry_run_never_commits(monkeypatch, capsys):
    args = _parse(["db", "dev-rebuild", "user.scratch_t", "--dry-run", "--lock-timeout-s", "5"], capsys)
    fake, calls = _outcome(monkeypatch)
    args.func(args)
    out = capsys.readouterr().out
    assert calls == [("user", "scratch_t", True)]
    assert "SET LOCAL lock_timeout = '5s'" in fake.statements
    assert fake.committed == 0
    assert out.strip().splitlines()[-1] == (
        "DRY RUN — ROLLED BACK · max_attnum 9 → 4 · rows 3 = 3 · catalog digest equal"
    )


def test_a_mismatch_exits_1_and_never_commits(monkeypatch, capsys):
    args = _parse(["db", "dev-rebuild", "user.scratch_t"], capsys)
    mismatch = _dev_rebuild().RebuildMismatch(
        ("grants",), before=_state(9, 5), after=_state(4, 0)
    )
    fake, _calls = _outcome(monkeypatch, raises=mismatch)
    with pytest.raises(SystemExit) as caught:
        args.func(args)
    assert caught.value.code == 1
    out = capsys.readouterr().out
    assert fake.committed == 0
    assert out.strip().splitlines()[-1] == "FAILED: grants — ROLLED BACK"


# ---------------------------------------------------------------------
# slot-guard S1 — every `cobalt db migrate` run prints the SLOTS line(s)
# ---------------------------------------------------------------------

#: `(schema, table, max_attnum, dropped, live)` as `slot_report` answers:
#: the 2026-10-01 measurement and the rebuilt table.
FULL = ("user", "aset_sizings", 1581, 1527, 54)
REBUILT_ROW = ("user", "aset_sizings", 664, 610, 54)

WARN_FULL = (
    "SLOTS WARN user.aset_sizings max_attnum 1581 of 1600 · dropped 1527 · live 54"
    " · fix: cobalt db dev-rebuild user.aset_sizings (dev only)"
)


class SlotConn:
    """A connection that answers the slot read with `rows`, records every
    statement, and answers `fetchone` with the database name. `fail` makes
    the slot read itself raise, as a real catalog error would."""

    def __init__(self, rows, *, fail: BaseException | None = None):
        self.rows = list(rows)
        self.fail = fail
        self.statements: list[str] = []
        self.committed = 0
        self.rolled_back = 0
        self.closed = 0

    def execute(self, stmt, params=None):
        text = str(stmt)
        self.statements.append(text)
        conn = self

        class _Cursor:
            def fetchall(self):
                if conn.fail is not None and "pg_attribute" in text:
                    raise conn.fail
                return list(conn.rows)

            def fetchone(self):
                return ("cobalt_dev",)

        return _Cursor()

    def commit(self):
        self.committed += 1

    def rollback(self):
        self.rolled_back += 1

    def close(self):
        self.closed += 1


def test_s1_slot_report_reads_the_rows_and_the_line_is_the_warn_line_exactly():
    from cobalt.db_migrations.dev_rebuild import slot_report

    conn = SlotConn([FULL])
    assert slot_report(conn) == [FULL]
    assert cli._slot_lines(SlotConn([FULL])) == [WARN_FULL]


def test_s1_below_the_warn_mark_is_one_ok_line_naming_the_highest():
    from cobalt.db_migrations.dev_rebuild import slot_report  # noqa: F401 — the row's red

    rows = [("system", "bars", 12, 0, 12), REBUILT_ROW, ("user", "traders", 5, 0, 5)]
    assert cli._slot_lines(SlotConn(rows)) == [
        "SLOTS ok · highest user.aset_sizings 664 of 1600"
    ]


@pytest.mark.parametrize(
    "max_attnum, expected",
    [
        (1200, "SLOTS WARN user.aset_sizings max_attnum 1200 of 1600 · dropped 1146 · live 54"
               " · fix: cobalt db dev-rebuild user.aset_sizings (dev only)"),
        (1199, "SLOTS ok · highest user.aset_sizings 1199 of 1600"),
    ],
)
def test_s1_the_two_ends_of_the_warn_edge(max_attnum, expected):
    from cobalt.db_migrations.dev_rebuild import slot_report  # noqa: F401 — the row's red

    assert cli.SLOT_WARN_AT == 1200
    row = ("user", "aset_sizings", max_attnum, max_attnum - 54, 54)
    assert cli._slot_lines(SlotConn([row])) == [expected]


def test_s1_one_warn_line_per_relation_at_or_above_the_mark():
    from cobalt.db_migrations.dev_rebuild import slot_report  # noqa: F401 — the row's red

    rows = [FULL, ("system", "radar_membership", 1300, 1290, 10), REBUILT_ROW]
    lines = cli._slot_lines(SlotConn(rows))
    assert lines == [
        WARN_FULL,
        "SLOTS WARN system.radar_membership max_attnum 1300 of 1600 · dropped 1290"
        " · live 10 · fix: cobalt db dev-rebuild system.radar_membership (dev only)",
    ]


def test_s1_a_failed_slot_read_is_named_and_undone_inside_its_savepoint():
    """The read sits inside the migrate transaction: a catalog error must be
    rolled back to its savepoint, or the migration's COMMIT would meet an
    aborted transaction."""
    from cobalt.db_migrations.dev_rebuild import slot_report  # noqa: F401 — the row's red

    conn = SlotConn([], fail=RuntimeError("catalog read failed"))
    assert cli._slot_lines(conn) == ["SLOTS UNKNOWN — RuntimeError: catalog read failed"]
    assert conn.statements[0].startswith("SAVEPOINT ")
    assert conn.statements[-1].startswith("ROLLBACK TO SAVEPOINT ")


def _migrate_output(monkeypatch, capsys, conn, **namespace) -> list[str]:
    """`cmd_migrate` on `conn`, the proof stubbed to one marker line."""
    monkeypatch.setenv("COBALT_ENV", "dev")
    monkeypatch.setattr(cli, "_connect", lambda *a, **k: conn)
    monkeypatch.setattr(cli, "_probe_all", lambda c: {})
    monkeypatch.setattr(cli, "_apply", lambda c, paths: None)
    monkeypatch.setattr(cli, "_print_probe", lambda *a, **k: print("<proof table>"))
    monkeypatch.setattr(cli, "_print_proof", lambda *a, **k: print("<proof table>") or 0)
    monkeypatch.setattr(cli, "_code_line", lambda: "<code line>")
    fields = {
        "proof_only": False, "rollback": False, "down_to": None, "allow_prod": False,
        "lock_timeout_s": cli.DEFAULT_LOCK_TIMEOUT_S,
    }
    fields.update(namespace)
    cli.cmd_migrate(argparse.Namespace(**fields))
    return [line for line in capsys.readouterr().out.splitlines() if line.strip()]


@pytest.mark.parametrize(
    "namespace",
    [
        {"proof_only": True},
        {},
        {"rollback": True, "down_to": "0013"},
        {"proof_only": True, "allow_prod": True},
    ],
    ids=["proof-only", "forward", "rollback", "proof-only-production"],
)
def test_s1_every_migrate_run_prints_the_slots_line_after_its_proof_table(
    monkeypatch, capsys, namespace
):
    from cobalt.db_migrations.dev_rebuild import slot_report  # noqa: F401 — the row's red

    conn = SlotConn([FULL])
    lines = _migrate_output(monkeypatch, capsys, conn, **namespace)
    assert lines[-3:] == ["<proof table>", WARN_FULL, "<code line>"]
    # Read inside the run's ONE transaction, before it ends.
    read_at = next(i for i, s in enumerate(conn.statements) if "pg_attribute" in s)
    assert all("pg_attribute" not in s for s in conn.statements[read_at + 1:])
    if namespace.get("proof_only"):
        # Read-only: the slot read sends nothing that writes, and nothing commits.
        assert conn.committed == 0
        assert [s.split()[0] for s in conn.statements] == ["SAVEPOINT", "SELECT", "RELEASE"]


# ---------------------------------------------------------------------
# slot-guard S2 — the with-DB suite's headroom verdict
# ---------------------------------------------------------------------


@pytest.mark.parametrize(
    "max_attnum, verdict",
    [(1581, "fail"), (1537, "fail"), (1536, "warn"), (1200, "warn"), (1199, "ok")],
)
def test_s2_slot_verdict(max_attnum, verdict):
    from cobalt.db_migrations.dev_rebuild import slot_verdict, SLOT_FAIL_HEADROOM

    assert SLOT_FAIL_HEADROOM == 64
    rows = [("user", "aset_sizings", max_attnum, max_attnum - 54, 54), ("system", "bars", 12, 0, 12)]
    assert slot_verdict(rows, cli.SLOT_WARN_AT, SLOT_FAIL_HEADROOM) == verdict


def test_s2_slot_verdict_with_no_rows_is_ok():
    from cobalt.db_migrations.dev_rebuild import slot_verdict, SLOT_FAIL_HEADROOM

    assert slot_verdict([], cli.SLOT_WARN_AT, SLOT_FAIL_HEADROOM) == "ok"


def _suite_conftest(request):
    """`tests/cobalt/conftest.py` as pytest registered it — found by its
    file, whatever module name the import mode gave it."""
    found = [
        p for p in request.config.pluginmanager.get_plugins()
        if str(getattr(p, "__file__", "")).replace("\\", "/").endswith("tests/cobalt/conftest.py")
    ]
    assert len(found) == 1, found
    return found[0]


class _Closable:
    def rollback(self):
        pass

    def close(self):
        pass


def _run_the_hook(request, monkeypatch, max_attnum):
    """The session-start hook, offline: Postgres settings present, the
    connection a stub, `slot_report` replaced. Returns `(exit, summary)`:
    the `pytest.exit` it raised (or None) and the terminal-summary lines."""
    from types import SimpleNamespace

    import cobalt.db_migrations.dev_rebuild as dev_rebuild

    conftest = _suite_conftest(request)
    monkeypatch.setenv("POSTGRES_HOST", "constructed-host")
    monkeypatch.setenv("POSTGRES_USER", "constructed-user")
    monkeypatch.setattr(conftest, "REAL_CONNECT", lambda *a, **k: _Closable())
    rows = [("user", "aset_sizings", max_attnum, max_attnum - 54, 54), ("system", "bars", 12, 0, 12)]
    monkeypatch.setattr(dev_rebuild, "slot_report", lambda conn: rows)
    config = SimpleNamespace(stash=pytest.Stash())
    stopped = None
    try:
        conftest.pytest_sessionstart(SimpleNamespace(config=config))
    except pytest.exit.Exception as e:
        stopped = e
    written: list[str] = []
    conftest.pytest_terminal_summary(
        SimpleNamespace(write_line=written.append), 0, config
    )
    return stopped, written


def test_s2_the_hook_stops_the_run_with_exit_3_naming_the_table(request, monkeypatch):
    stopped, written = _run_the_hook(request, monkeypatch, 1581)
    assert stopped is not None, "the hook did not stop the run"
    assert stopped.returncode == 3
    assert stopped.msg == (
        "cobalt_dev column slots: user.aset_sizings 1581 of 1600 — run a devfix "
        "(cobalt db dev-rebuild user.aset_sizings) before any with-DB gate"
    )
    assert written == []


def test_s2_the_hook_warns_in_the_summary_and_does_not_stop(request, monkeypatch):
    stopped, written = _run_the_hook(request, monkeypatch, 1300)
    assert stopped is None
    assert written == [
        "SLOTS WARN user.aset_sizings max_attnum 1300 of 1600 · dropped 1246 · live 54"
        " · fix: cobalt db dev-rebuild user.aset_sizings (dev only)"
    ]


def test_s2_the_hook_is_silent_below_the_warn_mark(request, monkeypatch):
    stopped, written = _run_the_hook(request, monkeypatch, 664)
    assert stopped is None
    assert written == []
