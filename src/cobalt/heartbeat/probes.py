"""F18's probes — one function per question, each answering honestly.

Charter §3 F18: "services alive · archiver freshness · every ops plist
loaded + last exit code · Obsidian running; red/green to daily note + DM;
red also out-of-band."

THE RULE EVERY PROBE HERE KEEPS. "The probe broke" and "the thing is
down" are different facts, and collapsing them is how a red condition
becomes invisible. A probe that cannot run returns UNKNOWN, and UNKNOWN
is RED — because a heartbeat that says green when it did not look is
worse than no heartbeat at all.
"""

from __future__ import annotations

import socket
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Optional
from urllib import request as urlrequest

from cobalt.session import clock as clock_mod


@dataclass
class Probe:
    """One answered question."""

    name: str
    ok: bool
    detail: str
    #: True when the probe could not run. Still red — but an operator
    #: needs to know they are looking at ignorance, not at a diagnosis.
    unknown: bool = False

    def line(self) -> str:
        mark = "OK  " if self.ok else ("??  " if self.unknown else "RED ")
        return f"{mark} {self.name:<24} {self.detail}"


def _tunable(key: str):
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(key)
    if row is None:
        raise RuntimeError(
            f"tunable {key!r} is missing from tunables.yaml — the heartbeat reads "
            "its thresholds from config and has no built-in defaults (F16)."
        )
    return row.value


def probe_timeout_s() -> float:
    return float(_tunable("heartbeat.probe_timeout_s"))


# ---------------------------------------------------------------------


def sheet_http(url: str = "http://127.0.0.1:5010/") -> Probe:
    """The ASET sheet answers 200.

    NOT the same question as "the process exists", and S1-P2 is why this
    is a separate probe: reshaping `configs/cobalt/aset.yaml` took the
    running sheet to HTTP 500 while the process stayed perfectly alive
    and launchd stayed perfectly happy. The thing he trades beside is the
    PAGE, not the PID.
    """
    try:
        with urlrequest.urlopen(url, timeout=probe_timeout_s()) as resp:
            code = resp.status
        if code == 200:
            return Probe("sheet HTTP", True, f"{url} -> 200")
        return Probe("sheet HTTP", False, f"{url} -> {code} (expected 200)")
    except Exception as e:  # noqa: BLE001
        return Probe("sheet HTTP", False, f"{url} unreachable: {type(e).__name__}: {e}")


def database(db_name: Optional[str] = None) -> Probe:
    """`cobalt_brain` (or whatever COBALT_ENV resolves) answers a query."""
    from cobalt import db, env

    name = db_name or env.resolve_db_name()
    try:
        with db.connect(name) as conn:
            row = conn.execute("SELECT 1").fetchone()
        if row and row[0] == 1:
            return Probe("database", True, f"{name} reachable")
        return Probe("database", False, f"{name} answered {row!r} to SELECT 1")
    except Exception as e:  # noqa: BLE001
        return Probe("database", False, f"{name} unreachable: {type(e).__name__}: {e}")


def obsidian() -> Probe:
    """Obsidian is running — RULING 6, and not a cosmetic check.

    The vault reaches his other devices only through a RUNNING Obsidian
    on this Mac. On 2026-09-04 a correct 05:15 write was silently
    overwritten by the trading PC's template because none was running
    here. This reads the SAME `cobalt.obsidian.sync_status()` the vault
    writer reads, so the two can never disagree about the wording.
    """
    from cobalt import obsidian as obsidian_mod

    try:
        running, message = obsidian_mod.sync_status()
    except obsidian_mod.ObsidianProbeError as e:
        return Probe("obsidian", False, f"PROBE FAILED — sync state UNKNOWN: {e}", unknown=True)
    return Probe("obsidian", running, message)


def mainframe(host: str = "127.0.0.1", port: int = 1234) -> Probe:
    """The local model server accepts a connection (L23's local lane)."""
    try:
        with socket.create_connection((host, port), timeout=probe_timeout_s()):
            return Probe("mainframe", True, f"{host}:{port} accepting connections")
    except Exception as e:  # noqa: BLE001
        return Probe("mainframe", False, f"{host}:{port} refused: {type(e).__name__}")


def archiver_freshness(store=None, now: Optional[datetime] = None) -> Probe:
    """Last run + rows written, against `heartbeat.archiver_max_age_min`.

    Both halves matter and the second is the one that would otherwise be
    missed: an archiver that runs nightly and writes ZERO rows is exiting
    0, looks green in every state column, and is quietly not collecting
    the corpus every later feature depends on.
    """
    from cobalt.jobs.store import JobStore

    store = store or JobStore()
    ts = now or clock_mod.now_utc()
    max_age = timedelta(minutes=int(_tunable("heartbeat.archiver_max_age_min")))
    row = store.get("com.cobalt.archiver")
    if row is None:
        return Probe("archiver", False, "no jobs row — not registered")
    finished = row["finished_at"]
    if finished is None:
        # SAME DAY-ONE RULE AS THE MISSED PROBE. The archiver has run
        # every night for weeks; what it has never done is run while this
        # table existed to notice. Calling that red would DM a false
        # alarm every 15 minutes until tomorrow night's run, and an alert
        # that is wrong on day one is one people learn to scroll past.
        # It goes red the moment a real window passes with no run.
        registered = row["registered_at"]
        if registered is not None and ts - registered <= max_age:
            return Probe(
                "archiver", True,
                f"registered {registered:%Y-%m-%d %H:%M} UTC; no run OBSERVED yet — "
                "the job row is younger than one archiver window, so there has not "
                "been a run for it to have missed",
            )
        return Probe("archiver", False, "has never completed a run")
    age = ts - finished
    result = row["last_result"] or {}
    rows_written = result.get("rows_written")
    detail = (
        f"last run {finished:%Y-%m-%d %H:%M} UTC ({age.total_seconds() / 3600:.1f} h ago)"
        f", rows written {rows_written if rows_written is not None else 'UNRECORDED'}"
        f", exit {row['exit_code']}"
    )
    if age > max_age:
        return Probe(
            "archiver", False,
            f"STALE — {detail} (limit {max_age.total_seconds() / 3600:.0f} h)",
        )
    if row["exit_code"] not in (0, None):
        return Probe("archiver", False, f"last run FAILED — {detail}")
    if rows_written == 0:
        return Probe(
            "archiver", False,
            f"ran and wrote NOTHING — {detail}. Exit 0 with zero rows is the "
            "failure that looks green in every state column.",
        )
    return Probe("archiver", True, detail)


