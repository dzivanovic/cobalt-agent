"""`"user".trade_defs` — the loaded copy of the vault's defs (ADR-0008 D3).

Lives in `tests/cobalt/` rather than `tests/taxonomy/` because it needs a
database, and the RULING 7.1d transaction fixture that gives every DB
test a `cobalt_dev` transaction it never commits lives here.

The thing worth testing about this store is `sync()`, and specifically
its DELETE: the vault is the truth and this table is a cache, so a def a
trader removed from their note must stop existing here too. A row that
outlived its note would be a strategy the radar still fires on and the
vault no longer documents.
"""

from __future__ import annotations

import copy
import re
from pathlib import Path

import pytest
import yaml

from cobalt.db import Side
from cobalt.taxonomy.loader import EXAMPLE_NOTE_PATH
from cobalt.taxonomy.store import TradeDefStore
from cobalt.taxonomy.vault_loader import STRATEGIES_DIR, load_vault_trade_defs

EXAMPLE_SLUG = "example-range-break"
EXAMPLE_NAME = "Example Range Break"

_FENCE_RE = re.compile(r"```ya?ml\n(.*?)\n```", re.DOTALL)
_DEF_UNIT_RE = re.compile(
    r"<!-- cobalt:unit trade_def:[^>]*-->\n(.*?)<!-- /cobalt:unit trade_def:", re.DOTALL
)


def _example_text() -> str:
    return EXAMPLE_NOTE_PATH.read_text(encoding="utf-8")


def _write_vault(root: Path, notes: dict[str, str]) -> Path:
    strategies = root / STRATEGIES_DIR
    strategies.mkdir(parents=True, exist_ok=True)
    for name, text in notes.items():
        (strategies / f"{name}.md").write_text(text, encoding="utf-8")
    return root


def _retargeted(slug: str, name: str) -> str:
    """The example note, re-keyed onto another slug (`trade_key` rewrite)."""
    text = _example_text()
    text = text.replace(f"trade_def: {EXAMPLE_SLUG}", f"trade_def: {slug}")
    text = text.replace(f"name: {EXAMPLE_NAME}", f"name: {name}")
    text = text.replace(f"trade_def:{EXAMPLE_SLUG}", f"trade_def:{slug}")
    text = text.replace(f"tunables:{EXAMPLE_SLUG}", f"tunables:{slug}")
    text = text.replace(f"stats:{EXAMPLE_SLUG}", f"stats:{slug}")
    text = text.replace("example_range_break", slug.replace("-", "_"))
    return text


@pytest.fixture
def store():
    s = TradeDefStore("cobalt_dev")
    s.ensure_schema()
    return s


@pytest.fixture
def example_vault(tmp_path):
    return _write_vault(tmp_path / "vault", {EXAMPLE_NAME: _example_text()})


class TestSchema:
    def test_the_store_is_user_side(self):
        assert TradeDefStore.SIDE is Side.USER

    def test_ensure_schema_creates_all_three_objects(self, store):
        with store._connect() as conn:
            tables = {
                r[0]
                for r in conn.execute(
                    "SELECT tablename FROM pg_tables WHERE schemaname = 'user'"
                )
            }
            views = {
                r[0]
                for r in conn.execute(
                    "SELECT viewname FROM pg_views WHERE schemaname = 'user'"
                )
            }
        assert {"trade_defs", "tunables"} <= tables
        assert "setup_trade_matrix" in views

    def test_user_id_defaults_to_the_tenant_guc(self, store, example_vault):
        store.sync(load_vault_trade_defs(example_vault))
        assert store.get(EXAMPLE_SLUG)["user_id"] == 1


