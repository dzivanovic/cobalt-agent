"""Card 547 db-copy (his R1471): each with-DB step on its own throwaway copy of cobalt_dev.

E1 `ops/desk/devdb-copy-env.sh`, G1 `ops/desk/gate.sh` copy mode, L1 `desk-launch.sh` `lock_free`,
D1 the `gate-lists.md` header paragraph, H1 the `BUILD-HUB.md` W (b) line and the no-clutter pin.

No run here touches a database. A tmp directory stands in for /Users/cobalt/cobalt-wt
(COBALT_WT_ROOT) and a tmp repo for /Users/cobalt/cobalt (COBALT_REPO_ROOT) holding a constructed
`.env`; the real one is never read. The gate runs from a tmp copy beside the real lock scripts and
the new devdb-copy-env.sh, with a stub `uv` that logs every call (the shape of
tests/ops/test_gate.py, rebuilt here, not imported).
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import time
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
DESK = REPO / "ops" / "desk"
GATE = DESK / "gate.sh"
TAKE = DESK / "take-devdb-lock.sh"
RELEASE = DESK / "release-devdb-lock.sh"
COPY_ENV = DESK / "devdb-copy-env.sh"
LAUNCH = DESK / "desk-launch.sh"
LISTS = DESK / "gate-lists.md"
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"
NO_CLUTTER_TEST = REPO / "tests" / "ops" / "test_build_hub_no_clutter.py"
LOCK_NAME = ".cobalt_dev.lock"
MARKS = ".devdb-copies"
CONSTRUCTED_ENV = "COBALT_TEST_CONSTRUCTED=1\n"
NAME = "x-job"
COPY = "cobalt_dev_x_job"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}


# ---- E1: devdb-copy-env.sh ----------------------------------------------------------------------


@pytest.fixture
def roots(tmp_path):
    wt = tmp_path / "wt"
    repo = tmp_path / "repo"
    wt.mkdir()
    repo.mkdir()
    (repo / ".env").write_text(CONSTRUCTED_ENV)
    for name in ("alpha", "beta"):
        (wt / name).mkdir()
    env = dict(os.environ, COBALT_WT_ROOT=str(wt), COBALT_REPO_ROOT=str(repo))
    env.pop("COBALT_DEV_DB_NAME", None)
    return wt, repo, env


def run(script: Path, *args: str, env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(script), *args], env=env, capture_output=True, text=True, timeout=300
    )


def test_e1_place_copies_the_env_by_name_and_writes_the_marker(roots):
    wt, repo, env = roots
    done = run(COPY_ENV, "place", "alpha", env=dict(env, COBALT_DEV_DB_NAME="cobalt_dev_alpha"))
    assert done.returncode == 0, done.stdout + done.stderr
    assert (wt / "alpha" / ".env").read_text() == CONSTRUCTED_ENV
    assert (wt / MARKS / "alpha").read_text().strip() == "cobalt_dev_alpha"
    assert not (wt / LOCK_NAME).exists()


def test_e1_remove_takes_the_env_and_the_marker_and_nothing_else(roots):
    wt, repo, env = roots
    (wt / "beta" / ".env").write_text("held-by-beta\n")
    (wt / LOCK_NAME).mkdir()
    (wt / LOCK_NAME / "owner").write_text("beta\n")
    placed = run(COPY_ENV, "place", "alpha", env=dict(env, COBALT_DEV_DB_NAME="cobalt_dev_alpha"))
    assert placed.returncode == 0, placed.stdout + placed.stderr
    done = run(COPY_ENV, "remove", "alpha", env=env)
    assert done.returncode == 0, done.stdout + done.stderr
    assert "copy env removed" in done.stdout
    assert not (wt / "alpha" / ".env").exists()
    assert not (wt / MARKS / "alpha").exists()
    assert (wt / "beta" / ".env").read_text() == "held-by-beta\n"
    assert (wt / LOCK_NAME / "owner").read_text() == "beta\n"


@pytest.mark.parametrize(
    "bad",
    ["cobalt_dev", "cobalt_brain", "cobalt_dev_", "cobalt_dev_A", "cobalt_dev_a-b",
     "cobalt_dev_" + "a" * 40, None],
)
def test_e1_a_name_outside_the_pattern_is_refused_and_nothing_is_touched(roots, bad):
    wt, repo, env = roots
    if bad is not None:
        env = dict(env, COBALT_DEV_DB_NAME=bad)
    done = run(COPY_ENV, "place", "alpha", env=env)
    assert done.returncode == 2, done.stdout + done.stderr
    assert not (wt / "alpha" / ".env").exists()
    assert not (wt / MARKS).exists()


def test_e1_the_longest_name_the_pattern_allows_is_placed(roots):
    """Negative control of the 50-in-all bound: 39 characters after `cobalt_dev_` pass."""
    wt, repo, env = roots
    name = "cobalt_dev_" + "a" * 39
    assert len(name) == 50
    done = run(COPY_ENV, "place", "alpha", env=dict(env, COBALT_DEV_DB_NAME=name))
    assert done.returncode == 0, done.stdout + done.stderr
    assert (wt / MARKS / "alpha").read_text().strip() == name


@pytest.mark.parametrize("bad", [".x", "a/b", ""])
def test_e1_a_bad_worktree_name_is_refused(roots, bad):
    wt, repo, env = roots
    (wt / "a" / "b").mkdir(parents=True)
    for verb in ("place", "remove"):
        done = run(COPY_ENV, verb, bad, env=dict(env, COBALT_DEV_DB_NAME="cobalt_dev_alpha"))
        assert done.returncode == 2, (verb, done.stdout + done.stderr)
    assert not (wt / MARKS).exists()


# ---- G1: gate.sh copy mode ------------------------------------------------------------------------

FP_ROW = "cols\trels\tviews_md5\n664\t35\t0123456789abcdef0123456789abcdef\n"
TABLES_LINE = "TABLES 0011"
FINGERPRINT_LINE = "FINGERPRINT cols 664 · rels 35 · views_md5 272c95bbb12241e3611e4b36326ccf87"

UV_STUB = r'''#!/usr/bin/env python3
import json, os, sys, time
argv = sys.argv[1:]
log = os.environ["GATE_STUB_LOG"]
wt = os.environ["COBALT_WT_ROOT"]
with open(log, "a") as f:
    f.write(json.dumps({"argv": argv, "COBALT_ENV": os.environ.get("COBALT_ENV"),
                        "COBALT_DEV_DB_NAME": os.environ.get("COBALT_DEV_DB_NAME"),
                        "lock": os.path.isdir(os.path.join(wt, ".cobalt_dev.lock"))}) + "\n")
script = json.load(open(os.environ["GATE_STUB_SCRIPT"]))
calls = [json.loads(l)["argv"] for l in open(log)]
db = os.environ.get("COBALT_DEV_DB_NAME") or "cobalt_dev"
def nth(kind):
    return sum(1 for a in calls if kind(a)) - 1
is_pytest = lambda a: a[:2] == ["run", "pytest"]
if "dev-copy" in argv:
    verb = argv[argv.index("dev-copy") + 1]
    print("stub uv: dev-copy %s %s" % (verb, argv[-1]))
    sys.exit(script.get("copy_%s_rc" % verb, 0))
if is_pytest(argv):
    answers = script.get("pytest", [])
    k = nth(is_pytest)
    ans = answers[k] if k < len(answers) else {"out": "5 passed in 0.10s", "rc": 0}
    if ans.get("marker"):
        open(ans["marker"], "w").write("started\n")
    if ans.get("wait_for"):
        end = time.time() + 120
        while not os.path.exists(ans["wait_for"]) and time.time() < end:
            time.sleep(0.1)
    print(ans["out"])
    sys.exit(ans["rc"])
if "query" in argv and any("pg_attribute" in x for x in argv):
    sys.stdout.write(script["fp"])
    sys.exit(0)
if "query" in argv:
    sys.stdout.write("ticker\tcount\n")
    sys.exit(0)
if "--proof-only" in argv:
    sys.stdout.write(script["proof"].replace("on cobalt_dev", "on " + db))
    sys.exit(0)
if "--rollback" in argv:
    print("cobalt db migrate — ROLLBACK on " + db)
    sys.exit(0)
if "migrate" in argv:
    print("cobalt db migrate — FORWARD on " + db)
    sys.exit(0)
print("stub uv: unscripted call", argv, file=sys.stderr)
sys.exit(97)
'''

PROOF = (
    "cobalt db migrate — PROOF ONLY on cobalt_dev (READ ONLY, nothing applied)\n\n"
    "table  side  schema  rows  digest  secs\n"
    "legs   user  -       -     -       0.00\n"
    "NOTHING WAS APPLIED: --proof-only ran in a READ ONLY transaction.\n"
    "code: 0000000 (clean) · /constructed\n"
    + FINGERPRINT_LINE + "\n" + TABLES_LINE + "\n"
)

COPY_SECTIONS = (
    "\n## COPY CREATE\n`uv run cobalt db dev-copy create <COPY>`\n"
    "\n## COPY DROP\n`uv run cobalt db dev-copy drop <COPY>`\n"
)

# the verdict lines a withdb run on the one lock prints today (no --tickers, no --deploy)
TODAY = [
    "lock: waited 0 min",
    "proof-only: on cobalt_dev, nothing CHANGED — the table is in the log (W (b))",
    "LEVEL 0013",
    "stray rows: not read (no --tickers given)",
    "cobalt_dev: 0013 — F2 = F0",
    ".env: removed",
    "with-DB 10/0",
]


class Tree:
    def __init__(self, tmp_path: Path):
        self.tmp = tmp_path
        self.wt = tmp_path / "wt"
        self.repo = tmp_path / "repo"
        self.desk = tmp_path / "desk"
        self.bin = tmp_path / "bin"
        for d in (self.wt, self.repo, self.desk, self.bin):
            d.mkdir()
        (self.repo / ".env").write_text(CONSTRUCTED_ENV)
        # the gate copied beside the REAL lock scripts and the new devdb-copy-env.sh
        for src in (GATE, TAKE, RELEASE, COPY_ENV):
            if src.exists():
                shutil.copy(src, self.desk / src.name)
        (self.bin / "uv").write_text(UV_STUB)
        (self.bin / "uv").chmod(0o755)
        # the take's retry is `sleep 60`: a run that waits behind a held lock calls it
        self.slept = tmp_path / "sleep-called"
        (self.bin / "sleep").write_text(f'#!/bin/sh\nprintf "%s\\n" "$*" >> "{self.slept}"\nexit 1\n')
        (self.bin / "sleep").chmod(0o755)

    def worktree(self, name: str, lists: str) -> Path:
        job = self.wt / name
        (job / "ops" / "desk").mkdir(parents=True)
        (job / "ops" / "desk" / "gate-lists.md").write_text(lists)
        return job

    def env(self, tag: str, **script) -> dict:
        data = {"fp": FP_ROW, "proof": PROOF}
        data.update(script)
        (self.tmp / f"script-{tag}.json").write_text(json.dumps(data))
        env = dict(
            os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
            PATH=f"{self.bin}{os.pathsep}{os.environ['PATH']}",
            GATE_STUB_LOG=str(self.tmp / f"calls-{tag}.jsonl"),
            GATE_STUB_SCRIPT=str(self.tmp / f"script-{tag}.json"),
        )
        for k in ("COBALT_ENV", "COBALT_LIVE_VAULT_ROOT", "COBALT_DEV_DB_NAME"):
            env.pop(k, None)
        return env

    def calls(self, tag: str) -> list[dict]:
        log = self.tmp / f"calls-{tag}.jsonl"
        if not log.exists():
            return []
        return [json.loads(line) for line in log.read_text().splitlines()]

    def gate(self, name: str, env: dict) -> subprocess.CompletedProcess:
        return subprocess.run(
            ["sh", str(self.desk / "gate.sh"), name, "withdb"], env=env,
            capture_output=True, text=True, timeout=300,
        )

    def popen(self, name: str, env: dict) -> subprocess.Popen:
        return subprocess.Popen(
            ["sh", str(self.desk / "gate.sh"), name, "withdb"], env=env,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        )


@pytest.fixture
def tree(tmp_path):
    return Tree(tmp_path)


def copy_lists() -> str:
    return LISTS.read_text() + COPY_SECTIONS


def dev_copy(call: dict) -> str | None:
    a = call["argv"]
    if "dev-copy" in a:
        return " ".join(a[a.index("dev-copy"):])
    return None


def kind(call: dict) -> str:
    a = call["argv"]
    if "dev-copy" in a:
        return dev_copy(call)
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


def assert_nothing_left(tree: Tree, name: str = NAME) -> None:
    assert not (tree.wt / name / ".env").exists()
    assert not (tree.wt / MARKS / name).exists()
    assert not (tree.wt / LOCK_NAME).exists()


def test_g1_copy_mode_creates_runs_on_the_copy_and_drops(tree):
    tree.worktree(NAME, copy_lists())
    done = tree.gate(NAME, tree.env("a"))
    assert done.returncode == 0, done.stdout + done.stderr
    log = tree.calls("a")
    kinds = [kind(c) for c in log]
    assert f"dev-copy drop {COPY}" in kinds and f"dev-copy create {COPY}" in kinds, kinds
    i = kinds.index(f"dev-copy drop {COPY}")
    j = kinds.index(f"dev-copy create {COPY}")
    assert i < j, kinds
    assert kinds[-1] == f"dev-copy drop {COPY}", kinds
    assert kinds.count(f"dev-copy drop {COPY}") == 2, kinds
    assert all(c["COBALT_DEV_DB_NAME"] is None for c in log[: j + 1]), log[: j + 1]
    assert all(c["COBALT_DEV_DB_NAME"] == COPY for c in log[j + 1 : -1]), log[j + 1 : -1]
    assert log[-1]["COBALT_DEV_DB_NAME"] is None
    # the suites run on the copy, with the lock given back
    assert [kind(c) for c in log[j + 1 : -1]] == [
        "fp", "proof", "pytest", "forward", "fp", "pytest", "rollback", "fp", "proof"]
    assert not any(c["lock"] for c in log[j + 1 :]), log
    out = done.stdout.splitlines()
    assert f"copy: {COPY} created" in out
    assert f"copy: {COPY} dropped" in out
    assert "cobalt_dev: 0013 — F2 = F0" in out
    assert "with-DB 10/0" in out
    assert out.count(".env: removed") == 1, out
    assert_nothing_left(tree)


def test_g1_a_second_build_takes_the_lock_while_the_first_runs_on_its_copy(tree):
    tree.worktree(NAME, copy_lists())
    tree.worktree("y-job", copy_lists())
    started = tree.tmp / "first-started"
    go = tree.tmp / "first-go"
    first = tree.popen(NAME, tree.env("a", pytest=[
        {"out": "5 passed in 0.10s", "rc": 0, "marker": str(started), "wait_for": str(go)}]))
    try:
        end = time.monotonic() + 120
        while not started.exists() and first.poll() is None and time.monotonic() < end:
            time.sleep(0.1)
        assert started.exists(), "the first run never reached pass 1"
        assert not (tree.wt / LOCK_NAME).exists()
        assert (tree.wt / NAME / ".env").exists()
        assert (tree.wt / MARKS / NAME).exists()
        second = tree.gate("y-job", tree.env("b"))
        assert second.returncode == 0, second.stdout + second.stderr
        assert not tree.slept.exists(), tree.slept.read_text()
    finally:
        go.write_text("go\n")
        out, err = first.communicate(timeout=300)
    assert first.returncode == 0, out + err
    a = [kind(c) for c in tree.calls("a")]
    b = [kind(c) for c in tree.calls("b")]
    assert f"dev-copy create {COPY}" in a, a
    assert "dev-copy create cobalt_dev_y_job" in b, b
    assert_nothing_left(tree)
    assert_nothing_left(tree, "y-job")


def test_g1_a_create_that_fails_leaves_nothing_and_exits_1(tree):
    tree.worktree(NAME, copy_lists())
    done = tree.gate(NAME, tree.env("a", copy_create_rc=1))
    assert done.returncode == 1, done.stdout + done.stderr
    assert "copy not created" in done.stdout.splitlines()
    log = tree.calls("a")
    assert [kind(c) for c in log] == ["fp", "proof", f"dev-copy drop {COPY}", f"dev-copy create {COPY}"]
    # the proof-only ran on the template: no copy name in its environment, so its first line is
    # `on cobalt_dev` (the stub prints the name it is given)
    assert all(c["COBALT_DEV_DB_NAME"] is None for c in log), log
    assert_nothing_left(tree)


def test_g1_a_red_suite_still_drops_the_copy(tree):
    tree.worktree(NAME, copy_lists())
    done = tree.gate(NAME, tree.env("a", pytest=[{"out": "1 failed, 4 passed in 0.10s", "rc": 1}]))
    assert done.returncode == 1, done.stdout + done.stderr
    log = tree.calls("a")
    assert kind(log[-1]) == f"dev-copy drop {COPY}", [kind(c) for c in log]
    assert f"copy: {COPY} dropped" in done.stdout.splitlines()
    assert_nothing_left(tree)


@pytest.mark.parametrize("lists", [
    "\n## COPY CREATE\n`uv run cobalt db dev-copy create <COPY>`\n",
    "\n## COPY DROP\n`uv run cobalt db dev-copy drop <COPY>`\n",
    "\n## COPY CREATE\n`uv run cobalt db dev-copy create <COPY> <COPY>`\n"
    "\n## COPY DROP\n`uv run cobalt db dev-copy drop <COPY>`\n",
    "\n## COPY CREATE\n`uv run cobalt db dev-copy create cobalt_dev_x`\n"
    "\n## COPY DROP\n`uv run cobalt db dev-copy drop <COPY>`\n",
])
def test_g1_half_a_copy_mode_is_refused_before_anything_runs(tree, lists):
    tree.worktree(NAME, LISTS.read_text() + lists)
    done = tree.gate(NAME, tree.env("a"))
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: gate-lists.md holds half a copy mode" in done.stderr
    assert tree.calls("a") == []
    assert not (tree.wt / LOCK_NAME).exists()


def test_g1_without_the_sections_the_gate_runs_on_the_one_lock(tree):
    """NEGATIVE CONTROL: the real lists file, no `## COPY` section — today's run, line for line."""
    tree.worktree(NAME, LISTS.read_text())
    done = tree.gate(NAME, tree.env("a"))
    assert done.returncode == 0, done.stdout + done.stderr
    log = tree.calls("a")
    assert not any(dev_copy(c) for c in log)
    assert all(c["COBALT_DEV_DB_NAME"] is None for c in log)
    assert all(c["lock"] for c in log), log
    assert not (tree.wt / LOCK_NAME).exists()
    assert not (tree.wt / MARKS).exists()
    out = done.stdout.splitlines()
    assert out[:-1] == TODAY, out
    assert out[-1].startswith(f"log: {tree.wt / '.gate-logs' / NAME}-withdb-")


