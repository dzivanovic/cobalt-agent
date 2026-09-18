"""The ONE miss line — unit `drc-misses/miss_line` in that day's DRC note
(S2-P4 STEP-7, R5, R1-18).

    Misses YYYY-MM-DD: cards N (unarmed a · passed b · not_filled c · window d · rule_10 e)
      · cf-R Σ ±x.xR, n=N · avg: insufficient data (n<30)
      · movers ≥ m%: K not in play — T1 +12.3% not_in_any_source · T2 −9.8% config_cap · T3 … (+J more)
      · formations: unavailable until S2-P2

(one line in the note; wrapped here). It is rendered ONLY from the run's
own reconciled current set, so the line and `job.result` cannot disagree.

Once S2-P2's replay is bound the formation segment carries its own count
and cf-R sum — the plan wrote only the unavailable text, so this is its
extension, in the same shape as the card segment:

    · formations: 2 not taken (no_card) · cf-R Σ −29.9R, n=2
      [· suppressed K] [· input_stale K]

A suppressed formation (an open radar card already covers that member,
def and direction) is NOT a second miss — it is surfaced on the line only
as its count, and in `job.result` in full.

L8: the cf-R sum always carries its n; an average renders only at n >= 30,
otherwise `avg: insufficient data (n<30)`. R1-12: a nonzero input_stale
count is printed on the line — a card that could not be replayed is never
a silent zero.

L28, through the one write path. `VaultWriter.upsert_unit` — versioned,
diffed, human-wins, sync-revert aware, mtime-guarded — into an EXISTING
note only: replay never calls `create_if_absent`. The DRC note belongs to
prefill-drc; absent -> `DrcNoteAbsent`, loud, nothing created. The first
write places the section ZERO-WIDTH right after the `drc-rules` section's
closing marker, touching no human line; a note without that anchor takes
the writer's own safe fallback (appended at the end, noted in the result).
"""

from __future__ import annotations

from datetime import date
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path
from typing import Any, Optional, Sequence

from cobalt.settings.models import BenchmarkSettings
from cobalt.vault import resolve_vault_path
from cobalt.vaultwrite import Placement, VaultWriter, WriteResult
from cobalt.vaultwrite.markers import find_section

from .models import FORMATION_UNAVAILABLE, ReplayError

SECTION = "drc-misses"
UNIT = "miss_line"
ANCHOR_SECTION = "drc-rules"
WRITER = "replay.nightly"

#: The ruled template shows three movers, then "(+J more)".
MOVERS_SHOWN = 3
#: L8's floor for an average.
MIN_N_FOR_AVERAGE = 30
CARD_GATES = ("unarmed", "passed", "not_filled", "window", "rule_10")
MINUS = "−"


class DrcNoteAbsent(ReplayError):
    """The day's DRC note does not exist. prefill-drc creates it; replay never does."""

    def __init__(self, path: Path):
        super().__init__(f"DRC note absent — prefill-drc owns creation ({path})")
        self.path = path


def _signed(value: Decimal, places: str, suffix: str) -> str:
    q = value.quantize(Decimal(places), rounding=ROUND_HALF_UP)
    return f"{'+' if q >= 0 else MINUS}{abs(q)}{suffix}"


def _plain(value: Decimal) -> str:
    text = format(value.normalize(), "f")
    return text


