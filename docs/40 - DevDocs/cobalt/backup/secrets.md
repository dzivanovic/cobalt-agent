# `src/cobalt/backup/secrets.py`

## What it does
One vault read, for the restic repository password and the B2 keys.

## It raises instead of returning `""`
An empty password is not a degraded backup — it is a repository nobody
can open later, written nightly, looking fine. Missing key, locked
vault, wrong shape: all refuse.

## The decryption exception's text is never included
Only its type. Same reasoning as `cobalt.redact.secrets`: a decryption
error can echo material back.
