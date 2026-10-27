"""radar-mirror-scope-port4 W1: radar builds the old tree's `Config` once, in
its main thread, before it starts the strike thread.

Port3's deploy (card 1041) failed smoke (b): the strike thread's first tick
raised `'Config' object has no attribute '_config'` (`radar.err:103098`).
`Config.__new__` sets `cls._instance` before `_config`, so a second thread
calling `get_instance()` inside `_load_config()` gets an instance with no
`_config`; radar's strike thread and its resident both reach it at start-up
(`resolve_token` → `FinvizApiClient` → `get_config`). The real module is
never imported: a fake `cobalt_agent.config` of the same shape sits in
`sys.modules`, its load held open by a forced delay. Constructed values only
(L32).
"""

from __future__ import annotations

import sys
import threading
import time
import types
from contextlib import contextmanager
from types import SimpleNamespace

import pytest

import cobalt.radar.runner as r


@pytest.fixture
def fake_config(monkeypatch):
    """A `cobalt_agent.config` whose `Config` is shaped as `config.py:400-421`:
    `__new__` sets `cls._instance` first, then `_config = _load()`. The load
    sets `loading` and sleeps, so a second thread can see it half-built."""
    state = SimpleNamespace(callers=[], loading=threading.Event())

    def _load():
        state.loading.set()
        time.sleep(0.3)
        return {"loaded": True}

    class Config:
        _instance = None

        def __new__(cls):
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._instance._config = _load()
            return cls._instance

        @staticmethod
        def get_instance():
            state.callers.append(threading.current_thread().name)
            if Config._instance is None:
                Config._instance = Config()
            return Config._instance

    module = types.ModuleType("cobalt_agent.config")
    module.Config = Config
    monkeypatch.setitem(sys.modules, "cobalt_agent.config", module)
    state.Config = Config
    return state


def test_w1_a_cold_singleton_hands_a_second_thread_no_config(fake_config):
    errors: list[BaseException] = []

    def first():
        fake_config.Config.get_instance()

    def second():
        fake_config.loading.wait(1)
        try:
            fake_config.Config.get_instance()._config
        except AttributeError as e:
            errors.append(e)

    a = threading.Thread(target=first, name="A")
    b = threading.Thread(target=second, name="B")
    a.start()
    b.start()
    a.join(5)
    b.join(5)

    assert len(errors) == 1 and "_config" in str(errors[0])


def test_w1_warm_config_builds_the_singleton_once_in_the_calling_thread(fake_config):
    r.warm_config()

    assert fake_config.callers == ["MainThread"]
    assert fake_config.Config._instance._config == {"loaded": True}


def test_w1_run_command_warms_config_before_the_strike_thread(monkeypatch, fake_config):
    errors: list[tuple[str, BaseException]] = []
    seen: dict[str, object] = {}
    cycles: list[int] = []
    strike_read = threading.Event()

    def read_config():
        name = threading.current_thread().name
        try:
            seen[name] = fake_config.Config.get_instance()._config
        except AttributeError as e:
            errors.append((name, e))

    class FakeRunner:
        async def cycle(self):
            strike_read.wait(2)  # the one cycle ends after the strike thread has read
            cycles.append(1)
            return SimpleNamespace(state="scanning", scan_id=len(cycles))

    async def build():
        fake_config.loading.wait(1)
        read_config()
        return FakeRunner()

    class Loop:
        async def tick(self):
            return None

        def interval_s(self):
            return 1

    async def make():
        read_config()
        strike_read.set()
        return Loop()

    @contextmanager
    def fake_job_run(_label):
        yield SimpleNamespace(result=None)

    monkeypatch.setattr(r, "build_runner", build)
    monkeypatch.setattr(r, "load_tunables",
                        lambda: SimpleNamespace(by_key={"radar.scan_interval": SimpleNamespace(value=0)}))
    monkeypatch.setattr(r, "should_keep_running", lambda _label: len(cycles) < 1)
    monkeypatch.setattr(r, "job_run", fake_job_run)
    monkeypatch.setattr(r, "make_strike_loop", make, raising=False)

    r.run_command(None)

    assert errors == []
    assert seen == {"MainThread": {"loaded": True}, "strike": {"loaded": True}}
    assert fake_config.callers[0] == "MainThread"
