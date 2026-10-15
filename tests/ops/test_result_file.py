"""The result file (card prompts/2026-10-14/548-result-file-card.md, his R1471 item (3)).

Every BUILT and CHECK DONE stop line gets a `<report minus .md>.result` beside it, one `key=value`
per field of that line, and the three deploy gates read it in place of the free-text line. RF1 the
helper `ops/desk/result-read.sh`; RF2 the two hub lines; RF3 `deploy-step0.sh` P2; RF4
`deploy-card.sh`; RF5 `desk-launch.sh` P2 and the three gates' agreement.

The gate harnesses are the gates' own test files, imported as modules: tests/ops has no
`__init__.py`, so pytest's default (prepend) import mode puts it on sys.path. Every repo is a tmp
repo; nothing here reads a real report, `.env` or database. Each test pins only the lines its own
row changes, found by content (brain R1472).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
import test_deploy_card as dc
import test_deploy_step0 as s0
import test_desk_launch_prechecks as dl

REPO = Path(__file__).resolve().parents[2]
HELPER = REPO / "ops" / "desk" / "result-read.sh"
HUBS = REPO / "docs" / "40 - DevDocs" / "prompts"

# the card's two key lists (THE FILE), the stop lines' own fields in their own order
BUILT_KEYS = ("job tip on migration offline with_db live_note cobalt_dev env restarts rows self_check "
              "decisions for_dejan tokens").split()
CHECK_KEYS = ("job pass tip house_a findings dropped held fixed held_unfixed open house_b offline with_db "
              "live_note cobalt_dev env restarts files_opened ready decisions for_dejan tokens").split()
ALL_KEYS = list(dict.fromkeys(BUILT_KEYS + CHECK_KEYS))
KEYS_LEAD = "one `key=value` per field of that line (`"


def read(key: str, text: str) -> subprocess.CompletedProcess:
    return subprocess.run(["sh", str(HELPER), key], input=text, capture_output=True, text=True, timeout=30)


def check_result(tip: str, **over: str) -> str:
    """A CHECK DONE result file, constructed values only; `over` replaces a key's value."""
    vals = {
        "job": "x", "pass": "1", "tip": tip, "house_a": "grok FINDINGS: 0", "findings": "0",
        "dropped": "0", "held": "0", "fixed": "0", "held_unfixed": "0", "open": "0",
        "house_b": "none available", "offline": "10/0", "with_db": "0/0", "live_note": "5/0",
        "cobalt_dev": "not taken", "env": "removed", "restarts": "none", "files_opened": "3",
        "ready": "YES", "decisions": "0", "for_dejan": "0", "tokens": "1000",
    }
    vals.update(over)
    return "".join(f"{k}={v}\n" for k, v in vals.items())


def built_result(tip: str) -> str:
    """A BUILT result file, constructed values only."""
    vals = {
        "job": "x", "tip": tip, "on": "00000000", "migration": "none", "offline": "10/0",
        "with_db": "0/0", "live_note": "5/0", "cobalt_dev": "not taken", "env": "removed",
        "restarts": "none", "rows": "1 of 1", "self_check": "3 of 3", "decisions": "0",
        "for_dejan": "0", "tokens": "1000",
    }
    return "".join(f"{k}={v}\n" for k, v in vals.items())


def result_of(report: Path) -> Path:
    return report.with_suffix(".result")


# ---- RF1: the helper -----------------------------------------------------------------------------


def test_helper_prints_the_value_of_a_key():
    done = read("tip", "job=x\ntip=5c92b589\nready=YES\n")
    assert (done.returncode, done.stdout, done.stderr) == (0, "5c92b589\n", ""), done
    done = read("house_a", "job=x\nhouse_a=grok FINDINGS: 0 = none\nrows=3 of 3\n")
    assert (done.returncode, done.stdout) == (0, "grok FINDINGS: 0 = none\n"), done
    done = read("rows", "job=x\n\nrows=3 of 3")  # a blank line means nothing; no final newline
    assert (done.returncode, done.stdout) == (0, "3 of 3\n"), done


