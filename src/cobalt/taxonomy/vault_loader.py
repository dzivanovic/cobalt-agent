"""The vault note IS the trade_def's truth (ADR-0008 D3).

ONE PATH: vault unit -> this loader -> `"user".trade_defs`. There is no
repo copy of a trade_def any more. Until 2026-09-08 the 13 populated defs
existed twice — as committed YAML under `configs/cobalt/taxonomy/
trade_defs/` and, verbatim, inside the 22 strategy notes written on 09-06
— and the first edit to either copy would have made them disagree with
nothing to say which was right.

WHAT A STRATEGY NOTE LOOKS LIKE. `1 - Trading/4 - Strategies/<note>.md`:

    ---
    trade_def: example-range-break     <- THE ID (ruling a)
    name: Example Range Break          <- THE DISPLAY NAME (ruling e)
    class: scalp                       <- checked against the def, not trusted
    family: [range_break]
    status: defined                    <- checked, never trusted
    ---
    ## Definition
    <!-- cobalt:section definition -->
    <!-- cobalt:unit trade_def:example-range-break -->
    ```yaml
    trade_def:
      family: [range_break]
      ...                              <- NO id:, NO name:
    ```
    <!-- /cobalt:unit trade_def:example-range-break -->
    <!-- cobalt:unit tunables:example-range-break -->
    ```yaml
    tunables:
      - key: example_range_break.range_duration_band
        scope: per_trade(example_range_break)
        ...
    ```
    <!-- /cobalt:unit tunables:example-range-break -->
    <!-- /cobalt:section definition -->

TWO UNITS, NOT ONE, and that is deliberate (ADR-0008 D3 b.3): replay
writes a tunable row's `status` field, and a `status` write that had to
re-render the whole Definition unit would rewrite the def and every
comment a human left inside it.

DRAFT vs ERROR — the distinction this module exists to make. A note whose
Definition unit is empty, or holds only a partial mapping (the 9 notes
that carry `valid_setups` and nothing else), is a DRAFT: skipped, listed
with its reason, never an error — a trader in the middle of writing a
strategy must not break the loader. A unit that has the FULL shape and
then fails validation IS an error, named by note and field: that is a
def someone believes is finished and it is not.

STATUS AND CLASS/FAMILY ARE CHECKED, NEVER TRUSTED. `status: defined`
means "this validated" and nothing else, so the loader derives it and
reports frontmatter that disagrees. `playbook` is REFUSED outright — it
is earned at n >= 30 (R3), never typed. Frontmatter `class`/`family`
drift is a warning and THE HUMAN WINS: this is a read path, it corrects
nothing. `cobalt taxonomy sync-frontmatter` (S2, owed) re-aligns with a
diff.
"""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any, Optional

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError

from cobalt.vault import resolve_vault_path
from cobalt.vaultwrite.frontmatter import FrontmatterError, split_frontmatter
from cobalt.vaultwrite.markers import MarkerError, find_section

from .loader import (
    TaxonomyConfigError,
    iter_cfg_tokens,
    iter_tunables,
    is_ma_ref,
    load_defaults,
    load_tunables,
    merge_tunables,
    resolve_cfg,
    resolve_ma_ref,
)
from .predicate import PredicateSyntaxError
from .slug import SlugError, per_trade_scope, validate_slug
from .trade_def import Family, TradeClass, TradeDef
from .tunables import TunableRegistry, TunableRow, TunableSource

#: Where a trader's strategy notes live, relative to the vault root.
STRATEGIES_DIR = "1 - Trading/4 - Strategies"

#: FINAL §8 [R2F-07]: the ONE note the assumed defaults live in, OUTSIDE the
#: Strategies folder (beside the list-config note), in one marker-bounded
#: unit. Read by `load_assumed_tunables`; an absent note = no assumed rows.
ASSUMED_NOTE = "1 - Trading/Assumed Defaults.md"
ASSUMED_SECTION = "assumed"
ASSUMED_UNIT = "tunables:assumed"

