"""The JEV shadow router and its routing ledger (card 591; design
`docs/30 - Design/jev-shadow-design-2026-10-14.md` §2-§6, his R1467).

    load_route_config()        configs/cobalt/classify/route.yaml — set ROUTE,
                               the R1532 routing table, the retire block (L10)
    load_card(repo, path)      the card AS LAUNCHED, answer-bearing lines out
    Router(cfg).route(card)    ONE keyed call -> ONE decision row
    run_batch(router, cards)   every failure a status row; no retry
    write_outcome(repo, path)  an outcome row from the CHECK DONE line
    weekly_read(rows, cfg)     aggregates only; n < 30 = insufficient data

SHADOW ONLY (design §4). The router writes ledger rows and nothing else: it
launches no seat, edits no card and touches no launch line; nothing routes.

THE MODEL IS CODE'S, NOT JEV'S (L35). The band picks the row of the R1532
table (`routing_table`, his ruling); `unsure` takes the HIGH row (R1532
condition 3: the higher band when unsure). The four gates and the band's
confidence are recorded on every row and route nothing (decision 3): no
threshold lives here.

THE SAME DOOR. `Router` is a second class beside `OpenRouterClassifier`
behind the same transport, guards and ledger; its one keyed call goes
through `_send` (the key path of collector.py, unchanged). The spend
ledger is the trial's ONE host-wide file (fold F2): the loader refuses a
`spend_ledger`, `spend_cap_usd` or `spend_cap_source` that differs from
trial.yaml's, and the two carried paid lines come from trial.yaml.

THE ROUTING LEDGER is an append-only JSONL file outside every checkout
(fold F8). A row is never rewritten; an outcome is a later row keyed to
its decision by `card_path` and `launch_sha`. No row holds card text.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import statistics
import subprocess
import time
from dataclasses import dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Literal, Optional
from urllib.parse import urlparse

import yaml
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator

from . import config as cfgmod
from .collector import KEY_NAME, ClassifyAuthError, ClassifyError, OpenRouterClassifier, Transport
from .config import ALLOWED_HOST, CarriedSpend, ClassifyConfigError, host_ledger_path
from .ledger import Ledger
from .models import Choice, Noul, Question, QuestionSet, RouteDecision, TrialItem

#: The code's own checkout: the committed config, the pricing record, the hubs.
PKG_ROOT = Path(__file__).resolve().parents[3]
ROUTE_CONFIG_PATH = PKG_ROOT / "configs" / "cobalt" / "classify" / "route.yaml"
SHADOW_HUB_PATH = PKG_ROOT / "docs" / "40 - DevDocs" / "prompts" / "SHADOW-HUB.md"
BUILD_HUB_PATH = PKG_ROOT / "docs" / "40 - DevDocs" / "prompts" / "BUILD-HUB.md"
PROMPTS_DIR = "docs/40 - DevDocs/prompts"
REPORTS_DIR = "docs/40 - DevDocs/reports"

SET_NAME = "ROUTE"
QUESTION_IDS = ("band", "write_path", "migration", "money", "new_horizon")
BAND_OPTIONS = {"low", "mid", "high", "unsure"}
BANDS = ("low", "mid", "high")

#: The `--model` of BUILD-HUB.md's launch line: a builder the table may name.
OPUS = "claude-opus-5-5"
#: R1532 "Sonnet routing for now" (design :81): never a builder.
REFUSED_BUILDERS = ("claude-sonnet-5-5",)

#: Header lines removed before the call (design :63 `[F-18]`, fold F4).
DROPPED_HEADERS = ("TIP:", "REPORT:", "CHECK REPORT:", "BAND:", "MODEL:")

#: L8: a cell under this n prints `insufficient data`, never a figure.
MIN_N = 30
UNKNOWN = "UNKNOWN"


# -- the config (L10) ---------------------------------------------------------------

class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class TableRow(_Strict):
    builder: str = Field(min_length=1)
    backup: Optional[str] = None


class RoutingTable(_Strict):
    """Band -> builder, his R1532 table. Read, never written, by the router."""

    source: str
    low: TableRow
    mid: TableRow
    high: TableRow

    @field_validator("source")
    @classmethod
    def _ruled(cls, v: str) -> str:
        if not v.startswith("ruling:"):
            raise ValueError(f"routing_table.source {v!r} must start 'ruling:' and name his row (L53)")
        return v

    def row(self, band: str) -> TableRow:
        return getattr(self, band)

    def sha256(self) -> str:
        blob = json.dumps(self.model_dump(mode="json"), sort_keys=True, separators=(",", ":"))
        return hashlib.sha256(blob.encode()).hexdigest()


class OutcomeRule(_Strict):
    method: str = Field(min_length=1)
    loss: str = Field(min_length=1)


class Retire(_Strict):
    """Predeclared before any outcome is read (fold F10, `[F-17]`)."""

    declared: date
    set_sha256: str = Field(min_length=64, max_length=64)
    source: str = Field(min_length=1)
    outcomes: dict[str, OutcomeRule]

    @field_validator("outcomes")
    @classmethod
    def _three(cls, v: dict[str, OutcomeRule]) -> dict[str, OutcomeRule]:
        want = {"opus_own_held", "fix_rounds", "tokens"}
        if set(v) != want:
            raise ValueError(f"retire.outcomes must be exactly {sorted(want)} (got {sorted(v)})")
        return v


class RouteSet(_Strict):
    version: int = Field(ge=1)
    questions: dict[str, Question]


def _engine(v: str) -> str:
    if not v.startswith("engine:"):
        raise ValueError(f"{v!r} must start 'engine:' and state its sum (an engine tunable)")
    return v


class RouteConfig(_Strict):
    door_url: str
    door: Literal["systemone"]
    model_id: str = Field(min_length=1)
    model_id_source: str
    entry_record: str = Field(min_length=1)
    timeout_s: float = Field(gt=0)
    spend_ledger: str = Field(min_length=1)
    spend_cap_usd: float = Field(gt=0)
    spend_cap_source: str
    call_ceiling: int = Field(ge=1)
    call_ceiling_source: str
    batch_wall_clock_s: float = Field(ge=0)
    batch_wall_clock_source: str
    routing_ledger: str = Field(min_length=1)
    routing_table: RoutingTable
    retire: Retire
    sets: dict[str, RouteSet]
    #: filled by the loader from trial.yaml, never written in route.yaml
    carried_spend: list[CarriedSpend] = Field(default_factory=list)

    @field_validator("door_url")
    @classmethod
    def _openrouter_only(cls, v: str) -> str:
        u = urlparse(v)
        if u.scheme != "https" or u.hostname != ALLOWED_HOST:
            raise ValueError(f"{v!r}: only https://{ALLOWED_HOST}/… is allowed")
        return v

    @field_validator("model_id_source", "spend_cap_source")
    @classmethod
    def _ruled(cls, v: str) -> str:
        if not v.startswith("ruling:"):
            raise ValueError(f"{v!r} must start 'ruling:' and name his row (L53)")
        return v

    @field_validator("call_ceiling_source", "batch_wall_clock_source")
    @classmethod
    def _engine_source(cls, v: str) -> str:
        return _engine(v)

    @field_validator("spend_ledger", "routing_ledger")
    @classmethod
    def _host(cls, v: str, info) -> str:
        host_ledger_path(v, info.field_name)
        return v

    @field_validator("sets")
    @classmethod
    def _route_only(cls, v: dict[str, RouteSet]) -> dict[str, RouteSet]:
        if set(v) != {SET_NAME}:
            raise ValueError(f"sets must be exactly ['{SET_NAME}'] (got {sorted(v)})")
        qs = v[SET_NAME].questions
        if tuple(qs) != QUESTION_IDS:
            raise ValueError(f"{SET_NAME} questions must be {list(QUESTION_IDS)} in order (got {list(qs)})")
        band = qs["band"]
        if not isinstance(band, Choice) or set(band.options) != BAND_OPTIONS:
            raise ValueError(f"{SET_NAME}.band must be a Choice of {sorted(BAND_OPTIONS)}")
        for qid in QUESTION_IDS[1:]:
            if not isinstance(qs[qid], Noul):
                raise ValueError(f"{SET_NAME}.{qid} must be a Noul")
        return v

    def question_set(self) -> QuestionSet:
        s = self.sets[SET_NAME]
        return QuestionSet(id=SET_NAME, version=s.version, questions=s.questions)

    def entry_pricing(self) -> dict:
        """The listed price, from the committed endpoints record (L1: no cost, no call)."""
        try:
            data = json.loads((PKG_ROOT / self.entry_record).read_text())["data"]
            (endpoint,) = data["endpoints"]
            pricing = endpoint["pricing"]
            if not isinstance(pricing, dict):
                raise TypeError("'pricing' is not an object")
        except Exception as e:  # noqa: BLE001
            raise ClassifyConfigError(
                f"entry_record {self.entry_record!r}: no single endpoint pricing ({type(e).__name__})"
            ) from None
        return pricing


def builder_ids(hub: Path) -> list[str]:
    """The row ids of SHADOW-HUB.md `## BUILDERS` (the reading of
    `tests/ops/test_shadow_hub_file.py`: a line that starts ``| ` ``)."""
    m = re.search(r"^## BUILDERS[ \t]*$(.*?)(?=^## |\Z)", hub.read_text(), re.M | re.S)
    if not m:
        raise ClassifyConfigError(f"{hub}: no ## BUILDERS section")
    return [ln.strip().strip("|").split("|")[0].strip().strip("`")
            for ln in m.group(1).splitlines() if ln.startswith("| `")]


