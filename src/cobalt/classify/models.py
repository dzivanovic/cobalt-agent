"""The neutral typed-question schema and the per-call record.

Three question types, the three primitives of the typed-classifier
research (`TYPESAFE-CLASSIFIER-RESEARCH-DEEP-2026-09-21.md` §2 rows 1–3):
pick one of many (`Choice`), rate on ordered levels (`Score`), give a
yes/no (`Noul`). They are written NEUTRALLY — no vendor field name — so
the same `QuestionSet` renders into whichever door a collector speaks
(L9: the local lane plugs in later as a second class, nothing upstream
noticing).

THE RULES THIS MODULE KEEPS:

* every `Choice` carries `unsure` — nothing turns "cannot tell" into an
  answer (deep §5 conventions);
* a state is WORDS: a dict state refuses any numeric value, because no
  raw number reaches a model (plan §2; the buckets are his, L53);
* a question set's identity is the sha256 of exactly what is sent, so a
  one-character wording change is a new classifier (L10);
* a `CallRecord` carries its inputs, the answer, confidence as returned
  (never computed, never defaulted), latency, usage and the model id AS
  RETURNED (L57). An absent confidence is `None` with `source: absent`.
"""

from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from typing import Annotated, Any, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

#: A value that reads as a number: an int, a float, or a string that is
#: one ("3", "-0.25", "1e3", " 12 "). Words only in a state.
_NUMERIC = re.compile(r"^\s*[-+]?(\d+\.?\d*|\.\d+)([eE][-+]?\d+)?\s*$")

UNSURE = "unsure"


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Choice(_Strict):
    """One option from a described set. `unsure` is REQUIRED."""

    type: Literal["choice"] = "choice"
    instructions: str = Field(min_length=1)
    options: dict[str, str] = Field(min_length=2)

    @field_validator("options")
    @classmethod
    def _unsure_required(cls, v: dict[str, str]) -> dict[str, str]:
        if UNSURE not in v:
            raise ValueError(
                f"a Choice must carry an '{UNSURE}' option (got {sorted(v)}) — the "
                "abstain path is the question's, never the code's"
            )
        return v


class Score(_Strict):
    """Ordered levels, lowest first. 2–10 levels (deep §2 row 2)."""

    type: Literal["score"] = "score"
    instructions: str = Field(min_length=1)
    levels: list[str] = Field(min_length=2, max_length=10)

    @field_validator("levels")
    @classmethod
    def _distinct(cls, v: list[str]) -> list[str]:
        if len(set(v)) != len(v):
            raise ValueError(f"Score levels must be distinct (got {v})")
        return v


class Noul(_Strict):
    """Yes / no, with optional descriptions of each side."""

    type: Literal["noul"] = "noul"
    instructions: str = Field(min_length=1)
    true: Optional[str] = None
    false: Optional[str] = None


Question = Annotated[Union[Choice, Score, Noul], Field(discriminator="type")]


class QuestionSet(_Strict):
    """An ordered map of question id → question. Order is what is sent."""

    id: str = Field(min_length=1)
    version: int = Field(ge=1)
    questions: dict[str, Question] = Field(min_length=1)

    def canonical(self) -> str:
        """The canonical JSON of everything that is SENT: the questions,
        in order. The set's id and version are Cobalt's labels and never
        leave the host, so they are not part of its identity."""
        return json.dumps(
            {k: q.model_dump(mode="json") for k, q in self.questions.items()},
            ensure_ascii=False,
            separators=(",", ":"),
        )

    @property
    def sha256(self) -> str:
        """Computed, never stored: a stored hash is a hash that can drift."""
        return hashlib.sha256(self.canonical().encode()).hexdigest()

    def first(self, n: int) -> "QuestionSet":
        """The first `n` questions (plan M2). More than the set holds → error."""
        if n < 1 or n > len(self.questions):
            raise ValueError(
                f"--questions {n}: set {self.id} holds {len(self.questions)} question(s)"
            )
        keep = list(self.questions.items())[:n]
        return self.model_copy(update={"questions": dict(keep)})

    def reversed(self) -> "QuestionSet":
        """The question map reversed, and nothing else (plan M6)."""
        return self.model_copy(update={"questions": dict(reversed(list(self.questions.items())))})

    def only(self, qid: str) -> "QuestionSet":
        """One question of this set, as its own set (parallel / sequential modes)."""
        return self.model_copy(update={"questions": {qid: self.questions[qid]}})


