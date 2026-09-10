"""F18 heartbeat host — the beat itself (Charter §3 F18, M10).

    uv run cobalt heartbeat beat

WHAT ONE BEAT DOES, in order:

1. probes everything (`probes.py`) and sweeps every job row
   (`jobs.watchdog`);
2. composes the beat, including the kill-switch state;
3. on red, sends the SECOND channel first (email, over Layer-B Google
   OAuth — `out_of_band` below), so that its outcome can appear in the
   DM;
4. DMs on any red — carrying "email channel DOWN: <reason>" when the
   second channel failed — plus one green summary a day at
   `heartbeat.green_summary_at`. The GREEN summary is DM-only: a daily
   all-clear in the alert inbox is how an alert inbox stops being read.
5. persists the beat independently of alert delivery;
6. writes the daily-note unit, unless the session clock says
   `market_reset`;
7. FINALIZE persists the vault outcome and sends a corrective
   out-of-band RED if that late write failed.

THE ALERT PATH IS NOT THE MONITORED PATH (Charter §3 F18). The DM goes
over Mattermost, which is one of the things being watched — so a
Mattermost outage would take the alert about the Mattermost outage with
it. That is the whole reason F18 asks for a second channel, and since
S1-P4 that channel exists: `cobalt.notify.email`, whose docstring states
the exact dependency chain. It needs neither Mattermost, nor Postgres,
nor the Obsidian vault. The `email` probe watches the watcher.

WHY THE BEAT NEVER RAISES ON A RED. A red heartbeat is the heartbeat
WORKING. It exits 0 and says RED loudly; it exits non-zero only when the
beat itself could not run, because a job row that flips to `failed` every
time something else is down would make the heartbeat's own history
useless.
"""

from __future__ import annotations

from datetime import datetime, time
from typing import Optional

from loguru import logger

from cobalt.jobs import killswitch
from cobalt.jobs.config import load_job_registry
from cobalt.jobs.store import JobStore
from cobalt.jobs.watchdog import sweep
from cobalt.session import clock as clock_mod
from cobalt.session.clock import session_clock
from cobalt.session.models import Session

from . import probes as probe_mod
from .render import SECTION, UNIT, WRITER, Beat

JOB_LABEL = "com.cobalt.heartbeat"
INTERVAL_KEY = "heartbeat.interval_min"
GREEN_SUMMARY_KEY = "heartbeat.green_summary_at"
VAULT_WRITTEN = "written"
VAULT_DEFERRED = "deferred_market_reset"
VAULT_FAILED = "failed"


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
        # Right after `sheet_http`, and a separate line on purpose: "the
        # server is up" and "the page will take a card" are different
        # facts, and on 2026-09-09 they disagreed for thirteen hours
        # while the beat stayed green.
        probe_mod.sheet_daymode(),
        probe_mod.obsidian(),
        probe_mod.mainframe(),
        probe_mod.herdr(),
        probe_mod.archiver_freshness(now=ts),
        probe_mod.seat_usage(now=ts),
        probe_mod.backup_freshness(now=ts),
        probe_mod.vaultwrite_blocks(now=ts),
        probe_mod.redactions(interval_min(), now=ts),
        probe_mod.email(),
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


