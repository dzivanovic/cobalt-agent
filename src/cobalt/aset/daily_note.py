"""Append-only "Save to Daily Note" writer.

Iteration 4 (ruled by Dejan, 2026-08-28): "Compute & persist" now
appends the card to the daily note in the same action — there is no
longer a separate save step (a card that isn't in the journal didn't
happen). A later "actual fill" entry appends a linked FILL UPDATE block
instead of mutating the original card — both stay in the audit trail.

Appends the sizing card as a timestamped fenced markdown block to
today's real daily note, under the vault root resolved by the ONE
vault-path resolver (`cobalt.vault.resolve_vault_path`) — never
configured here. All paths/patterns beyond the vault root come from
`AsetConfig.daily_note` — nothing hardcoded. Section targeting comes
later; the daily note is correct for now.

SAFETY GATE (the vault is no longer inside the repo — that IS the
safety property now): before every write, the resolved target's real
path must NOT start with the repo root. A target that resolves inside
the repo working tree, or any failure while resolving it, REFUSES the
write with a loud error. (Superseded the old git-check-ignore gate from
when the vault lived inside the repo at docs/0 - Inbox — see BACKLOG.md,
2026-08-26 vault-path migration.)

APPEND-ONLY forever: existing content is never read, modified, or
reordered — the file is only ever opened in append mode. If the note
doesn't exist yet, a stub is created with a visible banner line (the
daily template still needs to be applied by hand/Obsidian) before the
card is appended.
"""

from datetime import datetime
from pathlib import Path
from typing import Optional

from cobalt.vault import VaultConfigError, VaultWriteRefused, assert_within_vault, resolve_vault_path

from .config import AsetConfig
from .models import FillRecompute, SizingResult

STUB_BANNER = "> ⚠️ Created by Cobalt — apply daily template.\n"


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
    """
    try:
        assert_within_vault(path)
    except VaultWriteRefused as e:
        raise DailyNoteRefused(str(e)) from e


def format_card(result: SizingResult, when: datetime) -> str:
    i = result.input
    lines = [
        "",
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
        "",
    ]
    return "\n".join(lines)


def format_fill_update_card(
    fill: FillRecompute, when: datetime, orig_timestamp: datetime
) -> str:
    i = fill.original.input
    lines = [
        "",
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
    lines.append("")
    return "\n".join(lines)


def _append(cfg: AsetConfig, when: datetime, body: str) -> Path:
    """Append `body`, then re-read the file and confirm it's actually
    there (2026-09-02 incident: a TSLA card's /size POST reported this
    function succeeded — no exception — yet the card was never on disk;
    something else (most likely an external editor with the note open,
    per the forensics writeup) rewrote the file out from under this
    write sometime after it returned). open()/write()/close() not
    raising only proves the bytes were handed to the OS, not that they
    survived — fail-loud means checking the one thing that actually
    matters: is the card readable back right now. Not airtight against
    a clobber landing in the gap between this write and this re-read,
    but it turns "silent, undetected data loss" into "loud FAILED
    banner", which is the whole ask."""
    path = target_path(cfg, when)
    if not path.parent.is_dir():
        raise DailyNoteRefused(
            f"Daily notes directory missing: {path.parent} — refusing to "
            "create vault structure (folder policy is a Vault Session decision)."
        )
    assert_safe_target(path)
    is_new = not path.exists()
    with open(path, "a", encoding="utf-8") as f:
        if is_new:
            f.write(f"# {when:%Y-%m-%d}\n\n{STUB_BANNER}")
        f.write(body)

    on_disk = path.read_text(encoding="utf-8")
    if body not in on_disk:
        raise DailyNoteRefused(
            f"VERIFY FAILED: wrote to {path} without error, but the card is "
            "not there on re-read — something else modified the file after "
            "this write (a stale editor buffer autosaving over it is the "
            "prime suspect; see src/cobalt/aset/daily_note.py). The write "
            "did not survive; treat this card as NOT in the daily note."
        )
    return path


def save_card(
    cfg: AsetConfig, result: SizingResult, when: Optional[datetime] = None
) -> tuple[Path, datetime]:
    """Append the card to today's note; stub the note (with a banner) if
    absent. Returns (path, when) — `when` is the canonical card
    timestamp, threaded back to the caller so it can be carried forward
    (e.g. into a hidden orig_timestamp form field) for later fill linkage."""
    when = when or datetime.now().astimezone()
    path = _append(cfg, when, format_card(result, when))
    return path, when


def save_fill_update(
    cfg: AsetConfig,
    fill: FillRecompute,
    orig_timestamp: datetime,
    when: Optional[datetime] = None,
) -> Path:
    """Append a FILL UPDATE block linked to the original card's timestamp.
    Targets the note for `when` (today), not the original card's date —
    the original card's own date lives in orig_timestamp for cross-day
    fills, which are expected to be rare but not refused."""
    when = when or datetime.now().astimezone()
    return _append(cfg, when, format_fill_update_card(fill, when, orig_timestamp))
