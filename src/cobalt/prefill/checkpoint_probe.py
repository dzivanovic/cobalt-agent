"""`cobalt checkpoint probe <item>`: one F5 first-gate item, dev only (card 973; F5 FINAL `## First-gate experiments`).

THE OUTPUT is ONE stdout line: `PROBE <item> OK <clause>` (exit 0),
`PROBE <item> FAIL <clause>` (exit 1) or `PROBE <item> NOT RUN — <reason>`
(exit 3). A clause carries names, counts, slot ids, status kinds and phrase
ids only: never model text, a figure, note text, a token or an env value.

THE BOUNDARY, every item:
(a) DEV ONLY: `env.resolve_env()` must say `dev`; anything else is a FAIL
    line before anything is fetched or called.
(b) SCRATCH: the item runs with its cwd in `tempfile.mkdtemp(prefix="f5-probe-")`,
    refused when that is, or sits under, the repo, `~/.claude` or the
    resolved vault; removed in a `finally`.
(c) NO WRITE: no `VaultWriter`, no `ensure_daily_note`, no store (no
    database), no DM, no `as_job`, no `launchctl`, no plist. The one file
    written outside the scratch is X6's `--keep-groups` body (row G1). A
    secret-shaped hit inside `redact` (G1's check, or the guard X6's real
    `call_sync` path runs) is counted as F19 counts every hit.
(d) A crash is `FAIL error <ExceptionName>`, no message text.

THE ITEMS (F5-FINAL `:178-187`):
X6  four real-shape prompts through `narrate`, the guard inside `call_sync`
    (`:180`): one real fetch is 08:45's figures, 07:15-08:15 derived by
    rule D (DECISION 2).
X4  twenty generations, the four prompts x 5, through the [F-08] schema
    (`:178`); below 15 valid or a number-word is FAIL, never a load block.
    The sectors are a real Groups body read from disk (row (b)'s fixture,
    else X6's kept capture), the indices constructed (card 989): 20 model
    calls, no gate check, no GET.
X13 the window rule refuses a late fire on every slot, in process (`:187`);
    the launchd leg is not run.
X5, X7, X10 need his hand: NOT RUN, nothing called.
"""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import tempfile
from collections import Counter
from contextlib import contextmanager
from datetime import datetime, timedelta
from decimal import Decimal
from pathlib import Path
from typing import Callable, Optional

from loguru import logger

from cobalt import env
from cobalt.modelaccess import ModelCallError, ModelMessage, ModelRequest, load_routes
from cobalt.prefill import checkpoints
from cobalt.prefill.checkpoints import PROBE_ITEMS
from cobalt.redact import redact
from cobalt.session import SessionClock
from cobalt.session import clock as clock_mod

REPO_ROOT = Path(__file__).resolve().parents[3]
#: G1: the one place a kept Groups body may be written.
KEEP_ROOT = Path("/Users/cobalt/cobalt-wt/.f5-probe")
#: X6: the slot the one gate check names (the 970 dry run's slot).
GATE_SLOT = "07:45"
#: X4's Groups body, the first present: card 973 row (b)'s fixture, then X6's `--keep-groups` capture. Read only.
X4_GROUPS_FIXTURE = REPO_ROOT / "tests/cobalt/fixtures/checkpoints/groups_sector_v140_real.csv"
X4_GROUPS_KEPT = KEEP_ROOT / "groups_sector_v140_real.csv"
#: X4's indices (card 989, DECISION 3): constructed (price, change %), never fetched.
X4_INDICES = {"SPY": ("500.00", "0.10"), "QQQ": ("430.00", "0.20"), "IWM": ("200.00", "-0.10")}
#: Rule D (DECISION 2): per slot back, an index price falls 0.50 and its change % 0.10.
PRICE_STEP, CHANGE_STEP = Decimal("0.50"), Decimal("0.10")
#: X4 (FINAL :178): 4 prompts x 5 = 20 generations; 15 valid is the bar.
GENERATIONS_PER_PROMPT = 5
VALID_BAR = 15
#: X4's number-words (drafter DECISION 4).
NUMBER_WORDS = frozenset((
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
    "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty",
    "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand", "million", "billion",
    "half", "quarter", "dozen", "percent",
))
HIS_LEGS = {
    "X5": "a window with scripted voice local.plan calls (his voice may be slow)",
    "X7": "Obsidian open on a dev vault copy; the offline leg is the gate run's pytest",
    "X10": "Obsidian Sync on a dev vault copy",
}
OK, FAIL, NOT_RUN = "OK", "FAIL", "NOT RUN"
EXIT = {OK: 0, FAIL: 1, NOT_RUN: 3}
_WORD_SPLIT = re.compile(r"[^a-z]+")


