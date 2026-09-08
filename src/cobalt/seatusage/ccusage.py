"""The ccusage collector — a deterministic tool fetch, nothing more.

TOOLS FETCH, AGENTS REASON. This module runs one pinned binary over the
harness logs already on this disk, validates what comes back into typed
rows, and stops. There is no model in this path and no arithmetic beyond
summing what the tool reported.

THE FOUR GATES (L15), answered where they can be checked rather than
where they can be claimed:

* PROVEN — a widely used tool (~59k npm downloads in the week to
  2026-09-06), pinned to an exact version in `configs/cobalt/
  seat_usage.yaml` and re-checked against `--version` on every run.
* CONFORMANT — read-only over `~/.claude`, `~/.codex` and the other
  harness log trees; it opens no Cobalt database, writes no vault note,
  and is never given a path to write to. It is `subprocess.run` with a
  fixed argv, never a shell string.
* INDUSTRY-STANDARD — MIT, zero declared runtime dependencies, one bin.
* REVIEWED-CLEAN — installed into `~/.npm-global`, outside both the repo
  and the system prefix, so an install can be inspected and removed
  whole.

NO NETWORK AT RUN TIME. `--offline` prices from ccusage's bundled table
instead of fetching the live pricing DB. That is the gate — and it has a
consequence this module refuses to paper over: on 2026-09-08 the bundled
table had no entry for `claude-fable-5-1` and priced $17.32 of real
usage at exactly $0.00. A used model showing zero is a plausible-empty
artifact, so a model with tokens and no price comes back as UNPRICED
(`cost=None`), never as zero, and the day's total is a FLOOR. A model
that is genuinely free is named in the config's `zero_cost_models` and
keeps its honest $0.
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass, field
from datetime import date
from typing import Optional

from .config import SeatUsageConfig


class CcusageError(RuntimeError):
    """The tool is missing, mis-pinned, or answered something unusable."""


@dataclass(frozen=True)
class ModelUsage:
    """One model's day, as the tool observed it."""

    model: str
    cache_read: int
    cache_write: int
    input_tokens: int
    output_tokens: int
    #: None means UNPRICED — the tool reported no price for a model that
    #: was used. Never conflated with a true 0.0 (see `free`).
    cost: Optional[float]
    #: True when the config declares this model genuinely free.
    free: bool = False
    #: The harness seats this model was observed under. Observed, not
    #: configured — this is the honest half of the role-hint column.
    seats: tuple[str, ...] = ()

    @property
    def total_tokens(self) -> int:
        return self.cache_read + self.cache_write + self.input_tokens + self.output_tokens

    @property
    def unpriced(self) -> bool:
        return self.cost is None


@dataclass
class DayUsage:
    """One day. `models` is sorted by cost, dearest first."""

    day: date
    models: list[ModelUsage] = field(default_factory=list)
    #: Models used with no price in the bundled table. Loud, once a day.
    unpriced: list[str] = field(default_factory=list)
    #: Seats the tool detected logs for at all.
    seats: tuple[str, ...] = ()
    tool_version: str = ""

    @property
    def priced_total(self) -> float:
        """The sum of what IS priced. A FLOOR whenever `unpriced` is
        non-empty, and every caller that prints it says so."""
        return sum(m.cost for m in self.models if m.cost is not None)

    @property
    def total_tokens(self) -> int:
        return sum(m.total_tokens for m in self.models)


def tool_version(cfg: SeatUsageConfig) -> str:
    """What the pinned binary actually reports. Fail-loud if it is not
    there — "ccusage is not installed" and "nobody used a seat today"
    must never render the same way."""
    binary = cfg.tool.binary_path
    if not binary.exists():
        raise CcusageError(
            f"{cfg.tool.name} is not installed at {binary}. The seat-usage report "
            "runs one PINNED binary and never resolves one off PATH: install it "
            f"with `npm install -g --prefix ~/.npm-global {cfg.tool.name}@"
            f"{cfg.tool.version}`."
        )
    try:
        proc = subprocess.run(
            [str(binary), "--version"], capture_output=True, text=True, timeout=30
        )
    except (OSError, subprocess.SubprocessError) as e:
        raise CcusageError(f"could not run {binary}: {type(e).__name__}: {e}") from e
    if proc.returncode != 0:
        raise CcusageError(
            f"{binary} --version exited {proc.returncode}: "
            f"{proc.stderr.strip() or '(no stderr)'}"
        )
    # "ccusage 20.0.20" -> "20.0.20"
    return proc.stdout.strip().split()[-1]


def assert_pinned(cfg: SeatUsageConfig) -> str:
    """The installed version IS the pinned version, or crash.

    A silent bump is the failure this check exists for: the numbers keep
    coming, the shape of them changes, and the first anyone knows is a
    column that stopped meaning what it meant.
    """
    found = tool_version(cfg)
    if found != cfg.tool.version:
        raise CcusageError(
            f"{cfg.tool.name} is pinned to {cfg.tool.version} in "
            f"configs/cobalt/seat_usage.yaml but {cfg.tool.binary_path} reports "
            f"{found}. Either re-pin the config deliberately (and re-read the "
            "column meanings) or reinstall the pinned version — a job does not "
            "get to decide this on its own (L15)."
        )
    return found


