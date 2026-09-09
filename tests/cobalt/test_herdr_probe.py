"""F18's `herdr` probe — the terminal workspace every agent seat lives in.

THREE QUESTIONS, ALL ASKED, and that is the whole design. A socket file
outlives the process that created it, and a wedged server still holds
its socket open — so "the socket is there" cannot be the test any more
than "the process exists" could be the test for the ASET sheet (S1-P2
watched that one serve 500s while perfectly alive). The probe connects,
and then asks the server something it can only answer by traversing its
own live pane state.

Every test here drives a REAL AF_UNIX socket in a temp directory. A
mocked-out `socket` module would prove the code calls a function; a real
listener proves the probe can tell "accepting" from "stale file", which
is the distinction it exists to make.

THE THIRD QUESTION (2026-09-09) is whether `hooks.SessionStart` is still
EXACTLY the one harness-aware guard entry. It belongs to this probe and
not to a housekeeping check because `agent list` — the second question —
is the list a drifted hook silently corrupts: herdr's Claude integration
hardcodes `herdr:claude` with no harness detection, so without the guard
every Grok session reports itself as `claude`. On 09-09 at 08:33 an
integration update APPENDED a second entry rather than replacing the
pointer, which is why the assertion is a COUNT and not a presence check.
"""

import json
import socket
import tempfile
from pathlib import Path

import pytest

from cobalt.heartbeat import probes
from cobalt.jobs.config import load_job_registry

LABEL = "com.cobalt.herdr"

AGENTS = [
    {"agent": "claude", "pane_id": "w1:p1", "agent_status": "working"},
    {"agent": "codex", "pane_id": "w1:p6", "agent_status": "idle"},
]


@pytest.fixture
def live_socket():
    """A real listening AF_UNIX socket, short-pathed: macOS caps a unix
    socket path at ~104 bytes and pytest's tmp_path is long enough to
    trip it."""
    with tempfile.TemporaryDirectory(dir="/tmp") as d:
        path = Path(d) / "herdr.sock"
        server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        server.bind(str(path))
        server.listen(1)
        try:
            yield path
        finally:
            server.close()


@pytest.fixture
def stale_socket():
    """A socket FILE with nothing listening — what a killed server leaves
    behind, and the case a bare `path.exists()` check would call green."""
    with tempfile.TemporaryDirectory(dir="/tmp") as d:
        path = Path(d) / "herdr.sock"
        s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.bind(str(path))
        s.close()          # the file survives; nothing is listening
        yield path


def write_settings(tmp_path, entries) -> Path:
    """A `~/.claude/settings.json` shaped exactly like the real one, with
    whatever `hooks.SessionStart` the test wants to describe."""
    path = tmp_path / "settings.json"
    path.write_text(json.dumps({"model": "opus", "hooks": {"SessionStart": entries}}))
    return path


def write_guard(tmp_path, *, executable: bool = True) -> Path:
    path = tmp_path / "herdr-harness-guard.sh"
    path.write_text("#!/bin/sh\nexit 0\n")
    path.chmod(0o755 if executable else 0o644)
    return path


def one_good_entry(guard: Path) -> list:
    """The live 2026-09-09 shape, verbatim in structure."""
    return [
        {
            "matcher": "*",
            "hooks": [
                {"type": "command", "command": f"sh '{guard}' session", "timeout": 10}
            ],
        }
    ]


@pytest.fixture
def good_hooks(tmp_path):
    """Settings + guard in the state the probe wants to find. Returned as
    the kwargs every post-handover probe call passes, so a test that
    cares about the socket does not have to care about hooks."""
    guard = write_guard(tmp_path)
    return {"settings_path": write_settings(tmp_path, one_good_entry(guard)),
            "guard_path": guard}


@pytest.fixture
def enabled(monkeypatch):
    """Pretend the handover has happened. Shipped state is
    `enabled: false`, which is asserted separately below."""
    monkeypatch.setattr(probes, "_herdr_enabled", lambda: (True, ""))


# =====================================================================
# the shipped state: built, registered, deliberately not loaded
# =====================================================================


