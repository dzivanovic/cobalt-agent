"""Truthful all-source validation command and archiver diff status."""

import argparse
from pathlib import Path

import pytest

from cobalt.radar import sources as sources_module
from cobalt.radar.notes import RadarNoteError, load_sources

FIXTURES = Path("tests/fixtures/radar")


def _parsed(tmp_path, *, valid=True):
    screens = tmp_path / "screens.md"
    screens.write_bytes((FIXTURES / "radar-screens.example.md").read_bytes())
    if not valid:
        screens.write_text(screens.read_text().replace("cap: 5", "cap: 500"))
    return load_sources(
        screens,
        FIXTURES / "radar-lists.example.md",
        scan_interval=90,
        poll_interval=90,
        finviz_max_rpm=45,
        list_chunk_size=50,
        context_tickers=0,
    )


def test_sources_reports_both_notes_pool_budget_and_targets(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(sources_module, "configured_sources", lambda: _parsed(tmp_path))
    sources_module.command(argparse.Namespace(archiver_diff=False, json=False, yaml_rev="HEAD"))
    output = capsys.readouterr().out
    assert "screens.md" in output
    assert "radar-lists.example.md" in output
    assert "planned rpm:" in output
    assert "archive targets:" in output


def test_sources_refuses_invalid_pool_budget(tmp_path, monkeypatch):
    monkeypatch.setattr(
        sources_module, "configured_sources", lambda: _parsed(tmp_path, valid=False)
    )
    with pytest.raises(RadarNoteError, match="pool budget exceeded"):
        sources_module.command(
            argparse.Namespace(archiver_diff=False, json=False, yaml_rev="HEAD")
        )


def test_sources_refuses_missing_lists_note(tmp_path, monkeypatch):
    parsed = _parsed(tmp_path)
    parsed.lists.missing = True
    parsed.lists.errors = ["Lists note missing"]
    monkeypatch.setattr(sources_module, "configured_sources", lambda: parsed)
    with pytest.raises(RadarNoteError, match="Lists note missing"):
        sources_module.command(
            argparse.Namespace(archiver_diff=False, json=False, yaml_rev="HEAD")
        )


def test_archiver_diff_mismatch_is_nonzero_failure(tmp_path, monkeypatch):
    monkeypatch.setattr(sources_module, "configured_sources", lambda: _parsed(tmp_path))
    monkeypatch.setattr(sources_module, "archiver_diff", lambda *_args: ["- archive AAA i1"])
    with pytest.raises(RadarNoteError, match="archiver diff mismatch"):
        sources_module.command(
            argparse.Namespace(archiver_diff=True, json=False, yaml_rev="HEAD")
        )