#: The L28 section and the two unit-id prefixes inside it.
DEFINITION_SECTION = "definition"
DEF_UNIT_PREFIX = "trade_def:"
TUNABLES_UNIT_PREFIX = "tunables:"

#: A fenced YAML block inside a unit body. The fence is what separates
#: the machine-readable def from the prose a human may keep beside it.
_FENCE_RE = re.compile(r"```ya?ml\n(.*?)\n```", re.DOTALL)

#: Frontmatter `status:` values. `playbook` is refused — see the module
#: docstring and R3 (a playbook is earned at n >= 30, never typed).
STATUS_DEFINED = "defined"
STATUS_DRAFT = "draft"
STATUS_PLAYBOOK = "playbook"

#: The fields a mapping must carry before the loader will call it a
#: finished def rather than a draft. Everything else on `TradeDef` either
#: has a default or is injected. Derived from the model so a new required
#: field cannot be forgotten here.
def _required_unit_fields() -> set[str]:
    required = set()
    for name, field in TradeDef.model_fields.items():
        if name in TradeDef.INJECTED_FIELDS or not field.is_required():
            continue
        required.add(field.alias or name)
    return required


REQUIRED_UNIT_FIELDS = _required_unit_fields()


class VaultTaxonomyError(TaxonomyConfigError):
    """A strategy note is wrong in a way a human must fix."""


class LoadedTradeDef(BaseModel):
    """A validated def plus where it came from — what the store persists."""

    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)

    slug: str
    name: str
    #: Vault-relative, so the row means the same thing on any machine.
    note_path: str
    #: md5 of the unit's YAML text as authored. The change detector: a
    #: reload whose md5 matches wrote the same bytes.
    md5: str
    definition: TradeDef


class LoadedTunable(BaseModel):
    model_config = ConfigDict(extra="forbid")

    key: str
    #: The def the row belongs to; None for a `global` assumed row (FINAL
    #: §8, R2-3 = B — `"user".tunables.slug` is nullable from 0013).
    slug: Optional[str]
    note_path: str
    row: TunableRow


class DraftNote(BaseModel):
    model_config = ConfigDict(extra="forbid")

    slug: str
    note_path: str
    reason: str


class VaultTradeDefs(BaseModel):
    """Everything one read of the Strategies folder produced."""

    model_config = ConfigDict(extra="forbid")

    defs: list[LoadedTradeDef] = Field(default_factory=list)
    drafts: list[DraftNote] = Field(default_factory=list)
    user_tunables: list[LoadedTunable] = Field(default_factory=list)
    #: Frontmatter that disagrees with the def. The human wins; these are
    #: reported, never applied.
    warnings: list[str] = Field(default_factory=list)

    @property
    def by_slug(self) -> dict[str, TradeDef]:
        return {d.slug: d.definition for d in self.defs}

    @property
    def tunable_rows(self) -> dict[str, TunableRow]:
        return {t.key: t.row for t in self.user_tunables}


def _fence(body: str) -> Optional[str]:
    m = _FENCE_RE.search(body)
    return m.group(1) if m else None


def _load_mapping(text: str, where: str) -> dict[str, Any]:
    try:
        raw = yaml.safe_load(text)
    except yaml.YAMLError as e:
        raise VaultTaxonomyError(f"{where}: the fenced YAML does not parse:\n{e}") from e
    if not isinstance(raw, dict):
        raise VaultTaxonomyError(
            f"{where}: expected a YAML mapping, got {type(raw).__name__}"
        )
    return raw


