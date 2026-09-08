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

import json
import socket
import subprocess
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
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
        # ADR-0008: the probe names no table, but a connection still has
        # to declare a side. SYSTEM — the heartbeat is system-side, and a
        # liveness probe must never be the thing that opens user data.
        with db.connect(name, side=db.Side.SYSTEM) as conn:
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
    """Last run + rows written, checked against the archiver's own
    Mon-Fri cadence via the same `is_missed` arithmetic F17's watchdog
    uses — not a flat age window.

    A flat `now - last_run > N hours` window cannot tell a genuine miss
    from an ordinary Friday-to-Monday gap: whatever N is, it either
    fires every weekend (too small) or hides a multi-day outage (too
    big). 2026-09-06 is why this changed: the F17 wrapper was registered
    at 22:19 ET Friday, AFTER that evening's 20:30 run had already
    completed via the pre-wrapper code path, so the row's `finished_at`
    stayed NULL forever with nothing wrong — and the old flat
    `registered_at + heartbeat.archiver_max_age_min` grace expired
    Saturday just after midnight, painting the whole weekend red for a
    job that was never actually due again until Monday evening.
    `is_missed` already gets this right, including the exact "cannot
    miss a run it was not watching for" case above — reusing it here is
    the one-path rule, not a nicety.

    Rows written still matters once a run HAS completed — a nightly run
    that exits 0 having written zero rows looks green in every state
    column and is quietly not collecting the corpus every later feature
    depends on. That check is cadence-independent and unchanged.
    """
    from cobalt.jobs.config import load_job_registry
    from cobalt.jobs.store import JobStore
    from cobalt.jobs.watchdog import MISSED_GRACE_KEY, is_missed
    from cobalt.session.clock import session_clock

    store = store or JobStore()
    ts = now or clock_mod.now_utc()
    row = store.get("com.cobalt.archiver")
    if row is None:
        return Probe("archiver", False, "no jobs row — not registered")

    spec = load_job_registry().spec("com.cobalt.archiver")
    now_et = session_clock().to_et(ts)
    grace = timedelta(minutes=int(_tunable(MISSED_GRACE_KEY)))
    missed, missed_detail = is_missed(spec, row, now_et=now_et, grace=grace)

    finished = row["finished_at"]
    if finished is None:
        if missed:
            return Probe("archiver", False, missed_detail)
        return Probe(
            "archiver", True,
            f"no run OBSERVED yet — none due since registration "
            f"({row['registered_at']:%Y-%m-%d %H:%M} UTC)",
        )
    age = ts - finished
    result = row["last_result"] or {}
    rows_written = result.get("rows_written")
    detail = (
        f"last run {finished:%Y-%m-%d %H:%M} UTC ({age.total_seconds() / 3600:.1f} h ago)"
        f", rows written {rows_written if rows_written is not None else 'UNRECORDED'}"
        f", exit {row['exit_code']}"
    )
    if missed:
        return Probe("archiver", False, f"STALE — {detail} — {missed_detail}")
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
    except BackupError as e:
        # BackupError's text is credential-free BY CONTRACT (see
        # backup/restic.py), and it is the one carrying the actionable
        # sentence — "/Volumes/COBALT-BACKUP is NOT MOUNTED". A beat that
        # said only `BackupError` would send someone to read the log to
        # learn they need to plug a disk in.
        return Probe("backup", False, str(e).split(". ")[0], unknown=True)
    except Exception as e:  # noqa: BLE001 — a repo we cannot reach is not a diagnosis
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


# ---------------------------------------------------------------------
# herdr — the terminal workspace every agent seat lives in
# ---------------------------------------------------------------------

HERDR_LABEL = "com.cobalt.herdr"

#: Where herdr puts its API socket. Not a tunable: F16 governs
#: THRESHOLDS, and this is an address — a number you might tune versus a
#: path that is either right or wrong. `herdr status server` prints it,
#: and it has been this since 0.8.x.
HERDR_SOCKET = Path("~/.config/herdr/herdr.sock")

#: Absolute, for the same reason every plist's ProgramArguments is: a
#: probe that resolved a binary off PATH would answer a different
#: question under launchd than it answers in a shell.
HERDR_BINARY = Path("/opt/homebrew/bin/herdr")


def _herdr_enabled() -> tuple[bool, str]:
    """Is `com.cobalt.herdr` supposed to be up yet?

    The registry row answers, and until the handover it says no. This is
    read every beat rather than baked in, so flipping one flag in
    `configs/cobalt/jobs.yaml` is the whole of the last handover step.
    """
    from cobalt.jobs.config import load_job_registry

    spec = load_job_registry().by_label.get(HERDR_LABEL)
    if spec is None:
        return False, f"{HERDR_LABEL} is not in the job registry"
    return spec.enabled, ""


