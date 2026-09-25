"""DRC D4 — the DRC settings family, one reader of the daily stop and the
grade dollars, the daily note reads the key, the change line in ASET
(R95 / R96 / R101 / R102; v2 §5 T9 [F-18], [F-16]; §9 D4).

OFFLINE: every store here is a constructed in-memory double, every value
a constructed value (L32 / L45 / L69). The with-DB proofs are
tests/cobalt/test_drc_settings_db.py.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path

import pytest

SRC = Path(__file__).resolve().parents[2] / "src" / "cobalt"

#: SPEC §7 key NAMES (names only).
ACCOUNT_KEYS = ("account.daily_stop_full", "account.daily_stop_half")
DRC_KEYS = (
    *ACCOUNT_KEYS,
    "limits.card_match_window_minutes",
    "windows.premarket_end",
    "windows.first_window_minutes",
    "windows.prime",
    "windows.dead",
    "windows.second",
    "goal.primary",
    "goal.metric",
    "goal.target_pct",
    "goal.switch_threshold_pct",
)


# ---------------------------------------------------------------------
# constructed doubles
# ---------------------------------------------------------------------


def _sheet_modes(b_full="60", b_half="30"):
    from cobalt.aset.config import SheetModeGrades, SheetModesConfig
    from cobalt.aset.models import Grade

    return SheetModesConfig(
        sheets={
            "half": SheetModeGrades(A_plus=8, A=7, B=Decimal(b_half), C=2, D=0),
            "full": SheetModeGrades(A_plus=16, A=14, B=Decimal(b_full), C=4, D=0),
        },
        order=["half", "full"],
        enabled_grades=[Grade.A, Grade.B],
    )


def _sheet_row(sm):
    row = sm.model_dump(mode="json")
    row.pop("enabled_grades")
    return row


class FakeStore:
    """The settings store's surface: values / rows / put. `lose` names a
    key whose write silently does not land (a read-back mismatch)."""

    def __init__(self, rows=None, lose=None):
        self.data = dict(rows or {})
        self.puts = []
        self.lose = lose

    def values(self):
        return dict(self.data)

    def rows(self):
        return [
            {"key": k, "value": v, "source": "test", "updated_at": datetime(2026, 9, 3, 14, 0)}
            for k, v in sorted(self.data.items())
        ]

    def ensure_schema(self):
        return None

    def put(self, rows, *, source, delete=(), before_commit=None):
        self.puts.append((dict(rows), source, list(delete)))
        for k, v in rows.items():
            if k != self.lose:
                self.data[k] = v
        for k in delete:
            self.data.pop(k, None)
        return {k: "updated" for k in rows}


@pytest.fixture
def world(monkeypatch):
    """One constructed store behind every settings reader and writer, and
    the grade dollars read from it through `load_sheet_modes_config`."""
    from cobalt.settings import cli as settings_cli
    from cobalt.settings import drc as settings_drc

    sm = _sheet_modes()
    store = FakeStore({"aset.sheet_modes": _sheet_row(sm), "aset.enabled_grades": ["A", "B"]})

    def _load_sheet_modes():
        from cobalt.aset.config import SheetModesConfig

        return SheetModesConfig(
            **store.values()["aset.sheet_modes"],
            enabled_grades=store.values()["aset.enabled_grades"],
        )

    monkeypatch.setattr(settings_drc, "TraderSettingsStore", lambda: store)
    monkeypatch.setattr(settings_cli, "TraderSettingsStore", lambda: store)
    monkeypatch.setattr(settings_drc, "load_sheet_modes_config", _load_sheet_modes)
    return store


# ---------------------------------------------------------------------
# D4-1 keys + schema
# ---------------------------------------------------------------------


def test_every_drc_key_is_optional_and_none_is_required():
    from cobalt.settings.models import DRC_SETTING_KEYS, OPTIONAL_SETTING_KEYS, SETTING_KEYS

    assert set(DRC_SETTING_KEYS) == set(DRC_KEYS)
    for key in DRC_KEYS:
        assert key in OPTIONAL_SETTING_KEYS, key
        assert key not in SETTING_KEYS, key
    assert not any(k.startswith(("grades.", "sleep_trigger.")) for k in OPTIONAL_SETTING_KEYS)
    assert "account.sheet_mode_default" not in OPTIONAL_SETTING_KEYS


@pytest.mark.parametrize(
    "key,value,typed",
    [
        ("account.daily_stop_full", "250", Decimal("250")),
        ("account.daily_stop_half", 125, Decimal("125")),
        ("limits.card_match_window_minutes", 15, 15),
        ("windows.premarket_end", "09:30", "09:30"),
        ("windows.first_window_minutes", 15, 15),
        ("windows.prime", ["09:30", "11:00"], ("09:30", "11:00")),
        ("windows.dead", ["11:00", "14:00"], ("11:00", "14:00")),
        ("windows.second", ["14:00", "15:45"], ("14:00", "15:45")),
        ("goal.primary", "constructed goal", "constructed goal"),
        ("goal.metric", "constructed metric", "constructed metric"),
        ("goal.target_pct", [60, 65], (Decimal("60"), Decimal("65"))),
        ("goal.switch_threshold_pct", 60, Decimal("60")),
    ],
)
def test_each_drc_key_validates_a_good_constructed_value(key, value, typed):
    """D4 fix r1 F-5 (drc-d4-check-2026-09-25.md:129): the good value is
    TYPED as the family model declares it (`DrcKey.validate`,
    models.py:199), not merely accepted, and the stored row round-trips."""
    from cobalt.settings.models import OPTIONAL_SETTING_MODELS

    adapter = OPTIONAL_SETTING_MODELS[key]
    got = adapter.validate(value)
    assert got == typed and type(got) is type(typed), (key, got)
    if isinstance(typed, tuple):
        assert [type(v) for v in got] == [type(v) for v in typed], (key, got)
    row = adapter.from_rows({key: value}).row()
    assert adapter.from_rows({key: row}).row() == row
    assert adapter.validate(row) == typed


@pytest.mark.parametrize(
    "key,value",
    [
        ("account.daily_stop_full", "abc"),
        ("account.daily_stop_full", "-5"),
        ("account.daily_stop_half", 0),
        ("account.daily_stop_full", [1, 2]),
        ("account.daily_stop_full", None),
        ("limits.card_match_window_minutes", -1),
        ("limits.card_match_window_minutes", "soon"),
        ("windows.premarket_end", "9.30"),
        ("windows.prime", ["11:00", "09:30"]),
        ("windows.first_window_minutes", 0),
        ("goal.primary", ""),
        ("goal.target_pct", [70, 60]),
        ("goal.switch_threshold_pct", 140),
    ],
)
def test_each_drc_key_fails_naming_the_key_on_a_bad_value(key, value):
    from cobalt.settings.models import OPTIONAL_SETTING_MODELS, TraderSettingsError

    with pytest.raises(TraderSettingsError, match=re.escape(key)):
        OPTIONAL_SETTING_MODELS[key].from_rows({key: value})


def test_load_drc_settings_reads_present_keys_and_none_for_absent(world):
    from cobalt.settings.drc import load_drc_settings

    world.data["account.daily_stop_full"] = "250"
    world.data["limits.card_match_window_minutes"] = 15
    drc = load_drc_settings(None)
    assert drc.account.daily_stop_full == Decimal("250")
    assert drc.account.daily_stop_half is None
    assert drc.limits.card_match_window_minutes == 15
    assert drc.windows.prime is None
    assert drc.goal.target_pct is None


def test_load_drc_settings_takes_an_explicit_source():
    from cobalt.settings.drc import load_drc_settings

    drc = load_drc_settings(FakeStore({"windows.first_window_minutes": 20}))
    assert drc.windows.first_window_minutes == 20


def test_a_stored_value_known_false_is_loud_naming_the_key(world):
    from cobalt.settings.drc import load_drc_settings
    from cobalt.settings.models import TraderSettingsError

    world.data["account.daily_stop_half"] = "-3"
    with pytest.raises(TraderSettingsError, match="account.daily_stop_half"):
        load_drc_settings(None)


# ---------------------------------------------------------------------
# D4-2 the one reader
# ---------------------------------------------------------------------


def test_daily_risk_values_reads_the_stop_and_the_grade_dollars(world):
    from cobalt.settings.drc import daily_risk_values

    world.data["account.daily_stop_full"] = "250"
    risk = daily_risk_values(None)
    assert risk.daily_stop == {"full": Decimal("250"), "half": None}
    assert risk.grade_dollars["full"]["B"] == Decimal("60")
    assert risk.grade_dollars["half"]["B"] == Decimal("30")
    assert list(risk.grade_dollars) == ["half", "full"]


def test_daily_risk_values_absent_stop_is_none_never_zero(world):
    from cobalt.settings.drc import daily_risk_values

    risk = daily_risk_values(None)
    assert risk.daily_stop == {"full": None, "half": None}
    assert all(v is None for v in risk.daily_stop.values())


def _py_files(root: Path):
    return sorted(p for p in root.rglob("*.py") if "__pycache__" not in p.parts)


#: Every way a module can name the daily stop's keys (D4 fix r1 F-4).
_STOP_KEY_TOKENS = ("daily_stop_full", "daily_stop_half", "DAILY_STOP_KEYS", "account.daily_stop")
#: The ONE reader's entry points, and the two modules allowed to call them.
_READER_CALLS = ("daily_risk_values(", "load_drc_settings(")
_READER_CALLERS = ("prefill/daily.py", "aset/web.py")


def _second_readers(root: Path) -> list[str]:
    """Every hit, under `root`, of a second way to read the daily stop or
    the grade dollars: (a) a key token outside `settings/`; (b) a reader
    call outside `settings/` and the two named callers (the daily note and
    the change line's form, web.py:1200); (c) `sheet_modes` in a `drc/`
    module."""
    offenders = []
    for path in _py_files(root):
        rel = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        in_settings = rel.startswith("settings/")
        for token in _STOP_KEY_TOKENS:
            if token in text and not in_settings:
                offenders.append(f"{rel}: {token}")
        for call in _READER_CALLS:
            if call in text and not (in_settings or rel in _READER_CALLERS):
                offenders.append(f"{rel}: {call}")
        if rel.startswith("drc/") and "sheet_modes" in text:
            offenders.append(f"{rel}: sheet_modes")
    return offenders


def test_one_reader_of_the_daily_stop_and_the_grade_dollars():
    """L3: the daily-stop key names appear only in `settings/`; the ONE
    reader is called only by `prefill/daily.py` and the change line's form
    in `aset/web.py`; no DRC module reads `sheet_modes`; `prefill/daily.py`
    calls the sheet loader exactly once (D4 fix r1 F-4,
    drc-d4-check-2026-09-25.md:126)."""
    offenders = _second_readers(SRC)
    assert offenders == [], f"a second reader: {offenders}"
    daily = (SRC / "prefill" / "daily.py").read_text(encoding="utf-8")
    assert daily.count("load_sheet_modes_config()") == 1
    assert daily.count("daily_risk_values(") == 1


def test_the_one_reader_walk_flags_a_second_reader(tmp_path):
    """D4 fix r1 F-4's NEGATIVE CONTROL (drc-d4-check-2026-09-25.md:126):
    the walk names a key token and a reader call in a constructed `drc/`
    module, and a dotted key in a constructed `aset/` module."""
    (tmp_path / "drc").mkdir()
    (tmp_path / "aset").mkdir()
    (tmp_path / "drc" / "x.py").write_text(
        "from x import DAILY_STOP_KEYS\nrisk = daily_risk_values()\n", encoding="utf-8"
    )
    (tmp_path / "aset" / "y.py").write_text('KEY = "account.daily_stop"\n', encoding="utf-8")
    assert sorted(_second_readers(tmp_path)) == [
        "aset/y.py: account.daily_stop",
        "drc/x.py: DAILY_STOP_KEYS",
        "drc/x.py: daily_risk_values(",
    ]


# ---------------------------------------------------------------------
# D4-3 the daily note reads the key
# ---------------------------------------------------------------------


def _risk(full=None, half=None):
    from cobalt.settings.drc import DailyRisk

    return DailyRisk(daily_stop={"full": full, "half": half}, sheet_modes=_sheet_modes())


def _render_with(daily_stop_text: str) -> str:
    from test_prefill_daily import make_rules_cfg

    from cobalt.prefill import daily as daily_module

    ctx = daily_module.build_slot_contents(
        datetime(2026, 9, 3, 5, 15), [], None, [], [], None,
        make_rules_cfg(), _sheet_modes(), "", "- constructed",
    )
    ctx["daily_stop"] = daily_stop_text
    return daily_module._render_template(ctx)


def _stop_line(note: str) -> str:
    lines = [ln for ln in note.split("\n") if ln.startswith("Daily HARD Stop")]
    assert len(lines) == 1, lines
    return lines[0]


def test_the_daily_template_renders_the_value_passed_in():
    from cobalt.prefill.daily import format_daily_stop

    line = _stop_line(_render_with(format_daily_stop(_risk(full=Decimal("250")))))
    assert "$250" in line
    assert "not given" in line  # the half stop is absent


def test_the_daily_template_renders_not_given_and_no_digit_when_absent():
    from cobalt.prefill.daily import format_daily_stop

    line = _stop_line(_render_with(format_daily_stop(_risk())))
    assert "not given" in line
    assert not re.search(r"\d", line), line


def test_a_failed_read_renders_failed_never_blank():
    from cobalt.prefill.daily import format_daily_stop

    assert format_daily_stop(None, "boom").startswith("FAILED")


def test_the_template_carries_no_stop_number():
    text = (Path(__file__).resolve().parents[2] / "configs/cobalt/templates/daily.md.j2").read_text()
    line = _stop_line(text)
    assert "{{ daily_stop }}" in line
    assert not re.search(r"\d", line), "the committed template carries no stop number (R95)"


# ---------------------------------------------------------------------
# D4-4 the change line
# ---------------------------------------------------------------------


def _form(**over):
    """Every field of the change line as the page posts it, at the
    constructed current values, with `over` applied."""
    sm = _sheet_modes()
    names = {"A_plus", "A", "B", "C", "D"}
    form = {"account.daily_stop_full": "", "account.daily_stop_half": ""}
    for sheet in sm.order:
        for g in names:
            form[f"aset.sheet_modes.{sheet}.{g}"] = str(getattr(sm.sheets[sheet], g))
    form.update(over)
    return form


@pytest.fixture
def page(world, monkeypatch):
    from fastapi.testclient import TestClient
    from test_aset_web import _offline_daymode_config, _offline_sheet_modes_config

    from cobalt.aset import web as web_module

    cfg = _offline_daymode_config()
    monkeypatch.setattr(web_module, "load_sheet_modes_config", _offline_sheet_modes_config)
    monkeypatch.setattr(
        web_module,
        "_daymode_state",
        lambda: {
            "cfg": cfg, "day": None,
            "row": {"attested_sheet": cfg.hotkey_file_for_mode(cfg.lowest_enabled)},
            "mode": cfg.lowest_enabled, "stage": "stage 1 (system rule)", "error": None,
        },
    )
    return TestClient(web_module.app)


def _sha(payload):
    from cobalt.settings.cli import payload_sha256

    return payload_sha256(payload)


def test_the_page_shows_the_change_line_with_the_attestation_form(page, world):
    world.data["account.daily_stop_full"] = "250"
    r = page.get("/")
    assert r.status_code == 200
    assert 'action="/settings/daily"' in r.text
    assert r.text.index('action="/attest"') < r.text.index('action="/settings/daily"')
    assert 'value="250"' in r.text


def test_review_shows_the_per_key_diff_and_the_payload_sha(page, world):
    r = page.post("/settings/daily", data=_form(**{"account.daily_stop_full": "31337",
                                                   "aset.sheet_modes.full.B": "61"}))
    assert r.status_code == 200
    assert "account.daily_stop_full" in r.text and "not given" in r.text and "31337" in r.text
    assert "aset.sheet_modes.full.B" in r.text and "61" in r.text
    from cobalt.settings.drc import propose_daily_change

    proposal = propose_daily_change(_form(**{"account.daily_stop_full": "31337",
                                             "aset.sheet_modes.full.B": "61"}))
    assert proposal.sha256 in r.text
    assert set(proposal.payload) == {"account.daily_stop_full", "aset.sheet_modes"}
    assert 'action="/settings/daily/apply"' in r.text
    assert world.puts == [], "a review writes nothing"


def test_apply_with_a_wrong_sha_is_refused_and_writes_nothing(page, world):
    form = _form(**{"account.daily_stop_full": "31337"})
    r = page.post("/settings/daily/apply", data=dict(form, sha256="0" * 64))
    assert "FAILED" in r.text and "sha256" in r.text
    assert world.puts == []


def test_apply_inside_market_reset_is_refused_with_the_reason(page, world, monkeypatch):
    from cobalt.session import clock as clock_mod

    form = _form(**{"account.daily_stop_full": "31337"})
    sha = _sha({"account.daily_stop_full": "31337"})
    monkeypatch.setattr(clock_mod, "now_utc", lambda: datetime(2026, 9, 4, 0, 30, tzinfo=timezone.utc))
    r = page.post("/settings/daily/apply", data=dict(form, sha256=sha))
    assert "FAILED" in r.text and "MARKET RESET" in r.text
    assert world.puts == []


@pytest.mark.parametrize(
    "field,value,match",
    [
        ("account.daily_stop_full", "abc", "not a number"),
        ("account.daily_stop_half", "-5", "account.daily_stop_half"),
        ("aset.sheet_modes.full.B", "", "a grade with no dollar"),
        ("aset.sheet_modes.half.A", "x", "not a number"),
        ("aset.sheet_modes.half.D", "5", "aset.sheet_modes.half.D"),
    ],
)
def test_a_bad_field_is_refused_naming_it_and_nothing_is_written(page, world, field, value, match):
    form = _form(**{field: value})
    for route in ("/settings/daily", "/settings/daily/apply"):
        r = page.post(route, data=dict(form, sha256="0" * 64))
        assert "FAILED" in r.text, route
        assert field in r.text and match in r.text, (route, r.text[-1500:])
    assert world.puts == []


def test_a_good_apply_writes_through_the_one_apply_function_then_reads_back(
    page, world, monkeypatch, tmp_path
):
    from cobalt.settings import cli as settings_cli

    calls = []
    real = settings_cli.apply_settings

    def spy(*args, **kwargs):
        calls.append(("call", args, kwargs))
        return real(*args, **kwargs)

    monkeypatch.setattr(settings_cli, "apply_settings", spy)
    form = _form(**{"account.daily_stop_full": "31337", "aset.sheet_modes.full.B": "61"})
    from cobalt.settings.drc import propose_daily_change

    proposal = propose_daily_change(form)
    r = page.post("/settings/daily/apply", data=dict(form, sha256=proposal.sha256))
    assert "Settings saved" in r.text, r.text[-1500:]
    assert len(calls) == 1
    assert len(world.puts) == 1 and set(world.puts[0][0]) == {"account.daily_stop_full", "aset.sheet_modes"}
    assert world.data["account.daily_stop_full"] == "31337"
    assert proposal.sha256 in world.puts[0][1]

    # the CLI's optional apply goes through the SAME function object
    path = tmp_path / "optional.yaml"
    body = b"optional_settings:\n  account.daily_stop_half: 4242\n"
    path.write_bytes(body)
    settings_cli.cmd_load(argparse.Namespace(
        optional=str(path), sha256=hashlib.sha256(body).hexdigest(), dry_run=False,
        apply=True, from_dir=None, from_git=None,
    ))
    assert len(calls) == 2
    assert world.data["account.daily_stop_half"] == "4242"


def test_saved_only_after_the_read_back_equals_the_payload(page, world):
    world.lose = "account.daily_stop_full"
    form = _form(**{"account.daily_stop_full": "31337"})
    r = page.post("/settings/daily/apply", data=dict(form, sha256=_sha({"account.daily_stop_full": "31337"})))
    assert "FAILED" in r.text
    assert "Settings saved" not in r.text
    assert "differs from what was applied" in r.text
    assert "account.daily_stop_full" in r.text


_ISO_TIME = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?")
_HEX64 = re.compile(r"[0-9a-f]{64}")


def _leaks(message: str, figures: tuple[str, ...]) -> list[str]:
    """What of his a log message still carries once its timestamps are
    masked: each constructed figure it contains, and `digest` when a
    64-hex run remains (a digest of a small-value payload IS the value,
    D4 fix r1 F-8)."""
    masked = _ISO_TIME.sub("<time>", message)
    found = [f for f in figures if f in masked]
    if _HEX64.search(masked):
        found.append("digest")
    return found


def test_no_log_line_carries_a_value(page, world):
    """D4 fix r1 F-8 (drc-d4-check-2026-09-25.md:131, :178; L32): the one
    log line names the keys, never a value and never a digest of one."""
    from loguru import logger

    stop, grade = "31337", "7061"
    assert _leaks(f"x · {grade} · at 2026-09-03T14:00:00+00:00", (stop, grade)) == [grade]
    assert _leaks("source aset.change_line@sha256:" + "ab" * 32, (stop, grade)) == ["digest"]
    messages = []
    sink = logger.add(lambda m: messages.append(str(m)), format="{message}")
    try:
        form = _form(**{"account.daily_stop_full": stop, "aset.sheet_modes.full.B": grade})
        from cobalt.settings.drc import propose_daily_change

        sha = propose_daily_change(form).sha256
        r = page.post("/settings/daily/apply", data=dict(form, sha256=sha))
        assert "Settings saved" in r.text
    finally:
        logger.remove(sink)
    applied = [m for m in messages if "settings applied" in m]
    assert len(applied) == 1, messages
    assert "account.daily_stop_full" in applied[0] and "aset.sheet_modes" in applied[0]
    assert sha not in applied[0]
    for m in messages:
        assert _leaks(m, (stop, grade)) == [], m


# ---------------------------------------------------------------------
# D4-5 dry-run = `cobalt settings show`
# ---------------------------------------------------------------------


def test_settings_show_prints_each_drc_key_not_given_when_absent(world, capsys):
    from test_aset_web import _offline_daymode_config

    from cobalt.settings import cli as settings_cli
    from cobalt.settings.models import TraderSettings

    world.data.update(TraderSettings(sheet_modes=_sheet_modes(), daymode=_offline_daymode_config()).rows())
    world.data["limits.card_match_window_minutes"] = 15
    settings_cli.cmd_show(argparse.Namespace())
    out = capsys.readouterr().out
    for key in DRC_KEYS:
        line = [ln for ln in out.split("\n") if ln.strip().startswith(key + " ") or ln.strip() == key]
        assert line, f"{key} not printed:\n{out}"
        if key != "limits.card_match_window_minutes":
            assert "not given" in line[-1], line
    assert "not given" not in [ln for ln in out.split("\n") if "card_match_window_minutes" in ln][-1]
