# `src/cobalt/redact/` — F19 exfiltration guard

## What it does
One function on every outbound channel:

```python
from cobalt.redact import redact
safe, hits = redact(text, channel="mattermost")
```

The returned text is what may leave the host. `hits` says **what kind**
of secret was caught and how many times — never the value.

Charter §3 F19: *"outbound secret-regex redactor on every channel. Test:
a token in a DM payload is redacted before send."*

## The two halves, and why one is not enough
| half | catches | where it lives |
|---|---|---|
| **patterns** | anything token-shaped, in text nobody has seen before | `configs/cobalt/redact.yaml`, 17 rows |
| **literals** | the human usernames and passwords no shape can describe | the vault, in memory, via `secrets.py` |

Four of the credentials rotated on **2026-08-23** are usernames and
passwords — `smbtraining.com`, `rt.smbtraining.com`,
`financialjuice.com`, `finviz.com`. A regex broad enough to match a
human password matches ordinary prose; one narrow enough to spare prose
does not match the password. So those are matched **literally** against
the values VaultManager already holds, and reported by vault key *name*
(`literal:finviz.com::password`).

## No secret value is anywhere in git
The shapes in `redact.yaml` were derived from the vault
**programmatically** — documented prefix, character class, length —
and never printed. A pattern file carrying the thing it stops leaking
would be the leak.

## The files
| file | law it keeps |
|---|---|
| `config.py` | a regex that does not compile **crashes at load**, with its name. A guard that fails open is worse than none, because it is trusted. |
| `secrets.py` | vault values live in memory only, are never logged or persisted, and a locked vault is **not an error** — the pattern half still runs and the literal half says it is inactive. Reads the same encrypted file as the old tree's `VaultManager` without importing it (strangler rule). |
| `guard.py` | `redact()`, `install_log_guard()`. |
| `store.py` | `cobalt_redactions` — the counter F18 reads. |

## Three properties worth knowing
1. **Partial redaction.** A pattern that declares a `secret` group
   replaces only that group:
   `postgresql://cobalt:[REDACTED:connection_string_password]@host:5432/db`.
   A redactor that makes a DSN unreadable is one people route around at
   05:15.
2. **One pass, not N.** Matches are collected as spans over the
   *original* text and the output is built once, first claim winning.
   Substituting per pattern over the previous pattern's output let a
   later row match an earlier row's placeholder — one secret, two hits,
   wrong attribution.
3. **Idempotent.** A span that is already nothing but a placeholder is
   never re-claimed, so redacting an assembled message that contains
   already-redacted blocks does not inflate the count.

## It fails closed
A config that cannot be loaded **raises**. Every caller is about to send
something off the host, and "the guard is broken" must never be the
quiet path to "send it anyway".

## Ordering is policy
Patterns are walked in config order and the broad
`env_assignment_secret` row is **last**, so the specific rows claim
their shapes first and the operator learns *which kind* of secret nearly
left.

## Tests
`tests/cobalt/test_redact.py` — 64 cases, including **one per shipped
pattern driven off the config itself**: a pattern added to
`redact.yaml` with no sample fails the suite rather than shipping
untested.
