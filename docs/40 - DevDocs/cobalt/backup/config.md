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

## Both destinations ship `enabled: false`
Not an oversight, and `test_both_legs_are_off_today` fails if that
changes. On 2026-09-04 neither destination the ruling names existed on
this host — no SSD mounted, no B2 credential in the vault. A test that
fails when someone arms a leg is the point: arming a backup is a change
worth reviewing, not a config typo that slips through.
