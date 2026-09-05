"""F6 in the daily note — the sheet-mode line, both directions (L28).

WHAT THIS REPLACES. Slice 2 shipped one static string in
`prefill/daily.py`:

    "Sheet mode: [ ] FULL [ ] HALF — .htk loaded: [ ] full [ ] half"

Four markdown checkboxes that read nothing, compare nothing, persist
nothing and refuse nothing. A trader ticking one of them was talking to
a text file. That line is deleted; this module owns what stands in its
place, and it goes BOTH ways:

* **Cobalt -> note.** The day mode in force, the stage it came from, the
  sheet it sizes from, the keys it permits, and one checkbox per declared
  sheet with the attested one ticked. Written as a Cobalt-owned UNIT
  (`section daymode` / `unit sheet_mode`) through `VaultWriter` — stable
  id, update in place, human text beside it preserved, versioned to
  `vault_writes`, unified diff in the report. L28, not a second writer.
* **Note -> Cobalt.** A box HE ticks is an attestation. It is read back
  at the next sheet request and persisted to the `day_modes` row, so
  ticking `full.htk` in Obsidian on the trading PC is the same act as
  choosing it in the banner selector.

CONFLICT IS A REFUSAL, NOT A MERGE. If the note says one sheet and the
stored attestation says another, neither wins: `reconcile()` raises with
BOTH shown and the sheet refuses cards until he settles it. Picking one
silently is how a full-size key gets pressed on a reduced-size day, and
"the note is stale" and "the selector is stale" are indistinguishable
from inside the process. Two ticks in the note are the same refusal for
the same reason.

The checkbox list is DERIVED from `cfg.hotkey_file_names`, so a sheet
added to `configs/cobalt/aset.yaml` gets a checkbox with no edit here.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any, Optional

from loguru import logger

from cobalt.vaultwrite import VaultWriter, VaultWriteStore, WriteResult
from cobalt.vaultwrite.markers import find_section

from .config import DayModeConfig, load_daymode_config

#: The marker names this module owns. `sheet_mode` is the unit id the
#: daily-note template carries and the one this module updates in place.
SECTION = "daymode"
UNIT = "sheet_mode"

#: The writer name that lands on every `vault_writes` row from here.
WRITER = "daymode.note"

_CHECKBOX_RE = re.compile(r"^\s*-\s*\[(?P<tick>[ xX])\]\s*(?P<file>\S+\.htk)\b")


class NoteAttestationConflict(RuntimeError):
    """The note and the stored attestation disagree — refuse, show both."""


@dataclass(frozen=True)
class NoteAttestation:
    """What the note says, and why."""

    file: Optional[str]
    ticked: list[str]

    @property
    def ambiguous(self) -> bool:
        return len(self.ticked) > 1


# ---------------------------------------------------------------------
# Cobalt -> note
# ---------------------------------------------------------------------


def render_body(
    cfg: DayModeConfig,
    mode: str,
    *,
    stage: str,
    attested: Optional[str] = None,
    row: Optional[dict[str, Any]] = None,
) -> str:
    """The unit body. Deterministic, no LLM in the write path (L28)."""
    sheet = cfg.sheet_for(mode)
    keys = ", ".join(g.value for g in cfg.enabled_grades_for(mode))
    lines = [
        f"**Day mode: {mode.upper()}** — {stage} · sizes from the "
        f"{sheet.upper()} sheet · keys {keys}",
        "",
    ]
    proposed = (row or {}).get("proposed")
    decided = (row or {}).get("decided")
    if decided:
        line = f"09:00 proposal: {proposed or '-'} → decided **{decided}**"
        if (row or {}).get("overrule_reason"):
            line += f" (overrule: {row['overrule_reason']})"
        lines.append(line)
    elif proposed:
        lines.append(
            f"09:00 proposal: **{proposed}** — undecided, so the stage-1 floor holds."
        )
    else:
        lines.append(
            f"No 09:00 proposal yet — stage-1 system rule: the lowest enabled rung "
            f"({cfg.lowest_enabled})."
        )
    lines.extend(
        [
            "",
            ".htk loaded — tick ONE (Cobalt reads this back as your attestation; "
            "it never reads DAS):",
        ]
    )
    for name in cfg.hotkey_file_names:
        tick = "x" if name == attested else " "
        lines.append(f"- [{tick}] {name}")
    return "\n".join(lines)


def write(
    path: Path,
    cfg: DayModeConfig,
    mode: str,
    *,
    stage: str,
    attested: Optional[str] = None,
    row: Optional[dict[str, Any]] = None,
    dry_run: bool = False,
    store: Optional[VaultWriteStore] = None,
) -> Optional[WriteResult]:
    """Update the note's sheet-mode unit. None when there is no note.

    `upsert_unit` REFUSES to create a note (L28.1 — only
    `create_if_absent` with a template may), so a missing daily note is
    reported loudly and skipped rather than conjured from here. The
    05:15 prefill is what creates the day's note.
    """
    path = Path(path)
    if not path.exists():
        logger.error(
            "daymode note: {} does not exist — the sheet-mode unit was NOT written. "
            "The 05:15 prefill (com.cobalt.prefill-daily) creates the day's note; "
            "this writer never creates one (L28.1).",
            path,
        )
        return None
    if store is None:
        store = VaultWriteStore()
        store.ensure_schema()
    writer = VaultWriter(WRITER, store=store, dry_run=dry_run)
    return writer.upsert_unit(
        path,
        SECTION,
        UNIT,
        render_body(cfg, mode, stage=stage, attested=attested, row=row),
    )


# ---------------------------------------------------------------------
# note -> Cobalt
# ---------------------------------------------------------------------


def read_attestation(text: str, cfg: Optional[DayModeConfig] = None) -> NoteAttestation:
    """Which `.htk` box is ticked in the note. Never guesses.

    Only boxes inside Cobalt's own unit count. A checkbox somewhere else
    in his journal is his prose, and reading it would make any line
    containing `[x] full.htk` into a risk decision.
    """
    cfg = cfg or load_daymode_config()
    known = set(cfg.hotkey_file_names)
    lines = text.split("\n")
    block = find_section(lines, SECTION)
    if block is None:
        return NoteAttestation(file=None, ticked=[])
    unit = block.units.get(UNIT)
    if unit is None:
        return NoteAttestation(file=None, ticked=[])

    ticked: list[str] = []
    for line in unit.body(lines):
        m = _CHECKBOX_RE.match(line)
        if not m or m.group("tick") == " ":
            continue
        name = m.group("file")
        # An unknown file name in a ticked box is NOT an attestation and
        # NOT silently dropped-as-noise: it is a name that does not
        # correspond to a declared sheet, so it can only be stale.
        if name not in known:
            logger.error(
                "daymode note: ticked hotkey file {!r} is not a declared sheet file "
                "({}) — ignored as an attestation. The note is stale; re-run the "
                "sheet-mode writer.",
                name,
                ", ".join(sorted(known)),
            )
            continue
        ticked.append(name)
    return NoteAttestation(file=ticked[0] if len(ticked) == 1 else None, ticked=ticked)


def reconcile(note: NoteAttestation, stored: Optional[str]) -> Optional[str]:
    """The attestation in force, or a refusal naming both sides.

    * note silent          -> whatever is stored (possibly nothing)
    * note ticked, none stored -> the note IS the attestation
    * both, and they agree -> that one
    * both, and they differ -> REFUSE, showing both
    * two boxes ticked     -> REFUSE, showing them
    """
    if note.ambiguous:
        raise NoteAttestationConflict(
            f"REFUSED: {len(note.ticked)} hotkey files are ticked in today's daily "
            f"note ({', '.join(note.ticked)}). An attestation is a statement about "
            "ONE loaded key table; two ticks is not a smaller claim, it is no claim. "
            "Untick until one remains."
        )
    if note.file and stored and note.file != stored:
        raise NoteAttestationConflict(
            f"REFUSED: the daily note says {note.file} and the attestation on record "
            f"says {stored}. Cobalt will not pick one — 'the note is stale' and 'the "
            "selector is stale' look identical from here, and guessing is exactly how "
            "a full-size key gets pressed on a reduced-size day. Settle it: tick the "
            "right box in the note, or re-attest on the sheet."
        )
    return note.file or stored


def daily_note_path(day: Optional[date] = None) -> Path:
    """Today's daily note, through the ONE vault resolver + ASET config.

    Local imports: `prefill.vault_writer` imports the vault resolver and
    `aset.config` is imported by `daymode.config` — keeping both calls
    inside the function avoids an import cycle with `prefill.daily`,
    which imports THIS module for the template body.
    """
    from datetime import datetime

    from cobalt.aset.config import load_config as load_aset_config
    from cobalt.prefill.vault_writer import resolve_target

    cfg = load_aset_config()
    when = day or date.today()
    filename = datetime(when.year, when.month, when.day).strftime(
        cfg.daily_note.filename_pattern
    )
    return resolve_target(cfg.daily_note.daily_notes_dir, filename)


__all__ = [
    "SECTION",
    "UNIT",
    "WRITER",
    "NoteAttestation",
    "NoteAttestationConflict",
    "daily_note_path",
    "read_attestation",
    "reconcile",
    "render_body",
    "write",
]
