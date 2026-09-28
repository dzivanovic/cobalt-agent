"""X11 (v2 §7, before S1; W22): the `audit-export --replay` scorer
(`audit_export.export_replay`) with a formed member whose `last_price` is
None. At the base it substitutes `trigger` → proximity exactly 1. The
evaluator never produces that member (a formed evaluation has a fresh
closed bar), so the member is constructed by wrapping the real
`evaluate_member` — this records what the fallback emits, and after
STEP-2 the same path must never emit proximity 1."""

from __future__ import annotations

import json
from datetime import datetime, timezone

import radar_p2_support as sup
from cobalt.radar import audit_export as ax
from cobalt.session import session_clock

from stale_support import FIXED

GENERATED = datetime(2026, 9, 16, 22, 0, tzinfo=timezone.utc)


def test_x11_replay_bundle_member_without_last_price(tmp_path, monkeypatch):
    from test_radar_evaluate_cli import ReadOnlyRadar, _daily

    real = ax.evaluate_member
    calls = []

    def no_last(*args, **kwargs):
        ev = real(*args, **kwargs)
        calls.append(ev.evaluation)
        return ev.model_copy(update={"last_price": None})

    monkeypatch.setattr(ax, "evaluate_member", no_last)
    radar = ReadOnlyRadar(sup.members("FTFT"), {"FTFT": sup.fixture_bars("FTFT")})
    settings_rows = sup.fixture_settings_rows(**{"radar.cards_enabled": False})
    outcome, error = None, None
    try:
        ax.export_replay(
            sup.TRADE_DATE, pool_key="pool", slug_filter=None, radar_store=radar,
            defs_source=lambda: ([sup.loaded()], {}), daily_source=_daily, tunables=sup.engine_tunables(),
            defaults=sup.defaults(), settings_values=settings_rows, clock=session_clock(), out=tmp_path / "b",
            generated_at=GENERATED,
        )
        cards = json.loads((tmp_path / "b" / "cards.json").read_text())["cards"]
        outcome = [c["candidate"]["proximity"] for c in cards]
    except Exception as e:  # recorded, not hidden
        error = f"{type(e).__name__}: {e}"
    print(f"X11: fixed={FIXED} re_evaluations={len(calls)} evaluations={sorted(set(calls))} candidate_proximities={outcome} "
          f"error={error!r}")
    assert calls and set(calls) == {"formed"}
    if FIXED:  # [F-13]/[F-14]: no fallback — a fresh member without a last price raises (L1)
        assert outcome is None and error.startswith("EvaluateError")
    else:  # the base emits exactly the trigger fallback's value
        assert outcome is not None and set(outcome) == {"1"}
