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


def check_line(tip: str, ready: str = "YES", held: str = "0", open: str = "0") -> str:
    return (
        f"CHECK DONE · job: x · pass: 2 · tip: {tip} · held unfixed: {held} · open: {open}"
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


def test_l3_an_accented_tag_is_refused_under_a_utf8_locale(tmp_path):
    """Card 03 L3: `[!A-Za-z0-9._-]` admits `é` under en_US.UTF-8 unless the script runs LC_ALL=C."""
    desk = Desk(tmp_path)
    args = [
        "--job", "x-set", "--set", "xset", "--worktree", "x-gate", "--tag", "x-tagé",
        "--out", str(desk.out), str(desk.card["alpha"]),
    ]
    env = dict(desk.env, LC_ALL="en_US.UTF-8", LANG="en_US.UTF-8")
    done = subprocess.run(["sh", str(SCRIPT), *args], env=env, capture_output=True, text=True)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: --tag 'x-tagé' is not a plain tag name" in done.stderr
    assert not desk.out.exists()


# ---- card 63 N8: the deploy card carries the build's --tickers ---------------------------------

PROMPTS = REPO / "docs" / "40 - DevDocs" / "prompts"
CARD_MD_ROW = (
    "| `TICKERS` | — | — | optional | — | the build's `--tickers`, `A,B,…` of `[A-Z0-9.]`, or `none`; "
    "written by `deploy-card.sh`; the gate call takes it as `--tickers` (omitted when `none`) |"
)
HUB_OLD = "the set's `--tickers` and `--migration` as the card gives them"
HUB_NEW = ("the card's `TICKERS` as `--tickers` (omitted when `none`) and the set's `--migration` "
           "as the card gives it")


def grep_c(path: Path, fixed: str) -> int:
    """`grep -c -F <fixed> <path>`: the number of lines holding the string."""
    return sum(fixed in line for line in path.read_text().splitlines())


def test_n8_tickers_are_written_directly_after_set(tmp_path):
    desk = Desk(tmp_path)
    done = desk.run("--tickers", "ZZPB,TEST")
    assert done.returncode == 0, done.stderr
    text = desk.out.read_text()
    assert header(text)["TICKERS"] == "ZZPB,TEST"
    lines = text.splitlines()
    assert lines[lines.index("SET: xset") + 1] == "TICKERS: ZZPB,TEST"


def test_n8_no_tickers_given_writes_none(tmp_path):
    desk = Desk(tmp_path)
    done = desk.run()
    assert done.returncode == 0, done.stderr
    lines = desk.out.read_text().splitlines()
    assert header(desk.out.read_text())["TICKERS"] == "none"
    assert lines[lines.index("SET: xset") + 1] == "TICKERS: none"


@pytest.mark.parametrize("bad", ["zz", "A,,B", "A,B,", "A'B"])
def test_n8_tickers_outside_the_gates_pattern_are_refused(tmp_path, bad):
    """Negative controls, green on BASE (an unknown option there) and after (the pattern)."""
    desk = Desk(tmp_path)
    done = desk.run("--tickers", bad)
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: " in done.stderr and "--tickers" in done.stderr, done.stderr
    assert not desk.out.exists()


def test_n8_card_md_row_and_deploy_hub_phrase():
    card_md = PROMPTS / "CARD.md"
    hub = PROMPTS / "DEPLOY-HUB.md"
    assert grep_c(card_md, CARD_MD_ROW) == 1
    lines = card_md.read_text().splitlines()
    assert lines[lines.index(CARD_MD_ROW) - 1].startswith("| `SET` |")
    assert grep_c(card_md, "`MIGRATIONS`, `SET`, `TICKERS`. Body:") == 1
    assert grep_c(hub, HUB_NEW) == 1
    assert grep_c(hub, HUB_OLD) == 0


# ---- launcher-1010 row A: --fix-report fills a fix-round row (R810; CARD.md :48) ---------------

LAUNCH = REPO / "ops" / "desk" / "desk-launch.sh"


def fix_round(desk: Desk, *, last: str | None = None, on_head: bool = True,
              name: str = "alpha") -> tuple[str, str, Path]:
    """A small fix moves `name`'s code past its checked tip (R376, L75); its fix report is
    committed on the branch head only (card 63 N6), unless `on_head` is False (the head is then
    the fix commit). `last` is the report's last line, `FIXED` standing for the fix tip.
    Returns (fix tip, head, report path)."""
    git(desk.repo, "checkout", "-q", f"ops/{name}")
    (desk.repo / "src" / f"{name}.py").write_text(f"{name} = 2\n")
    git(desk.repo, "commit", "-q", "-am", f"{name} small fix")
    fixed = git(desk.repo, "rev-parse", "--short=8", "HEAD")
    report = desk.reports / f"{name}-fix.md"
    if on_head:
        line = (last or "BUILT · job: x · tip: FIXED | rows: 1 of 1").replace("FIXED", fixed)
        report.write_text(f"# {name} fix round\n\n{line}\n\n")
        git(desk.repo, "add", "-A")
        git(desk.repo, "commit", "-q", "-m", f"{name} fix report")
    head = git(desk.repo, "rev-parse", "--short=8", "HEAD")
    git(desk.repo, "checkout", "-q", "main")
    assert not report.exists()
    return fixed, head, report


def ships_row(text: str, n: int) -> str:
    return next(line for line in section(text, "SHIPS").splitlines() if line.startswith(f"| {n} |"))


def test_a_fix_report_fills_the_ships_row_cell_and_code_tip(tmp_path):
    """RED on BASE: `unknown option '--fix-report'` (exit 1)."""
    desk = Desk(tmp_path)
    fixed, head, report = fix_round(desk)
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
    text = desk.out.read_text()
    assert header(text)["TIP"] == f"{head} {desk.head['beta']}"
    alpha = ships_row(text, 1)
    cells = [c.strip() for c in alpha.split("|")]
    assert cells[3] == f"`{fixed}`", alpha  # code tip: the fix report's tip
    assert cells[4] == f"`{head}`", alpha
    assert cells[5] == f"`{desk.check['alpha']}`", alpha
    assert cells[6] == "`held unfixed: 0` and `ready: YES`", alpha
    assert cells[7] == f"`{report}`", alpha
    assert ships_row(text, 2).endswith("| `held unfixed: 0` and `ready: YES` | |")
    assert f"code tip `{fixed}`" in section(text, "RECORDS")


def test_no_fix_report_leaves_every_cell_empty(tmp_path):
    """Green on BASE and after: a row with no --fix-report is the `:147` row of today."""
    desk = Desk(tmp_path)
    done = desk.run()
    assert done.returncode == 0, done.stderr
    text = desk.out.read_text()
    for n, name in enumerate(("alpha", "beta"), start=1):
        assert ships_row(text, n) == (
            f"| {n} | `ops/{name}` | `{desk.tip[name]}` | `{desk.head[name]}` | `{desk.check[name]}` "
            "| `held unfixed: 0` and `ready: YES` | |"
        )


def _fix_refused(desk: Desk, extra: tuple[str, ...], reason: str) -> None:
    before = desk.state()
    done = desk.run(*extra)
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {reason}" in done.stderr, done.stderr
    assert not desk.out.exists()
    assert desk.state() == before


def test_a_fix_report_absent_at_the_head_is_refused(tmp_path):
    desk = Desk(tmp_path)
    fixed, head, report = fix_round(desk, on_head=False)
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: the fix report is absent at the branch head {head}: {report}")


def test_a_fix_report_whose_last_line_is_not_built_is_refused(tmp_path):
    desk = Desk(tmp_path)
    fixed, head, report = fix_round(desk, last="FAILED: W — x · tip: FIXED")
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: the fix report's last line is not 'BUILT ·' with a 'tip:': FAILED: W — x · tip: {fixed}")


def test_a_fix_tip_not_past_the_check_tip_is_refused(tmp_path):
    desk = Desk(tmp_path)
    base = git(desk.repo, "merge-base", "main", "ops/alpha")[:8]
    fixed, head, report = fix_round(desk, last=f"BUILT · job: x · tip: {base} | rows: 1 of 1")
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: the check's tip {desk.tip['alpha']} is not an ancestor of the fix tip {base}")


def test_a_fix_report_for_an_unknown_job_is_refused(tmp_path):
    desk = Desk(tmp_path)  # alpha and beta clean: only the unknown job can refuse
    _fix_refused(desk, ("--fix-report", f"gamma={desk.reports / 'gamma-fix.md'}"),
                 "--fix-report names job 'gamma', which is no JOB of the job cards given")


def test_a_fix_report_outside_the_reports_folder_is_refused(tmp_path):
    desk = Desk(tmp_path)
    fixed, head, report = fix_round(desk)
    stray = desk.prompts / "alpha-fix.md"
    _fix_refused(desk, ("--fix-report", f"alpha={stray}"),
                 f"alpha: --fix-report path is not {desk.reports}/<name>.md: {stray}")


@pytest.mark.parametrize("value, reason", [
    ("alpha", "--fix-report 'alpha' must be <job>=<fix report path>"),
    ("Alpha={reports}/a.md", "--fix-report job 'Alpha' must be [a-z0-9-]"),
    ("alpha={reports}/../a.md", "alpha: --fix-report path holds '..'"),
    ("alpha={reports}/a.md\nbeta={reports}/b.md", "--fix-report holds a line break"),
    ("alpha={reports}/a.txt", "alpha: --fix-report path is not"),
])
def test_a_fix_report_value_outside_its_shape_is_refused(tmp_path, value, reason):
    desk = Desk(tmp_path)
    _fix_refused(desk, ("--fix-report", value.format(reports=desk.reports)), reason)


def test_a_fix_report_naming_one_job_twice_is_refused(tmp_path):
    desk = Desk(tmp_path)
    fixed, head, report = fix_round(desk)
    _fix_refused(desk, ("--fix-report", f"alpha={report}", "--fix-report", f"alpha={report}"),
                 "--fix-report names job 'alpha' twice")


def test_check_o1_an_empty_fix_report_value_is_refused(tmp_path):
    desk = Desk(tmp_path)
    _fix_refused(desk, ("--fix-report", ""), "--fix-report '' must be <job>=<fix report path>")


def test_check_o2_a_fix_report_path_with_a_pipe_is_refused(tmp_path):
    desk = Desk(tmp_path)
    fixed, head, report = fix_round(desk)
    git(desk.repo, "checkout", "-q", "ops/alpha")
    piped = desk.reports / "alpha|fix.md"
    piped.write_text(f"# alpha fix round\n\nBUILT · job: x · tip: {fixed} | rows: 1 of 1\n")
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", "alpha piped fix report")
    git(desk.repo, "checkout", "-q", "main")
    _fix_refused(desk, ("--fix-report", f"alpha={piped}"), "alpha: --fix-report path holds")


def test_a_fix_report_round_trips_through_the_launchers_ships_checked(tmp_path):
    """The card written for a fix round passes desk-launch.sh's `ships_checked` (P2, P3): the
    code tip is the fix report's `tip:`, the check's tip its ancestor. RED on BASE: the option
    is refused, so no card exists to launch."""
    proof = ("\n## DEPLOY PROOF\n- `grep -c -F \"alpha = 2\" /x/src/alpha.py` · before `0` · after `1`\n"
             "- alpha read · `ls /x/src/alpha.py` · listed\n")
    desk = Desk(tmp_path, proof=proof)
    hub = desk.prompts.parent / "DEPLOY-HUB.md"
    hub.write_text((REPO / "docs" / "40 - DevDocs" / "prompts" / "DEPLOY-HUB.md").read_text())
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", "the fixed deploy file")
    fixed, head, report = fix_round(desk)
    done = desk.run("--fix-report", f"alpha={report}", cards=("alpha",))
    assert done.returncode == 0, done.stderr
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", "deploy card")
    launch = subprocess.run(
        ["sh", str(LAUNCH), "deploy", str(desk.out)], env=dict(desk.env, DESK_LAUNCH_DRY="1"),
        capture_output=True, text=True, timeout=120,
    )
    assert launch.returncode == 0, launch.stderr
    assert "REFUSED" not in launch.stderr, launch.stderr
    assert f"git -C {desk.repo} worktree add -b deploy/x-set {desk.wt}/x-gate main" in launch.stdout


# ---- card 317 H1: a held check writes its fix-round row (THE RULE, R993) -----------------------

HELD_RUN = ("- {id} · own · `uv run pytest -q tests/x.py` · `1 failed` · "
            "**HELD, NOT FIXED — `ops/x.sh:1`** (constructed)")
PLAIN_TEST = "import pytest\n\n\ndef test_o1():\n    assert True\n"
STRICT_TEST = ('import pytest\n\n\n@pytest.mark.xfail(strict=True, reason="carried")\n'
               "def test_o1():\n    assert False\n")
DESK_ROW = "| R7 | 09:00 ET | DESK RECORD (brain, L79): O1 is carried (constructed). | DESK RECORD |"
FIXED_O1 = "FIXED: O1 — tests/x.py::test_o1"
CARRIED_O1 = "CARRIED: O1 — tests/x.py::test_o1 — R7"


def held_round(desk: Desk, *, lines: list[str], tests: dict[str, str] | None = None,
               runs: tuple[str, ...] = ("O1",), held: str = "1", open: str | None = None,
               desk_rows: tuple[str, ...] = (DESK_ROW,),
               runs_text: str | None = None, last: str | None = None) -> tuple[str, str, Path]:
    """Alpha's check lists `runs` as `HELD, NOT FIXED` rows under `## RUNS` (or carries
    `runs_text` there instead, when given) and its last line (`last`, when given)
    says `held unfixed: <held>`, `open: <open>` (default `held`), `ready: NO`. A fix round then
    moves alpha's code past the check, writing `tests` (path → text) in the fix commit; its fix
    report, on the branch head only, carries `lines` above its `BUILT ·` line. The check report
    is dated (`alpha-check-2026-01-02.md`), and the day's desk report `cto-2026-01-02.md` holds
    `desk_rows`. Returns (fix tip, head, fix report path)."""
    tests = {"tests/x.py": PLAIN_TEST} if tests is None else tests
    git(desk.repo, "checkout", "-q", "ops/alpha")
    (desk.repo / "src" / "alpha.py").write_text("alpha = 2\n")
    for rel, text in tests.items():
        (desk.repo / rel).parent.mkdir(parents=True, exist_ok=True)
        (desk.repo / rel).write_text(text)
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", "alpha small fix")
    fixed = git(desk.repo, "rev-parse", "--short=8", "HEAD")
    report = desk.reports / "alpha-fix.md"
    report.write_text("# alpha fix round\n\n" + "".join(f"{ln}\n" for ln in lines)
                      + f"\nBUILT · job: x · tip: {fixed} | rows: 1 of 1\n")
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", "alpha fix report")
    head = git(desk.repo, "rev-parse", "--short=8", "HEAD")
    git(desk.repo, "checkout", "-q", "main")
    assert not report.exists()
    check = desk.reports / "alpha-check-2026-01-02.md"
    if runs_text is None:
        runs_text = "".join(HELD_RUN.format(id=i) + "\n" for i in runs)
    check.write_text(f"# check alpha\n\n## RUNS\n{runs_text}\n## OPEN\n- constructed\n\n"
                     + (f"{last}\n" if last is not None
                        else check_line(desk.tip["alpha"], "NO", held, held if open is None else open)))
    desk.card["alpha"].write_text(desk.card["alpha"].read_text().replace(str(desk.check["alpha"]), str(check)))
    desk.check["alpha"] = check
    (desk.reports / "cto-2026-01-02.md").write_text(
        "| # | time | row | status |\n|---|---|---|---|\n" + "".join(f"{r}\n" for r in desk_rows))
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", "alpha held check, card and desk report")
    return fixed, head, report


def held_cells(desk: Desk) -> list[str]:
    return [c.strip() for c in ships_row(desk.out.read_text(), 1).split("|")]


def test_h1_a_held_check_with_a_fixed_line_per_id_writes_the_card(tmp_path):
    """RED on BASE: exit 1, `REFUSED: alpha: the check's last line lacks 'held unfixed: 0'`."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=[FIXED_O1])
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
    cells = held_cells(desk)
    assert cells[3] == f"`{fixed}`", cells
    assert cells[4] == f"`{head}`", cells
    assert cells[5] == f"`{desk.check['alpha']}`", cells
    assert cells[6] == "`held unfixed: 1` and `ready: NO`", cells
    assert cells[7] == f"`{report}`", cells
    assert ships_row(desk.out.read_text(), 2).endswith("| `held unfixed: 0` and `ready: YES` | |")


def test_h1_a_carried_line_with_a_strict_xfail_test_and_a_desk_record_row_writes_the_card(tmp_path):
    """RED on BASE: exit 1, `REFUSED: alpha: the check's last line lacks 'held unfixed: 0'`."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=[CARRIED_O1], tests={"tests/x.py": STRICT_TEST})
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
    cells = held_cells(desk)
    assert cells[3] == f"`{fixed}`", cells
    assert cells[6] == "`held unfixed: 1` and `ready: NO`", cells
    assert cells[7] == f"`{report}`", cells


def test_h1_a_mix_of_one_fixed_and_one_carried_id_writes_the_card(tmp_path):
    """RED on BASE: exit 1, `REFUSED: alpha: the check's last line lacks 'held unfixed: 0'`."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(
        desk, runs=("O1", "O2"), held="2",
        lines=[FIXED_O1, "CARRIED: O2 — tests/y.py::test_o2 — R7"],
        tests={"tests/x.py": PLAIN_TEST, "tests/y.py": STRICT_TEST.replace("test_o1", "test_o2")})
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
    cells = held_cells(desk)
    assert cells[6] == "`held unfixed: 2` and `ready: NO`", cells
    assert cells[7] == f"`{report}`", cells


XFAIL_TEST = '@pytest.mark.xfail(reason="not yet")\ndef test_o1():\n    assert False\n'


@pytest.mark.parametrize("kw, reason", [
    pytest.param({"lines": []}, "alpha: held id O1 has no FIXED line in the fix report {report}",
                 id="a held id with no line"),
    pytest.param({"lines": [FIXED_O1, "FIXED: O2 — tests/x.py::test_o1"]},
                 "alpha: the fix report {report} names O2, which is no HELD, NOT FIXED id of the check {check}",
                 id="a line for an unlisted id"),
    pytest.param({"lines": [FIXED_O1, FIXED_O1]},
                 "alpha: held id O1 has 2 FIXED or CARRIED lines in the fix report {report}",
                 id="two lines for one id"),
    pytest.param({"lines": [FIXED_O1], "tests": {}},
                 "alpha: FIXED test tests/x.py::test_o1 of O1 is absent at {fixed}", id="test file absent"),
    pytest.param({"lines": [FIXED_O1], "tests": {"tests/x.py": "def test_other():\n    pass\n"}},
                 "alpha: FIXED test tests/x.py::test_o1 of O1 is absent at {fixed}", id="def absent"),
    pytest.param({"lines": [FIXED_O1], "tests": {"tests/x.py": "import pytest\n\n\n" + XFAIL_TEST}},
                 "alpha: FIXED test tests/x.py::test_o1 of O1 is marked xfail", id="xfail decorator"),
    pytest.param({"lines": [FIXED_O1], "tests": {"tests/x.py": "import pytest\n\npytestmark = pytest.mark.xfail\n\n\n"
                                                               "def test_o1():\n    assert True\n"}},
                 "alpha: FIXED test tests/x.py::test_o1 of O1 is marked xfail", id="pytestmark xfail"),
    pytest.param({"lines": [FIXED_O1], "runs": ("O1", "O2")},
                 "alpha: the check {check} lists 2 HELD, NOT FIXED row(s) under ## RUNS (O1 O2), "
                 "its last line says 'held unfixed: 1'", id="held rows not n"),
    pytest.param({"lines": [FIXED_O1], "open": "0"},
                 "alpha: the check's last line says 'held unfixed: 1' (held ids: O1) but not 'open: 1'",
                 id="open not n"),
    # check ask X3: the grammar is exact
    pytest.param({"lines": ["FIXED: O1 - tests/x.py::test_o1"]},
                 "alpha: held id O1 has no FIXED line in the fix report {report}", id="an ASCII hyphen"),
    pytest.param({"lines": ["  " + FIXED_O1]},
                 "alpha: held id O1 has no FIXED line in the fix report {report}", id="an indented line"),
    pytest.param({"lines": [FIXED_O1], "runs": ("O 1",)},
                 "alpha: the check {check} lists 0 HELD, NOT FIXED row(s) under ## RUNS (none), "
                 "its last line says 'held unfixed: 1'", id="an id with a space"),
    pytest.param({"lines": [FIXED_O1], "held": "10"},
                 "alpha: the check {check} lists 1 HELD, NOT FIXED row(s) under ## RUNS (O1), "
                 "its last line says 'held unfixed: 10'", id="held unfixed 10 is not 1"),
])
def test_h1_a_held_check_missing_one_proof_is_refused(tmp_path, kw, reason):
    """RED on BASE for each: `REFUSED: alpha: the check's last line lacks 'held unfixed: 0'`."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, **kw)
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 reason.format(report=report, fixed=fixed, check=desk.check["alpha"]))


