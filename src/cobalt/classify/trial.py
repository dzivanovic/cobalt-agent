"""The trial runner — plan, dry-run, run (plan §3 M1–M8).

    plan(cfg, clf, set, reps=, mode=, questions=, reverse=) -> Plan
    dry_run(plan, clf) -> the DRY line          (ZERO network calls)
    run(plan, clf, tag=) -> (results path, the RUN line)

MODES (plan M3 / M4): `single` = one call per item carrying every
question; `parallel` = one call per question, up to `max_parallel`
threads per item; `sequential` = one call per question, in order;
`gated` = a layered set (L20) as its four levels, one call per level, in
order. "Dependent" means ORDERED here: no level is skipped on an earlier
answer, because no gate rule is ruled (the rule would be his).
`questions=n` keeps the first n (M2); `reverse` reverses the question
map and nothing else (M6).

THE GUARD FIRST. Every rendered body passes `_guard_outbound` while the
plan is built. A REAL item (T9's day-open reports) that fails it is
SKIPPED loud and counted, never sent; a constructed item that fails it is
a broken config and raises.

THE MONEY. `run` asks the ledger for the WHOLE run's projection and call
count before the first call (refused = zero calls, TOTAL demand, L53);
each call is checked again inside `classify()`, and the running total
reaching the cap stops the run. One `CallRecord` JSON line per call goes
to `results_dir/classify-results-<set>-<tag>-<UTC stamp>.jsonl` (inside
`scratch/`), created on the first record only.

Percentiles are nearest-rank, computed here (L35: every number is code's).
"""

from __future__ import annotations

import math
import re
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from loguru import logger

from .collector import ClassifyError, OpenRouterClassifier
from .config import ClassifyConfigError, TrialConfig
from .models import CallRecord, QuestionSet, TrialItem

MODES = ("single", "parallel", "sequential", "gated")


@dataclass
class Plan:
    set_name: str
    mode: str
    reps: int
    qset: QuestionSet
    shapes: list[QuestionSet]
    items: list[TrialItem]
    skipped: list[TrialItem] = field(default_factory=list)

    @property
    def calls(self) -> int:
        return len(self.items) * self.reps * len(self.shapes)

    def shapes_ids(self) -> list[str]:
        return [qid for s in self.shapes for qid in s.questions]


def percentile(xs: list[float], p: float) -> float:
    """Nearest-rank percentile of a non-empty list."""
    if not xs:
        raise ValueError("percentile of nothing")
    s = sorted(xs)
    k = max(1, math.ceil(p / 100 * len(s)))
    return s[k - 1]


def _shapes(cfg: TrialConfig, name: str, qset: QuestionSet, mode: str) -> list[QuestionSet]:
    if mode == "single":
        return [qset]
    if mode in ("parallel", "sequential"):
        return [qset.only(q) for q in qset.questions]
    try:
        levels = cfg.level_keys(name)
    except ClassifyConfigError as e:
        raise ClassifyError(f"--mode gated: {e}") from None
    out = []
    for group in levels:
        keep = {k: q for k, q in qset.questions.items() if k in group}
        if keep:
            out.append(qset.model_copy(update={"questions": keep}))
    return out


def plan(cfg: TrialConfig, clf: OpenRouterClassifier, name: str, *, reps: int = 1,
         mode: str = "single", questions: Optional[int] = None, reverse: bool = False) -> Plan:
    if mode not in MODES:
        raise ClassifyError(f"--mode {mode!r}: one of {list(MODES)}")
    if reps < 1:
        raise ClassifyError(f"--reps {reps}: at least 1")
    qset, items = cfg.resolve(name)
    if questions is not None:
        try:
            qset = qset.first(questions)
        except ValueError as e:
            raise ClassifyError(str(e)) from None
    if reverse:
        qset = qset.reversed()
    shapes = _shapes(cfg, name, qset, mode)

    keep, skipped = [], []
    for item in items:
        try:
            for shape in shapes:
                clf._guard_outbound(clf.body(shape, item), keyed=False)
        except ClassifyError as e:
            if not item.provenance.startswith("real:"):
                raise
            logger.error(f"classify: SKIPPED {name}/{item.id} ({item.provenance}) — {e}")
            skipped.append(item)
            continue
        keep.append(item)
    if not keep:
        raise ClassifyError(f"{name}: every item was skipped by the outbound guard — L1: nothing to run")
    return Plan(name, mode, reps, qset, shapes, keep, skipped)


