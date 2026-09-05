"""F6 match check: the loaded `.htk` against the decided day mode.

Charter §3 F6: "the loaded `.htk` is checked against the mode and
mismatch refuses cards. Test: he loads the full sheet on a half day ->
card refused with the reason."

WHAT SLICE 2 ACTUALLY SHIPPED, and why this module is an attestation.
The ".htk-match check" appears in the ledger's slice-2 scope line
("day-mode line + .htk-match check"). What landed is ONE STATIC STRING —
`src/cobalt/prefill/daily.py`'s `SHEET_MODE_LINE`:

    "Sheet mode: [ ] FULL [ ] HALF — .htk loaded: [ ] full [ ] half"

Two pairs of markdown checkboxes in the daily note. It reads nothing,
compares nothing, persists nothing and refuses nothing; the trader ticks
a box and no code ever looks at it. There is no other `.htk` reference
anywhere in `src/` (verified by grep across the whole tree), so there is
no DAS-state read to keep.

Nor could there be. The trading PC has NOT joined the tailnet — S1-P1's
line-0 report found three devices (`cobalt`, `dejans-s25`, `fedora`) and
no Windows peer — and CLAUDE.md's first absolute boundary forbids
touching DAS Trader Pro at all, read-only or otherwise. So Cobalt cannot
know which hotkey file is loaded, and the honest design is not to
pretend: **he states it, and Cobalt holds him to it.**

That is what this module does. `attested_sheet` on the `day_modes` row
is his word, `attested_at` is when he gave it, and every card creation
is refused while his word disagrees with the decided mode. The refusal
names both sides and both ways out:

    "sheet FULL loaded, day mode REDUCED — reload reduced_day.htk or overrule"

The attestation is a weaker guarantee than a read, and it is labelled as
one everywhere it surfaces (the sheet says "attested, not read"). It is
strictly stronger than a checkbox nobody reads.
"""

from __future__ import annotations

from typing import Any, Optional

from cobalt.aset.models import Grade

from .config import DayModeConfig, load_daymode_config


class SheetMismatch(RuntimeError):
    """The attested `.htk` disagrees with the decided day mode."""

    def __init__(self, message: str, *, attested: Optional[str], mode: str):
        super().__init__(message)
        self.attested = attested
        self.mode = mode


def assert_sheet_matches(
    row: Optional[dict[str, Any]],
    mode: str,
    *,
    cfg: Optional[DayModeConfig] = None,
) -> str:
    """Refuse unless the attested file's mode IS the mode in force.

    Returns the attested filename on success. Raises `SheetMismatch`
    when he has attested a different rung — and ALSO when he has
    attested nothing at all, because "no attestation" is not the same as
    "it matches": an unstated hotkey file is exactly the state in which a
    full-size key gets pressed on a reduced-size day.
    """
    cfg = cfg or load_daymode_config()
    attested = (row or {}).get("attested_sheet")
    expected = _expected_file(cfg, mode)

    if not attested:
        raise SheetMismatch(
            "No hotkey file attested for today. Cobalt cannot read DAS (it never "
            "touches a trading platform) — say which .htk you have loaded before "
            f"writing a card. Day mode is {mode.upper()}; the matching file is "
            f"{expected}.",
            attested=None,
            mode=mode,
        )

    attested_mode = cfg.mode_for_hotkey_file(attested)
    if attested_mode != mode:
        raise SheetMismatch(
            f"sheet {attested_mode.upper()} loaded, day mode {mode.upper()} — "
            f"reload {expected} or overrule",
            attested=attested,
            mode=mode,
        )
    return attested


def _expected_file(cfg: DayModeConfig, mode: str) -> str:
    for entry in cfg.hotkey_files:
        if entry.mode == mode:
            return entry.file
    return f"(no .htk declared for mode {mode!r} in configs/cobalt/daymode.yaml)"


def assert_grade_allowed(
    grade: "Grade | str", mode: str, *, cfg: Optional[DayModeConfig] = None
) -> None:
    """Refuse a key outside the rung's grade ladder (F6/F10).

    The reduced rung narrows the account ladder to
    `daymode.reduced_enabled_grades` (today `[B]`). An A key on the
    reduced rung is not a smaller A — it is a key he has decided not to
    press today, so it is refused with the reason on screen rather than
    silently resized.
    """
    cfg = cfg or load_daymode_config()
    allowed = cfg.enabled_grades_for(mode)
    if Grade(grade) not in allowed:
        raise SheetMismatch(
            f"key {Grade(grade).value} is not enabled on the {mode.upper()} rung — "
            f"today's keys are {[g.value for g in allowed]}. "
            f"({mode.upper()} sizes from the {cfg.sheet_for(mode).upper()} sheet; the "
            "grade restriction is the day mode's, not the account's.)",
            attested=None,
            mode=mode,
        )


__all__ = ["SheetMismatch", "assert_grade_allowed", "assert_sheet_matches"]
