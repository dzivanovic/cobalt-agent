"""The vault-backed trade_def loader (ADR-0008 D3).

The corpus these tests build is the SHAPE of the real one — 22 notes, a
minority of them finished defs and the rest drafts — assembled from the
repo's synthetic example. It is not the real corpus and must never be:
the 22 strategy notes in Dejan's vault are his trades, and a test fixture
in this repo is the last place they belong (L32).

What each block proves:

* the happy path, on the note the repo actually ships;
* DRAFTS are listed, not raised — an empty unit, an absent `trade_def:`
  mapping, and a partial one (the `valid_setups`-only shape the 9 draft
  notes carry) are all "not finished yet", not "broken";
* a finished def that does not validate IS an error, named by note;
* the identity rules: an authored `id:`, a bad slug, a missing `name:`,
  two notes claiming one slug;
* `status: playbook` is refused (R3 — earned at n >= 30, never typed);
* frontmatter that disagrees with the def produces a WARNING and the
  human wins;
* the per-trade tunables unit: right scope accepted, wrong scope refused,
  an engine-key collision refused.
"""

from __future__ import annotations

import pytest

from cobalt.taxonomy.vault_loader import (
    REQUIRED_UNIT_FIELDS,
    VaultTaxonomyError,
    load_vault_trade_defs,
)

from taxonomy_example import (
    EXAMPLE_NAME,
    EXAMPLE_SLUG,
    example_def_mapping,
    example_def_yaml,
    example_tunables_yaml,
    finished_note,
    render_note,
)

#: The `valid_setups`-only shape the 9 real draft notes will carry once
#: their grid rows move into them (ADR-0008 D3 b.1).
PARTIAL_DEF_YAML = (
    "trade_def:\n"
    "  valid_setups:\n"
    "    - {setup_ref: range_break, relation: with_trend}\n"
)


_finished = finished_note


# ---------------------------------------------------------------------
# The shipped example
# ---------------------------------------------------------------------


class TestTheShippedExample:
    def test_it_loads(self, example_vault):
        result = load_vault_trade_defs(example_vault)
        assert [d.slug for d in result.defs] == [EXAMPLE_SLUG]
        assert result.defs[0].name == EXAMPLE_NAME
        assert result.drafts == []
        assert result.warnings == []

    def test_it_records_where_it_came_from(self, example_vault):
        loaded = load_vault_trade_defs(example_vault).defs[0]
        assert loaded.note_path.endswith(f"{EXAMPLE_NAME}.md")
        assert loaded.note_path.startswith("1 - Trading/4 - Strategies/")
        assert len(loaded.md5) == 32

    def test_the_md5_tracks_the_unit_text(self, make_vault, example_note):
        first = load_vault_trade_defs(make_vault({EXAMPLE_NAME: example_note}))
        edited = example_note.replace("max_attempts: {value: 2", "max_attempts: {value: 3")
        assert edited != example_note
        second = load_vault_trade_defs(make_vault({EXAMPLE_NAME: edited}))
        assert first.defs[0].md5 != second.defs[0].md5

    def test_it_carries_its_own_tunables_unit(self, example_vault):
        rows = load_vault_trade_defs(example_vault).user_tunables
        assert [t.key for t in rows] == ["example_range_break.range_duration_band"]
        assert rows[0].row.scope == "per_trade(example_range_break)"
        assert rows[0].slug == EXAMPLE_SLUG

    def test_the_by_slug_and_tunable_row_views(self, example_vault):
        result = load_vault_trade_defs(example_vault)
        assert set(result.by_slug) == {EXAMPLE_SLUG}
        assert set(result.tunable_rows) == {"example_range_break.range_duration_band"}


# ---------------------------------------------------------------------
# A 22-note corpus, the shape of the real one
# ---------------------------------------------------------------------