@pytest.mark.parametrize("key, text", [
    pytest.param("tip", "job=x\ntip 5c92b589\n", id="a line without ="),
    pytest.param("tip", "job=x\nship=1\ntip=5c92b589\n", id="a key outside the lists"),
    pytest.param("tip", "tip=5c92b589\ntip=5c92b589\n", id="a repeated key"),
    pytest.param("tip", "job=x\nready=YES\n", id="the key absent"),
    pytest.param("tip", "job=x\ntip=\n", id="the key empty"),
    pytest.param("ship", "job=x\n", id="asked for a key outside the lists"),
])
def test_helper_refuses_a_bad_file(key, text):
    """Negative control: every bad file is refused; RED on BASE: exit 127, the script absent."""
    done = read(key, text)
    assert done.returncode == 1, done
    assert done.stderr.startswith("REFUSED: "), done.stderr
    assert done.stdout == ""


def helper_list(label: str) -> list[str]:
    hits = [ln for ln in HELPER.read_text(encoding="utf-8").splitlines() if ln.startswith(f"# {label}: ")]
    assert len(hits) == 1, (label, hits)
    return hits[0].split(": ", 1)[1].split()


def test_helper_is_read_only_and_one_shell_file():
    text = HELPER.read_text(encoding="utf-8")
    assert text.startswith("#!/bin/sh\n")
    for word in ("git ", "rm ", "curl"):
        assert word not in text, word
    assert ">" not in text.replace(">&2", "")
    assert helper_list("BUILT keys") == BUILT_KEYS
    assert helper_list("CHECK DONE keys") == CHECK_KEYS
    cases = [ln.strip() for ln in text.splitlines() if ln.strip().startswith("job|")]
    assert len(cases) == 1, cases
    assert cases[0].removesuffix(")").split("|") == ALL_KEYS
    for said in ("read-only", "no write", "no network", "`env`", "`_env`"):
        assert said in text, said


# ---- RF2: the writers, as hub text ---------------------------------------------------------------


def result_line(hub: str) -> str:
    hits = [ln for ln in (HUBS / hub).read_text(encoding="utf-8").splitlines() if "RESULT FILE (his R1471):" in ln]
    assert len(hits) == 1, (hub, hits)
    return hits[0]


def hub_keys(hub: str) -> list[str]:
    line = result_line(hub)
    i = line.index(KEYS_LEAD) + len(KEYS_LEAD)
    return line[i:line.index("`", i)].split()


def test_build_hub_names_the_result_file_once():
    line = result_line("BUILD-HUB.md")
    assert line.startswith('A "DB: none" build writes'), line
    for said in (".result", "for_dejan tokens", "no key added"):
        assert said in line, said


def test_check_hub_names_the_result_file_once():
    line = result_line("CHECK-HUB.md")
    assert line.startswith('A "DB: none" card\'s check writes'), line
    for said in (".result", "held_unfixed", "files_opened", "no key added"):
        assert said in line, said


def test_the_result_key_lists_of_the_hubs_equal_the_helper_s():
    assert hub_keys("BUILD-HUB.md") == helper_list("BUILT keys") == BUILT_KEYS
    assert hub_keys("CHECK-HUB.md") == helper_list("CHECK DONE keys") == CHECK_KEYS


def test_each_hub_keeps_its_one_launch_line():
    """Negative control, green on BASE and after: RF2 adds no line and touches no `claude --bg ` line."""
    for hub in ("BUILD-HUB.md", "CHECK-HUB.md"):
        lines = (HUBS / hub).read_text(encoding="utf-8").splitlines()
        assert sum(ln.startswith("claude --bg ") for ln in lines) == 1, hub


# ---- RF3: deploy-step0.sh P2 ---------------------------------------------------------------------

FREE_TEXT = "CHECK DONE · job: x · reformatted by hand"


@pytest.fixture
def step0(tmp_path):
    return s0.Desk(tmp_path)


def p2_failed(done: subprocess.CompletedProcess) -> str:
    assert done.returncode == 1, done.stdout
    last = s0.last_line(done)
    assert last.startswith("FAILED STEP-0: P2 check 1 — "), done.stdout
    return last


def test_p2_reads_a_result_file_when_the_stop_line_is_free_text(step0):
    """RED on BASE: `FAILED STEP-0: P2 check 1 — … the last line lacks 'held unfixed: 0'`."""
    d = step0
    d.check["alpha"].write_text(f"# check alpha\n\n{FREE_TEXT}\n")
    result_of(d.check["alpha"]).write_text(check_result(d.tip["alpha"]))
    d.commit("alpha check reformatted, its result file beside it")
    done = d.run()
    assert done.returncode == 0, done.stdout
    assert s0.last_line(done) == "STEP-0 OK — window: (iii)"


