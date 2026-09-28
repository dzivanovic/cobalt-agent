"""X6 (v2 §7, before S1; W4): with intraday-stale bars, a non-None
`last_price` and a fresh daily series, is the `htf_level_proximity`
observation marked stale, or graded from the stale price? v2 W4 (PROVEN
from reads) says graded, with no stale flag — this records it by running
the engine. STEP-2 test (v) turns it: stale → `input_stale`, no grade."""

from __future__ import annotations

import radar_p2_support as sup
from cobalt.radar.evaluate import card_dots

from stale_support import FIXED, SCAN0, bars_before, evaluate, member, settings, stale_as_of


def test_x6_htf_level_proximity_on_stale_bars():
    kept = bars_before(SCAN0)
    at = stale_as_of(kept)
    ev = evaluate(member(at, kept))
    obs = ev.observations["htf_level_proximity"]
    dot = {d.factor: d for d in card_dots(sup.loaded(), ev, settings(), at, ())}["htf_level_proximity"]
    print(f"X6: fixed={FIXED} evaluation={ev.evaluation} last_price_present={ev.last_price is not None} "
          f"daily_present={ev.observations['htf_level_proximity'].inputs.get('prior_session') is not None} "
          f"obs_stale={obs.stale} obs_value_present={obs.value is not None} "
          f"dot_na_reason={dot.na_reason} dot_engine_grade_present={dot.engine_grade is not None} "
          f"atrs_from_open_stale={ev.observations['atrs_from_open'].stale}")
    assert ev.evaluation == "input_stale" and ev.last_price is not None
    assert ev.observations["atrs_from_open"].stale is True
    if FIXED:  # v2 §2 C step 5: stale=intraday_stale → input_stale, no engine grade
        assert obs.stale is True and dot.na_reason == "input_stale" and dot.engine_grade is None
    else:  # W4 as v2 states it: graded from the stale price, no stale flag
        assert obs.stale is False and obs.value is not None and dot.engine_grade is not None
