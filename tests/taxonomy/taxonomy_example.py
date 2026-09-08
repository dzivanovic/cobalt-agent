"""The synthetic example note, as a test helper.

Shared by `conftest.py` and the test modules. A plain module rather than
conftest constants because `tests/taxonomy` is not a package, so a test
module cannot do a relative import from its own conftest; pytest puts
this directory on `sys.path`, which makes a normal import work.
"""

from __future__ import annotations

import copy
import re
from pathlib import Path
from typing import Any, Optional

import yaml

from cobalt.taxonomy.loader import EXAMPLE_NOTE_PATH

EXAMPLE_SLUG = "example-range-break"
EXAMPLE_NAME = "Example Range Break"

_FENCE_RE = re.compile(r"```ya?ml\n(.*?)\n```", re.DOTALL)
_DEF_UNIT_RE = re.compile(
    r"<!-- cobalt:unit trade_def:[^>]*-->\n(.*?)<!-- /cobalt:unit trade_def:",
    re.DOTALL,
)


def example_note_text() -> str:
    return EXAMPLE_NOTE_PATH.read_text(encoding="utf-8")


def example_def_mapping(note_text: Optional[str] = None) -> dict[str, Any]:
    """The example note's `trade_def:` mapping — no `id`, no `name`."""
    text = note_text if note_text is not None else example_note_text()
    unit = _DEF_UNIT_RE.search(text)
    assert unit, "the example note has no trade_def unit"
    fence = _FENCE_RE.search(unit.group(1))
    assert fence, "the example note's trade_def unit has no YAML fence"
    return copy.deepcopy(yaml.safe_load(fence.group(1))["trade_def"])





def render_note(
    slug: str,
    name: str,
    *,
    def_yaml: Optional[str] = None,
    tunables_yaml: Optional[str] = None,
    status: Optional[str] = "defined",
    extra_frontmatter: Optional[dict[str, Any]] = None,
) -> str:
    """A strategy note in the exact vault shape (ADR-0008 D3).

    `def_yaml` is the BODY of the definition unit's fence — pass None for
    an empty unit (a draft). Same for `tunables_yaml`. The shape here is
    the shipped example's shape, and if the two ever diverge the loader's
    tests are testing a note nobody writes.
    """
    fm = {"trade_def": slug, "name": name}
    if status is not None:
        fm["status"] = status
    fm.update(extra_frontmatter or {})
    header = "\n".join(f"{k}: {_fm_value(v)}" for k, v in fm.items())

    def_body = f"```yaml\n{def_yaml}\n```\n" if def_yaml else ""
    tunables_unit = (
        f"<!-- cobalt:unit tunables:{slug} -->\n"
        f"```yaml\n{tunables_yaml}\n```\n"
        f"<!-- /cobalt:unit tunables:{slug} -->\n"
        if tunables_yaml
        else ""
    )
    return (
        f"---\n{header}\n---\n"
        "## Definition\n"
        "<!-- cobalt:section definition -->\n"
        f"<!-- cobalt:unit trade_def:{slug} -->\n"
        f"{def_body}"
        f"<!-- /cobalt:unit trade_def:{slug} -->\n"
        f"{tunables_unit}"
        "<!-- /cobalt:section definition -->\n"
        "\n## Stats\n"
        "<!-- cobalt:section stats -->\n"
        f"<!-- cobalt:unit stats:{slug} -->\n"
        "n: insufficient data (n<30)\n"
        f"<!-- /cobalt:unit stats:{slug} -->\n"
        "<!-- /cobalt:section stats -->\n"
    )


def _fm_value(value: Any) -> str:
    if isinstance(value, list):
        return "[" + ", ".join(str(v) for v in value) + "]"
    return "" if value is None else str(value)


def example_def_yaml(*, slug: str = EXAMPLE_SLUG, **overrides: Any) -> str:
    """The example's def mapping, optionally patched, as fence text.

    `slug` RE-KEYS the per-trade `cfg()` reference the example carries, so
    a synthetic note built for another slug resolves against its OWN
    tunables unit rather than the example's. That is not test scaffolding
    dodging a check — it is the same `trade_key()` rewrite a trader does
    by hand when they copy a strategy.
    """
    mapping = example_def_mapping()
    mapping.update(overrides)
    text = yaml.safe_dump({"trade_def": mapping}, sort_keys=False)
    return _retarget(text, slug)


def example_tunables_yaml(slug: str = EXAMPLE_SLUG) -> str:
    """The example note's own tunables unit, re-keyed for `slug`."""
    return _retarget(
        "tunables:\n"
        "  - key: example_range_break.range_duration_band\n"
        "    value: [4, 20]\n"
        "    unit: min\n"
        "    scope: per_trade(example_range_break)\n"
        "    dynamic: true\n"
        "    status: proposed\n"
        "    source: ruling\n",
        slug,
    )


def finished_note(slug: str, name: str, **frontmatter: Any) -> str:
    """A complete, VALID strategy note for `slug` — def + tunables unit."""
    return render_note(
        slug,
        name,
        def_yaml=example_def_yaml(slug=slug),
        tunables_yaml=example_tunables_yaml(slug),
        **frontmatter,
    )


def _retarget(text: str, slug: str) -> str:
    from cobalt.taxonomy.slug import trade_key

    return text.replace("example_range_break", trade_key(slug))


__all__ = [
    "EXAMPLE_NAME",
    "EXAMPLE_NOTE_PATH",
    "EXAMPLE_SLUG",
    "example_def_mapping",
    "example_def_yaml",
    "example_tunables_yaml",
    "finished_note",
    "example_note_text",
    "render_note",
]
