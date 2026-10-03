"""ops/desk/deploy-outage.sh — the outage as one script (card 20 deploy-steps, row D2).

No resident is touched: `launchctl` is a stub on PATH that keeps a tiny launchd in a JSON file
(label → pid, path) and records every call, in order, to one log shared with the `cobalt.sh`
stub in the tmp repo (COBALT_REPO_ROOT) and the `date` stub (FAKE_NOW). The radar plist sits in
a tmp LaunchAgents folder (COBALT_LAUNCHAGENTS). Production, launchd, the real repo and the
network are never touched.
"""

from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "ops" / "desk" / "deploy-outage.sh"
REAL_CARD = REPO / "docs" / "40 - DevDocs" / "prompts" / "2026-10-02" / "25-deploy-scripts-card.md"

ASET = "com.cobalt.aset"
RADAR = "com.cobalt.radar"
AGENT = "com.cobalt.agent"
SATURDAY_1400 = "2026-01-03T14:00:00-05:00"
THURSDAY_1400 = "2026-01-08T14:00:00-05:00"

RECORD = """#!__PY__
import json, os, sys, time
with open(os.environ["STUB_CALLS"], "a") as f:
    f.write(json.dumps({"name": "__NAME__", "argv": sys.argv[1:]}) + "\\n")
""".replace("__PY__", sys.executable)

# a tiny launchd: {"labels": {label: {"pid": n, "path": p}}, "next": n, "agent": pid or null}
LAUNCHCTL = """
path = os.environ["LAUNCHD_STATE"]
st = json.load(open(path))
def save():
    json.dump(st, open(path, "w"))
args = sys.argv[1:]
verb = args[0] if args else ""
fails = os.environ.get("STUB_FAIL_BOOTSTRAP", "").split(",")
if verb == "print":
    label = args[1].split("/")[-1]
    job = st["labels"].get(label)
    if job is None:
        print(f'Could not find service "{label}" in domain for user gui: 501')
        sys.exit(113)
    print(f"gui/501/{label} = {{\\n\\tpath = {job['path']}\\n\\tstate = running\\n\\tpid = {job['pid']}\\n}}")
    sys.exit(0)
if verb == "bootout":
    label = args[1].split("/")[-1]
    if label not in os.environ.get("STUB_STUCK", "").split(","):
        st["labels"].pop(label, None)
        save()
    if os.environ.get("STUB_MARK_ON") == label:
        open(os.environ["STUB_MARK"], "w").write("down")
        time.sleep(float(os.environ.get("STUB_HOLD", "2")))
    if os.environ.get("STUB_VANISH_AFTER") == label:
        # a missing launchctl, without removing the stub: /bin/launchctl must never answer a test
        with open(sys.argv[0], "w") as gone:
            gone.write('#!/bin/sh\\necho "launchctl: command not found" >&2\\nexit 127\\n')
    sys.exit(0)
if verb == "bootstrap":
    plist = args[2]
    label = os.path.basename(plist)[: -len(".plist")]
    if label in fails or label in st["labels"]:
        print("Bootstrap failed: 5: Input/output error", file=sys.stderr)
        sys.exit(5)
    st["labels"][label] = {"pid": st["next"], "path": plist}
    st["next"] += 1
    save()
    sys.exit(0)
if verb == "kickstart":
    target = args[-1].split("/")[-1]
    if target == "com.cobalt.agent":
        st["agent"] = st["next"]
        st["next"] += 1
        save()
    sys.exit(0)
sys.exit(1)
"""

COBALT_SH = """
path = os.environ["LAUNCHD_STATE"]
st = json.load(open(path))
verb = sys.argv[1] if len(sys.argv) > 1 else ""
if verb == "status":
    if st.get("agent"):
        print(f"  Cobalt is ONLINE (PID: {st['agent']}).")
    else:
        print("  Cobalt is OFFLINE.")
elif verb == "stop":
    st["agent"] = None
    json.dump(st, open(path, "w"))
    print("  Cobalt stopped safely.")
"""

