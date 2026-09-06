# `src/cobalt/backup/config.py`

## What it does
The backup's Pydantic schema — `configs/cobalt/backup.yaml`. Sources,
the database to dump, excludes, destinations, the vault KEY NAMES for
the credentials, and the retention policy.

## `enabled` is separate from `repo` being set
An empty `repo` could have meant "off". It does not. A destination
declares `enabled` explicitly, and an enabled destination with no `repo`
is a validation error, not a silent no-op. The state this distinguishes
is the one that matters: *configured but switched off* is reviewable in
a diff; *empty string quietly meaning nothing happens* is what a backup
discovers on the day it is needed.

## No credential is in this file
`password_vault_key`, `b2_key_id_vault_key` and `b2_app_key_vault_key`
name VaultManager keys. Same shape `configs/cobalt/notify.yaml` uses for
`MATTERMOST_CREDS`, and the same reason: the file is in git.

## `requires_mount` — the removable-disk guard, and it is mandatory
A local `repo` under `/Volumes/` MUST declare the volume it needs; the
schema refuses one that does not. This is not belt-and-braces, it is the
whole failure mode of a backup on an external disk:

> With the SSD unplugged, `/Volumes/COBALT-BACKUP` is simply a path that
> does not exist — and restic, `mkdir -p` and the shell will all
> cheerfully **create it on the boot disk**. The nightly job then writes
> the repository onto the disk it exists to protect against, exits 0,
> and paints the heartbeat green. Nothing errors until the day the Mac
> dies.

So the check is `os.path.ismount` (`Destination.mount_ok`), never
`exists`: the broken state is a directory that exists on the *wrong*
disk. `requires_mount` is also cross-validated against `repo` — guarding
a mount the repository does not live on checks nothing — and `/` is
normalised as a mount point rather than being eaten by `rstrip("/")`.

## Which legs are armed is pinned by a test
`test_the_ssd_is_armed_and_b2_is_not`. On 2026-09-04 both legs shipped
off because neither destination existed on this host; on 2026-09-05 the
SSD was mounted and armed, and that test was rewritten in the same
commit. B2 is still off — no credential in the vault. A test that fails
when someone arms or disarms a leg is the point: it is a change worth
reviewing, not a config typo that slips through.
