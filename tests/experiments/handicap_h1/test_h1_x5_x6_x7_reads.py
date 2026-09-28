"""Three offline reads (v3 first-gate experiments), plus X5's stored half:

X5 (grok X6): the S5 receipt's `pool_unit`, built exactly as
    `runner.py:319-323` builds it, from a constructed `SourceSet` whose
    `metrics` carry two extra keys — does the dump carry them? STOPS the
    build when `metrics` is absent. The stored half counts `cobalt_dev`'s
    receipts (inside the suite's rollback transaction; counts only).
X6 (grok X7): a `handicap` entry in `degraded_sources`, through the
    panel's degraded joiner (`radar_panel.py:586-590`) — does the rendered
    banner carry its REASON, or only the name?
X7 (grok X8): the poller's sort line and the runner's poll hand-off, quoted.
"""

from __future__ import annotations

import os
import re
from pathlib import Path

import pytest

from cobalt.radar.models import SourceSet

SRC = Path(__file__).resolve().parents[3] / "src" / "cobalt"


def test_x5_pool_unit_dump_carries_extra_metric_keys():
    source_sets = [SourceSet(
        source="screen:constructed@000000000000", kind="screen", tickers=["AAA"],
        metrics={"AAA": {"volume": 1.0, "rvol": 2.0, "float_m": 3.0, "market_cap_m": 4.0}},
    )]
    # runner.py:319-323, the expression as written there:
    pool_unit = {
        "pool_block": None,
        "frozen": False,
        "source_sets": [item.model_dump(mode="json") for item in source_sets],
    }
    carried = pool_unit["source_sets"][0]["metrics"]["AAA"]
    print(f"X5: pool_unit source_sets[0].metrics keys {sorted(carried)}")
    runner_src = (SRC / "radar" / "runner.py").read_text().splitlines()
    print("X5: runner.py:322 reads: " + runner_src[321].strip())
    assert {"float_m", "market_cap_m"} <= set(carried)


@pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="X5 stored half: needs cobalt_dev (run inside THE LOCK)",
)
def test_x5_stored_receipts_on_cobalt_dev_counts_only():
    from cobalt import db, env
    from cobalt.db import Side

    with db.connect(env.DEV_DB_NAME, side=Side.USER) as conn:
        total, with_value, with_metrics = conn.execute(
            "SELECT count(*), count(*) FILTER (WHERE pool_unit ? 'value'), "
            "count(*) FILTER (WHERE jsonb_path_exists(pool_unit, '$.value.source_sets[*].metrics')) "
            "FROM radar_score_receipt"
        ).fetchone()
    print(f"X5 stored: receipts {total} · carrying a pool_unit value {with_value} · "
          f"whose source_sets carry metrics {with_metrics}")


def test_x6_a_handicap_degradation_through_the_panel_joiner():
    from test_radar_panel import (  # tests/cobalt, on sys.path via this folder's conftest
        FakeClock, FakeRadarStore, FakeSettingsStore, NOW, _small_snapshot, _tunables,
    )

    from cobalt.aset import radar_panel as panel

    pool_row, members = _small_snapshot()
    pool_row.update(degraded=True, degraded_sources=[
        {"source": "handicap", "reason": "column missing: Shares Float", "since": "2026-01-05T16:00:00+00:00"},
    ])
    view = panel.build_pool_view(
        since=None, snapshot=True, radar_store=FakeRadarStore(pool_row, members),
        settings_store=FakeSettingsStore(), clock=FakeClock(), now=NOW, tunables_loader=_tunables(),
    )
    html = panel.render_pool(view)
    banner = re.search(r'<div class="panel-banner degraded">.*?</div>', html).group(0)
    print(f"X6: rendered banner: {banner}")
    print(f"X6: reason rendered: {'column missing' in banner}")


def test_x7_the_poller_sort_and_the_poll_hand_off_quoted():
    poller = (SRC / "radar" / "poller.py").read_text().splitlines()
    runner = (SRC / "radar" / "runner.py").read_text().splitlines()
    sort_line = next(i for i, line in enumerate(poller) if "sorted(members" in line)
    print(f"X7: poller.py:{sort_line + 1}: {poller[sort_line].strip()}")
    for number in (240, 245):
        print(f"X7: runner.py:{number}: {runner[number - 1].strip()}")
    assert "(item.rank, item.ticker)" in poller[sort_line]
