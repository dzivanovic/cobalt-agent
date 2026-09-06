"""Backup config + mechanism (RULED 2026-09-04: restic -> B2 + SSD).

The restic binary is NOT exercised here — these tests pin the decisions
that a future edit could quietly undo: that an armed destination must
have a repository, that a run with nothing armed REFUSES rather than
exiting 0, that the ruled retention numbers are the ones sent to
`forget`, and that the database dump has one stable path inside every
snapshot (the defect the first restore drill found).
"""

from __future__ import annotations

from pathlib import Path

import pytest

from cobalt.backup.config import (
    BackupConfig,
    BackupConfigError,
    DatabaseSpec,
    Destination,
    ForgetPolicy,
    load_backup_config,
)
from cobalt.backup import restic
from cobalt.backup.restic import STAGING, BackupError


def _cfg(**over) -> BackupConfig:
    base = dict(
        sources=[Path("/tmp/vault")],
        database=DatabaseSpec(enabled=True, name="cobalt_brain"),
        excludes=[".DS_Store"],
        destinations=[Destination(name="ssd", kind="local", repo="", enabled=False)],
        password_vault_key="RESTIC_PASSWORD",
        b2_key_id_vault_key="B2_ACCOUNT_ID",
        b2_app_key_vault_key="B2_ACCOUNT_KEY",
        forget=ForgetPolicy(daily=14, weekly=8, monthly=12),
    )
    base.update(over)
    return BackupConfig(**base)


class TestConfig:
    def test_shipped_config_loads(self):
        """The committed file is valid — config-as-code, validated on load."""
        cfg = load_backup_config()
        assert cfg.forget.daily == 14 and cfg.forget.weekly == 8 and cfg.forget.monthly == 12

    def test_the_ssd_is_armed_and_b2_is_not(self):
        """ARMED 2026-09-05, SSD leg only. Was `both legs are off`.

        This test exists to make arming or disarming a backup a change
        someone has to write down, not a config typo nobody reviews. If
        the B2 leg comes on, this fails and MUST be updated in the same
        commit — same as when the SSD leg did.
        """
        cfg = load_backup_config()
        assert [d.name for d in cfg.armed] == ["ssd"]
        assert {d.name for d in cfg.destinations} == {"ssd", "b2"}
        ssd = next(d for d in cfg.destinations if d.name == "ssd")
        assert ssd.repo == "/Volumes/COBALT-BACKUP/restic"
        assert ssd.requires_mount == "/Volumes/COBALT-BACKUP"

    def test_a_removable_repo_must_declare_its_mount(self):
        """The guard that keeps an unplugged disk from being 'backed up'
        to a same-named directory on the boot disk."""
        with pytest.raises(ValueError, match="declares no `requires_mount`"):
            Destination(name="ssd", kind="local", repo="/Volumes/X/restic", enabled=True)

    def test_the_mount_must_actually_contain_the_repo(self):
        with pytest.raises(ValueError, match="is not under"):
            Destination(name="ssd", kind="local", repo="/Volumes/X/restic",
                        requires_mount="/Volumes/Y", enabled=True)

    def test_a_non_removable_local_repo_needs_no_mount(self):
        d = Destination(name="local", kind="local", repo="/srv/restic", enabled=True)
        assert d.requires_mount == "" and d.mount_ok is True

    def test_enabled_without_a_repo_is_refused(self):
        with pytest.raises(ValueError, match="nowhere to write"):
            Destination(name="ssd", kind="local", repo="", enabled=True)

    def test_enabled_with_a_repo_is_fine(self):
        d = Destination(name="ssd", kind="local", repo="/Volumes/X/restic",
                        requires_mount="/Volumes/X", enabled=True)
        assert d.restic_repo() == "/Volumes/X/restic"

    def test_b2_repo_gets_its_scheme(self):
        d = Destination(name="b2", kind="b2", repo="bucket:/path", enabled=True)
        assert d.restic_repo() == "b2:bucket:/path"

    def test_duplicate_destination_names_are_refused(self):
        with pytest.raises(ValueError, match="duplicate destination"):
            _cfg(destinations=[
                Destination(name="ssd", kind="local"),
                Destination(name="ssd", kind="b2"),
            ])

    def test_missing_file_crashes_rather_than_defaulting(self, tmp_path):
        with pytest.raises(BackupConfigError, match="no built-in default"):
            load_backup_config(tmp_path / "nope.yaml")

    def test_unknown_key_is_refused(self, tmp_path):
        p = tmp_path / "backup.yaml"
        p.write_text("backup:\n  sources: [/tmp]\n  wat: 1\n")
        with pytest.raises(BackupConfigError):
            load_backup_config(p)


