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


# ---------------------------------------------------------------------
# F15 P2 — replay and corpus: pure reads (FINAL §5, §6)
# ---------------------------------------------------------------------
#
# REPLAY (§5, `[F-08]` as `[F-33]` / `[F-35]` / `[F-44]` amend it): every
# record, by `seq`, is recomputed against the RECORDED scorer — a record of
# another `scorer_version` is NOT REPLAYABLE, never re-graded with today's
# formula. A scan record (`create` / `refresh`) is recomputed through
# `replay_receipt` on its run's receipt chain (`ReplayError` caught, never
# aborting the command); a `tap` record from its own inputs. Numbers are
# compared as `Decimal` values (X7). The decision grade (R2-1 (c) B) and the
# ROW line are derived here and stored nowhere.
#
# CORPUS (§6, `[F-09]`): one row per card; realized R is `legs.realized_r`
# called on the card's current legs, its provisional flag used as returned
# (L3); the current `missed` row is read, never inferred.
#
# Nothing here writes, reads current settings or fetches market data: the
# only settings a replay uses are the ones its receipt or tap record holds.

_NUMERIC = ("proximity", "conviction")
_COMPARED = ("proximity", "conviction", "card_score", "score_suppressed", "proposed_key", "proposed_key_reason",
             "dots", "why")
_ROW_FIELDS = ("proximity", "conviction", "card_score", "score_suppressed", "proposed_key")
STATUSES = ("open", "provisional", "final", "awaiting nightly replay")


class ReplayRefused(ValueError):
    """A read that cannot be answered — refused loud, never guessed (L1)."""


class CardReads:
    """The ONE set of reads `replay` and `corpus` make, on the USER side.
    Every method is a SELECT; nothing is written and no lock is taken."""

    def __init__(self, store=None):
        if store is None:
            from .store import CardStore

            store = CardStore()
        self.store = store

    def _rows(self, sql: str, params) -> list[dict[str, Any]]:
        with self.store._connect() as conn:
            cur = conn.execute(sql, params)
            return [dict(zip([d.name for d in cur.description], r)) for r in cur.fetchall()]

    def card(self, card_id: int) -> dict[str, Any] | None:
        rows = self._rows(
            "SELECT id, ticker, direction, state, origin, radar_score_id, conviction, proximity, card_score, "
            "score_suppressed, proposed_key FROM aset_sizings WHERE id = %s", (card_id,),
        )
        return rows[0] if rows else None

    def records(self, card_id: int) -> list[dict[str, Any]]:
        return self._rows("SELECT * FROM prediction_records WHERE card_id = %s ORDER BY seq", (card_id,))

    def transitions(self, card_id: int) -> list[tuple[int, str | None, str]]:
        return [(r["id"], r["from_state"], r["to_state"]) for r in self._rows(
            "SELECT id, from_state, to_state FROM card_transitions WHERE card_id = %s ORDER BY id", (card_id,))]

    def score_run(self, radar_score_id: int) -> int | None:
        rows = self._rows("SELECT run_id FROM system.radar_score WHERE id = %s", (radar_score_id,))
        return int(rows[0]["run_id"]) if rows and rows[0]["run_id"] is not None else None

    def receipt_chain(self, run_id: int) -> list[dict[str, Any]] | None:
        receipt_id = self.store.receipt_for_run(run_id)
        return None if receipt_id is None else self.store.receipts_chain(receipt_id)

    def current_legs(self, card_id: int) -> list[dict[str, Any]]:
        return self._rows("SELECT * FROM legs_current_v WHERE card_id = %s ORDER BY seq", (card_id,))

    def missed(self, card_id: int) -> list[dict[str, Any]]:
        return self._rows(
            "SELECT cf_r, mfe_r, excluded_by FROM missed WHERE card_id = %s AND kind = 'card' AND is_current "
            "ORDER BY id", (card_id,),
        )

    def pick(self, card_id: int) -> dict[str, Any] | None:
        rows = self._rows(
            "SELECT id, transition_id, pool_basis, pool_rank, pool_size, rank_metric, rank_value, card_score, "
            "card_score_rank, focus_top4, score_basis FROM picks WHERE card_id = %s", (card_id,),
        )
        return rows[0] if rows else None

    def corpus_card_ids(self, since) -> list[int]:
        return [r["id"] for r in self._rows(
            "SELECT s.id FROM aset_sizings s WHERE EXISTS (SELECT 1 FROM prediction_records p "
            "WHERE p.card_id = s.id) AND (%s::date IS NULL OR "
            "(s.created_at AT TIME ZONE 'America/New_York')::date >= %s::date) ORDER BY s.id",
            (since, since),
        )]


