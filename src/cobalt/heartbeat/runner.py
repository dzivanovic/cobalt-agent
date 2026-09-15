"""F18 heartbeat host — the beat itself (Charter §3 F18, M10).

    uv run cobalt heartbeat beat

WHAT ONE BEAT DOES, in order:

1. probes everything (`probes.py`) and sweeps every job row
   (`jobs.watchdog`);
2. composes the beat, including the kill-switch state;
3. on a TRANSITION — something entered RED or recovered since the prior
   beat (ruled 2026-09-14, option B) — DMs it. A RED that is unchanged
   is silent;
4. DMs a standing-state summary at every `heartbeat.summary_at` slot,
   sent whether or not anything is red (a missing summary is the
   dead-heartbeat signal);
5. persists the beat independently of alert delivery;
6. writes the daily-note unit, unless the session clock says
   `market_reset`;
7. FINALIZE persists the vault outcome and sends a corrective DM if that
   late write failed or recovered.

THE SECOND CHANNEL WAS RETIRED 2026-09-14 (executed 2026-09-15). Charter
§3 F18 asked for an out-of-band alert path because the DM travels over
Mattermost, one of the watched services, so a Mattermost outage takes
the alert about it along. S1-P4 built that path as Gmail over Layer-B
Google OAuth. Google's Publish step for the `gmail.send` scope is gated
on restricted-scope verification, so the OAuth client never left
Testing and its refresh token expired every seven days — an alert path
that needs a human re-consent every week is not an alert path. Dejan
ruled it retired: alerts are DM-only, and that hole is known and named
here rather than hidden. The channel's send-log table stays in the
database as history (`db_migrations/placement.py`).

WHY THE BEAT NEVER RAISES ON A RED. A red heartbeat is the heartbeat
WORKING. It exits 0 and says RED loudly; it exits non-zero only when the
beat itself could not run, because a job row that flips to `failed` every
time something else is down would make the heartbeat's own history
useless.
"""

from __future__ import annotations

import stat
from dataclasses import dataclass, field
from datetime import datetime, time
from pathlib import Path
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
SUMMARY_KEY = "heartbeat.summary_at"
#: The key a failed vault unit takes in a transition note.
VAULT_KEY = "vault unit"
#: Stages that run BEFORE the alert decision. Only their failures are known
#: in time to take part in it; later stages are persisted, not compared.
EARLY_STAGES = ("probes", "compose")
VAULT_WRITTEN = "written"
VAULT_DEFERRED = "deferred_market_reset"
VAULT_DEFERRED_NOTE_ABSENT = "deferred_note_absent"
VAULT_FAILED = "failed"


class DailyNoteAbsent(Exception):
    """Positive evidence that the resolved daily-note target is absent."""

    def __init__(self, path: Path):
        self.path = Path(path)
        super().__init__(str(self.path))


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


