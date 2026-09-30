"""DRC D4 fix round 1 (L75) — the card apply goes through the ONE apply.

F-1 (HOLD 1, drc-d4-check-2026-09-25.md:122; D4-4; L3): `cobalt settings
load --card --apply` wrote `"user".trader_settings` by calling the store's
`put` directly, so `settings/cli.py`'s "every apply goes through
`apply_settings`" was false for one form. These tests fail while that
second write path exists.

OFFLINE: the store is `test_card_settings.py`'s constructed double, the
card file its constructed `DARK` text (L32 / L45 / L69). Symbols are
imported INSIDE each test so each is its own red.
"""

from __future__ import annotations

from pathlib import Path

SRC = Path(__file__).resolve().parents[2] / "src" / "cobalt"


def test_the_card_apply_writes_through_the_one_apply_function(tmp_path, monkeypatch):
    """F-1 (drc-d4-check-2026-09-25.md:122): the card apply calls
    `settings.cli.apply_settings` exactly once, with the reviewed hash in
    its source, its own actor, the whole-set delete and the same store."""
    from test_card_settings import DARK, FakeStore, _args, _write

    from cobalt.settings import card as card_mod
    from cobalt.settings import cli as settings_cli

    calls = []
    real = settings_cli.apply_settings

    def spy(*args, **kwargs):
        calls.append((args, kwargs))
        return real(*args, **kwargs)

    path, digest = _write(tmp_path, DARK)
    store = FakeStore({"card.curves": {"rvol": [[1, 1], [2, 2]]}})
    monkeypatch.setattr(settings_cli, "apply_settings", spy)
    monkeypatch.setattr(card_mod, "TraderSettingsStore", lambda: store)
    monkeypatch.setattr(settings_cli, "assert_writable", lambda *a, **k: None)
    monkeypatch.setattr(card_mod, "assert_writable", lambda *a, **k: None, raising=False)

    card_mod.cmd_load_card(_args(path, sha=digest, apply=True))

    assert len(calls) == 1, f"the card apply bypassed apply_settings: {calls}"
    _, kwargs = calls[0]
    assert digest in kwargs["source"]
    assert kwargs["actor"] == "settings.load.card"
    assert list(kwargs["delete"]) == ["card.curves"]
    assert kwargs["store"] is store
    assert len(store.puts) == 1


def test_the_settings_package_has_one_caller_of_put():
    """F-1 (drc-d4-check-2026-09-25.md:122; L3): inside `src/cobalt/settings`
    only `cli.py` (`apply_settings`) calls a store's `.put(`. `store.py`
    DEFINES `def put(`, which the `.put(` match does not contain.

    The ONE other writer of `trader_settings` rows in `src/` is outside
    this row: `radar/notes.py:747` `mirror_sources` — the radar's machine
    mirror of his radar notes (`radar.note.*` keys, S2-P4), with its own
    market-reset refusal (`:731`-`:732`); it is not a `cobalt settings load
    --apply` form and not D4's file (L52: `src/cobalt/radar` untouched)."""
    root = SRC / "settings"
    callers = sorted(p.name for p in root.glob("*.py") if ".put(" in p.read_text(encoding="utf-8"))
    offenders = [name for name in callers if name != "cli.py"]
    assert set(callers) == {"cli.py"}, f"a second caller of .put( in settings/: {offenders}"