class TestForgetPolicy:
    def test_the_ruled_numbers_reach_restic(self):
        assert ForgetPolicy(daily=14, weekly=8, monthly=12).restic_args() == [
            "--keep-daily", "14", "--keep-weekly", "8", "--keep-monthly", "12",
        ]

    def test_zero_retention_is_refused(self):
        with pytest.raises(ValueError):
            ForgetPolicy(daily=0, weekly=8, monthly=12)


class TestSnapshotRefusals:
    def test_no_armed_destination_refuses_rather_than_exiting_zero(self):
        """The failure this whole design exists to prevent: a nightly job
        that runs, writes nothing, and reports success."""
        with pytest.raises(BackupError, match="no backup destination is enabled"):
            restic.snapshot(_cfg())

    def test_refusal_happens_before_any_dump(self, monkeypatch):
        """Nothing is dumped for a run that cannot store it — a 360 MB
        dump written and thrown away is a real cost, and on a laptop it
        is a real disk-space incident."""
        called = []
        monkeypatch.setattr(restic, "dump_database", lambda *a, **k: called.append(a))
        with pytest.raises(BackupError):
            restic.snapshot(_cfg())
        assert called == []


class TestMountGuard:
    """The unplugged-disk case. `os.path.ismount`, not `exists`: with the
    SSD out, /Volumes/COBALT-BACKUP is a path restic, mkdir and the shell
    will all cheerfully create ON THE BOOT DISK — a run that exits 0,
    reports green, and protects nothing."""

    def _armed(self, tmp_path):
        return _cfg(destinations=[Destination(
            name="ssd", kind="local", repo=f"{tmp_path}/restic",
            requires_mount=str(tmp_path), enabled=True)])

    def test_an_unmounted_destination_refuses_and_names_the_mount(self, tmp_path):
        cfg = self._armed(tmp_path)          # tmp_path exists but is not a mount
        with pytest.raises(BackupError, match="is NOT MOUNTED") as e:
            restic.snapshot(cfg)
        assert str(tmp_path) in str(e.value)

    def test_it_refuses_before_any_dump(self, tmp_path, monkeypatch):
        """Same rule as the zero-armed refusal: nothing is dumped for a
        run that has nowhere to put it, and the operator hears 'plug the
        disk in' in the first second rather than six minutes later."""
        called = []
        monkeypatch.setattr(restic, "dump_database", lambda *a, **k: called.append(a))
        with pytest.raises(BackupError, match="is NOT MOUNTED"):
            restic.snapshot(self._armed(tmp_path))
        assert called == []

    def test_it_never_falls_back_to_another_destination(self, tmp_path):
        """No 'best effort'. An unmounted disk fails the whole run."""
        cfg = self._armed(tmp_path)
        assert cfg.armed[0].mount_ok is False
        with pytest.raises(BackupError):
            restic.snapshot(cfg)

    def test_a_mounted_destination_passes_the_guard(self):
        d = Destination(name="ssd", kind="local", repo="/restic",
                        requires_mount="/", enabled=True)
        assert d.mount_ok is True
        restic.require_mounted(d)   # does not raise

    def test_the_probe_reports_the_unmounted_mount_by_name(self, tmp_path, monkeypatch):
        """A beat that said only `BackupError` would send someone to read
        a log to learn they need to plug a disk in."""
        from cobalt.heartbeat import probes as probe_mod

        cfg = self._armed(tmp_path)
        monkeypatch.setattr("cobalt.backup.config.load_backup_config", lambda *a, **k: cfg)
        monkeypatch.setattr(probe_mod, "_tunable", lambda k: 1560)
        p = probe_mod.backup_freshness()
        assert p.ok is False
        assert "NOT MOUNTED" in p.detail and str(tmp_path) in p.detail


class TestStagingPath:
    def test_the_dump_has_one_stable_path(self):
        """Found by the first restore drill (2026-09-04): with
        `tempfile.mkdtemp()` the database landed at a different random
        path in every snapshot, so `restic restore --include` had no
        path anyone could type. Regression-pinned here."""
        assert STAGING == Path.home() / "cobalt-backups" / "staging"
        assert "tmp" not in str(STAGING).split("/")[1:3]

    def test_probe_is_red_and_explicit_when_nothing_is_armed(self, monkeypatch):
        """`unknown` (`??`) is for a probe that could not RUN. A config
        declaring no destination ran fine; the answer is simply bad.

        Against a CONSTRUCTED unarmed config since 2026-09-05, because
        the shipped one now arms the SSD."""
        from cobalt.heartbeat import probes as probe_mod

        monkeypatch.setattr("cobalt.backup.config.load_backup_config",
                            lambda *a, **k: _cfg())
        p = probe_mod.backup_freshness()
        assert p.ok is False
        assert p.unknown is False
        assert "NO DESTINATION ARMED" in p.detail
