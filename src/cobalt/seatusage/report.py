"""Rendering the seat-usage report: one marked unit per day, plus the
human cells that sit beside it and outlive it.

THE SHAPE, and why it is this shape (L28):

    <!-- cobalt:section seat-usage:2026-09-08 -->
    ### 2026-09-08                        <- seeded once, human-owned
                                             |
    weekly_pct_open:                         | clause 2a template cells
    weekly_pct_close:                        | filled by Dejan, never
                                             | overwritten
    <!-- cobalt:unit seat-usage:2026-09-08 -->
    | model | role hint | ... |             <- rewritten every hour
    <!-- /cobalt:unit seat-usage:2026-09-08 -->
    <!-- /cobalt:section seat-usage:2026-09-08 -->

ONE SECTION PER DAY, not one section holding every day, and that is a
mechanical decision rather than a stylistic one: `upsert_unit` appends a
new unit at the END of its section, and the newest day has to be at the
TOP. A per-day section can be PLACED — the writer's `placement` puts a
missing section wherever a locator says — so newest-on-top comes from
the write path itself instead of from re-sorting a file every hour.

THE HUMAN CELLS ARE SEEDED ONCE AND THEN LEFT ALONE. Not "written with a
merge that lets the human win" — actually left alone, checked before the
write, because the merge's baseline lives in Postgres and a run that
cannot reach Postgres would fall back to treating Cobalt's blank
template as the truth and wipe a filled cell. The guard is the file's
own content, which is always available: if the cells are there, nothing
is written.
"""

from __future__ import annotations

import re
from datetime import date, datetime
from typing import Optional

from cobalt.vaultwrite import Placement

from .ccusage import DayUsage, ModelUsage
from .config import SeatUsageConfig

#: The writer identity on every audit row.
WRITER = "seatusage.report"

#: The line new day-sections are placed directly after. It is a plain
#: HTML comment: invisible in a rendered view, unmissable in the source,
#: and it never moves.
ANCHOR = "<!-- cobalt:days -->"

_ANCHOR_RE = re.compile(r"^\s*<!--\s*cobalt:days\s*-->\s*$")

OPEN_CELL = "weekly_pct_open:"
CLOSE_CELL = "weekly_pct_close:"

_COLUMNS = (
    "| model | role hint | cache read | cache write | output "
    "| API-equivalent $ | Δ since last run |"
)
_RULE = "|---|---|---:|---:|---:|---:|---:|"


def section_name(day: date) -> str:
    return f"seat-usage:{day.isoformat()}"


def unit_id(day: date) -> str:
    return f"seat-usage:{day.isoformat()}"


def human_region_id(day: date, section_text: str) -> str:
    """The audit id for one day's human-cell seed.

    IT CARRIES A HASH OF WHAT IT IS SEEDING INTO, and that is the whole
    point. `upsert_region` merges three ways — stored baseline, on-disk
    text, Cobalt's text — and a seed has nothing to merge: the span it
    writes into is empty by definition, because the runner only seeds
    when the cells are absent. If a baseline for this day survived in
    Postgres while the block left the file (a deleted or truncated
    report), that merge reads an empty span against a non-empty baseline
    as "the human deleted these lines" and keeps them deleted.

    Including the section's own text in the id makes every seed a FRESH
    id with no baseline, so the merge always takes the clean insert
    path. It is deterministic — the same file gives the same id — and it
    never appears in the note: a region is marker-less, so this string
    lives only in `vault_writes`.
    """
    from cobalt.vaultwrite import sha256_text

    return f"seat-usage-human:{day.isoformat()}:{sha256_text(section_text)[:8]}"


def days_anchor() -> Placement:
    """New day-sections land immediately below the anchor — newest on
    top, without rewriting a single line of any older day."""

    def locate(lines: list[str]):
        for i, line in enumerate(lines):
            if _ANCHOR_RE.match(line):
                return (i + 1, i + 1)
        return None

    return Placement(f"immediately after {ANCHOR}", locate)


# ---------------------------------------------------------------------
# the file itself
# ---------------------------------------------------------------------


