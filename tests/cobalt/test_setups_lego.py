"""The setups one build — the corpus gates and (from STEP-9) the LEGO TEST.

FINAL §9 gate 2 ("registry evaluable ⇒ forms", a property test) and gate 4
point (4) (the corpus shape of every unlocked setup is `evaluable`), over the
neutral shape notes of `setups_shapes.py`.

NAMED DEVIATION FROM GATE 2's TEXT (carried under the report's ESCALATE):
the committed real-shape days are ONE trade date, two tickers
(`tests/fixtures/radar/_cut_p2_fixtures.py`). An evaluable shape that forms
on no scan of any committed day is PINNED in `AWAITING_A_DAY` — with its
path proven on definition-written constructed series in its own
`test_<slug>_path_*` tests — never given an invented or re-dated day. The
property fails when an evaluable shape with no day is not pinned, and when
the pinned set grows or shrinks unannounced.
"""

from __future__ import annotations

import pytest

import setups_shapes as shapes
from cobalt.radar.anatomy.registry import evaluability

#: Evaluable setup shapes that form on NO scan of the committed real-shape
#: day, by setup slug. Closed only by a DB-backed fixture-cut job + a blind
#: expected-values seat (FINAL [F-16] (1), [F-21]).
#: - rubberband: its full shape carries the day-1 HTF avoid, which is True on
#:   the committed day (proof ESCALATE 2) — `avoided` on every scan the
#:   relation path forms on.
#: - hitchhiker (STEP-4): evaluable; on FTFT its opening drive reads
#:   `consolidation` on 22 scans and a micro-Range instantiates on 68, but on
#:   no scan do the band and the upper-third preconditions hold with them (a
#:   False precondition, never an unknown); BGFI is stale by design. Its path
#:   forms on the definition-written day and its mirror
#:   (`test_setups_hitchhiker.py::test_hitchhiker_path_*`).
AWAITING_A_DAY: frozenset[str] = frozenset({"rubberband", "hitchhiker"})

#: Evaluable shapes whose acceptance is STOPPED on an open ruling — never in
#: `AWAITING_A_DAY` (prompt STEP-5):
#: - backside, fashionably-late: X10 FAILED (on a day that recovers past the
#:   open the backside shape never forms: the Extension's direction is
#:   recomputed from last − open). The FINAL offers Grok's fix and Fable's fix
#:   and chooses neither → ASK DESK. fashionably-late also reads the two
#:   `per_indicator` holes (F1): at production defaults it cannot form.
AWAITING_A_RULING: frozenset[str] = frozenset({"backside", "fashionably-late"})


@pytest.fixture(scope="module")
def corpus(tmp_path_factory):
    loaded = {}
    for key, shape in {**shapes.SHAPES, **shapes.VARIANTS}.items():
        loaded[key] = (shape, shapes.load_shape(tmp_path_factory.mktemp(key.replace(":", "-")), shape))
    return loaded


def _forms_on_a_committed_day(shape, ld) -> bool:
    return any(ev.evaluation == "formed" for ticker in shape.tickers for _, ev in shapes.every_scan(ld, ticker))


def test_every_unlocked_setup_shape_is_evaluable(corpus):
    """FINAL §9 point (4) / [F-16] (4): the corpus shape of every setup the
    build claims to unlock is `evaluable`, or the missing atom is named."""
    report = {key: evaluability(ld.definition) for key, (_s, ld) in corpus.items()}
    not_evaluable = {key: e.missing_atoms for key, e in report.items() if not e.evaluable}
    assert not_evaluable == {}, not_evaluable


def test_registry_evaluable_implies_forms_or_awaits_a_day(corpus):
    """FINAL §9 gate 2, with the named deviation of this module's docstring."""
    awaiting = set()
    for key, (shape, ld) in corpus.items():
        if not evaluability(ld.definition).evaluable or key in AWAITING_A_RULING:
            continue
        if not _forms_on_a_committed_day(shape, ld):
            awaiting.add(key)
    assert awaiting == set(AWAITING_A_DAY)


# =====================================================================
# THE LEGO TEST (R44, STEP-9) — tests and one DevDoc ONLY
# =====================================================================

