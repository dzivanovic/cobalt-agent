# `src/cobalt/generated/config.py`

## What it does
Loads `configs/cobalt/generated.yaml` into `GeneratedConfig`. Pydantic,
`extra="forbid"`, fail-loud — config-as-code, like every other family.

## The validation is the interesting part
The schema check is the easy half. What makes this list dangerous is a
path that has gone stale, so the loader **asks git**:

* **the file must exist.** A listed path that has been deleted makes the
  nightly job stage nothing and commit nothing, forever, with no red
  anywhere. A job that is silently a no-op is worse than a job that
  fails.
* **git must track it.** An untracked listed path would be **added** to
  the repository by a scheduled job — a file entering the history that
  no human reviewed.

Both raise `GeneratedConfigError`. There is no "skip the entries that
look wrong": a list this job trusts enough to run `git add` from is a
list that has to be right.

`ls-files`, not `git log`: a file staged for the first time but never
committed is still tracked and is still a legitimate entry.

## `path` is repo-relative, enforced
Absolute paths and any `..` component are refused by a field validator.
The list is resolved against a repository root, and a path that can
climb out of it is a path that can stage something outside the checkout.

## `written_by` is required, and it is not decoration
The first question asked of an unexpected diff in one of these files is
"what wrote this". The answer belongs beside the path rather than in
somebody's memory — the same reasoning that puts `consumers` on a
tunables row.

## `repo_root` is a parameter
`REPO_ROOT` (the checkout this package belongs to) is the default, so
the scheduled job cannot be aimed elsewhere by an accident of working
directory. Passing one is an explicit act — the scratch-clone proof in
the 2026-09-09 ops report is what it exists for.

## Neighbours
`committer.py` (the only consumer), `configs/cobalt/generated.yaml`.
