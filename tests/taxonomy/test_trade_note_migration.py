"""Trade notes gain `trade_def:` (ADR-0008 D4) — on synthetic notes only.

The real corpus is 69 of Dejan's trade notes and the free-text names he
typed into them over two years: user data (L32), none of it here. What is
testable without any of it is the whole of the mechanism — the alias
index built FROM a vault, the matching rules that make a value find a
slug, and the single-line insert that leaves every other byte alone.

The quoting cases are not hypothetical. The corpus really contains a
value that is a quoted string inside a quoted string with leading spaces,
because a Templater dropdown wrote it that way, and a matcher that strips
one layer would silently match nothing.
"""

from __future__ import annotations

import pytest

from cobalt.taxonomy.note_migration import NoteMigrationError
from cobalt.taxonomy.trade_note_migration import (
    build_alias_index,
    insert_trade_def_line,
    normalise,
    plan_trade_notes,
)

from taxonomy_example import finished_note, render_note

TRADES_DIR = "1 - Trading/2 - Trades"


def _trade_note(strategy: str | None, *, extra: str = "") -> str:
    line = "" if strategy is None else f"strategy:{strategy}\n"
    return (
        "---\n"
        "date: 2026-09-01 09:31\n"
        "symbol: NVDA\n"
        f"{line}"
        f"{extra}"
        "RVOL:\n"
        "tags:\n"
        "  - trade\n"
        "---\n"
        "# Trade\n"
        "body the command must not touch\n"
    )


@pytest.fixture
def vault(tmp_path, make_vault, example_note):
    """A vault with one strategy note and whatever trade notes a test adds."""
    root = make_vault({"Example Range Break": example_note})

    def _add(notes: dict[str, str]):
        directory = root / TRADES_DIR
        directory.mkdir(parents=True, exist_ok=True)
        for name, text in notes.items():
            (directory / f"{name}.md").write_text(text, encoding="utf-8")
        return root

    _add({})
    return root, _add


# ---------------------------------------------------------------------
# normalise
# ---------------------------------------------------------------------


class TestNormalise:
    @pytest.mark.parametrize(
        "raw",
        [
            "Example Range Break",
            " Example Range Break",
            '"Example Range Break"',
            '"  Example Range Break"',
            "'\"  Example Range Break\"'",     # the doubled-quote form
            "example range break",
        ],
    )
    def test_all_these_are_the_same_value(self, raw):
        assert normalise(raw) == "example range break"

    def test_interior_punctuation_is_untouched(self):
        """`Gap, Give and Go` and `Gap Give and Go` are different names."""
        assert normalise("Gap, Give and Go") != normalise("Gap Give and Go")

    def test_blank_forms(self):
        assert normalise("") == ""
        assert normalise("   ") == ""
        assert normalise('""') == ""


# ---------------------------------------------------------------------
# the alias index, read out of a vault
# ---------------------------------------------------------------------


class TestAliasIndex:
    def test_it_indexes_slug_name_and_aliases(self, vault):
        root, _add = vault
        index = build_alias_index(root)
        assert index.match("example-range-break") == "example-range-break"
        assert index.match("Example Range Break") == "example-range-break"
        assert index.match("Example Break") == "example-range-break"   # aliases[]

    def test_an_unknown_value_matches_nothing(self, vault):
        root, _add = vault
        assert build_alias_index(root).match("Never Heard Of It") is None

    def test_a_blank_value_matches_nothing(self, vault):
        root, _add = vault
        assert build_alias_index(root).match("   ") is None

    def test_two_notes_claiming_one_name_is_loud(self, make_vault, example_note):
        root = make_vault(
            {
                "Example Range Break": example_note,
                "Example Twin": finished_note("example-twin", "Example Twin").replace(
                    "aliases: [Example Break]", "aliases: [Example Break]"
                ),
            }
        )
        index = build_alias_index(root)
        with pytest.raises(NoteMigrationError, match="two strategy"):
            index.match("Example Break")

    def test_a_drafts_partial_aliases_count_too(self, make_vault, example_note):
        draft = render_note(
            "example-draft", "Example Draft", status="draft",
            def_yaml="trade_def:\n  aliases: [Draft Alias]\n"
                     "  valid_setups:\n    - {setup_ref: range_break, relation: with_trend}",
        )
        root = make_vault({"Example Range Break": example_note, "Example Draft": draft})
        assert build_alias_index(root).match("Draft Alias") == "example-draft"


