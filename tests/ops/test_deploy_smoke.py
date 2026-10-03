"""ops/desk/deploy-smoke.sh — a deploy card's smoke reads and markers as one run (card 20, row D3).

The card's rows point at files on a tmp root; `curl` and `uv` are stubs on PATH that record their
arguments (and the COBALT_ENV they saw) and answer from the test: `curl` answers `000` twice and
`200` on the third try. Production, launchd, the real repo and the network are never touched.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "ops" / "desk" / "deploy-smoke.sh"
REAL_CARD = REPO / "docs" / "40 - DevDocs" / "prompts" / "2026-10-02" / "25-deploy-scripts-card.md"

RECORD = """#!__PY__
import json, os, sys
with open(os.environ["STUB_CALLS"], "a") as f:
    f.write(json.dumps({"name": "__NAME__", "argv": sys.argv[1:], "env": os.environ.get("COBALT_ENV")}) + "\\n")
""".replace("__PY__", sys.executable)

CURL = """
n_path = os.environ["CURL_COUNT"]
n = int(open(n_path).read()) if os.path.exists(n_path) else 0
open(n_path, "w").write(str(n + 1))
if n + 1 < int(os.environ.get("CURL_OK_ON", "3")):
    sys.stdout.write("000")
    sys.exit(7)
