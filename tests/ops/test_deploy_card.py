"""deploy-card.sh writes a deploy card from checked job cards (card 18 desk-tools-b, row B1).

Every run points the script at a tmp repo standing in for /Users/cobalt/cobalt
(COBALT_REPO_ROOT) and a tmp directory standing in for /Users/cobalt/cobalt-wt
(COBALT_WT_ROOT). Two job branches each carry a code commit and a docs commit
past it; their check reports and job cards are committed on the tmp `main`.
`claude` is a stub on PATH; the script never calls it.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "ops" / "desk" / "deploy-card.sh"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, GIT_OPTIONAL_LOCKS="0", **GIT_ENV),  # the test's own reads write no index
        capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def check_line(tip: str, ready: str = "YES", held: str = "0") -> str:
    return (
        f"CHECK DONE · job: x · pass: 2 · tip: {tip} · held unfixed: {held} · open: 0"
        f" · ready: {ready} · decisions: 0 · for Dejan: 0\n"
    )


class Desk:
    """A tmp main repo with two checked job branches (alpha, beta)."""

    def __init__(self, tmp_path: Path, *, conflict: bool = False, proof: str = "") -> None:
        root = tmp_path.resolve()
        self.repo = root / "repo"
        self.wt = root / "wt"
        self.repo.mkdir()
        self.wt.mkdir()
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts" / "2026-01-02"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        self.prompts.mkdir(parents=True)
        self.reports.mkdir(parents=True)
        (self.prompts / ".keep").write_text("")
        (self.reports / ".keep").write_text("")
        (self.repo / "src").mkdir()
        (self.repo / "src" / "shared.py").write_text("line one\nline two\n")
        (self.repo / ".gitignore").write_text(".env\n")
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "base")

        self.tip: dict[str, str] = {}
        self.head: dict[str, str] = {}
        self.card: dict[str, Path] = {}
        self.check: dict[str, Path] = {}
        for n, name in enumerate(("alpha", "beta"), start=1):
            git(self.repo, "checkout", "-q", "-b", f"ops/{name}", "main")
            (self.repo / "src" / f"{name}.py").write_text(f"{name} = 1\n")
            if conflict:
                (self.repo / "src" / "shared.py").write_text(f"line one by {name}\nline two\n")
            git(self.repo, "add", "-A")
            git(self.repo, "commit", "-q", "-m", f"{name} code")
            self.tip[name] = git(self.repo, "rev-parse", "--short=8", "HEAD")
            report = self.reports / f"{name}-build.md"
            report.write_text(f"BUILT · job: {name}\n")
            git(self.repo, "add", "-A")
            git(self.repo, "commit", "-q", "-m", f"{name} report")
            self.head[name] = git(self.repo, "rev-parse", "--short=8", "HEAD")
            git(self.repo, "checkout", "-q", "main")
        for n, name in enumerate(("alpha", "beta"), start=1):
            check =self.reports / f"{name}-check.md"
            check.write_text(f"# check {name}\n\n{check_line(self.tip[name])}\n")
            self.check[name] = check
            card = self.prompts / f"0{n}-{name}-card.md"
            card.write_text(
                f"JOB: {name}\nLADDER: OFF-LADDER — cto-2026-01-02.md 2026-01-02 R{n}\n"
                f"BRANCH: ops/{name}\nWORKTREE: {name}-wt\nBASE: 00000000\nTIP: {self.tip[name]}\n"
                f"REPORT: {self.wt / name}/x.md\nCHECK REPORT: {check}\nHOUSE B: as needed\n"
                "TREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n| row | what |\n"
                + (proof if name == "alpha" else "")
            )
            self.card[name] = card
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "checks and cards")

        self.out = self.prompts / "03-deploy-x-set-card.md"
        stub = root / "bin"
        stub.mkdir()
        (stub / "claude").write_text(f'#!/bin/sh\nprintf "%s\\n" "$*" >> "{root / "claude-calls"}"\n')
        (stub / "claude").chmod(0o755)
        self.env = dict(
            os.environ, COBALT_REPO_ROOT=str(self.repo), COBALT_WT_ROOT=str(self.wt),
            PATH=f"{stub}{os.pathsep}{os.environ['PATH']}", **GIT_ENV,
        )

    def run(self, *extra: str, cards: tuple[str, ...] = ("alpha", "beta")) -> subprocess.CompletedProcess:
        args = [
            "--job", "x-set", "--set", "xset", "--worktree", "x-gate", "--tag", "x-tag",
            "--out", str(self.out), *extra, *(str(self.card[c]) for c in cards),
        ]
        return subprocess.run(
            ["sh", str(SCRIPT), *args], env=self.env, capture_output=True, text=True,
            errors="replace", timeout=120,
        )

    def state(self) -> dict[str, str]:
        return {
            "status": git(self.repo, "status", "--porcelain"),
            "refs": git(self.repo, "for-each-ref", "--format=%(refname) %(objectname)"),
            "worktrees": git(self.repo, "worktree", "list", "--porcelain"),
            "branches": git(self.repo, "branch", "--list"),
            "head": git(self.repo, "rev-parse", "HEAD"),
        }


def section(text: str, name: str) -> str:
    lines = text.splitlines()
    start = lines.index(f"## {name}")
    body = []
    for line in lines[start + 1:]:
        if line.startswith("## "):
            break
        body.append(line)
    return "\n".join(body)


def header(text: str) -> dict[str, str]:
    out = {}
    for line in text.splitlines():
        if line.startswith("## "):
            break
        if ": " in line:
            key, value = line.split(": ", 1)
            out[key] = value
    return out


def test_two_clean_checks_write_the_card_and_change_nothing_else(tmp_path):
    desk = Desk(tmp_path)
    # the check reports stat-stale: a `git diff` free to take its optional lock would refresh
    # and rewrite .git/index (X4: the script writes no file but --out)
    for check in desk.check.values():
        later = check.stat().st_mtime + 3600
        os.utime(check, (later, later))
    index = (desk.repo / ".git" / "index").read_bytes()
    before = desk.state()
    done = desk.run()
    assert done.returncode == 0, done.stderr
    text = desk.out.read_text()
    head = header(text)
    assert head["JOB"] == "x-set"
    assert head["LADDER"] == "OFF-LADDER — cto-2026-01-02.md 2026-01-02 R1"
    assert head["BRANCH"] == "deploy/x-set"
    assert head["WORKTREE"] == "x-gate"
    assert head["BASE"] == "main"
    assert head["TIP"] == f"{desk.head['alpha']} {desk.head['beta']}"
    assert head["REPORT"] == str(desk.reports / "deploy-x-set.md")
    assert head["RULINGS"] == "none"
    assert head["TAG"] == "x-tag"
    assert head["SET"] == "xset"
    assert head["MIGRATIONS"] == "none"
    ships = section(text, "SHIPS")
    for n, name in enumerate(("alpha", "beta"), start=1):
        row = next(line for line in ships.splitlines() if line.startswith(f"| {n} |"))
        assert f"`ops/{name}`" in row
        assert f"`{desk.tip[name]}`" in row
        assert f"`{desk.head[name]}`" in row
        assert str(desk.check[name]) in row
        assert "`held unfixed: 0` and `ready: YES`" in row
    records = section(text, "RECORDS")
    assert desk.head["alpha"] in records and desk.head["beta"] in records
    assert "CHECK DONE" in records
    # no DEPLOY PROOF on either card: the placeholder desk-launch.sh refuses
    assert "«FILL" in section(text, "MARKERS")
    assert "«FILL" in section(text, "SMOKE READS")
    after = desk.state()
    added = set(after["status"].splitlines()) - set(before["status"].splitlines())
    assert set(before["status"].splitlines()) <= set(after["status"].splitlines())
    assert len(added) == 1 and desk.out.relative_to(desk.repo).as_posix() in added.pop()
    assert {k: v for k, v in after.items() if k != "status"} == {
        k: v for k, v in before.items() if k != "status"
    }
    assert (desk.repo / ".git" / "index").read_bytes() == index


def test_rulings_are_written_when_given(tmp_path):
    desk = Desk(tmp_path)
    done = desk.run("--rulings", "2026-01-02 R7")
    assert done.returncode == 0, done.stderr
    assert header(desk.out.read_text())["RULINGS"] == "2026-01-02 R7"


def test_the_deploy_proof_section_fills_markers_and_smoke_reads(tmp_path):
    marker = '- `grep -c -F "alpha = 1" /x/src/alpha.py` · before `0` · after `1`'
    smoke = "- alpha read · `ls /x/src/alpha.py` · listed"
    desk = Desk(tmp_path, proof=f"\n## DEPLOY PROOF\n{marker}\n{smoke}\n\n## RECORDS\n- unrelated\n")
    done = desk.run()
    assert done.returncode == 0, done.stderr
    text = desk.out.read_text()
    assert marker in section(text, "MARKERS")
    assert smoke in section(text, "SMOKE READS")
    assert smoke not in section(text, "MARKERS")
    assert "- unrelated" not in text
    # beta has no DEPLOY PROOF: its placeholder stands, so the card cannot launch
    assert "«FILL" in section(text, "MARKERS")


def _refused(desk: Desk, done: subprocess.CompletedProcess, job: str) -> None:
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED" in done.stderr
    assert job in done.stderr
    assert not desk.out.exists()


def test_a_check_line_with_ready_no_is_refused(tmp_path):
    desk = Desk(tmp_path)
    desk.check["beta"].write_text(f"# check\n\n{check_line(desk.tip['beta'], ready='NO')}")
    git(desk.repo, "commit", "-q", "-am", "beta not ready")
    _refused(desk, desk.run(), "beta")


def test_a_check_line_with_a_held_defect_is_refused(tmp_path):
    desk = Desk(tmp_path)
    desk.check["alpha"].write_text(f"# check\n\n{check_line(desk.tip['alpha'], held='1')}")
    git(desk.repo, "commit", "-q", "-am", "alpha held")
    _refused(desk, desk.run(), "alpha")


def test_an_uncommitted_check_report_is_refused(tmp_path):
    desk = Desk(tmp_path)
    desk.check["alpha"].write_text(desk.check["alpha"].read_text() + "\nedited after commit\n" + check_line(desk.tip["alpha"]))
    _refused(desk, desk.run(), "alpha")


def test_a_staged_check_report_is_refused(tmp_path):
    desk = Desk(tmp_path)
    committed = desk.check["beta"].read_text()
    desk.check["beta"].write_text("# check, restaged\n\n" + check_line(desk.tip["beta"]))
    git(desk.repo, "add", str(desk.check["beta"]))
    desk.check["beta"].write_text(committed)  # the file is the commit's again; only the index differs
    _refused(desk, desk.run(), "beta")


def test_a_check_report_never_committed_is_refused(tmp_path):
    desk = Desk(tmp_path)
    fresh = desk.reports / "beta-check-2.md"
    fresh.write_text(check_line(desk.tip["beta"]))
    desk.card["beta"].write_text(desk.card["beta"].read_text().replace(str(desk.check["beta"]), str(fresh)))
    _refused(desk, desk.run(), "beta")


def test_an_absent_check_report_is_refused(tmp_path):
    desk = Desk(tmp_path)
    desk.card["beta"].write_text(
        desk.card["beta"].read_text().replace(str(desk.check["beta"]), str(desk.reports / "nope.md"))
    )
    _refused(desk, desk.run(), "beta")


def test_a_head_with_a_src_commit_past_the_code_tip_is_refused(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "checkout", "-q", "ops/alpha")
    (desk.repo / "src" / "alpha.py").write_text("alpha = 2\n")
    git(desk.repo, "commit", "-q", "-am", "alpha past its check")
    git(desk.repo, "checkout", "-q", "main")
    _refused(desk, desk.run(), "alpha")


def test_a_code_tip_that_is_not_an_ancestor_of_the_head_is_refused(tmp_path):
    desk = Desk(tmp_path)
    desk.check["alpha"].write_text(f"# check\n\n{check_line(desk.tip['beta'])}")
    git(desk.repo, "commit", "-q", "-am", "alpha names beta's tip")
    _refused(desk, desk.run(), "alpha")


def test_an_existing_out_path_is_refused_and_left_as_it_was(tmp_path):
    desk = Desk(tmp_path)
    desk.out.write_text("his own text\n")
    done = desk.run()
    assert done.returncode == 1
    assert "REFUSED" in done.stderr
    assert desk.out.read_text() == "his own text\n"


def test_a_conflict_exits_3_and_leaves_nothing_behind(tmp_path):
    desk = Desk(tmp_path, conflict=True)
    before = desk.state()
    done = desk.run()
    assert done.returncode == 3, done.stdout + done.stderr
    assert "CONFLICT beta src/shared.py" in done.stdout
    assert not desk.out.exists()
    assert desk.state() == before


def test_one_clean_job_alone_writes_a_one_row_card(tmp_path):
    """Negative control for the conflict: either branch alone merges clean."""
    desk = Desk(tmp_path, conflict=True)
    done = desk.run(cards=("beta",))
    assert done.returncode == 0, done.stderr
    head = header(desk.out.read_text())
    assert head["TIP"] == desk.head["beta"]
    assert head["LADDER"] == "OFF-LADDER — cto-2026-01-02.md 2026-01-02 R2"


def test_a_migration_on_a_head_leaves_the_placeholder(tmp_path):
    desk = Desk(tmp_path)
    git(desk.repo, "checkout", "-q", "ops/beta")
    mig = desk.repo / "src" / "cobalt" / "db_migrations"
    mig.mkdir(parents=True)
    (mig / "0099_x.sql").write_text("SELECT 1;\n")
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", "beta migration")
    tip = git(desk.repo, "rev-parse", "--short=8", "HEAD")
    git(desk.repo, "checkout", "-q", "main")
    desk.check["beta"].write_text(f"# check\n\n{check_line(tip)}")
    git(desk.repo, "commit", "-q", "-am", "beta rechecked")
    done = desk.run()
    assert done.returncode == 0, done.stderr
    migrations = header(desk.out.read_text())["MIGRATIONS"]
    assert migrations.startswith("«FILL")
    assert "src/cobalt/db_migrations/0099_x.sql" in migrations


@pytest.mark.parametrize("bad", ["X-Set", "x_set", "-x", "x;rm"])
def test_a_job_name_outside_lowercase_is_refused(tmp_path, bad):
    desk = Desk(tmp_path)
    args = [
        "--job", bad, "--set", "xset", "--worktree", "x-gate", "--tag", "x-tag",
        "--out", str(desk.out), str(desk.card["alpha"]),
    ]
    done = subprocess.run(["sh", str(SCRIPT), *args], env=desk.env, capture_output=True, text=True)
    assert done.returncode == 1
    assert "REFUSED" in done.stderr
    assert not desk.out.exists()


def test_check_o2_a_migration_only_main_has_leaves_migrations_none(tmp_path):
    desk = Desk(tmp_path)
    mig = desk.repo / "src" / "cobalt" / "db_migrations"
    mig.mkdir(parents=True)
    (mig / "0098_main.sql").write_text("SELECT 1;\n")
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", "main gains a migration after the branches were cut")
    done = desk.run()
    assert done.returncode == 0, done.stderr
    assert header(desk.out.read_text())["MIGRATIONS"] == "none"


@pytest.mark.parametrize("bad", ["../x-gate", "/abs/x-gate", "a/b", ".hidden", "agy-trial", ""])
def test_a_worktree_outside_the_pattern_is_refused(tmp_path, bad):
    desk = Desk(tmp_path)
    args = [
        "--job", "x-set", "--set", "xset", "--worktree", bad, "--tag", "x-tag",
        "--out", str(desk.out), str(desk.card["alpha"]),
    ]
    done = subprocess.run(["sh", str(SCRIPT), *args], env=desk.env, capture_output=True, text=True)
    assert done.returncode == 1
    assert "REFUSED" in done.stderr
    assert not desk.out.exists()
