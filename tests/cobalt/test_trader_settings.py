"""`"user".trader_settings` — the trader's own numbers (ADR-0008 D3.4).

THE REVISION-3 PROOF LIVES HERE. Before `configs/cobalt/aset.yaml` and
`daymode.yaml` could be deleted, one thing had to be true and provable:
what the runtime now reads out of the database is, field for field, what
those files said. `test_from_db_equals_from_yaml` is that assertion, and
it keeps being that assertion afterwards by reading the files out of git
— the same trick the taxonomy migration uses for its own deleted inputs.

Everything else here is the shape of the move: seven rows, one per
top-level setting, each with its own source and date; an empty table is a
loud failure and not a set of invented defaults; and a load is a
transaction, so a settings table can never be half a config.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest
import yaml

from cobalt.db import Side
from cobalt.settings import (
    SETTING_KEYS,
    TraderSettings,
    TraderSettingsError,
    TraderSettingsStore,
)
from cobalt.settings.models import ASET_FILENAME, DAYMODE_FILENAME

pytestmark = pytest.mark.skipif(
    not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER")),
    reason="requires_db: trader settings integration needs cobalt_dev",
)

REPO_ROOT = Path(__file__).resolve().parents[2]

#: The revision the two YAMLs were last committed at. The proof reads
#: them from here so it survives their deletion — see the module
#: docstring. Resolved at runtime so a rebase cannot stale it.
def _seed_texts() -> dict[str, str]:
    out = {}
    for name in (ASET_FILENAME, DAYMODE_FILENAME):
        path = REPO_ROOT / "configs" / "cobalt" / name
        if path.exists():
            out[name] = path.read_text(encoding="utf-8")
            continue
        rev = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--", f"configs/cobalt/{name}"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=False,
        ).stdout.strip()
        assert rev, f"no history for configs/cobalt/{name}"
        out[name] = subprocess.run(
            ["git", "show", f"{rev}^:configs/cobalt/{name}"],
            cwd=REPO_ROOT, capture_output=True, text=True, check=False,
        ).stdout
    return out


@pytest.fixture
def store():
    """An EMPTY table, inside the suite's rollback transaction.

    `cobalt_dev` legitimately holds this trader's seeded settings — the
    directory fixture wraps every test in a transaction it never commits,
    so clearing them here is invisible outside the test and makes
    `created` / `updated` / `unchanged` mean what they say.
    """
    s = TraderSettingsStore("cobalt_dev")
    s.ensure_schema()
    with s._connect() as conn:
        conn.execute("DELETE FROM trader_settings")
    return s


@pytest.fixture
def seeded(store):
    store.put(TraderSettings.rows_from_yaml(texts=_seed_texts()), source="test")
    return store


class TestShape:
    def test_the_store_is_user_side(self):
        assert TraderSettingsStore.SIDE is Side.USER

    def test_seven_rows_one_per_top_level_setting(self, seeded):
        assert sorted(seeded.values()) == sorted(SETTING_KEYS)
        assert len(SETTING_KEYS) == 7

    def test_every_row_carries_its_own_source_and_date(self, seeded):
        for row in seeded.rows():
            assert row["source"] == "test"
            assert row["updated_at"] is not None
            assert row["user_id"] == 1 if "user_id" in row else True

    def test_user_id_defaults_to_the_tenant_guc(self, seeded):
        with seeded._connect() as conn:
            ids = {r[0] for r in conn.execute("SELECT user_id FROM trader_settings")}
        assert ids == {1}


class TestRevisionThreeProof:
    def test_from_db_equals_from_yaml(self, seeded):
        """The proof the YAML deletion was gated on."""
        from_db = TraderSettings.from_db(seeded)
        from_yaml = TraderSettings.from_yaml(texts=_seed_texts())
        assert from_db.diff(from_yaml) == {}
        assert from_db.sheet_modes == from_yaml.sheet_modes
        assert from_db.daymode == from_yaml.daymode
        assert from_db == from_yaml

    def test_the_diff_is_not_vacuous(self, seeded):
        """A changed setting DOES show up — otherwise the proof above
        would pass on two objects that were never compared."""
        rows = TraderSettings.rows_from_yaml(texts=_seed_texts())
        rows["daymode.enabled_modes"] = ["reduced", "half"]
        other = TraderSettings._build(rows, where="test")
        diff = TraderSettings.from_db(seeded).diff(other)
        assert set(diff) == {"daymode.enabled_modes"}


class TestFailLoud:
    def test_an_empty_table_names_the_command(self, store):
        with store._connect() as conn:
            conn.execute("DELETE FROM trader_settings")
        with pytest.raises(TraderSettingsError, match="cobalt settings load"):
            TraderSettings.from_db(store)

    def test_a_missing_setting_is_named(self, seeded):
        with seeded._connect() as conn:
            conn.execute("DELETE FROM trader_settings WHERE key = 'daymode.stepdowns'")
        with pytest.raises(TraderSettingsError, match="daymode.stepdowns"):
            TraderSettings.from_db(seeded)

    def test_the_loaders_surface_it_as_a_config_error(self, store):
        from cobalt.aset.config import ConfigError, load_sheet_modes_config
        from cobalt.daymode.config import load_daymode_config

        with store._connect() as conn:
            conn.execute("DELETE FROM trader_settings")
        with pytest.raises(ConfigError, match="cobalt settings load"):
            load_sheet_modes_config()
        with pytest.raises(ConfigError, match="cobalt settings load"):
            load_daymode_config()


class TestPut:
    def test_it_reports_what_actually_moved(self, store):
        rows = TraderSettings.rows_from_yaml(texts=_seed_texts())
        first = store.put(rows, source="a")
        assert set(first.values()) <= {"created", "updated"}
        again = store.put(rows, source="b")
        assert set(again.values()) == {"unchanged"}

    def test_an_unchanged_row_keeps_its_source(self, store):
        rows = TraderSettings.rows_from_yaml(texts=_seed_texts())
        store.put(rows, source="original")
        store.put(rows, source="second-run")
        sources = {r["source"] for r in store.rows()}
        assert sources == {"original"}, "an unchanged value must not be re-dated"

    def test_a_changed_row_takes_the_new_source(self, store):
        rows = TraderSettings.rows_from_yaml(texts=_seed_texts())
        store.put(rows, source="original")
        rows["daymode.enabled_modes"] = ["reduced", "half"]
        store.put(rows, source="ruling")
        by_key = {r["key"]: r for r in store.rows()}
        assert by_key["daymode.enabled_modes"]["source"] == "ruling"
        assert by_key["daymode.stepdowns"]["source"] == "original"


class TestTheLoadersReadTheDatabase:
    def test_sheet_modes_comes_from_the_rows(self, seeded):
        from cobalt.aset.config import load_sheet_modes_config

        with seeded._connect() as conn:
            conn.execute(
                "UPDATE trader_settings SET value = %s::jsonb WHERE key = %s",
                (json.dumps(["A", "B", "C"]), "aset.enabled_grades"),
            )
        assert [g.value for g in load_sheet_modes_config().enabled_grades] == [
            "A", "B", "C"
        ]

    def test_daymode_comes_from_the_rows(self, seeded):
        from cobalt.daymode.config import load_daymode_config

        with seeded._connect() as conn:
            conn.execute(
                "UPDATE trader_settings SET value = %s::jsonb WHERE key = %s",
                (json.dumps("{sheet}-keys.htk"), "daymode.hotkey_file_template"),
            )
        assert load_daymode_config().hotkey_file_template == "{sheet}-keys.htk"

    def test_the_two_halves_still_validate_against_each_other(self, seeded):
        """`reduced_enabled_grades` may narrow the account ladder, never
        widen it — the check survived the move out of YAML."""
        from cobalt.aset.config import ConfigError
        from cobalt.daymode.config import load_daymode_config

        with seeded._connect() as conn:
            conn.execute(
                "UPDATE trader_settings SET value = %s::jsonb WHERE key = %s",
                (json.dumps(["B"]), "aset.enabled_grades"),
            )
        with pytest.raises(ConfigError, match="WIDEN"):
            load_daymode_config()


def test_the_yaml_reader_is_seeding_only():
    """`from_yaml` must not be reachable from the runtime path."""
    import cobalt.aset.config as aset_config
    import cobalt.daymode.config as daymode_config

    for module in (aset_config, daymode_config):
        source = Path(module.__file__).read_text()
        assert "from_yaml" not in source, (
            f"{module.__name__} reaches for the seeding reader — the runtime path "
            "reads the database and nothing else (ADR-0008 D3.4)."
        )
    # `aset.config.load_config()` still reads a YAML, and correctly so:
    # the daily-note folder, the bind address and the typo ceilings are
    # INSTALL settings, not the trader's trading rules.
    assert "yaml.safe_load" not in Path(daymode_config.__file__).read_text()
