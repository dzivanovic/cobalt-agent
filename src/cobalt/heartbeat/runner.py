"""F18 heartbeat host — the beat itself (Charter §3 F18, M10).

    uv run cobalt heartbeat beat

WHAT ONE BEAT DOES, in order:

1. probes everything (`probes.py`) and sweeps every job row
   (`jobs.watchdog`);
2. writes a Cobalt-owned red/green block into TODAY'S daily note through
   `VaultWriter` — one L28 unit, updated in place, one diff per beat;
3. DMs on any red, plus one green summary a day at
   `heartbeat.green_summary_at`;
4. on red, sends the second channel — see `_out_of_band` below for
   exactly what exists today, which is not OAuth email.

THE ALERT PATH IS NOT THE MONITORED PATH (Charter §3 F18). The DM goes
over Mattermost, which is one of the things being watched — so a
Mattermost outage would take the alert about the Mattermost outage with
it. That is the whole reason F18 asks for a second channel.

WHY THE BEAT NEVER RAISES ON A RED. A red heartbeat is the heartbeat
WORKING. It exits 0 and says RED loudly; it exits non-zero only when the
beat itself could not run, because a job row that flips to `failed` every
time something else is down would make the heartbeat's own history
useless.
"""

from __future__ import annotations

from datetime import datetime, time, timedelta
from typing import Optional

from loguru import logger

from cobalt.jobs.store import JobStore
from cobalt.jobs.watchdog import sweep
from cobalt.session import clock as clock_mod
from cobalt.session.clock import session_clock

from . import probes as probe_mod
from .render import SECTION, UNIT, WRITER, Beat

JOB_LABEL = "com.cobalt.heartbeat"
INTERVAL_KEY = "heartbeat.interval_min"
GREEN_SUMMARY_KEY = "heartbeat.green_summary_at"


def interval_min() -> int:
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(INTERVAL_KEY)
    if row is None:
        raise RuntimeError(
            f"tunable {INTERVAL_KEY!r} is missing from tunables.yaml — the heartbeat "
            "reads its own cadence from config and has no built-in default (F16). "
            "This is the number every 'red within one interval' claim is measured "
            "against."
        )
    return int(row.value)


def green_summary_at() -> time:
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(GREEN_SUMMARY_KEY)
    if row is None:
        raise RuntimeError(f"tunable {GREEN_SUMMARY_KEY!r} is missing from tunables.yaml (F16).")
    hh, _, mm = str(row.value).partition(":")
    return time(int(hh), int(mm))


# ---------------------------------------------------------------------
# 1. probe
# ---------------------------------------------------------------------


def take_beat(*, now: Optional[datetime] = None, probe: bool = True) -> Beat:
    """Every probe and every job row. Never raises on a red."""
    ts = now or clock_mod.now_utc()
    beat = Beat(at=session_clock().to_et(ts))

    beat.probes = [
        probe_mod.database(),
        probe_mod.sheet_http(),
        probe_mod.obsidian(),
        probe_mod.mainframe(),
        probe_mod.archiver_freshness(now=ts),
        probe_mod.backup_freshness(now=ts),
        probe_mod.vaultwrite_blocks(now=ts),
        probe_mod.redactions(interval_min(), now=ts),
    ]
    try:
        beat.jobs = sweep(now=ts, probe=probe)
    except Exception as e:  # noqa: BLE001 - a broken sweep is its own red
        beat.probes.append(
            probe_mod.Probe(
                "job sweep", False,
                f"the watchdog itself FAILED ({type(e).__name__}: {e}) — every job's "
                "state is UNKNOWN, which is not the same as green",
                unknown=True,
            )
        )
    return beat


# ---------------------------------------------------------------------
# 2. the daily-note block (Output 1)
# ---------------------------------------------------------------------


def write_note_block(beat: Beat, *, dry_run: bool = False):
    """One L28 unit in today's note, updated in place — one diff a beat.

    Returns the `WriteResult`, or None when there is no note yet. A
    missing note is NOT created from here (L28.1: only
    `create_if_absent` with a template may), and the 05:15 prefill is
    what creates the day's note.
    """
    from cobalt.daymode.note import daily_note_path
    from cobalt.vaultwrite import VaultWriter, VaultWriteStore

    path = daily_note_path(beat.at.date())
    if not path.exists():
        logger.error(
            "heartbeat: {} does not exist — the status block was NOT written. The "
            "05:15 prefill creates the day's note; this writer never does (L28.1).",
            path,
        )
        return None
    store = VaultWriteStore()
    store.ensure_schema()
    writer = VaultWriter(WRITER, store=store, dry_run=dry_run)
    return writer.upsert_unit(path, SECTION, UNIT, beat.note_body())


# ---------------------------------------------------------------------
# 3/4. the alert channels (Outputs 2 and 3)
# ---------------------------------------------------------------------