def test_g1_a_copy_name_over_50_characters_is_refused(tree):
    long = "w" * 45
    tree.worktree(long, copy_lists())
    done = tree.gate(long, tree.env("a"))
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: copy name too long" in done.stderr
    assert tree.calls("a") == []
    assert not (tree.wt / LOCK_NAME).exists()


def test_g1_a_leftover_marker_and_env_of_the_same_worktree_do_not_block_the_next_run(tree):
    tree.worktree(NAME, copy_lists())
    (tree.wt / NAME / ".env").write_text(CONSTRUCTED_ENV)
    (tree.wt / MARKS).mkdir()
    (tree.wt / MARKS / NAME).write_text(COPY + "\n")
    done = tree.gate(NAME, tree.env("a"))
    assert done.returncode == 0, done.stdout + done.stderr
    assert "lock not ours alone" not in done.stdout
    kinds = [kind(c) for c in tree.calls("a")]
    assert kinds[2:4] == [f"dev-copy drop {COPY}", f"dev-copy create {COPY}"], kinds
    assert_nothing_left(tree)


def test_g1_check_o1_a_signal_while_the_create_runs_still_drops_the_copy(tree):
    """CHECK O1 (X2, G1 step 5): a TERM that lands while `## COPY CREATE` runs, the create itself
    done, must not leave the copy behind: the trap drops it before the lock release."""
    tree.worktree(NAME, copy_lists())
    pidfile = tree.tmp / "gate-pid"
    real = tree.bin / "uv-real"
    (tree.bin / "uv").rename(real)
    (tree.bin / "uv").write_text(
        "#!/bin/sh\n"
        f'"{real}" "$@"\n'
        "rc=$?\n"
        'case " $* " in *" dev-copy create "*)\n'
        f'    while [ ! -s "{pidfile}" ]; do :; done\n'
        f'    kill -TERM "$(cat "{pidfile}")" ;;\n'
        "esac\n"
        'exit "$rc"\n'
    )
    (tree.bin / "uv").chmod(0o755)
    first = tree.popen(NAME, tree.env("a"))
    pidfile.write_text(str(first.pid))
    out, err = first.communicate(timeout=300)
    assert first.returncode == 143, out + err
    kinds = [kind(c) for c in tree.calls("a")]
    assert kinds[-1] == f"dev-copy drop {COPY}", kinds
    assert kinds.count(f"dev-copy drop {COPY}") == 2, kinds
    assert_nothing_left(tree)