def _check_frontmatter_agreement(
    fm: dict[str, Any], td: TradeDef, where: str
) -> list[str]:
    """`class` / `family` drift, as warnings. The human wins."""
    warnings: list[str] = []
    if "class" in fm and fm["class"] not in (None, ""):
        try:
            declared = TradeClass(fm["class"])
        except ValueError:
            warnings.append(
                f"{where}: frontmatter class={fm['class']!r} is not a TradeClass "
                f"(def says {td.trade_class.value!r})"
            )
        else:
            if declared is not td.trade_class:
                warnings.append(
                    f"{where}: frontmatter class={declared.value!r} but the def says "
                    f"{td.trade_class.value!r} — the human wins; run "
                    "`cobalt taxonomy sync-frontmatter` to re-align."
                )
    if "family" in fm and fm["family"] not in (None, "", []):
        raw = fm["family"]
        declared_raw = raw if isinstance(raw, list) else [raw]
        try:
            declared_fams = [Family(f) for f in declared_raw]
        except ValueError:
            warnings.append(
                f"{where}: frontmatter family={raw!r} is not a Family list "
                f"(def says {[f.value for f in td.family]})"
            )
        else:
            if set(declared_fams) != set(td.family):
                warnings.append(
                    f"{where}: frontmatter family={[f.value for f in declared_fams]} "
                    f"but the def says {[f.value for f in td.family]} — the human "
                    "wins; run `cobalt taxonomy sync-frontmatter` to re-align."
                )
    return warnings


def _check_status(fm: dict[str, Any], *, validated: bool, where: str) -> list[str]:
    """`status` is DERIVED and the frontmatter is compared to it."""
    declared = fm.get("status")
    if declared == STATUS_PLAYBOOK:
        raise VaultTaxonomyError(
            f"{where}: frontmatter status: playbook. A playbook is EARNED at "
            "n >= 30 (R3, sample-size law) and is never typed into a note. Use "
            f"{STATUS_DEFINED!r} or {STATUS_DRAFT!r}."
        )
    derived = STATUS_DEFINED if validated else STATUS_DRAFT
    if declared != derived:
        return [
            f"{where}: frontmatter status={declared!r} but this unit "
            f"{'validated' if validated else 'did not validate'}, so it is "
            f"{derived!r} — the human wins; the loader reports, it does not edit."
        ]
    return []


def _read_tunables_unit(
    body: str, *, slug: str, note_path: str
) -> list[LoadedTunable]:
    """The optional second unit: this trader's per-trade tunable rows."""
    text = _fence(body)
    if text is None or not text.strip():
        return []
    where = f"{note_path} (tunables:{slug})"
    raw = _load_mapping(text, where)
    try:
        registry = TunableRegistry(**raw)
    except ValidationError as e:
        raise VaultTaxonomyError(f"{where}: invalid tunables rows:\n{e}") from e

    expected_scope = per_trade_scope(slug)
    rows: list[LoadedTunable] = []
    for row in registry.tunables:
        if row.source is TunableSource.ASSUMED:
            raise VaultTaxonomyError(
                f"{where}: tunable {row.key!r} is marked `source: assumed`. An assumed "
                f"default has ONE home, {ASSUMED_NOTE!r} (unit {ASSUMED_UNIT!r}); a row "
                "in a strategy note is the trader's own ruled number."
            )
        if row.scope != expected_scope:
            raise VaultTaxonomyError(
                f"{where}: tunable {row.key!r} has scope {row.scope!r}, expected "
                f"{expected_scope!r}. A row in a strategy note is that trade's own "
                "row; a global or per-indicator row belongs in "
                "configs/cobalt/taxonomy/tunables.yaml (engine side)."
            )
        rows.append(
            LoadedTunable(key=row.key, slug=slug, note_path=note_path, row=row)
        )
    return rows


def _locate_predicate_errors(
    error: Exception, lines: list[str], unit, *, note_path: str, slug: str
) -> str:
    """`<note>:<line> (trade_def:<slug>): <syntax error>` per bad expr.

    R3: a parse failure must be locatable in the vault unit, so the
    expression text is searched for inside the unit's own line range and
    the 1-based note line is named. An expression that cannot be found
    verbatim (YAML escaping) is still reported, at the unit's opening
    marker line — never dropped.
    """
    found = []
    if isinstance(error, ValidationError):
        for item in error.errors():
            exc = (item.get("ctx") or {}).get("error")
            if isinstance(exc, PredicateSyntaxError):
                found.append(exc)
    elif isinstance(error, PredicateSyntaxError):
        found.append(error)
    out = []
    for exc in found:
        line_no = unit.open_line + 1
        for index in range(unit.open_line, unit.close_line + 1):
            if exc.expr and exc.expr in lines[index]:
                line_no = index + 1
                break
        out.append(f"{note_path}:{line_no} (trade_def:{slug}): {exc}\n")
    return "".join(out)


