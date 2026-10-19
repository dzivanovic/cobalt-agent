"""The CoS DM listener — deterministic, no LLM in the watch loop (F20 FINAL §2, §5; F-20, F-31; L2, L18).

It reads new posts in the DM between the bot `notify.yaml` names
(`MATTERMOST_CREDS`) and him, and for each post, in this order:

1. the bot's own posts (cards, replies, outcome lines) are skipped;
2. THE KILL PHRASE IS MATCHED FIRST (`killswitch.matches_kill_phrase`,
   exact, case-folded, stripped) → `killswitch.engage`. No turn row, no
   session. There is NO RESUME PATH here: the switch stops `com.cobalt.cos`
   itself (`jobs/wrapper.py` `should_keep_running`), so no listener is left
   to hear `COBALT RESUME` (F-31, T7') — `cobalt resume` is the way back;
3. every other post — a text "approve …" included — is ONE `cobalt_cos_turns`
   row, inserted `pending` before the session is called (unique
   `message_ref` = the post id), then `running` → `done` | `failed`. A DM
   text never changes a `cobalt_hitl_requests` row (L37).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Optional

from loguru import logger


@dataclass(frozen=True)
class Post:
    id: str
    user_id: str
    message: str
    create_at: int


def parse_posts(payload: dict) -> list[Post]:
    """A Mattermost `GET /channels/{id}/posts` body → posts, oldest first."""
    posts = payload.get("posts") or {}
    out = []
    for post_id in payload.get("order") or []:
        raw = posts.get(post_id)
        if not raw or raw.get("delete_at"):
            continue
        out.append(Post(id=str(raw["id"]), user_id=str(raw["user_id"]),
                        message=str(raw.get("message") or ""), create_at=int(raw["create_at"])))
    return sorted(out, key=lambda p: p.create_at)


def fetch_dm_posts(since_ms: int) -> tuple[dict, str]:
    """The DM's posts since `since_ms`, and the bot's own user id. Plain
    HTTP through the notify channel's credential (never logged)."""
    from cobalt.notify import mattermost
    from cobalt.notify.config import load_notify_config

    cfg = load_notify_config().mattermost
    url, token = mattermost._creds(cfg)
    timeout = mattermost.timeout_s()
    me = mattermost._api(url, token, "/users/me", None, timeout)
    them = mattermost._api(url, token, f"/users/username/{cfg.dm_username}", None, timeout)
    channel = mattermost._api(url, token, "/channels/direct", [me["id"], them["id"]], timeout)
    payload = mattermost._api(url, token, f"/channels/{channel['id']}/posts?since={int(since_ms)}",
                              None, timeout)
    return payload, me["id"]


def _engage(phrase: str) -> None:
    from cobalt.jobs import killswitch

    killswitch.engage(by="cos.listener", phrase=phrase)


def _is_kill(text: str) -> bool:
    from cobalt.jobs import killswitch

    return killswitch.matches_kill_phrase(text)


def _unique_violation(e: Exception) -> bool:
    import psycopg

    return isinstance(e, psycopg.errors.UniqueViolation)


class Listener:
    def __init__(
        self,
        *,
        fetch: Callable[[int], tuple[dict, str]] = fetch_dm_posts,
        store,
        run_turn: Callable[[str], Any],
        reply: Callable[[str], object],
        engage: Callable[[str], object] = _engage,
        is_kill: Callable[[str], bool] = _is_kill,
        since_ms: int = 0,
    ):
        self.fetch = fetch
        self.store = store
        self.run_turn = run_turn
        self.reply = reply
        self.engage = engage
        self.is_kill = is_kill
        self.since_ms = since_ms
        self.me_id: Optional[str] = None

    def handle(self, post: Post) -> str:
        if self.me_id is not None and post.user_id == self.me_id:
            return "own"
        if self.is_kill(post.message):
            logger.error("CoS listener: the kill phrase arrived in post {} — engaging the kill switch",
                         post.id)
            self.engage(post.message.strip())
            return "killed"
        try:
            turn = self.store.insert_turn(post.id)
        except Exception as e:  # noqa: BLE001
            if _unique_violation(e):
                return "duplicate"
            raise
        self.store.set_turn(turn, "running")
        try:
            outcome = self.run_turn(post.message)
        except BaseException as e:
            # Never left `running` (L18): the row ends `failed`, then the error goes on up.
            self.store.set_turn(turn, "failed", error=f"{type(e).__name__}: {e}")
            raise
        fields = {k: getattr(outcome, k, None) for k in
                  ("num_turns", "result_subtype", "is_error", "terminal_reason")}
        if outcome.ok:
            self.store.set_turn(turn, "done", **fields)
            if outcome.reply:
                self.reply(outcome.reply)
            return "done"
        self.store.set_turn(turn, "failed", error=outcome.error, **fields)
        # A failed turn still posts what it said before it stopped (FINAL §5: max turns).
        if outcome.reply:
            self.reply(outcome.reply)
        return "failed"

    def poll(self) -> list[str]:
        payload, self.me_id = self.fetch(self.since_ms)
        out = []
        for post in parse_posts(payload):
            out.append(self.handle(post))
            self.since_ms = max(self.since_ms, post.create_at)
            if out[-1] == "killed":
                # The switch is engaged: no later post of this batch opens a session.
                break
        return out


__all__ = ["Listener", "Post", "fetch_dm_posts", "parse_posts"]
