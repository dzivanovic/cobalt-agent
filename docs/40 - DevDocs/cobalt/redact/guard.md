# `src/cobalt/redact/guard.py`

## What it does
`redact(text, *, channel, cfg=None, record=True) -> RedactResult`, and
`install_log_guard()`.

`RedactResult` carries `text`, `hits` (name → count), `clean`, `total`
and `describe()`, and destructures as `text, hits`.

## Order of operations
1. **Literals first, longest first.** A password inside a DSN is claimed
   by the literal before `connection_string_password` reaches it, so the
   count names the credential it actually is rather than the shape it
   was wearing. Longest-first stops a shorter secret mangling a longer
   one it is a substring of.
2. **Patterns, in config order** — specific rows before the broad
   `env_assignment_secret`.
3. **Build the output once** from the claimed spans.

## Why span-claiming rather than `re.sub` per pattern
Substituting over the previous pattern's output means a later pattern
can match an earlier one's placeholder: `MATTERMOST_TOKEN=
[REDACTED:mattermost_token]` is still a `NAME=value` line. That produced
two hits for one secret and the wrong attribution. Safety was never at
risk; attribution was — and attribution is the point.

## `record=False` exists for exactly one caller
The log guard. Counting a redaction opens a database connection, a
database failure logs, and logging comes back through here. The
DM/email/heartbeat channels do the counting; the log guard only ever
prevents.

## `install_log_guard()`
Routes loguru's formatted message through the redactor. A secret reaches
`logs/*.log` the same way it reaches a DM, and those files are read over
Tailscale and pasted into reports. Installed at every scheduled entry
point by `cobalt.jobs.entrypoint.as_job`, so a new job gets it by using
the wrapper.

## Counting never blocks a send
`_record()` catches everything and logs at ERROR: the redaction already
happened, the text is safe whether or not the row lands. Same
degradation rule as `SessionBlockStore.record`.
