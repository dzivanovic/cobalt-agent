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


#: A kept capture's marker line (`_keep`'s shape), on the constructed day.
KEPT_MARKER = "# real capture 2026-09-03 07:40 ET, dev probe X6, header and 11 rows only (L45)"


def _groups_body(changes: dict[str, str], *, drop: int = 0) -> str:
    """`groups_csv()` with each sector's Change set from `changes`; `drop` rows cut from the end."""
    import csv
    import io

    header, *rows = [r for r in csv.reader(io.StringIO(groups_csv())) if r]
    name, change = header.index("Name"), header.index("Change")
    out = io.StringIO()
    writer = csv.writer(out, quoting=csv.QUOTE_ALL, lineterminator="\n")
    writer.writerow(header)
    for row in rows[:len(rows) - drop]:
        writer.writerow([f"{changes[row[name]]}%" if i == change else c for i, c in enumerate(row)])
    return out.getvalue()


def _write_body(path: Path, changes: dict[str, str], *, drop: int = 0) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(KEPT_MARKER + "\n" + _groups_body(changes, drop=drop), encoding="utf-8")


@pytest.fixture
def x4_paths(monkeypatch, tmp_path):
    """X4's two Groups sources moved into `tmp_path`; neither written yet."""
    from cobalt.prefill import checkpoint_probe

    keep_root = tmp_path / "keep-root"
    keep_root.mkdir()
    paths = SimpleNamespace(kept=keep_root / "groups_sector_v140_real.csv",
                            fixture=tmp_path / "fixtures" / "groups_sector_v140_real.csv")
    monkeypatch.setattr(checkpoint_probe, "KEEP_ROOT", keep_root)
    monkeypatch.setattr(checkpoint_probe, "X4_GROUPS_KEPT", paths.kept, raising=False)
    monkeypatch.setattr(checkpoint_probe, "X4_GROUPS_FIXTURE", paths.fixture, raising=False)
    return paths


@pytest.fixture
def x4_kept(x4_paths):
    """X4's Groups body: a kept capture of DISTINCT (constructed)."""
    _write_body(x4_paths.kept, DISTINCT)
    return x4_paths


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


def test_no_write_no_dm_no_db_no_launchctl(world, x4_kept, monkeypatch, capsys):
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


X4_SOURCES = "groups: kept capture · indices: constructed · "


def test_x4_fifteen_valid_is_ok_fourteen_fails(world, x4_kept, monkeypatch, capsys):
    _valid_then_invalid(world, 15)
    code, out, _ = _probe(monkeypatch, capsys, "X4")
    assert code == 0, out
    assert out.startswith(f"PROBE X4 OK {X4_SOURCES}valid 15/20 · invalid kinds UnsourcedFigure=5 · number-word hits none")
    assert "degraded-by-default" not in out and "plist load not blocked" not in out
    assert len(world.calls) == 20

    _valid_then_invalid(world, 14)
    code, out, _ = _probe(monkeypatch, capsys, "X4")
    assert code == 1
    assert out.startswith(f"PROBE X4 FAIL {X4_SOURCES}valid 14/20 · invalid kinds UnsourcedFigure=6")
    assert "→ narrative degraded-by-default (FINAL :178)" in out
    assert out.rstrip("\n").endswith("; plist load not blocked by X4")


def test_x4_a_number_word_fails_and_names_the_phrase(world, x4_kept, monkeypatch, capsys):
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


def test_x4_request_equals_narrates(world, x4_kept, monkeypatch, capsys):
    assert _probe(monkeypatch, capsys, "X4")[0] == 0
    assert len(world.calls) == 20
    from cobalt.prefill import checkpoint_probe, checkpoints

    cfg = _cfg()
    entries = checkpoints.compute_delta(
        {"indices": {t: {"price": p, "change_pct": c} for t, (p, c) in checkpoint_probe.X4_INDICES.items()},
         "sectors": {n: {"change": c, "rel_volume": "1.00", "perf_week": "0.50"} for n, c in DISTINCT.items()}},
        None)["lines"]
    narrative = checkpoints.narrate(cfg, entries, request_id="x4-pin")
    req, sha = checkpoint_probe._request(cfg, entries, "x4-pin")
    assert req.model_dump() == world.calls[-1].model_dump()
    assert sha == narrative.prompt_sha256


