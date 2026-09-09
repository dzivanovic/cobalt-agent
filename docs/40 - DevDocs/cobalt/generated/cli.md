# `src/cobalt/generated/cli.py`

## What it does
```
cobalt generated commit [--dry-run] [--repo PATH]
cobalt generated list
```

`commit` is what `com.cobalt.generated` runs at 23:37 ET. It goes
through the **F17 wrapper**, so a refusal is a red job row carrying the
reason rather than a silent no-op at 23:37 that nobody sees until the
tree is dirty again.

`--dry-run` deliberately skips the wrapper: a rehearsal must not leave a
row saying the nightly commit ran. Same rule as `cobalt seat-usage run`.

## `list` is also this family's config gate
Loading **is** the check — a stale or untracked path raises there rather
than at 23:37 — so printing the list exercises the gate, and the command
doubles as the answer to "what is this job allowed to commit".

## `_today_et`
The date in the subject line comes from the **ET session clock**, not
`date.today()`. The job fires at 23:37 ET, which is already tomorrow in
UTC for eight months of the year; a naive call would put the wrong date
on the commit all summer.

## `--repo`
A proof/test seam, documented as one. The default is the checkout the
package belongs to, so the scheduled job cannot be aimed at another
repository by an accident of working directory.

## Neighbours
`committer.py`, `config.py`, `cobalt/cli.py` (which registers this
parser), `jobs/wrapper.py`.