def summary_at() -> list[time]:
    """The ruled summary slots, ascending. A malformed row crashes (L1)."""
    from cobalt.taxonomy.loader import load_tunables

    row = load_tunables().by_key.get(SUMMARY_KEY)
    if row is None:
        raise RuntimeError(f"tunable {SUMMARY_KEY!r} is missing from tunables.yaml (F16).")
    if not isinstance(row.value, list) or not row.value:
        raise RuntimeError(
            f"tunable {SUMMARY_KEY!r} must be a non-empty list of ET \"HH:MM\" slots, "
            f"got {row.value!r}"
        )
    slots = []
    for value in row.value:
        hh, sep, mm = str(value).partition(":")
        if not sep:
            raise RuntimeError(f"tunable {SUMMARY_KEY!r}: {value!r} is not \"HH:MM\"")
        slots.append(time(int(hh), int(mm)))
    if slots != sorted(set(slots)):
        raise RuntimeError(f"tunable {SUMMARY_KEY!r}: slots must be ascending and unique")
    return slots


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
        probe_mod.radar(ts),
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

    Returns the `WriteResult`. A missing note raises `DailyNoteAbsent`
    carrying the one resolved target; it is NOT created from here (L28.1).
    """
    from cobalt.daymode.note import daily_note_path
    from cobalt.vaultwrite import VaultWriteError, VaultWriter, VaultWriteStore

    target_day = beat.at.astimezone(clock_mod.ET).date()
    try:
        path = Path(daily_note_path(target_day))
    except Exception as e:
        raise VaultWriteError(
            f"daily-note target unresolved for {target_day}: {e}"
        ) from e

    try:
        target_stat = path.stat()
    except FileNotFoundError:
        raise DailyNoteAbsent(path) from None
    except Exception as e:
        raise VaultWriteError(f"daily-note target {path}: {e}") from e
    if not stat.S_ISREG(target_stat.st_mode):
        raise VaultWriteError(f"daily-note target {path}: target is not a regular file")

    try:
        store = VaultWriteStore()
        store.ensure_schema()
        writer = VaultWriter(
            WRITER,
            store=store,
            dry_run=dry_run,
            now=(lambda: now) if now is not None else None,
        )
        result = writer.upsert_unit(path, SECTION, UNIT, beat.note_body())
    except Exception as e:
        detail = str(e).removeprefix(f"{path}: ")
        raise VaultWriteError(f"daily-note target {path}: {detail}") from e
    if result is None:
        raise VaultWriteError(
            f"daily-note target {path}: writer returned no result without an absence signal"
        )
    return result


# ---------------------------------------------------------------------
# 3/4. the alert channels (Outputs 2 and 3)
# ---------------------------------------------------------------------


def _stage_key(reason: str) -> Optional[str]:
    """`"probes FAILED (...)"` -> `"stage probes"`; None for a late stage."""
    stage = reason.partition(" FAILED")[0]
    return f"stage {stage}" if stage in EARLY_STAGES else None


@dataclass(frozen=True)
class PriorBeat:
    """What the previous beat left in the job row, read BEFORE this beat
    overwrites it. No new table: `last_result` already carries the red sets,
    exactly as the old green-summary dedup already read its date from it."""

    red: frozenset[str] = frozenset()
    vault_failed: bool = False
    summary_sent: dict = field(default_factory=dict)

    @classmethod
    def from_row(cls, row: Optional[dict]) -> "PriorBeat":
        row = row or {}
        last = row.get("last_result") or {}
        red = set(last.get("red_jobs") or []) | set(last.get("red_probes") or [])
        red |= {k for k in map(_stage_key, last.get("stage_failures") or []) if k}
        return cls(
            red=frozenset(red),
            vault_failed=row.get("vault_outcome") == VAULT_FAILED,
            summary_sent=dict(last.get("summary_sent") or {}),
        )


def alert_keys(beat: Beat) -> set[str]:
    """Everything in this beat that is RED at alert time, by stable name."""
    keys = {j.label for j in beat.red_jobs} | {p.name for p in beat.red_probes}
    keys |= {k for k in map(_stage_key, beat.stage_failures) if k}
    return keys


def transitions(prior: set[str], current: set[str]) -> tuple[set[str], set[str]]:
    """(entered RED, recovered). Both empty = unchanged = silent."""
    return set(current) - set(prior), set(prior) - set(current)


def transition_note(entered: set[str], recovered: set[str]) -> str:
    parts = []
    if entered:
        parts.append("ENTERED RED: " + ", ".join(sorted(entered)))
    if recovered:
        parts.append("RECOVERED: " + ", ".join(sorted(recovered)))
    return " · ".join(parts)


def summary_due(at: datetime, sent: dict, slots: list[time]) -> Optional[str]:
    """The slot to summarise now, or None.

    The latest slot at or before `at` (ET) that has not been sent today.
    Only the latest: a beat that was dead at 07:00 does not send a stale
    07:00 summary at 16:45 — it sends 16:30's.
    """
    passed = [slot for slot in slots if slot <= at.time()]
    if not passed:
        return None
    slot = f"{passed[-1]:%H:%M}"
    return None if sent.get(slot) == at.date().isoformat() else slot


def _read_prior(beat: Beat, store: JobStore) -> PriorBeat:
    try:
        return PriorBeat.from_row(store.get(JOB_LABEL))
    except Exception as e:  # noqa: BLE001
        # Fail toward alerting: an unreadable prior makes every standing
        # red a transition once, never a silent beat.
        _stage_failure(beat, "alerts/prior-read", e)
        return PriorBeat()


def send_summary(beat: Beat) -> str:
    return _send_text(beat.summary_body())


def send_dm(beat: Beat) -> str:
    return _send_text(beat.dm_body())


def _send_text(text: str) -> str:
    from cobalt.notify import MattermostError, send_dm as _send

    try:
        result = _send(text)
    except MattermostError as e:
        # The alert path failing is itself worth saying, in the note and
        # in the log — it is the one failure the DM cannot report.
        logger.error("heartbeat: Mattermost DM FAILED — {}", e)
        return f"Mattermost DM FAILED: {e}"
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


def _run_alerts(
    beat: Beat, store: JobStore, prior: PriorBeat, *, dry_run: bool
) -> Optional[dict]:
    """Transition alert, then the scheduled summary.

    Returns the updated `summary_sent` map when a summary went out, else
    None. The beat itself keeps the full standing state either way — only
    the decision to SEND changes.
    """
    if dry_run:
        beat.notes.append("DRY RUN — no DM sent, nothing written.")
        return None

    entered, recovered = transitions(prior.red, alert_keys(beat))
    if entered or recovered:
        beat.notes.append(transition_note(entered, recovered))
        _attempt_alert(beat, "transition-dm", send_dm)

    try:
        slot = summary_due(beat.at, prior.summary_sent, summary_at())
    except Exception as e:  # noqa: BLE001
        _stage_failure(beat, "alerts/summary-dedup", e)
        slot = None
    if slot is None:
        return None
    before = len(beat.stage_failures)
    _attempt_alert(beat, "summary-dm", send_summary)
    if len(beat.stage_failures) != before:
        return None
    return {**prior.summary_sent, slot: beat.at.date().isoformat()}


def _beat_result(beat: Beat, *, sent_summary: Optional[dict]) -> dict:
    result = {
        "green": beat.green,
        "red_jobs": [j.label for j in beat.red_jobs],
        "red_probes": [p.name for p in beat.red_probes],
        "stage_failures": list(beat.stage_failures),
        "kill_switch": beat.kill_switch,
    }
    # Omission preserves the prior dedup value through JobStore's JSON merge.
    if sent_summary:
        result["summary_sent"] = sent_summary
    return result


def _persist_beat(beat: Beat, store: JobStore, *, sent_summary: Optional[dict]) -> None:
    store.ensure_schema()
    store.register(load_job_registry().spec(JOB_LABEL))
    store.record_heartbeat_result(
        JOB_LABEL,
        result=_beat_result(beat, sent_summary=sent_summary),
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

    try:
        write = write_note_block(beat, dry_run=dry_run, now=now)
    except DailyNoteAbsent as absent:
        reason = (
            f"daily note absent at {absent.path}; heartbeat status write deferred; "
            "com.cobalt.prefill-daily owns note creation; heartbeat never creates "
            "notes (L28.1)"
        )
        return (
            VAULT_DEFERRED_NOTE_ABSENT,
            reason,
        )
    if write is None:
        return VAULT_FAILED, "daily-note writer returned no result"
    beat.notes.append(write.report())
    if write.write_id is None:
        reason = (
            f"daily-note target {write.path}: writer returned action={write.action} "
            "without a write id"
        )
        return (
            VAULT_FAILED,
            reason,
        )
    return VAULT_WRITTEN, None


def _finalize(
    beat: Beat,
    store: JobStore,
    prior: PriorBeat,
    *,
    sent_summary: Optional[dict],
    dry_run: bool,
) -> None:
    if dry_run:
        return

    # Persistence and notification are deliberately separate attempts. If the
    # final database update fails, the corrective DM still runs.
    try:
        store.record_heartbeat_result(
            JOB_LABEL,
            result=_beat_result(beat, sent_summary=sent_summary),
            vault_outcome=beat.vault_outcome,
            vault_reason=beat.vault_reason,
        )
    except Exception as e:  # noqa: BLE001
        _stage_failure(beat, "FINALIZE/persist", e)

    # The vault unit is decided after ALERTS, so its transition is decided
    # here, against the prior beat's persisted `vault_outcome`.
    failed = beat.vault_outcome == VAULT_FAILED
    if failed != prior.vault_failed:
        beat.notes.append(
            transition_note({VAULT_KEY}, set()) if failed else transition_note(set(), {VAULT_KEY})
        )
        _attempt_alert(beat, "corrective-dm", send_dm)


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
    # Read BEFORE PERSIST overwrites the row: the transition is this beat
    # against the one before it.
    prior = PriorBeat()
    try:
        if not dry_run:
            prior = _read_prior(beat, store)
        sent_summary = _run_alerts(beat, store, prior, dry_run=dry_run)
    except Exception as e:  # noqa: BLE001
        sent_summary = None
        _stage_failure(beat, "alerts", e)

    logger.info("heartbeat: stage PERSIST")
    if not dry_run:
        try:
            _persist_beat(beat, store, sent_summary=sent_summary)
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
    elif beat.vault_outcome == VAULT_DEFERRED_NOTE_ABSENT:
        logger.info("heartbeat: vault unit DEFERRED — {}", beat.vault_reason)

    logger.info("heartbeat: stage FINALIZE")
    try:
        _finalize(beat, store, prior, sent_summary=sent_summary, dry_run=dry_run)
    except Exception as e:  # noqa: BLE001
        _stage_failure(beat, "FINALIZE", e)

    (logger.info if beat.green else logger.error)("heartbeat: {}", beat.headline)
    return beat


__all__ = [
    "DailyNoteAbsent",
    "INTERVAL_KEY",
    "JOB_LABEL",
    "PriorBeat",
    "SUMMARY_KEY",
    "VAULT_DEFERRED",
    "VAULT_DEFERRED_NOTE_ABSENT",
    "VAULT_FAILED",
    "VAULT_WRITTEN",
    "alert_keys",
    "interval_min",
    "run_beat",
    "summary_at",
    "summary_due",
    "take_beat",
    "transitions",
    "write_note_block",
]
