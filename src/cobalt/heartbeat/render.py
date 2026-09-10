"""F18's block — what he reads, in the note and in the DM.

ONE RENDERER, two destinations. The daily-note block and the Mattermost
DM are the same text: a heartbeat whose two channels could disagree is a
heartbeat you have to check twice.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from cobalt.jobs.watchdog import Finding

from .probes import Probe

#: The L28 unit this writes. Section + stable id: same id every beat, so
#: it updates in place and the note never accumulates 96 blocks a day.
SECTION = "heartbeat"
UNIT = "status"
WRITER = "heartbeat"


@dataclass
class Beat:
    """One heartbeat's whole result."""

    at: datetime
    probes: list[Probe] = field(default_factory=list)
    jobs: list[Finding] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)
    stage_failures: list[str] = field(default_factory=list)
    vault_outcome: str | None = None
    vault_reason: str | None = None
    kill_switch: str | None = None

    @property
    def red_probes(self) -> list[Probe]:
        return [p for p in self.probes if not p.ok]

    @property
    def red_jobs(self) -> list[Finding]:
        return [j for j in self.jobs if not j.ok]

    @property
    def green(self) -> bool:
        return (
            not self.red_probes
            and not self.red_jobs
            and not self.stage_failures
            and self.vault_outcome != "failed"
        )

    @property
    def headline(self) -> str:
        if self.green:
            return (
                f"GREEN — {len(self.jobs)} job(s), {len(self.probes)} probe(s), "
                "nothing red"
            )
        parts = []
        if self.red_jobs:
            parts.append(f"{len(self.red_jobs)} job(s)")
        if self.red_probes:
            parts.append(f"{len(self.red_probes)} probe(s)")
        if self.stage_failures:
            parts.append(f"{len(self.stage_failures)} stage failure(s)")
        if self.vault_outcome == "failed":
            parts.append("vault write")
        return f"RED — {' and '.join(parts)}"

    # -- the two renderings -------------------------------------------

    def note_body(self) -> str:
        """The daily-note unit. Markdown, deterministic, no LLM (L28)."""
        mark = "🟢" if self.green else "🔴"
        lines = [
            f"{mark} **HEARTBEAT {self.headline}** · {self.at:%Y-%m-%d %H:%M:%S %Z}",
            "",
            "| | check | detail |",
            "|---|---|---|",
        ]
        for probe in self.probes:
            icon = "🟢" if probe.ok else ("⚪" if probe.unknown else "🔴")
            lines.append(f"| {icon} | {probe.name} | {_cell(probe.detail)} |")
        for job in self.jobs:
            icon = "🟢" if job.ok else "🔴"
            lines.append(f"| {icon} | `{job.label}` | {job.state} — {_cell(job.detail)} |")
        if self.vault_outcome:
            icon = "🔴" if self.vault_outcome == "failed" else "🟢"
            detail = self.vault_outcome
            if self.vault_reason:
                detail += f" — {self.vault_reason}"
            lines.append(f"| {icon} | vault unit | {_cell(detail)} |")
        for failure in self.stage_failures:
            lines.append(f"| 🔴 | heartbeat stage | {_cell(failure)} |")
        if self.kill_switch:
            lines += ["", f"> {self.kill_switch}"]
        for note in self.notes:
            lines += ["", f"> {note}"]
        return "\n".join(lines)

    def dm_body(self) -> str:
        """The Mattermost DM. Plain lines — a table in a DM is unreadable
        on a phone, and the phone is where a red alert is actually read."""
        head = ("🟢 " if self.green else "🔴 ") + f"COBALT HEARTBEAT {self.headline}"
        lines = [head, f"{self.at:%Y-%m-%d %H:%M:%S %Z}", ""]
        if self.green:
            lines.append(
                f"{len(self.jobs)} jobs and {len(self.probes)} probes all green."
            )
        else:
            lines.append("RED:")
            for item in [*self.red_jobs, *self.red_probes]:
                name = getattr(item, "label", None) or item.name
                detail = item.detail
                lines.append(f"  • {name}: {detail}")
            for failure in self.stage_failures:
                lines.append(f"  • heartbeat stage: {failure}")
            if self.vault_outcome == "failed":
                lines.append(f"  • vault unit: {self.vault_reason or 'write failed'}")
            lines.append("")
            lines.append("Green:")
            for probe in self.probes:
                if probe.ok:
                    lines.append(f"  • {probe.name}: {probe.detail}")
        for note in self.notes:
            lines += ["", note]
        if self.kill_switch:
            lines += ["", self.kill_switch]
        return "\n".join(lines)

    def console(self) -> str:
        lines = [f"HEARTBEAT {self.headline}  ({self.at:%Y-%m-%d %H:%M:%S %Z})", ""]
        lines += [p.line() for p in self.probes]
        lines += [j.line() for j in self.jobs]
        if self.vault_outcome:
            lines.append(
                f"{'RED ' if self.vault_outcome == 'failed' else 'OK  '} "
                f"{'vault unit':<24} {self.vault_outcome}"
                + (f" — {self.vault_reason}" if self.vault_reason else "")
            )
        lines += [f"RED  {'heartbeat stage':<24} {failure}" for failure in self.stage_failures]
        if self.kill_switch:
            lines.append(f"INFO {'kill switch':<24} {self.kill_switch}")
        lines += ["", *self.notes]
        return "\n".join(lines)


def _cell(text: str) -> str:
    """A markdown table cell cannot contain a raw pipe or a newline."""
    return text.replace("|", "\\|").replace("\n", " ").strip()


__all__ = ["SECTION", "UNIT", "WRITER", "Beat"]
