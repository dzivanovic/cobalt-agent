"""ops/desk/gate.sh — BUILD-HUB.md `## W`'s three suites in one call (card 19 worker-steps S3;
card 2026-10-03/03 adoption-scripts L2: the commands and the level from ops/desk/gate-lists.md).

No run here touches cobalt_dev. A stub `uv` on PATH appends its argument list and the
COBALT_ENV / COBALT_LIVE_VAULT_ROOT it saw to a call log and answers from a per-test
script (canned pytest summaries, a canned fingerprint row, a canned proof-only output).
A tmp directory stands in for /Users/cobalt/cobalt-wt (COBALT_WT_ROOT) and holds the job
worktree with a copy of THIS tree's ops/desk/gate-lists.md and NO hub file; a tmp repo
stands in for /Users/cobalt/cobalt (COBALT_REPO_ROOT) and holds a constructed `.env`.
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
LISTS = REPO / "ops" / "desk" / "gate-lists.md"
HUB = REPO / "docs" / "40 - DevDocs" / "prompts" / "BUILD-HUB.md"
DEPLOY_HUB = REPO / "docs" / "40 - DevDocs" / "prompts" / "DEPLOY-HUB.md"
CONSTRUCTED_ENV = "COBALT_TEST_CONSTRUCTED=1\n"
NAME = "x-job"

FP_ROW = "cols\trels\tviews_md5\n664\t35\t0123456789abcdef0123456789abcdef\n"
FP_OTHER = "cols\trels\tviews_md5\n670\t36\tfedcba9876543210fedcba9876543210\n"
# the two level lines of gate-lists.md `## LEVEL 0013` (L1 prints them last on --proof-only)
TABLES_LINE = "TABLES 0011"
FINGERPRINT_LINE = "FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87"
PROOF_HEAD = (
    "cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)\n\n"
    "table  side  schema  rows  digest  secs\n"
    "legs   user  -       -     -       0.00\n"
    "NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.\n"
    "code: 0000000 (clean) · /constructed\n"
)
PROOF = PROOF_HEAD + FINGERPRINT_LINE + "\n" + TABLES_LINE + "\n"

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
    rcs = script.get("fp_rc", [])
    if k < len(rcs) and rcs[k]:
        print("stub uv: the query failed", file=sys.stderr)
        sys.exit(rcs[k])
    sys.stdout.write(fps[k] if k < len(fps) else fps[-1])
    sys.exit(0)
if "query" in argv:
    sys.stdout.write(script.get("tickers", "ticker\tcount\n"))
    sys.exit(0)
if "--proof-only" in argv:
    proofs = script.get("proofs") or [script.get("proof", "")]
    k = nth(lambda a: "--proof-only" in a)
    sys.stdout.write(proofs[k] if k < len(proofs) else proofs[-1])
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


#: gate-lists.md section → the key both readers use
LIST_KEYS = {
    "OFFLINE": "offline", "PROOF ONLY": "proof", "PASS 1": "pass1", "FORWARD": "forward",
    "PASS 2": "pass2", "STRAY ROWS": "tickers", "LIVE-NOTE": "livenote", "ROLLBACK": "rollback",
    "FINGERPRINT": "fp", "ALLOWED SKIPS": "skips", "LEVEL 0013": "level",
}


def list_commands(path: Path = LISTS) -> dict[str, str]:
    """The ONE backticked line under each `## <name>` of gate-lists.md, read here
    independently of gate.sh so the two can be compared."""
    out: dict[str, str] = {}
    title = None
    for line in path.read_text().splitlines():
        if line.startswith("## "):
            title = line[3:].strip()
            continue
        if title in LIST_KEYS and line.strip():
            assert LIST_KEYS[title] not in out, f"## {title} holds more than one line"
            spans = re.findall(r"`([^`]*)`", line)
            assert len(spans) == 1 and line.strip() == f"`{spans[0]}`", line
            out[LIST_KEYS[title]] = spans[0]
    assert set(out) == set(LIST_KEYS.values()), sorted(set(LIST_KEYS.values()) - set(out))
    return out


def hub_commands() -> dict[str, str]:
    """The commands BUILD-HUB.md `## W` and `## THE LOCK` tell a worker to type, read here
    independently of gate.sh so the two can be compared."""
    text = HUB.read_text().splitlines()
    out: dict[str, str] = {}

    def put(key: str, found: list[str]) -> None:
        if found:
            out[key] = found[0]

    def spans(line: str) -> list[str]:
        return re.findall(r"`([^`]*)`", line)

    for i, line in enumerate(text):
        nxt = text[i + 1] if i + 1 < len(text) else ""
        if line.startswith("- (c) PASS 1"):
            put("pass1", [nxt.strip("`")] if nxt.startswith("`COBALT_ENV=dev uv run pytest ") else [])
        if line.startswith("- (c3) PASS 2"):
            put("pass2", [nxt.strip("`")] if nxt.startswith("`COBALT_ENV=dev uv run pytest ") else [])
        if line.startswith("- (a) OFFLINE"):
            put("offline", [s for s in spans(line) if s.startswith("uv run pytest ")])
        if line.startswith("- (e) LIVE-NOTE"):
            put("livenote", [s for s in spans(line) if s.startswith("COBALT_LIVE") and " uv run pytest " in s])
        if line.startswith("- (f) ALWAYS"):
            put("rollback", [s for s in spans(line) if s.startswith("COBALT_ENV=dev uv run cobalt db migrate --rollback")])
        if line.startswith("- (c2) FORWARD"):
            put("forward", [s for s in spans(line) if s == "COBALT_ENV=dev uv run cobalt db migrate"])
        if line.startswith("- (b) THE LOCK"):
            put("proof", [s for s in spans(line) if "--proof-only" in s])
        if line.startswith("`COBALT_ENV=dev uv run cobalt db query --side user \"SELECT (SELECT"):
            out["fp"] = line.strip("`")
        if line.startswith("- (c3r) "):
            put("tickers", [s for s in spans(line) if "SELECT ticker" in s])
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
    (job / "ops" / "desk").mkdir(parents=True)
    shutil.copy(LISTS, job / "ops" / "desk" / "gate-lists.md")
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


WITHDB_KINDS = ["fp", "proof", "pytest", "forward", "fp", "pytest", "rollback", "fp", "proof"]


def test_withdb_green_runs_the_lists_commands_byte_for_byte_in_order(gate):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "withdb")
    assert done.returncode == 0, done.stdout + done.stderr
    log = read_calls(calls)
    assert [kind(c) for c in log] == WITHDB_KINDS
    lists = list_commands()
    expect = [lists["fp"], lists["proof"], lists["pass1"], lists["forward"], lists["fp"], lists["pass2"],
              lists["rollback"], lists["fp"], lists["proof"]]
    for call, command in zip(log, expect):
        cenv, argv = argv_of(command)
        assert call["argv"] == argv, (call["argv"], command)
        assert call["COBALT_ENV"] == cenv.get("COBALT_ENV") == "dev"
    assert not (job / ".env").exists()
    out = done.stdout.splitlines()
    assert "LEVEL 0013" in out
    assert "with-DB 10/0" in out
    assert "cobalt_dev: 0013 — F2 = F0" in out
    assert ".env: removed" in out
    assert any(line.startswith(f"log: {wt / '.gate-logs' / NAME}-withdb-") for line in out)


def test_the_hub_holds_no_gate_command_and_points_at_the_lists_file():
    """Card 2026-10-03/02 adoption-hubs A1 replaced the hub lines with a reference to
    gate-lists.md: BUILD-HUB.md `## W` types none of the commands gate.sh runs and names the
    PASS 1 and PASS 2 commands of ops/desk/gate-lists.md. THE LOCK keeps `<FP>` for a step that
    takes the lock by hand (E2's with-DB red): that one stays byte-equal to the lists file. The
    allowed-skip set is DEPLOY-HUB.md's."""
    lists, hub = list_commands(), hub_commands()
    assert sorted(hub) == ["fp"], sorted(hub)
    assert lists["fp"] == hub["fp"]
    w = HUB.read_text().split("\n## W ", 1)[1].split("\n## ", 1)[0]
    assert "sh /Users/cobalt/cobalt/ops/desk/gate.sh <WORKTREE> all" in w
    assert "the PASS 1 and PASS 2 commands of `ops/desk/gate-lists.md`" in w
    for key in ("pass1", "pass2"):
        assert lists[key] not in HUB.read_text(), key
    (gate_line,) = [ln for ln in DEPLOY_HUB.read_text().splitlines() if "every SKIPPED line inside the allowed set" in ln]
    for item in lists["skips"].split(" · "):
        for word in item.split():
            # DEPLOY-HUB.md writes a second line of one file as `:401`
            for part in word.split(":"):
                assert part in gate_line, (item, part)
    assert lists["level"] == f"{TABLES_LINE} · {FINGERPRINT_LINE}"


def test_the_hub_file_is_no_longer_read_a_moved_pass_1_is_what_runs(gate):
    wt, repo, job, env, calls, script = gate
    assert not (job / "docs").exists()
    path = job / "ops" / "desk" / "gate-lists.md"
    moved = list_commands()["pass1"] + " --deselect tests/cobalt/test_moved.py"
    path.write_text(path.read_text().replace(f"`{list_commands()['pass1']}`", f"`{moved}`"))
    done = run_gate(env, "withdb")
    assert done.returncode == 0, done.stdout + done.stderr
    pytests = [c["argv"] for c in read_calls(calls) if kind(c) == "pytest"]
    assert pytests[0] == argv_of(moved)[1]


@pytest.mark.parametrize("proof, read", [
    (PROOF_HEAD + FINGERPRINT_LINE + "\nTABLES 0016\n", "TABLES 0016"),
    (PROOF_HEAD + FINGERPRINT_LINE + "\nTABLES MIXED — present above: 0017 · absent below: 0016\n",
     "TABLES MIXED — present above: 0017 · absent below: 0016"),
    (PROOF_HEAD + FINGERPRINT_LINE.replace("rels 35", "rels 36") + "\n" + TABLES_LINE + "\n",
     FINGERPRINT_LINE.replace("rels 35", "rels 36")),
    (PROOF_HEAD + TABLES_LINE + "\n", "(no FINGERPRINT line)"),
])
def test_level_lines_other_than_the_lists_exit_5_and_no_pass_runs(gate, proof, read):
    wt, repo, job, env, calls, script = gate
    set_script(script, proof=proof)
    done = run_gate(env, "withdb")
    assert done.returncode == 5, done.stdout + done.stderr
    assert [kind(c) for c in read_calls(calls)] == ["fp", "proof"]
    assert read in done.stdout
    assert "LEVEL 0013" not in done.stdout.splitlines()
    assert not (job / ".env").exists()


def test_level_lines_that_differ_after_the_rollback_exit_6(gate):
    wt, repo, job, env, calls, script = gate
    set_script(script, proofs=[PROOF, PROOF_HEAD + FINGERPRINT_LINE + "\nTABLES 0016\n"])
    done = run_gate(env, "withdb")
    assert done.returncode == 6, done.stdout + done.stderr
    assert [kind(c) for c in read_calls(calls)] == WITHDB_KINDS
    assert "cobalt_dev NOT back at 0013" in done.stdout
    assert "TABLES 0016" in done.stdout
    assert not (job / ".env").exists()


def test_a_pass_1_skip_outside_the_allowed_set_is_marked(gate):
    wt, repo, job, env, calls, script = gate
    set_script(script, pytest=[
        {"out": "SKIPPED [1] tests/cobalt/test_cards_picks.py:388: constructed\n"
                "SKIPPED [1] tests/cobalt/test_other.py:7: constructed\n4 passed, 2 skipped in 0.1s", "rc": 0},
    ])
    done = run_gate(env, "withdb")
    assert done.returncode == 0, done.stdout + done.stderr
    out = done.stdout.splitlines()
    assert "SKIPPED [1] tests/cobalt/test_cards_picks.py:388: constructed" in out
    assert "OUTSIDE the allowed set: SKIPPED [1] tests/cobalt/test_other.py:7: constructed" in out


def test_a_deselect_goes_into_pass_1_and_its_id_at_the_end_of_pass_2(gate):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "withdb", "--deselect", "x::y")
    assert done.returncode == 0, done.stdout + done.stderr
    pytests = [c["argv"] for c in read_calls(calls) if kind(c) == "pytest"]
    lists = list_commands()
    assert pytests[0] == argv_of(lists["pass1"])[1] + ["--deselect", "x::y"]
    assert pytests[1] == argv_of(lists["pass2"])[1] + ["x::y"]


