"""https-only row D (L80, R718) — the probes read the https URL.

The heartbeat's two web probes, the S2 smoke's K4 checks and the deploy
smoke's curl shape read aset the way his devices do: through `tailscale
serve` on https, so a down `serve` is red there. Each is pinned to the one
config home of the address, `configs/cobalt/voice.yaml` `https_url` (row A).
Offline: config loads and text reads only.
"""

from __future__ import annotations

import inspect
import re
from pathlib import Path

from cobalt.heartbeat import probes
from cobalt.smoke.config import SUITES_DIR, load_suite
from cobalt.voice import config as vc

REPO = Path(__file__).resolve().parents[2]
DEPLOY_SMOKE = REPO / "ops" / "desk" / "deploy-smoke.sh"
PLAIN = "http://127.0.0.1:5010/"


def _probe_default(fn) -> str:
    return inspect.signature(fn).parameters["url"].default


def _curl_pattern() -> str:
    """The first `case "$url" in` arm of the curl shape: the URLs it admits."""
    text = DEPLOY_SMOKE.read_text()
    m = re.search(r'case "\$url" in\n\s+(\S+)\) ;;', text)
    assert m, "deploy-smoke.sh: no curl case arm"
    return m.group(1)


def test_every_probe_reads_the_configured_https_url(monkeypatch):
    monkeypatch.delenv(vc.SCRATCH_ENV, raising=False)
    monkeypatch.delenv(vc.MODEL_ENV, raising=False)
    k4 = {c.id: c.url for c in load_suite(SUITES_DIR / "s2.yaml").checks if c.id.startswith("K4.")}
    assert sorted(k4) == ["K4.1", "K4.2", "K4.3", "K4.4"], sorted(k4)
    urls = {
        "sheet_http": _probe_default(probes.sheet_http),
        "sheet_daymode": _probe_default(probes.sheet_daymode),
        **k4,
        "deploy-smoke.sh curl case": _curl_pattern(),
    }
    plain = {k: u for k, u in urls.items() if u.startswith(PLAIN)}
    assert not plain, plain
    https = vc.load_voice_config().https_url
    off = {k: u for k, u in urls.items() if not u.startswith(https)}
    assert not off, (https, off)
    assert urls["sheet_http"] == https
    assert urls["sheet_daymode"] == https + "api/health"
    assert urls["deploy-smoke.sh curl case"] == https + "*"
    assert k4 == {
        "K4.1": https + "api/health",
        "K4.2": https,
        "K4.3": https + "radar",
        "K4.4": https + "api/radar/pool?since={cutoff}",
    }


def test_the_curl_refusal_names_the_https_url(monkeypatch):
    monkeypatch.delenv(vc.SCRATCH_ENV, raising=False)
    monkeypatch.delenv(vc.MODEL_ENV, raising=False)
    assert PLAIN not in DEPLOY_SMOKE.read_text()
    https = vc.load_voice_config().https_url
    assert f'why="curl reads {https} only"' in DEPLOY_SMOKE.read_text()
