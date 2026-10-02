"""ops/desk/gate.sh — BUILD-HUB.md `## W`'s three suites in one call (card 19 worker-steps S3).

No run here touches cobalt_dev. A stub `uv` on PATH appends its argument list and the
COBALT_ENV / COBALT_LIVE_VAULT_ROOT it saw to a call log and answers from a per-test
script (canned pytest summaries, a canned fingerprint row, a canned proof-only output).
A tmp directory stands in for /Users/cobalt/cobalt-wt (COBALT_WT_ROOT) and holds the job
worktree with a copy of THIS tree's BUILD-HUB.md; a tmp repo stands in for
/Users/cobalt/cobalt (COBALT_REPO_ROOT) and holds a constructed `.env`.
"""

from __future__ import annotations

import json
import os
import re
import shlex
import shutil
import signal
import subprocess
import time
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
GATE = REPO / "ops" / "desk" / "gate.sh"
HUB = REPO / "docs" / "40 - DevDocs" / "prompts" / "BUILD-HUB.md"
CONSTRUCTED_ENV = "COBALT_TEST_CONSTRUCTED=1\n"
NAME = "x-job"

FP_ROW = "cols\trels\tviews_md5\n664\t35\t0123456789abcdef0123456789abcdef\n"
FP_OTHER = "cols\trels\tviews_md5\n670\t36\tfedcba9876543210fedcba9876543210\n"
PROOF = (
    "cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)\n\n"
    "table  side  schema  rows  digest  secs\n"
    "legs   user  -       -     -       0.00\n"
    "NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.\n"
)

UV_STUB = r'''#!/usr/bin/env python3
import json, os, sys, time
argv = sys.argv[1:]
log = os.environ["GATE_STUB_LOG"]
with open(log, "a") as f:
    f.write(json.dumps({"argv": argv, "COBALT_ENV": os.environ.get("COBALT_ENV"),
                        "COBALT_LIVE_VAULT_ROOT": os.environ.get("COBALT_LIVE_VAULT_ROOT")}) + "\n")
script = json.load(open(os.environ["GATE_STUB_SCRIPT"]))
calls = [json.loads(l)["argv"] for l in open(log)]
def nth(kind):
    return sum(1 for a in calls if kind(a)) - 1
is_fp = lambda a: "query" in a and any("pg_attribute" in x for x in a)
is_pytest = lambda a: a[:2] == ["run", "pytest"]
if is_pytest(argv):
    answers = script.get("pytest", [])
    k = nth(is_pytest)
    ans = answers[k] if k < len(answers) else {"out": "5 passed in 0.10s", "rc": 0}
    if ans.get("marker"):
        open(ans["marker"], "w").write("started\n")
    time.sleep(ans.get("sleep", 0))
    print(ans["out"])
    sys.exit(ans["rc"])
if is_fp(argv):
    fps = script.get("fp", [])
    k = nth(is_fp)
    sys.stdout.write(fps[k] if k < len(fps) else fps[-1])
    sys.exit(0)
if "query" in argv:
    sys.stdout.write(script.get("tickers", "ticker\tcount\n"))
    sys.exit(0)
if "--proof-only" in argv:
    sys.stdout.write(script.get("proof", ""))
    sys.exit(script.get("proof_rc", 0))
if "--rollback" in argv:
    print("cobalt db migrate — ROLLBACK on cobalt_dev")
    sys.exit(script.get("rollback_rc", 0))
if "migrate" in argv:
    print("cobalt db migrate — FORWARD on cobalt_dev")
    sys.exit(script.get("forward_rc", 0))
print("stub uv: unscripted call", argv, file=sys.stderr)
sys.exit(97)
'''