@pytest.mark.parametrize("kw, reason", [
    pytest.param({"tests": {"tests/x.py": PLAIN_TEST}},
                 "alpha: CARRIED test tests/x.py::test_o1 of O1 is not a strict xfail", id="test not xfail"),
    pytest.param({"tests": {"tests/x.py": "import pytest\n\n\n" + XFAIL_TEST}},
                 "alpha: CARRIED test tests/x.py::test_o1 of O1 is not a strict xfail", id="xfail not strict"),
    pytest.param({"tests": {"tests/x.py": STRICT_TEST.replace("strict=True", "strict=False")}},
                 "alpha: CARRIED test tests/x.py::test_o1 of O1 is not a strict xfail", id="strict=False"),
    pytest.param({"tests": {"tests/x.py": 'import pytest\n\npytestmark = pytest.mark.xfail(strict=True)\n\n\n'
                                          "def test_o1():\n    assert False\n"}},
                 "alpha: CARRIED test tests/x.py::test_o1 of O1 is not a strict xfail", id="a pytestmark only"),
    pytest.param({"tests": {}}, "alpha: CARRIED test tests/x.py::test_o1 of O1 is absent at {fixed}",
                 id="test file absent"),
    pytest.param({"tests": {"tests/x.py": "def test_other():\n    pass\n"}},
                 "alpha: CARRIED test tests/x.py::test_o1 of O1 is absent at {fixed}", id="def absent"),
    pytest.param({"desk_rows": ()},
                 "alpha: CARRIED O1 names R7, which is no DESK RECORD row of {desk}", id="row absent"),
    pytest.param({"desk_rows": ("| R7 | 09:00 ET | a note on O1 (constructed). | APPLIED |",)},
                 "alpha: CARRIED O1 names R7, which is no DESK RECORD row of {desk}", id="row without DESK RECORD"),
    pytest.param({"lines": [FIXED_O1, CARRIED_O1]},
                 "alpha: held id O1 has 2 FIXED or CARRIED lines in the fix report {report}",
                 id="one FIXED and one CARRIED line for one id"),
])
def test_h1_a_carried_line_missing_one_proof_is_refused(tmp_path, kw, reason):
    """RED on BASE for each: `REFUSED: alpha: the check's last line lacks 'held unfixed: 0'`."""
    desk = Desk(tmp_path)
    kw = {"lines": [CARRIED_O1], "tests": {"tests/x.py": STRICT_TEST}, **kw}
    fixed, head, report = held_round(desk, **kw)
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 reason.format(report=report, fixed=fixed, desk=desk.reports / "cto-2026-01-02.md"))


