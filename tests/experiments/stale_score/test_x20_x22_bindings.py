"""X20 + X22 (v2 §7, before S1).

X20: `replay/formations.py`'s version gate — does it read a binding's
STORED string or the live module constant? A stored string would refuse old
nightly bindings until regenerated (accepted; the old string is never
unioned back).
X22: `aset/radar_panel.py`'s `last=r.last_price` site — display only, or a
missed scorer that recomputes proximity from `last`?
"""

from __future__ import annotations

import ast
import inspect

import cobalt.aset.radar_panel as panel
import cobalt.radar.evaluate as evaluate
import cobalt.replay.formations as formations
import cobalt.replay.runner as runner


def test_x20_the_nightly_binding_reads_the_live_module_constant():
    source = inspect.getsource(runner.formation_replay)
    live = 'getattr(evaluator, "EVALUATOR_VERSION", None)' in source
    passes_it = "evaluator_version=version" in source
    supported = evaluate.EVALUATOR_VERSION in formations.SUPPORTED_EVALUATORS
    print(f"X20: reads_live_constant={live} passes_that_value={passes_it} "
          f"current_version_supported={supported} supported={sorted(formations.SUPPORTED_EVALUATORS)} "
          f"evaluator={evaluate.EVALUATOR_VERSION}")
    assert live and passes_it and supported


def test_x22_the_panel_last_price_site_only_displays():
    tree = ast.parse(inspect.getsource(panel))
    called = {n.func.id if isinstance(n.func, ast.Name) else getattr(n.func, "attr", None)
              for n in ast.walk(tree) if isinstance(n, ast.Call)}
    scorers = sorted(called & {"proximity", "score_card", "card_score", "score_last"})
    view = inspect.getsource(panel.build_ladder_view)
    print(f"X22: panel_calls_a_scorer={bool(scorers)} scorers={scorers} "
          f"last_site_display={'last=r.last_price' in view} proximity_site_stored={'proximity=r.proximity' in view}")
    assert not scorers and "last=r.last_price" in view and "proximity=r.proximity" in view
