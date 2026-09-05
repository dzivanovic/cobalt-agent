# `src/cobalt/redact/config.py`

## What it does
Loads and validates `configs/cobalt/redact.yaml` — F19's pattern set as
data. `RedactConfig` (placeholder, `literal_min_length`, `patterns`) and
`Pattern` (`name`, `regex`, `because`).

## Why validation is strict
- **A regex that does not compile crashes at load, named.** The
  alternative is a pattern that silently matches nothing forever, in a
  guard people trust.
- **The placeholder must contain `{name}`.** An operator has to learn
  *which kind* of secret was about to leave — that is the whole
  diagnostic value a redaction leaves behind.
- **Duplicate pattern names are refused** (the counter is keyed by
  name).

## `SECRET_GROUP`
A pattern replaces its whole match **unless** it declares a group named
`secret`, in which case only that group goes. `replaces_whole_match`
reports which. See the `__init__` page's note on partial redaction.

## Where it lives, and why
`configs/cobalt/` — a sanctioned new-core location outside the old
loader's top-level `configs/*.yaml` glob (CLAUDE.md's config-boundary
law).
