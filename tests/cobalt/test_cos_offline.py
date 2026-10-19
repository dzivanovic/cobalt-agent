"""F20 CoS — offline (card 730 rows P1, C3b, C3c, C4c, C4d; FINAL §2, §4, §5).

THE SESSION RUNS ON A FAKE SDK CLIENT ONLY (T6 does not close U4): no test
here starts the CLI, reads his login or spends his meter. Constructed data
only (L32): no DM text of his, no real post id, no token.
"""

from __future__ import annotations

import asyncio
import os
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]


# ---------------------------------------------------------------------
# P1 — THE PIN, PINNED (FINAL §2 pyproject row, F-09)
# ---------------------------------------------------------------------


def test_agent_sdk_is_pinned_exact():
    import tomllib

    deps = tomllib.loads((REPO_ROOT / "pyproject.toml").read_text())["project"]["dependencies"]
    pins = [d for d in deps if d.replace(" ", "").startswith("claude-agent-sdk")]
    assert len(pins) == 1, f"one claude-agent-sdk entry, found {pins}"
    assert pins[0].replace(" ", "").startswith("claude-agent-sdk=="), pins[0]


# ---------------------------------------------------------------------
# C3b — the tool server (FINAL §2 `cos/tools.py`; L37)
# ---------------------------------------------------------------------

SEVEN = {"cards.open", "radar.pool", "jobs.status", "hitl.list", "agents.list",
         "request_action", "draft_agent"}


def test_the_tool_set_is_exact():
    import re

    from cobalt.agents.registry import AGENTS_DIR, TOOL_CATALOG, load_entry
    from cobalt.cos import tools

    assert set(tools.TOOLS) == SEVEN
    assert set(load_entry(AGENTS_DIR / "cos.yaml").tools) == SEVEN == set(TOOL_CATALOG)
    assert not [n for n in tools.TOOLS if re.search(r"approve|decide|execut", n, re.I)]


def test_draft_agent_writes_a_pending_row_only(monkeypatch):
    from cobalt.cos import tools
    from cobalt.hitl import actions

    calls: list[tuple] = []

    def fake_request(action, args, reason, **kw):
        calls.append((action, args, reason))
        return "pending c0ffee00"

    monkeypatch.setattr(actions, "request_action", fake_request)
    out = tools.call("draft_agent", {"yaml": "agent: {}", "reason": "constructed"})
    assert out == "pending c0ffee00"
    assert calls == [("agents.create", {"yaml": "agent: {}"}, "constructed")]
    # a refusal is a tool result, never an exception into the SDK
    assert tools.call("draft_agent", {}).startswith("refused:")
    assert tools.call("no.such.tool", {}).startswith("refused:")


# ---------------------------------------------------------------------
# C3c — the session, on a FAKE SDK client (FINAL §4, §5; D4, D5, U6)
# ---------------------------------------------------------------------


def _assistant(text="a constructed reply"):
    from types import SimpleNamespace

    return SimpleNamespace(content=[SimpleNamespace(text=text)])


def _result(**over):
    from types import SimpleNamespace

    base = dict(subtype="success", is_error=False, terminal_reason="completed", num_turns=1,
                session_id="constructed-session", result="a constructed reply")
    return SimpleNamespace(**{**base, **over})


class FakeClient:
    """The four calls the session makes, and `kill`. `script(client)` yields
    the response stream; the string "HANG" blocks it."""

    def __init__(self, options, tool_call, script, log):
        self.options, self.tool_call, self.script, self.log = options, tool_call, script, log
        self.killed = False
        log.append(self)

    async def connect(self):
        self.env_at_connect = dict(os.environ)

    async def query(self, text):
        self.text = text

    async def receive_response(self):
        for item in self.script(self):
            if item == "HANG":
                await asyncio.sleep(3600)
            yield item

    async def disconnect(self):
        pass

    def kill(self):
        self.killed = True