class TestSync:
    def test_it_upserts_the_def_and_its_tunables(self, store, example_vault):
        result = load_vault_trade_defs(example_vault)
        counts = store.sync(result)
        assert counts.defs_upserted == 1
        assert counts.tunables_upserted == 1
        assert counts.defs_deleted == 0

        row = store.get(EXAMPLE_SLUG)
        assert row["name"] == EXAMPLE_NAME
        assert row["md5"] == result.defs[0].md5
        assert row["note_path"].endswith(".md")
        assert row["def"]["id"] == EXAMPLE_SLUG      # injected, and persisted
        assert row["def"]["name"] == EXAMPLE_NAME

    def test_a_second_sync_is_idempotent(self, store, example_vault):
        result = load_vault_trade_defs(example_vault)
        store.sync(result)
        counts = store.sync(result)
        assert counts.defs_upserted == 1
        assert counts.defs_deleted == 0
        assert store.slugs() == [EXAMPLE_SLUG]

    def test_a_slug_that_left_the_vault_is_deleted(self, store, tmp_path):
        two = _write_vault(
            tmp_path / "v",
            {
                EXAMPLE_NAME: _example_text(),
                "Second": _retargeted("example-second", "Second"),
            },
        )
        store.sync(load_vault_trade_defs(two))
        assert store.slugs() == ["example-range-break", "example-second"]

        (two / STRATEGIES_DIR / "Second.md").unlink()
        counts = store.sync(load_vault_trade_defs(two))

        assert counts.defs_deleted == 1
        assert counts.deleted_slugs == ["example-second"]
        assert store.slugs() == [EXAMPLE_SLUG]

    def test_deleting_a_def_cascades_to_its_tunables(self, store, tmp_path):
        two = _write_vault(
            tmp_path / "v",
            {
                EXAMPLE_NAME: _example_text(),
                "Second": _retargeted("example-second", "Second"),
            },
        )
        store.sync(load_vault_trade_defs(two))
        assert "example_second.range_duration_band" in store.tunable_keys()

        (two / STRATEGIES_DIR / "Second.md").unlink()
        store.sync(load_vault_trade_defs(two))
        assert "example_second.range_duration_band" not in store.tunable_keys()

    def test_an_edited_note_updates_the_md5_and_the_def(self, store, tmp_path):
        vault = _write_vault(tmp_path / "v", {EXAMPLE_NAME: _example_text()})
        store.sync(load_vault_trade_defs(vault))
        first = store.get(EXAMPLE_SLUG)

        note = vault / STRATEGIES_DIR / f"{EXAMPLE_NAME}.md"
        note.write_text(
            note.read_text().replace("max_attempts: {value: 2", "max_attempts: {value: 3")
        )
        store.sync(load_vault_trade_defs(vault))
        second = store.get(EXAMPLE_SLUG)

        assert second["md5"] != first["md5"]
        assert second["def"]["max_attempts"]["value"] == 3

    def test_syncing_an_empty_vault_empties_the_table(self, store, example_vault):
        store.sync(load_vault_trade_defs(example_vault))
        (example_vault / STRATEGIES_DIR / f"{EXAMPLE_NAME}.md").unlink()
        counts = store.sync(load_vault_trade_defs(example_vault))
        assert counts.defs_deleted == 1
        assert store.slugs() == []

    def test_the_report_names_what_it_deleted(self, store, tmp_path):
        two = _write_vault(
            tmp_path / "v",
            {
                EXAMPLE_NAME: _example_text(),
                "Second": _retargeted("example-second", "Second"),
            },
        )
        store.sync(load_vault_trade_defs(two))
        (two / STRATEGIES_DIR / "Second.md").unlink()
        report = store.sync(load_vault_trade_defs(two)).report()
        assert "example-second" in report
        assert "1 deleted" in report


class TestSetupTradeMatrix:
    def test_the_view_unnests_valid_setups(self, store, example_vault):
        result = load_vault_trade_defs(example_vault)
        store.sync(result)
        rows = store.matrix()
        expected = sorted(
            (EXAMPLE_SLUG, vs.setup_ref.value, vs.relation.value)
            for vs in result.defs[0].definition.valid_setups
        )
        assert rows == expected
        assert len(rows) == 2

    def test_the_view_follows_the_def_with_no_second_write(self, store, tmp_path):
        """It was a second FILE that had to be kept equal; it is a view now,
        so it cannot disagree — editing the def is the only write."""
        vault = _write_vault(tmp_path / "v", {EXAMPLE_NAME: _example_text()})
        store.sync(load_vault_trade_defs(vault))
        assert len(store.matrix()) == 2

        note = vault / STRATEGIES_DIR / f"{EXAMPLE_NAME}.md"
        note.write_text(
            note.read_text().replace(
                "    - {setup_ref: volatility_in_range, relation: with_trend}\n", ""
            )
        )
        store.sync(load_vault_trade_defs(vault))
        assert store.matrix() == [(EXAMPLE_SLUG, "range_break", "with_trend")]


def test_the_def_column_round_trips_the_model(store, example_vault):
    """`def` is JSONB, not a blob: what goes in comes back as the def."""
    from cobalt.taxonomy.trade_def import TradeDef

    result = load_vault_trade_defs(example_vault)
    store.sync(result)
    reloaded = TradeDef(**store.get(EXAMPLE_SLUG)["def"])
    assert reloaded == result.defs[0].definition


def test_the_example_note_and_the_yaml_helper_agree():
    """Guards the fixture itself: if the shipped note's shape changes, the
    helpers in this file must change with it."""
    unit = _DEF_UNIT_RE.search(_example_text())
    assert unit
    fence = _FENCE_RE.search(unit.group(1))
    assert fence
    mapping = yaml.safe_load(fence.group(1))["trade_def"]
    assert "id" not in mapping and "name" not in mapping
    assert copy.deepcopy(mapping) == mapping
