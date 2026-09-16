"""`cobalt cards trail-fit-draft` — a review DRAFT, never an apply
(S2-P2 STEP-8; ruling R5).

WHY. `trail_fit` is declared `source: cobalt` in the notes, but Cobalt has
no computer for it in S2: the dot is N/A (`MANUAL`) and, untapped, it
suppresses `card_score` (the settled rule). R5 rules the fix is Dejan's —
flip the factor to `source: human` in his own notes if he agrees. So
this command reads every defined strategy note, finds its `trail_fit`
item, and writes ONE markdown draft: the item as it is, the item as it
would be, and whether that proposed item validates. It writes no note.
There is no `apply` in P2, and this module deliberately holds no vault
writer — the only file it creates is the draft, and it never overwrites
one.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from cobalt.taxonomy.factor_lines import FactorLinesError, factor_block
from cobalt.taxonomy.trade_def import QualityFactor
from cobalt.taxonomy.vault_loader import DEF_UNIT_PREFIX, DEFINITION_SECTION, load_vault_trade_defs
from cobalt.vaultwrite.markers import find_section

FACTOR = "trail_fit"


class TrailFitDraftError(RuntimeError):
    """The draft cannot be produced as asked — loud, never an empty draft."""


class DraftRow(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    note_path: str
    slug: str
    current: list[str]
    proposed: str | None
    status: str


class TrailFitDraft(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    drafted_on: date
    rows: list[DraftRow] = Field(min_length=1)


def draft_trail_fit(vault_root: Path, *, today: date) -> TrailFitDraft:
    rows = []
    for loaded in sorted(load_vault_trade_defs(vault_root=vault_root).defs, key=lambda d: d.note_path):
        factor = next((q for q in loaded.definition.quality_factors if q.name == FACTOR), None)
        if factor is None:
            continue
        lines = (vault_root / loaded.note_path).read_text(encoding="utf-8").splitlines()
        section = find_section(lines, DEFINITION_SECTION)
        unit = section.units[f"{DEF_UNIT_PREFIX}{loaded.slug}"]
        try:
            item = factor_block(unit.body(lines)).item(FACTOR)
        except FactorLinesError as e:
            raise TrailFitDraftError(f"{loaded.note_path}: {e}") from e
        current = [line.strip() for line in item.lines]
        if factor.source == "human":
            rows.append(DraftRow(note_path=loaded.note_path, slug=loaded.slug, current=current, proposed=None,
                                 status="already source: human"))
            continue
        mapping = dict(item.value) if isinstance(item.value, dict) else {"name": item.value}
        mapping["source"] = "human"
        try:
            QualityFactor.model_validate(mapping)
            status = "proposed item validates"
        except ValidationError as e:
            status = f"proposed item does NOT validate: {e.errors()[0]['msg']}"
        flow = yaml.safe_dump(mapping, default_flow_style=True, sort_keys=False).strip()
        rows.append(DraftRow(note_path=loaded.note_path, slug=loaded.slug, current=current,
                             proposed=f"- {flow}", status=status))
    if not rows:
        raise TrailFitDraftError("no defined note carries trail_fit — there is nothing to draft")
    return TrailFitDraft(drafted_on=today, rows=rows)


def render_draft(draft: TrailFitDraft) -> str:
    out = [
        "# trail_fit → source: human — DRAFT (S2-P2 R5)",
        "",
        f"Drafted {draft.drafted_on.isoformat()} by `cobalt cards trail-fit-draft`. This is a DRAFT, never applied "
        "by Cobalt: there is no apply command. If you agree, edit the item in the note yourself; the next "
        "`cobalt taxonomy load` picks it up.",
        "",
    ]
    for row in draft.rows:
        out += [f"## {row.slug}", "", f"- note: `{row.note_path}`", f"- status: {row.status}", "", "Current item:",
                "", "```yaml", *row.current, "```", ""]
        if row.proposed is not None:
            out += ["Proposed item:", "", "```yaml", row.proposed, "```", ""]
    return "\n".join(out)


def write_draft(vault_root: Path, out: Path, *, today: date) -> Path:
    text = render_draft(draft_trail_fit(vault_root, today=today))
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        with out.open("x", encoding="utf-8") as f:
            f.write(text)
    except FileExistsError:
        raise TrailFitDraftError(f"{out} exists — a draft is never overwritten; move it or pass --out") from None
    return out


def cmd_trail_fit_draft(args: argparse.Namespace) -> None:
    from cobalt.session.clock import now_utc, session_clock
    from cobalt.vault import REPO_ROOT, resolve_vault_path

    today = session_clock().to_et(now_utc()).date()
    out = Path(args.out) if args.out else (
        REPO_ROOT / "docs" / "40 - DevDocs" / "reports" / f"trail-fit-draft-{today.isoformat()}.md"
    )
    path = write_draft(resolve_vault_path(), out, today=today)
    print(f"trail_fit draft written (no note touched): {path}")


__all__ = ["DraftRow", "TrailFitDraft", "TrailFitDraftError", "cmd_trail_fit_draft", "draft_trail_fit",
           "render_draft", "write_draft"]