DATE = """
import datetime
now = datetime.datetime.fromisoformat(os.environ["FAKE_NOW"])
fmts = [a[1:] for a in sys.argv[1:] if a.startswith("+")]
fmt = fmts[0] if fmts else "%a %b %d %H:%M:%S %Z %Y"
print(now.strftime(fmt.replace("%s", str(int(now.timestamp())))))
"""

PLAIN = "sys.exit(0)\n"


def stub(path: Path, name: str, body: str) -> None:
    path.write_text(RECORD.replace("__NAME__", name) + body)
    path.chmod(0o755)


class Box:
    def __init__(self, tmp_path: Path) -> None:
        root = tmp_path.resolve()
        self.root = root
        self.repo = root / "repo"
        (self.repo / "ops").mkdir(parents=True)
        (self.repo / "logs").mkdir()
        self.agents = root / "LaunchAgents"
        self.agents.mkdir()
        self.wt = root / "wt"
        self.wt.mkdir()
        self.aset_plist = self.repo / "ops" / f"{ASET}.plist"
        self.radar_plist = self.agents / f"{RADAR}.plist"
        self.aset_plist.write_text("<plist/>\n")
        self.radar_plist.write_text("<plist/>\n")
        self.card = root / "deploy-x-set-card.md"
        self.card.write_text(
            "JOB: x-set\nBRANCH: deploy/x-set\nWORKTREE: x-gate\nTIP: aaaaaaaa\nRULINGS: none\n"
            "TAG: x-tag\nMIGRATIONS: none\nSET: xset\n\n## SHIPS\n\n## RECORDS\n- a desk fact\n"
        )
        self.state_path = root / "launchd.json"
        self.save({
            "labels": {
                ASET: {"pid": 501, "path": str(self.aset_plist)},
                RADAR: {"pid": 502, "path": str(self.radar_plist)},
            },
            "next": 900,
            "agent": 503,
        })
        self.bin = root / "bin"
        self.bin.mkdir()
        self.calls = root / "calls.jsonl"
        stub(self.bin / "launchctl", "launchctl", LAUNCHCTL)
        stub(self.bin / "date", "date", DATE)
        stub(self.repo / "cobalt.sh", "cobalt.sh", COBALT_SH)
        self.mark = root / "mark"
        self.env = dict(
            os.environ, COBALT_REPO_ROOT=str(self.repo), COBALT_WT_ROOT=str(self.wt),
            COBALT_LAUNCHAGENTS=str(self.agents), STUB_CALLS=str(self.calls),
            LAUNCHD_STATE=str(self.state_path), FAKE_NOW=SATURDAY_1400, DEPLOY_SETTLE="0",
            STUB_MARK=str(self.mark), PATH=f"{self.bin}{os.pathsep}{os.environ['PATH']}",
        )

    def save(self, st: dict) -> None:
        self.state_path.write_text(json.dumps(st))

    def launchd(self) -> dict:
        return json.loads(self.state_path.read_text())

    def args(self, labels: str, state: str = "MERGED", *flags: str) -> list[str]:
        return ["sh", str(SCRIPT), *flags, str(self.card), labels, state]

    def run(self, labels: str = f"{ASET},{RADAR}", state: str = "MERGED", *flags: str, **env: str):
        return subprocess.run(
            self.args(labels, state, *flags), env=dict(self.env, **env), capture_output=True,
            text=True, errors="replace", timeout=120,
        )

    def calls_list(self) -> list[dict]:
        if not self.calls.exists():
            return []
        return [json.loads(line) for line in self.calls.read_text().splitlines()]

    def launchctl_calls(self) -> list[list[str]]:
        return [c["argv"] for c in self.calls_list() if c["name"] == "launchctl"]


def last_line(done) -> str:
    return [ln for ln in done.stdout.splitlines() if ln.strip()][-1]


