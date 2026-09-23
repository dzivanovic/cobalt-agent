# `src/cobalt/modelaccess/adapters.py`

## What it does
One adapter per route `kind`. V1 has one: `OpenAICompatibleAdapter`
(`openai_compatible`), which posts `/chat/completions` to the route's
loopback `api_base` and returns a `RawReply` (content, any
`reasoning_content`, the model AS RETURNED, finish reason, token usage).
Transport failures come back as `AdapterFailure` already classified into
a seam kind: `timeout`, `http_status`, `unreachable`, `bad_response`.

## Why the `openai` client and not litellm
The seam prefers litellm if its import is silent. It is: a fresh
interpreter with every non-loopback socket blocked records zero attempts
(`test_modelaccess_silence.py`). But on the fake server litellm REWROTE
THE REPLY: a body of `<think>\n\n</think>\n{...}` reached the module as
`{...}`, so the think policy could not see what the server said; and it
reported a refused connection and a non-JSON body as HTTP-status errors.
The seam forbids both (the module never repairs content; it applies its
own think policy). The `openai` client passes the server's bytes through
unchanged. The interface did not change.

## No retries, no proxies
`max_retries=0` (a failure is one typed failure) and an `httpx.Client`
with `trust_env=False` (an environment proxy never reroutes a loopback
call).
