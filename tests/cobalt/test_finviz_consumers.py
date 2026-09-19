"""L53 total demand: every module that sends a Finviz request, pinned.

ops-2026-09-17 item 5b (P2 build ESCALATE 1). A new Finviz consumer must
fail this test, so the total-demand plan grows with it instead of by
surprise. The strict xfail records the owed fix: one shared cross-process
gate called before every request (P4 STEP-6 shape).

Second subject (AT-1 2.3): every one of those consumers asks for the SAME
column set. The index list was written out four times in `src/cobalt`;
`cobalt.radar.config.screener_columns()` is now its one source (L3), and
the scan at the bottom of this module is the `grep` that keeps it one.
"""

import re
from pathlib import Path
from types import SimpleNamespace

import pytest

from cobalt.archiver.collector import FetchMetrics
from cobalt.radar import throttle
from cobalt.radar.collector import FinvizScreenerCollector
from cobalt.radar.config import load_config
from cobalt.replay.movers import MoversCollector

SRC = Path(__file__).resolve().parents[2] / "src" / "cobalt"
_REQUEST = re.compile(r"elite\.finviz\.com|\bfinviz_get\(|\bfetch_bars\(")

#: What every consumer must send as `c=`, spelled out here rather than
#: imported, so a change to the one source fails this test loudly.
COLUMN_PARAM = ",".join(map(str, range(151)))

#: module -> who runs it and when (ET). The radar-bucket ones share
#: `radar.finviz_max_rpm` inside the radar process; the rest do not.
CONSUMERS = {
    "archiver/collector.py": "transport (finviz_get / fetch_bars)",
    "archiver/runner.py": "com.cobalt.archiver one-shot, 20:30, own 1.2 s pacing",
    "radar/collector.py": "com.cobalt.radar resident, radar TokenBucket",
    "radar/propose.py": "cobalt radar screens propose (CLI, by hand), no bucket",
    "radar/throttle.py": "throttle probe (CLI, by hand), no bucket",
    "prefill/market.py": "com.cobalt.prefill-daily 05:15, 1 screener request, no bucket",
    "prefill/calendar.py": "com.cobalt.prefill-daily 05:15, 2 calendar requests, no bucket",
    "aset/prefill.py": "com.cobalt.aset resident, /export/stock p=d on demand (RTH), no bucket",
}
BUCKETED = {"archiver/collector.py", "radar/collector.py"}


def _request_modules() -> set[str]:
    found = set()
    for path in SRC.rglob("*.py"):
        for line in path.read_text().splitlines():
            code = line.split("#", 1)[0]
            if _REQUEST.search(code) and "def finviz_get(" not in code and "def fetch_bars(" not in code:
                found.add(path.relative_to(SRC).as_posix())
                break
    return found


def test_every_finviz_consumer_is_in_the_total_demand_inventory():
    assert _request_modules() == set(CONSUMERS)


@pytest.mark.xfail(
    strict=True,
    reason="ops-2026-09-17 5b: no shared cross-process Finviz gate yet; aset, prefill-daily "
    "and the two CLIs request outside radar.finviz_max_rpm (P4 STEP-6 acceptance)",
)
def test_no_finviz_request_bypasses_the_shared_gate():
    assert _request_modules() - BUCKETED - {"archiver/runner.py"} == set()


# ---------------------------------------------------------------------
# AT-1 2.3 — one column set, one source
# ---------------------------------------------------------------------


class _NoWait:
    async def acquire(self):
        return None


def _probe_screen_params(monkeypatch) -> dict:
    """The throttle probe's own screener request, captured from a CLI run
    (`cobalt radar throttle-probe`) rather than from `run_probe`'s
    signature: the probe holds no config of its own, so the wiring under
    test is `command()` reading `load_config()` and handing the
    declaration down. Transport, credential, refusal clock and result
    file are all faked — no network, no vault, nothing written."""
    seen: dict[str, object] = {}

    async def bars(_ticker, _interval, _token, *, on_metrics):
        on_metrics(FetchMetrics(status=200, elapsed_ms=1, bytes=1, content_type="text/csv"))
        return []

    async def screen(_path, params, _token, *, on_metrics):
        seen.update(params)
        body = "Ticker,Volume\nAAA,1\n"
        on_metrics(FetchMetrics(status=200, elapsed_ms=1, bytes=len(body), content_type="text/csv"))
        return SimpleNamespace(text=body)

    async def token():
        return "synthetic-token"

    monkeypatch.setattr(throttle, "fetch_bars", bars)
    monkeypatch.setattr(throttle, "finviz_get", screen)
    monkeypatch.setattr(throttle, "resolve_token", token)
    monkeypatch.setattr(throttle, "refusal_reason", lambda _now: None)
    monkeypatch.setattr(throttle, "write_result", lambda stages, limit: throttle.REPO_ROOT / "data/none.json")
    throttle.command(SimpleNamespace(names=1, grids="600", cycles=1))
    assert seen, "the probe sent no screener request"
    return seen


def test_every_finviz_consumer_asks_for_the_same_column_set(monkeypatch, tmp_path):
    """The radar screen, both movers exports and the throttle probe all
    send the shipped config's `export.columns`. One shape reaches every
    parser, so one committed real-shape fixture can stand for all of
    them (L45)."""
    config = load_config()
    screener = FinvizScreenerCollector("synthetic-token", config=config, bucket=_NoWait(), cache_root=tmp_path)
    movers = MoversCollector("synthetic-token", config=config, bucket=_NoWait(), cache_root=tmp_path)

    assert screener._params()["c"] == COLUMN_PARAM
    assert movers._params("gainers")["c"] == COLUMN_PARAM
    assert movers._params("losers")["c"] == COLUMN_PARAM
    assert _probe_screen_params(monkeypatch)["c"] == COLUMN_PARAM


_RANGE_151 = re.compile(r"range\(\s*151\s*\)")
#: A `c=` request parameter assignment. A literal value is allowed
#: (`radar/propose.py`'s `ft` comparison probe deliberately asks for the
#: single column `"0"`); anything else must have come from the one
#: function, and may never be assembled on the spot.
_COLUMN_PARAM_ASSIGNMENT = re.compile(r'"c"\s*:\s*[^"\s]')
_ASSEMBLED = re.compile(r"\.join\(|range\(")


def test_only_one_function_in_the_new_core_builds_the_column_set():
    """`grep -rn "range(151)" src/cobalt` prints nothing: the index list
    is produced by `cobalt.radar.config.screener_columns()` alone, which
    derives it from the declaration and never spells the literal (L3).

    Then the shape of every `c=` assignment: never assembled inline, and
    any module that sends a computed one imports the one function. A
    fifth consumer that rolls its own fails here, the way a fifth Finviz
    caller fails the inventory test above.
    """
    literals = sorted(
        path.relative_to(SRC).as_posix() for path in SRC.rglob("*.py") if _RANGE_151.search(path.read_text())
    )
    assert literals == []

    assembled = []
    without_the_one_source = []
    for path in sorted(SRC.rglob("*.py")):
        text = path.read_text()
        computed = False
        for number, line in enumerate(text.splitlines(), start=1):
            code = line.split("#", 1)[0]
            if not _COLUMN_PARAM_ASSIGNMENT.search(code):
                continue
            computed = True
            if _ASSEMBLED.search(code):
                assembled.append(f"{path.relative_to(SRC).as_posix()}:{number}")
        if computed and "screener_columns_param" not in text:
            without_the_one_source.append(path.relative_to(SRC).as_posix())
    assert assembled == []
    assert without_the_one_source == []
