"""The slug is the id (ADR-0008 D3 ruling a) — shape and grammar key."""

import pytest

from cobalt.taxonomy.slug import (
    SlugError,
    is_slug,
    per_trade_scope,
    trade_key,
    validate_slug,
)


@pytest.mark.parametrize(
    "slug",
    [
        "hitchhiker",
        "big-dog",
        "nine-ema-scalp",
        "back-through-open",
        "first-vwap-pullback",
        "three-thirty",
        "example-range-break",
        "a1",
    ],
)
def test_valid_slugs(slug):
    assert validate_slug(slug) == slug
    assert is_slug(slug)


@pytest.mark.parametrize(
    "bad",
    [
        "",
        "Back$ide",          # the sheet's display name, not an identity
        "Big Dog",           # spaces
        "BigDog",            # uppercase
        "big_dog",           # underscore is the GRAMMAR spelling, not the slug
        "9-ema-scalp",       # leading digit
        "-leading",
        "trailing-",
        "double--hyphen",
        "has.dot",
    ],
)
def test_rejected_slugs(bad):
    assert not is_slug(bad)
    with pytest.raises(SlugError):
        validate_slug(bad)


def test_the_error_names_the_note():
    with pytest.raises(SlugError, match="Big Dog.md"):
        validate_slug("Big Dog", where="1 - Trading/4 - Strategies/Big Dog.md")


def test_missing_slug_says_it_is_the_id():
    with pytest.raises(SlugError, match="IS the trade's id"):
        validate_slug("")


def test_trade_key_is_the_grammar_spelling():
    assert trade_key("nine-ema-scalp") == "nine_ema_scalp"
    assert trade_key("big-dog") == "big_dog"
    assert trade_key("hitchhiker") == "hitchhiker"


def test_trade_key_validates_first():
    """A bad slug must not be silently converted into a plausible key."""
    with pytest.raises(SlugError):
        trade_key("Big Dog")


def test_per_trade_scope():
    assert per_trade_scope("nine-ema-scalp") == "per_trade(nine_ema_scalp)"
