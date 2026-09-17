"""The seven check kinds, evaluated read-only (S2-P4 STEP-9, R6).

`evaluate(check, ctx, deps)` returns one `CheckOutcome` and never raises:
a probe that could not run is `ERROR`, same rule as day-open and the
heartbeat ("the probe broke" and "the thing is down" are different
facts). Every collector is a `SmokeDeps` field, so tests hand in fakes
and `default_deps()` is the only place the real ones are named.

READ-ONLY, AND HOW THAT IS KEPT. SQL and job rows go through
`cobalt.db_query.read_rows` — the `cobalt db query` read path (guard,
READ ONLY transaction, timeout, role assertion, rollback). A vault note is
read as text and parsed with `find_section`; nothing here imports a
writer, a store or a job wrapper, and `test_smoke_imports_no_writer_and_
calls_no_write` holds both halves of that (static names, runtime
sentinels on every write surface).

VARIABLES render as SQL LITERALS, not bind parameters, on purpose: the
printed hand command must be the statement that actually ran, byte for
byte, and `cobalt db query` takes no parameters. Every value is a typed
date/datetime/number/str from `SmokeContext`, never free input; strings
are quoted with doubled `'`.
"""

from __future__ import annotations

import os
import re
import shlex
import subprocess
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Callable, Optional
from urllib import request as urlrequest
from urllib.error import HTTPError

from cobalt.dayopen.launchd import LaunchdPrintStatus, launchctl_print
from cobalt.db_query import QueryRows, hand_command, read_rows
from cobalt.session.calendar import TradingCalendar
from cobalt.session.clock import ET, SessionClock, session_clock
from cobalt.vaultwrite.markers import MarkerError, find_section

from .config import REPO_ROOT
from .models import (
    VAR_RE,
    CheckOutcome,
    CliCheck,
    HttpCheck,
    JobRowCheck,
    LaunchctlCheck,
    LogGrepCheck,
    Op,
    Predicate,
    SmokeContext,
    SqlCheck,
    Verdict,
    VaultUnitCheck,
)

HTTP_TIMEOUT_S = 10.0
CLI_TIMEOUT_S = 300.0


@dataclass(frozen=True)
class SmokeDeps:
    """Every collector a check can reach. Fakes in tests; `default_deps`."""

    read_rows: Callable[[str, str], QueryRows]
    launchctl_print: Callable[[str], LaunchdPrintStatus]
    launchctl_loaded: Callable[[str], bool]
    http_get: Callable[[str], tuple[int, str]]
    read_text: Callable[[Path], str]
    run_cli: Callable[[list[str]], tuple[int, str]]
    job_specs: Callable[[], list]
    drc_note_path: Callable[[date], Path]
    missed_grace: Callable[[], timedelta]


# ---------------------------------------------------------------------
# real collectors
# ---------------------------------------------------------------------


def load_job_specs() -> list:
    from cobalt.jobs.config import load_job_registry

    return list(load_job_registry().jobs)


def _http_get(url: str) -> tuple[int, str]:
    try:
        with urlrequest.urlopen(urlrequest.Request(url, method="GET"), timeout=HTTP_TIMEOUT_S) as r:
            return r.status, r.read().decode("utf-8", "replace")
    except HTTPError as e:  # a 4xx/5xx is an answer, not a broken probe
        return e.code, e.read().decode("utf-8", "replace")


def _run_cli(argv: list[str]) -> tuple[int, str]:
    proc = subprocess.run(
        ["uv", "run", *argv], cwd=REPO_ROOT, capture_output=True, text=True,
        timeout=CLI_TIMEOUT_S, env=dict(os.environ),
    )
    return proc.returncode, proc.stdout + proc.stderr


def _launchctl_loaded(label: str) -> bool:
    from cobalt.jobs.watchdog import launchctl_status

    return launchctl_status(label).loaded


def _drc_note_path(day: date) -> Path:
    """`prefill.yaml` review_dir + drc_filename_pattern in the resolved
    vault — the same two values prefill-drc and the replay miss line use."""
    from cobalt.prefill.config import load_prefill_paths
    from cobalt.vault import resolve_vault_path

    paths = load_prefill_paths()
    return resolve_vault_path() / paths.review_dir / day.strftime(paths.drc_filename_pattern)


