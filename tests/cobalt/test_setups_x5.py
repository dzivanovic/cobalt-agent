"""X5, offline (FINAL: "time 7 defs × 2 frames × 50 members … against a 100 s
budget" / "wall-clock of `EvaluateStage.run`, 50-member pool, last RTH scan
of a stored day"). Built as the build's offline timing test: a 50-member
pool made by repeating the committed FTFT / BGFI series under distinct
membership ids and tickers, every def of the corpus plus the shipped
example, both frames, `EvaluateStage.run` over the in-memory fakes, three
runs, the max quoted as p95. The stored-day run on `cobalt_dev` is at the
deploy. Over budget → `X5: FAIL`; the FINAL's two remedies are the desk's
to choose, not this test's.
"""

from __future__ import annotations

import asyncio
import time
from datetime import datetime, timezone

import radar_p2_support as sup
import setups_shapes as shapes
from cobalt.radar.anatomy.freshness import RvolObservation
from cobalt.radar.evaluate import EvaluateStage
from cobalt.session import session_clock
from cobalt.taxonomy.trade_def import TradeDef

BUDGET_S = 100.0
LAST_RTH_SCAN = datetime(2026, 1, 6, 20, 58, tzinfo=timezone.utc)
POOL = 50


def _stage(defs):
    tickers = [f"ZZ{i:02d}" for i in range(POOL)]
    bars = {t: [b.model_copy(update={"ticker": t}) for b in shapes.bars("FTFT" if i % 2 == 0 else "BGFI")]
            for i, t in enumerate(tickers)}
    radar = sup.FakeRadarStore(sup.members(*tickers), bars)

    async def daily(ticker, now):
        series = sup.fixture_daily("FTFT" if int(ticker[2:]) % 2 == 0 else "BGFI", now)
        return series.model_copy(update={"ticker": ticker})

    stage = EvaluateStage(
        radar_store=radar, card_store=sup.FakeCardStore(), defs_source=lambda: (defs, {}),
        settings_values=lambda: sup.fixture_settings_rows(**{"radar.cards_enabled": False}),
        daily_source=daily, tunables_loader=sup.engine_tunables, defaults_loader=sup.defaults,
        clock=session_clock(), now=lambda: LAST_RTH_SCAN,
    )
    rvol = {t: RvolObservation(ticker=t, value=2.0, observed_at=LAST_RTH_SCAN, source="screen:s",
                               candidates=("screen:s",)) for t in tickers}
    return stage, rvol


def test_x5_offline_wall_clock_of_the_stage_is_inside_the_budget(tmp_path):
    defs = [shapes.load_shape(tmp_path / key, shape) for key, shape in {**shapes.SHAPES, **shapes.VARIANTS}.items()]
    defs.append(sup.loaded(TradeDef.from_unit(shapes.example_mapping(), slug="example-range-break",
                                              name="Example Range Break"), md5="fedcba9876543210fedcba9876543210"))
    stage, rvol = _stage(defs)
    runs = []
    for _ in range(3):
        start = time.perf_counter()
        outcome = asyncio.run(stage.run(pool_key="pool", scan_id=1, session="RTH", instant=LAST_RTH_SCAN, rvol=rvol,
                                        pool_unit={"pool_block": {"cap": POOL}}, gate=lambda _l: (lambda: None)))
        runs.append(time.perf_counter() - start)
        assert len(outcome.evaluations) == POOL * len(defs)
    print(f"X5 offline: defs={len(defs)} frames=2 members={POOL} runs_s={[round(r, 2) for r in runs]} "
          f"p95~max={max(runs):.2f}s budget={BUDGET_S}s")
    assert max(runs) < BUDGET_S
