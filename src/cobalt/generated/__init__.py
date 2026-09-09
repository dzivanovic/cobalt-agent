"""Files in git that a JOB rewrites, and the one commit that lands them.

THE PROBLEM THIS SOLVES. Three tracked files are rewritten by scheduled
jobs and nothing commits them:

    docs/40 - DevDocs/reports/seat-usage.md   hourly, 06:00-23:00 ET
    docs/30 - Design/archiver-runs.md         nightly, after 20:30
    configs/cobalt/rules.yaml                 05:15, `generated_at`

So `~/cobalt` — which IS production (R4, 09-08) — is permanently dirty,
and a permanently dirty working tree is one nobody reads. Every deploy
starts by squinting at `git status` deciding which of those lines are
"just the jobs", which is exactly the state in which a real uncommitted
change gets waved through. The 09-08 and 09-09 ledger appendices both
record leaving them uncommitted "deliberately"; that is a decision being
re-made by hand every day, which is the definition of a rule that wants
to be code.

THE SHAPE. `configs/cobalt/generated.yaml` names the paths — declared,
Pydantic-validated on load, and every path must EXIST and BE TRACKED or
the load fails. A path that is neither is not a generated file, it is a
typo or a file somebody deleted, and either way silence is the wrong
answer. `cobalt generated commit` stages exactly those of them that are
dirty, commits them under one boring message, and stops.

WHAT IT REFUSES, and why each one:

* **not on `main`** — the job runs in production, production is `main`
  (R4). On any other branch the dirty file may be part of the work in
  progress, and a job that commits it is a job that steals a hunk.
* **a merge, rebase or cherry-pick in progress** — the index belongs to
  that operation; adding to it mid-flight corrupts a human's work.
* **anything already staged** — somebody is mid-`git add`. The commit
  would carry their half-staged change under a message that says
  "nightly rewrite", and they would find out at review time.

WHAT IT NEVER DOES: it never pushes, it never touches a path the config
does not name, and it never adds an authorship trailer. The commit is
made by the repo's own configured identity because the author IS the
repo's own scheduler — no agent wrote those bytes, a job did.
"""

from .config import (
    CONFIG_PATH,
    GeneratedConfig,
    GeneratedConfigError,
    load_generated_config,
)

__all__ = [
    "CONFIG_PATH",
    "GeneratedConfig",
    "GeneratedConfigError",
    "load_generated_config",
]
