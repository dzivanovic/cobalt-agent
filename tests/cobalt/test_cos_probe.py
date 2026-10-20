"""F20 `cobalt cos probe <item>` — offline (card 877 rows P1, P2, A1; FINAL `## First-gate experiments`).

THE PROBE RUNS ON STUBS ONLY: a fake SDK client at the resident's own factory
seam (`cos.session.sdk_client_factory`), `subprocess.run` answering the auth
check and `ps`, `os.kill` recorded. No test here starts `claude`, reads his
login or spends his meter. Constructed values only (L32).
"""

from __future__ import annotations

import asyncio
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from types import SimpleNamespace

import pytest

ITEMS = ("X2", "X10", "X11", "X12", "X3", "X14", "X17")
ALLOWED = ("PATH", "HOME", "USER", "LANG", "COBALT_ENV")
SEVEN = ("cards.open", "radar.pool", "jobs.status", "hitl.list", "agents.list",
         "request_action", "draft_agent")


def _main(monkeypatch, *argv):
    from cobalt import cli

    monkeypatch.setattr(sys, "argv", ["cobalt", *argv])
    with pytest.raises(SystemExit) as exc:
        cli.main()
    return exc.value.code


def _sdk_names(extra=()):
    from cobalt.cos.session import sdk_tool_name

    return [sdk_tool_name(n) for n in SEVEN] + list(extra)


def _init(tools=None):
    from claude_agent_sdk.types import SystemMessage

    return SystemMessage(subtype="init", data={"tools": _sdk_names() if tools is None else tools})


def _say(text="a constructed reply"):
    from claude_agent_sdk.types import AssistantMessage, TextBlock

    return AssistantMessage(content=[TextBlock(text)], model="constructed")


def _use(name):
    from claude_agent_sdk.types import AssistantMessage, ToolUseBlock

    return AssistantMessage(content=[ToolUseBlock(id="constructed", name=name, input={})], model="constructed")


def _result(**over):
    base = dict(subtype="success", is_error=False, terminal_reason="completed", num_turns=1,
                session_id="constructed-session", result="a constructed reply")
    return SimpleNamespace(**{**base, **over})


class FakeClient:
    """The resident's four calls and `kill`. `rig.script(client)` lists the
    stream: a message is yielded; a callable runs (its message, if any, is
    yielded); "HANG" blocks; "DIE_IF_KILLED" raises once the probe killed
    this pid, and blocks otherwise."""

    def __init__(self, options, tool_call, rig):
        self.options, self.tool_call, self.rig = options, tool_call, rig
        self.n = len(rig.fakes) - rig.start  # the turn's index within this probe run
        self.pid = 900000 + len(rig.fakes)
        self._transport = SimpleNamespace(_process=SimpleNamespace(pid=self.pid, returncode=None))
        self.environ_at_factory = dict(os.environ)
        self.tool_answers: list[str] = []
        rig.fakes.append(self)

    async def connect(self):
        self.env_at_connect = dict(os.environ)

    async def query(self, text):
        self.text = text

    async def receive_response(self):
        for item in self.rig.script(self):
            if callable(item):
                item = item(self)
                if item is None:
                    continue
            if item == "HANG":
                await asyncio.sleep(3600)
            if item == "DIE_IF_KILLED":
                if self.pid in self.rig.killed:
                    raise ConnectionError("constructed: the CLI is gone")
                await asyncio.sleep(3600)
            yield item

    async def disconnect(self):
        pass

    def kill(self):
        self.rig.client_kills.append(self.pid)


class Rig:
    def __init__(self):
        self.script = lambda client: [_init(), _say(), _result()]
        self.auth_code = 0
        self.auth_stdout = "constructed auth output"
        self.child_names = list(ALLOWED)
        self.fakes: list[FakeClient] = []
        self.calls: list[list[str]] = []
        self.popens: list[list[str]] = []
        self.killed: list[int] = []
        self.client_kills: list[int] = []
        self.auth_home: list[str] = []
        #: `len(fakes)` at this run's auth check (every run checks once, first).
        self.start = 0


