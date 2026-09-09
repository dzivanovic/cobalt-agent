"""`cobalt generated commit` — the three refusals and the one `git add`.

WHY THE COMMAND EXISTS. Three tracked files are rewritten by scheduled
jobs and nothing commits them, so `~/cobalt` — which IS production (R4)
— is permanently dirty. A permanently dirty working tree is one nobody
reads: every deploy starts by squinting at `git status` deciding which
lines are "just the jobs", which is exactly the state in which a real
uncommitted change gets waved through.

Every test drives a REAL git repository in a temp directory, for the
same reason the herdr tests drive a real socket: the whole value of this
command is what it refuses to do to an index, and an index is the one
thing a mock cannot model honestly.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from cobalt.generated import GeneratedConfigError, load_generated_config
from cobalt.generated.committer import (
    GeneratedCommitRefused,
    commit_generated,
)

LISTED = "docs/generated/report.md"
OTHER = "README.md"


def git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args], capture_output=True, text=True
    )
    assert proc.returncode == 0, f"git {args}: {proc.stderr}"
    return proc.stdout


CONFIG = """
files:
  - path: "docs/generated/report.md"
    written_by: "a test"
message: "chore(generated): nightly rewrite {date}"
"""


@pytest.fixture
def repo(tmp_path) -> Path:
    """A real repo on `main`, with one listed file and one unlisted one,
    both committed and both clean."""
    root = tmp_path / "repo"
    (root / "docs" / "generated").mkdir(parents=True)
    (root / "configs" / "cobalt").mkdir(parents=True)

    (root / LISTED).write_text("# the generated report\n\nrow 1\n")
    (root / OTHER).write_text("# a file nothing generates\n")
    (root / "configs" / "cobalt" / "generated.yaml").write_text(CONFIG)

    git(root.parent, "init", "-q", "-b", "main", str(root))
    git(root, "config", "user.email", "scheduler@example.invalid")
    git(root, "config", "user.name", "Test Scheduler")
    git(root, "config", "commit.gpgsign", "false")
    git(root, "add", "-A")
    git(root, "commit", "-q", "-m", "initial")
    return root


def dirty_the_listed_file(repo: Path) -> None:
    (repo / LISTED).write_text("# the generated report\n\nrow 1\nrow 2\n")


class TestTheThreeRefusals:
    """Each one has a victim, and it is always the same person."""

    def test_it_refuses_off_main(self, repo):
        git(repo, "checkout", "-q", "-b", "sprint-2/radar")
        dirty_the_listed_file(repo)

        with pytest.raises(GeneratedCommitRefused) as exc:
            commit_generated(repo, day="2026-09-09")

        assert "not 'main'" in str(exc.value)
        assert "steals a hunk" in str(exc.value)
        assert git(repo, "status", "--porcelain").strip(), "nothing was staged"

    def test_it_refuses_mid_merge(self, repo):
        """The index belongs to the merge. Adding to it mid-flight
        corrupts somebody's work."""
        git_dir = Path(git(repo, "rev-parse", "--absolute-git-dir").strip())
        (git_dir / "MERGE_HEAD").write_text(git(repo, "rev-parse", "HEAD"))
        dirty_the_listed_file(repo)

        with pytest.raises(GeneratedCommitRefused) as exc:
            commit_generated(repo, day="2026-09-09")
        assert "a merge is in progress" in str(exc.value)

    def test_it_refuses_mid_rebase(self, repo):
        git_dir = Path(git(repo, "rev-parse", "--absolute-git-dir").strip())
        (git_dir / "rebase-merge").mkdir()
        dirty_the_listed_file(repo)

        with pytest.raises(GeneratedCommitRefused) as exc:
            commit_generated(repo, day="2026-09-09")
        assert "a rebase is in progress" in str(exc.value)

    def test_it_refuses_mid_cherry_pick(self, repo):
        git_dir = Path(git(repo, "rev-parse", "--absolute-git-dir").strip())
        (git_dir / "CHERRY_PICK_HEAD").write_text(git(repo, "rev-parse", "HEAD"))
        dirty_the_listed_file(repo)

        with pytest.raises(GeneratedCommitRefused) as exc:
            commit_generated(repo, day="2026-09-09")
        assert "a cherry-pick is in progress" in str(exc.value)

    def test_it_refuses_when_something_is_already_staged(self, repo):
        """Somebody is mid-`git add`. This commit would carry their
        half-staged change under a message that says "nightly rewrite",
        and they would find out at review time."""
        (repo / OTHER).write_text("# half-staged work in progress\n")
        git(repo, "add", "--", OTHER)
        dirty_the_listed_file(repo)

        with pytest.raises(GeneratedCommitRefused) as exc:
            commit_generated(repo, day="2026-09-09")

        assert "already staged" in str(exc.value)
        assert OTHER in str(exc.value)
        assert git(repo, "diff", "--cached", "--name-only").split() == [OTHER], (
            "their staged change is exactly as they left it"
        )


