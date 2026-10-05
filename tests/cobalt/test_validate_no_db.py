"""03d P5: `cobalt validate --no-db`.

DEPLOY-HUB STEP-G (d2) runs `validate` from the gate worktree, outside the
dev-DB lock, where no `.env` sits (`reports/s3-d2-probe-2026-10-05.md`
`## CAUSE`). Three checks of `_cmd_validate` read `"user".trader_settings`
through `TraderSettings.from_db()` -> `db._open`: Sheets, the SheetMode
coupling (it reads `sheets.order`), and Day modes. `--no-db` skips those
three and says so, one `SKIPPED (--no-db):` line each (L1); every other
check runs unchanged. These tests open no connection: the Postgres
settings are removed, so any DB read raises `DbConfigError`.
"""

from __future__ import annotations

import argparse
import sys

import pytest

from cobalt import cli
from cobalt.db import DbConfigError

_DB_SETTINGS = ("POSTGRES_HOST", "COBALT_DB_USER", "COBALT_DB_PASSWORD", "POSTGRES_PORT")


@pytest.fixture(autouse=True)
def _no_db_settings(monkeypatch):
    for name in _DB_SETTINGS:
        monkeypatch.delenv(name, raising=False)
    # The taxonomy validator reads a vault (L28); it is not this card's check.
    monkeypatch.setattr(cli.taxonomy_validate, "main", lambda: 0)


def _skipped_lines(out: str) -> list[str]:
    return [line for line in out.splitlines() if line.startswith("SKIPPED (--no-db):")]


def test_no_db_skips_the_db_checks_and_exits_clean(capsys):
    assert cli._cmd_validate(argparse.Namespace(no_db=True)) is None

    out = capsys.readouterr().out
    skipped = _skipped_lines(out)
    assert len(skipped) == 3, skipped
    assert "Sheets" in skipped[0]
    assert "SheetMode coupling" in skipped[1]
    assert "Day modes" in skipped[2]
    assert not any(line.startswith("Sheets:") for line in out.splitlines())
    assert not any(line.startswith("Day modes:") for line in out.splitlines())
    # the checks that read files only still ran
    assert "Placement (docs/PLACEMENT.md): tree clean." in out
    assert "Jobs (F17):" in out


def test_without_the_flag_validate_still_reads_the_db(capsys):
    with pytest.raises(DbConfigError):
        cli._cmd_validate(argparse.Namespace(no_db=False))
    assert _skipped_lines(capsys.readouterr().out) == []


def test_no_db_still_fails_a_config_error_it_does_not_skip(monkeypatch, capsys):
    import importlib

    # `cobalt.daymode.propose` as a dotted string resolves to the package's
    # `propose` FUNCTION, so the module is patched as an object.
    propose_mod = importlib.import_module("cobalt.daymode.propose")

    def _bad_band(lo, hi):
        raise propose_mod.BandError("constructed band error")

    monkeypatch.setattr(propose_mod, "validate_band", _bad_band)
    with pytest.raises(SystemExit) as exc:
        cli._cmd_validate(argparse.Namespace(no_db=True))
    assert exc.value.code == 1
    assert "FAILED: constructed band error" in capsys.readouterr().out


def test_the_parser_carries_the_flag(monkeypatch):
    seen: list[argparse.Namespace] = []

    def _fake_validate(args):
        seen.append(args)

    monkeypatch.setattr(cli, "_cmd_validate", _fake_validate)
    monkeypatch.setattr(sys, "argv", ["cobalt", "validate", "--no-db"])
    cli.main()
    assert len(seen) == 1
    assert seen[0].no_db is True
    assert seen[0].func is _fake_validate

    seen.clear()
    monkeypatch.setattr(sys, "argv", ["cobalt", "validate"])
    cli.main()
    assert seen[0].no_db is False