# ---------------------------------------------------------------------
# the insert
# ---------------------------------------------------------------------


class TestInsert:
    FM = ["---", "date: x", "strategy: Something", "RVOL:", "---"]

    def test_exactly_one_line_after_strategy(self):
        out, note = insert_trade_def_line(self.FM, "example-range-break")
        assert out.split("\n") == [
            "---", "date: x", "strategy: Something",
            "trade_def: example-range-break", "RVOL:", "---",
        ]
        assert "inserted" in note

    def test_an_unmatched_value_gets_an_empty_key(self):
        out, note = insert_trade_def_line(self.FM, None)
        assert "trade_def:\n" in out + "\n"
        assert "clause-2a" in note

    def test_strategy_is_left_verbatim(self):
        weird = ["---", 'strategy: \'"  Big Value"\'', "---"]
        out, _ = insert_trade_def_line(weird, "example-range-break")
        assert 'strategy: \'"  Big Value"\'' in out

    def test_no_strategy_line_is_refused(self):
        with pytest.raises(NoteMigrationError, match="no `strategy:` line"):
            insert_trade_def_line(["---", "date: x", "---"], "example-range-break")

    def test_only_the_first_strategy_line_is_used(self):
        out, _ = insert_trade_def_line(
            ["---", "strategy: a", "strategy: b", "---"], "example-range-break"
        )
        assert out.count("trade_def:") == 1


# ---------------------------------------------------------------------
# planning over a vault
# ---------------------------------------------------------------------


class TestPlan:
    def test_a_matching_value_gets_its_slug(self, vault):
        root, add = vault
        add({"T1": _trade_note(" Example Break")})
        run = plan_trade_notes(root)
        assert [(p.slug, p.action) for p in run.plans] == [
            ("example-range-break", "insert")
        ]

    def test_an_unmatched_value_is_planned_blank_and_tallied(self, vault):
        root, add = vault
        add({"T1": _trade_note(" Not A Trade")})
        run = plan_trade_notes(root)
        assert run.plans[0].slug is None
        assert run.tally["Not A Trade"] == (None, 1)

    def test_a_blank_value_is_planned_blank(self, vault):
        root, add = vault
        add({"T1": _trade_note("")})
        run = plan_trade_notes(root)
        assert run.plans[0].slug is None
        assert run.tally["(blank)"] == (None, 1)

    def test_a_note_already_carrying_trade_def_is_skipped(self, vault):
        root, add = vault
        add({"T1": _trade_note(" Example Break", extra="trade_def: example-range-break\n")})
        run = plan_trade_notes(root)
        assert run.plans[0].action == "skip_has_trade_def"

    def test_a_note_with_no_strategy_key_is_reported_not_touched(self, vault):
        root, add = vault
        add({"T1": _trade_note(None)})
        run = plan_trade_notes(root)
        assert run.plans[0].action == "skip_no_strategy"
        assert any("no `strategy:` key" in p for p in run.problems)

    def test_a_note_with_no_frontmatter_is_reported(self, vault):
        root, add = vault
        add({"T1": "no frontmatter here\n"})
        run = plan_trade_notes(root)
        assert run.plans == []
        assert any("no frontmatter" in p for p in run.problems)

    def test_the_tally_counts_the_raw_value_and_names_its_slug(self, vault):
        root, add = vault
        add(
            {
                "T1": _trade_note(" Example Break"),
                "T2": _trade_note('"  Example Break"'),
                "T3": _trade_note(""),
            }
        )
        run = plan_trade_notes(root)
        assert run.tally["Example Break"] == ("example-range-break", 1)
        assert run.tally['"  Example Break"'] == ("example-range-break", 1)
        assert run.tally["(blank)"] == (None, 1)

    def test_only_the_named_note_is_planned(self, vault):
        root, add = vault
        add({"T1": _trade_note(" Example Break"), "T2": _trade_note("")})
        run = plan_trade_notes(root, only_note="T2.md")
        assert len(run.plans) == 1
        assert run.plans[0].path.name == "T2.md"

    def test_the_body_is_the_whole_frontmatter_and_nothing_else(self, vault):
        root, add = vault
        add({"T1": _trade_note(" Example Break")})
        body = plan_trade_notes(root).plans[0].body
        assert body.startswith("---") and body.rstrip().endswith("---")
        assert "body the command must not touch" not in body
