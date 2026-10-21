"""cos-env-load rows E1, E2 (offline): `com.cobalt.cos` loads the repo `.env`.

A launchd start hands `cobalt.cos.run` only `PATH` and `COBALT_ENV`
(`ops/com.cobalt.cos.plist`), and `ops/start_cos.sh` exports no Postgres
setting, so `main()` must load `.env` itself before its first DB read. Each
test clears every `PG*`, `POSTGRES_*` and `COBALT_*` name (`tests/conftest.py`
loads `.env` into the test process), sets `COBALT_ENV=dev` as the plist sets
one `COBALT_*` name, points `run.ENV_FILE` at a constructed decoy under
`tmp_path`, and runs `run.main([])` with `refuse_if_agent_alive` and
`psycopg.connect` as recorders: nothing is reached. Constructed values only
(L32); the real `.env` is never opened.
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest

DB_NAMES = ("POSTGRES_HOST", "COBALT_DB_USER", "COBALT_DB_PASSWORD")
CLEARED_PREFIXES = ("PG", "POSTGRES_", "COBALT_")
DECOY = {
    "POSTGRES_HOST": "decoy-host.invalid",
    "POSTGRES_PORT": "5999",
    "COBALT_DB_USER": "decoy_user",
    "COBALT_DB_PASSWORD": "decoy-pass",
}


class Reached(Exception):
    """The DSN reached `psycopg.connect`: the env was there."""


def _launchd_start(monkeypatch, tmp_path, *, decoy: bool):
    from cobalt import db
    from cobalt.cos import run

    import cobalt.jobs.config  # noqa: F401 — main's local imports, imported before the clear
    import cobalt.jobs.killswitch  # noqa: F401
    import cobalt.jobs.store  # noqa: F401
    import cobalt.jobs.wrapper  # noqa: F401

    # `load_dotenv` writes os.environ behind monkeypatch's back: a setenv
    # first makes the undo remove what the load adds.
    for name in DECOY:
        monkeypatch.setenv(name, "")
    for name in list(os.environ):
        if name.startswith(CLEARED_PREFIXES):
            monkeypatch.delenv(name)
    monkeypatch.setenv("COBALT_ENV", "dev")

    if decoy:
        env_file = tmp_path / ".env"
        env_file.write_text("".join(f"{k}={v}\n" for k, v in DECOY.items()))
    else:
        env_file = tmp_path / "absent" / ".env"
    monkeypatch.setattr(run, "ENV_FILE", env_file, raising=False)

    seen: list[dict] = []
    dsns: list[str] = []

    def refuse_if_agent_alive(spec=None):
        seen.append({name: os.environ.get(name) for name in DB_NAMES})

    def connect(dsn, *args, **kwargs):
        dsns.append(dsn)
        raise Reached(dsn)

    monkeypatch.setattr(run, "refuse_if_agent_alive", refuse_if_agent_alive)
    monkeypatch.setattr(db.psycopg, "connect", connect)
    return run, seen, dsns


def test_e1_a_launchd_start_reads_the_repo_env_file(monkeypatch, tmp_path):
    run, seen, dsns = _launchd_start(monkeypatch, tmp_path, decoy=True)

    with pytest.raises(Reached):
        run.main([])

    assert seen == [{
        "POSTGRES_HOST": "decoy-host.invalid",
        "COBALT_DB_USER": "decoy_user",
        "COBALT_DB_PASSWORD": "decoy-pass",
    }]
    assert len(dsns) == 1
    assert "decoy_user" in dsns[0]
    assert "@decoy-host.invalid:5999/cobalt_dev" in dsns[0]


def test_e1_the_env_file_is_the_repo_one():
    from cobalt.cos import run

    assert run.ENV_FILE == Path(run.__file__).resolve().parents[3] / ".env"
    assert run.ENV_FILE.name == ".env"
    assert (run.ENV_FILE.parent / "pyproject.toml").is_file()


def test_e2_the_environment_wins_over_the_file(monkeypatch, tmp_path):
    run, seen, dsns = _launchd_start(monkeypatch, tmp_path, decoy=True)
    monkeypatch.setenv("POSTGRES_HOST", "env-host.invalid")

    with pytest.raises(Reached):
        run.main([])

    assert len(dsns) == 1
    assert "@env-host.invalid:5999/" in dsns[0]
    assert "decoy_user" in dsns[0]


def test_e2_no_env_file_and_no_env_still_fails_loud(monkeypatch, tmp_path):
    from cobalt.db import DbConfigError

    run, seen, dsns = _launchd_start(monkeypatch, tmp_path, decoy=False)

    with pytest.raises(DbConfigError, match="Missing Postgres settings for the APP credential"):
        run.main([])

    assert dsns == []
