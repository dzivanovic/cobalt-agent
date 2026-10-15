"""The typed-classifier collector: one interface, one door (L9).

`Classifier` is the interface; `OpenRouterClassifier` is its first class.
The local lane plugs in later as a SECOND class behind the same protocol,
nothing upstream noticing (plan §8 step 3).

THE KEY. `OPENROUTER_API_KEY` lives in VaultManager (L4). It is read by
`cobalt.redact.secrets.read_secret` — the new core's ONE vault reader
(L3) — INSIDE each keyed request, placed in that request's
`Authorization` header, and dropped. It is never cached on the instance,
never returned upward, never logged, stored, raised or printed (L41).
Model discovery sends NO key at all: the list is public.

THE GUARDS. Every outbound body passes `cobalt.redact.redact()` — the
pattern half and the F19 literal half. A body the redactor would change
is REFUSED, never sent redacted: a redacted question is a different
question. A keyed call with the literal half INACTIVE (locked vault) is
refused before sending. Everything written to disk passes the same guard
(`_guard_stored`). Every error text passes `redact()` before it is raised
and is raised `from None` — a 401 body can echo the key back.

`record=False` on every `redact()` call here: a refusal RAISES, which is
louder than a counter row, and counting would open a database connection
this trial never holds (plan §7: not the DB). See ESCALATE in the build
report.

THE TRANSPORT is injectable (`transport(method, url, headers, body,
timeout) -> (status, body_bytes)`), so every test runs with no socket.
The default is urllib — `notify/mattermost.py`'s shape. No SDK, no
LiteLLM, no old-tree import (L15).
"""

from __future__ import annotations

import json
import math
import re
import time
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional, Protocol
from urllib import error as urlerror
from urllib import request as urlrequest

from loguru import logger

from cobalt.redact import guard as redact_guard
from cobalt.redact import redact
from cobalt.redact import secrets as vault_secrets

from .config import TrialConfig
from .ledger import OVERRUN_FACTOR, Ledger
from .models import Answer, CallRecord, Choice, ModelEntry, Noul, QuestionSet, Score, TrialItem, Usage

KEY_NAME = "OPENROUTER_API_KEY"
CHANNEL = "classify"

Transport = Callable[[str, str, dict, Optional[bytes], float], tuple[int, bytes]]


class ClassifyError(RuntimeError):
    """A classify step failed or was refused. Message is ALREADY redacted."""


class ClassifyAuthError(ClassifyError):
    """401 / 403 — the run stops."""


def _safe(text: str) -> str:
    return redact(text, channel=CHANNEL, record=False).text


@dataclass
class Discovery:
    """What OpenRouter's public reads said (L45).

    `entry` comes from the PER-MODEL endpoints record of his id — the
    authority (desk R46: the general list omits non-text-output models).
    `raw_record` is that response body byte for byte. `others` are the
    OTHER matching ids of the general list — recorded, never substituted.
    `total` is the general list's count."""

    entry: ModelEntry
    others: list[ModelEntry]
    total: int
    raw_record: bytes = b""
    raw_matches: list[dict] = field(default_factory=list)

    def artifact(self, ruled_id: str) -> dict:
        """The discovery file: his id's endpoints record, ONLY the other
        matching entries of the general list, its total count and
        `ruled_id_listed` — never the rest of the listing."""
        return {
            "models_listed": self.total,
            "ruled_id": ruled_id,
            "ruled_id_listed": True,
            "ruled_id_source": "per-model endpoints record",
            "endpoints_record": json.loads(self.raw_record),
            "other_matching": self.raw_matches,
        }


#: Fields the endpoints record carries per endpoint, not per model. With
#: exactly ONE endpoint they ARE the model's; with several they are not
#: merged (no pricing is picked for him — L1: no cost, no call).
_PER_ENDPOINT = ("pricing", "context_length", "supported_parameters")