@pytest.fixture
def corpus(make_vault):
    """13 finished defs + 9 drafts — the real corpus's proportions."""
    notes = {}
    for i in range(13):
        slug = f"example-def-{i:02d}"
        notes[f"Example Def {i:02d}"] = _finished(slug, f"Example Def {i:02d}")
    for i in range(9):
        slug = f"example-draft-{i:02d}"
        body = PARTIAL_DEF_YAML if i % 2 else None
        notes[f"Example Draft {i:02d}"] = render_note(
            slug, f"Example Draft {i:02d}", def_yaml=body, status="draft"
        )
    assert len(notes) == 22
    return make_vault(notes)


class TestCorpus:
    def test_thirteen_defs_nine_drafts(self, corpus):
        result = load_vault_trade_defs(corpus)
        assert len(result.defs) == 13
        assert len(result.drafts) == 9
        assert result.warnings == []

    def test_every_draft_says_why(self, corpus):
        for draft in load_vault_trade_defs(corpus).drafts:
            assert draft.reason
            assert draft.note_path.endswith(".md")
        reasons = {d.reason.split(" —")[0] for d in load_vault_trade_defs(corpus).drafts}
        assert reasons == {"Definition unit is empty", "partial definition"}

    def test_a_partial_definition_names_the_missing_fields(self, corpus):
        partial = [
            d for d in load_vault_trade_defs(corpus).drafts if "partial" in d.reason
        ]
        assert partial
        assert "trigger" in partial[0].reason and "stop" in partial[0].reason

    def test_required_unit_fields_come_from_the_model(self):
        """Not a hand-list: a new required TradeDef field joins it."""
        assert "id" not in REQUIRED_UNIT_FIELDS
        assert "name" not in REQUIRED_UNIT_FIELDS
        assert {"class", "trigger", "stop", "exit", "valid_setups"} <= REQUIRED_UNIT_FIELDS
        assert "aliases" not in REQUIRED_UNIT_FIELDS  # has a default


# ---------------------------------------------------------------------
# Identity — the rules ADR-0008 D3 rulings a and e put in one place
# ---------------------------------------------------------------------


class TestIdentity:
    def test_a_unit_that_authors_id_fails_loud(self, make_vault):
        vault = make_vault(
            {"N": render_note("example-n", "N", def_yaml=example_def_yaml(slug="example-n", id="n"))}
        )
        with pytest.raises(VaultTaxonomyError, match="id/name come from frontmatter"):
            load_vault_trade_defs(vault)

    def test_a_unit_that_authors_name_fails_loud(self, make_vault):
        vault = make_vault(
            {"N": render_note("example-n", "N", def_yaml=example_def_yaml(slug="example-n", name="Other"))}
        )
        with pytest.raises(VaultTaxonomyError, match="id/name come from frontmatter"):
            load_vault_trade_defs(vault)

    def test_a_bad_slug_fails_loud(self, make_vault):
        vault = make_vault({"N": render_note("Not A Slug", "N", def_yaml=example_def_yaml())})
        with pytest.raises(VaultTaxonomyError, match="invalid trade slug"):
            load_vault_trade_defs(vault)

    def test_a_missing_name_fails_loud(self, make_vault):
        note = finished_note("example-n", "N")
        vault = make_vault({"N": note.replace("name: N\n", "")})
        with pytest.raises(VaultTaxonomyError, match="`name:` is missing"):
            load_vault_trade_defs(vault)

    def test_two_notes_cannot_claim_one_slug(self, make_vault):
        vault = make_vault(
            {
                "First": _finished("example-same", "First"),
                "Second": _finished("example-same", "Second"),
            }
        )
        with pytest.raises(VaultTaxonomyError, match="duplicate trade_def slug"):
            load_vault_trade_defs(vault)

    def test_a_note_with_no_frontmatter_fails_loud(self, make_vault):
        vault = make_vault({"N": "## Definition\nnothing here\n"})
        with pytest.raises(VaultTaxonomyError, match="no frontmatter"):
            load_vault_trade_defs(vault)

    def test_the_unit_id_must_match_the_slug(self, make_vault):
        note = _finished("example-real", "N").replace(
            "trade_def:example-real", "trade_def:example-other"
        )
        vault = make_vault({"N": note})
        with pytest.raises(VaultTaxonomyError, match="has no unit"):
            load_vault_trade_defs(vault)

    def test_a_missing_definition_section_fails_loud(self, make_vault):
        note = _finished("example-n", "N").replace("cobalt:section definition", "cobalt:section other")
        vault = make_vault({"N": note})
        with pytest.raises(VaultTaxonomyError, match="no `definition` section"):
            load_vault_trade_defs(vault)