def _check_table(table: RoutingTable, hub: Path) -> None:
    """Fold F6: every builder and backup id is a `## BUILDERS` row id or
    Opus (BUILD-HUB's `--model`); Sonnet is refused as a builder."""
    allowed = set(builder_ids(hub)) | {OPUS}
    for band in BANDS:
        row = table.row(band)
        for role, mid in (("builder", row.builder), ("backup", row.backup)):
            if mid is None:
                continue
            if mid in REFUSED_BUILDERS:
                raise ClassifyConfigError(
                    f"routing_table.{band}.{role} {mid!r}: Sonnet is never a builder (R1532, design :81)")
            if mid not in allowed:
                raise ClassifyConfigError(
                    f"routing_table.{band}.{role} {mid!r} is no ## BUILDERS row of {hub.name} "
                    f"and not {OPUS} — refused")


def load_route_config(path: Optional[Path] = None, *, shadow_hub: Optional[Path] = None,
                      trial_path: Optional[Path] = None) -> RouteConfig:
    path = Path(path) if path is not None else ROUTE_CONFIG_PATH
    if not path.exists():
        raise ClassifyConfigError(f"route config not found: {path}. There is no built-in default.")
    try:
        raw = yaml.safe_load(path.read_text())
    except yaml.YAMLError as e:
        raise ClassifyConfigError(f"{path}: YAML does not parse:\n{e}") from None
    if not isinstance(raw, dict) or not isinstance(raw.get("route"), dict):
        raise ClassifyConfigError(f"{path}: expected a 'route' mapping")
    body = dict(raw["route"])
    if "carried_spend" in body:
        raise ClassifyConfigError(f"{path}: carried_spend lives in trial.yaml only (fold F2)")
    trial = cfgmod.load_trial_config(trial_path)
    try:
        cfg = RouteConfig(**body, carried_spend=trial.carried_spend)
    except ValidationError as e:
        raise ClassifyConfigError(f"{path}: invalid route config:\n{e}") from None
    for key in ("spend_ledger", "spend_cap_usd", "spend_cap_source"):
        if getattr(cfg, key) != getattr(trial, key):
            raise ClassifyConfigError(
                f"{path}: {key} {getattr(cfg, key)!r} differs from trial.yaml's "
                f"{getattr(trial, key)!r} — ONE ledger and ONE cap bind every keyed run (fold F2)")
    _check_table(cfg.routing_table, Path(shadow_hub) if shadow_hub is not None else SHADOW_HUB_PATH)
    sha = cfg.question_set().sha256
    if cfg.retire.set_sha256 != sha:
        raise ClassifyConfigError(
            f"{path}: retire.set_sha256 {cfg.retire.set_sha256} is not set {SET_NAME}'s sha256 {sha} "
            "— the retire block binds the set it was declared for (fold F10)")
    return cfg