def _herdr_agent_list(binary: Path, timeout: float) -> list:
    """`herdr agent list` -> the agents array. Raises on anything else."""
    proc = subprocess.run(
        [str(binary), "agent", "list"], capture_output=True, text=True, timeout=timeout
    )
    if proc.returncode != 0:
        raise RuntimeError(
            f"`herdr agent list` exited {proc.returncode}: "
            f"{proc.stderr.strip()[:200] or '(no stderr)'}"
        )
    payload = json.loads(proc.stdout)
    agents = (payload.get("result") or {}).get("agents")
    if not isinstance(agents, list):
        raise RuntimeError("`herdr agent list` returned no `result.agents` array")
    return agents


def herdr(
    *,
    socket_path: Optional[Path] = None,
    binary: Optional[Path] = None,
    list_agents=None,
) -> Probe:
    """The herdr server is up AND answering — two questions, both asked.

    THE SOCKET EXISTING IS NOT THE SERVER WORKING, which is the same
    lesson the ASET sheet's HTTP probe carries: a stale socket file
    outlives the process that made it, and a server that has wedged
    still holds its socket open. So this connects to the socket (does it
    accept?) and then asks it something real (`herdr agent list`, which
    has to traverse the server's live pane state to answer). Either half
    failing is red, and the message names the launchd label so a reader
    knows what to bootstrap.

    UNTIL THE HANDOVER IT IS GREEN AND SAYS WHY. The registry row ships
    `enabled: false` because the plist is built and deliberately not
    loaded — see ops/README.md's "herdr handover". A red every 15
    minutes for a state somebody chose on purpose is how a heartbeat
    stops being read, and the server is running perfectly well under a
    manual start in the meantime.
    """
    enabled, why = _herdr_enabled()
    if not enabled:
        return Probe(
            "herdr", True,
            (why or f"{HERDR_LABEL} is registered with `enabled: false`")
            + " — NOT PROBED. The plist is built and deliberately not loaded; the "
            "server is running under a manual start. ops/README.md 'herdr handover' "
            "is the procedure, and flipping that flag is its last step.",
        )

    path = Path(socket_path or HERDR_SOCKET).expanduser()
    timeout = probe_timeout_s()
    if not path.exists():
        return Probe(
            "herdr", False,
            f"no API socket at {path} — the server is not running. "
            f"`launchctl kickstart -k gui/$(id -u)/{HERDR_LABEL}`",
        )
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect(str(path))
    except OSError as e:
        return Probe(
            "herdr", False,
            f"the socket at {path} exists but REFUSED a connection "
            f"({type(e).__name__}) — a stale socket file outlives the process that "
            f"made it. {HERDR_LABEL} needs a kickstart.",
        )

    caller = list_agents or _herdr_agent_list
    try:
        agents = caller(Path(binary or HERDR_BINARY), timeout)
    except Exception as e:  # noqa: BLE001
        return Probe(
            "herdr", False,
            f"socket accepted but the server did not answer `agent list` "
            f"({type(e).__name__}: {e}) — {HERDR_LABEL} is up and not serving",
        )
    seats = ", ".join(sorted({str(a.get("agent")) for a in agents if a.get("agent")}))
    return Probe(
        "herdr", True,
        f"socket accepting at {path}; {len(agents)} pane(s)"
        + (f", seats: {seats}" if seats else ""),
    )


# ---------------------------------------------------------------------
# seat-usage report freshness
# ---------------------------------------------------------------------