class ProbeRefused(RuntimeError):
    """The probe will not run here. Loud, as a FAIL line."""


class NotRun(RuntimeError):
    """The item cannot run its real shape here: a NOT RUN line, exit 3."""


# ---------------------------------------------------------------------
# the boundary
# ---------------------------------------------------------------------


def _dev_only() -> None:
    try:
        mode = env.resolve_env()
    except env.EnvConfigError as e:
        raise ProbeRefused(str(e).split(". ")[0] + ".") from None
    if mode != env.DEV:
        raise ProbeRefused(f"{env.ENV_VAR}={mode} (dev only)")


def _under(path: Path, root: Path) -> bool:
    return path == root or root in path.parents


def _forbidden() -> list[tuple[str, Path]]:
    from cobalt.vault import resolve_vault_path

    return [("the repo", REPO_ROOT), ("~/.claude", (Path.home() / ".claude").resolve()),
            ("the vault", resolve_vault_path().resolve())]


@contextmanager
def _scratch():
    root = Path(tempfile.mkdtemp(prefix="f5-probe-")).resolve()
    cwd = os.getcwd()
    try:
        for name, forbidden in _forbidden():
            if _under(root, forbidden):
                raise ProbeRefused(f"the scratch dir is under {name}")
        os.chdir(root)
        yield root
    finally:
        os.chdir(cwd)
        shutil.rmtree(root, ignore_errors=True)


@contextmanager
def _at_repo():
    """The Finviz leg's cwd: the old tree resolves `configs/` and
    `data/.cobalt_vault` against the cwd (`cobalt_agent/config.py:543`,
    `security/vault.py:19`), which the scratch does not hold (card 989)."""
    cwd = os.getcwd()
    try:
        os.chdir(REPO_ROOT)
        yield REPO_ROOT
    finally:
        os.chdir(cwd)


def _keep_target(item: str, raw: Optional[str]) -> Optional[Path]:
    """G1: `--keep-groups PATH`, X6 only, a new file under `KEEP_ROOT`."""
    if raw is None:
        return None
    if item != "X6":
        raise ProbeRefused("--keep-groups is X6's")
    path = Path(raw)
    target = path.parent.resolve() / path.name
    if not path.is_absolute() or KEEP_ROOT.resolve() not in target.parents:
        raise ProbeRefused(f"--keep-groups PATH must be under {KEEP_ROOT}/")
    if not path.parent.is_dir():
        raise ProbeRefused("--keep-groups PATH's parent is not a directory")
    if path.exists():
        raise ProbeRefused("--keep-groups PATH exists (no overwrite)")
    for name, forbidden in _forbidden():
        if _under(target, forbidden):
            raise ProbeRefused(f"--keep-groups PATH is under {name}")
    return path


