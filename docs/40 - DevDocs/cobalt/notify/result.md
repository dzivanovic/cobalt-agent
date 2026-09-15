# `src/cobalt/notify/result.py`

## What it does
`SendResult(sent, detail, redactions, noun, ref)` — the one shape every
outbound channel returns.

## Why it moved out of `mattermost.py`
S1-P4. The heartbeat now reports on two channels in the same block, and
two near-identical result dataclasses would have been the second copy the
one-path rule kills on sight. `mattermost.SendResult` still imports from
where it always was — it *is* this class.

## `ref`
The remote system's own id — a Mattermost post id (a Gmail message id,
until that channel was retired 2026-09-14). Structured rather than left
for a caller to parse back out of `detail`: a caller that re-split a human-readable sentence would break the moment that
sentence was reworded. Not a credential.

## It carries no material
`detail` is written by the sender and is already redacted wherever it
could quote a server's reply. `redactions` carries F19's per-kind
**counts** — the whole of what a redaction is allowed to leave behind.
