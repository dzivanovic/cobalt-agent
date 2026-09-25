"""X12 (v2 §7, before S1): `published_numbers` of a null score — JSON null
on both sides, never the string "None". At the base `CardUpdate.proximity`
is a required Decimal: a null proximity cannot even be constructed, and
`str()` of a None there would print "None"."""

from __future__ import annotations

import json
from decimal import Decimal

from pydantic import ValidationError

from cobalt.radar.evaluate import CardUpdate, published_numbers

from stale_support import FIXED


def test_x12_null_proximity_and_score_publish_as_json_null():
    fields = dict(card_id=1, conviction=None, card_score=None, score_suppressed="s", proposed_key=None, dots=[],
                  health=None, radar_score_id=None)
    refused, null_payload = None, None
    try:
        null_payload = published_numbers(CardUpdate(proximity=None, **fields))
    except ValidationError as e:
        refused = e.errors()[0]["type"]
    scored_null = published_numbers(CardUpdate(proximity=Decimal("0.5"), **fields))
    texts = [json.dumps(p) for p in (scored_null, null_payload) if p is not None]
    string_none = any('"None"' in t for t in texts)
    print(f"X12: fixed={FIXED} null_proximity_refused_as={refused!r} "
          f"null_proximity_json={None if null_payload is None else json.dumps(null_payload['proximity'])} "
          f"card_score_json={json.dumps(scored_null['card_score'])} string_None_in_payload={string_none}")
    assert scored_null["card_score"] is None and not string_none
    if FIXED:  # v2 §2 C steps 4 + 6: Optional proximity, JSON null
        assert refused is None and null_payload["proximity"] is None and null_payload["card_score"] is None
    else:
        assert refused is not None
