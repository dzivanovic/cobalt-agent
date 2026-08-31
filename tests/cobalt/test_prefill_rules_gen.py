"""Rules generator tests: Rules.md is the source of truth, rules.yaml is
a GENERATED artifact — tag contract, fail-loud naming the exact line,
mantra parsing, and the regenerate-and-write round trip."""

import pytest

from cobalt.prefill import rules_gen as rules_gen_module
from cobalt.prefill.rules_gen import (
    RulesSourceError,
    _parse_rules_md,
    _split_trailing_tags,
    regenerate_rules_config,
)

GOOD_RULES_MD = """
**THE 12 RULES**

1. Card first: grade risk shares. #process
2. Grades: B = $30, A = $70. #sizing

**Tape check:** *In because criteria met — or because it excites me?*
**Identity:** *My sizing is arithmetic, not habit.*
"""


class TestSplitTrailingTags:
    def test_single_trailing_tag(self):
        assert _split_trailing_tags("some text #process") == ("some text", ["process"])

    def test_no_tag(self):
        assert _split_trailing_tags("some text") == ("some text", [])

    def test_multiple_trailing_tags(self):
        assert _split_trailing_tags("some text #process #sizing") == ("some text", ["process", "sizing"])

    def test_midline_hash_not_treated_as_trailing(self):
        # "#2" here is not at the end of the line -- must not be mistaken
        # for the trailing tag.
        assert _split_trailing_tags("Re-entry #2 same thesis #re_entry") == (
            "Re-entry #2 same thesis",
            ["re_entry"],
        )


class TestParseRulesMd:
    def test_parses_rules_and_mantras(self):
        rules, mantras = _parse_rules_md(GOOD_RULES_MD)
        assert len(rules) == 2
        assert rules[0].id == "rule_01"
        assert rules[0].category == "process"
        assert rules[0].text == "Card first: grade risk shares."
        assert rules[1].category == "sizing"
        assert len(mantras) == 2
        assert mantras[0].id == "tape_check"
        assert mantras[1].id == "identity"

    def test_missing_tag_fails_loud_naming_the_line(self):
        bad = "1. Card first: grade risk shares.\n"
        with pytest.raises(RulesSourceError, match="line 1.*rule #1.*found none"):
            _parse_rules_md(bad)

    def test_unrecognized_tag_fails_loud(self):
        bad = "1. Card first: grade risk shares. #bogus\n"
        with pytest.raises(RulesSourceError, match="#bogus.*not one of"):
            _parse_rules_md(bad)

    def test_multiple_tags_fails_loud(self):
        bad = "1. Card first: grade risk shares. #process #sizing\n"
        with pytest.raises(RulesSourceError, match="found \\['process', 'sizing'\\]"):
            _parse_rules_md(bad)

    def test_no_rule_lines_at_all_fails_loud(self):
        with pytest.raises(RulesSourceError, match="no numbered rule lines"):
            _parse_rules_md("just some prose, no rules here\n")

    def test_empty_text_after_stripping_tag_fails_loud(self):
        bad = "1. #process\n"
        with pytest.raises(RulesSourceError, match="empty rule text"):
            _parse_rules_md(bad)


class TestRegenerateRulesConfig:
    def test_writes_generated_yaml_with_hash_and_source(self, monkeypatch, tmp_path):
        vault_root = tmp_path / "vault"
        rules_dir = vault_root / "1 - Trading" / "5 - Review"
        rules_dir.mkdir(parents=True)
        rules_md = rules_dir / "Rules.md"
        rules_md.write_text(GOOD_RULES_MD)

        out_path = tmp_path / "rules.yaml"
        monkeypatch.setattr(rules_gen_module, "resolve_vault_path", lambda: vault_root)
        monkeypatch.setattr(rules_gen_module, "RULES_CONFIG_PATH", out_path)

        cfg = regenerate_rules_config()
        assert len(cfg.rules) == 2
        assert cfg.generated.source == str(rules_md)
        assert len(cfg.generated.source_sha256) == 64

        written = out_path.read_text()
        assert "GENERATED — do not hand-edit" in written
        assert cfg.generated.source_sha256 in written

    def test_missing_rules_md_fails_loud(self, monkeypatch, tmp_path):
        vault_root = tmp_path / "vault"
        vault_root.mkdir()
        monkeypatch.setattr(rules_gen_module, "resolve_vault_path", lambda: vault_root)
        monkeypatch.setattr(rules_gen_module, "RULES_CONFIG_PATH", tmp_path / "rules.yaml")
        with pytest.raises(RulesSourceError, match="Rules.md not found"):
            regenerate_rules_config()

    def test_regenerated_file_round_trips_through_load_rules_config(self, monkeypatch, tmp_path):
        from cobalt.prefill.config import load_rules_config

        vault_root = tmp_path / "vault"
        rules_dir = vault_root / "1 - Trading" / "5 - Review"
        rules_dir.mkdir(parents=True)
        (rules_dir / "Rules.md").write_text(GOOD_RULES_MD)

        out_path = tmp_path / "rules.yaml"
        monkeypatch.setattr(rules_gen_module, "resolve_vault_path", lambda: vault_root)
        monkeypatch.setattr(rules_gen_module, "RULES_CONFIG_PATH", out_path)
        monkeypatch.setattr("cobalt.prefill.config.RULES_CONFIG_PATH", out_path)

        regenerate_rules_config()
        reloaded = load_rules_config()
        assert len(reloaded.rules) == 2
        assert reloaded.generated.source_sha256
