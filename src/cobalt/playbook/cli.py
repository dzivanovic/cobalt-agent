"""`cobalt playbook` — the command `com.cobalt.playbook` runs (Sunday 17:30 ET).

    cobalt playbook render [--date YYYY-MM-DD] [--out DIR] [--dry-run]

`render` goes through the F17 wrapper, and the config loads INSIDE it, so
every failure — dead database, missing strategies folder, a finished note
that fails validation, a bad `playbook.yaml`, an unwritable folder, a save
error — is a red job row with `exit_code=1` and the exception propagates
(L1). A draft note is not a failure: it is listed on stdout.

`--dry-run` skips the wrapper and writes nothing: it prints the families,
counts and paths a run would write, and leaves no job row (L10).

THE IMPORT SEAM (FINAL [F-17]). `data`, `deck` and python-pptx are imported
inside the command only: `cobalt.cli` imports this module for `add_parser`,
and `import cobalt.cli` must leave `pptx` unloaded.

THE SWAP (FINAL [F-11], C11), `publish()`: decks are written only into a
fresh `<date>.tmp`; then `<date>` → `<date>.old`, `<date>.tmp` → `<date>`,
`<date>.old` deleted. `<date>` is never deleted first, so every ending
leaves either the previous folder or the complete new one.
"""

from __future__ import annotations

import argparse
import shutil
from datetime import date
from pathlib import Path
from typing import Callable, Optional

from cobalt.jobs.wrapper import job_run

from .config import load_playbook_config

JOB_LABEL = "com.cobalt.playbook"


class PlaybookRunError(RuntimeError):
    """A render that did not produce its six decks."""


def _iso_date(raw: str) -> str:
    try:
        return date.fromisoformat(raw).isoformat()
    except ValueError:
        raise argparse.ArgumentTypeError(f"{raw!r} is not a YYYY-MM-DD date") from None


def _now_et():
    """The ET wall clock, from the ONE session clock."""
    from cobalt.session import clock as clock_mod
    from cobalt.session.clock import session_clock

    return session_clock().to_et(clock_mod.now_utc())


def _rename(src: Path, dst: Path) -> None:
    src.rename(dst)


def publish(out_dir: Path, day: str, write: Callable[[Path], list]) -> list:
    """The C11 swap. `write(folder)` writes the decks and returns `deck.Written`s.

    Before the run: a leftover `<day>.old` with no `<day>` is the previous
    run a kill stranded between the two renames — it is renamed back first;
    a leftover `<day>.old` beside a `<day>` is the debris of a kill after
    the swap and is deleted. A leftover `<day>.tmp` is deleted, never
    written into.
    """
    from .data import DECK_NAMES

    out_dir.mkdir(parents=True, exist_ok=True)
    final, tmp, old = out_dir / day, out_dir / f"{day}.tmp", out_dir / f"{day}.old"
    if old.exists():
        if final.exists():
            shutil.rmtree(old)
        else:
            _rename(old, final)
    if tmp.exists():
        shutil.rmtree(tmp)
    tmp.mkdir()
    written = write(tmp)
    missing = [n for n in DECK_NAMES if not (tmp / f"{n}.pptx").is_file()]
    if missing:
        raise PlaybookRunError(f"{tmp}: decks not written: {', '.join(missing)} — a missing file is a failed run")
    had_previous = final.exists()
    if had_previous:
        _rename(final, old)
    try:
        _rename(tmp, final)
    except BaseException:
        if had_previous:
            _rename(old, final)
        raise
    if had_previous:
        shutil.rmtree(old)
    return [type(w)(name=w.name, path=final / w.path.name, slides=w.slides, cards=w.cards) for w in written]


def _out_dir(args: argparse.Namespace, cfg) -> Path:
    return Path(args.out).expanduser().resolve() if args.out else cfg.out_path()


def _result(day: str, book, written: Optional[list] = None) -> dict:
    """The per-family counts F18 and a later cap card read from the job row."""
    slides = {w.name: w.slides for w in written or []}
    return {
        "date": day,
        "families": {
            d.name: {"setups": len(d.setups), "cards": len(d.cards), "in_family": d.in_family,
                     "slides": slides.get(d.name)}
            for d in book.decks if not d.is_unfiled
        },
        "unfiled": len(book.deck("unfiled").cards),
        "drafts": list(book.drafts),
    }


def _print_tail(book) -> None:
    print(f"unfiled cards: {len(book.deck('unfiled').cards)}")
    print(f"drafts: {', '.join(book.drafts) if book.drafts else 'none'}")


def cmd_render(args: argparse.Namespace) -> None:
    from . import data, deck  # F-17: python-pptx loads here, never at `import cobalt.cli`

    day = args.date or _now_et().date().isoformat()
    if args.dry_run:
        cfg = load_playbook_config()
        book = data.load_playbook(cfg.latest_per_family)
        folder = _out_dir(args, cfg) / day
        print("DRY RUN — no deck written, no job row")
        for d in book.decks:
            print(f"{folder / f'{d.name}.pptx'}  {d.name}: setups {len(d.setups)}, cards {len(d.cards)}")
        _print_tail(book)
        return

    with job_run(JOB_LABEL) as run:
        cfg = load_playbook_config()
        book = data.load_playbook(cfg.latest_per_family)
        rendered_at = _now_et()
        written = publish(_out_dir(args, cfg), day, lambda folder: deck.write_all(
            book, folder, run_date=date.fromisoformat(day), rendered_at=rendered_at,
            rows_per_slide=cfg.rows_per_slide, why_max_chars=cfg.why_max_chars,
        ))
        run.result = _result(day, book, written)
    for w in written:
        print(f"{w.path}  slides {w.slides}  cards {w.cards}")
    _print_tail(book)


def _add_render(psub) -> None:
    render = psub.add_parser("render", help="Write one .pptx per setup family, plus unfiled.")
    render.add_argument("--date", type=_iso_date, default=None,
                        help="The run date, YYYY-MM-DD (default: today ET). Labels the week and the folder.")
    render.add_argument("--out", default=None,
                        help="Folder the dated deck folder goes under (default: out_dir in "
                             "configs/cobalt/playbook.yaml).")
    render.add_argument("--dry-run", action="store_true",
                        help="Print families, counts and paths; write no deck and no job row.")
    render.set_defaults(func=cmd_render)


def add_parser(sub) -> None:
    playbook = sub.add_parser("playbook", help="The Sunday playbook decks (com.cobalt.playbook).")
    _add_render(playbook.add_subparsers(dest="command", required=True))


def build_parser() -> argparse.ArgumentParser:
    """`cobalt playbook` on its own (tests and a direct entry point)."""
    parser = argparse.ArgumentParser(prog="cobalt playbook")
    _add_render(parser.add_subparsers(dest="command", required=True))
    return parser


__all__ = ["JOB_LABEL", "PlaybookRunError", "add_parser", "build_parser", "cmd_render", "publish"]