def test_p2_result_file_ready_no_wins_over_a_clean_stop_line(step0):
    """RED on BASE: P2 passes (the file is not read)."""
    d = step0
    result_of(d.check["alpha"]).write_text(check_result(d.tip["alpha"], ready="NO"))
    d.commit("alpha result says ready NO")
    assert "ready=NO" in p2_failed(d.run())


@pytest.mark.parametrize("ready", ["YES", "NO"])
def test_p2_no_result_file_reads_the_stop_line_as_today(step0, ready):
    """Negative control, green on BASE and after (the shape of test_deploy_step0.py:238)."""
    d = step0
    if ready == "NO":
        d.check["alpha"].write_text(f"# check alpha\n\n{s0.check_line(d.tip['alpha'], ready=ready)}\n")
        d.commit("alpha check")
    done = d.run()
    if ready == "YES":
        assert done.returncode == 0, done.stdout
    else:
        assert "ready: YES" in p2_failed(done)


@pytest.mark.parametrize("bad", ["an unknown key", "a tip that is not the row's code tip"])
def test_p2_a_bad_result_file_fails_p2(step0, bad):
    """RED on BASE: P2 passes on the clean stop line."""
    d = step0
    if bad == "an unknown key":
        text = check_result(d.tip["alpha"]) + "ship=1\n"
    else:
        text = check_result(d.tip["beta"])
    result_of(d.check["alpha"]).write_text(text)
    d.commit("alpha result file, bad")
    p2_failed(d.run())


def test_p2_a_held_row_still_reads_the_stop_line(step0):
    """Green on BASE and after: a held row takes THE RULE on the stop line; the result file beside
    it (clean keys, and a key outside the lists that the helper would refuse) is never read."""
    d = step0
    s0.held_round(d, lines=[s0.FIXED_O1])
    result_of(d.check["alpha"]).write_text(check_result(d.tip["alpha"]) + "ship=1\n")
    d.commit("a result file beside the held check")
    done = d.run()
    assert done.returncode == 0, done.stdout
    assert s0.last_line(done) == "STEP-0 OK — window: (iii)"


def step0_fix_round(d, *, fix_last: str, fix_result: bool) -> str:
    """Alpha's code tip moves past its check by a small fix (the shape of
    test_deploy_step0.py `fix_round`); the fix report, committed on the branch head only, ends
    `fix_last` (`FIXED` stands for the fix tip) and, with `fix_result`, has its result file beside
    it in the same commit. Returns the fix tip."""
    checked = d.tip["alpha"]
    s0.git(d.repo, "checkout", "-q", "ops/alpha")
    (d.repo / "src" / "alpha.py").write_text("alpha = 2\n")
    d.commit("alpha small fix")
    fixed = s0.git(d.repo, "rev-parse", "--short=8", "HEAD")
    fix_report = d.reports / "alpha-fix-build.md"
    fix_report.write_text(f"# alpha fix round\n\n{fix_last.replace('FIXED', fixed)}\n")
    if fix_result:
        result_of(fix_report).write_text(built_result(fixed))
    d.commit("alpha fix report")
    head = s0.git(d.repo, "rev-parse", "--short=8", "HEAD")
    s0.git(d.repo, "checkout", "-q", "main")
    d.tip["alpha"], d.head["alpha"] = fixed, head
    text = d.card_text()
    text = text.replace("its stop line must carry |\n|---|---|---|---|---|---|\n",
                        "its stop line must carry | fix report |\n|---|---|---|---|---|---|---|\n")
    text = text.replace(f"`{head}` | `{d.check['alpha']}` | `held unfixed: 0` and `ready: YES` |\n",
                        f"`{head}` | `{d.check['alpha']}` | `held unfixed: 0` and `ready: YES` | `{fix_report}` |\n")
    text = text.replace(f"`{d.check['beta']}` | `held unfixed: 0` and `ready: YES` |\n",
                        f"`{d.check['beta']}` | `held unfixed: 0` and `ready: YES` | |\n")
    d.card.write_text(text)
    d.check["alpha"].write_text(f"# check alpha\n\n{s0.check_line(checked)}\n")
    d.commit("fix round")
    return fixed