def should_send_green(beat: Beat, store: JobStore) -> bool:
    """One green summary a day, at `heartbeat.green_summary_at`.

    "Have we already sent today's?" is answered from the JOB ROW's own
    `last_result` rather than from a new table — the heartbeat is the
    only writer of that row, and a second table to remember one boolean a
    day is a table to migrate later for nothing.
    """
    if beat.at.time() < green_summary_at():
        return False
    row = store.get(JOB_LABEL) or {}
    last = (row.get("last_result") or {}).get("green_summary_date")
    return last != beat.at.date().isoformat()


def send_dm(beat: Beat) -> str:
    from cobalt.notify import MattermostError, send_dm as _send

    try:
        result = _send(beat.dm_body())
    except MattermostError as e:
        # The alert path failing is itself worth saying, in the note and
        # in the log — it is the one failure the DM cannot report.
        logger.error("heartbeat: Mattermost DM FAILED — {}", e)
        return f"Mattermost DM FAILED: {e}"
    logger.info("heartbeat: {}", result.report())
    return result.report()


def out_of_band(beat: Beat) -> str:
    """Charter §3 F18's SECOND channel, and the honest answer about it.

    The Charter says: "red also out-of-band = email via Layer-B Google
    OAuth at MVP (alert path != monitored path)."

    THAT SEND PATH DOES NOT EXIST IN THIS REPO. Searched at S1-P3
    (2026-09-04): no `smtplib`, no `sendmail`, no Gmail/OAuth client, no
    credentials file, no `send_email` anywhere in `src/`, `ops/`,
    `dev_utils/` or `configs/`. `google-api-python-client` is in
    pyproject's dependencies and `googleapiclient` appears in the old
    tree only as a Gemini/LLM import — never as a mail sender. The vault
    holds no Google OAuth token: its cloud keys are GEMINI/OPENAI/
    OPENROUTER API keys, which are not an OAuth credential and cannot
    send mail.

    S1-P3's instruction was explicit: do NOT build OAuth; report what
    exists and stop at Mattermost. So this function reports, loudly, on
    every red, and the second channel is a P4 line. Building an OAuth
    send path is a real piece of work — client registration, consent,
    refresh-token storage in the vault, a new secret shape for F19 — and
    it is not something to improvise inside a heartbeat.
    """
    return (
        "OUT-OF-BAND CHANNEL NOT AVAILABLE — Charter §3 F18 specifies email via the "
        "Layer-B Google OAuth path, and no email send path exists in this repo "
        "(verified S1-P3: no smtplib/sendmail/OAuth client/credential anywhere in "
        "src, ops, dev_utils or configs; the vault holds API keys, not an OAuth "
        "token). Alerting stopped at Mattermost, which IS one of the monitored "
        "services — so a Mattermost outage takes this alert with it. Carried to P4."
    )


# ---------------------------------------------------------------------
# the beat
# ---------------------------------------------------------------------


def run_beat(*, now: Optional[datetime] = None, dry_run: bool = False, probe: bool = True) -> Beat:
    """One whole heartbeat. Returns the Beat; never raises on a red."""
    store = JobStore()
    store.ensure_schema()
    beat = take_beat(now=now, probe=probe)

    write = write_note_block(beat, dry_run=dry_run)
    if write is None:
        beat.notes.append("Daily note: NOT WRITTEN — today's note does not exist yet.")
    else:
        # L28.4: the unified diff goes in the RUN REPORT, every time. The
        # heartbeat writes to the live vault every 15 minutes; a write
        # path that reported only "updated" would be the one write path
        # in this codebase whose changes nobody could read back.
        beat.notes.append(write.report())

    sent_green = False
    if dry_run:
        beat.notes.append("DRY RUN — no DM sent, nothing written.")
    elif not beat.green:
        beat.notes.append(send_dm(beat))
        beat.notes.append(out_of_band(beat))
    elif should_send_green(beat, store):
        beat.notes.append(send_dm(beat))
        sent_green = True

    if not dry_run:
        # The heartbeat records ITS OWN run like any other job — it is the
        # one job nobody else is watching, so it watches itself and a
        # stalled heartbeat shows up as its own MISSED row.
        result = {
            "green": beat.green,
            "red_jobs": [j.label for j in beat.red_jobs],
            "red_probes": [p.name for p in beat.red_probes],
        }
        prior = (store.get(JOB_LABEL) or {}).get("last_result") or {}
        result["green_summary_date"] = (
            beat.at.date().isoformat() if sent_green else prior.get("green_summary_date")
        )
        store.register_all(__import__(
            "cobalt.jobs.config", fromlist=["load_job_registry"]
        ).load_job_registry())
        store.mark_running(JOB_LABEL, now=now or clock_mod.now_utc())
        store.mark_finished(JOB_LABEL, exit_code=0, result=result, now=now or clock_mod.now_utc())

    (logger.info if beat.green else logger.error)("heartbeat: {}", beat.headline)
    return beat


__all__ = [
    "GREEN_SUMMARY_KEY",
    "INTERVAL_KEY",
    "JOB_LABEL",
    "green_summary_at",
    "interval_min",
    "out_of_band",
    "run_beat",
    "take_beat",
    "write_note_block",
]
