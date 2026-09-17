"""S2-P4 STEP-6 / Astra R1-14 — `radar.benchmark` loads through a real
settings-loader seam: `cobalt settings load --optional <file> --sha256
<hash> --dry-run|--apply`, validated by `BenchmarkSettings`, never added to
`SETTING_KEYS`, hash-verified, and refused inside the market_reset pause.
"""

from __future__ import annotations

import argparse
import hashlib
from datetime import datetime, timezone

import pytest

from cobalt.settings import cli as settings_cli
from cobalt.settings.models import SETTING_KEYS, BenchmarkSettings, TraderSettingsError

BODY = b"optional_settings:\n  radar.benchmark: {top_n: 20, min_move_pct: 10}\n"


class FakeStore:
    def __init__(self, rows=None):
        self.rows = dict(rows or {})
        self.puts = []

    def values(self):
        return dict(self.rows)

    def put(self, rows, *, source, before_commit=None):
        self.puts.append((dict(rows), source))
        self.rows.update(rows)
        return {k: "created" for k in rows}


def _args(path, *, sha=None, apply=False):
    return argparse.Namespace(optional=str(path), sha256=sha, dry_run=not apply, apply=apply,
                              from_dir=None, from_git=None)


@pytest.fixture
def store(monkeypatch):
    fake = FakeStore({"aset.sheet_modes": {"x": 1}})
    monkeypatch.setattr(settings_cli, "TraderSettingsStore", lambda: fake)
    return fake


def test_optional_key_round_trip_applies_and_rereads(tmp_path, store, capsys):
    path = tmp_path / "benchmark.yaml"
    path.write_bytes(BODY)
    digest = hashlib.sha256(BODY).hexdigest()
    settings_cli.cmd_load(_args(path, sha=digest, apply=True))
    assert store.puts == [({"radar.benchmark": {"top_n": 20, "min_move_pct": "10"}}, "optional:benchmark.yaml")]
    assert BenchmarkSettings.from_rows(store.values()) == BenchmarkSettings(top_n=20, min_move_pct=10)
    assert "round trip" in capsys.readouterr().out
    settings_cli.cmd_load(_args(path, sha=digest, apply=True))           # identical: no second put
    assert len(store.puts) == 1


def test_dry_run_prints_the_diff_and_writes_nothing(tmp_path, store, capsys):
    path = tmp_path / "benchmark.yaml"
    path.write_bytes(BODY)
    settings_cli.cmd_load(_args(path))
    assert store.puts == []
    assert "+ radar.benchmark" in capsys.readouterr().out


def test_hash_mismatch_and_a_missing_hash_on_apply_refuse(tmp_path, store):
    path = tmp_path / "benchmark.yaml"
    path.write_bytes(BODY)
    with pytest.raises(SystemExit, match="sha256 mismatch"):
        settings_cli.cmd_load(_args(path, sha="0" * 64, apply=True))
    with pytest.raises(SystemExit, match="needs --sha256"):
        settings_cli.cmd_load(_args(path, apply=True))
    assert store.puts == []


@pytest.mark.parametrize("body,match", [
    (b"optional_settings:\n  radar.benchmark: {top_n: 0, min_move_pct: 10}\n", "invalid radar.benchmark"),
    (b"optional_settings:\n  radar.benchmark: {top_n: 20}\n", "invalid radar.benchmark"),
    (b"optional_settings:\n  radar.cap: 3\n", "unknown optional setting"),
    (b"optional_settings:\n  aset.enabled_grades: [A]\n", "required sheet/day-mode setting"),
    (b"radar.benchmark: {top_n: 20, min_move_pct: 10}\n", "exactly one top-level mapping"),
])
def test_absent_or_malformed_benchmark_refuses(tmp_path, store, body, match):
    path = tmp_path / "benchmark.yaml"
    path.write_bytes(body)
    with pytest.raises(SystemExit, match=match):
        settings_cli.cmd_load(_args(path, sha=hashlib.sha256(body).hexdigest(), apply=True))
    assert store.puts == []


def test_apply_inside_the_market_reset_pause_refuses(tmp_path, store, monkeypatch):
    from cobalt.session import SessionBlocked
    from cobalt.session import clock as clock_mod

    monkeypatch.setattr(clock_mod, "now_utc", lambda: datetime(2026, 9, 4, 0, 30, tzinfo=timezone.utc))  # 20:30 ET
    path = tmp_path / "benchmark.yaml"
    path.write_bytes(BODY)
    with pytest.raises(SessionBlocked):
        settings_cli.cmd_load(_args(path, sha=hashlib.sha256(BODY).hexdigest(), apply=True))
    assert store.puts == []


def test_the_benchmark_never_joins_the_required_keys():
    assert "radar.benchmark" not in SETTING_KEYS
    with pytest.raises(TraderSettingsError):
        BenchmarkSettings.from_rows({"aset.sheet_modes": {}})