sys.stdout.write("200")
"""

UV = """
print(os.environ.get("UV_ANSWER", "7"))
"""

PLAIN = "sys.exit(0)\n"
CURL_CMD = r"curl -s -o /dev/null -w %{http_code} http://127.0.0.1:5010/radar\?frame=phone"


def stub(bin_dir: Path, name: str, body: str) -> None:
    (bin_dir / name).write_text(RECORD.replace("__NAME__", name) + body)
    (bin_dir / name).chmod(0o755)


class Box:
    def __init__(self, tmp_path: Path) -> None:
        root = tmp_path.resolve()
        self.root = root
        self.files = root / "prod"
        self.files.mkdir()
        (self.files / "a.txt").write_text("a\n")
        (self.files / "b.txt").write_text("needle one\nneedle two\nhay\n")
        (self.files / "new.txt").write_text("new\n")
        (self.files / "c.txt").write_text("the marker line\n")
        self.card = root / "deploy-x-set-card.md"
        self.wt = root / "wt"
        self.wt.mkdir()
        self.bin = root / "bin"
        self.bin.mkdir()
        self.calls = root / "calls.jsonl"
        stub(self.bin, "curl", CURL)
        stub(self.bin, "uv", UV)
        self.env = dict(
            os.environ, STUB_CALLS=str(self.calls), CURL_COUNT=str(root / "curl-count"),
            COBALT_WT_ROOT=str(self.wt), DEPLOY_SETTLE="0",
            PATH=f"{self.bin}{os.pathsep}{os.environ['PATH']}",
        )
        self.write()

    def write(self, *, migrations: str = "none", smoke_extra: str = "", markers: str | None = None) -> None:
        f = self.files
        if markers is None:
            markers = (
                f"- `ls {f}/new.txt` · before `No such file or directory` · after listed\n"
                f'- `grep -c -F "marker" {f}/c.txt` · before `0` · after `1`\n'
            )
        self.card.write_text(
            "JOB: x-set\nBRANCH: deploy/x-set\nTIP: aaaaaaaa\nRULINGS: none\nTAG: x-tag\n"
            f"MIGRATIONS: {migrations}\nSET: xset\n\n## SHIPS\n\n"
            f"## MARKERS\n{markers}\n"
            "## SMOKE READS\n"
            f"- file a · `ls {f}/a.txt` · exit 0, listed\n"
            f'- needle exact · `grep -c -F "needle" {f}/b.txt` · exit 0, `2`\n'
            f'- needle some · `grep -c -F "needle" {f}/b.txt` · exit 0, a count of 1 or more\n'
            f"- radar phone · `{CURL_CMD}` · exit 0, `200`\n"
            f"{smoke_extra}\n## RECORDS\n- a desk fact\n"
        )

    def run(self, *flags: str, **env: str):
        return subprocess.run(
            ["sh", str(SCRIPT), *flags, str(self.card)], env=dict(self.env, **env),
            capture_output=True, text=True, errors="replace", timeout=120,
        )

    def calls_list(self) -> list[dict]:
        if not self.calls.exists():
            return []
        return [json.loads(line) for line in self.calls.read_text().splitlines()]


def last_line(done) -> str:
    return [ln for ln in done.stdout.splitlines() if ln.strip()][-1]


def row(done, label: str) -> str:
    rows = [ln for ln in done.stdout.splitlines() if ln.startswith(label + " · ")]
    assert len(rows) == 1, (label, done.stdout)
    return rows[0]


@pytest.fixture
def box(tmp_path):
    return Box(tmp_path)


def test_four_smoke_rows_and_two_markers_are_green_with_every_line(box):
    done = box.run()
    assert done.returncode == 0, done.stdout + done.stderr
    assert last_line(done) == "SMOKE GREEN"
    assert row(done, "file a").endswith(" · GREEN")
    assert row(done, "needle exact") == f'needle exact · grep -c -F "needle" {box.files}/b.txt · 2 · GREEN'
    assert row(done, "needle some").endswith(" · 2 · GREEN")
    assert row(done, "radar phone") == f"radar phone · {CURL_CMD} · 200 · GREEN"
    assert row(done, "marker 1").endswith(" · GREEN")
    assert row(done, "marker 2").endswith(" · 1 · GREEN")
    curls = [c["argv"] for c in box.calls_list() if c["name"] == "curl"]
    assert len(curls) == 3
    assert curls[0] == ["-s", "-o", "/dev/null", "-w", "%{http_code}", "http://127.0.0.1:5010/radar?frame=phone"]
    assert list((box.wt / ".deploy-logs").glob("x-set-smoke-*.log"))


def test_a_marker_whose_after_differs_is_smoke_red(box):
    (box.files / "c.txt").write_text("no such line\n")
    done = box.run()
    assert done.returncode == 1
    assert row(done, "marker 2").endswith(" · 0 · RED")
    assert last_line(done) == "SMOKE RED: marker 2"


def test_a_curl_that_never_answers_200_is_red_after_three_tries(box):
    done = box.run(CURL_OK_ON="9")
    assert done.returncode == 1
    assert row(done, "radar phone").endswith(" · RED")
    assert len([c for c in box.calls_list() if c["name"] == "curl"]) == 3
    assert last_line(done) == "SMOKE RED: radar phone"


def test_a_smoke_read_whose_value_differs_is_red(box):
    (box.files / "b.txt").write_text("needle\n")
    done = box.run()
    assert row(done, "needle exact").endswith(" · 1 · RED")
    assert row(done, "needle some").endswith(" · 1 · GREEN")
    assert last_line(done) == "SMOKE RED: needle exact"


def test_a_db_query_row_on_a_migrations_none_card_is_skipped_and_said(box):
    box.write(smoke_extra='- table · `COBALT_ENV=production uv run cobalt db query --side user --prod "SELECT count(*) FROM \\"user\\".t"` · exit 0, one integer\n')
    done = box.run()
    assert done.returncode == 0, done.stdout
    assert "MIGRATIONS is none" in row(done, "table")
    assert row(done, "table").endswith(" · SKIPPED")
    assert [c for c in box.calls_list() if c["name"] == "uv"] == []
    assert last_line(done) == "SMOKE GREEN"


def test_a_db_query_row_runs_on_a_migration_card_and_a_census_is_recorded(box):
    sql = 'SELECT count(*) FROM \\"user\\".t'
    box.write(
        migrations="0002 · production at 0001 · creates: t · old code on the new schema: fine",
        smoke_extra=(
            f'- table · `COBALT_ENV=production uv run cobalt db query --side user --prod "{sql}"` · exit 0, one integer\n'
            f'- census · `COBALT_ENV=production uv run cobalt db query --side user --prod "{sql}"` · exit 0, one integer before the outage and one after, recorded\n'
        ),
    )
    done = box.run()
    assert done.returncode == 0, done.stdout + done.stderr
    assert row(done, "table").endswith(" · 7 · GREEN")
    assert row(done, "census").endswith(" · 7 · census")
    uvs = [c for c in box.calls_list() if c["name"] == "uv"]
    assert len(uvs) == 2
    assert uvs[0]["argv"] == ["run", "cobalt", "db", "query", "--side", "user", "--prod", 'SELECT count(*) FROM "user".t']
    assert uvs[0]["env"] == "production"


def test_a_db_query_carrying_a_percent_is_skipped_and_said(box):
    box.write(
        migrations="0002 · production at 0001 · creates: t · old code on the new schema: fine",
        smoke_extra="- like · `COBALT_ENV=production uv run cobalt db query --side user --prod \"SELECT count(*) FROM t WHERE x LIKE 'a%'\"` · exit 0, one integer\n",
    )
    done = box.run()
    assert "%" in row(done, "like") and row(done, "like").endswith(" · SKIPPED")
    assert [c for c in box.calls_list() if c["name"] == "uv"] == []


@pytest.mark.parametrize(
    "command",
    [
        "cat /etc/hosts",
        'grep -c -F "x" /tmp/$(whoami)',
        "ls /tmp; rm -rf /tmp/x",
        "curl -s http://example.com/",
        "COBALT_ENV=production uv run cobalt db migrate --allow-prod",
    ],
)
def test_a_command_outside_the_mapped_shapes_is_red_and_never_run(box, command):
    box.write(smoke_extra=f"- odd · `{command}` · exit 0, listed\n")
    done = box.run()
    assert done.returncode == 1
    assert "not a mapped smoke command" in row(done, "odd")
    assert row(done, "odd").endswith(" · RED")
    assert all(c["name"] == "curl" for c in box.calls_list())


def test_an_expectation_it_cannot_map_is_red(box):
    box.write(smoke_extra=f"- vague · `ls {box.files}/a.txt` · looks fine\n")
    done = box.run()
    assert row(done, "vague").endswith(" · RED")
    assert last_line(done) == "SMOKE RED: vague"


def test_dry_run_calls_nothing_and_prints_every_would_run_line(box):
    stub(box.bin, "git", PLAIN)
    stub(box.bin, "launchctl", PLAIN)
    done = box.run("--dry-run")
    assert done.returncode == 0, done.stdout + done.stderr
    assert box.calls_list() == []
    would = [ln for ln in done.stdout.splitlines() if ln.startswith("WOULD RUN: ")]
    assert len(would) == 6
    assert f"WOULD RUN: {CURL_CMD}" in would
    assert last_line(done).startswith("DRY RUN — nothing run")
    assert not (box.wt / ".deploy-logs").exists()


def test_d4_dry_run_on_the_10_02_deploy_card(box):
    """RUN row D4: the --dry-run of the real 10-02 night deploy card (the worktree copy, read only)."""
    stub(box.bin, "git", PLAIN)
    stub(box.bin, "launchctl", PLAIN)
    done = subprocess.run(
        ["sh", str(SCRIPT), "--dry-run", str(REAL_CARD)], env=box.env, capture_output=True,
        text=True, errors="replace", timeout=120,
    )
    print(done.stdout + done.stderr)
    assert box.calls_list() == []
    assert done.returncode == 0