def test_h1_held_check_without_a_fix_report_is_still_refused(tmp_path):
    """Pin, green on BASE and after: no --fix-report, so `:172` refuses as today."""
    desk = Desk(tmp_path)
    held_round(desk, lines=[FIXED_O1])
    _fix_refused(desk, (), "alpha: the check's last line lacks 'held unfixed: 0': CHECK DONE")


RULE_START = "# ---- THE RULE (card 317"
RULE_END = "# ---- end of THE RULE"


def rule_text(path: Path) -> str:
    text = path.read_text()
    start = text.index(RULE_START)
    return text[start:text.index(RULE_END, start)]


def test_h1_the_rule_is_one_text_in_the_three_scripts():
    """Check ask X4, L3: deploy-card.sh, desk-launch.sh and deploy-step0.sh read THE RULE through
    one text, byte for byte. RED on BASE: no script holds it."""
    texts = [rule_text(REPO / "ops" / "desk" / name)
             for name in ("deploy-card.sh", "desk-launch.sh", "deploy-step0.sh")]
    assert "held_rule() {" in texts[0]
    assert texts[0] == texts[1] == texts[2]


# ---- card 397 G1: a held id is read from ## RUNS or ## FIXES (R1157 (1)) ----------------------

HELD_ALONE_RUN = "- {id} · own · `uv run pytest -q tests/x.py` · `1 failed` · **HELD**."
FIXES_HELD = "- {id}: **HELD, NOT FIXED — `ops/x.sh`**"
G1_RUNS = HELD_ALONE_RUN.format(id="O1") + "\n\n## FIXES\n" + FIXES_HELD.format(id="O1") + "\n"
CHECK_386 = "docs/40 - DevDocs/reports/launcher-shadow-check-check-2026-10-11.md"


