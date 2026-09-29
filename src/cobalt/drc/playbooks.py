"""Playbook name → setup, ONE-TO-ONE (DRC D3-2b; R116 / R117; 09-23 R17 (1)).

    read_strategies(vault_root)          the titles of `4 - Strategies`, read NOW
    resolve_playbooks(names, vault_root) one `PlaybookResolution` per name, in order

THE RULE, whole — deterministic, no LLM, no mapping table (L2 / L57):
(1) the strategy note TITLES are read AT BUILD TIME from the vault's
    strategies folder (`taxonomy.vault_loader.STRATEGIES_DIR`, the one path
    constant, L3): top-level `*.md` files, title = the file name without
    `.md`. Never a committed list (L32 / L45).
(2) per name, in the stats log's order (R114: every name, nothing picked):
    strip ONE trailing ` Long` / ` Short` — case-insensitive, a WHOLE word
    (one space before it, ending the name; `X Long Long` strips once,
    `Longhorn` never) — and nothing else.
(3) the stripped name EQUALS a title (exact, case-sensitive) → that note's
    setup id: its frontmatter `trade_def:` read with the ONE frontmatter
    parser and validated by `validate_slug`.
(4) no equal title → `unmapped: <name>`; a matched note whose slug is
    missing or invalid → `unmapped: <name> — note <title>: <SlugError>`.
    Both are counted and shown; NEITHER fails the build. An unreadable
    folder unmaps every name with `strategies folder not readable` (L1:
    loud, never a guess).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable, Optional

from pydantic import BaseModel, ConfigDict

from cobalt.taxonomy.slug import SlugError, validate_slug
from cobalt.taxonomy.vault_loader import STRATEGIES_DIR
from cobalt.vaultwrite.frontmatter import FrontmatterError, split_frontmatter

#: ONE trailing side word, whole, case-insensitive (R116 desk reading).
_SIDE = re.compile(r"^(?P<stem>.+) (?:long|short)$", re.IGNORECASE)
NOT_READABLE = "strategies folder not readable"


@dataclass(frozen=True)
class Strategies:
    """What the build read of the strategies folder: title → slug, or the
    slug error text of a note whose `trade_def:` does not validate."""

    readable: bool
    slugs: dict[str, str] = field(default_factory=dict)
    errors: dict[str, str] = field(default_factory=dict)

    def listing(self) -> dict[str, str]:
        """The title → slug-or-error list, as stored in the row's inputs (L57)."""
        return {**{t: s for t, s in self.slugs.items()}, **{t: f"error: {e}" for t, e in self.errors.items()}}


class PlaybookResolution(BaseModel):
    """One name's outcome. `setup` set ⇔ mapped."""

    model_config = ConfigDict(frozen=True)

    name: str
    stripped: str
    title: Optional[str] = None
    setup: Optional[str] = None
    why: Optional[str] = None

    @property
    def mapped(self) -> bool:
        return self.setup is not None

    @property
    def text(self) -> str:
        if self.setup is not None:
            return f"{self.name} → {self.setup}"
        return f"unmapped: {self.name}" + (f" — {self.why}" if self.why else "")


def strip_side(name: str) -> str:
    m = _SIDE.match(name)
    return m.group("stem") if m else name


def read_strategies(vault_root: Path) -> Strategies:
    folder = Path(vault_root) / STRATEGIES_DIR
    try:
        notes = sorted(p for p in folder.iterdir() if p.is_file() and p.suffix == ".md")
    except OSError:
        return Strategies(readable=False)
    slugs: dict[str, str] = {}
    errors: dict[str, str] = {}
    for note in notes:
        title = note.name[: -len(".md")]
        try:
            fm, _ = split_frontmatter(note.read_text(encoding="utf-8"))
            slugs[title] = validate_slug((fm or {}).get("trade_def"), where=str(note))
        except (SlugError, FrontmatterError, OSError, UnicodeDecodeError) as e:
            errors[title] = str(e)
    return Strategies(readable=True, slugs=slugs, errors=errors)


def resolve(names: Iterable[str], strategies: Strategies) -> list[PlaybookResolution]:
    out: list[PlaybookResolution] = []
    for name in names:
        stripped = strip_side(name)
        if not strategies.readable:
            out.append(PlaybookResolution(name=name, stripped=stripped, why=NOT_READABLE))
        elif stripped in strategies.slugs:
            out.append(PlaybookResolution(name=name, stripped=stripped, title=stripped,
                                          setup=strategies.slugs[stripped]))
        elif stripped in strategies.errors:
            out.append(PlaybookResolution(name=name, stripped=stripped, title=stripped,
                                          why=f"note {stripped}: {strategies.errors[stripped]}"))
        else:
            out.append(PlaybookResolution(name=name, stripped=stripped))
    return out


def resolve_playbooks(names: list[str], vault_root: Path) -> list[PlaybookResolution]:
    """The titles read now, then every name resolved in order."""
    return resolve(names, read_strategies(vault_root))


__all__ = [
    "NOT_READABLE", "PlaybookResolution", "Strategies", "read_strategies", "resolve", "resolve_playbooks",
    "strip_side",
]
