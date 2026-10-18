"""F23 card 503 row P6: the `com.cobalt.playbook` registry row and its one config file.

The plist <-> registry parity (`tests/cobalt/test_jobs.py`
`TestTheShippedRegistry`) is generic and covers `ops/com.cobalt.playbook.plist`
unchanged; these two tests pin what is particular to this job.
"""

from __future__ import annotations

from cobalt.jobs.config import load_job_registry
from cobalt.jobs.models import JobKind

PLAYBOOK_YAML = "configs/cobalt/playbook.yaml"


def test_the_row_is_a_sunday_1730_one_shot():
    spec = load_job_registry().spec("com.cobalt.playbook")
    assert spec.kind is JobKind.ONE_SHOT
    assert spec.schedule is not None and spec.schedule.at == "17:30"
    assert spec.schedule.weekdays == [0]
    assert spec.enabled is True
    assert spec.reads == []


def test_playbook_yaml_is_read_by_the_one_shot_only():
    registry = load_job_registry()
    entry = registry.no_resident_read(PLAYBOOK_YAML)
    assert entry is not None, f"{PLAYBOOK_YAML} is not declared under no_resident_reads"
    assert entry.readers == ["com.cobalt.playbook"]
    assert "playbook/cli.py:" in entry.because
    assert registry.readers_of(PLAYBOOK_YAML) == []
