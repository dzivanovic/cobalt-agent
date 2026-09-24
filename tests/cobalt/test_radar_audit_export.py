"""S2-P2 STEP-11 — `cobalt radar audit-export --run <id> | --replay <date>`
writes the frozen L52-d bundle (R11): bars window, settings snapshot,
tunables rows, AST, published card rows, hashes.

The auditor is another house, network off, with an independently written
checker. What this suite proves is the bundle's half: every file is
there, every hash is recorded and re-verifiable, Cobalt's own replay of
the stored inputs agrees with what it published (or the export refuses),
and the numbers can be recomputed from the bundle's files alone.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timedelta, timezone
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

import pytest

import radar_p2_support as sup
from cobalt.radar import audit_export as ax
from cobalt.radar import cli as radar_cli
from cobalt.session import session_clock
from test_radar_evaluate import SCAN0, World
from test_radar_evaluate_cli import ReadOnlyRadar, _daily

UTC = timezone.utc
GENERATED = datetime(2026, 9, 16, 22, 0, tzinfo=UTC)
RUN_FILES = {"manifest.json", "bars.json", "settings.json", "tunables.json", "ast.json", "definitions.json",
             "cards.json", "seam.json", "receipts.json", "formulas.json"}


class RunStores:
    """The two side-scoped reads the run export makes, over a World."""

    def __init__(self, world: World):
        self.world = world

    # SYSTEM side
    def score_run(self, run_id):
        run = self.world.radar.runs.get(run_id)
        return None if run is None else dict(run)

    def scores_for_run(self, run_id):
        return [dict(s) for s in self.world.radar.scores.values() if s["run_id"] == run_id]

    # USER side
    def receipt_for_run(self, run_id):
        found = [r for r in self.world.cards.receipts if r["run_id"] == run_id]
        return found[0]["id"] if len(found) == 1 else None

    def receipts_chain(self, receipt_id):
        by_id = {r["id"]: r for r in self.world.cards.receipts}
        chain, current = [], receipt_id
        while current is not None:
            chain.append(by_id[current])
            current = by_id[current]["observations"]["base_receipt_id"]
        return list(reversed(chain))


def _world_with_taps() -> World:
    world = World()
    world.scan(SCAN0)
    world.cards.tap(1, "trail_fit", 7)
    world.cards.tap(1, "setup_relation", 8)
    world.scan(SCAN0 + timedelta(seconds=100))
    return world


def _export_run(world, out, run_id=2):
    stores = RunStores(world)
    return ax.export_run(run_id, radar_store=stores, card_store=stores, out=out, clock=session_clock(),
                         generated_at=GENERATED)


def _load(out: Path, name: str):
    return json.loads((out / name).read_text())


def test_run_bundle_has_every_file_and_a_manifest_of_their_hashes(tmp_path):
    out = tmp_path / "bundle"
    manifest = _export_run(_world_with_taps(), out)
    assert {p.name for p in out.iterdir()} == RUN_FILES
    on_disk = _load(out, "manifest.json")
    assert on_disk == json.loads(manifest.model_dump_json())
    for name, digest in on_disk["files"].items():
        assert hashlib.sha256((out / name).read_bytes()).hexdigest() == digest, name
    assert set(on_disk["files"]) == RUN_FILES - {"manifest.json"}
    assert on_disk["bundle_sha256"] == hashlib.sha256(
        json.dumps(on_disk["files"], sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    assert on_disk["mode"] == "run" and on_disk["source"] == {"run_id": 2}
    assert on_disk["hashes"]["tunables_sha256"]["matches"] and on_disk["hashes"]["settings_sha256"]["matches"]
    assert on_disk["hashes"]["cohort_sha256"]["matches"]
    assert on_disk["self_check"] == {"cards": 1, "evaluations": 1, "all_equal": True}


def test_run_bundle_carries_bars_window_settings_tunables_ast_and_published_cards(tmp_path):
    out = tmp_path / "bundle"
    _export_run(_world_with_taps(), out)
    bars = _load(out, "bars.json")
    member = bars["members"][0]
    assert member["ticker"] == "FTFT" and member["i1"] and member["daily"] and member["rvol"]["value"] == 4.2
    assert all(datetime.fromisoformat(r["ts"]) + timedelta(minutes=1) <= datetime.fromisoformat(member["as_of"])
               for r in member["i1"])
    settings = _load(out, "settings.json")
    assert settings["card"]["card.curves"] and settings["enabled_grades_today"]
    assert "radar.scan_interval" in _load(out, "tunables.json")["rows"]
    ast = _load(out, "ast.json")["defs"][0]
    pre = ast["preconditions"][0]
    assert pre["expr"] == "Extension.state == culminating" and pre["ast"]["node"] == "Compare"
    assert "Extension" in " ".join(pre["required_atoms"])
    card = _load(out, "cards.json")["cards"][0]
    assert card["published"]["card_score"] is not None and card["taps"]
    assert {d["factor"] for d in card["published"]["dots"]} >= {"rvol", "trail_fit"}
    seam = _load(out, "seam.json")
    assert seam["run"]["id"] == 2 and seam["scores"][0]["evaluation"] == "formed"
    formulas = _load(out, "formulas.json")
    assert "round(conviction × proximity × 100)" in formulas["card_score"]
    assert formulas["formula_sha256"] and formulas["files"]


def test_the_card_numbers_recompute_from_the_bundle_files_alone(tmp_path):
    """An independent-style recompute: bars.json + cards.json only."""
    out = tmp_path / "bundle"
    _export_run(_world_with_taps(), out)
    card = _load(out, "cards.json")["cards"][0]
    last = Decimal(_load(out, "bars.json")["members"][0]["i1"][-1]["close"])
    entry, stop = Decimal(card["entry"]), Decimal(card["stop"])
    raw = Decimal(1) - abs(last - entry) / (3 * abs(entry - stop))
    prox = min(max(raw, Decimal(0)), Decimal(1)).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
    taps = {}
    for tap in sorted(card["taps"], key=lambda t: t["id"]):
        taps[tap["factor"]] = tap["grade"]
    conviction = (Decimal(sum(taps.values())) / len(taps) / 10).quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)
    published = card["published"]
    assert abs(Decimal(published["proximity"]) - prox) <= Decimal("1e-6")
    assert abs(Decimal(published["conviction"]) - conviction) <= Decimal("1e-6")
    assert published["card_score"] == int((conviction * prox * 100).quantize(Decimal(1), rounding=ROUND_HALF_UP))


def test_the_bundle_is_frozen_an_existing_nonempty_out_dir_is_refused(tmp_path):
    out = tmp_path / "bundle"
    out.mkdir()
    (out / "old.json").write_text("{}")
    with pytest.raises(ax.AuditExportError, match="not empty"):
        _export_run(_world_with_taps(), out)


def test_a_stored_hash_that_does_not_match_its_inputs_refuses(tmp_path):
    world = _world_with_taps()
    world.radar.runs[2]["tunables_sha256"] = "0" * 64
    with pytest.raises(ax.AuditExportError, match="tunables_sha256"):
        _export_run(world, tmp_path / "bundle")
    assert not (tmp_path / "bundle").exists()


def test_cobalts_own_replay_disagreeing_with_what_it_published_refuses(tmp_path):
    world = _world_with_taps()
    world.cards.receipts[-1]["tap_versions"]["cards"][0]["published"]["card_score"] = 99
    with pytest.raises(ax.AuditExportError, match="replay disagrees"):
        _export_run(world, tmp_path / "bundle")


def test_a_run_without_its_receipt_or_row_refuses(tmp_path):
    world = _world_with_taps()
    with pytest.raises(ax.AuditExportError, match="no radar_score_run 9"):
        _export_run(world, tmp_path / "a", run_id=9)
    world.cards.receipts = [r for r in world.cards.receipts if r["run_id"] != 2]
    with pytest.raises(ax.AuditExportError, match="receipt"):
        _export_run(world, tmp_path / "b")


def test_a_dark_run_exports_with_an_explicit_empty_card_list(tmp_path):
    world = World(cards_enabled=False)
    world.scan(SCAN0)
    out = tmp_path / "bundle"
    _export_run(world, out, run_id=1)
    cards = _load(out, "cards.json")
    assert cards["cards"] == [] and cards["cards_enabled"] is False and "dark" in cards["note"]


# ---------------------------------------------------------------------
# --replay
# ---------------------------------------------------------------------


def test_replay_bundle_writes_nothing_to_stores_and_bundles_candidate_formations(tmp_path):
    radar = ReadOnlyRadar(sup.members("FTFT"), {"FTFT": sup.fixture_bars("FTFT")})
    out = tmp_path / "replay"
    settings_rows = sup.fixture_settings_rows(**{
        "radar.cards_enabled": False,
        "card.curves": {"rvol": [[1, 1], [3, 6], [10, 10]], "atrs_from_open": [[1, 2], [6, 9]]},
    })
    manifest = ax.export_replay(
        sup.TRADE_DATE, pool_key="pool", slug_filter=None, radar_store=radar,
        defs_source=lambda: ([sup.loaded()], {}), daily_source=_daily, tunables=sup.engine_tunables(),
        defaults=sup.defaults(), settings_values=settings_rows, clock=session_clock(), out=out,
        generated_at=GENERATED,
    )
    assert radar.runs == {} and radar.scores == {}
    assert manifest.mode == "replay" and manifest.source == {"replay": sup.TRADE_DATE.isoformat()}
    assert {p.name for p in out.iterdir()} == RUN_FILES - {"receipts.json"}
    cards = _load(out, "cards.json")
    assert cards["published"] is False and "writes nothing" in cards["note"]
    first = cards["cards"][0]
    assert first["ticker"] == "FTFT" and first["direction"] == "short" and first["formed_bar_ts"]
    dots = {d["factor"]: d for d in first["candidate"]["dots"]}
    assert dots["rvol"]["na_reason"] == "input_unavailable"  # replay has no RVOL snapshot
    assert dots["atrs_from_open"]["engine_grade"] is not None
    assert first["candidate"]["card_score"] is None and first["candidate"]["conviction"] is None
    bars = _load(out, "bars.json")["members"][0]
    assert bars["ticker"] == "FTFT" and len(bars["i1"]) == len(sup.fixture_bars("FTFT"))
    for name, digest in _load(out, "manifest.json")["files"].items():
        assert hashlib.sha256((out / name).read_bytes()).hexdigest() == digest


def test_cli_takes_exactly_one_of_run_or_replay_and_a_required_out():
    parser = argparse.ArgumentParser()
    radar_cli.add_parser(parser.add_subparsers(dest="group"))
    args = parser.parse_args(["radar", "audit-export", "--run", "7", "--out", "b"])
    assert args.run == 7 and args.out == "b"
    with pytest.raises(SystemExit):
        parser.parse_args(["radar", "audit-export", "--run", "7"])
    with pytest.raises(SystemExit):
        parser.parse_args(["radar", "audit-export", "--run", "7", "--replay", "2026-01-06", "--out", "b"])
