"""The one-off strategy-note migration (ADR-0008 D3 rulings a, b, d, e).

Every fixture here is SYNTHETIC. The command's real inputs are Dejan's 22
strategy notes and the two config families that were deleted with them —
all user data (L32), none of it in this repo. What is testable without
any of that is the part that matters: the textual editors are exact, the
drift check actually fires, and the tunables lift moves rows without
losing a comment or inventing a home for one.

The editors are TEXTUAL on purpose and the tests are written to hold them
to it: a re-serialisation through `yaml.safe_dump` would reorder keys,
drop every comment a human wrote next to a rule and re-flow every block,
so "every line the rules do not name is byte-identical" is the property
under test, not an implementation detail.
"""

from __future__ import annotations

import pytest

from cobalt.taxonomy.note_migration import (
    NoteMigrationError,
    assert_alias_move,
    canonical_md5,
    draft_unit_body,
    edit_definition_unit,
    edit_frontmatter,
    lift_per_trade_rows,
    migrate_strategy_template,
    tunables_unit_body,
)

UNIT = """```yaml
# A human's comment about where this came from.
trade_def:
  id: example_old_id
  name: Example Old Name
  aliases: [Ex]
  family: [range_break]
  class: scalp
  quality_factors:
    - plain_factor
    - measured_factor  # a trailing comment a human left
    - setup_relation
  reference_stats: {win_rate: "55%"}
```"""

REGISTRY = {
    "plain_factor": {},                                        # all defaults
    "measured_factor": {"source": "cobalt", "tier": "deterministic"},
    "setup_relation": {},
}


# ---------------------------------------------------------------------
# the definition unit (rulings a, e, b.2)
# ---------------------------------------------------------------------


class TestEditDefinitionUnit:
    def test_id_and_name_are_dropped(self):
        out, notes = edit_definition_unit(UNIT, fm_name="Example New Name", registry=REGISTRY)
        assert "  id:" not in out
        assert "\n  name:" not in out
        assert any("ruling a" in n for n in notes)

    def test_a_differing_yaml_name_joins_aliases(self):
        out, _ = edit_definition_unit(UNIT, fm_name="Example New Name", registry=REGISTRY)
        assert "  aliases: [Ex, Example Old Name]" in out

    def test_a_matching_yaml_name_does_not(self):
        out, _ = edit_definition_unit(UNIT, fm_name="Example Old Name", registry=REGISTRY)
        assert "  aliases: [Ex]" in out

    def test_a_name_with_a_comma_is_quoted(self):
        unit = UNIT.replace("name: Example Old Name", "name: Example, Old Name")
        out, _ = edit_definition_unit(unit, fm_name="New", registry=REGISTRY)
        assert '  aliases: [Ex, "Example, Old Name"]' in out

    def test_aliases_is_created_when_absent(self):
        unit = UNIT.replace("  aliases: [Ex]\n", "")
        out, notes = edit_definition_unit(unit, fm_name="New", registry=REGISTRY)
        assert "  aliases: [Example Old Name]" in out
        assert any("added aliases" in n for n in notes)

    def test_a_default_factor_stays_a_bare_string(self):
        out, _ = edit_definition_unit(UNIT, fm_name="New", registry=REGISTRY)
        assert "    - plain_factor\n" in out
        assert "    - setup_relation\n" in out

    def test_a_non_default_factor_becomes_a_mapping_and_keeps_its_comment(self):
        out, _ = edit_definition_unit(UNIT, fm_name="New", registry=REGISTRY)
        assert (
            "    - {name: measured_factor, source: cobalt, tier: deterministic}"
            "  # a trailing comment a human left" in out
        )

    def test_every_other_byte_is_untouched(self):
        out, _ = edit_definition_unit(UNIT, fm_name="Example Old Name", registry={})
        before = [
            line for line in UNIT.split("\n")
            if not line.startswith(("  id:", "  name:"))
        ]
        assert out.split("\n") == before

    def test_the_human_comment_survives(self):
        out, _ = edit_definition_unit(UNIT, fm_name="New", registry=REGISTRY)
        assert "# A human's comment about where this came from." in out

    def test_a_unit_with_no_fence_is_refused(self):
        with pytest.raises(NoteMigrationError, match="no fenced YAML"):
            edit_definition_unit("just prose", fm_name="N", registry={})

    def test_a_multiline_aliases_block_is_refused_rather_than_mangled(self):
        unit = UNIT.replace("  aliases: [Ex]", "  aliases:\n    - Ex")
        with pytest.raises(NoteMigrationError, match="one-line flow sequence"):
            edit_definition_unit(unit, fm_name="New", registry=REGISTRY)


