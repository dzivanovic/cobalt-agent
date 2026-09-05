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

    def test_both_legs_are_off_today(self):
        """2026-09-04: no SSD is mounted and no B2 credential exists.

        If someone arms a leg, this test fails and MUST be updated in the
        same commit — that is the point. Arming a backup is a change worth
        noticing, not a config typo nobody reviews.
        """
        cfg = load_backup_config()
        assert cfg.armed == [], "a destination was armed — see backup.yaml's header"
        assert {d.name for d in cfg.destinations} == {"ssd", "b2"}

    def test_enabled_without_a_repo_is_refused(self):
        with pytest.raises(ValueError, match="nowhere to write"):
            Destination(name="ssd", kind="local", repo="", enabled=True)

    def test_enabled_with_a_repo_is_fine(self):
        d = Destination(name="ssd", kind="local", repo="/Volumes/X/restic", enabled=True)
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


class TestStagingPath:
    def test_the_dump_has_one_stable_path(self):
        """Found by the first restore drill (2026-09-04): with
        `tempfile.mkdtemp()` the database landed at a different random
        path in every snapshot, so `restic restore --include` had no
        path anyone could type. Regression-pinned here."""
        assert STAGING == Path.home() / "cobalt-backups" / "staging"
        assert "tmp" not in str(STAGING).split("/")[1:3]

    def test_probe_is_red_and_explicit_when_nothing_is_armed(self):
        """`unknown` (`??`) is for a probe that could not RUN. A config
        declaring no destination ran fine; the answer is simply bad."""
        from cobalt.heartbeat.probes import backup_freshness

        p = backup_freshness()
        assert p.ok is False
        assert p.unknown is False
        assert "NO DESTINATION ARMED" in p.detail
