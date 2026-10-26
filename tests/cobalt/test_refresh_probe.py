"""`prefill probe X15` (card 1047 f4-probe; F4 FINAL `:221`), offline.

Every run is in process on the probe's virtual clock and mock transport:
no network, no database, no vault, no token (DECISION 1). Each test reaches
the probe through the CLI first, so on BASE each is red with argparse's
`invalid choice: 'probe'`. Constructed tickers `ZZA`-`ZZE` and the literal
token only (L32); each pin finds its lines by content (brain R1472).
"""

from __future__ import annotations

import re
import subprocess
import sys
from collections import Counter
from dataclasses import replace

import httpx
import pytest

from cobalt.prefill import cli

LINE = re.compile(r"^PROBE X15 (OK|FAIL|NOT RUN) ")
TOKEN = "probe-token-constructed"


def run(monkeypatch, capsys, argv) -> tuple[int, str, str]:
    monkeypatch.setattr(sys, "argv", ["prefill", *argv])
    try:
        cli.main()
        code = 0
    except SystemExit as e:
        code = e.code if isinstance(e.code, int) else (0 if e.code is None else 1)
    out, err = capsys.readouterr()
    return code, out, err


@pytest.fixture
def probe(monkeypatch, capsys):
    """The probe module, once `prefill probe` is mounted; every transport the
    run builds is kept in `probe.built`."""
    code, _, err = run(monkeypatch, capsys, ["probe", "--help"])
    assert code == 0, err
    from cobalt.prefill import refresh_probe

    built = []

    class Recording(refresh_probe.ProbeTransport):
        def __init__(self, *a, **kw):
            super().__init__(*a, **kw)
            built.append(self)

    monkeypatch.setattr(refresh_probe, "ProbeTransport", Recording)
    monkeypatch.setenv("COBALT_ENV", "dev")
    refresh_probe.built = built
    return refresh_probe


def small(probe):
    """A stand-in plan: 1 ARMED card, the radar at 10 rpm."""
    return replace(probe.SETUP, cards=1, radar_rpm=10.0, planned_rpm=10.0, headroom_rpm=40.0)


def x15(monkeypatch, capsys, probe, setup=None):
    if setup is not None:
        monkeypatch.setattr(probe, "SETUP", setup)
    code, out, err = run(monkeypatch, capsys, ["probe", "X15"])
    lines = out.splitlines()
    assert len(lines) == 1, out
    return code, lines[0], err


def records(probe):
    return [r for t in probe.built for r in t.records]


def per_minute(line: str) -> dict[str, int]:
    block = line.split(" · per minute ", 1)[1].split(" · ", 1)[0]
    return {k: int(v) for k, v in (cell.split("=") for cell in block.split(", "))}


# -- P1 the subcommand ----------------------------------------------------------


def test_the_probe_is_mounted_and_lists_x15(monkeypatch, capsys):
    code, out, err = run(monkeypatch, capsys, ["probe", "--help"])
    assert code == 0, err
    assert "X15" in out


# -- P2 the boundary ------------------------------------------------------------


def test_production_and_unset_env_are_refused(monkeypatch, capsys, probe):
    monkeypatch.setenv("COBALT_ENV", "production")
    code, line, _ = x15(monkeypatch, capsys, probe)
    assert (code, line) == (1, "PROBE X15 FAIL refused: COBALT_ENV=production (dev only)")

    monkeypatch.delenv("COBALT_ENV")
    code, line, _ = x15(monkeypatch, capsys, probe)
    assert code == 1
    assert line == "PROBE X15 FAIL refused: COBALT_ENV is unset — set it to one of production, dev."
    assert records(probe) == []


def test_no_write_no_db_no_token_no_launchctl(monkeypatch, capsys, probe, tmp_path):
    import importlib

    def _raise(name):
        def boom(*a, **kw):
            raise AssertionError(f"the probe reached {name}")

        return boom

    for module, names in (
        ("cobalt.vaultwrite", ("VaultWriter", "VaultWriteStore")),
        ("cobalt.vaultwrite.writer", ("VaultWriter",)),
        ("cobalt.vaultwrite.store", ("VaultWriteStore",)),
        ("cobalt.cards.store", ("CardStore",)),
        ("cobalt.archiver.store", ("BarStore",)),
        ("cobalt.taxonomy.store", ("TradeDefStore",)),
        ("cobalt.archiver.collector", ("resolve_token",)),
        ("cobalt.aset.prefill", ("resolve_token",)),
        ("cobalt.jobs.entrypoint", ("as_job",)),
        ("cobalt.prefill.cli", ("as_job",)),
        ("cobalt.notify.mattermost", ("send_dm",)),
    ):
        mod = importlib.import_module(module)
        for name in names:
            monkeypatch.setattr(mod, name, _raise(f"{module}.{name}"))
    spawned = []
    monkeypatch.setattr(subprocess, "run", lambda *a, **kw: spawned.append(a))
    monkeypatch.setattr(subprocess, "Popen", lambda *a, **kw: spawned.append(a))
    monkeypatch.chdir(tmp_path)

    code, line, err = x15(monkeypatch, capsys, probe)
    assert LINE.match(line), line
    assert "error" not in line, line
    assert code in (0, 1)
    assert spawned == []
    assert list(tmp_path.iterdir()) == []
    assert records(probe), "the run sent its requests to the mock transport"


