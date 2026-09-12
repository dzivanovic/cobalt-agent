"""Fenced note contract, per-field refusal matrix, hashes, and R2 tests."""

from datetime import datetime, timezone
from pathlib import Path
import re

import pytest

from cobalt.archiver.collector import scrub
from cobalt.radar.models import ScreenBlock
from cobalt.radar.notes import load_sources, mirror_sources, parse_note

FIXTURES = Path("tests/fixtures/radar")
MIRROR_NOW = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)


def test_both_fixtures_parse_and_exactly_one_synthetic_screen():
    screens = parse_note(FIXTURES / "radar-screens.example.md", "screens")
    lists = parse_note(FIXTURES / "radar-lists.example.md", "lists")
    assert screens.ok, screens.errors
    assert lists.ok, lists.errors
    assert sum(isinstance(x.block, ScreenBlock) for x in screens.blocks) == 1
    assert [x.block.screen for x in screens.blocks if isinstance(x.block, ScreenBlock)] == ["example_session_scan"]



def test_prose_and_non_yaml_fences_are_ignored_and_hash_changes_by_byte(tmp_path):
    source = (FIXTURES / "radar-screens.example.md").read_bytes()
    one = tmp_path / "one.md"
    two = tmp_path / "two.md"
    one.write_bytes(b"prose\n```text\nignored\n```\n" + source)
    two.write_bytes(b"Prose\n```text\nignored\n```\n" + source)
    parsed_one = parse_note(one, "screens")
    parsed_two = parse_note(two, "screens")
    assert parsed_one.ok and parsed_two.ok
    assert [b.sha256 for b in parsed_one.blocks] == [b.sha256 for b in parsed_two.blocks]
    assert parsed_one.note_sha256 != parsed_two.note_sha256


class MirrorStore:
    def __init__(self):
        self.sent = None

    def values(self):
        return {}

    def put(self, rows, *, source, before_commit=None):
        self.sent = rows
        if before_commit:
            before_commit()
        return {key: "created" for key in rows}


def _loaded(screens_path, *, rpm=100):
    return load_sources(
        screens_path,
        FIXTURES / "radar-lists.example.md",
        scan_interval=60,
        poll_interval=60,
        finviz_max_rpm=rpm,
        list_chunk_size=50,
    )


@pytest.mark.parametrize("case", ["missing", "duplicate"])
def test_pool_cardinality_refusal_freezes_and_is_mirrored(tmp_path, case):
    original = (FIXTURES / "radar-screens.example.md").read_text()
    if case == "missing":
        payload = original.rsplit("```yaml", 1)[0]
    else:
        pool_fence = "```yaml" + original.rsplit("```yaml", 1)[1]
        payload = original + "\n" + pool_fence
    path = tmp_path / f"{case}.md"
    path.write_text(payload)

    parsed = _loaded(path)
    assert parsed.frozen
    assert "pool" in scrub(parsed.pool_error or "")
    assert ("found 0" if case == "missing" else "duplicate block key 'pool'") in scrub(
        parsed.pool_error or ""
    )

    store = MirrorStore()
    mirror_sources(parsed, store=store, now=MIRROR_NOW)
    assert store.sent["radar.note.screens"]["status"] == "parse_failed"
    if case == "duplicate":
        assert store.sent["radar.pool"]["status"] == "parse_failed"


@pytest.mark.parametrize(
    ("case", "expected"),
    [("unknown_kind", "kind"), ("unknown_override", "unknown_override")],
)
def test_named_field_refusal_matrix(tmp_path, case, expected):
    if case == "unknown_kind":
        path = tmp_path / "unknown-kind.md"
        path.write_text("```yaml\nkind: unknown\n```\n")
        parsed = parse_note(path, "lists")
    else:
        path = tmp_path / "unknown-override.md"
        path.write_text(
            (FIXTURES / "radar-screens.example.md").read_text().replace(
                "  example_session_scan:\n", "  unknown_override:\n"
            )
        )
        parsed = parse_note(path, "screens")
    error = scrub("; ".join(parsed.errors))
    assert expected in error


@pytest.mark.parametrize(("ft", "expected"), [(None, None), (4, 4)])
def test_ft_absent_and_present_matrix(tmp_path, ft, expected):
    text = (FIXTURES / "radar-screens.example.md").read_text()
    if ft is not None:
        text = text.replace(
            "columns: [0, 1, 2, 3, 4, 5]\n",
            f"columns: [0, 1, 2, 3, 4, 5]\nft: {ft}\n",
        )
    path = tmp_path / "screens.md"
    path.write_text(text)
    parsed = parse_note(path, "screens")
    assert parsed.ok, [scrub(error) for error in parsed.errors]
    screen = next(x.block for x in parsed.blocks if isinstance(x.block, ScreenBlock))
    assert screen.ft == expected


def test_over_budget_refusal_names_field_and_computed_numbers():
    parsed = _loaded(FIXTURES / "radar-screens.example.md", rpm=1)
    error = scrub(parsed.pool_error or "")
    assert parsed.frozen
    assert "pool budget exceeded" in error
    assert "planned_rpm=" in error
    assert "finviz_max_rpm=1" in error
    assert "cap=" in error


def test_mirror_replaces_old_block_with_parse_failed_status(tmp_path):
    broken = tmp_path / "screens.md"
    broken.write_text((FIXTURES / "radar-screens.example.md").read_text().replace(
        "f: exch_nasd,sh_avgvol_o500", "f: forbidden=value"))
    parsed = load_sources(broken, FIXTURES / "radar-lists.example.md",
        scan_interval=60, poll_interval=60, finviz_max_rpm=100, list_chunk_size=50)

    class Store:
        def __init__(self):
            self.sent = None
        def values(self):
            return {"radar.screen.old": {"note_sha256": "old", "status": "ok"}}
        def put(self, rows, *, source, before_commit=None):
            self.sent = rows
            if before_commit:
                before_commit()
            return {key: "updated" for key in rows}

    store = Store()
    mirror_sources(parsed, store=store, now=MIRROR_NOW)
    assert store.sent["radar.note.screens"]["status"] == "parse_failed"
    assert store.sent["radar.screen.old"]["status"] == "removed"
