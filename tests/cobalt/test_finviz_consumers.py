"""L53 total demand: every module that sends a Finviz request, pinned.

ops-2026-09-17 item 5b (P2 build ESCALATE 1). A new Finviz consumer must
fail this test, so the total-demand plan grows with it instead of by
surprise. The strict xfail records the owed fix: one shared cross-process
gate called before every request (P4 STEP-6 shape).
"""

import re
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parents[2] / "src" / "cobalt"
_REQUEST = re.compile(r"elite\.finviz\.com|\bfinviz_get\(|\bfetch_bars\(")

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