def test_a_request_off_the_mock_transport_fails(monkeypatch, capsys, probe):
    reached = []

    async def no_network(self, request):
        reached.append(request.url.path)
        raise httpx.ConnectError("the test's own guard")

    monkeypatch.setattr(httpx.AsyncHTTPTransport, "handle_async_request", no_network)
    real = httpx.AsyncClient
    monkeypatch.setattr(probe, "_probe_client", lambda transport: real)
    code, line, _ = x15(monkeypatch, capsys, probe, small(probe))
    assert (code, line) == (1, "PROBE X15 FAIL error network")
    assert reached == [], "the probe's own guard stopped the request first"


# -- X15 the count ----------------------------------------------------------------


def test_x15_counts_every_consumer_per_minute(monkeypatch, capsys, probe):
    code, line, _ = x15(monkeypatch, capsys, probe, small(probe))
    assert code == 0 and line.startswith("PROBE X15 OK "), line
    seen = records(probe)
    assert per_minute(line) == dict(Counter(r.minute for r in seen))
    assert sum(per_minute(line).values()) == len(seen)
    assert [r.consumer for r in seen if r.minute == "08:43" and r.consumer == "refresh"] == ["refresh"] * 3
    assert {r.consumer for r in seen} == {"radar", "strike", "refresh"}
    assert "refresh gate admitted" in line


def test_x15_a_minute_above_50_fails_and_names_the_consequence(monkeypatch, capsys, probe):
    code, line, _ = x15(monkeypatch, capsys, probe, replace(probe.SETUP, radar_rpm=50.0))
    assert code == 1 and line.startswith("PROBE X15 FAIL "), line
    minute = [r for r in records(probe) if r.minute == "08:43"]
    assert len(minute) >= 51
    assert [r.status for r in minute[:50]].count(429) == 0
    assert minute[50].status == 429
    assert re.search(r"peak \d+/min at \d\d:\d\d", line)
    assert "FINAL :221" in line


def test_x15_a_redirect_is_counted(monkeypatch, capsys, probe):
    x15(monkeypatch, capsys, probe, small(probe))
    plain = len(records(probe))
    probe.built.clear()
    code, line, _ = x15(monkeypatch, capsys, probe, replace(small(probe), redirects=1))
    seen = records(probe)
    assert code == 0, line
    assert [r.status for r in seen[:2]] == [302, 200]
    assert seen[0].path == seen[1].path and seen[0].consumer == seen[1].consumer
    assert len(seen) == plain + 1
    assert sum(per_minute(line).values()) == len(seen)


def test_x15_refresh_gate_refusal_is_not_run(monkeypatch, capsys, probe):
    setup = replace(probe.SETUP, planned_rpm=49.95, headroom_rpm=0.05)
    code, line, _ = x15(monkeypatch, capsys, probe, setup)
    assert code == 3
    assert line.startswith("PROBE X15 NOT RUN — refresh refused by the gate: "), line
    assert [r for r in records(probe) if r.consumer == "refresh"] == []


def test_x15_clause_holds_no_query_or_token(monkeypatch, capsys, probe):
    code, line, err = x15(monkeypatch, capsys, probe)
    assert LINE.match(line), line
    for banned in ("?", "auth", TOKEN, "http", "/export", "finviz.com"):
        assert banned not in line, banned
        assert banned not in err, banned
    assert records(probe), "the run sent requests"


# -- C1 the control and the line ------------------------------------------------


@pytest.mark.parametrize("item", ["X7", "X99"])
def test_an_unknown_item_is_refused(monkeypatch, capsys, probe, item):
    code, out, err = run(monkeypatch, capsys, ["probe", item])
    assert code == 2
    assert f"invalid choice: '{item}'" in err
    assert out == ""
    assert probe.built == []


@pytest.mark.parametrize(
    ("verdict", "exit_code", "change"),
    [
        ("OK", 0, {}),
        ("FAIL", 1, {"cards": 5, "radar_rpm": 50.0, "planned_rpm": 40.0, "headroom_rpm": 10.0}),
        ("NOT RUN", 3, {"planned_rpm": 49.95, "headroom_rpm": 0.05}),
    ],
)
def test_x15_prints_one_line_and_exits_by_verdict(monkeypatch, capsys, probe, verdict, exit_code, change):
    code, line, _ = x15(monkeypatch, capsys, probe, replace(small(probe), **change))
    assert LINE.match(line).group(1) == verdict, line
    assert code == exit_code