def test_x4_clause_holds_no_reply_text(world, x4_kept, monkeypatch, capsys):
    marker = "constructed reply words"
    world.reply = json.dumps({"lines": [{"phrase_id": "leader", "refs": [0]}], "note": marker})
    code, out, err = _probe(monkeypatch, capsys, "X4")
    assert code == 1 and out.startswith(f"PROBE X4 FAIL {X4_SOURCES}valid 0/20 · invalid kinds UnsourcedFigure=20")
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
def test_each_item_prints_one_line_and_exits_by_verdict(world, x4_kept, monkeypatch, capsys, item, verdict, code,
                                                         how):
    _setup(world, monkeypatch, how)
    got, out, _ = _probe(monkeypatch, capsys, item)
    lines = out.split("\n")
    assert len(lines) == 2 and lines[1] == "", "exactly one stdout line"
    m = LINE.match(lines[0])
    assert m and m.group(1) == item and m.group(2) == verdict
    assert got == code


# ===========================================================================
# CHECK findings (f5-probe check, 2026-10-21) — judged by running
# ===========================================================================


def test_x6_rule_d_steps_the_indices_and_rotates_the_sectors(world, monkeypatch, capsys):
    """Check A5: rule D's values, not only its phrases. The `cp` SPY is
    500.00 / 0.10 (= S3); k slots back is k x 0.50 and k x 0.10 lower, and
    each sector takes the Change of the sector k places on in SECTORS."""
    code, out, _ = _probe(monkeypatch, capsys, "X6")
    assert code == 0, out
    texts = [[e["text"] for e in _sent(r)] for r in world.calls]
    assert "SPY 498.50 (-0.20% vs prior close)" in texts[0]
    assert "SPY 498.50 → 499.00 (+0.50), change -0.20% → -0.10%" in texts[1]
    assert "SPY 499.50 → 500.00 (+0.50), change +0.00% → +0.10%" in texts[3]
    top = max(DISTINCT, key=lambda n: float(DISTINCT[n]))
    rotated = SECTORS[(SECTORS.index(top) - 3) % len(SECTORS)]
    assert f"leader: {rotated} (+{DISTINCT[top]}%)" in texts[0]
    assert f"leader: {top} (+{DISTINCT[top]}%)" in texts[3]


# ===========================================================================
# f5-probe-x4-fix (card 989) — the Finviz leg at the repo root; X4 needs no Finviz
# ===========================================================================


def test_fr1_the_finviz_leg_runs_at_the_repo_root(world, monkeypatch, capsys, tmp_path):
    """The old tree resolves `configs/` and `data/.cobalt_vault` against the
    cwd (`cobalt_agent/config.py:543`, `security/vault.py:19`): the gate check
    and the fetch must see the repo root, never the scratch. A path compare
    only; the vault file is never opened."""
    from cobalt.prefill import checkpoint_probe, checkpoints

    monkeypatch.chdir(tmp_path)
    seen = []

    def recorder(name, inner):
        def record(*a, **kw):
            seen.append((name, Path.cwd(), Path("data/.cobalt_vault").resolve()))
            return inner(*a, **kw)

        return record

    for name in ("check_demand", "fetch_figures"):
        monkeypatch.setattr(checkpoints, name, recorder(name, getattr(checkpoints, name)))
    code, out, _ = _probe(monkeypatch, capsys, "X6")
    assert code == 0, out
    assert [name for name, *_ in seen] == ["check_demand", "fetch_figures"]
    root = checkpoint_probe.REPO_ROOT
    for name, cwd, vault in seen:
        assert cwd == root, f"{name} ran at {cwd}, where cobalt_agent/config.py:543 finds no configs/"
        assert (cwd / "configs").is_dir()
        assert vault == root / "data" / ".cobalt_vault"


def test_fr2_the_scratch_holds_everything_but_the_fetch(world, monkeypatch, capsys, tmp_path):
    from cobalt.prefill import checkpoint_probe

    monkeypatch.chdir(tmp_path)
    here = Path.cwd()
    seen = []
    world.on_call = lambda req: seen.append(Path.cwd())
    code, out, _ = _probe(monkeypatch, capsys, "X6")
    assert code == 0, out
    assert len(seen) == 4
    for cwd in seen:
        assert cwd.name.startswith("f5-probe-") and cwd != checkpoint_probe.REPO_ROOT
        assert not cwd.exists(), "the scratch dir is gone"
    assert Path.cwd() == here

    with pytest.raises(RuntimeError, match="constructed failure"):
        with checkpoint_probe._at_repo():
            assert Path.cwd() == checkpoint_probe.REPO_ROOT
            raise RuntimeError("constructed failure inside the fetch")
    assert Path.cwd() == here, "the cwd is restored on an exception"


