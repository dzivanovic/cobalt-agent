"""X14 (v2 §7, before S1; Q10): `evaluation == "input_stale"` from MISSING
DAILY bars (W3's second meaning) with a close younger than the ttl leaves
proximity computed — the guard is `intraday_stale`, never the label."""

from __future__ import annotations

import radar_p2_support as sup
from cobalt.radar.evaluate import refresh_card

from stale_support import ENABLED, FIXED, SCAN0, bars_before, evaluate, member, settings, tapped_pre_c1_card

#: An avoid on the higher-timeframe range break: unknown without daily bars
#: (`no_daily_bars`) — the shape `tests/cobalt/setups_shapes.HTF_AVOID` uses.
HTF_AVOID = {"expr": "RangeBreak(HTF).day_count == 1"}


def test_x14_daily_missing_input_stale_with_a_fresh_close_keeps_proximity():
    td = sup.anatomy_def(avoid=[{"expr": "NOT Extension.instantiated"}, HTF_AVOID])
    ld = sup.loaded(td)
    kept = bars_before(SCAN0)
    ev = evaluate(member(SCAN0, kept, daily=False), ld)
    card = tapped_pre_c1_card()
    update = refresh_card(card, ev, ld, settings(), ENABLED, at=SCAN0, thresholds=None)
    close_age = (SCAN0 - kept[-1].ts).total_seconds() - 60
    flag = getattr(ev, "intraday_stale", None)
    print(f"X14: fixed={FIXED} evaluation={ev.evaluation} note={ev.note!r} close_age_s={close_age} "
          f"intraday_stale_field={flag} proximity={update.proximity} card_score={update.card_score}")
    assert ev.evaluation == "input_stale" and "avoid unknown" in (ev.note or "")
    assert update.proximity is not None and update.card_score is not None
    if FIXED:
        assert flag is False
