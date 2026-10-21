"""The `com.cobalt.cos` resident (F20 FINAL §2, §5; F-14, F-20; L18). `python -m cobalt.cos.run`

NO `_Beater`. A beater thread stamps `heartbeat_at` whatever the loop is
doing, so a hung poll would look alive forever. Here the LOOP stamps: each
iteration calls `JobStore.beat` first, then polls the listener, runs one
executor claim, the sweeper and the outcome report. A blocked iteration
stamps nothing more, the stamp goes stale, and the watchdog's ZOMBIE rule
(`jobs/watchdog.py`, unchanged) turns it RED (T12).

THE LIFECYCLE is the wrapper's own store calls — `ensure_schema`,
`register`, the kill-switch refusal, `mark_running`, `mark_finished` —
without `job_run`, whose body always starts the beater (card DECISIONS).

ONE LISTENER (L3, F-14): the resident refuses to start while the
`com.cobalt.agent` pidfile holds a live pid — FAILED, loud. A stale pidfile
does not hold it. The row ships `enabled: false`: nothing loads it until
the deploy's D14 checklist (BOOTSTRAP deferred).
"""

from __future__ import annotations

import argparse
import asyncio
import shutil
import time
import traceback
from pathlib import Path
from typing import Callable, Optional

from dotenv import load_dotenv
from loguru import logger

JOB_LABEL = "com.cobalt.cos"
AGENT_LABEL = "com.cobalt.agent"
CHANNEL = "dm"
AGENT_ID = "cos"
#: The session's cwd: an empty scratch dir under the job state dir (§4).
SCRATCH_DIR = Path(__file__).resolve().parents[3] / "data" / "cos" / "scratch"
#: The repo `.env`, loaded at the top of `main()` (cos-env-load).
ENV_FILE = Path(__file__).resolve().parents[3] / ".env"


class CosRefused(RuntimeError):
    """The resident refused to start. Loud."""


def refuse_if_agent_alive(spec=None) -> None:
    """F-14 / C9: no second listener on the bot while the old agent lives."""
    from cobalt.jobs.config import load_job_registry
    from cobalt.jobs.watchdog import pidfile_alive

    spec = spec or load_job_registry().spec(AGENT_LABEL)
    alive, detail = pidfile_alive(spec)
    if alive:
        raise CosRefused(
            f"REFUSED: {AGENT_LABEL} is alive ({detail}). Two listeners on one bot is two "
            "approve paths (F-14); the deploy's D14 checklist stops it first."
        )


class Loop:
    """One iteration = beat, poll, then each step. Stops at `keep_running` False."""

    def __init__(self, *, store, poll: Callable[[], object], steps: list[Callable[[], object]],
                 keep_running: Callable[[], bool], poll_interval_s: float, label: str = JOB_LABEL,
                 sleep: Callable[[float], None] = time.sleep):
        self.store = store
        self.poll = poll
        self.steps = steps
        self.keep_running = keep_running
        self.poll_interval_s = poll_interval_s
        self.label = label
        self.sleep = sleep

    def iteration(self) -> None:
        self.store.beat(self.label)
        self.poll()
        for step in self.steps:
            try:
                step()
            except Exception as e:  # noqa: BLE001 - logged loud; the next iteration retries
                logger.exception("CoS step {} failed: {}: {}", getattr(step, "__name__", step),
                                 type(e).__name__, e)

    def run(self) -> None:
        while self.keep_running():
            self.iteration()
            self.sleep(self.poll_interval_s)


def _build(job_store):
    """The live wiring: session, turn store, listener, executor steps."""
    from cobalt.agents.registry import AGENTS_DIR, load_entry
    from cobalt.hitl import executor
    from cobalt.notify.mattermost import send_dm

    from .listener import Listener
    from .session import POLL_KEY, CosSession, tunable_int
    from .store import CosStore

    entry = load_entry(AGENTS_DIR / f"{AGENT_ID}.yaml")
    poll_s = tunable_int(POLL_KEY)
    # §4: the session's cwd is EMPTY — whatever a previous process left goes.
    if SCRATCH_DIR.exists():
        shutil.rmtree(SCRATCH_DIR)
    SCRATCH_DIR.mkdir(parents=True)
    turns = CosStore()
    turns.ensure_schema()
    from cobalt.hitl.store import HitlStore

    hitl = HitlStore()
    hitl.ensure_schema()
    session = CosSession(model=entry.chassis.model, scratch_dir=SCRATCH_DIR, charter=entry.charter)
    notes: list[str] = []

    def run_turn(text: str):
        current = turns.session(CHANNEL, AGENT_ID)
        prompt = "\n".join([*notes, text]) if notes else text
        notes.clear()
        outcome = asyncio.run(session.run_turn(prompt, resume=current["session_id"] if current else None))
        if outcome.session_id:
            turns.save_session(CHANNEL, AGENT_ID, outcome.session_id)
        return outcome

    listener = Listener(store=turns, run_turn=run_turn, reply=send_dm, since_ms=int(time.time() * 1000))
    steps = [
        lambda: executor.run_one(store=hitl),
        lambda: executor.sweep(store=hitl),
        lambda: notes.extend(executor.report_outcomes(store=hitl)),
    ]
    return listener, steps, poll_s


def main(argv: Optional[list[str]] = None) -> int:
    # launchd hands this process no Postgres settings (the plist sets PATH and
    # COBALT_ENV only), start_cos.sh exports none, and no import chain in cos
    # loads .env — card 929's first start died on DbConfigError. Load the repo
    # .env deliberately, as aset/__main__.py does, before any registry or store
    # read; the environment still wins. In main, not at import, so importing
    # this module loads nothing.
    load_dotenv(ENV_FILE)
    from cobalt.jobs import killswitch
    from cobalt.jobs.config import load_job_registry
    from cobalt.jobs.store import JobStore
    from cobalt.jobs.wrapper import JobStopped, should_keep_running

    parser = argparse.ArgumentParser(prog="cobalt.cos.run")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)
    spec = load_job_registry().spec(JOB_LABEL)
    if args.dry_run:
        from .session import build_options

        print(build_options(model="(cos.yaml)", cwd=SCRATCH_DIR, charter="(cos.yaml)",
                            max_turns=0, resume=None))
        return 0
    refuse_if_agent_alive()
    store = JobStore()
    store.ensure_schema()
    store.register(spec)
    if killswitch.is_active(store):
        state = killswitch.read(store)
        logger.error("F17: {} REFUSED TO START — {}", JOB_LABEL, state.describe())
        raise JobStopped(state.describe())
    store.mark_running(JOB_LABEL)
    try:
        listener, steps, poll_s = _build(store)
        Loop(store=store, poll=listener.poll, steps=steps,
             keep_running=lambda: should_keep_running(JOB_LABEL, store=store),
             poll_interval_s=poll_s).run()
    except BaseException as e:
        store.mark_finished(JOB_LABEL, exit_code=1,
                            error=f"{type(e).__name__}: {e}\n{traceback.format_exc(limit=8)}",
                            result=None)
        raise
    store.mark_finished(JOB_LABEL, exit_code=0, result={"stopped": True})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