class TestTheHappyPath:
    def test_it_commits_only_the_listed_file(self, repo):
        dirty_the_listed_file(repo)
        (repo / OTHER).write_text("# an unlisted file somebody is editing\n")
        (repo / "SCRATCH.md").write_text("an unlisted UNTRACKED file\n")

        outcome = commit_generated(repo, day="2026-09-09")

        assert outcome.committed
        assert outcome.paths == [LISTED]
        assert outcome.message == "chore(generated): nightly rewrite 2026-09-09"

        landed = git(repo, "show", "--pretty=", "--name-only", "HEAD").split("\n")
        assert [p for p in landed if p] == [LISTED]

    def test_it_leaves_every_other_dirty_path_exactly_as_it_found_it(self, repo):
        dirty_the_listed_file(repo)
        (repo / OTHER).write_text("# an unlisted file somebody is editing\n")
        (repo / "SCRATCH.md").write_text("an unlisted UNTRACKED file\n")

        outcome = commit_generated(repo, day="2026-09-09")

        # No .strip() on the lines: the two-character status prefix is
        # the assertion. " M" is modified-not-staged and "??" untracked —
        # exactly the states they were in before the command ran.
        after = sorted(
            line for line in git(repo, "status", "--porcelain").split("\n") if line
        )
        assert after == [" M README.md", "?? SCRATCH.md"], (
            f"the unlisted paths must survive untouched, got {after}"
        )
        assert set(outcome.left_alone) == {OTHER, "SCRATCH.md"}, (
            "and the outcome says which ones it deliberately did not take"
        )

    def test_nothing_to_commit_is_exit_zero_not_an_error(self, repo):
        """The ordinary case on a day nothing was regenerated. A job that
        failed on 'nothing changed' would paint F18 red every quiet
        Sunday."""
        outcome = commit_generated(repo, day="2026-09-09")
        assert outcome.committed is False
        assert outcome.paths == []
        assert "nothing to commit" in outcome.console()

    def test_the_author_is_the_repos_own_identity(self, repo):
        """No `--author`, and no agent trailer: no model wrote those
        bytes, the scheduler did."""
        dirty_the_listed_file(repo)
        commit_generated(repo, day="2026-09-09")

        assert git(repo, "log", "-1", "--format=%an").strip() == "Test Scheduler"
        body = git(repo, "log", "-1", "--format=%B")
        assert "Co-Authored-By" not in body
        assert "Claude" not in body
        assert body.strip() == "chore(generated): nightly rewrite 2026-09-09"

    def test_dry_run_stages_nothing(self, repo):
        dirty_the_listed_file(repo)
        head = git(repo, "rev-parse", "HEAD")

        outcome = commit_generated(repo, day="2026-09-09", dry_run=True)

        assert outcome.committed is False and outcome.paths == [LISTED]
        assert git(repo, "rev-parse", "HEAD") == head
        assert not git(repo, "diff", "--cached", "--name-only").strip()

    def test_a_path_with_a_space_is_handled(self, repo):
        """Two of the three real entries have spaces in them
        (`docs/40 - DevDocs/...`), which is why every git call uses `-z`
        and `--`."""
        spaced = "docs/40 - DevDocs/a report.md"
        (repo / "docs" / "40 - DevDocs").mkdir(parents=True)
        (repo / spaced).write_text("row 1\n")
        (repo / "configs" / "cobalt" / "generated.yaml").write_text(
            f'files:\n  - path: "{spaced}"\n    written_by: "a test"\n'
            'message: "chore(generated): nightly rewrite {date}"\n'
        )
        git(repo, "add", "-A")
        git(repo, "commit", "-q", "-m", "add the spaced file")
        (repo / spaced).write_text("row 1\nrow 2\n")

        outcome = commit_generated(repo, day="2026-09-09")
        assert outcome.paths == [spaced]


class TestItNeverPushes:
    def test_the_module_contains_no_push(self):
        """Not an omission — a rule. A job that pushes can put something
        on a remote at 23:37 with nobody awake; the next human `git push`
        is one review boundary this does not get to skip."""
        from cobalt.generated import committer

        source = Path(committer.__file__).read_text()
        code = "\n".join(
            line for line in source.split("\n") if not line.strip().startswith("#")
        )
        assert '"push"' not in code and "'push'" not in code

    def test_a_repo_with_a_remote_is_not_pushed_to(self, repo, tmp_path):
        remote = tmp_path / "remote.git"
        subprocess.run(["git", "init", "-q", "--bare", str(remote)], check=True)
        git(repo, "remote", "add", "origin", str(remote))
        dirty_the_listed_file(repo)

        commit_generated(repo, day="2026-09-09")

        refs = subprocess.run(
            ["git", "-C", str(remote), "for-each-ref"], capture_output=True, text=True
        )
        assert refs.stdout.strip() == "", "the remote must have received nothing"