def hub_commands() -> dict[str, str]:
    """The commands BUILD-HUB.md `## W` and `## THE LOCK` tell a worker to type, read here
    independently of gate.sh so the two can be compared."""
    text = HUB.read_text().splitlines()
    out: dict[str, str] = {}
    for i, line in enumerate(text):
        if line.startswith("- (c) PASS 1"):
            out["pass1"] = text[i + 1].strip("`")
        if line.startswith("- (c3) PASS 2"):
            out["pass2"] = text[i + 1].strip("`")
        if line.startswith("- (a) OFFLINE:"):
            out["offline"] = re.findall(r"`([^`]*)`", line)[0]
        if line.startswith("- (e) LIVE-NOTE"):
            out["livenote"] = [s for s in re.findall(r"`([^`]*)`", line) if s.startswith("COBALT_LIVE")][0]
        if line.startswith("- (f) ALWAYS"):
            out["rollback"] = re.findall(r"`([^`]*)`", line)[0]
        if line.startswith("- (c2) FORWARD:"):
            out["forward"] = re.findall(r"`([^`]*)`", line)[0]
        if line.startswith("- (b) THE LOCK"):
            out["proof"] = [s for s in re.findall(r"`([^`]*)`", line) if "--proof-only" in s][0]
        if line.startswith("`COBALT_ENV=dev uv run cobalt db query --side user \"SELECT (SELECT"):
            out["fp"] = line.strip("`")
    return out


def argv_of(command: str) -> tuple[dict[str, str], list[str]]:
    """`VAR=x uv run …` → ({VAR: x}, [run, …]): what the stub `uv` sees."""
    words = shlex.split(command)
    env = {}
    while "=" in words[0] and not words[0].startswith("-"):
        k, v = words.pop(0).split("=", 1)
        env[k] = v
    assert words.pop(0) == "uv"
    return env, words


@pytest.fixture
def gate(tmp_path):
    wt = tmp_path / "wt"
    repo = tmp_path / "repo"
    job = wt / NAME
    (job / "docs" / "40 - DevDocs" / "prompts").mkdir(parents=True)
    shutil.copy(HUB, job / "docs" / "40 - DevDocs" / "prompts" / "BUILD-HUB.md")
    (wt / "beta").mkdir()
    repo.mkdir()
    (repo / ".env").write_text(CONSTRUCTED_ENV)
    stub = tmp_path / "bin"
    stub.mkdir()
    (stub / "uv").write_text(UV_STUB)
    (stub / "uv").chmod(0o755)
    calls = tmp_path / "uv-calls.jsonl"
    script = tmp_path / "uv-script.json"
    script.write_text(json.dumps({"fp": [FP_ROW], "proof": PROOF}))
    env = dict(
        os.environ, COBALT_WT_ROOT=str(wt), COBALT_REPO_ROOT=str(repo),
        PATH=f"{stub}{os.pathsep}{os.environ['PATH']}",
        GATE_STUB_LOG=str(calls), GATE_STUB_SCRIPT=str(script),
    )
    env.pop("COBALT_ENV", None)
    env.pop("COBALT_LIVE_VAULT_ROOT", None)
    return wt, repo, job, env, calls, script


def set_script(script: Path, **kw) -> None:
    data = {"fp": [FP_ROW], "proof": PROOF}
    data.update(kw)
    script.write_text(json.dumps(data))


def run_gate(env: dict, *args: str, gate: Path = GATE) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(gate), NAME, *args], env=env, capture_output=True, text=True, timeout=300
    )


def read_calls(calls: Path) -> list[dict]:
    if not calls.exists():
        return []
    return [json.loads(line) for line in calls.read_text().splitlines()]


def kind(call: dict) -> str:
    a = call["argv"]
    if a[:2] == ["run", "pytest"]:
        return "pytest"
    if "query" in a:
        return "fp" if any("pg_attribute" in x for x in a) else "tickers"
    if "--proof-only" in a:
        return "proof"
    if "--rollback" in a:
        return "rollback"
    if "migrate" in a:
        return "forward"
    return "?"