def acts(box: Box) -> list[tuple[str, str]]:
    """Every launchctl call but print, as (verb, label)."""
    out = []
    for argv in box.launchctl_calls():
        if argv[0] == "print":
            continue
        target = argv[-1]
        label = os.path.basename(target)[: -len(".plist")] if target.endswith(".plist") else target.split("/")[-1]
        out.append((argv[0], label))
    return out


@pytest.fixture
def box(tmp_path):
    return Box(tmp_path)


def test_the_happy_path_boots_out_all_then_bootstraps_all_then_reads_status(box):
    done = box.run()
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "OUTAGE DONE 0s"
    assert acts(box) == [("bootout", ASET), ("bootout", RADAR), ("bootstrap", ASET), ("bootstrap", RADAR)]
    names = [c["name"] for c in box.calls_list()]
    assert names[-1] == "cobalt.sh" and box.calls_list()[-1]["argv"] == ["status"]
    st = box.launchd()["labels"]
    assert st[ASET]["pid"] not in (501, 502) and st[RADAR]["pid"] not in (501, 502)
    assert f"{ASET} · pid before 501 · pid after {st[ASET]['pid']}" in done.stdout
    assert f"{RADAR} · pid before 502 · pid after {st[RADAR]['pid']}" in done.stdout
    assert "RESIDENTS UP (trap)" not in done.stdout
    assert list((box.wt / ".deploy-logs").glob("x-set-outage-*.log"))


def test_a_bootstrap_that_fails_for_one_label_fails_and_the_trap_bootstraps_the_rest(box):
    done = box.run(STUB_FAIL_BOOTSTRAP=ASET)
    assert done.returncode == 1
    assert last_line(done).startswith(f"FAILED OUTAGE: {ASET} — ")
    assert f"down: {ASET}" in last_line(done)
    assert f"up: {RADAR}" in last_line(done)
    st = box.launchd()["labels"]
    assert RADAR in st and st[RADAR]["pid"] != 502
    # the failing label was tried with its one retry, and again by the trap
    assert acts(box).count(("bootstrap", ASET)) >= 2
    assert ("bootstrap", RADAR) in acts(box)


@pytest.mark.parametrize("sig", [signal.SIGTERM, signal.SIGINT, signal.SIGHUP])
def test_a_signal_between_bootout_and_bootstrap_brings_every_label_up(box, sig):
    proc = subprocess.Popen(
        box.args(f"{ASET},{RADAR}"), env=dict(box.env, STUB_MARK_ON=RADAR, STUB_HOLD="2"),
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, errors="replace",
    )
    deadline = time.monotonic() + 30
    while not box.mark.exists():
        assert time.monotonic() < deadline, "the bootout never ran"
        time.sleep(0.05)
    proc.send_signal(sig)
    out, err = proc.communicate(timeout=60)
    assert proc.returncode != 0, out + err
    assert "RESIDENTS UP (trap)" in out, out + err
    st = box.launchd()["labels"]
    assert ASET in st and RADAR in st
    assert st[ASET]["pid"] != 501 and st[RADAR]["pid"] != 502
    last = [ln for ln in out.splitlines() if ln.strip()][-1]
    assert last.startswith("FAILED OUTAGE: ") and "signal" in last


def test_not_merged_is_refused_with_no_launchctl_call(box):
    done = box.run(state="NOT MERGED")
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert box.launchctl_calls() == []


def test_a_label_outside_the_set_never_appears_in_the_call_log(box):
    done = box.run(labels=ASET)
    assert done.returncode == 0, done.stdout + done.stderr
    for argv in box.launchctl_calls():
        assert RADAR not in " ".join(argv), argv
    assert box.launchd()["labels"][RADAR]["pid"] == 502


def test_a_closed_window_is_refused_before_anything_goes_down(box):
    done = box.run(FAKE_NOW=THURSDAY_1400)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: window")
    assert box.launchctl_calls() == []


@pytest.mark.parametrize("labels", ["com.cobalt.herdr", f"{ASET},com.cobalt.mainframe", f"{ASET},,{RADAR}", ""])
def test_a_label_outside_the_residents_is_refused_before_anything_goes_down(box, labels):
    done = box.run(labels=labels)
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert box.launchctl_calls() == []


