"""desk-launch.sh install-ops (card prompts/2026-10-02/16-ops-seam-card.md, row P4).

`sh desk-launch.sh install-ops` links every regular `ops/desk/*.sh` and `ops/desk/*.py` of the
repo root into the link folder as `<link folder>/<name>` -> `<repo>/ops/desk/<name>`. A plain
regular file at the name is replaced by the link (card 2026-10-08 106 G3): `REPLACED: <name>` when
it differed from the repo copy, no line when identical. A symlink (to the repo, elsewhere or
dangling) or any other kind at the name is left untouched and printed KEPT; a link is never
re-pointed.

Every run points the script at a tmp repo (COBALT_REPO_ROOT) and a tmp link folder
(COBALT_OPS_LINK_DIR). desk-launch.sh runs from a copy under tmp_path with a stub
desk-context.sh beside it, the way tests/ops/test_desk_size_guard.py stubs the desk-size guard.
Nothing outside tmp_path is read, written or linked.
"""

from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

LAUNCH = Path(__file__).resolve().parents[2] / "ops" / "desk" / "desk-launch.sh"
REFUSED_300000 = "REFUSED: desk at 300000 tokens — REFRESH first"
KEPT_BYTES = "#!/bin/sh\n# a plain file the desk already keeps here\n"


@pytest.fixture
def world(tmp_path):
    repo = tmp_path / "repo"
    desk = repo / "ops" / "desk"
    desk.mkdir(parents=True)
    for name in ("alpha.sh", "beta.py", "gamma.sh"):
        (desk / name).write_text(f"# constructed {name}\n")
    links = tmp_path / "links"
    links.mkdir()
    (links / "gamma.sh").write_text(KEPT_BYTES)
    ops = tmp_path / "ops"
    ops.mkdir()
    launch = ops / "desk-launch.sh"
    launch.write_text(LAUNCH.read_text())
    launch.chmod(0o755)
    guard(tmp_path, refuse=False)
    env = dict(os.environ, COBALT_REPO_ROOT=str(repo), COBALT_OPS_LINK_DIR=str(links))
    env.pop("CLAUDE_JOB_DIR", None)
    return repo, links, launch, env


def guard(tmp_path: Path, refuse: bool) -> None:
    body = f'#!/bin/sh\necho "$*" >> "{tmp_path}/guard-calls"\n'
    body += f'echo "{REFUSED_300000}"\nexit 3\n' if refuse else "exit 0\n"
    stub = tmp_path / "ops" / "desk-context.sh"
    stub.write_text(body)
    stub.chmod(0o755)


def run(launch: Path, env: dict, *args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["sh", str(launch), "install-ops", *args], env=env, capture_output=True, text=True,
        timeout=60,
    )


def test_install_ops_links_the_missing_names_and_replaces_the_stale_plain_one(world, tmp_path):
    repo, links, launch, env = world
    done = run(launch, env)
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [
        "LINKED alpha.sh",
        "REPLACED: gamma.sh",
        "LINKED beta.py",
        "install-ops: 2 linked, 1 replaced, 0 kept",
    ]
    for name in ("alpha.sh", "beta.py", "gamma.sh"):
        assert (links / name).is_symlink()
        assert os.readlink(links / name) == str(repo / "ops" / "desk" / name)
    assert (tmp_path / "guard-calls").read_text() == "--guard\n"


def test_a_second_run_links_nothing_and_keeps_all_three(world):
    repo, links, launch, env = world
    assert run(launch, env).returncode == 0
    before = {p.name: os.readlink(p) for p in links.iterdir() if p.is_symlink()}
    done = run(launch, env)
    assert done.returncode == 0, done.stderr
    assert done.stdout.splitlines() == [
        "KEPT alpha.sh",
        "KEPT gamma.sh",
        "KEPT beta.py",
        "install-ops: 0 linked, 0 replaced, 3 kept",
    ]
    assert {p.name: os.readlink(p) for p in links.iterdir() if p.is_symlink()} == before
    # the first run replaced the plain gamma.sh: all three are the repo's links now
    assert before == {n: str(repo / "ops" / "desk" / n) for n in ("alpha.sh", "beta.py", "gamma.sh")}


def test_a_stale_plain_desk_list_is_replaced_by_the_link(world):
    """Card 106 G3: the 10-07 close found a stale plain desk-list.sh that install-ops kept."""
    repo, links, launch, env = world
    (repo / "ops" / "desk" / "desk-list.sh").write_text("# constructed desk-list.sh\n")
    (links / "desk-list.sh").write_text(KEPT_BYTES)
    done = run(launch, env)
    assert done.returncode == 0, done.stderr
    assert "REPLACED: desk-list.sh" in done.stdout.splitlines()
    assert (links / "desk-list.sh").is_symlink()
    assert os.readlink(links / "desk-list.sh") == str(repo / "ops" / "desk" / "desk-list.sh")
    assert not (links / ".desk-list.sh.new").exists()