import ast  # noqa: E402
import re  # noqa: E402
from datetime import timedelta  # noqa: E402
from decimal import Decimal  # noqa: E402
from pathlib import Path  # noqa: E402

import radar_p2_support as sup  # noqa: E402
from cobalt.session import session_clock  # noqa: E402
from cobalt.taxonomy.slug import trade_key  # noqa: E402

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "src" / "cobalt"
SETUP_SLUGS = ("rubberband", "hitchhiker", "backside", "second-chance", "fashionably-late", "nine-ema-scalp",
               "vwap-continuation")
NAME_PATTERN = re.compile(r"rubberband|hitchhiker|backside|second.chance|fashionably|nine.ema|vwap.continuation",
                          re.IGNORECASE)
#: (i) THE BASELINE — every src line that may carry a setup word, each with its
#: reason. Anything else is a setup's identity leaking into the code.
BASELINE = {
    # the slug-function docstring examples (PREFLIGHT, drafter's)
    ("taxonomy/slug.py", "matched, joined and put in URLs. So `9 EMA Scalp` is `nine-ema-scalp`: no"),
    ("taxonomy/slug.py", 'trade_key("nine-ema-scalp") == "nine_ema_scalp"'),
    # the anatomy word `backside` of `EntryMode` (PREFLIGHT, drafter's)
    ("taxonomy/trade_def.py", 'BACKSIDE = "backside"'),
    # a schema comment naming a corpus example (PREFLIGHT, beyond the drafter's three)
    ("taxonomy/trade_def.py", "# Second Chance step 2 (retest) carries no confirmation_policy in"),
    # the anatomy word `backside`: the D4 Extension state and its `extension.backside_*` engine keys
    ("radar/anatomy/extension.py", "# `reverting` from the snapback rule `A-08`, `backside` from ≥"),
    ("radar/anatomy/extension.py", "# `cfg(extension.backside_hh_min)` HH and ≥ `cfg(extension.backside_hl_min)` HL"),
    ("radar/anatomy/extension.py", "# * BACKSIDE, once reverting: ≥ hh_min higher highs (bars after the turn making"),
    ("radar/anatomy/extension.py", "#   A down run's backside is an up recovery; the mirrored frame gives the other."),
    ("radar/anatomy/extension.py",
     'LIFECYCLE_KEYS = ("extension.snapback_bars_cleared", "extension.backside_hh_min", "extension.backside_hl_min")'),
    ("radar/anatomy/extension.py", "backside_hh_min: int = Field(ge=0)"),
    ("radar/anatomy/extension.py", "backside_hl_min: int = Field(ge=0)"),
    ("radar/anatomy/extension.py", 'backside_hh_min=int(rows["extension.backside_hh_min"].value),'),
    ("radar/anatomy/extension.py", 'backside_hl_min=int(rows["extension.backside_hl_min"].value),'),
    ("radar/anatomy/extension.py", 'state: Literal["culminating", "reverting", "backside", "none"] | None'),
    ("radar/anatomy/extension.py", "if hh < params.backside_hh_min or hl < params.backside_hl_min:"),
    ("radar/anatomy/extension.py", 'return LifecycleObservation(state="backside" if rising and above else "reverting", **base)'),
    ("radar/formation/atoms.py", "# `backside`); `building` / `extending` / `resuming` have no rule → E8."),
    ("radar/formation/atoms.py",
     'AtomResolver("Extension.state", "symbol", domain=frozenset({"culminating", "reverting", "backside", "none"}),'),
}
#: The files where the anatomy word `backside` may appear as a string literal.
ANATOMY_BACKSIDE_FILES = {"taxonomy/trade_def.py", "radar/anatomy/extension.py", "radar/formation/atoms.py"}


def _src_files():
    return sorted(p for p in SRC.rglob("*.py") if "__pycache__" not in p.parts)


def test_lego_i_no_setup_name_in_source():
    hits = set()
    for path in _src_files():
        for line in path.read_text().splitlines():
            if NAME_PATTERN.search(line):
                hits.add((path.relative_to(SRC).as_posix(), line.strip()))
    print(f"LEGO (i): {len(hits)} source lines carry a setup word; baseline {len(BASELINE)}")
    assert hits == BASELINE, sorted(hits ^ BASELINE)