def _missed_grace() -> timedelta:
    from cobalt.jobs.watchdog import MISSED_GRACE_KEY
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(MISSED_GRACE_KEY)
    if row is None:
        raise RuntimeError(f"tunable {MISSED_GRACE_KEY!r} is missing from tunables.yaml (F16)")
    return timedelta(minutes=int(row.value))


def default_deps(*, prod: bool) -> SmokeDeps:
    return SmokeDeps(
        read_rows=lambda statement, side: read_rows(statement, side=side, prod=prod),
        launchctl_print=launchctl_print,
        launchctl_loaded=_launchctl_loaded,
        http_get=_http_get,
        read_text=lambda path: Path(path).read_text(),
        run_cli=_run_cli,
        job_specs=load_job_specs,
        drc_note_path=_drc_note_path,
        missed_grace=_missed_grace,
    )


# ---------------------------------------------------------------------
# context
# ---------------------------------------------------------------------


def last_trading_day(now: datetime, anchor_spec, calendar: Optional[TradingCalendar] = None) -> date:
    """The latest trading day whose anchor-job occurrence (`schedule.at` ET)
    plus that job's `timeout_s` has passed by `now`. Bounded to 14 days."""
    calendar = calendar or session_clock().calendar
    if anchor_spec.schedule is None or not anchor_spec.schedule.at:
        raise ValueError(f"{anchor_spec.label} has no calendar `at` schedule to anchor a day on")
    hh, _, mm = anchor_spec.schedule.at.partition(":")
    now_et = SessionClock.to_et(now)
    day = now_et.date()
    for _ in range(14):
        ready = datetime.combine(day, time(int(hh), int(mm)), tzinfo=ET) + timedelta(
            seconds=anchor_spec.timeout_s
        )
        if calendar.is_trading_day(day) and ready <= now_et:
            return day
        day -= timedelta(days=1)
    raise RuntimeError(f"no trading day with a finished {anchor_spec.label} occurrence in 14 days")


def build_context(
    *, now: datetime, report_date: Optional[date], cutoff: datetime, prod: bool,
    anchor_spec, tunables: dict[str, Any], clock: Optional[SessionClock] = None,
) -> SmokeContext:
    from cobalt.heartbeat.runner import summary_at

    clock = clock or session_clock()
    now_et = SessionClock.to_et(now)
    slots = summary_at()
    passed = [slot for slot in slots if slot <= now_et.time()]
    if passed:
        slot, slot_date = passed[-1], now_et.date()
    else:
        slot, slot_date = slots[-1], now_et.date() - timedelta(days=1)
    return SmokeContext(
        now=now,
        report_date=report_date or now_et.date(),
        session=clock.session(now).value,
        cutoff=cutoff,
        last_trading_day=last_trading_day(now, anchor_spec, clock.calendar),
        last_summary_slot=f"{slot:%H:%M}",
        last_summary_date=slot_date,
        prod=prod,
        tunables=tunables,
    )


def _var(token_name: str, arg: Optional[str], ctx: SmokeContext) -> Any:
    if token_name == "tunable":
        if arg not in ctx.tunables:
            raise KeyError(f"tunable {arg!r} is not in tunables.yaml")
        return ctx.tunables[arg]
    return getattr(ctx, token_name)


def sql_literal(value: Any) -> str:
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, datetime):
        return f"TIMESTAMPTZ '{value.isoformat()}'"
    if isinstance(value, date):
        return f"DATE '{value.isoformat()}'"
    if isinstance(value, (int, float, Decimal)):
        return str(value)
    return "'" + str(value).replace("'", "''") + "'"


def text_value(value: Any) -> str:
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return str(value)


def render_sql(template: str, ctx: SmokeContext) -> str:
    return VAR_RE.sub(lambda m: sql_literal(_var(m.group(1), m.group(2), ctx)), template)


def render_text(template: str, ctx: SmokeContext) -> str:
    return VAR_RE.sub(lambda m: text_value(_var(m.group(1), m.group(2), ctx)), template)


