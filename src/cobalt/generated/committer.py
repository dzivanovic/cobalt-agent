"""The commit itself — three refusals, one `git add`, no push.

Every git call is a fixed argv through `subprocess.run` with no shell,
in the tradition of `backup/pgdump.py`: nothing this module runs can be
influenced by a path that happens to contain a space or a semicolon, and
`--` separates options from paths on every command that takes both.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from loguru import logger

from .config import GeneratedConfig, load_generated_config

#: Production is `main` (R4, 2026-09-08: `~/cobalt` IS production, every
#: prompt works in a worktree off main, merge = deploy). On any other
#: branch a dirty generated file may be part of work in progress.
REQUIRED_BRANCH = "main"

#: The files git leaves behind while an operation owns the index.
IN_PROGRESS_MARKERS = (
    ("MERGE_HEAD", "a merge"),
    ("CHERRY_PICK_HEAD", "a cherry-pick"),
    ("REVERT_HEAD", "a revert"),
    ("rebase-merge", "a rebase"),
    ("rebase-apply", "a rebase or `git am`"),
    ("BISECT_LOG", "a bisect"),
)


class GeneratedCommitRefused(RuntimeError):
    """A precondition failed. NOTHING was staged and nothing committed."""


@dataclass
class CommitOutcome:
    committed: bool
    #: Repo-relative paths that went into the commit.
    paths: list[str] = field(default_factory=list)
    commit: Optional[str] = None
    message: Optional[str] = None
    #: Every dirty path in the repo this run deliberately left alone.
    left_alone: list[str] = field(default_factory=list)

    def console(self) -> str:
        if not self.committed:
            line = "nothing to commit — no listed file has changed"
        else:
            line = f"{self.commit}  {self.message}\n  " + "\n  ".join(self.paths)
        if self.left_alone:
            line += "\n  left alone (not listed): " + ", ".join(self.left_alone)
        return line


def _git(repo_root: Path, *args: str, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo_root), *args], capture_output=True, text=True
    )
    if check and proc.returncode != 0:
        raise GeneratedCommitRefused(
            f"`git {' '.join(args[:2])}` failed (exit {proc.returncode}): "
            f"{proc.stderr.strip()[:300]}"
        )
    return proc.stdout


def _assert_on_main(repo_root: Path) -> None:
    branch = _git(repo_root, "rev-parse", "--abbrev-ref", "HEAD").strip()
    if branch != REQUIRED_BRANCH:
        raise GeneratedCommitRefused(
            f"REFUSED: this checkout is on {branch!r}, not {REQUIRED_BRANCH!r}. "
            "The generated-files commit runs in production, and production is "
            f"{REQUIRED_BRANCH} (R4). On a feature branch a dirty generated file "
            "may be part of the work in progress, and a job that commits it is a "
            "job that steals a hunk."
        )


def _assert_no_operation_in_progress(repo_root: Path) -> None:
    git_dir = Path(_git(repo_root, "rev-parse", "--absolute-git-dir").strip())
    for marker, what in IN_PROGRESS_MARKERS:
        if (git_dir / marker).exists():
            raise GeneratedCommitRefused(
                f"REFUSED: {what} is in progress ({git_dir / marker} exists). The "
                "index belongs to that operation; adding to it mid-flight corrupts "
                "somebody's work."
            )


def _assert_index_is_clean(repo_root: Path) -> None:
    proc = subprocess.run(
        ["git", "-C", str(repo_root), "diff", "--cached", "--quiet"],
        capture_output=True,
        text=True,
    )
    if proc.returncode == 0:
        return
    staged = _git(repo_root, "diff", "--cached", "--name-only").split()
    raise GeneratedCommitRefused(
        f"REFUSED: {len(staged)} path(s) are already staged: {staged[:10]}. Somebody "
        "is mid-`git add`, and this commit would carry their half-staged change "
        'under a message that says "nightly rewrite".'
    )


def _dirty(repo_root: Path, paths: Optional[list[str]] = None) -> list[str]:
    """Repo-relative paths with unstaged changes (and untracked files
    when `paths` is None). `-z` because a repo path may contain a space —
    two of the three listed files do."""
    args = ["status", "--porcelain", "-z"]
    if paths is not None:
        args += ["--", *paths]
    out = _git(repo_root, *args)
    found = []
    for entry in out.split("\0"):
        if len(entry) > 3:
            found.append(entry[3:])
    return found


def commit_generated(
    repo_root: Path,
    *,
    day: str,
    config: Optional[GeneratedConfig] = None,
    dry_run: bool = False,
) -> CommitOutcome:
    """Stage the listed files that changed, commit them, and stop.

    NO PUSH. Not as an omission — as a rule. A scheduled job that pushes
    is a job that can put something on a remote at 23:37 with nobody
    awake; the commit is local and the next human `git push` carries it,
    which is one review boundary this does not get to skip.

    NO AUTHORSHIP TRAILER. The commit is made by the repo's own
    configured identity, with no `Co-Authored-By` and no session link,
    because no agent wrote those bytes — the scheduler did. A trailer
    naming a model on a commit no model composed is a false statement in
    the permanent record.
    """
    cfg = config or load_generated_config(repo_root=repo_root)

    _assert_on_main(repo_root)
    _assert_no_operation_in_progress(repo_root)
    _assert_index_is_clean(repo_root)

    listed = cfg.paths
    changed = _dirty(repo_root, listed)
    others = [p for p in _dirty(repo_root) if p not in set(listed)]

    if not changed:
        logger.info("generated: nothing to commit — no listed file has changed.")
        return CommitOutcome(committed=False, left_alone=others)

    if dry_run:
        return CommitOutcome(
            committed=False,
            paths=changed,
            message=cfg.commit_message(day),
            left_alone=others,
        )

    # ONLY the listed paths that are dirty. `--` so a path is never read
    # as an option, and the explicit list is what makes "never touches
    # any other dirty path" a property of the command rather than a hope.
    _git(repo_root, "add", "--", *changed)

    message = cfg.commit_message(day)
    _git(repo_root, "commit", "-m", message)
    sha = _git(repo_root, "rev-parse", "--short", "HEAD").strip()

    # TRUST THE ARTIFACT, NEVER THE REPORT: ask git what actually landed
    # rather than reporting what we asked for.
    landed = [
        p
        for p in _git(repo_root, "show", "--pretty=", "--name-only", "-z", "HEAD").split("\0")
        if p
    ]
    unexpected = sorted(set(landed) - set(listed))
    if unexpected:
        raise GeneratedCommitRefused(
            f"commit {sha} carries path(s) the config does not list: {unexpected}. "
            "This should be impossible; investigate before the next run."
        )

    logger.info("generated: committed {} ({} file(s)): {}", sha, len(landed), message)
    return CommitOutcome(
        committed=True, paths=sorted(landed), commit=sha, message=message,
        left_alone=others,
    )


__all__ = [
    "IN_PROGRESS_MARKERS",
    "REQUIRED_BRANCH",
    "CommitOutcome",
    "GeneratedCommitRefused",
    "commit_generated",
]
