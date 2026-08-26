# `src/cobalt/__init__.py`

## What it does
Package marker for the new core (strangler rebuild). No logic — just the
module docstring stating the ground rules that bind everything under
`src/cobalt/`: fail-loud, deterministic math, config-driven, dev
environment only until promoted.

## Key functions/classes
None.

## Data flow in/out
None — imported implicitly whenever anything under `cobalt.*` is used.

## Config it reads
None.
