"""S2-P2 STEP-6 amendment (Astra R1-5): the five card/radar keys enter
`cobalt settings load` with typed schemas, reviewed-artifact SHA
verification, a diff and a round-trip proof.

`card.dot.*` and `card.health.*` are NOT settings — they stay solely in
`tunables.yaml` (L53), and the settings loader refuses them by name.
"""

from __future__ import annotations

import argparse
import hashlib
import os
from decimal import Decimal
from pathlib import Path

import pytest

from cobalt.settings import card as card_mod
from cobalt.settings.card import (
    CARD_SETTING_KEYS,
    CardSettings,
    CardSettingsError,
    load_card_file,
)

requires_db = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="Postgres env settings not available",
)

DARK = """\
card_settings:
  radar.cards_enabled: false
  card.alignment_default: {with_grade: 8, flat_grade: 5, against_grade: 2, flat_pct: 0.15}
  card.shadow_promotion_bar: {sessions: 10, pairs: 30, median_max: 1, within2_min: 0.90}
"""

ENABLED = """\
card_settings:
  radar.cards_enabled: true
  card.proposed_key: {a_plus_min: 0.9, a_min: 0.8, b_min: 0.6, c_min: 0.4}
  card.curves:
    rvol: [[1, 1], [3, 6], [10, 10]]
    atrs_from_open: [[0.5, 2], [2.5, 9]]
  card.alignment_default: {with_grade: 8, flat_grade: 5, against_grade: 2, flat_pct: 0.15}
  card.shadow_promotion_bar: {sessions: 10, pairs: 30, median_max: 1, within2_min: 0.90}
"""


def _write(tmp_path: Path, text: str, name: str = "card.yaml") -> tuple[Path, str]:
    path = tmp_path / name
    path.write_text(text, encoding="utf-8")
    return path, hashlib.sha256(text.encode("utf-8")).hexdigest()


def test_the_five_keys_and_nothing_else():
    assert CARD_SETTING_KEYS == (
        "radar.cards_enabled", "card.proposed_key", "card.curves",
        "card.alignment_default", "card.shadow_promotion_bar",
    )


def test_a_reviewed_file_loads_with_its_hash_and_round_trips(tmp_path):
    path, digest = _write(tmp_path, ENABLED)
    settings, sha = load_card_file(path, expected_sha256=digest)
    assert sha == digest
    assert settings.cards_enabled is True
    assert settings.proposed_key.a_min == Decimal("0.8")
    assert settings.curves["rvol"].anchors[1].x == Decimal("3")
    again = CardSettings.from_rows(settings.rows())
    assert again == settings
    assert set(settings.rows()) == set(CARD_SETTING_KEYS)


def test_bad_hash_refused(tmp_path):
    path, digest = _write(tmp_path, DARK)
    with pytest.raises(CardSettingsError, match="sha256"):
        load_card_file(path, expected_sha256="0" * 64)
    path.write_text(DARK + "# edited after review\n", encoding="utf-8")
    with pytest.raises(CardSettingsError, match="sha256"):
        load_card_file(path, expected_sha256=digest)


@pytest.mark.parametrize(
    "body, match",
    [
        ("card_settings:\n  radar.cards_enabled: false\n  card.colour: 3\n", "unknown"),
        ("card_settings:\n  radar.cards_enabled: nope\n", "radar.cards_enabled"),
        ("card_settings:\n  radar.cards_enabled: false\n  card.proposed_key: {a_plus_min: 0.5, a_min: 0.8, b_min: 0.6, c_min: 0.4}\n", "descend"),
        ("card_settings:\n  radar.cards_enabled: false\n  card.curves: {rvol: [[3, 6], [1, 1]]}\n", "increasing"),
        ("card_settings:\n  radar.cards_enabled: false\n  card.curves: {rvol: [[1, 11], [3, 6]]}\n", "less than or equal"),
        ("card_settings:\n  radar.cards_enabled: false\n  aset.enabled_grades: [A]\n", "aset.enabled_grades"),
        ("radar.cards_enabled: false\n", "card_settings"),
        ("card_settings:\n  card.curves: {}\n", "radar.cards_enabled"),
    ],
)
def test_unknown_or_malformed_setting_refused(tmp_path, body, match):
    path, digest = _write(tmp_path, body)
    with pytest.raises(CardSettingsError, match=match):
        load_card_file(path, expected_sha256=digest)


@pytest.mark.parametrize("key", ["card.dot.red_max", "card.health.participation_warn"])
def test_tunables_only_keys_are_refused_by_the_settings_loader(tmp_path, key):
    path, digest = _write(tmp_path, f"card_settings:\n  radar.cards_enabled: false\n  {key}: 3\n")
    with pytest.raises(CardSettingsError, match="tunables.yaml"):
        load_card_file(path, expected_sha256=digest)


