"""desk-launch.sh prodwrite "<card>": the production-write seat on PRODWRITE-HUB.md (card 2026-10-12 392 W2).

In the shape of tests/ops/test_desk_launch_brain.py: every run copies ops/desk/desk-launch.sh into
tmp_path/ops/ beside two stubs, desk-context.sh (the desk-size guard, passing) and desk-list.sh
(LIST rows `id · name · cwd · status · state`). COBALT_REPO_ROOT and COBALT_WT_ROOT point at tmp
roots; the tmp repo holds this tree's real PRODWRITE-HUB.md and BUILD-HUB.md, two constructed desk
files — `cto-2026-01-01.md` (R1, the card's RULINGS row) and `cto-2026-01-02.md` (R1 HIS RULING ·
APPROVED, R2 a DESK RECORD) — and a constructed prodwrite card. `claude` is a stub on PATH that
records its cwd and arguments. Every command, table and count is constructed; nothing here reads a
real card, session list, database or `.env`.
"""

from __future__ import annotations

import os
import shlex
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

WRITE = "COBALT_ENV=production uv run cobalt settings load --apply x.yaml"
BACKUP = "COBALT_ENV=production uv run cobalt backup run"
COUNT = 'COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT count(*) FROM user.x_settings"'
HEAD_ROW = "| row | command | table | count read | expected rows | backup | inverse |\n|---|---|---|---|---|---|---|\n"
R0101 = "| R1 | 07:00 ET | HIS RULING (constructed): the class. | HIS RULING · APPROVED |\n"
R1 = "| R1 | 07:00 ET | HIS RULING (constructed): the write may run. | HIS RULING · APPROVED |\n"
R2 = "| R2 | 07:05 ET | DESK RECORD (constructed): a note. | RECORD |\n"
DESK = "d35c0001"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def write_exe(path: Path, body: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("#!/bin/sh\n" + body)
    path.chmod(0o755)
    return path


def row(command: str = WRITE, *, table: str = "user.x_settings", count: str = COUNT,
        expected: str = "3", backup: str = BACKUP, inverse: str = "none", rid: str = "P1") -> str:
    def cell(v: str) -> str:
        return f"`{v}`" if v else ""
    return f"| {rid} | {cell(command)} | {cell(table)} | {cell(count)} | {expected} | {cell(backup)} | {inverse} |\n"


class Desk:
    def __init__(self, tmp_path: Path):
        self.tmp = tmp_path
        self.repo = tmp_path / "repo"
        self.wt = tmp_path / "wt"
        self.wt.mkdir()
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        (self.prompts / "2026-01-02").mkdir(parents=True)
        self.reports.mkdir(parents=True)
        for name in ("PRODWRITE-HUB.md", "BUILD-HUB.md"):
            if (HUBS / name).exists():  # on BASE the prodwrite hub is not there: the kind is refused first
                shutil.copy(HUBS / name, self.prompts / name)
        (self.reports / "cto-2026-01-01.md").write_text(R0101)
        self.desk_file = self.reports / "cto-2026-01-02.md"
        self.desk_file.write_text(R1 + R2)
        git(self.repo, "init", "-q", "-b", "main")
        self.commit("base")
        self.base = git(self.repo, "rev-parse", "--short=8", "HEAD")
        self.card = self.prompts / "2026-01-02" / "07-x-write-card.md"
        self.report = self.reports / "prodwrite-x-write.md"
        self.write_card()
        self.commit("card")

        ops = tmp_path / "ops"
        ops.mkdir()
        self.launch = ops / "desk-launch.sh"
        # the prompt kind's cwd pattern re-pointed at tmp_path (test_desk_launch_prechecks.py's staging)
        self.launch.write_text(
            LAUNCH.read_text().replace("\\/Users\\/cobalt\\/", str(tmp_path).replace("/", "\\/") + "\\/"))
        write_exe(ops / "desk-context.sh", "exit 0\n")
        self.live([(DESK, "cto-desk")])
        self.calls = tmp_path / "claude-calls"
        write_exe(tmp_path / "bin" / "claude",
                  f'if [ "$1" = agents ]; then echo "[]"; exit 0; fi\nprintf "%s | %s\\n" "$PWD" "$*" >> "{self.calls}"\nexit 0\n')
        self.env = dict(
            os.environ, COBALT_WT_ROOT=str(self.wt), COBALT_REPO_ROOT=str(self.repo),
            PATH=f"{tmp_path / 'bin'}:{os.environ['PATH']}", **GIT_ENV,
        )

    def write_card(self, *, rows: str | None = None, cls: str = "K3, K5", branch: str = "main",
                   worktree: str = "none", ruling: str = "2026-01-02 R1", extra: str = "",
                   section: bool = True) -> None:
        body = HEAD_ROW + (row() if rows is None else rows)
        self.card.write_text(
            f"JOB: x-write\nLADDER: OFF-LADDER — constructed\nCLASS: {cls}\nBRANCH: {branch}\n"
            f"WORKTREE: {worktree}\nBASE: {self.base}\nREPORT: {self.report}\nRULINGS: 2026-01-01 R1\n"
            f"WRITE RULING: {ruling}\n{extra}\n"
            + (f"## ROWS\n\n{body}\n" if section else "")
            + "## RECORDS\n- constructed\n"
        )

    def live(self, rows: list[tuple[str, str]], status: int = 0) -> None:
        out = "".join(f"printf '%s\\n' '{i} · {n} · ~/cobalt · idle · working'\n" for i, n in rows)
        write_exe(self.launch.parent / "desk-list.sh", f"{out}exit {status}\n")

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", msg)

    def run(self, *args: str, dry: bool = True) -> subprocess.CompletedProcess:
        env = dict(self.env, DESK_LAUNCH_DRY="1") if dry else self.env
        return subprocess.run(["sh", str(self.launch), *args], env=env, cwd=self.tmp,
                              capture_output=True, text=True, timeout=120)


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path)