def _keep(path: Path, body: str, now: datetime) -> str:
    """The marker line, the CSV header and the eleven sector rows as sent;
    any other line dropped. A secret-shaped hit writes nothing."""
    lines = body.splitlines()
    header_at, name_col, rows = None, None, []
    for i, line in enumerate(lines):
        cells = next(csv.reader([line]), [])
        if header_at is None:
            if "Name" in cells:
                header_at, name_col = i, cells.index("Name")
        elif len(cells) > name_col and cells[name_col].strip() in checkpoints.SECTORS:
            rows.append(line)
    if header_at is None or len(rows) != len(checkpoints.SECTORS):
        return "kept: refused (not a header and 11 rows)"
    kept = [f"# real capture {now:%Y-%m-%d %H:%M} ET, dev probe X6, header and 11 rows only (L45)",
            lines[header_at], *rows]
    hits = redact("\n".join(kept), channel="modelaccess").hits
    if hits:
        return f"kept: refused (secret-shaped: {', '.join(sorted(hits))})"
    with open(path, "x", encoding="utf-8") as f:
        f.write("\n".join(kept) + "\n")
    return f"kept: {path}"


# ---------------------------------------------------------------------
# the figures and the four prompts (X6, X4)
# ---------------------------------------------------------------------


def _real_figures(cfg, keep: Optional[Callable[[str], None]]) -> dict:
    """ONE gate check, then ONE `fetch_figures`, both at the repo root: both
    sources ok, or NOT RUN."""
    with _at_repo():
        refusal = checkpoints.check_demand(GATE_SLOT)
        if refusal is not None:
            raise NotRun(f"Finviz gate: {refusal}")
        figures, status = checkpoints.fetch_figures(cfg, keep=keep)
    for source in (checkpoints.SCREENER, checkpoints.GROUPS):
        if status[source] != checkpoints.OK:
            raise NotRun(f"{source} degraded")
    return figures


def _step(raw: str, by: Decimal) -> str:
    value = Decimal(raw)
    return str((value - by).quantize(Decimal(1).scaleb(value.as_tuple().exponent)))


def derive(real: dict, k: int) -> dict:
    """Rule D: the figures `k` slots before the real fetch. Index price minus
    k x 0.50 and change % minus k x 0.10 at the figure's own exponent; each
    sector takes the real Change of the sector k places on in `SECTORS`
    (the `f5-x3-measure-2026-10-20.md:69` rotation)."""
    names = list(checkpoints.SECTORS)
    sectors = real["sectors"]
    return {
        "indices": {t: {"price": _step(f["price"], k * PRICE_STEP),
                        "change_pct": _step(f["change_pct"], k * CHANGE_STEP)}
                    for t, f in real["indices"].items()},
        "sectors": {n: dict(sectors[n], change=sectors[names[(i + k) % len(names)]]["change"])
                    for i, n in enumerate(names)},
    }


def _prompts(cfg, real: dict) -> list[tuple[str, list[dict]]]:
    """(slot, delta lines): 07:15 vs prior close, then each slot vs the one before."""
    s = [derive(real, 3 - i) for i in range(4)]
    pairs = [(s[0], None), (s[1], s[0]), (s[2], s[1]), (s[3], s[2])]
    return [(hhmm.replace(":", ""), checkpoints.compute_delta(figs, base)["lines"])
            for hhmm, (figs, base) in zip(cfg.slots, pairs, strict=True)]


def _request(cfg, entries: list[dict], request_id: str) -> tuple[ModelRequest, str]:
    """The request `narrate` builds for `entries`, and its `prompt_sha256`."""
    payload = [{"ref": i, "phrase": e["phrase"], "text": e["text"]} for i, e in enumerate(entries)]
    messages = [
        ModelMessage(role="system", content=checkpoints._SYSTEM),
        ModelMessage(role="user", content=json.dumps(payload, ensure_ascii=False)),
    ]
    sha = hashlib.sha256(json.dumps([m.model_dump() for m in messages], sort_keys=True).encode()).hexdigest()
    req = ModelRequest(route=cfg.route, caller=checkpoints.WRITER, request_id=request_id, messages=messages,
                       response_schema=checkpoints._response_schema(cfg.narrative_max_lines))
    return req, sha


def _now_et() -> datetime:
    return SessionClock.to_et(clock_mod.now_utc())


# ---------------------------------------------------------------------
# the items
# ---------------------------------------------------------------------


