"""C6 — the resolver and the deterministic value parsers (FINAL §4, [F-10]).

Cards: candidates are the OPEN cards (code-rendered labels); the Plan's
spans are matched by code; exactly one → bound; zero or two-plus →
clarify reading the candidates back; never nearest, never earliest.
Values: deterministic parsers; unparseable → clarify, never a guess; the
price parser refuses clock shapes (`H:MM`) — X-X5 / X-X12.
All values constructed (L32).
"""

from __future__ import annotations

from decimal import Decimal

import pytest

from cobalt.voice import resolve as rv
from cobalt.voice.models import CandidateRef, Span

ROWS = [
    {"id": 11, "ticker": "XYZ", "direction": "long", "state": "WATCH", "stop": Decimal("4.40")},
    {"id": 12, "ticker": "QRS", "direction": "short", "state": "FILLED", "stop": Decimal("12.60")},
    {"id": 13, "ticker": "XYZ", "direction": "short", "state": "WATCH", "stop": Decimal("4.90")},
]


def cands(rows=ROWS):
    return rv.card_candidates(rows)


def test_candidates_carry_code_rendered_labels():
    c = cands()
    assert [x.id for x in c] == ["card-11", "card-12", "card-13"]
    assert c[0].label == "XYZ long WATCH (card 11)"


# --- cards -------------------------------------------------------------------


def test_a_unique_ticker_binds():
    r = rv.resolve_card({"card": Span(span="QRS")}, "move the stop on QRS to 12.25", cands())
    assert r.bound and r.card_id == 12


@pytest.mark.parametrize("span", ["X Y Z", "xyz", "X.Y.Z.", "XYZ"])
def test_spoken_letter_forms_normalize(span):
    r = rv.resolve_card({"card": Span(span=span)}, f"move the stop on {span} long to 4.50", cands())
    assert r.bound and r.card_id == 11  # "long" narrows the two XYZ cards


def test_two_matches_clarify_reading_the_candidates_back():
    r = rv.resolve_card({"card": Span(span="XYZ")}, "move the stop on XYZ to 4.50", cands())
    assert not r.bound and r.clarify
    assert "XYZ long WATCH (card 11)" in r.clarify and "XYZ short WATCH (card 13)" in r.clarify


def test_a_side_word_narrows():
    r = rv.resolve_card({"card": Span(span="XYZ")}, "move the stop on the XYZ short to 4.95", cands())
    assert r.bound and r.card_id == 13


def test_an_ordinal_narrows_by_card_order():
    r = rv.resolve_card({"card": Span(span="XYZ")}, "move the stop on the second XYZ card to 4.95", cands())
    assert r.bound and r.card_id == 13


def test_zero_matches_clarify():
    r = rv.resolve_card({"card": Span(span="LMN")}, "move the stop on LMN to 4.50", cands())
    assert not r.bound and "no open card" in r.clarify.lower()


def test_no_card_argument_clarifies_even_with_one_open_card():
    # the floating widget sends no card id; nothing is ever picked for him
    r = rv.resolve_card({}, "move the stop to 4.50", cands(ROWS[:1]))
    assert not r.bound and r.clarify


def test_a_candidate_ref_binds():
    r = rv.resolve_card({"card": CandidateRef(candidate="card-13")}, "move that stop", cands())
    assert r.bound and r.card_id == 13


def test_a_candidate_ref_off_the_list_does_not_bind():
    r = rv.resolve_card({"card": CandidateRef(candidate="card-99")}, "move that stop", cands())
    assert not r.bound


def test_no_open_cards_says_so():
    r = rv.resolve_card({"card": Span(span="XYZ")}, "move the stop on XYZ", [])
    assert not r.bound and "no open card" in r.clarify.lower()


# --- the price parser (X-X12) -----------------------------------------------------


@pytest.mark.parametrize("text,value", [
    ("4.50", "4.50"), ("4.5", "4.5"), ("$4.50", "4.50"), ("12", "12"), ("12.25", "12.25"),
    ("4.50 dollars", "4.50"), ("0.95", "0.95"), ("1234.5678", "1234.5678"),
    ("four point five zero", "4.50"), ("twelve point two five", "12.25"), ("four point five", "4.5"),
])
def test_prices_that_parse(text, value):
    assert rv.parse_price(text) == Decimal(value)


@pytest.mark.parametrize("text", [
    "4:50", "4:50 pm", "12:25", "10:05 a.m.", "four fifty", "twelve twenty five", "", "abc", "0",
    "0.00", "-4.50", "4.50.1", "4.12345", "4 point", "point five", "about 4.50", "4.50 or so",
])
def test_prices_that_clarify(text):
    with pytest.raises(rv.Unparseable):
        rv.parse_price(text)


def test_x12_spoken_and_digit_forms_do_not_meet_in_silence():
    """X-X12 (grok): "four fifty" and "4.50". Same decimal → accept; else
    clarify. Measured by THIS parser: "4.50" → 4.50; "four fifty" is
    ambiguous (4.50 or 450) and CLARIFIES — the read-back never speaks a
    guessed price."""
    assert rv.parse_price("4.50") == Decimal("4.50")
    with pytest.raises(rv.Unparseable) as e:
        rv.parse_price("four fifty")
    assert "ambiguous" in str(e.value)


def test_a_clock_shape_is_never_a_price():
    with pytest.raises(rv.Unparseable) as e:
        rv.parse_price("4:50")
    assert "time" in str(e.value)


# --- shares and time -----------------------------------------------------------


@pytest.mark.parametrize("text,value", [("100", 100), ("1,000", 1000), ("one hundred", 100),
                                        ("two hundred fifty", 250), ("a hundred", 100), ("50 shares", 50)])
def test_share_counts(text, value):
    assert rv.parse_shares(text) == value


@pytest.mark.parametrize("text", ["0", "-5", "12.5", "half", "", "some"])
def test_share_counts_that_clarify(text):
    with pytest.raises(rv.Unparseable):
        rv.parse_shares(text)


@pytest.mark.parametrize("text,hm", [("9:45", (9, 45)), ("10:30 am", (10, 30)), ("3:05 pm", (15, 5)),
                                     ("15:05", (15, 5)), ("9:45 a.m.", (9, 45))])
def test_times(text, hm):
    t = rv.parse_time(text)
    assert (t.hour, t.minute) == hm


@pytest.mark.parametrize("text", ["9", "nine forty five", "25:00", "9:75", "", "4.50"])
def test_times_that_clarify(text):
    with pytest.raises(rv.Unparseable):
        rv.parse_time(text)