def _resolve(value: Any, ctx: SmokeContext) -> Any:
    """A predicate value: a whole-string `{variable}` becomes its typed
    value; a string with an embedded variable renders as text."""
    if isinstance(value, str):
        whole = VAR_RE.fullmatch(value)
        if whole:
            return _var(whole.group(1), whole.group(2), ctx)
        return render_text(value, ctx)
    return value


# ---------------------------------------------------------------------
# comparison
# ---------------------------------------------------------------------


def _number(value: Any) -> Optional[Decimal]:
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, float, Decimal)):
        return Decimal(str(value))
    return None


def same(actual: Any, expected: Any) -> bool:
    """Equality across the types a DB row and a YAML file carry: numbers by
    value, bools only to bools, dates to their ISO text, else text."""
    if isinstance(expected, bool) or isinstance(actual, bool):
        return isinstance(actual, bool) and isinstance(expected, bool) and actual is expected
    a, e = _number(actual), _number(expected)
    if a is not None and e is not None:
        return a == e
    if actual is None or expected is None:
        return actual is None and expected is None
    return text_value(actual) == text_value(expected)


def _order(actual: Any, expected: Any) -> int:
    a, e = _number(actual), _number(expected)
    if a is None or e is None:
        try:
            a, e = Decimal(str(actual)), Decimal(str(expected))
        except InvalidOperation:
            if isinstance(actual, (date, datetime)) and type(actual) is type(expected):
                return (actual > expected) - (actual < expected)
            raise TypeError(f"cannot order {actual!r} against {expected!r}")
    return (a > e) - (a < e)


def holds(pred: Predicate, row: dict[str, Any], ctx: SmokeContext) -> bool:
    if pred.column not in row:
        raise KeyError(f"column {pred.column!r} not returned (got {sorted(row)})")
    actual = row[pred.column]
    expected = _resolve(pred.value, ctx)
    op = pred.op
    if op is Op.IS_NULL:
        return actual is None
    if op is Op.NOT_NULL:
        return actual is not None
    if op is Op.EQ:
        return same(actual, expected)
    if op is Op.NE:
        return not same(actual, expected)
    if op is Op.IN:
        return any(same(actual, _resolve(v, ctx)) for v in expected)
    if op is Op.NOT_IN:
        return not any(same(actual, _resolve(v, ctx)) for v in expected)
    if actual is None:
        return False
    sign = _order(actual, expected)
    return {Op.LT: sign < 0, Op.LE: sign <= 0, Op.GT: sign > 0, Op.GE: sign >= 0}[op]


def _describe(pred: Predicate, row: dict[str, Any]) -> str:
    value = "" if pred.op in (Op.IS_NULL, Op.NOT_NULL) else f" {pred.value!r}"
    return f"{pred.column} {pred.op.value}{value} (actual {row.get(pred.column)!r})"


def _raw_rows(result: QueryRows) -> str:
    lines = ["\t".join(result.columns)]
    lines += ["\t".join("" if v is None else str(v) for v in row) for row in result.rows]
    return "\n".join(lines)


# ---------------------------------------------------------------------
# commands (the hand fallback, R6 A / Astra R1-24)
# ---------------------------------------------------------------------

JOB_ROW_SQL = (
    "SELECT label, state, exit_code, started_at, finished_at, updated_at, registered_at, "
    "last_result FROM cobalt_jobs WHERE label = {label}"
)
RELATION_SQL = "SELECT to_regclass({relation}) IS NOT NULL AS present"


def _job_sql(check: JobRowCheck) -> str:
    return JOB_ROW_SQL.format(label=sql_literal(check.label))


def _relation_sql(check: SqlCheck) -> str:
    return RELATION_SQL.format(relation=sql_literal(check.requires_relation))


