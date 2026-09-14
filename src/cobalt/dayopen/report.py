"""Renders and writes `docs/40 - DevDocs/reports/day-open-<date>.md`.

L48 (evidence in the report file): the report is written in the SAME
turn as the checks run, before anything is summarised in chat. Nothing
here touches the vault or the database — this is a plain repo file,
written directly, no `VaultWriter`, no marker units.
"""

from __future__ import annotations

import json
from pathlib import Path

from .models import CheckResult, DayOpenReport

REPO_ROOT = Path(__file__).resolve().parents[3]
REPORTS_DIR = REPO_ROOT / "docs" / "40 - DevDocs" / "reports"


class ReportPathError(RuntimeError):
    """A day-open report path was asked to write/append outside `reports/`."""


def report_path(report_date, *, reports_dir: Path = REPORTS_DIR) -> Path:
    return reports_dir / f"day-open-{report_date:%Y-%m-%d}.md"


def _assert_under_reports_dir(path: Path, *, reports_dir: Path = REPORTS_DIR) -> None:
    resolved_dir = reports_dir.resolve()
    resolved_path = path.resolve()
    if resolved_path.parent != resolved_dir:
        raise ReportPathError(
            f"refusing to write {path} — day-open reports live only directly under "
            f"{resolved_dir}"
        )


def _verdict_table(checks: list[CheckResult]) -> str:
    lines = ["| id | check | verdict | detail |", "|---|---|---|---|"]
    for c in checks:
        detail = c.detail.split(" — ", 1)[-1] if " — " in c.detail else c.detail
        lines.append(f"| {c.id} | {c.title} | {c.verdict.value} | {detail} |")
    return "\n".join(lines)


def render_verdict_section(report: DayOpenReport) -> str:
    return "\n".join(
        ["## VERDICT", _verdict_table(report.checks), "", f"OVERALL: {report.overall.value}"]
    )


def render_markdown(report: DayOpenReport) -> str:
    parts = [
        f"# DAY-OPEN {report.report_date:%Y-%m-%d}",
        f"Generated: {report.generated_at:%Y-%m-%d %H:%M:%S %Z}",
        "",
    ]
    for c in report.checks:
        parts.append(f"## {c.id} {c.title}")
        parts.append("```")
        parts.append(c.raw if c.raw else "(no output captured)")
        parts.append("```")
        parts.append("")
    parts.append(render_verdict_section(report))
    parts.append("")
    return "\n".join(parts)


def render_json(report: DayOpenReport) -> str:
    return json.dumps(
        {
            "report_date": report.report_date.isoformat(),
            "generated_at": report.generated_at.isoformat(),
            "overall": report.overall.value,
            "checks": [
                {"id": c.id, "title": c.title, "verdict": c.verdict.value, "detail": c.detail}
                for c in report.checks
            ],
        },
        indent=2,
    )


def write_report(report: DayOpenReport, *, reports_dir: Path = REPORTS_DIR) -> Path:
    """Write the markdown report, create-if-absent's simpler cousin: this
    is a repo file day-open owns outright (not a marker-bounded unit in a
    human's vault note), so every run OVERWRITES its own day's file —
    there is nothing here for a human to have edited."""
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = report_path(report.report_date, reports_dir=reports_dir)
    _assert_under_reports_dir(path, reports_dir=reports_dir)
    path.write_text(render_markdown(report))
    return path


def append_verdict(report_date, line: str, *, reports_dir: Path = REPORTS_DIR) -> Path:
    """`cobalt day-open verdict "<line>"` — the local seat's one write
    path, through Cobalt, not the shell. Refuses if today's report does
    not exist yet: there is nothing to add a verdict on top of."""
    path = report_path(report_date, reports_dir=reports_dir)
    _assert_under_reports_dir(path, reports_dir=reports_dir)
    if not path.exists():
        raise ReportPathError(
            f"no report at {path} — run `cobalt day-open` for {report_date} first."
        )
    with path.open("a") as f:
        f.write(f"\nSEAT VERDICT: {line}\n")
    return path


__all__ = [
    "REPORTS_DIR",
    "ReportPathError",
    "append_verdict",
    "render_json",
    "render_markdown",
    "render_verdict_section",
    "report_path",
    "write_report",
]
