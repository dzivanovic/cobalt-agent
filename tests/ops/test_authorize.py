"""ops/desk/authorize.sh — a fixed file's AUTHORIZATION block as one table (card 19 worker-steps S1).

Every run points the script at a tmp repo standing in for /Users/cobalt/cobalt
(COBALT_REPO_ROOT): a fixed file whose title cites its standing-list row, committed
desk reports holding approved rows, and a committed card. The real repo is never read.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
AUTHORIZE = REPO / "ops" / "desk" / "authorize.sh"

# the two tokens are built, never written whole, so no grep of this file ever matches one
INSTALL_TOKEN = "«" + "INSTALL"
FILL_TOKEN = "«" + "FILL"

GIT_ENV = {
    "GIT_AUTHOR_NAME": "test",
    "GIT_AUTHOR_EMAIL": "test@example.invalid",
    "GIT_COMMITTER_NAME": "test",
    "GIT_COMMITTER_EMAIL": "test@example.invalid",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_NOSYSTEM": "1",
}

TITLE = "# BUILD-HUB — the fixed build file (INSTALLED 2026-01-01 · STANDING = INSTALL: 2026-01-01 R1 of his approval of STANDING-LIST.md)\n"
R1 = "| R1 | 09:00 ET | **HIS RULING**: approves the standing list. | APPROVED |\n"
R2 = "| R2 | 09:05 ET | HIS RULING: the job's ruling. | HIS RULING · APPROVED |\n"
R3 = "| R3 | 09:10 ET | HIS RULING: the house overrule. | APPROVED |\n"


def git(cwd: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-c", "core.hooksPath=/dev/null", *args], cwd=cwd,
        env=dict(os.environ, **GIT_ENV), capture_output=True, text=True, check=True,
    )
    return done.stdout.strip()


def card_text(rulings: str = "2026-01-02 R2", extra: str = "") -> str:
    return (
        "JOB: x-job\nLADDER: OFF-LADDER\nBRANCH: ops/x-job\nWORKTREE: x-job\n"
        "BASE: 0000aaaa\nTIP:\nREPORT: /nowhere/x-job-build.md\n"
        f"TREE STATE: unchanged\nRULINGS: {rulings}\n{extra}\n## ROWS\n| row | what |\n"
    )


@pytest.fixture
def desk(tmp_path):
    repo = tmp_path / "repo"
    prompts = repo / "docs" / "40 - DevDocs" / "prompts"
    reports = repo / "docs" / "40 - DevDocs" / "reports"
    (prompts / "2026-01-02").mkdir(parents=True)
    reports.mkdir(parents=True)
    (prompts / "BUILD-HUB.md").write_text(TITLE + "\nbody\n")
    (prompts / "CHECK-HUB.md").write_text(TITLE.replace("BUILD-HUB", "CHECK-HUB") + "\nbody\n")
    (prompts / "DEPLOY-HUB.md").write_text(
        "# DEPLOY-HUB — the fixed deploy file (INSTALLED 2026-01-01 · STANDING = INSTALL: "
        "2026-01-01 R1 (+ R9 string changes) of his approval of STANDING-LIST.md)\n\nbody\n"
    )
    (reports / "cto-2026-01-01.md").write_text("| row | time | what | state |\n|---|---|---|---|\n" + R1)
    (reports / "cto-2026-01-02.md").write_text("| row | time | what | state |\n|---|---|---|---|\n" + R2 + R3)
    card = prompts / "2026-01-02" / "01-x-job-card.md"
    card.write_text(card_text())
    git(repo, "init", "-q", "-b", "main")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "base")
    env = dict(os.environ, COBALT_REPO_ROOT=str(repo), COBALT_WT_ROOT=str(tmp_path / "wt"), **GIT_ENV)
    return repo, card, env


def authorize(env: dict, kind: str, card: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(AUTHORIZE), kind, str(card)], env=env, capture_output=True, text=True, timeout=120
    )


def last_line(done: subprocess.CompletedProcess) -> str:
    return [ln for ln in done.stdout.splitlines() if ln.strip()][-1]


def recommit(repo: Path, card: Path, text: str) -> None:
    card.write_text(text)
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "card")


def test_a_complete_committed_card_is_authorized_with_every_row_printed(desk):
    repo, card, env = desk
    done = authorize(env, "build", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "AUTHORIZED"
    rows = done.stdout.splitlines()[:-1]
    names = [r.split(" · ")[0] for r in rows if " · " in r]
    for rule in (
        "INSTALLED", "PLACEHOLDER", "CARD COMMITTED", "CARD UNCHANGED",
        "STANDING LIST 2026-01-01 R1 row", "STANDING LIST 2026-01-01 R1 committed",
        "RULING 2026-01-02 R2 row", "RULING 2026-01-02 R2 committed",
    ):
        assert rule in names, (rule, done.stdout)
    # every row carries its four fields: rule · command · exit · result
    for r in rows:
        if " · " in r and not r.startswith("    "):
            assert len(r.split(" · ")) >= 4, r


def test_a_ruling_row_without_approved_fails_naming_it(desk):
    repo, card, env = desk
    reports = repo / "docs" / "40 - DevDocs" / "reports"
    (reports / "cto-2026-01-02.md").write_text(
        "| row |\n" + R2.replace("HIS RULING · APPROVED", "HIS RULING · PROPOSED") + R3
    )
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "unapproved")
    done = authorize(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED: authorization mismatch — RULING 2026-01-02 R2 row"


def test_a_ruling_row_only_in_the_working_tree_fails(desk):
    repo, card, env = desk
    reports = repo / "docs" / "40 - DevDocs" / "reports"
    with (reports / "cto-2026-01-02.md").open("a") as f:
        f.write("| R4 | 09:20 ET | HIS RULING: not committed yet. | APPROVED |\n")
    recommit_card = card_text("2026-01-02 R4")
    card.write_text(recommit_card)
    git(repo, "add", str(card))
    git(repo, "commit", "-q", "-m", "card cites R4", "--", str(card))
    done = authorize(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED: authorization mismatch — RULING 2026-01-02 R4 committed"


def test_approved_only_in_the_working_tree_over_a_committed_unapproved_row_fails(desk):
    repo, card, env = desk
    reports = repo / "docs" / "40 - DevDocs" / "reports"
    path = reports / "cto-2026-01-02.md"
    path.write_text("| row |\n" + R2.replace("HIS RULING · APPROVED", "HIS RULING · PROPOSED") + R3)
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "proposed")
    path.write_text("| row |\n" + R2 + R3)  # APPROVED typed, never committed
    done = authorize(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED: authorization mismatch — RULING 2026-01-02 R2 committed"


def test_a_card_with_a_placeholder_token_fails(desk):
    repo, card, env = desk
    recommit(repo, card, card_text() + f"\n{FILL_TOKEN}: the stop line\n")
    done = authorize(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED: authorization mismatch — PLACEHOLDER"


def test_a_card_modified_after_its_commit_fails(desk):
    repo, card, env = desk
    card.write_text(card_text() + "\nan edit after the commit\n")
    done = authorize(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED: authorization mismatch — CARD UNCHANGED"


def test_a_card_never_committed_fails(desk):
    repo, card, env = desk
    other = card.parent / "02-y-job-card.md"
    other.write_text(card_text())
    done = authorize(env, "build", other)
    assert done.returncode == 1
    assert last_line(done) == "FAILED: authorization mismatch — CARD COMMITTED"


def test_a_title_that_still_holds_the_install_token_fails(desk):
    repo, card, env = desk
    hub = repo / "docs" / "40 - DevDocs" / "prompts" / "BUILD-HUB.md"
    hub.write_text(TITLE.replace("INSTALLED 2026-01-01", f"{INSTALL_TOKEN}: his row") + "\nbody\n")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "uninstalled")
    done = authorize(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED: authorization mismatch — INSTALLED"


def test_rulings_none_passes_with_no_ruling_row(desk):
    repo, card, env = desk
    recommit(repo, card, card_text("none"))
    done = authorize(env, "build", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "AUTHORIZED"
    assert "RULING 2026" not in done.stdout


def test_a_ruling_in_another_dates_file_is_not_found(desk):
    repo, card, env = desk
    recommit(repo, card, card_text("2026-01-01 R2"))  # R2 lives in cto-2026-01-02.md only
    done = authorize(env, "build", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED: authorization mismatch — RULING 2026-01-01 R2 row"


def test_two_rulings_of_one_date_are_each_proved(desk):
    repo, card, env = desk
    recommit(repo, card, card_text("2026-01-02 R2, R3"))
    done = authorize(env, "build", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert "RULING 2026-01-02 R3 committed · " in done.stdout


def test_a_house_overrule_is_proved_like_a_ruling(desk):
    repo, card, env = desk
    recommit(repo, card, card_text(extra="HOUSE A: none — overruled 2026-01-02 R3"))
    done = authorize(env, "check", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert "HOUSE A overruled 2026-01-02 R3 committed · " in done.stdout
    recommit(repo, card, card_text(extra="HOUSE A: none — overruled 2026-01-02 R7"))
    done = authorize(env, "check", card)
    assert done.returncode == 1
    assert last_line(done) == "FAILED: authorization mismatch — HOUSE A overruled 2026-01-02 R7 row"


def test_an_openai_house_line_with_its_approved_row_is_authorized(desk):
    """Card 298 S4 (his 2026-10-10 R920): the line that lets Sol be probed spends his OpenAI
    meter, so it is proved like a ruling — row, committed, at HEAD."""
    repo, card, env = desk
    recommit(repo, card, card_text(extra="HOUSE A: OpenAI — his 2026-01-02 R2"))
    done = authorize(env, "check", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "AUTHORIZED"
    for rule in ("row", "committed", "at HEAD"):
        assert f"HOUSE A OpenAI 2026-01-02 R2 {rule} · " in done.stdout, (rule, done.stdout)


@pytest.mark.parametrize(
    ("extra", "proposed", "failed"),
    [
        ("HOUSE A: OpenAI — his 2026-01-02 R7", False, "HOUSE A OpenAI 2026-01-02 R7 row"),
        ("HOUSE A: OpenAI — his 2026-01-02 R2", True, "HOUSE A OpenAI 2026-01-02 R2 row"),
        ("HOUSE A: OpenAI — his 2026-01-02 R2 and more", False, "HOUSE A OpenAI"),
        ("HOUSE A: OpenAI", False, "HOUSE A OpenAI"),
        (
            "HOUSE A: none — overruled 2026-01-02 R3\nHOUSE A: OpenAI — his 2026-01-02 R7",
            False,
            "HOUSE A OpenAI 2026-01-02 R7 row",
        ),
    ],
    ids=["no-such-row", "proposed", "tail", "openai-alone", "second-house-a-line"],
)
def test_an_openai_house_line_without_its_row_fails(desk, extra, proposed, failed):
    repo, card, env = desk
    if proposed:
        reports = repo / "docs" / "40 - DevDocs" / "reports"
        (reports / "cto-2026-01-02.md").write_text(
            "| row |\n" + R2.replace("HIS RULING · APPROVED", "HIS RULING · PROPOSED") + R3
        )
    recommit(repo, card, card_text("none", extra=extra))
    done = authorize(env, "check", card)
    assert done.returncode == 1, done.stdout + done.stderr
    assert last_line(done).startswith(f"FAILED: authorization mismatch — {failed}"), done.stdout


@pytest.mark.parametrize("extra", ["", "HOUSE A: none — overruled 2026-01-02 R3"], ids=["plain", "none-overruled"])
def test_a_card_without_an_openai_line_prints_no_openai_row(desk, extra):
    repo, card, env = desk
    if extra:  # the plain card is the fixture's own, already committed
        recommit(repo, card, card_text(extra=extra))
    done = authorize(env, "check", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "AUTHORIZED"
    assert "HOUSE A OpenAI" not in done.stdout


def test_check_o1_a_first_openai_line_does_not_hide_a_later_overrule(desk):
    repo, card, env = desk
    recommit(repo, card, card_text("none", extra="HOUSE A: OpenAI — his 2026-01-02 R2\nHOUSE A: none — overruled 2026-01-02 R7"))
    done = authorize(env, "check", card)
    assert done.returncode == 1, done.stdout
    assert last_line(done).startswith("FAILED: authorization mismatch — HOUSE A overruled 2026-01-02 R7"), done.stdout


def test_the_deploy_kind_reads_the_first_row_of_its_own_title(desk):
    repo, card, env = desk
    done = authorize(env, "deploy", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert "STANDING LIST 2026-01-01 R1 row · " in done.stdout
    assert "DEPLOY-HUB.md" in done.stdout


def test_s4_kind_shadow_reads_shadow_hub_and_the_build_rows(desk):
    """Card 324 S4: the gate seat's AUTHORIZATION, its hub SHADOW-HUB.md, its rows as build's."""
    repo, card, env = desk
    (repo / "docs" / "40 - DevDocs" / "prompts" / "SHADOW-HUB.md").write_text(
        TITLE.replace("BUILD-HUB", "SHADOW-HUB") + "\nbody\n")
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", "shadow hub")
    done = authorize(env, "shadow", card)
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "AUTHORIZED"
    assert "SHADOW-HUB.md" in done.stdout
    build = authorize(env, "build", card)
    names = lambda d: [r.split(" · ")[0] for r in d.stdout.splitlines() if " · " in r]  # noqa: E731
    assert names(done) == names(build)


@pytest.mark.parametrize("args", [[], ["build"], ["judge", "x"], ["build", "/no/such/card.md"]])
def test_a_bad_call_is_refused(desk, args):
    repo, card, env = desk
    done = subprocess.run(
        ["sh", str(AUTHORIZE), *args], env=env, capture_output=True, text=True, timeout=60
    )
    assert done.returncode == 1
    assert done.stderr.startswith("REFUSED: ")
