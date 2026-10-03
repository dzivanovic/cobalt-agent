"""ops/desk/deploy-step0.sh — DEPLOY-HUB.md STEP-0 as one table (card 20 deploy-steps, row D1).

Every run points the script at a tmp repo standing in for /Users/cobalt/cobalt
(COBALT_REPO_ROOT): a fixed DEPLOY-HUB.md whose title cites its standing-list row, committed
desk reports with approved rows, two job branches (a code commit, then a docs commit past it),
their committed check reports and a committed deploy card. `launchctl` and `date` are stubs on
PATH: `launchctl` records its arguments and answers a census; `date` prints FAKE_NOW in the
asked format. The real repo, launchd and the network are never touched.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "ops" / "desk" / "deploy-step0.sh"
REAL_CARD = REPO / "docs" / "40 - DevDocs" / "prompts" / "2026-10-02" / "25-deploy-scripts-card.md"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

SATURDAY_1400 = "2026-01-03T14:00:00-05:00"
THURSDAY_1400 = "2026-01-08T14:00:00-05:00"

RECORD = f"""#!{sys.executable}
import json, os, sys
with open(os.path.join(os.environ["STUB_CALLS"], "{{name}}.jsonl"), "a") as f:
    f.write(json.dumps(sys.argv[1:]) + "\\n")
"""

LAUNCHCTL = """
args = sys.argv[1:]
if args[:1] == ["print"]:
    label = args[1].split("/")[-1]
    pids = {"com.cobalt.aset": 4101, "com.cobalt.radar": 4102, "com.cobalt.agent": 4103}
    print(f"gui/501/{label} = {{\\n\\tstate = running\\n\\tpid = {pids.get(label, 1)}\\n}}")
    sys.exit(0)