class TestTheShippedState:
    """The handover happened on 2026-09-08 at 19:21 ET: the plist is
    installed, launchd owns the server, and the registry row says so.

    These four tests asserted the PRE-handover state and were red on
    `main` from the evening of the flip until 2026-09-09 — a suite
    describing a world that had moved on. They now assert the world that
    exists, and the disabled BRANCH (which is still live code, and still
    the right behaviour for the next job built-but-not-loaded) is covered
    below by flipping the flag on a stub registry rather than by leaving
    the shipped file in a state nobody wants.
    """

    def test_the_registry_ships_it_enabled(self):
        spec = load_job_registry().spec(LABEL)
        assert spec.enabled is True, (
            "com.cobalt.herdr has been under launchd since 2026-09-08 19:21 ET "
            "(pid 72998 on 09-09, herdr 0.9.0). `enabled: false` would take the "
            "probe off and paint a live server as deliberately absent."
        )

    def test_the_probe_actually_probes(self, tmp_path):
        """The flag is what suppresses the probe, so with it true the
        probe must reach the socket — even to say it is not there."""
        probe = probes.herdr(socket_path=tmp_path / "nothing.sock")
        assert not probe.ok
        assert LABEL in probe.detail


class TestTheDisabledBranchStillWorks:
    """`enabled: false` is the declared state of a job that is built,
    registered and reviewable but not handed over. No row ships that way
    today; the branch is kept because the next one will."""

    @pytest.fixture
    def disabled(self, monkeypatch):
        monkeypatch.setattr(probes, "_herdr_enabled", lambda: (False, ""))

    def test_the_probe_is_green_and_says_why(self, disabled):
        probe = probes.herdr()
        assert probe.ok
        assert "enabled: false" in probe.detail
        assert "handover" in probe.detail
        assert not probe.unknown

    def test_it_does_not_touch_the_socket_while_disabled(self, disabled, monkeypatch):
        def explode(*a, **k):
            raise AssertionError("a disabled job must not be probed")

        monkeypatch.setattr(probes.socket, "socket", explode)
        assert probes.herdr().ok

    def test_it_does_not_read_the_hook_settings_while_disabled(self, disabled, monkeypatch):
        """With no server under launchd there is no `agent list` for a
        mislabelled seat to corrupt, so the third question is skipped
        too — and skipped for a reason, not by omission."""

        def explode(*a, **k):
            raise AssertionError("a disabled job must not read the hook settings")

        monkeypatch.setattr(probes, "_check_hook_guard", explode)
        assert probes.herdr().ok

    def test_the_sweep_reports_it_without_probing_launchd(self, monkeypatch):
        """The watchdog asks `launchctl` about every job FIRST. A row that
        is deliberately not loaded would answer 'NOT LOADED' forever, and
        a standing red is how a heartbeat stops being read."""
        from cobalt.jobs import watchdog

        def explode(label, **k):
            raise AssertionError(f"launchctl must not be asked about {label}")

        monkeypatch.setattr(watchdog, "launchctl_status", explode)

        spec = load_job_registry().spec(LABEL).model_copy(update={"enabled": False})

        class OnlyHerdr:
            jobs = [spec]

        class NoRows:
            def ensure_schema(self, **k):
                pass

            def all(self):
                return []

        findings = watchdog.sweep(store=NoRows(), registry=OnlyHerdr(), probe=True)
        assert len(findings) == 1
        finding = findings[0]
        assert finding.label == LABEL
        assert finding.ok, "a deliberately unloaded job is not a failure"
        assert finding.state == "disabled"
        assert "NOT LOADED BY DESIGN" in finding.detail


# =====================================================================
# after the handover: the socket and the agent list
# =====================================================================


class TestTheFirstTwoQuestions:
    def test_a_live_socket_and_a_real_agent_list_is_green(self, enabled, live_socket, good_hooks):
        probe = probes.herdr(
            socket_path=live_socket, list_agents=lambda binary, timeout: AGENTS, **good_hooks
        )
        assert probe.ok
        assert "2 pane(s)" in probe.detail
        assert "claude, codex" in probe.detail

    def test_a_missing_socket_is_red_and_names_the_label(self, enabled, tmp_path):
        probe = probes.herdr(socket_path=tmp_path / "nothing.sock")
        assert not probe.ok
        assert LABEL in probe.detail
        assert "not running" in probe.detail

    def test_a_stale_socket_file_is_red_not_green(self, enabled, stale_socket, good_hooks):
        """The case a `path.exists()` check gets wrong: the file is there
        and the server is gone."""
        probe = probes.herdr(
            socket_path=stale_socket, list_agents=lambda binary, timeout: AGENTS, **good_hooks
        )
        assert not probe.ok
        assert "REFUSED a connection" in probe.detail
        assert LABEL in probe.detail

    def test_a_socket_that_accepts_but_will_not_answer_is_red(self, enabled, live_socket, good_hooks):
        """Up and not serving. Accepting a connection is not answering a
        question, and only the second one means the seats work."""

        def broken(binary, timeout):
            raise RuntimeError("`herdr agent list` exited 1: protocol mismatch")

        probe = probes.herdr(socket_path=live_socket, list_agents=broken, **good_hooks)
        assert not probe.ok
        assert "did not answer `agent list`" in probe.detail
        assert LABEL in probe.detail

    def test_an_empty_pane_list_is_still_green(self, enabled, live_socket, good_hooks):
        """A server with no seats attached is idle, not broken — the
        probe watches the SERVER, and 'nobody is working right now' is
        not a fault."""
        probe = probes.herdr(socket_path=live_socket, list_agents=lambda b, t: [], **good_hooks)
        assert probe.ok and "0 pane(s)" in probe.detail


