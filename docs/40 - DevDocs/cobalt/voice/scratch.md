# `src/cobalt/voice/scratch.py`

## What it does
Everything that touches scratch audio: the ONE writer (`write_scratch`),
the ONE unlink (`unlink_scratch`), the per-turn context (`turn_audio`),
the directory lock (`DirectoryLock`) and the start sweep (`start_sweep`).

## The life of a clip (FINAL §5)
`<scratch_dir>/<turn_id>.<ext>`: the directory is created 0700 (or
tightened to it), the file 0600, opened with `O_EXCL` (one file per turn);
the extension comes from a CLOSED content-type map (webm, ogg, m4a, wav) —
anything else is refused by name, as is a zero-byte payload or a turn id
that is not a plain file name. `turn_audio` unlinks the file in `finally:`
whatever happened; if that unlink fails the turn raises
`ScratchUnlinkFailed` — a file is never silently left. Since fix r1 a write
that raises or comes back short is `ScratchWriteFailed`: the partial file is
removed through the one unlink and a RED line names the failure (never a
truncated clip); and an unlink that finds the file already gone keeps its
AMBER "already gone" line on the held audio.

## The start sweep — R2-1 side B
His letter (R56): at every ASET start, before the first request, EVERY
file in the directory is deleted — no age test — one AMBER line each, a RED
line for any unlink that fails or any unexpected sub-directory.

## The directory lock — X-X22's guard
X-X22 measured an orphaned python child alive and holding its port while
launchd respawned the job. A delete-everything sweep in the respawn would
delete that orphan's live audio. So the serving process takes an
exclusive, non-blocking `flock` on `<scratch_dir>/.lock` before the sweep
and keeps it for its life (the lock file carries the holder's pid). A lock
held elsewhere → `ScratchLocked`: nothing deleted, RED naming the holder,
the start fails loud. The sweep refuses to run without the lock. The
CLI's `--audio` path takes the same lock for its turn.