def test_pass_2_red_still_rolls_back_and_releases(gate):
    wt, repo, job, env, calls, script = gate
    set_script(script, pytest=[
        {"out": "5 passed in 0.1s", "rc": 0},
        {"out": "FAILED tests/cobalt/test_legs_db.py::test_x - assert 1 == 2\n1 failed, 4 passed in 0.1s", "rc": 1},
    ])
    done = run_gate(env, "withdb")
    assert done.returncode == 1, done.stdout + done.stderr
    kinds = [kind(c) for c in read_calls(calls)]
    assert kinds == WITHDB_KINDS
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


def test_a_failed_fingerprint_at_the_start_stops_and_releases(gate):
    wt, repo, job, env, calls, script = gate
    set_script(script, fp_rc=[1])
    done = run_gate(env, "withdb")
    assert done.returncode == 1, done.stdout + done.stderr
    assert [kind(c) for c in read_calls(calls)] == ["fp"]
    assert "the fingerprint query failed" in done.stdout
    assert not (job / ".env").exists()


def test_a_failed_fingerprint_after_the_forward_still_rolls_back(gate):
    wt, repo, job, env, calls, script = gate
    set_script(script, fp_rc=[0, 1])
    done = run_gate(env, "withdb")
    assert done.returncode == 1, done.stdout + done.stderr
    assert [kind(c) for c in read_calls(calls)] == ["fp", "proof", "pytest", "forward", "fp", "rollback", "fp", "proof"]
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
    cenv, argv = argv_of(list_commands()["livenote"])
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
    assert call["argv"] == argv_of(list_commands()["offline"])[1]
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
    assert [kind(c) for c in log][-3:] == ["rollback", "fp", "proof"]
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
    assert [kind(c) for c in read_calls(calls)][-3:] == ["rollback", "fp", "proof"]
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