class TestTheAgentListParser:
    def test_output_without_an_agents_array_is_an_error(self, monkeypatch):
        import subprocess

        class Proc:
            returncode = 0
            stdout = '{"id":"cli:agent:list","result":{}}'
            stderr = ""

        monkeypatch.setattr(subprocess, "run", lambda *a, **k: Proc())
        with pytest.raises(RuntimeError, match="no `result.agents`"):
            probes._herdr_agent_list(Path("/opt/homebrew/bin/herdr"), 5.0)

    def test_a_non_zero_exit_is_an_error(self, monkeypatch):
        import subprocess

        class Proc:
            returncode = 1
            stdout = ""
            stderr = "server not running"

        monkeypatch.setattr(subprocess, "run", lambda *a, **k: Proc())
        with pytest.raises(RuntimeError, match="exited 1"):
            probes._herdr_agent_list(Path("/opt/homebrew/bin/herdr"), 5.0)

    def test_it_reads_the_shape_the_live_server_returns(self, monkeypatch):
        """Recorded from `herdr agent list` against herdr 0.8.2 on
        2026-09-08 — the parser is pinned to a real payload, not to a
        guess about one."""
        import subprocess

        class Proc:
            returncode = 0
            stdout = (
                '{"id":"cli:agent:list","result":{"agents":['
                '{"agent":"claude","agent_status":"working","pane_id":"w1:p1"},'
                '{"agent":"grok","agent_status":"idle","pane_id":"w1:pB"}'
                '],"type":"agent_list"}}'
            )
            stderr = ""

        monkeypatch.setattr(subprocess, "run", lambda *a, **k: Proc())
        agents = probes._herdr_agent_list(Path("/opt/homebrew/bin/herdr"), 5.0)
        assert [a["agent"] for a in agents] == ["claude", "grok"]


# =====================================================================
# the third question: the SessionStart hook guard
# =====================================================================