# ---- L1: desk-launch.sh lock_free -----------------------------------------------------------------


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


@pytest.fixture
def desk(roots, tmp_path):
    """The `desk` fixture of tests/ops/test_devdb_lock.py, rebuilt here: a tmp main repo with the
    three fixed files, one job card whose build worktree exists, one deploy card, a stub `claude`."""
    wt, repo, env = roots
    prompts = repo / "docs" / "40 - DevDocs" / "prompts"
    reports = repo / "docs" / "40 - DevDocs" / "reports"
    (prompts / "2026-01-02").mkdir(parents=True)
    reports.mkdir(parents=True)
    for hub in ("BUILD-HUB.md", "CHECK-HUB.md", "DEPLOY-HUB.md"):
        shutil.copy(HUBS / hub, prompts / hub)
    (reports / "cto-2026-01-02.md").write_text(
        "| R1 | 07:00 ET | HIS RULING (constructed). | HIS RULING · APPROVED |\n")
    (repo / ".gitignore").write_text(".env\n")
    git(repo, "init", "-q", "-b", "main")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "base")
    base = git(repo, "rev-parse", "--short=8", "HEAD")

    job_wt = wt / "x-job"
    git(repo, "worktree", "add", "-q", "-b", "ops/x-job", str(job_wt), base)
    build_report = job_wt / "docs" / "40 - DevDocs" / "reports" / "x-job-build.md"
    build_report.parent.mkdir(parents=True, exist_ok=True)
    build_report.write_text("BUILT · job: x-job\n")
    git(job_wt, "add", "-A")
    git(job_wt, "commit", "-q", "-m", "build")
    tip = git(job_wt, "rev-parse", "--short=8", "HEAD")
    build_report.write_text(f"BUILT · job: x-job · tip: {tip}\n")
    git(job_wt, "add", "-A")
    git(job_wt, "commit", "-q", "-m", "build report")
    head = git(job_wt, "rev-parse", "--short=8", "HEAD")
    (reports / "x-job-ship-check.md").write_text(
        f"CHECK DONE · job: x-job · tip: {tip} · held unfixed: 0 · ready: YES\n")

    card = prompts / "2026-01-02" / "01-x-job-card.md"
    card.write_text(
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        f"BASE: {base}\nTIP: {tip}\nREPORT: {build_report}\n"
        f"CHECK REPORT: {reports / 'x-job-check.md'}\nHOUSE B: as needed\n"
        "TREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n"
    )
    deploy = prompts / "2026-01-02" / "02-x-deploy-card.md"
    deploy.write_text(
        "JOB: x-deploy\nLADDER: OFF-LADDER\nBRANCH: deploy/x-deploy\nWORKTREE: x-gate\n"
        f"BASE: main\nTIP: {head}\nREPORT: {reports / 'deploy-x.md'}\nRULINGS: none\n"
        "TAG: x-tag\nMIGRATIONS: none\nSET: x-job\n\n## SHIPS\n"
        f"| 1 | `ops/x-job` | `{tip}` | `{head}` | `{reports / 'x-job-ship-check.md'}` | `held unfixed: 0` and `ready: YES` |\n"
        "## MARKERS\n## SMOKE READS\n"
    )
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "cards")

    stub = tmp_path / "bin"
    stub.mkdir()
    calls = tmp_path / "claude-calls"
    (stub / "claude").write_text(
        '#!/bin/sh\nif [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
        f'printf "%s\\n" "$PWD" >> "{calls}"\nexit 0\n'
    )
    (stub / "claude").chmod(0o755)
    env = dict(env, PATH=f"{stub}:{os.environ['PATH']}", **GIT_ENV)
    return wt, card, deploy, env, calls


