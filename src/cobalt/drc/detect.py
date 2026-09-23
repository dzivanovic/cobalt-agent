"""The ONE header classifier (DRC D1-2a, R114 / R17 (5)).

Every import path — the `/drc` upload and the hand-dropped files of
`_imports/drc/<date>/` (D2) — and every test asks THIS module what a
file is (L3). It reads ONLY the first line. It NEVER reads the name or
the extension: his files end `.md` because Obsidian hides `.csv`, and he
names them differently every day. `name` is carried for messages only.

THE HEADER. The first line, decoded as UTF-8 (a BOM stripped, a CR
before the LF dropped), split as ONE CSV record. A single trailing
empty cell — E1's trading-log header ends with the delimiter — is
ignored for classification.

THE REQUIRED SETS are owned by the parser modules
(`trading_log.REQUIRED`, `stats_log.REQUIRED`), imported here and never
copied. The names both kinds share are COMPUTED from the two constants
(E1: `Symbol`, `Side`) and decide nothing.

OUTCOMES, deterministic:
- every name of ONE kind present → that kind, `parsed` (extra names →
  still that kind, with `<kind>_shape` naming the extras — L9);
- every name of BOTH kinds → `failed: header matches both kinds`;
- some names of a kind, no kind complete → decided ONLY by the names
  UNIQUE to one kind: one kind's unique names present → `partial`, with
  `missing` in that kind's column order and the loud flag `PARTIAL —
  missing: <columns>` (R17 (5): the file IS parsed on what it has);
  both kinds' unique names → `failed: header matches both kinds`;
- only shared names, or none → `ignored: <name> — header matches neither
  kind`; an undecodable first line → `ignored: <name> — not text`.
  Ignored files are listed, never parsed.
"""

from __future__ import annotations

import csv
import re
from datetime import date
from pathlib import Path
from typing import Iterable, Literal

from pydantic import BaseModel, ConfigDict, Field

from .models import Detection, Kind, Outcome
from .stats_log import REQUIRED as STATS_REQUIRED
from .trading_log import REQUIRED as TRADING_REQUIRED

REQUIRED: dict[Kind, tuple[str, ...]] = {
    Kind.TRADING_LOG: TRADING_REQUIRED,
    Kind.STATS_LOG: STATS_REQUIRED,
}

#: The names in both sets. Computed, never typed.
SHARED: frozenset[str] = frozenset(TRADING_REQUIRED) & frozenset(STATS_REQUIRED)

_UNIQUE: dict[Kind, frozenset[str]] = {
    kind: frozenset(names) - SHARED for kind, names in REQUIRED.items()
}

_BOTH = "header matches both kinds"
_NEITHER = "header matches neither kind"


def _header(data: bytes) -> list[str] | None:
    """The first line as one CSV record, or None when it is not text."""
    first = data.split(b"\n", 1)[0]
    if first.endswith(b"\r"):
        first = first[:-1]
    if b"\x00" in first:
        return None
    try:
        text = first.decode("utf-8-sig")
    except UnicodeDecodeError:
        return None
    if text == "":
        return []
    return next(csv.reader([text]))


def detect_kind(name: str, data: bytes) -> Detection:
    """What `data` is, from its first line alone. `name` is never read
    for the decision — it only labels the verdict."""
    cells = _header(data)
    if cells is None:
        return Detection(name=name, outcome=Outcome.IGNORED, reason=f"ignored: {name} — not text")
    if cells and cells[-1] == "":
        cells = cells[:-1]
    names = set(cells)

    complete = [k for k, req in REQUIRED.items() if set(req) <= names]
    if len(complete) == 2:
        return Detection(name=name, outcome=Outcome.FAILED, reason=f"failed: {name} — {_BOTH}")
    if complete:
        kind = complete[0]
        outcome = Outcome.PARSED
    else:
        touched = [k for k, unique in _UNIQUE.items() if unique & names]
        if len(touched) == 2:
            return Detection(name=name, outcome=Outcome.FAILED, reason=f"failed: {name} — {_BOTH}")
        if not touched:
            return Detection(name=name, outcome=Outcome.IGNORED, reason=f"ignored: {name} — {_NEITHER}")
        kind = touched[0]
        outcome = Outcome.PARTIAL

    required = REQUIRED[kind]
    duplicated = sorted({c for c in cells if c in required and cells.count(c) > 1})
    if duplicated:
        return Detection(
            name=name,
            kind=kind,
            outcome=Outcome.FAILED,
            reason=f"failed: {name} — duplicate column(s): {', '.join(duplicated)}",
        )
    missing = [c for c in required if c not in names]
    extras = [c for c in cells if c not in required]
    if outcome is Outcome.PARTIAL:
        reason = f"PARTIAL — missing: {', '.join(missing)}"
    else:
        reason = f"{kind.value}: header complete"
    if extras:
        reason += f"; degraded: {kind.value}_shape — extra: {', '.join(extras)}"
    return Detection(name=name, kind=kind, outcome=outcome, reason=reason, missing=missing, extras=extras)


