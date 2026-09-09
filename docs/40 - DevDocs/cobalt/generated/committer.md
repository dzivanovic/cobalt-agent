# `src/cobalt/generated/committer.py`

## What it does
Three refusals, one `git add`, one commit, no push.

## The three refusals, and each one's victim
| refused when | why |
|---|---|
| the checkout is not on `main` | The job runs in production and production is `main` (R4). On a feature branch a dirty generated file may be part of the work in progress, and **a job that commits it steals a hunk.** |
| a merge / rebase / cherry-pick / revert / bisect is in progress | The index belongs to that operation. Adding to it mid-flight corrupts somebody's work. Detected by the marker files under `git rev-parse --absolute-git-dir` — which is a *file* in a worktree, hence `rev-parse` rather than `repo / ".git"`. |
| anything is already staged | Somebody is mid-`git add`. The commit would carry their half-staged change under a message that says "nightly rewrite", and **they would find out at review time.** |

Each raises `GeneratedCommitRefused` **before anything is staged**, so a
refusal leaves the tree exactly as it was found.

## What it stages
Only the declared paths that are dirty — an explicit list, after `--`.
That explicit list is what makes *"never touches any other dirty path"* a
property of the command rather than a hope. Proven both in the suite and
in a scratch clone: an unlisted modified file and an unlisted untracked
file both survive untouched, and `CommitOutcome.left_alone` names them.

## It never pushes
Not an omission — a rule, with a test that greps this module for the
word. A scheduled job that pushes can put something on a remote at 23:37
with nobody awake. The commit is local; the next human `git push`
carries it, which is one review boundary this does not get to skip.

## It never signs its work
No `--author`, no `Co-Authored-By`, no session link. The commit is made
by the repo's own configured identity because **no agent wrote those
bytes — the scheduler did.** A trailer naming a model on a commit no
model composed is a false statement in the permanent record.

## Trust the artifact, never the report
After committing it asks `git show --name-only` what actually landed and
raises if anything outside the declared list is in there. The command
does not get to report its own success.

## Details that are load-bearing
`-z` on every `status`/`show`, and `--` before every path list: two of
the three real entries contain spaces (`docs/40 - DevDocs/...`).

## Neighbours
`config.py`, `cli.py`, `jobs/wrapper.py` (the F17 row this runs inside).