def _entry_from_record(raw: bytes, model_id: str) -> ModelEntry:
    """`{"data": {id, name, …, endpoints: [...]}}` → the model's entry.
    The record's own `id` must be his id; anything else is FAILED."""
    try:
        data = json.loads(raw)["data"]
        if not isinstance(data, dict):
            raise TypeError("'data' is not an object")
    except Exception as e:  # noqa: BLE001
        raise ClassifyError(
            f"the {model_id} endpoints record did not parse as {{'data': {{...}}}} "
            f"({type(e).__name__})"
        ) from None
    if data.get("id") != model_id:
        raise ClassifyError(
            f"the endpoints record for {model_id} names id {data.get('id')!r} — refused"
        )
    fields = dict(data)
    endpoints = data.get("endpoints")
    if isinstance(endpoints, list) and len(endpoints) == 1 and isinstance(endpoints[0], dict):
        for k in _PER_ENDPOINT:
            if fields.get(k) is None and endpoints[0].get(k) is not None:
                fields[k] = endpoints[0][k]
    return ModelEntry(**fields)


# -- the door: OpenRouter System One (desk R47) ----------------------------------
#
# `POST /api/v1/systemone`, built FIELD FOR FIELD from OpenRouter's
# published OpenAPI schema (`DecisionsRequest` / `DecisionsResponse`):
#   request   {model, state, questions: {id: {type, instructions, criteria}}}
#             choice → criteria = {option key: description}
#             score  → criteria = [level, …] (index 0 = the first level)
#             noul   → criteria = {"true": …, "false": …} (optional; both or none)
#   response  {id?, model, provider?, answers: {id: {type, …}}, usage:
#             {input_tokens, output_tokens, cost?}}
#             choice → {choice, probabilities?, confidence?}
#             score  → {score, probabilities?, confidence?, legend?}
#             noul   → {noul}  (the probability of yes)
# No field the schema does not name is sent — the schema has no usage
# accounting switch (`usage.cost` comes back by default, per its docs).


def render_systemone(model_id: str, qset: QuestionSet, item: TrialItem) -> dict:
    """The request body. Question order is the set's order."""
    questions: dict[str, dict] = {}
    for qid, q in qset.questions.items():
        if isinstance(q, Choice):
            questions[qid] = {"type": "choice", "instructions": q.instructions,
                              "criteria": dict(q.options)}
        elif isinstance(q, Score):
            questions[qid] = {"type": "score", "instructions": q.instructions,
                              "criteria": list(q.levels)}
        elif isinstance(q, Noul):
            rendered: dict[str, Any] = {"type": "noul", "instructions": q.instructions}
            if (q.true is None) != (q.false is None):
                raise ClassifyError(
                    f"{qset.id}.{qid}: a Noul's criteria need both 'true' and 'false' "
                    "(DecisionsNoulQuestion) — one side is never invented"
                )
            if q.true is not None:
                rendered["criteria"] = {"true": q.true, "false": q.false}
            questions[qid] = rendered
        else:  # pragma: no cover - the discriminated union holds three types
            raise ClassifyError(f"{qset.id}.{qid}: unknown question type {type(q).__name__}")
    return {"model": model_id, "state": item.state, "questions": questions}


def _is_number(x: Any) -> bool:
    if not isinstance(x, (int, float)) or isinstance(x, bool):
        return False
    try:
        return math.isfinite(x)
    except OverflowError:  # D2: an int too large for a float is no number we book
        return False


def parse_answers(qset: QuestionSet, resp: Any) -> list[Answer]:
    """`DecisionsResponse.answers` → one `Answer` per asked question.

    Anything the schema or the question does not allow raises
    `ValueError` — the caller records `status: invalid`, never a default
    label (plan B3). Probabilities / confidence are taken ONLY when the
    response carries them; absent → `None`, `source: absent`."""
    if not isinstance(resp, dict) or not isinstance(resp.get("answers"), dict):
        raise ValueError("the response carries no 'answers' object")
    answers = resp["answers"]
    missing = [q for q in qset.questions if q not in answers]
    extra = [a for a in answers if a not in qset.questions]
    if missing or extra:
        raise ValueError(f"answers do not match the questions: missing {missing}, unasked {extra}")

    out: list[Answer] = []
    for qid, q in qset.questions.items():
        a = answers[qid]
        if not isinstance(a, dict) or a.get("type") != q.type:
            raise ValueError(f"{qid}: answer type {a.get('type') if isinstance(a, dict) else a!r} "
                             f"for a {q.type} question")
        probs, conf = a.get("probabilities"), a.get("confidence")
        if probs is not None and not (
            isinstance(probs, dict) and all(isinstance(k, str) and _is_number(v) for k, v in probs.items())
        ):
            raise ValueError(f"{qid}: probabilities is not a map of numbers")
        if conf is not None and not _is_number(conf):
            raise ValueError(f"{qid}: confidence is not a number")

        if isinstance(q, Choice):
            value: Any = a.get("choice")
            if not isinstance(value, str) or value not in q.options:
                raise ValueError(f"{qid}: choice {value!r} is not one of {sorted(q.options)}")
        elif isinstance(q, Score):
            value = a.get("score")
            if not _is_number(value) or not 0 <= value <= len(q.levels) - 1:
                raise ValueError(f"{qid}: score {value!r} is outside 0..{len(q.levels) - 1}")
            value = float(value)
        else:
            value = a.get("noul")
            if not _is_number(value) or not 0 <= value <= 1:
                raise ValueError(f"{qid}: noul {value!r} is not a probability in 0..1")
            value = float(value)

        out.append(Answer(
            question_id=qid,
            value=value,
            probabilities={k: float(v) for k, v in probs.items()} if probs is not None else None,
            confidence=float(conf) if conf is not None else None,
            source="returned" if (probs is not None or conf is not None) else "absent",
        ))
    return out


