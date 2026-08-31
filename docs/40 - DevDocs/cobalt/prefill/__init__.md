# `src/cobalt/prefill/__init__.py`

## What it does
Package marker for Slice 2 (DRC & Daily prefill engine, pre-beta
increment 2). Docstring states the package's one hard rule: Cobalt fills
the grunt data, Dejan's critical thinking is the only manual input —
every writer in this package either creates a note fresh from a Jinja
template or appends a clearly fenced "Cobalt Prefill" block; existing
content is never read for mutation.

## Key functions/classes
None.

## Data flow in/out
None.

## Config it reads
None directly — see `config.py` for the package's config schemas.