# -- the card as launched (F4) ---------------------------------------------------------

def _git(repo: Path, *args: str) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise ClassifyError(f"git {args[0]} {' '.join(args[1:])!s}: exit {r.returncode}")
    return r.stdout


def _split(text: str) -> tuple[list[str], list[str]]:
    """(header lines, body lines): the header ends at the first `## ` line."""
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        if ln.startswith("## "):
            return lines[:i], lines[i:]
    return lines, []


def _value(header: list[str], key: str) -> Optional[str]:
    for ln in header:
        if ln.startswith(key):
            return ln[len(key):].strip()
    return None


def launch_sha(repo: Path, path: str) -> str:
    """The commit that launched the card's build (ASK DESK 9): the last
    commit of the card file whose `TIP:` header is empty (a card with no
    `TIP:` line counts as empty)."""
    for sha in _git(repo, "log", "--format=%H", "--", path).split():
        tip = _value(_split(_git(repo, "show", f"{sha}:{path}"))[0], "TIP:")
        if not tip:
            return sha
    raise ClassifyError(f"{path}: no commit of the card has an empty TIP: header — no launch commit")


@dataclass(frozen=True)
class CardText:
    path: str
    launch_sha: str
    blob_sha: str
    state: str
    card_band: Optional[str]
    rows: int
    restarts: Optional[list[str]]