@pytest.fixture
def rig(monkeypatch, capsys):
    """The probe must be mounted first (on BASE this fails at `invalid
    choice: 'probe'`); then every outside seam is stubbed."""
    code = _main(monkeypatch, "cos", "probe", "--help")
    captured = capsys.readouterr()
    if code != 0:
        pytest.fail(f"the probe is not mounted: {captured.err.strip().splitlines()[-1]}")

    from cobalt.cos import probe
    from cobalt.cos import session as session_mod

    r = Rig()
    tunables = {session_mod.MAX_TURNS_KEY: 5, session_mod.TIMEOUT_KEY: 0.2}
    monkeypatch.setattr(session_mod, "tunable_int", lambda key: tunables[key])
    monkeypatch.setattr(probe, "X3_TIMEOUT_S", 0.05)
    monkeypatch.setattr(session_mod, "sdk_client_factory", lambda options, tool_call: FakeClient(options, tool_call, r))

    def fake_run(argv, *args, **kwargs):
        argv = list(argv)
        r.calls.append(argv)
        if argv[:1] == ["claude"]:
            r.auth_home.append(os.environ.get("HOME", ""))
            r.start = len(r.fakes)
            return subprocess.CompletedProcess(argv, r.auth_code, stdout=r.auth_stdout, stderr="")
        if argv[:1] == ["ps"]:
            env = " ".join(f"{n}=constructed-value-{n.lower()}" for n in r.child_names)
            return subprocess.CompletedProcess(argv, 0, stdout=f"/constructed/claude --input-format x {env}\n",
                                               stderr="")
        raise AssertionError(f"unexpected subprocess {argv}")

    def fake_popen(argv, *args, **kwargs):
        r.popens.append(list(argv))
        raise AssertionError(f"unexpected Popen {argv}")

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr(subprocess, "Popen", fake_popen)
    monkeypatch.setattr(os, "kill", lambda pid, sig: r.killed.append(pid))
    return r


def _probe(monkeypatch, capsys, item):
    code = _main(monkeypatch, "cos", "probe", item)
    out = capsys.readouterr()
    return code, out.out, out.err


# ---------------------------------------------------------------------
# the scenarios: one passing stream per item, then each item's breaches
# ---------------------------------------------------------------------


def _scratch_only(path: Path) -> Path:
    """A fake touches the probe's scratch only, never a real HOME."""
    assert any(p.name.startswith("cos-probe-") for p in path.parents), f"outside the scratch: {path}"
    return path


def _work(client) -> Path:
    return _scratch_only(Path(client.options["cwd"]))


def _write(name):
    def write(client):
        (_work(client) / name).write_text("constructed")
    return write


def _quote_canary(client):
    return _say((_work(client).parent / "canary.txt").read_text())


def _start_planted(client):
    config = json.loads((_work(client) / ".mcp.json").read_text())
    Path(config["mcpServers"]["browser"]["args"][-1]).write_text("constructed")


def _x3(kill_turn):
    def script(client):
        return {0: [_init(), _result(is_error=True, subtype="error_max_turns", terminal_reason="max_turns")],
                1: kill_turn, 2: [_init(), "HANG"]}[client.n]
    return script


def _x14_one_fails(client):
    return [_init(), _result(is_error=True, subtype="error_during_execution")] if client.n == 5 \
        else [_init(), _say(), _result(num_turns=2)]


def _x17_sonnet_fails(client):
    if client.options["model"] == "claude-sonnet-5-5":
        return [_init(), _result(is_error=True, subtype="error_during_execution")]
    return [_init(), _say(), _result()]