def test_g1_a_held_id_under_fixes_closed_by_its_fixed_line_writes_the_card(tmp_path):
    """RED on BASE: exit 1, `REFUSED: alpha: the check … lists 0 HELD, NOT FIXED row(s) under
    ## RUNS (none), its last line says 'held unfixed: 1'`."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=[FIXED_O1], runs_text=G1_RUNS)
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
    assert held_cells(desk)[6] == "`held unfixed: 1` and `ready: NO`"


def test_g1_the_386_check_lines_and_its_f1_line_write_the_card(tmp_path):
    """Card 386's check `## RUNS` and `## FIXES` (`:163-173`), its corrected stop line (`:230`,
    `tip:` set to the fixture's) and its F1 line (the fixture's plain test). RED on BASE: the
    same `lists 0 … (none)` refusal."""
    text = git(REPO, "show", f"HEAD:{CHECK_386}").splitlines()
    assert (text[162], text[171]) == ("## RUNS", "## FIXES")
    runs_text = "".join(f"{ln}\n" for ln in text[163:173])
    last = [ln for ln in text if ln.strip()][-1]
    assert " · tip: a8c18242 · " in last and " · held unfixed: 1 · open: 1 · " in last
    desk = Desk(tmp_path)
    fixed, head, report = held_round(
        desk, lines=["FIXED: G3 — tests/x.py::test_o1"], runs_text=runs_text,
        last=last.replace(" · tip: a8c18242 · ", f" · tip: {desk.tip['alpha']} · "))
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
    assert held_cells(desk)[6] == "`held unfixed: 1` and `ready: NO`"


def test_g1_a_held_id_under_fixes_with_no_fixed_line_is_refused(tmp_path):
    """Exit 1 on BASE (`lists 0 … (none)`) and after, for the reason below."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=[], runs_text=G1_RUNS)
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: held id O1 has no FIXED line in the fix report {report}")