def render_line(
    trade_date: date,
    *,
    card_rows: Sequence[dict[str, Any]],
    mover_rows: Sequence[dict[str, Any]],
    settings: Optional[BenchmarkSettings],
    formation_replay: str,
    input_stale: int,
    formation_rows: Sequence[dict[str, Any]] = (),
    formation_suppressed: int = 0,
    formation_input_stale: int = 0,
) -> str:
    """The line body. `card_rows`/`mover_rows` are CURRENT `"user".missed` rows."""
    counts = {gate: 0 for gate in CARD_GATES}
    for row in card_rows:
        counts[row["excluded_by"]] = counts.get(row["excluded_by"], 0) + 1
    cards = f"cards {len(card_rows)} (" + " · ".join(f"{g} {counts[g]}" for g in CARD_GATES) + ")"
    parts = [f"Misses {trade_date.isoformat()}: {cards}"]
    if input_stale:
        parts.append(f"input_stale {input_stale}")

    rs = [Decimal(str(row["cf_r"])) for row in card_rows if row.get("cf_r") is not None]
    n = len(rs)
    total = sum(rs, Decimal(0))
    parts.append(f"cf-R Σ {_signed(total, '0.1', 'R')}, n={n}")
    if n >= MIN_N_FOR_AVERAGE:
        parts.append(f"avg {_signed(total / n, '0.01', 'R')}")
    else:
        parts.append(f"avg: insufficient data (n<{MIN_N_FOR_AVERAGE})")

    if settings is None:
        parts.append("movers: unavailable")
    else:
        ordered = sorted(
            mover_rows, key=lambda r: (-abs(Decimal(str(r["gate_detail"]["change_pct"]))), r["ticker"])
        )
        shown = [
            f"{r['ticker']} {_signed(Decimal(str(r['gate_detail']['change_pct'])), '0.1', '%')} {r['excluded_by']}"
            for r in ordered[:MOVERS_SHOWN]
        ]
        segment = f"movers ≥ {_plain(settings.min_move_pct)}%: {len(ordered)} not in play"
        if shown:
            segment += " — " + " · ".join(shown)
            if len(ordered) > MOVERS_SHOWN:
                segment += f" (+{len(ordered) - MOVERS_SHOWN} more)"
        parts.append(segment)

    if formation_replay == FORMATION_UNAVAILABLE:
        parts.append("formations: unavailable until S2-P2")
    else:
        rs = [Decimal(str(row["cf_r"])) for row in formation_rows if row.get("cf_r") is not None]
        segment = (f"formations: {len(formation_rows)} not taken (no_card) · "
                   f"cf-R Σ {_signed(sum(rs, Decimal(0)), '0.1', 'R')}, n={len(rs)}")
        if formation_suppressed:
            segment += f" · suppressed {formation_suppressed}"
        if formation_input_stale:
            segment += f" · input_stale {formation_input_stale}"
        parts.append(segment)
    return " · ".join(parts)


def _after_rules(lines: list[str]) -> Optional[tuple[int, int]]:
    section = find_section(lines, ANCHOR_SECTION)
    if section is None:
        return None
    return (section.close_line + 1, section.close_line + 1)


def after_drc_rules() -> Placement:
    """Zero-width, immediately after the `drc-rules` closing marker."""
    return Placement(f"after the {ANCHOR_SECTION} section's closing marker", _after_rules)


def drc_note_path(trade_date: date) -> Path:
    """`prefill.yaml` review_dir + drc_filename_pattern, in the resolved vault.
    Absent -> `DrcNoteAbsent` (nothing is ever created here)."""
    from cobalt.prefill.config import load_prefill_paths

    paths = load_prefill_paths()
    path = resolve_vault_path() / paths.review_dir / trade_date.strftime(paths.drc_filename_pattern)
    if not path.is_file():
        raise DrcNoteAbsent(path)
    return path


def write_miss_line(path: Path, body: str, *, writer: VaultWriter) -> WriteResult:
    """Upsert the unit through the one write path. Never creates the note."""
    path = Path(path)
    if not path.is_file():
        raise DrcNoteAbsent(path)
    return writer.upsert_unit(path, SECTION, UNIT, body, placement=after_drc_rules())


__all__ = [
    "ANCHOR_SECTION", "DrcNoteAbsent", "MIN_N_FOR_AVERAGE", "MOVERS_SHOWN", "SECTION", "UNIT", "WRITER",
    "after_drc_rules", "drc_note_path", "render_line", "write_miss_line",
]
