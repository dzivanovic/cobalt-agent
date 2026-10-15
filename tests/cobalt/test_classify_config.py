"""R1 — `configs/cobalt/classify/trial.yaml` and its schema (L10).

The committed file is loaded for real (it IS the artifact); the refusals
are proven on constructed copies of it written to a tmp dir.
"""

from __future__ import annotations

import re

import pytest
import yaml

from cobalt.classify import config as cfg_mod
from cobalt.classify.config import (
    CONFIG_PATH,
    SET_NAMES,
    ClassifyConfigError,
    load_trial_config,
)


def _raw() -> dict:
    return yaml.safe_load(CONFIG_PATH.read_text())


def _write(tmp_path, raw) -> "Path":  # noqa: F821
    p = tmp_path / "trial.yaml"
    p.write_text(yaml.safe_dump(raw, sort_keys=False))
    return p


class TestTheCommittedFile:
    def test_it_loads(self):
        cfg = load_trial_config()
        assert set(cfg.sets) == set(SET_NAMES)

    def test_the_model_id_and_cap_are_his_rulings(self):
        cfg = load_trial_config()
        assert cfg.model_id == "typesafe/jev-1.13"
        assert cfg.model_id_source.startswith("ruling:")
        assert cfg.spend_cap_usd == 5
        assert cfg.spend_cap_source.startswith("ruling:")
        assert cfg.call_ceiling == 1100

    def test_the_file_sits_outside_the_old_loaders_glob(self):
        # CLAUDE.md config boundary: the old loader globs configs/*.yaml,
        # top level only.
        assert CONFIG_PATH.parent.name == "classify"
        assert CONFIG_PATH.parent.parent.name == "cobalt"

    @pytest.mark.parametrize(
        "name,questions,items",
        [("FLOOR", 1, 3), ("S1", 4, 50), ("S2", 3, 40), ("S3", 3, 60), ("L20", 20, 40)],
    )
    def test_each_set_has_the_plans_shape(self, name, questions, items):
        qset, its = load_trial_config().resolve(name)
        assert len(qset.questions) == questions
        assert len(its) == items
        assert len({i.id for i in its}) == len(its)

    def test_t9_reads_the_day_open_reports_at_run_time(self):
        cfg = load_trial_config()
        qset, items = cfg.resolve("T9")
        assert len(qset.questions) == 5
        assert items, "T9 found no day-open report — L1: never an empty set"
        assert all(i.provenance.startswith("real:docs/40 - DevDocs/reports/day-open-") for i in items)

    def test_every_choice_carries_unsure_and_no_real_state_carries_a_number(self):
        cfg = load_trial_config()
        for name in ("FLOOR", "S1", "S2", "S3", "L20"):
            qset, items = cfg.resolve(name)
            for q in qset.questions.values():
                if q.type == "choice":
                    assert "unsure" in q.options
            for it in items:
                text = it.state if isinstance(it.state, str) else " ".join(it.state.values())
                assert not re.search(r"\d", text), f"{name}/{it.id} carries a digit"

    def test_l20_is_s1_s2_s3_then_ten_gates(self):
        cfg = load_trial_config()
        l20, _ = cfg.resolve("L20")
        head = [*cfg.resolve("S1")[0].questions, *cfg.resolve("S2")[0].questions,
                *cfg.resolve("S3")[0].questions]
        assert list(l20.questions)[: len(head)] == head
        assert len(l20.questions) - len(head) == 10

    def test_floor_padding_states_are_about_the_plans_sizes(self):
        _, items = load_trial_config().resolve("FLOOR")
        sizes = sorted(len(i.state) // 4 for i in items)   # chars / 4 ≈ tokens
        assert sizes[0] < 60
        assert 250 <= sizes[1] <= 350
        assert 1400 <= sizes[2] <= 1600

    @pytest.mark.parametrize("name", ["FLOOR", "S1", "S2", "S3", "T9", "L20"])
    def test_each_sets_hash_is_stable_across_two_loads(self, name):
        a = load_trial_config().resolve(name)[0].sha256
        b = load_trial_config().resolve(name)[0].sha256
        assert a == b

    def test_one_character_in_one_option_changes_the_sets_hash(self, tmp_path):
        before = load_trial_config().resolve("S1")[0].sha256
        raw = _raw()
        opts = raw["classify"]["sets"]["S1"]["questions"]["relevance"]["options"]
        opts["unsure"] = opts["unsure"] + "."
        after = load_trial_config(_write(tmp_path, raw)).resolve("S1")[0].sha256
        assert before != after

    def test_an_unknown_set_name_is_refused(self):
        with pytest.raises(ClassifyConfigError, match="S9"):
            load_trial_config().resolve("S9")


class TestRefusals:
    def test_a_non_openrouter_host_is_refused(self, tmp_path):
        raw = _raw()
        raw["classify"]["door_url"] = "https://example.com/api/v1/systemone"
        with pytest.raises(ClassifyConfigError, match="openrouter.ai"):
            load_trial_config(_write(tmp_path, raw))

    def test_a_plain_http_openrouter_url_is_refused(self, tmp_path):
        raw = _raw()
        raw["classify"]["models_url"] = "http://openrouter.ai/api/v1/models"
        with pytest.raises(ClassifyConfigError):
            load_trial_config(_write(tmp_path, raw))

    def test_a_results_dir_outside_scratch_is_refused(self, tmp_path):
        raw = _raw()
        raw["classify"]["results_dir"] = "docs"
        with pytest.raises(ClassifyConfigError, match="scratch"):
            load_trial_config(_write(tmp_path, raw))

    def test_a_results_dir_escaping_scratch_is_refused(self, tmp_path):
        raw = _raw()
        raw["classify"]["results_dir"] = "scratch/../src"
        with pytest.raises(ClassifyConfigError, match="scratch"):
            load_trial_config(_write(tmp_path, raw))

    @pytest.mark.parametrize("key", ["spend_cap_source", "model_id_source"])
    def test_a_source_that_is_not_a_ruling_is_refused(self, tmp_path, key):
        raw = _raw()
        raw["classify"][key] = "assumed"
        with pytest.raises(ClassifyConfigError, match="ruling:"):
            load_trial_config(_write(tmp_path, raw))

    def test_an_unknown_key_is_refused(self, tmp_path):
        raw = _raw()
        raw["classify"]["temperature"] = 0
        with pytest.raises(ClassifyConfigError):
            load_trial_config(_write(tmp_path, raw))

    def test_a_missing_file_crashes(self, tmp_path):
        with pytest.raises(ClassifyConfigError, match="not found"):
            load_trial_config(tmp_path / "absent.yaml")

    def test_a_bad_yaml_crashes_with_its_line(self, tmp_path):
        p = tmp_path / "trial.yaml"
        p.write_text("classify:\n  models_url: [unclosed\n")
        with pytest.raises(ClassifyConfigError, match="line"):
            load_trial_config(p)

    def test_a_choice_without_unsure_in_the_file_is_refused(self, tmp_path):
        raw = _raw()
        del raw["classify"]["sets"]["S1"]["questions"]["relevance"]["options"]["unsure"]
        with pytest.raises(ClassifyConfigError, match="unsure"):
            load_trial_config(_write(tmp_path, raw))

    def test_results_dir_is_resolved_against_the_repo_root(self, tmp_path, monkeypatch):
        monkeypatch.setattr(cfg_mod, "REPO_ROOT", tmp_path)
        cfg = load_trial_config()
        assert cfg.results_path() == (tmp_path / "scratch").resolve()