class SetDetection(BaseModel):
    """A folder listing or a multi-file drop, classified as ONE set."""

    model_config = ConfigDict(frozen=True)

    status: Literal["pass", "failed", "incomplete"]
    reason: str
    by_kind: dict[Kind, Detection] = Field(default_factory=dict)
    partial: list[Detection] = Field(default_factory=list)
    ignored: list[Detection] = Field(default_factory=list)
    failed: list[Detection] = Field(default_factory=list)


def detect_set(files: Iterable[tuple[str, bytes]]) -> SetDetection:
    """Exactly one file per kind (complete or `partial`) → `pass`. Two of
    one kind → `FAILED: <kind> ambiguous — <name 1>, <name 2>`: both
    named, neither picked. Every ignored, partial and failed file is
    listed either way."""
    detections = [detect_kind(name, data) for name, data in files]
    per_kind: dict[Kind, list[Detection]] = {k: [] for k in Kind}
    for d in detections:
        if d.kind is not None and d.outcome in (Outcome.PARSED, Outcome.PARTIAL):
            per_kind[d.kind].append(d)
    lists = dict(
        partial=[d for d in detections if d.outcome is Outcome.PARTIAL],
        ignored=[d for d in detections if d.outcome is Outcome.IGNORED],
        failed=[d for d in detections if d.outcome is Outcome.FAILED],
    )
    ambiguous = [k for k in Kind if len(per_kind[k]) > 1]
    if ambiguous:
        reason = "; ".join(
            f"FAILED: {k.value} ambiguous — {', '.join(d.name for d in per_kind[k])}" for k in ambiguous
        )
        chosen = {k: v[0] for k, v in per_kind.items() if len(v) == 1}
        return SetDetection(status="failed", reason=reason, by_kind=chosen, **lists)
    chosen = {k: v[0] for k, v in per_kind.items() if v}
    absent = [k.value for k in Kind if k not in chosen]
    if absent:
        return SetDetection(
            status="incomplete", reason=f"no {' / '.join(absent)} file in the set", by_kind=chosen, **lists
        )
    return SetDetection(status="pass", reason="one file per kind", by_kind=chosen, **lists)


_DATE_FOLDER = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")


def import_folder_date(folder_name: str) -> date | None:
    """The import date a folder of `_imports/drc/` names, or None. ONLY a
    `YYYY-MM-DD` folder is an import folder; `_reference/` and anything
    else is never an input."""
    m = _DATE_FOLDER.match(folder_name)
    if not m:
        return None
    try:
        return date(int(m[1]), int(m[2]), int(m[3]))
    except ValueError:
        return None


def import_folders(root: Path) -> list[Path]:
    """The `YYYY-MM-DD` folders directly under `root`, oldest first. The
    one rule D2's folder reader applies; it lists, it opens nothing."""
    return sorted(
        (p for p in root.iterdir() if p.is_dir() and import_folder_date(p.name) is not None),
        key=lambda p: p.name,
    )


__all__ = [
    "REQUIRED",
    "SHARED",
    "SetDetection",
    "detect_kind",
    "detect_set",
    "import_folder_date",
    "import_folders",
]
