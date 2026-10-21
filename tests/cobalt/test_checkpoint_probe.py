"""f5-probe (card 973): `cobalt checkpoint probe <item>`, offline.

The world is `test_checkpoints_offline.py`'s `cp` (every seam faked, a
`tmp_path` vault, no network) and its `groups_http` (httpx faked). Every
test reaches the probe through the CLI first, so each is red on BASE at
`invalid choice: 'probe'`. Each pin finds its lines by content and holds
no hash (brain R1472). Constructed figures and notes only (L32).
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from contextlib import contextmanager
from pathlib import Path
from types import SimpleNamespace

import pytest

from test_checkpoints_offline import SECTORS, _cfg, at, cp, groups_csv, groups_http, reply  # noqa: F401
from test_prefill_refresh import finviz, plan, vault  # noqa: F401 — F4's fixtures, under `cp`

ITEMS = ("X4", "X5", "X6", "X7", "X10", "X13")
LINE = re.compile(r"^PROBE (X4|X5|X6|X7|X10|X13) (OK|FAIL|NOT RUN) ")
#: Eleven distinct constructed Changes: a rotation of one place moves every rank.
DISTINCT = {n: f"{(i - 5) * 0.15:.2f}" for i, n in enumerate(SECTORS)}
HIS_LEGS = {
    "X5": "a window with scripted voice local.plan calls (his voice may be slow)",
    "X7": "Obsidian open on a dev vault copy; the offline leg is the gate run's pytest",
    "X10": "Obsidian Sync on a dev vault copy",
}


def _main(monkeypatch, *argv):
    import cobalt.cli

    monkeypatch.setattr("sys.argv", ["cobalt", *argv])
    with pytest.raises(SystemExit) as exc:
        cobalt.cli.main()
        raise SystemExit(0)
    return exc.value.code


def _probe(monkeypatch, capsys, *argv):
    capsys.readouterr()
    code = _main(monkeypatch, "checkpoint", "probe", *argv)
    out = capsys.readouterr()
    return code, out.out, out.err


@pytest.fixture
def real_fetch_groups():
    """The real `fetch_groups`, taken before `cp` fakes it (list it first)."""
    from cobalt.prefill import checkpoints

    return checkpoints.fetch_groups


@pytest.fixture
def world(cp, monkeypatch):  # noqa: F811
    """`cp` at 07:45 ET on its constructed day, Groups GETs counted."""
    from cobalt.prefill import checkpoints
    from cobalt.session import clock as clock_mod

    monkeypatch.setattr(clock_mod, "now_utc", lambda: at(7, 45))
    cp.sectors = dict(DISTINCT)
    cp.groups_gets = 0
    inner = checkpoints.fetch_groups

    async def counted(params, **kw):
        cp.groups_gets += 1
        return await inner(params, **kw)

    monkeypatch.setattr(checkpoints, "fetch_groups", counted)
    return cp


def _sent(req) -> list[dict]:
    return json.loads(req.messages[-1].content)


# ===========================================================================
# P1 — the subcommand
# ===========================================================================


def test_the_probe_is_mounted_and_lists_the_six_items(monkeypatch, capsys):
    assert _main(monkeypatch, "checkpoint", "probe", "--help") == 0
    out = capsys.readouterr().out
    for item in ITEMS:
        assert item in out
    assert "--keep-groups" in out


# ===========================================================================
# P2 — the boundary
# ===========================================================================


@pytest.mark.parametrize("item", ITEMS)
def test_production_and_unset_env_are_refused(world, monkeypatch, capsys, item):
    monkeypatch.setenv("COBALT_ENV", "production")
    assert _probe(monkeypatch, capsys, item)[:2] == (1, f"PROBE {item} FAIL refused: COBALT_ENV=production (dev only)\n")
    monkeypatch.delenv("COBALT_ENV")
    assert _probe(monkeypatch, capsys, item)[:2] == (
        1, f"PROBE {item} FAIL refused: COBALT_ENV is unset — set it to one of production, dev.\n")
    assert world.gets == 0 and world.calls == [], "nothing fetched, nothing called"


def test_no_write_no_dm_no_db_no_launchctl(world, monkeypatch, capsys):
    from cobalt.prefill import checkpoints

    def forbidden(name):
        def boom(*a, **kw):
            raise AssertionError(f"{name} reached")

        return boom

    for name in ("VaultWriter", "ensure_daily_note", "CheckpointStore", "VaultWriteStore", "send_dm", "as_job"):
        monkeypatch.setattr(checkpoints, name, forbidden(name))
    spawned = []
    real_run, real_popen = subprocess.run, subprocess.Popen

    def run(*a, **kw):
        spawned.append(a[0] if a else kw.get("args"))
        return real_run(*a, **kw)

    def popen(*a, **kw):
        spawned.append(a[0] if a else kw.get("args"))
        return real_popen(*a, **kw)

    monkeypatch.setattr(subprocess, "run", run)
    monkeypatch.setattr(subprocess, "Popen", popen)
    verdicts = {}
    for item in ITEMS:
        code, out, _ = _probe(monkeypatch, capsys, item)
        assert "error" not in out, out
        verdicts[item] = LINE.match(out).group(2)
    assert verdicts == {"X4": "OK", "X5": "NOT RUN", "X6": "OK", "X7": "NOT RUN", "X10": "NOT RUN", "X13": "OK"}
    assert not [a for a in spawned if "launchctl" in str(a)]
    assert world.dms == []


def test_the_scratch_dir_is_gone_after_the_run(world, monkeypatch, capsys):
    import tempfile

    made, seen = [], []
    real = tempfile.mkdtemp

    def record(*a, **kw):
        path = real(*a, **kw)
        made.append(path)
        return path

    monkeypatch.setattr(tempfile, "mkdtemp", record)
    world.on_call = lambda req: seen.append(os.getcwd())
    cwd = os.getcwd()
    for item in ("X6", "X13", "X5"):
        assert LINE.match(_probe(monkeypatch, capsys, item)[1])
    probes = [p for p in made if Path(p).name.startswith("f5-probe-")]
    assert len(probes) == 3
    assert not [p for p in probes if Path(p).exists()]
    assert seen and {Path(s).resolve() for s in seen} == {Path(probes[0]).resolve()}, "X6 ran in its scratch"
    assert os.getcwd() == cwd


def test_checkpoint_run_is_unchanged(monkeypatch):
    from cobalt.prefill import checkpoints

    assert _main(monkeypatch, "checkpoint", "probe", "--help") == 0  # red on BASE: the probe is not there
    seen = []
    monkeypatch.setattr(checkpoints, "cmd_run", lambda args: seen.append((args.slot, args.dry_run)))
    assert _main(monkeypatch, "checkpoint", "run", "--slot", "0745", "--dry-run") == 0
    assert seen == [("0745", True)]


# ===========================================================================
# G1 — the keep seam
# ===========================================================================


def test_keep_groups_writes_header_and_eleven_rows_once(real_fetch_groups, world, groups_http, monkeypatch, capsys,
                                                         tmp_path):
    from cobalt.prefill import checkpoints

    keep_root = tmp_path / "keep-root"
    keep_root.mkdir()
    target = keep_root / "groups_real.csv"
    assert _probe(monkeypatch, capsys, "X4", "--keep-groups", str(target))[:2] == (
        1, "PROBE X4 FAIL refused: --keep-groups is X6's\n")
    monkeypatch.setattr("cobalt.prefill.checkpoint_probe.KEEP_ROOT", keep_root)
    outside = tmp_path / "elsewhere.csv"
    code, out, _ = _probe(monkeypatch, capsys, "X6", "--keep-groups", str(outside))
    assert code == 1 and f"FAIL refused: --keep-groups PATH must be under {keep_root}/" in out
    assert not outside.exists() and world.gets == 0

    monkeypatch.setattr(checkpoints, "fetch_groups", real_fetch_groups)
    header, *rows = [line for line in groups_csv().split("\n") if line]
    groups_http.body = "\n".join([header, "", *rows, "", ""])  # blank lines: the parse skips them, the file drops them
    code, out, _ = _probe(monkeypatch, capsys, "X6", "--keep-groups", str(target))
    assert code == 0, out
    assert out.rstrip("\n").endswith(f"kept: {target}")
    kept = target.read_text(encoding="utf-8").split("\n")
    assert kept[0].startswith("# real capture ")
    assert kept[0].endswith(" ET, dev probe X6, header and 11 rows only (L45)")
    assert kept[1:] == [header, *rows, ""]
    assert len(groups_http.seen) == 1

    before = target.read_bytes()
    code, out, _ = _probe(monkeypatch, capsys, "X6", "--keep-groups", str(target))
    assert code == 1 and "refused: --keep-groups PATH exists" in out
    assert target.read_bytes() == before and len(groups_http.seen) == 1, "no overwrite, no second GET"

    hit = keep_root / "hit.csv"
    monkeypatch.setattr("cobalt.prefill.checkpoint_probe.redact",
                        lambda text, **kw: SimpleNamespace(hits={"constructed_kind": 1}))
    code, out, _ = _probe(monkeypatch, capsys, "X6", "--keep-groups", str(hit))
    assert code == 0 and out.rstrip("\n").endswith("kept: refused (secret-shaped: constructed_kind)")
    assert not hit.exists()


def test_the_run_path_writes_no_body(real_fetch_groups, world, groups_http, monkeypatch, capsys, tmp_path):
    import asyncio
    import inspect

    from cobalt.prefill import checkpoints

    # Found by content: `keep=` only in the pass-on, never in the run path.
    pass_on = inspect.getsource(checkpoints.fetch_figures)
    keep_lines = [line.strip() for line in inspect.getsource(checkpoints).split("\n") if "keep=" in line]
    assert keep_lines, "fetch_figures passes keep= on"
    assert all(line in pass_on or line in inspect.getsource(real_fetch_groups) for line in keep_lines)
    for fn in (checkpoints.cmd_run, checkpoints.run_checkpoint):
        assert "keep" not in inspect.getsource(fn)

    dirs = [tmp_path / name for name in ("cwd", "home", "keep-root")]
    for d in dirs:
        d.mkdir()
    monkeypatch.chdir(dirs[0])
    monkeypatch.setenv("HOME", str(dirs[1]))
    monkeypatch.setattr("cobalt.prefill.checkpoint_probe.KEEP_ROOT", dirs[2])

    asyncio.run(real_fetch_groups(_cfg().groups))
    monkeypatch.setattr(checkpoints, "fetch_groups", real_fetch_groups)
    checkpoints.fetch_figures(_cfg())

    @contextmanager
    def fake_as_job(label, *, skip=False, store=None):
        yield SimpleNamespace(result=None)

    monkeypatch.setattr(checkpoints, "as_job", fake_as_job)
    monkeypatch.setattr(checkpoints, "default_stores", lambda: (world.store, world.vstore))
    assert _main(monkeypatch, "checkpoint", "run", "--slot", "0745", "--dry-run") == 0
    assert len(groups_http.seen) == 3
    for d in dirs:
        assert list(d.iterdir()) == []
    header = groups_http.body.split("\n")[0]
    assert not [p for p in tmp_path.rglob("*") if p.is_file() and header in p.read_text(errors="ignore")]


# ===========================================================================
# X6 — four real-shape prompts
# ===========================================================================


def test_x6_four_prompts_one_per_slot_pair(world, monkeypatch, capsys):
    code, out, _ = _probe(monkeypatch, capsys, "X6")
    assert code == 0, out
    assert out.startswith("PROBE X6 OK figures: 1 real fetch + 3 derived by rule D · prompts 4 · prompt_refused 0 · ")
    assert "0715 ok · 0745 ok · 0815 ok · 0845 ok" in out
    assert world.groups_gets == 1 and world.gets == 2, "ONE Groups GET, one screener GET"
    assert [r.request_id[-4:] for r in world.calls] == ["0715", "0745", "0815", "0845"]
    phrases = [{e["phrase"] for e in _sent(r)} for r in world.calls]
    assert "prior_close" in phrases[0] and "index_move" not in phrases[0]
    for later in phrases[1:]:
        assert {"index_move", "rank_move"} <= later and "prior_close" not in later


def test_x6_one_prompt_refused_fails(world, monkeypatch, capsys):
    def on_call(req):
        world.error = "prompt_refused" if req.request_id.endswith("0815") else None

    world.on_call = on_call
    code, out, _ = _probe(monkeypatch, capsys, "X6")
    assert code == 1
    assert out.startswith("PROBE X6 FAIL — prompt_refused 1 of 4 (0815) · ")
    assert "0815 degraded (prompt_refused)" in out


def test_x6_no_note_is_not_run_and_fetches_nothing(world, monkeypatch, capsys):
    world.note.unlink()
    code, out, _ = _probe(monkeypatch, capsys, "X6")
    assert code == 3
    assert out.startswith("PROBE X6 NOT RUN — no daily note for ") and "(checkpoints.py:747-751)" in out
    assert world.gets == 0 and world.calls == []


def test_x6_gate_refusal_and_dead_source_are_not_run(world, plan, monkeypatch, capsys):  # noqa: F811
    plan.ceiling, world.rpm = 50, 49.0
    code, out, _ = _probe(monkeypatch, capsys, "X6")
    assert code == 3 and out.startswith("PROBE X6 NOT RUN — Finviz gate: ")
    assert world.gets == 0
    world.rpm = 10.0
    world.groups_dead = "Finviz groups fetch failed: constructed outage"
    assert _probe(monkeypatch, capsys, "X6")[:2] == (3, "PROBE X6 NOT RUN — finviz-groups degraded\n")
    assert world.calls == []


# ===========================================================================
# X4 — twenty generations
# ===========================================================================


def _valid_then_invalid(world, n_valid):
    count = {"n": 0}

    def on_call(req):
        count["n"] += 1
        world.reply = None if count["n"] <= n_valid else "not json"

    world.on_call = on_call


def test_x4_fifteen_valid_is_ok_fourteen_fails(world, monkeypatch, capsys):
    _valid_then_invalid(world, 15)
    code, out, _ = _probe(monkeypatch, capsys, "X4")
    assert code == 0, out
    assert out.startswith("PROBE X4 OK valid 15/20 · invalid kinds UnsourcedFigure=5 · number-word hits none")
    assert "degraded-by-default" not in out and "plist load not blocked" not in out
    assert len(world.calls) == 20

    _valid_then_invalid(world, 14)
    code, out, _ = _probe(monkeypatch, capsys, "X4")
    assert code == 1
    assert out.startswith("PROBE X4 FAIL valid 14/20 · invalid kinds UnsourcedFigure=6")
    assert "→ narrative degraded-by-default (FINAL :178)" in out
    assert out.rstrip("\n").endswith("; plist load not blocked by X4")


def test_x4_a_number_word_fails_and_names_the_phrase(world, monkeypatch, capsys):
    from cobalt.prefill import checkpoints

    assert _probe(monkeypatch, capsys, "X4")[0] == 0
    monkeypatch.setitem(checkpoints.PHRASES, "leader_three", "leading")
    real_delta = checkpoints.compute_delta

    def renamed(figs, base):
        delta = real_delta(figs, base)
        lines = [dict(x, phrase="leader_three") if x["phrase"] == "leader" else x for x in delta["lines"]]
        return dict(delta, lines=lines)

    def on_call(req):
        pick = next(e for e in _sent(req) if e["phrase"] == "leader_three")
        world.reply = reply(("leader_three", [pick["ref"]]))

    monkeypatch.setattr(checkpoints, "compute_delta", renamed)
    world.on_call = on_call
    code, out, _ = _probe(monkeypatch, capsys, "X4")
    assert code == 1
    assert "valid 20/20" in out and "number-word hits leader_three=20" in out
    assert "→ leader_three removed from the enum (FINAL :178)" in out
    assert "degraded-by-default" not in out
    assert out.rstrip("\n").endswith("; plist load not blocked by X4")


def test_x4_request_equals_narrates(world, monkeypatch, capsys):
    assert _probe(monkeypatch, capsys, "X4")[0] == 0
    assert len(world.calls) == 20
    from cobalt.prefill import checkpoint_probe, checkpoints

    cfg = _cfg()
    entries = checkpoints.compute_delta(
        {"indices": {"SPY": {"price": "500.00", "change_pct": "0.10"}},
         "sectors": {n: {"change": c, "rel_volume": "1.00", "perf_week": "0.50"} for n, c in DISTINCT.items()}},
        None)["lines"]
    narrative = checkpoints.narrate(cfg, entries, request_id="x4-pin")
    req, sha = checkpoint_probe._request(cfg, entries, "x4-pin")
    assert req.model_dump() == world.calls[-1].model_dump()
    assert sha == narrative.prompt_sha256


def test_x4_clause_holds_no_reply_text(world, monkeypatch, capsys):
    marker = "constructed reply words"
    world.reply = json.dumps({"lines": [{"phrase_id": "leader", "refs": [0]}], "note": marker})
    code, out, err = _probe(monkeypatch, capsys, "X4")
    assert code == 1 and out.startswith("PROBE X4 FAIL valid 0/20 · invalid kinds UnsourcedFigure=20")
    assert marker not in out and marker not in err
    assert re.search(r"\d\.\d", out) is None, "no figure in the line"


# ===========================================================================
# X13 — the window rule, in process
# ===========================================================================


def test_x13_four_late_fires_refused_ok(world, monkeypatch, capsys):
    assert _probe(monkeypatch, capsys, "X13")[:2] == (
        0, "PROBE X13 OK (offline: the window rule refuses a late fire on 4 of 4 slots; "
           "launchd leg not run, no plist loaded)\n")
    assert world.gets == 0 and world.calls == []


def test_x13_a_window_that_admits_a_late_fire_fails(world, monkeypatch, capsys):
    from cobalt.prefill import checkpoints

    assert _probe(monkeypatch, capsys, "X13")[0] == 0
    monkeypatch.setattr(checkpoints, "window_refusal", lambda *a, **kw: None)
    code, out, _ = _probe(monkeypatch, capsys, "X13")
    assert code == 1 and out.startswith("PROBE X13 FAIL — 07:15 ")
    assert world.gets == 0, "an admitted late fire fetches nothing in the probe"


# ===========================================================================
# H1 — his legs
# ===========================================================================


@pytest.mark.parametrize("item", sorted(HIS_LEGS))
def test_his_legs_are_not_run_and_call_nothing(world, monkeypatch, capsys, item):
    spawned = []
    monkeypatch.setattr(subprocess, "run", lambda *a, **kw: spawned.append(a))
    monkeypatch.setattr(subprocess, "Popen", lambda *a, **kw: spawned.append(a))
    assert _probe(monkeypatch, capsys, item)[:2] == (3, f"PROBE {item} NOT RUN — needs his hand: {HIS_LEGS[item]}\n")
    assert world.gets == 0 and world.calls == [] and world.dms == [] and spawned == []


# ===========================================================================
# C1 — the control and the line
# ===========================================================================


@pytest.mark.parametrize("item", ["X2", "X12", "X99"])
def test_an_unknown_item_is_refused(world, monkeypatch, capsys, item):
    code, out, err = _probe(monkeypatch, capsys, item)
    assert code == 2 and f"invalid choice: '{item}'" in err
    assert world.gets == 0


def _setup(world, monkeypatch, how):
    from cobalt.prefill import checkpoints

    if how == "refused_0815":
        world.on_call = lambda req: setattr(world, "error", "prompt_refused" if req.request_id.endswith("0815") else None)
    elif how == "no_note":
        world.note.unlink()
    elif how == "all_invalid":
        world.reply = "not json"
    elif how == "window_open":
        monkeypatch.setattr(checkpoints, "window_refusal", lambda *a, **kw: None)


@pytest.mark.parametrize("item,verdict,code,how", [
    ("X6", "OK", 0, None), ("X6", "FAIL", 1, "refused_0815"), ("X6", "NOT RUN", 3, "no_note"),
    ("X4", "OK", 0, None), ("X4", "FAIL", 1, "all_invalid"),
    ("X13", "OK", 0, None), ("X13", "FAIL", 1, "window_open"),
    ("X5", "NOT RUN", 3, None), ("X7", "NOT RUN", 3, None), ("X10", "NOT RUN", 3, None),
])
def test_each_item_prints_one_line_and_exits_by_verdict(world, monkeypatch, capsys, item, verdict, code, how):
    _setup(world, monkeypatch, how)
    got, out, _ = _probe(monkeypatch, capsys, item)
    lines = out.split("\n")
    assert len(lines) == 2 and lines[1] == "", "exactly one stdout line"
    m = LINE.match(lines[0])
    assert m and m.group(1) == item and m.group(2) == verdict
    assert got == code