def hold_the_lock(wt: Path, by: str = "beta") -> None:
    (wt / LOCK_NAME).mkdir()
    (wt / LOCK_NAME / "owner").write_text(by + "\n")
    (wt / by / ".env").write_text(CONSTRUCTED_ENV)


def mark_a_copy(wt: Path, by: str = "beta") -> None:
    (wt / by / ".env").write_text(CONSTRUCTED_ENV)
    (wt / MARKS).mkdir(exist_ok=True)
    (wt / MARKS / by).write_text(f"cobalt_dev_{by}\n")


def launch(env: dict, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(LAUNCH), *args], env=env, capture_output=True, text=True, timeout=120
    )


def test_l1_a_build_resume_ignores_another_worktrees_copy_env(desk):
    wt, card, deploy, env, calls = desk
    mark_a_copy(wt)
    done = launch(env, "build", str(card), "W")
    assert done.returncode == 0, done.stderr
    assert calls.read_text().splitlines() == [str(wt / "x-job")]


def test_l1_an_env_with_no_marker_is_still_the_lock(desk):
    """NEGATIVE CONTROL: a `.env` with no marker (a decoy, a lock-mode run) is the lock."""
    wt, card, deploy, env, calls = desk
    (wt / "beta" / ".env").write_text(CONSTRUCTED_ENV)
    done = launch(env, "build", str(card), "W")
    assert done.returncode == 1
    assert "the cobalt_dev lock is held" in done.stderr
    assert not calls.exists()


