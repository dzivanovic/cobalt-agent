"""The HITL card DM and the outcome DM (F20 FINAL §3 step 4, F-06 B).

Every line leaves through `notify.mattermost.send_dm`, so the F19 redaction
runs on it (`mattermost.py:140`). The card carries the action, a one-line
summary, the short id and the page link with the one-time key in the
FRAGMENT: `<base>/hitl/<id>#k=<key>`. A fragment is never sent to the
server, so no access log carries the key.

THE BASE URL is config: `hitl.page_base_url` in tunables.yaml. No house set
it (the tailnet front's name is not in the repo); while it is null a card
cannot be sent and the request says so (L1).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

#: The page's base URL, a `label` row (no value set yet — a gate item).
BASE_URL_KEY = "hitl.page_base_url"


@dataclass(frozen=True)
class CardFacts:
    """What a card shows: `actions.Prepared` carries the same two fields."""

    action: str
    summary: str


def page_base_url() -> str:
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(BASE_URL_KEY)
    if row is None or not row.value:
        raise RuntimeError(
            f"tunable {BASE_URL_KEY!r} has no value in tunables.yaml — the card cannot link "
            "the /hitl page, and a guessed host is never written (L1)."
        )
    value = str(row.value)
    if not value.startswith("https://"):
        raise RuntimeError(f"tunable {BASE_URL_KEY!r} must be an https:// URL, got {value!r}")
    return value.rstrip("/")


def card_text(row_id: int, short_id: str, facts, key: str, *, base_url: str) -> str:
    return (
        f"HITL card {short_id} · {facts.action}\n"
        f"{facts.summary}\n"
        f"Review, then approve or deny: {base_url.rstrip('/')}/hitl/{row_id}#k={key}\n"
        "A reply \"approve\" here is not an approval — only the page is."
    )


def send_card(row_id: int, short_id: str, facts, key: str, *, base_url: Optional[str] = None,
              cfg=None):
    from cobalt.notify.mattermost import send_dm

    text = card_text(row_id, short_id, facts, key, base_url=base_url or page_base_url())
    return send_dm(text, cfg=cfg)


def outcome_line(short_id: str, status: str) -> str:
    """The one line that goes into the session (FINAL §3 step 6)."""
    return f"HITL {short_id} {status}"


def send_outcome(short_id: str, status: str, *, cfg=None):
    from cobalt.notify.mattermost import send_dm

    return send_dm(outcome_line(short_id, status), cfg=cfg)


__all__ = ["BASE_URL_KEY", "CardFacts", "card_text", "outcome_line", "page_base_url",
           "send_card", "send_outcome"]
