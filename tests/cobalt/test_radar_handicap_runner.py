"""Float handicap H1 — the resident's two seams with the shadow step
(STEP-4; ESCALATED as edits outside `runner.py`'s metrics hunk): the cycle
hands `decide()` the header config, and the pool row carries the
`Decision`'s reason for a `handicap` degradation instead of the fixed
"source failure" (X6's consequence).
"""

from __future__ import annotations

import asyncio
import time
from datetime import datetime, timezone

from test_radar_runner import _active_runner

from cobalt.radar import runner as runner_module
from cobalt.radar.pool import Decision, decide
from cobalt.session.models import Session

INSTANT = datetime(2026, 9, 3, 14, 30, tzinfo=timezone.utc)


def test_the_cycle_hands_decide_the_configured_handicap_headers(monkeypatch):
    seen = {}

    def spy(*args, **kwargs):
        seen.update(kwargs)
        return decide(*args, **kwargs)

    monkeypatch.setattr(runner_module, "decide", spy)
    events: list[str] = []
    runner = _active_runner(events)
    asyncio.run(runner.cycle())
    assert seen["handicap_headers"] == runner.config.export.handicap_headers


def test_the_pool_row_writes_the_decisions_reason_and_keeps_source_failure_otherwise():
    runner = _active_runner([])
    decision = Decision(
        transitions=[], degraded=True, degraded_sources=["screen:x@000000000000", "handicap"],
        reasons={"handicap": "mode live needs H2 — ranking raw"},
    )
    row = runner._pool_row(runner.sources_loader(), decision, 1, INSTANT, Session.RTH, time.monotonic(), [], None)
    assert [(item["source"], item["reason"]) for item in row["degraded_sources"]] == [
        ("screen:x@000000000000", "source failure"),
        ("handicap", "mode live needs H2 — ranking raw"),
    ]