def test_l1_a_deploy_launch_is_still_refused_while_the_lock_directory_is_held_even_with_a_marked_env(desk):
    """NEGATIVE CONTROL: lock_dir_free stands."""
    wt, card, deploy, env, calls = desk
    mark_a_copy(wt)
    (wt / LOCK_NAME).mkdir()
    (wt / LOCK_NAME / "owner").write_text("beta\n")
    done = launch(env, "deploy", str(deploy))
    assert done.returncode == 1
    assert "the cobalt_dev lock is held by" in done.stderr
    assert not calls.exists()


# ---- D1: the lists file's header paragraph ---------------------------------------------------------


def header_text() -> str:
    out = []
    for line in LISTS.read_text().splitlines():
        if line.startswith("## "):
            break
        out.append(line)
    return "\n".join(out)


def test_d1_the_lists_file_names_both_copy_sections_in_its_header():
    head = header_text()
    assert head.count("## COPY CREATE") == 1, head
    assert head.count("## COPY DROP") == 1, head


def test_d1_the_real_lists_file_holds_no_copy_section_yet():
    """NEGATIVE CONTROL: copy mode stays off until the code card adds the sections."""
    assert not [ln for ln in LISTS.read_text().splitlines() if ln.startswith("## COPY")]


# ---- H1: the build hub's W (b) line ------------------------------------------------------------------


