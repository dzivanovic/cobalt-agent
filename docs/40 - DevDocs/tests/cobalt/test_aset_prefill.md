# `tests/cobalt/test_aset_prefill.py`

## What it does
Tests exactly one thing, deliberately narrow: `prefill.scrub()` never
leaks an auth token. No network calls, no vault access — this suite
doesn't test `fetch_last_price` itself (that would need a live Finviz
token or a mocked httpx client, neither of which exists yet for this
module).

## Key functions/classes (what's covered, not defined)
- `test_scrub_redacts_auth_token_in_urls` — a realistic httpx redirect
  error string containing `auth=<token>` gets the token stripped and
  replaced with `auth=REDACTED`.
- `test_scrub_handles_token_at_end_and_mid_query` — token at the end of
  a query string, and a string with no secret at all (passthrough
  unchanged).

## Data flow in/out
None — pure string-function tests.

## Config it reads
None.