def allow_of(line: str) -> list[str]:
    words, out, inside = shlex.split(line), [], False
    for w in words:
        if w.startswith("--"):
            inside = w == "--allowedTools"
            continue
        if inside:
            out.append(w)
    return out


def refused(desk: Desk, done: subprocess.CompletedProcess, text: str) -> None:
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {text}" in done.stderr, done.stderr
    assert done.stdout == ""
    assert not desk.calls.exists()


# ---- P1 the good card --------------------------------------------------------------------------


def test_p1_a_good_card_prints_the_cd_and_the_line_with_its_one_write(desk):
    """RED on BASE: REFUSED: kind 'prodwrite' is none of … (desk-launch.sh:892)."""
    done = desk.run("prodwrite", str(desk.card))
    assert done.returncode == 0, done.stderr
    out = done.stdout.splitlines()
    assert out[0] == f"cd {desk.repo}", out
    (line,) = out[1:]
    allow = allow_of(line)
    assert allow[-1] == f"Bash({WRITE})", allow
    assert allow.count(f"Bash({WRITE})") == 1
    assert "<" not in line and ">" not in line, line
    assert f"--remote-control prodwrite-x-write --name prodwrite-x-write " in line
    assert f"CARD: '{desk.card}'" in line
    assert f'desk-watch.sh prodwrite "{desk.card}"' in done.stderr


def test_p1_a_real_launch_runs_the_line_from_the_repo(desk):
    done = desk.run("prodwrite", str(desk.card), dry=False)
    assert done.returncode == 0, done.stderr
    (call,) = desk.calls.read_text().splitlines()
    cwd, args = call.split(" | ", 1)
    assert Path(cwd).resolve() == desk.repo.resolve()
    assert f"Bash({WRITE})" in args


# ---- P2 every refusal, each with its own text --------------------------------------------------


def two_rows() -> str:
    return row() + row("COBALT_ENV=production uv run cobalt settings load --apply y.yaml", rid="P2")


P2 = {
    # the write row unnamed
    "no ROWS section": (dict(section=False), "the write row is unnamed: ## ROWS holds 0 rows"),
    "zero rows": (dict(rows=""), "the write row is unnamed: ## ROWS holds 0 rows"),
    "two rows": (dict(rows=two_rows()), "the write row is unnamed: ## ROWS holds 2 rows"),
    "empty command": (dict(rows=row("")), "the write row is unnamed: its command cell is empty"),
    # a differently shaped write
    "no prefix": (dict(rows=row("uv run cobalt x")), "the write is not a cobalt command"),
    "semicolon": (dict(rows=row(WRITE + "; ls")), "the write holds a character the line cannot carry"),
    "dollar": (dict(rows=row(WRITE + " $HOME")), "the write holds a character the line cannot carry"),
    "bar": (dict(rows=row(WRITE + " \\| ls")), "the write holds a character the line cannot carry"),
    "quote": (dict(rows=row(WRITE + ' "x"')), "the write holds a character the line cannot carry"),
    "migrate": (dict(rows=row("COBALT_ENV=production uv run cobalt db migrate --allow-prod")),
                "the write db migrate has its own home"),
    "query": (dict(rows=row("COBALT_ENV=production uv run cobalt db query --side user --prod x")),
              "the write db query has its own home"),
    "restore": (dict(rows=row("COBALT_ENV=production uv run cobalt backup restore")),
                "the write backup has its own home"),
    # the ruling row not his
    "ruling empty": (dict(ruling=""), "incomplete card: 'WRITE RULING' is empty"),
    "desk record": (dict(ruling="2026-01-02 R2"), "ruling 2026-01-02 R2: not HIS RULING + APPROVED"),
    "no row": (dict(ruling="2026-01-02 R9"), "ruling 2026-01-02 R9: no such row"),
    # the backup step missing
    "backup empty": (dict(rows=row(backup="")), "the backup step is missing"),
    "backup none": (dict(rows=row(backup="none")), "the backup step is missing"),
    "backup dry": (dict(rows=row(backup=BACKUP + " --dry-run")), "the backup step is missing"),
    # the header
    "class": (dict(cls="K5"), "prodwrite: CLASS 'K5' does not name K3"),
    "branch": (dict(branch="ops/x"), "prodwrite: BRANCH 'ops/x' is not main"),
    "worktree": (dict(worktree="x-write"), "prodwrite: WORKTREE 'x-write' is not none"),
}