def test_p2_fix_round_tip_from_the_fix_report_result_file(step0):
    """RED on BASE: `the fix report … does not end 'BUILT · … tip: …'`."""
    step0_fix_round(step0, fix_last="fix round done by hand", fix_result=True)
    done = step0.run()
    assert done.returncode == 0, done.stdout
    assert s0.last_line(done) == "STEP-0 OK — window: (iii)"


def test_p2_fix_round_without_a_result_file_reads_the_built_line_as_today(step0):
    """Negative control, green on BASE and after: no result file, a free-text fix report fails."""
    step0_fix_round(step0, fix_last="fix round done by hand", fix_result=False)
    assert "does not end 'BUILT ·" in p2_failed(step0.run())


@pytest.mark.parametrize("state", ["uncommitted", "edited after its commit"])
def test_p2_an_uncommitted_or_edited_result_file_fails_p2(step0, state):
    """RED on BASE: P2 passes, the file ignored (the stop line is clean)."""
    d = step0
    res = result_of(d.check["alpha"])
    if state == "uncommitted":
        res.write_text(check_result(d.tip["alpha"]))
    else:
        res.write_text(check_result(d.tip["alpha"], tokens="1000"))
        d.commit("alpha result file")
        res.write_text(check_result(d.tip["alpha"], tokens="1001"))
    last = p2_failed(d.run())
    assert f"the result file is not committed or is modified since its commit: {res}" in last


# ---- RF4: deploy-card.sh --------------------------------------------------------------------------

FREE_TEXT_DC = "CHECK DONE · job: x · pass: 2 · reformatted by hand"


def dc_commit(d, msg: str) -> None:
    dc.git(d.repo, "add", "-A")
    dc.git(d.repo, "commit", "-q", "-m", msg)


@pytest.fixture
def card(tmp_path):
    return dc.Desk(tmp_path)


def dc_refused(d, done: subprocess.CompletedProcess, text: str) -> None:
    assert done.returncode == 1, done.stdout + done.stderr
    assert f"REFUSED: alpha: {text}" in done.stderr, done.stderr
    assert not d.out.exists()


def test_card_accepts_a_check_whose_stop_line_is_free_text_but_whose_result_file_is_clean(card):
    """RED on BASE: refused `the check's last line lacks 'held unfixed: 0'`."""
    d = card
    d.check["alpha"].write_text(f"# check alpha\n\n{FREE_TEXT_DC}\n")
    result_of(d.check["alpha"]).write_text(check_result(d.tip["alpha"]))
    dc_commit(d, "alpha check reformatted, its result file beside it")
    done = d.run(cards=("alpha",))
    assert done.returncode == 0, done.stderr
    ships = [ln for ln in dc.section(d.out.read_text(), "SHIPS").splitlines() if ln.startswith("| ")
             and not ln.startswith("| #")]
    assert ships == [f"| 1 | `ops/alpha` | `{d.tip['alpha']}` | `{d.head['alpha']}` | `{d.check['alpha']}` "
                     "| `held unfixed: 0` and `ready: YES` | |"], ships


@pytest.mark.parametrize("state", ["uncommitted", "edited after its commit", "staged"])
def test_card_refuses_an_uncommitted_or_edited_result_file(card, state):
    """RED on BASE: the card is written, the file ignored."""
    d = card
    res = result_of(d.check["alpha"])
    res.write_text(check_result(d.tip["alpha"]))
    if state != "uncommitted":
        dc_commit(d, "alpha result file")
        res.write_text(check_result(d.tip["alpha"], tokens="1001"))
    if state == "staged":
        dc.git(d.repo, "add", str(res))
        res.write_text(check_result(d.tip["alpha"]))
    dc_refused(d, d.run(cards=("alpha",)),
               f"the check's result file is not committed or is modified since its commit: {res}")


def test_card_refuses_result_ready_no(card):
    """RED on BASE: the card is written."""
    d = card
    result_of(d.check["alpha"]).write_text(check_result(d.tip["alpha"], ready="NO"))
    dc_commit(d, "alpha result says ready NO")
    done = d.run(cards=("alpha",))
    assert done.returncode == 1 and "ready=NO" in done.stderr, done.stderr
    assert not d.out.exists()


