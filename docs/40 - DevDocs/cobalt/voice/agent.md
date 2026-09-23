# `src/cobalt/voice/agent.py`

## What it does
Builds the prompt and makes the ONE Plan call per turn through
`cobalt.modelaccess` on the route the registry names (`voice.plan` is the
caller name, the turn id the request id), then validates the reply into a
`Plan`.

## The prompt is a whitelist (L4, L41)
`build_messages` reads only `PromptInputs` and the registry entry: a
system message (charter, output rules, tool list) and ONE user message
that is a JSON object of `clock`, `candidates` (id + label), `history`
(said + reply) and `transcript`. No path, env value, config value or key
name has a way in; a secret-shaped value that reaches any of those fields
is refused by the S1 guard before a byte leaves (tested per field).

## The Plan is checked by code (FINAL §2.4)
`validate_plan` fails the turn (`PlanFailed`, failure class
`voice_plan`) when the reply is not a JSON `Plan` (`plan_parse` — a fenced
code block included), names a tool off the allowlist (`plan_tool`), pairs
a kind with the wrong tool kind or an unknown argument (`plan_shape`),
carries a span that is not a VERBATIM substring of the transcript
(`plan_span`), or a candidate id not on the closed list
(`plan_candidate`). A model-access error keeps its own kind. No retry:
one call per turn; the raw result stays on the failure as a stored input.

## `PLAN_SCHEMA`
The JSON schema sent with the call (as `response_format` or in the system
message, per the route), built from the committed registry's tool list.
