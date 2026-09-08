"""L31 / ADR-0008 D5 — no trade name lives in this repo (a lint).

THE PRODUCT INSTALLS EMPTY. Everything named after a trade, everything
SMB- or cheat-sheet-derived, is USER data: it lives in a trader's vault
and never here (L32). Until 2026-09-08 the 13 sheet-derived defs were
committed YAML, their ids were written into test assertions and
docstrings, and a second config file carried a person's name in its
filename. All of it is gone (ADR-0008 D3/D5), and this test is what keeps
it gone — a docstring is exactly the place a trade name comes back.

THE LINT IS STRUCTURAL, NOT A DENYLIST, and that is deliberate. The
obvious implementation — a list of the 13 names, grepped for — would put
the trader's 13 trade names in a committed file, which is precisely the
leak the rule forbids. It would also only ever catch those thirteen. So
the rule is inverted instead:

    every trade slug and every per-trade tunable key written anywhere
    under src/ or tests/ begins with `example`.

That is leak-free, and it catches a name nobody has thought of yet. The
one synthetic def the repo ships (`example-range-break`) and the test
variants built from it all satisfy it; a real trade name cannot.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SEARCHED = (REPO_ROOT / "src", REPO_ROOT / "tests")
TAXONOMY_CONFIG = REPO_ROOT / "configs" / "cobalt" / "taxonomy"

#: Everything the repo may call a trade. One prefix, no exceptions.
ALLOWED_PREFIX = "example"

#: `trade_def: <slug>` (frontmatter) and `trade_def:<slug>` (unit id).
_SLUG_RE = re.compile(r"trade_def:\s?([a-z][a-z0-9-]*)")
#: `per_trade(<trade_key>)` — the tunables scope. `<id>`-style
#: placeholders in prose do not match (they are not `[a-z0-9_]`).
_SCOPE_RE = re.compile(r"per_trade\(([a-z][a-z0-9_]*)\)")

#: Two false positives that are the SCHEMA, not an instance of it:
#: `trade_def:` as a bare key with no slug after it, and the matrix view's
#: own column, which is literally named `trade_def`.
_NOT_A_SLUG = {"s", "the", "and"}


#: This file's own negative fixtures spell out what a violation looks
#: like, so it is the one file the lint does not read. It is also the one
#: file where a real trade name would be visible on sight in review.
SELF = Path(__file__).resolve()


def _files():
    for root in SEARCHED:
        for path in sorted(root.rglob("*")):
            if path.suffix not in (".py", ".sql", ".yaml", ".yml", ".md"):
                continue
            if "__pycache__" in path.parts or "egg-info" in str(path):
                continue
            if path.resolve() == SELF:
                continue
            yield path


def _offenders(pattern: re.Pattern, label: str) -> list[str]:
    out = []
    for path in _files():
        rel = str(path.relative_to(REPO_ROOT))
        for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for match in pattern.findall(line):
                if match in _NOT_A_SLUG or match.startswith(ALLOWED_PREFIX):
                    continue
                out.append(f"{rel}:{i}: {label} {match!r} -> {line.strip()[:80]}")
    return out


def test_every_trade_slug_in_the_repo_is_an_example():
    offenders = _offenders(_SLUG_RE, "slug")
    assert not offenders, (
        "L31 / ADR-0008 D5: a trade name is USER data and does not live in this "
        f"repo. Every slug written under src/ or tests/ starts with "
        f"{ALLOWED_PREFIX!r} — the one synthetic def and the fixtures built from "
        "it. Found:\n  " + "\n  ".join(offenders)
    )


def test_every_per_trade_tunable_key_in_the_repo_is_an_example():
    offenders = _offenders(_SCOPE_RE, "per_trade scope")
    assert not offenders, (
        "L31 / ADR-0008 D5: a per-trade tunable row belongs to one trader's "
        "trade and lives in that trade's note, not in this repo. Found:\n  "
        + "\n  ".join(offenders)
    )


def test_the_lint_would_actually_catch_one():
    """A lint nobody has seen fail is a lint nobody should trust."""
    assert _SLUG_RE.findall("trade_def: some-real-trade") == ["some-real-trade"]
    assert _SLUG_RE.findall("<!-- cobalt:unit trade_def:some-real-trade -->") == [
        "some-real-trade"
    ]
    assert _SCOPE_RE.findall("scope: per_trade(some_real_trade)") == [
        "some_real_trade"
    ]
    # ... and passes what the repo is allowed to say
    assert all(
        s.startswith(ALLOWED_PREFIX)
        for s in _SLUG_RE.findall("trade_def: example-range-break")
    )


def test_the_repo_ships_exactly_one_trade_def_and_it_is_synthetic():
    """ADR-0008 D3's last line, as an assertion.

    The taxonomy config directory is listed EXACTLY, not merely checked
    for the absence of the files that were deleted: a new file with a
    trade in it would pass a not-exists check and fail this one.
    """
    present = sorted(
        str(p.relative_to(TAXONOMY_CONFIG))
        for p in TAXONOMY_CONFIG.rglob("*")
        if p.is_file()
    )
    assert present == [
        "defaults.yaml",
        "examples/example_trade_def.md",
        "tunables.yaml",
    ], (
        "configs/cobalt/taxonomy holds the ENGINE's taxonomy config and one "
        f"synthetic example. Found: {present}"
    )


def test_the_setup_matrix_is_named_for_what_it_is():
    """D5: the matrix carried a person's name; it is `setup_trade_matrix`
    now, in the migration that builds it and in the store that reads it."""
    migration = (
        REPO_ROOT / "src" / "cobalt" / "taxonomy" / "migrations" / "0001_trade_defs.sql"
    ).read_text()
    store = (REPO_ROOT / "src" / "cobalt" / "taxonomy" / "store.py").read_text()
    assert "CREATE OR REPLACE VIEW setup_trade_matrix" in migration
    assert "setup_trade_matrix" in store


# ---------------------------------------------------------------------
# tunables.yaml is the ENGINE's file (ADR-0008 D3 b.3)
# ---------------------------------------------------------------------


def test_tunables_yaml_holds_no_per_trade_row():
    """Every trader's per-trade row lives in that trade's own note.

    `configs/cobalt/taxonomy/tunables.yaml` ships identically to every
    Cobalt install, so a row scoped to one trader's trade in it is the
    same leak as a committed trade_def — and it is the row the union in
    `merge_tunables` would then refuse as a collision.
    """
    import yaml

    from cobalt.taxonomy.loader import TUNABLES_PATH

    rows = yaml.safe_load(TUNABLES_PATH.read_text())["tunables"]
    per_trade = [r["key"] for r in rows if r["scope"].startswith("per_trade(")]
    assert not per_trade, (
        "ADR-0008 D3 b.3: these per-trade rows belong in their trade's note, "
        f"not in the engine's config: {per_trade}"
    )


def test_no_engine_tunable_key_is_named_after_a_trade():
    """The structural half of the same rule.

    An engine key names an ENGINE concept — a session boundary, a
    heartbeat interval, an anatomy threshold. It never begins with a
    trade's name, and the way to check that without listing anybody's
    trades is to require every remaining row to be `global` or
    `per_indicator(...)`: a trade-named key has nowhere else to be scoped.
    """
    import yaml

    from cobalt.taxonomy.loader import TUNABLES_PATH

    rows = yaml.safe_load(TUNABLES_PATH.read_text())["tunables"]
    bad = [
        (r["key"], r["scope"])
        for r in rows
        if r["scope"] != "global" and not r["scope"].startswith("per_indicator(")
    ]
    assert not bad, f"engine rows must be global or per_indicator: {bad}"
