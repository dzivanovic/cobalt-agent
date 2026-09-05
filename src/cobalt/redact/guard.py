"""F19 EXFILTRATION GUARD — one function, on every outbound channel.

Charter §3 F19: "outbound secret-regex redactor on every channel. Test: a
token in a DM payload is redacted before send."

    from cobalt.redact import redact

    safe, hits = redact(text, channel="mattermost")

THE CONTRACT, in three lines:

* the returned text is what may leave the host;
* `hits` says WHAT KIND of secret was caught and how many times — never
  the value, not once, not truncated, not in a log line;
* a hit is COUNTED (`RedactionStore`), and the count reaches the F18
  heartbeat. A guard that fires silently teaches nobody anything.

ORDER MATTERS, and it is deliberate. Literals run FIRST, longest first,
then patterns in config order (specific rows before the broad
`env_assignment_secret`). A password sitting inside a DSN is claimed by
the literal before `connection_string_password` reaches it, so the count
names the credential it actually is rather than the shape it was wearing.

ONE PASS, NOT N PASSES. Matches are collected as SPANS over the original
text and the output is built once. The obvious implementation —
`re.sub` per pattern, over the text the last pattern returned — has a
bug that showed up the first time two rows overlapped: the second
pattern matched the FIRST one's placeholder (`MATTERMOST_TOKEN=
[REDACTED:mattermost_token]` is still a `NAME=value` line), redacted the
placeholder, and reported two hits for one secret. Safety was never at
risk; attribution was, and attribution is the entire diagnostic value a
redaction leaves behind. First claim wins; later overlaps are dropped.

FAIL CLOSED. If the config cannot be loaded, `redact()` raises — it does
not pass the text through. Every caller here is about to send something
off the host, and "the guard is broken" must never be the quiet path to
"send it anyway".
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional

from .config import SECRET_GROUP, RedactConfig, load_redact_config
from .secrets import load_literals

#: The name a literal hit is reported under: the vault key, never the
#: value. `literal:finviz.com::password` in a heartbeat is exactly as
#: much as an operator needs.
LITERAL_PREFIX = "literal:"


@dataclass
class RedactResult:
    """What may be sent, and what was caught on the way."""

    text: str
    hits: dict[str, int] = field(default_factory=dict)

    @property
    def clean(self) -> bool:
        return not self.hits

    @property
    def total(self) -> int:
        return sum(self.hits.values())

    def describe(self) -> str:
        if self.clean:
            return "no secrets found"
        return ", ".join(f"{name} x{n}" for name, n in sorted(self.hits.items()))

    # A RedactResult is destructured as `text, hits` at most call sites.
    def __iter__(self):
        return iter((self.text, self.hits))


def redact(
    text: str,
    *,
    channel: str = "unknown",
    cfg: Optional[RedactConfig] = None,
    record: bool = True,
) -> RedactResult:
    """Strip every known secret shape out of `text`. THE one entry point.

    `channel` names where this was headed (mattermost / email / log /
    heartbeat) and is what the counter row carries, so the heartbeat can
    say not just "3 redactions" but which surface nearly leaked.

    `record=False` is for the log guard, and only for it: recording a
    redaction writes a row, writing a row logs on failure, and logging
    goes through the guard. Nothing else may turn the counter off.
    """
    if text is None:
        return RedactResult(text="", hits={})
    cfg = cfg or load_redact_config()
    original = str(text)
    hits: dict[str, int] = {}

    # (start, end, replacement) — claimed, non-overlapping, first wins.
    claims: list[tuple[int, int, str]] = []
    already = _placeholder_re(cfg)

    def _claim(start: int, end: int, name: str) -> bool:
        if start >= end:
            return False
        # REDACTION IS IDEMPOTENT. A span that is already nothing but a
        # placeholder is not a secret — it is this function's own earlier
        # output, reaching it again because a block was redacted before it
        # was assembled into a message that is redacted again. Claiming it
        # would inflate the heartbeat's count with secrets that no longer
        # exist.
        if already.fullmatch(original[start:end]):
            return False
        for c_start, c_end, _ in claims:
            if start < c_end and c_start < end:
                return False          # already covered by an earlier claim
        claims.append((start, end, cfg.placeholder_for(name)))
        hits[name] = hits.get(name, 0) + 1
        return True

    # 1. LITERALS, longest first — see the module docstring.
    guard = load_literals(cfg.literal_min_length)
    for name, value in guard.items():
        if not value:
            continue
        label = f"{LITERAL_PREFIX}{name}"
        start = original.find(value)
        while start != -1:
            _claim(start, start + len(value), label)
            start = original.find(value, start + len(value))

    # 2. PATTERNS, in config order.
    for pattern in cfg.patterns:
        for match in pattern.compiled.finditer(original):
            if pattern.replaces_whole_match:
                span = match.span()
            else:
                # Only the `secret` group goes; everything around it stays,
                # so the line remains diagnosable.
                span = match.span(SECRET_GROUP)
            _claim(span[0], span[1], pattern.name)

    # 3. Build the output once, left to right.
    out_parts: list[str] = []
    cursor = 0
    for start, end, replacement in sorted(claims):
        out_parts.append(original[cursor:start])
        out_parts.append(replacement)
        cursor = end
    out_parts.append(original[cursor:])
    out = "".join(out_parts)

    result = RedactResult(text=out, hits=hits)
    if hits and record:
        _record(channel, hits)
    return result


def _placeholder_re(cfg: RedactConfig) -> re.Pattern:
    """Matches a run of this config's own placeholders (and whitespace).

    Built from the configured placeholder rather than from a literal, so
    changing `placeholder:` in redact.yaml cannot silently break the
    idempotence guarantee above.
    """
    body = re.escape(cfg.placeholder).replace(re.escape("{name}"), r"[^\s\]]+")
    return re.compile(rf"\s*(?:{body}\s*)+")


def _record(channel: str, hits: dict[str, int]) -> None:
    """Count the hit. NEVER let counting break the send.

    The redaction already happened by the time this runs — the text is
    safe whether or not the row lands. Same degradation rule as
    `SessionBlockStore.record`: loud, and non-blocking, in that order.
    """
    from loguru import logger

    try:
        from .store import RedactionStore

        RedactionStore().record(channel=channel, hits=hits)
    except Exception as e:  # noqa: BLE001
        logger.error(
            "F19: {} redaction(s) on channel {} were NOT counted ({}: {}) — the "
            "REDACTION STANDS; only the heartbeat's counter row is missing.",
            sum(hits.values()), channel, type(e).__name__, e,
        )


def install_log_guard() -> None:
    """Route loguru's own output through the redactor (F19: log lines).

    A secret reaches a log file the same way it reaches a DM, and
    `logs/*.log` is read over Tailscale and pasted into reports. This
    patches the formatted message on every record.

    `record=False`: counting a redaction opens a database connection, and
    a database failure logs — which would come straight back through
    here. The DM/email/heartbeat channels do the counting; this one only
    ever prevents.
    """
    from loguru import logger

    def _patch(record):
        try:
            safe = redact(record["message"], channel="log", record=False)
        except Exception:  # noqa: BLE001 - a broken guard must not kill logging
            return
        if not safe.clean:
            record["message"] = safe.text
            record["extra"]["redacted"] = safe.describe()

    logger.configure(patcher=_patch)


__all__ = ["LITERAL_PREFIX", "RedactResult", "install_log_guard", "redact"]