# ---------------------------------------------------------------------
# the drift check
# ---------------------------------------------------------------------


class TestDriftCheck:
    def test_dropping_id_and_name_does_not_change_the_canonical_md5(self):
        before = {"id": "x", "name": "N", "family": ["range_break"]}
        after = {"family": ["range_break"]}
        assert canonical_md5(before) == canonical_md5(after)

    def test_quality_factors_are_compared_by_name(self):
        before = {"quality_factors": ["a", "b"]}
        after = {"quality_factors": [{"name": "a", "source": "cobalt"}, "b"]}
        assert canonical_md5(before) == canonical_md5(after)

    def test_a_real_change_does_change_it(self):
        assert canonical_md5({"max_attempts": 1}) != canonical_md5({"max_attempts": 2})

    def test_aliases_are_hashed_unless_dropped(self):
        a, b = {"aliases": ["x"]}, {"aliases": ["x", "y"]}
        assert canonical_md5(a) != canonical_md5(b)
        assert canonical_md5(a, drop_aliases=True) == canonical_md5(b, drop_aliases=True)

    def test_the_alias_move_is_asserted_exactly(self):
        before = {"aliases": ["Ex"], "name": "Old"}
        assert_alias_move(
            before, {"aliases": ["Ex", "Old"]}, yaml_name="Old", fm_name="New"
        )
        with pytest.raises(NoteMigrationError, match="aliases\\[\\] moved wrongly"):
            assert_alias_move(
                before, {"aliases": ["Ex", "Something Else"]},
                yaml_name="Old", fm_name="New",
            )

    def test_an_unchanged_name_must_not_gain_an_alias(self):
        with pytest.raises(NoteMigrationError):
            assert_alias_move(
                {"aliases": ["Ex"]}, {"aliases": ["Ex", "Same"]},
                yaml_name="Same", fm_name="Same",
            )


# ---------------------------------------------------------------------
# the frontmatter (ruling d)
# ---------------------------------------------------------------------


FM = [
    "---",
    "trade_def: example-range-break",
    "name: Example Range Break",
    "category:",
    "sides: [long, short]",
    "status: defined",
    "---",
]


class TestEditFrontmatter:
    def test_class_and_family_go_in_after_name(self):
        out, notes = edit_frontmatter(FM, trade_class="scalp", families=["range_break"])
        assert out.split("\n")[:5] == [
            "---",
            "trade_def: example-range-break",
            "name: Example Range Break",
            "class: scalp",
            "family: [range_break]",
        ]
        assert any("removed blank `category:`" in n for n in notes)

    def test_a_draft_gets_empty_values(self):
        out, _ = edit_frontmatter(FM, trade_class=None, families=[])
        assert "class:\n" in out + "\n"
        assert "family: []" in out

    def test_a_non_blank_category_is_refused(self):
        bad = [line if line != "category:" else "category: momentum" for line in FM]
        with pytest.raises(NoteMigrationError, match="not blank"):
            edit_frontmatter(bad, trade_class="scalp", families=[])

    def test_every_other_line_is_byte_identical(self):
        out, _ = edit_frontmatter(FM, trade_class="scalp", families=["range_break"])
        lines = out.split("\n")
        for original in FM:
            if original == "category:":
                continue
            assert original in lines

    def test_a_second_run_updates_rather_than_duplicates(self):
        once, _ = edit_frontmatter(FM, trade_class="scalp", families=["range_break"])
        twice, notes = edit_frontmatter(
            once.split("\n"), trade_class="scalp", families=["range_break"]
        )
        assert twice == once
        assert any("updated existing" in n for n in notes)

    def test_it_reports_when_there_was_no_category(self):
        without = [line for line in FM if line != "category:"]
        _out, notes = edit_frontmatter(without, trade_class="scalp", families=[])
        assert any("no `category:`" in n for n in notes)