def test_withdb_green_runs_the_hub_commands_byte_for_byte_in_order(gate):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "withdb")
    assert done.returncode == 0, done.stdout + done.stderr
    log = read_calls(calls)
    assert [kind(c) for c in log] == ["fp", "proof", "pytest", "forward", "fp", "pytest", "rollback", "fp"]
    hub = hub_commands()
    expect = [hub["fp"], hub["proof"], hub["pass1"], hub["forward"], hub["fp"], hub["pass2"], hub["rollback"], hub["fp"]]
    for call, command in zip(log, expect):
        cenv, argv = argv_of(command)
        assert call["argv"] == argv, (call["argv"], command)
        assert call["COBALT_ENV"] == cenv.get("COBALT_ENV") == "dev"
    assert not (job / ".env").exists()
    out = done.stdout.splitlines()
    assert "with-DB 10/0" in out
    assert "cobalt_dev: 0013 — F2 = F0" in out
    assert ".env: removed" in out
    assert any(line.startswith(f"log: {wt / '.gate-logs' / NAME}-withdb-") for line in out)


def test_a_deselect_goes_into_pass_1_and_its_id_at_the_end_of_pass_2(gate):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "withdb", "--deselect", "x::y")
    assert done.returncode == 0, done.stdout + done.stderr
    pytests = [c["argv"] for c in read_calls(calls) if kind(c) == "pytest"]
    hub = hub_commands()
    assert pytests[0] == argv_of(hub["pass1"])[1] + ["--deselect", "x::y"]
    assert pytests[1] == argv_of(hub["pass2"])[1] + ["x::y"]


def test_pass_2_red_still_rolls_back_and_releases(gate):
    wt, repo, job, env, calls, script = gate
    set_script(script, pytest=[
        {"out": "5 passed in 0.1s", "rc": 0},
        {"out": "FAILED tests/cobalt/test_legs_db.py::test_x - assert 1 == 2\n1 failed, 4 passed in 0.1s", "rc": 1},
    ])
    done = run_gate(env, "withdb")
    assert done.returncode == 1, done.stdout + done.stderr
    kinds = [kind(c) for c in read_calls(calls)]
    assert kinds == ["fp", "proof", "pytest", "forward", "fp", "pytest", "rollback", "fp"]
    assert not (job / ".env").exists()
    assert "FAILED tests/cobalt/test_legs_db.py::test_x - assert 1 == 2" in done.stdout
    assert ".env: removed" in done.stdout


def test_pass_1_red_applies_nothing_and_releases(gate):
    wt, repo, job, env, calls, script = gate
    set_script(script, pytest=[{"out": "ERROR tests/cobalt/test_a.py\n1 error in 0.1s", "rc": 1}])
    done = run_gate(env, "withdb")
    assert done.returncode == 1, done.stdout + done.stderr
    assert [kind(c) for c in read_calls(calls)] == ["fp", "proof", "pytest"]
    assert not (job / ".env").exists()


def test_a_sibling_env_is_a_held_lock_and_no_uv_runs(gate):
    wt, repo, job, env, calls, script = gate
    (wt / "beta" / ".env").write_text(CONSTRUCTED_ENV)
    done = run_gate(env, "withdb")
    assert done.returncode == 4, done.stdout + done.stderr
    assert read_calls(calls) == []
    assert not (job / ".env").exists()
    assert (wt / "beta" / ".env").read_text() == CONSTRUCTED_ENV


def test_a_fingerprint_that_differs_after_the_rollback_exits_6(gate):
    wt, repo, job, env, calls, script = gate
    set_script(script, fp=[FP_ROW, FP_ROW, FP_OTHER])
    done = run_gate(env, "withdb")
    assert done.returncode == 6, done.stdout + done.stderr
    assert "cobalt_dev NOT back at 0013" in done.stdout
    assert not (job / ".env").exists()


