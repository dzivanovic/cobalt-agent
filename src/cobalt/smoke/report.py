"""Renders and writes `docs/40 - DevDocs/reports/<suite>-smoke-<date>.md`.

Same file discipline as day-open's report (L48): written in the same
turn the checks run, a plain repo file (no `VaultWriter`, no markers),
never replacing an existing report — a second run the same day lands
beside it as `…-<HHMMSS>.md`. The hub commits it under L51(2).

Layout: the run's variables (so every rendered command is replayable),
the numbered verdict table (# | check | verdict | evidence), OVERALL,
then one section per check with its exact command, expected output and
the raw evidence — the hand fallback runs from this file alone (R6 A).
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from cobalt.dayopen.report import REPORTS_DIR
from cobalt.session.clock import SessionClock, now_utc

from .models import CheckOutcome, SmokeContext, SmokeReport, overall_verdict


class ReportPathError(RuntimeError):
    """A smoke report would replace a file or land outside `reports/`."""


def build_report(suite: str, title: str, ctx: SmokeContext, outcomes: list[CheckOutcome],
                 *, generated_at: datetime | None = None) -> SmokeReport:
    return SmokeReport(
        suite=suite, title=title, context=ctx, generated_at=generated_at or ctx.now,
        checks=outcomes, overall=overall_verdict(outcomes),
    )


def report_path(rep: SmokeReport, *, reports_dir: Path) -> Path:
    return reports_dir / f"{rep.suite}-smoke-{rep.context.report_date:%Y-%m-%d}.md"


def _cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def render_table(rep: SmokeReport) -> str:
    lines = ["| # | check | verdict | evidence |", "|---|---|---|---|"]
    lines += [f"| {c.id} | {_cell(c.title)} | {c.verdict.value} | {_cell(c.detail)} |" for c in rep.checks]
    return "\n".join(lines + ["", f"OVERALL: {rep.overall.value}"])


def render_markdown(rep: SmokeReport) -> str:
    parts = [
        f"# {rep.title.upper()} {rep.context.report_date:%Y-%m-%d}",
        f"Generated: {SessionClock.to_et(rep.generated_at):%Y-%m-%d %H:%M:%S %Z} · "
        f"`cobalt smoke {rep.suite}` · configs/cobalt/smoke/{rep.suite}.yaml",
        "",
        "## Variables",
        *[f"- {key}: {value}" for key, value in rep.context.printable().items()],
        "",
        "## VERDICT",
        render_table(rep),
        "",
        "Rule: RED any ERROR · AMBER any FAIL · GREEN otherwise; KNOWN never lowers it. "
        f"{rep.suite.upper()} done = GREEN only.",
        "",
    ]
    for c in rep.checks:
        parts += [
            f"## {c.id} {c.title} — {c.verdict.value}",
            f"- kind: {c.kind}",
            f"- command: `{c.command}`",
            f"- expected: {c.expected}",
            f"- verdict detail: {c.detail}",
            "```",
            c.raw if c.raw else "(no output captured)",
            "```",
            "",
        ]
    return "\n".join(parts)


def render_json(rep: SmokeReport) -> str:
    return json.dumps(
        {
            "suite": rep.suite,
            "report_date": rep.context.report_date.isoformat(),
            "generated_at": rep.generated_at.isoformat(),
            "variables": rep.context.printable(),
            "overall": rep.overall.value,
            "checks": [
                {"id": c.id, "title": c.title, "kind": c.kind, "verdict": c.verdict.value,
                 "detail": c.detail, "command": c.command, "expected": c.expected}
                for c in rep.checks
            ],
        },
        indent=2,
    )


def write_report(rep: SmokeReport, *, reports_dir: Path | None = None) -> Path:
    reports_dir = reports_dir or REPORTS_DIR
    reports_dir.mkdir(parents=True, exist_ok=True)
    path = report_path(rep, reports_dir=reports_dir)
    if path.exists():
        stamp = SessionClock.to_et(now_utc()).strftime("%H%M%S")
        path = path.with_name(f"{path.stem}-{stamp}.md")
    if path.resolve().parent != reports_dir.resolve():
        raise ReportPathError(f"refusing to write {path} outside {reports_dir}")
    try:
        with path.open("x") as f:
            f.write(render_markdown(rep))
    except FileExistsError as e:
        raise ReportPathError(f"refusing to replace {path} — a smoke report is never overwritten") from e
    return path


__all__ = [
    "REPORTS_DIR", "ReportPathError", "build_report", "render_json", "render_markdown",
    "render_table", "report_path", "write_report",
]