# ---------------------------------------------------------------------
# the tunables lift (ruling b.3 / a)
# ---------------------------------------------------------------------


TUNABLES = """# header of the file
tunables:
  - key: global.thing
    value: 1
    unit: count
    scope: global
    dynamic: false
    status: proposed
    source: ruling

  # --- per_trade: a grouping header that belongs to the FILE ------------
  # this comment belongs to the row under it
  - key: example_a.band
    value: [1, 2]
    unit: min
    scope: per_trade(example_a)
    dynamic: true
    status: proposed
    source: sheet

  - key: example_old.thing
    value: 3
    unit: count
    scope: per_trade(example_old)
    dynamic: false
    status: proposed
    source: ruling

  - key: another.global
    value: 9
    unit: count
    scope: global
    dynamic: false
    status: proposed
    source: ruling
"""


class TestLiftPerTradeRows:
    def _lift(self):
        return lift_per_trade_rows(
            TUNABLES, slug_by_key={"example_a": "example-a", "example_old": "example-new"}
        )

    def test_only_per_trade_rows_are_lifted(self):
        lift = self._lift()
        assert set(lift.blocks) == {"example-a", "example-new"}
        assert "global.thing" in lift.remaining_text
        assert "another.global" in lift.remaining_text
        assert "example_a.band" not in lift.remaining_text

    def test_a_rows_own_comment_travels_with_it(self):
        block = "\n".join(self._lift().blocks["example-a"])
        assert "# this comment belongs to the row under it" in block

    def test_a_group_header_stays_in_the_file(self):
        lift = self._lift()
        assert "grouping header that belongs to the FILE" in lift.remaining_text
        assert all(
            "grouping header" not in "\n".join(b) for b in lift.blocks.values()
        )

    def test_a_key_whose_slug_differs_is_rekeyed(self):
        lift = self._lift()
        block = "\n".join(lift.blocks["example-new"])
        assert "key: example_new.thing" in block
        assert "scope: per_trade(example_new)" in block
        assert any("example_old" in r for r in lift.rekeyed)

    def test_a_row_with_no_note_fails_loud(self):
        with pytest.raises(NoteMigrationError, match="no strategy note claims"):
            lift_per_trade_rows(TUNABLES, slug_by_key={})

    def test_the_remaining_file_still_parses(self):
        import yaml

        rows = yaml.safe_load(self._lift().remaining_text)["tunables"]
        assert [r["key"] for r in rows] == ["global.thing", "another.global"]


class TestUnitBodies:
    def test_a_draft_body_carries_its_matrix_rows_and_says_it_is_partial(self):
        body = draft_unit_body(
            [{"setup_ref": "range_break", "relation": "with_trend"}]
        )
        assert "# partial — draft" in body
        assert "  valid_setups:" in body
        assert "    - {setup_ref: range_break, relation: with_trend}" in body
        import yaml

        parsed = yaml.safe_load(body.split("```")[1].removeprefix("yaml\n"))
        assert parsed["trade_def"]["valid_setups"][0]["setup_ref"] == "range_break"

    def test_a_tunables_body_says_why_it_is_its_own_unit(self):
        body = tunables_unit_body("example-a", ["  - key: example_a.x"])
        assert "tunables:" in body
        assert "replay writes a" in body
        assert "  - key: example_a.x" in body


# ---------------------------------------------------------------------
# the template (human-tree file, plain edit)
# ---------------------------------------------------------------------


