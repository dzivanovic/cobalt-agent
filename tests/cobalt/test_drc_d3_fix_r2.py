"""DRC D3 fix round 2 — the OFFLINE rows (`prompts/2026-09-29/21-drc-d3-fix-r2-build.md`
`## THE FIX ROWS`, L75): F-1r2 red first on `15c23748` with its pin, and
the two RUNs (L70: stated as a `UserWarning`, never asserted).

Each row is backed by a `09-29/09` HOLD or NOT CHECKABLE line
(`reports/drc-d3-fix-r1-check-2026-09-29.md` `## Checked against the
branch`). The harness is `test_drc_build.py`'s, BY IMPORT (its `_Store`
double, `_record`, `_deps`, `_vault`, the helpers) — never a copy.
Constructed 2001 dates, symbols and strategy titles only (L32 / L45 / L69);
every note in a `tmp_path` vault.
"""

from __future__ import annotations

import argparse
import warnings

import pytest


def _build_parser():
    """`cobalt drc` built IN-PROCESS: the top parser, its subparsers, and
    `cobalt.drc.cli.add_parser` on them — the CLI's own flags."""
    from cobalt.drc import cli as drc_cli

    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers()
    drc_cli.add_parser(sub)
    return parser, sub


# ---------------------------------------------------------------------
# F-1r2 — `--dry-run --no-trades` writes nothing (L10, L1, L3)
# ---------------------------------------------------------------------


def test_f1r2_the_dry_run_with_no_trades_writes_nothing(capsys, monkeypatch):
    """F-1r2 (`drc-d3-fix-r1-check-2026-09-29.md:119`; `09-28/10` D3-4
    "`--dry-run` writes nothing"): `cobalt drc build --date D --dry-run
    --no-trades` never reaches `imports.no_trade` nor
    `DrcStore.record_stated_book`; it is refused with ONE named line and
    exit 2 (the misuse exit)."""
    from cobalt.drc import cli as drc_cli
    from cobalt.drc.store import DrcStore

    from test_drc_build import D

    called: list[str] = []

    def no_trade_spy(*args, **kwargs):
        called.append("no_trade")
        raise AssertionError("imports.no_trade called on a dry run")

    def record_spy(*args, **kwargs):
        called.append("record_stated_book")
        raise AssertionError("record_stated_book called on a dry run")

    monkeypatch.setattr("cobalt.drc.imports.no_trade", no_trade_spy)
    monkeypatch.setattr(DrcStore, "record_stated_book", record_spy)
    parser, _ = _build_parser()
    args = parser.parse_args(["drc", "build", "--date", D.isoformat(), "--dry-run", "--no-trades"])
    with pytest.raises(SystemExit) as e:
        args.func(args)
    assert e.value.code == 2
    assert drc_cli.DRY_RUN_NO_TRADES == (
        "refused: --dry-run with --no-trades — a no-trade DRC is a statement; preview it with "
        "cobalt drc state-book --no-trade DAY (a dry run unless --apply)"
    )
    assert drc_cli.DRY_RUN_NO_TRADES in capsys.readouterr().out
    assert called == []


def test_f1r2_pin_the_build_command_has_exactly_two_flags():
    """F-1r2 PIN (green before and after; `drc-d3-fix-r1-check-2026-09-29.md:119`):
    the `build` subparser's `store_true` flags are EXACTLY `dry_run` and
    `no_trades` — so every accepted combination carrying `--dry-run` is
    `{--dry-run}` (fix r1's F-1) or `{--dry-run, --no-trades}` (F-1r2), and
    a new flag fails here until its dry-run combination is covered."""
    _, sub = _build_parser()
    group = sub.choices["drc"]
    commands = next(a for a in group._actions if isinstance(a, argparse._SubParsersAction))
    build = commands.choices["build"]
    flags = {a.dest for a in build._actions if isinstance(a, argparse._StoreTrueAction)}
    assert flags == {"dry_run", "no_trades"}


# ---------------------------------------------------------------------
# RUN-4 / RUN-5 (L70) — stated, never asserted
# ---------------------------------------------------------------------


