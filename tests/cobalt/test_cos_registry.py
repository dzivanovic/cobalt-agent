"""F20 C4a — the `com.cobalt.cos` registry row (FINAL §2 jobs row, F-20, F-14, C9; L42).

Built and registered: a self resident. An enabled row has its plist on
disk. The generic plist parity tests (`test_jobs.py` TestTheShippedRegistry)
cover `ops/com.cobalt.cos.plist`.
"""

from __future__ import annotations

import json
import re
from datetime import date, datetime, timezone
from pathlib import Path

#: DECISION 7 fallback: `cos.poll_interval_s` has no value from any house, so
#: the poll term is this named constant — UNMEASURED; the desk may rule
#: another number.
POLL_FALLBACK_S = 60

REPO_ROOT = Path(__file__).resolve().parents[2]
JOBS_YAML = REPO_ROOT / "configs" / "cobalt" / "jobs.yaml"
COS_LABEL = "com.cobalt.cos"


def test_the_row_is_a_self_resident():
    from cobalt.jobs.config import load_job_registry
    from cobalt.jobs.models import JobKind, Supervisor
    from cobalt.taxonomy.loader import load_tunables

    spec = load_job_registry().spec(COS_LABEL)
    assert spec.kind is JobKind.RESIDENT and spec.supervisor is Supervisor.SELF
    if spec.enabled:
        assert (REPO_ROOT / "ops" / "com.cobalt.cos.plist").is_file()
    rows = load_tunables().by_key
    poll = rows["cos.poll_interval_s"].value
    poll = POLL_FALLBACK_S if poll is None else int(poll)
    assert spec.timeout_s > int(rows["cos.turn_timeout_s"].value) + poll
    assert spec.imports == ["cobalt.cos.run"]


def test_every_cos_read_cites_a_loader():
    from cobalt.jobs.config import load_job_registry

    spec = load_job_registry().spec(COS_LABEL)
    assert spec.reads, "a resident declares what it re-reads"
    lines = JOBS_YAML.read_text().splitlines()
    start = next(i for i, l in enumerate(lines) if l.strip() == "- label: com.cobalt.cos")
    end = next(i for i in range(start + 1, len(lines)) if lines[i].strip().startswith("- label:")
               or lines[i].strip().startswith("# ----------------"))
    block = lines[start:end]
    for path in spec.reads:
        line = next(l for l in block if f'"{path}"' in l)
        assert re.search(r"#.*\w+\.(py|plist|sh):\d+", line), f"{path}: no loader cite on its line"


def _smoke_deps(**overrides):
    from cobalt.smoke.checks import SmokeDeps

    def unexpected(name):
        def fail(*_a, **_k):
            raise AssertionError(f"this test did not expect a {name} call")

        return fail

    values = dict(
        read_rows=unexpected("read_rows"),
        launchctl_print=unexpected("launchctl_print"),
        launchctl_loaded=unexpected("launchctl_loaded"),
        http_get=unexpected("http_get"),
        read_text=unexpected("read_text"),
        run_cli=unexpected("run_cli"),
        job_specs=unexpected("job_specs"),
        drc_note_path=unexpected("drc_note_path"),
        missed_grace=unexpected("missed_grace"),
    )
    values.update(overrides)
    return SmokeDeps(**values)


def _k18(monkeypatch, tmp_path, *, listed):
    """K18 (`registry_match`) over the real registry. The owed file is under tmp_path."""
    from cobalt.jobs import watchdog
    from cobalt.smoke import checks
    from cobalt.smoke.models import LaunchctlCheck, SmokeContext

    path = tmp_path / "data" / "deploy" / "bootstrap-owed.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({lab: {"gate": ["X8"], "card": "constructed"} for lab in listed}))
    monkeypatch.setattr(watchdog, "BOOTSTRAP_OWED_PATH", path, raising=False)
    match = LaunchctlCheck(id="K18", title="drift", kind="launchctl", mode="registry_match",
                           expect_text="no drift")
    now = datetime(2026, 9, 3, 14, 0, tzinfo=timezone.utc)
    day = date(2026, 9, 3)
    context = SmokeContext(
        now=now, report_date=day, session="overnight", cutoff=now,
        last_trading_day=day, last_summary_slot="16:30", last_summary_date=day, prod=True,
    )
    specs = checks.load_job_specs()
    return checks.evaluate(
        match, context,
        _smoke_deps(job_specs=lambda: specs, launchctl_loaded=lambda label: label != COS_LABEL),
    )


def test_k18_reads_cos_as_owed_while_unloaded(monkeypatch, tmp_path):
    from cobalt.smoke.models import Verdict

    out = _k18(monkeypatch, tmp_path, listed=[COS_LABEL])
    assert out.verdict is Verdict.PASS, out.detail
    assert f"OWED (deferred bootstrap): {COS_LABEL}" in out.detail
    # CONTROL: nothing owed, and the label is still unloaded.
    out = _k18(monkeypatch, tmp_path, listed=[])
    assert out.verdict is Verdict.FAIL, out.detail
    assert COS_LABEL in out.detail and "enabled but not loaded" in out.detail
