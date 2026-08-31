# `src/cobalt/prefill/errors.py`

## What it does
One shared exception type, `PrefillFetchError`, for `market.py` and
`calendar.py`'s external-data fetches — fail-loud contract: the caller
renders FAILED, never guesses a value.

## Key functions/classes
- `PrefillFetchError(RuntimeError)`.

## Data flow in/out
None.

## Config it reads
None.
