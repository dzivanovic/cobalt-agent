"""F20 C4a — the `com.cobalt.cos` registry row (FINAL §2 jobs row, F-20, F-14, C9; L42).

Built, registered, not handed over: `enabled: false` (jobs.yaml's
`enabled` comment; card DECISION 6). The generic plist parity tests
(`test_jobs.py` TestTheShippedRegistry) cover `ops/com.cobalt.cos.plist`.
"""

from __future__ import annotations

import re
from pathlib import Path

#: DECISION 7 fallback: `cos.poll_interval_s` has no value from any house, so
#: the poll term is this named constant — UNMEASURED; the desk may rule
#: another number.
POLL_FALLBACK_S = 60

JOBS_YAML = Path(__file__).resolve().parents[2] / "configs" / "cobalt" / "jobs.yaml"


def test_the_row_is_a_disabled_self_resident():
    from cobalt.jobs.config import load_job_registry
    from cobalt.jobs.models import JobKind, Supervisor
    from cobalt.taxonomy.loader import load_tunables

    spec = load_job_registry().spec("com.cobalt.cos")
    assert spec.kind is JobKind.RESIDENT and spec.supervisor is Supervisor.SELF
    assert spec.enabled is False
    rows = load_tunables().by_key
    poll = rows["cos.poll_interval_s"].value
    poll = POLL_FALLBACK_S if poll is None else int(poll)
    assert spec.timeout_s > int(rows["cos.turn_timeout_s"].value) + poll
    assert spec.imports == ["cobalt.cos.run"]


def test_every_cos_read_cites_a_loader():
    from cobalt.jobs.config import load_job_registry

    spec = load_job_registry().spec("com.cobalt.cos")
    assert spec.reads, "a resident declares what it re-reads"
    lines = JOBS_YAML.read_text().splitlines()
    start = next(i for i, l in enumerate(lines) if l.strip() == "- label: com.cobalt.cos")
    end = next(i for i in range(start + 1, len(lines)) if lines[i].strip().startswith("- label:")
               or lines[i].strip().startswith("# ----------------"))
    block = lines[start:end]
    for path in spec.reads:
        line = next(l for l in block if f'"{path}"' in l)
        assert re.search(r"#.*\w+\.(py|plist|sh):\d+", line), f"{path}: no loader cite on its line"