class TrialItem(_Strict):
    """One state to classify. WORDS only; provenance says where it came from."""

    id: str = Field(min_length=1)
    state: Union[str, dict[str, str]]
    provenance: str

    @field_validator("state", mode="before")
    @classmethod
    def _words_only(cls, v: Any) -> Any:
        if isinstance(v, dict):
            for k, val in v.items():
                if isinstance(val, bool) or not isinstance(val, str) or _NUMERIC.match(val):
                    raise ValueError(
                        f"state key {k!r} carries a numeric value — a state is WORDS "
                        "only; code buckets a number into a word before it gets here"
                    )
        return v

    @field_validator("provenance")
    @classmethod
    def _provenance(cls, v: str) -> str:
        if v != "constructed" and not (v.startswith("real:") and len(v) > len("real:")):
            raise ValueError(f"provenance must be 'constructed' or 'real:<repo path>' (got {v!r})")
        return v


class Answer(_Strict):
    """One typed answer. Probabilities / confidence only as RETURNED.

    `value` is what the door returned for the question's own field, never
    thresholded: a Choice's option key; a Score's probability-weighted
    position (index 0 = the first level); a Noul's probability of yes.
    Turning a number into a label is a rule, and rules are his (L53)."""

    question_id: str
    value: Union[bool, str, float, None] = None
    probabilities: Optional[dict[str, float]] = None
    confidence: Optional[float] = None
    source: Literal["returned", "absent"]


class Usage(_Strict):
    input_tokens: int = Field(ge=0)
    output_tokens: int = Field(ge=0)


class ModelEntry(BaseModel):
    """One entry of OpenRouter's public model list, as returned.

    `extra="allow"`: the listing is the vendor's shape, and a field this
    schema does not name is kept, not dropped (L45 — the fixture is the
    real entry, not a subset of it)."""

    model_config = ConfigDict(extra="allow")

    id: str
    name: str = ""
    created: Optional[int] = None
    description: str = ""
    context_length: Optional[int] = None
    pricing: Optional[dict[str, Any]] = None
    supported_parameters: list[str] = Field(default_factory=list)
    architecture: Optional[dict[str, Any]] = None


#: Widened for the router's decision rows (fold F9): every ClassifyError of a
#: routed card is a status, never a crash of the batch.
CallStatus = Literal[
    "ok", "invalid", "refused", "http_error", "transport_error", "auth_error",
    "cap_refused", "ceiling_refused", "overrun", "timeout",
]


class CallRecord(_Strict):
    """One call, replayable (L57). Written guarded; never holds a key."""

    set_id: str
    set_sha256: str = Field(min_length=64, max_length=64)
    item_id: str
    provenance: str
    request: dict[str, Any]
    raw_response: Optional[Any] = None
    answers: list[Answer] = Field(default_factory=list)
    latency_ms: float = Field(ge=0)
    http_ms: float = Field(ge=0)
    status: CallStatus
    http_status: Optional[int] = None
    usage: Optional[Usage] = None
    cost_usd: Optional[float] = None
    cost_source: Optional[Literal["returned", "computed"]] = None
    projected_usd: Optional[float] = None
    model_returned: Optional[str] = None
    provider_returned: Optional[str] = None
    door: Literal["openrouter"] = "openrouter"
    error: Optional[str] = None
    at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @model_validator(mode="after")
    def _ok_is_complete(self) -> "CallRecord":
        if self.status == "ok" and (self.usage is None or self.cost_usd is None):
            raise ValueError("an ok CallRecord carries usage and a cost (L1: no cost, no call)")
        return self


class RouteDecision(_Strict):
    """One DECISION row of the routing ledger (design §3 step 1; card 591 J2).

    Written once per routed card and never rewritten; an outcome is a later
    row keyed to it by `card_path` and `launch_sha`. JEV's answers are stored
    as returned, never recomputed. It never holds the card text (L32,
    decision 5): only its path, its shas and code-computed counts."""

    kind: Literal["decision"] = "decision"
    card_path: str
    card_blob_sha: Optional[str] = None
    launch_sha: Optional[str] = None
    set_id: str
    set_sha256: str = Field(min_length=64, max_length=64)
    table_sha256: str = Field(min_length=64, max_length=64)
    jev_model_returned: Optional[str] = None
    band: Optional[str] = None
    band_probabilities: Optional[dict[str, float]] = None
    band_confidence: Optional[float] = None
    gates: dict[str, Optional[float]] = Field(default_factory=dict)
    card_band: Optional[str] = None
    model: Optional[str] = None
    backup: Optional[str] = None
    rule_path: Optional[Literal["table", "unsure-higher"]] = None
    score_band: str
    score_components: dict[str, Union[int, str]]
    rows_band: Optional[int] = None
    latency_ms: float = Field(default=0.0, ge=0)
    cost_usd: Optional[float] = None
    cost_source: Optional[str] = None
    status: CallStatus
    error: Optional[str] = None
    at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


__all__ = [
    "Answer",
    "CallRecord",
    "CallStatus",
    "Choice",
    "ModelEntry",
    "Noul",
    "Question",
    "QuestionSet",
    "RouteDecision",
    "Score",
    "TrialItem",
    "UNSURE",
    "Usage",
]
