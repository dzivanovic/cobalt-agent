"""X29 fixture (card 2026-10-10/242, row A): every experiment conftest that
re-exports the autouse `dev_db_tx` also re-exports `offline_skip_guard`,
the fixture `dev_db_tx` takes as an argument (`tests/cobalt/conftest.py`).
Without it every test of that folder errors at setup. Reads files only;
reaches no database."""

from __future__ import annotations

from pathlib import Path

_EXPERIMENTS = Path(__file__).resolve().parents[1] / "experiments"


def _reexports(source: str, name: str) -> bool:
    return any(line.startswith(f"{name} = ") for line in source.splitlines())


def _aliases(source: str, name: str) -> bool:
    """The re-export binds the fixture itself (`<name> = <module>.<name>`),
    not some other value (check S1)."""
    return any(
        line.startswith(f"{name} = ") and line.rstrip().endswith(f".{name}")
        for line in source.splitlines()
    )


def _conftests_with_dev_db_tx() -> list[Path]:
    return sorted(
        path for path in _EXPERIMENTS.glob("*/conftest.py")
        if _reexports(path.read_text(), "dev_db_tx")
    )


def test_a1_every_dev_db_tx_reexport_carries_offline_skip_guard():
    lacking = [
        path.parent.name for path in _conftests_with_dev_db_tx()
        if not _aliases(path.read_text(), "offline_skip_guard")
    ]
    assert not lacking, (
        f"experiment conftests re-export dev_db_tx without offline_skip_guard: {lacking}"
    )


def test_a2_the_check_sees_at_least_five_dev_db_tx_reexports():
    folders = [path.parent.name for path in _conftests_with_dev_db_tx()]
    assert len(folders) >= 5, f"only {folders} re-export dev_db_tx"
    assert "f15_p2" in folders


def test_a1_rejects_a_non_fixture_offline_skip_guard_assignment(monkeypatch):
    import pytest

    victim = _EXPERIMENTS / "stale_score" / "conftest.py"
    real_read_text = Path.read_text

    def mutated_read_text(path, *args, **kwargs):
        source = real_read_text(path, *args, **kwargs)
        if path == victim:
            return source.replace(
                "offline_skip_guard = _conftest.offline_skip_guard",
                "offline_skip_guard = None",
                1,
            )
        return source

    monkeypatch.setattr(Path, "read_text", mutated_read_text)
    with pytest.raises(AssertionError):
        test_a1_every_dev_db_tx_reexport_carries_offline_skip_guard()