def test_a_proof_only_that_is_not_clean_exits_5_before_any_suite(gate):
    wt, repo, job, env, calls, script = gate
    set_script(script, proof=PROOF.replace("0.00\n", "0.00 CHANGED\n"))
    done = run_gate(env, "withdb")
    assert done.returncode == 5, done.stdout + done.stderr
    assert [kind(c) for c in read_calls(calls)] == ["fp", "proof"]
    assert not (job / ".env").exists()


def test_livenote_with_an_env_present_is_refused(gate):
    wt, repo, job, env, calls, script = gate
    (job / ".env").write_text(CONSTRUCTED_ENV)
    done = run_gate(env, "livenote")
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert read_calls(calls) == []
    assert (job / ".env").read_text() == CONSTRUCTED_ENV  # not ours to remove


def test_livenote_runs_the_hub_command_and_reads_its_skips(gate):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "livenote")
    assert done.returncode == 0, done.stdout + done.stderr
    (call,) = read_calls(calls)
    cenv, argv = argv_of(hub_commands()["livenote"])
    assert call["argv"] == argv
    assert call["COBALT_LIVE_VAULT_ROOT"] == cenv["COBALT_LIVE_VAULT_ROOT"]
    assert call["COBALT_ENV"] is None
    assert "live-note 5/0" in done.stdout.splitlines()
    calls.unlink()
    set_script(script, pytest=[{"out": "SKIPPED [1] tests/x.py:1: COBALT_LIVE_VAULT_ROOT not set\n4 passed, 1 skipped in 0.1s", "rc": 0}])
    done = run_gate(env, "livenote")
    assert done.returncode == 1, done.stdout + done.stderr


def test_offline_makes_one_pytest_call_with_no_cobalt_env(gate):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "offline")
    assert done.returncode == 0, done.stdout + done.stderr
    (call,) = read_calls(calls)
    assert call["argv"] == argv_of(hub_commands()["offline"])[1]
    assert call["COBALT_ENV"] is None
    assert "offline 5/0" in done.stdout.splitlines()


def test_offline_reads_a_coloured_summary(gate):
    wt, repo, job, env, calls, script = gate
    set_script(script, pytest=[{"out": "\x1b[32m3784 passed\x1b[0m, \x1b[33m673 skipped\x1b[0m in 645.49s", "rc": 0}])
    done = run_gate(env, "offline")
    assert done.returncode == 0, done.stdout + done.stderr
    assert "offline 3784/0" in done.stdout.splitlines()


def test_probe_takes_reads_and_releases(gate):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "probe")
    assert done.returncode == 0, done.stdout + done.stderr
    assert [kind(c) for c in read_calls(calls)] == ["fp", "proof"]
    assert not (job / ".env").exists()
    assert ".env: removed" in done.stdout


def test_tickers_left_behind_are_a_decision_and_the_rollback_still_runs(gate):
    wt, repo, job, env, calls, script = gate
    set_script(script, tickers="ticker\tcount\nZZTA\t2\n")
    done = run_gate(env, "withdb", "--tickers", "ZZTA,ZZTB")
    assert done.returncode == 1, done.stdout + done.stderr
    log = read_calls(calls)
    (q,) = [c for c in log if kind(c) == "tickers"]
    assert "WHERE ticker IN ('ZZTA','ZZTB') GROUP BY ticker" in q["argv"][-1]
    assert [kind(c) for c in log][-2:] == ["rollback", "fp"]
    assert "DECISION 0: the suite left ZZTA rows on cobalt_dev" in done.stdout
    assert not (job / ".env").exists()


def test_migration_runs_forward_and_back_twice(gate):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "withdb", "--migration")
    assert done.returncode == 0, done.stdout + done.stderr
    kinds = [kind(c) for c in read_calls(calls)]
    assert kinds[-3:] == ["forward", "rollback", "fp"]
    assert kinds.count("forward") == 2 and kinds.count("rollback") == 2
    assert "forward, back, forward, back — F = F0 twice" in done.stdout