def test_an_identical_plain_file_is_replaced_silently(world):
    repo, links, launch, env = world
    (links / "alpha.sh").write_text((repo / "ops" / "desk" / "alpha.sh").read_text())
    done = run(launch, env)
    assert done.returncode == 0, done.stderr
    assert [l for l in done.stdout.splitlines() if "alpha.sh" in l] == []
    assert (links / "alpha.sh").is_symlink()
    assert os.readlink(links / "alpha.sh") == str(repo / "ops" / "desk" / "alpha.sh")
    assert done.stdout.splitlines()[-1] == "install-ops: 1 linked, 2 replaced, 0 kept"


def test_a_failed_replace_is_refused_and_the_plain_file_stays(world):
    repo, links, launch, env = world
    (links / ".gamma.sh.new").write_text("# in the way\n")
    done = run(launch, env)
    assert done.returncode == 1
    assert done.stderr.splitlines()[-1] == f"REFUSED: install-ops: the replace failed: {links}/gamma.sh"
    assert not (links / "gamma.sh").is_symlink()
    assert (links / "gamma.sh").read_text() == KEPT_BYTES


def test_a_directory_at_the_name_stays_kept(world):
    repo, links, launch, env = world
    (links / "alpha.sh").mkdir()
    done = run(launch, env)
    assert done.returncode == 0, done.stderr
    assert "KEPT alpha.sh" in done.stdout.splitlines()
    assert (links / "alpha.sh").is_dir() and not (links / "alpha.sh").is_symlink()


def test_an_existing_link_to_elsewhere_is_never_re_pointed(world, tmp_path):
    repo, links, launch, env = world
    (links / "alpha.sh").symlink_to(tmp_path / "elsewhere.sh")  # dangling, and not the repo's
    done = run(launch, env)
    assert done.returncode == 0, done.stderr
    assert "KEPT alpha.sh" in done.stdout.splitlines()
    assert os.readlink(links / "alpha.sh") == str(tmp_path / "elsewhere.sh")
    assert done.stdout.splitlines()[-1] == "install-ops: 1 linked, 1 replaced, 1 kept"


def test_only_regular_sh_and_py_files_are_linked(world):
    repo, links, launch, env = world
    desk = repo / "ops" / "desk"
    (desk / "pre-commit").write_text("# no suffix\n")
    (desk / "notes.md").write_text("# not a script\n")
    (desk / "folder.sh").mkdir()
    done = run(launch, env)
    assert done.returncode == 0, done.stderr
    assert sorted(p.name for p in links.iterdir()) == ["alpha.sh", "beta.py", "gamma.sh"]
    assert done.stdout.splitlines()[-1] == "install-ops: 2 linked, 1 replaced, 0 kept"


def test_a_symlink_under_ops_desk_is_not_linked(world):
    repo, links, launch, env = world
    (repo / "ops" / "desk" / "delta.sh").symlink_to(repo / "ops" / "desk" / "alpha.sh")
    done = run(launch, env)
    assert done.returncode == 0, done.stderr
    assert sorted(p.name for p in links.iterdir()) == ["alpha.sh", "beta.py", "gamma.sh"]
    assert "delta.sh" not in done.stdout


def test_a_missing_link_folder_is_refused_and_never_made(world):
    repo, links, launch, env = world
    links.joinpath("gamma.sh").unlink()
    links.rmdir()
    done = run(launch, env)
    assert done.returncode == 1
    assert done.stderr == f"REFUSED: install-ops: no link folder {links}\n"
    assert done.stdout == ""
    assert not links.exists()


def test_one_extra_argument_is_refused_and_nothing_is_linked(world):
    repo, links, launch, env = world
    done = run(launch, env, "extra")
    assert done.returncode == 1
    assert done.stderr == "REFUSED: usage: desk-launch.sh install-ops\n"
    assert done.stdout == ""
    assert sorted(p.name for p in links.iterdir()) == ["gamma.sh"]


def test_a_refusing_guard_stops_install_ops_before_any_link(world, tmp_path):
    repo, links, launch, env = world
    guard(tmp_path, refuse=True)
    done = run(launch, env)
    assert (done.returncode, done.stdout) == (3, REFUSED_300000 + "\n")
    assert sorted(p.name for p in links.iterdir()) == ["gamma.sh"]