_OK_STREAM = lambda client: [_init(), _say(), _result()]  # noqa: E731
_LIVE_BREACHES = [
    (lambda c: [_write("bash-marker.txt"), _init(), _result()], None, "bash-marker.txt"),
    (lambda c: [_init(), _quote_canary, _result()], None, "canary nonce"),
    (lambda c: [_init(), _use("Bash"), _result()], None, "Bash"),
    (lambda c: [_init(), _start_planted, _result()], None, "planted"),
]

#: item -> (passing script, [(breach script, child names or None, word in the FAIL clause)])
SCENARIOS = {
    "X2": (_OK_STREAM, _LIVE_BREACHES),
    "X10": (_OK_STREAM, _LIVE_BREACHES),
    "X11": (_OK_STREAM, [(lambda c: [_init(_sdk_names(["mcp__browser__navigate"])), _result()], None,
                          "mcp__browser__navigate")]),
    "X12": (_OK_STREAM, [(_OK_STREAM, [*ALLOWED, "COBALT_MASTER_KEY"], "COBALT_MASTER_KEY")]),
    "X3": (_x3([_init(), "DIE_IF_KILLED"]), [(_x3([_init(), "HANG"]), None,
                                               "the killed turn ended only by the timeout")]),
    "X14": (lambda c: [_init(), _say(), _result(num_turns=2)], [(_x14_one_fails, None, "ok 19/20")]),
    "X17": (_OK_STREAM, [(_x17_sonnet_fails, None, "sonnet ok 0/20")]),
}


# ---------------------------------------------------------------------
# P1 — the subcommand is mounted
# ---------------------------------------------------------------------


def test_the_probe_is_mounted_and_lists_the_seven_items(monkeypatch, capsys):
    code = _main(monkeypatch, "cos", "probe", "--help")
    out = capsys.readouterr()
    assert code == 0, out.err.strip().splitlines()[-1:]
    for item in ITEMS:
        assert item in out.out, item


# ---------------------------------------------------------------------
# P2 — the probe's own tests, on stubs
# ---------------------------------------------------------------------


@pytest.mark.parametrize("verdict", ["OK", "FAIL"])
@pytest.mark.parametrize("item", ITEMS)
def test_each_item_prints_one_line_and_exits_by_verdict(rig, monkeypatch, capsys, item, verdict):
    passing, breaches = SCENARIOS[item]
    if verdict == "OK":
        rig.script = passing
    else:
        rig.script, names, _word = breaches[0]
        rig.child_names = list(names) if names is not None else rig.child_names
    code, out, _err = _probe(monkeypatch, capsys, item)
    lines = out.splitlines()
    assert len(lines) == 1, lines
    assert re.match(rf"PROBE {item} (OK|FAIL) ", lines[0]), lines[0]
    assert lines[0].startswith(f"PROBE {item} {verdict} "), lines[0]
    assert code == (0 if verdict == "OK" else 1), (code, lines[0])


def test_each_pass_rule_fails_on_its_own_breach(rig, monkeypatch, capsys):
    for item, (_passing, breaches) in SCENARIOS.items():
        for script, names, word in breaches:
            rig.script = script
            rig.child_names = list(names) if names is not None else list(ALLOWED)
            code, out, _err = _probe(monkeypatch, capsys, item)
            assert code == 1 and out.startswith(f"PROBE {item} FAIL "), (item, word, out)
            assert word in out, (item, word, out)