# ---- card 03c M2: the gate WAITS — the take script's retry is the wait -------------------------


def waiting_lock_scripts(tmp_path: Path, calls: Path, free_on_try: int, budget: int) -> Path:
    """gate.sh beside a stub take script that retries like take-devdb-lock.sh: while the
    sibling `beta/.env` exists it records `try <n> held`; on try `free_on_try` the holder has
    let go (the sibling .env is gone); after `budget` held tries it exits 4. It records
    `uv before the lock` when any uv call was logged before it started."""
    ops = tmp_path / "ops"
    ops.mkdir()
    shutil.copy(GATE, ops / "gate.sh")
    rec = tmp_path / "lock-calls"
    sibling = '"$COBALT_WT_ROOT/beta/.env"'
    (ops / "take-devdb-lock.sh").write_text(
        f'printf "take %s\\n" "$*" >> "{rec}"\n'
        f'[ ! -e "{calls}" ] || printf "uv before the lock\\n" >> "{rec}"\n'
        'n=1\n'
        'while :; do\n'
        f'    [ "$n" -lt {free_on_try} ] || rm -f {sibling}\n'
        f'    [ -e {sibling} ] || break\n'
        f'    printf "try %s held\\n" "$n" >> "{rec}"\n'
        f'    [ "$n" -lt {budget} ] || {{ printf "cobalt_dev lock not free in 0 min (held by beta)\\n" >&2; exit 4; }}\n'
        '    n=$((n + 1))\n'
        'done\n'
        'cp "$COBALT_REPO_ROOT/.env" "$COBALT_WT_ROOT/$1/.env"\n'
        'printf "lock taken: %s\\n" "$1"\n'
    )
    (ops / "release-devdb-lock.sh").write_text(
        f'printf "release %s\\n" "$*" >> "{rec}"\nrm -f "$COBALT_WT_ROOT/$1/.env"\nprintf "lock released\\n"\n'
    )
    return ops