def _rows(body: list[str]) -> int:
    """The `## ROWS` table's row count (`[F-17]`): its lines less the header
    line and the separator."""
    table, inside = [], False
    for ln in body:
        if ln.startswith("## "):
            inside = ln.strip() == "## ROWS"
            continue
        if inside and ln.startswith("|") and not re.match(r"^\|\s*:?-", ln):
            table.append(ln)
    return max(0, len(table) - 1)


def load_card(repo: Path, path: str, *, launch: Optional[str] = None) -> CardText:
    """The card at its launch commit, never the working copy (design :62).
    The five answer-bearing header lines are removed (fold F4); `BAND:` is
    kept apart as `card_band` and never sent."""
    repo = Path(repo)
    sha = launch or launch_sha(repo, path)
    text = _git(repo, "show", f"{sha}:{path}")
    blob = _git(repo, "rev-parse", f"{sha}:{path}").strip()
    header, body = _split(text)
    kept = [ln for ln in header if not ln.startswith(DROPPED_HEADERS)]
    restarts = _value(header, "RESTARTS:")
    return CardText(
        path=path, launch_sha=sha, blob_sha=blob,
        state="\n".join(kept + body),
        card_band=_value(header, "BAND:") or None,
        rows=_rows(body),
        restarts=None if restarts is None else [s for s in restarts.split() if s.lower() != "none"],
    )


def score(card: CardText) -> tuple[str, dict[str, Any]]:
    """The frozen complexity score from card fields (`[F-11]`, `[F-13]`):
    R from the row count, S from `RESTARTS:`; M, X, H and $ are UNKNOWN —
    no card field states them — and any UNKNOWN makes the band UNKNOWN."""
    comps: dict[str, Any] = {
        "R": max(0, card.rows - 3),
        "M": UNKNOWN,
        "S": len(card.restarts) if card.restarts is not None else UNKNOWN,
        "X": UNKNOWN,
        "H": UNKNOWN,
        "$": UNKNOWN,
    }
    if any(v == UNKNOWN for v in comps.values()):
        return UNKNOWN, comps
    total = sum(comps.values())
    return ("LOW" if total <= 2 else "MID" if total <= 6 else "HIGH"), comps


# -- the router (J2) -------------------------------------------------------------------

def status_of(e: ClassifyError) -> str:
    """A ClassifyError of a routed card as its decision-row status (fold F9)."""
    if isinstance(e, ClassifyAuthError):
        return "auth_error"
    m = str(e)
    if m.startswith("spend cap"):
        return "cap_refused"
    if m.startswith("call ceiling"):
        return "ceiling_refused"
    if m.startswith("returned cost"):
        return "overrun"
    if "on POST systemone" in m:
        return "transport_error"
    if m.startswith(KEY_NAME):              # the key could not be read: no keyed call
        return "auth_error"
    if "refused" in m:
        return "refused"
    return "invalid"