def test_g1_a_fixed_line_naming_an_absent_test_is_refused(tmp_path):
    """Exit 1 on BASE (`lists 0 … (none)`) and after, for the reason below."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=[FIXED_O1], runs_text=G1_RUNS,
                                     tests={"tests/x.py": "def test_other():\n    pass\n"})
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: FIXED test tests/x.py::test_o1 of O1 is absent at {fixed}")


@pytest.mark.parametrize("held, reason", [
    pytest.param("1", "alpha: the check {check} lists 2 HELD, NOT FIXED row(s) under ## RUNS and ## FIXES "
                      "(O1 O1), its last line says 'held unfixed: 1'", id="n 1"),
    pytest.param("2", "alpha: the check {check} lists a held id twice under ## FIXES (O1 O1)", id="n 2"),
])
def test_g1_an_id_twice_under_fixes_is_refused(tmp_path, held, reason):
    """Exit 1 on BASE (`lists 0 … (none)`) and after, for the reason given."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=[FIXED_O1], held=held,
                                     runs_text=G1_RUNS + FIXES_HELD.format(id="O1") + "\n")
    _fix_refused(desk, ("--fix-report", f"alpha={report}"), reason.format(check=desk.check["alpha"]))


def test_g1_the_rule_header_names_card_397_once():
    """The card's DEPLOY PROOF: `grep -c -F "card 397"` → 1 in each script, in THE RULE's header
    comment. RED on BASE: `assert 0 == 1`."""
    for name in ("deploy-card.sh", "desk-launch.sh", "deploy-step0.sh"):
        text = (REPO / "ops" / "desk" / name).read_text()
        assert text.count("card 397") == 1, name
        header = rule_text(REPO / "ops" / "desk" / name).split("\nheld_n() {")[0]
        assert "card 397" in header, name


