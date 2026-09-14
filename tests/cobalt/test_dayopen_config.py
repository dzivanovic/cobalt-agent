"""day-open's own tunables load through the real F16 gate (no DB
involved — `tunables.yaml` is committed config)."""

from cobalt.dayopen.config import load_dayopen_config


def test_dayopen_config_loads_ruled_numbers():
    cfg = load_dayopen_config()
    assert cfg.c4_expected_session_blocks == 8
    assert cfg.c6_max_gap_min == 20
