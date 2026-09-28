# `src/cobalt/modelaccess/client.py`

## What it does
`call_sync(req)` and `call(req)`: resolve the route → build the messages
(the `/no_think` switch on the last user message; a response schema as
`response_format` or in the system message, per the route) → GUARD every
byte that would leave → adapter → think policy → `ModelResult`.

## One path
`call()` is `call_sync()` under `asyncio.to_thread`, so a FastAPI route
never blocks the event loop (FINAL [F-04]) and the CLI and the tests run
the same code. A test proves a concurrent coroutine keeps ticking during
a slow call.

## Think policy `forbid_nonempty`
An empty leading `<think>` block is removed and recorded
(`empty_removed`); a non-empty one, an unclosed one, a stray tag, or any
non-empty `reasoning_content` is `think_leak` — the caller's turn fails,
it never executes. Empty content is `empty`.

## The call record (L57)
Exactly one log line per call, success or error: route, caller, request
id, lane, kind, model_returned, latency, token usage, think block, the
literal guard's state, error kind. Never the message text or the reply.
The module keeps no table; the caller stores what it needs (voice: the
`voice_turns` row).
