"""The shapes `cobalt smoke` loads and renders (S2-P4 STEP-9, R6).

A suite file (`configs/cobalt/smoke/<suite>.yaml`) is one `SmokeSuite`: an
ordered list of checks, each one of eight kinds, discriminated on `kind`
(L10: a Pydantic schema per config family, validated on load). Every
check kind is READ-ONLY by construction, and the schema is where that is
enforced first:

    sql       — the statement must pass `cobalt db query`'s own guard
    job_row   — reads one `cobalt_jobs` row through that same read path
    cli       — argv must start with a prefix in `READ_ONLY_CLI`
    log_grep  — a repo-relative path, never `..`
    http      — a GET
    launchctl — `launchctl print` / `launchctl list`
    vault_unit — a marker read over the note's text
    compare   — reads nothing: two checks' already-collected numbers

`compare` exists because of the tenancy wall (L32). An assertion that
spans both sides — "the corpus has as many card rows as the job that
wrote them says it wrote" — cannot be one statement, because no role may
read both `system.cobalt_jobs` and `"user".missed`. So each side is asked
by its own check, each names THE number of its result (`result_number`),
and a `compare` row asserts the equality between them. Everything it
needs is validated at load: an operand that is not a check ABOVE it, or
one that names no number, crashes the file with its line (L1/L10) rather
than producing a row that could never run.

The verdict vocabulary and the OVERALL roll-up are day-open's
(`cobalt.dayopen.models`), not a second copy (L3).
"""

from __future__ import annotations

import re
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Annotated, Any, Literal, Optional, Union

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

from cobalt.dayopen.models import Overall, Verdict, overall_verdict
from cobalt.db_query import QueryRefused, guard_select

#: The variables a suite may name. `{tunable:<key>}` is the one
#: parameterised form. Values are computed by `checks.build_context`.
VARIABLES = frozenset({
    "now", "report_date", "session", "cutoff", "last_trading_day",
    "last_summary_slot", "last_summary_date",
})
VAR_RE = re.compile(r"\{([a-z_]+)(?::([A-Za-z0-9_.]+))?\}")

#: argv prefixes a `cli` check may run. Only commands that neither write a
#: row, a file nor a vault note, nor run DDL: `cobalt validate` reads config.
#: (`cobalt jobs check` and `cobalt heartbeat show` sweep and stamp job rows;
#: `cobalt cards picks` runs `ensure_schema` — none of them is on this list.)
READ_ONLY_CLI: tuple[tuple[str, ...], ...] = (("cobalt", "validate"),)

CHECK_ID = r"^K\d+(\.\d+)?$"

#: A `result_number`: a column name for `sql`, a dotted `last_result` path
#: for `job_row`. Lower-case identifiers joined by dots — the same shape
#: `result_equals` already uses, so one file reads one way.
RESULT_NUMBER = r"^[a-z_][a-z0-9_]*(\.[a-z_][a-z0-9_]*)*$"


def variables_in(text: str) -> list[str]:
    """Every `{name}` / `{tunable:key}` in `text`; raises on an unknown name."""
    found = []
    for match in VAR_RE.finditer(text):
        name, arg = match.group(1), match.group(2)
        if name == "tunable":
            if not arg:
                raise ValueError("`{tunable:<key>}` needs a key")
        elif arg is not None or name not in VARIABLES:
            raise ValueError(
                f"unknown variable {match.group(0)!r} — known: "
                f"{', '.join(sorted(VARIABLES))}, tunable:<key>"
            )
        found.append(match.group(0))
    return found


class CompareOp(str, Enum):
    """The operators a `compare` row may use between two numbers.

    One member on purpose: `eq` is the assertion the K8 split lost, and an
    operator nothing asserts is an untested branch. Adding one is adding
    its test (desk ruling, row 4).
    """

    EQ = "eq"


