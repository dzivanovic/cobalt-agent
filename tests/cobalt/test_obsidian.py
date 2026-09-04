"""RULING 6.3c/3d — the Obsidian-running probe and the writer's ERROR line.

The failure being defended against is 2026-09-04, and it is subtle: the
write SUCCEEDED. `prefill-daily` created `2026-09-04.md` at 05:15 with
118 correct lines and four `vault_writes` rows (525-528). Nothing failed,
nothing logged an error, the run report was green. But no Obsidian
process had run on the Mac since the previous evening's reboot, so those
bytes never reached Sync — and at 06:30 the trading PC's Obsidian
created its own bare template for the same date and Sync carried THAT
back over the top.

A green report for a write nobody will ever see is a plausible-empty
artifact in the fail-loud sense. These tests pin the two halves of the
fix: the probe answers honestly (including "I could not tell"), and a
write with no Obsidian running is reported as ERROR, not NOTE.
"""

import subprocess
from pathlib import Path

import pytest

from cobalt import obsidian
from cobalt.vaultwrite import VaultWriter
from cobalt.vaultwrite.writer import WriteResult


# ---------------------------------------------------------------------
# The probe
# ---------------------------------------------------------------------


class TestProbe:
    def test_reports_running_when_pgrep_finds_pids(self, monkeypatch):
        monkeypatch.setattr(obsidian, "obsidian_pids", lambda: [4242, 4243])
        running, message = obsidian.sync_status()
        assert running is True
        assert "4242" in message

    def test_reports_the_exact_ruling_wording_when_absent(self, monkeypatch):
        monkeypatch.setattr(obsidian, "obsidian_pids", lambda: [])
        running, message = obsidian.sync_status()
        assert running is False
        assert message == "written; Obsidian not running — will not sync"

    def test_pgrep_exit_1_means_not_running_not_broken(self, monkeypatch):
        """Exit 1 is pgrep's documented "no match" — the ONE non-zero
        code that is an answer rather than a failure."""
        monkeypatch.setattr(
            subprocess, "run",
            lambda *a, **k: subprocess.CompletedProcess(a, 1, stdout="", stderr=""),
        )
        assert obsidian.obsidian_pids() == []
        assert obsidian.is_running() is False

    def test_a_broken_probe_raises_and_is_never_reported_as_down(self, monkeypatch):
        """"The probe is broken" and "Obsidian is down" are different
        facts. Collapsing them is how a red condition goes unnoticed."""
        monkeypatch.setattr(
            subprocess, "run",
            lambda *a, **k: subprocess.CompletedProcess(a, 3, stdout="", stderr="boom"),
        )
        with pytest.raises(obsidian.ObsidianProbeError):
            obsidian.obsidian_pids()

    def test_missing_pgrep_raises_rather_than_answering_false(self, monkeypatch):
        monkeypatch.setattr(obsidian.shutil, "which", lambda _: None)
        with pytest.raises(obsidian.ObsidianProbeError, match="pgrep not found"):
            obsidian.obsidian_pids()

    def test_the_real_probe_runs_on_this_machine(self):
        """Not mocked: exercises the actual pgrep call so a change in
        its interface can't pass the suite silently."""
        assert isinstance(obsidian.obsidian_pids(), list)


# ---------------------------------------------------------------------
# The writer's run report
# ---------------------------------------------------------------------


class TestWriterErrorLine:
    def _writer(self):
        return VaultWriter("test.obsidian", store=None, dry_run=True)

    def test_a_write_with_no_obsidian_carries_an_error_line(self, monkeypatch):
        monkeypatch.setattr(obsidian, "obsidian_pids", lambda: [])
        result = WriteResult(path=Path("/x/note.md"), action="created", diff="+a")
        self._writer()._annotate_sync(result)
        assert result.errors == ["written; Obsidian not running — will not sync"]
        assert "  ERROR: written; Obsidian not running — will not sync" in result.report()

    def test_no_error_line_when_obsidian_is_running(self, monkeypatch):
        monkeypatch.setattr(obsidian, "obsidian_pids", lambda: [999])
        result = WriteResult(path=Path("/x/note.md"), action="created", diff="+a")
        self._writer()._annotate_sync(result)
        assert result.errors == []
        assert "ERROR" not in result.report()

    @pytest.mark.parametrize("action", ["unchanged", "skipped", "skipped_exists"])
    def test_a_write_that_wrote_nothing_raises_no_false_alarm(self, monkeypatch, action):
        """No bytes, no delivery problem. A red line here would train
        exactly the wrong reflex."""
        monkeypatch.setattr(obsidian, "obsidian_pids", lambda: [])
        result = WriteResult(path=Path("/x/note.md"), action=action)
        self._writer()._annotate_sync(result)
        assert result.errors == []

    @pytest.mark.parametrize("action", ["created", "updated", "restored"])
    def test_every_byte_producing_action_is_covered(self, monkeypatch, action):
        monkeypatch.setattr(obsidian, "obsidian_pids", lambda: [])
        result = WriteResult(path=Path("/x/note.md"), action=action)
        self._writer()._annotate_sync(result)
        assert result.errors, f"{action} must report the sync condition"

    def test_a_broken_probe_says_unknown_not_not_running(self, monkeypatch):
        def boom():
            raise obsidian.ObsidianProbeError("pgrep exploded")

        monkeypatch.setattr(obsidian, "obsidian_pids", boom)
        result = WriteResult(path=Path("/x/note.md"), action="created")
        self._writer()._annotate_sync(result)
        assert len(result.errors) == 1
        assert "UNKNOWN" in result.errors[0]
        assert "will not sync" not in result.errors[0]

    def test_the_public_write_methods_are_all_decorated(self):
        """The annotation hangs off four entry points rather than ten
        `return WriteResult(...)` sites; if one loses its decorator the
        condition goes unreported for that whole path."""
        for name in ("create_if_absent", "upsert_unit", "upsert_region", "restore"):
            method = getattr(VaultWriter, name)
            assert getattr(method, "__wrapped__", None) is not None, (
                f"VaultWriter.{name} lost its @_reports_sync_status decorator"
            )