def write_note_block(
    beat: Beat, *, dry_run: bool = False, now: Optional[datetime] = None
):
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
    writer = VaultWriter(
        WRITER,
        store=store,
        dry_run=dry_run,
        now=(lambda: now) if now is not None else None,
    )
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
    """Charter §3 F18's SECOND channel — email, over Layer-B Google OAuth.

    Built at S1-P4 (2026-09-08). Until then this function existed only to
    say, loudly and on every red, that the channel did NOT exist; the
    honest placeholder is in the git history and its S1-P3 reasoning is
    unchanged — alerting that stops at Mattermost is alerting that shares
    a fate with one of the things it watches.

    THIS RUNS BEFORE `send_dm`, and the order is the whole point. The DM
    is the channel that can carry a report ABOUT the email channel; the
    email channel cannot carry a report about itself. So the second
    channel goes first, and its outcome — including "email channel DOWN:
    <reason>" — is appended to the beat's notes in time for
    `beat.dm_body()` to render it.

    NEVER RAISES. A failure here is a note, not a crash: a beat that died
    trying to send the backup alert would take the primary alert with it,
    which is the exact coupling this channel exists to break.
    """
    from cobalt.notify import EmailError, record_attempt, send_email
    from cobalt.notify.config import load_notify_config

    try:
        cfg = load_notify_config().email
    except Exception as e:  # noqa: BLE001
        reason = f"notify config unreadable ({type(e).__name__}: {e})"
        logger.error("heartbeat: email channel DOWN — {}", reason)
        return f"email channel DOWN: {reason}"

    subject = f"{beat.headline} · {beat.at:%Y-%m-%d %H:%M %Z}"
    try:
        result = send_email(cfg.to, subject, beat.dm_body())
    except EmailError as e:
        # `EmailError`'s message is redacted BY CONTRACT, so it is safe to
        # put straight into a Mattermost DM — which is exactly where it is
        # about to go.
        record_attempt(ok=False, caller="heartbeat", detail=str(e))
        logger.error("heartbeat: email channel DOWN — {}", e)
        return f"email channel DOWN: {e}"

    record_attempt(
        ok=result.sent, caller="heartbeat", detail=result.detail, message_id=result.ref
    )
    if not result.sent:
        # A disabled channel is deliberate, not an outage — but the DM
        # still says so, because "no email arrived" must never be
        # ambiguous between "off" and "broken".
        logger.warning("heartbeat: {}", result.report())
        return f"email channel OFF: {result.detail}"
    logger.info("heartbeat: {}", result.report())
    return result.report()


# ---------------------------------------------------------------------
# the six isolated stages
# ---------------------------------------------------------------------


def _stage_failure(beat: Beat, stage: str, error: BaseException) -> str:
    """Make a stage failure safe for persistence and outbound channels."""
    raw = f"{stage} FAILED ({type(error).__name__}: {error})"
    try:
        from cobalt.redact import redact

        reason = redact(raw, channel="heartbeat.stage").text
    except Exception as redact_error:  # noqa: BLE001
        logger.error(
            "heartbeat: {} and its reason could not be redacted ({}: {})",
            stage,
            type(redact_error).__name__,
            redact_error,
        )
        reason = f"{stage} FAILED ({type(error).__name__}; detail unavailable)"
    logger.error("heartbeat: {}", reason)
    beat.stage_failures.append(reason)
    return reason


def _compose_beat(beat: Beat, store: JobStore) -> None:
    state = killswitch.read(store)
    beat.kill_switch = state.describe()
    if state.active:
        beat.kill_switch += " Heartbeat exemption active — this watcher is still running."


def _attempt_alert(beat: Beat, name: str, sender) -> None:
    try:
        beat.notes.append(sender(beat))
    except Exception as e:  # noqa: BLE001 - one channel cannot suppress the next
        _stage_failure(beat, f"alerts/{name}", e)


def _run_alerts(beat: Beat, store: JobStore, *, dry_run: bool) -> bool:
    if dry_run:
        beat.notes.append("DRY RUN — no DM sent, nothing written.")
        return False

    if beat.green:
        try:
            send_green = should_send_green(beat, store)
        except Exception as e:  # noqa: BLE001
            _stage_failure(beat, "alerts/green-dedup", e)
            send_green = False
        if send_green:
            before = len(beat.stage_failures)
            _attempt_alert(beat, "green-dm", send_dm)
            if len(beat.stage_failures) == before:
                return True

    if not beat.green:
        # OUT-OF-BAND FIRST. Its result is included in the primary DM, and
        # an unexpected exception in either channel cannot suppress the other.
        _attempt_alert(beat, "out-of-band", out_of_band)
        _attempt_alert(beat, "red-dm", send_dm)
    return False


def _beat_result(beat: Beat, *, sent_green: bool) -> dict:
    result = {
        "green": beat.green,
        "red_jobs": [j.label for j in beat.red_jobs],
        "red_probes": [p.name for p in beat.red_probes],
        "stage_failures": list(beat.stage_failures),
        "kill_switch": beat.kill_switch,
    }
    # Omission preserves the prior dedup value through JobStore's JSON merge.
    if sent_green:
        result["green_summary_date"] = beat.at.date().isoformat()
    return result


def _persist_beat(beat: Beat, store: JobStore, *, sent_green: bool) -> None:
    store.ensure_schema()
    store.register(load_job_registry().spec(JOB_LABEL))
    store.record_heartbeat_result(
        JOB_LABEL,
        result=_beat_result(beat, sent_green=sent_green),
        vault_outcome=None,
        vault_reason=None,
    )


