"""F5 — the four checkpoint jobs, offline (card 731 row K9; FINAL §2.8, [F-13] need 6, [F-14]; L42).

Schedule parity: `prefill.yaml` `checkpoints.slots` = the four `jobs.yaml`
`at` values = the four plists' calendar entries. The generic parity tests
(`test_jobs.py` `TestTheShippedRegistry`) cover each plist's shape.
"""

from __future__ import annotations

import plistlib

from cobalt.jobs.config import load_job_registry

LABELS = [f"com.cobalt.checkpoint-{s}" for s in ("0715", "0745", "0815", "0845")]


def test_four_one_shots_at_the_slot_times():
    registry = load_job_registry()
    specs = [registry.spec(label) for label in LABELS]
    assert [(s.kind.value, s.supervisor.value) for s in specs] == [("one-shot", "self")] * 4
    assert [s.schedule.at for s in specs] == ["07:15", "07:45", "08:15", "08:45"]
    assert all(s.schedule.weekdays == [1, 2, 3, 4, 5] for s in specs)
    assert [s.timeout_s for s in specs] == [300] * 4  # card DECISION 4, UNMEASURED
    labels = [s.label for s in registry.jobs]
    refresh = labels.index("com.cobalt.prefill-refresh")
    assert labels[refresh + 1: refresh + 5] == LABELS, "directly after F4's refresh row"


def test_slots_equal_jobs_ats_equal_plists():
    from cobalt.prefill.config import load_checkpoints_config

    slots = load_checkpoints_config().slots
    registry = load_job_registry()
    ats = [registry.spec(label).schedule.at for label in LABELS]
    plists = []
    for label in LABELS:
        data = plistlib.loads(registry.spec(label).plist_path.read_bytes())
        entries = {(e["Hour"], e["Minute"]) for e in data["StartCalendarInterval"]}
        assert len(entries) == 1 and sorted(e["Weekday"] for e in data["StartCalendarInterval"]) == [1, 2, 3, 4, 5]
        (hour, minute), = entries
        plists.append(f"{hour:02d}:{minute:02d}")
        hhmm = label.rsplit("-", 1)[1]
        assert data["ProgramArguments"][1:] == ["run", "cobalt", "checkpoint", "run", "--slot", hhmm]
        assert data["RunAtLoad"] is False
        assert data["EnvironmentVariables"]["COBALT_VAULT_PATH"] == "/Users/cobalt/Vault/Think"
        assert data["StandardOutPath"].endswith(f"logs/checkpoint-{hhmm}.log")
        assert data["StandardErrorPath"].endswith(f"logs/checkpoint-{hhmm}.err")
    assert slots == ats == plists


def test_the_template_readers_name_the_four():
    entry = load_job_registry().no_resident_read("configs/cobalt/templates/daily.md.j2")
    assert entry.readers == ["com.cobalt.prefill-daily", "com.cobalt.prefill-refresh", *LABELS]
