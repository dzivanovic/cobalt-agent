"""DRC K2 fix r1 — OFFLINE half (L75; the fix prompt
`prompts/2026-09-25/02-drc-k2-fix-r1-build.md` F2).

F-5: ONE partial-import rule for the first record and every re-pair
(v3 `:181` "as its first record did", `FR14`; L3), `52`'s HOLD 6
(`drc-k2-check-2026-09-24.md:164`). Every symbol is imported INSIDE the
test that needs it, so each test is its own red until the fix exists.
Constructed values only (L32 / L45).
"""

from __future__ import annotations

import pytest


def test_missing_of_a_parsed_import_is_empty():
    """F-5 (`drc-k2-check-2026-09-24.md:164`): a file that is not partial
    is missing nothing."""
    from cobalt.drc.models import Outcome, missing_of

    assert missing_of(Outcome.PARSED, "") == []


def test_missing_of_inverts_the_partial_flag():
    """F-5 (`drc-k2-check-2026-09-24.md:164`): `missing_of` is the one
    inverse of `partial_flag` — the stored reason gives back the file's
    own missing columns."""
    from cobalt.drc import trading_log
    from cobalt.drc.models import ImportResult, Kind, Outcome, missing_of

    for missing in ([trading_log.ACCOUNT], [trading_log.PRICE, trading_log.ACCOUNT]):
        r = ImportResult(name="t.md", kind=Kind.TRADING_LOG, outcome=Outcome.PARTIAL, missing=missing)
        assert missing_of(Outcome.PARTIAL, r.partial_flag) == missing


def test_missing_of_refuses_an_unreadable_partial_reason():
    """F-5 (`drc-k2-check-2026-09-24.md:164`): a partial reason that is not
    the partial flag is never guessed (L1)."""
    from cobalt.drc.models import Outcome, missing_of

    with pytest.raises(ValueError):
        missing_of(Outcome.PARTIAL, "not a partial flag")


def test_pairing_not_computed_is_the_first_records_text():
    """F-5 (`drc-k2-check-2026-09-24.md:164`): a file missing only a
    non-pairing column pairs; one missing a pairing column stores exactly
    the first record's text (`trading_log.py:170-171`)."""
    from cobalt.drc import trading_log
    from cobalt.drc.trading_log import pairing_not_computed

    assert pairing_not_computed([trading_log.ACCOUNT]) == {}
    assert pairing_not_computed([trading_log.PRICE]) == {
        "pairing": f"not computed — missing: {trading_log.PRICE}"
    }