# ---------------------------------------------------------------------
# A finished def that does not validate is an ERROR, not a draft
# ---------------------------------------------------------------------


class TestFinishedButInvalid:
    def test_it_raises_and_names_the_note_and_the_field(self, make_vault):
        mapping = example_def_mapping()
        mapping["exit"][0]["fraction"] = 0.9  # sums to 1.4
        vault = make_vault(
            {
                "Broken": render_note(
                    "example-broken", "Broken",
                    def_yaml=example_def_yaml(slug="example-broken", **mapping),
                    tunables_yaml=example_tunables_yaml("example-broken"),
                )
            }
        )
        with pytest.raises(VaultTaxonomyError) as exc:
            load_vault_trade_defs(vault)
        message = str(exc.value)
        assert "Broken.md" in message
        assert "exit fractions sum to" in message

    def test_an_unknown_cfg_key_fails_loud(self, make_vault):
        mapping = example_def_mapping()
        mapping["avoid"] = [{"expr": "Range(micro).duration >= cfg(no.such.key) min"}]
        vault = make_vault(
            {
                "N": render_note(
                    "example-n", "N",
                    def_yaml=example_def_yaml(slug="example-n", **mapping),
                    tunables_yaml=example_tunables_yaml("example-n"),
                )
            }
        )
        with pytest.raises(VaultTaxonomyError, match="no.such.key"):
            load_vault_trade_defs(vault)

    def test_unparseable_yaml_fails_loud(self, make_vault):
        vault = make_vault({"N": render_note("example-n", "N", def_yaml="trade_def: [oops")})
        with pytest.raises(VaultTaxonomyError, match="does not parse"):
            load_vault_trade_defs(vault)


# ---------------------------------------------------------------------
# status: checked, never trusted
# ---------------------------------------------------------------------


class TestStatus:
    def test_playbook_is_refused(self, make_vault):
        vault = make_vault({"N": _finished("example-n", "N", status="playbook")})
        with pytest.raises(VaultTaxonomyError, match="EARNED at n >= 30"):
            load_vault_trade_defs(vault)

    def test_a_validated_unit_declared_draft_warns(self, make_vault):
        result = load_vault_trade_defs(make_vault({"N": _finished("example-n", "N", status="draft")}))
        assert len(result.defs) == 1
        assert any("status='draft'" in w and "validated" in w for w in result.warnings)

    def test_an_empty_unit_declared_defined_warns(self, make_vault):
        vault = make_vault({"N": render_note("example-n", "N", def_yaml=None, status="defined")})
        result = load_vault_trade_defs(vault)
        assert len(result.drafts) == 1
        assert any("did not validate" in w for w in result.warnings)

    def test_a_missing_status_warns(self, make_vault):
        result = load_vault_trade_defs(make_vault({"N": _finished("example-n", "N", status=None)}))
        assert any("status=None" in w for w in result.warnings)


# ---------------------------------------------------------------------
# class / family drift — a warning, and the human wins
# ---------------------------------------------------------------------


class TestFrontmatterAgreement:
    def test_a_class_mismatch_warns_and_still_loads(self, make_vault):
        vault = make_vault(
            {"N": _finished("example-n", "N", extra_frontmatter={"class": "move2move"})}
        )
        result = load_vault_trade_defs(vault)
        assert len(result.defs) == 1                       # the human wins
        assert result.defs[0].definition.trade_class.value == "scalp"
        assert any("frontmatter class='move2move'" in w for w in result.warnings)

    def test_a_family_mismatch_warns(self, make_vault):
        vault = make_vault(
            {"N": _finished("example-n", "N", extra_frontmatter={"family": ["reversion"]})}
        )
        result = load_vault_trade_defs(vault)
        assert any("frontmatter family=['reversion']" in w for w in result.warnings)

    def test_agreement_is_silent(self, make_vault):
        vault = make_vault(
            {
                "N": _finished(
                    "example-n", "N", extra_frontmatter={"class": "scalp", "family": ["range_break"]}
                )
            }
        )
        assert load_vault_trade_defs(vault).warnings == []

    def test_a_nonsense_class_warns_rather_than_raising(self, make_vault):
        vault = make_vault({"N": _finished("example-n", "N", extra_frontmatter={"class": "wat"})})
        result = load_vault_trade_defs(vault)
        assert len(result.defs) == 1
        assert any("is not a TradeClass" in w for w in result.warnings)