def _dec(value: Any) -> Decimal | None:
    return None if value is None else Decimal(str(value))


def _text(value: Any) -> str | None:
    return None if value is None else str(value)


def decision_seq(records, transitions) -> int | None:
    """R2-1 (c) B, his R145: the last record, by `seq`, whose
    `transition_id` is below the id of the card's first `card_transitions`
    row with `from_state = 'WATCH'`; None while the card has no such row.
    Never derived from `at` or a state column."""
    leaves = [t[0] for t in transitions if t[1] == "WATCH"]
    if not leaves:
        return None
    first_leave = min(leaves)
    below = [r["seq"] for r in records if r["transition_id"] < first_leave]
    return max(below) if below else None


#: `card_dots.engine_value NUMERIC(18, 6)` (`0007_radar_cards.sql:127`): a
#: refresh record's dots are re-read from that column (`[F-32]`), so an
#: engine value is compared at the scale a record can hold.
_ENGINE_VALUE_SCALE = Decimal("0.000001")


def _engine_value(value: Any) -> Decimal | None:
    from decimal import ROUND_HALF_UP

    return None if value is None else Decimal(str(value)).quantize(_ENGINE_VALUE_SCALE, rounding=ROUND_HALF_UP)


def _dots_diff(stored: list, recomputed: list) -> bool:
    """True when the dots differ: the same factors, and every field the
    recompute carries equal (numbers as Decimal; an engine value at its
    column's scale)."""
    have = {d["factor"]: d for d in stored or []}
    want = {d["factor"]: d for d in recomputed or []}
    if set(have) != set(want):
        return True
    for factor, dot in want.items():
        for key, value in dot.items():
            got = have[factor].get(key)
            if key == "engine_value":
                if _engine_value(got) != _engine_value(value):
                    return True
            elif got != value:
                return True
    return False


def output_diff(stored: Mapping[str, Any], stored_why: str | None, recomputed: Mapping[str, Any]) -> list[str]:
    """The field names where `recomputed` differs from the stored `output`
    (and `why`, when the stored one is given): numbers as Decimal values
    (X7), never strings."""
    diff = []
    for key in _COMPARED:
        if key == "why":
            if stored_why is not None and grade_why(recomputed) != stored_why:
                diff.append(key)
        elif key == "dots":
            if _dots_diff(stored.get("dots"), recomputed.get("dots")):
                diff.append(key)
        elif key in _NUMERIC:
            if _dec(stored.get(key)) != _dec(recomputed.get(key)):
                diff.append(key)
        elif stored.get(key) != recomputed.get(key):
            diff.append(key)
    return diff


def recompute_tap(inputs: Mapping[str, Any]) -> dict[str, Any]:
    """A tap record from its own inputs (`[F-08]` tap line): the locked
    dots → conviction → the NULL-proximity branch (the stored sentence,
    else `PROXIMITY_UNKNOWN`) or `suppression(dots)` → `card_score` →
    `proposed_key(conviction, bands, enabled)`. The dots carry what the
    inputs hold; `engine_value` is no input of the tap's grade."""
    from cobalt.aset.models import Grade
    from cobalt.settings.card import ProposedKeyBands

    from .scoring import PROXIMITY_UNKNOWN, Dot, card_score, conviction, proposed_key, suppression

    shape = TapInputs.model_validate(inputs)
    dots = [Dot.model_construct(factor=d.factor, source=d.source, tier=d.tier, na_reason=d.na_reason,
                                engine_grade=d.engine_grade, trader_grade=d.trader_grade) for d in shape.dots]
    conv = conviction(dots)
    prox = shape.proximity
    if prox is None:
        suppressed = shape.score_suppressed_before if shape.score_suppressed_before is not None else PROXIMITY_UNKNOWN
    else:
        suppressed = suppression(dots)
    bands = None if shape.bands is None else ProposedKeyBands(**shape.bands.model_dump())
    key, reason = proposed_key(conv, bands, [Grade(g) for g in shape.enabled])
    return {
        "proximity": _text(prox), "conviction": _text(conv), "card_score": card_score(conv, prox, suppressed),
        "score_suppressed": suppressed, "proposed_key": key.value if key else None, "proposed_key_reason": reason,
        "dots": [{"factor": d.factor, "engine_grade": d.engine_grade, "na_reason": d.na_reason,
                  "trader_grade": d.trader_grade} for d in shape.dots],
    }