def command_for(check, ctx: SmokeContext, *, note_path: Optional[Path] = None) -> str:
    if isinstance(check, LaunchctlCheck):
        if check.mode == "running":
            return f"launchctl print gui/$(id -u)/{check.label}"
        return "launchctl list | grep com.cobalt.  # compare to `enabled` in configs/cobalt/jobs.yaml"
    if isinstance(check, SqlCheck):
        main = hand_command(render_sql(check.query, ctx), side=check.side, prod=ctx.prod)
        if check.requires_relation:
            return hand_command(_relation_sql(check), side=check.side, prod=ctx.prod) + " && " + main
        return main
    if isinstance(check, JobRowCheck):
        return hand_command(_job_sql(check), side="system", prod=ctx.prod)
    if isinstance(check, HttpCheck):
        url = shlex.quote(render_text(check.url, ctx))
        base = f"curl -s -o /dev/null -w '%{{http_code}}' {url}"
        for needle in check.contains:
            base += f" && curl -s {url} | grep -F {shlex.quote(needle)}"
        return base
    if isinstance(check, LogGrepCheck):
        path = shlex.quote(render_text(check.path, ctx))
        grep = f"grep -E {shlex.quote(check.pattern)}"
        if check.block_start:
            return f"tail -r {path} | sed -E '/{check.block_start}/q' | {grep}"
        return f"{grep} {path}"
    if isinstance(check, VaultUnitCheck):
        day = getattr(ctx, check.day)
        target = shlex.quote(str(note_path)) if note_path else f"<{check.note} note for {day:%Y-%m-%d}>"
        return (
            f"grep -n -F -e {shlex.quote(f'<!-- cobalt:section {check.section} -->')} "
            f"-e {shlex.quote(f'<!-- cobalt:unit {check.unit} -->')} {target}"
        )
    if isinstance(check, CliCheck):
        return "uv run " + " ".join(shlex.quote(render_text(a, ctx)) for a in check.argv)
    raise TypeError(f"unknown check type {type(check).__name__}")


# ---------------------------------------------------------------------
# evaluation
# ---------------------------------------------------------------------


def _out(check, verdict: Verdict, detail: str, command: str, raw: str) -> CheckOutcome:
    return CheckOutcome(
        id=check.id, title=check.title, kind=check.kind, verdict=verdict, detail=detail,
        command=command, expected=check.expect_text, raw=raw,
    )


def _launchctl(check: LaunchctlCheck, ctx: SmokeContext, deps: SmokeDeps) -> CheckOutcome:
    command = command_for(check, ctx)
    if check.mode == "running":
        status = deps.launchctl_print(check.label)
        detail = f"state={status.state}, pid={status.pid}, last exit code={status.last_exit_code}"
        verdict = Verdict.PASS if status.running_with_pid else Verdict.FAIL
        return _out(check, verdict, detail, command, status.raw)
    specs = deps.job_specs()
    lines, not_loaded, loaded_disabled = [], [], []
    for spec in specs:
        loaded = deps.launchctl_loaded(spec.label)
        lines.append(f"{spec.label}\tenabled={spec.enabled}\tloaded={loaded}")
        if spec.enabled and not loaded:
            not_loaded.append(spec.label)
        if not spec.enabled and loaded:
            loaded_disabled.append(spec.label)
    if not_loaded or loaded_disabled:
        detail = (f"enabled but not loaded: {not_loaded or 'none'}; "
                  f"loaded but enabled: false: {loaded_disabled or 'none'}")
        return _out(check, Verdict.FAIL, detail, command, "\n".join(lines))
    return _out(check, Verdict.PASS, f"{len(specs)} registry label(s) match launchd", command, "\n".join(lines))


def _grade(check, row: dict[str, Any], expect: list[Predicate], ctx: SmokeContext,
           command: str, raw: str) -> CheckOutcome:
    failed, known = [], []
    for pred in expect:
        if holds(pred, row, ctx):
            continue
        if pred.known and any(same(row[pred.column], k) for k in pred.known):
            known.append(_describe(pred, row))
        else:
            failed.append(_describe(pred, row))
    if failed:
        return _out(check, Verdict.FAIL, "; ".join(failed), command, raw)
    if known:
        return _out(check, Verdict.KNOWN, "known: " + "; ".join(known), command, raw)
    return _out(check, Verdict.PASS, "; ".join(f"{p.column} ok" for p in expect), command, raw)


def _one_row(result: QueryRows) -> Optional[dict[str, Any]]:
    if len(result.rows) > 1:
        raise ValueError(f"expected at most one row, got {len(result.rows)}")
    return dict(zip(result.columns, result.rows[0])) if result.rows else None