def test_lego_i_no_string_literal_is_a_setup_or_a_per_trade_key():
    names = {s for slug in SETUP_SLUGS for s in (slug, trade_key(slug))}
    prefixes = tuple(f"{trade_key(slug)}." for slug in SETUP_SLUGS)
    leaks = []
    for path in _src_files():
        rel = path.relative_to(SRC).as_posix()
        for node in ast.walk(ast.parse(path.read_text())):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                value = node.value
                if value == "backside" and rel in ANATOMY_BACKSIDE_FILES:
                    continue  # the anatomy word (EntryMode, the D4 Extension state)
                if value in names or value.startswith(prefixes):
                    leaks.append((rel, node.lineno, value))
    assert leaks == []


def test_lego_ii_rubberband_forms_through_the_registries_and_nothing_else():
    """STEP-2's byte-identity pins run GREEN in `test_setups_registries.py`;
    here: the shape's formation dispatches through `TRIGGERS["bar_break"]` and
    `STOPS["structural_extreme"]` / `STRUCTURAL_REFS["snapback_candle"]`, and no
    branch of the stage names that trigger or stop."""
    ld = shapes.load_shape_fresh("rubberband-without-htf-avoid")
    formed = next(ev for _, ev in shapes.every_scan(ld, "FTFT") if ev.evaluation == "formed")
    f = formed.formation
    assert (f.trigger_outcome.kind, f.stop_outcome.placement, f.stop_ref) == (
        "bar_break", "structural_extreme", "snapback_candle")
    stage = (SRC / "radar" / "evaluate.py").read_text()
    constants = {n.value for n in ast.walk(ast.parse(stage)) if isinstance(n, ast.Constant) and isinstance(n.value, str)}
    assert not constants & {"bar_break", "structural_extreme", "snapback_candle", "turn_low"}


# ---------------------------------------------------------------------
# (iii) THE EIGHTH DEFINITION, FROM DATA ONLY
# ---------------------------------------------------------------------


def eighth_mapping() -> dict:
    """Existing bricks in a combination no def of the corpus uses: the pool
    admission, price above the EMA21, an instantiated micro-Range; a 3-bar
    `bar_break`; the `range_base` stop. Anatomy words only; this file's literals."""
    mapping = shapes.example_mapping()
    mapping.update(
        valid_setups=[{"setup_ref": "range_break", "relation": "with_trend"}],
        preconditions=[{"expr": "InPlay.state == active"}, {"expr": "price > EMA21"},
                       {"expr": "Range(micro).instantiated"}],
        avoid=[{"text": "human-only read"}],
        trigger={"type": "bar_break", "params": {"bars_cleared": 3, "direction": "any"},
                 "confirmation_policy": {"type": "intrabar"}},
        quality_factors=sup.ANATOMY_FACTORS, preferred_windows=["morning"],
        preferred_windows_ref="anatomy: any micro-Range above the EMA21",
    )
    mapping.pop("radar_watch", None)
    mapping["stop"]["placement"]["ref"] = "range_base"
    return mapping


@pytest.fixture(scope="module")
def eighth(tmp_path_factory):
    return shapes.load_note(tmp_path_factory.mktemp("eighth"), "example-lego-eighth", eighth_mapping(),
                            engine=shapes.D2_CONSTRUCTED)


def test_lego_iii_the_eighth_definition_is_new_evaluable_and_forms_only_when_it_says(eighth):
    from cobalt.radar.anatomy.structure import structural_stop
    from cobalt.radar.evaluate import evaluate_member
    import test_setups_hitchhiker as hh

    corpus = [shape.mapping() for shape in shapes.SHAPES.values()]
    mine = eighth.definition
    assert all((m["trigger"], m["stop"]["placement"], m.get("preconditions"))
               != (eighth_mapping()["trigger"], eighth_mapping()["stop"]["placement"], eighth_mapping()["preconditions"])
               for m in corpus)
    assert evaluability(mine).evaluable, evaluability(mine).missing_atoms
    rows = shapes.tunables_for(eighth)
    bars = hh.drive_then_range()
    ev = evaluate_member(eighth, hh._syn_member(bars, hh.SYN_SCAN), tunables=rows, defaults=sup.defaults(),
                         scan_interval=100, clock=session_clock())
    assert ev.evaluation == "formed" and ev.direction == "long", (ev.evaluation, ev.missing, ev.note)
    f = ev.formation
    assert f.trigger.price == Decimal("11.00") and f.trigger.bars_cleared == 3  # the last three buckets' high
    assert f.stop.price == structural_stop(Decimal("10.85"), "long", Decimal("0.02")).price  # the range base
    early = [b for b in bars if b.ts < hh._et(9, 40)]  # the same day before the range exists
    ev = evaluate_member(eighth, hh._syn_member(early, hh._et(9, 40)), tunables=rows, defaults=sup.defaults(),
                         scan_interval=100, clock=session_clock())
    assert ev.evaluation != "formed"