def _usage(resp: Any) -> Optional[Usage]:
    u = resp.get("usage") if isinstance(resp, dict) else None
    if not isinstance(u, dict):
        return None
    i, o = u.get("input_tokens"), u.get("output_tokens")
    if not (isinstance(i, int) and isinstance(o, int)) or isinstance(i, bool) or isinstance(o, bool):
        return None
    if i < 0 or o < 0:  # not two non-negative ints: no usage (its cost is not taken)
        return None
    return Usage(input_tokens=i, output_tokens=o)


def _str_field(resp: Any, key: str) -> Optional[str]:
    v = resp.get(key) if isinstance(resp, dict) else None
    return v if isinstance(v, str) else None


class _NoRedirect(urlrequest.HTTPRedirectHandler):
    """Follow NO redirect. The stdlib default re-sends every non-content
    header — `Authorization` included — to any `Location` host; refusing
    here makes a 3xx surface as the `HTTPError` the transport returns."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_OPENER = urlrequest.build_opener(_NoRedirect)


def urllib_transport(method: str, url: str, headers: dict, body: Optional[bytes],
                     timeout: float) -> tuple[int, bytes]:
    """The default transport. An HTTP error status is RETURNED, not raised,
    so the caller records it; only a failure to talk at all raises. A 3xx
    is returned as its status — never followed (`_NoRedirect`)."""
    req = urlrequest.Request(url, data=body, headers=headers, method=method)
    try:
        with _OPENER.open(req, timeout=timeout) as resp:
            return resp.status, resp.read()
    except urlerror.HTTPError as e:
        try:
            payload = e.read()
        except Exception:  # noqa: BLE001
            payload = b""
        return e.code, payload


class Classifier(Protocol):
    """The collector interface (L9). A second lane is a second class."""

    def discover(self) -> list[ModelEntry]: ...

    def classify(self, qset: QuestionSet, item: TrialItem) -> CallRecord: ...


class OpenRouterClassifier:
    """The OpenRouter door. Holds a config, a transport and a ledger —
    never a key."""

    def __init__(self, cfg: TrialConfig, transport: Optional[Transport] = None,
                 ledger: Optional[Ledger] = None, pricing: Optional[dict] = None):
        self.cfg = cfg
        self.transport: Transport = transport or urllib_transport
        # fold F2: the ONE host-wide spend ledger, never a per-checkout file
        self.ledger = ledger or Ledger(
            Path(cfg.spend_ledger),
            cap_usd=cfg.spend_cap_usd,
            call_ceiling=cfg.call_ceiling,
            carried=[c.cost_usd for c in cfg.carried_spend],
        )
        self._pricing_given = pricing

    # -- the price (L1: no cost, no call) -----------------------------------------

    def pricing(self) -> tuple[float, float]:
        """(prompt, completion) USD per token, from the listed entry."""
        p = self._pricing_given
        if p is None:
            try:
                p = self.cfg.entry_pricing()
            except Exception as e:  # noqa: BLE001 - ClassifyConfigError, reworded as a refusal
                raise ClassifyError(f"no listed pricing — no call ({e})") from None
        try:
            prompt, completion = float(p["prompt"]), float(p["completion"])
        except Exception:  # noqa: BLE001
            raise ClassifyError(
                f"the entry's pricing carries no numeric prompt / completion price "
                f"(keys: {sorted(p) if isinstance(p, dict) else type(p).__name__}) — no call"
            ) from None
        if not all(math.isfinite(x) and x >= 0 for x in (prompt, completion)):
            raise ClassifyError("the entry's pricing is negative or not finite — no call") from None
        return prompt, completion

    def project(self, body: bytes) -> float:
        """Projected USD of one call: the rendered body's bytes ÷ 4 as input
        tokens (an ESTIMATE, stated as one) × the listed prompt price.
        Output tokens are not projected (listed completion price: see the
        entry; the returned cost is checked against 10× this)."""
        prompt, _ = self.pricing()
        return math.ceil(len(body) / 4) * prompt

    # -- the door ---------------------------------------------------------------

    def render(self, qset: QuestionSet, item: TrialItem) -> dict:
        if self.cfg.door != "systemone":
            raise ClassifyError(f"no door decided (door={self.cfg.door!r}) — no request can be rendered")
        return render_systemone(self.cfg.model_id, qset, item)

    def body(self, qset: QuestionSet, item: TrialItem) -> bytes:
        return json.dumps(self.render(qset, item), ensure_ascii=False).encode("utf-8")

    def classify(self, qset: QuestionSet, item: TrialItem) -> CallRecord:
        return self._classify(qset, item)[0]

    def _classify(self, qset: QuestionSet, item: TrialItem, *,
                  overrun_check: bool = True) -> tuple[CallRecord, bytes]:
        """render → price → outbound guard → ledger check → timed POST →
        parse ONLY what came back → ledger record → stored guard →
        overrun check. Returns (the guarded record, the raw body).

        The ledger line is written BEFORE the stored guard: a refused body
        was still paid for, and the total demand must count it (L53)."""
        t0 = time.perf_counter()
        payload = self.render(qset, item)
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        projected = self.project(body)
        status, raw, http_ms = self._send(payload, projected_usd=projected)

        try:
            resp: Any = json.loads(raw)
        except Exception:  # noqa: BLE001
            resp = None
        base = dict(
            set_id=qset.id, set_sha256=qset.sha256, item_id=item.id,
            provenance=item.provenance, request=payload, http_ms=http_ms,
            http_status=status, projected_usd=projected,
            raw_response=resp if resp is not None else raw[:2000].decode("utf-8", "replace"),
            model_returned=_str_field(resp, "model"),
            provider_returned=_str_field(resp, "provider"),
        )

        if status != 200:
            logger.warning(f"classify: HTTP {status} for {qset.id}/{item.id} — recorded, not retried")
            # it came back with no cost: booked at its own projection (never 0, L1)
            self.ledger.record(f"local-{uuid.uuid4()}", projected, "projected")
            rec = CallRecord(**base, status="http_error", error=f"HTTP {status}",
                             latency_ms=(time.perf_counter() - t0) * 1000.0)
            self._guard_stored(rec.model_dump(mode="json"))
            self._guard_stored(raw.decode("utf-8", "replace"))
            return rec, raw

        usage = _usage(resp)
        cost: Optional[float] = None
        cost_source: Optional[str] = None
        # F9: a cost the server stated is booked whatever the tokens beside
        # it (L1) — read even when `_usage` refused the token counts
        u = resp.get("usage") if isinstance(resp, dict) else None
        returned = u.get("cost") if isinstance(u, dict) else None
        if _is_number(returned) and returned >= 0:
            cost, cost_source = float(returned), "returned"
        elif usage is not None:
            if _is_number(returned):
                logger.error(
                    f"classify: returned cost is negative for {qset.id}/{item.id} — "
                    "computed from tokens instead"
                )
            prompt, completion = self.pricing()
            cost = usage.input_tokens * prompt + usage.output_tokens * completion
            cost_source = "computed"
            if not math.isfinite(cost) or cost < 0:
                logger.error(
                    f"classify: computed cost is not finite for {qset.id}/{item.id} — "
                    "booked at its projection"
                )
                cost, cost_source = None, None

        answers: list[Answer] = []
        error: Optional[str] = None
        try:
            if base["model_returned"] is None:
                raise ValueError("the response carries no 'model' (required)")
            if usage is None:
                raise ValueError("the response carries no usage {input_tokens, output_tokens} (required)")
            if cost is None:  # F8: an ok record carries a cost (CallRecord, L1)
                raise ValueError("the usage × the listed price gives no bookable cost (required)")
            answers = parse_answers(qset, resp)
            call_status = "ok"
        except ValueError as e:
            call_status, error = "invalid", _safe(str(e))
            logger.error(f"classify: INVALID response for {qset.id}/{item.id}: {error}")

        if cost is not None:
            # the response id only when it passes the guard; the cost is
            # still recorded under a local id when it does not
            call_id = _str_field(resp, "id")
            if not (call_id and redact(call_id, channel=CHANNEL, record=False).clean):
                call_id = f"local-{uuid.uuid4()}"
            self.ledger.record(call_id, cost, cost_source)
        else:
            # a 200 with no usage came back with no cost: its own projection
            self.ledger.record(f"local-{uuid.uuid4()}", projected, "projected")

        rec = CallRecord(**base, status=call_status, answers=answers, usage=usage,
                         cost_usd=cost, cost_source=cost_source, error=error,
                         latency_ms=(time.perf_counter() - t0) * 1000.0)
        self._guard_stored(rec.model_dump(mode="json"))
        self._guard_stored(raw.decode("utf-8", "replace"))
        if overrun_check and cost is not None:
            self.ledger.check_cost(returned=cost, projected=projected)
        return rec, raw

    # -- the key ------------------------------------------------------------

    def _key(self) -> str:
        """Read at call time, inside the request that needs it. Never cached."""
        try:
            value = vault_secrets.read_secret(KEY_NAME)
        except vault_secrets.VaultAccessError as e:
            raise ClassifyError(
                f"{KEY_NAME} could not be read from the vault: {_safe(str(e))}"
            ) from None
        if not value:
            raise ClassifyError(
                f"{KEY_NAME} is not in the vault — no keyed call can be made "
                "(the value is never printed; only its name)"
            )
        return value

    # -- the guards -----------------------------------------------------------

    def _guard_outbound(self, body: bytes, *, keyed: bool) -> None:
        text = body.decode("utf-8")
        if keyed:
            lit = redact_guard.load_literals()
            if not lit.available:
                raise ClassifyError(
                    "F19 literal guard INACTIVE on a keyed call — refused before sending "
                    f"({_safe(lit.reason)})"
                )
        safe = redact(text, channel=CHANNEL, record=False)
        if not safe.clean:
            raise ClassifyError(
                "outbound body carries secret-shaped text — refused, not sent "
                f"(kinds: {safe.describe()})"
            )

    def _guard_stored(self, obj) -> None:
        text = json.dumps(obj, default=str, ensure_ascii=False)
        safe = redact(text, channel=CHANNEL, record=False)
        if not safe.clean:
            raise ClassifyError(
                "object to store carries secret-shaped text — refused, not written "
                f"(kinds: {safe.describe()})"
            )

    def literal_guard_state(self) -> str:
        return "active" if redact_guard.load_literals().available else "INACTIVE"

    # -- discovery (KEYLESS) ----------------------------------------------------

    def endpoints_url(self) -> str:
        """His id's per-model endpoints record, on the same host as the list."""
        return f"{self.cfg.models_url.rstrip('/')}/{self.cfg.model_id}/endpoints"

    def _public_get(self, url: str, what: str) -> tuple[int, bytes]:
        """A KEYLESS GET: no `Authorization` header — the key stays out of
        every call that does not need it."""
        headers = {"Accept": "application/json", "User-Agent": "cobalt-classify/1"}
        try:
            return self.transport("GET", url, headers, None, self.cfg.timeout_s)
        except Exception as e:  # noqa: BLE001
            raise ClassifyError(_safe(f"{type(e).__name__} on GET {what}: {e}")) from None

    def _general_list(self) -> tuple[list[dict], int]:
        """The general list: (matching entries, total). Read to RECORD other
        Jev / typesafe ids only — zero matches here is not an error."""
        status, raw = self._public_get(self.cfg.models_url, "models")
        if status != 200:
            text = raw[:400].decode("utf-8", "replace")
            raise ClassifyError(_safe(f"HTTP {status} on GET models: {text}")) from None
        try:
            data = json.loads(raw)["data"]
            if not isinstance(data, list):
                raise TypeError("'data' is not a list")
        except Exception as e:  # noqa: BLE001
            raise ClassifyError(
                f"the model list did not parse as {{'data': [...]}} ({type(e).__name__})"
            ) from None
        pat = re.compile(self.cfg.match_pattern)
        matches = [
            e for e in data
            if isinstance(e, dict)
            and (pat.search(str(e.get("id", ""))) or pat.search(str(e.get("name", ""))))
        ]
        return matches, len(data)

    def discover_detail(self) -> "Discovery":
        """Two KEYLESS GETs, in this order (desk R46):

        1. his id's PER-MODEL endpoints record — THE AUTHORITY. 404 → he
           is not listed (FAILED, naming the general list's matching ids).
        2. the general list — only to RECORD any other matching id.

        Verifies HIS id (`cfg.model_id`, R42); never picks one. Another
        matching id is RECORDED in `others`, never an error and never
        substituted."""
        status, raw = self._public_get(self.endpoints_url(), "model endpoints")
        if status not in (200, 404):
            text = raw[:400].decode("utf-8", "replace")
            raise ClassifyError(
                _safe(f"HTTP {status} on GET {self.cfg.model_id} endpoints: {text}")
            ) from None

        matches, total = self._general_list()
        other_raw = [e for e in matches if str(e.get("id")) != self.cfg.model_id]

        if status == 404:
            if not matches:
                raise ClassifyError(
                    f"OpenRouter lists no model matching {self.cfg.match_pattern} — "
                    f"{total} models listed (per-model endpoints of "
                    f"{self.cfg.model_id}: HTTP 404)"
                )
            ids = [str(e.get("id")) for e in matches]
            raise ClassifyError(
                f"OpenRouter does not list {self.cfg.model_id} — matching ids: "
                f"{', '.join(ids)} — {total} models listed"
            )

        entry = _entry_from_record(raw, self.cfg.model_id)
        return Discovery(
            entry=entry,
            others=[ModelEntry(**e) for e in other_raw],
            total=total,
            raw_record=raw,
            raw_matches=other_raw,
        )

    def discover(self) -> list[ModelEntry]:
        """[his id's entry, *every other matching entry]."""
        d = self.discover_detail()
        return [d.entry, *d.others]

    # -- the one keyed send --------------------------------------------------

    def _send(self, payload: dict, *, projected_usd: float) -> tuple[int, bytes, float]:
        """Guard → ledger check → key → POST. Returns (status, body, http_ms).

        401 / 403 raise `ClassifyAuthError` (the run stops); every other
        status is returned for the caller to record — 429 / 5xx are NOT
        retried (the trial measures raw behaviour)."""
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self._guard_outbound(body, keyed=True)
        # fold F3: the cap is checked on this call's WORST-CASE cost — the
        # largest returned cost it can book before check_cost stops the run
        self.ledger.check(OVERRUN_FACTOR * projected_usd, calls=1)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._key()}",
        }
        t0 = time.perf_counter()
        try:
            status, raw = self.transport("POST", self.cfg.door_url, headers, body,
                                         self.cfg.timeout_s)
        except Exception as e:  # noqa: BLE001 - the KIND matters; the text is redacted
            raise ClassifyError(_safe(f"{type(e).__name__} on POST systemone: {e}")) from None
        finally:
            headers = None  # noqa: F841 - the header dict (and the key in it) is dropped here
        http_ms = (time.perf_counter() - t0) * 1000.0
        if status in (401, 403):
            # it came back: one ledger line at its projection, before the raise
            self.ledger.record(f"local-{uuid.uuid4()}", projected_usd, "projected")
            text = raw[:400].decode("utf-8", "replace")
            raise ClassifyAuthError(
                _safe(f"HTTP {status} on POST systemone (auth) — run stopped: {text}")
            ) from None
        return status, raw, http_ms


__all__ = [
    "CHANNEL",
    "ClassifyAuthError",
    "ClassifyError",
    "Classifier",
    "Discovery",
    "KEY_NAME",
    "OpenRouterClassifier",
    "Transport",
    "parse_answers",
    "render_systemone",
    "urllib_transport",
]