def _session(tmp_path, script, *, max_turns=5, timeout_s=5.0, connect_error=None, wrap=None):
    from cobalt.cos.session import CosSession

    log: list[FakeClient] = []
    dms: list[str] = []

    def factory(options, tool_call):
        if connect_error is not None and options.get("resume"):
            raise connect_error
        client = FakeClient(options, tool_call, script, log)
        return wrap(client) if wrap is not None else client

    session = CosSession(model="claude-sonnet-5-5", scratch_dir=tmp_path, charter="constructed",
                         client_factory=factory, notify=dms.append,
                         max_turns=max_turns, timeout_s=timeout_s)
    return session, log, dms


def test_options_allowlist_disallowed_mode_settings(tmp_path):
    from cobalt.cos import session as session_mod

    opts = session_mod.build_options(model="claude-sonnet-5-5", cwd=tmp_path, charter="c",
                                     max_turns=5, resume=None)
    assert set(opts["allowed_tools"]) == {session_mod.sdk_tool_name(n) for n in SEVEN}
    assert opts["tools"] == [], "no built-in tool is in the base set"
    must = {"Bash", "Write", "Edit", "NotebookEdit", "WebFetch", "WebSearch", "Task", "Agent",
            "Read", "Grep", "Glob"}
    assert must <= set(opts["disallowed_tools"])
    assert opts["setting_sources"] == [] and opts["strict_mcp_config"] is True
    assert opts["permission_mode"] != "bypassPermissions"
    import ast

    constants = [n.value for n in ast.walk(ast.parse(Path(session_mod.__file__).read_text()))
                 if isinstance(n, ast.Constant) and isinstance(n.value, str)]
    assert "bypassPermissions" not in constants, "the mode string never appears as a value (L55)"
    assert "can_use_tool" not in opts and "hooks" not in opts
    assert opts["cwd"] == str(tmp_path) and opts["model"] == "claude-sonnet-5-5"


def test_spawn_env_is_the_allowlist(monkeypatch, tmp_path):
    from cobalt.cos import session as session_mod

    monkeypatch.setenv("COBALT_MASTER_KEY", "dummy")
    monkeypatch.setenv("ANTHROPIC_API_KEY", "dummy")
    monkeypatch.setenv("ANTHROPIC_BASE_URL", "http://dummy.invalid")
    monkeypatch.setenv("POSTGRES_PASSWORD", "dummy")
    env = session_mod.child_env()
    assert set(env) <= {"PATH", "HOME", "USER", "LANG", "COBALT_ENV"}
    assert "PATH" in env and env.get("COBALT_ENV") == "dev"

    session, log, _dms = _session(tmp_path, lambda c: [_assistant(), _result()])
    out = asyncio.run(session.run_turn("constructed", resume=None))
    assert out.ok
    seen = log[0].env_at_connect
    assert set(seen) <= {"PATH", "HOME", "USER", "LANG", "COBALT_ENV"}, sorted(seen)
    assert log[0].options["env"] == env
    assert os.environ["COBALT_MASTER_KEY"] == "dummy", "the parent env is restored after the spawn"


def test_hang_max_turns_no_result_each_fail_and_dm(tmp_path):
    session, log, dms = _session(tmp_path, lambda c: [_assistant(), "HANG"], timeout_s=0.05)
    out = asyncio.run(session.run_turn("constructed", resume=None))
    assert not out.ok and "timeout" in out.error and log[-1].killed

    session, log, dms2 = _session(tmp_path, lambda c: [_assistant()] * 4 + [_result()], max_turns=2)
    out = asyncio.run(session.run_turn("constructed", resume=None))
    assert not out.ok and "max turns" in out.error and log[-1].killed

    session, log, dms3 = _session(tmp_path, lambda c: [_assistant()])
    out = asyncio.run(session.run_turn("constructed", resume=None))
    assert not out.ok and "no result" in out.error

    assert len(dms) == 1 and len(dms2) == 1 and len(dms3) == 1, "each failure DMs once"