# ---------------------------------------------------------------------
# the per-trade tunables unit
# ---------------------------------------------------------------------


def _def_without_per_trade_cfg() -> str:
    """The example def with its per-trade `cfg()` precondition removed.

    These tests supply their OWN tunables rows, so the def must not also
    demand the example's — otherwise every one of them would be asserting
    two things at once.
    """
    mapping = example_def_mapping()
    mapping["preconditions"] = [
        p for p in mapping["preconditions"]
        if "example_range_break" not in str(p)
    ]
    return example_def_yaml(**mapping)


GOOD_ROW = (
    "tunables:\n"
    "  - key: example_n.band\n"
    "    value: 3\n"
    "    unit: min\n"
    "    scope: per_trade(example_n)\n"
    "    dynamic: true\n"
    "    status: proposed\n"
    "    source: ruling\n"
)


class TestTunablesUnit:
    def test_a_correctly_scoped_row_loads(self, make_vault):
        vault = make_vault(
            {"N": render_note("example-n", "N", def_yaml=_def_without_per_trade_cfg(), tunables_yaml=GOOD_ROW)}
        )
        rows = load_vault_trade_defs(vault).user_tunables
        assert [r.key for r in rows] == ["example_n.band"]

    def test_a_global_scope_row_is_refused(self, make_vault):
        vault = make_vault(
            {
                "N": render_note(
                    "example-n", "N",
                    def_yaml=_def_without_per_trade_cfg(),
                    tunables_yaml=GOOD_ROW.replace("per_trade(example_n)", "global"),
                )
            }
        )
        with pytest.raises(VaultTaxonomyError, match="expected 'per_trade\\(example_n\\)'"):
            load_vault_trade_defs(vault)

    def test_the_scope_uses_the_grammar_spelling_of_the_slug(self, make_vault):
        """kebab in the slug, underscore in the scope — `trade_key()`."""
        rows = GOOD_ROW.replace("example_n.band", "example_a_b.band").replace("per_trade(example_n)", "per_trade(example_a_b)")
        vault = make_vault(
            {"N": render_note("example-a-b", "N", def_yaml=_def_without_per_trade_cfg(), tunables_yaml=rows)}
        )
        assert load_vault_trade_defs(vault).user_tunables[0].row.scope == "per_trade(example_a_b)"

    def test_a_row_shadowing_an_engine_key_is_refused(self, make_vault):
        rows = GOOD_ROW.replace("example_n.band", "stop.buffer")
        vault = make_vault(
            {"N": render_note("example-n", "N", def_yaml=_def_without_per_trade_cfg(), tunables_yaml=rows)}
        )
        with pytest.raises(VaultTaxonomyError, match="shadow engine keys"):
            load_vault_trade_defs(vault)

    def test_a_draft_may_still_carry_tunables(self, make_vault):
        vault = make_vault(
            {"N": render_note("example-n", "N", def_yaml=None, status="draft", tunables_yaml=GOOD_ROW)}
        )
        result = load_vault_trade_defs(vault)
        assert result.drafts and [r.key for r in result.user_tunables] == ["example_n.band"]


# ---------------------------------------------------------------------
# the directory itself
# ---------------------------------------------------------------------


def test_a_missing_strategies_directory_fails_loud(tmp_path):
    with pytest.raises(VaultTaxonomyError, match="strategy notes directory not found"):
        load_vault_trade_defs(tmp_path)


def test_an_empty_strategies_directory_is_empty_not_broken(make_vault):
    result = load_vault_trade_defs(make_vault({}))
    assert result.defs == [] and result.drafts == []