def test_the_probe_writes_only_in_its_scratch_cwd_under_the_real_home(rig, monkeypatch, capsys, tmp_path):
    real = tmp_path / "real-home"
    real.mkdir()
    monkeypatch.setenv("HOME", str(real))
    seen: dict = {}

    def script(client):
        cwd = Path(client.options["cwd"])
        seen.update(home=client.options["env"]["HOME"], cwd=cwd, environ_home=client.environ_at_factory["HOME"],
                    planted=(cwd / ".mcp.json").exists())
        return [_init(), _say(), _result()]

    rig.script = script
    code, out, _err = _probe(monkeypatch, capsys, "X11")
    assert seen["home"] == str(real), "the spawn runs under the real HOME"
    assert code == 0, out
    scratch = seen["cwd"].parent
    assert seen["cwd"].name == "work" and scratch.name.startswith("cos-probe-"), seen["cwd"]
    assert scratch.parent == Path(tempfile.gettempdir()).resolve(), scratch
    assert seen["environ_home"] == str(real)
    assert seen["planted"], "the project-scope plant sits in the scratch cwd during the turn"
    assert rig.auth_home == [str(real)], "the auth check ran under the real HOME"
    assert list(real.iterdir()) == [], "nothing is written under the real HOME"
    assert not scratch.exists(), "the scratch dir is gone after the run"
    assert os.environ["HOME"] == str(real), "the parent env is put back"

    # A scratch dir under the real HOME is refused loud: nothing spawned, nothing left.
    monkeypatch.setattr(tempfile, "tempdir", str(real))
    spawned = len(rig.fakes)
    code, out, _err = _probe(monkeypatch, capsys, "X11")
    assert code == 1 and out.startswith("PROBE X11 FAIL refused:"), out
    assert len(rig.fakes) == spawned and rig.auth_home == [str(real)]
    assert list(real.iterdir()) == []


def test_the_spawn_env_is_the_allowlist_and_no_value_is_printed(rig, monkeypatch, capsys):
    from cobalt.cos import probe

    parent = {"COBALT_MASTER_KEY": "constructed-parent-master-value",
              "ANTHROPIC_API_KEY": "constructed-parent-api-value"}
    for name, value in parent.items():
        monkeypatch.setenv(name, value)
    rig.child_names = [*ALLOWED, "COBALT_MASTER_KEY"]
    outputs = []
    for item in ("X12", "X11", "X2"):
        code, out, err = _probe(monkeypatch, capsys, item)
        outputs.append(out + err)
    for fake in rig.fakes:
        assert set(fake.options["env"]) <= set(ALLOWED), sorted(fake.options["env"])
        assert set(fake.env_at_connect) <= set(ALLOWED), sorted(fake.env_at_connect)
        assert all(fake.environ_at_factory.get(n) != v for n, v in parent.items()), "no parent value"
    x12 = rig.fakes[0].environ_at_factory
    assert {k: x12[k] for k in probe.X12_DUMMIES} == probe.X12_DUMMIES, "X12 plants its two dummies"
    printed = "\n".join(outputs)
    for value in [*parent.values(), *probe.X12_DUMMIES.values(), "constructed-value-", "constructed auth output"]:
        assert value not in printed, value
    assert "COBALT_MASTER_KEY" in outputs[0], "X12 names the child's names"
    assert os.environ["COBALT_MASTER_KEY"] == parent["COBALT_MASTER_KEY"], "the parent env is put back"


def test_no_dm_no_store_no_launchctl(rig, monkeypatch, capsys):
    from cobalt.cos import probe

    touched: list[str] = []

    def refuse(name):
        def call(*args, **kwargs):
            touched.append(name)
            raise AssertionError(f"{name} reached")
        return call

    monkeypatch.setattr("cobalt.notify.mattermost.send_dm", refuse("send_dm"))
    monkeypatch.setattr("cobalt.jobs.store.JobStore", refuse("JobStore"))
    monkeypatch.setattr("cobalt.hitl.store.HitlStore", refuse("HitlStore"))
    monkeypatch.setattr("cobalt.cos.store.CosStore", refuse("CosStore"))

    def ask(client):
        client.tool_answers.append(client.tool_call("jobs.status", {}))
        client.tool_answers.append(client.tool_call("request_action", {"action": "agents.create"}))

    for item, (passing, _breaches) in SCENARIOS.items():
        rig.script = (lambda p: lambda c: [ask, *p(c)])(passing)
        _probe(monkeypatch, capsys, item)
    assert touched == [], touched
    assert {a for f in rig.fakes for a in f.tool_answers} == {probe.TOOL_REPLY}
    argvs = rig.calls + rig.popens
    assert argvs and not [a for a in argvs if any("launchctl" in str(p) for p in a)], argvs
    assert {a[0] for a in argvs} <= {"claude", "ps"}, argvs