def test_is_error_fails_even_when_subtype_success(tmp_path):
    session, _log, dms = _session(tmp_path, lambda c: [_result(is_error=True, subtype="success")])
    out = asyncio.run(session.run_turn("constructed", resume=None))
    assert not out.ok and out.is_error and dms

    session, _log, _ = _session(tmp_path, lambda c: [_result(terminal_reason="max_turns")])
    assert not asyncio.run(session.run_turn("constructed", resume=None)).ok

    session, _log, dms = _session(tmp_path, lambda c: [_result(subtype="error_during_execution")])
    out = asyncio.run(session.run_turn("constructed", resume=None))
    assert out.ok and not dms, "never fail on subtype alone (D5)"
    assert out.session_id == "constructed-session"


def test_parallel_requests_each_post_a_card(monkeypatch, tmp_path):
    from cobalt.hitl import actions

    cards: list[str] = []

    def fake_request(action, args, reason, **kw):
        cards.append(args["yaml"])
        return f"pending {len(cards):08x}"

    monkeypatch.setattr(actions, "request_action", fake_request)

    def script(client):
        # two request calls in ONE turn, as a parallel tool use delivers them
        replies = [client.tool_call("draft_agent", {"yaml": "agent: a", "reason": "r"}),
                   client.tool_call("draft_agent", {"yaml": "agent: b", "reason": "r"})]
        assert replies == ["pending 00000001", "pending 00000002"]
        return [_assistant(), _result()]

    session, _log, _dms = _session(tmp_path, script)
    assert asyncio.run(session.run_turn("constructed", resume=None)).ok
    assert cards == ["agent: a", "agent: b"], "each request in the turn posted its own card"


def test_failed_resume_opens_fresh_and_dms(tmp_path):
    session, log, dms = _session(tmp_path, lambda c: [_result()], connect_error=RuntimeError("gone"))
    out = asyncio.run(session.run_turn("constructed", resume="constructed-old-session"))
    assert out.ok and log[-1].options.get("resume") is None
    assert any("fresh session" in d for d in dms)


def test_import_cobalt_cli_leaves_the_sdk_unloaded():
    proc = subprocess.run(
        [sys.executable, "-c",
         "import sys, cobalt.cli, cobalt.cos.session, cobalt.cos.run; "
         "print('claude_agent_sdk' in sys.modules)"],
        capture_output=True, text=True, cwd=REPO_ROOT, env={**os.environ, "COBALT_ENV": "dev"},
    )
    assert proc.returncode == 0, proc.stderr
    assert proc.stdout.strip() == "False"


# ---------------------------------------------------------------------
# C4c — every cos/hitl tunable is read loud (L1, F16)
# ---------------------------------------------------------------------


def _registry_with(key, value, _real={}):
    from cobalt.taxonomy import loader
    from cobalt.taxonomy.tunables import TunableRegistry

    # The REAL registry, read once before any test patches the loader.
    if "rows" not in _real:
        _real["rows"] = loader.load_tunables().tunables
    rows = [r for r in _real["rows"] if r.key != key]
    if value is not None:
        template = rows[0].model_copy(update={"key": key, "value": value})
        rows.append(template)
    return TunableRegistry(tunables=rows)


@pytest.mark.parametrize("key", ["cos.max_turns", "cos.turn_timeout_s", "cos.poll_interval_s",
                                 "hitl.request_ttl_min"])
def test_each_cos_tunable_is_read_loud(monkeypatch, key):
    from cobalt.cos import session as session_mod
    from cobalt.hitl import actions
    from cobalt.taxonomy import loader

    read = actions.request_ttl_min if key.startswith("hitl.") else (lambda: session_mod.tunable_int(key))
    _registry_with(key, 7)  # the real rows, read before the loader is patched
    for bad in (None, 0, -5, "thirty"):
        monkeypatch.setattr(loader, "load_tunables", lambda bad=bad: _registry_with(key, bad))
        with pytest.raises(Exception, match=key.replace(".", r"\.")):
            read()
    monkeypatch.setattr(loader, "load_tunables", lambda: _registry_with(key, 7))
    assert read() == 7


