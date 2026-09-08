"""F18's `herdr` probe — the terminal workspace every agent seat lives in.

TWO QUESTIONS, BOTH ASKED, and that is the whole design. A socket file
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
"""

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


@pytest.fixture
def enabled(monkeypatch):
    """Pretend the handover has happened. Shipped state is
    `enabled: false`, which is asserted separately below."""
    monkeypatch.setattr(probes, "_herdr_enabled", lambda: (True, ""))


# =====================================================================
# the shipped state: built, registered, deliberately not loaded
# =====================================================================


class TestBeforeTheHandover:
    def test_the_registry_ships_it_disabled(self):
        spec = load_job_registry().spec(LABEL)
        assert spec.enabled is False, (
            "the plist must not be loaded until the keyboard handover — a session "
            "that bootstraps it takes down the server hosting itself"
        )

    def test_the_probe_is_green_and_says_why(self):
        probe = probes.herdr()
        assert probe.ok
        assert "enabled: false" in probe.detail
        assert "handover" in probe.detail
        assert not probe.unknown

    def test_it_does_not_touch_the_socket_while_disabled(self, monkeypatch):
        def explode(*a, **k):
            raise AssertionError("a disabled job must not be probed")

        monkeypatch.setattr(probes.socket, "socket", explode)
        assert probes.herdr().ok

    def test_the_sweep_reports_it_without_probing_launchd(self, monkeypatch):
        """The watchdog asks `launchctl` about every job FIRST. A row that
        is deliberately not loaded would answer 'NOT LOADED' forever, and
        a standing red is how a heartbeat stops being read."""
        from cobalt.jobs import watchdog

        def explode(label, **k):
            raise AssertionError(f"launchctl must not be asked about {label}")

        monkeypatch.setattr(watchdog, "launchctl_status", explode)

        class OnlyHerdr:
            jobs = [load_job_registry().spec(LABEL)]

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
# after the handover: the two questions
# =====================================================================


class TestTheTwoQuestions:
    def test_a_live_socket_and_a_real_agent_list_is_green(self, enabled, live_socket):
        probe = probes.herdr(
            socket_path=live_socket, list_agents=lambda binary, timeout: AGENTS
        )
        assert probe.ok
        assert "2 pane(s)" in probe.detail
        assert "claude, codex" in probe.detail

    def test_a_missing_socket_is_red_and_names_the_label(self, enabled, tmp_path):
        probe = probes.herdr(socket_path=tmp_path / "nothing.sock")
        assert not probe.ok
        assert LABEL in probe.detail
        assert "not running" in probe.detail

    def test_a_stale_socket_file_is_red_not_green(self, enabled, stale_socket):
        """The case a `path.exists()` check gets wrong: the file is there
        and the server is gone."""
        probe = probes.herdr(
            socket_path=stale_socket, list_agents=lambda binary, timeout: AGENTS
        )
        assert not probe.ok
        assert "REFUSED a connection" in probe.detail
        assert LABEL in probe.detail

    def test_a_socket_that_accepts_but_will_not_answer_is_red(self, enabled, live_socket):
        """Up and not serving. Accepting a connection is not answering a
        question, and only the second one means the seats work."""

        def broken(binary, timeout):
            raise RuntimeError("`herdr agent list` exited 1: protocol mismatch")

        probe = probes.herdr(socket_path=live_socket, list_agents=broken)
        assert not probe.ok
        assert "did not answer `agent list`" in probe.detail
        assert LABEL in probe.detail

    def test_an_empty_pane_list_is_still_green(self, enabled, live_socket):
        """A server with no seats attached is idle, not broken — the
        probe watches the SERVER, and 'nobody is working right now' is
        not a fault."""
        probe = probes.herdr(socket_path=live_socket, list_agents=lambda b, t: [])
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
