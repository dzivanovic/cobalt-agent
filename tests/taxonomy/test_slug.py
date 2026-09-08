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
        "example-range-break",
        "example",
        "nine-ema-example",
        "a-b-c",
        "three-thirty",
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
        "Exa$mple",          # a display spelling, not an identity
        "Example Break",     # spaces
        "ExampleBreak",      # uppercase
        "example_break",     # underscore is the GRAMMAR spelling, not the slug
        "9-ema-example",     # leading digit
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
    with pytest.raises(SlugError, match="Example Break.md"):
        validate_slug(
            "Example Break", where="1 - Trading/4 - Strategies/Example Break.md"
        )


def test_missing_slug_says_it_is_the_id():
    with pytest.raises(SlugError, match="IS the trade's id"):
        validate_slug("")


def test_trade_key_is_the_grammar_spelling():
    assert trade_key("example-range-break") == "example_range_break"
    assert trade_key("nine-ema-example") == "nine_ema_example"
    assert trade_key("example") == "example"


def test_trade_key_validates_first():
    """A bad slug must not be silently converted into a plausible key."""
    with pytest.raises(SlugError):
        trade_key("Example Break")


def test_per_trade_scope():
    assert per_trade_scope("example-range-break") == "per_trade(example_range_break)"