def test_h1_the_build_hub_w_b_line_names_the_copy():
    lines = [ln for ln in (HUBS / "BUILD-HUB.md").read_text(encoding="utf-8").splitlines()
             if "## COPY CREATE" in ln]
    assert len(lines) == 1, lines
    line = lines[0]
    assert line.startswith("- (b) THE LOCK")
    for words in ("copy: <copy> created", "copy: <copy> dropped", "copy not created", "his R1471"):
        assert words in line, words
    assert line.count("LEVEL 0013") == 1


def hub_line(name: str) -> str:
    lines = [ln for ln in (HUBS / name).read_text(encoding="utf-8").splitlines() if ln.startswith("claude --bg ")]
    assert len(lines) == 1, f"{name}: {len(lines)} launch lines"
    return lines[0]


def test_h1_the_launch_lines_of_the_hubs_carry_no_new_allow_string():
    """NEGATIVE CONTROL: no new command string on a launch line (R411, R412)."""
    for name in ("BUILD-HUB.md", "CHECK-HUB.md", "DEPLOY-HUB.md"):
        line = hub_line(name)
        assert "devdb-copy" not in line and "dev-copy" not in line, name


def test_h1_the_no_clutter_pin_exempts_the_b_line():
    assert 'startswith("- (b) THE LOCK")' in NO_CLUTTER_TEST.read_text(encoding="utf-8")