def _read_note(path: Path, vault_root: Path) -> tuple[
    Optional[LoadedTradeDef], Optional[DraftNote], list[LoadedTunable], list[str]
]:
    note_path = str(path.relative_to(vault_root))
    text = path.read_text(encoding="utf-8")

    try:
        fm, _ = split_frontmatter(text)
    except FrontmatterError as e:
        raise VaultTaxonomyError(f"{note_path}: {e}") from e
    if fm is None:
        raise VaultTaxonomyError(
            f"{note_path}: no frontmatter. Every strategy note carries "
            "`trade_def:` (the id) and `name:` (the display name) — ADR-0008 D3."
        )

    try:
        slug = validate_slug(fm.get("trade_def"), where=note_path)
    except SlugError as e:
        raise VaultTaxonomyError(str(e)) from e

    name = fm.get("name")
    if not isinstance(name, str) or not name.strip():
        raise VaultTaxonomyError(
            f"{note_path}: frontmatter `name:` is missing or empty. It is the "
            "trade's display name (ADR-0008 D3 ruling e) and the loader injects "
            "it — the YAML unit must not carry its own."
        )
    name = name.strip()

    lines = text.splitlines()
    try:
        section = find_section(lines, DEFINITION_SECTION)
    except MarkerError as e:
        raise VaultTaxonomyError(f"{note_path}: {e}") from e
    if section is None:
        raise VaultTaxonomyError(
            f"{note_path}: no `{DEFINITION_SECTION}` section. The def lives inside "
            f"<!-- cobalt:section {DEFINITION_SECTION} --> (LAW L28)."
        )

    def_unit_id = f"{DEF_UNIT_PREFIX}{slug}"
    unit = section.units.get(def_unit_id)
    if unit is None:
        raise VaultTaxonomyError(
            f"{note_path}: the `{DEFINITION_SECTION}` section has no unit "
            f"{def_unit_id!r} (found: {sorted(section.units) or 'none'}). The unit "
            "id is derived from the frontmatter slug and must match it."
        )

    body = "\n".join(unit.body(lines))
    warnings: list[str] = []

    tunables_unit = section.units.get(f"{TUNABLES_UNIT_PREFIX}{slug}")
    tunables = (
        _read_tunables_unit(
            "\n".join(tunables_unit.body(lines)), slug=slug, note_path=note_path
        )
        if tunables_unit is not None
        else []
    )

    # ---- draft? -------------------------------------------------------
    fence = _fence(body)
    if fence is None or not fence.strip():
        warnings += _check_status(fm, validated=False, where=note_path)
        return (
            None,
            DraftNote(
                slug=slug,
                note_path=note_path,
                reason="Definition unit is empty — nothing authored yet",
            ),
            tunables,
            warnings,
        )

    where = f"{note_path} (trade_def:{slug})"
    raw = _load_mapping(fence, where)
    if "trade_def" not in raw:
        raise VaultTaxonomyError(
            f"{where}: the fenced YAML has no top-level `trade_def:` key."
        )
    mapping = raw["trade_def"]
    if mapping is None:
        warnings += _check_status(fm, validated=False, where=note_path)
        return (
            None,
            DraftNote(
                slug=slug, note_path=note_path,
                reason="`trade_def:` is present but empty",
            ),
            tunables,
            warnings,
        )
    if not isinstance(mapping, dict):
        raise VaultTaxonomyError(
            f"{where}: `trade_def:` must be a mapping, got {type(mapping).__name__}"
        )

    missing = sorted(REQUIRED_UNIT_FIELDS - set(mapping))
    if missing:
        warnings += _check_status(fm, validated=False, where=note_path)
        return (
            None,
            DraftNote(
                slug=slug,
                note_path=note_path,
                reason=f"partial definition — missing {missing}",
            ),
            tunables,
            warnings,
        )

    # ---- a finished def: from here on, a failure is an ERROR ----------
    try:
        td = TradeDef.from_unit(mapping, slug=slug, name=name)
    except (ValidationError, ValueError) as e:
        located = _locate_predicate_errors(
            e, lines, unit, note_path=note_path, slug=slug
        )
        raise VaultTaxonomyError(f"{located}{where}: invalid trade_def:\n{e}") from e

    warnings += _check_status(fm, validated=True, where=note_path)
    warnings += _check_frontmatter_agreement(fm, td, note_path)

    return (
        LoadedTradeDef(
            slug=slug,
            name=name,
            note_path=note_path,
            md5=hashlib.md5(fence.encode("utf-8")).hexdigest(),
            definition=td,
        ),
        None,
        tunables,
        warnings,
    )