def _x6(cfg, keep_path: Optional[Path]) -> tuple[str, str]:
    """X6 (FINAL :180): any `prompt_refused` over four real-shape prompts."""
    from cobalt.daymode.note import daily_note_path

    now = _now_et()
    if not daily_note_path(now.date()).exists():
        raise NotRun(f"no daily note for {now.date()} in the dev vault (checkpoints.py:747-751)")
    bodies: list[str] = []
    real = _real_figures(cfg, bodies.append if keep_path is not None else None)
    routes = load_routes()
    statuses = {slot: checkpoints.narrate(cfg, entries, request_id=f"f5-probe-x6-{slot}", config=routes).status
                for slot, entries in _prompts(cfg, real)}
    refused = [s for s, v in statuses.items() if v == "degraded (prompt_refused)"]
    empty = [s for s, v in statuses.items() if v == "degraded (empty delta)"]
    clause = (f"figures: 1 real fetch + 3 derived by rule D · prompts {len(statuses)} · "
              f"prompt_refused {len(refused)} · " + " · ".join(f"{s} {v}" for s, v in statuses.items()))
    if keep_path is not None:
        clause += " · " + (_keep(keep_path, bodies[-1], now) if bodies else "kept: refused (no body seen)")
    if refused:
        return FAIL, f"— prompt_refused {len(refused)} of {len(statuses)} ({', '.join(refused)}) · {clause}"
    if empty:
        return FAIL, f"— empty delta {len(empty)} of {len(statuses)} ({', '.join(empty)}) · {clause}"
    return OK, clause


def _has_number_word(text: str) -> bool:
    return any(w in NUMBER_WORDS for w in _WORD_SPLIT.split(text.lower()))


def _x4_figures(cfg) -> tuple[dict, str]:
    """X4's figures and the Groups source's name: the sectors from the first
    present real Groups body (its `#` lines dropped), the indices
    `X4_INDICES`. No gate check, no token, no GET."""
    for path, source in ((X4_GROUPS_FIXTURE, "row (b) fixture"), (X4_GROUPS_KEPT, "kept capture")):
        if path.is_file():
            break
    else:
        raise NotRun("no real Groups body (X6 --keep-groups capture or the row (b) fixture)")
    text = path.read_text(encoding="utf-8")
    try:
        sectors = checkpoints.parse_groups("\n".join(line for line in text.split("\n") if not line.startswith("#")))
    except checkpoints.GroupsShapeError:
        raise NotRun("the Groups body is not the 11 sector rows") from None
    lacking = [t for t in cfg.indices if t not in X4_INDICES]
    if lacking:
        raise NotRun(f"X4_INDICES lacks {lacking[0]}")
    indices = {t: {"price": X4_INDICES[t][0], "change_pct": X4_INDICES[t][1]} for t in cfg.indices}
    return {"indices": indices, "sectors": sectors}, source


def _x4(cfg, _keep_path: Optional[Path]) -> tuple[str, str]:
    """X4 (FINAL :178): 20 generations; valid >= 15 of 20 and no number-word."""
    real, source = _x4_figures(cfg)
    routes = load_routes()
    total, valid, invalid, hits = 0, 0, Counter(), Counter()
    for slot, entries in _prompts(cfg, real):
        for n in range(1, GENERATIONS_PER_PROMPT + 1):
            total += 1
            if not entries:
                invalid["empty delta"] += 1
                continue
            req, _ = _request(cfg, entries, f"f5-probe-x4-{slot}-{n}")
            try:
                result = checkpoints.call_sync(req, config=routes)
                checkpoints.validate_reply(result.content, entries, cfg.narrative_max_lines)
            except ModelCallError as e:
                invalid[e.kind] += 1
                continue
            except checkpoints.UnsourcedFigure:
                invalid["UnsourcedFigure"] += 1
                continue
            valid += 1
            for line in json.loads(result.content)["lines"]:
                if any(_has_number_word(s) for s in checkpoints._strings(line)):
                    hits[line["phrase_id"]] += 1
    clause = " · ".join([
        f"groups: {source}",
        "indices: constructed",
        f"valid {valid}/{total}",
        "invalid kinds " + (", ".join(f"{k}={v}" for k, v in sorted(invalid.items())) or "none"),
        "number-word hits " + (", ".join(f"{k}={v}" for k, v in sorted(hits.items())) or "none"),
    ])
    if valid >= VALID_BAR and not hits:
        return OK, clause
    if valid < VALID_BAR:
        clause += " → narrative degraded-by-default (FINAL :178)"
    for phrase in sorted(hits):
        clause += f" → {phrase} removed from the enum (FINAL :178)"
    return FAIL, clause + "; plist load not blocked by X4"


