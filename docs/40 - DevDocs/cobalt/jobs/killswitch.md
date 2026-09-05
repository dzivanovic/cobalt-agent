# `src/cobalt/jobs/killswitch.py`

## What it does
F17d — the kill phrase.

```
cobalt stop      # one-shots refuse to start; residents exit cleanly
cobalt resume    # clears it
```

The phrase is config (`configs/cobalt/jobs.yaml`: `COBALT STOP` /
`COBALT RESUME`), compared case-insensitively on a stripped line — a
stop that failed because of a trailing space would be the worst possible
bug in this feature.

## Why the flag is in Postgres
Cobalt's jobs are separate launchd processes with no shared memory, and
the one thing they all already reach is the database. A file works until
one job runs from a different working directory — and the failure mode
of a switch nobody's process can see is that it silently stops nothing.

## What "stops" means
- a **one-shot refuses to start**: marks nothing, writes nothing, exits
  **0** with a loud line;
- a **resident exits cleanly** at its next check, rather than being torn
  out of a write.

It does not reach into the database or the vault to undo anything. It
stops new work.

## It fails OPEN, loudly
If the switch cannot be read the answer is *not stopped*. A database
blip silently stopping every scheduled job on the host is far worse than
one run happening after a stop was requested — and it would look exactly
like the switch working correctly.

## The DM half
`matches_kill_phrase()` / `matches_resume_phrase()` exist and are
tested. They are **not wired**: the only Mattermost *listener* lives in
the old tree, which the strangler rule keeps closed. The first new-core
listener picks them up unchanged.
