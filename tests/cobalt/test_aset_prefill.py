"""Prefill scrubbing tests — the auth token must never leak in errors."""

from cobalt.aset.prefill import scrub


def test_scrub_redacts_auth_token_in_urls():
    leaked = (
        "Redirect response '301' for url "
        "'https://elite.finviz.com/quote_export.ashx?t=NVDA&auth=aaaa-bbbb-cccc'"
    )
    cleaned = scrub(leaked)
    assert "aaaa-bbbb-cccc" not in cleaned
    assert "auth=REDACTED" in cleaned


def test_scrub_handles_token_at_end_and_mid_query():
    assert scrub("x?auth=tok123&y=1") == "x?auth=REDACTED&y=1"
    assert scrub("no secrets here") == "no secrets here"