def test_the_shipped_cos_rows():
    from cobalt.taxonomy.loader import load_tunables

    rows = load_tunables().by_key
    assert rows["cos.max_turns"].value == 30 and rows["cos.max_turns"].status.value == "proposed"
    assert rows["cos.turn_timeout_s"].value == 900
    for gap in ("cos.poll_interval_s", "hitl.request_ttl_min"):
        assert rows[gap].value is None and rows[gap].status.value == "proposed", gap


# ---------------------------------------------------------------------
# C4d — the commands, read and dry-run only (L10)
# ---------------------------------------------------------------------


def _main(monkeypatch, *argv):
    from cobalt import cli

    monkeypatch.setattr(sys, "argv", ["cobalt", *argv])
    with pytest.raises(SystemExit) as exc:
        cli.main()
    return exc.value.code


def test_the_cli_mounts_cos_agents_hitl(monkeypatch):
    for group in (("cos", "run"), ("agents", "list"), ("hitl", "list"), ("cos",), ("agents",), ("hitl",)):
        assert _main(monkeypatch, *group, "--help") == 0, group


def test_no_approve_subcommand(monkeypatch):
    for argv in (("hitl", "approve", "1"), ("cos", "approve"), ("agents", "approve")):
        assert _main(monkeypatch, *argv) == 2, argv


# ---------------------------------------------------------------------
# check (CHECK-HUB ## 4) — findings run as written
# ---------------------------------------------------------------------


def test_check_o1_max_turns_keeps_the_partial_reply(tmp_path):
    session, log, dms = _session(
        tmp_path, lambda c: [_assistant("constructed partial one"), _assistant("two"), _assistant("three"),
                             _result()], max_turns=2)
    out = asyncio.run(session.run_turn("constructed", resume=None))
    assert not out.ok and "max turns" in out.error and log[-1].killed
    assert "constructed partial one" in out.reply, "the partial reply is kept for posting (FINAL §5)"


def test_check_o5_tool_result_messages_are_not_rounds(tmp_path):
    from claude_agent_sdk.types import AssistantMessage, TextBlock, ToolResultBlock, UserMessage

    def a(text):
        return AssistantMessage(content=[TextBlock(text)], model="constructed")

    def u():
        return UserMessage(content=[ToolResultBlock(tool_use_id="constructed", content="r")])

    session, log, dms = _session(tmp_path, lambda c: [a("one"), u(), a("two"), u(), a("three"), _result()],
                                 max_turns=3)
    out = asyncio.run(session.run_turn("constructed", resume=None))
    assert out.ok, out.error


def test_check_o6_a_hung_connect_is_inside_the_turn_timeout(tmp_path):
    class HungConnect(FakeClient):
        async def connect(self):
            await asyncio.sleep(3600)

    from cobalt.cos.session import CosSession

    log, dms = [], []
    session = CosSession(model="claude-sonnet-5-5", scratch_dir=tmp_path, charter="constructed",
                         client_factory=lambda o, t: HungConnect(o, t, lambda c: [], log),
                         notify=dms.append, max_turns=5, timeout_s=0.05)
    out = asyncio.run(asyncio.wait_for(session.run_turn("constructed", resume=None), 5))
    assert not out.ok and "timeout" in out.error and dms


def test_max_turns_posts_the_partial_reply(tmp_path):
    session, _log, _dms = _session(
        tmp_path,
        lambda c: [_assistant("partial constructed"), _assistant("more"), _assistant("over")],
        max_turns=1,
    )
    out = asyncio.run(session.run_turn("constructed", resume=None))
    assert not out.ok
    assert "partial constructed" in (out.reply or "")


# ---------------------------------------------------------------------
# fix round W (card 730 row W) — G5, G6
# ---------------------------------------------------------------------

