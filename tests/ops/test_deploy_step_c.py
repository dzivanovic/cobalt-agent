"""ops/desk/deploy-step-c.sh — DEPLOY-HUB.md STEP-C as one script (card 2026-10-13/496
plist-step-c, rows C1, C2, B1, R1, D1, DF1, BO1).

Every run points the script at a tmp repo standing in for /Users/cobalt/cobalt
(COBALT_REPO_ROOT), the shape of tests/ops/test_deploy_step0.py: `main` holds `jobs.yaml` and a
committed build card whose row C2 names `ops/com.cobalt.prefill-refresh.plist` in its `files`
cell (card 304 `:20`); `<m0>` is `main`; a gate branch adds that plist (the Label pair of card
304's plist at fc6a1e2a, row A1) and its `jobs.yaml` row. The deploy card names the label in
`## LAUNCHD`, or not. `launchctl` is a stub on PATH that records its arguments: the script never
calls it (C1). The real repo, launchd and `data/` are never touched.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "ops" / "desk" / "deploy-step-c.sh"
HUB = REPO / "docs" / "40 - DevDocs" / "prompts" / "DEPLOY-HUB.md"
CARD_MD = REPO / "docs" / "40 - DevDocs" / "prompts" / "CARD.md"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

LABEL = "com.cobalt.prefill-refresh"
PLIST_PATH = f"ops/{LABEL}.plist"
BUILD_CARD = "prompts/2026-01-02/01-x-build-card.md"
FAILED_TAIL = ("installing or changing a launchd job is not on this list; the desk runs it as its "
               "own job · rollback: not used")
GATE = "X7 render, X8, X9, X10 dry run, X15"

# launchctl stub: records each call; `bootstrap` marks the label loaded, `print` answers from that
LAUNCHCTL = f"""#!{sys.executable}
import json, os, sys
calls = os.environ["STUB_CALLS"]
with open(os.path.join(calls, "launchctl.jsonl"), "a") as f:
    f.write(json.dumps(sys.argv[1:]) + "\\n")
loaded = os.path.join(calls, "loaded")
args = sys.argv[1:]
if args[:1] == ["bootstrap"]:
    label = os.path.basename(args[2])[: -len(".plist")]
    with open(loaded, "a") as f:
        f.write(label + "\\n")
    sys.exit(0)
if args[:1] == ["print"]:
    label = args[1].split("/")[-1]
    names = open(loaded).read().split() if os.path.exists(loaded) else []
    if label in names:
        print(f"gui/501/{{label}} = {{{{\\n\\tpath = /Users/cobalt/cobalt/ops/{{label}}.plist\\n}}}}")
        sys.exit(0)
    print(f"Could not find service \\"{{label}}\\" in domain for user gui: 501")
    sys.exit(113)