def test_g1_an_id_held_in_both_sections_counts_once(tmp_path):
    """Pin, green on BASE and after: a `HELD, NOT FIXED` RUNS bullet and its FIXES row are one id."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(
        desk, lines=[FIXED_O1],
        runs_text=HELD_RUN.format(id="O1") + "\n\n## FIXES\n" + FIXES_HELD.format(id="O1") + "\n")
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr


# ---- card 397 G2: `open:` past held unfixed is settled by a desk record (R1157 (2), R1160) -------

REJECTED_RUN = "- {id} · own · `uv run pytest -q tests/x.py` · `1 failed` · **REJECTED — row X1 \"constructed\"**"
G2_RUNS = "".join(f"{r}\n" for r in (HELD_RUN.format(id="O1"), REJECTED_RUN.format(id="O2"),
                                     REJECTED_RUN.format(id="O3")))
SETTLED_O2 = "SETTLED: O2 — R7"
SETTLED_O3 = "SETTLED: O3 — R7"


def desk_day(desk: Desk, name: str, *rows: str) -> Path:
    """One more desk report, `name` under the reports folder, holding `rows`, committed on main."""
    path = desk.reports / name
    path.write_text("| # | time | row | status |\n|---|---|---|---|\n" + "".join(f"{r}\n" for r in rows))
    git(desk.repo, "add", "-A")
    git(desk.repo, "commit", "-q", "-m", f"desk report {name}")
    return path


def test_g2_rejected_ids_settled_by_a_desk_record_are_not_counted_open(tmp_path):
    """RED on BASE: `REFUSED: alpha: the check's last line says 'held unfixed: 1' (held ids: O1)
    but not 'open: 1'`."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, open="3", runs_text=G2_RUNS,
                                     lines=[FIXED_O1, SETTLED_O2, SETTLED_O3])
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
    assert held_cells(desk)[6] == "`held unfixed: 1` and `ready: NO`"


def test_g2_an_unsettled_table_row_is_settled_like_a_rejected_bullet(tmp_path):
    """RED on BASE: `… but not 'open: 1'`."""
    desk = Desk(tmp_path)
    rows = (HELD_RUN.format(id="O1") + "\n" + TABLE_HEAD
            + "| O2 | own | `tests/x.py::test_o2` | `1 failed` | UNSETTLED — not on the list (constructed) |\n")
    fixed, head, report = held_round(desk, open="2", runs_text=rows, lines=[FIXED_O1, SETTLED_O2])
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr


def test_g2_an_open_rejected_id_without_a_settled_line_is_refused(tmp_path):
    """Exit 1 on BASE (`not 'open: 1'`) and after, for the reason below."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, open="3", runs_text=G2_RUNS, lines=[FIXED_O1, SETTLED_O2])
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: 'open: 3' counts 2 open id(s) past held unfixed, 1 settled in the fix report {report}")


def test_g2_a_settled_line_naming_a_row_that_is_no_desk_record_is_refused(tmp_path):
    """Exit 1 on BASE (`not 'open: 1'`) and after, for the reason below."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, open="3", runs_text=G2_RUNS,
                                     lines=[FIXED_O1, SETTLED_O2, "SETTLED: O3 — R8"])
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: SETTLED O3 names R8, which is no DESK RECORD row of {desk.reports / 'cto-2026-01-02.md'}")


