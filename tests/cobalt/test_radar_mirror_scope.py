"""radar-mirror-scope (card 1020): the vault-note mirror tombstones only the
`radar.*` keys it owns.

On 2026-10-21 the mirror rewrote `radar.cards_enabled` (written by
`--card`) and `radar.benchmark` (written by `--optional`) as `removed`
after a Lists note edit, because it tombstoned every `radar.*` key absent
from the notes, whoever wrote it. A key is the mirror's when its stored
`source` starts with `vault:radar-notes@`; every other key is left alone,
an unknown source with one warning (M1). The label names the note that
changed (M4). A fake store, never a database (L69); constructed values
only (L32); each pin finds its lines by content and holds no hash.
"""

from __future__ import annotations

import hashlib
import json
from datetime import UTC, datetime
from pathlib import Path

import pytest
from loguru import logger

from cobalt.radar.notes import load_sources, mirror_sources

FIXTURES = Path("tests/fixtures/radar")
SCREENS = FIXTURES / "radar-screens.example.md"
LISTS = FIXTURES / "radar-lists.example.md"
MIRROR_NOW = datetime(2026, 9, 3, 14, 0, tzinfo=UTC)
MIRROR_LABEL = "vault:radar-notes@"
CARD_SOURCE = "card:card-settings.yaml@sha256:" + "0" * 64
OPTIONAL_SOURCE = "optional:optional-settings.yaml"
SEEDS = {
    "radar.cards_enabled": {"value": True, "source": CARD_SOURCE},
    "radar.benchmark": {"value": {"top_n": 20, "min_move_pct": 10}, "source": OPTIONAL_SOURCE},
}


class _Store:
    """The settings store's shape: `put` skips a row whose value is
    unchanged, so that row keeps its old `source` (`settings/store.py`)."""

    def __init__(self, seeds):
        self.stored = {key: dict(row) for key, row in seeds.items()}
        self.sent = None
        self.sent_source = None

    def rows(self):
        return [
            {"key": key, "value": row["value"], "source": row["source"], "updated_at": None}
            for key, row in sorted(self.stored.items())
        ]

    def values(self):
        return {key: row["value"] for key, row in self.stored.items()}

    def put(self, rows, *, source, delete=(), before_commit=None):
        self.sent = rows
        self.sent_source = source
        if before_commit is not None:
            before_commit()
        outcome = {}
        for key, value in rows.items():
            if key in self.stored and self.stored[key]["value"] == value:
                outcome[key] = "unchanged"
                continue
            outcome[key] = "updated" if key in self.stored else "created"
            self.stored[key] = {"value": value, "source": source}
        return outcome


def _parsed(screens_path, lists_path):
    return load_sources(
        screens_path,
        lists_path,
        scan_interval=60,
        poll_interval=60,
        finviz_max_rpm=100,
        list_chunk_size=50,
        context_tickers=0,
    )


def _seed_from_notes(store, lists_path=LISTS, screens_path=SCREENS):
    return mirror_sources(_parsed(screens_path, lists_path), store=store, now=MIRROR_NOW)


def _lists_without_exclude(tmp_path):
    """The Lists fixture with its last fence (`kind: exclude`) cut, by content."""
    text = LISTS.read_text()
    head, marker, last = text.rpartition("```yaml\n")
    assert marker and last.startswith("kind: exclude\n"), "the fixture's last fence is the exclude block"
    path = tmp_path / "lists.md"
    path.write_text(head.rstrip() + "\n")
    return path


def _snapshot(store, key):
    return json.dumps(store.stored[key], sort_keys=True)


def _warnings_during(call):
    lines: list[str] = []
    sink = logger.add(
        lambda message: lines.append(message.record["message"]), level="WARNING"
    )
    try:
        call()
    finally:
        logger.remove(sink)
    return lines


def test_m1_unknown_source_is_left_alone_loudly(tmp_path):
    store = _Store({**SEEDS, "radar.hand_typed": {"value": 1, "source": "hand:typed"}})
    hand_before = _snapshot(store, "radar.hand_typed")
    edited = _lists_without_exclude(tmp_path)

    for lists_path in (LISTS, edited):
        lines = _warnings_during(lambda: _seed_from_notes(store, lists_path))
        assert "radar.hand_typed" not in store.sent, store.sent.get("radar.hand_typed")
        assert _snapshot(store, "radar.hand_typed") == hand_before
        named = [line for line in lines if "radar.hand_typed" in line]
        assert len(named) == 1, lines
        assert "hand:typed" in named[0]
        # a known other writer is left alone silently
        assert not [line for line in lines if "radar.cards_enabled" in line or "radar.benchmark" in line]


def test_m2_a_lists_edit_that_drops_a_block_leaves_card_and_optional_keys_byte_identical(tmp_path):
    store = _Store(SEEDS)
    _seed_from_notes(store)
    assert store.stored["radar.exclude"]["source"].startswith(MIRROR_LABEL)
    snapshots = {key: _snapshot(store, key) for key in SEEDS}

    _seed_from_notes(store, _lists_without_exclude(tmp_path))

    for key in SEEDS:
        assert key not in store.sent, (key, store.sent.get(key))
    assert {key: _snapshot(store, key) for key in SEEDS} == snapshots
    assert snapshots == {key: json.dumps(row, sort_keys=True) for key, row in SEEDS.items()}


def test_m3_a_block_the_note_drops_is_still_tombstoned(tmp_path):
    store = _Store(SEEDS)
    _seed_from_notes(store)
    assert store.stored["radar.exclude"]["value"]["status"] == "ok"

    _seed_from_notes(store, _lists_without_exclude(tmp_path))

    assert store.sent["radar.exclude"]["status"] == "removed"
    assert store.stored["radar.exclude"]["value"]["status"] == "removed"
    assert store.stored["radar.exclude"]["source"].startswith(MIRROR_LABEL)
    assert store.sent.get("radar.list.index_heavyweights", {}).get("status") != "removed"


def _note_label(path):
    return MIRROR_LABEL + hashlib.sha256(path.read_bytes()).hexdigest()[:12]


def test_m4_the_source_names_the_note_that_changed(tmp_path):
    store = _Store(SEEDS)
    _seed_from_notes(store)
    edited = _lists_without_exclude(tmp_path)

    _seed_from_notes(store, edited)

    assert store.sent_source == _note_label(edited)
    assert store.sent_source != _note_label(SCREENS)


def _screens_copy(tmp_path):
    path = tmp_path / "screens.md"
    path.write_text(SCREENS.read_text() + "\nA constructed prose edit.\n")
    return path


@pytest.mark.parametrize("case", ["first", "screens_only", "lists_only", "both", "lists_missing"])
def test_m4_the_label_in_each_case(tmp_path, case):
    store = _Store(SEEDS)
    if case == "first":
        _seed_from_notes(store)
        assert store.sent_source == _note_label(SCREENS)
        return
    _seed_from_notes(store)
    screens, lists = SCREENS, LISTS
    if case in ("screens_only", "both"):
        screens = _screens_copy(tmp_path)
    if case in ("lists_only", "both"):
        lists = _lists_without_exclude(tmp_path)
    if case == "lists_missing":
        lists = tmp_path / "absent.md"

    _seed_from_notes(store, lists, screens)

    if case == "lists_missing":
        # the only changed note has no hash, and Screens did not change
        expected = MIRROR_LABEL + "missing"
    else:
        expected = _note_label(lists if case == "lists_only" else screens)
    assert store.sent_source == expected