def _run_vault_stage(
    beat: Beat, *, now: datetime, dry_run: bool
) -> tuple[Optional[str], Optional[str]]:
    # The session decision happens before daily-note resolution, store setup,
    # or VaultWriter construction. Deferral therefore cannot create a
    # `session_blocks` refusal row.
    current = session_clock().session(now)
    if current is Session.MARKET_RESET:
        return (
            VAULT_DEFERRED,
            "session clock resolved market_reset; no vault write was attempted",
        )

    write = write_note_block(beat, dry_run=dry_run, now=now)
    if write is None:
        return VAULT_FAILED, "daily-note writer returned no result"
    beat.notes.append(write.report())
    if write.write_id is None:
        return VAULT_FAILED, "daily-note writer returned success without a write id"
    return VAULT_WRITTEN, None


def _finalize(
    beat: Beat,
    store: JobStore,
    *,
    sent_green: bool,
    dry_run: bool,
) -> None:
    if dry_run:
        return

    # Persistence and notification are deliberately separate attempts. If the
    # final database update fails, the corrective out-of-band RED still runs.
    try:
        store.record_heartbeat_result(
            JOB_LABEL,
            result=_beat_result(beat, sent_green=sent_green),
            vault_outcome=beat.vault_outcome,
            vault_reason=beat.vault_reason,
        )
    except Exception as e:  # noqa: BLE001
        _stage_failure(beat, "FINALIZE/persist", e)

    if beat.vault_outcome == VAULT_FAILED:
        _attempt_alert(beat, "corrective-out-of-band", out_of_band)


def run_beat(*, now: Optional[datetime] = None, dry_run: bool = False, probe: bool = True) -> Beat:
    """One whole heartbeat. Every stage fails loud and yields to the next."""
    ts = now or clock_mod.now_utc()
    store = JobStore()

    logger.info("heartbeat: stage PROBES")
    try:
        beat = take_beat(now=ts, probe=probe)
    except Exception as e:  # noqa: BLE001
        beat = Beat(at=ts.astimezone(clock_mod.ET))
        _stage_failure(beat, "probes", e)

    logger.info("heartbeat: stage COMPOSE")
    try:
        _compose_beat(beat, store)
    except Exception as e:  # noqa: BLE001
        _stage_failure(beat, "compose", e)

    logger.info("heartbeat: stage ALERTS")
    try:
        sent_green = _run_alerts(beat, store, dry_run=dry_run)
    except Exception as e:  # noqa: BLE001
        sent_green = False
        _stage_failure(beat, "alerts", e)

    logger.info("heartbeat: stage PERSIST")
    if not dry_run:
        try:
            _persist_beat(beat, store, sent_green=sent_green)
        except Exception as e:  # noqa: BLE001
            _stage_failure(beat, "persist", e)

    logger.info("heartbeat: stage VAULT")
    try:
        beat.vault_outcome, beat.vault_reason = _run_vault_stage(
            beat, now=ts, dry_run=dry_run
        )
    except Exception as e:  # noqa: BLE001
        beat.vault_outcome = VAULT_FAILED
        beat.vault_reason = _stage_failure(beat, "vault", e)
    if beat.vault_outcome == VAULT_FAILED:
        logger.error("heartbeat: vault unit FAILED — {}", beat.vault_reason)
    elif beat.vault_outcome == VAULT_DEFERRED:
        logger.warning("heartbeat: vault unit DEFERRED — {}", beat.vault_reason)

    logger.info("heartbeat: stage FINALIZE")
    try:
        _finalize(beat, store, sent_green=sent_green, dry_run=dry_run)
    except Exception as e:  # noqa: BLE001
        _stage_failure(beat, "FINALIZE", e)

    (logger.info if beat.green else logger.error)("heartbeat: {}", beat.headline)
    return beat


__all__ = [
    "GREEN_SUMMARY_KEY",
    "INTERVAL_KEY",
    "JOB_LABEL",
    "VAULT_DEFERRED",
    "VAULT_FAILED",
    "VAULT_WRITTEN",
    "green_summary_at",
    "interval_min",
    "out_of_band",
    "run_beat",
    "take_beat",
    "write_note_block",
]