# ---------------------------------------------------------------------
# (iv) EVALUABILITY FOR ALL EIGHT
# ---------------------------------------------------------------------


def test_lego_iv_evaluability_for_all_eight(corpus, eighth):
    """The seven setups of the FINAL's scope (rubberband included) and the eighth."""
    lines = {key: evaluability(ld.definition) for key, (_s, ld) in corpus.items() if key in shapes.SHAPES}
    lines["example-lego-eighth"] = evaluability(eighth.definition)
    for key, e in lines.items():
        print(f"EVALUABILITY {key}: " + ("evaluable" if e.evaluable else f"not_evaluable {e.missing_atoms}"))
    assert len(lines) == 8 and all(e.evaluable for e in lines.values())


# ---------------------------------------------------------------------
# (v) R45 — ADDING-A-SETUP.md matches the registries
# ---------------------------------------------------------------------

DOC = REPO / "docs" / "40 - DevDocs" / "cobalt" / "radar" / "ADDING-A-SETUP.md"
SECTIONS = {"Triggers (`TRIGGERS`)": "TRIGGERS", "Stop placements (`STOPS`)": "STOPS",
            "Structural refs (`STRUCTURAL_REFS`)": "STRUCTURAL_REFS", "Relations (`RELATIONS`)": "RELATIONS",
            "Atoms (`ATOMS`)": "ATOMS"}


def _doc_bricks() -> dict[str, set[str]]:
    out, current = {name: set() for name in SECTIONS.values()}, None
    for line in DOC.read_text().splitlines():
        if line.startswith("### "):
            current = SECTIONS.get(line[4:].strip())
            continue
        if line.startswith("## "):
            current = None
        if current and line.startswith("- "):
            head = line[2:].split(" — ")[0]
            out[current] |= set(re.findall(r"`([^`]+)`", head))
    return out


def test_lego_v_adding_a_setup_names_exactly_the_registries():
    from cobalt.radar.formation.atoms import ATOMS, RELATIONS
    from cobalt.radar.formation.stops import STOPS, STRUCTURAL_REFS
    from cobalt.radar.formation.triggers import TRIGGERS

    registries = {
        "TRIGGERS": {t.value for t in TRIGGERS}, "STOPS": set(STOPS),
        "STRUCTURAL_REFS": {r.value for r in STRUCTURAL_REFS}, "RELATIONS": set(RELATIONS), "ATOMS": set(ATOMS),
    }
    doc = _doc_bricks()
    for name, keys in registries.items():
        assert doc[name] == keys, (name, sorted(keys - doc[name]), sorted(doc[name] - keys))
    assert len(DOC.read_text().splitlines()) <= 120


# ---------------------------------------------------------------------
# The closing experiments
# ---------------------------------------------------------------------


#: X22's STEP-9 FINDING (report ESCALATE): the stage builds the Extension, and
#: publishes its observations (`atrs_from_open`, `leg_count`, the seam
#: values), for EVERY def, so every def reads the Extension's `TUNABLE_KEYS`;
#: only an Extension-anchored def declares them in its closure. None of the
#: three rows is `source: assumed` today, so no assumed mark is lost; the repair (the
#: stage's always-read keys in `closure_keys`) is a source change, not STEP-9's.
ALWAYS_READ_UNDECLARED = frozenset({"extension.path_a_volume_ma_bars", "extension.path_a_volume_sigma",
                                    "extension.path_b_atr"})