sys.exit(1)
"""

DATE = """
import datetime
now = datetime.datetime.fromisoformat(os.environ["FAKE_NOW"])
fmts = [a[1:] for a in sys.argv[1:] if a.startswith("+")]
fmt = fmts[0] if fmts else "%a %b %d %H:%M:%S %Z %Y"
print(now.strftime(fmt.replace("%s", str(int(now.timestamp())))))
"""

PLAIN = "sys.exit(0)\n"


def stub(bin_dir: Path, name: str, body: str) -> None:
    (bin_dir / name).write_text(RECORD.format(name=name) + body)
    (bin_dir / name).chmod(0o755)


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, GIT_OPTIONAL_LOCKS="0", **GIT_ENV),
        capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def check_line(tip: str, ready: str = "YES", held: str = "0") -> str:
    return (
        f"CHECK DONE · job: x · pass: 1 · tip: {tip} · held unfixed: {held} · open: 0"
        f" · ready: {ready} · decisions: 0 · for Dejan: 0\n"
    )


class Desk:
    """A tmp main repo with two checked job branches (alpha, beta) and a deploy card."""

    def __init__(self, tmp_path: Path, *, beta_migration: bool = False) -> None:
        root = tmp_path.resolve()
        self.root = root
        self.repo = root / "repo"
        self.wt = root / "wt"
        self.wt.mkdir()
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        (self.prompts / "2026-01-02").mkdir(parents=True)
        self.reports.mkdir(parents=True)
        (self.prompts / "DEPLOY-HUB.md").write_text(
            "# DEPLOY-HUB — the fixed deploy file (INSTALLED 2026-01-01 · STANDING = INSTALL: "
            "2026-01-01 R1 of his approval of STANDING-LIST.md)\n\nbody\n"
        )
        (self.reports / "cto-2026-01-01.md").write_text(
            "| row |\n| R1 | 09:00 ET | **HIS RULING**: approves the standing list. | APPROVED |\n"
        )
        self.write_rulings("| R2 | 09:05 ET | HIS RULING: the set ships. | HIS RULING · APPROVED |\n")
        mig = self.repo / "src" / "cobalt" / "db_migrations"
        mig.mkdir(parents=True)
        (mig / "0001_base.sql").write_text("-- base\n")
        (mig / "0001_base.rollback.sql").write_text("-- base back\n")
        (mig / "__init__.py").write_text("FORWARD = []\n")
        git(self.repo, "init", "-q", "-b", "main")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", "base")

        self.tip: dict[str, str] = {}
        self.head: dict[str, str] = {}
        for name in ("alpha", "beta"):
            git(self.repo, "checkout", "-q", "-b", f"ops/{name}", "main")
            (self.repo / "src" / f"{name}.py").write_text(f"{name} = 1\n")
            if name == "beta" and beta_migration:
                (mig / "0002_beta.sql").write_text("-- beta\n")
                (mig / "0002_beta.rollback.sql").write_text("-- beta back\n")
            git(self.repo, "add", "-A")
            git(self.repo, "commit", "-q", "-m", f"{name} code")
            self.tip[name] = git(self.repo, "rev-parse", "--short=8", "HEAD")
            (self.reports / f"{name}-build.md").write_text(f"BUILT · job: {name}\n")
            git(self.repo, "add", "-A")
            git(self.repo, "commit", "-q", "-m", f"{name} report")
            self.head[name] = git(self.repo, "rev-parse", "--short=8", "HEAD")
            git(self.repo, "checkout", "-q", "main")
        self.check = {n: self.reports / f"{n}-check.md" for n in ("alpha", "beta")}
        for name, path in self.check.items():
            path.write_text(f"# check {name}\n\n{check_line(self.tip[name])}\n")
        self.card = self.prompts / "2026-01-02" / "03-deploy-x-set-card.md"
        self.card.write_text(self.card_text())
        self.commit("checks and card")

        bin_dir = root / "bin"
        bin_dir.mkdir()
        self.calls = root / "calls"
        self.calls.mkdir()
        stub(bin_dir, "launchctl", LAUNCHCTL)
        stub(bin_dir, "date", DATE)
        self.bin = bin_dir
        self.env = dict(
            os.environ, COBALT_REPO_ROOT=str(self.repo), COBALT_WT_ROOT=str(self.wt),
            STUB_CALLS=str(self.calls), FAKE_NOW=SATURDAY_1400,
            PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}", **GIT_ENV,
        )

    def write_rulings(self, rows: str) -> None:
        (self.reports / "cto-2026-01-02.md").write_text("| row |\n" + rows)

    def card_text(self, *, migrations: str = "none", rulings: str = "2026-01-02 R2", records: str = "") -> str:
        ships = "".join(
            f"| {n} | `ops/{name}` | `{self.tip[name]}` | `{self.head[name]}` | `{self.check[name]}`"
            " | `held unfixed: 0` and `ready: YES` |\n"
            for n, name in enumerate(("alpha", "beta"), start=1)
        )
        return (
            "JOB: x-set\nLADDER: OFF-LADDER\nBRANCH: deploy/x-set\nWORKTREE: x-gate\nBASE: main\n"
            f"TIP: {self.head['alpha']} {self.head['beta']}\n"
            f"REPORT: {self.reports}/deploy-x-set.md\nRULINGS: {rulings}\nTAG: x-tag\n"
            f"MIGRATIONS: {migrations}\nSET: xset\n\n## SHIPS\n\n"
            "| # | branch | code tip | branch head | check report | its stop line must carry |\n"
            "|---|---|---|---|---|---|\n" + ships + "\n## MARKERS\n"
            "- `ls /nowhere/marker` · before `No such file or directory` · after listed\n\n"
            "## SMOKE READS\n- one · `ls /nowhere/marker` · exit 0, listed\n\n"
            f"## RECORDS\n- a desk fact\n{records}"
        )

    def commit(self, msg: str) -> None:
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", msg)

    def recard(self, **kw: str) -> None:
        self.card.write_text(self.card_text(**kw))
        self.commit("card")

    def run(self, *flags: str, now: str | None = None, env: dict | None = None) -> subprocess.CompletedProcess:
        e = dict(env or self.env)
        if now:
            e["FAKE_NOW"] = now
        return subprocess.run(
            ["sh", str(SCRIPT), *flags, str(self.card)], env=e, capture_output=True, text=True,
            errors="replace", timeout=120,
        )

    def calls_of(self, name: str) -> list[list[str]]:
        path = self.calls / f"{name}.jsonl"
        if not path.exists():
            return []
        return [json.loads(line) for line in path.read_text().splitlines()]

    def state(self) -> dict[str, str]:
        return {
            "status": git(self.repo, "status", "--porcelain"),
            "refs": git(self.repo, "for-each-ref", "--format=%(refname) %(objectname)"),
            "head": git(self.repo, "rev-parse", "HEAD"),
            "index": (self.repo / ".git" / "index").read_bytes().hex(),
        }


def last_line(done: subprocess.CompletedProcess) -> str:
    return [ln for ln in done.stdout.splitlines() if ln.strip()][-1]


@pytest.fixture
def desk(tmp_path):
    return Desk(tmp_path)


def test_a_clean_set_on_a_saturday_prints_the_table_and_step0_ok(desk):
    before = desk.state()
    done = desk.run()
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "STEP-0 OK — window: (iii)"
    rules = [ln.split(" · ")[0] for ln in done.stdout.splitlines() if " · " in ln]
    for rule in (
        "KEYS", "P0 authorization", "P1 window", "P2 check 1", "P2 check 2", "P2 committed 1",
        "P2 committed 2", "P3 tip 1", "P3 tip 2", "P7 migrations", "P8 census com.cobalt.aset",
        "P8 census com.cobalt.radar", "P8 census com.cobalt.agent", "disk", "main status",
    ):
        assert rule in rules, (rule, done.stdout)
    # every row carries its four fields: rule · command · exit · output
    for ln in done.stdout.splitlines():
        if ln.startswith(("KEYS", "P1", "P2", "P3", "P7", "P8", "disk", "main status")):
            assert len(ln.split(" · ")) >= 4, ln
    assert "pid 4101" in done.stdout
    # read-only: launchctl is only ever asked to print, and the tmp repo did not move
    assert desk.calls_of("launchctl")
    assert all(c[0] == "print" for c in desk.calls_of("launchctl"))
    assert desk.state() == before
    logs = list((desk.wt / ".deploy-logs").glob("x-set-step0-*.log"))
    assert len(logs) == 1 and "STEP-0 OK — window: (iii)" in logs[0].read_text()


def test_a_ready_no_check_report_fails_naming_the_rule(desk):
    desk.check["beta"].write_text(f"# check beta\n\n{check_line(desk.tip['beta'], ready='NO')}\n")
    desk.commit("beta not ready")
    done = desk.run()
    assert done.returncode == 1
    assert last_line(done).startswith("FAILED STEP-0: P2 check 2 — ")
    assert "ready: YES" in last_line(done)


def test_a_check_report_whose_tip_is_not_the_row_s_code_tip_fails(desk):
    desk.check["alpha"].write_text(f"# check alpha\n\n{check_line(desk.head['alpha'])}\n")
    desk.commit("alpha tip moved")
    done = desk.run()
    assert done.returncode == 1
    assert last_line(done).startswith("FAILED STEP-0: P2 check 1 — ")


def test_a_check_report_edited_after_its_commit_fails(desk):
    with desk.check["alpha"].open("a") as f:
        f.write("\nan edit after the commit\n" + check_line(desk.tip["alpha"]))
    done = desk.run()
    assert done.returncode == 1
    assert last_line(done).startswith("FAILED STEP-0: P2 committed 1 — ")


def test_a_migrations_mismatch_fails_naming_the_rule(tmp_path):
    desk = Desk(tmp_path, beta_migration=True)
    done = desk.run()
    assert done.returncode == 1
    assert last_line(done).startswith("FAILED STEP-0: P7 migrations — ")
    assert "0002" in last_line(done)
    # the card naming the number passes the same rule
    desk.recard(migrations="0002 · production at 0001 · creates: nothing · old code on the new schema: none")
    done = desk.run()
    assert done.returncode == 0, done.stdout
    assert last_line(done) == "STEP-0 OK — window: (iii)"


def test_a_rulings_row_without_approved_fails_naming_the_rule(desk):
    desk.write_rulings("| R2 | 09:05 ET | HIS RULING: the set ships. | HIS RULING · PROPOSED |\n")
    desk.commit("unapproved")
    done = desk.run()
    assert done.returncode == 1
    assert last_line(done) == (
        "FAILED STEP-0: P0 authorization — FAILED: authorization mismatch — RULING 2026-01-02 R2 row"
    )


def test_a_weekday_1400_with_no_override_fails_on_the_window(desk):
    done = desk.run(now=THURSDAY_1400)
    assert done.returncode == 1
    assert last_line(done) == "FAILED STEP-0: window — Thu 2026-01-08 14:00 ET"


def test_a_missing_key_fails_on_keys(desk):
    desk.card.write_text(desk.card_text().replace("TAG: x-tag\n", ""))
    desk.commit("no tag")
    done = desk.run()
    assert done.returncode == 1
    assert last_line(done).startswith("FAILED STEP-0: KEYS — ")
    assert "TAG" in last_line(done)


@pytest.mark.parametrize(
    "now, holds",
    [
        ("2026-01-08T20:30:00-05:00", "(i)"),     # Thursday pause
        ("2026-01-08T22:00:00-05:00", "(ii)"),    # Thursday overnight
        ("2026-01-09T02:00:00-05:00", "(ii)"),    # Friday small hours, after Thursday
        ("2026-01-10T02:00:00-05:00", "(ii)"),    # Saturday small hours, after Friday
        ("2026-01-11T22:00:00-05:00", "(iii)"),   # Sunday evening
        ("2026-01-12T03:59:00-05:00", "(iii)"),   # Monday before 04:00 counts as Sunday
        ("2026-12-01T02:00:00-05:00", "(ii)"),    # Tuesday small hours across a month end
        ("2026-03-01T14:00:00-05:00", "(iii)"),   # Sunday
    ],
)
def test_the_window_names_which_rule_holds(desk, now, holds):
    done = desk.run("--window", now=now)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == f"WINDOW {holds}"


@pytest.mark.parametrize(
    "now",
    [
        "2026-01-12T04:00:00-05:00",  # Monday 04:00: the Sunday evening is over
        "2026-01-08T19:59:00-05:00",  # Thursday before the pause
        "2026-01-09T04:30:00-05:00",  # Friday morning after the overnight idle
    ],
)
def test_outside_every_rule_the_window_fails(desk, now):
    done = desk.run("--window", now=now)
    assert done.returncode == 1
    assert last_line(done).startswith("FAILED STEP-0: window — ")


def test_a_market_holiday_named_in_records_is_a_non_trading_day(desk):
    holiday = "2026-01-19T14:00:00-05:00"  # a Monday
    assert desk.run("--window", now=holiday).returncode == 1
    desk.recard(records="- MARKET HOLIDAY 2026-01-19: the exchange is closed (desk read).\n")
    done = desk.run("--window", now=holiday)
    assert last_line(done) == "WINDOW (iii)"
    # the small hours after a holiday are not an overnight idle after a trading day
    done = desk.run("--window", now="2026-01-20T02:00:00-05:00")
    assert done.returncode == 1


def test_his_override_naming_this_job_opens_the_window(desk):
    desk.write_rulings(
        "| R2 | 09:05 ET | HIS RULING: the set ships. | HIS RULING · APPROVED |\n"
        "| R3 | 09:10 ET | HIS RULING: overrules L66 for deploy x-set at 14:00. | HIS RULING · APPROVED |\n"
    )
    desk.commit("override")
    desk.recard(rulings="2026-01-02 R2, R3")
    done = desk.run("--window", now=THURSDAY_1400)
    assert done.returncode == 0, done.stdout
    assert last_line(done) == "WINDOW (iv)"
    assert "2026-01-02 R3" in done.stdout


def test_an_override_that_names_another_job_does_not_open_the_window(desk):
    desk.write_rulings(
        "| R2 | 09:05 ET | HIS RULING: the set ships. | HIS RULING · APPROVED |\n"
        "| R3 | 09:10 ET | HIS RULING: overrules L66 for deploy y-set at 14:00. | HIS RULING · APPROVED |\n"
    )
    desk.commit("override for another job")
    desk.recard(rulings="2026-01-02 R2, R3")
    done = desk.run("--window", now=THURSDAY_1400)
    assert done.returncode == 1


def test_dry_run_calls_nothing_and_prints_every_would_run_line(desk):
    for name in ("git", "curl", "uv"):
        stub(desk.bin, name, PLAIN)
    before = desk.state()
    done = desk.run("--dry-run")
    assert done.returncode == 0, done.stdout + done.stderr
    for name in ("launchctl", "git", "curl", "uv", "date"):
        assert desk.calls_of(name) == [], name
    would = [ln for ln in done.stdout.splitlines() if ln.startswith("WOULD RUN: ")]
    assert any("authorize.sh deploy" in w for w in would)
    assert any(w.startswith("WOULD RUN: launchctl print gui/501/com.cobalt.aset") for w in would)
    assert any(str(desk.check["beta"]) in w for w in would)
    assert last_line(done).startswith("DRY RUN — nothing run")
    assert desk.state() == before
    assert not (desk.wt / ".deploy-logs").exists()


def test_d4_dry_run_on_the_10_02_deploy_card(desk):
    """RUN row D4: the --dry-run of the real 10-02 night deploy card (the worktree copy, read only)."""
    for name in ("git", "curl", "uv"):
        stub(desk.bin, name, PLAIN)
    env = {k: v for k, v in desk.env.items() if k != "COBALT_REPO_ROOT"}  # the real paths, printed only
    done = subprocess.run(
        ["sh", str(SCRIPT), "--dry-run", str(REAL_CARD)], env=env, capture_output=True,
        text=True, errors="replace", timeout=120,
    )
    print(done.stdout + done.stderr)
    for name in ("launchctl", "git", "curl", "uv", "date"):
        assert desk.calls_of(name) == [], name
    assert done.returncode == 0


@pytest.mark.parametrize("args", [[], ["--window"], ["/no/such/card.md"], ["--bogus", "x"]])
def test_a_bad_call_is_refused(desk, args):
    done = subprocess.run(
        ["sh", str(SCRIPT), *args], env=desk.env, capture_output=True, text=True, timeout=60
    )
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