def test_a_resident_loaded_from_another_plist_is_refused_before_anything_goes_down(box):
    st = box.launchd()
    st["labels"][RADAR]["path"] = "/somewhere/else/com.cobalt.radar.plist"
    box.save(st)
    done = box.run()
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert [a for a in box.launchctl_calls() if a[0] != "print"] == []


def test_a_bootout_that_leaves_the_label_loaded_fails_and_residents_stay_up(box):
    done = box.run(STUB_STUCK=ASET)
    assert done.returncode == 1
    assert last_line(done).startswith(f"FAILED OUTAGE: {ASET} — ")
    st = box.launchd()["labels"]
    assert ASET in st
    assert ("bootstrap", RADAR) not in acts(box) or RADAR in st


def test_launchctl_gone_after_the_first_bootout_reports_the_residents_down(box):
    done = box.run(STUB_VANISH_AFTER=ASET)
    assert "command not found" in done.stdout + (box.wt / ".deploy-logs").joinpath(
        next(p.name for p in (box.wt / ".deploy-logs").glob("*.log"))
    ).read_text()
    assert done.returncode == 1
    last = last_line(done)
    assert last.startswith(f"FAILED OUTAGE: {ASET} — ")
    assert f"down: {ASET}" in last


def test_the_agent_goes_down_by_cobalt_sh_and_up_by_kickstart(box):
    done = box.run(labels=AGENT)
    assert done.returncode == 0, done.stdout + done.stderr
    calls = [(c["name"], c["argv"]) for c in box.calls_list()]
    assert ("cobalt.sh", ["stop"]) in calls
    assert ("launchctl", ["kickstart", f"gui/501/{AGENT}"]) in calls
    assert calls.index(("cobalt.sh", ["stop"])) < calls.index(("launchctl", ["kickstart", f"gui/501/{AGENT}"]))
    assert box.launchd()["agent"] not in (None, 503)
    assert all(a[0] in ("print", "kickstart") for a in box.launchctl_calls())


def test_dry_run_calls_nothing_and_prints_every_would_run_line_in_order(box):
    for name in ("git", "curl", "uv"):
        stub(box.bin / name, name, PLAIN)
    done = box.run(f"{ASET},{RADAR}", "MERGED", "--dry-run")
    assert done.returncode == 0, done.stdout + done.stderr
    assert box.calls_list() == []
    would = [ln[len("WOULD RUN: "):] for ln in done.stdout.splitlines() if ln.startswith("WOULD RUN: ")]
    order = [w for w in would if w.startswith("launchctl boot")]
    assert order == [
        f"launchctl bootout gui/501/{ASET}",
        f"launchctl bootout gui/501/{RADAR}",
        f"launchctl bootstrap gui/501 {box.aset_plist}",
        f"launchctl bootstrap gui/501 {box.radar_plist}",
    ]
    assert any("cobalt.sh status" in w for w in would)
    assert last_line(done).startswith("DRY RUN — nothing run")
    assert not (box.wt / ".deploy-logs").exists()


def test_dry_run_still_refuses_not_merged(box):
    done = box.run(f"{ASET},{RADAR}", "NOT MERGED", "--dry-run")
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
    assert box.calls_list() == []


def test_d4_dry_run_on_the_10_02_deploy_card(box):
    """RUN row D4: the --dry-run of the real 10-02 night deploy card (the worktree copy, read only)."""
    for name in ("git", "curl", "uv"):
        stub(box.bin / name, name, PLAIN)
    env = {k: v for k, v in box.env.items() if k not in ("COBALT_REPO_ROOT", "COBALT_LAUNCHAGENTS")}
    done = subprocess.run(
        ["sh", str(SCRIPT), "--dry-run", str(REAL_CARD), f"{ASET},{RADAR}", "MERGED"], env=env,
        capture_output=True, text=True, errors="replace", timeout=120,
    )
    print(done.stdout + done.stderr)
    assert box.calls_list() == []
    assert done.returncode == 0