def _projection(p: Plan, clf: OpenRouterClassifier) -> tuple[int, float]:
    """(estimated input tokens, projected USD) of the whole plan."""
    tokens, usd = 0, 0.0
    for item in p.items:
        for shape in p.shapes:
            body = clf.body(shape, item)
            tokens += math.ceil(len(body) / 4)
            usd += clf.project(body)
    return tokens * p.reps, usd * p.reps


def dry_run(p: Plan, clf: OpenRouterClassifier) -> str:
    tokens, usd = _projection(p, clf)
    return (
        f"DRY set={p.set_name} mode={p.mode} reps={p.reps} items={len(p.items)} "
        f"skipped={len(p.skipped)} questions={len(p.qset.questions)} calls={p.calls} "
        f"projected_input_tokens_est={tokens} projected_usd={usd:.6f} "
        f"ledger_usd={clf.ledger.spent():.6f} cap_usd={clf.cfg.spend_cap_usd:g} "
        "(tokens = rendered body bytes / 4, an estimate; nothing sent)"
    )


def _tag(tag: str) -> str:
    t = re.sub(r"[^A-Za-z0-9_-]+", "-", tag).strip("-")
    if not t:
        raise ClassifyError(f"--tag {tag!r} has no usable character")
    return t


def run(p: Plan, clf: OpenRouterClassifier, *, tag: str) -> tuple[Path, str]:
    _, projected = _projection(p, clf)
    clf.ledger.check(projected, calls=p.calls)          # the WHOLE run first: refused = zero calls

    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out = clf.cfg.results_path() / f"classify-results-{p.set_name}-{_tag(tag)}-{stamp}.jsonl"
    lock = threading.Lock()
    records: list[CallRecord] = []
    walls: list[float] = []

    def write(rec: CallRecord) -> None:
        with lock:
            out.parent.mkdir(parents=True, exist_ok=True)
            with out.open("a") as fh:
                fh.write(rec.model_dump_json() + "\n")
            records.append(rec)

    pool = ThreadPoolExecutor(max_workers=clf.cfg.max_parallel) if p.mode == "parallel" else None
    try:
        for _rep in range(p.reps):
            for item in p.items:
                t0 = time.perf_counter()
                if pool is not None:
                    for rec in pool.map(lambda s: clf.classify(s, item), p.shapes):
                        write(rec)
                else:
                    for shape in p.shapes:
                        write(clf.classify(shape, item))
                walls.append((time.perf_counter() - t0) * 1000.0)
                clf.ledger.stop_if()
    finally:
        if pool is not None:
            pool.shutdown(wait=True)

    counts = {s: sum(r.status == s for r in records) for s in ("ok", "invalid", "http_error")}
    lat = [r.latency_ms for r in records]
    spent = sum(r.cost_usd or 0.0 for r in records)
    line = (
        f"RUN set={p.set_name} mode={p.mode} reps={p.reps} calls={len(records)} "
        f"ok={counts['ok']} invalid={counts['invalid']} http_error={counts['http_error']} "
        f"skipped={len(p.skipped)} latency_ms p50={percentile(lat, 50):.1f} "
        f"p95={percentile(lat, 95):.1f} p99={percentile(lat, 99):.1f}"
    )
    if len(p.shapes) > 1:
        line += (f" wall_ms p50={percentile(walls, 50):.1f} p95={percentile(walls, 95):.1f} "
                 f"p99={percentile(walls, 99):.1f}")
    line += f" spent_usd={spent:.8f} ledger_usd={clf.ledger.spent():.8f} results={out}"
    if counts["invalid"]:
        logger.error(f"classify: {counts['invalid']} INVALID response(s) in {out.name} (plan B3)")
    return out, line


__all__ = ["MODES", "Plan", "dry_run", "percentile", "plan", "run"]