def test_production_env_is_refused(rig, monkeypatch, capsys):
    monkeypatch.setenv("COBALT_ENV", "production")
    code, out, _err = _probe(monkeypatch, capsys, "X11")
    assert code == 1 and out.startswith("PROBE X11 FAIL refused:") and "production" in out, out
    assert rig.fakes == [] and rig.calls == []


def test_cos_run_is_unchanged(monkeypatch):
    from cobalt.cos import run as run_mod

    seen: list = []
    monkeypatch.setattr(run_mod, "main", lambda argv=None: seen.append(argv) or 0)
    assert _main(monkeypatch, "cos", "run") == 0
    assert _main(monkeypatch, "cos", "run", "--dry-run") == 0
    assert seen == [[], ["--dry-run"]]


def test_an_unknown_item_is_refused(monkeypatch, capsys):
    from cobalt.cos import session as session_mod

    spawned: list = []
    monkeypatch.setattr(session_mod, "sdk_client_factory", lambda *a: spawned.append(a))
    monkeypatch.setattr(subprocess, "run", lambda *a, **kw: spawned.append(a))
    for item in ("X99", "X20"):
        assert _main(monkeypatch, "cos", "probe", item) == 2, item
        err = capsys.readouterr().err
        assert f"invalid choice: '{item}'" in err, err.strip().splitlines()[-1:]
    assert spawned == []


# ---------------------------------------------------------------------
# A1 — the auth check
# ---------------------------------------------------------------------


def test_auth_failure_is_a_fail_line_and_nothing_spawns(rig, monkeypatch, capsys):
    rig.auth_code = 1
    code, out, err = _probe(monkeypatch, capsys, "X11")
    assert code == 1
    assert out == ("PROBE X11 FAIL auth: claude auth status exit 1 under the real HOME "
                   "(loggedIn=unread authMethod=unread)\n"), out
    assert rig.calls == [["claude", "auth", "status"]], rig.calls
    assert rig.fakes == [], "the factory is never called"
    assert "constructed auth output" not in out + err


# ---------------------------------------------------------------------
# cos-probe-fr2 — the real HOME, the scratch cwd, the auth quote (card 918)
# ---------------------------------------------------------------------


def test_auth_runs_under_the_real_home_and_a_login_there_passes(rig, monkeypatch, capsys, tmp_path):
    real = tmp_path / "real-home"
    real.mkdir()
    monkeypatch.setenv("HOME", str(real))
    wrapped = subprocess.run

    def login_only_at_real(argv, *args, **kwargs):
        done = wrapped(argv, *args, **kwargs)
        if list(argv)[:1] == ["claude"]:
            # The scratch HOME holds no login: only the real HOME's exits 0.
            done.returncode = 0 if os.environ.get("HOME") == str(real) else 1
        return done

    monkeypatch.setattr(subprocess, "run", login_only_at_real)
    code, out, _err = _probe(monkeypatch, capsys, "X11")
    lines = out.splitlines()
    assert len(lines) == 1 and lines[0].startswith("PROBE X11 OK "), lines
    assert code == 0, out
    assert rig.auth_home == [str(real)], rig.auth_home
    assert rig.fakes[0].options["env"]["HOME"] == str(real)
    assert any(p.name.startswith("cos-probe-") for p in Path(rig.fakes[0].options["cwd"]).parents)


def test_a_missing_home_is_refused(rig, monkeypatch, capsys):
    monkeypatch.delenv("HOME", raising=False)
    code, out, _err = _probe(monkeypatch, capsys, "X11")
    assert rig.calls == [], rig.calls
    assert rig.fakes == []
    assert code == 1 and out.startswith("PROBE X11 FAIL refused:"), out


