"""`JobSpec.reads` and `cobalt jobs readers` — the RESTARTS line, derived.

THE LAW, ruled three times: 2026-09-04, 2026-09-08 (aset.yaml) and
2026-09-09 (tunables.yaml) — a config-shape change and the restart of
every resident that reads that file are ONE ACTION.

The third ruling is the one that cost something. The 09-08 seat-usage
deploy added a `TunableUnit.WINDOW` row to `tunables.yaml`, and its plan
said "nothing else is restarted". The ASET sheet re-reads that file on
every request, through code that predated the enum value, so from
roughly 19:00 to 07:06 the page he trades beside answered HTTP 200 and
refused every card. The deploy was right about its own job and wrong
about everybody else's — because the list of everybody else lived in
somebody's memory.

Now it lives in the registry, and `cobalt jobs readers` prints it.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest
from pydantic import ValidationError

from cobalt.jobs.config import REPO_ROOT, JobSpec, load_job_registry

SHEET = "com.cobalt.aset"
TUNABLES = "configs/cobalt/taxonomy/tunables.yaml"


class TestTheDerivedRows:
    """Every row is a claim about a specific loader call, measured on the
    request path with an instrumented `open`. See the 09-09 ops report
    for the file:line citations."""

    def test_the_sheet_re_reads_the_tunables_the_0909_deploy_changed(self):
        spec = load_job_registry().spec(SHEET)
        assert TUNABLES in spec.reads, (
            "taxonomy/loader.py:79 (load_tunables) is on the sheet's request path — "
            "this is the row that would have caught the 09-08 deploy"
        )

    def test_the_sheet_re_reads_its_own_config(self):
        spec = load_job_registry().spec(SHEET)
        assert "configs/dev/aset.yaml" in spec.reads, "aset/config.py:134 (load_config)"

    def test_the_dev_only_vault_config_is_NOT_listed(self):
        """`cobalt/vault.py:167` reads `configs/dev/vault.yaml` per
        request in DEV, and never in production — the sheet's plist sets
        COBALT_VAULT_PATH and the resolver returns before the file read.
        A row true only in dev would send an operator to restart the
        sheet for a file production never opens."""
        spec = load_job_registry().spec(SHEET)
        assert "configs/dev/vault.yaml" not in spec.reads

    def test_every_declared_path_exists(self):
        for spec in load_job_registry().jobs:
            for path in spec.reads:
                assert (REPO_ROOT / path).exists(), f"{spec.label}: {path}"

    def test_every_one_shot_leaves_it_empty(self):
        for spec in load_job_registry().jobs:
            if spec.kind.value == "one-shot":
                assert spec.reads == [], (
                    f"{spec.label}: a one-shot re-reads everything every run — "
                    "there is no stale process to restart"
                )

    def test_the_other_residents_declare_it_empty_deliberately(self):
        """An empty list has to be an answer, not an omission — so every
        resident carries the key and the YAML carries the reasoning."""
        text = (REPO_ROOT / "configs" / "cobalt" / "jobs.yaml").read_text()
        for label in (
            "com.cobalt.mainframe", "com.cobalt.obsidian",
            "com.cobalt.agent", "com.cobalt.herdr",
        ):
            spec = load_job_registry().spec(label)
            assert spec.reads == []
        assert text.count("reads:") == 6, "one per resident, none on a one-shot"


class TestTheModelRefusesNonsense:
    def _spec(self, **kw):
        base = dict(
            label="com.cobalt.x", kind="resident", supervisor="launchd",
            timeout_s=300, what="a test",
        )
        return JobSpec(**{**base, **kw})

    def test_a_one_shot_may_not_declare_reads(self):
        with pytest.raises(ValidationError) as exc:
            JobSpec(
                label="com.cobalt.x", kind="one-shot", supervisor="self",
                timeout_s=300, what="a test",
                schedule={"at": "05:15", "weekdays": [1]},
                reads=["configs/cobalt/jobs.yaml"],
            )
        assert "belongs to a RESIDENT" in str(exc.value)

    def test_an_absolute_path_is_refused(self):
        with pytest.raises(ValidationError) as exc:
            self._spec(reads=["/etc/passwd"])
        assert "REPO-RELATIVE" in str(exc.value)

    def test_an_escaping_path_is_refused(self):
        with pytest.raises(ValidationError):
            self._spec(reads=["../../etc/passwd"])

    def test_the_default_is_empty(self):
        assert self._spec().reads == []


class TestReadersOf:
    def test_it_finds_the_sheet(self):
        readers = load_job_registry().readers_of(TUNABLES)
        assert [r.label for r in readers] == [SHEET, "com.cobalt.radar"]

    def test_a_leading_dot_slash_is_the_same_file(self):
        """An operator pastes a path off a `git status` line; a leading
        `./` must not produce an empty answer."""
        readers = load_job_registry().readers_of("./" + TUNABLES)
        assert [r.label for r in readers] == [SHEET, "com.cobalt.radar"]

    def test_an_unknown_path_finds_nothing(self):
        assert load_job_registry().readers_of("configs/cobalt/notify.yaml") == []


class TestTheCommand:
    """Through the real CLI, because the exit code is half the contract."""

    def _run(self, *args):
        return subprocess.run(
            [sys.executable, "-m", "cobalt.cli", "jobs", "readers", *args],
            capture_output=True, text=True, cwd=REPO_ROOT,
            env={**__import__("os").environ, "COBALT_ENV": "dev"},
        )

    def test_a_known_path_exits_zero_with_a_RESTARTS_line(self):
        proc = self._run(TUNABLES)
        assert proc.returncode == 0, proc.stderr
        assert f"RESTARTS: {SHEET} com.cobalt.radar" in proc.stdout
        assert "launchctl kickstart" in proc.stdout

    def test_an_unknown_path_exits_ONE(self):
        """"No resident re-reads this" and "nobody has written down who
        reads this" are different answers, and only one of them means it
        is safe to deploy without a restart."""
        proc = self._run("configs/cobalt/notify.yaml")
        assert proc.returncode == 1
        assert "UNKNOWN PATH" in proc.stderr
        assert "NOT the same as" in proc.stderr
        assert TUNABLES in proc.stderr, "it lists what IS covered"


class TestTheDeployChecklistIsWrittenDown:
    def test_ops_readme_carries_the_law_and_the_command(self):
        text = (REPO_ROOT / "ops" / "README.md").read_text()
        assert "## Deploy checklist" in text
        assert "cobalt jobs readers" in text
        assert "RESTARTS:" in text
