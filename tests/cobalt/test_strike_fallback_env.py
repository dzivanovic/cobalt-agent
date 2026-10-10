"""strike-fallback-env-1010 row A (offline): the sheet's fallback thread
starts with the DB env loaded.

`python -m cobalt.aset` is run through `runpy` with `uvicorn.run` a no-op
and `start_fallback_thread` replaced by one real `FallbackTail` pass over a
store whose `seam_rows` opens `cobalt.db._open` (its `psycopg.connect`
stubbed: nothing is reached). `dotenv.load_dotenv` is a recording fake that
fills the three DB names — so the pass sees them only if `__main__` loaded
`.env` BEFORE it started the thread. The three names are cleared first:
`tests/conftest.py:13` loads `.env` into the test process. Constructed
values only (L32).
"""

from __future__ import annotations

import runpy
from datetime import datetime, timezone
from pathlib import Path

import pytest

DB_NAMES = ("POSTGRES_HOST", "COBALT_DB_USER", "COBALT_DB_PASSWORD")
T0 = datetime(2001, 1, 2, 15, 0, 5, tzinfo=timezone.utc)


def _run_main(monkeypatch, *, fills: bool) -> list:
    import dotenv
    import uvicorn

    import cobalt.aset.config  # noqa: F401 — imported before the fakes, so its chain sees the real ones
    import cobalt.aset.net
    import cobalt.aset.strike
    from cobalt import db
    from cobalt.aset.strike import FallbackTail
    from cobalt.strike.delivery_config import DeliverySettings

    for name in DB_NAMES:
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv("LOGURU_LEVEL", "INFO")

    paths: list = []

    def load_dotenv(*args, **kwargs):
        paths.append(args[0] if args else kwargs.get("dotenv_path"))
        if fills:
            for name in DB_NAMES:
                monkeypatch.setenv(name, "constructed")
        return fills

    class SeamOnDb:
        def seam_rows(self, after_id, day):
            db._open("cobalt_dev")
            return []

    def start_fallback_thread():
        FallbackTail(store=SeamOnDb(), send=lambda text: None, settings=DeliverySettings(),
                     now=lambda: T0).pass_once()

    monkeypatch.setattr(dotenv, "load_dotenv", load_dotenv)
    monkeypatch.setattr(uvicorn, "run", lambda *a, **kw: None)
    monkeypatch.setattr(cobalt.aset.net, "local_lan_ip", lambda: None)
    monkeypatch.setattr(cobalt.aset.strike, "start_fallback_thread", start_fallback_thread)
    monkeypatch.setattr(db.psycopg, "connect", lambda *a, **kw: object())

    runpy.run_module("cobalt.aset.__main__", run_name="__main__")
    return paths


def test_a1_main_loads_the_repo_env_before_the_fallback_thread_starts(monkeypatch):
    paths = _run_main(monkeypatch, fills=True)
    assert len(paths) == 1, paths
    path = Path(paths[0])
    assert path.name == ".env"
    assert (path.parent / "pyproject.toml").is_file()
    assert path == Path(__file__).resolve().parents[2] / ".env"


def test_a2_no_env_anywhere_still_fails_loud(monkeypatch):
    from cobalt.db import DbConfigError

    with pytest.raises(DbConfigError, match="Missing Postgres settings for the APP credential"):
        _run_main(monkeypatch, fills=False)