@pytest.mark.parametrize("ready", ["YES", "NO"])
def test_card_with_no_result_file_reads_the_stop_line_as_today(card, ready):
    """Negative control, green on BASE and after (the shape of test_deploy_card.py:232)."""
    d = card
    d.check["alpha"].write_text(f"# check\n\n{dc.check_line(d.tip['alpha'], ready=ready)}")
    dc_commit(d, "alpha check")
    done = d.run()
    if ready == "NO":
        dc_refused(d, done, "the check's last line lacks 'ready: YES'")
        return
    assert done.returncode == 0, done.stderr
    assert dc.ships_row(d.out.read_text(), 1) == (
        f"| 1 | `ops/alpha` | `{d.tip['alpha']}` | `{d.head['alpha']}` | `{d.check['alpha']}` "
        "| `held unfixed: 0` and `ready: YES` | |")


def test_card_a_held_stop_line_beside_a_clean_result_file_with_no_fix_report_is_refused(card):
    """Green on BASE and after: `hn` is read whenever the result file exists; with no fix report
    a held line is refused as `deploy-card.sh` refuses it today."""
    d = card
    d.check["alpha"].write_text(f"# check\n\n{dc.check_line(d.tip['alpha'], held='1')}")
    result_of(d.check["alpha"]).write_text(check_result(d.tip["alpha"]))
    dc_commit(d, "alpha held, a clean result file beside it")
    dc_refused(d, d.run(cards=("alpha",)), "the check's last line lacks 'held unfixed: 0'")


def test_card_fix_round_tip_from_the_fix_report_result_file(card):
    """RED on BASE: refused `the fix report's last line is not 'BUILT ·' with a 'tip:'`."""
    d = card
    dc.git(d.repo, "checkout", "-q", "ops/alpha")
    (d.repo / "src" / "alpha.py").write_text("alpha = 2\n")
    dc.git(d.repo, "commit", "-q", "-am", "alpha small fix")
    fixed = dc.git(d.repo, "rev-parse", "--short=8", "HEAD")
    report = d.reports / "alpha-fix.md"
    report.write_text("# alpha fix round\n\nfix round done by hand\n")
    result_of(report).write_text(built_result(fixed))
    dc_commit(d, "alpha fix report")
    dc.git(d.repo, "checkout", "-q", "main")
    done = d.run("--fix-report", f"alpha={report}", cards=("alpha",))
    assert done.returncode == 0, done.stderr
    cells = [c.strip() for c in dc.ships_row(d.out.read_text(), 1).split("|")]
    assert cells[3] == f"`{fixed}`", cells


# ---- RF5: desk-launch.sh deploy P2 ---------------------------------------------------------------

FREE_TEXT_DL = "CHECK DONE · job: x-job · reformatted by hand"


@pytest.fixture
def launch(tmp_path):
    return dl.Desk(tmp_path)


def test_launcher_accepts_a_free_text_check_with_a_clean_result_file(launch):
    """RED on BASE: `deploy ops/x-job: its stop line lacks 'held unfixed: 0' — the check is not clean`."""
    d = launch
    d.ship(FREE_TEXT_DL, commit=False)
    result_of(d.check_report).write_text(check_result(d.tip))
    d.commit("check report and its result file")
    done = d.launch("deploy", str(d.deploy))
    assert done.returncode == 0, done.stderr
    assert (d.wt / "x-gate").is_dir()


def test_launcher_refuses_result_ready_no_on_a_clean_stop_line(launch):
    """RED on BASE: launches."""
    d = launch
    d.ship(commit=False)
    result_of(d.check_report).write_text(check_result(d.tip, ready="NO"))
    d.commit("check report and its result file")
    done = d.launch("deploy", str(d.deploy))
    assert done.returncode == 1, done.stdout + done.stderr
    assert "REFUSED: deploy ops/x-job: " in done.stderr and "ready=NO" in done.stderr, done.stderr
    assert d.called() == [] and not d.gate_left()


@pytest.mark.parametrize("brk", ["break_ready_no", "break_held_unfixed"])
def test_launcher_with_no_result_file_refuses_as_today(launch, brk):
    """Negative control, green on BASE and after: test_desk_launch_prechecks.py:561 and :566."""
    text = getattr(dl, brk)(launch)
    dl.refused(launch, launch.launch("deploy", str(launch.deploy)), text)


def test_launcher_refuses_an_uncommitted_result_file(launch):
    """RED on BASE: launches, the file ignored."""
    d = launch
    d.ship()
    res = result_of(d.check_report)
    res.write_text(check_result(d.tip))
    dl.refused(d, d.launch("deploy", str(d.deploy)),
               f"deploy ops/x-job: the check's result file is not committed or differs from its commit — commit {res}")