@pytest.mark.skipif('not (os.getenv("POSTGRES_HOST") and os.getenv("POSTGRES_USER"))', reason="reaches cobalt_dev (lock-relief G1)")
def test_run4_a_dry_run_with_the_real_risk_parameters_opens_nothing_for_write(tmp_path, capsys, monkeypatch):
    """RUN-4 (`drc-d3-fix-r1-check-2026-09-29.md:123`, NOT CHECKABLE): fix r1
    F-1's harness with the REAL `prefill.drc.risk_parameters_line` — every
    `open` whose mode writes, every `os.open` whose flags write, and every
    `os.replace` / `os.rename` / `os.mkdir`, recorded (each passes through)
    during `cmd_build(--dry-run)`. The result is STATED; a raise is caught
    and stated."""
    import builtins
    import io
    import os

    from cobalt.drc import cli as drc_cli
    from cobalt.prefill.drc import risk_parameters_line, rules_checkbox_block

    from test_drc_build import D, _deps, _record, _Store, _vault

    store = _Store()
    root = _vault(tmp_path)
    _record(store)
    deps = _deps(store, root, rules_block=rules_checkbox_block, risk_parameters=risk_parameters_line)
    seen: list[str] = []
    on = [False]
    real_open, real_io_open, real_os_open = builtins.open, io.open, os.open
    real_replace, real_rename, real_mkdir = os.replace, os.rename, os.mkdir
    write_flags = os.O_WRONLY | os.O_RDWR | os.O_CREAT

    def _mode(args, kwargs) -> str:
        return str(args[1] if len(args) > 1 else kwargs.get("mode", "r"))

    def wrap_open(real, label):
        def wrapped(*args, **kwargs):
            if on[0] and any(c in _mode(args, kwargs) for c in "wax+"):
                seen.append(f"{label}({args[0]!s}, {_mode(args, kwargs)})")
            return real(*args, **kwargs)
        return wrapped

    def wrapped_os_open(path, flags, *args, **kwargs):
        if on[0] and flags & write_flags:
            seen.append(f"os.open({path!s}, {flags:#o})")
        return real_os_open(path, flags, *args, **kwargs)

    def wrap_path(real, label):
        def wrapped(*args, **kwargs):
            if on[0]:
                seen.append(f"{label}({', '.join(str(a) for a in args)})")
            return real(*args, **kwargs)
        return wrapped

    monkeypatch.setattr(builtins, "open", wrap_open(real_open, "open"))
    monkeypatch.setattr(io, "open", wrap_open(real_io_open, "io.open"))
    monkeypatch.setattr(os, "open", wrapped_os_open)
    monkeypatch.setattr(os, "replace", wrap_path(real_replace, "os.replace"))
    monkeypatch.setattr(os, "rename", wrap_path(real_rename, "os.rename"))
    monkeypatch.setattr(os, "mkdir", wrap_path(real_mkdir, "os.mkdir"))
    try:
        on[0] = True
        try:
            drc_cli.cmd_build(argparse.Namespace(date=D, dry_run=True, no_trades=False), deps=deps)
        finally:
            on[0] = False
        message = (
            "RUN-4: files opened for write on a dry run with the real risk_parameters_line = "
            f"{len(seen)}; {'; '.join(seen) if seen else 'none'}"
        )
    except BaseException as e:  # noqa: BLE001 — the RUN states a raise, never fixes it (L70)
        import traceback

        frames = [f"{f.filename.rsplit('/src/', 1)[-1]}:{f.lineno} {f.name}" for f in traceback.extract_tb(e.__traceback__)]
        message = (
            f"RUN-4: raised {type(e).__name__}: {e} | raised through: {' <- '.join(reversed(frames[-4:]))} | "
            f"files opened for write before the raise = {len(seen)}; {'; '.join(seen) if seen else 'none'}"
        )
    capsys.readouterr()
    warnings.warn(message, UserWarning)


def test_run5_the_unmapped_count_under_a_non_utf8_note(tmp_path):
    """RUN-5 (`drc-d3-fix-r1-check-2026-09-29.md:120`, NOT CHECKABLE): fix r1
    F-5's construction (a strategy note holding a non-UTF-8 byte), the build
    over it; the `build_day` row's `unmapped_playbooks` and, from each
    `build_trade` row's `playbooks`, the names that did not map. STATED."""
    from cobalt.drc import build

    from test_drc_build import D, STRATEGIES, _deps, _record, _Store, _vault

    try:
        root = _vault(tmp_path)
        (root / STRATEGIES / "Gamma Setup.md").write_bytes(b"---\ntrade_def: example-gamma-setup\n---\n\xff\n")
        store = _Store()
        build.run_drc_build(_record(store), deps=_deps(store, root))
        rows = store.build[D]
        (day,) = [r for r in rows if r["kind"] == "build_day"]
        unmapped = [
            p for r in rows if r["kind"] == "build_trade" for p in r["derived"]["playbooks"] if p.get("setup") is None
        ]
        names = [p["name"] for p in unmapped]
        message = (
            f"RUN-5: unmapped playbooks = {day['derived']['unmapped_playbooks']}; names = {names}; "
            f"the non-UTF-8 note's name among them = {any(p.get('stripped') == 'Gamma Setup' for p in unmapped)}"
        )
    except Exception as e:  # noqa: BLE001 — the RUN states a raise, never fixes it (L70)
        message = f"RUN-5: raised {type(e).__name__}: {e}"
    warnings.warn(message, UserWarning)
