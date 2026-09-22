"""The setups one build — the corpus gates and (from STEP-9) the LEGO TEST.

FINAL §9 gate 2 ("registry evaluable ⇒ forms", a property test) and gate 4
point (4) (the corpus shape of every unlocked setup is `evaluable`), over the
neutral shape notes of `setups_shapes.py`.

NAMED DEVIATION FROM GATE 2's TEXT (carried under the report's ESCALATE):
the committed real-shape days are ONE trade date, two tickers
(`tests/fixtures/radar/_cut_p2_fixtures.py`). An evaluable shape that forms
on no scan of any committed day is PINNED in `AWAITING_A_DAY` — with its
path proven on definition-written constructed series in its own
`test_<slug>_path_*` tests — never given an invented or re-dated day. The
property fails when an evaluable shape with no day is not pinned, and when
the pinned set grows or shrinks unannounced.
"""

from __future__ import annotations

import pytest

import setups_shapes as shapes
from cobalt.radar.anatomy.registry import evaluability

#: Evaluable setup shapes that form on NO scan of the committed real-shape
#: day, by setup slug. Closed only by a DB-backed fixture-cut job + a blind
#: expected-values seat (FINAL [F-16] (1), [F-21]).
#: - rubberband: its full shape carries the day-1 HTF avoid, which is True on
#:   the committed day (proof ESCALATE 2) — `avoided` on every scan the
#:   relation path forms on.
#: - hitchhiker (STEP-4): evaluable; on FTFT its opening drive reads
#:   `consolidation` on 22 scans and a micro-Range instantiates on 68, but on
#:   no scan do the band and the upper-third preconditions hold with them (a
#:   False precondition, never an unknown); BGFI is stale by design. Its path
#:   forms on the definition-written day and its mirror
#:   (`test_setups_hitchhiker.py::test_hitchhiker_path_*`).
AWAITING_A_DAY: frozenset[str] = frozenset({"rubberband", "hitchhiker"})


@pytest.fixture(scope="module")
def corpus(tmp_path_factory):
    loaded = {}
    for key, shape in {**shapes.SHAPES, **shapes.VARIANTS}.items():
        loaded[key] = (shape, shapes.load_shape(tmp_path_factory.mktemp(key.replace(":", "-")), shape))
    return loaded


def _forms_on_a_committed_day(shape, ld) -> bool:
    return any(ev.evaluation == "formed" for ticker in shape.tickers for _, ev in shapes.every_scan(ld, ticker))


def test_every_unlocked_setup_shape_is_evaluable(corpus):
    """FINAL §9 point (4) / [F-16] (4): the corpus shape of every setup the
    build claims to unlock is `evaluable`, or the missing atom is named."""
    report = {key: evaluability(ld.definition) for key, (_s, ld) in corpus.items()}
    not_evaluable = {key: e.missing_atoms for key, e in report.items() if not e.evaluable}
    assert not_evaluable == {}, not_evaluable


def test_registry_evaluable_implies_forms_or_awaits_a_day(corpus):
    """FINAL §9 gate 2, with the named deviation of this module's docstring."""
    awaiting = set()
    for key, (shape, ld) in corpus.items():
        if not evaluability(ld.definition).evaluable:
            continue
        if not _forms_on_a_committed_day(shape, ld):
            awaiting.add(key)
    assert awaiting == set(AWAITING_A_DAY)
