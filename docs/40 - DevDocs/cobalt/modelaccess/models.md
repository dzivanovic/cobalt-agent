# `src/cobalt/modelaccess/models.py`

## What it does
The Pydantic contract of seam S1 §2.2: `ModelMessage`, `ModelRequest`,
`Usage`, `ModelResult`, the `ModelCallError` exception and `ERROR_KINDS`.

## The rules the types carry
- `ModelRequest.route` is a route NAME; `caller` and `request_id` are
  recorded on the call line (voice passes `voice.plan` and the turn id).
- `max_output_tokens` / `timeout_s` are optional; a caller may only LOWER
  the route's budget (the client refuses a raise with a `ValueError` — a
  caller bug, not a model failure).
- `ModelResult.model_returned` is what the server said, never the alias.
  `think_block` is `absent` or `empty_removed`; anything else failed.
- `ModelCallError.kind` is one of nine seam kinds (`route_unknown`,
  `prompt_refused`, `unreachable`, `timeout`, `http_status`,
  `bad_response`, `empty`, `think_leak`, `schema_refused`); `detail` has
  passed `redact()`. `empty` is an error — an empty string is never an
  answer (L1).
