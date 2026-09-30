"""F15 P1 — the prediction record: its shapes and its ONE writer (L3, L10).

`"user".prediction_records` (`db_migrations/0022_prediction_records.sql`,
FINAL §3 `[F-40]`) holds one append-only row per grade write on a radar
card: the card's creation, every scan's refresh, every dot tap. The row is
written INSIDE the transaction that writes the card-row numbers it
describes (`[F-32]`), by `write_record` and nothing else — the only
`INSERT INTO prediction_records` in `src/`.

THE SHAPES (validated before the INSERT, so a bad input raises and nothing
is written):

* `RecordInputs` — one shape per kind (FINAL §3 `inputs` by kind, as
  `[F-05]` and `[F-32]` amend it):
  - `create` / `refresh`: `{taps_moved, locked}`; `locked` is the
    `{conviction, score_suppressed, proposed_key}` read under the row lock
    when a tap landed after the stage read the card, else null. The card's
    slice (entry, stop, definition, taps) is its run's receipt's, never
    copied (`[F-32]`).
  - `tap`: `{tap_id, dots, proximity, score_suppressed_before, bands,
    enabled}` — self-contained, no receipt needed.
* `RecordOutput` — `published_numbers(...)`'s keys plus
  `proposed_key_reason`; numbers are the strings `published_numbers` writes
  (`radar/evaluate.py`), so replay compares like with like (X7, X10).
* `PredictionRecord` — every `[F-40]` column but `id` and `user_id`; the
  sibling model that validates both sha256 fields as 64 lowercase hex (as
  `cards/radar.py` validates the card's) and the kind / run rule.

ORDER AND DECISION GRADE. `seq` is 1 + the card's max `seq` and
`transition_id` the card's max `card_transitions.id`, both read inside the
CALLER's row lock (`[F-33]`; R2-1 (c) B, his R145): every record writer
holds the card's `FOR UPDATE` lock, and `transition()` takes the same lock
before it inserts, so both rise in commit order (X12). Records observe
`card_score`; nothing here ranks or feeds a ranking (L7, L52 (b)).
"""

from __future__ import annotations

import json
from datetime import datetime
from decimal import Decimal
from typing import Any, Literal, Mapping

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field, model_validator

from .scoring import grade_why

RecordKind = Literal["create", "refresh", "tap"]
SCORER_ID = "card_grade"
SHA256 = r"^[0-9a-f]{64}$"


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class LockedNumbers(_Strict):
    """What the refresh's lock SELECT read on a taps-moved scan (`[F-05]`)."""

    conviction: Decimal | None
    score_suppressed: str | None
    proposed_key: str | None


class ScanInputs(_Strict):
    """`create` / `refresh` inputs (`[F-32]` last paragraph)."""

    taps_moved: bool
    locked: LockedNumbers | None


class TapDot(_Strict):
    factor: str = Field(min_length=1)
    source: str
    tier: str
    na_reason: str | None
    engine_grade: int | None
    trader_grade: int | None


class Bands(_Strict):
    """`settings.proposed_key` as the tap used it (`[F-05]`)."""

    a_plus_min: Decimal
    a_min: Decimal
    b_min: Decimal
    c_min: Decimal


class TapInputs(_Strict):
    """`tap` inputs (FINAL §3): the locked dots after the trader-grade
    update, the stored proximity and reason, the bands and enabled keys."""

    tap_id: int
    dots: list[TapDot]
    proximity: Decimal | None
    score_suppressed_before: str | None
    bands: Bands | None
    enabled: list[str]


_INPUTS: dict[str, type[_Strict]] = {"create": ScanInputs, "refresh": ScanInputs, "tap": TapInputs}


class RecordInputs(_Strict):
    """A record's `inputs`, validated against the ONE shape of its kind."""

    kind: RecordKind
    inputs: ScanInputs | TapInputs

    @model_validator(mode="before")
    @classmethod
    def _shape_of_kind(cls, data: Any) -> Any:
        if isinstance(data, Mapping) and data.get("kind") in _INPUTS:
            shape = _INPUTS[data["kind"]]
            raw = data.get("inputs")
            if not isinstance(raw, shape):
                raw = shape.model_validate(raw)
            return {**data, "inputs": raw}
        return data