@pytest.mark.parametrize("case", list(P2))
def test_p2_a_card_outside_the_shape_is_refused_with_its_own_text(desk, case):
    """RED on BASE: every case is refused by the kind refusal alone (`kind 'prodwrite' is none of`)."""
    kw, text = P2[case]
    desk.write_card(**kw)
    desk.commit(case)
    refused(desk, desk.run("prodwrite", str(desk.card), dry=False), text)


def test_p2_approved_only_in_the_working_tree_is_refused(desk):
    desk.desk_file.write_text(R1.replace("HIS RULING · APPROVED", "HIS RULING · PROPOSED") + R2)
    desk.commit("proposed")
    desk.desk_file.write_text(R1 + R2)  # APPROVED typed, never committed
    refused(desk, desk.run("prodwrite", str(desk.card), dry=False), "ruling 2026-01-02 R1: not committed")


def test_p2_a_present_report_is_refused(desk):
    desk.report.write_text("# an earlier run\n")
    refused(desk, desk.run("prodwrite", str(desk.card), dry=False), "the prodwrite report already exists")


def test_p2_a_resume_step_is_refused(desk):
    refused(desk, desk.run("prodwrite", str(desk.card), "WRITE", dry=False),
            "a prodwrite never resumes: a stopped write is a new card")


def test_p2_code_moved_since_base_is_refused(desk):
    (desk.repo / "ops").mkdir()
    (desk.repo / "ops" / "x.sh").write_text("true\n")
    desk.commit("code past BASE")
    refused(desk, desk.run("prodwrite", str(desk.card), dry=False), "production code moved since BASE")


@pytest.mark.parametrize("name", ["deploy-hub-x", "prodwrite-y"])
def test_p2_a_live_deploy_or_prodwrite_session_is_refused(desk, name):
    desk.live([(DESK, "cto-desk"), ("aaaa0001", name)])
    refused(desk, desk.run("prodwrite", str(desk.card), dry=False),
            "prodwrite: a deploy-hub- or prodwrite- session is live (aaaa0001)")


def test_p2_an_unreadable_session_list_is_refused(desk):
    desk.live([], status=1)
    refused(desk, desk.run("prodwrite", str(desk.card), dry=False), "prodwrite: the session list is unreadable")


def test_p2_negative_control_other_live_sessions_do_not_block(desk):
    desk.live([(DESK, "cto-desk"), ("aaaa0002", "x-job-build"), ("aaaa0003", "brain")])
    done = desk.run("prodwrite", str(desk.card))
    assert done.returncode == 0, done.stderr


# ---- P3 two-sided: no other kind's line changes ------------------------------------------------


def test_p3_a_build_launch_prints_the_build_hub_line_unchanged(desk):
    report = desk.wt / "x-job" / "docs" / "40 - DevDocs" / "reports" / "x-job-build.md"
    card = desk.prompts / "2026-01-02" / "01-x-job-card.md"
    card.write_text(
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        f"BASE: {desk.base}\nREPORT: {report}\nRULINGS: 2026-01-01 R1\n\n## ROWS\n| row | what |\n")
    desk.commit("build card")
    done = desk.run("build", str(card))
    assert done.returncode == 0, done.stderr
    line = done.stdout.splitlines()[-1]
    (src,) = [ln for ln in (HUBS / "BUILD-HUB.md").read_text().splitlines() if ln.startswith("claude --bg ")]
    assert line == src.replace("<card>", str(card)).replace("<job>", "x-job").replace("<worktree>", "x-job")
    assert '"Bash(COBALT_ENV=production*)"' in line.split("--disallowedTools", 1)[1]
    assert "<prod write>" not in line


def test_p3_a_prompt_line_is_unchanged_by_the_fill(desk):
    pfile = desk.prompts / "2026-01-02" / "06-x-survey.md"
    line = (f"claude --bg \"Read '{pfile}' and follow it exactly.\" --model claude-opus-5-5 "
            "--permission-mode auto --remote-control x-survey --name x-survey --allowedTools \"Read\" "
            "\"Bash(ls *)\" --disallowedTools \"AskUserQuestion\" \"EnterWorktree\" --add-dir /Users/cobalt/cobalt")
    pfile.write_text(f"MODEL: Opus · its line: `cd {desk.repo}`, then `{line}`\n\n# SURVEY (constructed)\n")
    desk.commit("prompt")
    done = desk.run("prompt", str(pfile))
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines()[-1] == line