def load_vault_trade_defs(vault_root: Optional[Path] = None) -> VaultTradeDefs:
    """Read every strategy note. Defs, drafts, user tunables, warnings.

    Fails loud on anything a human must fix: a bad slug, a missing
    `name:`, a malformed section, a duplicate slug, a unit that authors
    `id:`, a finished def that does not validate, a per-trade row on the
    wrong scope, a user row shadowing an engine key, an unknown `cfg()`.
    Drafts are none of those and are listed, not raised.
    """
    root = Path(vault_root) if vault_root is not None else resolve_vault_path()
    directory = root / STRATEGIES_DIR
    if not directory.is_dir():
        raise VaultTaxonomyError(
            f"strategy notes directory not found: {directory}. The trade_defs live "
            f"in the vault under {STRATEGIES_DIR!r} (ADR-0008 D3), not in the repo."
        )

    result = VaultTradeDefs()
    seen: dict[str, str] = {}
    for path in sorted(directory.glob("*.md")):
        loaded, draft, tunables, warnings = _read_note(path, root)
        slug = loaded.slug if loaded is not None else draft.slug  # type: ignore[union-attr]
        if slug in seen:
            raise VaultTaxonomyError(
                f"duplicate trade_def slug {slug!r}: "
                f"{seen[slug]} and {path.relative_to(root)}. The slug is the trade's "
                "identity — two notes cannot claim the same trade."
            )
        seen[slug] = str(path.relative_to(root))
        if loaded is not None:
            result.defs.append(loaded)
        if draft is not None:
            result.drafts.append(draft)
        result.user_tunables.extend(tunables)
        result.warnings.extend(warnings)

    result.user_tunables.extend(load_assumed_tunables(root, loaded_slugs={d.slug for d in result.defs}))
    suppliers: dict[str, str] = {}
    for tunable in result.user_tunables:
        if tunable.key in suppliers:
            raise VaultTaxonomyError(
                f"duplicate tunable key {tunable.key!r}: supplied by {suppliers[tunable.key]} and "
                f"{tunable.note_path}. One key, one row."
            )
        suppliers[tunable.key] = tunable.note_path
    _resolve_every_cfg(result)
    return result


