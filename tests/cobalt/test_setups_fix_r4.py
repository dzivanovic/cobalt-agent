"""Setups fix round 4 (prompt `72-setups-fix-r4.md`): the FIX rows of the
round-2 house check (`setups-check-r2r3-2026-09-22.md`), as classified by
`setups-fix-r4-draft-2026-09-22.md` (L75). Offline; constructed literals of
this file's own only (L32 / L69).
"""

from __future__ import annotations

import pytest

import radar_p2_support as sup
import setups_shapes as shapes
from test_setups_fix_r3 import _per_trade_accepted

# =====================================================================
# F1 — the dials probe asserts WHY a note row was refused
# =====================================================================


def _rubberband_probe(tmp_path):
    shape = shapes.SHAPES["rubberband"]
    return tmp_path, shape.note_slug, shape.mapping(), shape.rows()


def test_f1_a_malformed_probe_note_fails_the_probe_loudly(tmp_path):
    """RED on 8da261a: any refusal printed "not reachable". A tunables row
    that does not parse is a broken probe, not an engine-key refusal."""
    from cobalt.taxonomy.vault_loader import VaultTaxonomyError

    root, slug, mapping, rows = _rubberband_probe(tmp_path)
    malformed = [*rows, {"key": "example_probe.malformed", "value": 1}]  # no unit, scope, …
    unit = sup.engine_tunables()["stop.buffer"].unit.value
    with pytest.raises(VaultTaxonomyError, match="invalid tunables rows"):
        _per_trade_accepted(root, slug, mapping, malformed, "stop.buffer", unit)


def test_f1_the_engine_key_refusal_still_reads_not_reachable(tmp_path):
    """GREEN guard: r3's `## DIALS` row `rubberband | stop.buffer |
    assumed / engine only (global)` stays a refusal (False), not a raise."""
    root, slug, mapping, rows = _rubberband_probe(tmp_path)
    unit = sup.engine_tunables()["stop.buffer"].unit.value
    assert _per_trade_accepted(root, slug, mapping, rows, "stop.buffer", unit) is False