def scan_recompute(inputs: Mapping[str, Any], *, replayed: Mapping[str, Any], published: Mapping[str, Any],
                   bands, enabled, preceding_output: Mapping[str, Any] | None) -> dict[str, Any]:
    """A `create` / `refresh` record from its receipt's recompute of the
    card (`replayed`, `published_numbers` keys).

    Not taps-moved: the recompute, plus `proposed_key_reason` from
    `proposed_key(conviction, bands, enabled)` with the RECEIPT's settings.
    Taps-moved (`[F-08]`, `[F-44]`): the output as the store wrote it —
    proximity and the dots' engine fields from the recompute, each dot's
    `trader_grade` from the preceding record's `output.dots`; conviction and
    proposed key the locked ones (not recomputed, reason None);
    `score_suppressed` the receipt's published one when proximity is None,
    else the locked one; `card_score` from those."""
    from .scoring import card_score, proposed_key

    shape = ScanInputs.model_validate(inputs)
    if not shape.taps_moved:
        _key, reason = proposed_key(_dec(replayed.get("conviction")), bands, list(enabled))
        return {**replayed, "proposed_key_reason": reason}
    locked = shape.locked
    if locked is None:
        raise ReplayRefused("a taps-moved refresh record holds no locked numbers")
    if preceding_output is None:
        raise ReplayRefused("a taps-moved refresh record has no preceding record to take its trader grades from")
    proximity = replayed.get("proximity")
    suppressed = published.get("score_suppressed") if proximity is None else locked.score_suppressed
    grades = {d["factor"]: d.get("trader_grade") for d in preceding_output.get("dots") or []}
    return {
        "proximity": proximity, "conviction": _text(locked.conviction),
        "card_score": card_score(locked.conviction, _dec(proximity), suppressed),
        "score_suppressed": suppressed, "proposed_key": locked.proposed_key, "proposed_key_reason": None,
        "dots": [{**d, "trader_grade": grades.get(d["factor"])} for d in replayed.get("dots") or []],
    }


class RecordReplay(_Strict):
    """One record's replay (`[F-44]` record object)."""

    seq: int
    id: int
    kind: RecordKind
    at: datetime
    run_id: int | None
    transition_id: int
    scorer_version: str
    formula_sha256: str
    inputs: dict[str, Any]
    output: dict[str, Any]
    recomputed: dict[str, Any] | None
    verdict: Literal["MATCH", "DIFF", "NOT_REPLAYABLE"]
    reason: str | None
    diff: list[str]
    formula_changed: bool = False


class RowCheck(_Strict):
    """The card row's current numbers against the last record by `seq`."""

    verdict: Literal["MATCH", "DIFF"] | None
    record_seq: int | None
    diff: list[str]


class CorpusRow(_Strict):
    """One card of the ONE read (`[F-09]`, FINAL §6)."""

    card_id: int
    ticker: str
    direction: str | None
    origin: str | None
    state: str
    records: int
    decision_seq: int | None
    final_seq: int | None
    realized_r: str | None
    realized_r_reason: str | None
    realized_provisional: bool
    realized_function: str
    missed: dict[str, Any] | None
    pick: dict[str, Any] | None
    outcome_status: Literal["open", "provisional", "final", "awaiting nightly replay"]


