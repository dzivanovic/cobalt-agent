"""Append-only "Save to Daily Note" writer.

Appends the current sizing card as a timestamped fenced markdown block to
today's daily note under the CONFIGURED vault path (docs/ playground
vault today; live-vault migration is a scheduled design decision). All
paths and patterns come from config — nothing hardcoded. Section
targeting comes later; the inbox is correct for now.

SAFETY GATE (vault content must never become committable): before every
write the target must be confirmed git-ignored via `git check-ignore`
AND not tracked. A tracked target, or any failure of the checks
themselves, REFUSES the write with a loud error.

APPEND-ONLY forever: existing content is never read, modified, or
reordered — the file is only ever opened in append mode.
"""

import subprocess
from datetime import datetime
from pathlib import Path
from typing import Optional

from .config import REPO_ROOT, AsetConfig
from .models import SizingResult


class DailyNoteRefused(RuntimeError):
    """Write refused — safety gate failed or note target misconfigured."""


def target_path(cfg: AsetConfig, when: datetime) -> Path:
    root = Path(cfg.daily_note.vault_path)
    if not root.is_absolute():
        root = REPO_ROOT / root
    return root / cfg.daily_note.inbox_dir / when.strftime(cfg.daily_note.filename_pattern)


def _git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(REPO_ROOT), *args],
        capture_output=True,
        text=True,
        timeout=10,
    )


def assert_safe_target(path: Path) -> None:
    """Refuse unless `path` is git-ignored and untracked."""
    try:
        ignored = _git("check-ignore", "-q", str(path))
        tracked = _git("ls-files", "--error-unmatch", str(path))
    except Exception as e:
        raise DailyNoteRefused(f"Safety gate could not run git checks: {e}") from e

    if tracked.returncode == 0:
        raise DailyNoteRefused(
            f"REFUSED: {path} is TRACKED by git — vault content must never be committable."
        )
    if ignored.returncode != 0:
        raise DailyNoteRefused(
            f"REFUSED: {path} is not git-ignored (check-ignore rc="
            f"{ignored.returncode}{': ' + ignored.stderr.strip() if ignored.stderr.strip() else ''}) "
            "— vault content must never be committable."
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
    """Append the card to today's note; create the note on first save."""
    when = when or datetime.now().astimezone()
    path = target_path(cfg, when)
    if not path.parent.is_dir():
        raise DailyNoteRefused(
            f"Inbox directory missing: {path.parent} — refusing to create "
            "vault structure (folder policy is a Vault Session decision)."
        )
    assert_safe_target(path)
    is_new = not path.exists()
    with open(path, "a", encoding="utf-8") as f:
        if is_new:
            f.write(f"# {when:%Y-%m-%d}\n")
        f.write(format_card(result, when))
    return path
