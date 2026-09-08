"""One seat-usage run: gate the tool, read the day, write the report.

    uv run cobalt seat-usage run [--dry-run]

WHAT ONE RUN DOES, in order:

1. checks the pinned tool is the pinned tool (L15) and runs it, offline,
   read-only, over the harness logs already on this disk;
2. reads the PREVIOUS run's snapshot out of its own job row, so the Δ
   column compares like with like and only within one day;
3. creates the report file if it is not there, then rewrites TODAY's
   marked unit in place through the L28 writer — same unit id, same
   diff-and-audit path as every other Cobalt write;
4. seeds the day's two human cells exactly once, and never again.

WHY THE REPORT IS A REPO FILE AND STILL GOES THROUGH THE VAULT WRITER.
It is repo content by R3 — versioned, reviewed in a diff, no human note
in the folder. It goes through the writer anyway because the writer is
the only code here that can rewrite half a file hourly while leaving the
other half exactly as its author left it, record the override, and hand
back the diff. See `cobalt.vault.REPO_OWNED_ROOTS`.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Optional

from loguru import logger

from cobalt.session.clock import session_clock

from . import ccusage as ccusage_mod
from . import report as report_mod
from .config import SeatUsageConfig, load_seat_usage_config

JOB_LABEL = "com.cobalt.seat-usage"


@dataclass
class RunOutcome:
    """What the run did, for the console and for the job row."""

    day: date
    usage: "ccusage_mod.DayUsage"
    notes: list[str] = field(default_factory=list)
    unit_action: str = ""
    human_action: str = ""
    diffs: list[str] = field(default_factory=list)

    def console(self) -> str:
        lines = [
            f"seat-usage {self.day.isoformat()} — {len(self.usage.models)} model(s), "
            f"{'≥ ' if self.usage.unpriced else ''}${self.usage.priced_total:,.2f} "
            "API-equivalent",
            f"unit: {self.unit_action}",
        ]
        if self.human_action:
            lines.append(f"human cells: {self.human_action}")
        lines += self.notes
        lines += self.diffs
        return "\n".join(lines)


def today_et(now: Optional[datetime] = None) -> date:
    """The day the report is written FOR — an ET calendar day, because
    every other cadence in this system is ET and a UTC boundary would
    roll the row at 20:00 local."""
    from cobalt.session import clock as clock_mod

    return session_clock().to_et(now or clock_mod.now_utc()).date()


def run(
    *,
    now: Optional[datetime] = None,
    dry_run: bool = False,
    cfg: Optional[SeatUsageConfig] = None,
    day: Optional[date] = None,
    previous: Optional[dict] = None,
) -> RunOutcome:
    """The whole run. Raises on anything it cannot do honestly."""
    from cobalt.vaultwrite import VaultWriter, VaultWriteStore

    from cobalt.session import clock as clock_mod

    cfg = cfg or load_seat_usage_config()
    ts = now or clock_mod.now_utc()
    target_day = day or today_et(ts)
    stamp = session_clock().to_et(ts)

    usage = ccusage_mod.collect(cfg, target_day)
    argv = ccusage_mod.argv(cfg, target_day)

    if previous is None:
        previous = _previous_from_job_row()
    prior = report_mod.previous_snapshot(previous, target_day)

    path = cfg.report_file
    store = VaultWriteStore()
    store.ensure_schema()
    writer = VaultWriter(report_mod.WRITER, store=store, dry_run=dry_run)

    outcome = RunOutcome(day=target_day, usage=usage)

    created = writer.create_if_absent(path, report_mod.TEMPLATE)
    if created.action == "created":
        outcome.notes.append(
            f"report file {'WOULD BE created' if dry_run else 'created'}: {path}"
        )
    if dry_run and not path.exists():
        # Nothing was written, so there is no file for `upsert_unit` to
        # merge into. Say so and stop, rather than raising a REFUSED that
        # reads like a bug in the job.
        outcome.notes.append(
            "DRY RUN and the report file does not exist yet — the unit was not "
            "rendered into it. Run once without --dry-run to create it."
        )
        outcome.unit_action = "not attempted (dry run, no file)"
        return outcome

    body = report_mod.unit_body(
        cfg, usage, now=stamp, previous=prior, argv=argv
    )
    unit_result = writer.upsert_unit(
        path,
        report_mod.section_name(target_day),
        report_mod.unit_id(target_day),
        body,
        placement=report_mod.days_anchor(),
    )
    outcome.unit_action = unit_result.report()
    if unit_result.diff:
        outcome.diffs.append(unit_result.diff)

    # -- the human cells, seeded ONCE -----------------------------------
    # Checked against the FILE, not against the database: the merge's
    # baseline lives in Postgres, and a run that could not read it would
    # treat Cobalt's blank template as the truth and wipe a filled cell.
    text = path.read_text() if path.exists() else ""
    if report_mod.human_cells_present(text, target_day):
        outcome.human_action = "already present — not touched (clause 2a)"
    elif dry_run:
        outcome.human_action = "would be seeded (dry run)"
    else:
        human = writer.upsert_region(
            path,
            report_mod.section_name(target_day),
            report_mod.human_region_id(target_day, text),
            report_mod.human_body(target_day),
            locate=report_mod.human_region_locator(target_day),
        )
        outcome.human_action = human.report()
        if human.diff:
            outcome.diffs.append(human.diff)
        _assert_cells_landed(path, target_day)

    if usage.unpriced:
        logger.error(
            "seat-usage: UNPRICED model(s) {} — the day total is a floor, not a "
            "total. Bump the pinned {} version deliberately; never let the job "
            "reach the network.",
            ", ".join(usage.unpriced),
            cfg.tool.name,
        )
    logger.info(
        "seat-usage: {} — {} model(s), {}${:,.2f} API-equivalent",
        target_day, len(usage.models), "≥" if usage.unpriced else "", usage.priced_total,
    )
    return outcome



def _assert_cells_landed(path, day) -> None:
    """The seed wrote; the cells must now be in the file.

    THE ONE WAY THIS FAILS, and it is worth naming because the symptom
    is silence. `upsert_region` merges three ways: the stored baseline,
    what is on disk, and what Cobalt wants. If the report FILE loses a
    day's block while that day's baseline row survives in Postgres, the
    merge reads an empty span against a non-empty baseline as "the human
    deleted these lines", keeps them deleted, and reports `unchanged` —
    the correct answer to the question it was asked, and the wrong
    outcome here.

    A day block with no cells under it is a plausible-empty artifact:
    Dejan would find nowhere to write his percentages and nothing would
    have said so. So the run FAILS instead, loudly, with the fix — which
    is his to make, because they are his cells and Cobalt owning the
    repair would be Cobalt owning the cells.
    """
    from cobalt.vaultwrite import VaultWriteError

    if report_mod.human_cells_present(path.read_text(), day):
        return
    raise VaultWriteError(
        f"REFUSED to leave {path} with a {day.isoformat()} block and no human "
        f"cells under it. The seed wrote nothing because a stale audit baseline "
        f"for section {report_mod.section_name(day)} disagrees with the file — "
        "which happens when the report file was deleted or truncated while its "
        "`vault_writes` history survived.\n"
        "FIX (one line, and it is yours to make): paste these two lines into the "
        f"file directly under `### {day.isoformat()}`, then re-run —\n"
        f"    {report_mod.OPEN_CELL}\n"
        f"    {report_mod.CLOSE_CELL}\n"
        "Every later run leaves them alone; the presence check reads the file."
    )


def _previous_from_job_row() -> Optional[dict]:
    """The previous run's snapshot. A missing row, an unreachable
    database or a first run all mean the same thing to the Δ column —
    "no comparable figure" — and it renders as an em dash rather than as
    a zero."""
    try:
        from cobalt.jobs.store import JobStore

        return JobStore().last_result(JOB_LABEL)
    except Exception as e:  # noqa: BLE001
        logger.warning(
            "seat-usage: could not read the previous run's snapshot ({}: {}) — the "
            "Δ column will read as unknown for this run.", type(e).__name__, e
        )
        return None


def run_as_job() -> RunOutcome:
    """The plist's entry point: the same run, inside the F17 wrapper, so
    it gets a `running`/`done` row, a heartbeat and an exit code.

    A DRY RUN NEVER COMES THROUGH HERE. `--dry-run` writes nothing, and
    a job row saying a run completed when it deliberately did nothing
    would make the freshness probe below green on the strength of a
    rehearsal.
    """
    from cobalt.jobs.wrapper import job_run

    with job_run(JOB_LABEL) as job:
        outcome = run()
        job.result = report_mod.snapshot(outcome.usage)
    return outcome


__all__ = ["JOB_LABEL", "RunOutcome", "run", "run_as_job", "today_et"]