def test_launcher_fix_round_tip_from_the_fix_report_result_file(launch):
    """RED on BASE: refused `… is neither the code tip … nor the branch head …`."""
    d = launch
    checked = d.tip
    (d.job_wt / "src" / "x.py").write_text("X = 2\n")
    d.commit_job("small fix after the check")
    fixed = dl.short(d.job_wt)
    copy = d.job_wt / dl.FIX_REL
    copy.write_text("# x-job fix round\n\nfix round done by hand\n")
    result_of(copy).write_text(built_result(fixed))
    d.commit_job("fix report and its result file")
    head = dl.short(d.job_wt)
    d.write_deploy(code_tip=fixed, head=head, fix=str(d.repo / dl.FIX_REL))
    d.ship(dl.check_line(checked))
    done = d.launch("deploy", str(d.deploy))
    assert done.returncode == 0, done.stderr
    assert (d.wt / "x-gate").is_dir()


# ---- RF5 (4): the three gates agree --------------------------------------------------------------

AGREE = [
    ("a clean result file beside a free-text line", "ok"),
    ("ready=NO", "refused"),
    ("a key outside the lists", "refused"),
    ("a tip that is not the code tip", "refused"),
    ("an uncommitted result file", "refused"),
    ("a result file edited after its commit", "refused"),
    ("no result file", "ok"),
    ("a held stop line beside a clean result file, no fix report", "refused"),
]


def stage(case: str, *, check: Path, tip: str, other: str, clean: str, held: str, free: str, commit) -> None:
    """One row of AGREE, written on a gate's own check report; `commit` commits the tmp repo."""
    line = {AGREE[0][0]: free, AGREE[7][0]: held}.get(case, clean)
    check.write_text(f"# check\n\n{line}\n")
    if case == "no result file":
        commit()
        return
    over = {"ready=NO": {"ready": "NO"}, "a tip that is not the code tip": {"tip": other}}.get(case, {})
    over = dict(over)
    text = check_result(over.pop("tip", tip), **over) + ("ship=1\n" if case == "a key outside the lists" else "")
    res = result_of(check)
    if case == "an uncommitted result file":
        commit()
        res.write_text(text)
        return
    res.write_text(text)
    commit()
    if case == "a result file edited after its commit":
        res.write_text(text.replace("tokens=1000", "tokens=1001"))


def verdict_step0(root: Path, case: str) -> str:
    d = s0.Desk(root)
    stage(case, check=d.check["alpha"], tip=d.tip["alpha"], other=d.tip["beta"],
          clean=s0.check_line(d.tip["alpha"]), held=s0.check_line(d.tip["alpha"], held="1"),
          free=FREE_TEXT, commit=lambda: d.commit("case"))
    return "ok" if d.run().returncode == 0 else "refused"


def verdict_card(root: Path, case: str) -> str:
    d = dc.Desk(root)
    stage(case, check=d.check["alpha"], tip=d.tip["alpha"], other=d.tip["beta"],
          clean=dc.check_line(d.tip["alpha"]), held=dc.check_line(d.tip["alpha"], held="1"),
          free=FREE_TEXT_DC, commit=lambda: dc_commit(d, "case"))
    return "ok" if d.run(cards=("alpha",)).returncode == 0 else "refused"


def verdict_launch(root: Path, case: str) -> str:
    d = dl.Desk(root)
    stage(case, check=d.check_report, tip=d.tip, other=d.base,
          clean=dl.check_line(d.tip), held=dl.check_line(d.tip, held_unfixed=1),
          free=FREE_TEXT_DL, commit=lambda: d.commit("case"))
    return "ok" if d.launch("deploy", str(d.deploy)).returncode == 0 else "refused"


@pytest.mark.parametrize("case, want", AGREE, ids=[c for c, _ in AGREE])
def test_the_three_gates_agree(tmp_path, case, want):
    """RED on BASE: the first row is refused by all three, not ok."""
    got = {}
    for name, gate in (("deploy-step0.sh", verdict_step0), ("deploy-card.sh", verdict_card),
                       ("desk-launch.sh", verdict_launch)):
        root = tmp_path / name
        root.mkdir()
        got[name] = gate(root, case)
    assert got == dict.fromkeys(got, want), got
