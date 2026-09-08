"""Fixtures for the taxonomy suite — the SYNTHETIC example is the fixture.

Every test in this directory that needs a trade_def builds it from
`configs/cobalt/taxonomy/examples/example_trade_def.md`, the one strategy
note the repo ships (ADR-0008 D3). Before 2026-09-08 these tests read the
13 committed YAMLs, which meant the suite could not run on an install
that had not been handed a trader's strategies — and, more to the point,
meant a trader's strategies were in the repo at all.

`make_vault(...)` builds a throwaway vault: a directory with
`1 - Trading/4 - Strategies/` and whatever notes a test puts in it. The
real vault is never read here — `load_vault_trade_defs(vault_root=...)`
takes the root explicitly for exactly this reason.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Optional

import pytest

from cobalt.taxonomy.vault_loader import STRATEGIES_DIR
from taxonomy_example import EXAMPLE_NAME, example_def_mapping, example_note_text


@pytest.fixture(scope="session")
def example_note() -> str:
    return example_note_text()


@pytest.fixture
def base_trade_def_dict() -> dict[str, Any]:
    """A known-valid `trade_def:` mapping to mutate per bad-fixture test.

    It carries NO `id` and NO `name` — those are injected by
    `TradeDef.from_unit()`, which is the contract these tests exercise.
    """
    return example_def_mapping()


@pytest.fixture
def make_vault(tmp_path):
    """`make_vault({"Note Name": text, ...}) -> vault root Path`."""

    def _make(notes: dict[str, str], *, root: Optional[Path] = None) -> Path:
        vault_root = root or (tmp_path / "vault")
        strategies = vault_root / STRATEGIES_DIR
        strategies.mkdir(parents=True, exist_ok=True)
        for name, text in notes.items():
            (strategies / f"{name}.md").write_text(text, encoding="utf-8")
        return vault_root

    return _make


@pytest.fixture
def example_vault(make_vault, example_note):
    """A vault holding exactly the synthetic example note."""
    return make_vault({EXAMPLE_NAME: example_note})