def test_m2_a_sibling_env_that_goes_on_the_second_try_is_waited_for(gate, tmp_path):
    wt, repo, job, env, calls, script = gate
    (wt / "beta" / ".env").write_text(CONSTRUCTED_ENV)
    ops = waiting_lock_scripts(tmp_path, calls, free_on_try=2, budget=90)
    done = run_gate(env, "withdb", gate=ops / "gate.sh")
    assert done.returncode == 0, done.stdout + done.stderr
    assert (tmp_path / "lock-calls").read_text().splitlines() == [
        f"take {NAME} 90", "try 1 held", f"release {NAME}"]
    assert [kind(c) for c in read_calls(calls)] == WITHDB_KINDS
    out = done.stdout.splitlines()
    assert "lock: waited 0 min" in out
    assert "with-DB 10/0" in out
    assert not (job / ".env").exists()


def test_m2_a_lock_never_free_exits_4_after_the_take_scripts_budget_and_runs_no_uv(gate, tmp_path):
    wt, repo, job, env, calls, script = gate
    (wt / "beta" / ".env").write_text(CONSTRUCTED_ENV)
    ops = waiting_lock_scripts(tmp_path, calls, free_on_try=99, budget=3)
    done = run_gate(env, "withdb", gate=ops / "gate.sh")
    assert done.returncode == 4, done.stdout + done.stderr
    rec = tmp_path / "lock-calls"
    assert (rec.read_text().splitlines() if rec.exists() else []) == [
        f"take {NAME} 90", "try 1 held", "try 2 held", "try 3 held"], done.stdout
    assert read_calls(calls) == []
    assert "cobalt_dev lock not free (take-devdb-lock.sh exit 4)" in done.stdout
    assert not (job / ".env").exists()
    assert (wt / "beta" / ".env").read_text() == CONSTRUCTED_ENV


