# `src/cobalt/modelaccess/guard.py`

## What it does
`refuse_if_secret_shaped(text, where=...)` — THE outbound guard for every
model call. It runs the existing F19 redactor (`cobalt.redact.redact`:
the secret patterns and the VaultManager literal half) over the text; if
redaction would change anything, it raises `PromptRefused` naming the
KINDS of hit (pattern names / vault key names), never the text. The
client turns that into `ModelCallError(prompt_refused)` with zero
network calls (L4, L41).

## Refused, not redacted
A prompt that was about to carry a secret is a caller bug; sending the
redacted version would hide it.

## Locked vault
When the literal half is INACTIVE (no `COBALT_MASTER_KEY` on the
process), a LOCAL route is still allowed — the text never leaves the host
— and the call line records `literal_guard=INACTIVE`. A future non-local
route must refuse in that state (seam §3).

## The JEV duplicate
`classify/collector.py::_guard_outbound` on the unmerged `jev/trial-0923`
is a pre-S1 copy of this check. It was NOT on `main` when V1 was built,
so the seam §3 re-point is owed by JEV's merge.
