"""X26 (v2 §7, before S1; Fable X13): an open card refreshed through the
slug-match path (the note edited since formation) with a `not_evaluable`
evaluation — can `evaluability` differ while `formation_changes` is empty?
Either answer leaves [F-10]'s wording (the flag is on every return path);
"yes" would make it load-bearing."""

from __future__ import annotations

import radar_p2_support as sup
from cobalt.radar.anatomy.registry import evaluability
from cobalt.radar.evaluate import formation_changes
from cobalt.taxonomy.tunables import TunableRow

from stale_support import FIXED, SCAN, SCAN0, bars_before, member


def test_x26_catalyst_edit_cannot_change_evaluability_but_a_convention_row_can_refuse():
    original = sup.anatomy_def()
    edited = sup.anatomy_def(quality_factors=[*sup.ANATOMY_FACTORS, "catalyst"])
    changes = formation_changes(original, edited)
    same = evaluability(original) == evaluability(edited)
    # A not_evaluable outcome with an EMPTY formation diff: a convention row
    # naming a rule the code does not implement (a tunables change, not a def edit).
    rows = dict(sup.engine_tunables())
    key = "anatomy.orientation.extension"
    rows[key] = TunableRow.model_validate({**rows[key].model_dump(mode="json"), "value": "a_label_no_code_implements"})
    from cobalt.radar.evaluate import evaluate_member
    from cobalt.session import session_clock

    kept = bars_before(SCAN0)
    ev = evaluate_member(sup.loaded(edited), member(SCAN0, kept), tunables=rows, defaults=sup.defaults(),
                         scan_interval=SCAN, clock=session_clock())
    flag = getattr(ev, "intraday_stale", "absent")
    print(f"X26: fixed={FIXED} formation_changes={changes} evaluability_equal={same} "
          f"refused_evaluation={ev.evaluation} last_price_present={ev.last_price is not None} "
          f"intraday_stale_on_not_evaluable={flag}")
    assert changes == [] and same
    assert ev.evaluation == "not_evaluable" and ev.last_price is not None
    if FIXED:
        assert flag is False