class TestTheHookGuardCheck:
    """The five shapes `~/.claude/settings.json` can be in.

    THE ONE THAT ACTUALLY HAPPENED is `two_entries`: on 2026-09-09 at
    08:33 `herdr integration install claude` (v8 -> v9) did not replace
    the guard pointer — it APPENDED a second SessionStart entry aimed at
    herdr's own script, so both would have fired. A presence check would
    have called that fine, which is why the assertion is a count.
    """

    def test_one_correct_entry_is_the_good_case(self, tmp_path):
        guard = write_guard(tmp_path)
        settings = write_settings(tmp_path, one_good_entry(guard))
        line = probes._check_hook_guard(settings, guard)
        assert "1 SessionStart entry" in line
        assert guard.name in line

    def test_zero_entries_is_drift(self, tmp_path):
        guard = write_guard(tmp_path)
        settings = write_settings(tmp_path, [])
        with pytest.raises(probes.HookGuardDrift) as exc:
            probes._check_hook_guard(settings, guard)
        assert "0 entries" in str(exc.value)
        assert "report as claude" in str(exc.value)

    def test_two_entries_is_drift_and_names_what_happened(self, tmp_path):
        """The 09-09 08:33 shape, reproduced."""
        guard = write_guard(tmp_path)
        herdr_own = {
            "matcher": "*",
            "hooks": [
                {"type": "command",
                 "command": "sh '/Users/cobalt/.claude/hooks/herdr-agent-state.sh' session"}
            ],
        }
        settings = write_settings(tmp_path, one_good_entry(guard) + [herdr_own])
        with pytest.raises(probes.HookGuardDrift) as exc:
            probes._check_hook_guard(settings, guard)
        message = str(exc.value)
        assert "2 entries, expected exactly 1" in message
        assert "appended/replaced" in message
        assert "Grok sessions will report as claude" in message

    def test_one_entry_pointing_somewhere_else_is_drift(self, tmp_path):
        """The failure the checklist line was written for: the pointer
        reverted to herdr's own script. Present, single, and wrong."""
        guard = write_guard(tmp_path)
        settings = write_settings(tmp_path, [{
            "matcher": "*",
            "hooks": [{"type": "command", "command": "sh '/somewhere/else.sh' session"}],
        }])
        with pytest.raises(probes.HookGuardDrift) as exc:
            probes._check_hook_guard(settings, guard)
        assert "does not run" in str(exc.value)

    def test_a_missing_guard_script_is_drift(self, tmp_path):
        guard = write_guard(tmp_path)
        settings = write_settings(tmp_path, one_good_entry(guard))
        guard.unlink()
        with pytest.raises(probes.HookGuardDrift) as exc:
            probes._check_hook_guard(settings, guard)
        assert "DOES NOT EXIST" in str(exc.value)

    def test_a_non_executable_guard_is_drift(self, tmp_path):
        """It is `sh <path>` today, which would run anyway — but the hook
        contract is an executable script, and a chmod that went missing
        is a thing to fix before the next integration update makes it
        matter."""
        guard = write_guard(tmp_path, executable=False)
        settings = write_settings(tmp_path, one_good_entry(guard))
        with pytest.raises(probes.HookGuardDrift) as exc:
            probes._check_hook_guard(settings, guard)
        assert "NOT EXECUTABLE" in str(exc.value)

    def test_two_command_hooks_inside_one_entry_is_drift(self, tmp_path):
        """The other way to append: same entry, second hook. Counting
        entries alone would miss it."""
        guard = write_guard(tmp_path)
        entries = one_good_entry(guard)
        entries[0]["hooks"].append({"type": "command", "command": "sh '/other.sh'"})
        settings = write_settings(tmp_path, entries)
        with pytest.raises(probes.HookGuardDrift) as exc:
            probes._check_hook_guard(settings, guard)
        assert "2 command hook(s)" in str(exc.value)

    def test_unparseable_settings_is_drift_not_a_shrug(self, tmp_path):
        guard = write_guard(tmp_path)
        settings = tmp_path / "settings.json"
        settings.write_text("{ not json")
        with pytest.raises(probes.HookGuardDrift) as exc:
            probes._check_hook_guard(settings, guard)
        assert "UNKNOWN" in str(exc.value)

    def test_missing_settings_file_is_drift(self, tmp_path):
        guard = write_guard(tmp_path)
        with pytest.raises(probes.HookGuardDrift) as exc:
            probes._check_hook_guard(tmp_path / "nope.json", guard)
        assert "does not exist" in str(exc.value)


class TestDriftTurnsTheProbeRed:
    """The unit above answers the question; this is the probe carrying
    the answer, with a live socket and a healthy `agent list`."""

    def test_a_healthy_server_with_a_drifted_hook_is_RED(
        self, enabled, live_socket, tmp_path
    ):
        guard = write_guard(tmp_path)
        settings = write_settings(tmp_path, one_good_entry(guard) * 2)
        probe = probes.herdr(
            socket_path=live_socket,
            list_agents=lambda b, t: AGENTS,
            settings_path=settings,
            guard_path=guard,
        )
        assert not probe.ok
        assert "SEAT LABELS ARE NOT TRUSTWORTHY" in probe.detail
        assert "2 entries" in probe.detail

    def test_the_green_line_says_the_guard_was_checked(
        self, enabled, live_socket, good_hooks
    ):
        """A check nobody can see the result of is a check nobody trusts."""
        probe = probes.herdr(
            socket_path=live_socket, list_agents=lambda b, t: AGENTS, **good_hooks
        )
        assert probe.ok
        assert "hook guard: 1 SessionStart entry" in probe.detail

    def test_the_socket_is_still_asked_first(self, enabled, tmp_path):
        """A dead server is reported as a dead server, not as a hook
        problem — the questions are ordered so the message names the
        thing to fix."""
        guard = write_guard(tmp_path)
        settings = write_settings(tmp_path, [])
        probe = probes.herdr(
            socket_path=tmp_path / "nothing.sock",
            settings_path=settings,
            guard_path=guard,
        )
        assert not probe.ok
        assert "not running" in probe.detail