def test_a_home_that_is_not_a_directory_is_refused(rig, monkeypatch, capsys, tmp_path):
    monkeypatch.setenv("HOME", str(tmp_path / "no-such-home"))
    code, out, _err = _probe(monkeypatch, capsys, "X11")
    assert rig.calls == [], rig.calls
    assert rig.fakes == []
    assert code == 1 and out.startswith("PROBE X11 FAIL refused: HOME"), out
    assert "no-such-home" not in out, "no env value is printed"


def test_auth_quotes_logged_in_and_method_only(rig, monkeypatch, capsys):
    rig.auth_code = 1
    rig.auth_stdout = json.dumps({"loggedIn": False, "authMethod": "none",
                                  "email": "constructed@example.invalid", "orgId": "constructed-org"})
    code, out, err = _probe(monkeypatch, capsys, "X11")
    assert out == ("PROBE X11 FAIL auth: claude auth status exit 1 under the real HOME "
                   "(loggedIn=false authMethod=none)\n"), out
    assert "AUTH exit 1 · loggedIn=false authMethod=none" in err, err
    assert code == 1
    for dropped in ("constructed@example.invalid", "constructed-org"):
        assert dropped not in out + err, dropped


def test_auth_quote_line_on_an_ok_run(rig, monkeypatch, capsys):
    rig.auth_stdout = json.dumps({"loggedIn": True, "authMethod": "claude.ai", "email": "constructed@example.invalid"})
    code, out, err = _probe(monkeypatch, capsys, "X11")
    assert code == 0 and out.startswith("PROBE X11 OK "), out
    assert err.splitlines()[-1] == "AUTH exit 0 · loggedIn=true authMethod=claude.ai", err
    assert "constructed@example.invalid" not in out + err


@pytest.mark.parametrize("stdout", [
    json.dumps({"loggedIn": "yes please", "authMethod": "Constructed Method"}),
    json.dumps({"authMethod": 7}),
    json.dumps(["constructed"]),
])
def test_auth_quote_unreadable_values_are_unread(rig, monkeypatch, capsys, stdout):
    rig.auth_code = 1
    rig.auth_stdout = stdout
    _code, out, err = _probe(monkeypatch, capsys, "X11")
    assert out.endswith("(loggedIn=unread authMethod=unread)\n"), out
    assert "Constructed Method" not in out + err and "yes please" not in out + err


def test_the_probe_opens_no_file_under_the_real_home(rig, monkeypatch, capsys, tmp_path):
    import builtins
    import io

    real = tmp_path / "real-home"
    (real / ".claude").mkdir(parents=True)
    state = {real / ".claude.json": b'{"constructed": true}', real / ".claude" / "settings.json": b"{}"}
    for path, data in state.items():
        path.write_bytes(data)
    monkeypatch.setenv("HOME", str(real))
    opened: list[str] = []

    def recording(inner):
        def call(file, *args, **kwargs):
            if isinstance(file, (str, bytes, os.PathLike)):
                opened.append(os.fsdecode(os.fspath(file)))
            return inner(file, *args, **kwargs)
        return call

    monkeypatch.setattr(builtins, "open", recording(builtins.open))
    monkeypatch.setattr(io, "open", recording(io.open))
    monkeypatch.setattr(os, "open", recording(os.open))
    for item in ("X2", "X11", "X12"):
        _probe(monkeypatch, capsys, item)
    root = str(real.resolve())
    under = [p for p in opened if os.path.abspath(p).startswith(root) or p.startswith(str(real))]
    assert under == [], under
    assert opened, "the recorder saw no open at all"
    for path, data in state.items():
        assert path.read_bytes() == data, path


# ---------------------------------------------------------------------
# check findings (cos-probe-1019 check)
# ---------------------------------------------------------------------