def load_assumed_tunables(vault_root: Path, *, loaded_slugs: set[str]) -> list[LoadedTunable]:
    """FINAL §8 (R2-3.1 B): the assumed rows, from `ASSUMED_NOTE`'s one unit.

    An absent note is no rows, not an error. Every row validates through
    `TunableRegistry`, carries scope `global`, `per_trade(<a def loaded in
    this pass>)` or — R48 (F1 WIDENED, fix r3 F2) — `per_indicator(<ind>)`
    for a key whose committed engine row carries that SAME scope and a null
    value (a HOLE); any other `per_indicator` row is refused, naming why
    (L1). `source` is assumed or ruling. A `global` or `per_indicator` row
    has no def: its `slug` is None."""
    path = Path(vault_root) / ASSUMED_NOTE
    if not path.exists():
        return []
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        section = find_section(lines, ASSUMED_SECTION)
    except MarkerError as e:
        raise VaultTaxonomyError(f"{ASSUMED_NOTE}: {e}") from e
    unit = section.units.get(ASSUMED_UNIT) if section is not None else None
    if unit is None:
        raise VaultTaxonomyError(
            f"{ASSUMED_NOTE}: no unit {ASSUMED_UNIT!r} inside <!-- cobalt:section {ASSUMED_SECTION} -->"
        )
    text = _fence("\n".join(unit.body(lines)))
    if text is None or not text.strip():
        return []
    where = f"{ASSUMED_NOTE} ({ASSUMED_UNIT})"
    raw = _load_mapping(text, where)
    if not raw.get("tunables"):
        return []
    try:
        registry = TunableRegistry(**raw)
    except ValidationError as e:
        raise VaultTaxonomyError(f"{where}: invalid tunables rows:\n{e}") from e
    per_trade = {per_trade_scope(slug): slug for slug in loaded_slugs}
    engine = load_tunables().by_key
    rows: list[LoadedTunable] = []
    for row in registry.tunables:
        if row.source not in (TunableSource.ASSUMED, TunableSource.RULING):
            raise VaultTaxonomyError(
                f"{where}: tunable {row.key!r} has source {row.source.value!r}; an assumed-defaults row "
                "reads `assumed` until he rules it, then `ruling`."
            )
        if row.scope == "global":
            slug = None
        elif row.scope in per_trade:
            slug = per_trade[row.scope]
        elif row.scope.startswith("per_indicator("):
            hole = engine.get(row.key)
            why = ("it has no engine row" if hole is None
                   else f"its engine row's scope is {hole.scope!r}" if hole.scope != row.scope
                   else "its engine row is not a hole (it carries a value)" if hole.value is not None
                   else None)
            if why is not None:
                raise VaultTaxonomyError(
                    f"{where}: tunable {row.key!r} has scope {row.scope!r}, but {why}. A per_indicator "
                    "row fills ONLY an engine hole (`value: null`) of that same per_indicator scope (R48)."
                )
            slug = None
        else:
            raise VaultTaxonomyError(
                f"{where}: tunable {row.key!r} has scope {row.scope!r}. The reader accepts `global`, "
                "`per_trade(<a def loaded in this pass>)`, or `per_indicator(<ind>)` filling an engine "
                "hole of that same scope."
            )
        rows.append(LoadedTunable(key=row.key, slug=slug, note_path=ASSUMED_NOTE, row=row))
    return rows


def _resolve_every_cfg(result: VaultTradeDefs) -> None:
    """Every `cfg()` token in every def resolves, against the UNION.

    Load-time, not first-use: an unknown key discovered at 09:31 on a
    live morning is the failure mode this check exists to move to boot.
    """
    defaults = load_defaults()
    try:
        merged = merge_tunables(load_tunables().by_key, result.tunable_rows)
    except TaxonomyConfigError as e:
        notes = sorted({t.note_path for t in result.user_tunables})
        raise VaultTaxonomyError(f"{', '.join(notes)}: {e}") from e
    for loaded in result.defs:
        for tunable in iter_tunables(loaded.definition):
            if isinstance(tunable.value, str) and is_ma_ref(tunable.value):
                resolve_ma_ref(tunable.value, defaults)
        for cfg_key in iter_cfg_tokens(loaded.definition):
            try:
                resolve_cfg(cfg_key, merged, defaults)
            except TaxonomyConfigError as e:
                raise VaultTaxonomyError(
                    f"{loaded.note_path} (trade_def:{loaded.slug}): {e}"
                ) from e


__all__ = [
    "ASSUMED_NOTE",
    "ASSUMED_SECTION",
    "ASSUMED_UNIT",
    "DEFINITION_SECTION",
    "DEF_UNIT_PREFIX",
    "REQUIRED_UNIT_FIELDS",
    "STRATEGIES_DIR",
    "TUNABLES_UNIT_PREFIX",
    "DraftNote",
    "LoadedTradeDef",
    "LoadedTunable",
    "VaultTaxonomyError",
    "VaultTradeDefs",
    "load_assumed_tunables",
    "load_vault_trade_defs",
]