class TestTheConfigGate:
    """Loading IS the check. A list a scheduled job runs `git add` from
    is a list that has to be right."""

    def test_a_listed_path_that_does_not_exist_fails_the_load(self, repo):
        (repo / "configs" / "cobalt" / "generated.yaml").write_text(
            'files:\n  - path: "docs/generated/gone.md"\n    written_by: "a test"\n'
            'message: "chore(generated): nightly rewrite {date}"\n'
        )
        with pytest.raises(GeneratedConfigError) as exc:
            load_generated_config(repo_root=repo)
        assert "do not exist" in str(exc.value)

    def test_an_untracked_listed_path_fails_the_load(self, repo):
        """It would put a file into the history that no human reviewed."""
        (repo / "docs" / "generated" / "new.md").write_text("hello\n")
        (repo / "configs" / "cobalt" / "generated.yaml").write_text(
            'files:\n  - path: "docs/generated/new.md"\n    written_by: "a test"\n'
            'message: "chore(generated): nightly rewrite {date}"\n'
        )
        with pytest.raises(GeneratedConfigError) as exc:
            load_generated_config(repo_root=repo)
        assert "NOT TRACKED" in str(exc.value)

    def test_an_escaping_path_is_refused(self, repo):
        (repo / "configs" / "cobalt" / "generated.yaml").write_text(
            'files:\n  - path: "../outside.md"\n    written_by: "a test"\n'
            'message: "m {date}"\n'
        )
        with pytest.raises(GeneratedConfigError) as exc:
            load_generated_config(repo_root=repo)
        assert "REPO-RELATIVE" in str(exc.value)

    def test_an_absolute_path_is_refused(self, repo):
        (repo / "configs" / "cobalt" / "generated.yaml").write_text(
            'files:\n  - path: "/etc/passwd"\n    written_by: "a test"\n'
            'message: "m {date}"\n'
        )
        with pytest.raises(GeneratedConfigError):
            load_generated_config(repo_root=repo)

    def test_a_missing_config_is_refused(self, repo):
        (repo / "configs" / "cobalt" / "generated.yaml").unlink()
        with pytest.raises(GeneratedConfigError) as exc:
            load_generated_config(repo_root=repo)
        assert "no built-in list" in str(exc.value)

    def test_written_by_is_required(self, repo):
        (repo / "configs" / "cobalt" / "generated.yaml").write_text(
            f'files:\n  - path: "{LISTED}"\nmessage: "m {{date}}"\n'
        )
        with pytest.raises(GeneratedConfigError):
            load_generated_config(repo_root=repo)


class TestTheShippedConfigAndJob:
    def test_the_repos_own_config_loads(self):
        """Which asserts, against THIS repository, that all three paths
        exist and are tracked."""
        cfg = load_generated_config()
        assert cfg.paths == [
            "docs/40 - DevDocs/reports/seat-usage.md",
            "docs/30 - Design/archiver-runs.md",
            "configs/cobalt/rules.yaml",
        ]

    def test_the_job_is_registered_as_a_daily_one_shot(self):
        from cobalt.jobs.config import load_job_registry

        spec = load_job_registry().spec("com.cobalt.generated")
        assert spec.kind.value == "one-shot"
        assert spec.supervisor.value == "self"
        assert spec.enabled is True
        assert spec.schedule.at == "23:37"
        assert sorted(spec.schedule.weekdays) == [0, 1, 2, 3, 4, 5, 6], (
            "every day: a Sunday's dirty tree is as unreadable as a Monday's"
        )

    def test_it_runs_after_everything_that_writes(self):
        """23:37 is after the last seat-usage run (23:00), the archiver
        (20:30 + ~23 min) and the backup (21:40)."""
        from cobalt.jobs.config import load_job_registry

        registry = load_job_registry()
        mine = registry.spec("com.cobalt.generated").schedule
        for other in ("com.cobalt.archiver", "com.cobalt.backup"):
            assert registry.spec(other).schedule.at < mine.at

    def test_the_plist_mirrors_the_schedule(self):
        """`cobalt validate` checks this too; asserting it here means a
        drift fails the suite and not only the gate."""
        import plistlib

        from cobalt.jobs.config import load_job_registry

        spec = load_job_registry().spec("com.cobalt.generated")
        data = plistlib.loads(spec.plist_path.read_bytes())
        entries = data["StartCalendarInterval"]
        assert len(entries) == 7
        assert {e["Hour"] for e in entries} == {23}
        assert {e["Minute"] for e in entries} == {37}
        assert sorted(e["Weekday"] for e in entries) == [0, 1, 2, 3, 4, 5, 6]
        assert data["EnvironmentVariables"]["COBALT_ENV"] == "production"
        assert data["RunAtLoad"] is False
        assert data["WorkingDirectory"] == "/Users/cobalt/cobalt"