def test_g2_a_settled_line_naming_a_held_id_is_refused(tmp_path):
    """Exit 1 on BASE (`not 'open: 1'`) and after, for the reason below."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, open="3", runs_text=G2_RUNS,
                                     lines=[FIXED_O1, SETTLED_O2, "SETTLED: O1 — R7"])
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: the fix report {report} settles O1, which is a held id of the check {desk.check['alpha']}")


@pytest.mark.parametrize("kw, reason", [
    pytest.param({"open": "3", "lines": [FIXED_O1, SETTLED_O2, SETTLED_O3, SETTLED_O3]},
                 "alpha: SETTLED O3 has 2 SETTLED lines in the fix report {report}", id="two lines for one id"),
    pytest.param({"open": "2", "lines": [FIXED_O1, SETTLED_O2, "SETTLED: O4 — R7"],
                  "runs_text": G2_RUNS + "- O4 · own · `x` · `1 passed` · **NOT HELD**\n"},
                 "alpha: the fix report {report} settles O4, which is no REJECTED or UNSETTLED id under "
                 "## RUNS of the check {check}", id="a NOT HELD id"),
    pytest.param({"open": "2", "lines": [FIXED_O1, SETTLED_O2, "SETTLED: O9 — R7"]},
                 "alpha: the fix report {report} settles O9, which is no REJECTED or UNSETTLED id under "
                 "## RUNS of the check {check}", id="an id the check does not list"),
    pytest.param({"open": "1", "lines": [FIXED_O1, SETTLED_O2]},
                 "alpha: 'open: 1' counts 0 open id(s) past held unfixed, 1 settled in the fix report {report}",
                 id="a settled line with open equal to n"),
    pytest.param({"open": "4", "lines": [FIXED_O1, SETTLED_O2, SETTLED_O3]},
                 "alpha: 'open: 4' counts 3 open id(s) past held unfixed, 2 settled in the fix report {report}",
                 id="fewer settled than m - n"),
])
def test_g2_a_settled_line_missing_one_proof_is_refused(tmp_path, kw, reason):
    """Check ask X2. Exit 1 on BASE (`not 'open: 1'`, or `open: 1` with no SETTLED read at all
    for `a settled line with open equal to n`) and after, for the reason given."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, **{"runs_text": G2_RUNS, **kw})
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 reason.format(report=report, check=desk.check["alpha"]))


def test_g2_open_below_held_unfixed_keeps_todays_text(tmp_path):
    """Pin, green on BASE and after: `open: 0` against `held unfixed: 1`."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, open="0", lines=[FIXED_O1])
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 "alpha: the check's last line says 'held unfixed: 1' (held ids: O1) but not 'open: 1'")


# ---- R1160 (the brain row): R<k> is found in a desk report dated on or after the check ----------

def test_g2_a_settled_row_recorded_the_next_day_is_accepted(tmp_path):
    """RED on BASE: `… but not 'open: 1'`."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, open="3", runs_text=G2_RUNS, desk_rows=(),
                                     lines=[FIXED_O1, SETTLED_O2, SETTLED_O3])
    desk_day(desk, "cto-2026-01-03.md", DESK_ROW)
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr


def test_g2_a_carried_row_recorded_the_next_day_is_accepted(tmp_path):
    """RED on BASE: `REFUSED: alpha: CARRIED O1 names R7, which is no DESK RECORD row of
    …/cto-2026-01-02.md`."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=[CARRIED_O1], tests={"tests/x.py": STRICT_TEST}, desk_rows=())
    desk_day(desk, "cto-2026-01-03.md", DESK_ROW)
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr


@pytest.mark.parametrize("days, lines", [
    pytest.param((("cto-2026-01-01.md", DESK_ROW),), [CARRIED_O1], id="CARRIED, the day before"),
    pytest.param((("cto-2026-01-03-words.md", DESK_ROW),), [CARRIED_O1], id="CARRIED, a words file"),
    pytest.param((("cto-2026-01-03.md", "| R7 | 09:00 ET | a note on O1 (constructed). | APPLIED |"),
                  ("cto-2026-01-02.md", DESK_ROW)), [CARRIED_O1], id="CARRIED, newest first"),
    pytest.param((), [CARRIED_O1], id="CARRIED, in no desk report"),
    pytest.param((("cto-2026-01-01.md", DESK_ROW),), [FIXED_O1, SETTLED_O2, SETTLED_O3],
                 id="SETTLED, the day before"),
    pytest.param((), [FIXED_O1, SETTLED_O2, SETTLED_O3], id="SETTLED, in no desk report"),
])
def test_g2_a_row_outside_the_days_on_or_after_the_check_is_refused(tmp_path, days, lines):
    """Exit 1 on BASE and after: R7 is no DESK RECORD row found on or after the check's day."""
    desk = Desk(tmp_path)
    settled = lines[0] == FIXED_O1
    fixed, head, report = held_round(
        desk, lines=lines, desk_rows=(),
        **({"open": "3", "runs_text": G2_RUNS} if settled else {"tests": {"tests/x.py": STRICT_TEST}}))
    for name, row in days:
        desk_day(desk, name, row)
    who = "SETTLED O2" if settled else "CARRIED O1"
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 f"alpha: {who} names R7, which is no DESK RECORD row of {desk.reports / 'cto-2026-01-02.md'}")


# ---- card 361 T1: the held-id read takes a table row marked **HELD** (R1084) -------------------

TABLE_HEAD = "| id | source | run | output | verdict |\n|---|---|---|---|---|\n"
TABLE_HELD = ("| {id} | own | `tests/x.py::test_o1`, alone | `1 failed` | "
              "**HELD** — red for its stated reason: `ops/x.sh:1` (constructed) |")
TABLE_NOT_HELD = ("| {id} | own | `tests/x.py::test_o2`, alone | `1 passed` | "
                  "NOT HELD — green on the tip (constructed) |")


def test_t1_a_bullet_row_is_still_counted(tmp_path):
    """Pin, GREEN on BASE and after: the bullet form reads as before."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=[FIXED_O1], runs_text=HELD_RUN.format(id="O1") + "\n")
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
    assert held_cells(desk)[6] == "`held unfixed: 1` and `ready: NO`"


def test_t1_a_table_row_marked_held_is_counted(tmp_path):
    """RED on BASE: exit 1, `lists 0 HELD, NOT FIXED row(s) under ## RUNS (none)`."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=[FIXED_O1],
                                     runs_text=TABLE_HEAD + TABLE_HELD.format(id="O1") + "\n")
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
    cells = held_cells(desk)
    assert cells[3] == f"`{fixed}`", cells
    assert cells[4] == f"`{head}`", cells
    assert cells[6] == "`held unfixed: 1` and `ready: NO`", cells
    assert cells[7] == f"`{report}`", cells


