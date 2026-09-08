"""What an outbound channel returns. ONE shape, every channel.

Lifted out of `mattermost.py` when `email.py` landed (S1-P4): the
heartbeat now reports on two channels in the same block, and two
near-identical result dataclasses would have been the second copy the
one-path rule kills. `mattermost.SendResult` is still importable from
where it always was — it is this class.

A `SendResult` carries no material. `detail` is written by the sender and
is already redacted where it could quote a server's reply; `redactions`
carries F19's per-kind COUNTS, which is the whole of what a redaction is
allowed to leave behind.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SendResult:
    sent: bool
    detail: str
    redactions: dict[str, int] = field(default_factory=dict)
    #: What the channel calls itself in a report — "DM", "Email".
    noun: str = "DM"
    #: The remote system's own id for what was sent — a Gmail message id,
    #: a Mattermost post id. STRUCTURED rather than left for a caller to
    #: parse back out of `detail`: `email-test` has to print the id and
    #: store it in a column, and a channel that made it re-split a
    #: human-readable sentence would break the moment that sentence was
    #: reworded. Not a credential — it is what an operator quotes in a
    #: support thread.
    ref: str | None = None

    def report(self) -> str:
        head = f"{self.noun} sent" if self.sent else f"{self.noun} NOT sent"
        if self.redactions:
            kinds = ", ".join(f"{k} x{v}" for k, v in sorted(self.redactions.items()))
            return f"{head} — {self.detail} · F19 redacted: {kinds}"
        return f"{head} — {self.detail}"


__all__ = ["SendResult"]