class ReplayReport(_Strict):
    card_id: int
    card: dict[str, Any]
    records: list[RecordReplay]
    decision_seq: int | None
    decision_to_state: str | None
    row: RowCheck
    outcome: CorpusRow | None
    no_records_line: str | None
    exit: Literal[0, 1, 2]

    def as_json(self) -> dict[str, Any]:
        """The ONE object of `[F-44]` (R2-5 (5))."""
        return {
            "card_id": self.card_id,
            "records": [{
                "seq": r.seq, "id": r.id, "kind": r.kind, "at": r.at.isoformat(), "run_id": r.run_id,
                "transition_id": r.transition_id, "scorer_version": r.scorer_version,
                "formula_sha256": r.formula_sha256, "inputs": r.inputs, "output": r.output,
                "recomputed": r.recomputed, "verdict": r.verdict, "reason": r.reason, "diff": r.diff,
            } for r in self.records],
            "row": self.row.model_dump(mode="json"),
            "outcome": None if self.outcome is None else self.outcome.model_dump(mode="json"),
            "exit": self.exit,
        }


def _replay_record(record: Mapping[str, Any], *, reads, clock, preceding: Mapping[str, Any] | None) -> RecordReplay:
    from cobalt.aset.models import Grade
    from cobalt.radar.evaluate import EVALUATOR_VERSION, ReplayError, _resolve_snapshot, formula_sha256, replay_receipt
    from cobalt.settings.card import CardSettings

    base = dict(
        seq=record["seq"], id=record["id"], kind=record["kind"], at=record["at"], run_id=record["run_id"],
        transition_id=record["transition_id"], scorer_version=record["scorer_version"],
        formula_sha256=record["formula_sha256"], inputs=record["inputs"], output=record["output"],
    )

    def not_replayable(reason: str) -> RecordReplay:
        return RecordReplay(**base, recomputed=None, verdict="NOT_REPLAYABLE", reason=reason, diff=[])

    if record["scorer_version"] != EVALUATOR_VERSION:
        return not_replayable(f"recorded scorer {record['scorer_version']}, this code {EVALUATOR_VERSION}; "
                              "replay from the deploy that wrote it")
    if record["kind"] == "tap":
        recomputed = recompute_tap(record["inputs"])
    else:
        chain = reads.receipt_chain(record["run_id"])
        if chain is None:
            return not_replayable(f"run {record['run_id']} has no receipt: it failed after this card was written (L57)")
        try:
            _evaluations, cards = replay_receipt(chain, clock=clock)
            settings_raw = _resolve_snapshot(chain, "settings_snapshot", len(chain) - 1)
        except ReplayError as e:
            return not_replayable(f"run {record['run_id']}: its receipt does not replay — {e}")
        mine = [c for c in cards if c.card_id == record["card_id"]]
        if not mine:
            return not_replayable(f"run {record['run_id']}: its receipt holds no slice of card {record['card_id']}")
        try:
            recomputed = scan_recompute(
                record["inputs"], replayed=mine[0].recomputed, published=mine[0].published,
                bands=CardSettings.from_rows(settings_raw["card"]).proposed_key,
                enabled=[Grade(g) for g in settings_raw["enabled_grades_today"]],
                preceding_output=None if preceding is None else preceding["output"],
            )
        except ReplayRefused as e:
            return not_replayable(str(e))
    diff = output_diff(record["output"], record["why"], recomputed)
    return RecordReplay(**base, recomputed=recomputed, verdict="DIFF" if diff else "MATCH", reason=None, diff=diff,
                        formula_changed=record["formula_sha256"] != formula_sha256())


def _row_check(card: Mapping[str, Any], last: Mapping[str, Any] | None) -> RowCheck:
    if last is None:
        return RowCheck(verdict=None, record_seq=None, diff=[])
    out = last["output"]
    diff = [k for k in _ROW_FIELDS
            if (_dec(card.get(k)) != _dec(out.get(k)) if k in _NUMERIC else card.get(k) != out.get(k))]
    return RowCheck(verdict="DIFF" if diff else "MATCH", record_seq=last["seq"], diff=diff)