def test_a_term_mid_pass_2_still_rolls_back_and_releases(gate, tmp_path):
    wt, repo, job, env, calls, script = gate
    marker = tmp_path / "pass2-started"
    set_script(script, pytest=[
        {"out": "5 passed in 0.1s", "rc": 0},
        {"out": "5 passed in 0.1s", "rc": 0, "marker": str(marker), "sleep": 3},
    ])
    proc = subprocess.Popen(["sh", str(GATE), NAME, "withdb"], env=env,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for _ in range(600):
        if marker.exists():
            break
        time.sleep(0.1)
    assert marker.exists()
    proc.send_signal(signal.SIGTERM)
    out, err = proc.communicate(timeout=120)
    assert proc.returncode != 0, out + err
    assert [kind(c) for c in read_calls(calls)][-2:] == ["rollback", "fp"]
    assert not (job / ".env").exists()


def test_all_runs_offline_withdb_livenote_in_order(gate):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "all")
    assert done.returncode == 0, done.stdout + done.stderr
    log = read_calls(calls)
    pytests = [c for c in log if kind(c) == "pytest"]
    assert [c["COBALT_ENV"] for c in pytests] == [None, "dev", "dev", None]
    assert pytests[-1]["COBALT_LIVE_VAULT_ROOT"] is not None
    out = done.stdout.splitlines()
    for line in ("offline 5/0", "with-DB 10/0", "live-note 5/0", "cobalt_dev: 0013 — F2 = F0", ".env: removed"):
        assert line in out, (line, done.stdout)


def lock_scripts(tmp_path: Path, take_exit: int) -> Path:
    """gate.sh copied beside stub take/release scripts that record their arguments."""
    ops = tmp_path / "ops"
    ops.mkdir()
    shutil.copy(GATE, ops / "gate.sh")
    rec = tmp_path / "lock-calls"
    (ops / "take-devdb-lock.sh").write_text(
        f'printf "take %s\\n" "$*" >> "{rec}"\n'
        f'[ {take_exit} -eq 0 ] || exit {take_exit}\n'
        'cp "$COBALT_REPO_ROOT/.env" "$COBALT_WT_ROOT/$1/.env"\n'
    )
    (ops / "release-devdb-lock.sh").write_text(
        f'printf "release %s\\n" "$*" >> "{rec}"\nrm -f "$COBALT_WT_ROOT/$1/.env"\nprintf "lock released\\n"\n'
    )
    return ops


def test_the_lock_scripts_beside_it_are_used_when_both_exist(gate, tmp_path):
    wt, repo, job, env, calls, script = gate
    ops = lock_scripts(tmp_path, 0)
    done = run_gate(env, "withdb", gate=ops / "gate.sh")
    assert done.returncode == 0, done.stdout + done.stderr
    assert (tmp_path / "lock-calls").read_text().splitlines() == [f"take {NAME} 90", f"release {NAME}"]
    assert not (job / ".env").exists()


def test_a_lock_script_that_says_not_free_exits_4(gate, tmp_path):
    wt, repo, job, env, calls, script = gate
    ops = lock_scripts(tmp_path, 4)
    done = run_gate(env, "withdb", gate=ops / "gate.sh")
    assert done.returncode == 4, done.stdout + done.stderr
    assert read_calls(calls) == []
    assert not (job / ".env").exists()


@pytest.mark.parametrize("args", [
    [], ["withdb"], [NAME, "nope"], [NAME, "withdb", "--deselect"], [NAME, "withdb", "--deselect", "a;b"],
    [NAME, "withdb", "--tickers", "a'b"], [NAME, "offline", "--migration"], ["../x", "offline"],
])
def test_a_bad_call_is_refused(gate, args):
    wt, repo, job, env, calls, script = gate
    done = subprocess.run(["sh", str(GATE), *args], env=env, capture_output=True, text=True, timeout=60)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith("REFUSED: ")
    assert read_calls(calls) == []
