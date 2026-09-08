"""Trade notes gain `trade_def:` (ADR-0008 D4).

`cobalt taxonomy migrate-trade-notes --dry-run | --apply [--note PATH]`

WHAT IT DOES, AND WHAT IT REFUSES TO DO. Every note in
`1 - Trading/2 - Trades/` carries a free-text `strategy:` — a value typed
into a Templater dropdown over two years, with leading spaces, doubled
quotes and names that drifted from the ones the strategy notes use. None
of them carries `trade_def:`, so every strategy note's `## Instances`
dataview renders empty. This command inserts exactly ONE line,
`trade_def: <slug>`, immediately after the `strategy:` line, through
`VaultWriter.upsert_region` (the L28 frontmatter carve-out). Every other
byte is preserved and `strategy:` itself is left VERBATIM — it is a
human's line and it stays one.

THE ALIAS INDEX IS DERIVED FROM THE VAULT, NEVER FROM A TABLE HERE. A
trade name is user data (L32), so this module contains none. It builds
the index by reading the strategy notes: each contributes its slug, its
frontmatter `name:`, its def's (or draft's) `aliases[]`, and any legacy
`strategy:` key of its own. A trade note's value matches iff — trimmed,
surrounding quotes stripped, casefolded — it equals one of those strings
for EXACTLY ONE note. Two notes claiming a value is a loud error, not a
coin toss.

An unmatched value gets `trade_def:` EMPTY, on purpose (ADR-0008 D4):
that is a clause-2a cell a human fills in later, and it is a very
different thing from a note that was never considered. Every unmatched
value is reported by name and count.

IDEMPOTENT: a note that already carries `trade_def:` is skipped, so a
second `--apply` writes nothing. A note with no `strategy:` key at all is
reported and NOT touched — inventing a key in someone's frontmatter is
not this command's business.
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

import yaml

from cobalt.vault import resolve_vault_path
from cobalt.vaultwrite import VaultWriter, VaultWriteStore
from cobalt.vaultwrite.frontmatter import frontmatter_span, split_frontmatter
from cobalt.vaultwrite.markers import find_section

from .note_migration import NoteMigrationError, _fence_span
from .vault_loader import DEFINITION_SECTION, DEF_UNIT_PREFIX, STRATEGIES_DIR

#: Where the trade notes live, relative to the vault root. Read from
#: `configs/cobalt/prefill.yaml` (`trades_dir`) so there is one answer.
def trades_dir() -> str:
    from cobalt.prefill.config import load_prefill_paths

    return load_prefill_paths().trades_dir


#: The frontmatter region's section label — its own, so a trade note's
#: baseline never collides with a strategy note's.
FRONTMATTER_SECTION = "trade-frontmatter"
FRONTMATTER_REGION = "frontmatter"

WRITER_NAME = "taxonomy.migrate_trade_notes"

_STRATEGY_LINE_RE = re.compile(r"^strategy:(?P<value>.*)$")
_TRADE_DEF_LINE_RE = re.compile(r"^trade_def:")


def normalise(value: Any) -> str:
    """Trim, strip surrounding quotes (repeatedly), casefold.

    The corpus really does contain `'"  Big Dawg"'` — a quoted string
    inside a quoted string, with leading spaces — because a Templater
    dropdown wrote it that way. Stripping ONE layer would leave `"  Big
    Dawg"` and match nothing, so the loop runs until the value stops
    being wrapped. It never touches interior punctuation: `Gap, Give and
    Go` and `Gap Give and Go` are different names and must stay so.
    """
    text = str(value).strip()
    while len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
        text = text[1:-1].strip()
    return text.casefold()


# ---------------------------------------------------------------------
# The alias index, read out of the strategy notes
# ---------------------------------------------------------------------


@dataclass
class AliasIndex:
    by_value: dict[str, set[str]] = field(default_factory=lambda: defaultdict(set))
    #: What each slug contributed, for the report.
    sources: dict[str, list[str]] = field(default_factory=dict)

    def match(self, value: str) -> Optional[str]:
        """The one slug this value names, or None. Two = loud."""
        key = normalise(value)
        if not key:
            return None
        hits = self.by_value.get(key) or set()
        if len(hits) > 1:
            raise NoteMigrationError(
                f"the strategy value {value!r} names {sorted(hits)} — two strategy "
                "notes claim the same name or alias, so no trade note can be "
                "assigned to either. Remove the duplicate alias first."
            )
        return next(iter(hits), None)


def build_alias_index(vault_root: Optional[Path] = None) -> AliasIndex:
    """Every string that names a trade, read from the strategy notes."""
    root = Path(vault_root) if vault_root is not None else resolve_vault_path()
    directory = root / STRATEGIES_DIR
    if not directory.is_dir():
        raise NoteMigrationError(f"strategy notes directory not found: {directory}")

    index = AliasIndex()
    for path in sorted(directory.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        fm, _ = split_frontmatter(text)
        if fm is None or not fm.get("trade_def"):
            continue
        slug = fm["trade_def"]
        values: list[str] = [slug]
        for key in ("name", "strategy"):
            if fm.get(key):
                values.append(str(fm[key]))

        section = find_section(text.splitlines(), DEFINITION_SECTION)
        unit = section.units.get(f"{DEF_UNIT_PREFIX}{slug}") if section else None
        if unit is not None:
            body = "\n".join(unit.body(text.splitlines()))
            fence = _fence_span(body.split("\n"))
            if fence is not None:
                raw = yaml.safe_load(
                    "\n".join(body.split("\n")[fence[0]:fence[1]])
                )
                mapping = (raw or {}).get("trade_def") or {}
                values.extend(str(a) for a in (mapping.get("aliases") or []))

        index.sources[slug] = values
        for value in values:
            if str(value).strip():
                index.by_value[normalise(value)].add(slug)
    return index


# ---------------------------------------------------------------------
# The edit
# ---------------------------------------------------------------------


def insert_trade_def_line(lines: list[str], slug: Optional[str]) -> tuple[str, str]:
    """One line after `strategy:`. Returns (new frontmatter, note).

    `lines` is the frontmatter INCLUDING both `---` fences (what
    `frontmatter_span` hands back), and every line that is not the
    inserted one comes out byte-identical.
    """
    out: list[str] = []
    inserted = False
    for line in lines:
        out.append(line)
        if not inserted and _STRATEGY_LINE_RE.match(line):
            out.append(f"trade_def: {slug}" if slug else "trade_def:")
            inserted = True
    if not inserted:
        raise NoteMigrationError(
            "this note has no `strategy:` line, so there is nowhere to put "
            "`trade_def:` — reported, not guessed at."
        )
    return "\n".join(out), (
        f"inserted `trade_def: {slug}` after `strategy:`"
        if slug
        else "inserted an empty `trade_def:` after `strategy:` (clause-2a cell)"
    )


# ---------------------------------------------------------------------
# Planning
# ---------------------------------------------------------------------


@dataclass
class TradeNotePlan:
    path: Path
    strategy_value: str
    slug: Optional[str]
    action: str                     # insert | skip_has_trade_def | skip_no_strategy
    body: Optional[str] = None
    note: str = ""


@dataclass
class TradeNoteRun:
    plans: list[TradeNotePlan] = field(default_factory=list)
    #: `{raw value: (slug or None, n)}` — the tally the report carries.
    tally: dict[str, tuple[Optional[str], int]] = field(default_factory=dict)
    problems: list[str] = field(default_factory=list)


def plan_trade_notes(
    vault_root: Optional[Path] = None,
    *,
    only_note: Optional[str] = None,
    index: Optional[AliasIndex] = None,
) -> TradeNoteRun:
    root = Path(vault_root) if vault_root is not None else resolve_vault_path()
    directory = root / trades_dir()
    if not directory.is_dir():
        raise NoteMigrationError(f"trade notes directory not found: {directory}")

    idx = index or build_alias_index(root)
    run = TradeNoteRun()
    counts: Counter = Counter()
    slugs: dict[str, Optional[str]] = {}

    for path in sorted(directory.glob("*.md")):
        if only_note and path.name != only_note and str(path) != only_note:
            continue
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        span = frontmatter_span(lines)
        if span is None:
            run.problems.append(f"{path.name}: no frontmatter block — not touched")
            continue
        fm_lines = lines[span[0]:span[1]]

        if any(_TRADE_DEF_LINE_RE.match(line) for line in fm_lines):
            run.plans.append(
                TradeNotePlan(path, "", None, "skip_has_trade_def",
                              note="already carries `trade_def:`")
            )
            continue

        strategy = next(
            (m.group("value") for m in
             (_STRATEGY_LINE_RE.match(line) for line in fm_lines) if m),
            None,
        )
        if strategy is None:
            run.problems.append(f"{path.name}: no `strategy:` key — not touched")
            run.plans.append(
                TradeNotePlan(path, "", None, "skip_no_strategy",
                              note="no `strategy:` key")
            )
            continue

        raw = strategy.strip()
        slug = idx.match(raw) if raw else None
        body, note = insert_trade_def_line(fm_lines, slug)
        run.plans.append(TradeNotePlan(path, raw, slug, "insert", body=body, note=note))

        label = raw if raw else "(blank)"
        counts[label] += 1
        slugs[label] = slug

    run.tally = {label: (slugs[label], n) for label, n in counts.items()}
    return run


# ---------------------------------------------------------------------
# Applying
# ---------------------------------------------------------------------


@dataclass
class TradeNoteOutcome:
    path: Path
    strategy_value: str
    slug: Optional[str]
    action: str
    write_id: Optional[int] = None
    diff: str = ""
    sha_before: Optional[str] = None
    sha_after: Optional[str] = None


def apply_trade_notes(
    run: TradeNoteRun, *, dry_run: bool, db_name: Optional[str] = None
) -> list[TradeNoteOutcome]:
    store = VaultWriteStore(db_name)
    store.ensure_schema()
    writer = VaultWriter(WRITER_NAME, store=store, dry_run=dry_run)

    outcomes: list[TradeNoteOutcome] = []
    for plan in run.plans:
        if plan.action != "insert":
            outcomes.append(
                TradeNoteOutcome(plan.path, plan.strategy_value, None, plan.action)
            )
            continue
        result = writer.upsert_region(
            plan.path, FRONTMATTER_SECTION, FRONTMATTER_REGION, plan.body,
            locate=frontmatter_span,
        )
        outcomes.append(
            TradeNoteOutcome(
                plan.path, plan.strategy_value, plan.slug, result.action,
                write_id=result.write_id, diff=result.diff,
                sha_before=result.hash_before, sha_after=result.hash_after,
            )
        )
    return outcomes


#: The Templater file new trade notes are stamped from. A HUMAN-TREE file
#: (no markers, a Templater expression in the frontmatter), so this edit is
#: a plain deterministic write and its diff IS the artifact — the 09-06 R4
#: hand-work precedent, same as the strategy template.
TRADE_TEMPLATE = "5 - Templates/Individual Trade Template.md"

#: The dropdown Cobalt writes into it. The slugs come from the VAULT at
#: edit time — a list typed here would be a list of trade names in this
#: repo, and it would go stale the first time a trader adds a strategy.
_DROPDOWN = 'trade_def: "{{{{VALUE:trade_def, {slugs} }}}}"'


def migrate_trade_template(
    vault_root: Optional[Path] = None, *, dry_run: bool
) -> tuple[Optional[Path], str]:
    """`strategy:` dropdown out, `trade_def:` dropdown in (ADR-0008 D4).

    The `strategy:` LINE goes with it: a new note carries the id, and the
    free-text name it used to carry is what D4 spent 69 notes replacing.
    Existing notes keep their own `strategy:` verbatim — this is the
    template, not a migration.
    """
    from difflib import unified_diff

    root = Path(vault_root) if vault_root is not None else resolve_vault_path()
    path = root / TRADE_TEMPLATE
    if not path.exists():
        return None, f"(no {TRADE_TEMPLATE} in this vault — nothing to do)"

    slugs = sorted(build_alias_index(root).sources)
    if not slugs:
        raise NoteMigrationError(
            f"{TRADE_TEMPLATE}: the vault has no strategy notes, so the dropdown "
            "would be empty. Refusing to write a template nobody can use."
        )
    dropdown = _DROPDOWN.format(slugs=", ".join(slugs))

    before = path.read_text(encoding="utf-8")
    out: list[str] = []
    replaced = False
    for line in before.split("\n"):
        if _STRATEGY_LINE_RE.match(line) and not replaced:
            out.append(dropdown)
            replaced = True
            continue
        if _TRADE_DEF_LINE_RE.match(line):
            out.append(dropdown)
            replaced = True
            continue
        out.append(line)
    after = "\n".join(out)

    if not replaced:
        return path, f"({TRADE_TEMPLATE}: no `strategy:` or `trade_def:` line)"
    if after == before:
        return path, f"({TRADE_TEMPLATE}: already carries this dropdown)"

    diff = "\n".join(
        unified_diff(
            before.splitlines(), after.splitlines(),
            fromfile=f"{TRADE_TEMPLATE} (before)",
            tofile=f"{TRADE_TEMPLATE} (after)",
            lineterm="",
        )
    )
    if not dry_run:
        path.write_text(after, encoding="utf-8")
    return path, diff


__all__ = [
    "TRADE_TEMPLATE",
    "migrate_trade_template",
    "FRONTMATTER_REGION",
    "FRONTMATTER_SECTION",
    "AliasIndex",
    "TradeNoteOutcome",
    "TradeNotePlan",
    "TradeNoteRun",
    "apply_trade_notes",
    "build_alias_index",
    "insert_trade_def_line",
    "normalise",
    "plan_trade_notes",
    "trades_dir",
]