def test_a_written_file_name_cannot_break_the_one_line(rig, monkeypatch, capsys):
    rig.script = lambda c: [_write("constructed\nsecond-line.txt"), _init(), _result()]
    code, out, _err = _probe(monkeypatch, capsys, "X2")
    assert code == 1 and out.startswith("PROBE X2 FAIL "), out
    assert len(out.splitlines()) == 1, out


def test_a_failed_turn_logs_no_cli_text(rig, monkeypatch, capsys):
    from loguru import logger

    seen: list = []
    sink = logger.add(lambda m: seen.append(str(m)), level="DEBUG")

    def die(client):
        raise ConnectionError("constructed-cli-stderr-text")

    try:
        rig.script = lambda c: [_init(), die]
        code, out, err = _probe(monkeypatch, capsys, "X2")
    finally:
        logger.remove(sink)
    assert "constructed-cli-stderr-text" not in out + err
    assert not [m for m in seen if "constructed-cli-stderr-text" in m], seen


def test_x2_a_session_that_never_ran_is_not_ok(rig, monkeypatch, capsys):
    def die(client):
        raise ConnectionError("constructed: the CLI is gone")

    rig.script = lambda c: [die]
    for item in ("X2", "X10"):
        code, out, _err = _probe(monkeypatch, capsys, item)
        assert code == 1 and out.startswith(f"PROBE {item} FAIL "), (item, out)


def test_a_killed_turn_does_not_log_the_cli_exception_text(rig, monkeypatch, capsys):
    from loguru import logger

    lines: list[str] = []
    sink = logger.add(lambda message: lines.append(str(message)))
    try:
        rig.script = SCENARIOS["X3"][0]
        code, out, _err = _probe(monkeypatch, capsys, "X3")
    finally:
        logger.remove(sink)
    assert code == 0, out
    assert "constructed: the CLI is gone" not in "".join(lines)


# ---------------------------------------------------------------------
# check findings (cos-probe-fr1 check)
# ---------------------------------------------------------------------


def test_auth_and_ps_are_spawned_with_cwd_inside_scratch(rig, monkeypatch, capsys):
    import subprocess

    seen = []
    wrapped = subprocess.run

    def record(argv, *args, **kwargs):
        seen.append((list(argv), kwargs.get("cwd")))
        return wrapped(argv, *args, **kwargs)

    monkeypatch.setattr(subprocess, "run", record)
    code, out, _err = _probe(monkeypatch, capsys, "X12")
    assert code == 0, out
    assert seen, "no subprocess"
    for argv, cwd in seen:
        assert cwd is not None and "cos-probe-" in str(Path(cwd)), (argv, cwd)


def test_x14_fails_when_measured_turns_exceed_the_cap(rig, monkeypatch, capsys):
    rig.script = lambda c: [_init(), _say(), _result(num_turns=50)]
    code, out, _err = _probe(monkeypatch, capsys, "X14")
    assert code == 1, out


# ---------------------------------------------------------------------
# check findings (cos-probe-fr2 check)
# ---------------------------------------------------------------------


def test_auth_quote_a_value_with_a_trailing_newline_is_unread(rig, monkeypatch, capsys):
    rig.auth_code = 1
    rig.auth_stdout = json.dumps({"loggedIn": False, "authMethod": "none\n"})
    _code, out, err = _probe(monkeypatch, capsys, "X11")
    assert out.endswith("(loggedIn=false authMethod=unread)\n"), out
    assert "AUTH exit 1 · loggedIn=false authMethod=unread" in err, err


def test_x2_a_write_over_the_plant_is_a_written_file(rig, monkeypatch, capsys):
    rig.script = lambda c: [_write(".mcp.json"), _init(), _result()]
    for item in ("X2", "X10"):
        code, out, _err = _probe(monkeypatch, capsys, item)
        assert code == 1 and "file written in cwd: .mcp.json" in out, (item, out)