class _NeverReached:
    """X13's stores: the refusal returns before any store is touched."""

    def __getattr__(self, name):
        raise ProbeRefused(f"X13 reached a store ({name})")


class _TradingDay:
    def is_trading_day(self, day) -> bool:
        return True

    def describe(self, day) -> str:
        return f"{day}: a trading day (probe stub)"


def _x13(cfg, _keep_path: Optional[Path]) -> tuple[str, str]:
    """X13 (FINAL :187): each slot fired at its window close + 5 min is refused,
    exit 2. A window the rule admits fails before `run_checkpoint` (no fetch)."""
    today = _now_et().date()
    for hhmm in cfg.slots:
        closes = checkpoints._window(cfg, hhmm)[1]
        late = checkpoints.slot_instant(today, closes) + timedelta(minutes=5)
        if checkpoints.window_refusal(cfg, hhmm, late) is None:
            return FAIL, f"— {hhmm} admitted at close + 5 min by window_refusal (run_checkpoint not called)"
        result = checkpoints.run_checkpoint(hhmm.replace(":", ""), late, dry_run=False, store=_NeverReached(),
                                            vault_store=_NeverReached(), calendar=_TradingDay())
        expected = f"REFUSED: slot {hhmm} window closed at {closes}"
        if result.action != "refused" or result.exit_code != 2 or expected not in result.failures:
            return FAIL, f"— {hhmm} {result.action} exit {result.exit_code}"
    n = len(cfg.slots)
    return OK, (f"(offline: the window rule refuses a late fire on {n} of {n} slots; "
                "launchd leg not run, no plist loaded)")


ITEMS: dict[str, Callable] = {"X4": _x4, "X6": _x6, "X13": _x13}
assert set(ITEMS) | set(HIS_LEGS) == set(PROBE_ITEMS), "checkpoints.PROBE_ITEMS and the probe's items disagree"


def _verdict(item: str, keep_groups: Optional[str]) -> tuple[str, str]:
    # narrate logs a dropped reply's strings; the probe's line carries kinds only.
    logger.disable("cobalt.prefill.checkpoints")
    try:
        _dev_only()
        keep_path = _keep_target(item, keep_groups)
        with _scratch():
            if item in HIS_LEGS:
                raise NotRun(f"needs his hand: {HIS_LEGS[item]}")
            return ITEMS[item](checkpoints.load_checkpoints_config(), keep_path)
    except ProbeRefused as e:
        return FAIL, f"refused: {e}"
    except NotRun as e:
        return NOT_RUN, f"— {e}"
    except Exception as e:  # noqa: BLE001 - a crash is a FAIL line; its message may carry fetched text
        return FAIL, f"error {type(e).__name__}"
    finally:
        logger.enable("cobalt.prefill.checkpoints")


def main(item: str, *, keep_groups: Optional[str] = None) -> int:
    verdict, clause = _verdict(item, keep_groups)
    clause = " ".join(clause.split())
    print(f"PROBE {item} {verdict} {clause}")
    return EXIT[verdict]


__all__ = ["HIS_LEGS", "ITEMS", "KEEP_ROOT", "NUMBER_WORDS", "derive", "main"]