class TestStrategyTemplate:
    def _vault(self, tmp_path, text):
        (tmp_path / "5 - Templates").mkdir(parents=True)
        (tmp_path / "5 - Templates" / "Strategy.md").write_text(text)
        return tmp_path

    TEMPLATE = "---\ntrade_def: example-x\nname: Example X\ncategory:\nstatus: draft\n---\n"

    def test_dry_run_writes_nothing(self, tmp_path):
        root = self._vault(tmp_path, self.TEMPLATE)
        _path, diff = migrate_strategy_template(root, dry_run=True)
        assert "-category:" in diff and "+class:" in diff
        assert (root / "5 - Templates" / "Strategy.md").read_text() == self.TEMPLATE

    def test_apply_replaces_category(self, tmp_path):
        root = self._vault(tmp_path, self.TEMPLATE)
        migrate_strategy_template(root, dry_run=False)
        text = (root / "5 - Templates" / "Strategy.md").read_text()
        assert "category:" not in text
        assert "class:\nfamily: []\n" in text

    def test_a_second_run_is_a_no_op(self, tmp_path):
        root = self._vault(tmp_path, self.TEMPLATE)
        migrate_strategy_template(root, dry_run=False)
        _path, diff = migrate_strategy_template(root, dry_run=False)
        assert "already migrated" in diff

    def test_a_non_blank_category_is_refused(self, tmp_path):
        root = self._vault(tmp_path, self.TEMPLATE.replace("category:", "category: mine"))
        with pytest.raises(NoteMigrationError, match="not blank"):
            migrate_strategy_template(root, dry_run=True)

    def test_a_vault_without_the_template_is_not_an_error(self, tmp_path):
        path, message = migrate_strategy_template(tmp_path, dry_run=True)
        assert path is None and "nothing to do" in message


# ---------------------------------------------------------------------
# ruled pairings arrive as ARGUMENTS (R1)
# ---------------------------------------------------------------------


class TestKeyAliases:
    def test_matrix_aliases_invert_to_slug_keyed(self):
        from cobalt.taxonomy.note_migration import parse_matrix_aliases

        assert parse_matrix_aliases(["example_old=example-new"]) == {
            "example-new": "example_old"
        }

    def test_a_note_may_take_only_one_matrix_row(self):
        from cobalt.taxonomy.note_migration import parse_matrix_aliases

        with pytest.raises(NoteMigrationError, match="twice"):
            parse_matrix_aliases(["example_a=example-n", "example_b=example-n"])

    def test_a_malformed_pair_is_refused(self):
        from cobalt.taxonomy.note_migration import parse_key_aliases

        for bad in ("no-equals", "=example-n", "example_a="):
            with pytest.raises(NoteMigrationError):
                parse_key_aliases([bad], flag="matrix-alias")

    def test_tunable_aliases_stay_key_keyed(self):
        from cobalt.taxonomy.note_migration import parse_key_aliases

        assert parse_key_aliases(["example_old=example-new"], flag="tunable-alias") == {
            "example_old": "example-new"
        }

    def test_none_is_an_empty_map(self):
        from cobalt.taxonomy.note_migration import parse_key_aliases

        assert parse_key_aliases(None, flag="x") == {}


def test_the_rekey_covers_the_whole_row_including_consumers():
    """A row whose key says one trade and whose consumer list says another
    is a row nobody can grep — the re-key is whole-word over the block."""
    text = (
        "tunables:\n"
        "  - key: example_old.thing\n"
        "    value: 1\n"
        "    unit: count\n"
        "    scope: per_trade(example_old)\n"
        "    dynamic: false\n"
        "    status: proposed\n"
        "    source: ruling\n"
        '    consumers: ["example_old"]\n'
    )
    lift = lift_per_trade_rows(text, slug_by_key={"example_old": "example-new"})
    block = "\n".join(lift.blocks["example-new"])
    assert "key: example_new.thing" in block
    assert "scope: per_trade(example_new)" in block
    assert 'consumers: ["example_new"]' in block
    assert "example_old" not in block
