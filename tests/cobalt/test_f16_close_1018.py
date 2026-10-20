"""F16 close: `validate` builds the F23 and F4 families; the engine loader refuses a row with no consumer.

No DB: the fixture removes the Postgres settings and stubs `cli.taxonomy_validate.main`.
Each refusal test builds its own file under `tmp_path` (nothing is read from `trader_settings`).
"""

from __future__ import annotations

import argparse
import sys

import pytest
from pydantic import ValidationError

from cobalt import cli
from cobalt.playbook import config as playbook_config
from cobalt.playbook.config import PlaybookConfigError
from cobalt.prefill import config as prefill_config
from cobalt.prefill.config import PrefillConfigError
from cobalt.taxonomy.loader import TaxonomyConfigError, load_tunables

_DB_SETTINGS = ("POSTGRES_HOST", "COBALT_DB_USER", "COBALT_DB_PASSWORD", "POSTGRES_PORT")

_NO_CONSUMER_KEY = "test.f16.no_consumer"


@pytest.fixture(autouse=True)
def _no_db_settings(monkeypatch):
    for name in _DB_SETTINGS:
        monkeypatch.delenv(name, raising=False)
    # The taxonomy validator reads a vault (L28); it is not this card's check.
    monkeypatch.setattr(cli.taxonomy_validate, "main", lambda: 0)


def test_v1_validate_refuses_a_bad_playbook_config(monkeypatch, tmp_path):
    bad = tmp_path / "playbook.yaml"
    bad.write_text(
        "latest_per_family: null\n"
        "rows_per_slide: 8\n"
        "why_max_chars: 120\n"
        "out_dir: data/playbook\n"
        "unknown_key: 1\n"
    )
    real = playbook_config.load_playbook_config
    monkeypatch.setattr(playbook_config, "load_playbook_config", lambda: real(bad))
    with pytest.raises((ValidationError, PlaybookConfigError, SystemExit)):
        cli._cmd_validate(argparse.Namespace(no_db=True))


def test_v1_validate_prints_the_playbook_line_and_leaves_pptx_unloaded(monkeypatch, capsys):
    # Unload pptx and the playbook modules that import it, so the assert runs
    # whatever an earlier test loaded (check O2); monkeypatch puts them back.
    import cobalt.playbook as playbook_pkg

    for name in [m for m in sys.modules if m == "pptx" or m.startswith("pptx.")]:
        monkeypatch.delitem(sys.modules, name)
    for sub in ("deck", "data"):
        monkeypatch.delitem(sys.modules, f"cobalt.playbook.{sub}", raising=False)
        monkeypatch.delattr(playbook_pkg, sub, raising=False)
    cli._cmd_validate(argparse.Namespace(no_db=True))
    out = capsys.readouterr().out
    assert any(line.startswith("Playbook (F23): ") for line in out.splitlines())
    assert "pptx" not in sys.modules


def test_v2_validate_refuses_a_bad_daily_refresh(monkeypatch, tmp_path):
    bad = tmp_path / "prefill.yaml"
    bad.write_text(
        "daily_refresh:\n"
        "  units: [trading/market_table, market_calendar/market_calendar]\n"
        "  fields: {SPY: cobalt, QQQ: cobalt, IWM: cobalt, VIX: cobalt, BTC: manual}\n"
    )
    real = prefill_config.load_daily_refresh_config
    monkeypatch.setattr(prefill_config, "load_daily_refresh_config", lambda: real(bad))
    with pytest.raises((PrefillConfigError, SystemExit)):
        cli._cmd_validate(argparse.Namespace(no_db=True))


def test_v2_validate_prints_the_daily_refresh_line(capsys):
    cli._cmd_validate(argparse.Namespace(no_db=True))
    out = capsys.readouterr().out
    assert any(line.startswith("Daily refresh (F4): ") for line in out.splitlines())


def test_c1_a_row_with_no_consumer_is_refused(tmp_path):
    bad = tmp_path / "tunables.yaml"
    bad.write_text(
        "tunables:\n"
        "  - key: test.f16.with_consumer\n"
        "    unit: count\n"
        "    scope: global\n"
        "    dynamic: false\n"
        "    status: proposed\n"
        "    source: dwv\n"
        "    consumers: [x]\n"
        "  - key: test.f16.no_consumer\n"
        "    unit: count\n"
        "    scope: global\n"
        "    dynamic: false\n"
        "    status: proposed\n"
        "    source: dwv\n"
    )
    with pytest.raises(TaxonomyConfigError, match=_NO_CONSUMER_KEY):
        load_tunables(bad)


def test_c1_a_row_whose_consumers_are_blank_is_refused(tmp_path):
    bad = tmp_path / "tunables.yaml"
    bad.write_text(
        "tunables:\n"
        "  - key: test.f16.blank_consumer\n"
        "    unit: count\n"
        "    scope: global\n"
        "    dynamic: false\n"
        "    status: proposed\n"
        "    source: dwv\n"
        "    consumers: [\"\", \"  \"]\n"
    )
    with pytest.raises(TaxonomyConfigError, match="test.f16.blank_consumer"):
        load_tunables(bad)


def test_c1_the_engine_registry_loads():
    registry = load_tunables()
    assert registry.tunables