def test_x4_model_calls_run_in_the_scratch(world, x4_kept, monkeypatch, capsys, tmp_path):
    """Check O1: X4 reaches no Finviz, so none of its steps may leave the scratch."""
    from cobalt.prefill import checkpoint_probe

    monkeypatch.chdir(tmp_path)
    here = Path.cwd()
    seen = []
    world.on_call = lambda req: seen.append(Path.cwd())
    code, out, _ = _probe(monkeypatch, capsys, "X4")
    assert code == 0, out
    assert len(seen) == 20
    for cwd in seen:
        assert cwd.name.startswith("f5-probe-") and cwd != checkpoint_probe.REPO_ROOT, f"an X4 call ran at {cwd}"
        assert not cwd.exists(), "the scratch dir is gone"
    assert Path.cwd() == here


def _no_finviz(monkeypatch):
    """Every Finviz seam X4 could reach raises."""
    import httpx

    import cobalt.aset.prefill
    from cobalt.prefill import checkpoints, market

    def boom(name):
        def reached(*a, **kw):
            raise AssertionError(f"{name} reached")

        return reached

    for name in ("check_demand", "fetch_figures", "fetch_groups", "fetch_market_table", "resolve_token"):
        monkeypatch.setattr(checkpoints, name, boom(name))
    monkeypatch.setattr(cobalt.aset.prefill, "resolve_token", boom("resolve_token"))
    monkeypatch.setattr(market, "resolve_token", boom("resolve_token"))
    monkeypatch.setattr(httpx, "AsyncClient", boom("httpx"))


def test_fr3_x4_reaches_no_finviz(world, x4_kept, monkeypatch, capsys):
    _no_finviz(monkeypatch)
    code, out, _ = _probe(monkeypatch, capsys, "X4")
    assert code == 0, out
    assert out.startswith("PROBE X4 OK groups: kept capture · indices: constructed · valid 20/20")
    assert len(world.calls) == 20
    assert world.gets == 0 and world.groups_gets == 0


def test_fr3_x4_without_a_body_is_not_run(world, x4_paths, monkeypatch, capsys):
    _no_finviz(monkeypatch)
    assert _probe(monkeypatch, capsys, "X4")[:2] == (
        3, "PROBE X4 NOT RUN — no real Groups body (X6 --keep-groups capture or the row (b) fixture)\n")
    assert world.calls == []


def test_fr3_the_fixture_wins_over_the_kept_capture(world, x4_paths, monkeypatch, capsys):
    fixture = {n: f"{float(c) + 0.05:.2f}" for n, c in DISTINCT.items()}  # eleven Changes, none of DISTINCT's
    assert not set(fixture.values()) & set(DISTINCT.values())
    _write_body(x4_paths.kept, DISTINCT)
    _write_body(x4_paths.fixture, fixture)
    _no_finviz(monkeypatch)
    code, out, _ = _probe(monkeypatch, capsys, "X4")
    assert code == 0, out
    assert out.startswith("PROBE X4 OK groups: row (b) fixture · indices: constructed · ")
    first = " ".join(e["text"] for e in _sent(world.calls[0]))
    assert f"(+{max(fixture.values(), key=float)}%)" in first
    assert f"(+{max(DISTINCT.values(), key=float)}%)" not in first


def test_fr3_a_short_body_is_not_run(world, x4_paths, monkeypatch, capsys):
    _write_body(x4_paths.kept, DISTINCT, drop=1)
    _no_finviz(monkeypatch)
    assert _probe(monkeypatch, capsys, "X4")[:2] == (
        3, "PROBE X4 NOT RUN — the Groups body is not the 11 sector rows\n")
    assert world.calls == []


def test_fr3_an_index_x4_indices_lacks_is_not_run(world, x4_kept, monkeypatch, capsys):
    from cobalt.prefill import checkpoint_probe

    monkeypatch.setattr(checkpoint_probe, "X4_INDICES",
                        {t: v for t, v in checkpoint_probe.X4_INDICES.items() if t != "IWM"})
    _no_finviz(monkeypatch)
    assert _probe(monkeypatch, capsys, "X4")[:2] == (3, "PROBE X4 NOT RUN — X4_INDICES lacks IWM\n")
    assert world.calls == []
