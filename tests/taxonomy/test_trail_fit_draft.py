"""S2-P2 STEP-8 / R5 — `cobalt cards trail-fit-draft` writes a review draft
only. The `trail_fit` → `source: human` note change is Dejan's to make;
there is no apply path in P2."""

from __future__ import annotations

import argparse
import inspect
from datetime import date

import pytest

from cobalt.cards import cli as cards_cli
from cobalt.cards import trail_fit_draft as draft_module
from taxonomy_example import (
    EXAMPLE_NAME,
    example_def_mapping,
    example_def_yaml,
    example_note_text,
    example_tunables_yaml,
    render_note,
)

TODAY = date(2026, 9, 16)
SLUG = "example-trail-probe"


def _note(item) -> str:
    factors = [*example_def_mapping()["quality_factors"], item]
    return render_note(SLUG, "Example Trail Probe", def_yaml=example_def_yaml(slug=SLUG, quality_factors=factors),
                       tunables_yaml=example_tunables_yaml(SLUG))


def test_trail_fit_draft_never_applied(make_vault, tmp_path):
    vault = make_vault({
        EXAMPLE_NAME: example_note_text(),
        "Example Trail Probe": _note({"name": "trail_fit", "source": "cobalt", "tier": "deterministic"}),
    })
    notes = {p: p.read_bytes() for p in (vault / "1 - Trading/4 - Strategies").glob("*.md")}
    out = tmp_path / "trail-fit-draft.md"
    path = draft_module.write_draft(vault, out, today=TODAY)
    text = path.read_text()
    assert {p: p.read_bytes() for p in notes} == notes  # no note byte moved
    assert "DRAFT" in text and "never applied by Cobalt" in text
    assert SLUG in text and "source: cobalt" in text
    assert "- {name: trail_fit, source: human, tier: deterministic}" in text
    assert EXAMPLE_NAME not in text  # a note without trail_fit has no row
    # no apply path anywhere: the module holds no vault writer, the CLI no apply command
    source = inspect.getsource(draft_module)
    assert "VaultWriter" not in source and "upsert" not in source
    parser = argparse.ArgumentParser()
    cards_cli.add_parser(parser.add_subparsers(dest="group"))
    choices = parser._subparsers._group_actions[0].choices["cards"]._subparsers._group_actions[0].choices
    assert "trail-fit-draft" in choices
    assert not [name for name in choices if "trail" in name and name != "trail-fit-draft"]
    with pytest.raises(draft_module.TrailFitDraftError, match="exists"):
        draft_module.write_draft(vault, out, today=TODAY)


def test_a_note_already_human_says_so_and_no_trail_fit_anywhere_is_loud(make_vault, tmp_path):
    vault = make_vault({"Example Trail Probe": _note({"name": "trail_fit", "source": "human"})})
    draft = draft_module.draft_trail_fit(vault, today=TODAY)
    assert draft.rows[0].proposed is None and draft.rows[0].status == "already source: human"
    empty = make_vault({EXAMPLE_NAME: example_note_text()}, root=tmp_path / "empty")
    with pytest.raises(draft_module.TrailFitDraftError, match="no defined note carries trail_fit"):
        draft_module.draft_trail_fit(empty, today=TODAY)