def _sql(check: SqlCheck, ctx: SmokeContext, deps: SmokeDeps) -> CheckOutcome:
    command = command_for(check, ctx)
    raw_parts = []
    if check.requires_relation:
        present = deps.read_rows(_relation_sql(check), check.side)
        raw_parts.append(_raw_rows(present))
        row = _one_row(present)
        if not row or row.get("present") is not True:
            return _out(check, Verdict.FAIL, f"relation {check.requires_relation} does not exist",
                        command, "\n".join(raw_parts))
    result = deps.read_rows(render_sql(check.query, ctx), check.side)
    raw_parts.append(_raw_rows(result))
    raw = "\n".join(raw_parts)
    row = _one_row(result)
    if row is None:
        return _out(check, Verdict.FAIL, "no row returned", command, raw)
    if check.known_if and all(holds(p, row, ctx) for p in check.known_if):
        return _out(check, Verdict.KNOWN, f"KNOWN: {check.known_text}", command, raw)
    return _grade(check, row, check.expect, ctx, command, raw)


def _dig(data: Any, dotted: str) -> tuple[bool, Any]:
    for part in dotted.split("."):
        if not isinstance(data, dict) or part not in data:
            return False, None
        data = data[part]
    return True, data


def _job_row(check: JobRowCheck, ctx: SmokeContext, deps: SmokeDeps) -> CheckOutcome:
    command = command_for(check, ctx)
    result = deps.read_rows(_job_sql(check), "system")
    raw = _raw_rows(result)
    row = _one_row(result)
    if row is None:
        return _out(check, Verdict.FAIL, f"no cobalt_jobs row for {check.label}", command, raw)
    failed = []
    if check.state is not None and row.get("state") != check.state:
        failed.append(f"state {row.get('state')!r} (expected {check.state!r})")
    if check.exit_code is not None and row.get("exit_code") != check.exit_code:
        failed.append(f"exit_code {row.get('exit_code')!r} (expected {check.exit_code})")
    if check.max_age_min is not None:
        updated = row.get("updated_at")
        if updated is None or ctx.now - updated > timedelta(minutes=check.max_age_min):
            failed.append(f"updated_at {updated} older than {check.max_age_min} min")
    if check.not_missed:
        from cobalt.jobs.watchdog import is_missed

        spec = next((s for s in deps.job_specs() if s.label == check.label), None)
        if spec is None:
            raise KeyError(f"{check.label} is not in configs/cobalt/jobs.yaml")
        missed, why = is_missed(spec, row, now_et=SessionClock.to_et(ctx.now), grace=deps.missed_grace())
        if missed:
            failed.append(f"MISSED — {why}")
    last = row.get("last_result") or {}
    for key in check.result_keys:
        if key not in last:
            failed.append(f"last_result has no {key!r}")
    for path_template, expected in check.result_equals.items():
        path = render_text(path_template, ctx)
        found, actual = _dig(last, path)
        want = _resolve(expected, ctx)
        if not found or not same(actual, want):
            failed.append(f"last_result.{path} = {actual!r} (expected {text_value(want)!r})")
    for key in check.result_positive:
        value = _number(last.get(key))
        if value is None or value <= 0:
            failed.append(f"last_result.{key} = {last.get(key)!r} (expected > 0)")
    if failed:
        return _out(check, Verdict.FAIL, "; ".join(failed), command, raw)
    return _out(check, Verdict.PASS, f"{check.label}: state={row.get('state')}, "
                f"exit={row.get('exit_code')}, finished_at={row.get('finished_at')}", command, raw)


def _http(check: HttpCheck, ctx: SmokeContext, deps: SmokeDeps) -> CheckOutcome:
    command = command_for(check, ctx)
    url = render_text(check.url, ctx)
    status, body = deps.http_get(url)
    raw = f"HTTP {status}\n{body[:2000]}"
    failed = []
    if status != check.status:
        failed.append(f"HTTP {status} (expected {check.status})")
    failed += [f"body lacks {needle!r}" for needle in check.contains if needle not in body]
    if failed:
        return _out(check, Verdict.FAIL, "; ".join(failed), command, raw)
    return _out(check, Verdict.PASS, f"HTTP {status}", command, raw)