class Op(str, Enum):
    EQ = "eq"
    NE = "ne"
    LT = "lt"
    LE = "le"
    GT = "gt"
    GE = "ge"
    IN = "in"
    NOT_IN = "not_in"
    IS_NULL = "is_null"
    NOT_NULL = "not_null"


class Predicate(BaseModel):
    """One comparison over a column of the check's single row.

    `value` may be a literal or a `{variable}` string. `known` lists actual
    values that make a FAILING predicate KNOWN instead of FAIL — each entry
    exists only by ruling, so every committed list starts empty.
    """

    model_config = ConfigDict(extra="forbid", frozen=True)

    column: str = Field(min_length=1)
    op: Op
    value: Any = None
    known: list[Any] = Field(default_factory=list)

    @model_validator(mode="after")
    def _value_shape(self) -> "Predicate":
        if self.op in (Op.IS_NULL, Op.NOT_NULL):
            if self.value is not None:
                raise ValueError(f"op {self.op.value} takes no value")
        elif self.op in (Op.IN, Op.NOT_IN):
            if not isinstance(self.value, list):
                raise ValueError(f"op {self.op.value} needs a list value")
        elif self.value is None:
            raise ValueError(f"op {self.op.value} needs a value (use is_null for NULL)")
        if isinstance(self.value, str):
            variables_in(self.value)
        return self


