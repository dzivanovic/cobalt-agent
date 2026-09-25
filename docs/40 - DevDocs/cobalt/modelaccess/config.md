# `src/cobalt/modelaccess/config.py`

## What it does
Loads and validates the route registry `configs/cobalt/modelaccess.yaml`
into `ModelAccessConfig` / `Route` (seam S1 §2.3).

## What it refuses (L1, L10)
- A missing key — every field is required, none has a default.
- An unknown key (`extra="forbid"`), and a `fallback` key ANYWHERE in the
  file, named by its path: fallback is the routing lane's (L23 / L25
  frozen, FINAL [F-23]).
- A `lane: local` route whose `api_base` host is not loopback
  (`127.0.0.1`, `::1`, `localhost`).
- Any lane other than `local`, kind other than `openai_compatible`, think
  policy other than `forbid_nonempty`, `response_format` other than
  `json_schema` / `in_prompt` — V1's whole vocabulary.
- A non-positive `timeout_s` / `max_output_tokens`.
- A `key_name` that is not an UPPER_SNAKE VaultManager name (a value in
  that slot would be a secret in git).
- A YAML syntax error is reported with its line and column.

## `response_format`
Added beside the seam's keys to hold X-E4's evidence: whether the server
honours an OpenAI `response_format` JSON schema. The caller validates the
content with its own Pydantic model either way.