def _log_grep(check: LogGrepCheck, ctx: SmokeContext, deps: SmokeDeps) -> CheckOutcome:
    command = command_for(check, ctx)
    path = REPO_ROOT / render_text(check.path, ctx)
    text = deps.read_text(path)
    lines = text.splitlines()
    if check.block_start:
        starts = [i for i, line in enumerate(lines) if re.search(check.block_start, line)]
        if not starts:
            return _out(check, Verdict.ERROR, f"no line matching {check.block_start!r} in {check.path}",
                        command, "\n".join(lines[-20:]))
        lines = lines[starts[-1]:]
    hits = [line for line in lines if re.search(check.pattern, line)]
    raw = "\n".join(lines[:60] if check.block_start else hits[-20:]) or "(no lines)"
    if bool(hits) == check.present:
        detail = f"{len(hits)} line(s) match {check.pattern!r}" if hits else f"no line matches {check.pattern!r}"
        return _out(check, Verdict.PASS, detail, command, raw)
    detail = (f"no line matches {check.pattern!r}" if check.present
              else f"{len(hits)} line(s) match {check.pattern!r}")
    return _out(check, Verdict.FAIL, detail, command, raw)


def _vault_unit(check: VaultUnitCheck, ctx: SmokeContext, deps: SmokeDeps) -> CheckOutcome:
    day = getattr(ctx, check.day)
    path = deps.drc_note_path(day)
    command = command_for(check, ctx, note_path=path)
    if not Path(path).is_file():
        return _out(check, Verdict.FAIL, f"note absent: {path}", command, "")
    lines = deps.read_text(Path(path)).splitlines()
    try:
        section = find_section(lines, check.section)
    except MarkerError as e:
        return _out(check, Verdict.ERROR, f"markers unreadable: {e}", command, "")
    if section is None:
        return _out(check, Verdict.FAIL, f"section {check.section!r} absent in {path}", command, "")
    raw = section.text(lines)
    unit = section.units.get(check.unit)
    if unit is None:
        return _out(check, Verdict.FAIL, f"unit {check.section}/{check.unit} absent in {path}", command, raw)
    return _out(check, Verdict.PASS, f"unit {check.section}/{check.unit} present in {path}", command, raw)


def _cli(check: CliCheck, ctx: SmokeContext, deps: SmokeDeps) -> CheckOutcome:
    command = command_for(check, ctx)
    argv = [render_text(a, ctx) for a in check.argv]
    code, output = deps.run_cli(argv)
    raw = f"exit {code}\n" + "\n".join(output.splitlines()[-40:])
    if code != check.exit_code:
        return _out(check, Verdict.FAIL, f"exit {code} (expected {check.exit_code})", command, raw)
    return _out(check, Verdict.PASS, f"exit {code}", command, raw)


_EVALUATORS = {
    "launchctl": _launchctl, "sql": _sql, "job_row": _job_row, "http": _http,
    "log_grep": _log_grep, "vault_unit": _vault_unit, "cli": _cli,
}


def evaluate(check, ctx: SmokeContext, deps: SmokeDeps) -> CheckOutcome:
    try:
        return _EVALUATORS[check.kind](check, ctx, deps)
    except Exception as e:  # noqa: BLE001 — a broken probe is ERROR, never a crash
        try:
            command = command_for(check, ctx)
        except Exception:  # noqa: BLE001
            command = f"(command not renderable: {check.kind})"
        return _out(check, Verdict.ERROR, f"ERROR(probe failed) — {type(e).__name__}: {e}", command, str(e))


def run_suite(suite, ctx: SmokeContext, deps: SmokeDeps) -> list[CheckOutcome]:
    """Every check in file order. One broken probe never stops the rest."""
    return [evaluate(check, ctx, deps) for check in suite.checks]


__all__ = [
    "SmokeDeps", "build_context", "command_for", "default_deps", "evaluate", "holds",
    "last_trading_day", "load_job_specs", "render_sql", "render_text", "run_suite", "same",
    "sql_literal",
]
