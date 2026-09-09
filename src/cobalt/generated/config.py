"""`configs/cobalt/generated.yaml` — the declared list, validated on load.

Config-as-code (TRIAGE): a Pydantic schema per config family, in git,
fail-loud. The validation here is stronger than "is this a string",
because the thing that makes this list dangerous is a path that has gone
stale: a job that stages a path which no longer exists writes an empty
commit, and one that stages an UNTRACKED path adds a file to the
repository that nobody reviewed. Both are silent. So the load asks git.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

#: The checkout this package belongs to. `cobalt generated commit`
#: defaults to it, so the command acts on the repo it is part of and
#: cannot be aimed elsewhere by an accident of working directory.
REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG_PATH = REPO_ROOT / "configs" / "cobalt" / "generated.yaml"


class GeneratedConfigError(RuntimeError):
    """Missing/invalid generated-files config — crash, never fall back."""


class GeneratedFile(BaseModel):
    """One tracked file that a job rewrites."""

    model_config = ConfigDict(extra="forbid")

    path: str = Field(min_length=1)
    #: Which job rewrites it, and how often. Prose, and it earns its
    #: place: the first question asked of an unexpected diff in one of
    #: these files is "what wrote this", and the answer belongs beside
    #: the path rather than in somebody's memory.
    written_by: str = Field(min_length=1)

    @field_validator("path")
    @classmethod
    def _repo_relative(cls, v: str) -> str:
        p = Path(v)
        if p.is_absolute() or ".." in p.parts:
            raise ValueError(
                f"{v!r} must be REPO-RELATIVE with no `..` — this list is resolved "
                "against a repository root, and a path that can climb out of it is "
                "a path that can stage something outside the checkout."
            )
        return v


class GeneratedConfig(BaseModel):
    model_config = ConfigDict(extra="forbid")

    files: list[GeneratedFile] = Field(min_length=1)
    #: The commit subject. `{date}` is the only placeholder.
    message: str = Field(min_length=1)

    @field_validator("files")
    @classmethod
    def _unique(cls, v: list[GeneratedFile]) -> list[GeneratedFile]:
        paths = [f.path for f in v]
        dupes = sorted({p for p in paths if paths.count(p) > 1})
        if dupes:
            raise ValueError(f"duplicate path(s): {dupes}")
        return v

    @property
    def paths(self) -> list[str]:
        return [f.path for f in self.files]

    def commit_message(self, day: str) -> str:
        return self.message.format(date=day)


def _tracked(repo_root: Path, paths: list[str]) -> set[str]:
    """The subset of `paths` git has under version control.

    `ls-files` and not `git log`: a file staged for the first time but
    never committed is still tracked, and is still a legitimate entry.
    """
    proc = subprocess.run(
        ["git", "-C", str(repo_root), "ls-files", "-z", "--", *paths],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise GeneratedConfigError(
            f"`git ls-files` failed in {repo_root} (exit {proc.returncode}): "
            f"{proc.stderr.strip()[:200]}"
        )
    return {p for p in proc.stdout.split("\0") if p}


def load_generated_config(
    path: Path | None = None, *, repo_root: Path | None = None
) -> GeneratedConfig:
    """Load, validate, and CHECK EACH PATH AGAINST THE REPOSITORY.

    Two checks beyond the schema, and neither is optional:

    * the file exists on disk — a listed path that has been deleted
      makes the nightly job stage nothing and commit nothing, forever,
      with no red anywhere;
    * git tracks it — an UNTRACKED listed path would be ADDED to the
      repository by a scheduled job, which is a file entering the
      history that no human reviewed.

    Both raise. There is no "skip the ones that look wrong": a list this
    job trusts enough to `git add` from is a list that has to be right.
    """
    root = Path(repo_root or REPO_ROOT)
    cfg_path = Path(path) if path else (root / "configs" / "cobalt" / "generated.yaml")

    if not cfg_path.exists():
        raise GeneratedConfigError(
            f"generated-files config not found: {cfg_path}. There is no built-in "
            "list: a file a job may commit is a file somebody declared."
        )
    raw = yaml.safe_load(cfg_path.read_text())
    if not isinstance(raw, dict):
        raise GeneratedConfigError(f"{cfg_path}: expected a YAML mapping")
    try:
        cfg = GeneratedConfig(**raw)
    except ValidationError as e:
        raise GeneratedConfigError(f"{cfg_path}: invalid generated-files config:\n{e}") from e

    missing = [p for p in cfg.paths if not (root / p).exists()]
    if missing:
        raise GeneratedConfigError(
            f"{cfg_path}: listed path(s) do not exist under {root}: {missing}. "
            "A stale entry makes the nightly job a no-op that nothing reports."
        )

    tracked = _tracked(root, cfg.paths)
    untracked = [p for p in cfg.paths if p not in tracked]
    if untracked:
        raise GeneratedConfigError(
            f"{cfg_path}: listed path(s) are NOT TRACKED by git: {untracked}. "
            "This list is what a scheduled job runs `git add` on — an untracked "
            "entry would put a file into the history that no human reviewed."
        )
    return cfg


__all__ = [
    "CONFIG_PATH",
    "REPO_ROOT",
    "GeneratedConfig",
    "GeneratedConfigError",
    "GeneratedFile",
    "load_generated_config",
]
