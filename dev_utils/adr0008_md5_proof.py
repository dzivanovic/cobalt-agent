"""ADR-0008 D3 — the PROOF that must pass before the 13 YAMLs are deleted.

WHY IT EXISTS. The 13 populated trade_defs lived twice: as committed YAML
under `configs/cobalt/taxonomy/trade_defs/<id>.yaml`, and verbatim inside
the strategy notes written on 2026-09-06. ADR-0008 keeps the note and
deletes the YAML — which is only safe if the two copies are actually the
same def. This script is that check, and its table goes into the report.

WHAT IT COMPARES, and why the comparison is not naive:

* The YAML file's `trade_def` mapping, MINUS `id` and `name` (the note's
  frontmatter owns both now — ADR-0008 rulings a and e).
* The note unit's `trade_def` mapping, minus the same two keys. At the
  time this runs the units STILL carry `id:`/`name:` — step 4 removes
  them — so stripping is what makes the two sides comparable rather than
  a way of hiding a difference.
* Both are canonicalised (`yaml.safe_dump(sort_keys=True)`) before
  hashing, so a re-ordered key or a re-flowed block is not reported as a
  changed def. A CHANGED VALUE still is.

It also re-checks the SECOND fold ADR-0008 makes: each YAML's
`quality_factors[]` name set must equal its `variables/<id>.yaml`
registry's name set. That check used to run on every load; the registry
file is about to be folded into `quality_factors[]` (step 4) and this is
the last moment it can be verified against the file it came from.

READ-ONLY. It writes nothing, deletes nothing and touches no database.
Run it, read the table, and only then delete.

    COBALT_ENV=dev uv run python dev_utils/adr0008_md5_proof.py [--vault PATH]

`--vault` defaults to whatever `COBALT_ENV` resolves — in dev, the dev
vault, which is where the corpus was copied for exactly this proof.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path
from typing import Any, Optional

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "src"))

from cobalt.taxonomy.loader import TAXONOMY_DIR  # noqa: E402
from cobalt.vault import resolve_vault_path  # noqa: E402
from cobalt.vaultwrite.frontmatter import split_frontmatter  # noqa: E402
from cobalt.vaultwrite.markers import find_section  # noqa: E402

TRADE_DEFS_DIR = TAXONOMY_DIR / "trade_defs"
VARIABLES_DIR = TAXONOMY_DIR / "variables"
STRATEGIES_DIR = "1 - Trading/4 - Strategies"

#: Loader-injected from the note's frontmatter; not part of the def's body.
INJECTED = ("id", "name")

_FENCE_RE = re.compile(r"```ya?ml\n(.*?)\n```", re.DOTALL)


def canonical_md5(mapping: dict[str, Any]) -> tuple[str, str]:
    """(md5, canonical text) of a def mapping with id/name stripped."""
    body = {k: v for k, v in mapping.items() if k not in INJECTED}
    text = yaml.safe_dump(body, sort_keys=True, default_flow_style=False)
    return hashlib.md5(text.encode("utf-8")).hexdigest(), text


def read_yaml_def(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))["trade_def"]


def read_note_defs(vault_root: Path) -> dict[str, tuple[Path, dict[str, Any]]]:
    """{slug: (note path, trade_def mapping)} for every populated unit."""
    out: dict[str, tuple[Path, dict[str, Any]]] = {}
    for note in sorted((vault_root / STRATEGIES_DIR).glob("*.md")):
        text = note.read_text(encoding="utf-8")
        fm, _ = split_frontmatter(text)
        if not fm or not fm.get("trade_def"):
            continue
        slug = fm["trade_def"]
        section = find_section(text.splitlines(), "definition")
        if section is None:
            continue
        unit = section.units.get(f"trade_def:{slug}")
        if unit is None:
            continue
        body = "\n".join(unit.body(text.splitlines()))
        fence = _FENCE_RE.search(body)
        if fence is None or not fence.group(1).strip():
            continue          # a draft; it has no YAML twin to compare
        mapping = yaml.safe_load(fence.group(1)).get("trade_def")
        if isinstance(mapping, dict):
            out[slug] = (note, mapping)
    return out


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, default=None)
    args = parser.parse_args(argv)
    vault_root = args.vault or resolve_vault_path()

    yaml_defs = {
        path.stem: read_yaml_def(path) for path in sorted(TRADE_DEFS_DIR.glob("*.yaml"))
    }
    note_defs = read_note_defs(vault_root)

    # The YAML id is the note's slug with hyphens for underscores — EXCEPT
    # the three ruling `a` records as not inter-derivable. Pair on the
    # YAML's own `id:` against the note unit's `id:`, which is the only
    # link that exists before step 4 removes them.
    by_note_id = {m.get("id"): (slug, note, m) for slug, (note, m) in note_defs.items()}

    rows: list[tuple[str, str, str, str, str]] = []
    for yaml_id, yaml_map in sorted(yaml_defs.items()):
        pair = by_note_id.get(yaml_map.get("id", yaml_id))
        if pair is None:
            rows.append((yaml_id, "-", "-", "-", "NO NOTE"))
            continue
        slug, _note, note_map = pair
        y_md5, y_text = canonical_md5(yaml_map)
        n_md5, n_text = canonical_md5(note_map)
        verdict = "EQUAL" if y_md5 == n_md5 else "DIFF"
        rows.append((yaml_id, slug, y_md5, n_md5, verdict))
        if verdict == "DIFF":
            _print_first_difference(yaml_id, y_text, n_text)

    header = f"{'yaml id':<22} {'note slug':<22} {'yaml md5':<34} {'note md5':<34} verdict"
    print(header)
    print("-" * len(header))
    for row in rows:
        print(f"{row[0]:<22} {row[1]:<22} {row[2]:<34} {row[3]:<34} {row[4]}")
    print("-" * len(header))

    equal = sum(1 for r in rows if r[4] == "EQUAL")
    print(
        f"{equal}/{len(rows)} def(s) EQUAL "
        "(md5 over the trade_def mapping minus id/name, "
        "yaml.safe_dump(sort_keys=True) canonicalised)."
    )

    var_ok = _check_variable_registries(yaml_defs)
    orphans = sorted(set(by_note_id) - {m.get("id", i) for i, m in yaml_defs.items()})
    if orphans:
        print(f"\nNote units with no YAML twin: {orphans}")

    ok = equal == len(rows) and var_ok and not orphans
    print(
        "\nPROOF PASSED — the YAMLs may be deleted."
        if ok
        else "\nPROOF FAILED — do NOT delete."
    )
    return 0 if ok else 1


def _print_first_difference(name: str, a: str, b: str) -> None:
    import difflib

    diff = list(difflib.unified_diff(a.splitlines(), b.splitlines(), "yaml", "note", n=1))
    print(f"\n--- {name}: first differences ---")
    print("\n".join(diff[:40]))
    print()


def _check_variable_registries(yaml_defs: dict[str, dict[str, Any]]) -> bool:
    """quality_factors[] == variables/<id>.yaml, one last time."""
    print(
        f"\n{'yaml id':<22} {'#quality_factors':<18} {'#registry':<12} verdict"
    )
    ok = True
    for yaml_id, mapping in sorted(yaml_defs.items()):
        qf = set(mapping.get("quality_factors") or [])
        registry_path = VARIABLES_DIR / f"{yaml_id}.yaml"
        if not registry_path.exists():
            print(f"{yaml_id:<22} {len(qf):<18} {'-':<12} NO REGISTRY")
            ok = False
            continue
        registry = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
        names = {v["name"] for v in registry["variables"]}
        verdict = "EQUAL" if names == qf else f"DIFF {sorted(qf ^ names)}"
        if names != qf:
            ok = False
        print(f"{yaml_id:<22} {len(qf):<18} {len(names):<12} {verdict}")
    print(
        "quality_factors[] vs variables/<id>.yaml: "
        + ("every set EQUAL." if ok else "MISMATCH — do not fold.")
    )
    return ok


if __name__ == "__main__":
    sys.exit(main())
