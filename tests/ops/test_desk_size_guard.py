"""desk-size-guard (card prompts/2026-10-01/02-desk-size-guard-card.md, ruling cto-2026-10-01 R8).

The desk-size guard on the CTO desk's ops scripts: `desk-context.sh --guard` (G1), run first by
`desk-launch.sh` for every kind but `desk` (G2) and by `wait-stop-line.sh` (G3); the closeout
paths stay unguarded (G4, a RUN row).

Every script runs from a copy under tmp_path whose fixed roots (the transcripts, desk-list.sh,
the repo and the worktrees) are re-pointed at constructed fixtures; `claude`, `sleep` and the
guard are stubs on PATH or beside the copy. Nothing outside tmp_path is read, written or run.
"""

import json
import os
import subprocess
from pathlib import Path

import pytest

OPS = Path(__file__).resolve().parents[2] / "ops" / "desk"
REFUSED_300000 = "REFUSED: desk at 300000 tokens — REFRESH first"
WARNING = "WARNING: desk size unread — guard skipped"

# constructed session ids (8-hex LIST ids; the transcript name is the full session id)
DESK = "d35c0001"
SUCCESSOR = "d35c0002"
BUILDER = "b0110001"


# ---- staging --------------------------------------------------------------------------------

def stage(tmp_path: Path, name: str, subs: dict[str, str]) -> Path:
    """Copy ops/desk/<name> to tmp_path/ops/<name> with its fixed roots re-pointed."""
    text = (OPS / name).read_text()
    for old, new in subs.items():
        text = text.replace(old, new)
    dst = tmp_path / "ops" / name
    dst.parent.mkdir(exist_ok=True)
    dst.write_text(text)
    dst.chmod(0o755)
    return dst


