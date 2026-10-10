"""ops/desk/orphan-clean.sh — find, verify and (on --kill) signal an orphaned resident child
(card 229 orphan-clean-1010, rows O1-O4).

No real process is read or signalled: `ps`, `launchctl` and `lsof` are Python stubs on PATH that
answer from a JSON fake table in a tmp dir and log each call (argv) as one JSON line;
ORPHAN_CLEAN_KILL points at a stub that logs the call and edits the fake table (TERM removes the
pid unless it is marked TERM-ignoring, KILL unless it is marked unkillable). ORPHAN_CLEAN_GRACE=1.
Every pid and start time here is constructed.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "ops" / "desk" / "orphan-clean.sh"
LOCK = "/Users/cobalt/.cobalt/voice-scratch/.lock"
PORT = 5010
PY = "/Users/cobalt/cobalt/.venv/bin/python"
START = "Mon Jan  5 09:30:00 2099"

HEAD = '''#!/usr/bin/env python3
import json, os, sys
D = os.environ["ORPHAN_FAKE"]
def load():
    with open(os.path.join(D, "table.json")) as f:
        return json.load(f)
def save(t):
    with open(os.path.join(D, "table.json"), "w") as f:
        json.dump(t, f)
def log(name):
    with open(os.path.join(D, "calls.jsonl"), "a") as f:
        f.write(json.dumps({"tool": name, "argv": sys.argv[1:]}) + "\\n")
def proc(t, pid):
    for p in t["procs"]:
        if p["pid"] == pid:
            return p
    return None
'''

PS = HEAD + '''log("ps")
t = load()
a = sys.argv[1:]
if a[:1] == ["-A"]:
    e = t.get("ps_error")
    if e:
        sys.stderr.write(e + "\\n")
        sys.exit(1)
    for p in t["procs"]:
        print("%5d %5d %s" % (p["pid"], p["ppid"], p["command"]))
    for line in t.get("ps_extra", []):
        print(line)
    sys.exit(0)
if a[:1] == ["-p"]:
    pid = int(a[1])
    p = proc(t, pid)
    if p is None:
        sys.exit(1)
    n = sum(1 for c in open(os.path.join(D, "calls.jsonl"))
            if json.loads(c)["argv"][:2] == ["-p", str(pid)])
    command = p["command"]
    if p.get("reused_after") is not None and n > p["reused_after"]:
        command = p["reused_command"]
    if "-o" in a:
        print("%5d %s %s" % (p["ppid"], p.get("lstart", "''' + START + '''"), command))
    else:
        print("%5d" % pid)
    sys.exit(0)
sys.stderr.write("ps stub: unknown call\\n")
sys.exit(2)
'''

LAUNCHCTL = HEAD + '''log("launchctl")
t = load()
l = t["launchctl"]
sys.stdout.write(l.get("stdout", ""))
sys.stderr.write(l.get("stderr", ""))
sys.exit(l.get("code", 0))
'''

LSOF = HEAD + '''log("lsof")
t = load()
a = sys.argv[1:]
e = t.get("lsof_error")
if e:
    sys.stderr.write(e + "\\n")
    sys.exit(1)
pid = int(a[a.index("-p") + 1])
p = proc(t, pid)
if p is None:
    sys.exit(1)
if "--" in a:
    path = a[a.index("--") + 1]
    if p.get("holds_lock") and path == "''' + LOCK + '''":
        print("p%d" % pid)
        print("f3")
        print("n" + path)
        sys.exit(0)
    sys.exit(1)
if any(x.startswith("-iTCP:") for x in a):
    if p.get("listens") and "-iTCP:''' + str(PORT) + '''" in a and "-sTCP:LISTEN" in a:
        print("p%d" % pid)
        sys.exit(0)
    sys.exit(1)
sys.stderr.write("lsof stub: unknown call\\n")
sys.exit(2)
'''

KILL = HEAD + '''log("kill")
t = load()
sig, pid = sys.argv[1], int(sys.argv[2])
p = proc(t, pid)
if p is None:
    sys.exit(1)
if sig == "-TERM" and not p.get("term_ignoring"):
    t["procs"].remove(p)
elif sig == "-KILL" and not p.get("unkillable"):
    t["procs"].remove(p)
save(t)
'''

NOT_FOUND = 'Could not find service "com.cobalt.aset" in domain for user gui: 501\n'


def running(pid: int) -> str:
    return (
        "gui/501/com.cobalt.aset = {\n"
        "\tactive count = 1\n"
        "\tpath = /Users/cobalt/Library/LaunchAgents/com.cobalt.aset.plist\n"
        "\ttype = LaunchAgent\n"
        "\tstate = running\n"
        "\n"
        "\tprogram = /Users/cobalt/cobalt/ops/start_aset.sh\n"
        "\tworking directory = /Users/cobalt/cobalt\n"
        "\n"
        "\tstdout path = /Users/cobalt/cobalt/logs/aset.log\n"
        "\tstderr path = /Users/cobalt/cobalt/logs/aset.err\n"
        "\truns = 3\n"
        f"\tpid = {pid}\n"
        "\timmediate reason = speculative\n"
        "\tforks = 4\n"
        "\texecs = 1\n"
        "\tlast exit code = 1\n"
        "}\n"
    )


UV = 7100      # launchd's job pid today: `exec uv run python -m cobalt.aset` (start_aset.sh:73)
HEALTHY = 7101  # its python child, ppid UV (row O2 (a))
ORPHAN = 7002   # the R851 shape: ppid 1, holds the voice lock (row O2 (b))
DECOYS = (7201, 7202, 7203, 7204, 7205)


def r851_table() -> dict:
    return {
        "procs": [
            {"pid": 1, "ppid": 0, "command": "/sbin/launchd"},
            {"pid": UV, "ppid": 1, "command": "/Users/cobalt/.local/bin/uv run python -m cobalt.aset"},
            {"pid": HEALTHY, "ppid": UV, "command": f"{PY} -m cobalt.aset", "listens": True},
            {"pid": ORPHAN, "ppid": 1, "command": f"{PY} -m cobalt.aset", "holds_lock": True},
            # row O2 (c): ppid 1 and holding the lock, so only the exact match keeps them out
            {"pid": 7201, "ppid": 1, "command": "grep cobalt.aset", "holds_lock": True},
            {"pid": 7202, "ppid": 1, "command": f"{PY} -m cobalt.aset.web", "holds_lock": True},
            {"pid": 7203, "ppid": 1, "command": f"{PY} -m cobalt.asetx", "holds_lock": True},
            {"pid": 7204, "ppid": 1, "command": f"{PY} -m cobalt.aset --debug", "holds_lock": True},
            {"pid": 7205, "ppid": 1, "command": f"{PY}x -m cobalt.aset", "holds_lock": True},
        ],
        "launchctl": {"stdout": running(UV), "code": 0},
    }


@pytest.fixture
def fake(tmp_path):
    d = tmp_path / "fake"
    d.mkdir()
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    for name, body in (("ps", PS), ("launchctl", LAUNCHCTL), ("lsof", LSOF), ("kill-stub", KILL)):
        (bin_dir / name).write_text(body)
        (bin_dir / name).chmod(0o755)
    (d / "calls.jsonl").write_text("")
    env = dict(
        os.environ,
        ORPHAN_FAKE=str(d),
        ORPHAN_CLEAN_KILL=str(bin_dir / "kill-stub"),
        ORPHAN_CLEAN_GRACE="1",
        PATH=f"{bin_dir}{os.pathsep}{os.environ['PATH']}",
    )
    return Fake(d, env)


class Fake:
    def __init__(self, d: Path, env: dict):
        self.d = d
        self.env = env
        self.pids: set[int] = set()

    def set(self, table: dict) -> None:
        self.pids |= {p["pid"] for p in table["procs"]}
        (self.d / "table.json").write_text(json.dumps(table))

    def table(self) -> dict:
        return json.loads((self.d / "table.json").read_text())

    def calls(self, tool: str | None = None) -> list[list[str]]:
        rows = [json.loads(ln) for ln in (self.d / "calls.jsonl").read_text().splitlines()]
        return [r["argv"] for r in rows if tool is None or r["tool"] == tool]

    def run(self, *args: str) -> subprocess.CompletedProcess:
        done = subprocess.run(
            ["sh", str(SCRIPT), *args], env=self.env, capture_output=True, text=True, timeout=60
        )
        self.no_stranger_pid()
        return done

    def no_stranger_pid(self) -> None:
        """No stub log names a pid outside the fake table."""
        for argv in self.calls():
            for i, word in enumerate(argv):
                if word == "-p" and i + 1 < len(argv):
                    assert int(argv[i + 1]) in self.pids, argv
        for argv in self.calls("kill"):
            assert int(argv[1]) in self.pids, argv


def lines(done: subprocess.CompletedProcess, prefix: str) -> list[str]:
    return [ln for ln in done.stdout.splitlines() if ln.startswith(prefix)]


def test_script_text_holds_no_broad_kill():
    text = SCRIPT.read_text()
    for word in ("pkill", "pgrep", "killall", "kill -9 $("):
        assert word not in text, word


# ---- O1 the label table and the call shape --------------------------------------------------


@pytest.mark.parametrize(
    "args",
    [["radar"], ["aset", "aset"], ["--force", "aset"], ["aset", "--kill"], [], ["--kill"],
     ["--kill", "radar"], ["--kill", "aset", "aset"], ["ASET"]],
)
def test_label_table_and_refusals(fake, args):
    fake.set(r851_table())
    done = fake.run(*args)
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert fake.calls() == []  # nothing read


def test_header_names_every_command_and_the_reports():
    head = "\n".join(ln for ln in SCRIPT.read_text().splitlines() if ln.startswith("#"))
    for word in ("ps -A -o pid= -o ppid= -o command=", "ps -p", "launchctl print gui/501/",
                 "lsof -nP -a -p", "kill -TERM", "kill -KILL", "sleep 1",
                 "ORPHAN_CLEAN_KILL", "ORPHAN_CLEAN_GRACE", LOCK, str(PORT),
                 "com.cobalt.aset", "R851", "R853", "R854", "R855"):
        assert word in head, word


# ---- O2 find and verify ---------------------------------------------------------------------


def test_find_and_verify(fake):
    fake.set(r851_table())
    done = fake.run("aset")
    assert done.returncode == 0, done.stdout + done.stderr
    assert lines(done, "CANDIDATE:") == [f"CANDIDATE: {ORPHAN} ppid 1 {PY} -m cobalt.aset"]
    assert lines(done, "VERIFIED:") == [f"VERIFIED: {ORPHAN} holds lock {LOCK}"]
    assert lines(done, "SPARED:") == []
    assert fake.calls("launchctl") == [["print", "gui/501/com.cobalt.aset"]]
    assert fake.calls("ps")[0] == ["-A", "-o", "pid=", "-o", "ppid=", "-o", "command="]
    lsof = fake.calls("lsof")
    assert ["-nP", "-a", "-p", str(ORPHAN), "-Fn", "--", LOCK] in lsof
    assert all(a[3] == str(ORPHAN) for a in lsof)


def test_verified_by_the_port(fake):
    t = r851_table()
    t["procs"][3] = {"pid": ORPHAN, "ppid": 1, "command": f"{PY} -m cobalt.aset", "listens": True}
    fake.set(t)
    done = fake.run("aset")
    assert done.returncode == 0, done.stdout + done.stderr
    assert lines(done, "VERIFIED:") == [f"VERIFIED: {ORPHAN} listens on :{PORT}"]
    assert ["-nP", "-a", "-p", str(ORPHAN), f"-iTCP:{PORT}", "-sTCP:LISTEN", "-Fp"] in fake.calls("lsof")


@pytest.mark.parametrize("interp", ["python", "python3", "python3.14"])
def test_interpreter_names(fake, interp):
    t = r851_table()
    t["procs"][3]["command"] = f"/Users/cobalt/cobalt/.venv/bin/{interp} -m cobalt.aset"
    fake.set(t)
    done = fake.run("aset")
    assert len(lines(done, "CANDIDATE:")) == 1 and len(lines(done, "VERIFIED:")) == 1, done.stdout


def test_spares_the_job_pid(fake):
    """NEGATIVE CONTROL: aset after the orphan-cause card's option (ii) — launchd's pid IS python."""
    job = 7300
    t = {
        "procs": [
            {"pid": job, "ppid": 1, "command": f"{PY} -m cobalt.aset", "holds_lock": True, "listens": True},
        ],
        "launchctl": {"stdout": running(job), "code": 0},
    }
    fake.set(t)
    done = fake.run("aset")
    assert done.returncode == 0, done.stdout + done.stderr
    assert lines(done, "SPARED:") == [f"SPARED: {job} is com.cobalt.aset's own pid"]
    assert lines(done, "WOULD KILL:") == []
    done = fake.run("--kill", "aset")
    assert done.returncode == 0, done.stdout + done.stderr
    assert lines(done, "SPARED:") == [f"SPARED: {job} is com.cobalt.aset's own pid"]
    assert fake.calls("kill") == []
    assert done.stdout.splitlines()[-1] == "orphan-clean: aset · verified 0 · spared 1 · killed 0"


def test_no_job_loaded_is_not_a_spare(fake):
    t = r851_table()
    t["launchctl"] = {"stderr": NOT_FOUND, "code": 113}
    fake.set(t)
    done = fake.run("aset")
    assert done.returncode == 0, done.stdout + done.stderr
    assert lines(done, "VERIFIED:") == [f"VERIFIED: {ORPHAN} holds lock {LOCK}"]
    assert lines(done, "SPARED:") == []


def test_unverifiable_fails_loud(fake):
    t = r851_table()
    t["procs"][3] = {"pid": ORPHAN, "ppid": 1, "command": f"{PY} -m cobalt.aset"}
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert done.returncode == 1, done.stdout + done.stderr
    assert lines(done, "UNVERIFIED:") == [f"UNVERIFIED: {ORPHAN} — holds neither lock {LOCK} nor port :{PORT}"]
    assert "REFUSED: " in done.stderr
    assert fake.calls("kill") == []


def test_one_unverifiable_candidate_stops_the_whole_run(fake):
    t = r851_table()
    t["procs"].append({"pid": 7003, "ppid": 1, "command": f"{PY} -m cobalt.aset"})
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert done.returncode == 1, done.stdout + done.stderr
    assert lines(done, "UNVERIFIED:") and "REFUSED: " in done.stderr
    assert fake.calls("kill") == []


@pytest.mark.parametrize(
    "launchctl",
    [
        {"stdout": "gui/501/com.cobalt.aset = {\n\tstate = not running\n}\n", "code": 0},
        {"stdout": running(UV).replace("\tpid = 7100\n", ""), "code": 0},
        {"stdout": running(UV) + "\tpid = 7101\n", "code": 0},
        {"stdout": running(UV).replace("pid = 7100", "pid = 71x0"), "code": 0},
        {"stderr": "Bad request.\n", "code": 5},
        {"stdout": "", "code": 0},
    ],
)
def test_unknown_launchctl_shape_fails_loud(fake, launchctl):
    t = r851_table()
    t["launchctl"] = launchctl
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: " in done.stderr
    assert fake.calls("kill") == []


@pytest.mark.parametrize(
    "broken",
    [{"ps_error": "ps: permission denied"}, {"lsof_error": "lsof: WARNING: can't stat()"},
     {"ps_extra": ["not a ps line at all"]}],
)
def test_a_tool_failure_or_odd_line_fails_loud(fake, broken):
    t = r851_table()
    t.update(broken)
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: " in done.stderr
    assert fake.calls("kill") == []


# ---- O3 the dry run -------------------------------------------------------------------------


def test_dry_run_kills_nothing(fake):
    fake.set(r851_table())
    before = fake.table()
    done = fake.run("aset")
    assert done.returncode == 0, done.stdout + done.stderr
    assert lines(done, "WOULD KILL:") == [f"WOULD KILL: {ORPHAN}"]
    assert done.stdout.splitlines()[-1] == "orphan-clean: aset dry-run · verified 1 · spared 0 · killed 0"
    assert fake.calls("kill") == []
    assert fake.table() == before
    assert lines(done, "RUN:") == []


def test_dry_run_with_no_candidate(fake):
    t = r851_table()
    del t["procs"][3]
    fake.set(t)
    done = fake.run("aset")
    assert done.returncode == 0, done.stdout + done.stderr
    assert done.stdout.splitlines() == ["orphan-clean: aset · none found"]
    assert fake.calls("kill") == []


# ---- O4 the kill ----------------------------------------------------------------------------


def never_the_residents(fake: Fake, *more: int) -> None:
    """NEGATIVE CONTROL: the healthy python (a) and the job pid are never in the kill log."""
    killed = {int(a[1]) for a in fake.calls("kill")}
    assert not killed & {HEALTHY, UV, *DECOYS, *more}, killed


def test_kill_term_enough(fake):
    fake.set(r851_table())
    done = fake.run("--kill", "aset")
    assert done.returncode == 0, done.stdout + done.stderr
    assert lines(done, "RUN:") == [f"RUN: kill -TERM {ORPHAN}"]
    assert lines(done, "KILLED:") == [f"KILLED: {ORPHAN} (TERM)"]
    assert fake.calls("kill") == [["-TERM", str(ORPHAN)]]
    assert done.stdout.splitlines()[-1] == "orphan-clean: aset · verified 1 · spared 0 · killed 1"
    assert ORPHAN not in {p["pid"] for p in fake.table()["procs"]}
    never_the_residents(fake)


def test_kill_escalates_when_term_ignored(fake):
    t = r851_table()
    t["procs"][3]["term_ignoring"] = True  # R854: pid 39280 ignored SIGTERM
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert done.returncode == 0, done.stdout + done.stderr
    assert lines(done, "RUN:") == [f"RUN: kill -TERM {ORPHAN}", f"RUN: kill -KILL {ORPHAN}"]
    assert lines(done, "KILLED:") == [f"KILLED: {ORPHAN} (KILL)"]
    assert fake.calls("kill") == [["-TERM", str(ORPHAN)], ["-KILL", str(ORPHAN)]]
    never_the_residents(fake)


def test_survives_kill_fails_loud(fake):
    t = r851_table()
    t["procs"][3].update(term_ignoring=True, unkillable=True)
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert done.returncode == 1, done.stdout + done.stderr
    assert done.stdout.splitlines()[-1] == f"FAILED: {ORPHAN} survived KILL"
    assert fake.calls("kill") == [["-TERM", str(ORPHAN)], ["-KILL", str(ORPHAN)]]
    never_the_residents(fake)


def test_pid_reused_is_not_signalled(fake):
    t = r851_table()
    t["procs"][3].update(reused_after=1, reused_command="/usr/bin/some-other-program --serve")
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: {ORPHAN} changed before TERM" in done.stderr
    assert fake.calls("kill") == []
    never_the_residents(fake)


def test_pid_reused_between_term_and_kill_is_not_signalled(fake):
    t = r851_table()
    # the O2 reading, the re-read before TERM and the first poll see the orphan; then the pid is another program
    t["procs"][3].update(term_ignoring=True, reused_after=3, reused_command="/usr/bin/some-other-program")
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert fake.calls("kill") == [["-TERM", str(ORPHAN)]]
    assert lines(done, "RUN:") == [f"RUN: kill -TERM {ORPHAN}"]
    never_the_residents(fake)


# ---- the check (orphan-clean-1010-check) ----------------------------------------------------


def test_identity_read_at_verify_is_the_candidates(fake):
    t = r851_table()
    # every `ps -p` reading of the orphan's pid shows another ppid-1 program: the pid was reused after lsof
    t["procs"][3].update(reused_after=0, reused_command="/usr/sbin/some-daemon --serve")
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert done.returncode == 1, done.stdout + done.stderr
    assert fake.calls("kill") == []
    never_the_residents(fake)


def test_x1_ps_p_command_must_still_be_python_m_aset(fake):
    t = r851_table()
    t["procs"][3].update(reused_after=0, reused_command="/usr/bin/some-other-program --serve")
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert done.returncode == 1, done.stdout + done.stderr
    assert fake.calls("kill") == [], fake.calls("kill")


def test_resource_ownership_is_rechecked_before_signal(fake):
    t = r851_table()
    fake.set(t)
    bin_dir = Path(fake.env["PATH"].split(os.pathsep, 1)[0])
    dropping_lsof = HEAD + f'''log("lsof")
t = load()
a = sys.argv[1:]
pid = int(a[a.index("-p") + 1])
p = proc(t, pid)
if "--" in a:
    path = a[a.index("--") + 1]
    if p is not None and p.get("holds_lock") and path == {LOCK!r}:
        print("n" + path)
        p["holds_lock"] = False
        save(t)
        sys.exit(0)
sys.exit(1)
'''
    (bin_dir / "lsof").write_text(dropping_lsof)
    (bin_dir / "lsof").chmod(0o755)

    done = fake.run("--kill", "aset")

    assert done.returncode == 1, done.stdout + done.stderr
    assert lines(done, "UNVERIFIED:")
    assert fake.calls("kill") == []


def test_launchctl_not_found_plus_other_error_is_unverifiable(fake):
    t = r851_table()
    t["launchctl"] = {
        "stderr": NOT_FOUND + "launchctl: input/output error\n",
        "code": 5,
    }
    fake.set(t)

    done = fake.run("--kill", "aset")

    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: " in done.stderr
    assert fake.calls("kill") == []


def test_x1_not_found_substring_does_not_hide_the_job_pid(fake):
    job = 7300
    t = {
        "procs": [
            {"pid": job, "ppid": 1, "command": f"{PY} -m cobalt.aset", "holds_lock": True, "listens": True},
        ],
        "launchctl": {
            "stdout": running(job) + 'Could not find service "com.cobalt.aset" in domain for user gui: 501\n',
            "code": 0,
        },
    }
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert fake.calls("kill") == [], done.stdout + done.stderr


def test_ps_a_failure_prints_unverified_then_refuses(fake):
    t = r851_table()
    t["ps_error"] = "ps: permission denied"
    fake.set(t)

    done = fake.run("--kill", "aset")

    assert done.returncode == 1, done.stdout + done.stderr
    unverified = lines(done, "UNVERIFIED:")
    assert len(unverified) == 1, done.stdout
    assert unverified[0].startswith("UNVERIFIED: ? — ")
    assert "REFUSED: " in done.stderr
    assert fake.calls("kill") == []


def test_ps_a_stderr_prints_unverified_then_refuses(fake):
    t = r851_table()
    t["ps_error"] = "ps: permission denied"
    fake.set(t)
    done = fake.run("--kill", "aset")
    assert done.returncode == 1, done.stdout + done.stderr
    assert lines(done, "UNVERIFIED:"), done.stdout + done.stderr
    assert "REFUSED: " in done.stderr
    assert fake.calls("kill") == []


def test_ps_p_failure_prints_unverified_then_refuses(fake):
    t = r851_table()
    fake.set(t)
    bin_dir = Path(fake.env["PATH"].split(os.pathsep, 1)[0])
    broken_ps = PS.replace(
        'if a[:1] == ["-p"]:\n    pid = int(a[1])',
        'if a[:1] == ["-p"]:\n'
        '    sys.stderr.write("ps: permission denied\\n")\n'
        '    sys.exit(1)\n'
        '    pid = int(a[1])',
    )
    (bin_dir / "ps").write_text(broken_ps)
    (bin_dir / "ps").chmod(0o755)

    done = fake.run("--kill", "aset")

    assert done.returncode == 1, done.stdout + done.stderr
    unverified = lines(done, "UNVERIFIED:")
    assert len(unverified) == 1, done.stdout
    assert unverified[0].startswith(f"UNVERIFIED: {ORPHAN} — ")
    assert "REFUSED: " in done.stderr
    assert fake.calls("kill") == []