def replay(card_id: int, *, reads=None, clock=None) -> ReplayReport:
    """`cobalt cards replay <card_id>` (FINAL §5). Exit 0 only when every
    record MATCHes and ROW matches; 1 when any record DIFFs or ROW does
    not match; 2 when nothing differs and something is NOT REPLAYABLE —
    a record, a pre-F15 card, a manual card."""
    if reads is None:
        reads = CardReads()
    if clock is None:
        from cobalt.session import session_clock

        clock = session_clock()
    card = reads.card(card_id)
    if card is None:
        raise ReplayRefused(f"no card {card_id}")
    records = sorted(reads.records(card_id), key=lambda r: r["seq"])
    transitions = reads.transitions(card_id)
    (outcome,) = corpus(None, card_id=card_id, reads=reads)
    no_records = None
    if card["origin"] != "radar":
        no_records = "manual card: the key is the trader's; there is no derived grade"
    elif not records:
        run_id = None if card["radar_score_id"] is None else reads.score_run(card["radar_score_id"])
        export = (f"cobalt radar audit-export --run {run_id}" if run_id is not None
                  else "cobalt radar audit-export --run: none — the card names no radar_score run")
        no_records = f"NO PREDICTION RECORDS — graded before F15 lands\n{export}"
    replayed: list[RecordReplay] = []
    for i, record in enumerate(records):
        replayed.append(_replay_record(record, reads=reads, clock=clock, preceding=records[i - 1] if i else None))
    row = _row_check(card, records[-1] if records and card["origin"] == "radar" else None)
    chosen = decision_seq(records, transitions)
    leaves = sorted(t for t in transitions if t[1] == "WATCH")
    if any(r.verdict == "DIFF" for r in replayed) or row.verdict == "DIFF":
        code = 1
    elif no_records is not None or any(r.verdict == "NOT_REPLAYABLE" for r in replayed):
        code = 2
    else:
        code = 0
    return ReplayReport(
        card_id=card_id, card=card, records=replayed, decision_seq=chosen,
        decision_to_state=leaves[0][2] if leaves else None, row=row, outcome=outcome, no_records_line=no_records,
        exit=code,
    )


def _figure(value: Any) -> str:
    return "—" if value is None else str(value)


def _outcome_text(row: CorpusRow) -> str:
    if row.realized_r is None:
        realized = f"realized R {row.realized_r_reason}"
    else:
        realized = (f"realized R {Decimal(row.realized_r).quantize(Decimal('0.01')):+} "
                    f"{'provisional' if row.realized_provisional else 'final'}")
    if row.missed is not None:
        missed = (f"missed: cf_r {_figure(row.missed['cf_r'])} · mfe_r {_figure(row.missed['mfe_r'])} · "
                  f"excluded_by {row.missed['excluded_by']}")
    elif row.outcome_status == "awaiting nightly replay":
        missed = "missed: awaiting nightly replay"
    else:
        missed = "missed: no current row"
    pick = "pick: none" if row.pick is None else f"pick: #{row.pick.get('id')}"
    return f"{row.state} · {row.outcome_status} · {realized} [{row.realized_function}] · {missed} · {pick}"


def render_replay(report: ReplayReport) -> str:
    from cobalt.session.clock import ET

    card = report.card
    versions = sorted({r.scorer_version for r in report.records}) or ["—"]
    lines = [f"card {report.card_id} {card['ticker']} {card['direction']} · {card['origin']} · {card['state']} · "
             f"scorer {SCORER_ID} {', '.join(versions)} · {len(report.records)} records"]
    if report.no_records_line is not None:
        lines.extend(report.no_records_line.splitlines())
    for r in report.records:
        head = f"#{r.seq:<3} {r.kind:<8} {r.at.astimezone(ET):%H:%M:%S}  "
        if r.verdict == "NOT_REPLAYABLE":
            body = f"NOT REPLAYABLE — {r.reason}"
        elif r.verdict == "DIFF":
            body = "DIFF " + "; ".join(
                f"{k} recorded {_figure(r.output.get(k))} → replayed {_figure(r.recomputed.get(k))}"
                if k not in ("dots", "why") else k for k in r.diff)
        else:
            body = "MATCH"
        mark = (f"            ← decision grade (last record before {report.decision_to_state})"
                if r.seq == report.decision_seq else "")
        lines.append(head + body + mark)
    if report.records and report.decision_seq is None:
        lines.append("decision grade: none — the card is still WATCH" if report.decision_to_state is None
                     else "decision grade: none — no record before the card left WATCH")
    changed = [r.seq for r in report.records if r.formula_changed]
    if changed:
        lines.append(f"NOTE formula source changed since record #{changed[0]}; replayed with current code")
    if report.row.verdict == "MATCH":
        lines.append(f"ROW: matches record #{report.row.record_seq}")
    elif report.row.verdict == "DIFF":
        lines.append(f"ROW: holds numbers no record stores (record #{report.row.record_seq} differs: "
                     f"{', '.join(report.row.diff)})")
    if report.outcome is not None:
        lines.append(f"OUTCOME: {_outcome_text(report.outcome)}")
    counts = {v: sum(1 for r in report.records if r.verdict == v) for v in ("MATCH", "DIFF", "NOT_REPLAYABLE")}
    lines.append(f"card {report.card_id}: {len(report.records)} records · {counts['MATCH']} match · "
                 f"{counts['DIFF']} differ · {counts['NOT_REPLAYABLE']} not replayable")
    return "\n".join(lines)


