# `src/cobalt/backup/__init__.py`

The nightly backup (RULED 2026-09-04: "restic → B2 + SSD, NOT Time
Machine"). Re-exports `snapshot`, `restore`, `latest_snapshot_age` and
the config types.

**Built and proven 2026-09-04; NOT ARMED.** The mechanism was driven end
to end against a throwaway repository — 547 files plus a fresh 360 MB
`cobalt_brain` dump, snapshot taken, one daily note and the dump
restored, the note byte-identical to live, and the dump reloaded into a
scratch database matching `cobalt_brain` on every table and on md5 over
4.79M ordered `bars` rows. The throwaway repository was destroyed
afterwards; it was a mechanism proof, never a backup.

Neither ruled destination exists on this host yet. See
`configs/cobalt/backup.yaml`'s header and `ops/pending/README.md`.