class Router(OpenRouterClassifier):
    """Card text -> one decision row. Holds a config, a transport and the
    spend ledger — never a key (collector.py's key path is the only one)."""

    def __init__(self, cfg: RouteConfig, transport: Optional[Transport] = None,
                 ledger: Optional[Ledger] = None, pricing: Optional[dict] = None):
        super().__init__(cfg, transport=transport, ledger=ledger, pricing=pricing)
        self.qset = cfg.question_set()
        self.table_sha256 = cfg.routing_table.sha256()

    def item(self, card: CardText) -> TrialItem:
        return TrialItem(id=Path(card.path).stem, state=card.state,
                         provenance=f"real:{card.path}@{card.launch_sha}")

    def _base(self, card: CardText) -> dict:
        band, comps = score(card)
        return dict(card_path=card.path, card_blob_sha=card.blob_sha, launch_sha=card.launch_sha,
                    set_id=self.qset.id, set_sha256=self.qset.sha256,
                    table_sha256=self.table_sha256, card_band=card.card_band,
                    score_band=band, score_components=comps, rows_band=card.rows)

    def status_row(self, card: CardText, status: str, error: str) -> RouteDecision:
        """A row for a card that got no call (timeout, after an auth_error)."""
        return self.write(RouteDecision(**self._base(card), status=status, error=error))

    def route(self, card: CardText) -> RouteDecision:
        """ONE keyed call through `_send` (no retry); the decision row is
        written whatever came back."""
        t0 = time.perf_counter()
        base = self._base(card)
        try:
            rec, _raw = self._classify(self.qset, self.item(card))
        except ClassifyError as e:
            return self.write(RouteDecision(**base, status=status_of(e), error=str(e),
                                            latency_ms=(time.perf_counter() - t0) * 1000.0))
        row = dict(base, jev_model_returned=rec.model_returned, latency_ms=rec.latency_ms,
                   cost_usd=rec.cost_usd, cost_source=rec.cost_source, status=rec.status,
                   error=rec.error)
        if rec.status == "ok":
            answers = {a.question_id: a for a in rec.answers}
            band = answers["band"]
            row.update(band=band.value, band_probabilities=band.probabilities,
                       band_confidence=band.confidence,
                       gates={q: answers[q].value for q in QUESTION_IDS[1:]})
            if band.value == "unsure":           # R1532 condition 3: the higher band
                pick, rule = self.cfg.routing_table.high, "unsure-higher"
            else:
                pick, rule = self.cfg.routing_table.row(band.value), "table"
            row.update(model=pick.builder, backup=pick.backup, rule_path=rule)
        return self.write(RouteDecision(**row))

    def write(self, row: RouteDecision) -> RouteDecision:
        """The router's one write: an appended routing-ledger line (guarded)."""
        data = row.model_dump(mode="json")
        self._guard_stored(data)
        _append(Path(self.cfg.routing_ledger), data)
        return row