def backup_freshness(now: Optional[datetime] = None) -> Probe:
    """Age of the newest nightly snapshot, against
    `heartbeat.backup_max_age_min` (26 h).

    THE UNARMED CASE IS RED, AND SAYS SO. Both legs of the backup ruling
    (external SSD, Backblaze B2) are off until their inputs exist, and
    the honest report of that is "there is no backup", not `??` and not
    a green tick. `unknown` is reserved for a probe that could not RUN;
    a config that declares no destination ran fine and the answer is bad.
    """
    from cobalt.backup.config import BackupConfigError, load_backup_config
    from cobalt.backup.restic import BackupError, latest_snapshot_age

    ts = now or clock_mod.now_utc()
    try:
        cfg = load_backup_config()
    except BackupConfigError as e:
        return Probe("backup", False, f"config unreadable: {e}", unknown=True)

    if not cfg.armed:
        off = ", ".join(d.name for d in cfg.destinations)
        return Probe(
            "backup", False,
            f"NO DESTINATION ARMED ({off} all off) — there is no backup. "
            "configs/cobalt/backup.yaml says what each leg is missing.",
        )

    max_age = timedelta(minutes=int(_tunable("heartbeat.backup_max_age_min")))
    try:
        age = latest_snapshot_age(cfg)
    except (BackupError, Exception) as e:  # noqa: BLE001 — a repo we cannot reach is not a diagnosis
        return Probe("backup", False, f"could not read the repository: {type(e).__name__}",
                     unknown=True)
    if age is None:
        return Probe("backup", False,
                     f"armed ({', '.join(d.name for d in cfg.armed)}) but the repository "
                     "holds NO snapshot yet")
    hours = age.total_seconds() / 3600
    detail = (f"newest snapshot {hours:.1f} h old across "
              f"{', '.join(d.name for d in cfg.armed)}")
    if age > max_age:
        return Probe("backup", False,
                     f"STALE — {detail} (limit {max_age.total_seconds()/3600:.0f} h)")
    return Probe("backup", True, detail)


def vaultwrite_blocks(now: Optional[datetime] = None) -> Probe:
    """market_reset refusals + ungated migration runs since the last beat.

    NOT RED ON ITS OWN. A refusal is the guard WORKING — F1 turning away
    a write inside 20:00-21:00 is the system doing its job. The number is
    reported because a spike means something is retrying blind, and
    because the RULING on migration tooling (S1-P3, decided-with-veto)
    says every ungated repair run inside the block increments this same
    counter so it can never happen quietly.
    """
    from cobalt.session.store import SessionBlockStore

    try:
        store = SessionBlockStore()
        counts = store.counts_over_window(now=now)
    except Exception as e:  # noqa: BLE001
        return Probe("vault blocks", False, f"counter unreadable: {type(e).__name__}: {e}",
                     unknown=True)
    refused = counts.get(SessionBlockStore.REFUSED, 0)
    ungated = counts.get(SessionBlockStore.UNGATED_RUN, 0)
    # BOTH numbers, always, and never summed into one. They share a
    # counter because they are both "a write met the market_reset window"
    # — but a refusal is the guard working and an ungated run is the
    # carve-out being used, and reading five repairs as five refusals
    # would send someone hunting a bug that is not there.
    return Probe(
        "vault blocks", True,
        f"{refused} refused, {ungated} ungated repair run(s) in the counter window",
    )


def redactions(minutes: int, now: Optional[datetime] = None) -> Probe:
    """F19 hits since the last beat.

    Also not red on its own — the guard firing is the guard working. It
    is on the block because a redaction count that suddenly climbs means
    something started putting credentials into outbound text, and that is
    worth seeing the day it starts rather than at the next audit.
    """
    from cobalt.redact.store import RedactionStore

    try:
        store = RedactionStore()
        store.ensure_schema()
        count = store.count_over_minutes(minutes, now=now)
        by_pattern = store.by_pattern_since(
            (now or clock_mod.now_utc()) - timedelta(minutes=minutes)
        )
    except Exception as e:  # noqa: BLE001
        return Probe("redactions", False, f"counter unreadable: {type(e).__name__}: {e}",
                     unknown=True)
    if not count:
        return Probe("redactions", True, "0 since the last beat")
    kinds = ", ".join(f"{p} on {c} x{n}" for c, p, n in by_pattern[:5])
    return Probe("redactions", True, f"{count} since the last beat ({kinds})")


__all__ = [
    "Probe",
    "archiver_freshness",
    "database",
    "mainframe",
    "obsidian",
    "probe_timeout_s",
    "redactions",
    "sheet_http",
    "vaultwrite_blocks",
]
