"""Append-only "Save to Daily Note" writer.

Appends the current sizing card as a timestamped fenced markdown block
to today's real daily note, under the vault root resolved by the ONE
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

from cobalt.vault import VaultConfigError, resolve_vault_path

from .config import REPO_ROOT, AsetConfig
from .models import SizingResult

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
    """Refuse unless `path` resolves OUTSIDE the repo working tree."""
    resolved = path.resolve()
    repo_root_resolved = REPO_ROOT.resolve()
    try:
        resolved.relative_to(repo_root_resolved)
    except ValueError:
        return  # not inside the repo — safe
    raise DailyNoteRefused(
        f"REFUSED: resolved target {resolved} is INSIDE the repo working "
        f"tree ({repo_root_resolved}) — the vault must live outside the "
        "repo, never inside it."
    )


def format_card(result: SizingResult, when: datetime) -> str:
    i = result.input
    lines = [
        "",
        f"### {when:%H:%M:%S} — {i.ticker} {i.direction.value.upper()} {i.grade.value}",
        "```aset",
        f"ticker: {i.ticker}",
        f"direction: {i.direction.value}",
        f"grade: {i.grade.value} ({result.risk_pct}%)",
        f"entry: {i.entry}",
        f"stop: {i.stop}",
        f"daily_stop: {i.daily_stop}",
        f"risk_budget: {result.risk_budget}",
        f"shares: {result.shares}",
        f"timestamp: {when.isoformat(timespec='seconds')}",
        "```",
        "",
    ]
    return "\n".join(lines)


def save_card(
    cfg: AsetConfig, result: SizingResult, when: Optional[datetime] = None
) -> Path:
    """Append the card to today's note; stub the note (with a banner) if absent."""
    when = when or datetime.now().astimezone()
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
        f.write(format_card(result, when))
    return path
