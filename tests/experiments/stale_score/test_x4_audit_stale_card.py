"""X4, CHANGE (v2 §7, before the audit / deploy gate): a same-version
STALE card — `audit-export --run` replays it and recompute = published,
JSON null included; a pre-change receipt — refused with the version
message, and the test fails if the error is the replay-mismatch path."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import pytest

from cobalt.radar import audit_export as ax
from cobalt.session import session_clock

from stale_support import SCAN0, bars_before, stale_as_of

GENERATED = datetime(2026, 9, 16, 22, 0, tzinfo=timezone.utc)


def _stale_world():
    from test_radar_evaluate import World
    from test_radar_audit_export import RunStores

    world = World()
    world.scan(SCAN0)
    kept = bars_before(SCAN0)
    world.radar.bars["FTFT"] = list(kept)
    world.scan(stale_as_of(kept))
    return world, RunStores(world)


def test_x4_a_stale_card_exports_and_a_pre_change_receipt_is_refused_by_version(tmp_path):
    world, stores = _stale_world()
    manifest = ax.export_run(2, radar_store=stores, card_store=stores, out=tmp_path / "ok", clock=session_clock(),
                             generated_at=GENERATED)
    published = json.loads((tmp_path / "ok" / "cards.json").read_text())["cards"][0]["published"]
    text = (tmp_path / "ok" / "cards.json").read_text()
    for receipt in world.cards.receipts:
        receipt["observations"]["evaluator_version"] = "s2p2.2"
    with pytest.raises(ax.AuditExportError) as refused:
        ax.export_run(2, radar_store=stores, card_store=stores, out=tmp_path / "old", clock=session_clock(),
                      generated_at=GENERATED)
    message = str(refused.value)
    print(f"X4: self_check_all_equal={manifest.self_check['all_equal']} published_proximity={published['proximity']!r} "
          f"published_card_score={published['card_score']!r} json_null={'\"proximity\": null' in text} "
          f"reason_is_sentence={str(published['score_suppressed']).startswith('bars stale — last close ')} "
          f"pre_change_refused_by_version={'evaluator version' in message} "
          f"mismatch_path={'replay disagrees' in message or 'own replay failed' in message} "
          f"nothing_written={not (tmp_path / 'old').exists()}")
    assert manifest.self_check["all_equal"] is True
    assert published["proximity"] is None and published["card_score"] is None and '"proximity": null' in text
    assert "evaluator version" in message and "'s2p2.2'" in message
    assert "replay disagrees" not in message and "own replay failed" not in message
    assert not (tmp_path / "old").exists()