def outcome_status(state: str, realized, missed: dict[str, Any] | None) -> str:
    """`[F-09]`: CLOSED → final or provisional solely from `realized_r`; a
    card not terminal → open; EXPIRED / PASSED / MISSED → final only when
    its current `missed` row exists, else `awaiting nightly replay` (the
    absence of a row is never a miss of none)."""
    from .models import TERMINAL, CardState

    card_state = CardState(state)
    if card_state is CardState.CLOSED:
        return "provisional" if realized.provisional else "final"
    if card_state not in TERMINAL:
        return "open"
    return "final" if missed is not None else "awaiting nightly replay"


def _plain(row: Mapping[str, Any] | None) -> dict[str, Any] | None:
    if row is None:
        return None
    return {k: (str(v) if isinstance(v, Decimal) else v) for k, v in row.items()}


def corpus(since=None, *, card_id: int | None = None, reads=None) -> list[CorpusRow]:
    """THE ONE READ (FINAL §6): one row per card with prediction records
    (created on or after `since`, ET), or the one `card_id` asked for."""
    from .legs import realized_r

    if reads is None:
        reads = CardReads()
    ids = [card_id] if card_id is not None else reads.corpus_card_ids(since)
    rows = []
    for cid in ids:
        card = reads.card(cid)
        if card is None:
            raise ReplayRefused(f"no card {cid}")
        records = sorted(reads.records(cid), key=lambda r: r["seq"])
        realized = realized_r(card, reads.current_legs(cid))
        current = reads.missed(cid)
        if len(current) > 1:
            raise ReplayRefused(f"card {cid} has {len(current)} current missed rows — expected at most one")
        missed = _plain(current[0]) if current else None
        rows.append(CorpusRow(
            card_id=cid, ticker=card["ticker"], direction=card["direction"], origin=card["origin"],
            state=card["state"], records=len(records), decision_seq=decision_seq(records, reads.transitions(cid)),
            final_seq=records[-1]["seq"] if records else None, realized_r=_text(realized.value),
            realized_r_reason=realized.reason, realized_provisional=realized.provisional,
            realized_function=realized.function_id, missed=missed, pick=_plain(reads.pick(cid)),
            outcome_status=outcome_status(card["state"], realized, missed),
        ))
    return rows


def status_counts(rows: list[CorpusRow]) -> dict[str, int]:
    return {status: sum(1 for r in rows if r.outcome_status == status) for status in STATUSES}


def render_corpus(rows: list[CorpusRow]) -> str:
    """n per status first (L8), then every row. No EV, no aggregate."""
    counts = status_counts(rows)
    lines = [f"corpus: n={len(rows)} · " + " · ".join(f"{s} {counts[s]}" for s in STATUSES)]
    for r in rows:
        lines.append(f"card {r.card_id} {r.ticker} {r.direction} · records {r.records} · decision "
                     f"{'#' + str(r.decision_seq) if r.decision_seq is not None else 'none'} · final "
                     f"{'#' + str(r.final_seq) if r.final_seq is not None else 'none'} · {_outcome_text(r)}")
    return "\n".join(lines)


__all__ = [
    "Bands", "CardReads", "CorpusRow", "LockedNumbers", "OutputDot", "PredictionRecord", "RecordInputs",
    "RecordKind", "RecordOutput", "RecordReplay", "ReplayRefused", "ReplayReport", "RowCheck", "SCORER_ID",
    "STATUSES", "ScanInputs", "TapDot", "TapInputs", "corpus", "decision_seq", "outcome_status", "output_diff",
    "recompute_tap", "render_corpus", "render_replay", "replay", "scan_recompute", "status_counts", "write_record",
]