def test_m2_no_lock_scripts_beside_the_gate_is_refused_before_any_uv_call(gate, tmp_path):
    """The lock is taken ONLY by take-devdb-lock.sh: no `cp .env` way is left (CHECK ASK X1)."""
    wt, repo, job, env, calls, script = gate
    ops = tmp_path / "ops"
    ops.mkdir()
    shutil.copy(GATE, ops / "gate.sh")
    for mode in ("withdb", "all", "probe"):
        done = run_gate(env, mode, gate=ops / "gate.sh")
        assert done.returncode == 1, done.stdout + done.stderr
        assert done.stderr.startswith("REFUSED: "), done.stderr
        assert read_calls(calls) == []
        assert not (job / ".env").exists()


# ---- card 03c M3: the deploy's whole pass 1 ---------------------------------------------------


def without_db_only(command: str) -> str:
    assert command.split(" ").count("--db-only") == 1
    return command.replace(" --db-only", "", 1)


def test_m3_deploy_runs_pass_1_without_db_only(gate):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "all", "--deploy")
    assert done.returncode == 0, done.stdout + done.stderr
    pytests = [c["argv"] for c in read_calls(calls) if kind(c) == "pytest"]
    lists = list_commands()
    assert pytests[1] == argv_of(without_db_only(lists["pass1"]))[1]
    assert "--db-only" not in pytests[1]
    assert pytests[2] == argv_of(lists["pass2"])[1]
    assert "pass 1: whole (deploy)" in done.stdout.splitlines()


def test_m3_without_deploy_pass_1_keeps_db_only(gate):
    """Negative control: a build's or a check's gate never loses the option."""
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "all")
    assert done.returncode == 0, done.stdout + done.stderr
    pytests = [c["argv"] for c in read_calls(calls) if kind(c) == "pytest"]
    assert pytests[1] == argv_of(list_commands()["pass1"])[1]
    assert "--db-only" in pytests[1]
    assert "pass 1: whole (deploy)" not in done.stdout


def test_m3_deploy_with_a_deselect_strips_only_the_option(gate):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, "withdb", "--deploy", "--deselect", "x::y")
    assert done.returncode == 0, done.stdout + done.stderr
    pytests = [c["argv"] for c in read_calls(calls) if kind(c) == "pytest"]
    assert pytests[0] == argv_of(without_db_only(list_commands()["pass1"]))[1] + ["--deselect", "x::y"]