def _append(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as fh:
        fh.write(json.dumps(data, ensure_ascii=False) + "\n")


def run_batch(router: Router, cards: list[CardText], *, wall_clock_s: float,
              clock=time.monotonic) -> list[RouteDecision]:
    """Fold F9: each card one call, in order. A failure is that card's
    status row; after an `auth_error` no further keyed call is made; at
    `wall_clock_s` the batch stops sending and the cards left get
    `timeout` rows. A failed call never retries."""
    t0, rows, auth_failed = clock(), [], False
    for card in cards:
        if clock() - t0 >= wall_clock_s:
            row = router.status_row(card, "timeout", f"batch wall clock {wall_clock_s:g}s reached — not sent")
        elif auth_failed:
            row = router.status_row(card, "auth_error", "an earlier call of this batch got auth_error — not sent")
        else:
            row = router.route(card)
            auth_failed = row.status == "auth_error"
        rows.append(row)
    return rows


# -- which cards closed on a day (F9) ----------------------------------------------------

def _report_rel(repo: Path, value: str) -> Optional[str]:
    if not value:
        return None
    p = Path(value)
    if not p.is_absolute():
        return value
    try:
        return p.relative_to(Path(repo).resolve()).as_posix()
    except ValueError:
        i = value.find("docs/")
        return value[i:] if i >= 0 else None


def _last_line(text: str) -> str:
    lines = [ln for ln in text.splitlines() if ln.strip()]
    return lines[-1] if lines else ""


def _check_report(repo: Path, path: str) -> Optional[tuple[str, str]]:
    """(report path, report text at HEAD) of a card, or None."""
    header = _split(_git(repo, "show", f"HEAD:{path}"))[0]
    rel = _report_rel(repo, _value(header, "CHECK REPORT:") or "")
    if rel is None:
        return None
    try:
        return rel, _git(repo, "show", f"HEAD:{rel}")
    except ClassifyError:
        return None


def closed_cards(repo: Path, day: str) -> list[str]:
    """ASK DESK 16: the cards whose `CHECK REPORT:` file's last line starts
    `CHECK DONE`, that file last committed on `day` (committer date)."""
    out = []
    for path in sorted(_git(repo, "ls-files", "--", PROMPTS_DIR).splitlines()):
        if not path.endswith("-card.md"):
            continue
        found = _check_report(repo, path)
        if found is None or not _last_line(found[1]).startswith("CHECK DONE"):
            continue
        if _git(repo, "log", "-1", "--format=%cs", "--", found[0]).strip() == day:
            out.append(path)
    return out


# -- outcome rows (F7) ---------------------------------------------------------------------

def _int(v: Optional[str]) -> Optional[int]:
    return int(v) if v is not None and v.strip().isdigit() else None


def _builder(header: list[str]) -> Optional[str]:
    """The build's builder from its launch record: a shadow card's JOB slug
    against SHADOW-HUB `## BUILDERS`, else BUILD-HUB.md's `--model`."""
    try:
        if _value(header, "SHADOW OF:") is not None:
            job = _value(header, "JOB:") or ""
            m = re.search(r"^## BUILDERS[ \t]*$(.*?)(?=^## |\Z)", SHADOW_HUB_PATH.read_text(), re.M | re.S)
            for ln in (m.group(1).splitlines() if m else []):
                if ln.startswith("| `"):
                    cells = [c.strip().strip("`") for c in ln.strip().strip("|").split("|")]
                    if job.endswith(f"-{cells[1]}"):
                        return cells[0]
            return None
        m = re.search(r"--model (\S+)", BUILD_HUB_PATH.read_text())
        return m.group(1) if m else None
    except OSError:
        return None


def write_outcome(repo: Path, path: str, ledger: Path, *, stage: str = "check") -> Optional[dict]:
    """One OUTCOME row from committed artifacts (design §3 step 2), only
    when the card's check report ends in a `CHECK DONE` line. Each outcome
    is stored apart, never summed (`[F-17]`); a field no committed artifact
    states is null (UNKNOWN). Appended; the decision row is never touched."""
    repo = Path(repo)
    found = _check_report(repo, path)
    if found is None:
        return None
    rel, text = found
    last = _last_line(text)
    if not last.startswith("CHECK DONE"):
        return None
    kv = {}
    for seg in last.split(" · "):
        if ": " in seg:
            k, v = seg.split(": ", 1)
            kv[k.strip()] = v.strip()
    passes = _int(kv.get("pass"))
    header = _split(_git(repo, "show", f"HEAD:{path}"))[0]
    held_rows = [ln for ln in text.splitlines()
                 if re.match(r"^\|\s*O\d+\s*\|", ln) and re.search(r"\bHELD\b", ln) and "NOT HELD" not in ln]
    row = {
        "kind": "outcome", "card_path": path, "launch_sha": launch_sha(repo, path), "stage": stage,
        "check_report": rel, "builder": _builder(header),
        "held": _int(kv.get("held")), "fixed": _int(kv.get("fixed")),
        "held_unfixed": _int(kv.get("held unfixed")), "open": _int(kv.get("open")),
        "pass": passes, "ready": kv.get("ready"), "tokens": _int(kv.get("tokens")),
        "opus_own_held": len(held_rows),
        "fix_rounds": passes - 1 if passes else None,
        "re_passes": None, "suites_first_run": None, "deploy_attempts": None,
        "at": datetime.now(timezone.utc).isoformat(),
    }
    _append(Path(ledger), row)
    return row


# -- the weekly read (F10, F11) --------------------------------------------------------------

OUTCOMES = ("opus_own_held", "fix_rounds", "re_passes", "tokens")


def _cell(values: list) -> str:
    n = len(values)
    if n < MIN_N:
        return f"n={n} insufficient data"
    return f"n={n} mean={statistics.mean(values):.3f} median={statistics.median(values):.3f}"


def _day(row: dict) -> Optional[date]:
    try:
        return datetime.fromisoformat(str(row.get("at"))).date()
    except ValueError:
        return None


def weekly_read(rows: list[dict], cfg: RouteConfig, *, week: Optional[date],
                spent: Optional[float] = None) -> str:
    """Design §5 / §6 as aggregates only (fold F8): no card path, no launch
    sha. Code computes every figure; every cell under n=30 reads
    `insufficient data` (L8). It retires nothing (fold F10)."""
    dec = [r for r in rows if r.get("kind") == "decision"]
    if week is not None:
        dec = [r for r in dec if (d := _day(r)) is not None and week <= d < week + timedelta(days=7)]
    outs = [r for r in rows if r.get("kind") == "outcome"]
    by_key = {(r.get("card_path"), r.get("launch_sha")): r for r in dec}
    joined = [(by_key[k], o) for o in outs if (k := (o.get("card_path"), o.get("launch_sha"))) in by_key]

    out = [f"# Routing read — {'week of ' + week.isoformat() if week else 'all rows'}", "",
           "Aggregates only (fold F8). Every cell under n=30 reads insufficient data (L8).", ""]
    for sha in sorted({r.get("set_sha256") for r in dec if r.get("set_sha256")}):
        rows_s = [r for r in dec if r.get("set_sha256") == sha]
        out += [f"## set {sha}", "", f"decision rows: n={len(rows_s)}", ""]
        cells: dict[tuple, list] = {}
        for d, o in joined:
            if d.get("set_sha256") == sha:
                cells.setdefault((d.get("band"), o.get("builder")), []).append(o)
        for (band, builder), os_ in sorted(cells.items(), key=lambda kv: (str(kv[0][0]), str(kv[0][1]))):
            for name in OUTCOMES:
                vals = [o[name] for o in os_ if isinstance(o.get(name), (int, float))]
                out.append(f"G1-G3 band={band} builder={builder} {name}: {_cell(vals)}")
        out.append("")

    comparable = [r for r in dec if r.get("score_band") not in (None, UNKNOWN) and r.get("band")]
    agree = sum(str(r["band"]).lower() == str(r["score_band"]).lower() for r in comparable)
    out.append(f"G4 JEV band vs score_band: {agree} of {len(comparable)} agree "
               f"(UNKNOWN score bands left out; decision rows n={len(dec)})")
    for band in (*BANDS, "unsure"):
        rb = [r["rows_band"] for r in dec if r.get("band") == band and isinstance(r.get("rows_band"), int)]
        out.append(f"- G4 rows_band at JEV band={band}: n={len(rb)}"
                   + (f" median rows={statistics.median(rb):g}" if rb else ""))
    off = sum(1 for r in dec if r.get("model") and r.get("model") != OPUS)
    out.append(f"G5 decision rows naming a model other than {OPUS}: {off} of {len(dec)}")
    cost = sum(r.get("cost_usd") or 0.0 for r in dec)
    out.append(f"G6 spend: decision rows ${cost:.8f}; spend ledger "
               + (f"${spent:.8f}" if spent is not None else "not read")
               + f" of cap ${cfg.spend_cap_usd:g}")
    both = [r for r in dec if r.get("band") and r.get("card_band")]
    same = [r for r in both if str(r["band"]).lower() == str(r["card_band"]).lower()]
    out.append(f"G7 JEV band vs card_band: {len(same)} of {len(both)} agree (n={len(both)})")
    for band in (*BANDS, "unsure"):
        b = [r for r in both if r["band"] == band]
        a = sum(str(r["band"]).lower() == str(r["card_band"]).lower() for r in b)
        out.append(f"- G7 JEV band={band}: {a} of {len(b)} agree (n={len(b)})")
    out.append("")

    ret = cfg.retire
    eligible = [(d, o) for d, o in joined
                if d.get("set_sha256") == ret.set_sha256 and (dd := _day(d)) is not None and dd >= ret.declared]
    for name in ret.outcomes:
        n = sum(isinstance(o.get(name), (int, float)) for _, o in eligible)
        tail = "insufficient data" if n < MIN_N else "eligible; the declared method's comparison is a card"
        out.append(f"retire comparison {name} (set {ret.set_sha256}, rows on or after "
                   f"{ret.declared.isoformat()}): n={n} {tail}")
    return "\n".join(out) + "\n"


def write_read(text: str, out_dir: Path, week: date) -> Path:
    p = Path(out_dir) / f"routing-read-{week.isoformat()}.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text)
    return p


def _ledger_rows(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(ln) for ln in path.read_text().splitlines() if ln.strip()]


# -- the commands -------------------------------------------------------------------------

def _dry(router: Router, path: str, card: CardText) -> tuple[str, float]:
    body = router.body(router.qset, router.item(card))
    try:
        router._guard_outbound(body, keyed=False)
        status = "ok"
    except ClassifyError:
        status = "refused"
    usd = router.project(body)
    return (f"ROUTE DRY card={path} launch={card.launch_sha} bytes={len(body)} "
            f"tokens_est={math.ceil(len(body) / 4)} projected_usd={usd:.8f} guard={status}"), usd


def cmd_route(args: argparse.Namespace) -> int:
    """`--dry-run` renders, guards and projects ONE call per card — zero
    network. `--run` is KEYED and METERED (never run by build 591)."""
    cfg = load_route_config()
    repo = Path(args.repo) if args.repo else cfgmod.REPO_ROOT
    paths = list(args.card) if args.card else closed_cards(repo, args.day)
    router = Router(cfg)
    if args.dry_run:
        total = 0.0
        for path in paths:
            line, usd = _dry(router, path, load_card(repo, path))
            total += usd
            print(line)
        print(f"ROUTE DRY TOTAL cards={len(paths)} calls={len(paths) * args.reps} "
              f"projected_usd={total * args.reps:.8f} (nothing sent)")
        return 0
    cards = [load_card(repo, p) for p in paths for _ in range(args.reps)]
    rows = run_batch(router, cards, wall_clock_s=cfg.batch_wall_clock_s)
    counts: dict[str, int] = {}
    for r in rows:
        counts[r.status] = counts.get(r.status, 0) + 1
    print(f"ROUTE RUN cards={len(rows)} " + " ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


def cmd_route_read(args: argparse.Namespace) -> int:
    cfg = load_route_config()
    week = date.fromisoformat(args.week)
    spent = Ledger(Path(cfg.spend_ledger), cap_usd=cfg.spend_cap_usd, call_ceiling=cfg.call_ceiling,
                   carried=[c.cost_usd for c in cfg.carried_spend]).spent()
    text = weekly_read(_ledger_rows(Path(cfg.routing_ledger)), cfg, week=week, spent=spent)
    out_dir = Path(args.out_dir) if args.out_dir else cfgmod.REPO_ROOT / REPORTS_DIR
    print(f"ROUTE READ wrote={write_read(text, out_dir, week)}")
    return 0


def add_route_parsers(csub) -> None:
    r = csub.add_parser("route", help="JEV shadow router: --dry-run (nothing sent) or --run (KEYED, METERED).")
    which = r.add_mutually_exclusive_group(required=True)
    which.add_argument("--card", nargs="+", help="repo-relative card path(s)")
    which.add_argument("--day", help="YYYY-MM-DD: the cards whose check closed that day")
    how = r.add_mutually_exclusive_group(required=True)
    how.add_argument("--dry-run", dest="dry_run", action="store_true")
    how.add_argument("--run", action="store_true")
    r.add_argument("--reps", type=int, default=1)
    r.add_argument("--repo", default=None, help="the checkout the cards are read from (default: this one)")
    r.set_defaults(func=cmd_route)

    rr = csub.add_parser("route-read", help="The weekly read of the routing ledger (aggregates only).")
    rr.add_argument("--week", required=True, help="YYYY-MM-DD, the week's first day")
    rr.add_argument("--out-dir", dest="out_dir", default=None)
    rr.set_defaults(func=cmd_route_read)


__all__ = [
    "CardText",
    "RouteConfig",
    "Router",
    "add_route_parsers",
    "closed_cards",
    "launch_sha",
    "load_card",
    "load_route_config",
    "run_batch",
    "score",
    "status_of",
    "weekly_read",
    "write_outcome",
    "write_read",
]