@pytest.mark.parametrize("rows, ok", [
    pytest.param(TABLE_HELD.format(id="O1") + "\n" + TABLE_NOT_HELD.format(id="O2") + "\n", True,
                 id="one held and one not held"),
    pytest.param(TABLE_NOT_HELD.format(id="O1") + "\n" + TABLE_NOT_HELD.format(id="O2") + "\n", False,
                 id="not held only"),
])
def test_t1_a_table_row_marked_not_held_is_ignored(tmp_path, rows, ok):
    """`one held and one not held` RED on BASE (`lists 0`); `not held only` GREEN on BASE and
    after: refused with `lists 0 … (none)`."""
    desk = Desk(tmp_path)
    fixed, head, report = held_round(desk, lines=[FIXED_O1], runs_text=TABLE_HEAD + rows)
    if ok:
        done = desk.run("--fix-report", f"alpha={report}")
        assert done.returncode == 0, done.stderr
        assert held_cells(desk)[6] == "`held unfixed: 1` and `ready: NO`"
    else:
        _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                     f"alpha: the check {desk.check['alpha']} lists 0 HELD, NOT FIXED row(s) under "
                     "## RUNS (none), its last line says 'held unfixed: 1'")


def test_t1_a_mixed_report_counts_both_forms(tmp_path):
    """RED on BASE: `lists 1 HELD, NOT FIXED row(s) under ## RUNS (O1), … 'held unfixed: 2'`."""
    desk = Desk(tmp_path)
    rows = (HELD_RUN.format(id="O1") + "\n" + TABLE_HEAD + TABLE_HELD.format(id="O2") + "\n"
            + TABLE_NOT_HELD.format(id="O3") + "\n")
    fixed, head, report = held_round(
        desk, held="2", runs_text=rows,
        lines=[FIXED_O1, "FIXED: O2 — tests/y.py::test_o2"],
        tests={"tests/x.py": PLAIN_TEST, "tests/y.py": PLAIN_TEST.replace("test_o1", "test_o2")})
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 0, done.stderr
    assert held_cells(desk)[6] == "`held unfixed: 2` and `ready: NO`"


# ---- check of card 317: THE RULE's decorator read (O1 O2, house A 1, house B 1 2) -------------

def test_check_o1_an_xfail_decorator_above_a_comment_is_still_xfail(tmp_path):
    desk = Desk(tmp_path)
    src = ('import pytest\n\n\n@pytest.mark.xfail(reason="not yet")\n'
           "# a constructed comment between the decorator and its def\n"
           "def test_o1():\n    assert False\n")
    fixed, head, report = held_round(desk, lines=[FIXED_O1], tests={"tests/x.py": src})
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 "alpha: FIXED test tests/x.py::test_o1 of O1 is marked xfail")


def test_check_o2_a_previous_functions_decorator_is_not_the_named_tests(tmp_path):
    desk = Desk(tmp_path)
    src = ('import pytest\n\n\n@pytest.mark.xfail(strict=True, reason="other")\n'
           "def test_other():\n    assert False\n"
           "def test_o1():\n    assert True\n")
    fixed, head, report = held_round(desk, lines=[CARRIED_O1], tests={"tests/x.py": src})
    _fix_refused(desk, ("--fix-report", f"alpha={report}"),
                 "alpha: CARRIED test tests/x.py::test_o1 of O1 is not a strict xfail")


def test_h1_a_fixed_line_uses_the_top_level_test_node(tmp_path):
    desk = Desk(tmp_path)
    source = (
        "import pytest\n\n"
        "def helper():\n"
        "    def test_o1():\n"
        "        return None\n"
        "    return test_o1\n\n"
        '@pytest.mark.xfail(strict=True, reason="still broken")\n'
        "def test_o1():\n"
        "    assert False\n"
    )
    fixed, head, report = held_round(
        desk, lines=[FIXED_O1], tests={"tests/x.py": source}
    )
    _fix_refused(
        desk,
        ("--fix-report", f"alpha={report}"),
        "alpha: FIXED test tests/x.py::test_o1 of O1 is marked xfail",
    )


def test_h1_a_carried_class_decorator_is_not_the_defs_decorator(tmp_path):
    desk = Desk(tmp_path)
    src = (
        "import pytest\n\n\n"
        "@pytest.mark.xfail(strict=True, reason='carried')\n"
        "class T:\n"
        "    def test_o1(self):\n"
        "        assert False\n"
    )
    fixed, head, report = held_round(desk, lines=[CARRIED_O1], tests={"tests/x.py": src})
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 1, done.stderr
    assert "alpha: CARRIED test tests/x.py::test_o1 of O1 is not a strict xfail" in done.stderr, done.stderr
    assert not desk.out.exists()


def test_h1_an_indented_pytestmark_xfail_still_marks_the_fixed_test(tmp_path):
    desk = Desk(tmp_path)
    src = (
        "import pytest\n\n\n"
        "class T:\n"
        "    pytestmark = pytest.mark.xfail\n"
        "    def test_o1(self):\n"
        "        assert True\n"
    )
    fixed, head, report = held_round(desk, lines=[FIXED_O1], tests={"tests/x.py": src})
    done = desk.run("--fix-report", f"alpha={report}")
    assert done.returncode == 1, done.stderr
    assert "alpha: FIXED test tests/x.py::test_o1 of O1 is marked xfail" in done.stderr, done.stderr
    assert not desk.out.exists()


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
