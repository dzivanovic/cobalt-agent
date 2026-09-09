"""F18's `sheet_daymode` probe — the sheet is WORKING, not just serving.

THE THIRTEEN-HOUR GREEN (2026-09-09). The ASET sheet answered HTTP 200
from roughly 19:00 the previous evening to 07:06 while the page carried
"⚠ DAY MODE UNRESOLVED — cards are refused until this is fixed". Every
card write was refused; `sheet_http` was green throughout, and it was
telling the truth — the server was up. It was answering a different
question from the one that mattered.

Cause, and it is the shape this probe watches for: the 09-08 seat-usage
deploy added a `TunableUnit.WINDOW` row to `tunables.yaml`; the sheet
process re-reads that file per request through code that predated the
enum value, so every render raised `TaxonomyConfigError`. And
`_daymode_state()` catches everything and renders a banner — deliberately,
because a sheet that will not paint is a sheet he cannot trade beside. A
page that refuses cards politely is externally indistinguishable from one
that is working.

Every test here drives a REAL HTTP server on a real socket, for the same
reason `test_herdr_probe.py` drives a real AF_UNIX socket: a mocked
`urlopen` proves the code calls a function, while a real server proves
the probe can tell "answering" from "answering a refusal" — which is the
distinction it exists to make.
"""

from __future__ import annotations

import json
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

import pytest

from cobalt.heartbeat import probes


def serve(payload, status: int = 200, *, raw: bytes | None = None):
    """A one-endpoint HTTP server on a free port. Returns its URL."""

    body = raw if raw is not None else json.dumps(payload).encode()

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a):
            pass

    server = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return server, f"http://127.0.0.1:{server.server_port}/api/health"


@pytest.fixture
def sheet():
    """`sheet(payload)` -> url, torn down after the test."""
    servers = []

    def _start(payload=None, status: int = 200, raw: bytes | None = None):
        server, url = serve(payload, status, raw=raw)
        servers.append(server)
        return url

    yield _start
    for s in servers:
        s.shutdown()
        s.server_close()


GREEN = {
    "ok": True,
    "day": "2026-09-09",
    "mode": "reduced",
    "stage": "stage 1",
    "sheet_mode": "half",
    "error": None,
}

# The payload the live sheet would have served all night on 09-09.
THE_0909_FAILURE = {
    "ok": False,
    "day": None,
    "mode": None,
    "stage": "UNRESOLVED",
    "sheet_mode": None,
    "error": (
        "TaxonomyConfigError: tunables.yaml row 'seat_usage.window' has unit "
        "'window', which is not a TunableUnit — the loader has no built-in "
        "defaults and refuses a row it cannot type (F16)."
    ),
}


class TestTheGreenCase:
    def test_a_resolved_day_mode_is_green_and_says_which(self, sheet):
        probe = probes.sheet_daymode(sheet(GREEN))
        assert probe.ok and not probe.unknown
        assert "reduced" in probe.detail
        assert "half" in probe.detail
        assert "stage 1" in probe.detail


class TestTheRefusalCase:
    def test_the_0909_banner_is_RED(self, sheet):
        """The whole point: 200, valid JSON, and red."""
        probe = probes.sheet_daymode(sheet(THE_0909_FAILURE))
        assert not probe.ok
        assert not probe.unknown, (
            "this is a DIAGNOSIS, not ignorance — the sheet told us exactly what "
            "is wrong and the probe read it"
        )
        assert "SERVING BUT REFUSING CARDS" in probe.detail
        assert "seat_usage.window" in probe.detail, "the sheet's own words"

    def test_the_error_is_truncated_to_160_chars(self, sheet):
        long = {**THE_0909_FAILURE, "error": "X" * 900}
        probe = probes.sheet_daymode(sheet(long))
        assert not probe.ok
        assert "X" * probes.DAYMODE_ERROR_CHARS in probe.detail
        assert "X" * (probes.DAYMODE_ERROR_CHARS + 1) not in probe.detail

    def test_a_null_mode_with_no_error_is_still_red(self, sheet):
        """`ok` is false iff error is set OR mode is null — to a trader
        those are the same thing, because `assert_sheet_matches` refuses
        every card either way."""
        probe = probes.sheet_daymode(
            sheet({**GREEN, "ok": False, "mode": None, "error": None})
        )
        assert not probe.ok
        assert "no day mode resolved" in probe.detail


class TestTheProbeCannotRun:
    def test_unreachable_is_red_AND_unknown(self, sheet):
        """"The probe broke" and "the thing is down" are different facts.
        A closed port means we did not look, and UNKNOWN is red."""
        url = sheet(GREEN)
        probe_url = url.replace(url.split(":")[2].split("/")[0], "1")  # port 1
        probe = probes.sheet_daymode(probe_url)
        assert not probe.ok and probe.unknown
        assert "unreachable" in probe.detail

    def test_a_non_200_is_unknown(self, sheet):
        probe = probes.sheet_daymode(sheet(GREEN, status=503))
        assert not probe.ok and probe.unknown

    def test_a_payload_without_ok_is_unknown_not_green(self, sheet):
        """A shape this probe does not recognise is ignorance, and
        ignorance is never green."""
        probe = probes.sheet_daymode(sheet({"status": "fine"}))
        assert not probe.ok and probe.unknown
        assert "not answering the shape" in probe.detail

    def test_html_instead_of_json_is_unknown(self, sheet):
        probe = probes.sheet_daymode(sheet(None, raw=b"<html>404</html>"))
        assert not probe.ok and probe.unknown


class TestItIsWiredIntoTheBeat:
    def test_the_runner_asks_it_right_after_sheet_http(self, monkeypatch):
        from cobalt.heartbeat import runner

        asked: list[str] = []

        def record(name, ok=True):
            def _probe(*a, **k):
                asked.append(name)
                return probes.Probe(name, ok, "stub")

            return _probe

        for name in (
            "database", "sheet_http", "sheet_daymode", "obsidian", "mainframe",
            "herdr", "archiver_freshness", "seat_usage", "backup_freshness",
            "vaultwrite_blocks", "redactions", "email",
        ):
            monkeypatch.setattr(probes, name, record(name))
        monkeypatch.setattr(runner, "sweep", lambda **k: [])

        runner.take_beat()

        assert "sheet_daymode" in asked
        assert asked.index("sheet_daymode") == asked.index("sheet_http") + 1

    def test_sheet_http_is_unchanged(self, sheet):
        """Two questions, both kept. A dead server fails both, and
        `sheet_http`'s message is the one that says what to restart."""
        url = sheet(GREEN).replace("/api/health", "/")
        probe = probes.sheet_http(url)
        assert probe.ok and probe.name == "sheet HTTP"
        assert "-> 200" in probe.detail