#: The stub CLI: each role writes its pid, starts the next role, sleeps.
STUB_CLI = """\
import os, subprocess, sys, time
role, out = sys.argv[1], sys.argv[2]
nxt = {"cli": "child", "child": "grandchild"}.get(role)
if nxt:
    subprocess.Popen([sys.executable, "-I", __file__, nxt, out])
tmp = os.path.join(out, role + ".pid.tmp")
with open(tmp, "w") as f:
    f.write(str(os.getpid()))
os.replace(tmp, os.path.join(out, role + ".pid"))
time.sleep(600)
"""


def _gone(pid: int) -> bool:
    """No such process, or a zombie (dead, not yet reaped): read the state."""
    state = subprocess.run(["ps", "-o", "stat=", "-p", str(pid)], capture_output=True, text=True).stdout.strip()
    return state == "" or state.startswith("Z")


def _poll(pred, timeout_s=10.0):
    import time

    end = time.monotonic() + timeout_s
    while time.monotonic() < end:
        if pred():
            return True
        time.sleep(0.05)
    return pred()


def test_max_turns_leaves_no_descendant_alive_and_the_resident_stands(tmp_path):
    import signal
    from types import SimpleNamespace

    from cobalt.cos.session import _SdkClient

    script = tmp_path / "stub_cli.py"
    script.write_text(STUB_CLI)
    roles = ("cli", "child", "grandchild")
    cli = subprocess.Popen([sys.executable, "-I", str(script), "cli", str(tmp_path)])
    pids: dict[str, int] = {}
    try:
        assert _poll(lambda: all((tmp_path / f"{r}.pid").exists() for r in roles)), "the stub tree started"
        pids = {r: int((tmp_path / f"{r}.pid").read_text()) for r in roles}
        assert pids["cli"] == cli.pid

        def wrap(fake):
            fake._transport = SimpleNamespace(_process=cli)
            return _SdkClient(fake)

        session, _log, _dms = _session(tmp_path, lambda c: [_assistant("one"), _assistant("two"),
                                                            _assistant("three"), _result()],
                                       max_turns=2, wrap=wrap)
        out = asyncio.run(session.run_turn("constructed", resume=None))
        assert not out.ok and "max turns" in out.error
        alive = [r for r in roles if not _poll(lambda r=r: _gone(pids[r]), 5.0)]
        assert alive == [], f"alive after the max-turns kill: {alive} ({pids})"
        assert not _gone(os.getpid()), "the resident's stand-in (this process) stands"
    finally:
        for pid in pids.values():
            try:
                os.kill(pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        cli.kill()
        cli.wait(5)


def _recorder(calls: list, name: str, ret=None):
    def record(*args, **kwargs):
        calls.append(name)
        return ret

    return record


def test_cos_run_without_the_flag_reaches_the_resident_start_on_a_fake(monkeypatch, capsys):
    from types import SimpleNamespace

    from cobalt.cos import run as run_mod
    from cobalt.jobs import store as store_mod

    calls: list[str] = []
    store = SimpleNamespace(**{m: _recorder(calls, f"store.{m}") for m in
                               ("ensure_schema", "register", "mark_running", "mark_finished", "beat")},
                            kill_switch=_recorder(calls, "store.kill_switch", {"active": False}))

    class FakeLoop:
        def __init__(self, **kwargs):
            calls.append("Loop")

        def run(self):
            calls.append("Loop.run")

    monkeypatch.setattr(run_mod, "refuse_if_agent_alive", _recorder(calls, "refuse_if_agent_alive"))
    monkeypatch.setattr(store_mod, "JobStore", lambda: calls.append("JobStore") or store)
    monkeypatch.setattr(run_mod, "_build", lambda job_store: calls.append("_build") or
                        (SimpleNamespace(poll=lambda: None), [], 1))
    monkeypatch.setattr(run_mod, "Loop", FakeLoop)

    assert _main(monkeypatch, "cos", "run", "--dry-run") == 0
    assert calls == [], "the dry run starts nothing"
    assert "allowed_tools" in capsys.readouterr().out, "the dry run prints the options"

    assert _main(monkeypatch, "cos", "run") == 0
    assert calls.count("Loop.run") == 1, calls
    for step in ("refuse_if_agent_alive", "JobStore", "_build"):
        assert step in calls, (step, calls)


# ---------------------------------------------------------------------
# check r2 (CHECK-HUB ## 4) — findings run as written
# ---------------------------------------------------------------------

#: The stub CLI whose middle process exits: the grandchild is orphaned (reparented), still a descendant of the CLI's run.
STUB_CLI_ORPHAN = """\
import os, subprocess, sys, time
role, out = sys.argv[1], sys.argv[2]
nxt = {"cli": "child", "child": "grandchild"}.get(role)
if nxt:
    subprocess.Popen([sys.executable, "-I", __file__, nxt, out])
tmp = os.path.join(out, role + ".pid.tmp")
with open(tmp, "w") as f:
    f.write(str(os.getpid()))
os.replace(tmp, os.path.join(out, role + ".pid"))
if role == "child":
    while not os.path.exists(os.path.join(out, "grandchild.pid")):
        time.sleep(0.05)
    sys.exit(0)
time.sleep(600)
"""


def test_max_turns_leaves_no_orphaned_descendant_alive(tmp_path):
    import signal
    from types import SimpleNamespace

    from cobalt.cos.session import _SdkClient

    script = tmp_path / "stub_cli.py"
    script.write_text(STUB_CLI_ORPHAN)
    # As `_SdkClient.connect` spawns the CLI: in its own session (pinned below).
    cli = subprocess.Popen([sys.executable, "-I", str(script), "cli", str(tmp_path)], start_new_session=True)
    pids: dict[str, int] = {}
    try:
        assert _poll(lambda: all((tmp_path / f"{r}.pid").exists() for r in ("cli", "child", "grandchild")))
        pids = {r: int((tmp_path / f"{r}.pid").read_text()) for r in ("cli", "child", "grandchild")}
        assert _poll(lambda: _gone(pids["child"])), "the middle process exited"

        def wrap(fake):
            fake._transport = SimpleNamespace(_process=cli)
            return _SdkClient(fake)

        session, _log, _dms = _session(tmp_path, lambda c: [_assistant("one"), _assistant("two"),
                                                            _assistant("three"), _result()],
                                       max_turns=2, wrap=wrap)
        out = asyncio.run(session.run_turn("constructed", resume=None))
        assert not out.ok and "max turns" in out.error
        assert _poll(lambda: _gone(pids["cli"]), 5.0)
        assert _poll(lambda: _gone(pids["grandchild"]), 5.0), f"orphaned grandchild alive ({pids})"
        assert not _gone(os.getpid())
    finally:
        for pid in pids.values():
            try:
                os.kill(pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
        cli.kill()
        cli.wait(5)


def test_the_cli_is_spawned_in_its_own_session_and_the_wrap_is_put_back(tmp_path):
    """O1's fix: the SDK's spawn (`anyio.open_process`) inside `_SdkClient.connect`
    starts the CLI as the leader of a new group, never the resident's."""
    from types import SimpleNamespace

    import anyio

    from cobalt.cos.session import _SdkClient

    real = anyio.open_process

    class Inner:
        async def connect(self):
            process = await anyio.open_process([sys.executable, "-I", "-c", "import time; time.sleep(60)"])
            self._transport = SimpleNamespace(_process=process)

    inner = Inner()
    client = _SdkClient(inner)
    asyncio.run(client.connect())
    pid = inner._transport._process.pid
    try:
        assert anyio.open_process is real, "the wrap is put back after the open"
        assert os.getpgid(pid) == pid != os.getpgrp(), "the CLI leads its own process group"
        client.kill()
        assert _poll(lambda: _gone(pid), 5.0)
        assert not _gone(os.getpid())
    finally:
        try:
            os.kill(pid, 9)
        except ProcessLookupError:
            pass