sys.exit(1)
"""


def plist(label: str) -> str:
    # the Label pair as card 304's plist at fc6a1e2a has it (row A1: `:5`, `:6`)
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n<plist version="1.0">\n<dict>\n'
        f"    <key>Label</key>\n    <string>{label}</string>\n"
        "    <key>RunAtLoad</key>\n    <false/>\n</dict>\n</plist>\n"
    )


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, GIT_OPTIONAL_LOCKS="0", **GIT_ENV),
        capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def launchd(*lines: str) -> str:
    return "## LAUNCHD\n" + "".join(f"{ln}\n" for ln in lines)


def line(label: str = LABEL, mode: str = "add", row: str = "C2", gate: str | None = None,
         dry: str = "none") -> str:
    out = f"{label} · {mode} · {BUILD_CARD}:{row} · dry run: {dry}"
    return out + (f" · gate: {gate}" if gate is not None else "")


class Repo:
    """A tmp main repo, a committed build card, a gate branch that adds the plist."""

    def __init__(self, tmp_path: Path) -> None:
        root = tmp_path.resolve()
        self.repo = root / "repo"
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        (self.prompts / "2026-01-02").mkdir(parents=True)
        self.write("configs/cobalt/jobs.yaml", "jobs:\n  - label: com.cobalt.aset\n")
        self.write("ops/desk/keep.txt", "x\n")
        self.write(".gitignore", "data/\n")  # as the real `.gitignore:6`
        (self.prompts / "2026-01-02" / "01-x-build-card.md").write_text(
            "JOB: x\n\n## ROWS\n\n| row | what | red first | files |\n|---|---|---|---|\n"
            f"| C2 | the job row and plist | T10 | `configs/cobalt/jobs.yaml`, `{PLIST_PATH}` |\n"
            "| C3 | the smoke row | T11 | `configs/cobalt/smoke/s2.yaml` |\n"
            "| C4 | the aset plist | T12 | `ops/com.cobalt.aset.plist` |\n"
        )
        git(self.repo, "init", "-q", "-b", "main")
        self.commit("base")
        self.m0 = git(self.repo, "rev-parse", "--short=8", "HEAD")
        self.branch = "deploy/x-gate"
        git(self.repo, "checkout", "-q", "-b", self.branch)
        self.card = self.prompts / "2026-01-02" / "02-x-deploy-card.md"
        bin_dir = root / "bin"
        bin_dir.mkdir()
        (bin_dir / "launchctl").write_text(LAUNCHCTL)
        (bin_dir / "launchctl").chmod(0o755)
        self.calls = root / "calls"
        self.calls.mkdir()
        self.env = dict(os.environ, COBALT_REPO_ROOT=str(self.repo), STUB_CALLS=str(self.calls),
                        PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}", **GIT_ENV)
        self.owed = self.repo / "data" / "deploy" / "bootstrap-owed.json"

    def write(self, rel: str, text: str) -> None:
        p = self.repo / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", msg)

    def add_plist(self, label: str = LABEL, file_label: str | None = None) -> None:
        self.write(f"ops/{file_label or label}.plist", plist(label))
        self.write("configs/cobalt/jobs.yaml",
                   "jobs:\n  - label: com.cobalt.aset\n  - label: com.cobalt.prefill-refresh\n")
        self.commit("gate: the plist")

    def deploy_card(self, body: str) -> None:
        self.card.write_text("JOB: x-deploy\nBASE: main\nTAG: x-tag\n\n## SHIPS\n\n" + body)

    def run(self, body: str, *, mode: tuple[str, ...] = ()) -> subprocess.CompletedProcess:
        self.deploy_card(body)
        args = [*mode, str(self.card)] + ([LABEL] if mode else [self.m0, self.branch])
        return subprocess.run(["sh", str(SCRIPT), *args], env=self.env, capture_output=True,
                              text=True, timeout=60)

    def launchctl_calls(self) -> list[list[str]]:
        f = self.calls / "launchctl.jsonl"
        return [json.loads(x) for x in f.read_text().splitlines()] if f.exists() else []


@pytest.fixture
def repo(tmp_path):
    return Repo(tmp_path)


def last(done: subprocess.CompletedProcess) -> str:
    return [ln for ln in done.stdout.splitlines() if ln.strip()][-1]


# ---- C1: the STEP-C read ---------------------------------------------------------------------


def test_c1_a_card_named_one_shot_plist_is_admitted(repo):
    repo.add_plist()
    done = repo.run(launchd(line()))
    assert done.returncode == 0, done.stdout + done.stderr
    assert f"ADMITTED: {LABEL} · add" in done.stdout.splitlines()
    assert last(done) == "STEP-C: ADMITTED 1"
    assert not repo.owed.exists()
    assert repo.launchctl_calls() == []


def test_c1_an_unnamed_plist_is_refused(repo):
    repo.add_plist()
    done = repo.run("")
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {PLIST_PATH} — no ## LAUNCHD line names {LABEL}" in done.stdout.splitlines()
    assert last(done) == f"FAILED: C — {PLIST_PATH}: {FAILED_TAIL}"


def test_c1_a_changed_plist_named_change_is_admitted(repo):
    repo.add_plist()
    git(repo.repo, "checkout", "-q", "main")
    git(repo.repo, "merge", "-q", "--ff-only", repo.branch)
    repo.m0 = git(repo.repo, "rev-parse", "--short=8", "HEAD")
    git(repo.repo, "checkout", "-q", repo.branch)
    repo.write(PLIST_PATH, plist(LABEL).replace("<false/>", "<true/>"))
    repo.commit("gate: the plist changed")
    done = repo.run(launchd(line(mode="change")))
    assert done.returncode == 0, done.stdout + done.stderr
    assert f"ADMITTED: {LABEL} · change" in done.stdout.splitlines()
    # the same M under `add` is refused
    done = repo.run(launchd(line(mode="add")))
    assert done.returncode == 1 and "REFUSED: " in done.stdout


@pytest.mark.parametrize("case", ["label_differs", "row_lacks_path", "add_on_m", "aset", "untouched"])
def test_c1_each_failed_test_is_refused(repo, case):
    body = launchd(line())
    if case == "label_differs":
        repo.add_plist(label="com.cobalt.other", file_label=LABEL)
    elif case == "row_lacks_path":
        repo.add_plist()
        body = launchd(line(row="C3"))
    elif case == "add_on_m":
        repo.add_plist()
        git(repo.repo, "checkout", "-q", "main")
        git(repo.repo, "merge", "-q", "--ff-only", repo.branch)
        repo.m0 = git(repo.repo, "rev-parse", "--short=8", "HEAD")
        git(repo.repo, "checkout", "-q", repo.branch)
        repo.write(PLIST_PATH, plist(LABEL).replace("<false/>", "<true/>"))
        repo.commit("gate: changed")
    elif case == "aset":
        repo.write("ops/com.cobalt.aset.plist", plist("com.cobalt.aset"))
        repo.commit("gate: aset")
        body = launchd(line(label="com.cobalt.aset", row="C4"))
    elif case == "untouched":
        repo.add_plist()
        body = launchd(line(), line(label="com.cobalt.ghost"))
    done = repo.run(body)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: " in done.stdout, done.stdout
    assert last(done).startswith("FAILED: C — ") and last(done).endswith(FAILED_TAIL)
    assert not repo.owed.exists()


def test_c1_the_ops_desk_exception_stands(repo):
    repo.write("ops/desk/x.plist", plist("com.cobalt.desk-x"))
    repo.commit("gate: a desk plist")
    done = repo.run("")
    assert done.returncode == 0, done.stdout + done.stderr
    assert any(ln.startswith("EXCEPTION: ops/desk/x.plist") for ln in done.stdout.splitlines())
    assert last(done) == "STEP-C: ADMITTED 0"
    # one whose Label IS a jobs.yaml label is refused
    repo.write("ops/desk/x.plist", plist("com.cobalt.aset"))
    repo.commit("gate: the desk plist names aset")
    done = repo.run("")
    assert done.returncode == 1, done.stdout + done.stderr
    assert last(done) == f"FAILED: C — ops/desk/x.plist: {FAILED_TAIL}"


# ---- FR-O2b: the dry run names `cobalt` first, then 1-4 words ------------------------------------


@pytest.mark.parametrize("dry", [
    "COBALT_ENV=production uv run pkill -f cobalt --dry-run",
    "COBALT_ENV=production uv run cobalt --dry-run",
    "COBALT_ENV=production uv run cobalt a b c d e --dry-run",
])
def test_fr_o2b_a_dry_run_that_is_no_cobalt_command_is_refused(repo, dry):
    repo.add_plist()
    done = repo.run(launchd(line(dry=dry)))
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: ## LAUNCHD " in done.stdout, done.stdout
    assert last(done).startswith("FAILED: C — ") and last(done).endswith(FAILED_TAIL)


@pytest.mark.parametrize("dry", [
    "COBALT_ENV=production uv run cobalt prefill refresh --dry-run",
    "COBALT_ENV=production uv run cobalt a b c d --dry-run",
])
def test_fr_o2b_a_cobalt_dry_run_is_admitted(repo, dry):
    repo.add_plist()
    done = repo.run(launchd(line(dry=dry)))
    assert done.returncode == 0, done.stdout + done.stderr
    assert f"ADMITTED: {LABEL} · add" in done.stdout.splitlines()


def test_c1_a_removed_plist_is_retire_owed(repo):
    repo.add_plist()
    git(repo.repo, "checkout", "-q", "main")
    git(repo.repo, "merge", "-q", "--ff-only", repo.branch)
    repo.m0 = git(repo.repo, "rev-parse", "--short=8", "HEAD")
    git(repo.repo, "checkout", "-q", repo.branch)
    (repo.repo / PLIST_PATH).unlink()
    repo.commit("gate: retire")
    done = repo.run("")
    assert done.returncode == 0, done.stdout + done.stderr
    assert f"RETIRE OWED: {LABEL}" in done.stdout.splitlines()


# ---- C2, B1, R1, D1: the hub and the card format ----------------------------------------------


def section(text: str, head: str) -> str:
    return text.split(f"\n## {head}", 1)[1].split("\n## ", 1)[0]


def test_c2_step_c_calls_the_script_once():
    text = HUB.read_text(encoding="utf-8")
    assert section(text, "STEP-C ").count("ops/desk/deploy-step-c.sh") == 1
    (model,) = [ln for ln in text.splitlines() if ln.startswith("MODEL: ")]
    assert "<launchd set>" in model, model


def test_c2_pin_step_c_still_refuses_an_unnamed_plist():
    text = HUB.read_text(encoding="utf-8")
    assert "installing or changing a launchd job is not on this list" in section(text, "STEP-C ")


def test_b1_step_4_6l_bootstraps_and_verifies():
    lines = HUB.read_text(encoding="utf-8").splitlines()
    i46 = next(i for i, ln in enumerate(lines) if ln.startswith("4.6 "))
    i47 = next(i for i, ln in enumerate(lines) if ln.startswith("## STEP-4.7"))
    (l,) = [ln for ln in lines[i46 + 1:i47] if ln.startswith("4.6L ")]
    assert "launchctl bootstrap gui/501 /Users/cobalt/cobalt/ops/com.cobalt.<label>.plist" in l
    assert "launchctl print gui/501/com.cobalt.<label>" in l
    assert "kickstart" not in l


def test_b1_d1_reads_each_launchd_label():
    d1 = section(HUB.read_text(encoding="utf-8"), "STEP-D1 ")
    assert "<launchd set>" in d1 and "already loaded" in d1


def test_r1_step_5_boots_each_launchd_label_out():
    s5 = section(HUB.read_text(encoding="utf-8"), "STEP-5 ")
    (item,) = [ln for ln in s5.splitlines() if "(1L)" in ln]
    assert "launchctl bootout gui/501/com.cobalt.<label>" in item
    (tail,) = [ln for ln in s5.splitlines() if ln.startswith("- (5) ")]
    assert "launchd:" in tail


def test_d1_card_md_names_launchd():
    lines = CARD_MD.read_text(encoding="utf-8").splitlines()
    assert any(ln.startswith("`## LAUNCHD` (deploy)") for ln in lines)


# ---- DF1: the deferred mode -------------------------------------------------------------------


def test_df1_304_with_deferred_merges_and_loads_nothing(repo):
    repo.add_plist()
    done = repo.run(launchd(line(mode="deferred", gate=GATE)))
    assert done.returncode == 0, done.stdout + done.stderr
    out = done.stdout.splitlines()
    assert any(ln.startswith(f"ADMITTED: {LABEL} · add") for ln in out), out
    assert f"BOOTSTRAP OWED: {LABEL} — {GATE}" in out
    owed = json.loads(repo.owed.read_text())
    assert owed[LABEL]["gate"] == ["X7 render", "X8", "X9", "X10 dry run", "X15"]
    assert repo.launchctl_calls() == []


def test_df1_304_without_deferred_is_admitted_and_bootstrapped(repo):
    repo.add_plist()
    done = repo.run(launchd(line()))
    assert done.returncode == 0, done.stdout + done.stderr
    assert f"ADMITTED: {LABEL} · add" in done.stdout.splitlines()
    assert "BOOTSTRAP OWED" not in done.stdout and not repo.owed.exists()
    # the add label is the launchd set the hub bootstraps at 4.6L
    lines = HUB.read_text(encoding="utf-8").splitlines()
    assert any(ln.startswith("4.6L ") and "launchctl bootstrap gui/501 " in ln for ln in lines)


def test_df1_an_unnamed_plist_is_refused_before_and_after(repo):
    repo.add_plist()
    done = repo.run("")
    assert done.returncode == 1 and last(done) == f"FAILED: C — {PLIST_PATH}: {FAILED_TAIL}"
    assert f"REFUSED: {PLIST_PATH} — no ## LAUNCHD line names {LABEL}" in done.stdout.splitlines()
    # after the deferred deploy: a bootstrap-only run whose card does not name the label
    assert repo.run(launchd(line(mode="deferred", gate=GATE))).returncode == 0
    done = repo.run("", mode=("--bootstrap-only",))
    assert done.returncode == 1 and "REFUSED: " in done.stdout, done.stdout + done.stderr


# ---- BO1: the bootstrap-only deploy -----------------------------------------------------------


def owed_then_merged(repo: Repo) -> None:
    """The deferred deploy ran (the owed file written) and its merge is on `main`."""
    repo.add_plist()
    assert repo.run(launchd(line(mode="deferred", gate=GATE))).returncode == 0
    git(repo.repo, "checkout", "-q", "main")
    git(repo.repo, "merge", "-q", "--ff-only", repo.branch)


RESULTS = "## GATE RESULTS\n" + "".join(f"GATE RESULT: {LABEL} · {item} · run, green (constructed)\n"
                  for item in ("X7 render", "X8", "X9", "X10 dry run", "X15"))


def test_bo1_a_label_only_run_is_refused_when_the_label_is_not_named(repo):
    owed_then_merged(repo)
    done = repo.run(RESULTS, mode=("--bootstrap-only",))
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {LABEL} — the card's ## LAUNCHD names no line for this label" in done.stdout.splitlines()


def test_bo1_a_label_only_run_is_refused_without_recorded_gate_results(repo):
    owed_then_merged(repo)
    done = repo.run(launchd(line()), mode=("--bootstrap-only",))
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: " in done.stdout
    # one item short is refused the same
    done = repo.run(launchd(line()) + "## GATE RESULTS\n" + RESULTS.split("\n", 2)[2],
                    mode=("--bootstrap-only",))
    assert done.returncode == 1 and "REFUSED: " in done.stdout


def test_bo1_a_named_label_with_results_bootstraps_and_merges_nothing(repo):
    owed_then_merged(repo)
    head = git(repo.repo, "rev-parse", "HEAD")
    body = launchd(line()) + "\n" + RESULTS
    done = repo.run(body, mode=("--bootstrap-only",))
    assert done.returncode == 0, done.stdout + done.stderr
    assert f"ADMITTED: {LABEL} · bootstrap-only" in done.stdout.splitlines()
    assert repo.launchctl_calls() == []
    # the hub's 4.6L, typed by the hub (here: by the test, on the stub)
    env = repo.env
    subprocess.run(["launchctl", "bootstrap", "gui/501", f"/Users/cobalt/cobalt/{PLIST_PATH}"],
                   env=env, check=True)
    found = subprocess.run(["launchctl", "print", f"gui/501/{LABEL}"], env=env,
                           capture_output=True, text=True)
    assert found.returncode == 0 and f"path = /Users/cobalt/cobalt/{PLIST_PATH}" in found.stdout
    done = repo.run(body, mode=("--owed-clear",))
    assert done.returncode == 0, done.stdout + done.stderr
    assert f"OWED CLEARED: {LABEL}" in done.stdout.splitlines()
    assert LABEL not in json.loads(repo.owed.read_text())
    # nothing merged, nothing tracked changed
    assert git(repo.repo, "rev-parse", "HEAD") == head
    assert git(repo.repo, "status", "--porcelain", "--untracked-files=no") == ""


# ---- check of plist-step-c-1013 ---------------------------------------------------------------


def test_check_o1_a_plist_that_arrives_by_rename_is_refused_unnamed(repo):
    repo.write("ops/notes.txt", plist(LABEL))
    repo.commit("gate: a note")
    git(repo.repo, "checkout", "-q", "main")
    git(repo.repo, "merge", "-q", "--ff-only", repo.branch)
    repo.m0 = git(repo.repo, "rev-parse", "--short=8", "HEAD")
    git(repo.repo, "checkout", "-q", repo.branch)
    git(repo.repo, "mv", "ops/notes.txt", PLIST_PATH)
    repo.commit("gate: the note becomes a plist")
    done = repo.run("")
    assert done.returncode == 1, done.stdout + done.stderr
    assert last(done) == f"FAILED: C — {PLIST_PATH}: {FAILED_TAIL}"


def test_check_o3_an_add_admission_leaves_no_owed_entry_for_its_label(repo):
    repo.add_plist()
    assert repo.run(launchd(line(mode="deferred", gate=GATE))).returncode == 0
    assert LABEL in json.loads(repo.owed.read_text())
    done = repo.run(launchd(line()))
    assert done.returncode == 0, done.stdout + done.stderr
    assert LABEL not in json.loads(repo.owed.read_text())


def test_c1_a_files_cell_that_only_contains_the_path_is_refused(repo):
    repo.add_plist()
    git(repo.repo, "checkout", "-q", "main")
    repo.write(
        "docs/40 - DevDocs/prompts/2026-01-02/01-x-build-card.md",
        "JOB: x\n\n## ROWS\n\n| row | what | red first | files |\n|---|---|---|---|\n"
        "| C2 | the job row and plist | T10 | `xxops/com.cobalt.prefill-refresh.plistyy` |\n",
    )
    repo.commit("main: the files cell does not name the path")
    git(repo.repo, "checkout", "-q", repo.branch)
    done = repo.run(launchd(line()))
    assert done.returncode == 1, done.stdout + done.stderr
    assert "files cell does not name" in done.stdout


def test_check_a2_a_deferred_admission_is_marked_deferred(repo):
    repo.add_plist()
    done = repo.run(launchd(line(mode="deferred", gate=GATE)))
    assert done.returncode == 0, done.stdout + done.stderr
    assert f"ADMITTED: {LABEL} · add · deferred" in done.stdout.splitlines()


def test_check_a3_the_hub_names_the_bootstrap_only_step():
    lines = HUB.read_text(encoding="utf-8").splitlines()
    (bo,) = [ln for ln in lines if ln.startswith("4.6L-BO ")]
    assert "deploy-step-c.sh --bootstrap-only" in bo and "deploy-step-c.sh --owed-clear" in bo


def test_check_a5_a_refusal_at_4_6l_goes_to_step_5():
    (rule,) = [ln for ln in HUB.read_text(encoding="utf-8").splitlines()
               if ln.startswith("- A DEPLOY NEVER CONTINUES BY MESSAGE")]
    assert "4.6L" in rule, rule
