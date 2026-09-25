# `src/cobalt/voice/turn.py`

## What it does
`run_turn(inp, deps)` — THE turn function (FINAL [F-01]). Three callers:
`POST /voice/turn` (+ the Confirm / Cancel taps), `cobalt voice turn`, the
tests. Every dependency is in `TurnDeps` (config, agent, store,
transcriber, the Plan call, the card / pool reads, the act's execute, the
clock); `default_deps()` wires the real ones and crashes on a config error.

## One turn, in order
1. The reaper runs; a tap goes straight to its pending action (same
   session only).
2. The row is created `received`. Audio: `transcribing`; the clip goes to
   scratch through the one writer; its length is probed against
   `max_clip_s` before any decode; the transcript comes back under
   `stt_timeout_s`; the file is unlinked right after — and in `finally:` on
   every failure path. The row keeps sha256, byte length, duration and
   `audio_deleted_at`, never the bytes.
3. Empty transcript → `failed: empty_transcript`, "I heard nothing."
4. A live pending action of THIS session → no model call: `yes` executes,
   `no` cancels, anything else ends it; the words are not planned. A
   pending action past its TTL is marked `expired`; a late yes / no is told
   so; other words are planned normally. In PRODUCTION a turn that is not
   the widget's (the CLI) and finds a pending action is refused whole —
   `failed: cli_confirm_refused`, RED, nothing executed, the pending action
   left for the widget ([F-02], L37; fix r1). A confirm whose act failed or
   was refused by its expert carries a RED line.
5. ONE Plan call → `planned` with the Plan, route, model as returned,
   latency and usage on the row.
6. Hard refusals by code (orders → `refuse`; trading logic → `unsupported`).
7. Clarify → `done`. A read → a code template (`answered` → `done`). The
   act → card resolution, the price parser, the dry run (X-X5's guard) →
   `awaiting_confirm` with the read-back. Nothing is written by the act
   turn itself.

## Failures are named
`voice_stt`, `clip_too_long`, `audio_refused`, `scratch_unlink`, `scratch_write`,
`cli_confirm_refused`,
`empty_transcript`, `tool_read`, `voice_plan` ("Cobalt can't think right
now (<kind>)"), `turn_error` — each on the row and in the reply, with a
RED line where the widget's banner needs one. Since fix r2 any other error
raised by the Plan call (a `ValueError`, say) is also `voice_plan`, "Cobalt
can't think right now (<class>)", RED — FINAL §7's row — not `turn_error`.

## Dry run
`dry_run=True` returns the Plan, the resolution and the exact change and
writes nothing at all — no row, no pending action, no reap.
