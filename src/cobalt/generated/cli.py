"""`cobalt generated` — the command `com.cobalt.generated` runs.

    cobalt generated commit [--dry-run] [--repo PATH]
    cobalt generated list

`commit` goes through the F17 wrapper, so a refusal is a red job row
with the reason on it rather than a silent no-op at 23:37. `--dry-run`
deliberately skips the wrapper: a rehearsal must not leave a row saying
the nightly commit ran.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from cobalt import env

from .committer import GeneratedCommitRefused, commit_generated
from .config import REPO_ROOT, load_generated_config

JOB_LABEL = "com.cobalt.generated"


def _today_et() -> str:
    """The ET calendar date, from the ONE session clock. The job fires at
    23:37 ET, which is tomorrow in UTC for eight months of the year — a
    `date.today()` here would put the wrong date in the subject line all
    summer."""
    from cobalt.session import clock as clock_mod
    from cobalt.session.clock import session_clock

    return f"{session_clock().to_et(clock_mod.now_utc()).date()}"


def cmd_commit(args: argparse.Namespace) -> None:
    from cobalt.redact import install_log_guard

    install_log_guard()
    repo = Path(args.repo).expanduser().resolve() if args.repo else REPO_ROOT
    day = _today_et()

    print(f"repo: {repo}  (COBALT_ENV={env.resolve_env()})")

    if args.dry_run:
        outcome = commit_generated(repo, day=day, dry_run=True)
        print("DRY RUN — nothing staged, nothing committed")
        print(outcome.console() if outcome.paths else "nothing would be committed")
        if outcome.paths:
            print("  would commit: " + ", ".join(outcome.paths))
        return

    from cobalt.jobs.wrapper import job_run

    with job_run(JOB_LABEL) as run:
        outcome = commit_generated(repo, day=day)
        run.result = {
            "committed": outcome.committed,
            "commit": outcome.commit,
            "paths": outcome.paths,
        }
    print(outcome.console())


def cmd_list(args: argparse.Namespace) -> None:
    """What the config declares, and what git says about each entry.

    Loading IS the check — a stale or untracked path raises here rather
    than at 23:37 — so this command is also the config gate for this
    family, the way `cobalt validate` is for the others.
    """
    repo = Path(args.repo).expanduser().resolve() if args.repo else REPO_ROOT
    cfg = load_generated_config(repo_root=repo)
    from .committer import _dirty

    dirty = set(_dirty(repo, cfg.paths))
    print(f"repo: {repo}")
    print(f"message: {cfg.commit_message('<YYYY-MM-DD>')}")
    print(f"\n{'STATE':<9} {'PATH':<44} WRITTEN BY")
    for f in cfg.files:
        state = "dirty" if f.path in dirty else "clean"
        print(f"{state:<9} {f.path:<44} {f.written_by}")
    print(f"\n{len(cfg.files)} declared, {len(dirty)} dirty. Every one exists and is tracked.")


def add_parser(sub) -> None:
    gen = sub.add_parser(
        "generated", help="Files in git that a job rewrites (com.cobalt.generated)."
    )
    gsub = gen.add_subparsers(dest="command", required=True)

    commit = gsub.add_parser(
        "commit", help="Commit the declared generated files that changed. Never pushes."
    )
    commit.add_argument("--dry-run", action="store_true", help="Show the plan, stage nothing.")
    #: A PROOF/TEST SEAM. The default is the checkout this package
    #: belongs to, so the scheduled job cannot be aimed at another
    #: repository by an accident of working directory; passing one is an
    #: explicit act, and the scratch-clone proof in the 09-09 ops report
    #: is what it exists for.
    commit.add_argument("--repo", default=None, help="Repository root (default: this checkout).")
    commit.set_defaults(func=cmd_commit)

    lst = gsub.add_parser("list", help="The declared files and whether each is dirty.")
    lst.add_argument("--repo", default=None)
    lst.set_defaults(func=cmd_list)


def main() -> None:
    """Direct entry point, for a plist that would rather not go through
    the top-level parser. Not used today; kept out of `__main__` so the
    package has no import-time side effects."""
    parser = argparse.ArgumentParser(prog="cobalt-generated")
    sub = parser.add_subparsers(dest="group", required=True)
    add_parser(sub)
    args = parser.parse_args()
    try:
        args.func(args)
    except GeneratedCommitRefused as e:
        print(f"{e}", file=sys.stderr)
        sys.exit(1)


__all__ = ["JOB_LABEL", "add_parser", "cmd_commit", "cmd_list"]
