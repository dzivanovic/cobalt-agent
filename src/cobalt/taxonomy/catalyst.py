"""Taxonomy v0.8's `catalyst` standard: ONE review file, ONE batch apply
(S2-P2 STEP-9; ruling R10; Astra R1-17).

    cobalt taxonomy catalyst-review [--out <file>]
    cobalt taxonomy catalyst-apply --review <file> --sha256 <hash> (--dry-run | --apply)

THE RULING. Schema 0.5 adds `catalyst` to the standard quality factors.
Cobalt does not decide what that means for each strategy: it drafts one
`- catalyst` line per DEFINED note into ONE review file, next to the
`catalyst_*` factors the note already grades. Dejan marks each row
`keep`, `drop`, or `drop: <factor>, …`; the whole file is applied in one
batch bound to the sha256 of the bytes he marked. A `catalyst_*` factor
is removed only where the row says so.

WHY EACH UNIT IS HASHED TOO (R1-17). The file's sha256 proves the review
did not change; it does not prove the NOTES did not. The review records
each Definition unit's sha256 as drafted, and the apply preflights every
row before it writes any: a unit that drifted (he edited the note, or
Obsidian Sync put back something else) refuses the whole batch. A unit
that already carries the reviewed change is "already applied" — which is
how an interrupted batch resumes: re-run the same command and the
applied units are recognised, not rewritten, not lost.

WHAT "DONE" MEANS. Not the exit code. After the writes, every reviewed
unit is re-read from disk and must validate at schema 0.5 with the line
present and the marked factors gone; only then is `gate_ready` true. The
loader gate (`trade_def.LOADER_SCHEMA_GATE`) stays 0.4 until STEP-D4
flips it in code.

Every write goes through `VaultWriter.upsert_unit` (L28: versioned, a
diff per unit, human-wins merge).
"""

from __future__ import annotations

import argparse
import hashlib
import re
from datetime import date
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator, model_validator

from cobalt.vaultwrite.frontmatter import split_frontmatter
from cobalt.vaultwrite.markers import find_section

from .factor_lines import FactorLinesError, append_factor, factor_block, remove_factors
from .trade_def import CATALYST_FACTOR, TradeDef, schema_gate
from .vault_loader import (
    DEF_UNIT_PREFIX,
    DEFINITION_SECTION,
    VaultTaxonomyError,
    load_vault_trade_defs,
)

REVIEW_OPEN = "<!-- catalyst-review:v1 -->"
REVIEW_CLOSE = "<!-- /catalyst-review:v1 -->"
PROPOSED_LINE = f"- {CATALYST_FACTOR}"
TARGET_SCHEMA = "0.5"
_HEADER = "| note | trade_def | unit sha256 | proposed line | existing catalyst_* factors | decision |"
_SHA_RE = re.compile(r"^[0-9a-f]{64}$")


class CatalystReviewError(VaultTaxonomyError):
    """The review file, a note, or the batch cannot be applied as reviewed."""


