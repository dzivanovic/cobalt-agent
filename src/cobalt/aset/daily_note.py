"""ASET's daily-note writer — now a thin caller of the ONE write path.

Converted 2026-09-03 (LAW L28). What changed and why:

BEFORE: this module opened the note in append mode itself
(`open(path, "a")`), stubbed a missing note inline, and appended a
fenced card block with no marker and no identity. Three consequences,
all real:
  * a re-run appended a SECOND copy of the same card — nothing tied a
    block to a card;
  * `prefill/daily.py` had to special-case the stub banner, and its
    special case discarded everything above that banner;
  * nothing was recorded anywhere, so nothing could be diffed, reported
    or rolled back.

AFTER: every write goes through `cobalt.vaultwrite` — marker-bounded
sections, one unit per card with a stable id (so the same card updates
in place), a deterministic three-way merge that never touches human
text, a mtime+hash-guarded atomic write, and a `vault_writes` row per
write. Cards live in the `aset-cards` section, appended at the end of
the note; nothing above it is ever touched.

Unit ids (stable, deterministic, no lookup needed):
    card-YYYYMMDDTHHMMSS    the sizing card, keyed on its own timestamp
    fill-YYYYMMDDTHHMMSS    the FILL UPDATE, keyed on the ORIGINAL
                            card's timestamp — so recomputing the same
                            card's fill three times leaves ONE block.

The write-disable flag (`daily_note.write_enabled`, 2026-09-03) exists
because the containment session had no way to keep the sheet serving
while stopping its note writes and had to stop the whole process. With
it, `write_enabled: false` keeps sizing, persistence and the sheet fully
alive and turns the note write into a loud, logged no-op.

The post-write verification from the 2026-09-02 incident is kept: after
the writer returns, the note is re-read and the unit must be there. The
writer's own guard covers the read->rename window; this covers the
window AFTER the rename, where an editor buffer flush has twice
destroyed data.
"""

from datetime import datetime
from pathlib import Path
from typing import Optional

from loguru import logger

from cobalt.vault import VaultConfigError, VaultWriteRefused, assert_within_vault, resolve_vault_path
from cobalt.vaultwrite import VaultWriteError, VaultWriter, VaultWriteStore, WriteResult
from cobalt.vaultwrite.markers import find_section

from .config import AsetConfig
from .models import FillRecompute, SizingResult

# Kept for backwards compatibility with notes ASET stubbed before L28 —
# prefill no longer branches on it (that branch is deleted), and the
# stub template below still carries it so a hand-applied Templater run
# still has its visible cue.
STUB_BANNER = "> ⚠️ Created by Cobalt — apply daily template.\n"

CARDS_SECTION = "aset-cards"


class DailyNoteRefused(RuntimeError):
    """Write refused — safety gate failed or note target misconfigured."""


def target_path(cfg: AsetConfig, when: datetime) -> Path:
    try:
        vault_root = resolve_vault_path()
    except VaultConfigError as e:
        raise DailyNoteRefused(f"Vault path unresolved: {e}") from e
    return (
        vault_root
        / cfg.daily_note.daily_notes_dir
        / when.strftime(cfg.daily_note.filename_pattern)
    )


def assert_safe_target(path: Path) -> None:
    """Refuse unless `path` resolves OUTSIDE the repo working tree.

    Thin wrapper over the shared gate (cobalt.vault.assert_within_vault,
    one-path rule) — kept as its own function/exception type here since
    callers and tests already depend on DailyNoteRefused specifically.
    The vaultwrite writer applies this same gate plus the production-
    vault fence on every call; this stays for the early, explicit refusal.
    """
    try:
        assert_within_vault(path)
    except VaultWriteRefused as e:
        raise DailyNoteRefused(str(e)) from e


def card_unit_id(when: datetime) -> str:
    return f"card-{when:%Y%m%dT%H%M%S}"


def fill_unit_id(orig_timestamp: datetime) -> str:
    return f"fill-{orig_timestamp:%Y%m%dT%H%M%S}"


def stub_template(when: datetime) -> str:
    return f"# {when:%Y-%m-%d}\n\n{STUB_BANNER}"


def format_card(result: SizingResult, when: datetime) -> str:
    i = result.input
    lines = [
        f"### {when:%H:%M:%S} — {i.ticker} {i.direction.value.upper()} {i.grade.value}",
        "```aset",
        f"ticker: {i.ticker}",
        f"direction: {i.direction.value}",
        f"grade: {i.grade.value}",
        f"sheet_mode: {i.sheet_mode.value}",
        f"entry: {i.entry}",
        f"stop: {i.stop}",
        f"risk_budget: {result.risk_budget}",
        f"shares: {result.shares}",
        f"timestamp: {when.isoformat(timespec='seconds')}",
        "```",
    ]
    return "\n".join(lines)