#: X22's second STEP-9 FINDING (report ESCALATE): a TRIGGER resolver's own
#: detector keys are not in R2-2.2's closure (its three terms are cfg tokens,
#: the detectors of the atoms the def NAMES, and conventions) — `trendline_break`
#: reads the micro-Range and pivot keys for its flat / sloped case. Today no card
#: can be under-marked by it: vwap-continuation cannot form at production
#: defaults (F1). The repair (trigger / stop resolvers declare `TUNABLE_KEYS`
#: into the closure) is a source change, not STEP-9's.
TRIGGER_READ_UNDECLARED = frozenset({"pivot.n", "range.micro.bound_flat_slope_atr",
                                     "range.micro.touch_tolerance_atr", "range.micro.touches_per_side"})
EXPECTED_UNDECLARED = {
    "rubberband": frozenset(), "backside": frozenset(), "fashionably-late": frozenset(),
    "nine-ema-scalp": frozenset(), "hitchhiker": ALWAYS_READ_UNDECLARED, "second-chance": ALWAYS_READ_UNDECLARED,
    "example-lego-eighth": ALWAYS_READ_UNDECLARED,
    "vwap-continuation": ALWAYS_READ_UNDECLARED | TRIGGER_READ_UNDECLARED,
}


def test_x22_over_all_eight(corpus, eighth):
    """X22 at STEP-9: every instrumented read inside each def's declared
    closure, but for the always-read Extension keys (named above)."""
    import test_setups_registries as reg
    from cobalt.radar.evaluate import closure_keys

    defs = {key: ld for key, (_s, ld) in corpus.items() if key in shapes.SHAPES}
    defs["example-lego-eighth"] = eighth
    extra: dict[str, list[str]] = {}
    for key, ld in defs.items():
        rows = reg._RecordingRows(shapes.tunables_for(ld))
        for m in range(0, 391, 30):
            shapes.evaluate(ld, "FTFT", shapes.DAY_START + timedelta(minutes=m), tunables=rows)
        declared = closure_keys(ld.definition) | set(shapes.user_rows(ld))
        extra[key] = sorted(rows.read - declared)
        print(f"X22 {key}: reads={len(rows.read)} undeclared={extra[key]}")
    assert {k: frozenset(v) for k, v in extra.items()} == EXPECTED_UNDECLARED, extra  # a guard: exactly these
    # none of them is `source: assumed` in committed config, so no assumed mark is lost today
    assert all(sup.engine_tunables()[k].source.value != "assumed" for k in ALWAYS_READ_UNDECLARED)


def test_frame_property_over_every_atom_on_the_committed_day():
    """[F-04] at STEP-9, every atom: `pred_as_long(mirror(bars)) == pred_as_short(bars)`
    — the short frame of the real member equals the long frame of the member
    whose bars (and daily series) are mirrored."""
    from cobalt.radar.anatomy.daily import DailySeries
    from cobalt.radar.evaluate import member_frames
    from cobalt.radar.formation.atoms import ATOMS

    rows = shapes.tunables_for(shapes.load_shape_fresh("second-chance"))
    checked = 0
    for m in (60, 120, 200, 300):
        at = shapes.DAY_START + timedelta(minutes=m)
        real = shapes.member("FTFT", at)
        flip = lambda b: b.model_copy(update={"open": -b.open, "high": -b.low, "low": -b.high, "close": -b.close})
        mirrored = real.model_copy(update={
            "bars": tuple(flip(b) for b in real.bars),
            "daily": DailySeries(ticker=real.daily.ticker, bars=tuple(flip(b) for b in real.daily.bars),
                                 fetched_at=real.daily.fetched_at, source=real.daily.source),
        })
        short = member_frames(real, tunables=rows, defaults=sup.defaults(), clock=session_clock())["short"]
        long = member_frames(mirrored, tunables=rows, defaults=sup.defaults(), clock=session_clock())["long"]
        for name in ATOMS:
            assert short.atoms[name] == long.atoms[name], (at, name, short.atoms[name], long.atoms[name])
            checked += 1
    print(f"F-04 at STEP-9: atoms={len(ATOMS)} checks={checked}")
    assert checked == 4 * len(ATOMS)