class ReviewRow(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    note_path: str = Field(min_length=1)
    slug: str = Field(min_length=1)
    unit_sha256: str
    proposed: Literal["- catalyst", "already present"]
    existing: list[str]
    drop: list[str] = Field(default_factory=list)

    @field_validator("unit_sha256")
    @classmethod
    def _sha(cls, value: str) -> str:
        if not _SHA_RE.match(value):
            raise ValueError(f"unit sha256 must be 64 lowercase hex, got {value!r}")
        return value

    @model_validator(mode="after")
    def _drop_is_existing(self) -> ReviewRow:
        unknown = [name for name in self.drop if name not in self.existing]
        if unknown:
            raise ValueError(f"{self.slug}: drop names {unknown}, which the note does not carry ({self.existing})")
        return self

    @property
    def decision(self) -> str:
        if not self.drop:
            return "keep"
        if self.drop == self.existing:
            return "drop"
        return "drop: " + ", ".join(self.drop)


class CatalystReview(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    drafted_on: date
    rows: list[ReviewRow] = Field(min_length=1)

    @model_validator(mode="after")
    def _unique(self) -> CatalystReview:
        slugs = [r.slug for r in self.rows]
        if len(set(slugs)) != len(slugs):
            raise ValueError(f"duplicate trade_def rows in the review: {sorted({s for s in slugs if slugs.count(s) > 1})}")
        return self


def unit_sha256(body: str) -> str:
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def _catalyst_names(names: list[str]) -> list[str]:
    return [name for name in names if name.startswith(f"{CATALYST_FACTOR}_")]


class _Unit(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    path: Path
    name: str
    body: str


def _read_unit(vault_root: Path, note_path: str, slug: str) -> _Unit:
    path = vault_root / note_path
    if not path.is_file():
        raise CatalystReviewError(f"{note_path}: the reviewed note is gone")
    text = path.read_text(encoding="utf-8")
    fm, _ = split_frontmatter(text)
    if not fm or fm.get("trade_def") != slug:
        raise CatalystReviewError(f"{note_path}: frontmatter trade_def is no longer {slug!r}")
    lines = text.splitlines()
    section = find_section(lines, DEFINITION_SECTION)
    unit = section.units.get(f"{DEF_UNIT_PREFIX}{slug}") if section else None
    if unit is None:
        raise CatalystReviewError(f"{note_path}: no {DEF_UNIT_PREFIX}{slug} unit")
    return _Unit(path=path, name=str(fm.get("name", "")).strip(), body="\n".join(unit.body(lines)))


def draft_review(vault_root: Path, *, today: date) -> CatalystReview:
    """One row per DEFINED note (drafts have nothing to grade yet)."""
    loaded = load_vault_trade_defs(vault_root=vault_root)
    rows = []
    for d in sorted(loaded.defs, key=lambda d: d.note_path):
        unit = _read_unit(vault_root, d.note_path, d.slug)
        try:
            names = factor_block(unit.body.split("\n")).names
        except FactorLinesError as e:
            raise CatalystReviewError(f"{d.note_path}: {e}") from e
        rows.append(ReviewRow(
            note_path=d.note_path, slug=d.slug, unit_sha256=unit_sha256(unit.body),
            proposed="already present" if CATALYST_FACTOR in names else PROPOSED_LINE,
            existing=_catalyst_names(names),
        ))
    if not rows:
        raise CatalystReviewError("no defined strategy notes — nothing to review")
    return CatalystReview(drafted_on=today, rows=rows)


def _cell(text: str) -> str:
    if "|" in text or "\n" in text:
        raise CatalystReviewError(f"a review cell cannot hold '|' or a newline: {text!r}")
    return text


def render_review(review: CatalystReview) -> str:
    lines = [
        "# Catalyst review — taxonomy v0.8 (S2-P2 R10)",
        "",
        f"Drafted {review.drafted_on.isoformat()} by `cobalt taxonomy catalyst-review`: one row per defined "
        "strategy note. Nothing is applied until this file is marked, hashed and batch-applied.",
        "",
        "Mark ONLY the last cell of each row:",
        "",
        "- `keep` — add the `- catalyst` line; every existing `catalyst_*` factor stays.",
        "- `drop` — add the line and remove every listed `catalyst_*` factor.",
        "- `drop: <factor>, <factor>` — add the line and remove only the named factors.",
        "",
        "Then: `shasum -a 256 <this file>`, `cobalt taxonomy catalyst-apply --review <this file> --sha256 <hash> "
        "--dry-run`, then `--apply`. The apply refuses if these bytes, or any note's definition unit, changed "
        "since the draft.",
        "",
        REVIEW_OPEN,
        f"drafted: {review.drafted_on.isoformat()}",
        "",
        _HEADER,
        "|---|---|---|---|---|---|",
    ]
    for row in review.rows:
        proposed = f"`{row.proposed}`" if row.proposed == PROPOSED_LINE else row.proposed
        existing = ", ".join(row.existing) or "—"
        cells = [row.note_path, row.slug, row.unit_sha256, proposed, existing, row.decision]
        lines.append("| " + " | ".join(_cell(c) for c in cells) + " |")
    lines += [REVIEW_CLOSE, ""]
    return "\n".join(lines)


def _parse_decision(text: str, existing: list[str], where: str) -> list[str]:
    text = text.strip()
    if text == "keep":
        return []
    if text == "drop":
        if not existing:
            raise CatalystReviewError(f"{where}: `drop` on a note with no catalyst_* factors")
        return list(existing)
    if text.startswith("drop:"):
        names = [n.strip() for n in text[len("drop:"):].split(",") if n.strip()]
        if not names:
            raise CatalystReviewError(f"{where}: `drop:` names no factor")
        return names
    raise CatalystReviewError(f"{where}: decision must be keep | drop | drop: <factor>, …; got {text!r}")


def parse_review(text: str) -> CatalystReview:
    if text.count(REVIEW_OPEN) != 1 or text.count(REVIEW_CLOSE) != 1:
        raise CatalystReviewError("the review file must hold exactly one catalyst-review:v1 block")
    block = text.split(REVIEW_OPEN, 1)[1].split(REVIEW_CLOSE, 1)[0]
    lines = [line for line in block.split("\n") if line.strip()]
    if not lines or not lines[0].startswith("drafted: "):
        raise CatalystReviewError("the review block has no `drafted:` line")
    try:
        drafted = date.fromisoformat(lines[0][len("drafted: "):].strip())
    except ValueError as e:
        raise CatalystReviewError(f"bad drafted date: {e}") from e
    if len(lines) < 3 or lines[1].strip() != _HEADER:
        raise CatalystReviewError("the review table header was changed")
    rows = []
    for number, line in enumerate(lines[3:], start=1):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        where = f"review row {number}"
        if len(cells) != 6:
            raise CatalystReviewError(f"{where}: expected 6 cells, got {len(cells)}")
        note_path, slug, sha, proposed, existing_cell, decision = cells
        existing = [] if existing_cell == "—" else [n.strip() for n in existing_cell.split(",") if n.strip()]
        proposed = proposed.strip("`")
        try:
            rows.append(ReviewRow(
                note_path=note_path, slug=slug, unit_sha256=sha, proposed=proposed, existing=existing,
                drop=_parse_decision(decision, existing, f"{where} ({slug})"),
            ))
        except ValidationError as e:
            raise CatalystReviewError(f"{where} ({slug}): {e}") from e
    try:
        return CatalystReview(drafted_on=drafted, rows=rows)
    except ValidationError as e:
        raise CatalystReviewError(str(e)) from e


def write_review(vault_root: Path, out: Path, *, today: date) -> tuple[Path, str]:
    """Create the review file (never overwrite one). Returns (path, sha256)."""
    text = render_review(draft_review(vault_root, today=today))
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    try:
        with out.open("x", encoding="utf-8") as f:
            f.write(text)
    except FileExistsError:
        raise CatalystReviewError(f"{out} exists — a review file is never overwritten; move it or pass --out") from None
    return out, hashlib.sha256(out.read_bytes()).hexdigest()


# ---------------------------------------------------------------------
# apply
# ---------------------------------------------------------------------


def _names(body: str, where: str) -> list[str]:
    try:
        return factor_block(body.split("\n")).names
    except FactorLinesError as e:
        raise CatalystReviewError(f"{where}: {e}") from e


def target_body(body: str, row: ReviewRow) -> str:
    lines = body.split("\n")
    names = _names(body, row.note_path)
    if CATALYST_FACTOR not in names:
        lines = append_factor(lines, PROPOSED_LINE)
    if row.drop:
        lines = remove_factors(lines, set(row.drop))
    return "\n".join(lines)


def is_applied(body: str, row: ReviewRow) -> bool:
    names = _names(body, row.note_path)
    return CATALYST_FACTOR in names and not set(row.drop) & set(names)


def _validate_at_target(body: str, unit: _Unit, row: ReviewRow) -> None:
    fence = re.search(r"```ya?ml\n(.*?)\n```", body, re.DOTALL)
    if fence is None:
        raise CatalystReviewError(f"{row.note_path}: the definition unit has no YAML fence")
    try:
        mapping = yaml.safe_load(fence.group(1))["trade_def"]
        with schema_gate(TARGET_SCHEMA):
            TradeDef.from_unit(mapping, slug=row.slug, name=unit.name)
    except (ValidationError, ValueError, TypeError, KeyError, yaml.YAMLError) as e:
        raise CatalystReviewError(f"{row.note_path}: does not validate at schema {TARGET_SCHEMA}: {e}") from e


class UnitPlan(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    row: ReviewRow
    path: Path
    action: Literal["write", "already_applied"]
    before_sha256: str
    new_body: str | None


def plan_apply(vault_root: Path, review: CatalystReview) -> list[UnitPlan]:
    """Preflight EVERY row before anything is written."""
    defined = {d.slug: d.note_path for d in load_vault_trade_defs(vault_root=vault_root).defs}
    reviewed = {r.slug for r in review.rows}
    unreviewed = sorted(set(defined) - reviewed)
    if unreviewed:
        raise CatalystReviewError(
            f"defined notes not in the review: {unreviewed} — the review is stale; draft a new one"
        )
    plans, problems = [], []
    for row in review.rows:
        if row.slug not in defined:
            problems.append(f"{row.slug}: no longer a defined note")
            continue
        unit = _read_unit(vault_root, row.note_path, row.slug)
        sha = unit_sha256(unit.body)
        if sha == row.unit_sha256:
            new_body = target_body(unit.body, row)
            _validate_at_target(new_body, unit, row)
            plans.append(UnitPlan(row=row, path=unit.path, action="write", before_sha256=sha, new_body=new_body))
        elif is_applied(unit.body, row):
            _validate_at_target(unit.body, unit, row)
            plans.append(UnitPlan(row=row, path=unit.path, action="already_applied", before_sha256=sha, new_body=None))
        else:
            problems.append(
                f"{row.note_path}: definition unit drifted since the review (sha256 {sha[:12]} != "
                f"reviewed {row.unit_sha256[:12]}) and does not carry the reviewed change"
            )
    if problems:
        raise CatalystReviewError("batch refused before any write:\n  " + "\n  ".join(problems))
    return plans


class ApplyReport(BaseModel):
    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)

    review_sha256: str
    written: list[str] = Field(default_factory=list)
    already_applied: list[str] = Field(default_factory=list)
    results: list[Any] = Field(default_factory=list)
    gate_ready: bool = False
    dry_run: bool = False


def verify_applied(vault_root: Path, review: CatalystReview) -> None:
    problems = []
    for row in review.rows:
        unit = _read_unit(vault_root, row.note_path, row.slug)
        try:
            if not is_applied(unit.body, row):
                problems.append(f"{row.note_path}: re-read does not carry the reviewed change")
                continue
            _validate_at_target(unit.body, unit, row)
        except CatalystReviewError as e:
            problems.append(str(e))
    if problems:
        raise CatalystReviewError(
            "applied, but the re-read does not satisfy schema 0.5 — the loader gate must NOT flip:\n  "
            + "\n  ".join(problems)
        )


def apply_review(vault_root: Path, review_path: Path, *, expected_sha256: str, writer) -> ApplyReport:
    raw = Path(review_path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != expected_sha256:
        raise CatalystReviewError(
            f"review file sha256 {digest} != --sha256 {expected_sha256}: these are not the bytes that were reviewed"
        )
    review = parse_review(raw.decode("utf-8"))
    plans = plan_apply(vault_root, review)
    report = ApplyReport(review_sha256=digest, dry_run=bool(writer.dry_run))
    report.already_applied = [p.row.slug for p in plans if p.action == "already_applied"]
    pending = [p for p in plans if p.action == "write"]
    for index, plan in enumerate(pending):
        applied_so_far = len(report.already_applied) + len(report.written)
        stop = f"applied so far: {applied_so_far} of {len(plans)} ({report.already_applied + report.written})"
        current = unit_sha256(_read_unit(vault_root, plan.row.note_path, plan.row.slug).body)
        if current != plan.before_sha256:
            raise CatalystReviewError(
                f"batch stopped: {plan.row.note_path} drifted during the batch (a human edit landed); {stop}. "
                "Nothing else was written; re-draft its row or restore the unit, then re-run to resume."
            )
        try:
            result = writer.upsert_unit(
                plan.path, DEFINITION_SECTION, f"{DEF_UNIT_PREFIX}{plan.row.slug}", plan.new_body,
            )
        except Exception as e:
            raise CatalystReviewError(
                f"batch stopped at {plan.row.note_path}: {type(e).__name__}: {e}; {stop}. "
                "Re-run the same command to resume — applied units are recognised, not rewritten."
            ) from e
        report.results.append(result)
        report.written.append(plan.row.slug)
    if report.dry_run:
        return report
    verify_applied(vault_root, review)
    report.gate_ready = True
    return report


# ---------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------


def default_review_path(today: date) -> Path:
    # docs/_inflight/ is gitignored (PLACEMENT.md) — the review carries
    # note paths and factor names, user data under L32; --out overrides.
    from cobalt.vault import REPO_ROOT

    return REPO_ROOT / "docs" / "_inflight" / f"catalyst-review-{today.isoformat()}.md"


def cmd_catalyst_review(args: argparse.Namespace) -> None:
    from cobalt.session.clock import now_utc, session_clock
    from cobalt.vault import resolve_vault_path

    today = session_clock().to_et(now_utc()).date()
    out = Path(args.out) if args.out else default_review_path(today)
    path, digest = write_review(resolve_vault_path(), out, today=today)
    print(f"catalyst review written: {path}\n  sha256 (as drafted, before marking): {digest}")
    print("  mark each row keep | drop | drop: <factor>, then hash the marked file for catalyst-apply.")


def cmd_catalyst_apply(args: argparse.Namespace) -> None:
    from cobalt.vault import resolve_vault_path
    from cobalt.vaultwrite import VaultWriter
    from cobalt.vaultwrite.store import VaultWriteStore

    if bool(args.dry_run) == bool(args.apply):
        raise SystemExit("cobalt taxonomy catalyst-apply: pass exactly one of --dry-run or --apply")
    store = VaultWriteStore()
    store.ensure_schema()
    writer = VaultWriter("taxonomy.catalyst_apply", store=store, dry_run=bool(args.dry_run))
    report = apply_review(resolve_vault_path(), Path(args.review), expected_sha256=args.sha256, writer=writer)
    for result in report.results:
        print(result.report())
    print(f"\nreview sha256 {report.review_sha256}")
    print(f"  written: {report.written or 'none'}")
    print(f"  already applied: {report.already_applied or 'none'}")
    if report.dry_run:
        print("DRY RUN — nothing written; schema 0.5 readiness is proven only by --apply's re-read.")
    else:
        print(f"GATE READY: every reviewed unit re-reads valid at schema {TARGET_SCHEMA} "
              "(the loader gate flips in code at STEP-D4, not here).")


__all__ = [
    "ApplyReport", "CatalystReview", "CatalystReviewError", "PROPOSED_LINE", "REVIEW_CLOSE", "REVIEW_OPEN",
    "ReviewRow", "UnitPlan", "apply_review", "cmd_catalyst_apply", "cmd_catalyst_review", "default_review_path",
    "draft_review", "is_applied", "parse_review", "plan_apply", "render_review", "target_body", "unit_sha256",
    "verify_applied", "write_review",
]