def argv(cfg: SeatUsageConfig, day: date) -> list[str]:
    """The exact command. Kept as a function so the report can print the
    argv it actually ran, and so the tests can assert on it."""
    args = [
        str(cfg.tool.binary_path),
        "daily",
        "--json",
        "--breakdown",
        "--since",
        day.strftime("%Y%m%d"),
        "--until",
        day.strftime("%Y%m%d"),
        # Observed seats — the honest half of the role-hint column. It
        # adds a dimension to the SAME rows; it changes no number.
        "--by-agent",
    ]
    if cfg.tool.offline:
        args.append("--offline")
    return args


def fetch_raw(cfg: SeatUsageConfig, day: date, *, timeout: float = 120.0) -> dict:
    """Run the tool and return its parsed JSON. Read-only, no shell."""
    command = argv(cfg, day)
    try:
        proc = subprocess.run(command, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired as e:
        raise CcusageError(
            f"{cfg.tool.name} did not finish within {timeout:.0f}s over the harness "
            "logs — the report is not written rather than written from half a day."
        ) from e
    except (OSError, subprocess.SubprocessError) as e:
        raise CcusageError(f"could not run {cfg.tool.name}: {type(e).__name__}: {e}") from e
    if proc.returncode != 0:
        raise CcusageError(
            f"{cfg.tool.name} exited {proc.returncode}: "
            f"{proc.stderr.strip()[:400] or '(no stderr)'}"
        )
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as e:
        raise CcusageError(
            f"{cfg.tool.name} did not return JSON ({e}). First 200 bytes: "
            f"{proc.stdout[:200]!r}"
        ) from e


def parse(cfg: SeatUsageConfig, raw: dict, day: date, *, version: str = "") -> DayUsage:
    """Typed rows from the tool's JSON. Pure — the tests drive it from a
    fixture, which is the whole reason it is separate from `fetch_raw`."""
    if not isinstance(raw, dict) or "daily" not in raw:
        raise CcusageError(
            "unexpected ccusage output: no `daily` key. The pinned version's "
            "output shape is part of what the pin is protecting."
        )
    wanted = day.isoformat()
    rows = [r for r in raw.get("daily") or [] if r.get("period") == wanted]
    usage = DayUsage(day=day, tool_version=version)
    if not rows:
        # A day with no seat activity is a real, reportable answer. It is
        # NOT an error and it is NOT an empty file — the caller writes a
        # table that says so in words.
        return usage
    row = rows[0]
    usage.seats = tuple(sorted((row.get("metadata") or {}).get("agents") or []))

    # model -> the seats it was observed under
    seats_by_model: dict[str, set[str]] = {}
    for agent_row in row.get("agents") or []:
        seat = agent_row.get("agent")
        for m in agent_row.get("modelBreakdowns") or []:
            if seat:
                seats_by_model.setdefault(m.get("modelName", ""), set()).add(seat)

    for m in row.get("modelBreakdowns") or []:
        name = m.get("modelName") or "(unnamed)"
        cache_read = int(m.get("cacheReadTokens") or 0)
        cache_write = int(m.get("cacheCreationTokens") or 0)
        inp = int(m.get("inputTokens") or 0)
        out = int(m.get("outputTokens") or 0)
        raw_cost = m.get("cost")
        cost = float(raw_cost) if raw_cost is not None else None
        free = cfg.is_free(name)
        used = (cache_read + cache_write + inp + out) > 0

        # THE SILENT-ZERO GUARD. A used model priced at exactly zero, that
        # the config does not declare free, is a HOLE in the bundled
        # pricing table — not a free model. Reported as unpriced.
        if cfg.unpriced_is_loud and used and not free and (cost is None or cost == 0.0):
            cost = None
            usage.unpriced.append(name)

        usage.models.append(
            ModelUsage(
                model=name,
                cache_read=cache_read,
                cache_write=cache_write,
                input_tokens=inp,
                output_tokens=out,
                cost=cost,
                free=free,
                seats=tuple(sorted(seats_by_model.get(name, ()))),
            )
        )

    # Dearest first; unpriced rows sort to the top, because an unknown
    # number is the one a reader should see before any known one.
    usage.models.sort(key=lambda m: (m.cost is not None, m.cost or 0.0), reverse=True)
    usage.unpriced.sort()
    return usage


def collect(cfg: SeatUsageConfig, day: date) -> DayUsage:
    """Gate, run, parse. The one entry point the job calls."""
    version = assert_pinned(cfg)
    return parse(cfg, fetch_raw(cfg, day), day, version=version)


__all__ = [
    "CcusageError",
    "DayUsage",
    "ModelUsage",
    "argv",
    "assert_pinned",
    "collect",
    "fetch_raw",
    "parse",
    "tool_version",
]