def test_absent_dark_only_optional_keys_are_null_and_enabling_requires_them(tmp_path):
    path, digest = _write(tmp_path, DARK)
    settings, _ = load_card_file(path, expected_sha256=digest)
    assert settings.proposed_key is None and settings.curves is None
    assert set(settings.rows()) == {
        "radar.cards_enabled", "card.alignment_default", "card.shadow_promotion_bar",
    }
    with pytest.raises(CardSettingsError, match="card.proposed_key"):
        CardSettings.from_rows({"radar.cards_enabled": True, "card.curves": {"rvol": [[1, 1], [2, 2]]}})


def test_the_runtime_reader_refuses_missing_cards_enabled_rather_than_defaulting():
    with pytest.raises(CardSettingsError, match="radar.cards_enabled"):
        CardSettings.from_rows({"aset.enabled_grades": ["A"]})
    assert CardSettings.from_rows({"radar.cards_enabled": False}).cards_enabled is False


class FakeStore:
    def __init__(self, values=None, fail=False):
        self.data = dict(values or {})
        self.puts = []
        self.fail = fail

    def ensure_schema(self):
        return None

    def values(self):
        return dict(self.data)

    def put(self, rows, *, source, delete=(), before_commit=None):
        self.puts.append((dict(rows), tuple(delete), source))
        if self.fail:
            raise RuntimeError("synthetic failure inside the transaction")
        self.data.update(rows)
        for key in delete:
            self.data.pop(key, None)
        return {key: "updated" for key in rows}


def _args(path, *, sha=None, apply=False):
    return argparse.Namespace(
        card=str(path), sha256=sha, dry_run=not apply, apply=apply,
        from_dir=None, from_git=None,
    )


def test_dry_run_prints_the_diff_and_the_hash_and_writes_nothing(tmp_path, monkeypatch, capsys):
    path, digest = _write(tmp_path, DARK)
    store = FakeStore({"radar.cards_enabled": True, "card.curves": {"rvol": [[1, 1], [2, 2]]}})
    monkeypatch.setattr(card_mod, "TraderSettingsStore", lambda: store)
    card_mod.cmd_load_card(_args(path))
    out = capsys.readouterr().out
    assert digest in out
    assert "~ radar.cards_enabled" in out and "- card.curves" in out
    assert store.puts == []


def test_apply_requires_the_hash_verifies_the_round_trip_and_is_one_put(tmp_path, monkeypatch, capsys):
    path, digest = _write(tmp_path, DARK)
    store = FakeStore({"card.curves": {"rvol": [[1, 1], [2, 2]]}, "aset.enabled_grades": ["A"]})
    monkeypatch.setattr(card_mod, "TraderSettingsStore", lambda: store)
    monkeypatch.setattr(card_mod, "assert_writable", lambda *a, **k: None)
    with pytest.raises(SystemExit, match="--sha256"):
        card_mod.cmd_load_card(_args(path, apply=True))
    assert store.puts == []
    card_mod.cmd_load_card(_args(path, sha=digest, apply=True))
    assert len(store.puts) == 1
    rows, deleted, source = store.puts[0]
    assert deleted == ("card.curves",) and digest in source
    assert "aset.enabled_grades" in store.data  # never touches the sheet keys
    assert "round trip" in capsys.readouterr().out


def test_a_failed_apply_leaves_the_store_untouched(tmp_path, monkeypatch):
    path, digest = _write(tmp_path, ENABLED)
    store = FakeStore({"radar.cards_enabled": False}, fail=True)
    monkeypatch.setattr(card_mod, "TraderSettingsStore", lambda: store)
    monkeypatch.setattr(card_mod, "assert_writable", lambda *a, **k: None)
    with pytest.raises(RuntimeError, match="synthetic"):
        card_mod.cmd_load_card(_args(path, sha=digest, apply=True))
    assert store.data == {"radar.cards_enabled": False}


def test_settings_are_re_read_on_every_call_not_cached():
    store = FakeStore({"radar.cards_enabled": False})
    reader = card_mod.CardSettingsReader(store)
    assert reader.current().cards_enabled is False
    store.data["radar.cards_enabled"] = True
    store.data["card.proposed_key"] = {"a_plus_min": 0.9, "a_min": 0.8, "b_min": 0.6, "c_min": 0.4}
    store.data["card.curves"] = {"rvol": [[1, 1], [2, 2]]}
    assert reader.current().cards_enabled is True


@requires_db
def test_card_settings_apply_and_delete_round_trip_on_cobalt_dev():
    from cobalt.settings.store import TraderSettingsStore

    store = TraderSettingsStore("cobalt_dev")
    store.ensure_schema()
    enabled = CardSettings.from_rows(
        {"radar.cards_enabled": True,
         "card.proposed_key": {"a_plus_min": 0.9, "a_min": 0.8, "b_min": 0.6, "c_min": 0.4},
         "card.curves": {"rvol": [[1, 1], [3, 6]]}}
    )
    store.put(enabled.rows(), source="test")
    assert CardSettings.from_rows(store.values()) == enabled
    dark = CardSettings.from_rows({"radar.cards_enabled": False})
    store.put(dark.rows(), source="test", delete=["card.proposed_key", "card.curves"])
    assert CardSettings.from_rows(store.values()) == dark
