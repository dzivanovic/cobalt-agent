"""THE outbound guard for every model call (seam S1 §2.1, §2.4 (1); L4, L41).

Built on the existing F19 redactor (`cobalt.redact.redact` — patterns +
the VaultManager literal half). A prompt whose redaction differs from
itself is REFUSED, never sent redacted: a redacted prompt is still a
prompt that was about to carry a secret, and the caller has a bug to fix.

The refusal names the KIND of hit (pattern / literal vault-key names),
never the text. When the literal half reports itself INACTIVE (a locked
vault), a LOCAL route is not refused — the text never leaves the host —
and the result says so; a future non-local route refuses in that state
(the JEV rule, seam §3).

`classify/collector.py::_guard_outbound` (unmerged, `jev/trial-0923`) is
a pre-S1 duplicate of this check; the seam rule re-points it here at
whichever merge lands second (L3).
"""

from __future__ import annotations

from dataclasses import dataclass

from cobalt.redact import load_literals, redact


class PromptRefused(RuntimeError):
    """A message carried something secret-shaped. Names kinds, never text."""

    def __init__(self, kinds: list[str], where: str):
        self.kinds = kinds
        self.where = where
        super().__init__(f"prompt refused at {where}: secret-shaped content ({', '.join(kinds)})")


@dataclass(frozen=True)
class GuardReport:
    literal_guard_active: bool


def refuse_if_secret_shaped(text: str, *, where: str) -> GuardReport:
    """Raise `PromptRefused` if `text` would be changed by `redact()`."""
    result = redact(text, channel="modelaccess")
    if result.hits:
        raise PromptRefused(sorted(result.hits), where)
    return GuardReport(literal_guard_active=load_literals().available)


__all__ = ["GuardReport", "PromptRefused", "refuse_if_secret_shaped"]