TEMPLATE = f"""# Seat usage — daily

What the agent seats cost, per model, per day. Written hourly inside
`seat_usage.window` by `com.cobalt.seat-usage`; the tables are generated
and are rewritten in place every run.

**The two cells under each date are yours.** `{OPEN_CELL}` and
`{CLOSE_CELL}` are the weekly-allowance percentages the harnesses show
you at the start and the end of the day — the one number in this file
that no tool on this machine can read. They sit OUTSIDE the generated
unit, they are seeded blank once, and nothing here ever writes them
again once they have a value (L28 clause 2a).

**"API-equivalent $" is not a bill.** The seats run on consumer plans
(L29); this column is what the same tokens would have cost at published
API rates, which is the only comparable number available. Read it as a
size, not as an amount owed.

Newest day first.

{ANCHOR}
"""


# ---------------------------------------------------------------------
# the human cells (seeded once)
# ---------------------------------------------------------------------


def human_body(day: date) -> str:
    """The heading and the two empty cells, exactly as seeded."""
    return "\n".join([f"### {day.isoformat()}", "", OPEN_CELL, CLOSE_CELL, ""])


def human_cells_present(text: str, day: date) -> bool:
    """Are this day's human cells already in the file?

    Answered from the FILE, never from the database. This is the check
    that makes "never overwritten once filled" true even on a run that
    cannot reach Postgres.
    """
    from cobalt.vaultwrite.markers import find_section

    section = find_section(text.split("\n"), section_name(day))
    if section is None:
        return False
    body = section.body(text.split("\n"))
    return any(line.strip().startswith(OPEN_CELL) for line in body)


def human_region_locator(day: date):
    """The span between this day's section-open marker and its unit-open
    marker — everything Cobalt does NOT own inside the day's section.

    Line-based and exact, like every other locator in the write path: it
    matches the two markers by their literal text and returns the lines
    strictly between them. On a section that has just been created that
    span is empty, and an empty span is an insertion point.
    """
    from cobalt.vaultwrite.markers import section_open, unit_open

    open_marker = section_open(section_name(day))
    unit_marker = unit_open(unit_id(day))

    def locate(lines: list[str]):
        try:
            start = lines.index(open_marker) + 1
        except ValueError:
            return None
        for i in range(start, len(lines)):
            if lines[i] == unit_marker:
                return (start, i)
        return None

    return locate


# ---------------------------------------------------------------------
# the generated unit
# ---------------------------------------------------------------------


def _n(value: int) -> str:
    return f"{value:,}"


def _money(model: ModelUsage) -> str:
    if model.cost is None:
        return "**unpriced**"
    if model.free:
        return "$0.00 [^free]"
    return f"${model.cost:,.2f}"


def _delta(model: ModelUsage, previous: Optional[dict]) -> str:
    """Change in API-equivalent $ since the previous run of this job.

    An em dash means "no comparable previous figure", and it is used for
    every case where one does not exist — first run of the day, a model
    that was not in the last snapshot, and either side being unpriced.
    A zero would claim the number held steady, which is a different
    statement from not knowing.
    """
    if model.cost is None or not previous:
        return "—"
    before = (previous.get("models") or {}).get(model.model)
    if not isinstance(before, dict):
        return "—"
    prior = before.get("cost")
    if prior is None:
        return "—"
    diff = model.cost - float(prior)
    if abs(diff) < 0.005:
        return "$0.00"
    return f"{'+' if diff > 0 else '−'}${abs(diff):,.2f}"


def role_hint(cfg: SeatUsageConfig, model: ModelUsage) -> str:
    """Observed seat, then configured role. Never a guess.

    The seat half is a fact ccusage read out of a harness log. The role
    half is standing intent from `configs/cobalt/seat_usage.yaml`. They
    are printed in that order and separated, so a reader can tell which
    half is evidence.
    """
    seats = " + ".join(model.seats) if model.seats else "—"
    role = cfg.role_hint(model.model)
    return f"{seats} · {role}" if role else f"{seats} · —"