@pytest.mark.parametrize("mode", ["offline", "livenote", "probe"])
def test_m3_deploy_outside_withdb_and_all_is_refused(gate, mode):
    wt, repo, job, env, calls, script = gate
    done = run_gate(env, mode, "--deploy")
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith("REFUSED: ")
    assert read_calls(calls) == []


def test_m3_deploy_on_a_pass_1_without_db_only_is_refused_before_any_uv_call(gate):
    """L1: the one token to strip is missing — refused loud, never run as it stands."""
    wt, repo, job, env, calls, script = gate
    path = job / "ops" / "desk" / "gate-lists.md"
    pass1 = list_commands()["pass1"]
    path.write_text(path.read_text().replace(f"`{pass1}`", f"`{without_db_only(pass1)}`"))
    done = run_gate(env, "all", "--deploy")
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith("REFUSED: ")
    assert read_calls(calls) == []


def test_check_o1_a_warning_line_before_the_fingerprint_does_not_hide_a_changed_f2(gate):
    wt, repo, job, env, calls, script = gate
    warn = "warning: `VIRTUAL_ENV=/x` does not match the project environment path `.venv` and will be ignored\n"
    set_script(script, fp=[warn + FP_ROW, warn + FP_ROW, warn + FP_OTHER])
    done = run_gate(env, "withdb")
    assert done.returncode == 6, done.stdout + done.stderr
    assert "cobalt_dev NOT back at 0013" in done.stdout
    assert not (job / ".env").exists()


def test_check_o2_a_term_during_the_lock_take_still_releases(gate, tmp_path):
    wt, repo, job, env, calls, script = gate
    ops = tmp_path / "ops"
    ops.mkdir()
    shutil.copy(GATE, ops / "gate.sh")
    rec = tmp_path / "lock-calls"
    marker = tmp_path / "take-started"
    (ops / "take-devdb-lock.sh").write_text(
        f'printf "take %s\\n" "$*" >> "{rec}"\n'
        f': > "{marker}"\n'
        'sleep 2\n'
        'cp "$COBALT_REPO_ROOT/.env" "$COBALT_WT_ROOT/$1/.env"\n'
    )
    (ops / "release-devdb-lock.sh").write_text(
        f'printf "release %s\\n" "$*" >> "{rec}"\nrm -f "$COBALT_WT_ROOT/$1/.env"\n'
    )
    proc = subprocess.Popen(["sh", str(ops / "gate.sh"), NAME, "withdb"], env=env,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for _ in range(600):
        if marker.exists():
            break
        time.sleep(0.1)
    assert marker.exists()
    proc.send_signal(signal.SIGTERM)
    out, err = proc.communicate(timeout=120)
    assert proc.returncode != 0, out + err
    assert read_calls(calls) == []
    assert not (job / ".env").exists(), out + err
    assert rec.read_text().splitlines() == [f"take {NAME} 90", f"release {NAME}"]


def test_check_o3_offline_runs_with_no_cobalt_env_even_when_the_caller_has_one(gate):
    wt, repo, job, env, calls, script = gate
    env = dict(env, COBALT_ENV="dev", COBALT_LIVE_VAULT_ROOT="/nowhere")
    done = run_gate(env, "offline")
    assert done.returncode == 0, done.stdout + done.stderr
    (call,) = read_calls(calls)
    assert call["COBALT_ENV"] is None
    assert call["COBALT_LIVE_VAULT_ROOT"] is None


def test_l3_an_accented_worktree_name_is_refused_under_a_utf8_locale(gate):
    """Card 03 L3: `[!A-Za-z0-9._-]` admits `é` under en_US.UTF-8 unless the script runs LC_ALL=C."""
    wt, repo, job, env, calls, script = gate
    (wt / "x-jobé" / "ops" / "desk").mkdir(parents=True)
    shutil.copy(LISTS, wt / "x-jobé" / "ops" / "desk" / "gate-lists.md")
    env = dict(env, LC_ALL="en_US.UTF-8", LANG="en_US.UTF-8")
    done = subprocess.run(["sh", str(GATE), "x-jobé", "offline"], env=env, capture_output=True, text=True, timeout=60)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: worktree 'x-jobé' is not one directory name" in done.stderr
    assert read_calls(calls) == []


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
