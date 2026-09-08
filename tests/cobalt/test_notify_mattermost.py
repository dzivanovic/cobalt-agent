"""The Mattermost channel's one number (ADR-0008 D7 / F16).

`MattermostConfig.timeout_s` was a field in `configs/cobalt/notify.yaml`
— the last threshold in the new core still living in a config file rather
than a `tunables.yaml` row. The email channel had already moved its two
(`notify.email.auth_port`, `notify.email.timeout_s`); one channel reading
its numbers from a row while the other read its own from a YAML field was
two answers to "where does a number live", and this is the second one
being retired.
"""

from __future__ import annotations

import pytest

from cobalt.notify import mattermost
from cobalt.notify.config import MattermostConfig, load_notify_config
from cobalt.taxonomy.loader import load_tunables
from cobalt.taxonomy.tunables import TunableRegistry


def test_the_field_is_gone_from_the_model():
    assert "timeout_s" not in MattermostConfig.model_fields


def test_the_field_is_gone_from_notify_yaml():
    cfg = load_notify_config()
    assert not hasattr(cfg.mattermost, "timeout_s")


def test_it_is_a_tunables_row_with_its_consumer_named():
    row = load_tunables().by_key[mattermost.TIMEOUT_KEY]
    assert row.value == 10
    assert row.unit.value == "duration"
    assert row.scope == "global"
    assert row.consumers and "mattermost" in row.consumers[0]


def test_the_helper_reads_it():
    assert mattermost.timeout_s() == 10.0


def test_a_missing_row_fails_loud_rather_than_defaulting(monkeypatch):
    """F16: the channel has no built-in default. A timeout Cobalt invented
    is a hang nobody chose the length of."""
    empty = TunableRegistry(
        tunables=[
            {
                "key": "unrelated.row", "value": 1, "unit": "count",
                "scope": "global", "dynamic": False, "status": "proposed",
                "source": "ruling",
            }
        ]
    )
    monkeypatch.setattr(
        "cobalt.taxonomy.loader.load_tunables", lambda *a, **k: empty
    )
    with pytest.raises(mattermost.MattermostError, match=mattermost.TIMEOUT_KEY):
        mattermost.timeout_s()


def test_every_rest_call_is_bounded_by_it():
    """Four call sites, one number — and none of them a literal."""
    source = __import__("pathlib").Path(mattermost.__file__).read_text()
    assert source.count("timeout_s()") >= 4
    assert "cfg.timeout_s" not in source