def format_fill_update_card(
    fill: FillRecompute, when: datetime, orig_timestamp: datetime
) -> str:
    i = fill.original.input
    lines = [
        f"### {when:%H:%M:%S} — {i.ticker} FILL UPDATE "
        f"(orig {orig_timestamp.isoformat(timespec='seconds')})",
        "```aset-fill",
        f"ticker: {i.ticker}",
        f"orig_timestamp: {orig_timestamp.isoformat(timespec='seconds')}",
        f"actual_fill: {fill.actual_fill}",
        f"stop: {i.stop}",
        f"planned_shares: {fill.original.shares}",
        f"recomputed_shares: {fill.recomputed_shares}",
        f"share_delta: {fill.share_delta:+d}",
        f"recomputed_used_risk: {fill.recomputed_used_risk}",
        f"distance_change_pct: {fill.distance_change_pct}",
        f"timestamp: {when.isoformat(timespec='seconds')}",
        "```",
    ]
    if fill.structural_warning:
        lines.append(f"> ⚠️ {fill.structural_warning}")
    return "\n".join(lines)


def build_writer(cfg: AsetConfig, *, dry_run: bool = False, run_id: Optional[str] = None) -> VaultWriter:
    store = VaultWriteStore()
    store.ensure_schema()
    return VaultWriter("aset.daily_note", store=store, run_id=run_id, dry_run=dry_run)


def _write_unit(
    cfg: AsetConfig,
    when: datetime,
    unit_id: str,
    body: str,
    *,
    dry_run: bool = False,
    writer: Optional[VaultWriter] = None,
) -> tuple[Path, Optional[WriteResult]]:
    path = target_path(cfg, when)
    if not path.parent.is_dir():
        raise DailyNoteRefused(
            f"Daily notes directory missing: {path.parent} — refusing to "
            "create vault structure (folder policy is a Vault Session decision)."
        )
    assert_safe_target(path)

    if not cfg.daily_note.write_enabled:
        logger.warning(
            f"DAILY-NOTE WRITE DISABLED (daily_note.write_enabled=false): "
            f"unit {unit_id} was NOT written to {path}. The sheet is serving and "
            "the card is persisted to Postgres; the journal entry is not."
        )
        return path, None

    vw = writer or build_writer(cfg, dry_run=dry_run)
    try:
        vw.create_if_absent(path, stub_template(when))
        result = vw.upsert_unit(path, CARDS_SECTION, unit_id, body)
    except (VaultWriteError, VaultWriteRefused) as e:
        raise DailyNoteRefused(str(e)) from e

    logger.info(result.report())

    if not vw.dry_run:
        # 2026-09-02 incident: a write returned cleanly and the card was
        # not on disk afterwards (an external editor rewrote the file).
        # open/write/close not raising only proves the bytes reached the
        # OS. Check the one thing that matters: is it readable back now.
        on_disk = path.read_text(encoding="utf-8").split("\n")
        section = find_section(on_disk, CARDS_SECTION)
        if section is None or unit_id not in section.units:
            raise DailyNoteRefused(
                f"VERIFY FAILED: wrote unit {unit_id} to {path} without error, but "
                "it is not there on re-read — something else modified the file "
                "after this write (a stale editor buffer autosaving over it is the "
                "prime suspect). Treat this card as NOT in the daily note."
            )
    return path, result


def save_card(
    cfg: AsetConfig,
    result: SizingResult,
    when: Optional[datetime] = None,
    *,
    dry_run: bool = False,
    writer: Optional[VaultWriter] = None,
) -> tuple[Path, datetime, Optional[WriteResult]]:
    """Upsert the card into today's note. Returns (path, when, write) —
    `when` is the canonical card timestamp, threaded back to the caller
    so it can be carried forward (into a hidden orig_timestamp form
    field) for later fill linkage; `write` is None when the note write is
    disabled by config."""
    when = when or datetime.now().astimezone()
    path, write = _write_unit(
        cfg, when, card_unit_id(when), format_card(result, when),
        dry_run=dry_run, writer=writer,
    )
    return path, when, write


def save_fill_update(
    cfg: AsetConfig,
    fill: FillRecompute,
    orig_timestamp: datetime,
    when: Optional[datetime] = None,
    *,
    dry_run: bool = False,
    writer: Optional[VaultWriter] = None,
) -> tuple[Path, Optional[WriteResult]]:
    """Upsert the FILL UPDATE block keyed on the ORIGINAL card's
    timestamp — recomputing the same card's fill twice updates one block
    instead of appending a second. Targets the note for `when` (today),
    not the original card's date; the original card's own date lives in
    orig_timestamp for cross-day fills."""
    when = when or datetime.now().astimezone()
    return _write_unit(
        cfg, when, fill_unit_id(orig_timestamp),
        format_fill_update_card(fill, when, orig_timestamp),
        dry_run=dry_run, writer=writer,
    )