def unit_body(
    cfg: SeatUsageConfig,
    usage: DayUsage,
    *,
    now: datetime,
    previous: Optional[dict] = None,
    argv: Optional[list[str]] = None,
) -> str:
    """The whole generated block for one day. Deterministic given its
    inputs — the only thing that moves between two identical runs is the
    timestamp, and that is there so a stale table is visible in the file
    and not only in the heartbeat."""
    lines: list[str] = [_COLUMNS, _RULE]

    if not usage.models:
        lines.append(
            "| _no seat activity recorded_ | — | 0 | 0 | 0 | $0.00 | — |"
        )
    for model in usage.models:
        lines.append(
            f"| `{model.model}` | {role_hint(cfg, model)} | {_n(model.cache_read)} "
            f"| {_n(model.cache_write)} | {_n(model.output_tokens)} "
            f"| {_money(model)} | {_delta(model, previous)} |"
        )

    total = f"${usage.priced_total:,.2f}"
    if usage.unpriced:
        total = f"≥ {total}"
    lines += [
        "",
        f"**Day total (API-equivalent):** {total} · "
        f"**{_n(usage.total_tokens)}** tokens across "
        f"{len(usage.models)} model(s)"
        + (f", seats: {', '.join(usage.seats)}" if usage.seats else ""),
    ]

    input_total = sum(m.input_tokens for m in usage.models)
    lines.append(
        f"**Fresh input tokens:** {_n(input_total)} — not a column above because "
        "it is a rounding error beside cache reads, but it is priced into the "
        "dollar figures."
    )

    if usage.unpriced:
        # LOUD, and every hour it is true — this is not the mainframe
        # case and must not be softened into a footnote.
        lines += [
            "",
            "> **UNPRICED MODELS: "
            + ", ".join(f"`{m}`" for m in usage.unpriced)
            + ".** These were used today and the pinned tool's offline pricing "
            "table has no rate for them, so their cost is missing rather than "
            "zero, and the day total above is a FLOOR. Fix by bumping the pin in "
            "`configs/cobalt/seat_usage.yaml` (a decision, with a diff), never by "
            "letting the job reach the network.",
        ]

    free = [m.model for m in usage.models if m.free]
    if free:
        lines += [
            "",
            "[^free]: "
            + "; ".join(
                f"`{m}` — {cfg.zero_cost_models.get(m, '').strip()}" for m in free
            ),
        ]

    stamp = f"{now:%Y-%m-%d %H:%M %Z}".strip()
    lines += [
        "",
        f"_Generated {stamp} by `{WRITER}` · {cfg.tool.name} "
        f"{usage.tool_version or cfg.tool.version} ({cfg.tool.license}, pinned) · "
        + ("offline pricing, no network at run time" if cfg.tool.offline
           else "ONLINE pricing")
        + "._",
    ]
    if argv:
        lines.append(f"_Command: `{' '.join(argv)}`_")
    return "\n".join(lines)


def snapshot(usage: DayUsage) -> dict:
    """What this run hands the NEXT one so it can compute Δ.

    Lives in the job row's `last_result` rather than in a table of its
    own: the seat-usage job is the only writer and the only reader, and
    a table to remember one dictionary an hour is a table to migrate
    later for nothing (the same call `should_send_green` makes).
    """
    return {
        "day": usage.day.isoformat(),
        "priced_total": round(usage.priced_total, 6),
        "unpriced": list(usage.unpriced),
        "models": {
            m.model: {
                "cost": m.cost,
                "cache_read": m.cache_read,
                "cache_write": m.cache_write,
                "output": m.output_tokens,
            }
            for m in usage.models
        },
    }


def previous_snapshot(raw: Optional[dict], day: date) -> Optional[dict]:
    """The last run's snapshot, but ONLY if it is the same day. A Δ
    against yesterday's totals would be a number that looks like a
    change and is a calendar boundary."""
    if not isinstance(raw, dict):
        return None
    if raw.get("day") != day.isoformat():
        return None
    return raw


__all__ = [
    "ANCHOR",
    "CLOSE_CELL",
    "OPEN_CELL",
    "TEMPLATE",
    "WRITER",
    "days_anchor",
    "human_body",
    "human_cells_present",
    "human_region_id",
    "human_region_locator",
    "previous_snapshot",
    "role_hint",
    "section_name",
    "snapshot",
    "unit_body",
    "unit_id",
]
