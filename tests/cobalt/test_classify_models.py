"""R1 — the neutral question schema (`cobalt.classify.models`).

Every case here is CONSTRUCTED: the three question types are the
vendor-neutral shape of the research (deep §2 rows 1–3), and no item
carries a real ticker (L32) or a number (the plan §2: states are WORDS).
"""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from cobalt.classify.models import (
    Answer,
    CallRecord,
    Choice,
    Noul,
    QuestionSet,
    Score,
    TrialItem,
    Usage,
)


def _choice(**over):
    base = dict(
        instructions="Which kind of item is this?",
        options={"a": "the first kind", "b": "the second kind", "unsure": "cannot tell"},
    )
    base.update(over)
    return Choice(**base)


def _set(**questions):
    return QuestionSet(id="T", version=1, questions=questions or {"q": _choice()})


class TestChoice:
    def test_a_choice_with_unsure_validates(self):
        assert _choice().type == "choice"

    def test_a_choice_without_unsure_is_refused(self):
        with pytest.raises(ValidationError, match="unsure"):
            _choice(options={"a": "one", "b": "two"})

    def test_a_choice_with_only_unsure_is_refused(self):
        with pytest.raises(ValidationError):
            _choice(options={"unsure": "cannot tell"})


class TestScore:
    def test_two_to_ten_levels_validate(self):
        assert len(Score(instructions="how much", levels=["low", "high"]).levels) == 2
        assert len(Score(instructions="how much", levels=[f"l{c}" for c in "abcdefghij"]).levels) == 10

    @pytest.mark.parametrize("n", [1, 11])
    def test_one_or_eleven_levels_are_refused(self, n):
        with pytest.raises(ValidationError):
            Score(instructions="how much", levels=[f"level {i}" for i in range(n)])

    def test_duplicate_levels_are_refused(self):
        with pytest.raises(ValidationError):
            Score(instructions="how much", levels=["low", "low"])


class TestNoul:
    def test_descriptions_are_optional(self):
        assert Noul(instructions="this is new").true is None
        assert Noul(instructions="this is new", true="yes it is", false="no").false == "no"


class TestTrialItem:
    def test_a_string_state_validates(self):
        assert TrialItem(id="x", state="XYZ Co. announces a contract", provenance="constructed")

    def test_a_word_dict_state_validates(self):
        item = TrialItem(id="x", state={"trend": "up", "strength": "high"}, provenance="constructed")
        assert item.state["trend"] == "up"

    @pytest.mark.parametrize("value", [3, 2.5, "3", "-0.25", "1e3", " 12 "])
    def test_a_numeric_value_in_a_dict_state_is_refused(self, value):
        with pytest.raises(ValidationError, match="(?i)numer"):
            TrialItem(id="x", state={"trend": value}, provenance="constructed")

    def test_provenance_is_constructed_or_real_path(self):
        assert TrialItem(id="x", state="s", provenance="real:docs/a.md")
        with pytest.raises(ValidationError):
            TrialItem(id="x", state="s", provenance="invented")


class TestQuestionSetHash:
    def test_the_hash_is_stable(self):
        assert _set().sha256 == _set().sha256
        assert len(_set().sha256) == 64

    def test_one_character_in_one_option_changes_the_hash(self):
        a = _set(q=_choice())
        b = _set(q=_choice(options={"a": "the first kinD", "b": "the second kind", "unsure": "cannot tell"}))
        assert a.sha256 != b.sha256

    def test_question_order_changes_the_hash(self):
        one = Noul(instructions="one")
        two = Noul(instructions="two")
        assert _set(a=one, b=two).sha256 != _set(b=two, a=one).sha256

    def test_first_n_and_reversed(self):
        qs = _set(a=Noul(instructions="a"), b=Noul(instructions="b"), c=Noul(instructions="c"))
        assert list(qs.first(2).questions) == ["a", "b"]
        assert list(qs.reversed().questions) == ["c", "b", "a"]
        with pytest.raises(ValueError, match="3"):
            qs.first(4)

    def test_a_set_with_no_question_is_refused(self):
        with pytest.raises(ValidationError):
            QuestionSet(id="T", version=1, questions={})


class TestRecords:
    def test_an_absent_confidence_is_none_not_a_default(self):
        a = Answer(question_id="q", value="a", source="absent")
        assert a.probabilities is None and a.confidence is None

    def test_a_call_record_validates(self):
        rec = CallRecord(
            set_id="FLOOR", set_sha256="0" * 64, item_id="f1", provenance="constructed",
            request={"model": "m"}, raw_response={"id": "gen-x"},
            answers=[Answer(question_id="q", value=True, source="absent")],
            latency_ms=1.0, http_ms=0.5, status="ok", http_status=200,
            usage=Usage(input_tokens=1, output_tokens=1), cost_usd=0.0,
            cost_source="returned", model_returned="m", provider_returned=None,
        )
        assert rec.door == "openrouter"
        assert rec.at.tzinfo is not None
