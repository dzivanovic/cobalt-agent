"""`cobalt voice turn` — the turn function's third caller ([F-01], FINAL §8).

    cobalt voice turn --text "<text>"  [--dry-run] [--session S]
    cobalt voice turn --audio <file>   [--dry-run] [--session S]
    cobalt voice turn --confirm <turn_id> [--session S]

Any house runs the SAME path in DEV with synthetic audio or text ([F-02]).
`--dry-run` prints the Plan, the resolution and the exact change and writes
nothing — no row, no pending action. `--confirm` is REFUSED when
`COBALT_ENV=production`: in production an act is confirmed only by the
widget (a tap, or his next spoken / typed turn); no house confirms a
production act (L37). `--audio` takes the scratch-dir lock for the length
of its turn and refuses, named, while a server holds it.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from cobalt import env

from . import scratch
from .config import load_voice_config
from .turn import TurnInput, default_deps, run_turn

DEFAULT_SESSION = "cli-local"


def _fail(msg: str) -> None:
    print(f"FAILED: {msg}", file=sys.stderr)
    sys.exit(2)


def cmd_turn(args: argparse.Namespace) -> None:
    session = args.session
    if args.confirm:
        if env.is_production():
            _fail("--confirm is refused in production: an act there is confirmed only by the widget "
                  "(a tap or his own next turn) — no house confirms a production act (L37, FINAL [F-02]).")
        inp = TurnInput(session_id=session, source="cli", tap="confirm", pending_turn_id=args.confirm)
        return _run(inp, args, lock=None)
    if args.audio:
        path = Path(args.audio)
        ext = path.suffix.lstrip(".").lower()
        ctype = scratch.EXTENSIONS.get(ext)
        if ctype is None:
            _fail(f"unsupported audio file type {path.suffix!r} — the closed map is {sorted(scratch.EXTENSIONS)}")
        cfg = load_voice_config()
        try:
            lock = scratch.DirectoryLock(cfg.scratch_dir)
        except scratch.ScratchLocked as e:
            _fail(f"{e} (a server owns the scratch dir; use the widget or --text)")
        inp = TurnInput(session_id=session, source="cli", audio=path.read_bytes(), content_type=ctype,
                        dry_run=args.dry_run)
        return _run(inp, args, lock=lock)
    inp = TurnInput(session_id=session, source="cli", text=args.text, dry_run=args.dry_run)
    return _run(inp, args, lock=None)


def _run(inp: TurnInput, args: argparse.Namespace, *, lock) -> None:
    try:
        out = run_turn(inp, default_deps())
    finally:
        if lock is not None:
            lock.release()
    print(f"turn:  {out.turn_id}")
    print(f"state: {out.state.value}")
    if out.transcript is not None:
        print(f"heard: {out.transcript}")
    print(f"reply: {out.reply}")
    for line in out.degraded:
        print(f"{line.level.upper()}: {line.text}")
    if out.pending_turn_id:
        print(f"pending: {out.pending_turn_id} (confirm in the widget; in dev: --confirm {out.pending_turn_id})")
    if out.dry_run is not None:
        print("dry run (nothing written):")
        print(json.dumps(out.dry_run, indent=2, default=str))
    if out.state.value == "failed":
        sys.exit(1)


def add_parser(sub) -> None:
    v = sub.add_parser("voice", help="Voice V1: one turn through the same function the widget uses.")
    vsub = v.add_subparsers(dest="command", required=True)
    t = vsub.add_parser("turn", help="Run one voice turn (text, audio file, or a dev confirm).")
    src = t.add_mutually_exclusive_group(required=True)
    src.add_argument("--text", help="The words, as the text box would send them.")
    src.add_argument("--audio", help="An audio file (webm / ogg / m4a / wav) — synthetic in dev.")
    src.add_argument("--confirm", metavar="TURN_ID", help="DEV ONLY: confirm a pending act (refused in production).")
    t.add_argument("--dry-run", action="store_true", help="Print the Plan, resolution and change; write nothing.")
    t.add_argument("--session", default=DEFAULT_SESSION, help="The widget-session id this turn belongs to.")
    t.set_defaults(func=cmd_turn)


__all__ = ["add_parser", "cmd_turn"]