def write_exe(path: Path, body: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("#!/bin/sh\n" + body)
    path.chmod(0o755)
    return path


def transcript(projects: Path, sid8: str, tokens: int | None) -> Path:
    """A transcript in the real line shape; the last usage line sums to `tokens`.

    An earlier assistant line carries a different usage (the guard reads the LAST one) and a
    user line closes the file. tokens=None writes no usage line at all.
    """
    session = f"{sid8}-0000-4000-8000-000000000001"
    folder = projects / "-Users-fixture-desk"
    folder.mkdir(parents=True, exist_ok=True)

    def assistant(total: int, n: int) -> dict:
        return {
            "parentUuid": f"u-{n}", "isSidechain": False, "type": "assistant",
            "message": {
                "model": "claude-opus-5-5", "id": f"msg_{n}", "type": "message", "role": "assistant",
                "content": [{"type": "text", "text": "ok"}], "stop_reason": "end_turn",
                "usage": {"input_tokens": 3, "cache_creation_input_tokens": 1997,
                          "cache_read_input_tokens": total - 2000, "output_tokens": 12,
                          "service_tier": "standard"},
            },
            "uuid": f"a-{n}", "timestamp": "2026-01-02T12:00:00.000Z", "sessionId": session,
        }

    user = {"parentUuid": "a-2", "isSidechain": False, "type": "user",
            "message": {"role": "user", "content": "next"}, "uuid": "u-3",
            "timestamp": "2026-01-02T12:01:00.000Z", "sessionId": session}
    lines = [user]
    if tokens is not None:
        lines = [assistant(5000, 1), assistant(tokens, 2), user]
    path = folder / f"{session}.jsonl"
    path.write_text("".join(json.dumps(x) + "\n" for x in lines))
    return path


def desk_list(tmp_path: Path, rows: list[tuple[str, str]], status: int = 0) -> Path:
    """A desk-list.sh stub printing LIST rows `id · name · cwd · status · state`; it logs each call."""
    out = "".join(f"printf '%s\\n' '{i} · {n} · ~/cobalt · idle · working'\n" for i, n in rows)
    return write_exe(tmp_path / "list" / "desk-list.sh",
                     f'echo list >> "{tmp_path}/list-calls"\n{out}exit {status}\n')


def staged_context(tmp_path: Path, list_stub: Path) -> Path:
    return stage(tmp_path, "desk-context.sh", {
        "/Users/cobalt/.claude/projects": str(tmp_path / "projects"),
        "/Users/cobalt/.claude/ops/desk-list.sh": str(list_stub),
    })


def env(tmp_path: Path, **extra: str) -> dict[str, str]:
    e = {k: v for k, v in os.environ.items() if k != "CLAUDE_JOB_DIR"}
    e["PATH"] = f"{tmp_path / 'bin'}:{e.get('PATH', '/usr/bin:/bin')}"
    e.update(extra)
    return e


def run(argv: list[str], e: dict[str, str], cwd: Path | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(argv, env=e, cwd=cwd, capture_output=True, text=True, timeout=60)


def guard(tmp_path: Path, rows: list[tuple[str, str]], job: str | None = None,
          list_status: int = 0) -> subprocess.CompletedProcess:
    script = staged_context(tmp_path, desk_list(tmp_path, rows, list_status))
    extra = {} if job is None else {"CLAUDE_JOB_DIR": f"/Users/fixture/.claude/jobs/{job}"}
    return run(["sh", str(script), "--guard"], env(tmp_path, **extra))


# ---- G1: desk-context.sh --guard ---------------------------------------------------------------

def test_g1_guard_below_300000_is_silent_and_passes(tmp_path):
    transcript(tmp_path / "projects", DESK, 299_999)
    r = guard(tmp_path, [(DESK, "cto-desk")])
    assert (r.returncode, r.stdout, r.stderr) == (0, "", "")


def test_g1_guard_at_300000_refuses_with_the_exact_line(tmp_path):
    transcript(tmp_path / "projects", DESK, 300_000)
    r = guard(tmp_path, [(DESK, "cto-desk")])
    assert (r.returncode, r.stdout, r.stderr) == (3, REFUSED_300000 + "\n", "")


def test_g1_the_plain_call_is_unchanged_and_never_reads_the_list(tmp_path):
    """Negative control: the plain call's output on the same fixture equals today's."""
    transcript(tmp_path / "projects", DESK, 300_000)
    script = staged_context(tmp_path, desk_list(tmp_path, [(DESK, "cto-desk")]))
    e = env(tmp_path, CLAUDE_JOB_DIR=f"/Users/fixture/.claude/jobs/{DESK}")
    r = run(["sh", str(script), DESK, "250000"], e)
    assert (r.returncode, r.stdout) == (0, "context 300000 of 250000 — REFRESH\n")
    r = run(["sh", str(script), DESK], e)
    assert (r.returncode, r.stdout) == (0, "context 300000 of 400000 — ok\n")
    r = run(["sh", str(script), "d35c"], e)
    assert (r.returncode, r.stdout) == (2, "no transcript for d35c\n")
    r = run(["sh", str(script), "deadbeef"], e)
    assert (r.returncode, r.stdout) == (2, "no transcript for deadbeef\n")
    assert not (tmp_path / "list-calls").exists()


def test_g1_the_callers_own_desk_row_is_the_one_measured(tmp_path):
    transcript(tmp_path / "projects", DESK, 310_000)
    transcript(tmp_path / "projects", SUCCESSOR, 1_000)
    r = guard(tmp_path, [(DESK, "cto-desk"), (SUCCESSOR, "cto-desk")], job=DESK)
    assert (r.returncode, r.stdout) == (3, "REFUSED: desk at 310000 tokens — REFRESH first\n")


@pytest.mark.parametrize("sizes, expect", [
    ((450_000, 120_000), (0, "")),
    ((450_000, 300_001), (3, "REFUSED: desk at 300001 tokens — REFRESH first\n")),
])
def test_g1_a_caller_that_is_no_desk_row_measures_the_smallest_cto_desk(tmp_path, sizes, expect):
    """A build or the successor's predecessor: the smallest cto-desk (the successor in a handover)."""
    transcript(tmp_path / "projects", DESK, sizes[0])
    transcript(tmp_path / "projects", SUCCESSOR, sizes[1])
    transcript(tmp_path / "projects", BUILDER, 999_000)
    rows = [(DESK, "cto-desk"), (BUILDER, "fx-build"), (SUCCESSOR, "cto-desk")]
    r = guard(tmp_path, rows, job=BUILDER)
    assert (r.returncode, r.stdout) == expect


@pytest.mark.parametrize("case", ["no cto-desk row", "list fails", "no transcript", "no usage line"])
def test_g1_an_unread_desk_size_warns_and_never_blocks(tmp_path, case):
    """DECISION G-A, fail-open: the guard never blocks on its own failure."""
    rows = [(DESK, "cto-desk")]
    status = 0
    if case == "no cto-desk row":
        transcript(tmp_path / "projects", BUILDER, 999_000)
        rows = [(BUILDER, "fx-build")]
    elif case == "list fails":
        rows, status = [], 1
    elif case == "no usage line":
        transcript(tmp_path / "projects", DESK, None)
    r = guard(tmp_path, rows, list_status=status)
    assert (r.returncode, r.stdout, r.stderr) == (0, "", WARNING + "\n")


def test_g1_one_unread_desk_in_a_handover_warns_and_passes(tmp_path):
    """Both desks live, the successor has no usage yet: fail-open, never the predecessor's size."""
    transcript(tmp_path / "projects", DESK, 450_000)
    r = guard(tmp_path, [(DESK, "cto-desk"), (SUCCESSOR, "cto-desk")])
    assert (r.returncode, r.stdout, r.stderr) == (0, "", WARNING + "\n")


# ---- G2: desk-launch.sh runs the guard for every kind but `desk` ------------------------------

def git(cwd: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-c", "user.name=fixture", "-c", "user.email=fixture@example.invalid",
         "-c", "commit.gpgsign=false", *args],
        cwd=cwd, check=True, capture_output=True, text=True).stdout.strip()


HUB_LINE = ('claude --bg "Read \'<card>\' and follow it exactly." --permission-mode dontAsk '
            '--remote-control <job>-x --name <job>-x --allowedTools "Read" '
            '--disallowedTools "AskUserQuestion" "EnterWorktree"')


class World:
    """A constructed repo, worktree root, cards, fixed files and prompt for desk-launch.sh."""

    def __init__(self, tmp_path: Path):
        self.tmp = tmp_path
        root = tmp_path / "w"
        self.repo = root / "repo"
        self.wt = root / "wt"
        self.wt.mkdir(parents=True)
        self.prompts = self.repo / "docs" / "40 - DevDocs" / "prompts"
        self.reports = self.repo / "docs" / "40 - DevDocs" / "reports"
        (self.prompts / "2026-01-02").mkdir(parents=True)
        self.reports.mkdir(parents=True)
        git(self.repo, "init", "-q", "-b", "main")
        (self.repo / "README.md").write_text("fixture\n")
        git(self.repo, "add", "README.md")
        git(self.repo, "commit", "-q", "-m", "base")
        base = git(self.repo, "rev-parse", "HEAD")[:8]

        for hub in ("BUILD-HUB.md", "CHECK-HUB.md", "DEPLOY-HUB.md"):
            (self.prompts / hub).write_text(f"# {hub} fixture\n{HUB_LINE}\n")
        (self.prompts / "CLOSE-HUB.md").write_text(
            "# close fixture\nclaude --bg \"Read 'close <date> <mmdd>' and follow it exactly.\" "
            "--permission-mode dontAsk --remote-control close-<mmdd> --name close-<mmdd>\n")
        (self.prompts / "CTO-DESK-WAKEUP.md").write_text(
            "# wake-up fixture\n- LAUNCH (successor): `claude --bg \"Read wake\" --permission-mode "
            "dontAsk --remote-control cto-desk --name cto-desk`\n")

        day = self.prompts / "2026-01-02"
        self.build_card = day / "01-fx-card.md"
        self.build_card.write_text(
            f"JOB: fx\nLADDER: OFF-LADDER\nBRANCH: fx-build\nWORKTREE: fx-wt\nBASE: {base}\nTIP:\n"
            f"REPORT: {self.wt}/fx-wt/docs/40 - DevDocs/reports/fx-build.md\nCHECK REPORT:\nHOUSE B:\n"
            "TREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n")
        self.build_report = tmp_path / "fy-build.md"
        self.build_report.write_text("BUILT · fixture\n")
        self.check_report = self.reports / "fy-check.md"
        self.check_card = day / "02-fy-card.md"
        self.check_card.write_text(
            f"JOB: fy\nLADDER: OFF-LADDER\nBRANCH: fy-build\nWORKTREE: fy-wt\nBASE: {base}\n"
            f"TIP: {base}\nREPORT: {self.build_report}\nCHECK REPORT: {self.check_report}\n"
            "HOUSE B: as needed\nTREE STATE: unchanged\nRULINGS: 2026-01-02 R1\n\n## ROWS\n")
        self.deploy_card = day / "03-fz-card.md"
        self.deploy_card.write_text(
            f"JOB: fz\nLADDER: OFF-LADDER\nBRANCH: deploy-fz\nWORKTREE: fz-gate\nBASE: main\n"
            f"TIP: {base}\nTAG: deploy-fz-1\nMIGRATIONS: none\nSET: fx\n"
            f"REPORT: {self.reports}/deploy-fz.md\nRULINGS: none\n\n## SHIPS\n## MARKERS\n## SMOKE READS\n")
        self.prompt = day / "04-brain-prompt.md"
        self.prompt.write_text(
            f"cd {self.repo}\n\nclaude --bg \"Read '{self.prompt}' and follow it exactly.\" "
            "--permission-mode auto --remote-control brain --name brain "
            '--disallowedTools "AskUserQuestion" "EnterWorktree"\n')
        git(self.repo, "add", "docs")
        git(self.repo, "commit", "-q", "-m", "fixture files")
        git(self.repo, "worktree", "add", "-q", "-b", "fy-build", str(self.wt / "fy-wt"), base)

        esc = str(root).replace("/", "\\/") + "\\/"
        self.launch = stage(tmp_path, "desk-launch.sh", {
            "REPO=${COBALT_REPO_ROOT:-/Users/cobalt/cobalt}\n": f"REPO={self.repo}\n",
            "WT=${COBALT_WT_ROOT:-/Users/cobalt/cobalt-wt}\n": f"WT={self.wt}\n",
            "\\/Users\\/cobalt\\/": esc,
        })
        self.calls = tmp_path / "claude-calls"
        self.guard_calls = tmp_path / "guard-calls"
        write_exe(tmp_path / "bin" / "claude",
                  'if [ "$1" = "agents" ]; then echo "[]"; exit 0; fi\n'
                  f'printf "%s\\n" "$*" >> "{self.calls}"\nexit 0\n')

    def guard_stub(self, refuse: bool) -> None:
        body = f'echo "$*" >> "{self.guard_calls}"\n'
        body += f'echo "{REFUSED_300000}"\nexit 3\n' if refuse else "exit 0\n"
        write_exe(self.launch.parent / "desk-context.sh", body)

    def argv(self, form: str) -> list[str]:
        if form == "check PASS-2":
            self.check_report.write_text("# check\n\nCHECK DONE · pass: 1 · house B: needed\n")
        if form == "deploy STEP-D0":
            (self.wt / "fz-gate").mkdir()
        if form == "close STEP-3":
            (self.reports / "close-2026-01-02.md").write_text("# close\n")
        return {
            "build": ["build", str(self.build_card)],
            "build E2": ["build", str(self.build_card), "E2"],
            "check": ["check", str(self.check_card)],
            "check PASS-2": ["check", str(self.check_card), "PASS-2"],
            "check E3": ["check", str(self.check_card), "E3"],
            "deploy": ["deploy", str(self.deploy_card)],
            "deploy STEP-D0": ["deploy", str(self.deploy_card), "STEP-D0"],
            "prompt": ["prompt", str(self.prompt)],
            "close": ["close", "2026-01-02"],
            "close STEP-3": ["close", "2026-01-02", "STEP-3"],
            "desk": ["desk"],
        }[form]

    def launch_run(self, form: str, **extra: str) -> subprocess.CompletedProcess:
        return run(["sh", str(self.launch), *self.argv(form)], env(self.tmp, **extra), cwd=self.tmp)


GUARDED = ["build", "build E2", "check", "check PASS-2", "check E3", "deploy", "deploy STEP-D0",
           "prompt", "close", "close STEP-3"]


@pytest.mark.parametrize("form", GUARDED)
def test_g2_a_refusing_guard_stops_every_kind_but_desk_before_any_launch(tmp_path, form):
    w = World(tmp_path)
    w.guard_stub(refuse=True)
    r = w.launch_run(form)
    assert not w.calls.exists(), f"{form} reached claude: {w.calls.read_text()}"
    assert (r.returncode, r.stdout, r.stderr) == (3, REFUSED_300000 + "\n", "")
    assert w.guard_calls.read_text() == "--guard\n"


@pytest.mark.parametrize("form", GUARDED)
def test_g2_a_passing_guard_lets_every_kind_reach_its_launch(tmp_path, form):
    """Negative control: the fixture world is launchable; the guard passing changes nothing."""
    w = World(tmp_path)
    w.guard_stub(refuse=False)
    r = w.launch_run(form)
    assert r.returncode == 0, r.stderr
    assert w.calls.read_text().startswith("--bg ")


def test_g2_desk_never_calls_the_guard_and_reaches_its_launch(tmp_path):
    """Negative control: `desk-launch.sh desk` with the refusing guard still launches."""
    w = World(tmp_path)
    w.guard_stub(refuse=True)
    r = w.launch_run("desk")
    assert r.returncode == 0, r.stderr
    assert "--remote-control cto-desk --name cto-desk" in w.calls.read_text()
    assert not w.guard_calls.exists()


def test_g2_the_real_guard_refuses_a_build_and_lets_the_desk_launch(tmp_path):
    w = World(tmp_path)
    transcript(tmp_path / "projects", DESK, 300_000)
    staged_context(tmp_path, desk_list(tmp_path, [(DESK, "cto-desk")]))
    job = {"CLAUDE_JOB_DIR": f"/Users/fixture/.claude/jobs/{DESK}"}
    r = w.launch_run("build", **job)
    assert (r.returncode, r.stdout) == (3, REFUSED_300000 + "\n")
    assert not w.calls.exists()
    r = w.launch_run("desk", **job)
    assert r.returncode == 0, r.stderr
    assert "cto-desk" in w.calls.read_text()


# ---- G3: wait-stop-line.sh runs the guard first ------------------------------------------------

def stop_line_world(tmp_path: Path, refuse: bool, append: str = "") -> tuple[Path, Path]:
    script = stage(tmp_path, "wait-stop-line.sh", {})
    body = f'echo "{REFUSED_300000}"\nexit 3\n' if refuse else "exit 0\n"
    write_exe(script.parent / "desk-context.sh", body)
    watched = tmp_path / "report.md"
    watched.write_text("## RECORDS\n\n(run in progress — next step under ## CONTINUE)\n\n")
    sleep_body = f'echo "$1" >> "{tmp_path}/sleep-calls"\n'
    if append:
        sleep_body += f'printf "%s\\n" "{append}" >> "{watched}"\n'
    write_exe(tmp_path / "bin" / "sleep", sleep_body)
    return script, watched


def test_g3_a_refusing_guard_exits_3_and_never_enters_the_loop(tmp_path):
    script, watched = stop_line_world(tmp_path, refuse=True)
    # lastline() is the only reader of the watched file, through grep: a logging grep on PATH
    # shows whether the file was read before the guard refused (check H2).
    write_exe(tmp_path / "bin" / "grep", f'echo grep >> "{tmp_path}/grep-calls"\nexec /usr/bin/grep "$@"\n')
    r = run(["sh", str(script), str(watched), "^(BUILT|FAILED)", "40"], env(tmp_path))
    assert not (tmp_path / "sleep-calls").exists(), "the loop ran"
    assert not (tmp_path / "grep-calls").exists(), "the watched file was read"
    assert (r.returncode, r.stdout) == (3, REFUSED_300000 + "\n")


@pytest.mark.xfail(strict=True, reason="check H2's mutation probe: the guard moved below the first "
                   "read of the watched file; it must stay red (the file IS read)")
def test_g3_shipped_refusal_checks_stay_green_when_the_file_is_read_first(tmp_path):
    script, watched = stop_line_world(tmp_path, refuse=True)
    text = script.read_text()
    guard_line = 'sh "$(dirname "$0")/desk-context.sh" --guard || exit $?\n'
    anchor = 'initial=$(lastline "$f")\n'
    assert guard_line in text
    assert anchor in text
    text = text.replace(guard_line, "", 1)
    text = text.replace(anchor, anchor + guard_line, 1)
    script.write_text(text)
    write_exe(
        tmp_path / "bin" / "grep",
        f'echo grep >> "{tmp_path}/grep-calls"\nexec /usr/bin/grep "$@"\n',
    )
    r = run(["sh", str(script), str(watched), "^(BUILT|FAILED)", "40"], env(tmp_path))
    assert not (tmp_path / "sleep-calls").exists()
    assert (r.returncode, r.stdout) == (3, REFUSED_300000 + "\n")
    assert not (tmp_path / "grep-calls").exists()


def test_g3_a_passing_guard_keeps_the_match_path(tmp_path):
    script, watched = stop_line_world(tmp_path, refuse=False, append="BUILT · job: fx")
    r = run(["sh", str(script), str(watched), "^(BUILT|FAILED)", "60"], env(tmp_path))
    assert (r.returncode, r.stdout) == (0, "BUILT · job: fx\n")
    assert (tmp_path / "sleep-calls").read_text() == "20\n"


def test_g3_a_passing_guard_keeps_the_timeout_path(tmp_path):
    script, watched = stop_line_world(tmp_path, refuse=False)
    r = run(["sh", str(script), str(watched), "^(BUILT|FAILED)", "40"], env(tmp_path))
    assert (r.returncode, r.stdout) == (
        2, "TIMEOUT after 40s — last line was: (run in progress — next step under ## CONTINUE)\n")
    assert (tmp_path / "sleep-calls").read_text() == "20\n20\n"


def test_g3_wait_desk_idle_is_not_guarded(tmp_path):
    """Negative control: the successor's one wait runs with the guard refusing beside it."""
    script = stage(tmp_path, "wait-desk-idle.sh", {})
    write_exe(script.parent / "desk-context.sh",
              f'echo guard >> "{tmp_path}/guard-calls"\necho "{REFUSED_300000}"\nexit 3\n')
    write_exe(tmp_path / "bin" / "claude", 'echo "[]"\n')
    report = tmp_path / "cto.md"
    report.write_text("| R1 | fixture |\nHANDOVER fixture\n")
    r = run(["sh", str(script), DESK, str(report), "30"], env(tmp_path))
    assert (r.returncode, r.stdout) == (0, f"{DESK}: absent\nHANDOVER fixture\n")
    assert not (tmp_path / "guard-calls").exists()


# ---- G4: RUN — the closeout always completes (asserts nothing; -rP prints it) ------------------

def test_g4_run_the_closeout_paths_with_the_real_guard_refusing(tmp_path):
    w = World(tmp_path)
    transcript(tmp_path / "projects", DESK, 300_000)
    context = staged_context(tmp_path, desk_list(tmp_path, [(DESK, "cto-desk")]))
    job = {"CLAUDE_JOB_DIR": f"/Users/fixture/.claude/jobs/{DESK}"}
    report = tmp_path / "cto.md"
    report.write_text("| R1 | fixture |\nHANDOVER fixture\n")
    idle = stage(tmp_path, "wait-desk-idle.sh", {})
    shown = [
        ("desk-context.sh --guard (the guard itself)", ["sh", str(context), "--guard"]),
        ("desk-launch.sh build (guarded)", ["sh", str(w.launch), *w.argv("build")]),
        ("desk-launch.sh desk", ["sh", str(w.launch), "desk"]),
        ("wait-desk-idle.sh", ["sh", str(idle), DESK, str(report), "30"]),
        ("desk-context.sh <id>", ["sh", str(context), DESK]),
    ]
    for title, argv in shown:
        r = run(argv, env(tmp_path, **job), cwd=tmp_path)
        print(f"=== {title} → exit {r.returncode}\n--- stdout\n{r.stdout}--- stderr\n{r.stderr}")
    print("=== stub claude calls\n" + (w.calls.read_text() if w.calls.exists() else "(none)\n"))