class _Check(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    id: str = Field(pattern=CHECK_ID)
    title: str = Field(min_length=1)
    #: The exact expected output, printed beside the command (Astra R1-24).
    expect_text: str = Field(min_length=1)


class LaunchctlCheck(_Check):
    kind: Literal["launchctl"]
    #: `running`: one label, `state = running` with a pid.
    #: `registry_match`: every enabled jobs.yaml label loaded, no disabled one.
    mode: Literal["running", "registry_match"]
    label: Optional[str] = None

    @model_validator(mode="after")
    def _label(self) -> "LaunchctlCheck":
        if (self.mode == "running") != (self.label is not None):
            raise ValueError("`label` is required for mode running and forbidden for registry_match")
        return self


class SqlCheck(_Check):
    kind: Literal["sql"]
    side: Literal["system", "user"]
    query: str = Field(min_length=1)
    expect: list[Predicate] = Field(min_length=1)
    known_if: list[Predicate] = Field(default_factory=list)
    known_text: Optional[str] = None
    #: Checked first with `to_regclass`; absent -> FAIL naming it.
    requires_relation: Optional[str] = Field(default=None, pattern=r"^[a-z_]+\.[a-z_]+$")
    #: OPTIONAL and additive: the column of the returned row that IS this
    #: check's number, for a `compare` row to read. It grades nothing here
    #: — `expect` still owns this check's own verdict.
    result_number: Optional[str] = Field(default=None, pattern=RESULT_NUMBER)

    @field_validator("query")
    @classmethod
    def _read_only(cls, value: str) -> str:
        variables_in(value)
        try:
            guard_select(value)
        except QueryRefused as e:
            raise ValueError(f"not a read-only statement (refused token: {e})") from e
        return value

    @model_validator(mode="after")
    def _known_text(self) -> "SqlCheck":
        if bool(self.known_if) != bool(self.known_text):
            raise ValueError("`known_if` and `known_text` go together")
        return self


class HttpCheck(_Check):
    kind: Literal["http"]
    url: str = Field(pattern=r"^https?://")
    status: int = 200
    contains: list[str] = Field(default_factory=list)


class LogGrepCheck(_Check):
    kind: Literal["log_grep"]
    #: Repo-relative (the production checkout's `logs/`).
    path: str = Field(min_length=1)
    #: When set, only the text from the LAST line matching this regex on.
    block_start: Optional[str] = None
    #: POSIX ERE-compatible, so the printed `grep -E` runs the same pattern.
    pattern: str = Field(min_length=1)
    present: bool = True

    @field_validator("path")
    @classmethod
    def _relative(cls, value: str) -> str:
        if value.startswith("/") or ".." in value.split("/"):
            raise ValueError(f"log path {value!r} must be repo-relative with no '..'")
        return value

    @field_validator("pattern", "block_start")
    @classmethod
    def _compiles(cls, value: Optional[str]) -> Optional[str]:
        if value is not None:
            re.compile(value)
        return value


class JobRowCheck(_Check):
    kind: Literal["job_row"]
    label: str = Field(pattern=r"^com\.cobalt\.[a-z0-9-]+$")
    state: Optional[Literal["pending", "running", "done", "failed", "zombie"]] = None
    exit_code: Optional[int] = None
    #: `cobalt.jobs.watchdog.is_missed` against the registry's schedule.
    not_missed: bool = False
    #: `updated_at` no older than this.
    max_age_min: Optional[int] = Field(default=None, gt=0)
    result_keys: list[str] = Field(default_factory=list)
    #: dotted path in `last_result` -> expected (literal or `{variable}`).
    result_equals: dict[str, Any] = Field(default_factory=dict)
    #: keys in `last_result` whose value must be a number > 0.
    result_positive: list[str] = Field(default_factory=list)
    #: OPTIONAL and additive: the dotted `last_result` path that IS this
    #: check's number, for a `compare` row to read (see `SqlCheck`).
    result_number: Optional[str] = Field(default=None, pattern=RESULT_NUMBER)

    @model_validator(mode="after")
    def _asks_something(self) -> "JobRowCheck":
        asks = [self.state, self.exit_code, self.max_age_min]
        if not (any(a is not None for a in asks) or self.not_missed or self.result_keys
                or self.result_equals or self.result_positive):
            raise ValueError("a job_row check must expect something")
        for key, value in self.result_equals.items():
            variables_in(key)
            if isinstance(value, str):
                variables_in(value)
        return self


class VaultUnitCheck(_Check):
    kind: Literal["vault_unit"]
    note: Literal["drc"]
    day: Literal["last_trading_day", "report_date"]
    section: str = Field(min_length=1)
    unit: str = Field(min_length=1)


class CliCheck(_Check):
    kind: Literal["cli"]
    argv: list[str] = Field(min_length=1)
    exit_code: int = 0

    @field_validator("argv")
    @classmethod
    def _allowlisted(cls, value: list[str]) -> list[str]:
        if not any(tuple(value[: len(prefix)]) == prefix for prefix in READ_ONLY_CLI):
            raise ValueError(
                f"argv {value!r} is not on the read-only allowlist "
                f"{[' '.join(p) for p in READ_ONLY_CLI]}"
            )
        return value


class CompareCheck(_Check):
    """Two checks' numbers, compared once both have run.

    It reads no source of its own: `left` and `right` name checks ABOVE it
    in the file, each declaring `result_number`, and the comparison is
    made over the numbers those two runs already collected. That is what
    keeps it read-only and what keeps it honest — the numbers it grades
    are the ones printed on their own rows.
    """

    kind: Literal["compare"]
    left: str = Field(pattern=CHECK_ID)
    right: str = Field(pattern=CHECK_ID)
    op: CompareOp = CompareOp.EQ

    @model_validator(mode="after")
    def _two_other_checks(self) -> "CompareCheck":
        if self.left == self.right:
            raise ValueError(
                f"left and right are both {self.left} — a compare names two different checks"
            )
        if self.id in (self.left, self.right):
            raise ValueError(f"check {self.id} compares itself")
        return self


SmokeCheck = Annotated[
    Union[LaunchctlCheck, SqlCheck, HttpCheck, LogGrepCheck, JobRowCheck, VaultUnitCheck,
          CliCheck, CompareCheck],
    Field(discriminator="kind"),
]


class SmokeSuite(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    suite: str = Field(pattern=r"^[a-z0-9_-]+$")
    title: str = Field(min_length=1)
    #: The one-shot whose last finished occurrence defines `{last_trading_day}`.
    day_anchor_job: str = Field(pattern=r"^com\.cobalt\.[a-z0-9-]+$")
    checks: list[SmokeCheck] = Field(min_length=1)

    @field_validator("checks")
    @classmethod
    def _unique_ids(cls, value: list) -> list:
        seen: set[str] = set()
        for check in value:
            if check.id in seen:
                raise ValueError(f"duplicate check id {check.id}")
            seen.add(check.id)
        return value

    @field_validator("checks")
    @classmethod
    def _compare_operands(cls, value: list) -> list:
        """A `compare` row's operands are resolved at LOAD, never at 21:50.

        Both must be checks EARLIER in the file (the run evaluates in file
        order, so a later one has no result yet) and both must name a
        `result_number`. Either mistake crashes the file with its line
        rather than producing a row that reports ERROR on the close
        evening (L1).
        """
        kinds: dict[str, str] = {}
        numbered: set[str] = set()
        for check in value:
            if isinstance(check, CompareCheck):
                for role, cid in (("left", check.left), ("right", check.right)):
                    if cid not in kinds:
                        above = ", ".join(kinds) or "nothing"
                        raise ValueError(
                            f"{check.id}.{role} names {cid}, which is not a check above it "
                            f"(a compare reads results that have already run; above it: {above})"
                        )
                    if cid not in numbered:
                        raise ValueError(
                            f"{check.id}.{role} names {cid} (kind {kinds[cid]}), which declares "
                            "no `result_number` — only a check that names THE number of its "
                            "result can be compared"
                        )
            kinds[check.id] = check.kind
            if getattr(check, "result_number", None):
                numbered.add(check.id)
        return value


class SmokeContext(BaseModel):
    """The run's variables. Printed at the top of the report, so every
    rendered command is replayable from the file alone (L57)."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    now: datetime
    report_date: date
    session: str
    cutoff: datetime
    last_trading_day: date
    last_summary_slot: str
    last_summary_date: date
    prod: bool
    tunables: dict[str, Any] = Field(default_factory=dict)

    @field_validator("now", "cutoff")
    @classmethod
    def _aware(cls, value: datetime) -> datetime:
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError("timestamps must carry a timezone")
        return value

    def printable(self) -> dict[str, str]:
        return {
            "now": self.now.isoformat(),
            "report_date": self.report_date.isoformat(),
            "session": self.session,
            "cutoff": self.cutoff.isoformat(),
            "last_trading_day": self.last_trading_day.isoformat(),
            "last_summary_slot": self.last_summary_slot,
            "last_summary_date": self.last_summary_date.isoformat(),
            "database": "production (--prod)" if self.prod else "COBALT_ENV-resolved",
        }


class CheckOutcome(BaseModel):
    """One check's verdict with its evidence. `raw` is the collected
    output, verbatim; `command` + `expected` are the hand fallback."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    id: str
    title: str
    kind: str
    verdict: Verdict
    detail: str
    command: str
    expected: str
    raw: str
    #: THE number of this check's result, when it declared a
    #: `result_number` and the run produced one. `None` everywhere else —
    #: including a check that declared one and came back with a value that
    #: is not a number, which is what makes a `compare` over it ERROR
    #: instead of quietly passing.
    number: Optional[Decimal] = None


class SmokeReport(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)

    suite: str
    title: str
    context: SmokeContext
    generated_at: datetime
    checks: list[CheckOutcome] = Field(min_length=1)
    overall: Overall


__all__ = [
    "CHECK_ID", "CheckOutcome", "CliCheck", "CompareCheck", "CompareOp", "HttpCheck",
    "JobRowCheck", "LaunchctlCheck", "LogGrepCheck", "Op", "Overall", "Predicate",
    "READ_ONLY_CLI", "RESULT_NUMBER", "SmokeCheck", "SmokeContext", "SmokeReport",
    "SmokeSuite", "SqlCheck", "VARIABLES", "VAR_RE", "VaultUnitCheck", "Verdict",
    "overall_verdict", "variables_in",
]