def seat_usage(store=None, now: Optional[datetime] = None) -> Probe:
    """Has the seat-usage report been refreshed recently ENOUGH, and is
    it even due right now?

    ASKED ONLY INSIDE THE WINDOW. The job runs hourly between 06:00 and
    23:00 ET; at 03:00 the last run is four hours old and everything is
    exactly as it should be. A flat age check would be red all night for
    a schedule working as written — the same mistake the archiver's
    freshness probe made against weekends, and fixed on 2026-09-06 by
    asking the schedule instead of guessing a number.

    Inside the window, the limit is `seat_usage.max_age_min` (two
    intervals): one missed run is a hiccup nobody needs to be told
    about, two in a row means the number Dejan reads at the close is
    wrong.
    """
    from cobalt.jobs.config import load_job_registry
    from cobalt.jobs.store import JobStore
    from cobalt.session.clock import session_clock
    from cobalt.seatusage.runner import JOB_LABEL

    ts = now or clock_mod.now_utc()
    now_et = session_clock().to_et(ts)
    spec = load_job_registry().by_label.get(JOB_LABEL)
    if spec is None or spec.schedule is None:
        return Probe("seat usage", False, f"{JOB_LABEL} is not in the job registry")
    if not spec.enabled:
        return Probe(
            "seat usage", True,
            f"{JOB_LABEL} is registered with `enabled: false` — NOT PROBED",
        )
    cadence = spec.cadence or "(no cadence)"
    if not spec.schedule.due_now(now_et):
        return Probe(
            "seat usage", True,
            f"outside its window — not due ({cadence}). The report holds "
            "yesterday's last run until the window opens again.",
        )

    store = store or JobStore()
    try:
        row = store.get(JOB_LABEL)
    except Exception as e:  # noqa: BLE001
        return Probe("seat usage", False,
                     f"jobs row unreadable: {type(e).__name__}: {e}", unknown=True)
    if row is None:
        return Probe("seat usage", False, f"no jobs row for {JOB_LABEL} — not registered")

    limit = timedelta(minutes=int(_tunable("seat_usage.max_age_min")))
    finished = row["finished_at"]
    if finished is None:
        opened = spec.schedule.window_opened_at(now_et)
        reference = max(
            [d for d in (opened, session_clock().to_et(row["registered_at"])) if d]
        )
        if now_et - reference <= limit:
            return Probe(
                "seat usage", True,
                f"no run OBSERVED yet — none due since {reference:%Y-%m-%d %H:%M} ET "
                f"({cadence})",
            )
        return Probe(
            "seat usage", False,
            f"NEVER RUN inside its window — nothing since "
            f"{reference:%Y-%m-%d %H:%M} ET ({cadence})",
        )

    age = ts - finished
    result = row["last_result"] or {}
    unpriced = result.get("unpriced") or []
    detail = (
        f"last run {session_clock().to_et(finished):%Y-%m-%d %H:%M} ET "
        f"({age.total_seconds() / 60:.0f} min ago), exit {row['exit_code']}"
    )
    if unpriced:
        # NOT RED. An unpriced model is loud in the report itself, every
        # hour, where the number it distorts is. Repeating it as a red
        # beat would put a permanent alert on a condition that is fixed
        # by a deliberate version bump, not by anything at 03:00.
        detail += f"; UNPRICED in the report: {', '.join(unpriced)}"
    if row["exit_code"] not in (0, None):
        return Probe("seat usage", False, f"last run FAILED — {detail}")
    if age > limit:
        return Probe(
            "seat usage", False,
            f"STALE — {detail}, limit {limit.total_seconds() / 60:.0f} min "
            f"({cadence}). The report is no longer today's.",
        )
    return Probe("seat usage", True, detail)


def email() -> Probe:
    """The out-of-band alert channel is armed — token present + last send.

    THE ONE PROBE THAT WATCHES THE ALERT PATH ITSELF. Every other probe
    here answers "is a monitored thing up?"; this one answers "could we
    still tell him if it were not?". An email channel that quietly lost
    its refresh token would take every red with it and leave the beat
    looking exactly as green as before — which is the failure this row
    exists to make impossible.

    It NEVER SENDS. A probe that mailed a test every 15 minutes would put
    96 messages a day in the inbox and train its reader to filter the
    channel, defeating the thing it was checking. Presence of the
    credential is read from the vault (names only, no values, no
    network); the last real send is read from `cobalt_email_sends`,
    written by whoever actually sent one.

    A FAILED LAST SEND IS RED, and stays red until a later send succeeds.
    "It worked in July" is not an answer about an alert path.
    """
    from cobalt.notify.email import channel_status
    from cobalt.notify.store import EmailSendStore

    try:
        armed, detail = channel_status()
    except Exception as e:  # noqa: BLE001
        return Probe("email", False, f"PROBE FAILED — channel state UNKNOWN: {e}", unknown=True)
    if not armed:
        return Probe("email", False, detail)

    try:
        last = EmailSendStore().last()
    except Exception as e:  # noqa: BLE001
        # The credential IS there; only the history is unreadable. That
        # is ignorance about half the question, not a dead channel — and
        # `unknown` is what says so.
        return Probe("email", False, f"{detail}; last send UNKNOWN ({type(e).__name__})",
                     unknown=True)

    if last is None:
        # Never sent is not "broken", but it is not proven either, and
        # F18's whole claim is that this path works. `cobalt notify
        # email-test` is one command.
        return Probe("email", False,
                     f"{detail}, but NO SEND HAS EVER BEEN MADE from this host — the "
                     "out-of-band path is unproven. Run `cobalt notify email-test`.")
    when = f"{last['ts']:%Y-%m-%d %H:%M} UTC"
    if not last["ok"]:
        return Probe("email", False,
                     f"{detail}; LAST SEND FAILED at {when} ({last['caller']}) — "
                     f"{last['detail']}")
    return Probe("email", True, f"{detail}; last send OK {when} ({last['caller']})")


__all__ = [
    "Probe",
    "archiver_freshness",
    "database",
    "email",
    "herdr",
    "mainframe",
    "obsidian",
    "probe_timeout_s",
    "redactions",
    "seat_usage",
    "sheet_http",
    "vaultwrite_blocks",
]