class OutputDot(_Strict):
    factor: str
    engine_value: str | None
    engine_grade: int | None
    na_reason: str | None
    trader_grade: int | None


class RecordOutput(_Strict):
    """`published_numbers(...)` (`radar/evaluate.py`) + `proposed_key_reason`."""

    proximity: str | None
    conviction: str | None
    card_score: int | None
    score_suppressed: str | None
    proposed_key: str | None
    proposed_key_reason: str | None
    dots: list[OutputDot]


class PredictionRecord(_Strict):
    """One `"user".prediction_records` row, every `[F-40]` column but `id`
    and `user_id` — the seam P2 reads (L72)."""

    card_id: int
    seq: int = Field(ge=1)
    transition_id: int
    kind: RecordKind
    at: AwareDatetime
    scorer_id: Literal["card_grade"]
    scorer_version: str = Field(min_length=1)
    formula_sha256: str = Field(pattern=SHA256)
    settings_sha256: str = Field(pattern=SHA256)
    run_id: int | None
    inputs: ScanInputs | TapInputs
    output: RecordOutput
    why: str = Field(min_length=1)

    @model_validator(mode="before")
    @classmethod
    def _inputs_of_kind(cls, data: Any) -> Any:
        if isinstance(data, Mapping) and data.get("kind") in _INPUTS:
            return {**data, "inputs": RecordInputs.model_validate({"kind": data["kind"],
                                                                   "inputs": data.get("inputs")}).inputs}
        return data

    @model_validator(mode="after")
    def _run_by_kind(self) -> PredictionRecord:
        if (self.kind == "tap") != (self.run_id is None):
            raise ValueError(f"a {self.kind} record {'carries no' if self.kind == 'tap' else 'names its'} run: "
                             f"run_id {self.run_id!r}")
        return self


def write_record(
    conn,
    *,
    card_id: int,
    kind: RecordKind,
    at: datetime,
    run_id: int | None,
    scorer_version: str,
    formula_sha256: str,
    settings_sha256: str,
    inputs: Mapping[str, Any],
    output: Mapping[str, Any],
) -> int:
    """Append one record on the CALLER's open transaction and return its id.

    The caller holds the card's row lock (`SELECT … FOR UPDATE`, or the row
    it just inserted); this function never opens, commits or rolls back.
    Everything is validated before the INSERT, so a bad input raises and
    nothing is written (L10). `seq` and `transition_id` are read here,
    under that lock (`[F-33]`, R2-1 (c)); `why` is `grade_why(output)`."""
    shape = RecordInputs.model_validate({"kind": kind, "inputs": inputs})
    numbers = RecordOutput.model_validate(output)
    seq = conn.execute(
        "SELECT COALESCE(MAX(seq), 0) + 1 FROM prediction_records WHERE card_id = %s", (card_id,)
    ).fetchone()[0]
    transition_id = conn.execute(
        "SELECT max(id) FROM card_transitions WHERE card_id = %s", (card_id,)
    ).fetchone()[0]
    if transition_id is None:
        raise ValueError(f"card {card_id} has no card_transitions row — no record without a state (F7)")
    out = numbers.model_dump(mode="json")
    record = PredictionRecord(
        card_id=card_id, seq=int(seq), transition_id=int(transition_id), kind=kind, at=at, scorer_id=SCORER_ID,
        scorer_version=scorer_version, formula_sha256=formula_sha256, settings_sha256=settings_sha256,
        run_id=run_id, inputs=shape.inputs, output=numbers, why=grade_why(out),
    )
    row = conn.execute(
        "INSERT INTO prediction_records (card_id, seq, transition_id, kind, at, scorer_id, scorer_version, "
        "formula_sha256, settings_sha256, run_id, inputs, output, why) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s::jsonb, %s::jsonb, %s) RETURNING id",
        (
            record.card_id, record.seq, record.transition_id, record.kind, record.at, record.scorer_id,
            record.scorer_version, record.formula_sha256, record.settings_sha256, record.run_id,
            json.dumps(record.inputs.model_dump(mode="json")), json.dumps(out), record.why,
        ),
    ).fetchone()
    return int(row[0])


__all__ = [
    "Bands", "LockedNumbers", "OutputDot", "PredictionRecord", "RecordInputs", "RecordKind", "RecordOutput",
    "SCORER_ID", "ScanInputs", "TapDot", "TapInputs", "write_record",
]
